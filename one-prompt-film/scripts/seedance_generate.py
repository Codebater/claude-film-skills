#!/usr/bin/env python3
"""Create a Seedance video generation task on BytePlus ModelArk, poll it, download the result.

Stdlib only. Needs ARK_API_KEY in the environment.

Examples:
  python seedance_generate.py --prompt-file prompt.txt --duration 20 --ratio 16:9 --out film.mp4
  python seedance_generate.py --prompt-file p.txt --asset reference_image=https://x/y.png \
      --asset first_frame=https://x/f.png --out film.mp4
  python seedance_generate.py --prompt-file edit.txt --task-type edit \
      --asset reference_video=https://x/in.mov --format mov --out edited.mov
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

API_BASE = "https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks"
DEFAULT_MODEL = "dreamina-seedance-2-5-260628"

ROLE_TO_TYPE = {
    "reference_image": ("image_url", "image_url"),
    "first_frame": ("image_url", "image_url"),
    "last_frame": ("image_url", "image_url"),
    "reference_video": ("video_url", "video_url"),
    "reference_audio": ("audio_url", "audio_url"),
}


def api(method, url, key, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}",
    })
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        sys.exit(f"API error {e.code} on {method} {url}:\n{detail}")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--prompt-file", required=True, help="UTF-8 text file with the full prompt")
    p.add_argument("--asset", action="append", default=[], metavar="ROLE=URL",
                   help="repeatable; ROLE is one of %s; order = upload order (@Image1...)"
                        % ", ".join(ROLE_TO_TYPE))
    p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument("--duration", type=int, default=-1, help="4..30 or -1 (model decides)")
    p.add_argument("--ratio", default="adaptive",
                   help="21:9|16:9|4:3|1:1|3:4|9:16|adaptive")
    p.add_argument("--resolution", default="720p", choices=["480p", "720p"])
    p.add_argument("--format", dest="fmt", default="mp4", choices=["mp4", "mov"])
    p.add_argument("--no-audio", action="store_true")
    p.add_argument("--watermark", action="store_true")
    p.add_argument("--task-type", choices=["auto", "edit", "extend"],
                   help="sets omni_reference_task_type; edit/extend also force locked params")
    p.add_argument("--out", required=True, help="output file path")
    p.add_argument("--poll-interval", type=int, default=20)
    p.add_argument("--timeout-min", type=int, default=40)
    args = p.parse_args()

    key = os.environ.get("ARK_API_KEY")
    if not key:
        sys.exit("ARK_API_KEY is not set. Get one at console.byteplus.com (ModelArk > API Key).")

    with open(args.prompt_file, encoding="utf-8") as f:
        prompt = f.read().strip()
    if not prompt:
        sys.exit("Prompt file is empty.")

    content = [{"type": "text", "text": prompt}]
    for a in args.asset:
        role, _, url = a.partition("=")
        if role not in ROLE_TO_TYPE or not url:
            sys.exit(f"Bad --asset '{a}'. Use ROLE=URL with ROLE in {list(ROLE_TO_TYPE)}")
        typ, field = ROLE_TO_TYPE[role]
        content.append({"type": typ, field: {"url": url}, "role": role})

    ratio, duration = args.ratio, args.duration
    if args.task_type == "edit":
        ratio, duration = "adaptive", -1  # hard requirement for editing tasks
    elif args.task_type == "extend" or any(x.startswith(("first_frame", "last_frame")) for x in args.asset):
        ratio = "adaptive"  # extension and first/last-frame lock the ratio

    body = {
        "model": args.model,
        "content": content,
        "generate_audio": not args.no_audio,
        "ratio": ratio,
        "duration": duration,
        "resolution": args.resolution,
        "output_format": args.fmt,
        "watermark": args.watermark,
    }
    if args.task_type:
        body["omni_reference_task_type"] = args.task_type

    print(f"Submitting task ({args.model}, {duration}s, {ratio}, {args.resolution}, {args.fmt})...")
    resp = api("POST", API_BASE, key, body)
    task_id = resp.get("id") or resp.get("task_id")
    if not task_id:
        sys.exit(f"No task id in response: {json.dumps(resp)[:2000]}")
    print(f"Task id: {task_id}")

    deadline = time.time() + args.timeout_min * 60
    status, task = "queued", {}
    while time.time() < deadline:
        task = api("GET", f"{API_BASE}/{task_id}", key)
        status = task.get("status", "unknown")
        if status in ("succeeded", "failed", "cancelled"):
            break
        print(f"  {time.strftime('%H:%M:%S')} status={status}")
        time.sleep(args.poll_interval)

    if status != "succeeded":
        sys.exit(f"Task ended with status '{status}':\n{json.dumps(task, indent=2)[:3000]}")

    video_url = (task.get("content") or {}).get("video_url") or task.get("video_url")
    if not video_url:
        sys.exit(f"Succeeded but no video_url found:\n{json.dumps(task, indent=2)[:3000]}")

    print("Downloading (URL expires in 24h)...")
    urllib.request.urlretrieve(video_url, args.out)
    size_mb = os.path.getsize(args.out) / 1e6
    print(f"Saved {args.out} ({size_mb:.1f} MB)")
    usage = task.get("usage")
    if usage:
        print(f"Usage: {json.dumps(usage)}")


if __name__ == "__main__":
    main()
