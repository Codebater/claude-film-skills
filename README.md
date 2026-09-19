# AI Film Skills for Claude Code

Three [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) for
making video with an AI model that doesn't know how film works.

The models are good enough now that the bottleneck isn't the generator — it's the prompt
and the dramaturgy. These skills are the accumulated fixes: what actually keeps a face
consistent across shots, what kills the slow-motion tell, why your second act is boring
and what to do about it.

| Skill | Use it when |
|---|---|
| [`one-prompt-film`](one-prompt-film/) | "Make a video of X" → finished film. The whole pipeline: story, storyboard, direction, prompt, generation, grade. |
| [`seedance-prompt`](seedance-prompt/) | The prompt text itself. Write one, repair one, or work out why a generation came out wrong. |
| [`motion-ui-video`](motion-ui-video/) | UI motion, not camera film. Animated React scene → deterministic frame capture → mp4. |

---

## Install

Copy the skill directories into your project's `.claude/skills/` (or `~/.claude/skills/`
to use them everywhere):

```bash
git clone https://github.com/<you>/claude-film-skills.git
cp -r claude-film-skills/one-prompt-film  .claude/skills/
cp -r claude-film-skills/seedance-prompt  .claude/skills/
cp -r claude-film-skills/motion-ui-video  .claude/skills/
```

Claude picks them up from the description — you don't have to name the skill. "Make me a
30-second commercial for X" routes to `one-prompt-film` on its own.

---

## one-prompt-film

Idea → finished film, in ten steps that each refuse to move on until the previous one is
actually good:

```
0  Story capture & scope          trailer or packed short?
1  Dramaturgy gate                the step that kills bad ideas before they cost money
2  Storyboard & continuity plates GPT Image boards; character/world plates locked
3  Direction pass                 director + DP + editor, with technique research
4  Production analysis            per the Seedance 2.5 guide
5  Compose the prompt             hands off to seedance-prompt
6  Generate                       ModelArk API, Higgsfield MCP fallback
7  Audio production               VO, mix
8  Optional flim grade            filmic colour
9  Deliver
```

The **dramaturgy gate** is the part that matters most and the part every other
prompt-engineering guide skips. A technically flawless generation of a boring idea is a
boring video, and you will have paid for it. The gate evaluates the premise against both
film and commercial storytelling before a single frame is rendered.

Continuity plates are the second load-bearing idea: characters and worlds are pixel-locked
into reference plates once, then reused, rather than re-described per shot and drifting.

**Reference material** — `references/`: `dramaturgy.md`, `directing.md`, `storyboard.md`,
`continuity.md`, `seams.md`, `audio-direction.md`, `seedance-25.md`.

**Scripts** — `scripts/`: `seedance_generate.py`, `flim_grade.py`, `signature_look.py`,
`eleven_audio.py`, `mix_audio.py`.

**Needs** — `ARK_API_KEY` (BytePlus ModelArk) for generation, `ELEVENLABS_API_KEY` for
voice. The grade step is optional.

---

## seedance-prompt

A production dialect for Seedance 2.5 prompts, distilled from prompts that actually
shipped rather than from the docs.

The house schema: bible header, asset legend, `LOCKS`, scale, geometry map, then per-shot
`LOCATION MAP` / `FORMAT MODE` / `OPTICS` / `CAMERA` / `ACTION TIMING`.

Two things make it work:

**The six drift classes.** Identity, scale, geometry, optics, lighting and time each drift
independently, and each needs its own explicit restatement. Handling them as one "be
consistent" instruction is why characters change height between shots.

**The anti-tells.** Named, specific rules against the frozen face, waxy skin, unrequested
slow motion, dead-centre framing and wrong-scale subjects — the five things that make a
generation read as AI at a glance.

There's also a **redundancy budget**: a prompt has finite attention, and spending it on
restating the things that actually drift beats spreading it evenly. And an audit step to
run *before* you spend a generation.

`library/` holds annotated exemplars from real productions, each with a note on what it
teaches. New prompts get ingested there through a documented procedure, so the skill
gets better as you use it.

---

## motion-ui-video

Different problem: not camera film, but UI in motion — a counter ticking up, a radial
menu opening, a liquid button rippling. B-roll for a launch post.

```
idea → animated React scene from animate-ui's registry
     → choreograph on a timeline
     → deterministic frame-by-frame Playwright capture
     → ffmpeg → mp4
```

Frame-by-frame rather than a screen recorder, so the result is smooth regardless of
machine load and identical between runs. Two pipelines share the skill: `record.mjs`
when the shot needs **real input driving real state** (a cursor clicking an actual
button, typing that actually flips state), HyperFrames when it doesn't.

`references/`: `catalog.md` (the component registry), `recording.md`,
`apple-motion-hig.md`, `hyperframes.md`.

---

## A note on the exemplar library

`seedance-prompt/library/` holds annotated prompts from real, shipped productions rather
than invented examples. That is what makes it useful and it is also the thing to check
before pushing: each exemplar names a real production. Ship the ones you have the rights
to show.

---

## License

MIT. See [LICENSE](LICENSE).

Seedance, ModelArk, ElevenLabs, flim, animate-ui and HyperFrames are separate products
with their own terms. These skills are instructions for using them, not redistributions.
