#!/usr/bin/env python3
"""Execute an audio manifest: position/trim/fade stems, bus them, duck music under
dialogue, limit, normalize, and mux the mix back into the video. Needs ffmpeg on PATH.

  python mix_audio.py --video film.mp4 --manifest manifest.json --out film_mixed.mp4

Manifest schema (times in seconds, gains in dB):
{
  "native": {"mode": "layer", "gain_db": -8},        // keep | layer | replace  (default: replace)
  "assets": [
    {"file": "vo.mp3", "type": "dialogue",           // dialogue|voiceover|ambience|foley|
     "start": 1.35, "gain_db": -2,                    //   sfx|transition|branding|music
     "fade_in": 0.02, "fade_out": 0.15,               // optional
     "trim_start": 0.0, "trim_end": 4.2,              // optional, source-relative
     "pan": -0.3}                                     // optional, -1 L .. +1 R
  ],
  "music_duck": {"enabled": true, "threshold": 0.03, "ratio": 8,
                 "attack_ms": 20, "release_ms": 400},  // optional (defaults shown)
  "loudnorm": {"i": -16, "tp": -1.5, "lra": 11}        // optional (defaults shown)
}

Buses: DIALOGUE (dialogue+voiceover), MUSIC (music), FX (everything else + native bed).
Ducking uses the dialogue bus as sidechain over the music bus. Video stream is copied.
The mix is padded/cut to exactly the video's length. Prints a loudness report at the end.
"""
import argparse
import json
import shutil
import subprocess
import sys

DIALOGUE = ("dialogue", "voiceover", "vo")
MUSIC = ("music",)


def ffprobe_duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        sys.exit(f"Could not probe {path}")


def has_audio(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a",
                        "-show_entries", "stream=index", "-of", "csv=p=0", path],
                       capture_output=True, text=True)
    return bool(r.stdout.strip())


def chain(asset, label_in, label_out):
    """Per-asset filter chain: trim -> gain -> fades -> pan -> resample -> delay."""
    f = [f"[{label_in}]aresample=48000,aformat=channel_layouts=stereo"]
    ts, te = asset.get("trim_start"), asset.get("trim_end")
    if ts or te:
        args = []
        if ts:
            args.append(f"start={ts}")
        if te:
            args.append(f"end={te}")
        f.append("atrim=" + ":".join(args) + ",asetpts=PTS-STARTPTS")
    gain = asset.get("gain_db", 0)
    if gain:
        f.append(f"volume={gain}dB")
    if asset.get("fade_in"):
        f.append(f"afade=t=in:st=0:d={asset['fade_in']}")
    if asset.get("fade_out"):
        # fade relative to the trimmed segment, not the full source file
        eff = (te if te is not None else asset.get("_dur", 0)) - (ts or 0)
        if eff > 0:
            f.append(f"afade=t=out:st={max(0, eff - asset['fade_out'])}:d={asset['fade_out']}")
    if asset.get("pan"):
        p = max(-1.0, min(1.0, asset["pan"]))
        l, r = min(1.0, 1.0 - p), min(1.0, 1.0 + p)
        f.append(f"pan=stereo|c0={l:.3f}*c0|c1={r:.3f}*c1")
    delay = int(round(asset.get("start", 0) * 1000))
    f.append(f"adelay={delay}|{delay}")
    return ",".join(f) + f"[{label_out}]"


def mix_bus(labels, out_label, parts):
    if len(labels) == 1:
        parts.append(f"[{labels[0]}]anull[{out_label}]")
    else:
        parts.append("".join(f"[{l}]" for l in labels) +
                      f"amix=inputs={len(labels)}:duration=longest:normalize=0[{out_label}]")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--video", required=True)
    p.add_argument("--manifest", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        sys.exit("ffmpeg/ffprobe not found on PATH. Install ffmpeg (e.g. winget install Gyan.FFmpeg) and retry.")

    with open(args.manifest, encoding="utf-8") as f:
        m = json.load(f)
    assets = m.get("assets", [])
    if not assets and m.get("native", {}).get("mode", "replace") == "replace":
        sys.exit("Manifest has no assets and native mode is 'replace' — nothing to mix.")

    vdur = ffprobe_duration(args.video)
    native = m.get("native", {"mode": "replace"})
    native_mode = native.get("mode", "replace")
    use_native = native_mode in ("keep", "layer") and has_audio(args.video)

    cmd = ["ffmpeg", "-y", "-i", args.video]
    for a in assets:
        cmd += ["-i", a["file"]]
        a["_dur"] = ffprobe_duration(a["file"])

    parts, dial, music, fx = [], [], [], []
    if use_native:
        g = native.get("gain_db", -6 if native_mode == "layer" else 0)
        parts.append(f"[0:a]aresample=48000,aformat=channel_layouts=stereo,volume={g}dB[nat]")
        fx.append("nat")
    for i, a in enumerate(assets):
        lab = f"a{i}"
        parts.append(chain(a, f"{i+1}:a", lab))
        t = a.get("type", "sfx").lower()
        (dial if t in DIALOGUE else music if t in MUSIC else fx).append(lab)

    buses = []
    if dial:
        mix_bus(dial, "DIAL", parts)
    if music:
        mix_bus(music, "MUS", parts)
    if fx:
        mix_bus(fx, "FX", parts)

    duck = {**{"enabled": True, "threshold": 0.03, "ratio": 8, "attack_ms": 20,
               "release_ms": 400}, **m.get("music_duck", {})}
    if dial and music and duck["enabled"]:
        parts.append("[DIAL]asplit=2[DIALm][DIALsc]")
        parts.append(f"[MUS][DIALsc]sidechaincompress=threshold={duck['threshold']}:"
                     f"ratio={duck['ratio']}:attack={duck['attack_ms']}:"
                     f"release={duck['release_ms']}[MUSd]")
        buses = ["DIALm", "MUSd"] + (["FX"] if fx else [])
    else:
        buses = ([l for l, present in (("DIAL", dial), ("MUS", music), ("FX", fx)) if present])

    ln = {**{"i": -16, "tp": -1.5, "lra": 11}, **m.get("loudnorm", {})}
    head = "".join(f"[{b}]" for b in buses)
    mixer = (f"amix=inputs={len(buses)}:duration=longest:normalize=0"
             if len(buses) > 1 else "anull")
    parts.append(f"{head}{mixer},alimiter=limit=0.891,"
                 f"loudnorm=I={ln['i']}:TP={ln['tp']}:LRA={ln['lra']},"
                 f"aresample=48000,apad,atrim=end={vdur}[MIX]")

    fc = ";".join(parts)
    cmd += ["-filter_complex", fc, "-map", "0:v", "-map", "[MIX]",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", args.out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("ffmpeg failed:\n" + r.stderr[-3000:])

    rep = subprocess.run(["ffmpeg", "-i", args.out, "-af",
                          "loudnorm=print_format=summary", "-f", "null", "-"],
                         capture_output=True, text=True)
    tail = "\n".join(l for l in rep.stderr.splitlines()
                     if any(k in l for k in ("Input Integrated", "Input True Peak", "Input LRA")))
    print(f"Mixed {len(assets)} stems (+native: {use_native}) -> {args.out}")
    print(tail or "(loudness report unavailable)")


if __name__ == "__main__":
    main()
