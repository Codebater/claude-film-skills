# Directing layer — director, DP, and editor between the idea and the prompt

This layer answers one question before any Seedance prompting happens: **how would an excellent director and cinematographer shoot this?** Its output is a shot-by-shot director's plan. The Seedance layer (SKILL.md Steps 3–4 + `seedance-25.md`) then decides how to *communicate* that plan to the model. Keep the separation: the director decides what happens; the Seedance layer decides how to say it.

Mental model: **CONCEPT → RESEARCH → EXTRACT TECHNIQUE → ADAPT → DIRECT → PROMPT** — never reference → copy → prompt.

## 1. Director pass — the visual idea

Before shots exist, decide what the *visual idea* of the sequence is — not what happens, but how seeing it is organized:

- What is initially **visible**, and what is initially **hidden**? Where does the viewer's **anticipation** point?
- Where does the **reveal** occur, and what earns it?
- Where should **attention** move, shot by shot? How do subjects **enter and exit** frame?
- How does the **environment participate** (not just backdrop — geometry, reflections, light, weather as actors)?
- Does the camera **follow** the subject, **anticipate** it (arrive first), or **observe** it (refuse to move)?
- Where does tension build; where is the payoff?

Think in blocking and visual storytelling, not beautiful frames. A frame that doesn't move attention or information is decoration.

## 2. Cinematography pass — motivated choices

**Camera.** Choose from real grammar: creeping dolly, push-in, pull-out, orbit reveal, lateral tracking, camera leading/following the subject, tracking handoff, crane reveal, overhead, macro-to-wide, foreground tracking, telephoto tracking, controlled handheld, body-mounted, locked camera, camera passing through environmental geometry. Then interrogate every move: **why is the camera moving?** Valid motivations: follow action, reveal information, transfer attention, create anticipation, establish scale, increase energy, hide a transition, mirror character movement, create contrast. No motivation → a locked camera is probably stronger. Never default to orbits or physically impossible moves.

**Lens / depth.** Intentional, not decorative: macro, wide-angle proximity (distortion as intimacy/threat), normal perspective, telephoto compression, deep staging (action layered front-to-back in focus), shallow focus, rack focus, foreground bokeh, focus change *caused by physical movement*. Banned as a default: "anamorphic shallow depth of field" pasted onto everything.

**Light.** Motivated by the world: directional sun, window bounce, practicals (lamps, signs, screens), screen illumination on faces, reflected light, edge light, silhouette, atmospheric backlight, moving environmental light (passing car, flickering sign), natural exposure changes (walking from interior to daylight). Prefer a believable source over "cinematic lighting" as an adjective.

## 3. Editor pass — cut before you shoot

Decide the edit before writing the prompt: where each shot begins and **ends** (late in, early out), what motivates every cut (action completes, look off-screen, sound, movement match), pacing — acceleration, deceleration, interruption, breathing room — and where reveal and payoff land on the timeline.

Rhythm shapes that work (pick what the concept implies, never force one):
- intrigue → build → acceleration → interruption → hero → payoff
- setup → misdirection → reveal
- detail → detail → detail → unexpected wide
- chaos → sudden stillness

## 4. Transition intelligence

The best transitions emerge from physics or composition, not editing presets: foreground occlusion, object wipe, match-on-action, graphic match, shape match, movement match, whip bridge, reflection transition, light/exposure transition, focus transition, environmental wipe, camera-through-object, motivated hidden cut. **One excellent transition beats five obvious tricks** — most cuts should just be good cuts. (Seedance handles these well when given trigger time + physical mechanism; see the transition rule in `seedance-25.md`.)

## 5. Signature device

For sequences that matter, ask whether **one** memorable filmmaking idea can carry the piece: a passer-by crossing frame hides the location change; a reflection introduces the subject before the camera does; a macro texture becomes an enormous environment; identical geometry connects two unrelated scenes; the camera hands off from one character to another; a lighting change *is* the cut; an object exiting one frame enters the next. If the scene doesn't need one, don't force it. One strong idea > five tricks.

## 6. Genre grammar — don't shoot everything the same way

| Genre | Grammar that tends to work |
|---|---|
| Comedy | locked compositions, awkward holds, delayed reactions, sudden reframes, crash zooms, deliberately mundane coverage |
| Luxury | restraint, tactile macro, controlled movement, precision lighting, negative space, slow confident pacing |
| Tech / UI | geometric composition, macro interface detail, graphic matches, physical depth, screen reflections, choreographed precise camera |
| Sport | physical proximity, telephoto compression, body-mounted movement, kinetic tracking, cuts on impact, environment interaction |
| Fashion | strong blocking, unusual composition, movement relationships, texture, rhythm, graphic silhouettes |
| Documentary | observational framing, natural light, restrained handheld, imperfect human composition, authenticity over polish |
| Surreal / conceptual | visual metaphor, impossible spatial relationships, unexpected scale, match cuts, practical-feeling transformations |

