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
- `brand/growth-playbook.md`: the researched rules R1–R10 (opening, pace,
  reason, ending, formats). Section 3 below applies them.
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
- **Format:** Quick build (11–25 s), the default. Big transformation
  (45–60 s) only when the user asks. See section 3.
- **Opening action:** what Luna is already doing in frame 0, and the first
  tool-on-junk contact that has started by 1.0 s. It must be step one of the
  build, and it must be striking. If step one is dull, change the build.
- **Reason:** who or what the piece is for, shown in one beat without words
  (a pet with no bed, a guest with nowhere to sit, a dull corner), and how
  the ending closes it.

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

**Use beat (required, growth rule R6).** Whatever the ending style, the
last 3–4 s include someone using or reacting to the piece: Luna, a guest, a
child or a pet (rotate them). With a travelling ending that has no person
(`orbit`, `lights-on`, `pull-back`), put a 1.5–2 s use beat just before the
travel. The travel itself is at most 3.5 s in the edit.

| Key | Ending | How to make it |
|---|---|---|
| `orbit` | The camera circles the finished piece in its place; no person | Start from the hero without Luna; a smooth steady arc, one continuous move, no shake |
| `pull-back` | Starts close on a detail, pulls back and up to show the whole luxury setting | Start on a detail frame; the clip ends wide (end frame = the wide hero) |
| `use` | Someone uses it: sits, puts a drink down, places a plant, a pet settles | Luna, a guest or an animal; one action |
| `lights-on` | The lights come on at dusk while the camera glides forward along the piece through the place (not locked, not a zoom) | Start frame only (lights off, at the near end of the piece); **no end frame**, because the same framing at both ends locks the camera. The travel and the lights going on go in the prompt |
| `walk-away` | Luna walks out of frame; the piece stays, beautifully placed | End frame without Luna |
| `match-cut` | The same framing cuts from the junk or empty spot to the finished piece | Two frames with identical framing; the edit cuts between them |


## 2d. Camera language (required: the video must be ready to publish without extra editing)

Real DIY Shorts aren't one fixed wide shot. Every plan includes:

1. **Insert close-ups: 2–3 per project** (1 per project in a compilation),
   on the most satisfying details: a blade cutting, a trowel digging, hands
   lowering or pressing something, a pour, a texture being smoothed, glass or
   gravel close up.
   - Each insert is its own clip with its own start frame `In-<name>`.
   - That frame is **one edit of the stage frame it belongs to**: "the same
     moment seen as a macro close-up from about 30 cm, shallow depth of field,
     same light and materials". This is allowed on top of a stage frame.
   - In the edit, an insert sits between the wide shots of that step and is
     usually 0.6–1.2 s.
2. **Camera move per clip type** (write it into the CAPTURE line of the video
   prompt):

   | Clip | Camera |
   |---|---|
   | Build step (wide) | Tripod, fixed framing |
   | Insert | Macro close-up on a tripod, camera still; only the **focus shifts** from foreground to the detail. No zoom, no shake |
   | Human moment (planting, placing, reacting) | Tripod, still camera (or cut to an insert for the detail). **No handheld, no shake** |
   | **Ending** | **Always a camera move that shows the place:** the camera itself travels (gimbal walk forward along the piece, pull-back and rise, or orbit) so the viewer sees the whole setting around the piece: house, terrace, lawn, hedge, room. A static ending only for a deliberate match-cut |
   | Lights-on | The lights come on **while the camera travels** along the piece through the place, not a locked shot |

   **Ending move: show the place, don't inspect the piece.** The last move
   starts at one end of what she built and travels all the way to the other
   end, so the viewer sees the whole environment she made. It moves *through* the setting, like walking down the garden path with a
   gimbal: the piece passes under the camera, and the house, lawn and hedge
   open up. Never:
   - a zoom or push-in onto the piece (it looks like checking a detail)
   - **any shake**: handheld wobble, jitter or peeking around. The move is
     smooth and steady from the first frame to the last, like a gimbal or a
     slider
   - a locked tripod shot
   Give a travelling ending a **start frame only** (or an end frame that is
   clearly wider or further along). Never the same framing at both ends:
   that forces Veo to hold the camera still.

