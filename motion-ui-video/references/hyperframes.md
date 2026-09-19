# HyperFrames — the composition & finishing pipeline

HyperFrames (github.com/dftcodedev/dft-hyperframes, by HeyGen, Apache 2.0, Node 22+) turns plain HTML/CSS/JS into deterministic mp4 — same architecture as our recorder (frame-seeking in headless Chrome + ffmpeg), but built as a full production framework: timeline compositions, a 400+ block catalog, shader transitions, audio, cloud rendering. Local rendering is free.

## When to route where

| The shot needs… | Use |
| --- | --- |
| A **live app UI driven by real input** — cursor clicks real buttons, typing flips React state, animate-ui components react (the interaction-first golden rule) | **This skill's `record.mjs`** — HyperFrames has `simulated-cursor` / `typed-prompt` blocks, but they're choreographed fakes, not real events against a real app |
| **Motion graphics**: title sequences, kinetic type, animated charts/maps, lower thirds, logo stings, liquid-glass VFX | **HyperFrames** — the catalog already has it; don't rebuild in React |
| **Multi-scene videos**: several clips joined with real transitions, captions, music, an endcard | **HyperFrames composition** embedding the clips as media |
| The full promo: recorded UI scenes + titles + transitions + music | **Hybrid** (below) — this is the usual best answer for anything >15s |

## The hybrid workflow

1. Record UI scenes with `record.mjs` as usual → `out/<name>.mp4` per scene.
2. `npx hyperframes init <video-project>` → an editable HTML project.
3. Place scene mp4s as media elements on the timeline; add catalog blocks around them (titlecard → scene 1 → shader transition → scene 2 → logo outro, captions/lower thirds as overlay tracks, music track).
4. `npx hyperframes preview` (live-reload browser preview) → `npx hyperframes render --output final.mp4`.

This replaces hand-rolled ffmpeg xfade/concat work (video-pipeline's assemble stage) with a declarative timeline.

## Timing model (core of authoring)

Elements become timeline clips via data attributes; give timed DOM/image elements `class="clip"`:

- `data-start` — seconds, or a clip-id reference with arithmetic: `data-start="intro + 0.5"` (starts 0.5s after clip `intro` ends), `"intro - 0.5"` (overlap for crossfades). Same-composition refs only, no circular chains.
- `data-duration` — seconds the slot lasts.
- `data-track-index` — timeline lane. Tracks prevent time collisions only; visual stacking is plain CSS `z-index`. Overlapping clips (crossfades) need separate tracks.

Media elements additionally support source offset, playback rate, volume. Animations inside a clip can be GSAP, CSS, WAAPI, Lottie, Three.js, or Anime.js — all seeked frame-accurately via adapters, so anything the catalog or you author renders deterministically (same guarantee as our virtual-clock recorder).

## CLI

```bash
npx hyperframes init my-video      # scaffold project
npx hyperframes add <block-name>   # pull a catalog block into the project
npx hyperframes preview            # live-reload browser preview
npx hyperframes render --output video.mp4
```

There's also an official agent skill (`npx skills add heygen-com/hyperframes --full-depth`) and a Studio editor UI — not required; the CLI + HTML is enough for our flow.

## Catalog highlights (fetch the page before using a block)

Docs index for everything: `https://hyperframes.heygen.com/llms.txt` — each block has a page at `hyperframes.heygen.com/catalog/{blocks|components}/<name>.md`. Fetch the block's page for its API before adding it. The categories that matter most for our videos:

- **Transitions** (shader/WebGL): `flash-through-white`, `cinematic-zoom`, `whip-pan`, `glitch`, `light-leak`, `sdf-iris`, `cross-warp-morph`, plus whole families (blur/push/radial/3d/destruction).
- **Camera** (apply over any content, incl. embedded UI clips): `push-in`, `pull-back-reveal`, `camera-dolly-zoom`, `rack-focus`, `ui-focus-zoom`, `camera-shake`, `drift-hold`.
- **Captions/kinetic type**: `caption-pill-karaoke`, `caption-kinetic-slam`, `headline-slam`, `scramble-reveal`, `morph-text`, `per-word-rise`, `titlecard-calm`, `titlecard-lockup`.
- **UI story blocks** (fake-UI motion graphics — fine when no real app is involved): `ai-chat-reveal`, `chatgpt-exchange`/`claude-exchange`, `typed-prompt`, `notification-cascade`, `checkout-flow`, `signup-flow`, `device-frame-stage`, `browser-device-stage`, `app-showcase`.
- **Finishing**: `logo-outro`, `logo-sting`, `cta-close`, `cta-lockup`, lower-third family (`lt-*`), `grain-overlay`, `vignette`, color grading (`reference/color-grading.md`).
- **VFX**: `vfx-liquid-glass`, `ios26-liquid-glass`, `vfx-shatter`, `vfx-portal`, `mesh-gradient-bg`, `aurora-drift`.
- **Data**: `data-chart`, `bar-chart-race`, `chart-story`, `us-map`/`world-map` family, `count-up`, `number-wheel`.

## Gotchas

- HyperFrames' determinism covers its adapters — a raw `<video>` of a recorded scene is seeked as media (fine), but don't put live real-time logic inside a HyperFrames clip and expect our recorder's virtual-clock tricks; each pipeline owns its own determinism.
- Brand it: catalog blocks ship with default styling — restyle to the target brand (e.g. Fregio tokens from `motion-scenes/_fregio-ui/fregio.ts`) before rendering, or the output reads as a template.
- The Apple-HIG bar (references/apple-motion-hig.md) applies to compositions too: one hero motion per beat, transitions serve the story (a shader wipe between unrelated shots reads as noise), end at rest.
