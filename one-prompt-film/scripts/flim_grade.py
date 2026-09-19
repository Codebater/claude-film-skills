#!/usr/bin/env python3
"""Apply the flim filmic color transform (github.com/bean-mhm/flim) to a video as a finishing grade.

flim's official LUTs (.spi3d) expect scene-linear input passed through a log2 allocation
mapping [-10, +10] stops to [0, 1]. Video from Seedance is display sRGB, so this script bakes
the whole chain (sRGB decode -> log2 allocation -> flim LUT) into one standard .cube LUT and
applies it with ffmpeg's lut3d filter. Audio is copied untouched.

Needs: ffmpeg on PATH. numpy is used if available (faster), pure-python fallback otherwise.

Examples:
  python flim_grade.py film.mp4 --preset default --out film_graded.mp4
  python flim_grade.py film.mp4 --preset nostalgia --strength 0.7 --out film_graded.mp4
"""
import argparse
import math
import os
import subprocess
import sys
import urllib.request

FLIM_VERSION = "v1.2.0"
PRESETS = ("default", "nostalgia", "silver")
LUT_URL = "https://github.com/bean-mhm/flim/releases/download/{v}/flim_{p}.spi3d"
CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache", "flim-luts")
CUBE_SIZE = 49  # baked output grid; trilinear in ffmpeg smooths the rest


def fetch_spi3d(preset):
    os.makedirs(CACHE_DIR, exist_ok=True)
    path = os.path.join(CACHE_DIR, f"flim_{preset}_{FLIM_VERSION}.spi3d")
    if not os.path.exists(path):
        url = LUT_URL.format(v=FLIM_VERSION, p=preset)
        print(f"Downloading {url} ...")
        urllib.request.urlretrieve(url, path)
    return path


def parse_spi3d(path):
    """Return (size, table) where table[i][j][k] = (r,g,b), indices in file order."""
    with open(path) as f:
        header = f.readline().strip()
        if not header.upper().startswith("SPILUT"):
            sys.exit(f"Not an spi3d file: {path}")
        f.readline()  # "3 3"
        dims = f.readline().split()
        nx, ny, nz = int(dims[0]), int(dims[1]), int(dims[2])
        table = [[[None] * nz for _ in range(ny)] for _ in range(nx)]
        for line in f:
            parts = line.split()
            if len(parts) != 6 or parts[0].startswith("#"):
                continue
            i, j, k = int(parts[0]), int(parts[1]), int(parts[2])
            table[i][j][k] = (float(parts[3]), float(parts[4]), float(parts[5]))
    if nx != ny or ny != nz:
        sys.exit("Non-cubic spi3d not supported")
    return nx, table


def srgb_to_linear(v):
    return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4


def alloc_log2(lin):
    """OCIO lg2 allocation vars [-10, 10] -> [0, 1]."""
    lin = max(lin, 2.0 ** -10)
    return min(max((math.log2(lin) + 10.0) / 20.0, 0.0), 1.0)


def trilinear(table, n, x, y, z):
    def prep(t):
        t = min(max(t, 0.0), 1.0) * (n - 1)
        i0 = min(int(t), n - 2)
        return i0, t - i0
    xi, xf = prep(x)
    yi, yf = prep(y)
    zi, zf = prep(z)
    out = [0.0, 0.0, 0.0]
    for dx, wx in ((0, 1 - xf), (1, xf)):
        for dy, wy in ((0, 1 - yf), (1, yf)):
            for dz, wz in ((0, 1 - zf), (1, zf)):
                w = wx * wy * wz
                c = table[xi + dx][yi + dy][zi + dz]
                out[0] += w * c[0]
                out[1] += w * c[1]
                out[2] += w * c[2]
    return out


