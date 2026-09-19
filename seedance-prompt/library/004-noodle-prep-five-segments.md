# 004 — Noodle prep on the mech (5 segments, one generation)

**Shape:** single generation, five segments joined by hard cuts, declared as a controlled sequence
**Assets:** 6 (1 mech, 1 pilot, 1 location, 2 props, 1 sub-assembly of the mech)
**Register:** photoreal overcast documentary, no dialogue, ends on a boil

Same world as [001](001-mech-sniper-ramen.md), but a far more *engineered* prompt. Where 001
directs, this one **specifies** — and it is the first exemplar in the corpus with a complete
optical and compositional geometry.

## What it taught

New to the catalog when ingested:

- **SCENE CONTEXT preamble** (techniques §6.8) — a plain-prose synopsis of the whole piece *before*
  any technical block. The model gets the arc before the constraints fragment it.
- **Frame coordinates** (§3.6) — `x 35%–70%, y 20%–85%`. Normalised bounding boxes for subject and
  background placement. The single most precise compositional device in the corpus.
- **LENS LOCK** (§3.7) — field of view in **degrees**, declared per segment, closing with
  `No lens drift mid-segment.` Degrees beat millimetres: focal length is meaningless without a
  sensor size, FOV is not.
- **Camera distance in metres** (§3.8) — `camera 2m behind the mech`, `camera ~0.8–1.2m from her`,
  `camera 3–4m reach`. FOV + distance fully determines the framing; nothing is left to inference.
- **FIRST FRAME as a named sub-block** (§Part B) — the opening composition separated from the
  camera move and from the action. The model anchors hardest on frame one; give it its own block.
- **PHYSICS block** (§8.4) — an inventory of mass and contact for every interaction in the piece.
  Generalises our physics clause from a *law* to a *manifest*.
- **Asset channel exclusion** (§8.3a) — `Controls geography, materials, atmosphere, and weather
  only` and `use the reference for geography… not for camera angle`. A location plate has a camera
  angle baked into it and will drag the shot toward it unless you say not to.
- **Fidelity clause** (§1.7) — `100% matches the reference`, stated per asset.
- **Specify the boring parts** (§6.9) — `an ordinary plain grey foil seal lid (no print)`. Left
  unspecified, the model decorates.
- **Rule with a scoped exception** (§4.6) — a global flat-overcast lighting law, then
  `Exception for Seg 2: …soft natural shadows fall across her face`. Better than contradicting
  yourself and hoping the local statement wins.
- **No internal cuts, per segment** (§6.10) — `ONE CONTINUOUS UNCUT ACTION … No internal cuts; the
  whole pour-and-fill is a single take.` Distinct from the piece-level FORMAT MODE.
- **Anti-fisheye clause** (§3.9) — `straight rails rectilinear`, `no fisheye curve`. Wide-angle
  prompts drift to fisheye.
- **Stage a reaction that proves the invisible** (§5.5) — steam is hard to read on screen, so she
  turns her face away from it. The flinch renders the vapour.
- **Emotion carried by physical business** (§5.6) — `licks her lips with hungry delight` rather
  than naming a mood and hoping.
- **POSITIVE LOCKS as a closing recap** (§6.11) — every critical constraint restated once at the
  very end, phrased as assertions.

## Notes and cautions

- **Lock placement diverges from 001.** 001 puts `LOCKS:` before the shots; this puts
  `POSITIVE LOCKS` after them. Both shipped. House rule adopted: identity, scale and geometry go
  **above** the shots because you cannot read the shots without them; the locks *recap* goes
  **below**, bracketing the piece (see §8.2).
- `no new place identity is added` is a phrase worth stealing verbatim — it names the exact failure
  (the model inventing a second location) better than "stay consistent".
- The lens plan is `84° / 84° / 84° / 29° / 29°` — two lenses across five segments, not five. A
  lens plan is a *restriction*, not a menu.
- Segment 2 is an inside-the-cup POV with `The framing is level and upright — no canted/tilted
  horizon` stated twice. POV-from-inside-an-object reliably produces a dutch tilt unless blocked.

---

## Source prompt

