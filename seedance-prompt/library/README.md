# Exemplar library

Real production prompts, kept verbatim, each annotated with the devices it contributed to
[`../references/techniques.md`](../references/techniques.md). The catalog is the distillation; this
folder is the evidence. When they disagree, the evidence wins and the catalog gets corrected.

| id | Piece | Shape | Contributed |
|---|---|---|---|
| [001](001-mech-sniper-ramen.md) | Mech / sniper / ramen — 4 shots | one generation, `HARD CUT.` between shots | travelling scale · geometry map · optics-not-proximity · LOCKS · paired negatives · pore list + shadow conditional · non-verbal vocals · non-reaction playing · miss-as-event |
| [002](002-sofa-scene-mira-harumin.md) | Sofa scene, Mira & Harumin — 3 shots | shot series under one shared bible, three generations | the series bible · labelled shot sub-schema · identity strings · signature detail · context variants · voice casting · two-face location plating · accent doctrine · redundancy budget · dialogue split across the cut |
| [003](003-the-inside-curved-world.md) | THE INSIDE (ours) | single 15 s oner | physics clause · overall-requirements tail · asset binding by channel · material truth as a positive — **and** the gap analysis that motivated this skill |
| [004](004-noodle-prep-five-segments.md) | Noodle prep on the mech — 5 segments | one generation, controlled multi-shot sequence | **frame coordinates · lens lock in degrees · camera distance in metres · FIRST FRAME block · physics manifest** · scene-context preamble · channel exclusion · fidelity clause · scoped exception · specify-the-boring-parts · positive-locks recap |
| [005](005-mecha-vs-bug-oner.md) | Mecha vs bug, through-the-body — ~10 s | one unbroken take, six numbered camera beats | **named asset handles** · behaviour lock · anti-affordance clause · focal rack as a curve · numbered camera beats · scoped slow-mo · enumerated absolute colour rule · declared absence with a reason · `nothing floats` |
| [006](006-fregio-everywhere-commercial.md) | FREGIO "Everywhere" (ours) — 28 s | single generation, tonal hard cut at 23 s | **all of §9 commercial dramaturgy** — product-as-motif · deliberate un-readability · motivated transitions · music-stop as payoff · tonal hard cut · one-line-of-dialogue · benefit as a facial flip — **plus the corpus's only verified failure**, with both frames as evidence |

**004 and 005 changed house doctrine in two places:** named semantic handles replaced positional
`@Image N`, and the locks recap moved from before the shots to after them (bracketing the piece).

**006 is the one to read first when a generation comes back wrong.** It is the only entry with the
prompt, the failed output, the diagnosis and the fix all in one place.

## Adding one

Procedure in [`../SKILL.md`](../SKILL.md), section "Ingesting a new exemplar". In short: save the
prompt verbatim, list only what is *new*, promote each new device into the technique catalog with a
verbatim quote and an exemplar id, record contradictions rather than resolving them silently, and
update the table above.

Capture alongside the prompt, when known: whether it shipped, how many re-rolls it took, and which
constraint failed first. [006](006-fregio-everywhere-commercial.md) is the template — prompt, a
frame from the failed output, the diagnosis, the fix plate, and the version count. 001–005 still
carry none of that; adding it to any of them is the cheapest improvement available here.

Evidence frames live in [`assets/`](assets/), named `NNN-<what-it-shows>.png`.

**Save the repair prompt, not just the repaired clip.** When a beat gets re-generated, write the new
prompt next to the output. `[006]`'s fix prompt was never saved, so the wording that actually worked
is gone and the diagnosis had to be reconstructed from a plate, some durations and file timestamps.
The prompt that fixes a failure is worth more to this library than the one that caused it.

## Recorded contradictions

Kept rather than resolved, because two shipped productions disagreeing is information:

- **Negatives.** Official guide restricts them to subtitles and audio; every exemplar uses them for
  category/material/object exclusion, always after the positive, never against an event.
  (techniques §6.2–6.3)
- **Timestamp granularity.** Official guide requires integer seconds; `[005]` uses half-seconds to
  fit six camera beats into a 10 s oner. (library/005, "Recorded contradiction")
- **Lock placement.** `[001]` before the shots, `[004]` after. Resolved into a house rule rather
  than a winner: identity/scale/geometry above, locks recap below. (techniques §6.11)

## Wanted

Gaps in the corpus — exemplars that would teach something none of the current six can:

- A **transformation** — morph, destruction, weather turn, time-lapse. `[005]` covers kinetic
  action and a pass through an interior, but nothing here changes state.
- A **long dialogue scene** with real lip-sync load. `[002]` splits one sentence across three
  4-second shots; nothing tests a sustained conversation.
- **More failures.** `[006]` is one data point. Two more would let us tell which constraints fail
  *often* from which failed *once*.
- A **hero-product commercial** where the product is on screen. `[006]` deliberately never shows
  it, which is a strategy, not a general solution — nothing here handles a packshot, a texture
  beat, or a product as the turn.

## Closed gaps

- ~~product / commercial spot~~ → `[006]`
- ~~a prompt that failed, with the output described~~ → `[006]`, with frames