def bake_cube(spi3d_path, cube_path):
    n, table = parse_spi3d(spi3d_path)
    steps = [i / (CUBE_SIZE - 1) for i in range(CUBE_SIZE)]
    enc = [alloc_log2(srgb_to_linear(v)) for v in steps]  # per-channel encode is separable
    with open(cube_path, "w") as f:
        f.write(f"# flim {FLIM_VERSION} baked for display-sRGB input\n")
        f.write(f"LUT_3D_SIZE {CUBE_SIZE}\n")
        # .cube ordering: red fastest
        for b in range(CUBE_SIZE):
            for g in range(CUBE_SIZE):
                for r in range(CUBE_SIZE):
                    rgb = trilinear(table, n, enc[r], enc[g], enc[b])
                    f.write("%.6f %.6f %.6f\n" % (
                        min(max(rgb[0], 0.0), 1.0),
                        min(max(rgb[1], 0.0), 1.0),
                        min(max(rgb[2], 0.0), 1.0)))
    return cube_path


def ffmpeg_path_escape(path):
    # ffmpeg filter args: forward slashes, escape the drive colon
    return path.replace("\\", "/").replace(":", "\\:")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input")
    p.add_argument("--preset", default="default", choices=PRESETS)
    p.add_argument("--strength", type=float, default=1.0,
                   help="0..1 blend of graded over original (default 1.0)")
    p.add_argument("--out", required=True)
    args = p.parse_args()

    if not (0.0 < args.strength <= 1.0):
        sys.exit("--strength must be in (0, 1]")

    spi3d = fetch_spi3d(args.preset)
    cube = os.path.join(CACHE_DIR, f"flim_{args.preset}_{FLIM_VERSION}_srgb_{CUBE_SIZE}.cube")
    if not os.path.exists(cube):
        print("Baking sRGB-input .cube LUT (one-time per preset)...")
        try:
            import numpy as np  # fast path
            n, table = parse_spi3d(spi3d)
            t = np.array([[[table[i][j][k] for k in range(n)] for j in range(n)] for i in range(n)])
            steps = np.linspace(0.0, 1.0, CUBE_SIZE)
            lin = np.where(steps <= 0.04045, steps / 12.92, ((steps + 0.055) / 1.055) ** 2.4)
            enc = np.clip((np.log2(np.maximum(lin, 2.0 ** -10)) + 10.0) / 20.0, 0.0, 1.0)
            coords = enc * (n - 1)
            i0 = np.minimum(coords.astype(int), n - 2)
            fr = coords - i0
            with open(cube, "w") as f:
                f.write(f"# flim {FLIM_VERSION} baked for display-sRGB input\n")
                f.write(f"LUT_3D_SIZE {CUBE_SIZE}\n")
                for b in range(CUBE_SIZE):
                    bi, bf = i0[b], fr[b]
                    for g in range(CUBE_SIZE):
                        gi, gf = i0[g], fr[g]
                        row = []
                        for r in range(CUBE_SIZE):
                            ri, rf = i0[r], fr[r]
                            c = (t[ri:ri + 2, gi:gi + 2, bi:bi + 2]
                                 * np.array([1 - rf, rf])[:, None, None, None]
                                 * np.array([1 - gf, gf])[None, :, None, None]
                                 * np.array([1 - bf, bf])[None, None, :, None]).sum(axis=(0, 1, 2))
                            row.append("%.6f %.6f %.6f" % tuple(np.clip(c, 0.0, 1.0)))
                        f.write("\n".join(row) + "\n")
        except ImportError:
            bake_cube(spi3d, cube)

    lut_arg = ffmpeg_path_escape(cube)
    if args.strength >= 1.0:
        vf = f"lut3d='{lut_arg}'"
        cmd = ["ffmpeg", "-y", "-i", args.input, "-vf", vf,
               "-c:a", "copy", args.out]
    else:
        fc = (f"[0:v]split[a][b];[b]lut3d='{lut_arg}'[g];"
              f"[a][g]blend=all_mode=normal:all_opacity={args.strength}[v]")
        cmd = ["ffmpeg", "-y", "-i", args.input, "-filter_complex", fc,
               "-map", "[v]", "-map", "0:a?", "-c:a", "copy", args.out]

    print("Running:", " ".join(cmd))
    r = subprocess.run(cmd)
    if r.returncode != 0:
        sys.exit("ffmpeg failed")
    print(f"Graded video saved to {args.out} (preset={args.preset}, strength={args.strength})")


if __name__ == "__main__":
    main()
