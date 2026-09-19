# Continuity — plates, elements, and chaining acts

## 0. The law: keyframe-first control

**A video model re-animates what the still already decided.** Whatever the first frame establishes —
camera position, lens height, subject orientation, world design — the generation inherits and
mostly obeys. Whatever exists only in prose is a suggestion the model may overrule.

This is not a style preference. It is the single highest-leverage fact in the pipeline:

> When a shot must obey a hard constraint, **do not argue with prose — hand it a plate.**

**Verified failure (Duke's Big Chill, Act 1).** The brief demanded a locked overhead camera in
capitals. It was written as a dedicated camera-rule paragraph, restated inside every beat, and
repeated in the overall requirements. Seedance broke it and cut to a frontal wide **three times
out of three** — in a 15 s chained attempt and again in a 30 s single take. It was fixed on the
first try by generating one unambiguous overhead plate (floor filling frame, every object seen from
its top surface) and passing it as `start_image`. Prose lost three times; the plate won immediately.

Corollary: when a generation disobeys a constraint, the fix is almost never a stronger sentence.
Ask *"what still would make this unambiguous?"* and generate that instead.

---

## 1. Plate types

Build these **before** spending on video. Images are cheap and verifiable; video is neither.

| Plate | Purpose | Model | Notes |
|---|---|---|---|
| **Character sheet** | identity anchor | `nano_banana_2` 4k | turnaround + expressions; register as an Element |
| **World plate** | one per region/location | `nano_banana_2` 4k | same architecture, new area, per act |
| **Prop / creature plate** | recurring object or antagonist | `nano_banana_2` 4k | multi-view, plain dark background |
| **Geometry plate** | to force a camera the prose can't hold | `nano_banana_2` 2k | used as `start_image`, not `image_references` |
| **Storyboard** | shot-selection contract | `gpt_image_2` 4k `high` | typography model — see [storyboard.md](storyboard.md) |

**Never put a human figure in a plate that only needs environment or geometry.** It costs nothing
to omit and it avoids moderation rejections.

### Character sheet → Element
Build the sheet from whatever reference exists (real photos, storyboard panel crops, prior frames),
then register it once as a reusable Element via `show_reference_elements action=create`. From then
on it is one id, reusable across every act, and it never has to be re-derived. Follow the
`character-sheet` workflow (`get_workflow_instructions`) for the sheet prompt itself.

### World plates — one per region
A single "world" reference is not enough for a multi-act story: every act wants a **new place that
is recognisably the same world**. Generate one plate per region holding the world's *architecture*
constant while changing the *content* (forest vs. meadow vs. ruin). Describe the architecture in
identical language each time; vary only the inhabitants, structures and light.

---

## 2. Identity strings

Write the character, world and key-object descriptions **once**, then paste them **verbatim** into
every prompt that needs them. Do not paraphrase between shots — paraphrase is how drift starts.

Keep each string to the traits a model can actually hold: silhouette, hair, facial structure,
one or two costume specifics, and one memorable prop. Twenty adjectives dilute; six survive.

> Duke: *matted dark-brown corkscrew curls to the jaw, unkempt four-week beard with grey flecks,
> gaunt weathered sun-damaged face, deep-set hazel-brown eyes, lean wiry build, filthy olive canvas
> work jacket.* Plus one signature prop — a battered olive backpack with a yellow smiley keychain —
> which is what an audience actually tracks between acts.

Bind plates to roles explicitly and by upload order: `@Image1 is Duke… @Image2 is the robot…
@Image3 is the world…`. Unbound references get averaged into mush.

---

## 3. Chaining acts

To continue Act N+1 from Act N:

```bash
ffmpeg -sseof -0.08 -i actN.mp4 -update 1 -frames:v 1 -q:v 2 lastframe.jpg
```

Upload it and pass as `start_image`, keeping the character/world plates as `image_references`.
Open the prompt with *"The shot begins on exactly the supplied first frame and continues
seamlessly from that instant: [describe the frame]."*

**`start_image` is a strong reference, not a literal first frame.** Seedance re-renders it.
Measured on Duke: **7.6 % mean per-channel delta** between Act 1's last frame and Act 2's first.
Pose, lighting, props, costume and framing carried; scale and face shape drifted slightly. On a hard
cut at 24 fps that reads as continuous — but never promise a frame-identical join. If it must be
invisible, trim 2 frames off the incoming clip and cross-dissolve 3.

**Always pull the chain frame from the UNGRADED master.** Chaining from a graded frame bakes the
LUT into the next act's source, and the finishing pass then applies it twice.

---

## 4. Order of operations

```
story → board (approve) → plates (verify by eye) → video → grade
```

Each stage is cheaper than the next and constrains it. A bad board wastes a plate; a bad plate
wastes a generation; a bad generation wastes an hour of queue. Verify at every step — look at the
image, do not assume it.

The grade is **one pass at the end, applied identically to every act** from a single baked `.cube`,
so the acts match. Never grade per-act by eye.
