# 001 — Mech / sniper / ramen (4 shots, one generation)

**Shape:** single multi-shot generation — one bible header, four shots separated by `HARD CUT.`
**Assets:** 7 (2 characters, 1 mech, 1 interior, 1 location, 1 creature, 1 prop)
**Register:** photoreal war-drama look, anime-comedic performance, non-verbal vocals

## What it taught

New to the catalog when ingested:

- **Travelling scale** (techniques §2.1) — the metric size restated at every mention of the noun,
  not just in the SCALE block. The strongest single idea in this prompt.
- **Geometry map in prose** (§2.2) — a full top-down blocking paragraph inside LOCKS, closing with
  `Continuity across cuts.`
- **Optics, not proximity** (§3.1) — the ≈8° FOV passage. The most transferable line in the corpus.
- **LOCKS block** (§6.1) — non-negotiables pulled out of prose into a named list.
- **Paired negative** (§6.2) and **category-not-event** (§6.3) — negatives used heavily, but always
  after the positive and never against an event.
- **Pore list plus shadow conditional** (§4.4) — `Half-face in shadow, texture still readable.`
- **Name the hardest asset** (§1.6) — `SKIN / REALISM (hardest on @Image 2)`.
- **Performance-register permission** (§5.2) — `Anime-comedic performance is allowed.`
- **Play the non-reaction** (§5.3) and **describe a miss as a positive event** (§5.4).
- **Non-verbal vocal design** (§7.1) — deciding against dialogue as a craft decision.
- **Named DP, then decoded** (§4.1).

## Notes and cautions

- The four shots share one generation, so the header is written once. If these were re-cut as four
  separate submissions, every block above `SHOT 1` would need pasting onto each — and the asset
  numbering would change per submission.
- `no sun` inside the light description is load-bearing: it removes the model's default key light.
- The interface lock is enumerated (`reticle, crosshair, scope ring, HUD, UI, range numbers,
  targeting graphics`) rather than left as "no UI". Enumeration is what makes an object-class
  negative reliable.
- Shot 2 is a POV through a scope with *no scope furniture at all* — a deliberately hard ask, which
  is why the lock appears in the header, in the shot title, and in the shot body: three channels,
  the redundancy budget spent on the one thing most likely to fail.

---

## Source prompt

```
Tags: @Image 1 = Haru Min (pilot) · @Image 2 = Reina (sniper) · @Image 3 = Haru's mech (seated rest-mode) · @Image 4 = Reina's cabin · location @Image 5 = broken bridge · @Image 6 = monster/bug · @Image 7 = sage-green ramen jar

GLOBAL STYLE

4K photorealistic, large-format 65mm film look, real grain + halation, Hoyte van Hoytema — foggy, atmospheric, shallow DoF, documentary handheld. Source-motivated cold natural light, desaturated earthy palette, no sun, no heavy grade. Real-time 24fps, 180° shutter. NOT 3D/game/cartoon.

SKIN / REALISM (hardest on @Image 2): both women read as real photographed humans — visible pores, peach-fuzz, subsurface translucency, asymmetry, true eye catchlights, flyaway hairs; matte, lived-in. NOT waxy/plastic/airbrushed/CGI/doll. Half-face in shadow, texture still readable.

FACIAL PERFORMANCE (both): both blink naturally and show live forehead/brow micro-expression (eyebrows lifting, knitting, relaxing, forehead creasing). No frozen, blank, or mask-like faces.

SCALE: the @Image 3 mech is 5 meters tall; Haru (~165cm) sits on its highest point. The @Image 6 monster is 2 meters.

LOCKS:

@Image 1 wardrobe: glossy nude-latex long-sleeve crop, bare midriff, khaki cargo (belt + knee straps), orange boots, holographic nose strip. NO harness/seatbelt/vest/straps on her torso.

Food (@Image 7): Korean fire-spicy ramen — vivid bright-red chili broth, glossy noodles, heavy steam. Not pale, not clear.

Vocals: non-verbal only (Reina's smoke-exhale + low hum; Haru's tiny "hmm… wow" + chewing). NO words.

NO interface anywhere — no reticle, crosshair, scope ring, HUD, UI, range numbers, targeting graphics in any shot.

@Image 3 5m mech sits on its butt with its cabin/cockpit facing the cliff edge (far back from the edge). Haru sits on top of the mech with her back to the cliff edge (facing the road). @Image 2 Reina is on the road side, looking down the road toward the cliff — sees Haru frontally. @Image 6 2m monster bleeds dark purple ichor, runs in from the cliff side straight at Haru's back. Continuity across cuts.


SHOT 1 — INT. CABIN, REINA SPRAWLED, SMOKING (handheld)

Inside @Image 4: @Image 2 sprawled languidly and sexily in her seat, smoking a lit cigarette, arrogant and in control. Front medium-close, camera LOW looking up at her to emphasize her pose, composition off-center. Hard shadows carve across her face, half in deep shadow; no sun, cold foggy light of location @Image 5 only, warm ember glow on lips/fingers. Slow blink, brow flick, long drag, smoke curls, low amused exhale. Audio: cockpit hum, cigarette crackle, slow exhale, low hum. HARD CUT.

SHOT 2 — SNIPER-RIFLE VIEW, NO INTERFACE (handheld)

What Reina sees through her sniper scope — completely clean, no interface of any kind (no reticle, crosshair, scope ring, HUD, range numbers, markers). First it holds @Image 1 in a tight close-up from a slightly high angle (looking gently down on her) as she sits on her @Image 3 mech in location @Image 5, happily eating red @Image 7 ramen. The close framing is achieved through long-lens reach, NOT proximity — extreme super-telephoto compression (≈8° FOV), camera very far away, background flattened into creamy soft bokeh, atmospheric haze, only Haru sharp; it reads as observed from a great distance, never like the camera is right next to her. Then the scope pulls/pans back a little from Haru, widening, revealing a @Image 6 2m monster running in fast behind her, straight at her back. Cold distant fog. Audio: wind, faint chitin scuttle building. HARD CUT.

SHOT 3 — INT. CABIN, REINA PRESSES THE BUTTON (handheld)

Back in @Image 4: @Image 2 still sprawled and unbothered, smug, half-lidded, cigarette in one hand. She calmly presses a single firing button with one gloved finger — no drama, pure cool. Same low angle, hard shadows on her face, cold foggy light of location @Image 5, ember glow. Audio: a soft button click, a heavy concussive rifle report + supersonic crack from outside, cabin rattle, slow smoke exhale. HARD CUT.

SHOT 4 — EXT. BRIDGE, HARU CLOSE (handheld)

In location @Image 5: tight on @Image 1 sitting on her @Image 3 (back to the cliff), eating red @Image 7 ramen, soft shadows on her face, blinking with live brow micro-expression. Behind her the @Image 6 2m monster is right on top of her, lunging in mid-air, about to land on her back — but it never reaches her: the AP round punches through it just short, bursting dark purple ichor, and the body drops and crashes. Haru hears it, calmly turns to look behind her at the downed monster while still chewing — chopsticks in hand, cheeks full of noodles — shows no surprise at all, a tiny "hmm… wow," then turns back and keeps eating, unbothered. Cold overcast light, warm steam pocket on Haru. Audio: leap-hiss cut short, wet airborne punch-through + body crash + ichor splatter, Haru's small "hmm… wow" through a full mouth, continued chewing, wind. END on her eating.
```
