# Technique catalog

Named devices extracted from the library. Each entry: **the problem it solves → the pattern → a
verbatim line from the source → exemplar id**. Add to this file when a new exemplar teaches
something not already here (procedure in SKILL.md, "Ingesting a new exemplar").

Exemplar ids: `[001]` mech/sniper/ramen · `[002]` sofa scene, Mira & Harumin · `[003]` THE INSIDE
(ours, `curved-world/prompt.txt`) · `[004]` noodle prep, 5 segments · `[005]` mecha vs bug, oner ·
`[006]` FREGIO "Everywhere" commercial (ours, **with a verified failure**).

---

## 1. Identity and continuity

### 1.1 The series bible
*Problem:* separately-generated shots of the same scene do not look like the same scene.
*Pattern:* everything constant — style, light, colour, texture, optics, skin, acting, composition,
technical, audio policy, identity strings, geometry — is written once and pasted **byte-identical**
on top of every shot's submission. Only the asset legend (numbering is per submission) and the shot
block change. `[002]`

This is why `[002]` re-declares its full OPTICS and LOCATION MAP inside every shot: those three
shots were three separate generations, not one. `[001]` is the other shape — one submission, four
shots, `HARD CUT.` between them, one header.

### 1.2 Identity string
*Problem:* "a woman in a jacket" is a different woman in every generation.
*Pattern:* height in cm · hair shape *and* colour transition · wardrobe head to toe **including
feet** · one signature detail · voice register and attitude. Written once, reused verbatim.
> `@Image 4 = REINA — 183cm, Korean features; black hair with light-brown ends, wet-look mid-length shag, ragged side-swept fringe; heavy smoky eye, full lips; BROWN eyes; silver hoop earrings. Lilac strapless tube bodysuit, dusty-purple baggy knee-length drawstring shorts, barefoot.` `[002]`

"Barefoot" is not a throwaway. Unspecified feet get invented shoes.

### 1.3 Signature detail
*Problem:* you cannot tell at a glance whether identity held.
*Pattern:* give each character one small, unusual, binary-checkable marker and order it kept.
> `permanent holographic glitter strip across the bridge of the nose (keep in every frame)` `[002]`

It doubles as your QC test: scrub the output, look for the strip. Present or absent, no judgement
call. Re-state it in every shot block (`Keep holographic nose strip.`).

### 1.4 Context variant as a delta
*Problem:* the same character in a different setting spawns a contradictory second identity string.
*Pattern:* write the variant as a parenthetical subtraction from the canonical string, never as a
new description.
> `barefoot (no choker at home)` · `NO horns at home` `[002]`

### 1.5 Voice casting by register
*Problem:* generated voices default to a flat neutral read.
*Pattern:* cast the voice in the identity string using musical register plus attitude.
> `Voice strict, focused, mezzo-soprano.` / `Voice flirty, sarcastic, playful, soprano.` `[002]`

### 1.6 Name the hardest asset
*Problem:* a global constraint gets applied evenly when one subject is the actual risk.
*Pattern:* say where the constraint will fail.
> `SKIN / REALISM (hardest on @Image 2): …` `[001]`

### 1.7 Fidelity clause
*Problem:* a reference image is treated as inspiration rather than as a spec.
*Pattern:* state the required fidelity on the asset itself, per asset.
> `100% matches the reference.` `[004] [005]`

### 1.8 Named asset handles — **house default**
*Problem:* `@Image 1` is positional, so the same character is a different number in every
submission, every shot of a series has to be re-numbered by hand, and the prose reads as
coordinates instead of names.
*Pattern:* give every asset a semantic handle and use it everywhere.
> `@zero_mecha`, `@STVOL`, `@bug_22`, `@location_scene_1` `[005]`

Self-documenting inside the shot prose (`the ribbed @STVOL barrel aimed point-blank`),
order-independent, and portable across every shot in a series. Supersedes the per-submission
renumbering caveat that positional `@Image N` forces. Keep a `HANDLE = description` block so the
binding is still explicit; upload order then only has to match that block once.

### 1.9 Behaviour lock
*Problem:* an object is described by appearance and then behaves generically.
*Pattern:* a dedicated block for how a thing *acts*, separate from how it looks.
> `Weapon behaviour: @STVOL fires ONLY in fast full-auto bursts - an Uzi-like rapid cyclic rate, short ripping bursts, never single deliberate shots.` `[005]`

