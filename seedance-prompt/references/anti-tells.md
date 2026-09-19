# Anti-tells and the negatives policy

The generated-video look is not one flaw, it is a stack of about a dozen defaults. Each has a
specific verbal fix. Run this as a pre-flight pass over a finished prompt.

## The negatives policy

The official BytePlus guide says: positive phrasing only, negatives reserved for subtitles and
audio. Both library exemplars use negatives heavily and shipped good work. The reconciliation, and
the rule to actually follow:

**1. Every negative is preceded by the positive that replaces it.**
The positive does the work; the exclusion narrows the prior. A bare negative is a coin flip.

> `matte, lived-in. NOT waxy/plastic/airbrushed/CGI/doll`
> `4K photorealistic, large-format 65mm film look, real grain + halation … NOT 3D/game/cartoon.`

**2. Negatives may exclude a category, a material, or an object class. Never an event.**

| Works | Fails |
|---|---|
| `NOT 3D/game/cartoon` (category) | `the car does not crash` (event) |
| `NOT waxy/plastic/airbrushed` (material) | `she does not turn around` (event) |
| `NO harness/seatbelt/vest/straps on her torso` (object) | `nothing falls from the shelf` (event) |
| `no reticle, crosshair, scope ring, HUD, UI` (object class) | `the door never opens` (event) |

A model cannot render the absence of an event. Replace those with the physical thing that happens
instead — `but it never reaches her: the AP round punches through it just short` — see techniques
§5.4.

**3. When in doubt, use the counter-phrase.** Every avoidance has a positive twin that is strictly
safer:

| Avoid | Positive counter-phrase |
|---|---|
| slow motion | `real-time 24fps, 180° shutter`, `natural real-time motion speed throughout` |
| hazy AI glow | `clean air`, `matte highlights`, `natural halation around highlights only` |
| plastic skin | `visible pores, peach-fuzz, subsurface translucency, asymmetry, flyaway hairs; matte, lived-in` |
| dead face | `blinks naturally, forehead and brows active throughout` |
| dead-centre framing | `off-centre, non-symmetrical, spontaneous documentary framing` |
| teal-and-orange | accent doctrine with percentages and named sources |
| floaty drone move | `handheld`, `locked camera`, or a move with a stated motivation |
| lens-flare spam | `no artificial flares, no anamorphic streaks` after `natural halation` |
| morphing hands/faces | `smooth stable motion, no flicker, no warping, no morphing` |
| generic sci-fi HUD | `completely clean, no interface of any kind` + enumerate the graphics |
| weightless floating objects | a physics manifest, material by material, closing `nothing floats` |
| fisheye bulge on a wide | `environment visible to edges, straight rails rectilinear` |
| dutch tilt on an inside-an-object POV | `the framing is level and upright — no canted/tilted horizon` |
| invented print, logos, greebles | say it is plain: `an ordinary plain grey foil seal lid (no print)` |
| a second location appearing | `the location stays <plate>; no new place identity is added` |
| unrequested montage or cuts | `No invented cuts, no montage`, and per shot `no internal cuts` |
| every shot inheriting the plate's angle | `controls geography, materials, atmosphere and weather only, not camera angle` |
| a prop used the conventional way | anti-affordance clause: mechanism, why it matters, wrong reading named |

---

## Pre-flight checklist

Run top to bottom. Each line is a question about the prompt, not about the output.

**Motion**
- [ ] Is real-time speed stated explicitly? (Unsaid → drifts to slow motion.)
- [ ] Is the shutter stated? (`180° shutter` gives natural motion blur.)
- [ ] Does every camera move have a stated motivation? No motivation → lock the camera.
- [ ] Is each shot declared as a oner or as containing cuts? (`FORMAT MODE`)
- [ ] Is there a `HARD CUT.` token between shots in a multi-shot generation?
- [ ] Is montage explicitly ruled out at the piece level? (`No invented cuts, no montage`)
- [ ] Where two actions run together in one shot, is it marked `ONE CONTINUOUS UNCUT ACTION`?
- [ ] If slow motion is wanted anywhere, is it *allocated* (where, how much, return to real time)
      rather than banned or left open?

**Materiality**
- [ ] Is there a physics manifest covering every interaction in the piece?
- [ ] Does each material say how it behaves — what tears, pours, hinges, presses, settles?
- [ ] Does it close with `nothing floats`?
- [ ] For a oner, is physics run inline in the action timing, beat by beat, instead?
- [ ] Are non-standard world rules stated once as a law everything inherits?

