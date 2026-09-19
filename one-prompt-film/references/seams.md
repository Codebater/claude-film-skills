# Seams — breaking a film that must be generated in ≤30 s pieces

A generation cap is not an editing style. But the moment a film is longer than one generation, the
places where it breaks stop being editorial decisions alone — each one is also a **technical
handoff**, and the two jobs pull in opposite directions. This file is how to serve both.

---

## 1. The inversion

> **Traditional editing cuts on action. Chained generation must cut on stillness.**

In a normal edit you cut mid-movement because motion masks the splice — the eye is tracking, and it
does not audit the join. That instinct is not merely unhelpful here, it is **backwards**.

A chained seam is not hidden by the cut. The last frame of act N is handed to the model as the seed
for act N+1, and the model **re-renders it**. It never copies it. So the question is no longer
"will the audience notice this join?" but "**can a model reconstruct this exact frame from
scratch?**" — and a frame full of motion blur, mid-gesture limbs and half-formed effects is a frame
with no canonical answer. The model invents one, and the invention is the drift.

Every instinct trained on real footage has to be re-pointed. Cut where the picture is *most
resolved*, not where it is most kinetic.

---

## 2. The chain frame has two jobs

Judge every candidate seam twice, because a frame can ace one test and fail the other:

| | **As a terminal frame** (editorial) | **As a seed** (technical) |
|---|---|---|
| Wants | a beat resolved, a question posed, an image worth holding on | sharpness, simple geometry, low fine detail, no transient state |
| Fails on | arriving early, arriving late, landing on nothing | motion blur, crowds, mid-VFX, mid-speech, tiny subjects |

When they conflict, **the seed requirement wins** — because an editorially perfect seam that drifts
gives you two acts that look like different films, and no edit fixes that. An editorially
*adequate* seam that chains cleanly is recoverable; the reverse is not.

---

## 3. Seed quality — what survives re-rendering

Ranked from most to least reliable. Reach as far up this list as the story allows.

**Excellent seeds**
- A **strong simple silhouette** against a distinctive ground — figure in a doorway, against sky,
  against fire. Silhouettes carry almost no fine detail to drift.
- **A held object filling frame** — a hand on a wall, a keychain, a lens, a sealed capsule.
  Objects re-render far more faithfully than faces.
- **Rigid geometry** — a corridor, a capsule, an architectural vanishing point. Hard edges anchor.
- **A still figure in even, motivated light**, subject large and centred.

**Workable seeds**
- A face close-up, still, mouth closed, even light. *Measured on Duke: 7.6 % mean per-channel delta
  — pose, props, costume and framing carried; scale and face shape drifted slightly.* Fine on a
  hard cut; do not promise invisibility.
- A held wide where the environment is distinctive enough to carry identity by itself.

**Poor seeds — avoid or mitigate**
- Any **motion blur**. There is no canonical de-blurred frame; the model picks one.
- **Mid-speech faces** — mouth shape at a given instant is effectively arbitrary and will not match.
- **Crowds and multiple faces** — drift compounds per person.
- **Transient effects mid-formation** — half-formed frost, an explosion in progress, a dissolve, a
  lens flare at peak. The model has no stable target for "40 % through this event".
- **Legible on-screen text** — re-renders as garbled text, and the garble is highly visible.
- **A small subject in a large frame** — too few pixels to constrain identity; gets re-invented.

---

## 4. Design the hold — don't hunt for it

The decisive move, and the one that separates a chain that works from one that fights you:

> **Write the hold into the act. Do not go looking for one in the footage afterwards.**

Every act's final beat should be *scripted* as a hold — the last 1–2 s explicitly described as
stillness: a face landing, a figure stopping, an object settling, breath held. This costs almost
nothing dramatically (held beats read as weight, not as dead air) and it converts the seam from
something you discover into something you **specify**.

In the prompt, end the last time range with an explicit instruction — *"…and holds absolutely
still on his face for the final second"* — rather than letting the act run out mid-gesture.

An act with a designed hold also ends better as *drama*. Films breathe at act ends anyway; the
technical constraint and the craft agree here, which is rare and worth exploiting.

---

## 5. The handshake — describe the seam from both sides

Bind the seed twice, in words, from both directions:

