---
name: one-prompt-film
description: >
  Turn an idea or a story into finished AI-generated film: capture the story with the user,
  choose trailer vs. packed short, board the scenes a great director would choose and render the
  storyboard with GPT Image, lock character/world continuity plates, evaluate dramaturgy
  (film + commercial storytelling), direct it like a film — director/DP/editor pass with
  Eyecandy (eyecannndy.com) technique research for camera, blocking, reveals, and transitions —
  then engineer a production-grade Seedance 2.5 prompt per the official BytePlus ModelArk guide,
  generate the video via the ModelArk API (or Higgsfield MCP fallback), and optionally apply a
  flim filmic color grade. Use this skill whenever the user
  wants to create a video, film, commercial, ad, spot, trailer, music video, short film, multi-act
  story, or "make a video of X" from an idea or one-line prompt — even if they don't mention
  Seedance, ModelArk, storyboards, or dramaturgy. Also use it when the user asks to develop a story
  for film, build a storyboard, evaluate/improve a video idea's story, keep a character or world
  consistent across shots, or color-grade an AI-generated video with flim.
---

# One-Prompt Film

Pipeline: **story capture → dramaturgy gate → storyboard → continuity plates → direction pass (picture + sound) → production analysis → Seedance 2.5 prompt → generate → audio production (analyze native → ElevenLabs stems → mix → QC) → (optional) flim grade → deliver**.

The goal is not "a video that matches the words" — it's a video a viewer would actually watch to the end. That is why dramaturgy and direction come before prompt engineering: Seedance 2.5 executes whatever structure you give it, so a weak structure produces an expensive, well-rendered nothing, and undirected coverage produces a generic one. Behave as if a creative director, film director, DP, editor, supervising sound editor, and music supervisor sit between the user's idea and the Seedance prompt engineer. Don't just describe a cinematic video — direct one, picture and sound together.

**The keyframe law.** A video model re-animates what the still already decided. Anything living only in prose is a suggestion the model may overrule; anything in the first frame is inherited. When a shot must obey a hard constraint, do not argue with prose — hand it a plate. Order of operations is therefore **story → board → plates → video → grade**, cheapest first, each stage constraining the next. Full mechanics and the verified proof in [references/continuity.md](references/continuity.md).

## Step 0 — Story capture & scope

**Fork first.** Two front doors:

- **Quick clip** — a one-off spot, social video, product ad, or single scene. Don't interrogate: infer format from context (a product name → commercial; a mood/character → film scene), state which reading you picked, and go straight to Step 1. Skip Step 2 (board) unless the piece has enough structure to need one.
- **Story project** — a film, short, trailer, multi-act piece, or anything the user describes as "a story". Here you **do** sit down with them first. This is a conversation, not an interview: offer, don't quiz.

For a story project, capture — proposing candidate answers rather than asking open questions, so the user reacts instead of composing:

1. **The engine in one line** — who wants what, what stops them, what turns.
2. **The concept image** — the single frame that contains the premise. If neither of you can name it, the story is not ready; find it before boarding.
3. **The ending**, even for a trailer. You cannot select scenes without knowing what they are building toward.
4. **Format** — **trailer** (argument for watching, withholds the ending) or **packed short** (whole story, resolution included). These are different dramaturgies, not different lengths; the fork is spelled out in [references/storyboard.md](references/storyboard.md) §2. Recommend one and say why.
5. **World and character** — enough to write the identity strings in [continuity.md](references/continuity.md) §2.

Then also settle:

- **Total runtime and act count.** Seedance caps a single generation at 30 s, so anything longer is N acts of ≤ 30 s chained last-frame → `start_image`. Prefer the longest single take that holds — one 30 s generation beats a stitched multi-clip edit for continuity and seamlessness, and beat capacity scales with duration (7 beats held fine across 30 s where 4 beats in 15 s silently dropped one).
- **Aspect ratio.** Reels/TikTok/Shorts `9:16`; YouTube/web `16:9`; cinematic *delivery* `21:9` — "cinematic" as a tone adjective does not force 21:9, and top-down or vertically-composed framing crops badly in it. Square feed `1:1`. Instagram's native 4:5 is not in Seedance's list — use `9:16` or `1:1`.
- **Assets**: did the user supply or *mention* images/videos/audio? Via the ModelArk API Seedance needs **publicly reachable URLs**; via the Higgsfield MCP upload local files with `media_upload` → PUT → `media_confirm`. Seedance rejects reference assets containing real human faces.

