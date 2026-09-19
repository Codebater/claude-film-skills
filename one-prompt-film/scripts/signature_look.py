#!/usr/bin/env python3
"""Bake a signature look on top of a flim base LUT, as one portable .cube.

flim_grade.py gives you flim's three presets and nothing else. This adds a look layer —
contrast, saturation, split-tone, channel gain — composed onto flim's output and baked
into a single .cube, so a signature grade is one LUT file, one ffmpeg pass, reusable
across every film without re-deriving the numbers.

Chain: display sRGB in -> flim (from flim_grade.py's baked cube) -> look ops -> sRGB out.

  python signature_look.py --look graphite --out graphite.cube
  python signature_look.py --list
  python signature_look.py --look ember --apply film.mp4 --out-video film_ember.mp4

Halation is spatial and cannot live in a LUT; --halation adds it as an ffmpeg pass
(bloom on the highlights, tinted red-orange, the way film's anti-halation layer fails).
"""
import argparse
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flim_grade import CACHE_DIR, CUBE_SIZE, FLIM_VERSION, fetch_spi3d, ffmpeg_path_escape  # noqa: E402

LUMA = (0.2126, 0.7152, 0.0722)

# Each look: base flim preset + look ops. Keep values small — a signature is a
# fingerprint, not a filter. contrast/sat are multipliers around 1.0; tints are
# per-channel offsets applied with a luma-weighted mask.
LOOKS = {
    "clean": dict(
        base="default", contrast=1.00, sat=1.00,
        shadow_tint=(0.000, 0.000, 0.000), high_tint=(0.000, 0.000, 0.000),
        desc="flim default, no look layer — the control",
    ),
    "graphite": dict(
        base="default", contrast=1.06, sat=0.94,
        shadow_tint=(-0.012, -0.004, 0.018), high_tint=(0.010, 0.004, -0.008),
        desc="cool graphite shadows, warm-neutral highlights, slightly desaturated — editorial/minimal",
    ),
    "ember": dict(
        base="default", contrast=1.08, sat=1.04,
        shadow_tint=(0.004, -0.002, -0.010), high_tint=(0.022, 0.008, -0.014),
        desc="warm amber highlights over neutral shadows — firelight, bronze, lightning",
    ),
    "violet": dict(
        base="default", contrast=1.05, sat=0.97,
        shadow_tint=(0.008, -0.008, 0.026), high_tint=(0.014, 0.006, -0.004),
        desc="violet shadows against warm cream highlights — the most distinctive of the set",
    ),
    "bleach": dict(
        base="silver", contrast=1.14, sat=0.82,
        shadow_tint=(-0.006, -0.002, 0.010), high_tint=(0.006, 0.004, 0.000),
        desc="silver-halide base, pushed contrast, pulled saturation — harsh, monochrome-leaning",
    ),
}


def base_cube(preset):
    """Path to flim_grade.py's baked sRGB-input cube, building it if absent."""
    cube = os.path.join(CACHE_DIR, f"flim_{preset}_{FLIM_VERSION}_srgb_{CUBE_SIZE}.cube")
    if not os.path.exists(cube):
        from flim_grade import bake_cube
        bake_cube(fetch_spi3d(preset), cube)
    return cube


def read_cube(path):
    vals = []
    size = None
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.upper().startswith("LUT_3D_SIZE"):
                size = int(line.split()[-1])
                continue
            if line.upper().startswith(("TITLE", "DOMAIN_")):
                continue
            parts = line.split()
            if len(parts) == 3:
                vals.append(tuple(float(p) for p in parts))
    if size is None or len(vals) != size ** 3:
        sys.exit(f"Malformed cube: {path} (size={size}, entries={len(vals)})")
    return size, vals


def apply_look(rgb, look):
    r, g, b = rgb
    # contrast around an 18%-grey pivot in display space
    pivot = 0.435
    c = look["contrast"]
    r, g, b = [(v - pivot) * c + pivot for v in (r, g, b)]
    # saturation toward luma
    y = LUMA[0] * r + LUMA[1] * g + LUMA[2] * b
    s = look["sat"]
    r, g, b = [y + (v - y) * s for v in (r, g, b)]
    # split-tone: weights fall off quadratically so mids stay clean
    y = max(0.0, min(1.0, LUMA[0] * r + LUMA[1] * g + LUMA[2] * b))
    w_lo = (1.0 - y) ** 2
    w_hi = y ** 2
    st, ht = look["shadow_tint"], look["high_tint"]
    out = [r + st[0] * w_lo + ht[0] * w_hi,
           g + st[1] * w_lo + ht[1] * w_hi,
           b + st[2] * w_lo + ht[2] * w_hi]
    return [max(0.0, min(1.0, v)) for v in out]


def bake(look_name, out_path):
    look = LOOKS[look_name]
    size, vals = read_cube(base_cube(look["base"]))
    with open(out_path, "w") as f:
        f.write(f"# signature look '{look_name}' — {look['desc']}\n")
        f.write(f"# base: flim {look['base']} {FLIM_VERSION}, display-sRGB input\n")
        f.write(f"TITLE \"{look_name}\"\n")
        f.write(f"LUT_3D_SIZE {size}\n")
        for v in vals:
            f.write("%.6f %.6f %.6f\n" % tuple(apply_look(v, look)))
    return out_path


def apply_video(cube, src, dst, halation=0.0):
    lut = ffmpeg_path_escape(os.path.abspath(cube))
    if halation <= 0:
        vf = f"lut3d='{lut}'"
        cmd = ["ffmpeg", "-y", "-v", "error", "-i", src, "-vf", vf, "-c:a", "copy", dst]
    else:
        # isolate highlights, blur them, tint red-orange, screen back over the graded image
        fc = (
            f"[0:v]lut3d='{lut}'[g];"
            f"[g]split[base][hl];"
            f"[hl]lut=r='max(0,val-170)*3':g='max(0,val-190)*2':b='max(0,val-215)*1',"
            f"gblur=sigma=14[bloom];"
            f"[base][bloom]blend=all_mode=screen:all_opacity={halation}[v]"
        )
        cmd = ["ffmpeg", "-y", "-v", "error", "-i", src, "-filter_complex", fc,
               "-map", "[v]", "-map", "0:a?", "-c:a", "copy", dst]
    r = subprocess.run(cmd)
    if r.returncode != 0:
        sys.exit("ffmpeg failed")
    return dst


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--look", choices=sorted(LOOKS))
    p.add_argument("--list", action="store_true", help="list looks and exit")
    p.add_argument("--out", help="output .cube path")
    p.add_argument("--apply", metavar="VIDEO", help="also apply the look to this video")
    p.add_argument("--out-video")
    p.add_argument("--halation", type=float, default=0.0,
                   help="0..1 highlight bloom on top of the LUT (0 = off)")
    a = p.parse_args()

    if a.list:
        for k in sorted(LOOKS):
            print(f"{k:10s} base={LOOKS[k]['base']:8s} {LOOKS[k]['desc']}")
        return
    if not a.look or not a.out:
        p.error("--look and --out are required (or use --list)")

    bake(a.look, a.out)
    print(f"Baked {a.out} (look={a.look}, base=flim {LOOKS[a.look]['base']})")
    if a.apply:
        dst = a.out_video or os.path.splitext(a.apply)[0] + f"_{a.look}.mp4"
        apply_video(a.out, a.apply, dst, a.halation)
        print(f"Graded video saved to {dst}"
              + (f" (halation {a.halation})" if a.halation else ""))


if __name__ == "__main__":
    main()
