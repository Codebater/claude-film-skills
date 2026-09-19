---
name: seedance-prompt
description: >
  Write, review, or repair a production-grade Seedance 2.5 video prompt using the house
  production dialect learned from real shipped productions — the block schema (bible header,
  asset legend, LOCKS, scale, geometry map, per-shot LOCATION MAP / FORMAT MODE / OPTICS /
  CAMERA / ACTION TIMING), the named technique catalog, and the anti-tell rules that kill
  the frozen-face, waxy-skin, slow-mo, dead-center, wrong-scale AI look. Use whenever the
  task is the prompt text itself: "write a Seedance prompt", "improve this prompt", "why did
  my generation come out wrong", "keep this character consistent across shots", "make it look
  really cinematic / like real film", or when composing the prompt step of one-prompt-film.
  Also use to ingest a new exemplar prompt into the library and distil what it teaches.
---

# Seedance Prompt Craft

The official BytePlus guide teaches the **grammar** (subject + action + scene + style + camera +
sound, timestamps, asset syntax). It does not teach the **dialect** that separates a prompt which
technically renders from one that produces a shot a viewer believes. This skill is that dialect,
distilled from shipped productions in [library/](library/).

Params, task types, API constraints, ratio/duration locks live in
[`../one-prompt-film/references/seedance-25.md`](../one-prompt-film/references/seedance-25.md) — do
not duplicate them here. Story, board and plate work live in `one-prompt-film` itself. This skill
owns **the words that go in the box**.

## The core claim

A video model does not fail at rendering. It fails at **holding things**. It drops the constraint
you stated once, invents scale it was never given, re-centres what you composed off-centre, freezes
the face between the two actions you named, and quietly slides into slow motion. A production
prompt is therefore organised not as a description but as a **hierarchy of things that must not
drift**, with the drift-prone ones stated first, stated physically, and stated more than once.

Everything below follows from that.

## Step 1 — Pick the shape

Two shapes, both valid. Decide before writing a word, because it changes the block order.

| Shape | When | Structure |
|---|---|---|
| **Single multi-shot generation** | ≤30 s total, shots share one location and lighting continuity, you want the model to carry continuity for you | One bible header, then `SHOT 1 … HARD CUT. SHOT 2 …` in one prompt, one submission |
| **Shot series under a shared bible** | Total exceeds 30 s, or each shot needs its own reference-asset set, or you want per-shot re-rolls without re-rolling the good ones | The **same bible header** pasted on top of every shot, each shot submitted alone, assembled in the edit |

The second is the professional default for anything with characters, because it lets you re-roll one
bad shot for the cost of one shot. Its whole trick is that **the header is identical every time** —
that is what keeps three separately-generated shots looking like one scene. Write the bible once to
a file; paste it, never retype it.

**Use named semantic handles, not positional numbers** — `@zero_mecha`, `@bug_22`,
`@location_scene_1`, not `@Image 1`. Positional numbers change with upload order, so a shot series
has to be renumbered by hand for every submission and the prose reads as coordinates. Named handles
are self-documenting inside the shot text (`the ribbed @STVOL barrel aimed point-blank`) and make
the whole bible portable. Keep one `HANDLE = description` block so the binding to upload order is
still stated explicitly, once.

## Step 2 — Write the bible header

Constants first, variables last. Nothing that changes between shots may appear up here. Full
block-by-block spec and a copy-paste template: [references/prompt-schema.md](references/prompt-schema.md).

```
SCENE CONTEXT    one plain-prose paragraph: what happens, in order, ending on the last image
GLOBAL STYLE     format, film stock/lens, DP name + decoded, grain/halation, 24fps real-time
LIGHT            every source named and motivated; exceptions scoped and bounded
COLOUR           accent doctrine with percentages (≈70/20/10), one band bound to the subject
TEXTURE          materials, matte vs gloss, raised detail for the one extreme moment
CAMERA/OPTICS    house lens behaviour
LENS LOCK        field of view in degrees per segment · no lens drift mid-segment
SKIN             pore-level list, then the exclusion
ACTING           blink + brow micro-expression, mandatory
COMPOSITION      off-centre doctrine
TECHNICAL        real-time 24fps, 180° shutter, no morphing; slow-mo allocated, not banned
AUDIO            dialogue policy, music policy, subtitle policy
BEHAVIOUR LOCK   how a key prop acts, and the wrong reading it must not fall into
ASSETS           named handles · identity string · channels controlled · fidelity clause
SCALE            metric size of every object that shares a frame with another
GEOMETRY / MAP   who is where, facing where, entering from where
FORMAT MODE      segments-and-cuts or one unbroken take · no invented cuts, no montage
PHYSICS          mass and contact for every interaction · nothing floats
———— shots ————
POSITIVE LOCKS   every critical constraint restated as an assertion, at the very end
```

Not every piece needs every block — a product spot needs no ACTING block. But **SCALE**,
**GEOMETRY**, **PHYSICS** and the **LOCKS** recap are needed far more often than they feel like
they are, and they are the ones almost always missing from an amateur prompt.