### 1.10 Anti-affordance clause
*Problem:* the model has a strong prior about how an object class is used — a gun is held in a
hand — which overrides your design.
*Pattern:* state the mechanism, state why it matters, then name the wrong reading. The
object-design twin of 3.1.
> `The hand stays FREE below the barrel, so the same arm can grip an enemy while the barrel fires. Fired from the forearm in fast full-auto bursts (Uzi-like), NEVER held as a pistol.` `[005]`

### 1.11 Instance count
*Problem:* an asset appears once when the beat needs two, or duplicates when it should not.
*Pattern:* say how many exist in this piece, in the asset block.
> `Two appear across this beat.` `[005]`

---

## 2. Space and scale

### 2.1 Travelling scale
*Problem:* declared once at the top, scale is gone by the third shot; mechs read as toys, creatures
read as buildings.
*Pattern:* metric size + human anchor + relational placement in the header, then **the number
travels with the noun at every single mention**.
> `SCALE: the @Image 3 mech is 5 meters tall; Haru (~165cm) sits on its highest point. The @Image 6 monster is 2 meters.` `[001]`
> …then throughout: `the @Image 3 5m mech`, `a @Image 6 2m monster running in fast behind her` `[001]`

### 2.2 Geometry map in prose
*Problem:* reverse angles flip screen direction; characters look at nothing; entrances come from
the wrong side.
*Pattern:* write the top-down blocking as sentences — position, facing, eyeline, entrance vector —
and close with an explicit continuity order.
> `Haru sits on top of the mech with her back to the cliff edge (facing the road). @Image 2 Reina is on the road side, looking down the road toward the cliff — sees Haru frontally. @Image 6 2m monster … runs in from the cliff side straight at Haru's back. Continuity across cuts.` `[001]`

For a static ensemble, a seating chart with LEFT / MIDDLE / RIGHT:
> `SEATING (per top-down maps): on the dark-green L-sofa, @Image 4 LEFT, @Image 3 MIDDLE, @Image 5 RIGHT; @Image 2 is up front by the coffee table.` `[002]`

### 2.3 Two-face location plating
*Problem:* the reverse shot invents a different room.
*Pattern:* plate both walls of one room and bind them as opposing faces of the same space.
> `Locations: @Image 7 (main face) and @Image 1 (reverse face) — same room, opposite walls.` `[002]`

### 2.4 Per-shot LOCATION MAP
*Problem:* the header geometry does not survive into a tight framing.
*Pattern:* each shot restates its own slice — who is behind whom, what is defocused, where the
camera sits relative to the map.
> `@Image 3 sits in the MIDDLE of the sofa; BEHIND HER is @Image 7 main face, rendered as a COMPLETELY OUT-OF-FOCUS WASH … Camera from the coffee-table side, ~50mm, off-centre, never centred, on Mira.` `[002]`

---

## 3. Optics and framing

### 3.1 Optics, not proximity
*Problem:* "close-up" is read as *camera physically near the subject*, destroying a surveillance,
sniper, or observed-from-afar read.
*Pattern:* name the optical mechanism, give a number, then state how it should read — and name the
wrong read you are guarding against.
> `The close framing is achieved through long-lens reach, NOT proximity — extreme super-telephoto compression (≈8° FOV), camera very far away, background flattened into creamy soft bokeh, atmospheric haze, only Haru sharp; it reads as observed from a great distance, never like the camera is right next to her.` `[001]`

Generalised: **physical cause → numeric value → intended read → the wrong read, named.**

### 3.2 Contrastive read
*Problem:* a bare positive leaves the nearest wrong interpretation live.
*Pattern:* `it reads as X, never like Y`. Different from a negative — you are not banning an
object, you are disambiguating a perception.
> `never like the camera is right next to her` `[001]`

### 3.3 Declare what is sharp
*Problem:* the model distributes focus democratically and the shot has no subject.
*Pattern:* name the one sharp thing and the state of everything else, with a stop.
> `Large-format 65mm spherical shot WIDE OPEN at ~f/1.4 … ONLY @Image 3's face is in sharp focus; the entire background is heavily defocused into creamy bokeh — the room behind must be BLURRED AND UNREADABLE, NOT sharp, with soft round bokeh on any highlights.` `[002]`

### 3.4 Fight the centering prior
*Problem:* models centre subjects by default; centred framing is itself an AI tell.
*Pattern:* state it as doctrine in the header and repeat it in every shot header and location map.
> `off-centre, non-symmetrical compositions welcome — never centred` `[002]`

### 3.5 Frame the room, not the subject
*Problem:* a subject filling the frame edge to edge leaves no space for the event to happen in.
*Pattern:* when an entrance, a landing, a time-lapse or a reveal must occur, describe the negative
space it needs. In `[001]` shot 4 the monster has to lunge in from behind and drop — the framing
had to hold Haru plus that airspace. `[001]`