3. **Prompt vocabulary for Veo** (no "slowly"; use "gentle", "steady",
   "smooth"):
   - "the camera glides smoothly forward, low along the whole border toward the hedge, revealing the garden and the villa" (ending)
   - **Never write "gimbal", "stabiliser", "rig" or "phone" in a video prompt.** Veo puts the gear in the shot (019 C8 showed a phone on a gimbal). Describe only how the view moves, and end every moving prompt with "No camera equipment in the frame."
   - "camera pulls back and rises to reveal …"
   - "steady orbit around …"
   - "macro close-up, shallow depth of field, focus shifts from … to …"
4. The **reference ending** in `/same-idea` is copied as a camera move (the
   analysis tool measures it). Never replace a moving ending with a static
   one.

## 3. Story beats (from `brand/growth-playbook.md`)

**Pick the format first.**

| Format | Final length | Beats | Clips | Use for |
|---|---|---|---|---|
| **Quick build (default)** | 11–25 s | 8–14 | 6–9 | one object or one corner, every step shown fast |
| **Big transformation** (only when the user asks) | 45–60 s | 20–30 | 12–16 | a whole room, yard, terrace or wreck, with a reason |

A **beat** is one visible change, 1–2 s long. One 8 s Veo clip usually
gives 1–3 beats (use 2–3 short trims from a clip, never one long trim).

| Beat | Time | Content |
|---|---|---|
| **Open** | 0–1.5 s | **Luna already in action** on the junk or the empty place: movement within 0.5 s, first tool-on-junk contact by 1.0 s. For a reason-led video, the problem beat goes here instead. **Never the finished piece** |
| **Reason** | 1.5–3 s inside the first 4 s | Who or what it is for, shown without words. May be the Open itself |
| **Build** | the middle | Quick: 5–11 beats of 1–1.5 s, every real step shown. Big: 16–24 beats. **One physical action each**, a visible change every 1–2 s, inserts on the most satisfying moments |
| **Reveal** | ~1.5 s | The finished piece in place. Its first appearance in the video |
| **Use** | 1.5–2 s | Someone uses it or reacts. This closes the reason |
| **Ending** | at most 3.5 s | The chosen ending style (2c) in the checked placement (2b) |

**Pace rules.**
- No shot longer than 2.5 s in the edit. The only exception is a
  fixed-camera time-lapse clip in which something new appears every second.
- The finished piece is not shown before the last third.
- The story stays in order. The opening is step one of the build, already
  in motion.
