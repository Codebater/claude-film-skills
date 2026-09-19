# Recording reference — record.mjs

## How it works (mental model)

`record.mjs` is NOT a screen recorder. It:

1. Probes `cfg.url`; if down, spawns `npm run dev` in the config's directory (killed after, unless `--keep-server`).
2. Launches headless Chromium and injects a **virtual clock** via `addInitScript` — before any page JS runs, it replaces `performance.now`, `Date.now`, `requestAnimationFrame`, `setTimeout`/`setInterval`. The page's time is frozen at 0 until stepping begins.
3. Waits for `networkidle` + `window.__SCENE_READY === true` (the template sets this after fonts load).
4. Per output frame: runs due beat actions (real mouse/keyboard events) → advances the clock exactly `1000/fps` ms (fires due timers chronologically, flushes rAF callbacks, seeks WAAPI/CSS animations) → screenshots.
5. Assembles with ffmpeg: `-framerate fps`, libx264 CRF 18, `yuv420p`, `+faststart`, lanczos downscale from the 2× capture to exact `viewport` size.

Consequences worth internalizing:

- Motion/framer-motion is fully deterministic — it reads time from `performance.now`/rAF timestamps, both virtualized. A 60-frame capture is identical on a loaded or idle machine.
- Springs, staggers, `setInterval`-driven typing effects: all follow the virtual clock.
- **Not** virtualized: `<video>` playback, Web Workers, WebSocket-driven updates, CSS `steps()` driven by real media time. Avoid these in scenes.
- Capture speed is ~5–15 fps of wall time (screenshot-bound). A 10 s / 30 fps video ≈ 30–60 s capture.

## Config schema (`scene.video.json`)

```jsonc
{
  "name": "liquid-cta",           // output file stem
  "url": "http://localhost:3998", // dev server (auto-started if down)
  "fps": 30,                      // 60 for micro-interaction close-ups
  "seconds": 8,
  "viewport": { "width": 1280, "height": 720 },  // final video size
  "deviceScaleFactor": 2,         // capture at 2x, downscale = crisp text. Keep 2.
  "colorScheme": "dark",          // matches the stage's default dark theme
  "outDir": "out",                // relative to this config file
  "formats": ["webm"],            // optional extra outputs besides mp4
  "cursor": true,                 // cursor dot; defaults to true when beats exist
  "beats": [ /* see below */ ]
}
```

Aspect presets: 16:9 → 1280×720 · 9:16 → 1080×1920 · 1:1 → 1080×1080. (At 1080+ widths capture is slower; fine.)

## Beats

Each beat: `{ "at": seconds, "action": ..., ...params }`. Actions fire **real** input events — the scene must be wired so they genuinely cause the effect (real buttons, real handlers).

| action | params | behavior |
| --- | --- | --- |
| `move` / `hover` | `selector` or `to:[x,y]`, `over` (default 0.6), `ease` | Cursor flies on an eased, slightly arced path, interpolated per frame. First flight starts from bottom-center offscreen. |
| `click` | same as move | Flight, then mousedown (+0.08 s) and mouseup (+0.12 s later) — the press is visible; cursor dot shrinks while down. |
| `dblclick` | same | Two spaced press cycles. |
| `type` | `selector` (focused first), `text`, `over` | Keystrokes spread evenly across `over` seconds. |
| `press` | `key` (e.g. `"Enter"`) | Single key press. |
| `scroll` | `by` px, `over`, `ease` | Eased wheel deltas across frames. |
| `eval` | `js` string | Escape hatch: run JS in the page at that moment (e.g. `window.__fire()` to trigger scene state you exposed). |

Timing note: a `click` beat's *press* lands at roughly `at + over + 0.08` — plan the scene's reaction from there. Leave ≥ 0.5 s after the last beat's effect settles before the video ends.

## Scene contract (what the template provides)

- `window.__SCENE_READY = true` is set in `main.tsx` after `document.fonts.ready` — the recorder waits for it, so entrance animations (which start on first rAF) begin exactly at frame 0.
- Stage is `#stage`, full-viewport, `dark` class applied, overflow hidden.
- Dev server port **3998** (`vite.config.ts`).

## Gotchas (learned the hard way — video-pipeline lineage)

- **Windows Chromium freezes rAF for occluded windows** — the launch flags `--disable-features=CalculateNativeWinOcclusion` + backgrounding/throttling flags are load-bearing. Don't remove them.
- **ffmpeg paths on Windows filtergraphs**: record.mjs avoids filtergraph file paths entirely (argv arrays, `scale=` only). If you extend it with `drawtext`, use `textfile=` and escape `\` → `/`, `:` → `\:`.
- **Killing the dev server on Windows** needs `taskkill /T /F` on the npm shell pid — plain `.kill()` orphans vite. record.mjs handles this.
- **Even dimensions**: yuv420p requires even width/height — the explicit `scale=vw:vh` guarantees it; keep viewport dims even.
- **Randomness**: virtual time makes runs deterministic, but `Math.random()` isn't patched. Scenes must seed/hardcode anything positional.
- **First-frame flash**: if the video's first frame shows the fully-assembled UI for a split second, something rendered before the clock started (e.g. `initial={false}`, or CSS without a delay). Give every entrance an explicit `initial` state and a `T`-derived delay.
- **Looping videos**: to make a seamless loop, design the scene so state at `seconds` equals state at 0, then optionally crossfade head over tail in ffmpeg (`video-pipeline/lib/loop.mjs` has the recipe: shift head over tail with alpha fade, start the fade one frame early to avoid a ghost frame).
- **Verifying**: `ffprobe -v error -show_entries format=duration -of csv=p=0 out/<name>.mp4` should equal `seconds` ± one frame. Read 3–4 PNGs from `out/frames/` at key beats to confirm choreography before sending.

## Relation to video-pipeline/

`Webseiten/video-pipeline/` is the sibling system for **website** films (scroll-driven capture, story takes with recordVideo, reels, music, intro/outro cards). This skill's recorder is for **component scenes** with time-driven motion.

When a request outgrows a single recorded scene — music, title cards, transitions between scenes, captions, logo outros — prefer assembling the recorded mp4s in a **HyperFrames composition** (see hyperframes.md): declarative timeline, shader transitions, audio tracks, deterministic render. Fall back to `video-pipeline/lib/assemble.mjs` ffmpeg patterns only when HyperFrames isn't available.
