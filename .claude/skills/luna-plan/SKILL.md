---
name: luna-plan
description: Turn a picked Luna Upcycles idea into a complete, production-ready video plan — story beats, a hero image, every stage image (start/end frames) and every Veo clip prompt, written to the realism playbook and ready for Google Flow. Creates the project folder projects/NNN-slug/ with plan.md and edit.json. Use when the user says "plan idea #N", "plan the kitten igloo", "make the plan", "let's do idea X", "write the prompts", or runs /luna-plan. Planning only — never generates images or video (that is /luna-generate).
---

# Luna Plan

Takes **one idea** and turns it into a plan. The next skill
(`/luna-generate`) can run that plan in Google Flow without making any
decisions of its own. This skill writes files only. It never generates
anything.

The user should not need to explain anything. Everything you need is in this
file, the project folder and `plan-template.md` next to this file.

## 0. Which idea?

- The user names it ("idea #2", "the kitten igloo"): find it in the newest
  `ideas/shortlist-*.md`.
- The user describes a new idea in their own words: use that, but run it
  through the idea checks in step 2 first.
- Nothing given: show the top 3 `proposed` ideas from `ideas/log.md` and ask
  which one.

## 1. Load context (always)

Read these before writing anything:

- `brand/luna.md`: Luna's **exact** description. Copy it word for word.
- `brand/locations.md`: pick the idea's location and copy its prompt text
  word for word into every prompt, replacing the cottage garden text. One
  location per video. Use wider full-body framing for big builds.
- `brand/realism-playbook.md`: **every** prompt follows its image recipe,
  video recipe, banned words and checklists.
- The idea's row in the shortlist, plus the reference videos listed there.
- `ideas/log.md`: why earlier ideas were rejected, so you don't repeat those
  mistakes.

## 2. Lock the concept

Work **result first**. Lock the beautiful finished piece, then confirm the
object makes exactly that shape. If it doesn't, change the **object**,
never the result.

Before writing prompts, write the concept in these lines, in this order:

- **Finished piece:** what it is, its size, materials and finish. This is
  the HERO, and the thing the video sells.
- **Junk:** the object whose own shape makes that piece, its real size,
  and how it looks at the start (scuffed, dirty, used).
- **The junk's job:** how its shape is still visible and useful in the
  finished piece.
- **Shape test:** the junk's outline with its real size, plus the concrete
  thickness, must give the finished piece's outline and size. Example:
  "jug 27 × 48 cm cylinder on its side + 3 cm concrete → 33 × 54 cm
  barrel". If the numbers or outlines don't match, the concept fails.
  (010's first version failed: a long jug became a round igloo.)
- **Placement:** exactly where the finished piece lives in its reveal place,
  and why a real designer would put it there (see section 2b).
- **Ending:** which ending style closes the video (see section 2c).

Check the concept against these hard rules. If one fails, fix the concept
before going further:

1. The process is physically real: actual DIY steps, real materials, a
   sensible order (mould → pour → cure → unmould → finish → place).
2. Concrete stays concrete. The final paint must never make the piece look
   like the original junk again.
3. One build location plus one reveal location per project, from
   `brand/locations.md`. Never change place inside a clip: the reveal gets its
   own hero (`H-reveal`) and its own clip. For a compilation, plan each
   project as a block (hero + 3–4 frames + 3–4 clips, about 11 s used) inside
   one plan.md.
4. Only one of the piece appears, unless a finale shot deliberately shows
   more.
5. **Shape continuity in the frames.** In every stage image, the piece's
   outline must follow from the image before it: same length, same
   orientation, same opening position. Check this again on the generated
   frames, in the contact sheet, before asking the user to approve them.

## 2b. Placement check (required)

The final shot has to show the piece **where it really belongs**. Rejected
example: 015's first version stood the bench alone in the middle of a villa
lawn, facing the house. Nobody puts a bench there.

Write the placement in one sentence and check it against these rules:
1. **It has a job there.** A bench faces a view, a fire pit or a path; a lamp
   hangs over a bed or a table; a vase sits on a console; a planter flanks a
   door; an aquarium sits against a living-room wall.
2. **It has a backdrop.** It sits against a hedge, a wall, a railing or
   furniture, or in a deliberate spot like the end of a path or the edge of
   a terrace. Never floating in an open middle.
3. **It's dressed for its setting.** Add 2–3 real context items (cushions, a
   throw, potted olive trees, a rug, a drink, books, plants), chosen to match
   the location, so the result reads as "lived in".