- Every beat has its own clear sound (see the AUDIO line in section 5).

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
- **Check / Focus / Same size as lines** (required, written right under the
  Source line; `tools/review.py` reads them and builds the logic check):
  ```
  **Check:** <3–6 facts that must be true in THIS frame, joined with " · ">
  **Focus:** x0, y0, x1, y1   (fractions of the frame: the area that proves the facts)
  **Same size as:** <the anchor this frame's piece must match in size and spot>
  ```
  Write the facts from the story logic, not the look: where the material
  goes and where it must NOT go ("the stream lands in the channel, never in
  the open centre"), what is open, empty or full, how many walls, rings or
  parts there are ("exactly one inner wall per loop, nothing else inside"),
  which tool is in her hands and which is not, and what must already have
  happened or must not have happened yet. Anchors get Check and Focus too.
- **Model:** Nano Banana **Pro** for anchors (heroes / build anchors), Nano Banana 2
  for stage edits; 9:16, x1 (see playbook §6 Quality)
- **References:** `brand/luna-sheet.png` for Luna. Add `brand/luna-garden.png`
  for the HERO only, since stage images inherit it.
- **Source:** `new` (HERO only) or `edit of H-hero`

## 5. Clips: one action each, start + end frame

Each clip goes **from one stage image to the next**:
`C1: S1 → S2`, `C2: S2 → S3`, … then `Cn: reveal → H-hero (payoff)`.

**Start and end frames must tell the clip's story, nothing else** (user, 2026-11-14):
- **The first frame is the empty place plus the junk in Luna's hands**, e.g.
  a bare wall while she carries the tyre. Never start with the junk already
  in position.
- **An end frame shows only the result of that clip's action**, with the
  tool from that same action. If the next step needs a new tool or material
  in her hands (a plank, a brush, a reel), give the next clip **its own start
  frame**. The cut hides the swap. Never put the next step's tool in an end
  frame, or Veo morphs one action into the other.
- So a clip is a **pair**, `Ck: Ak-start → Ak-end`. Reuse the previous end
  frame as the next start only when her hands hold the same thing.
- **An insert sits inside its own step**: wide start of the step → insert
  close-up → wide end of the same step. It must not show something that
  happens after the next wide clip.
- **Constant backdrop:** write in the fixed description exactly what shows
  behind or inside the piece (e.g. "the green wall shows through the
  circle") and repeat it in every frame prompt. Don't add backing boards,
  panels or fills that the junk stage doesn't have.

Write each video prompt with the playbook's video recipe: CAPTURE · ACTION ·
STABILITY · LOOK · AUDIO · EXCLUDE.
- **One verb-action.** Never use "then" or "and then". If you need two
  actions, make two clips.
- **The action starts at once.** Write the clip so the tool is already
  touching the material in its first second. A clip that spends 2 s walking
  up or lining up gives nothing to the edit.
- **AUDIO names one loud, clear sound** for the action (saw buzz, drill
  whirr, concrete pour, tape snap, thud). The breakouts carry a distinct
  sound on every beat.
- Describe the end state so it matches the end frame.
- **Framing for detail:** medium shots for build steps, close-ups for material
  moments (pour, texture, glow), at most one wide shot per project. AI video
  loses detail when the subject is small in the frame.
- Tripod and fixed framing for build steps. The ending follows its style
  (2c): an orbit, a pull-back, a travelling lights-on shot, and so on.
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
     "clip_db": 0, "grain": 3,
     "logo": "brand/logo.png", "logo_y": 0.10,
     "loop": 0.4,
     "segments": [
       { "clip": "clips/C1.mp4", "start": 0.6, "end": 2.0, "label": "OPEN: … (action from frame 0)" },
       { "clip": "clips/C1.mp4", "start": 4.1, "end": 5.4, "label": "…" },
       { "clip": "clips/C2.mp4", "start": 1.0, "end": 2.0, "label": "INSERT …" }
     ]
   }
   ```

   **No music.** Leave `music` out: the video keeps Flow's own sound (cutting,
   tapping, pouring, birds) exactly as generated. Only add a track when the
   user asks for one for that video.

   **No on-screen text, ever** (user, 2026-11-14): never add a `hook` caption.
   The opening is Luna in action (section 3). **Never put a flash of the
   finished piece in front** (research 2026-11-15: 0 of 27 breakouts do).
   The first segment's label starts with `OPEN:` and its `start` is trimmed
   into the action, so frame 0 is already moving. No segment is longer than
   2.5 s except a time-lapse clip or the ending (at most 3.5 s).
   `assemble.py` prints a pace report and warns about every break of these
   rules.
   `loop` dissolves the ending into the opening frame so the Short replays
   seamlessly.
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
- [ ] Frames: the first frame is the empty place + junk in hand; no end frame holds the next step's tool; inserts sit inside their own step; the backdrop behind/inside the piece is the same in every frame
- [ ] Object sizes, colours and shapes are written the same way in every
      prompt
- [ ] Every frame has **Check:** facts (logic: where material goes, what is empty or full, counts, tools), a **Focus:** box, and **Same size as:** its anchor
- [ ] The junk is still recognisable and has a job
- [ ] Camera (2d): 2–3 inserts per project with In-* frames; the ending clip has a camera move; build steps on a tripod; the ending travels smoothly through the whole place; no handheld shake anywhere
- [ ] Sound: no music in edit.json; Flow's own sound is kept as generated
- [ ] No `hook` key and no on-screen text in edit.json
- [ ] Growth rules: format chosen (Quick 11–25 s by default / Big 45–60 s only if asked); the first segment is `OPEN:` with action from frame 0; the finished piece first appears in the last third; a reason beat in the first 4 s; a use beat near the end; no segment over 2.5 s (time-lapse and ending excepted); ending at most 3.5 s; beat count fits the format
- [ ] Every clip's AUDIO line names one clear sound, and its action starts in the first second
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
After the video is assembled, `/luna-score` checks it against the growth
rules before posting.
