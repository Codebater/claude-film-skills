---
name: motion-ui-video
description: Turn a one-line idea into a polished motion-UI video — scaffold a small React scene from animate-ui's animated component registry (text effects, backgrounds, liquid/ripple buttons, radial menus, notification lists, animated icons), choreograph it on a timeline, then deterministically record it frame-by-frame with Playwright and assemble an mp4 with ffmpeg. Use this skill whenever the user wants a "motion UI video", "UI animation clip", "animated component demo", "micro-interaction reel", a social clip showing UI motion, B-roll of an interface animating, or wants to showcase/record any animated UI concept as video — even if they don't name animate-ui or say "video" explicitly (e.g. "make a clip of a counter ticking up", "I need UI b-roll for the launch post").
---

# Motion UI Video

Idea → animated React scene built from animate-ui components → deterministic frame capture → mp4.

Two rendering pipelines share this skill; pick during the Direct step:

- **`record.mjs`** (this skill's recorder) — when the shot is a **live UI driven by real input**: cursor clicks real buttons, typing flips real state. Nothing else can do this.
- **HyperFrames** — when the shot is **motion graphics** (title sequences, kinetic captions, charts, shader transitions, logo stings) or a **multi-scene composition** joining clips with transitions and music. Read [references/hyperframes.md](references/hyperframes.md) for routing, the timing model, and the 400+ block catalog before reaching for it.
- **Hybrid** is the default for full promos (>15 s): record UI scenes with `record.mjs`, then assemble them in a HyperFrames composition (titlecard → scenes joined by shader transitions → logo outro, music track).

The output is not a screen recording of a website. It is a **directed micro-film of UI motion**: a composed stage, a choreographed timeline, and (when interaction is involved) a visible cursor causing every effect. Cause → effect is the golden rule — nothing animates "because the video decided to"; either it enters on the timeline as a reveal, or the cursor makes it happen.

## Pipeline overview

1. **Direct** — turn the idea into a shot plan (what's on stage, what moves, when, why).
2. **Scaffold** — copy the bundled Vite+React+Tailwind template, install animate-ui pieces.
3. **Compose** — write `Scene.tsx` against a timeline constant, style the stage.
4. **Verify** — dev server + browser preview, console clean, motion looks right.
5. **Record** — `scripts/record.mjs` steps virtual time frame-by-frame and assembles the mp4.
6. **Deliver** — ffprobe-check, send the file, iterate on feedback.

## 1. Direct the shot

Before touching code, decide:

- **Format**: 16:9 (1280×720) for landing/embed, 9:16 (1080×1920) for reels/shorts, 1:1 (1080×1080) for feeds. Ask only if the destination is genuinely ambiguous; default 16:9.
- **Duration**: 6–10 s is the sweet spot for a single concept; 12–20 s for a multi-beat story. Short and dense beats long and sparse.
- **fps**: 30 default; 60 for buttery micro-interaction close-ups (doubles capture time).
- **Beats**: write the timeline as seconds before writing code, e.g. `0.0 stage fades in → 0.6 headline splits in → 1.8 cursor flies to button → 2.3 click, ripple → 2.9 notification list cascades → 5.5 hold → 6.0 end`. End on a resolved, stable frame (or design a seamless loop: last state ≡ first state).
- **Components**: read [references/catalog.md](references/catalog.md) and pick 1–3 animate-ui pieces that carry the idea. One hero motion + one supporting layer (background, caption) beats five competing effects.

Interaction-first rule (standing directive for all video work): anything a user would trigger in real life must be triggered on camera by the virtual cursor — hover, click, type. Timeline-only reveals are for entrances and ambient layers.

**Motion quality bar**: before finalizing the beat plan, read [references/apple-motion-hig.md](references/apple-motion-hig.md) — Apple HIG principles translated into directing rules (every beat needs a communicative job, reactions emanate from the press point within 2–3 frames, one hero motion per scene, springs overshoot once, no idle wiggle, end at rest). Run its checklist again before recording.

## 2. Scaffold the scene

Create the project (default location: `motion-scenes/<slug>/` under the current working directory, unless the user points elsewhere):

```bash
cp -r "<this-skill>/assets/scene-template" motion-scenes/<slug>
cd motion-scenes/<slug> && npm install
```

Then add the animate-ui pieces you picked. The template's `components.json` already maps the `@animate-ui` registry, so namespaced installs resolve their own dependencies (motion, radix, etc. get npm-installed automatically):

```bash
npx shadcn@latest add @animate-ui/primitives-texts-splitting --yes --overwrite
```

Components land in `src/components/animate-ui/{components|primitives}/<category>/<name>.tsx`. **Read the installed file before using it** — props are typed and self-documenting. If usage is unclear, install the matching `demo-<item>` (every item has one) and read it, or fetch `https://animate-ui.com/r/demo-<item>.json` and read `files[0].content` without installing.

If `npx shadcn` misbehaves (interactive hang, registry error), fall back to manual install: fetch `https://animate-ui.com/r/<item>.json`, write each `files[].content` to its `target` under `src/`, `npm i` the listed `dependencies`, and recurse into `registryDependencies`.

## 3. Compose the scene

The template renders `src/scene/Scene.tsx` on a fixed full-viewport stage (`#stage`, dark by default). Author the scene like a title sequence, not a webpage:

- **One timeline constant.** Put every beat in a single `const T = { headline: 0.6, cta: 1.8, ... }` (seconds) at the top of `Scene.tsx` and derive all `delay` props from it. When the user asks to "make the notification come in later", you change one number.
- **Entrances via motion.** animate-ui components animate their own behavior (typing, counting, rippling); wrap them in `motion.div` with `initial`/`animate` + `delay` for stage entrances. `transition={{ delay: T.x, duration: 0.5, ease: [0.22, 1, 0.36, 1] }}` is a good default enter. Timing/easing rules — micro vs transition vs hero durations, springs vs eases, decelerate-in/accelerate-out — live in [references/apple-motion-hig.md](references/apple-motion-hig.md).
- **Stage design matters.** A component floating on flat black reads as a tech demo. Give it a context: a soft radial glow behind the hero, an animate-ui background layer at low opacity, a caption in a real typeface, generous negative space. Load `frontend-design` skill sensibilities: intentional palette, no default-looking UI.
- **State-driven interactions.** Anything the cursor triggers must be real: an actual `<button>` with a click handler flipping React state, a real hover style. The recorder sends real mouse events — wire the UI so those events do the work.
- **Determinism.** Never use `Math.random()` unseeded or `Date.now()` for visuals — the recorder virtualizes time but random layouts change per run. Seed or hardcode.

## 4. Verify before recording

Start the dev server (template runs on **port 3998**) and check it in the browser preview: console clean, animation timing feels right, nothing clipped at the stage edges. Fix here, not by re-recording blind. A `?freeze=<seconds>` query param is not built in — to inspect a moment, temporarily set the relevant `T` values to 0.

## 5. Record

Fill in `scene.video.json` (the template ships one), then:

```bash
node "<this-skill>/scripts/record.mjs" scene.video.json
```

The recorder starts the dev server itself if the URL is down, patches the page clock (rAF, `performance.now`, timers, WAAPI) before any script runs, then advances time exactly `1000/fps` ms per frame and screenshots each step — so motion/framer-motion output is frame-perfect and machine-load independent. Cursor beats (`move`, `click`, `type`…) fire real mouse/keyboard events interpolated across frames, with a visible cursor dot injected on stage. ffmpeg assembles at CRF 18, yuv420p, faststart; capture runs at 2× device scale and downscales for crisp text.

Config schema, beat actions, and every known gotcha: [references/recording.md](references/recording.md). Read it before your first recording and whenever output looks wrong.

## 6. Deliver

- `ffprobe` the mp4 (duration, resolution match the plan).
- Eyeball 3–4 spread frames from `out/frames/` — entrance, interaction, resolution.
- Send the mp4 to the user with a one-line description of the beats. Offer format variants (9:16 crop re-render = change viewport + re-record, cheap).
- Keep the scene project — iteration requests ("slower", "blue instead") are one-line edits + re-record.

## When something looks wrong

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Animations frozen in video | Component drives itself off real `setInterval`/worker outside the patched clock | Check recording.md § virtual time; prefer motion-driven primitives |
| Motion jumps/pops at frame 0 | Scene animated during load, before capture began | Gate entrances on `T` delays ≥ 0.1 s; recorder starts clock at 0 only after `__SCENE_READY` |
| Cursor invisible | `cursor: false` in config, or no beats defined | Set `"cursor": true` / add beats |
| Text blurry | deviceScaleFactor 1 | Keep `deviceScaleFactor: 2` (default) |
| Colors washed out | yuv420p limited-range is normal; extreme cases | design brighter accents; don't chase exact sRGB in mp4 |