**Lock placement:** identity, scale and geometry go *above* the shots — you cannot read the shots
without them. The locks *recap* goes *below*. The same constraint at both ends of a prompt survives
better than the same constraint twice in the middle.

## Step 3 — Handle the six drift classes explicitly

These are the six things the model will not hold on its own. Each has a named handling in
[references/techniques.md](references/techniques.md); this is the checklist.

1. **Identity** — a character described as "a woman in a jacket" is a different woman every shot.
   Write a full identity string once (height in cm, hair shape *and* colour transition, wardrobe
   head to toe *including feet*, voice register) and reuse it verbatim. Give each character one
   **signature detail** that is trivially checkable by eye (`holographic glitter strip across the
   bridge of the nose — keep in every frame`) and re-state it per shot.
2. **Geometry** — write the top-down map as prose: positions, facings, eyelines, which side each
   entrance comes from. Without it, reverse angles invent a new room and screen direction flips
   across the cut. For a scene shot both ways, plate **both walls** and bind them as `main face` /
   `reverse face`.
3. **Scale** — give metric sizes, and give them **again at every mention**: `the @Image 3 5m mech`,
   `the @Image 6 2m monster`. Declared once at the top is not enough; the number must travel with
   the noun. Anchor to a human: `5 metres tall; Haru (~165cm) sits on its highest point`.
4. **Performance** — the frozen forehead is the single loudest AI tell. Command it away explicitly
   and per shot: *blinks naturally, forehead and brows active throughout*. Where the visual style
   and the acting register disagree (photoreal look, comedic playing), grant permission in words:
   *anime-comedic performance is allowed*.
5. **Optics** — state the *physical cause*, then the number, then the read. `Close-up` alone gets
   you a camera standing next to the subject. What you usually mean is
   `extreme super-telephoto compression (≈8° FOV), camera very far away … it reads as observed from
   a great distance, never like the camera is right next to her`. Systematised: give **field of
   view in degrees plus camera distance in metres** — together they fully determine the framing,
   and neither does alone. Lock the lens per segment (`No lens drift mid-segment`), or animate it
   across a oner with start FOV, end FOV and the triggering event.
6. **Materiality** — objects with no weight are the deepest cause of the CGI look, and it is
   invisible in a still. Write a **physics manifest**: mass and contact for every interaction,
   material by material — what tears with what resistance, what pours, what takes a hinge, what
   presses into the ground. Close it with `nothing floats`.

## Step 4 — Write the shots

Each shot gets its own labelled sub-blocks. The labels matter: they stop the model averaging
"where things are" together with "how it is shot" together with "what happens".

```
SHOT n — SHOT SIZE / (one-line intent, off-centre note, who is sharp)
  FIRST FRAME      the opening composition, with x/y % bounding boxes for subject and background
  LOCATION MAP     where everyone and everything is, what is behind, what is blurred
  FORMAT MODE      one continuous take, ~Ns, real-time, no cut · HARD CUT from Shot n-1
  OPTICS           FOV in degrees + camera distance in metres, what is sharp, rectilinear
  CAMERA           handheld or locked, size, what it follows, where focus is locked
  ACTION TIMING    0–Ns: beats, {dialogue with pause marks}, <SFX>, (music), blink/brow reminder
```

`FIRST FRAME` earns its own block because the model anchors hardest on frame one. Coordinate the
*start* of the shot, not every beat — the action moves from there. Mark it `FIRST FRAME (locked)`
for a oner, and number the camera's beats `(1) … (2) …` when there is no edit to carry structure.

Timeline rules from the official guide still apply inside `ACTION TIMING`: integer seconds, no
gaps, roughly one beat per 2–4 s. Beat capacity scales with duration — 7 beats hold across 30 s
where 4 beats in 15 s can silently drop one.

## Step 5 — Spend the redundancy budget

You get to over-state roughly **one thing per shot**. Pick the constraint most likely to lose, and
restate it in three to five *different sections in different words* — not the same sentence twice.
In library exemplar 002, "the background must be unreadable" appears in the shot header, the
LOCATION MAP, the OPTICS block, the CAMERA block and the ACTION TIMING line, phrased differently
each time. Everything else in that prompt is stated once.

Restating everything is not emphasis, it is noise, and it flattens the hierarchy built in Step 2.
If two constraints both feel like they need the budget, the shot is doing too much.

**ALL-CAPS is the priority channel.** Use it only for constraints that must survive — `ONLY`,
`NOT`, `COMPLETELY OUT-OF-FOCUS WASH`, `NEVER CENTRED`. Caps on ordinary description spends the
signal for nothing.

## Step 6 — Audit before spending

Run [references/anti-tells.md](references/anti-tells.md) as a checklist. The short form:

- Is every negative **preceded by the positive that replaces it**? (`matte, lived-in. NOT
  waxy/plastic/airbrushed/CGI/doll`) A bare negative is a coin flip; a positive with an exclusion
  tail is reliable.
- Are all negatives **category or object** exclusions, never **event** negations? "NO HUD" works.
  "The car does not crash" does not — a model cannot render the absence of an event.