Write the captured story to `STORY.md` in the project folder before proceeding — acts get made over days, and the engine, ending and identity strings must survive between sessions.

## Step 1 — Dramaturgy gate

Read [references/dramaturgy.md](references/dramaturgy.md) and evaluate the idea with **both** rubrics:

- **Film dramaturgy**: desire → obstacle → turn; setup/payoff; visual (not verbal) storytelling; one emotional arc that fits the duration.
- **Commercial dramaturgy** (always for ads, and for any video that sells something): hook ≤ 2 s, single-minded proposition, product as the turn (not wallpaper), a memory point, brand payoff.

Produce a verdict:

- **GREEN** — idea has a working engine. State the one-line dramatic engine and proceed.
- **YELLOW** — engine is weak (no turn, no hook, two messages, arc too big for the duration). Fix it yourself using the repair moves in the reference, show the user "your idea → strengthened treatment" in 3–4 sentences, and proceed with the strengthened version.
- **RED** — no engine at all (a description, not a story: "a drone shot of mountains"). Do not silently generate wallpaper. Offer 2–3 concrete treatments that give it an engine, recommend one, and ask the user to pick **only if** the treatments genuinely diverge in intent; otherwise pick the best and say so. In the verdict block, show both scores with an arrow: `RED as submitted (…) → GREEN with Treatment A (…)`.

Keep the written verdict short: verdict, engine in one line, what you changed and why. No essays — except a RED's treatments, which earn a few lines each.

## Step 2 — Storyboard & continuity plates

Skip for a quick clip with no real structure. Required for any story project — and the board is not decoration, it is **the shot-selection contract**: once approved, its panels are the generation plan and its crops become the plates that control the video.

Read [references/storyboard.md](references/storyboard.md). In short:

