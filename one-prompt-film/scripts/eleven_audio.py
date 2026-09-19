#!/usr/bin/env python3
"""Generate one audio stem via the ElevenLabs API (dialogue/VO, SFX/foley/ambience, or music).

Stdlib only. Reads ELEVENLABS_API_KEY from the environment (falls back to the Windows
user-registry value if the current process started before the variable was set).
The key is never printed or written anywhere.

Examples:
  python eleven_audio.py list-voices
  python eleven_audio.py dialogue --text "Call the number." --voice "Brian" \
      --performance "quiet, restrained authority" --out vo.mp3
  python eleven_audio.py sfx --prompt "single premium smartphone notification, short crystalline digital tone, extremely clean transient, no reverb" --duration 1.2 --out ding.mp3
  python eleven_audio.py music --prompt "minimal cinematic tension for a luxury tech commercial, sparse piano and low strings, 92 BPM, builds gradually, clean ending" --duration 18 --out score.mp3
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

API = "https://api.elevenlabs.io/v1"


def get_key():
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key and sys.platform == "win32":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
                key = winreg.QueryValueEx(k, "ELEVENLABS_API_KEY")[0]
        except OSError:
            pass
    if not key:
        sys.exit("ELEVENLABS_API_KEY is not set.")
    return key


def call(path, key, body=None, method=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(API + path, data=data,
                                 method=method or ("POST" if data else "GET"),
                                 headers={"xi-api-key": key,
                                          "Content-Type": "application/json"})
    try:
        return urllib.request.urlopen(req, timeout=300).read()
    except urllib.error.HTTPError as e:
        sys.exit(f"ElevenLabs API error {e.code} on {path}:\n{e.read().decode(errors='replace')[:1500]}")


def resolve_voice(key, voice):
    """Accept a voice_id directly or resolve a voice by (partial) name."""
    if len(voice) >= 20 and " " not in voice:
        return voice
    voices = json.loads(call("/voices", key))["voices"]
    for v in voices:
        if v["name"].lower() == voice.lower():
            return v["voice_id"]
    for v in voices:
        if voice.lower() in v["name"].lower():
            return v["voice_id"]
    names = ", ".join(v["name"] for v in voices[:30])
    sys.exit(f"Voice '{voice}' not found. Available: {names}")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("type", choices=["dialogue", "vo", "sfx", "ambience", "foley", "music", "list-voices"])
    p.add_argument("--text", help="spoken text (dialogue/vo)")
    p.add_argument("--prompt", help="acoustic description (sfx/ambience/foley/music)")
    p.add_argument("--voice", default="Brian", help="voice name or voice_id (dialogue/vo)")
    p.add_argument("--performance", default="", help="delivery note; v3 renders it as an audio tag prefix")
    p.add_argument("--model", default=None, help="override model_id (e.g. eleven_v3, eleven_multilingual_v2)")
    p.add_argument("--stability", type=float, default=0.45)
    p.add_argument("--style", type=float, default=0.35)
    p.add_argument("--speed", type=float, default=1.0)
    p.add_argument("--duration", type=float, help="seconds: sfx 0.5-30; music 3-600")
    p.add_argument("--prompt-influence", type=float, default=0.5, help="sfx only, 0-1")
    p.add_argument("--loop", action="store_true", help="sfx only: seamless loop (for ambience beds)")
    p.add_argument("--out", help="output audio file (.mp3)")
    args = p.parse_args()

    key = get_key()

    if args.type == "list-voices":
        voices = json.loads(call("/voices", key))["voices"]
        for v in voices:
            labels = ", ".join(f"{k}={val}" for k, val in (v.get("labels") or {}).items())
            print(f"{v['voice_id']}  {v['name']}  [{labels}]")
        return

    if not args.out:
        sys.exit("--out is required")

    if args.type in ("dialogue", "vo"):
        if not args.text:
            sys.exit("--text is required for dialogue/vo")
        voice_id = resolve_voice(key, args.voice)
        text = args.text
        model = args.model or "eleven_multilingual_v2"
        if args.performance and model.startswith("eleven_v3"):
            text = f"[{args.performance}] {text}"
        body = {"text": text, "model_id": model,
                "voice_settings": {"stability": args.stability, "similarity_boost": 0.8,
                                   "style": args.style, "speed": args.speed,
                                   "use_speaker_boost": True}}
        audio = call(f"/text-to-speech/{voice_id}", key, body)

    elif args.type in ("sfx", "ambience", "foley"):
        if not args.prompt:
            sys.exit("--prompt is required for sfx/ambience/foley")
        body = {"text": args.prompt, "prompt_influence": args.prompt_influence}
        if args.duration:
            body["duration_seconds"] = max(0.5, min(30.0, args.duration))
        if args.loop:
            body["loop"] = True
        audio = call("/sound-generation", key, body)

    else:  # music
        if not args.prompt:
            sys.exit("--prompt is required for music")
        body = {"prompt": args.prompt}
        if args.duration:
            body["music_length_ms"] = int(max(3.0, min(600.0, args.duration)) * 1000)
        audio = call("/music", key, body)

    with open(args.out, "wb") as f:
        f.write(audio)
    print(f"Saved {args.out} ({len(audio)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
