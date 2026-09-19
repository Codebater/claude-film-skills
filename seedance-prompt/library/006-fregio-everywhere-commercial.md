# 006 — FREGIO "Everywhere" (ours) — 28 s commercial, and the beat that failed

**Shape:** single generation, 28 s, seven timeline ranges, one tonal hard cut at 23 s
**Assets:** none — pure text-to-video
**Register:** premium global-tech commercial for 23 s, then deadpan restroom comedy for 5 s
**Source:** [`fregio-spot/fregio_everywhere_prompt.txt`](../../../../fregio-spot/fregio_everywhere_prompt.txt)

Fills both remaining gaps in the library at once: the **commercial** exemplar, and the first entry
that carries **outcome data and a documented failure**.

## Outcome data

| Artifact | Duration | Note |
|---|---|---|
| `fregio_everywhere_raw.mp4` | 28.06 s | the single generation from the prompt below |
| `fregio_everywhere_FINAL.mp4` | 32.08 s | raw + end card |
| `toilet_clip.mp4` → `toilet_clip2.mp4` | 5.08 s / — | the ending **regenerated separately**, off a dedicated plate |
| `toilet_edited.mp4` → `toilet_edited2.mp4` | 5.38 s | two video-edit passes on that clip |
| `fregio_20s_FINAL_v1…v8` | ~22.3 s | eight cut versions of the 20 s trim |

**The 23 s montage landed in one generation. The 5 s payoff did not, and cost a plate, two
regenerations, two edit passes and eight cut versions.** All 720p/24fps.

## The failure, verified

The prompt's final range asked for this:

> `23-28s: … a locked-off symmetrical shot of two occupied stalls side by side, feet visible under the doors. Inside the left stall (seen in a closer locked shot): a guy sits peacefully on the toilet, casually working on his phone…`

What the generation produced at 25.5 s ([evidence](assets/006-failed-generation-25s.png)):

- A conventional **tight medium close-up**, not the locked-off symmetrical two-stall wide.
- **The neighbouring stall is not in frame at all** — no second door, no feet underneath. The
  entire premise of the joke has no visual referent; the sound comes from nowhere.
- **He does not read as being on a toilet.** No toilet visible, no trousers down, no gag. A man
  sitting in a beige tiled room.
- Wardrobe drifted — bomber jacket, not the suit the composition needed.

Two distinct mechanisms, both already named in this skill:

1. **The keyframe law.** Prose cannot hold camera geometry through a shot that has to *reveal an
   environment*. "Two stalls side by side, feet visible under the doors" is exactly that, and the
   model overruled it with its portrait prior. A second verified instance of the failure documented
   in `../../one-prompt-film/references/continuity.md`.
2. **Beat overload.** Count the beats asked for in 5 seconds: stop typing → turn head → disgust →
   second sound → close eyes → resume typing → ding → expression flips → approving nod → "Sorry" →
   look back → hold in silence. Twelve. At one beat per 2–4 s that range holds two.

Also structural: the range describes **two camera setups** (`a locked-off symmetrical shot` *and*
`seen in a closer locked shot`) inside one timeline range, with no cut declared between them.

## The fix — one plate carrying both shots

The regeneration was seeded from [`toiletscene.png`](assets/006-fix-plate.png), and the plate is
the lesson: it collapses the two requested setups into **one frame that carries both**.

- **Left stall open**, him centred and fully readable — that is the "closer locked shot", the
  performance.
- **Right stall closed**, a second pair of legs and white sneakers under the door — that is the
  "symmetrical two-stall wide", the neighbour's presence.
- The gag is **baked into the plate**: suit jacket and tie still on, trousers around the ankles.
  Nothing about the joke depends on the model choosing to render it.
- The neighbour is differentiated by footwear alone — white sneakers against his brown shoes —
  which is all a shot through a stall gap can carry.

Generalised into technique §3.12: **when a range describes two shots to deliver one idea, plate a
single frame that carries both.** Cheaper than a cut, and it removes the geometry from prose
entirely.

## What it taught — commercial dramaturgy (new §9)

- **Structural statement of intent** (§9.1) — the opening paragraph says what the film *does to the
  audience*, not just what it shows: `The first 23 seconds are extremely expensive and beautifully
  choreographed; the ending deliberately destroys all of it with deadpan comedy.`
- **The product as a recurring motif** (§9.2) — the product is never shown. It is one sound.
- **Deliberate un-readability** (§9.3) — `Phone screens are never readable` plus three mechanisms
  and the reason. Turns the model's UI-garbling weakness into a style rule.
- **Motivated transitions as the continuity engine** (§9.4) — every cut hidden in a door, a body
  wiping frame, a whip pan, a reflection.
- **Music tracked as structure, with the stop as the payoff** (§9.5) — five music cues across the
  timeline, ending in `<the music stops completely, instantly>`.
- **Silence scored as a beat** (§9.6) — `Dead silence.` … `Hold the beat in silence.`
- **Tonal hard cut** (§9.7) — genre, palette, camera grammar and sound all flip on one frame.
- **One line of dialogue, placed last** (§9.8) — 28 wordless seconds, then `{English, sheepish:
  "Sorry."}`.
- **Benefit delivered as a facial flip** (§9.9) — `His expression flips instantly from disgust to
  quiet satisfaction.`
- **Name the moment identity must hold** (§9.10) — `All characters keep consistent appearance when
  they reappear in the 19-23s intercutting.`

## Notes and cautions

