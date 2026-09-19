# The production prompt schema

The canonical block order, why each block exists, and a fill-in template. Derived from the shipped
prompts in [../library/](../library/). Blocks are optional individually; the **order** is not —
constants above variables, and the drift-prone above the merely descriptive.

---

## Part A — the bible header (write once, paste on every shot)

### A0. Scene context

One plain-prose paragraph at the very top: what happens, in order, ending on the last image. No
jargon, no asset handles, no camera. The model gets the arc before the constraints fragment it.

```
SCENE CONTEXT

On a fog-shrouded broken bridge above a dead grey city, a small 5-meter mecha sits slumped on its
rear well back from the collapsed edge… Its pilot, a young woman, climbs up on top of the mech and
cooks instant noodles using the mech's own battery heat — tearing open a noodle cup, pouring it
into a steel jar, adding water, opening the battery compartment on the mech's back (steam rising
out, she turns her face away from it), and setting the jar onto the hot battery, where it
immediately boils. The video ends on the noodles boiling.
```

### A1. Asset legend

**Use named semantic handles, not positional numbers.** `@zero_mecha`, `@STVOL`, `@bug_22`,
`@location_scene_1` — self-documenting inside the shot prose, order-independent, and portable
across every shot of a series without renumbering. Keep one `HANDLE = description` block so the
binding to upload order is still explicit, stated once.

Each entry carries: what it is · the description · **which channels it controls** · the fidelity
clause.

```
ASSETS
@zero_mecha = ZERO'S MECHA - angular, least-armoured but most advanced frame… White / light-grey
body, dark-steel joints, mint/teal accent panels. Genuinely heavy machine, clearly taller than the
bug - real inertia, ground impact, settling suspension; never floats. 100% matches the reference.
@bug_22 = ENEMY BUG - ~2.5-3 m spider-like creature… Two appear across this beat.
@location_scene_1 = LOCATION + LIGHTING - a ruined city… Location and lighting reference
@location_scene_1.
```

**Channel exclusion matters as much as channel binding.** A location plate has a camera angle, a
lens and a composition baked into it, and it will drag every shot toward that angle unless you say
otherwise:

```
@Image 3 — location. A broken/collapsed cable-stayed bridge deck… Controls geography, materials,
atmosphere, and weather only.
```
> …and again in the location map: `Use the reference for geography, materials, atmosphere, and
> weather, not for camera angle.`

Other rules: never rely on text printed inside the image; state the fidelity requirement
(`100% matches the reference`); give instance counts where more than one exists; and say
explicitly when a surface is plain (`an ordinary plain grey foil seal lid (no print)`) — anything
unspecified gets decorated.

The compact middot form still works for a simple piece:

```
Tags: @Image 1 = Haru Min (pilot) · @Image 2 = Reina (sniper) · @Image 3 = Haru's mech
(seated rest-mode) · location @Image 5 = broken bridge
```

### A2. Global style

Format, film stock, lens family, grain behaviour, motion rate, and the category exclusion. Name the
DP if there is one — and then **decode the name**, because the name alone is compression that may
not survive.

```
4K photorealistic, large-format 65mm film look, real grain + halation, Hoyte van Hoytema —
foggy, atmospheric, shallow DoF, documentary handheld. Source-motivated cold natural light,
desaturated earthy palette, no sun, no heavy grade. Real-time 24fps, 180° shutter.
NOT 3D/game/cartoon.
```

```
OPERATING STYLE — HOYTE VAN HOYTEMA: large-scale realism with intimate handheld closeness,
immersive in-camera feel, tactile textures, atmospheric haze and volumetric light. Shallow depth
of field on the face, documentary framing, photochemical look.
```

### A3. Light

Every source named, every source motivated. No free-floating "cinematic lighting". Bind interior
light to the exterior location asset so cuts between them match.

```
Light: motivated natural light, one soft key, desaturated rich earthy colour, faithful skin
tones, soft roll-off, no heavy grade.
```

```
…cold foggy light of location @Image 5 only, warm ember glow on lips/fingers.
```

### A4. Colour — accent doctrine

Percentages, not adjectives. Three bands: dominant, accent, counter-note.

