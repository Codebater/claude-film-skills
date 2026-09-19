# Storyboard — scene selection and board generation

The board is not decoration and not a summary. It is **the shot-selection contract**: once the user
approves it, its panels are the generation plan, and individual panels get cropped into the
character/world plates that actually control the video (see [continuity.md](continuity.md)).

So the only question that matters is **which frames earn a panel**.

---

## 1. The selection law — what Christopher Nolan would board

A conventional board shows **what happens**. A Nolan board shows **how the story is built**.
Given N panels, spend them on the frames that make the *structure* legible and the *concept*
visible — not on a proportional walk through the plot.

Select by these, in priority order:

1. **The image that IS the concept.** One frame that contains the whole premise with no dialogue —
   the spinning top, the folding city, the rotating corridor. If the film has a thesis, it has a
   picture. Board that picture first; everything else is support. If you cannot name this frame,
   the story is not ready to board.
2. **Structure made visible.** The moments where the architecture shows: two timelines rhyming,
   scales colliding, a cut that reveals the shape of the whole. Dunkirk's mole/sea/air converging;
   the kick cascade. If your story cross-cuts, at least one panel must show the cross-cut *as* a
   cross-cut (split panel, or two panels deliberately adjacent).
3. **The unequal cost of time.** Any frame whose meaning is that time was spent asymmetrically —
   one character pays hours, another pays years. This is the most Nolan-specific criterion and it
   is worth a panel even when "nothing happens" in it.
4. **The physical event, not the spectacle.** Prefer the frame with weight, consequence and
   tangible material over the frame that is merely large. A truck flipping beats a city exploding.
5. **The moment before the explanation.** Board the beat where the audience's model of reality
   breaks — not the beat where a character explains it. Withholding is a panel; exposition is not.
6. **The human anchor.** One frame carrying the single emotional stake the structure is about
   (the child, the promise, the debt). Without it the puzzle is cold. Exactly one is usually enough.
7. **The ending that reframes the opening.** The last panel should make the first panel mean
   something different. If it doesn't, reconsider the first panel.

**Do not spend panels on:** establishing shots that establish nothing, travel between locations,
characters agreeing with each other, a beat already implied by the panel before it, or "and then
they talked". If two adjacent panels can be merged with no loss, merge them.

**The test:** hand the board to someone who has not heard the story. If they can describe the
*shape* of it — not just the events — the selection worked.

---

## 2. Trailer vs. packed short — pick before boarding

These are different dramaturgies, not different lengths. Ask the user which one, or infer and say
which you picked.

### TRAILER (typically 60–90 s, 12–15 panels)
An **argument for watching**, not a compressed story. It sells the premise and withholds the answer.

- Structure: hook (≤ 3 s) → premise stated visually → escalation montage → the turn → title card.
- **Never show the resolution.** The trailer's job is to make the ending a question.
- Withhold the *mechanism*: show that the world is impossible, not how it works.
- Escalation is rhythmic — panels get shorter and louder toward the turn, then one hard silence.
- The last panel before the title is the memory point: the single image people will describe to
  a friend.
- Sound sets the cuts more than picture does; mark the audio beat on each panel.

### PACKED SHORT (typically 3–5 min, 15–20 panels)
The **whole story**, compressed. Every act present, resolution included.

- Structure: full arc — setup, turn, escalation, climax, resolution. Nothing withheld at the end.
- Cut connective tissue, keep turns. Every scene must do **two or more jobs** (advance plot AND
  reveal character; or pay a setup AND plant a new one) or it does not survive compression.
- Enter every scene as late as possible and leave as early as possible.
- Because there is no room for a second pass, each act gets one signature image, not three.
- If the story will not fit, the answer is fewer subplots, never faster panels.

### SINGLE ACT / ONE SCENE (≤ 30 s, 6–9 panels)
Board only when the act has a real structure to hold. A 30 s single-generation piece often needs no
board at all — go straight to the director's plan.

---

## 3. Board layout spec

Generate the board as **one image**, not a series — it is easier to judge as a whole and cheaper.

- Grid: 3×3, 4×3, 5×3 or 4×4 depending on panel count. Keep panels the same size; do not hero one.
- Each panel carries: **number**, **short title in caps**, **timecode range**, and a one- or
  two-line caption underneath in sentence case.
- Caption writes the *story function*, not the picture ("He doesn't read the fine print" beats
  "close-up of a document").
- Dialogue that must survive into production goes in the caption in quotes.
- Header: film title, subtitle, and the format + total runtime.
- Dark charcoal background, thin panel borders, hand-lettered or condensed sans caption type.
- Aspect: **16:9** or **3:2**. `gpt_image_2` does not offer 21:9.

---

## 4. Generating the board — `gpt_image_2`

Use **`gpt_image_2`** (OpenAI, via Higgsfield `generate_image`). It is chosen specifically because
it is tagged for **text rendering and typography** — a board is mostly type, and the models that
beat it on photoreal imagery cannot spell. Never use a photoreal-first model for a board.

