# Seedance 2.5 (BytePlus ModelArk) — condensed production reference

Distilled from the official docs (2026-08): Dreamina Seedance 2.5 tutorial (docs.byteplus.com/en/docs/ModelArk/2607688) and prompt guide (…/2607689). Verify against those pages if the API errors in ways this file doesn't predict.

## Model capabilities

- **Model ID**: `dreamina-seedance-2-5-260628` (2.0 series: `dreamina-seedance-2-0-260128`, `-fast-260128`, `-mini-260615`).
- Single generation up to **30 s**, with native audio (`generate_audio: true`), in 11 languages (EN, ZH, ES, ID, MS, TH, AR, PT, VI, JA, KO).
- Up to **50 reference assets** per request: ≤30 images, ≤10 videos (combined ≤30 s), ≤10 audio clips (combined ≤30 s).
- **Resolution**: `480p` or `720p` only (no 1080p/4K on 2.5; 2.0 has them).
- **Ratio**: `21:9, 16:9, 4:3, 1:1, 3:4, 9:16, adaptive` (adaptive = model picks from prompt/assets). Via input assets, any ratio in [0.4, 2.5] is reachable.
- **Duration**: `[4, 30]` integer seconds or `-1` (model picks).
- **Output format**: `mp4` (default, compatible) or `mov` (H.264 + yuv444p + PCM — higher color fidelity; **use mov in editing/extension chains**; playback needs VLC/mpv/ffplay).
- `watermark: true|false` (default false).
- No real human faces in reference images/videos — input moderation blocks them. (Platform offers preset digital characters and "trusted model outputs" for faces.)

## API

Create task:

```
POST https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks
Authorization: Bearer $ARK_API_KEY
{
  "model": "dreamina-seedance-2-5-260628",
  "content": [
    {"type": "text", "text": "<the prompt>"},
    {"type": "image_url", "image_url": {"url": "https://..."}, "role": "reference_image"},
    {"type": "video_url", "video_url": {"url": "https://..."}, "role": "reference_video"},
    {"type": "audio_url", "audio_url": {"url": "https://..."}, "role": "reference_audio"}
  ],
  "generate_audio": true,
  "ratio": "16:9",
  "duration": 20,
  "resolution": "720p",
  "output_format": "mp4",
  "watermark": false
}
```

- Async: response returns a task `id`; poll `GET …/tasks/{id}` until `status` is `succeeded`/`failed`; result contains the video URL.
- **Video URL lives 24 h, max 100 downloads — download immediately.** Task records last 7 days.
- Rate limits (individual account): 180 RPM, 3 concurrent tasks.
- Asset URLs must be publicly reachable (BytePlus TOS recommended). Images may also be Base64 or asset ID; request body ≤ 64 MB.
- Optional `omni_reference_task_type`: `auto` | `edit` | `extend` — setting it moves constraint validation to submit time (sync error instead of async failure). Mismatch with actual prompt intent → `InvalidParameter.TaskTypeMismatch`.

### Asset input limits

| Type | Formats | Limits |
|---|---|---|
| Image | jpeg png webp bmp tiff gif heic heif | 300–6000 px sides, ratio 0.4–2.5, < 30 MB |
| Video | mp4, mov (H.264/H.265 + AAC/MP3) | 2–30 s each, 480p/720p, 24–60 fps, ≤ 200 MB, pixels 407 696–8 295 044 |
| Audio | wav, mp3 | 2–30 s each, ≤ 15 MB |

## Task types and locked parameters (mandatory table)

The model infers the task type from assets + prompt intent. Wrong parameter combos error (`InvalidParameter.TaskTypeConstraint`).

| Task | Trigger | Locked params |
|---|---|---|
| Text-to-video | text only | none |
| First/first-last frame | `role: first_frame` (+ `last_frame`) | `ratio` **must be** `adaptive` (output matches first-frame image); duration free |
| Reference-to-video | any `reference_*` role, no edit/extend intent | none |
| Video **editing** | `reference_video` + edit intent words (*edit video, add, remove, delete, modify, replace, change to*) | `ratio: adaptive`, `duration: -1`; input video 4–30 s; output ≈ input length (−≤0.4 s); prefer mov |
| Video **extension** | `reference_video` + extend intent words (*extend forward/backward, continue, continue the story*) | `ratio: adaptive`; duration free; prefer mov |

First and last frames must share the same aspect ratio (mismatched last frame gets stretched).

## Prompt structure (official formula)

> **subject + action/event + scene/environment + visual style + camera movement/cuts + sound** — omit what's unneeded.

Recommended layout:

1. **One-sentence summary** — subject + location + event + genre/style + camera.
2. **Style block** — lighting, texture, lens/film stock, palette, atmosphere. State recurring constants once (camera feel, environment, mood).
3. **Asset bindings** — one line per asset by upload order.
4. **Shot list on a timeline** — `0-3s: …` or `Shot 1: …`, each with visuals, action, camera, audio.
5. **Overall requirements** — consistency notes, ratio, negatives.