```
Colour — ACCENT DOCTRINE: ~70% desaturated green-grey room tone + raw concrete; ~20% warm
orange-yellow accent (warm daylight + warm ceiling-panel light through the camo netting);
~10% cool daylight blue as a counter-note from the windows.
```

Each band should name **where the colour comes from**, not just the hue. "20% warm orange" is a
wish; "20% warm orange from the ceiling panels through the camo netting" is a lighting plan.

### A5. Texture

```
Texture: matte non-reflective surfaces, lived-in worn materials (aged concrete, fabric, leather,
dust), organic 65mm film grain, no digital gloss, no plastic sheen.
```

### A6. Camera / optics doctrine

The house lens behaviour, separate from any one shot's framing.

```
Camera/Optics: large-format 65mm spherical prime, natural motion blur at a 180° shutter; shallow
large-format depth of field with creamy focus falloff, natural halation around highlights, subtle
lens breathing. No artificial flares, no anamorphic streaks.
```

### A6a. Lens lock

Field of view **in degrees**, assigned per segment, closed with an anti-drift clause. Degrees, not
millimetres — focal length is meaningless without a sensor size. A lens plan is a restriction, not
a menu: two focal lengths across five segments is a plan, five is a shrug.

```
LENS LOCK

SEGMENT 1 = 84° classic wide.
SEGMENT 2 = 84° classic wide (inside-cup POV).
SEGMENT 3 = 84° classic wide.
SEGMENT 4 = 29° short telephoto portrait.
SEGMENT 5 = 29° short telephoto portrait.

No lens drift mid-segment.
```

For a continuous take, animate it instead — start FOV, end FOV, and the event that triggers each
change:

```
~80 degree wide for the over-the-arms opening…; as the camera enters the big hole and travels
through the interior the focal length racks from ~70 degrees to ~110 degree wide rectilinear; it
settles ~55-60 degrees, low, as it turns onto the mecha and the second bug.
```

### A7. Skin

Positive list of what real skin has, then the exclusion tail. The conditional clause at the end is
the important part — it stops the model using shadow as an excuse to drop texture.

```
SKIN / REALISM (hardest on @Image 2): both women read as real photographed humans — visible
pores, peach-fuzz, subsurface translucency, asymmetry, true eye catchlights, flyaway hairs;
matte, lived-in. NOT waxy/plastic/airbrushed/CGI/doll. Half-face in shadow, texture still
readable.
```

Naming *which asset the problem is hardest on* focuses the constraint where it will actually fail.

### A8. Acting

Non-optional whenever a human face is on screen for more than a beat.

```
FACIAL PERFORMANCE (both): both blink naturally and show live forehead/brow micro-expression
(eyebrows lifting, knitting, relaxing, forehead creasing). No frozen, blank, or mask-like faces.
```

Where the visual register and the performance register disagree, grant permission explicitly:
`Anime-comedic performance is allowed.`

### A9. Composition

```
Composition: spontaneous documentary framing; off-centre, non-symmetrical compositions welcome —
never centred.
```

### A10. Technical

```
Technical: smooth stable motion, 8K, no flicker, no warping, no morphing; real-time 24fps,
no slow-mo.
```

### A11. Audio policy

Decide **whether there is dialogue at all** here, at the top, once. Choosing non-verbal is a
legitimate and often superior choice — it sidesteps lip-sync and synthetic-voice tells entirely,
and it must then be specified positively as vocal texture.

```
Vocals: non-verbal only (Reina's smoke-exhale + low hum; Haru's tiny "hmm… wow" + chewing).
NO words.
```

```
Audio: room ambience + diegetic dialogue. No music. No subtitles. No on-screen text or
watermarks.
```

Notation stays official: `{}` dialogue, `<>` SFX, `()` music, `【】` subtitles.

### A12. Assets — identity strings

One paragraph per character. Height in cm, hair shape *and* colour transition, wardrobe head to toe
**including feet**, signature detail, voice register. State context variants inline in parentheses.

```
@Image 4 = REINA — 183cm, Korean features; black hair with light-brown ends, wet-look mid-length
shag, ragged side-swept fringe; heavy smoky eye, full lips; BROWN eyes; silver hoop earrings.
Lilac strapless tube bodysuit, dusty-purple baggy knee-length drawstring shorts, barefoot.
```