```
SCENE CONTEXT

On a fog-shrouded broken bridge above a dead grey city, a small 5-meter mecha sits slumped on its rear well back from the collapsed edge, legs stretched out forward toward the distant drop. Its pilot, a young woman, climbs up on top of the mech and cooks instant noodles using the mech's own battery heat — tearing open a noodle cup, pouring it into a steel jar, adding water, opening the battery compartment on the mech's back (steam rising out, she turns her face away from it), and setting the jar onto the hot battery, where it immediately boils. The video ends on the noodles boiling.

ACTIVE REFERENCES

@Image 1 — mecha. "Haru Min's Mecha": small, maneuverable humanoid mech, about 5 meters tall, white/grey panels with orange and yellow accents, exposed pistons and cabling, a front chest cockpit, retractable forearm blades. It has a battery compartment on its back, behind a hinged hatch. 100% matches the reference.

@Image 2 — pilot, Harumin. ~165cm young woman, short shaggy brown hair, a holographic strip patch across the bridge of her nose, yellow glossy long-sleeve crop top, khaki cargo pants, red lace-up boots. Energetic, playful, expressive. 100% matches the reference.

@Image 3 — location. A broken/collapsed cable-stayed bridge deck, wet cracked asphalt with lane lines, steel guardrails, dangling cables, ending at a torn drop-off; a foggy grey high-rise skyline fading into mist behind. Controls geography, materials, atmosphere, and weather only.

@Image 4 — "ZEZE" Korean cup ramen, red packaging with a chibi devil-girl mascot. The food being prepared. Its sealed top is an ordinary plain grey foil seal lid (no print).

@Image 5 — sage-green insulated stainless-steel food jar with a bare steel rim/interior. The cooking vessel.

@Image 6 — the mech's battery unit, inside the back compartment behind the hatch: a recessed bay with a battery carrying an orange label, warning markings, red cabling, faintly steaming/venting. The jar is set directly onto this @Image 6 battery.

FACIAL PERFORMANCE (pilot)

In every shot where @Image 2's face is visible, her face stays alive and joyful: she blinks naturally, licks her lips with hungry delight, and shows real forehead and brow micro-expression — eyebrows lifting, knitting, and relaxing, forehead subtly creasing. Her dominant expression is genuine happy anticipation of the meal. No frozen, blank, or mask-like face.

SCALE

The mecha is ~5 meters tall. The pilot (~165cm) sits astride on top of the seated mech's upper torso/shoulders while preparing the noodles, and stands on the mech's back directly in front of the battery compartment to open it.

LOCATION MAP

The mecha sits on the bridge deck several meters back from the broken edge, facing it — its extended legs and feet point north toward the torn drop-off and the misty skyline, but its body is set well back on solid deck. Wet asphalt and lane lines run forward past its feet to the edge; guardrails frame screen-left and screen-right; loose cables snake on the ground. Use the reference for geography, materials, atmosphere, and weather, not for camera angle.

FORMAT MODE

CONTROLLED MULTI-SHOT SEQUENCE — five segments joined by hard cuts, in order. Real-time motion. Every segment is handheld. Continuity locked: same foggy grey bridge, same flat overcast weather, same mecha and pilot, the steel jar and noodles carry through. Ends on the boil. No invented cuts, no montage.

CAMERA — GLOBAL

The entire piece is shot handheld — real operator breath, hand tremor, micro weight-shifts, small live reframes, documentary energy in every segment. No locked-off tripod shots, no gimbal float, no digital jitter.

LENS LOCK

SEGMENT 1 = 84° classic wide.

SEGMENT 2 = 84° classic wide (inside-cup POV).

SEGMENT 3 = 84° classic wide.

SEGMENT 4 = 29° short telephoto portrait.

SEGMENT 5 = 29° short telephoto portrait.

No lens drift mid-segment.

SEGMENT 1 — MECHA AT REST

First frame: low wide handheld shot from directly behind the mecha. @Image 1 sits on its rear on the wet asphalt, back to camera, x 35%–70%, y 20%–85%, its extended legs reaching away from camera toward the distant broken edge. The mech is set well back from the edge on solid deck; the torn drop-off and foggy skyline are far ahead in BG center, x 0%–100%, y 0%–40%. Guardrails lead the eye into depth.

Camera move: handheld slow push-in from directly behind the mecha, following its eyeline toward the distant edge, gentle operator weight and breath, fog drifting through frame.

Optics: 84° classic wide, camera 2m behind the mech, environment visible to edges, straight rails rectilinear.

Action: the mecha sits still, faint steam venting from its back battery hatch seam; cables sway slightly in the wind.

HARD CUT to Segment 2.

SEGMENT 2 — POV FROM INSIDE THE NOODLE CUP

First frame: a handheld POV from inside the @Image 4 ZEZE cup, camera looking straight up and out through the sealed ordinary plain grey foil lid above; the interior cup walls frame the edges evenly, dim. The framing is level and upright — no canted/tilted horizon.

Camera move: handheld level low inside-the-cup view with a faint live wobble, staying upright; as the grey foil lid peels back, the pale grey daylight fills in and reveals @Image 2's face above, looking down into the cup.

Optics: 84° classic wide, camera at the bottom of the cup looking up, her face centered in the opening, slight wide presence, no fisheye curve, level framing.

Action: the ordinary grey foil lid tears and folds back; @Image 2 looks down into the cup and licks her lips with joyful hungry delight, blinking and lifting her eyebrows, forehead creasing. As she leans over the opening, soft shadows fall across her face — her hair and her own form casting gentle shadow over her features in the grey light.

HARD CUT to Segment 3.

SEGMENT 3 — POURING & WATER, ASTRIDE THE MECH (CLOSE-UP, HANDHELD, WIDE, ONE CONTINUOUS ACTION)

First frame: a handheld close-up of @Image 2 sitting astride on top of the mech, x 30%–70%, y 5%–95%, her face and hands tight in frame with the @Image 4 cup and the open @Image 5 sage-green steel jar at chest height; the mech's panels and the foggy bridge soft behind/below her.

Camera move: handheld wide-angle, close to her, alive with operator breath, hand tremor, micro weight-shifts and small reframes.

Optics: 84° classic wide-angle lens character, camera ~0.8–1.2m from her, strong close foreground presence, the mech and environment visible around her to the frame edges, straight lines rectilinear, no fisheye.

Action: ONE CONTINUOUS UNCUT ACTION — perched on top of the mech, she first pours out everything from the @Image 4 noodle package (the dry noodle block and red seasoning) into the @Image 5 jar, then in the same shot reaches off to the side for a plastic water bottle, brings it back, and pours water over the noodles, blinking and smiling with eager joyful anticipation, brows lifting. No internal cuts; the whole pour-and-fill is a single take.

HARD CUT to Segment 4.

SEGMENT 4 — LOW ANGLE FROM BELOW: STANDING AT THE COMPARTMENT, OPENING IT, STEAM, SHE TURNS AWAY

First frame: a handheld low-angle shot from below, looking up at @Image 2 as she stands on the mech's back directly in front of the @Image 6 battery compartment, facing it square-on, x 25%–75%, y 0%–95%; the @Image 5 jar in one hand, the closed hatch in front of her.

Camera move: handheld, low angle from below looking up at her, alive with breath and small reframes.

Optics: 29° short telephoto portrait, camera 3–4m reach, her face and upper body razor-sharp, background softly compressed into the grey fog.

Action: standing squarely in front of the compartment (not reaching over her shoulder), she opens the battery hatch directly; steam rises out toward her, and she blinks and simply turns her face away from it, brows lifting and forehead creasing, leaning her head aside out of the vapor. Then she faces back and carefully lowers the @Image 5 jar onto the hot @Image 6 battery.

HARD CUT to Segment 5.

SEGMENT 5 — CLOSE: THE JAR ON THE HOT BATTERY, IT BOILS (FINAL)

First frame: a handheld close shot on the open @Image 6 back battery bay, x 35%–75%, y 25%–80%, the hot battery with its orange label and red cabling exposed and steaming; the @Image 5 jar settling onto it.

Camera move: handheld close, small live push-in, settling onto the battery for the ending.

Optics: 29° short telephoto portrait, camera 3–4m reach, the battery and jar razor-sharp, background softly compressed.

Action: the @Image 5 jar sits snug on the hot @Image 6 battery. The moment it settles, the broth immediately begins to boil — the noodles roll in a fast rolling boil, steam billowing up, broth turning deep red. The shot holds on the boiling jar and ends here.

PHYSICS

Real mass and contact throughout — the seated 5-meter mech's weight presses the asphalt, cables hang with gravity and sway in wind, the mech barely shifts under the pilot's small weight on top. Foil lid tears with thin metallic resistance; dry noodle block drops with light weight; water glugs and pours with surface tension, splashing slightly. The steel jar has real heft. The back hatch swings up on its hinge with weight; steam vents in a real soft burst toward her face, stirring her hair, then rises and curls, denser as the broth boils; bubbles roll and break at the surface; condensation beads on the steel rim. Fog drifts in slow volumetric layers across all shots.

LIGHTING

Flat, diffuse, fog-filtered overcast light exactly like the @Image 3 reference — no sun, no visible sun, no directional key, no warm light anywhere. Even cool grey ambient light coming softly from the whole misted sky. Heavy desaturated grey-blue palette — wet asphalt, grey skyline, white mech, all under a pale flat haze. Faces and the yellow top stay readable in the soft grey light, gentle shadowless rolloff, no crushed black. Exception for Seg 2: as she leans over the cup to open it, soft natural shadows fall across her face from her hair and her own form, giving her face shape and depth (still cool and overcast, just gently shadowed). The battery steam is the only faint warmth, reading as luminous pale vapor against the cold fog. Damp, cold, overcast weather throughout.

AUDIO

No dialogue. Low foggy wind across the bridge, distant muffled city ambience, faint creak and servo-tick from the resting mech, the thin metallic crinkle of the foil lid tearing, the glug of pouring water, a metallic clunk and a soft steam hiss as the back hatch opens, and a rising bubbling as the noodles boil into the final beat. Optional light playful music sting at the boil. No subtitles.

POSITIVE LOCKS

Only @Image 2 (the pilot) and @Image 1 (the mecha) are present — no other characters. The mech is ~5 meters tall and stays seated on its rear, set well back from the broken edge with its extended legs and feet pointing toward the distant edge. The pilot prepares the noodles astride on top of the mech (Seg 3) and stands directly in front of the back compartment to open it (Seg 4), not reaching over her shoulder. She stays joyful, blinks, and licks her lips with live forehead/brow micro-expression whenever her face is visible. The @Image 4 cup lid is an ordinary plain grey foil seal, the inside-cup POV (Seg 2) is level/upright, and soft shadows fall on her face as she opens the package. The @Image 6 battery compartment is on the mech's back. Every segment is handheld. Segment 4 is shot from below; Segment 5 ends on the boiling noodles. The weather stays flat foggy overcast with no sun, matching @Image 3. The location stays the @Image 3 foggy broken bridge; no new place identity is added.
```
