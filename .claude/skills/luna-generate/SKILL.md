---
name: luna-generate
description: Generate the images and video clips for an approved Luna Upcycles plan in Google Flow (Nano Banana 2 frames, Veo 3.1 frame-to-video clips) through the Flow Connector / flow-auto CLI, save them into the project folder with the plan's names, check every result against the realism playbook, and pause for the user's approval at the hero image and at the full frame set. Use when the user says "generate", "generate the frames", "make the clips", "start Flow", "generate project 010", or runs /luna-generate. Needs projects/NNN-slug/plan.md from /luna-plan.
---

# Luna Generate

Runs an approved `plan.md` in Google Flow. This skill:
- generates every image and clip
- saves each one under the plan's name
- checks every result before moving on

It never changes the concept. If a prompt needs rewriting, it changes
wording only.

The low-level Flow tool is the **flow-generate** skill (the `flow-auto` CLI).
Load that skill first and follow its rules on batching, refusals, `stop`,
the hidden tab and notices. This file adds only what is specific to Luna.

## 0. Pick the project

- The user names it ("project 010", "the kitten igloo"): use that one.
- Otherwise: use the newest `projects/NNN-*/` whose `plan.md` status line is
  not finished yet.
- If `plan.md` is missing, stop and point the user to `/luna-plan`.

