# 005 — Mecha vs bug, through-the-body oner (~10 s, one unbroken take)

**Shape:** single generation, ONE continuous take, six numbered camera beats, no cuts
**Assets:** 4, all with **named semantic handles** rather than positional numbers
**Register:** photoreal kinetic action, run-and-gun handheld, environmental SFX only, no face in frame

The action counterpart to [004](004-noodle-prep-five-segments.md). Where 004 locks a lens per
segment, this one **animates** the lens across a single take and says exactly when.

## What it taught

New to the catalog when ingested:

- **Named asset handles** (techniques §1.8) — `@zero_mecha`, `@STVOL`, `@bug_22`,
  `@location_scene_1`. Semantic, self-documenting, order-independent. This retires the
  per-submission renumbering problem that `@Image N` creates across a shot series. **Adopted as
  house default.**
- **Behaviour lock on a prop** (§1.9) — `Weapon behaviour: @STVOL fires ONLY in fast full-auto
  bursts … never single deliberate shots.` A block for how an object *behaves*, separate from what
  it looks like.
- **Anti-affordance clause** (§1.10) — the model's prior is "gun = held in hand". The prompt states
  the mechanism, why it matters, and the wrong reading: `The hand stays FREE below the barrel, so
  the same arm can grip an enemy while the barrel fires … NEVER held as a pistol.`
- **Absolute colour rule with enumerated instances** (§4.7) — `ALL BLOOD IS DARK PURPLE, every drop,
  every splatter, every smear - never red.` The enumeration is what makes it hold.
- **Accent band bound to the subject** (§4.2a) — `~20% mint/teal accent (@zero_mecha panels - the
  mecha is the subject)`. The palette serves the composition instead of floating free.
- **Focal rack as an animated curve** (§3.10) — `~80 degree wide for the opening; … racks from ~70
  degrees to ~110 degree wide rectilinear; it settles ~55-60 degrees, low`. Degrees plus the
  trigger moment for each change.
- **Numbered camera beats inside one take** (§3.11) — six numbered events choreographing a oner.
  This is how you direct a continuous shot without an edit to hang structure on.
- **Scoped slow-motion allocation** (§4.5a) — rather than banning slow-mo, spend it precisely:
  `mostly real-time 24fps with ONE very slight, almost imperceptible slow-motion touch during the
  pass through the bug's interior, then back to real time`, restated in three blocks.
- **Detail level raised for one moment** (§6.12) — `Inside the bug, the flesh is rendered in maximal
  detail`, declared in TEXTURE, because the camera goes somewhere it normally would not.
- **Declared absence with a diegetic reason** (§5.7) — `No human face in frame (pilot in cockpit).`
  Prevents face invention and sidesteps Seedance's real-face moderation in one clause.
- **Instance count on an asset** (§1.11) — `Two appear across this beat.`
- **Arrow-chain shot title** (§6.13) — `OVER-THE-ARMS OPENING -> BLAST ONE BIG HOLE -> FLY THROUGH
  (TEARING FLESH) -> TURN TO REVEAL MECHA -> KILL LEAPING BUG 2 INTO LENS / EXTERIOR`. The whole
  structure of a oner in one scannable line.
- **`nothing floats`** (§8.4) — the most compact anti-CGI clause in the corpus, closing a
  beat-by-beat physics run-down inside ACTION TIMING.

## Recorded contradiction — decimal timestamps

The official BytePlus guide requires **integer** seconds on the timeline. This prompt uses halves:
`0-2.5s`, `2.5-6.0s`, `6.0-7.5s`, `7.5-10.0s`. Across a 10 s oner with six camera beats, integer
granularity cannot express the structure. Recorded rather than resolved: prefer integers where the
duration allows, and treat halves as available when a short piece needs sub-second beat placement.
Do not silently "fix" a working prompt to match the guide.

## Notes and cautions

- The physics run-down lives **inside ACTION TIMING**, tied beat by beat, rather than in a separate
  block as in 004. Both work. The separate block is better for a multi-segment piece; the inline
  version is better for a oner, where physics and timing are the same axis.
- `FIRST FRAME (locked)` — the word *locked* is worth keeping.
- Note what is *not* here: no identity string with height and wardrobe, because the only "character"
  is a machine and a creature, both covered by fidelity clauses. Asset blocks scale down when the
  subject is not human.