4. **Scale and contact are right:** the true size next to the setting, with
   contact shadows, and nothing that blocks the piece.
5. **The camera makes the piece the subject:** it's framed by the setting,
   not lost in it. Show it big enough to read its detail.

If the placement fails, change the placement (or the reveal location),
never the piece.

## 2c. Ending styles (vary them)

Pick one per video. Read the `end:` tags of the last 3 made or picked videos
in `ideas/log.md`, and **don't repeat the style of the previous video**.
Luna is in the final frame **at most every other video**.

| Key | Ending | How to make it |
|---|---|---|
| `orbit` | The camera circles the finished piece in its place; no person | Start from the hero without Luna; handheld or gimbal arc, one continuous move |
| `pull-back` | Starts close on a detail, pulls back and up to show the whole luxury setting | Start on a detail frame; the clip ends wide (end frame = the wide hero) |
| `use` | Someone uses it: sits, puts a drink down, places a plant, a pet settles | Luna, a guest or an animal; one action |
| `lights-on` | Static wide shot; the lights come on or day turns to dusk | Start and end frames are the same framing, lights off → on |
| `walk-away` | Luna walks out of frame; the piece stays, beautifully placed | End frame without Luna |
| `match-cut` | The same framing cuts from the junk or empty spot to the finished piece | Two frames with identical framing; the edit cuts between them |

## 3. Story beats (16–30 s final video)

| Beat | Time | Content |
|---|---|---|
| **Hook** | 0–2 s | Either a flash of the finished piece with the animal, or the problem in a story idea (kitten shivering in the rain) |
| **Junk** | ~2 s | The raw junk on the workbench, so it's recognisable |
| **Build** | 10–18 s | 4–6 steps, **one physical action each** |
| **Reveal** | ~2 s | The finished piece in place |
| **Ending** | 3–5 s | The chosen ending style (2c), in the checked placement (2b). This is the shot people rewatch |

Plan **6–8 clips** in total. Each clip is 8 s in Veo, but only 1.5–3 s of it
ends up in the edit.

## 4. Frames: build them from the hero, never chain them

Write the image prompts in this order:

1. **HERO.** The finished piece in its checked placement (2b), dressed for
   the setting, as the chosen ending needs it (with or without Luna), made
   with the playbook's full image recipe. Every other reveal image is built
   from it. If the build place differs, make a separate build anchor
   (`B-hero`) from the hero's piece, with the hero attached as a reference
   so the piece is identical.