Read `plan.md`, `brand/realism-playbook.md` (especially section 4, "Check
before spending credits", and **section 6, Quality**) and `brand/luna.md`.

**Quality defaults (playbook §6):**
- **Anchors** (H-hero, B-hero, Pn-H, Pn-B): Nano Banana Pro (`--pro`). Stages: Nano Banana 2.
- **Frames:** use `tools/flow_frames.py`. It submits from plan.md, sends small JPEG
  references, waits, saves `frames/raw/` and writes clean `frames/*.png`.
- **Clips:** 1080p, chosen before generating; Veo Quality for the reveal.
- **Watermark:** none on Flow downloads, so use files as downloaded, with no clean step.
- **Clip pairs:** before approving frames, put each clip's start and end side by side and check that only that clip's action changed (no new tool in hand, no backdrop or colour change behind the piece). If something else changed, remake the frame.
- **Insert close-ups (`In-*` frames):** make each one as an edit of its stage frame
  (`tools/flow_frames.py ... In-cut:S6-plant,luna`), after the stage frames pass
  review. Check that it shows the same objects, colours and gloves as its stage
  frame, only closer.


**Resume, don't redo.** Before generating each file, check whether it
already exists in `frames/` or `clips/`. If it does, skip it. That way a
stopped run picks up where it left off, and nothing gets paid for twice.

## 1. Preflight

Run `flow-auto status --site flow` and handle what it reports:

- **`flow tab: HIDDEN`:** stop. Tell the user to put Chrome with Flow on one
  half of the screen and this app on the other, so both stay visible.
- **Free plan:** jobs run one at a time, and the Flow Connector **side panel
  must stay open**. The limits are 30 videos and 40 images a day.
  Downloads are 1K images and 720p video. That is fine for Shorts, since the
  assemble step scales to 1080×1920.
- **Daily limit:** if what is left in the plan is more than what is left
  today, say so and generate as far as the limit allows.

**Before the first job of a project,** say once: "This will use about N
Flow credits" (from the plan's Credits table).

Use one Flow project per video. Put `--new-project` on the very first job
only, and never on retries.

## 2. Phase A: the HERO (checkpoint 1)

1. **Prepare the prompt.** Take the `H-hero` prompt from `plan.md`. Replace
   `@Luna` with `Luna (the woman in the first reference image)`.
2. **Submit it:**
   ```bash
   flow-auto generate create flow-image-to-image --new-project \
     --prompt "<prompt>" --image brand/luna-sheet.png --image brand/luna-garden.png \
     --model nano-banana-2 --aspect-ratio 9:16 --outputs 1 --wait
   ```
3. **Save it** as `frames/H-hero.png`, untouched. `tools/flow_frames.py` does this
   automatically; Flow downloads have no watermark, so there is nothing to
   clean.
4. (No watermark step.)
5. **Check it yourself** (Read the image) against playbook section 4:
   - hands and gloves are right
   - sizes make sense next to Luna
   - contact shadows are there
   - light comes from camera left
   - no garbled text
   - Luna matches `luna-sheet.png`
   - the piece matches the plan's locked description, including the junk
     detail (for 010, the blue jug neck vent)
6. **If it fails,** fix only the wording that caused the problem and
   regenerate. Allow **one** retry. If it still fails, show the user both
   versions and ask.
7. **CHECKPOINT 1.** Show the user `frames/H-hero.png` and ask them to
   approve it. Every other image comes from it, so a weak hero means a weak
   video. **Don't continue until they approve.**

## 3. Phase B: stage images (checkpoint 2)

**Keep references small.** The extension can pass at most 64 MB per message,
and every queued job carries its reference images. On 2026-11-08, 29 jobs
with two 2 MB PNGs each failed with `Message exceeded maximum allowed size of
64MiB`. So:
- Attach compact JPEG copies (quality ~90, about 300–500 KB) of the hero and
  `luna-sheet`, saved in the scratchpad. Never attach the full PNGs.
- Submit **one video's frames per batch** (≤ 9 jobs). Wait for that batch to
  finish before submitting the next video.

For every other image in Part 1 of `plan.md`:

1. **Build the prompt.** Use the full lock sentence plus that image's change
   text. Expand `<lock sentence>` with the exact sentence from the plan.
2. **Source is always `frames/H-hero.png`,** unless the plan names another
   source for that image. Add `--image brand/luna-sheet.png` when the plan
   lists it under Refs.
3. **Submit them all as one batch,** without `--wait`, with `--index` and
   `--folder <NNN>-frames`, following the flow-generate batching rules:
   ```bash
   flow-auto generate create flow-image-to-image --prompt "<lock + change>" \
     --image projects/<NNN>/frames/H-hero.png --image brand/luna-sheet.png \
     --model nano-banana-2 --aspect-ratio 9:16 --outputs 1 --index <n> --folder <NNN>-frames
   ```
4. **Watch the queue** with `flow-auto generate list`. Keep talking to the
   user while it runs; don't block on it.
5. **When the run finishes,** copy each file to `frames/<name>.raw.png`,
   and `frames/<name>.png`, untouched.
6. **Check every image** against the playbook checklist. Also check that it
   still matches the hero: same camera, same board position, same size of
   piece, same light. Common problems:
   - extra objects
   - Luna's outfit changing
   - the piece moving or changing size
   - a missing junk detail (the jug neck)
   - rain or sun in the wrong shot
7. **If an image fails,** allow one retry with corrected wording. Always
   regenerate it **from the hero again**, never from the bad image.
8. **Detailed review: required, pixel level.** The small contact sheet
   hides details, so after all frames exist, run:
   ```bash
   .venv/bin/python tools/review.py frames projects/<NNN>
   ```
   - **Read `frames/_review/drift.jpg`.** It shows a heat map of what
     changed compared with the hero. The garden, fence and shed must stay
     dark; only the piece and Luna should light up. Any sunny frame
     flagged `<-- check` (background drift above 6) has drifted, so look
     at it.
   - **Read every `frames/_review/pairs_*.jpg`.** These show consecutive
     frames side by side at full resolution, cropped to the piece, Luna's
     face and her hands. For each pair, check:
     - the piece's shape, size, opening and position
     - gloves on or off (the same across a clip, unless the clip's action
       is taking them off)
     - tools and props: the same items, in the same places
     - Luna's face, hair, earrings and outfit
     - anything that appears or vanishes between the two frames, which
       Veo would show as a pop

     Example from 010: gloves on in S6 but bare hands in S7 would make the
     gloves vanish in the limewash clip. That gets fixed before the clip.
   - **Fix every mismatch** by regenerating the frame from the hero with
     the corrected wording. Rerun the review until it's clean.
9. **CHECKPOINT 2.** Make a contact sheet: all frames side by side, in plan
   order, labelled, saved as `frames/_contact.jpg`. Use Pillow from the
   project `.venv`. Show it to the user and ask them to approve the full
   set. **Clips cost far more than images, so don't start them before they
   approve.**

## 4. Phase C: clips

For every clip in Part 2 of `plan.md`:

1. **Submit the clips as one batch,** with `--index` and
   `--folder <NNN>-clips`. The first `--image` is the start frame and the
   second is the end frame:
   ```bash
   flow-auto generate create flow-frame-to-video --prompt "<clip prompt>" \
     --image projects/<NNN>/frames/<start>.png --image projects/<NNN>/frames/<end>.png \
     --model veo-3.1-fast --aspect-ratio 9:16 --outputs 1 --index <n> --folder <NNN>-clips
   ```
   - If the plan gives no end frame (like 010's C0), pass only the start
     frame.
   - **Payoff clip:** before using `veo-3.1-quality` (100 credits), ask the
     user. By default it uses `veo-3.1-fast`.
2. **Save.** Copy each video to `clips/raw/<Cn>.mp4`, then into `clips/` unchanged:
   ```bash
   cp clips/raw/<Cn>.mp4 clips/<Cn>.mp4
   ```
   No watermark removal: Flow downloads carry no visible mark (checked
   2026-11-12). Cropping or patching only loses quality.
3. **Check every clip frame by frame.** Run:
   ```bash
   .venv/bin/python tools/review.py clip projects/<NNN>/clips/<Cn>.mp4
   ```
   It decodes every frame and flags sudden changes, which are where pops,
   vanishing objects and morphs happen. It prints the clean windows
   between them. Then:
   - Read `clips/_review/<Cn>/grid.jpg` (a frame every 0.25 s, with
     flagged moments in red).
   - Read every `jump_*.jpg`, which shows the frames around each flagged
     moment.

   Check:
   - nothing appears, vanishes or duplicates
   - faces, hands and the piece keep their shape
   - motion has weight; nothing floats
   - the clip ends close to the end frame
   - the one action actually happens and isn't skipped

   Then check the audio for music or voices. If you can't check it, say
   so.
4. **Write down the usable window** for each clip: the clean seconds, the
   timestamp of any glitch, and the best 1.5–3 s. Update that segment's
   `start`/`end` in `edit.json` so it cuts before the glitch.
5. **If a clip has no usable 1.5 s,** allow one retry with tightened
   wording: stronger STABILITY lines, a simpler action. If it fails again,
   report it to the user and suggest splitting the action or changing the
   frames.

## 5. Finish

1. **Update the status line in `plan.md`,** for example
   `images: 8/8 · clips: 7/7 · edited: no`.
2. **Keep the review files** (`frames/_review/`, `clips/_review/`) until the
   video is published; they are what the edit's trims are based on. Keep
   `frames/_contact.jpg` and the `*.raw.*` originals.
3. **Report to the user in a few lines:**
   - what was made
   - any clips that need attention, with the reason
   - roughly how many credits were used

   The next step is `/luna-assemble`. Until that skill exists, run
   `.venv/bin/python tools/assemble.py projects/<NNN>`.

## Rules

- **Follow flow-generate's rules on refusals.** A refusal is never
  resubmitted unchanged. Rewrite the wording once; if it's refused again,
  stop and ask the user.
- **If anything starts going wrong mid-batch,** run
  `flow-auto stop --site flow` first, then explain.
- **Never change the concept, the locked descriptions or the camera** while
  fixing a prompt. Change wording only. Anything bigger goes back to
  `/luna-plan`.
- **Don't paste job ids or raw JSON in chat.** Give the file paths and a
  one-line summary instead.