### 3.6 Frame coordinates
*Problem:* "she is off-centre, the skyline is behind her" is a wish; the model composes to its own
prior anyway.
*Pattern:* normalised percentage bounding boxes for subject and background, in the first-frame
description.
> `@Image 1 sits on its rear on the wet asphalt, back to camera, x 35%–70%, y 20%–85%` `[004]`
> `the torn drop-off and foggy skyline are far ahead in BG center, x 0%–100%, y 0%–40%` `[004]`

The most precise compositional device in the corpus. Use on the first frame of a segment, not on
every beat — it fixes where a shot *starts*, and the action moves from there.

### 3.7 Lens lock in degrees
*Problem:* millimetres are meaningless without a sensor size, and lenses drift mid-shot.
*Pattern:* a dedicated block assigning a **field of view in degrees** to each segment, closed with
an anti-drift clause.
> `LENS LOCK — SEGMENT 1 = 84° classic wide. … SEGMENT 4 = 29° short telephoto portrait. … No lens drift mid-segment.` `[004]`

A lens plan is a restriction, not a menu: `[004]` uses two focal lengths across five segments.

### 3.8 Camera distance in metres
*Problem:* FOV alone does not determine framing — the same lens at 1 m and at 4 m are different
shots.
*Pattern:* give the distance with the FOV. Together they fully specify the geometry.
> `84° classic wide, camera 2m behind the mech` · `camera ~0.8–1.2m from her` · `29° short telephoto portrait, camera 3–4m reach` `[004]`

This is the systematised form of 3.1: **FOV + distance = the shot**, with nothing left to infer.

### 3.9 Anti-fisheye clause
*Problem:* wide-angle requests drift into barrel distortion and fisheye curvature.
*Pattern:* pair the wide request with a rectilinear assertion, naming a straight thing in frame.
> `environment visible to edges, straight rails rectilinear` · `slight wide presence, no fisheye curve, level framing` `[004]`

Also applies to POV-from-inside-an-object, which reliably produces a dutch tilt unless blocked:
`The framing is level and upright — no canted/tilted horizon.` `[004]`

### 3.10 Focal rack as an animated curve
*Problem:* a lens change inside a take is described as a vibe ("it goes wider") and lands anywhere.
*Pattern:* give the start FOV, the end FOV, and the event that triggers the change.
> `~80 degree wide for the over-the-arms opening …; as the camera enters the big hole and travels through the interior the focal length racks from ~70 degrees to ~110 degree wide rectilinear; it settles ~55-60 degrees, low, as it turns onto the mecha` `[005]`

Where 3.7 locks the lens per segment, this animates it across a oner. Opposite tools, same units.

### 3.11 Numbered camera beats inside one take
*Problem:* a continuous shot has no cuts to hang structure on, so it renders as one undifferentiated
move.
*Pattern:* number the *camera's* events even though there is no edit.
> `(1) riding behind the mecha's forearms on the grip-and-fire, a snap zoom punching in…; (2) a committed straight drive plus crash-zoom into the one big hole; (3) a glide through the wet interior…; (4) a fast whip and zoom-out as it bursts out the far side; (5) a turn that reveals the mecha low and wide…; (6) it stays raw, shaky, run-and-gun` `[005]`

### 3.12 One plate carrying both shots
*Problem:* a beat needs two setups to work — a wide that establishes the situation and a closer one
that plays the performance — and describing both inside one timeline range gets you neither.
*Pattern:* design a single frame that carries both jobs, and plate it.