- **The fix prompt was never saved.** A repo-wide search turns up only
  `fregio_everywhere_prompt.txt` / `.json`; there is no prompt file for the toilet regeneration, so
  the wording that finally worked is lost and only the plate and the output survive. The failure is
  reconstructed here from the artifacts — the plate, the clip durations, and the file timeline —
  not from a record. **Save the fix, not just the fix's output**: when a beat is re-generated,
  write the new prompt next to the clip. The repair is worth more than the original.
- Written in our older house style: no bible header, no locks, no physics manifest, no first-frame
  blocks, no lens plan. Rewriting it in the current schema is the obvious next test of whether the
  schema actually earns its length.
- The end card was composited in post, not generated — consistent with the standing gotcha that
  small copy garbles in-model.
- The 20 s trim (`f20`) re-uses the same generation with a tighter cut and the ding re-placed at
  18.54 s. Worth noting that a 28 s master can yield a 20 s cut without regenerating.

---

## Source prompt

```
An epic, kinetic global technology commercial: one continuous flowing camera journey through a city of people calmly building something on their phones — elevator, street, luxury car, lobbies, escalators, airports — every one of them finishing with the same elegant notification ding, an enormous inspirational build-up, and then a hard cut to a dead-silent public restroom where the campaign's true finale happens. The first 23 seconds are extremely expensive and beautifully choreographed; the ending deliberately destroys all of it with deadpan comedy.

Style: premium global-brand cinematography — ambitious camera choreography, elegant match cuts and motivated transitions (doors, people crossing the lens, reflections, whip pans), shallow depth of field, beautiful modern architecture and cinematic city photography at dusk, realistic phone behavior, natural motion with speed ramps used sparingly. Phone screens are never readable: phones are always angled away from camera, caught in glare, or out of focus — we understand everything through behavior, environments, notifications and reactions. The recurring sound motif is one sophisticated, soft crystalline notification ding, identical every time it appears.

0-4s: Extreme close-up: a thumb moving quickly across a phone held low. The camera rapidly pulls backward — <a bright elevator DING> — and elevator doors open exactly on that beat, revealing a sharply dressed woman stepping out mid-stride, still working on her phone, which faces away from us. The camera tracks smoothly backward in front of her through a marble lobby as passers-by cross close to the lens, wiping the frame. <heels on marble, fabric movement, the soft tap-tap of her thumb> (a minimal confident rhythmic pulse begins, built around the footstep tempo)

4-8s: One of the passers-by crosses fully in front of the lens and the camera emerges behind him onto a busy evening city street — a different person now, a young man walking fast through the crowd, building something on his phone, screen angled away. The camera circles him in a half orbit as traffic streaks past, then he steps toward the curb and into a taxi — the car door closes directly across the lens into black. <street traffic, footsteps, a car door clunk> (the pulse gains a driving beat)

8-12s: Match cut: the closing door becomes the door of a moving luxury car interior. A passenger in the back seat works calmly on his phone, screen catching only glare; city lights streak across his face. <the soft crystalline DING> — a subtle satisfied smile — he slides the phone into his jacket pocket. The camera drifts past him and travels out through the window into the flowing city lights. <muffled car interior hum, leather creak, one soft ding> (music opens up, warmer)

12-19s: Accelerating rhythmic montage, every transition motivated by movement — a door swing, a person wiping frame, a whip pan, a reflection: a man crossing a vast hotel lobby, phone in hand — <DING> — pockets it; a woman gliding up an escalator, thumb tapping — <DING> — small smile; a barista counter, a customer waiting for coffee, typing — <DING> — picks up his cup; a traveler striding through an airport terminal — <DING>; a fan sitting courtside in an empty arena before a game — <DING>; a silhouette walking into a nightclub past a bouncer — <DING>. Phones everywhere, screens never visible. The camera feels like it is traveling through one continuous world. <each ding identical, layered over footsteps, escalator hum, espresso machine, terminal announcements> (the music accelerates, each DING landing on the beat)

19-23s: The music becomes enormous — full drums and soaring synths. Fast intercutting between all the characters we have met: walking, typing, moving, <DING>, walking, typing, <DING>, airport doors sliding open, the luxury car racing through the city, the elevator rising in its glass shaft. Everything builds toward what feels like a huge inspirational finale — and at the 23-second mark, HARD CUT: <the music stops completely, instantly>.

23-28s: Dead silence. An aggressively ordinary public restroom, flat fluorescent light, beige tiles: a locked-off symmetrical shot of two occupied stalls side by side, feet visible under the doors. Inside the left stall (seen in a closer locked shot): a guy sits peacefully on the toilet, casually working on his phone, screen angled away. From the neighboring stall: <a horrible, long, echoing flatulent BRRRRAAAP>. He slowly stops typing. Turns his head toward the wall. Pure disgust. <a second, shorter horrible sound>. He closes his eyes, tries to ignore it, resumes typing — then <the same elegant crystalline DING>. His expression flips instantly from disgust to quiet satisfaction. He looks at the phone, gives a small approving nod. From the next stall, a muffled male voice: {English, sheepish: "Sorry."} He looks back at the wall. Hold the beat in silence. <restroom room tone, a dripping tap, echo>

Overall requirements: 16:9. The first 23 seconds feel like one continuous world — every cut hidden by motion, doors, bodies or reflections. All characters keep consistent appearance when they reappear in the 19-23s intercutting. The notification ding is the identical sophisticated sound every single time, including in the restroom. Phone screens are never readable anywhere in the film. No on-screen text, no captions, no subtitles, no logos.
```
