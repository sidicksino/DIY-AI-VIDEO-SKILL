---
name: luna-steps
description: Turn a step-by-step DIY image (a numbered collage of build steps, e.g. cardboard mould → pour concrete → unmould → paint → luxury room) into a full Luna Upcycles project of 4–6 Veo clips, each 8 s, with one action written second by second so the whole clip is usable and nothing jumps. Writes plan.md, MANUAL.md, edit.json (format "steps") and post.md. Use when the user runs /luna-steps, tags a step image ("make this one", "do the infinity table", "steps/IMG_9728.jpeg"), or drops images in frames-images/. Planning only — frames are made afterwards with /luna-generate.
---

# Luna Steps

The user found a DIY idea shown as **numbered step images** and wants it as
a Luna video. The steps are already in order, so the job is to turn each
real step into **one 8-second clip that is good from its first second to its
last**. Then the edit keeps whole clips, and cuts only what is actually bad.

**Copy the idea and the steps, never the image.** Never upload their image
to Flow, never use it as a reference image, never copy its captions, text or
watermark. Read it, then write our own frames with Luna in our locations.

## 1. Pick the image

- The user tags a path: use it. A folder: list every image in it with a
  one-line description of each idea, and ask which one (stop until they
  answer, unless the message already says).
- Read the optional note `<same name>.txt` next to the image.
- Check `ideas/log.md` for `source:frames-images/<file>` (or the path given). If
  that image already has a project, say so and ask before making another.

## 2. Load context (always)

- `brand/luna.md`, `brand/locations.md`, `brand/realism-playbook.md`:
  exactly as in `/luna-plan` section 1.
- `brand/growth-playbook.md`: open in action, use beat, sound on every beat.
- `.claude/skills/luna-plan/SKILL.md` sections 2–7 and `plan-template.md`:
  this skill follows them, with the clip and edit rules below in place of
  luna-plan's section 3 and its edit.json pace rules.

## 3. Read the steps

Write the **step breakdown** (it goes into plan.md, section "Source steps"):
one row per numbered image: #, what we see (object and its state), the
action that leads to it, the tool in hand, the place (workshop, outdoor,
luxury room).

Then lock the concept as in `/luna-plan` section 2 (finished piece, mould
or junk, shape test, placement, ending), and apply:
- **Luna** and a location from `brand/locations.md` (build place + reveal
  place). The step images usually build outdoors on a tarp and reveal in a
  luxury room: pick our closest pair.
- **At least one design change** of our own (colour, finish, material or
  shape detail): the note decides; with no note, propose one.
- Our placement check (2b): fix the reveal if theirs fails it.

## 4. Map steps to clips (4–6 clips)

Each clip is **one real action that naturally takes about 8 seconds**:
pouring a mould full, peeling a mould away, painting a whole surface,
fitting a glass top, placing the piece and dressing it.

- **Merge** two image steps into one clip when together they are still one
  continuous action (step 1 "mould built" + "mould taped" = Luna bends and
  tapes the strip into the shape).
- **Split** an image step into two clips when it holds two actions with
  different tools (paint black, then paint gold lines = two clips).
- **Too short for 8 s?** (pressing a button, a single brush stroke) Make it
  bigger (paint the whole surface) or fold it into the next clip as its
  first second. Never leave an action that ends at second 3: Veo fills the
  rest by morphing.
- **Time skips go between clips, never inside one:** curing, drying,
  waiting. The cut hides them.
- **Clip 1 opens in action** (growth rule R1): Luna is already working on
  the junk or the mould in frame 0. Never open on the finished piece.
- **The last clip is the reveal with use and a camera move:** Luna or a
  guest places the last item or sits, while the camera glides smoothly
  (luna-plan 2c/2d). It may be the only clip with a moving camera.
- Choose the count that the steps need: 4, 5 or 6. Not more.

## 5. Frames

Follow `/luna-plan` sections 4–5 exactly (H-hero first, B-hero build anchor,
every stage one edit of its anchor, start/end pairs, constant backdrop,
first frame = empty place + junk or mould in hand, no next-step tool in an
end frame).

Every frame gets **Check:**, **Focus:** and **Same size as:** lines
(luna-plan section 4). For moulds and pours, always include: the material
lands only where it belongs (the channel, never an open centre), the count
of walls or parts, empty/full state, and that the mould has the same length
and spot as the finished piece and the same band width.

**Steps rule for end frames:** the change from start frame to end frame must
be reachable by the one action in 8 seconds, with the same tool still in
Luna's hands. If the end state needs a time skip (the concrete has cured),
the end frame is the last moment *before* the skip, and the next clip gets
its own start frame after the skip.