**Faces**
- [ ] Blink + brow mandate present in the header?
- [ ] Repeated in each shot's action timing?
- [ ] Pore-level skin list present, with the exclusion tail?
- [ ] Shadow conditional present where half the face is dark? (`texture still readable`)
- [ ] If the look and the acting register disagree, is permission granted in words?

**Identity**
- [ ] Full identity string per character — height, hair, wardrobe head to toe **including feet**?
- [ ] One signature detail per character, marked `keep in every frame`?
- [ ] Signature detail re-stated per shot?
- [ ] Context variants written as deltas, not as second descriptions?
- [ ] Voice cast by register, not left neutral?

**Space**
- [ ] Metric size on everything sharing a frame with something else?
- [ ] Does the size travel with the noun at every mention, not just in the SCALE block?
- [ ] Geometry map present — positions, facings, eyelines, entrance vectors?
- [ ] For reverse angles: is a second plate bound as the opposite wall of the same room?
- [ ] Per-shot LOCATION MAP present?
- [ ] Is there room in frame for the event to happen in?

**Optics**
- [ ] Does each shot say what is sharp and what is not?
- [ ] Is a stop or DoF behaviour given, not just "shallow"?
- [ ] Is the FOV given **in degrees** and the camera distance **in metres**? (Neither alone
      determines the framing.)
- [ ] Is there a lens lock per segment with an anti-drift clause — or, for a oner, a focal rack
      with start FOV, end FOV, and the triggering event?
- [ ] Is every wide request paired with a rectilinear assertion naming a straight thing in frame?
- [ ] Where framing is tight but the camera should be far, is the optical cause stated with a
      number and the intended read?
- [ ] Is the wrong read named contrastively where a wrong read is likely?
- [ ] Does each shot have a `FIRST FRAME` block with x/y percentage bounding boxes?

**Light and colour**
- [ ] Every source named and motivated?
- [ ] Default sun removed if you do not want it? (`no sun`)
- [ ] Interior light bound to the exterior location plate?
- [ ] Colour given as percentage bands with named physical sources?

**Assets**
- [ ] Named semantic handles rather than positional `@Image N`?
- [ ] Does each asset say **which channels it controls** — and which it does not?
- [ ] Fidelity clause stated per asset? (`100% matches the reference`)
- [ ] Instance counts given where more than one exists?
- [ ] Are surfaces that should be plain stated as plain?
- [ ] Behaviour lock on any prop whose conventional use differs from yours?

**Structure**
- [ ] A plain-prose `SCENE CONTEXT` paragraph at the very top, before any technical block?
- [ ] Constants all above the shots, variables all below?
- [ ] Locks recap as a closing paragraph, bracketing the piece?
- [ ] Global rules that need a local break written as *scoped exceptions*, not as contradictions?
- [ ] LOCKS block present and short?
- [ ] Redundancy budget spent on exactly one constraint per shot, across different sections?
- [ ] CAPS reserved for must-survive constraints only?
- [ ] Overall-requirements tail closing the prompt?

**Sound**
- [ ] Dialogue policy decided at the top — words or non-verbal?
- [ ] If non-verbal, is the vocal texture specified per character?
- [ ] Delivery notes attached to each line?
- [ ] Pause marks (ellipses) inside lines that need timing?
- [ ] Subtitles policy stated?
- [ ] Audio notation correct — `{}` dialogue, `<>` SFX, `()` music, `【】` subtitles?

**Timeline**
- [ ] Integer seconds, continuous, no gaps? (Half-seconds are attested in a shipped 10 s oner with
      six camera beats — see `../library/005-mecha-vs-bug-oner.md`. Prefer integers where the
      duration allows; do not "fix" a working prompt to match the guide.)
- [ ] Roughly one beat per 2–4 s?
- [ ] Not more beats than the duration can hold? (7 beats hold across 30 s; 4 in 15 s can drop one.)

---

## Reading the output

When a generation comes back wrong, diagnose before re-rolling — a re-roll costs a full generation
and usually reproduces the same failure, because the same prompt has the same hole in it.

1. **Was the constraint in the prompt at all?** Most "the model ignored me" is "I said it once, in
   one section, in film jargon."
2. **Was it stated as a physical cause or as a film term?** Jargon fails silently; physics does not.
   `locked-on shot` → `the runner stays pinned dead-centre while the street blurs past`.
3. **Did something else in the prompt contradict it?** Check header vs. shot block — the shot block
   usually wins.
4. **Is it a geometry or camera-path constraint?** Prose cannot hold camera geometry through a shot
   that reveals an environment. Stop arguing in words and hand it a `start_image` plate — see the
   keyframe law in `../one-prompt-film/references/continuity.md`.
5. **Is it a dropped beat?** That is a density problem, not a comprehension problem. Lengthen the
   range or merge beats.