```
generate_image({ model: "gpt_image_2", resolution: "4k", quality: "high",
                 aspect_ratio: "16:9", prompt: <board prompt> })
```

`quality` defaults to `low` — **always pass `high` for a board**, or the caption type breaks up.

Prompt shape:

```
A [N]-panel film storyboard sheet titled "[TITLE]" — [FORMAT], [RUNTIME].
Grid of [R] rows × [C] columns on a dark charcoal background, thin light panel borders,
each panel a photorealistic cinematic still, condensed sans-serif labels in pale grey.

Header across the top: "[TITLE]" left, "[SUBTITLE]" right.

Panel 1 — "[SHORT TITLE IN CAPS]" ([0:00–0:04]): [what is in frame, camera, light].
  Caption beneath: "[story function, one or two lines]"
Panel 2 — ...

Consistent character across every panel: [identity string — see continuity.md].
Consistent world: [world string].
Photorealistic prestige cinema, 35mm anamorphic texture, fine film grain, deep natural contrast.
No watermark, no logos, no page numbers.
```

Keep each panel description to one sentence of picture plus one of caption — a board prompt that
over-describes any single panel starves the rest and the grid collapses.

### Bind existing canon — do not re-invent it

`gpt_image_2` accepts reference images (`medias` role `image`). **If any plate or finished shot
already exists, bind it.** A board generated from prose alone will quietly redesign locked
canon — a capsule becomes a porthole, a robot loses its antennae — and then the board and the
footage disagree about what the film looks like.

Rule: for any element already locked (a registered character Element, a world plate, a creature
plate, or a frame lifted from an act already shot), pass it as a reference and say in the prompt
that panels showing it must match. Verified failure: an AI Labyrinth board written from prose
alone redesigned both the cryo capsule and the eyebot away from plates that already existed —
because the plates were not bound, not because the prompt was unclear.

Board first only when nothing is locked yet. Once a single act is shot, the board serves the
footage, not the other way round.

---

## 4b. Two tiers: the master board and the act boards

Seedance generates **30 s maximum per call**, so any film longer than that is N acts chained
last-frame → `start_image`. That forces two different board artifacts. Do not conflate them.

| | **Master board** | **Act board** |
|---|---|---|
| Answers | *which scenes exist* | *how this act is shot* |
| Panel = | a story beat | a **shot**, with a timecode |
| Panels | 12–20 for the whole film | 6–9 for one act |
| Captions | story function | shot action + dialogue |
| Selected by | the §1 law | the §1 law again, applied *within* the act |
| Purpose | approval + structure | **bound as a Seedance reference** |

### Dividing the film into acts

Place the seams **before** boarding the acts — the boundaries decide what each board has to contain.
`ceil(total runtime ÷ 30 s)` gives a count, never the boundaries; 30 s is a ceiling, not a grid, and
good acts are unequal. The full method — the cut-on-stillness inversion, seed-quality ranking,
designed holds, audio seams and the escape hatches — is in [seams.md](seams.md). Read it first.

One rule belongs here because it is a boarding constraint rather than a seam one:

- **Each act needs its own small arc.** It is not a 30 s slice, it is a scene: it opens on a
  question and closes on a change. If an act has no turn, its boundaries are wrong — merge it with
  a neighbour or move the seam.

### The act board must serve the whole film, not just itself

Before boarding an act, write one line stating **what this act does for the film** — which setup it
pays, which it plants, and what has changed by its final frame. Panels that serve neither the act's
own turn nor that larger job get cut. An act board that reads well alone but does not advance the
master board's spine is a well-shot detour.

Carry the master board's rhymes down into the act boards: if panel 3 of the master rhymes with
panel 16, the act boards containing them must frame those shots **identically**. Rhymes only work
if they are executed to the pixel.

### How an act board actually reaches the generation

**Do not bind the board image itself.** A board is a grid, and a reference plate contributes its
*texture* whether you ask for it or not — binding a grid risks panel borders, split-screen layouts
and caption type bleeding into the render. The board reaches the generation two other ways:

1. **As the shot list.** Each panel becomes one timestamped range in the prompt, in order, with its
   framing, action and camera carried across in words. This is the board's main job.
2. **As crops, when a single panel needs to be exact.** One panel cropped out of the grid is a
   clean plate and can be bound — as `start_image` for that act, or as an extra `image_reference`.
   Never the whole sheet.

What *is* bound is the underlying canon: the character Element, the world plate, the creature/prop
plates. So the act board must be **canon-accurate to those plates** — it is the document a human
reads to check the act before money is spent, and a board that disagrees with the plates will send
someone in the wrong direction. A master board may drift; an act board may not.

## 5. After approval — the board becomes the plates

This is why board quality matters more than it looks:

1. The user approves the board (re-roll or patch panels before moving on — boards are cheap,
   video is not).
2. Crop the panels that show the protagonist best → build the **character sheet** → register as a
   reusable Element.
3. Crop or re-generate the panel showing the signature location → the **world plate**.
4. Each remaining panel becomes a shot in the director's plan with its timecode already assigned.

Full mechanics in [continuity.md](continuity.md). The board is where continuity starts, not where
it ends.