## 6. The 8-second prompt (the core of this skill)

Write every clip prompt with the playbook's video recipe, and replace the
single ACTION line with a **timeline of the same one action** across all
8 seconds:

```
[CAPTURE]  Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot with no cuts.
[TIMELINE]
0–1 s: <the action is already happening: what her hands and the tool are doing>.
1–4 s: <the action continues: what the material does, how far it has got>.
4–7 s: <the action continues: the visible progress>.
7–8 s: <the action finishes: the exact state of the end frame, Luna's hands and tool>.
[STABILITY]  One continuous motion from the first frame to the last, steady progress, no pause, no jump, nothing appears or disappears. <what must not change: the mould shape, size, the backdrop>.
[LOOK]  Natural motion blur on fast movements, true-to-life colors, no color grading, <light>.
[AUDIO]  SFX: <one loud clear sound for the action>, <one supporting sound>. Ambient: <place>.
[EXCLUDE]  No music, no voices, no on-screen text, no sudden changes, no time skips. (Moving shots add: No camera equipment in the frame.)
```

Rules for the timeline:
- **Every second describes the same action at a later stage.** Never a new
  action ("then she paints"). Progress words: "keeps pouring", "the grey
  level rises to halfway", "spreads into the right loop".
- **Hands never leave the work** until 7–8 s.
- **The 7–8 s line matches the end frame** word for word on the piece's
  state.
- **Progress is visible every second**, so the whole clip can stay in the
  edit.
- Under ~130 words in total. Short phrases per second.
- The reveal clip's timeline describes the camera travel second by second
  ("0–2 s: the camera starts low at the near end of the table … 6–8 s: it
  rises to show the whole living room").

## 7. Write the project

Like `/luna-plan` section 6, with these differences:
- `plan.md` gets a **"Source steps"** section at the top: the image path,
  the step breakdown, the step → clip map, and "Changed vs the source".
- `MANUAL.md`: the clips for the user, with the 1080p line. Under each
  prompt add one line: **"Check: <what must be true at 2 s, 5 s and 8 s>"**,
  so the user can see quickly whether a take is clean.
- `edit.json`:

  ```json
  {
    "output": "output/final.mp4",
    "format": "steps",
    "clip_db": 0, "grain": 3,
    "logo": "brand/logo.png", "logo_y": 0.10,
    "loop": 0.4,
    "segments": [
      { "clip": "clips/C1.mp4", "start": 0.0, "end": 7.9, "speed": 1.3, "label": "OPEN: Luna tapes the mould (action from frame 0)" },
      { "clip": "clips/C2.mp4", "start": 0.0, "end": 7.9, "speed": 1.3, "label": "pour" },
      { "clip": "clips/C5.mp4", "start": 0.0, "end": 7.9, "label": "reveal + use, camera glides" }
    ]
  }
  ```

  - **Whole clips by default.** `start` 0.0, `end` the clip's length.
  - **Cut only what is bad:** a glitch, a jump, or dead seconds where
    nothing changes. `/luna-generate`'s clip review finds them.
  - **`speed`** 1.25–1.5 on build clips when the action is slow (it plays
    faster, sound too, and looks like the time-lapse style the breakouts
    use). The reveal clip stays at 1.0.
  - Target **18–36 s** in total, every segment 6.5 s or less after speed.
    `assemble.py` warns otherwise.
  - No music, no `hook`, no on-screen text.
- `post.md`: our own title, description, tags, captions per
  `brand/keywords.md`. Never their caption.
- `ideas/log.md`: a row with status `picked` and
  `[cat:<key> · <build>→<reveal> · payoff:<type> · fmt:steps · end:<style> · source:frames-images/<file>]`

## 8. Self-check

Everything in `/luna-plan` section 7, except the Quick-build pace items,
plus:
- [ ] 4–6 clips, each one action that naturally fills 8 s
- [ ] Every prompt has a 0–1 / 1–4 / 4–7 / 7–8 s timeline of that one action, and its 7–8 s line matches the end frame
- [ ] Time skips only between clips
- [ ] Clip 1 is in action from frame 0; the finished piece is first seen in the last clip
- [ ] The last clip has a use beat and a smooth camera move
- [ ] Their image is not used as a reference anywhere; their text is not copied
- [ ] Every frame has Check / Focus / Same size as lines
- [ ] edit.json has `"format": "steps"`, whole clips, speeds where needed, 18–36 s

## 9. Report

Keep it short: the source in one line, the step → clip table, what changed,
the link to `plan.md`. Ask the user to approve. When they do, the next step
is `/luna-generate`.