Examples, not templates — the grammar should emerge from the concept.

## 7. Anti-"AI cinematic" blacklist

Actively avoid, unless the concept specifically motivates it: unnecessary slow motion, constant orbiting, meaningless drone shots, lens flare, random whip pans, wall-to-wall shallow DOF, "anamorphic" as a magic word, floating particles, default teal/orange, impossible camera moves without motivation, a transition on every cut, glowing everything, generic luxury imagery, random speed ramps, macro for macro's sake. **"Cinematic" must come from direction, not adjectives.** For every decision, ask: does this improve the story, subject, action, emotion, information, reveal, or rhythm? If not, cut it.

## 8. Eyecandy research (eyecannndy.com)

Eyecandy is a visual **technique library** (~130 named techniques, each a page of real-world clips) — the research library, not the creative director.

**When to use it.** Not for every request. Reach for it when the honest self-check says *"the idea is good, but the way we're shooting it is ordinary"* — or when a specific problem needs options: the opening shot, the product reveal, a location transition, camera choreography, the payoff. If the user supplied strong references or the direction is already clear, use those first.

**How to search: by filmmaking problem, not subject.** For a car spot, don't look for "car commercial" — name the actual problems: *How is the car revealed? How does the camera meet it? Can movement hide the cut? Can a reflection introduce it before the hero shot?* Then pull the techniques that answer those problems (reveals → `epiphany-shot`, `reflections`, `object-portal`; hidden cuts → `pass-through`, `match-cut`, `whip-pan`).

**Access.** Direct HTTP fetches return 403 — browse it with whatever browser surface the session has (in-app browser pane first, Chrome extension second; `navigate` to `https://eyecannndy.com/technique/<slug>`, then read/screenshot). No browser available (headless/subagent runs) → work from the embedded taxonomy below, which is the designed fallback, not a degraded mode. Pages are clip grids; the technique *name and your knowledge of it* carry most of the value, the clips confirm nuance. The taxonomy below is embedded so most research needs no page visit at all.

**Extraction protocol.** When a reference is useful, analyze *why* it works — camera trajectory/speed/height, lens behavior, shot scale, composition layers (fg/mg/bg), blocking, subject movement, camera-to-subject relationship, reveal/transition mechanics, lighting direction and practicals, focus behavior, environmental interaction, edit rhythm, timing, tension, payoff — then **abstract the principle away from the reference**. Example: *camera follows a hand into a mirror and emerges elsewhere* → extract *"a reflection becomes a motivated spatial transition between environments"* → decide if that principle serves the current concept, and re-stage it in this concept's world. Never recreate the reference shot.

**Multiple references.** Don't blend into vague soup. Assign each a job — Reference A → camera choreography, B → lighting, C → transition, D → composition, E → rhythm — extract one principle from each, combine into a single coherent direction.

### Technique taxonomy (name → slug at `/technique/<slug>`)