`[006]` asked in prose for `a locked-off symmetrical shot of two occupied stalls side by side, feet
visible under the doors` **and** `Inside the left stall (seen in a closer locked shot)`. The
generation delivered a conventional medium close-up with the neighbouring stall entirely absent —
the joke's whole premise had no visual referent. The fix plate solves it in one composition: **left
stall open** with the subject fully readable (the closer shot), **right stall closed** with a second
pair of legs and different shoes under the door (the wide's information). No cut required.

Cheaper than a cut and it removes the geometry from prose entirely. Corollary: **bake the gag into
the plate** — in `[006]` the suit jacket, the tie and the trousers around the ankles are all in the
still, so nothing about the joke depends on the model electing to render it.

---

## 4. Look and light

### 4.1 Named DP, then decoded
*Problem:* a name alone is compression that may decompress to nothing.
*Pattern:* invoke the name, then spell out the observable behaviour it stands for.
> `Hoyte van Hoytema — foggy, atmospheric, shallow DoF, documentary handheld.` `[001]`
> `OPERATING STYLE — HOYTE VAN HOYTEMA: large-scale realism with intimate handheld closeness, immersive in-camera feel, tactile textures, atmospheric haze and volumetric light. Shallow depth of field on the face, documentary framing, photochemical look.` `[002]`

### 4.2 Accent doctrine
*Problem:* "muted palette" is unfalsifiable and the model averages toward teal-orange.
*Pattern:* three bands with percentages, **each naming its physical source**.
> `~70% desaturated green-grey room tone + raw concrete; ~20% warm orange-yellow accent (warm daylight + warm ceiling-panel light through the camo netting); ~10% cool daylight blue as a counter-note from the windows.` `[002]`

### 4.3 Source-motivated light, bound to the location asset
*Problem:* interiors and exteriors of the same scene get different light and the cut breaks.
*Pattern:* every source named; interior light explicitly inherited from the exterior plate.
> `Hard shadows carve across her face, half in deep shadow; no sun, cold foggy light of location @Image 5 only, warm ember glow on lips/fingers.` `[001]`

`no sun` here is doing real work — it removes the model's favourite default key.

### 4.4 Pore list plus shadow conditional
*Problem:* skin renders waxy; and where you ask for deep shadow, texture disappears entirely.
*Pattern:* positive texture inventory, exclusion tail, then a conditional protecting texture inside
the shadow.
> `visible pores, peach-fuzz, subsurface translucency, asymmetry, true eye catchlights, flyaway hairs; matte, lived-in. NOT waxy/plastic/airbrushed/CGI/doll. Half-face in shadow, texture still readable.` `[001]`

### 4.5 Real-time declaration
*Problem:* unprompted, generations drift into slow motion — the most common single tell.
*Pattern:* state the frame rate, the shutter, and the exclusion.
> `Real-time 24fps, 180° shutter.` + `real-time 24fps, no slow-mo` `[001] [002]`
> positive-only variant: `natural real-time motion speed throughout` `[003]`

### 4.2a Accent band bound to the subject *(refinement of 4.2)*
*Problem:* a palette floats free of the composition and the subject does not own a colour.
*Pattern:* attach one band to the subject and say so.
> `~20% mint/teal accent (@zero_mecha panels - the mecha is the subject)` `[005]`

### 4.5a Scoped slow-motion *(refinement of 4.5)*
*Problem:* banning slow motion outright costs you the one place it would help.
*Pattern:* allocate it precisely instead — where, how much, and the return to real time. Worth the
redundancy budget: `[005]` states it in FORMAT, in Technical, and again in ACTION TIMING.
> `mostly real-time 24fps with ONE very slight, almost imperceptible slow-motion touch during the pass through the bug's interior, then back to real time` `[005]`

### 4.6 Rule with a scoped exception
*Problem:* one shot needs to break the global look, so the prompt quietly contradicts itself and
the model picks a winner at random.
*Pattern:* state the law, then name the exception by segment and bound it.
> `Flat, diffuse, fog-filtered overcast light … no directional key, no warm light anywhere. … Exception for Seg 2: as she leans over the cup to open it, soft natural shadows fall across her face from her hair and her own form … (still cool and overcast, just gently shadowed).` `[004]`

The parenthetical re-asserting the law is what keeps the exception from becoming a new rule.

### 4.7 Absolute rule with enumerated instances
*Problem:* a colour or material rule holds for the first instance and lapses.
*Pattern:* state it absolutely, then enumerate the instances it covers.
> `ALL BLOOD IS DARK PURPLE, every drop, every splatter, every smear - never red.` `[005]`

Same mechanism as enumerating the HUD graphics in `[001]` — enumeration is what makes a
category rule stick.

---

## 5. Performance

### 5.1 Blink and brow mandate
*Problem:* the frozen forehead and unblinking stare — the loudest uncanny tell in AI video.
*Pattern:* command the micro-movement by name in the header **and** again in each shot's action
timing.
> `both blink naturally and show live forehead/brow micro-expression (eyebrows lifting, knitting, relaxing, forehead creasing). No frozen, blank, or mask-like faces.` `[001]`
> per shot: `@Image 2 blinks naturally, forehead and brows active throughout.` `[002]`

### 5.2 Performance-register permission
*Problem:* a photoreal style block silently suppresses stylised playing, producing flat acting.
*Pattern:* where look and performance registers disagree, grant permission in one clause.
> `Anime-comedic performance is allowed.` `[001]`

### 5.3 Play the non-reaction
*Problem:* every generated character reacts hugely; the comedy or the menace is in the character
who does not.
*Pattern:* describe the absence of reaction as an action, with the competing physical business
continuing through it.
> `calmly turns to look behind her at the downed monster while still chewing — chopsticks in hand, cheeks full of noodles — shows no surprise at all, a tiny "hmm… wow," then turns back and keeps eating, unbothered.` `[001]`

### 5.4 Describe a miss as a positive event
*Problem:* "the monster does not reach her" is an event negation and cannot be rendered.
*Pattern:* replace the absence with the physical thing that happens instead.
> `but it never reaches her: the AP round punches through it just short, bursting dark purple ichor, and the body drops and crashes.` `[001]`

### 5.5 Stage a reaction that proves the invisible
*Problem:* steam, heat, wind, smell and sound have no reliable visual signature and render as
nothing.
*Pattern:* give a character a physical reaction to the thing. The flinch renders the vapour.
> `steam rises out toward her, and she blinks and simply turns her face away from it … leaning her head aside out of the vapor` `[004]`

The word `simply` is doing anti-melodrama work — worth keeping.

### 5.6 Emotion carried by physical business
*Problem:* naming a mood produces a face pulling that mood, which reads as acting.
*Pattern:* name the mood once, then give it a physical action to ride on.
> `she blinks naturally, licks her lips with hungry delight … Her dominant expression is genuine happy anticipation of the meal.` `[004]`

### 5.7 Declared absence with a diegetic reason
*Problem:* the model invents a human face where none should be — and real faces are a Seedance
input-moderation risk in the first place.
*Pattern:* declare the absence and give it an in-world reason, in one clause.
> `No human face in frame (pilot in cockpit).` `[005]`

---

## 6. Structure and emphasis

### 6.1 LOCKS block
*Problem:* the two or three things that would ruin the piece are buried in prose.
*Pattern:* a short named list of non-negotiables, each stated positive-first, placed immediately
before the shots. Keep it short — a fifteen-item lock list is a wish list.
> `LOCKS: @Image 1 wardrobe: glossy nude-latex long-sleeve crop … NO harness/seatbelt/vest/straps on her torso. … NO interface anywhere — no reticle, crosshair, scope ring, HUD, UI, range numbers, targeting graphics in any shot.` `[001]`

### 6.2 Paired negative
*Problem:* the official guide says positive phrasing only; both shipped exemplars use negatives
heavily and they work.
*Resolution:* in every case the negative is **preceded by the positive that replaces it**. The
positive does the work; the exclusion narrows the prior. A bare negative is a coin flip.
> `matte, lived-in. NOT waxy/plastic/airbrushed/CGI/doll` `[001]`
> `4K photorealistic, large-format 65mm film look, real grain + halation … NOT 3D/game/cartoon.` `[001]`
> `completely clean, no interface of any kind (no reticle, crosshair, scope ring, HUD, range numbers, markers)` `[001]`

*Recorded disagreement:* the BytePlus guide restricts negatives to subtitles and audio. Both
exemplars contradict it for **category and object** exclusions. Neither uses a negative for an
event. Treat that boundary as the actual rule — see 6.3.

### 6.3 Category exclusion, never event negation
*Problem:* negatives fail unpredictably.
*Pattern:* a model can suppress a *category* (`NOT 3D/game/cartoon`), a *material*
(`NOT waxy/plastic`), or an *object class* (`NO HUD`, `NO harness`). It cannot render the absence
of an *event* — for those, use 5.4 instead. `[001] [002]`

### 6.4 Redundancy budget
*Problem:* restating everything flattens the hierarchy; restating nothing loses the critical one.
*Pattern:* pick one constraint per shot and restate it in three to five *different sections, in
different words*. In `[002]` shot 1, "the background is unreadable" appears in the shot header, the
LOCATION MAP, the OPTICS block, the CAMERA block and the ACTION TIMING line — five channels, five
phrasings. Everything else in that prompt is stated once. `[002]`

### 6.5 CAPS as the priority channel
*Problem:* everything in a long prompt reads at the same weight.
*Pattern:* reserve ALL-CAPS for constraints that must survive — `ONLY`, `NOT`, `NEVER CENTRED`,
`COMPLETELY OUT-OF-FOCUS WASH`, `EXTREMELY SHALLOW`. Caps on ordinary description spends the
signal. `[001] [002]`

### 6.6 HARD CUT token and FORMAT MODE
*Problem:* multi-shot prompts render as one continuous camera move; single-shot prompts sprout
cuts you did not ask for.
*Pattern:* terminate each shot with `HARD CUT.`, and declare each shot's internal structure.
> `One continuous take, ~5s, real-time, no cut.` / `One continuous take, ~4s, real-time. Hard CUT from Shot 1.` `[002]`

### 6.7 Constants above variables
*Problem:* a per-shot line contradicts the header and wins.
*Pattern:* that resolution order is usually what you want for deltas and always what you must avoid
for constants — so put every constant above every shot, leaving only deliberate contradictions.
`[001] [002]`

### 6.8 SCENE CONTEXT preamble
*Problem:* a prompt that opens with tags and technical blocks hands the model constraints before it
has any idea what the piece is, and the arc gets assembled from fragments.
*Pattern:* one plain-prose paragraph at the very top — what happens, in order, ending on the last
image. No jargon, no assets, no camera.
> `On a fog-shrouded broken bridge above a dead grey city, a small 5-meter mecha sits slumped on its rear … Its pilot, a young woman, climbs up on top of the mech and cooks instant noodles using the mech's own battery heat — tearing open a noodle cup, pouring it into a steel jar, adding water, opening the battery compartment … The video ends on the noodles boiling.` `[004]`

### 6.9 Specify the boring parts
*Problem:* anything left unspecified gets decorated — plain surfaces acquire print, logos, patterns
and greebles.
*Pattern:* say explicitly when something is plain.
> `Its sealed top is an ordinary plain grey foil seal lid (no print).` `[004]`

Restated in the closing locks, because it is exactly the kind of detail that drifts.

### 6.10 No internal cuts, per segment
*Problem:* two sequential actions inside one shot invite the model to cut between them.
*Pattern:* declare the segment uncut, name the span it covers, and say it twice.
> `ONE CONTINUOUS UNCUT ACTION — … she first pours out everything from the @Image 4 noodle package … then in the same shot reaches off to the side for a plastic water bottle … No internal cuts; the whole pour-and-fill is a single take.` `[004]`

Distinct from the piece-level `FORMAT MODE`, which also earns its own anti-montage clause:
`No invented cuts, no montage.` `[004]`

### 6.11 POSITIVE LOCKS as a closing recap
*Problem:* by the fifth segment the header is far away and its constraints have decayed.
*Pattern:* one closing paragraph restating every critical constraint as a positive assertion —
cast, scale, blocking, performance, prop details, per-segment camera rules, weather, location.
> `Only @Image 2 (the pilot) and @Image 1 (the mecha) are present — no other characters. The mech is ~5 meters tall and stays seated on its rear … Every segment is handheld. Segment 4 is shot from below; Segment 5 ends on the boiling noodles. … The location stays the @Image 3 foggy broken bridge; no new place identity is added.` `[004]`

`no new place identity is added` names the actual failure — the model inventing a second location —
far better than "stay consistent".

**Placement, resolved:** `[001]` puts locks before the shots, `[004]` after. Both shipped. House
rule: identity, scale and geometry go **above** the shots (you cannot read the shots without them);
the locks *recap* goes **below**, bracketing the piece per 8.2.

### 6.12 Raise the detail level for one moment
*Problem:* a uniform texture instruction under-serves the one shot that goes somewhere extreme.
*Pattern:* name the moment and its detail level inside the texture block.
> `Inside the bug, the flesh is rendered in maximal detail - wet membranes, fibrous tissue, glistening veins, ragged torn chitin.` `[005]`

### 6.13 Arrow-chain shot title
*Problem:* a long oner has no scannable structure.
*Pattern:* the whole shot as one arrow chain, above the detail.
> `SHOT - OVER-THE-ARMS OPENING -> BLAST ONE BIG HOLE -> FLY THROUGH (TEARING FLESH) -> TURN TO REVEAL MECHA -> KILL LEAPING BUG 2 INTO LENS / EXTERIOR.` `[005]`

### 6.14 One range, one setup
*Problem:* a timeline range that describes two camera setups with no cut declared between them
gets rendered as one, and the model picks which.
*Pattern:* one range = one setup. If the beat genuinely needs two, either split the range and
declare the cut, or collapse them into one frame per 3.12.

`[006]`'s final range asked for a symmetrical two-stall wide *and* a closer shot inside one stall,
inside 5 seconds — and got a single conventional close-up. Same range also carried twelve
performance beats where the duration holds two. Both failures are visible in
[`library/006`](../library/006-fregio-everywhere-commercial.md); it is the corpus's clearest worked
example of over-asking a range.

---

## 7. Sound

### 7.1 Non-verbal vocal design
*Problem:* generated dialogue brings lip-sync artefacts and synthetic-voice tells.
*Pattern:* choosing no words is a positive creative decision, and the vocal texture that replaces
them must be specified per character.
> `Vocals: non-verbal only (Reina's smoke-exhale + low hum; Haru's tiny "hmm… wow" + chewing). NO words.` `[001]`

### 7.2 Dialogue split across the cut
*Problem:* a line delivered inside one shot has no room to breathe, and a cut mid-line usually
resets the performance.
*Pattern:* break one sentence across two shots with ellipses at the seam, and give each half its
own delivery note.
> Shot 2: `"Cappy, have you ever seen..."` — `draws out the line VERY SULTRY AND SEXY`
> Shot 3: `"...anyone... push a mech to its limit... like that?"` — `SLOWLY, in a WHISPER, sultry and mysterious, WITH SMALL PAUSES` `[002]`

The internal ellipses are pause marks — they encode timing the model otherwise flattens.

### 7.3 Sound as the event
*Problem:* action beats read as mime.
*Pattern:* write the sound of the physical event with the same specificity as the picture, in
sequence.
> `leap-hiss cut short, wet airborne punch-through + body crash + ichor splatter, Haru's small "hmm… wow" through a full mouth, continued chewing, wind.` `[001]`

---

## 8. World logic (from our own work)

### 8.1 The physics clause
*Problem:* impossible geography renders as a collage of unrelated planes.
*Pattern:* state the world's governing rule once, in the overall requirements, as a physical law —
then everything downstream (smoke, water, cloth, debris) inherits it without further instruction.
> `Gravity is local: each landscape pulls toward the surface it sits on, so waterfalls, smoke and clouds each follow their own ground's direction.` `[003]`

This is the strongest device in our own corpus and neither external exemplar has an equivalent.
Keep it.

### 8.2 Overall-requirements tail
*Problem:* global truths stated only in the style block get outvoted by shot-level detail.
*Pattern:* close the prompt with a short paragraph re-asserting the whole-piece constraints —
continuity, material truth, motion rate, frame, subtitles.
> `one continuous unbroken shot with no cuts … all of it solid anchored terrain built from real photographic forest, rock, grass, sand and water at every distance and in every part of the frame … Consistent sunlight, consistent atmosphere and natural real-time motion throughout. Widescreen 16:9 anamorphic frame. No subtitles.` `[003]`

Header and tail together bracket the shots — the same constraint at both ends of the prompt
survives better than the same constraint stated twice in the middle.

### 8.3 Asset binding by channel
*Problem:* a reference image contributes its whole self, including the parts you did not want.
*Pattern:* bind the asset to the specific channel it should drive.
> `@Image2 defines the overhead geometry: land, lakes and forest hanging upside down high above the character…` `[003]`
> `Refer to @Image1 for lighting and filters only.` (official guide)

### 8.3a Asset channel **exclusion** *(refinement of 8.3)*
*Problem:* a location plate has a camera angle, a lens and a composition baked into it, and it drags
every shot toward that angle no matter what the shot block says.
*Pattern:* state what the asset controls **and what it does not**.
> `@Image 3 — location. … Controls geography, materials, atmosphere, and weather only.` `[004]`
> `Use the reference for geography, materials, atmosphere, and weather, not for camera angle.` `[004]`

Say it in the asset block and again in the location map. This is the fix for "every shot looks like
the plate".

### 8.4 The physics manifest
*Problem:* generated objects have no mass — things float, hinges have no weight, liquids do not
pour, contact does not register. The deepest cause of the CGI look, and invisible in a still.
*Pattern:* a dedicated block inventorying mass and contact for **every** interaction in the piece,
material by material. Generalises 8.1 from a *law* to a *manifest*.
> `Real mass and contact throughout — the seated 5-meter mech's weight presses the asphalt, cables hang with gravity and sway in wind, the mech barely shifts under the pilot's small weight on top. Foil lid tears with thin metallic resistance; dry noodle block drops with light weight; water glugs and pours with surface tension, splashing slightly. The steel jar has real heft. The back hatch swings up on its hinge with weight; steam vents in a real soft burst toward her face, stirring her hair, then rises and curls, denser as the broth boils; bubbles roll and break at the surface; condensation beads on the steel rim.` `[004]`

For a oner, run it inline in the action timing instead, tied beat by beat, and close with the
compact form:
> `real creature weight fighting the grip, full-auto recoil through the forearm … the dead second bug keeps real momentum into the lens; nothing floats.` `[005]`

`nothing floats` is the most compact anti-CGI clause in the corpus. Separate block for a
multi-segment piece; inline for a continuous take, where physics and timing are the same axis.

---

## 9. Commercial dramaturgy

All from `[006]`. Use alongside the commercial rubric in
`../../one-prompt-film/references/dramaturgy.md` — that one judges whether the idea works, these
are how it gets written into a prompt.

### 9.1 Structural statement of intent
*Problem:* a synopsis tells the model what is shown, not what the film is *doing*, so a two-part
structure gets flattened into one even tone.
*Pattern:* say what each half does to the audience, and say that they are opposed.
> `The first 23 seconds are extremely expensive and beautifully choreographed; the ending deliberately destroys all of it with deadpan comedy.`

### 9.2 The product as a recurring motif
*Problem:* the product becomes wallpaper, or every shot turns into a packshot.
*Pattern:* the product need not be visible at all. Represent it with one repeated sensory
signature, keep it byte-identical at every appearance, and make it the thing that pays off.
> `The recurring sound motif is one sophisticated, soft crystalline notification ding, identical every time it appears.`
> …and in the overall requirements: `The notification ding is the identical sophisticated sound every single time, including in the restroom.`

The last three words are the whole commercial: the premium promise survives into the least premium
place in the film.

### 9.3 Deliberate un-readability
*Problem:* AI video garbles UI, small type and screen content — the exact things a software
commercial wants to show.
*Pattern:* turn the weakness into a style rule. State the ban, give **several mechanisms** for how
to obey it, and give the reason so the model has something to do instead.
> `Phone screens are never readable: phones are always angled away from camera, caught in glare, or out of focus — we understand everything through behavior, environments, notifications and reactions.`

Generalises past screens: anything the model renders badly can be composed around rather than
fought. Put real UI and small copy in post.

### 9.4 Motivated transitions as the continuity engine
*Problem:* a montage across many locations reads as a slideshow.
*Pattern:* every cut is hidden inside a physical event, and each transition names both ends.
> `Match cut: the closing door becomes the door of a moving luxury car interior.`
> `every transition motivated by movement — a door swing, a person wiping frame, a whip pan, a reflection`
> `the first 23 seconds feel like one continuous world — every cut hidden by motion, doors, bodies or reflections`

### 9.5 Music tracked as structure, with the stop as the payoff
*Problem:* music written as one instruction sits under the film instead of building it.
*Pattern:* place a music cue in *every* range, each describing its change of state, and treat the
stop as an event with a timestamp.
> `(a minimal confident rhythmic pulse begins, built around the footstep tempo)` → `(the pulse gains a driving beat)` → `(music opens up, warmer)` → `(the music accelerates, each DING landing on the beat)` → `The music becomes enormous — full drums and soaring synths` → `at the 23-second mark, HARD CUT: <the music stops completely, instantly>`

The cut in the sound *is* the cut in the film. Music stopping dead is the single most reliable comic
and dramatic device available in a prompt.

### 9.6 Silence scored as a beat
*Problem:* silence is treated as the absence of an instruction and gets filled.
*Pattern:* write it as a positive event, twice — once to establish, once to hold.
> `Dead silence.` … `Hold the beat in silence.`

### 9.7 Tonal hard cut
*Problem:* a turn that only changes location does not read as a turn.
*Pattern:* flip every axis on the same frame — genre, palette, camera grammar, sound.

In `[006]`: flowing choreographed handheld at dusk → `locked-off symmetrical`; premium architecture
→ `aggressively ordinary public restroom, flat fluorescent light, beige tiles`; enormous score →
dead silence. Four axes, one frame.

### 9.8 One line of dialogue, placed last
*Problem:* dialogue spread through a commercial invites lip-sync artefacts everywhere.
*Pattern:* run the piece wordless and spend the entire dialogue budget on one line at the end, with
its language and delivery named.
> `From the next stall, a muffled male voice: {English, sheepish: "Sorry."}`

### 9.9 Benefit delivered as a facial flip
*Problem:* the product benefit is narrated, or shown as a screen.
*Pattern:* stage it as a change of expression on one face, in the least flattering setting
available — the contrast is the argument.
> `His expression flips instantly from disgust to quiet satisfaction. He looks at the phone, gives a small approving nod.`

### 9.10 Name the moment identity must hold
*Problem:* a montage introduces many faces, then reprises them, and the reprise recasts everyone.
*Pattern:* name the exact range where identity has to survive.
> `All characters keep consistent appearance when they reappear in the 19-23s intercutting.`

Reliable only for background continuity. For anyone who carries a beat, use an identity string
(1.2) and a plate.