- The camera passes through the interior of a creature — the one shot in the whole corpus that
  genuinely could not be plated. When geometry is impossible to plate, this level of optical
  specification is the substitute.

---

## Source prompt

```
Style: 8K IMAX, photorealism. Real organic film grain and halation. Shot on large-format film. High dynamic range. NOT a 3D render, NOT a game engine, NOT game-cutscene aesthetic, NOT a cartoon.

OPERATING STYLE - HOYTE VAN HOYTEMA: large-scale realism with intimate handheld closeness, immersive in-camera feel, tactile real-world textures, atmospheric haze and volumetric light, photochemical look.

Light: only natural motivated light - a soft overcast daylight key from the open sky, faithful desaturated tones, gentle roll-off, no heavy grade. No artificial film fixtures, no fabricated glow; any in-frame source is practical and diegetic. Expose for the real scene, let shadows fall naturally.

Colour - ACCENT DOCTRINE: ~70% cold desaturated grey-blue base (overcast sky, aged concrete, dust) + ~20% mint/teal accent (@zero_mecha panels - the mecha is the subject) + ~10% purple counter-note. ALL BLOOD IS DARK PURPLE, every drop, every splatter, every smear - never red.

Texture: matte non-reflective real surfaces, lived-in worn materials (aged concrete, scorched steel, dust, cracked asphalt, dented mecha plating, wet chitin), organic 65mm film grain, no digital gloss, no plastic sheen. Inside the bug, the flesh is rendered in maximal detail - wet membranes, fibrous tissue, glistening veins, ragged torn chitin.

Camera/Optics: large-format 65mm spherical prime, natural motion blur at a 180-degree shutter; large-format depth of field with creamy focus falloff, natural halation around highlights, subtle lens breathing. No artificial flares, no anamorphic streaks. An in-shot focal-length change (focal rack) happens during the pass through the bug. The camera is bold and very kinetic: live handheld shake throughout, plus aggressive in-lens zooms - snap zooms and crash zooms that punch in and pull out - all physically grounded with real rig weight.

Continuity: this is filmed as ONE single unbroken continuous take, one rolling camera from the first frame to the last; everything happens inside that one shot, the camera keeps moving the whole way through.

Weapon behaviour: @STVOL fires ONLY in fast full-auto bursts - an Uzi-like rapid cyclic rate, short ripping bursts, never single deliberate shots.

Acting: any living creature reads as alive - the enemy is aggressive and reactive, never a static prop.

Composition: spontaneous documentary framing; off-centre, non-symmetrical compositions welcome.

Technical: smooth stable motion, 8K, no flicker, no warping, no morphing; mostly real-time 24fps with ONE very slight, almost imperceptible slow-motion touch during the pass through the bug's interior, then back to real time.

Audio: environmental SFX only - bug shrieks and chittering, fast full-auto gun bursts (Uzi-like), wet flesh penetration and tearing, dark-blood spatter, heavy mecha servos and a fast pivot, a heavy body impact on the lens, settling debris, low wind ambience. No music. No subtitles. No on-screen text or watermarks.

ASSETS

@zero_mecha = ZERO'S MECHA - angular, least-armoured but most advanced frame; bright, agile, light. White / light-grey body, dark-steel joints, mint/teal accent panels. Genuinely heavy machine, clearly taller than the bug - real inertia, ground impact, settling suspension; never floats. 100% matches the reference.

@STVOL = ZERO'S WEAPON - a FOREARM-MOUNTED gun: a thick ribbed gunmetal barrel running along the top of the forearm, integrated into the arm armour (one per arm), worn steel barrel in a white/grey housing. The hand stays FREE below the barrel, so the same arm can grip an enemy while the barrel fires. Fired from the forearm in fast full-auto bursts (Uzi-like), NEVER held as a pistol. 100% matches the reference.

@bug_22 = ENEMY BUG - ~2.5-3 m spider-like creature, stone-grey chitin, glowing purple veins, many clawed legs, wide fanged pincers. Alive, aggressive, fast. Bleeds DARK PURPLE blood. Two appear across this beat.

@location_scene_1 = LOCATION + LIGHTING - a ruined city: destroyed mixed-architecture streets, Soviet brutalist blocks, faded Asian shop signs, burnt-out cars and heavy debris, deep street-level shadow, dust and cold haze drifting between buildings, overcast diffused daylight, dark and oppressive. Location and lighting reference @location_scene_1.

FORMAT: ONE SINGLE UNBROKEN CONTINUOUS TAKE, ~10s total, one rolling camera the whole way through, mostly real-time 24fps with one very slight slow-motion touch inside the bug.

SHOT - OVER-THE-ARMS OPENING -> BLAST ONE BIG HOLE -> FLY THROUGH (TEARING FLESH) -> TURN TO REVEAL MECHA -> KILL LEAPING BUG 2 INTO LENS / EXTERIOR.

FIRST FRAME (locked)

Camera rides just behind @zero_mecha's forearms, looking out over them down a wide wet ruined street. Lower-left: one mecha hand clamps @bug_22, holding it out. Screen-right: the other forearm reaches into frame, the ribbed @STVOL barrel aimed point-blank at the bug's horned, fanged face. @bug_22 is center-left, facing the gun. Behind them a wide rain-slick avenue of @location_scene_1 - burnt-out cars, debris, cold haze, overcast sky.

LOCATION MAP

One rolling camera, single unbroken take. From the over-the-arms opening, after the big hole is blown open the camera drives into that hole, through the body, and out the far side; it then turns to reveal @zero_mecha standing wide in the ruined street (low angle, the slumped first @bug_22 carcass in the FG). A second @bug_22 leaps in at the mecha from behind; she kills it and the carcass is flung toward the lens. Ruined city street of @location_scene_1 and cold haze fill the BG throughout.

OPTICS

Large-format 65mm spherical with an in-shot focal rack: ~80 degree wide for the over-the-arms opening (both arms and the bug in frame, street readable behind); as the camera enters the big hole and travels through the interior the focal length racks from ~70 degrees to ~110 degree wide rectilinear; it settles ~55-60 degrees, low, as it turns onto the mecha and the second bug. Natural halation, organic grain.

CAMERA

ONE rolling camera, no stops, with live handheld shake the whole way through and aggressive in-lens zooms: (1) riding behind the mecha's forearms on the grip-and-fire, a snap zoom punching in onto the bug's face as the gun levels; (2) a committed straight drive plus crash-zoom into the one big hole; (3) a glide through the wet interior with a very slight slow-motion touch while the focal length racks; (4) a fast whip and zoom-out as it bursts out the far side; (5) a turn that reveals the mecha low and wide in the street, a quick zoom-out to take in the full frame; (6) it stays raw, shaky, run-and-gun ACTION handheld - jolting with each burst and with the mecha's move, snap-zooming on the action - as she kills the leaping second bug, then the carcass rushes and slams the lens. Real operator motion only, no morphing.

ACTION TIMING

0-2.5s (real time): over-the-arms opening - @zero_mecha's hand clamps @bug_22 as it thrashes and the other forearm @STVOL, reaching in from screen-right, presses to one point on the bug's face and rips a fast Uzi-like burst into that single spot, blasting open ONE big hole, DARK-PURPLE blood spraying onto the lens; a snap zoom punches in. 2.5-6.0s (very slight slow-motion + focal rack, barely there): the camera crash-zooms and drives into the one big hole and flies through the bug; directly in front of the lens the flesh tears apart in MAXIMAL DETAIL - wet membranes, fibrous tissue, glistening purple veins, ragged chitin and purple-blood strings streaking past as the focal length racks wider. 6.0-7.5s (real time): the camera whips and zooms out the far side and turns to reveal @zero_mecha standing low and wide in the ruined street, the slumped first bug in the FG. 7.5-10.0s (real time, raw action handheld): a second @bug_22 leaps in at the mecha from behind; the camera goes shaky and kinetic, snap-zooming and jolting with each fast @STVOL burst as she kills it mid-air - dark-purple blood bursts and the carcass's momentum flings it straight into the camera, slamming across the lens. Physics: real creature weight fighting the grip, full-auto recoil through the forearm, the big hole punches through with real penetration, the interior flesh tears wet and heavy, the first body slumps with mass, the kill move carries real mecha mass, the dead second bug keeps real momentum into the lens; nothing floats. No human face in frame (pilot in cockpit).
```