```
@Image 2 = HARUMIN — 165cm, short brown wavy shag with fringe, large eyes; permanent holographic
glitter strip across the bridge of the nose (keep in every frame). … Voice flirty, sarcastic,
playful, soprano.
```

Context variants — the same character in a different state — are written as deltas, not as a
second identity: `(no choker at home)`, `NO horns at home`.

### A13. Scale

Metric size for anything that shares a frame with anything else, plus a human anchor and a
relational placement.

```
SCALE: the @Image 3 mech is 5 meters tall; Haru (~165cm) sits on its highest point. The
@Image 6 monster is 2 meters.
```

Then carry the number with the noun everywhere below: `the @Image 6 2m monster`, never just "the
monster".

### A14. Geometry map

The top-down blocking, written as prose. Positions, facings, eyelines, entrance vectors. This is
what keeps screen direction stable across cuts.

```
@Image 3 5m mech sits on its butt with its cabin/cockpit facing the cliff edge (far back from the
edge). Haru sits on top of the mech with her back to the cliff edge (facing the road). @Image 2
Reina is on the road side, looking down the road toward the cliff — sees Haru frontally. @Image 6
2m monster bleeds dark purple ichor, runs in from the cliff side straight at Haru's back.
Continuity across cuts.
```

For a fixed set, state it as a seating chart with left/middle/right:

```
SEATING (per top-down maps): on the dark-green L-sofa, @Image 4 LEFT, @Image 3 MIDDLE,
@Image 5 RIGHT; @Image 2 is up front by the coffee table.
Locations: @Image 7 (main face) and @Image 1 (reverse face) — same room, opposite walls.
```

That last line is the reverse-angle fix: two plates for one room, explicitly labelled as opposite
walls, so the reverse shot does not invent a second room.

### A15. Locks

The numbered non-negotiables — the things that would ruin the piece if they drifted. Keep the list
short; a lock list of fifteen items is a wish list, not a lock list. Each lock states the positive
first where one exists.

```
LOCKS:
@Image 1 wardrobe: glossy nude-latex long-sleeve crop, bare midriff, khaki cargo (belt + knee
straps), orange boots, holographic nose strip. NO harness/seatbelt/vest/straps on her torso.
Food (@Image 7): Korean fire-spicy ramen — vivid bright-red chili broth, glossy noodles, heavy
steam. Not pale, not clear.
NO interface anywhere — no reticle, crosshair, scope ring, HUD, UI, range numbers, targeting
graphics in any shot.
```

**Placement.** Identity, scale and geometry go **above** the shots — you cannot read the shots
without them. The *locks recap* goes **below** them (Part C), bracketing the piece. The same
constraint at both ends of a prompt survives better than the same constraint twice in the middle.

### A16. Physics manifest

An inventory of mass and contact for every interaction in the piece, material by material. This is
the deepest cause of the CGI look and it is invisible in a still — objects with no weight, hinges
with no resistance, liquids that do not pour, contact that does not register.

```
PHYSICS

Real mass and contact throughout — the seated 5-meter mech's weight presses the asphalt, cables
hang with gravity and sway in wind, the mech barely shifts under the pilot's small weight on top.
Foil lid tears with thin metallic resistance; dry noodle block drops with light weight; water glugs
and pours with surface tension, splashing slightly. The steel jar has real heft. The back hatch
swings up on its hinge with weight; steam vents in a real soft burst toward her face, stirring her
hair, then rises and curls, denser as the broth boils; bubbles roll and break at the surface;
condensation beads on the steel rim. Fog drifts in slow volumetric layers across all shots.
```

Separate block for a multi-segment piece. For a continuous take, run it inline in the action
timing, tied beat by beat, and close with `nothing floats`.

Where the world's rules are non-standard, state the governing law once and let everything inherit
it: `Gravity is local: each landscape pulls toward the surface it sits on, so waterfalls, smoke and
clouds each follow their own ground's direction.`

---

## Part B — the shot blocks

Labelled sub-blocks, in this order. The labels are load-bearing: they keep spatial facts,
optical facts and temporal facts from being averaged together.