1. **Select the scenes a great director would board.** A conventional board shows *what happens*; a Nolan board shows *how the story is built*. Spend panels on the image that IS the concept, the frames where the structure becomes visible, the unequal cost of time, the physical event over the spectacle, the moment *before* the explanation, one human anchor, and an ending that reframes the opening. Do not spend them on travel, agreement, or beats already implied. Full criteria and the anti-patterns in §1.
2. **Panel count follows format** — trailer 12–15, packed short 15–20, single act 6–9 (§2).
2b. **Two tiers when the film exceeds 30 s** (§4b). The **master board** selects which scenes
   exist; an **act board** (6–9 panels, timecodes summing to the act's length) decides how one act
   is shot and is then bound into that act's generation as reference. Write each act's
   job-in-the-film in one line before boarding it, and execute any master-board rhyme identically
   in both acts that carry it.
2c. **Place the seams before boarding the acts** — read [references/seams.md](references/seams.md).
   `ceil(runtime ÷ 30)` gives a count, never the boundaries: 30 s is a ceiling, not a grid, and
   acts should be unequal. The governing law is an inversion of normal editing — **traditional
   editing cuts on action; chained generation must cut on stillness**, because the seam is not
   hidden by the cut, it is re-rendered by a model that needs a stable target. So *design* a held
   beat into the end of each act rather than hunting for one afterwards, keep dialogue from
   straddling a seam, and prefer fewer long acts to many short ones — the cheapest seam is the one
   you never create.
3. **Render it with `gpt_image_2`** at `resolution: "4k"`, `quality: "high"`, one image, 16:9 or 3:2. Chosen because it is the typography model — a board is mostly type, and the photoreal-first models cannot spell. `quality` defaults to `low`; always override it or the captions break up.
4. **Show the user the board and get approval before spending on video.** Boards are cheap, re-rolls are cheap, generations are not.
5. **Then build the plates** per [references/continuity.md](references/continuity.md): crop the best protagonist panels → character sheet → register as a reusable Element; generate one world plate per region; add prop/creature plates as needed. Write the identity strings once and reuse them verbatim everywhere.

Verify every plate by eye before moving on. Look at the image; do not assume it.

## Step 3 — Direction pass (director + DP + editor)

Read [references/directing.md](references/directing.md) and direct the piece before prompting it. The question changes from *"how do I prompt Seedance to generate this?"* to *"how would an excellent director and cinematographer shoot this?"* — the answers then get translated into Seedance language in Steps 5–6.

In short (full detail in the reference):

1. **Visual idea** — what's hidden vs. visible, where the reveal lands, how attention moves, how the environment participates, whether the camera follows/anticipates/observes.
2. **Research when warranted** — if the honest check says *"the idea is good but the way we're shooting it is ordinary"*, mine the Eyecandy technique library (taxonomy embedded in the reference; browse eyecannndy.com via the in-app browser for nuance — direct fetches 403). Search by **filmmaking problem** (how is the product revealed? can movement hide the cut?), never by subject. Extract the *principle* from any reference and re-stage it in this concept's world — never copy the shot. Skip research entirely when the direction is already clear or the user supplied strong references.
3. **Cinematography** — every camera move needs a stated motivation (no motivation → locked camera); lens, depth, and *motivated* light sources chosen per shot.
4. **Editor pass + master audiovisual timeline** — decide where shots begin/end, what motivates each cut, and the rhythm shape before writing anything; transitions arise from physics/composition (one excellent one beats five tricks). Design sound in the same breath, per §1 of [references/audio-direction.md](references/audio-direction.md): audio beats may set cut frames (a ding fixes the reaction shot, music stopping dead sets up the joke, a door slam *is* the transition), and the timeline marks dialogue, ambience, foley, hero SFX, music movements, silences, and the sonic brand moment — this same timeline later becomes the audio manifest.
5. **Genre grammar + blacklist** — shoot comedy, luxury, tech, sport, docu, and surreal differently; actively avoid the generic-AI-cinematic tells listed in the reference.

Output the **director's plan** in the reference's handoff format (visual idea, signature device or "none", genre grammar, per-shot intent/blocking/camera-with-why/lens/light/cut). Every decision must earn its place: story, reveal, rhythm, emotion, or information — otherwise cut it.

## Step 4 — Production analysis (per Seedance 2.5 guide)

Read [references/seedance-25.md](references/seedance-25.md). Decide, and note explicitly:

1. **Task type** → text-to-video (no assets), reference-to-video (assets as semantic reference), first/last-frame, keyframes, editing, or extension. This dictates locked vs. free `ratio`/`duration` — the constraint table in the reference is mandatory reading, wrong combos hard-error at the API.
2. **Duration allocation**: place the director's plan's shots on a continuous timeline (`0-3s / 3-8s / …`, integer seconds, no gaps). One beat per 2–4 s; don't overpack a range or the model cuts or drops plot.
3. **Camera plan**: comes from the direction pass — carry over each shot's camera, motivation, and cut mechanism, written in plain camera language.
4. **Audio plan**: dialogue `{}` with language stated, SFX `<>`, music `()`, subtitles `【】` or "No subtitles". Set `generate_audio: true` unless the user will score it themselves.
5. **Style block**: genre, lens/film texture, lighting, palette, atmosphere — consistent things stated once, up front or as "Overall requirements".

## Step 5 — Compose the prompt

**Read the `seedance-prompt` skill first** (`../seedance-prompt/SKILL.md`) and compose in the house production dialect. The official structure below is the *grammar*; that skill is the *dialect* — the bible header, LOCKS, scale/geometry blocks, the labelled per-shot sub-schema, and the anti-tell pass that kills the frozen-face / waxy-skin / slow-mo / dead-centre look. Anything with a character on screen needs it; a plateless landscape oner can get by on the grammar alone.

Translate the director's plan into the official structure exactly (full template + worked examples in the reference). This is translation, not re-invention: the director decided *what* happens; this step decides how to communicate it to Seedance. Prefer a plain physical description over film jargon whenever it's more reliable ("the runner stays pinned dead-center while the street blurs past" beats "locked-on shot") — keep terms Seedance knows (push in, orbit, wide shot, handheld), explain niche ones inline. Blocking, entrances/exits, and named light sources must survive translation — they're what makes the result feel shot rather than generated.

```
[One-sentence summary: subject + location + event + genre/style + camera]
[Style block: visual style, lighting, texture, atmosphere]
[Asset bindings, if any: "@Image1 is the product…" — one line per asset, by upload order]
0-Xs: shot 1 — visuals, action, camera, {dialogue}, <SFX>, (music)
X-Ys: shot 2 — …
[Overall requirements: consistency notes, ratio, "No subtitles" etc.]
```

Rules that matter most: positive phrasing (negatives only for subtitles/audio), explicit asset-to-role bindings by upload order, timestamps in whole seconds with no timeline gaps, niche camera terms explained inline. Two translation details: the director's plan's approximate `~Xs` durations become the firm `X-Ys` timeline **here**, and the directing blacklist is enforced by omission and positive counter-phrasing ("natural motion speed", "clean air") — never as a negative list in the prompt, which Seedance doesn't support outside subtitles/audio.

Show the user the final prompt before spending money.

## Step 6 — Generate

**Primary — ModelArk API** (needs `ARK_API_KEY` env var and purchased Seedance 2.5 quota):

```bash
python scripts/seedance_generate.py --prompt-file prompt.txt --duration 20 --ratio 16:9 --out film.mp4
```

The script creates the task, polls until done, and downloads the result. Add `--asset reference_image=URL` (repeatable) for assets — URLs must be publicly reachable. Full flags: `--resolution 480p|720p`, `--format mp4|mov`, `--no-audio` (audio generation is ON by default), `--watermark`. Pass `--task-type edit|extend` for those tasks: `edit` auto-forces `ratio adaptive` + `duration -1`; `extend` (and any first/last-frame asset) auto-forces `ratio adaptive` only — duration stays yours.

**Fallback — Higgsfield MCP**: if there is no `ARK_API_KEY`, check `models_explore` for a Seedance model and use `generate_video` with the same composed prompt (asset-binding syntax may need simplification to the MCP's schema). Say which backend you used.

Generation costs real money and takes minutes: get the user's go-ahead on the prompt + duration before the first paid call, then poll patiently — don't resubmit on slow tasks.

## Step 7 — Audio production

Read [references/audio-direction.md](references/audio-direction.md). Default for commercials and any piece with dialogue/VO or a designed music moment; skip only when the native Seedance soundtrack fully serves the direction (verify by listening, not by assumption). Needs `ELEVENLABS_API_KEY` — if it's absent, say so and deliver with native audio.

1. **Analyze native audio** — extract/play it, then decide per element: **KEEP / ENHANCE / REPLACE / LAYER** (criteria in the reference). Never replace genuinely good native audio out of principle; the common outcome is keep ambience+foley, replace dialogue and music, add hero SFX + brand sting.
2. **Generate stems** with `scripts/eleven_audio.py` — one call per stem (dialogue, VO, ambience, foley, hero SFX, music, sonic branding), directed like performances: acoustic-result prompts for SFX, actor notes for dialogue, timeline-aware briefs for music ("builds to 14s, cuts, one warm chord at 17s"). Stems stay separate.
3. **Write the manifest** — translate the master AV timeline from Step 3 into `manifest.json` (schema in the reference): exact start times, gains, fades, trims, native mode, ducking.
4. **Mix**: `python scripts/mix_audio.py --video film.mp4 --manifest manifest.json --out film_mixed.mp4` — positions/fades stems, auto-ducks music under dialogue, limits, loudness-normalizes, muxes with the video untouched.
5. **Audio QC** — listen to the result against the checklist in the reference (intelligibility, sync, hierarchy, believable space, no clipping, correct sonic ending). Fix the offending *stem or manifest entry* and re-mix — mixing is cheap, regeneration is not.

Restraint rule: sound has hierarchy — decide what the audience should hear at each moment; no whoosh/boom/ding on every action.

## Step 8 — Optional flim grade

flim (github.com/bean-mhm/flim) is a filmic color transform; applied as a finishing look it adds highlight rolloff and film-like color. Offer it when the result should feel cinematic/graded; skip for UI captures or flat animation styles.

```bash
python scripts/flim_grade.py film.mp4 --preset default --out film_graded.mp4
```

Presets: `default` (neutral filmic), `nostalgia` (warm, saturated), `silver` (dramatic, silver-halide contrast). `--strength 0.7` blends with the original.

For a **signature look** — a grade that is recognisably ours across films, not just "filmic" — use `scripts/signature_look.py`, which composes a look layer (contrast, saturation, split-tone) onto a flim base and bakes the whole thing into one portable `.cube`:

```bash
python scripts/signature_look.py --look graphite --apply film.mp4 --out graphite.cube --out-video film_graded.mp4 --halation 0.2
```

`--list` shows the looks (`clean`, `graphite`, `ember`, `violet`, `bleach`); add new ones by adding an entry to `LOOKS`. Keep the numbers small — a signature is a fingerprint, not a filter. `--halation` is a separate spatial pass (highlight bloom tinted red-orange, the way film's anti-halation layer fails); it lifts the whole frame slightly, so 0.15–0.25 is the useful range and anything above ~0.4 reads as a glow effect. The script downloads the official LUT on first use, bakes the correct sRGB→log2 chain into a .cube, and applies it with ffmpeg (`-c:a copy`, audio untouched). Requires ffmpeg on PATH.

For editing/extension chains, generate `--format mov` and grade only the final export.

## Step 9 — Deliver

Send the finished file to the user (the mixed + graded final, plus the raw Seedance original; keep stems and manifest on disk for revisions). Report: verdict from the gate, backend + parameters used, cost-relevant facts (duration, resolution), and the task ID. ModelArk video URLs expire after 24 h — always download before reporting success.

## Failure modes

Diagnose the mechanism before re-rolling — a re-roll costs a full generation and usually reproduces the same failure.

**Camera / composition**
- **A stated camera constraint is ignored** (locked overhead becomes a frontal wide, a hold becomes a pull-back): prose cannot hold camera geometry through a shot that reveals an environment. Do not restate it louder — generate an unambiguous geometry plate and pass it as `start_image`. See the keyframe law and its verified proof in [references/continuity.md](references/continuity.md) §0.
- **Subject axis flips between shots** (lying vertical in one, horizontal in the next — kills a match cut): state the axis physically ("head at the top of frame, feet at the bottom, body running vertically up the centre") *and* say it matches the previous shot.
- **No room for the event**: a subject filling the frame edge-to-edge leaves nowhere for a time-lapse or an entrance to happen. Frame the room, not just the subject.

**Story / beats**
- **A shot is silently dropped** (usually the last one): too many beats per second in that range. Beat *capacity scales with duration* — 7 beats hold across 30 s where 4 beats in 15 s can drop one. Lengthen the range or merge beats; don't just re-roll.
- **The board reads as a plot summary**: panels were spent on events instead of structure. Re-select against [references/storyboard.md](references/storyboard.md) §1 before generating anything.

**API / assets**
- `InvalidParameter.TaskTypeConstraint` / `TaskTypeMismatch`: prompt intent and parameters disagree — re-check the constraint table (locked tasks need `ratio: adaptive`, editing needs `duration: -1` and an edit trigger word in the prompt).
- Asset rejected: real human face in a reference (not allowed), >30 MB image, video outside 2–30 s / 24–60 fps, or URL not public.
- **Higgsfield offers a preset instead of generating** ("this prompt looks like the preset X"): moody/dark prompts trigger it. Retry the identical call with `declined_preset_id: <id>`.
- **Queue stalls**: Higgsfield job times vary from ~4 min to over 2 h for the same model and duration. Poll patiently and never resubmit — a duplicate is a duplicate charge.

**Finishing**
- **Graded output looks soft / grain crushed**: `signature_look.py` leaves ffmpeg at its default CRF (~2.2 Mbps at 1080p). Re-run its filter chain manually with `-crf 15 -preset slow -c:a copy`.
- **Acts don't match after grading**: grade once from a single baked `.cube` applied identically to every act, and always pull chain frames from the *ungraded* master so the LUT isn't baked in twice.
- mov won't play for the user: that's expected (yuv444p+PCM); point them to VLC/mpv or deliver mp4.
- ElevenLabs `401 detected_unusual_activity`: the key is valid but the account's free tier is blocked (VPN/proxy or multi-account flag) — generation needs a paid plan on that account. Fall back to native Seedance audio and tell the user; don't retry.