### Asset referencing rules

- Refer to assets by upload order: `@Image1`, `@Video 2`, `@Audio 1`. Bind explicitly in text: *"@Image1 depicts the protagonist John and uses the voice timbre from @Audio1."* Never rely on text written inside the image (causes character confusion).
- Many subjects → list bindings one per line. 1–8 subject images work best (9–12 unstable). Subject A/V refs: 1–5 subjects, 5–10 s clips work best.
- Say **which aspect** of the asset to use: *"Refer to the casting action in @Video1 and the orbit camera move in @Video2"*, *"Refer to @Image1 for lighting and filters only."*
- If the asset is accurate, don't re-describe it — *"Strictly follow the actions and camera movements of @Video1"* suffices.

### Timestamps

- Integer seconds, continuous timeline — **no gaps** (`0-3s … 3-8s`, never `0-3s … 5-8s`).
- Too little plot in a range → model improvises; too much → excess cuts or dropped beats. ~One beat per 2–4 s.
- Time-point control works: *"at the 5-second mark, quick left wipe with a natural dissolve"*. Relative control works: *"after 3 seconds, …"*. Don't timestamp high-frequency actions ("shake head 3×/s").
- Seedance 2.0 ignores timestamps (only Shot N); 2.5 obeys them.

### Camera language

Write plain terms directly: shot size (extreme wide/wide/medium/medium close-up/close-up), movement (push in, pull out, pan, track, follow, orbit, dive, tilt up, handheld), angle (low angle, overhead, FPV), techniques (long take/one-shot, dolly zoom, bullet time, speed ramp). Niche terms → term + plain explanation (*"Rack focus: focus shifts smoothly from foreground trees to the character behind"*). Transitions: give **trigger time + method**.

### Audio notation

- `()` music, `<>` sound effects, `{}` dialogue, `【】` on-screen subtitles. Non-default-language dialogue: name the language before the line.
- Negatives only for subtitles/audio: *"No subtitles."*, *"No BGM; environmental sounds only."*, *"No audio."* Everything else: positive phrasing.

### Actions and expressions

General beats over micro-choreography (*"does a few sets of high-knee raises"*), specifics only for the 1–2 memorable actions. Expressions: descriptive sentences, not idioms.

## Special modes (when relevant)

- **Keyframes (strict storyboard)**: input each frame as its own `reference_image`, open the prompt with *"Use Images 1 to N in order as keyframes."* Output aligns closely with the images. Duration free.
- **Multi-panel storyboard (loose)**: one image containing ≤15 simple line-art panels; only high-level plot guidance, model keeps autonomy; fill in actions/camera/style via prompt. Avoid noisy AI-rendered boards and text-in-image.
- **3D clay-model previz**: a blocky 3D animatic drives camera/motion/blocking; say exactly which channels to take (*"reference @Video1 only for camera movement, rhythm and blocking, not visual content"*) and map models to characters explicitly.
- **First/last frame**: prefer `role: first_frame`/`last_frame` (locks ratio to the image); as loose alternative use `reference_image` + "Image 1 is the first frame" (ratio stays free, match is approximate).
- **Extension**: *"Extend @Video1 by 5 seconds: …"* — mov in/out for seamless stitch; volume step is smaller when extending a 2.5-generated video.
- **Seamless transition**: two videos in, model generates the in-between; specify the transition camera move and what morphs.
- **One-click video**: pile of images/videos → montage; state style, that images may only subtly move ("live-photo effect"), and audio direction.

## Worked example skeleton (30 s commercial, from official docs)

```
3D animated advertising style, bright translucent colors, high-quality commercial
animated short with slightly exaggerated humor. The [mascot] is cute and expressive,
referring to @Image1. [texture/lighting notes]
0-3s: [world at its problem state; heat, thirst] <SFX: roaring heat waves>
3-6s: [discovery of product; eyes widen] <SFX: "ding">
6-8s: [embrace; hold 1s — the advertising memory point] <thump, half-second silence>
8-11s: [product opens; sensory burst begins] <crack, juice-burst>
11-16s: [transformation: product floods the world into the promise]
16-20s: [comic consequence; mascot floats on the product]
20-23s: [cut to white: brand name + slogan; VO reads the slogan] <clean brand sting>
23-29s: [afterglow: vacation state, pull out, freeze] (relaxed summer music)
Subtitles may keep only the brand name; no other text.
```

## Official prompt-optimizer skill

BytePlus ships its own prompt optimizer (`/sd25-pe`), installable via
`npx --yes skills@latest add "https://arkdocs-en.tos-ap-southeast-1.volces.com/skills/" --skill sd25-pe --yes` — useful as a second opinion on a composed prompt, not a replacement for the dramaturgy gate.
