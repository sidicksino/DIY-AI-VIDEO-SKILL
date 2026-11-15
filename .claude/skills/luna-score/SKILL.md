---
name: luna-score
description: Score a finished Luna Upcycles video against the researched growth rules before it is posted — opening in action, pace, length, reason, use beat, ending, sound — and list exactly what to fix in edit.json. Use when the user says "score the video", "check before posting", "is it ready to post", "score 020", or runs /luna-score, and always after tools/assemble.py writes a final.mp4. Checking only — it never changes the video unless the user asks.
---

# Luna Score

Checks one finished video against `brand/growth-playbook.md` (rules R1–R10,
from the 2026-11-15 research on 27 breakout videos). It reports a score and
a fix list. It does not re-edit anything unless the user says so.

## 1. Which video?

- The user names a project ("score 020"): use `projects/NNN-slug/`.
- Nothing given: use the newest project that has `output/final.mp4`.

## 2. Measure

```bash
.venv/bin/python tools/score_video.py projects/NNN-slug
```

It prints the measured score out of 100 and writes
`output/_score/opening.jpg`, `shots.jpg` and `score.json`.

| Measured check | Points | Passes when |
|---|---|---|
| Length | 10 | 15–22 s (Quick build) or 45–60 s (Big transformation) |
| Opening moves | 20 | clear movement between 0 and 0.5 s |
| Opening is not the result | 15 | the first segment is not the finished piece |
| Pace | 20 | average shot 2.0 s or less, none over 2.5 s |
| First 3 seconds | 5 | at least 2 beats start in the first 3 s |
| Ending length | 10 | last shot 3.5 s or less |
| Sound on every beat | 10 | no nearly silent second |
| No music / no text | 5 + 5 | edit.json has no `music` and no `hook` |

A fixed-camera time-lapse reads as one long shot. If `shots.jpg` shows
that something new appears every second, the Pace check passes: say so in
the report and count it as 20.

## 3. Judge what the file cannot show

**Read** `output/_score/opening.jpg` and `output/_score/shots.jpg`, and the
project's `plan.md`. Answer each with yes or no and one line of evidence:

1. **Action in frame 0 (R1, R2).** Is Luna already doing something to the
   junk or the empty place in the 0 s frame, with tool-on-junk contact by
   1.0 s?
2. **Curiosity.** From the first 2 s alone, would a stranger wonder what
   she is making? (Junk plus an unexpected action: yes. A nice room: no.)
3. **Reason (R3).** Is there a beat in the first 4 s that shows who or what
   it is for, without words?
4. **Result held back (R1).** Does the finished piece first appear in the
   last third?
5. **Use beat (R6).** Does someone use or react to the piece near the end?
6. **Enough steps (R5).** 8–12 beats for a Quick build, 20–30 for a Big
   transformation?
7. **Looks real.** Any frame in the sheets that looks AI-made (warped
   hands, morphing objects, text glitches)? Use
   `brand/realism-playbook.md`.

Each "no" on 1–6 takes 5 points off the measured score. A "yes" on 7 is a
blocker whatever the score.

## 4. Report

Keep it short:

- **Score:** NN/100, and the verdict: **80+ post it · 60–79 fix the
  listed items first · under 60 re-edit**.
- **Fixes, in order of weight**, each as a concrete change to `edit.json`:
  which segment, the new `start` and `end`, or which beat to add. If a fix
  needs a new clip (a use beat, a reason beat), say which frame and prompt
  it needs.
- The paths of `opening.jpg` and `shots.jpg`.

Then ask whether to apply the fixes. Only on a yes: edit `edit.json`, run
`tools/assemble.py`, and score again. Never change a video the user has
already posted unless they ask for that video by name.

## 5. After posting (R10)

When the user shares numbers for a posted video (views, "viewed vs swiped
away", average percentage viewed), add them to that video's row in
`ideas/log.md` next to its score. After 10 scored videos, compare: if high
scores do not get more views, say so and propose which rule to re-test.
