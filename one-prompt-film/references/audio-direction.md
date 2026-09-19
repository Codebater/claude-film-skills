# Audio direction — supervising sound editor, music supervisor, dialogue director, re-recording mixer

Audio is not an afterthought bolted onto a finished picture: every production is a synchronized audiovisual piece. This layer plugs in at two points: the **master audiovisual timeline** is designed *during* the direction pass (audio decisions shape cuts and camera), and the **audio production pipeline** runs *after* Seedance generates the picture.

## 1. Master audiovisual timeline (design-time, with the director)

While the editor pass decides cuts, decide sound in the same breath — the two must influence each other:

- A notification ding can set the exact frame of a reaction shot. A bass hit can motivate a hard cut. A riser can accompany a camera push. Music can stop dead one beat before the joke. A door slam can *be* the transition. Footsteps can establish rhythm before music enters. The product reveal can own a sonic motif.
- Think in layers, each with its own timeline: **VISUAL** (action/camera/cuts) · **DIALOGUE** (lines, reactions, breaths, timing) · **AMBIENCE** (room tone, city, wind, office hum) · **FOLEY** (footsteps, cloth, objects, phone handling) · **HERO SFX** (notifications, product sounds, UI, impacts) · **TRANSITION SFX** (whooshes, risers, reverses — sparingly) · **MUSIC** (structure, builds, drops, ending) · **SILENCE** (deliberate gaps: comedy, tension, anticipation) · **SONIC BRANDING** (logo sting, reveal signature).
- Write it as one timeline with second-level marks, e.g.:

```
0.0-4.0  VISUAL locked wide, failed deploy | AMB office hum, night | MUSIC none yet
2.8      SFX error blip (hero) — motivates the deflate
4.0      CUT hard | MUSIC waltz enters WITH the cut (sound bridge: last error blip decays over it)
4.0-8.0  VISUAL grandma | DIALOGUE line starts 5.2 | AMB clock + budgie
11.2     SFX ding — lands exactly on the tea-blow; MUSIC drops to near-silence 11.0-11.6
16.0     MUSIC stops dead | SILENCE 0.4 | SFX can drop 16.4
18.0     SONIC BRANDING sting under logo assemble | VO 18.2
```

Timing is designed for the piece's actual duration. **Do not fill every second** — decide what the audience should hear *right now*; everything else supports that focal element.

## 2. Commercial sound grammar (use when it improves the film, never mechanically)

- **Pre-lap / J-cut**: next scene's audio enters before its picture. **L-cut**: outgoing audio continues across the cut. **Sound bridge**: one sound connects two locations. **Matched audio cut**: a sound morphs into a similar sound across the cut (kettle whistle → train whistle).
- **Rhythmic editing**: cuts on musical or foley beats. **Hard audio cut**: sudden intentional silence — the strongest attention magnet available.
- **Micro-SFX**: tiny tactile sounds (cloth, fingertip on glass, cup set down) are what make footage feel expensive and physical.

## 3. Sound aesthetic

Tactile, cinematic, spatial, restrained, believable. A luxury spot must not sound like a YouTube intro; comedy runs on timing and silence, not cartoon SFX; tech avoids generic futuristic beeps unless creatively justified; documentary keeps natural imperfections. **Hierarchy over density**: never a WHOOSH/BOOM/DING on every action. Match the sound language to the direction pass's genre grammar.

## 4. Native Seedance audio: KEEP / ENHANCE / REPLACE / LAYER

Always generate the Seedance video with native audio (`generate_audio: true`) — it is a synchronized performance reference even when it will be replaced. After generation, extract and listen (`ffmpeg -i film.mp4 -vn audio.wav`, or just play the file), then decide per element:

- **KEEP** — native audio is genuinely good (often: ambience, synced foley, natural performance). Don't replace good audio out of principle.
- **ENHANCE** — keep native as the bed, add hero SFX / music / sonic branding on top (`native.mode: "layer"` with a modest negative gain).
- **REPLACE** — native dialogue is off-voice or mushy, music is generic: rebuild those stems externally (`native.mode: "replace"`; regenerate what's lost, e.g. ambience).
- **LAYER** — keep native at low gain purely as glue/room tone under a full external mix.

The commonest professional outcome: keep native ambience+foley, replace dialogue/VO and music, add hero SFX and the brand sting.

## 5. ElevenLabs stem generation (`scripts/eleven_audio.py`, needs `ELEVENLABS_API_KEY`)

One call per stem — keep stems separate for mix control; never bake everything into one generation when individual control is better.

- **Dialogue / VO**: `eleven_audio.py dialogue --text "..." --voice <name|id> --performance "quiet, restrained authority"`. Direct it like an actor: character, age impression, emotion, intensity, pace, distance, whisper/shout. `--model eleven_v3` renders the performance note as an audio tag for more expressive takes; default `eleven_multilingual_v2` is the reliable workhorse. `list-voices` shows the cast. Dialogue must sound performed, not read — if a take reads flat, change the performance note or voice, don't just re-roll.
- **SFX / Foley / Ambience**: `eleven_audio.py sfx --prompt "..." --duration 1.2`. Describe the **acoustic result**, not a label: not "phone sound" but "single premium smartphone notification, short crystalline digital tone, extremely clean transient, no reverb, modern luxury technology commercial". `--loop` for seamless ambience beds.
- **Music**: `eleven_audio.py music --prompt "..." --duration 18`. Describe genre, instrumentation, tempo, emotional arc, structure and — critically — **where it must move**: "builds until 14s, cuts to silence, one final warm chord at 17s". Score the timeline, don't order wallpaper. Music length ≥ 3 s.

## 6. Audio manifest (machine-readable; executed by `scripts/mix_audio.py`)

```json
{
  "native": {"mode": "layer", "gain_db": -8},
  "assets": [
    {"file": "amb_office.mp3", "type": "ambience", "start": 0, "gain_db": -26, "fade_in": 0.3},
    {"file": "vo_grandma.mp3", "type": "dialogue", "start": 5.2, "gain_db": -1},
    {"file": "ding.mp3", "type": "sfx", "start": 11.2, "gain_db": -9},
    {"file": "score.mp3", "type": "music", "start": 4.0, "gain_db": -14,
     "fade_in": 0.2, "fade_out": 0.5, "trim_end": 14.0}
  ],
  "music_duck": {"enabled": true},
  "loudnorm": {"i": -16, "tp": -1.5, "lra": 11}
}
```

Types → buses: `dialogue`/`voiceover` → DIALOGUE bus; `music` → MUSIC bus; everything else (`ambience`, `foley`, `sfx`, `transition`, `branding`) + native bed → FX bus. The mixer positions/trims/fades stems, **auto-ducks music under the dialogue bus** (sidechain), limits, loudness-normalizes (-16 LUFS web default; -14 for pure social delivery), pads/cuts to the video length, and muxes with the video stream copied. Dialogue stays the most intelligible element by construction — set gains so it wins before ducking, not because of it.

Rough gain staging start points (dB, pre-mix): dialogue/VO 0 to -3 · hero SFX -6 to -12 · music bed -12 to -18 · ambience -22 to -30 · micro-foley -18 to -24. Trust ears over numbers.

## 7. Audio QC (before delivery)

Extract the mixed audio and listen (or at minimum inspect the mixer's loudness report + waveform). Check: every important line intelligible? dialogue sounds like the character? competing sounds? does music support the story and end *with* the picture (no abrupt tail-cut)? SFX actually on their sync frames? enough quiet? physically believable space? clipping (mixer's limiter should prevent it — verify True Peak ≤ -1 dBTP)? correct sonic ending on the final frame? If something fails, fix the *stem or its manifest entry* and re-mix — the mix is cheap, regeneration is not.

## 8. Pipeline placement

```
direction pass  ──►  master AV timeline (this file §1) — feeds shot design AND the manifest
seedance generate (native audio ON)
native audio analysis  ──►  KEEP / ENHANCE / REPLACE / LAYER
eleven_audio.py per stem (dialogue, VO, ambience, foley, SFX, music, branding)
manifest.json  ──►  mix_audio.py  ──►  QC  ──►  (flim grade)  ──►  deliver
```

Grade (flim) after the mix — the grade touches only video, the mix only audio, so order is free; doing the mix first means QC hears the final file. The user gives one idea; the audio director infers the rest — they should never need to specify sounds for the system to produce a designed soundtrack.