```
SHOT 2 — SNIPER-RIFLE VIEW, NO INTERFACE (handheld)
```

The header line carries: shot number, shot size or POV, the one-line intent, and the
mode (`handheld`). Where a shot has a single dominant constraint, put it in the header too —
that is the first payment from the redundancy budget. For a long continuous take, make the header
an arrow chain: `OVER-THE-ARMS OPENING -> BLAST ONE BIG HOLE -> FLY THROUGH (TEARING FLESH) ->
TURN TO REVEAL MECHA -> KILL LEAPING BUG 2 INTO LENS`.

### B0. FIRST FRAME

The opening composition, separated from the camera move and from the action — the model anchors
hardest on frame one. Use **normalised percentage bounding boxes** for subject and background
placement. This fixes where the shot *starts*; the action moves from there, so do not coordinate
every beat.

```
First frame: low wide handheld shot from directly behind the mecha. @Image 1 sits on its rear on
the wet asphalt, back to camera, x 35%–70%, y 20%–85%, its extended legs reaching away from camera
toward the distant broken edge. The mech is set well back from the edge on solid deck; the torn
drop-off and foggy skyline are far ahead in BG center, x 0%–100%, y 0%–40%. Guardrails lead the
eye into depth.
```

For a oner, mark it `FIRST FRAME (locked)`.

### B1. LOCATION MAP

Where everyone is *for this shot*, what is behind them, what is defocused. Restates the relevant
slice of A14 rather than assuming it carried.

### B2. FORMAT MODE

Take structure and its relationship to the neighbours.

```
One continuous take, ~5s, real-time, no cut.
```
```
One continuous take, ~4s, real-time. Hard CUT from Shot 1.
```

### B3. OPTICS

Lens, stop, DoF behaviour, and — when it matters — the **optical cause of the framing**. Give the
FOV in degrees **and** the camera distance in metres: together they fully specify the geometry,
and neither does alone.

```
84° classic wide, camera 2m behind the mech, environment visible to edges, straight rails
rectilinear.
```
```
29° short telephoto portrait, camera 3–4m reach, her face and upper body razor-sharp, background
softly compressed into the grey fog.
```

Pair any wide request with a rectilinear assertion, or it drifts to fisheye — and block the dutch
tilt on any POV-from-inside-an-object: `The framing is level and upright — no canted/tilted
horizon.`

```
Large-format 65mm spherical shot WIDE OPEN at ~f/1.4, telephoto / long-lens compression,
EXTREMELY SHALLOW depth of field. ONLY @Image 3's face is in sharp focus; the entire background
is heavily defocused into creamy bokeh — the room behind must be BLURRED AND UNREADABLE, NOT
sharp, with soft round bokeh on any highlights. Strong subject-background separation. Halation,
grain.
```

### B4. CAMERA

Movement, size, what it follows, where focus is locked. Every move needs a motivation; with no
motivation, lock the camera.

```
Handheld, medium close-up, FOLLOWS Haru as she approaches Mira (reframes with her move).
```

### B5. ACTION TIMING

Local timeline starting at 0. Beats, dialogue with its delivery notes and pause marks, audio
notation, and the per-shot performance reminder.

```
0–4s: @Image 2, mysterious and squinting, draws out the line VERY SULTRY AND SEXY: "Cappy, have
you ever seen..." — moving in closer to @Image 3 as she speaks. Slow, teasing, seductive build.
Keep holographic nose strip. @Image 2 blinks naturally, forehead and brows active throughout.
```

Dialogue split across a cut carries its own ellipses so the pauses survive:
`"Cappy, have you ever seen..."` → `"...anyone... push a mech to its limit... like that?"`

Where two sequential actions live in one shot, block the model's instinct to cut between them:
`ONE CONTINUOUS UNCUT ACTION — … No internal cuts; the whole pour-and-fill is a single take.`

For a continuous take with no edit to hang structure on, number the **camera's** beats:
`(1) riding behind the forearms…; (2) a crash-zoom into the hole; (3) a glide through the interior
while the focal length racks; (4) a whip and zoom-out as it bursts out the far side; …`

---

## Part C — the closing recap

