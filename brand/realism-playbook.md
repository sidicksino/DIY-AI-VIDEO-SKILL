# Realism playbook — prompts that don't look AI

The standard every Luna Upcycles image and clip is written to. The goal is
footage a viewer believes was filmed on a phone in a real garden.

## 1. What gives AI away (and the fix)

| Tell | Why it happens | Fix in the prompt |
|---|---|---|
| Plastic, airbrushed skin | model defaults to "beauty" | *realistic skin with visible pores, light freckles, stray flyaway hairs* |
| Everything spotless and new | nothing says it was used | name the wear: *concrete dust on jeans, paint drips, chipped edges, scuffed bucket* |
| Orange "golden hour" glow, oversaturated | words like *golden hour, cinematic, stunning* | *late-afternoon sun from camera left, true-to-life colors, no color grading* |
| Perfect symmetrical studio composition | no camera described | *real smartphone photo, chest height, about 2 m away, slightly off-centre* |
| Lawn like a carpet, flowers too perfect | idealised garden | *slightly uneven lawn with clover and a few fallen leaves, fence with peeling paint* |
| Floaty, weightless motion | vague verbs | force + weight: *scoops heavy wet concrete, it slumps and sticks, firm tugs* |
| Slow-motion feel | "slowly", "cinematic" | *real-time speed, steady natural pace, natural motion blur* |
| Objects morph or appear | too many actions, no end frame | one action per clip, **start + end frame** |
| Surprise music, voices, captions | not excluded | *No music, no voices, no on-screen text* |
| Over-sharp, noiseless frames | model output is too clean | *slight sensor noise*; plus light grain added in the edit |

**Never write:** cinematic, masterpiece, 8K, ultra-detailed, stunning,
beautiful, perfect, epic, hyper-realistic. They push the glossy AI look.

## 2. Image recipe (Nano Banana 2)

Order matters — camera first, so the model "shoots" the scene instead of
illustrating it:

```
[CAPTURE]  Real smartphone photo, vertical, shot on an iPhone at <height> from <distance>, slightly off-centre handheld framing.
[SUBJECT + STATE]  @Luna <pose> <what she's doing>. <the object, with real size in cm/m, material, and signs of handmade work>.
[SETTING]  Her garden: slightly uneven lawn with clover and a few fallen leaves, weathered white picket fence with peeling paint, lavender bushes.
[LIGHT]  Late-afternoon sun from camera left, soft natural shadows falling to the right, true-to-life colors, no color grading.
[TEXTURE]  Realistic skin with visible pores, light freckles and stray flyaway hairs; <dust / drips / scuffs on the specific things>.
[LOOK]  Natural phone camera look with slight sensor noise and mild lens distortion at the edges.
[EXCLUDE]  No text, no watermark.
```

**Editing an image** — always this opening, then **one** change:

```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and change only this: <one change>.
```

Two changes at once is where shapes drift. Big change → two edits.

**Never edit an edit more than once.** Every re-edit re-renders the whole
picture and adds sharpening: by the 4th generation (003 mushroom, 2026-09-15)
the frames were crunchy HDR with glow and sparkles — obviously AI. Make each
stage image **directly from the hero** (describe the whole target state in
one edit), and at most one more edit on top for a pose. Add to the lock
sentence: *"keep the natural smartphone-photo look of the original exactly:
same softness, grain and color, no extra sharpening, no HDR, no glow, no
sparkles."*

## 3. Video recipe (Veo 3.1 Fast, Frames with start + end)

```
[CAPTURE]  Vertical smartphone video <on a tripod, fixed framing | on a smooth gimbal, the camera travels steadily …>, real-time speed, one continuous shot.
[ACTION]  <who> <one physical action with force and weight verbs>, <what the material does>, <how it ends — matching the end frame>.
[STABILITY]  <the things that must not change>, e.g. "The dome stays exactly the same shape and size."
[LOOK]  Natural motion blur on fast movements, true-to-life colors, no color grading, late-afternoon sun from camera left.
[AUDIO]  SFX: <2–3 specific sounds>. Ambient: birds, light breeze.
[EXCLUDE]  No music, no voices, no on-screen text.
```

- **Tripod** for build steps — it's how real DIY creators film, and a still
  camera hides small glitches. The only moving shot is the **ending**: a smooth
  gimbal move through the place. **Never handheld shake.**
- Describe **the end state** in the action so it agrees with the end frame.
- Keep the prompt under ~120 words. Longer prompts get ignored in places.
- Download **1080p**.
- If the budget allows, spend **Veo 3.1 Quality (100 credits)** on the payoff
  shot only — it's the one people rewatch.

## 4. Check before spending credits

**Image**
- [ ] Hands: five fingers, gloves on both hands, tools held properly
- [ ] Object size makes sense next to Luna
- [ ] Contact shadows under the object and her knees (no floating)
- [ ] Light comes from the same side as the previous image
- [ ] No garbled text or extra logos
- [ ] It matches the image it was edited from (shape, colour, position)

**Video** (Claude checks frame grids)
- [ ] Nothing appears, vanishes or duplicates
- [ ] Faces, hands and objects keep their shape
- [ ] Motion has weight; nothing floats
- [ ] Ends close to the end frame
- [ ] No voice or music in the audio

## 5. In the edit (Claude)

- Light moving grain (`"grain": 3` in `edit.json`) — takes the clean AI sheen off
- 1–2 s shots, cut before any glitch
- **No music**: keep Flow's own sound (cuts, taps, pours, birds) as generated; loudness to −14 LUFS

## 6. Quality: settings that decide sharpness (2026-11-12)

**At generation (this is where most quality is won or lost):**
- **Anchors** (H-hero, B-hero, Pn-H, Pn-B): **Nano Banana Pro**, downloaded at the **largest size offered (2K)**. Stage edits can stay on Nano Banana 2.
- **Video: set 1080p BEFORE generating.** Flow defaults to 720p (the composer pill reads "Video · 720p · 8s"). Click it and choose **1080p**, or **4K** if your plan offers it. Download at the same size. Upscaling a 720p file later can't add real detail.
- **Veo 3.1 Quality** for the reveal/ending clip and any close-up of the finished piece; **Veo 3.1 Fast** for build steps.
- **Camera language:** 2–3 macro insert close-ups per project (focus pull, shallow depth of field) and a **moving ending** (glide, pull-back, orbit), never a locked last shot (luna-plan §2d).
- **Framing for detail:** AI video loses fine detail in wide shots. Keep the subject large: medium shots for build steps, close-ups for the material moments (pours, textures, glow), at most one wide establishing shot.
- Simple motion keeps detail: one action, steady tripod, no fast whip pans.

**In the edit (`tools/assemble.py` does this automatically):**
- Keep **24 fps** (Veo's native rate); never convert to 30.
- Near-lossless intermediates (CRF 12); one final high-quality encode: H.264 High, CRF 16, preset slow, tune film, about 12–20 Mbps, AAC 256k.
- Lanczos scaling with a light sharpen when a clip is below 1080p.
- **No watermark step.** Clips and images downloaded from Flow have no visible watermark (checked 2026-11-12), so they're used exactly as downloaded. Never crop (it zooms 13.5% and loses detail), patch or delogo them.
- Grain at most 2–3: YouTube's encoder turns heavy noise into blocks.

**Upload:** 1080×1920 H.264 MP4 straight from `output/`. Never upload a re-downloaded or screen-recorded copy.