**Camera movement & rigs:** Dolly `dolly-shot` · Double Dolly `double-dolly` (subject and camera on separate movers) · Dolly Zoom `dolly-zoom` · Arc `arc-movement` · Lazy Susan `lazy-susan` (subject rotates, camera doesn't) · Tracking `tracking` · Trucking `trucking` · Pedestal `pedestal` · Pan `pan` · Tilt `tilt` · Camera Roll `camera-roll` · Handheld `shaky-cam` · Snorricam `snorricam` (body-mounted, world moves around a locked face) · Bolt Cam `bolt-cam` (high-speed robot arm precision) · FPV Drone `fpv-drone` · Aerial `aerial` · Probe `probe-lens` (macro that travels *through* scenes) · Omnidirectional `omnidirectional` · Conveyor `conveyor` (world slides past a fixed camera) · Wandering `wandering` · Locked-On `locked-on` (subject stabilized center-frame, world jitters) · Fixed Cam `fixed-camera` · Boomerang `boomerang`

**POV & angle:** First-Person `first-person-pov` · Object POV `as-object` (camera *is* the product/object) · Voyeur `voyeur` · Over the Shoulder `over-the-shoulder` · High Angle `high-angle` · Low Angle `low-angle` · Worms-Eye `worms-eye` · Overhead `overhead` · Ground Level `ground-shot` · Dutch Angle `dutch-angle` · Fourth Wall `fourth-wall`

**Framing & composition:** Central Framing `central-framing` · Wide Shot `wide-shot` · Close-Up `close-up` · Cut-ins `cut-ins` · Two Shot `two-shot` · Profile `profile-shot` · Tableau `tableau-shots` (staged frozen compositions) · Silhouette `silhouette` · Vignette `vignette` · Void `void` (subject in emptiness) · Architexture `architexture` (architecture as graphic form) · Screen in Screen `screen-in-screen` · Split Screen `split-screen` · Ratio Switch `aspect-ratio-switch` · Masking `masking`

**Lens & optics:** Fisheye `fisheye` · Ultra Wide `ultra-wide-zero-d` · Tilt Shift `tilt-shift` · Shallow Focus `focal-focus` · Focal Shift `focal-shift` (rack focus) · Split Diopter `split-diopter` (two planes sharp at once) · Magnification `magnification` · Zoom `zoom-in` (incl. crash zoom, infinite zoom) · Parallax `parallax` · Motion Blur `motion-blur` · Halation `halation` · Haze `haze` · Distortions `distortions`

**Light:** Hard Light `hard-light` · Spotlight `spotlight` · Light Flash `light-flash` · Shadow Box `shadow-box` · Projections `projections` (projected imagery on subjects/sets) · Color Shift `color-shift` · Night Vision `night-vision` · Thermal `thermal` · X-Ray `x-ray`

**Transitions & cuts:** Match Cut `match-cut` · Match Motion `match-motion` · Match Split `match-split` · Whip Pan `whip-pan` · Crash Cut `crash-transition` · Flash Cut `flash-cut` · Jump Cut `jump-cut` · Quick Cuts `quick-cuts` · Object Portal `object-portal` (camera enters an object/opening and exits elsewhere) · Pass Through `pass-through` (camera through solid geometry hides the cut) · Set Transition `set-transition` (the set physically changes around the subject) · Transitions `transition` (general index) · Freeze Frame `freeze-frame`

**Speed & time:** Slow Motion `slow-motion` · Fast Motion `undercranking` · Speed Ramp `speed-ramping` · Bullet Time `bullet-time` · Stutter `stutter` · Step-print `step-printing` (smeared shutter dream look) · Infinite Loop `infinite` · Cinemagraph `cinemagraph` · Zoetrope `zoetrope`

**Space, scale & reveals:** Scale Shift `scale-shift` (macro becomes landscape, giant becomes toy) · Diorama `model` · Levitation `floating` · Falling `falling` · Epiphany `epiphany-shot` (slow push on a realization) · Reflections `reflections` · Duplication `duplication` · Morphing `morphing` · Transformation `transformation` · Photogrammetry `photogrammetry` (frozen 3D-scanned moment flown through) · Slit-scan `slit-scan` · Underwater `underwater`

**Texture, media & aesthetic worlds:** Double Exposure `double-exposure` · Echo Print `echo-printing` · Datamosh `datamosh` · Feedback `glitch` · Collage `collage` · Mixed Media `mixed-media` · Stop Motion `stop-motion` · Pixel Art `pixel-art` · Video Game `video-game` · Typography `typography` · Vintage `vhs` · Photography `photography` · Generative `generative` · Maximalism `maximalism` · Dreamcore `dreamcore` · Weirdcore `wierdcore` · Dystopian `dystopian` · Magical Realism `surrealism` · Anthropo `anthropomorphism` · Floating UI `digital-overlay` · Gesture `digital-gesture` · Kaleidoscope `kaleidoscope` · Wigglegram `wigglegram` · Interview `interview` · Video Portraits `video-portraits` · Choreo `choreo` · Product `product` · Altered State `trip` · Animation `traditional` · Stylistic Suck `stylistic-suck` (deliberate lo-fi)

Treat this as a growing vocabulary organized by problem (camera / blocking / composition / lens / light / transitions / editing / reveals / metaphor / texture), not a checklist. Select by concept.

## 9. Output: the director's plan (handoff contract)

The direction pass ends with a compact plan the Seedance layer translates. Format:

```
Visual idea: <one line — what is hidden, what is revealed, how seeing is organized>
Signature device: <one line, or "none — straight coverage serves this better">
Genre grammar: <which register and its 2-3 operative rules>
Shot 1 (~Xs): intent (what it makes the viewer feel/know) | blocking (who/what moves where,
  enters/exits) | camera + WHY it moves (or why locked) | lens/depth | light source |
  cut: what motivates the outgoing cut or transition mechanism
Shot 2 (~Xs): ...
```

Translation rules for the Seedance layer:
- Convert direction into **physical description** wherever a plain sentence is more reliable than jargon: "locked-on" → "the runner stays pinned dead-center while the street shakes and blurs past". Keep common terms Seedance knows (push in, orbit, wide shot, handheld); explain niche ones inline per `seedance-25.md`.
- Blocking and light motivation survive translation — they're what makes the output feel shot, not generated. Say where light comes from, and how subjects enter/exit frame.
- The editor pass's cut motivations become transition instructions with **trigger time + mechanism**.
- Timing, timestamps, asset binding, audio notation, and all locked-parameter rules stay exactly as `seedance-25.md` specifies. The director proposes; the Seedance constraint table disposes.
