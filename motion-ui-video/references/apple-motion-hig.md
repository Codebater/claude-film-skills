# Motion quality bar — Apple HIG, adapted for directing UI video

Distilled from Apple's Human Interface Guidelines (Motion, Feedback — developer.apple.com/design/human-interface-guidelines) and the principles behind them (WWDC "Designing Fluid Interfaces"). The HIG describes real interfaces; each rule below is translated into a **directing rule for a scene on camera**. Apply this during the Direct and Compose steps — it is the difference between "components animating" and motion that reads as designed.

## 1. Every beat needs a job (purposeful motion)

HIG: add motion purposefully; it conveys status, provides feedback and instruction — never add motion for the sake of motion; gratuitous animation distracts and can cause discomfort.

Directing: for each beat in `T`, be able to say what it *communicates* (arrival, causation, success, hierarchy). A beat with no answer gets cut. If two elements animate simultaneously with different motions and neither explains the other, one of them is noise.

## 2. Effects follow their cause (realistic feedback)

HIG: strive for feedback that follows people's gestures and expectations; motion that doesn't make sense is disorienting — a view revealed by sliding down shouldn't be dismissed sideways.

Directing:
- Reactions **emanate from the point of interaction**: a click's consequence starts at or radiates from the cursor (ripple from the press point, the counter nearest the button moving first, a stagger ordered by distance from the trigger).
- **Enter/exit symmetry**: whatever motion introduced an element, its removal mirrors it (slide down in → slide up out, scale in → scale out). Breaking symmetry on camera reads as a glitch.
- The reaction starts **immediately** on the press frame (perceived response < 100 ms — at 30 fps that's within 2–3 frames). The animation may take time to *finish*, but it must *start* instantly. Dead frames between click and reaction kill the causation read.

## 3. Brief and precise beats prominent (feedback hierarchy)

HIG: brief, precise feedback feels lightweight and conveys information *better* than prominent animation; avoid motion on frequent interactions; match delivery to significance — status is passive, only meaningful successes get confirmation, interruptions are reserved for what matters.

Directing:
- **One hero motion per scene.** Everything else is supporting cast: quieter, smaller, slower-fading. If the background, the headline, the button, and the icon all demand attention, nothing gets it.
- Micro-feedback (press states, toggles, hovers): **0.15–0.25 s**. Standard element transitions: **0.3–0.5 s**. Hero moments (the one payoff): up to **0.8 s**. These are iOS-feel conventions, not HIG numerals — but a 1.5 s button press reads as broken on camera.
- Confirmation moments (checkmark, success tick) earn screen time only when the action was the point of the video.

## 4. Springs and physical continuity

Fluid-interfaces school (the physics behind system motion): prefer spring curves over fixed-duration ease curves for anything interactive — springs preserve perceived momentum and never look truncated.

Directing:
- Interaction responses: springs with at most **one visible overshoot** (motion's default `stiffness`/`damping` around 300/30 for snappy UI, softer 100/30 for large numbers/panels). More bounces = toy, not product.
- Entrances (non-interactive): eased curves are fine — `[0.22, 1, 0.36, 1]` style ease-out; things *arriving* decelerate, things *leaving* accelerate.
- Nothing moves linearly except conveyor-belt style ambience.

## 5. Restraint rules (comfort & reduced-motion sensibility)

HIG: make motion optional; avoid sustained oscillation (people are acutely sensitive around 0.2 Hz); prefer fades when relocating an object whose travel communicates nothing; keep peripheral areas calm.

Directing:
- **No idle wiggle.** Elements at rest stay at rest. Endless floating/pulsing loops on things that aren't the subject read as cheap.
- **Relocations that mean nothing get crossfades**, not flights. Fly an element only when the path itself is the message (item → cart).
- Keep the stage edges calm — ambient background layers animate slowly and at low contrast; the motion budget is spent center-frame on the hero.
- End the video at rest: the final 0.5–1 s is a stable, resolved frame. A video that cuts mid-motion feels broken; one that settles feels engineered.

## 6. The Apple-feel checklist (run before recording)

- [ ] Every beat has a stated communicative job.
- [ ] Click reaction starts within 2–3 frames of the press and emanates from the press point.
- [ ] One hero motion; supporting motion is visibly subordinate.
- [ ] Micro ≤ 0.25 s, transitions ≤ 0.5 s, single hero moment ≤ 0.8 s.
- [ ] Springs overshoot at most once; enters decelerate, exits accelerate.
- [ ] No idle oscillation; no meaningless flights; edges calm.
- [ ] Enter/exit motions mirror each other.
- [ ] Final frames are fully at rest.
