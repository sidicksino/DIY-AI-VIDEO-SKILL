---
name: same-idea
description: Remake a DIY video the user found and liked, with Luna as the maker. Takes a video from the same-idea/ folder, breaks it into shots, and writes a full Luna project (plan.md, MANUAL.md, edit.json, post.md) that follows the same shots, order and pacing, with Luna, our locations and the user's design changes (colour, shape, finish, object). Use when the user runs /same-idea, or says "remake this video", "do the same as this video", "copy this format", or drops a video in same-idea/. Planning only — frames are made afterwards with /luna-generate.
---

# Same Idea

The user found a DIY video that works and wants **the same video with
Luna**. You don't invent anything: you **follow the reference shot by
shot**, then hand over to the normal pipeline.

**The rule: copy the format, change the look.**

| Keep (copy freely) | Always change |
|---|---|
| Structure and order of shots, method (dip, pour, mould, melt…), pacing, total length, type of reveal | **Character:** Luna (`brand/luna.md`). **Place:** one of `brand/locations.md`. **At least one design choice:** colour, finish, shape or object (the user's note decides; if there's no note, propose one). **Title, hook text, music, caption:** always ours |

**Never reuse** their footage, frames, music, voice, on-screen text,
watermark or title. The remake is fully generated from our own prompts.

## 1. Pick the video

- The user names it ("/same-idea cool-planter"): use `same-idea/<name>.*`.
- Otherwise: use the **newest** video in `same-idea/` that has no project
  yet. Check `ideas/log.md` for `source:same-idea/<file>`.
- Read the optional note `same-idea/<same name>.txt`. It holds the user's
  wishes, e.g. "make it gold, use a bucket".
- If `same-idea/` has no video, tell the user to drop one in, and stop.

## 2. Study it shot by shot

```bash
.venv/bin/python tools/analyze_ref.py same-idea/<video>
```

Then **Read** these files in `same-idea/_analysis/<video>/`:
- `shots.jpg`: every shot in order, with times
- `timeline.jpg`: what moves inside each shot
- any `shot_NN.jpg` you need at full size
- the printed **camera** column (also in `shots.json`): static, push-in,
  pull-out, pan, tilt, orbit/arc or handheld, with the zoom % and travel.
  These are measured, not guessed

Write a **reference breakdown** (it goes into plan.md, section
"Reference"):
- **Overview:** length, number of shots, average shot length, music only
  or voice, any text on screen.
- **Projects:** if it's a compilation, list each project with its shot
  range. **Ask the user which project(s) to remake** unless the note says,
  and stop until they answer.
- **For the chosen project, one row per shot:** #, time, what we see
  (object and state), the single action, camera (wide, medium, close-up,
  top-down) **plus the measured camera move**, and its role (hook, junk, build step,
  satisfying moment, reveal, ending).
- **What makes it work:** the hook in the first 2 s, the most satisfying
  shot, the reveal place, the ending.

## 3. Map it to Luna

Build the **shot map**: each reference shot becomes one of our frames or
clips.
- **Merge** reference cuts that are the same action from two angles (for
  example a wide shot and a close-up of the same pour) into **one clip**.
  Our edit can still cut in on the close-up if Veo gives one. Aim for 5–8
  clips per project.
- **Keep** their order, pacing and type of reveal.
- **Keep their camera language** (luna-plan §2d):
  - every close-up cut-in in the reference becomes an **insert** clip
    (`In-*` frame) in ours
  - every measured move (push-in, pull-back, orbit, handheld) goes into
    that clip's CAPTURE line
  - **their ending move is copied**, e.g. "the camera glides forward along
    the finished border". Never end on a locked shot when they move
- **Apply the changes:** Luna, a location from `brand/locations.md` (the
  closest match to theirs), and the design change from the note (or your
  proposal).
- **Then run our quality gates on the remake**, exactly as `/luna-plan`
  does:
  - camera language: inserts and a moving ending (luna-plan §2d)
  - the shape test (the object's shape makes the result)
  - the placement check (the piece sits where it belongs)
  - an ending style different from the previous video's
  - one action per clip
  - framing for detail
  - 1080p and Veo Quality for the reveal (`brand/realism-playbook.md` §6)

  If their reveal fails our placement check (for example, a piece floating
  in an odd spot), fix it. A better ending is allowed.

## 4. Write the project

Follow `/luna-plan` sections 4–7 (read
`.claude/skills/luna-plan/SKILL.md` and its `plan-template.md`):
- Use the next project number, with the slug `NNN-<short-name>`.
- **`plan.md`:** the normal sections, plus a **"Reference"** section at the
  top with the reference breakdown, the shot map (reference shot # → our
  frame or clip) and the "Changed vs the reference" list.
- **`MANUAL.md`:** the clips for the user, with the 1080p settings line.
- **`edit.json`:** the same segment order and roughly the same timing as
  the reference (their shot lengths are your first trims), plus our hook
  text, loop and music.
- **`post.md`:** our own title, description, tags, and Instagram and TikTok
  captions. Never their title.
- **`ideas/log.md`:** add a row with status `picked` and these tags:
  `[cat:<key> · <build>→<reveal> · payoff:<type> · fmt:<A|B> · end:<style> · source:same-idea/<file>]`

## 5. Report and hand over

Keep it short:
- the reference in one line (length, shots, what it is)
- the shot map as a short table (theirs → ours)
- what changed (character, place, design)
- the link to `plan.md`

Ask the user to approve the plan. When they do, the next step is
`/luna-generate` (frames by Claude, then clips by the user from
MANUAL.md). Don't generate anything inside this skill.