- **Act N's prompt**: final beat describes the held frame explicitly.
- **Act N+1's prompt**: opens with *"The shot begins on exactly the supplied first frame and
  continues seamlessly from that instant: [same description, same nouns]."*

Use **identical vocabulary** on both sides — same nouns for costume, props, light and framing.
Paraphrase between the two sides is a second source of drift on top of the re-render itself.

---

## 6. Audio seams

Picture is only half the join, and audio discontinuity is often the more noticeable failure — native
generated ambience does not match across calls, so the room tone changes at every seam.

- **Never let a line of dialogue straddle a seam.** Voice render differs per generation; a line cut
  in half will never match. Land every line wholly inside one act and leave the seam clean.
- **Mask the seam with a transient.** A door slam, gunshot, thunderclap, hard impact or an abrupt
  silence placed *at* the cut hides an ambience mismatch the way motion hides a picture cut. This is
  the audio counterpart of cutting on action — and unlike picture, here the trick still works.
- **Prefer seams where the soundscape is already changing** — leaving a room, surfacing from water,
  a machine powering down. A scene that is *supposed* to change acoustically absorbs the mismatch.
- Fix what remains in the mix, not by regenerating: a shared ambience bed laid across all acts, or a
  short crossfade on the ambience stem alone, removes seam artefacts for a fraction of the cost.

---

## 7. When no good seam exists — five escape hatches

Ranked cheapest and most reliable first.

1. **Cut away to an object.** If the story wants the seam on a character moment, end on the thing
   instead — the backpack in the moss, the hand on the glass, the indicator light. Objects drift far
   less than faces, and an insert is almost always available.
2. **Cut to black.** A beat of black at the seam absorbs any discontinuity completely. Cheap,
   invisible, and it reads as a deliberate act break. Do not overuse or the film becomes chapters.
3. **Transient mask** (§6) — sell the join on sound when the picture join is imperfect.
4. **Cross-dissolve 2–3 frames in post.** Verified to work at the measured drift level. Trim the
   incoming clip by 2 frames and dissolve 3. Costs nothing, no regeneration.
5. **Deliberate motion-to-motion match.** End on motion *and* open the next act on motion in the
   **same direction and speed** — a whip pan out, a whip pan in. The mismatch hides inside blur.
   This is the one case where the §1 inversion is suspended, and it only works when both sides are
   designed for it together. Never fall into it by accident.

---

## 8. Thirty seconds is a ceiling, not a grid

`ceil(runtime ÷ 30)` gives you a **count**, never the boundaries. Acts do not have to be equal, and
uniform 30 s blocks are almost always the wrong answer — they place seams by arithmetic in a film
whose seams should be placed by story.

- If the seam wants to be at 0:24, **make the act 24 s.** Shorter acts also generate faster and cost
  less, so following the story is cheaper than fighting it.
- If a beat genuinely needs 34 s it must split — but split it at its own internal hold, not at 30.0.
- Prefer **fewer, longer acts** where the material allows: every seam is a risk, and the cheapest
  seam is the one you never create. Beat capacity scales with duration, so a single 30 s act
  carrying seven beats is safer than two 15 s acts carrying three and four.

---

## 9. Keep a seam ledger

One table per project, updated as acts land. It turns continuity from a vibe into a record:

| Seam | Frame chosen | Why | Type | Measured Δ | Fix applied |
|---|---|---|---|---|---|
| 1→2 | face CU, still, wet | designed hold | workable | 7.6 % | none, hard cut |

Measure it — it takes one command:

```bash
ffmpeg -sseof -0.08 -i actN.mp4 -update 1 -frames:v 1 a.png
ffmpeg -i actN1.mp4 -frames:v 1 b.png
python -c "from PIL import Image,ImageChops;a=Image.open('a.png').convert('RGB');b=Image.open('b.png').convert('RGB').resize(a.size);d=ImageChops.difference(a,b);import statistics;print(sum(sum(p) for p in d.getdata())/(a.width*a.height*3))"
```

Working rubric from the one seam measured so far — treat as provisional, and update the ledger as
the sample grows:

- **< 5 %** — effectively invisible on a hard cut.
- **5–10 %** — reads as continuous at 24 fps; do not claim frame-identical.
- **> 10 %** — visible. Apply an escape hatch rather than shipping it.