- Is real-time speed stated? Left unsaid, generations drift to slow motion.
- Is every light **motivated by a named source**?
- Does anything share a frame with something else while lacking a metric size?
- Does each shot say what is sharp and what is not?
- Is the composition instruction fighting the centering prior, or silently accepting it?

Then show the user the prompt before the first paid call.

## Ingesting a new exemplar

When a strong prompt from a real production comes in:

1. Save it **verbatim** to `library/NNN-slug.md` under a `## Source prompt` heading — never edit
   the original, its exact wording is the evidence.
2. Under `## What it does that we do not`, list only the devices *not already* in
   `references/techniques.md`. Resist re-describing known technique.
3. Promote each genuinely new device into `references/techniques.md` as a named entry:
   **problem it solves → pattern → verbatim line from the source → exemplar id**.
4. If it contradicts something already in the references, say so in the entry rather than
   overwriting — a contradiction between two shipped productions is information, and the honest
   note ("official guide says positive-only; both exemplars use paired negatives") is more useful
   than a false consensus.
5. Update [library/README.md](library/README.md).

## Failure → fix

| Symptom | Mechanism | Fix |
|---|---|---|
| Character changes between shots | identity carried by adjective, not string | full identity string + signature detail, verbatim every shot |
| Reverse angle invents a new room | only one wall was ever plated | plate both faces, bind as main/reverse |
| Screen direction flips across a cut | no geometry map | write the top-down map as prose in the header |
| Object reads as toy or as giant | scale stated once, or not at all | metric size travelling with the noun at every mention |
| Faces look dead between actions | no performance instruction | blink + brow line in the header **and** each shot |
| Skin looks waxy | style block asked for "beautiful", not "textured" | pore-level positive list + exclusion tail |
| Camera is next to the subject instead of far away on a long lens | "close-up" taken literally | state the optical cause + FOV number + the read |
| Drifts into slow motion | speed never specified | `real-time 24fps, 180° shutter, no slow-mo` |
| Subject stuck dead centre | centering prior unopposed | `off-centre, never centred`, repeated |
| HUD / UI / reticles appear | sci-fi prior | `completely clean, no interface of any kind` + enumerate the specific graphics |
| Shots feel like one long move instead of an edit | no cut token | `HARD CUT.` between shots; `FORMAT MODE: one continuous take, no cut` inside them |
| Last beat missing | too many beats per second | lengthen the range or merge beats — do not re-roll blind |
| Everything floats; no weight anywhere | no physics manifest | mass and contact per interaction; `nothing floats` |
| Every shot looks like the reference plate | plate's baked-in camera angle inherited | asset channel *exclusion* — `controls geography, materials, atmosphere and weather only, not camera angle` |
| Wide shot bends into fisheye | wide request unopposed | pair with a rectilinear assertion naming a straight thing in frame |
| POV-from-inside-an-object comes out dutch-tilted | no level assertion | `framing is level and upright — no canted/tilted horizon` |
| Plain surfaces acquire print, logos, patterns | left unspecified | say explicitly that it is plain — `an ordinary plain grey foil seal lid (no print)` |
| A prop is used the conventional way, not your way | object-class affordance prior | anti-affordance clause: mechanism, why it matters, the wrong reading named |
| A cut appears inside a shot that should be uncut | two sequential actions in one shot | `ONE CONTINUOUS UNCUT ACTION … no internal cuts` |
| A second location appears | no location identity lock | `the location stays <plate>; no new place identity is added` |
| Steam / heat / wind renders as nothing | no reaction staged | give a character a physical reaction to it |
| A range described two setups; you got one | one range, two camera positions, no cut declared | split the range and declare the cut, or collapse both into one plated frame (techniques §3.12) |
| The joke's premise is not in frame | the element the gag depends on was prose, not composition | plate it — bake the gag into the still so nothing depends on the model electing to render it |
| Screens, UI or small type garble | model renders small copy badly | compose around it (`screens are never readable` + mechanisms + the reason), put real copy in post |
| Montage reads as a slideshow | cuts not motivated | hide every cut in a physical event, naming both ends of each transition |

## Commercials

Everything above still applies, plus [references/techniques.md](references/techniques.md) §9:
the product can be a recurring *motif* rather than a visible object; anything the model renders
badly (screens, UI, small type) gets composed around and added in post; music is tracked cue by cue
across the timeline and its **stop** is the payoff; a tonal turn flips genre, palette, camera
grammar and sound on the same frame; and the benefit lands as a change of expression on one face.
Judge the idea first with the commercial rubric in
[`../one-prompt-film/references/dramaturgy.md`](../one-prompt-film/references/dramaturgy.md).

## Library

Annotated exemplars and what each one taught: [library/README.md](library/README.md).

**When a generation comes back wrong, read
[library/006](library/006-fregio-everywhere-commercial.md) first** — it is the only entry carrying
the prompt, a frame from the failed output, the diagnosis and the fix plate together, and both of
its failure mechanisms (the keyframe law, beat overload) are the two most common in this corpus.