2. **Stage images (S1…Sn).** Each one is a single edit of the HERO. Use the
   playbook's lock sentence, then describe the **whole state** of that stage
   in that one edit ("the piece is raw grey concrete, still in the mould,
   Luna is…").
   - **Never edit an edit.** At most one extra edit on top of a stage image,
     for a pose change only.
   - If a stage is too far from the HERO (raw junk on the workbench, for
     example), make it from an earlier stage image, but only once, and say
     so in the plan.
3. Give every image a file name: `H-hero`, `S1-junk`, `S2-cut`, … These
   become the filenames the generate step saves and uploads.

Each image needs:
- **Model:** Nano Banana **Pro** for anchors (heroes / build anchors), Nano Banana 2
  for stage edits; 9:16, x1 (see playbook §6 Quality)
- **References:** `brand/luna-sheet.png` for Luna. Add `brand/luna-garden.png`
  for the HERO only, since stage images inherit it.
- **Source:** `new` (HERO only) or `edit of H-hero`

## 5. Clips: one action each, start + end frame

Each clip goes **from one stage image to the next**:
`C1: S1 → S2`, `C2: S2 → S3`, … then `Cn: reveal → H-hero (payoff)`.

Write each video prompt with the playbook's video recipe: CAPTURE · ACTION ·
STABILITY · LOOK · AUDIO · EXCLUDE.
- **One verb-action.** Never use "then" or "and then". If you need two
  actions, make two clips.
- Describe the end state so it matches the end frame.
- **Framing for detail:** medium shots for build steps, close-ups for material
  moments (pour, texture, glow), at most one wide shot per project. AI video
  loses detail when the subject is small in the frame.
- Tripod and fixed framing for build steps. The ending follows its style
  (2c): an orbit, a pull-back, a static lights-on shot, and so on.
- Under ~120 words.
- **Resolution:** every clip at **1080p** (written into MANUAL.md as "set
  before you generate").
- **Model:** Veo 3.1 Fast (20 credits). Mark the payoff clip
  *"Quality if budget allows (100 credits)"*.
- Note the time skips that happen between clips (curing, drying). The edit
  hides them with a cut.

## 6. Write the project folder

1. **Pick the project number.** Use the next free number after the highest
   one in `projects/` (numbers 003–009 were used before the restart, so never go below 010). Slug it, e.g.
   `010-kitten-igloo`.
2. **Create the folders** `projects/NNN-slug/`, with `frames/`, `clips/` and
   `output/` inside.
3. **Write `plan.md`** using `plan-template.md` (next to this skill file).
   Fill in every section, with no placeholders left.
4. **Write `edit.json`** in the format `tools/assemble.py` reads:

   ```json
   {
     "output": "output/final.mp4",
     "music": "music/<pick a track from music/ that fits the mood>",
     "music_db": -18, "clip_db": -2, "grain": 5,
     "logo": "brand/logo.png", "logo_y": 0.10,
     "hook": {"text": "<4-6 words that stop the scroll, e.g. She was freezing in the rain…>", "end": 2.4},
     "loop": 0.4,
     "segments": [
       { "clip": "clips/C6.mp4", "start": 3.0, "end": 4.5, "label": "HOOK: …" },
       { "clip": "clips/C1.mp4", "start": 0.5, "end": 2.5, "label": "…" }
     ]
   }
   ```

   `hook` is the on-screen caption for the first 2.4 s: most people scroll on
   mute, so these words decide the swipe. Write the problem ("They had nowhere
   to swim…") or a promise ("Wait for the peel…"); no emoji. `loop` dissolves the
   ending into the opening frame so the Short replays seamlessly.
   Trim times are first guesses. The assemble step fixes them after looking
   at the real clips.
5. **Update the log.** In `ideas/log.md`, set the idea's status to `picked`,
   note the project folder, and add `end:<style>` to its tags.

## 7. Self-check before showing the user

Go through the plan and confirm every item:

- [ ] Luna's description and garden are copied exactly from `brand/luna.md`
- [ ] None of the playbook's banned words (cinematic, stunning, 8K, …)
- [ ] Every stage image is one edit from the HERO, with no chains
- [ ] Every clip has exactly one action, and its start and end frames exist
      in the image list
- [ ] Object sizes, colours and shapes are written the same way in every
      prompt
- [ ] The junk is still recognisable and has a job
- [ ] Placement passes 2b: it has a job, a backdrop and dressing, and is framed as the subject
- [ ] The ending style differs from the previous video's; Luna isn't in the last frame two videos running
- [ ] Every clip prompt has the EXCLUDE line (no music, voices or text)
- [ ] MANUAL.md settings line says 1080p set before generating, and Veo Quality for the reveal
- [ ] Credit estimate: images + (clips × 20) + payoff upgrade

## 8. Report to the user

Keep it short:
- the concept (4 lines)
- the beat list, one line per clip
- the credit estimate
- the link to `plan.md`

Then ask the user to approve the plan, or say what to change. When they
approve, the next step is `/luna-generate`. Don't start generating yourself.