One paragraph after the last shot, restating every critical constraint as a positive assertion:
cast, scale, blocking, performance, prop details, per-segment camera rules, weather, location.

```
POSITIVE LOCKS

Only @Image 2 (the pilot) and @Image 1 (the mecha) are present — no other characters. The mech is
~5 meters tall and stays seated on its rear, set well back from the broken edge… She stays joyful,
blinks, and licks her lips with live forehead/brow micro-expression whenever her face is visible.
… Every segment is handheld. Segment 4 is shot from below; Segment 5 ends on the boiling noodles.
The weather stays flat foggy overcast with no sun, matching @Image 3. The location stays the
@Image 3 foggy broken bridge; no new place identity is added.
```

`no new place identity is added` names the actual failure — the model inventing a second
location — far better than "stay consistent".

---

## Copy-paste template

```
SCENE CONTEXT
<one plain-prose paragraph: what happens, in order, ending on the last image. No jargon, no handles, no camera.>

GLOBAL STYLE
<format, stock, lens, grain/halation, DP name, real-time 24fps, 180° shutter. NOT <categories>.>

OPERATING STYLE — <NAME>: <decode the name into observable behaviour>

Light: <motivated sources only. Exception for <segment>: <bounded exception, then re-assert the law>>
Colour — ACCENT DOCTRINE: ~70% <dominant, with source> · ~20% <accent, with source — bind one band to the subject> · ~10% <counter-note, with source>
Texture: <materials; matte vs gloss>. <raised detail level for the one extreme moment, if any>
Camera/Optics: <house lens behaviour>
Skin: <pore-level positive list>. NOT <waxy/plastic/CGI>. <shadow conditional>
Acting: <blink + brow mandate>. <performance-register permission, if it conflicts with the look>
Composition: off-centre, never centred.
Technical: real-time 24fps, no flicker, no warping, no morphing. <scoped slow-mo allocation, if any>
Audio: <dialogue policy> · <music policy> · No subtitles.
<Behaviour lock: how a key prop acts, and the wrong reading it must not fall into>

ASSETS
@handle = NAME — <height>, <hair>, <wardrobe head to toe incl. feet>, <signature detail — keep in every frame>. Voice <register + attitude>. 100% matches the reference.
@location_handle = LOCATION — <geography, materials, atmosphere, weather>. Controls <channels> only, not camera angle.

SCALE: <object> is <N> m; <human> (~<N>cm) <relational placement>.

GEOMETRY: <top-down map in prose — positions, facings, eyelines, entrance vectors>. Continuity across cuts.

FORMAT MODE
<N segments joined by hard cuts, in order | ONE unbroken continuous take, ~Ns>. Real-time motion. Continuity locked: <what carries through>. Ends on <the last image>. No invented cuts, no montage.

LENS LOCK
SEGMENT 1 = <N>° <name>.  SEGMENT 2 = <N>° <name>.  …
No lens drift mid-segment.

PHYSICS
<mass and contact for every interaction, material by material>. Nothing floats.

SEGMENT 1 — <TITLE / arrow chain for a oner>
  First frame:   <opening composition; subject x <a>%–<b>%, y <c>%–<d>%; BG placement in coords>
  Camera move:   <move + motivation>
  Optics:        <N>° <name>, camera <N>m from <subject>, <what is sharp>, rectilinear, no fisheye
  Action:        <beats> {dialogue with… pause… marks} <SFX> (music). <blink/brow reminder>. <signature-detail reminder>.
                 <ONE CONTINUOUS UNCUT ACTION — no internal cuts, if two actions run together>
HARD CUT to Segment 2.

SEGMENT 2 — …

POSITIVE LOCKS
<every critical constraint restated as an assertion: cast, scale, blocking, performance, prop details, per-segment camera rules, weather, location. …no new place identity is added.>
```

## Ordering rationale

Constants above variables is not tidiness. A model reading a contradiction resolves it with
whatever it saw in the most locally coherent context, so a per-shot line that contradicts the
header usually wins — which is exactly what you want for *deltas* and exactly what you must avoid
for *constants*. Keeping every constant above every shot means the only contradictions left in the
prompt are deliberate ones.
