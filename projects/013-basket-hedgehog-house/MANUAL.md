# 013 — make it in Flow by hand

**Video:** A Hedgehog Was Hiding in the Cold… So I Built Him a Stone House 🦔

Open a **new Flow project** for this video. Save every download into this project folder exactly as named below. Watermarks are fine; Claude removes them.

## Part A — Images

**Settings for every image:** Image → **Nano Banana 2** · **9:16** · **x1**.

### A1. The hero (do this first, alone)
Attach `brand/luna-sheet.png` and `brand/luna-garden.png`, paste the prompt, generate.
Save the download as **`frames/raw/H-hero.jpg`**, then **tell Claude** "hero ready". Claude checks it and makes the clean `frames/H-hero.png` that every other image is built from.
```
Real smartphone photo, vertical, shot on an iPhone on a low tripod about 70 cm off the ground and 1.5 m away, slightly off-centre framing. A round stone hedgehog house on a plywood board on the stone path left of centre: a low dome about 40 cm across and 25 cm tall, its pale grey cement shell showing the woven pattern of a wicker basket, an arched 12 cm doorway facing the camera at a three-quarter angle, a cushion of green moss on top and dry autumn leaves at the entrance. A small brown European hedgehog with cream-tipped spines and a dark pointed nose pokes its head out of the doorway, sniffing. On the right, Luna (the woman in the first reference image) kneels on the path smiling down at the hedgehog, a little dried cement on her jeans. Luna, a woman in her mid-twenties with light-brown skin, long curly dark-brown hair with caramel highlights pulled into a high ponytail, freckles across her nose and cheeks, brown eyes, small gold hoop earrings, a bright friendly smile and a fit, athletic figure. She wears a fitted sage-green ribbed cropped tank top with a small white leaf logo on the chest, high-waisted light-blue denim jeans, a brown leather tool belt and tan leather work boots. Grey work gloves when handling concrete. Setting: a sunny cottage backyard with a weathered wooden workbench, a white picket fence, lavender and pink hydrangea beds, a stone path and a small garden shed, warm late-afternoon sunlight; slightly uneven lawn with clover and a few fallen leaves, fence with peeling paint. Late-afternoon sun from camera left, soft natural shadows falling to the right, contact shadows under every object, true-to-life colors, no color grading. Realistic skin with visible pores, light freckles and stray flyaway hairs. Natural phone camera look with slight sensor noise and mild lens distortion at the edges. No text, no watermark.
```

### A2. The other frames (after Claude says the hero is good)
For each one: attach **`frames/H-hero.png`** (the clean one Claude made) plus the refs listed, paste the prompt, generate, save as `frames/raw/<name>.jpg`.
When all are saved, **tell Claude** "frames ready": Claude runs the pixel-level review and tells you if any frame must be redone **before** you spend credits on clips.

#### R-cold — the problem (hook)
Attach `frames/H-hero.png` · save as **`frames/raw/R-cold.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: it is a grey, cold, overcast early morning with no sunshine and soft shadows. Luna, the hedgehog house and the board are gone. The same small brown hedgehog is curled into a tight ball on the bare stone path where the house was, a few cold wet leaves around it.
```

#### S1-basket — basket upside down
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S1-basket.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the hedgehog house, moss, leaves and hedgehog are gone. On the plywood board sits an old round wicker laundry basket about 38 cm across turned upside down, natural tan wicker, a little dusty. Luna kneels on the right in grey work gloves holding a pair of pruning shears against the basket's rim facing the camera, focused, not smiling.
```

#### S2-door — doorway cut
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S2-door.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the hedgehog house, moss, leaves and hedgehog are gone. On the plywood board sits an old round wicker basket turned upside down, an arched 12 cm doorway freshly cut into its side facing the camera at a three-quarter angle, a few wicker offcuts on the board. Luna kneels on the right in grey work gloves holding the pruning shears, looking at the doorway.
```

#### S3-slurry — first cement brushed on
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S3-slurry.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the moss, leaves and hedgehog are gone. The upturned wicker basket with its arched doorway is half covered in wet grey cement slurry: the left half grey and wet, the right half still bare tan wicker. A black bucket of cement slurry on the path. Luna kneels on the right in grey work gloves, holding a wide brush loaded with slurry against the bare wicker.
```

#### S4-coated — fully coated, wet
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S4-coated.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the moss, leaves and hedgehog are gone. The upturned basket is fully coated in wet dark-grey cement slurry, the woven pattern still clearly visible through it, same dome shape and arched doorway. Drips of slurry on the board. Luna kneels on the right in grey work gloves, the brush resting on the bucket.
```

#### S5-dry — dry stone dome, no moss
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S5-dry.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the moss, leaves and hedgehog are gone. The house is dry pale grey cement with the woven texture, same dome and doorway. Luna kneels on the right with bare hands, holding a clump of fresh green moss above the top of the dome.
```

#### S6-moss — moss on, no hedgehog
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S6-moss.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the hedgehog is gone; the doorway is empty and dark inside. Luna kneels on the right with bare hands resting on her knees, looking at the finished house.
```

#### S7-hedgehog — hedgehog approaching
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S7-hedgehog.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the hedgehog is no longer in the doorway: the same small brown hedgehog now stands on the stone path at the far left, a little way from the house, nose pointed at the doorway. Luna kneels on the right, watching quietly.
```

## Part B — Clips (only after Claude approves the frames)

**Settings for every clip:** Video → **Frames** · **Veo 3.1 Fast** (use **Veo 3.1 Quality** for the REVEAL/PAYOFF clip) · **9:16** · **x1** · 8 s · **resolution 1080p, set BEFORE you generate** (click "720p" in the composer and pick 1080p; 4K if your plan offers it). Download at that same size.
Pick **Start** (and **End** where given) from the clean `frames/*.png` files. Watch each clip once in Flow; regenerate once if something is clearly broken. 
Save as **`clips/raw/<clip>.mp4`**, then tell Claude "clips ready".

### C0 — hedgehog curled in the cold
**Start:** `R-cold` · **End:** none · save as **`clips/raw/C0.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. The small brown hedgehog curled in a tight ball on the cold stone path uncurls bit by bit, lifts its pointed nose and sniffs the cold air, its spines settling. The hedgehog stays in the same spot and keeps the same size and colour. Natural motion blur, true-to-life colors, no color grading, grey overcast light. SFX: tiny sniffs, a few leaves rustling. Ambient: soft wind. No music, no voices, no on-screen text.
```

### C1 — cut the doorway
**Start:** `S1-basket` · **End:** `S2-door` · save as **`clips/raw/C1.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. Luna cuts an arched doorway into the side of the upturned wicker basket with firm squeezes of the pruning shears, snipping through the wicker strands until a small arch opens; offcuts fall onto the board. The basket stays upside down in the same place and keeps its round shape. Natural motion blur, true-to-life colors, no color grading, late-afternoon sun from camera left. SFX: crisp wicker snips, offcuts dropping. Ambient: birds, light breeze. No music, no voices, no on-screen text.
```

### C2 — brush on the cement
**Start:** `S3-slurry` · **End:** `S4-coated` · save as **`clips/raw/C2.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. Luna brushes thick wet grey cement slurry over the upturned wicker basket with a wide brush, working the slurry into the weave until the whole dome is coated and grey, the woven pattern still showing. The basket keeps exactly the same dome shape, size and arched doorway. Natural motion blur, true-to-life colors, no color grading, late-afternoon sun from camera left. SFX: wet brush strokes, slurry dripping. Ambient: birds, light breeze. No music, no voices, no on-screen text.
```

### C3 — press on the moss
**Start:** `S5-dry` · **End:** `S6-moss` · save as **`clips/raw/C3.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. Luna presses clumps of fresh green moss onto the top of the dry stone dome with both hands, patting each clump down until a soft green cushion covers the top. The dome keeps exactly the same shape, texture and doorway. Natural motion blur, true-to-life colors, no color grading, late-afternoon sun from camera left. SFX: soft moss pats, rustling leaves. Ambient: birds, light breeze. No music, no voices, no on-screen text.
```

### C4 — PAYOFF: hedgehog moves in
**Start:** `S7-hedgehog` · **End:** `H-hero` · ⭐ use **Veo 3.1 Quality** here if you have the credits · save as **`clips/raw/C4.mp4`**
```
Vertical smartphone video, handheld with subtle natural shake, real-time speed, one continuous shot. The small brown hedgehog shuffles across the stone path into the arched doorway of the stone house, turns around inside and pokes its nose back out; Luna, kneeling beside it, breaks into a big smile. The house, moss and Luna stay the same shape and size. Natural motion blur, true-to-life colors, no color grading, late-afternoon sun from camera left. SFX: tiny footsteps on stone, a soft snuffle. Ambient: birds, light breeze. No music, no voices, no on-screen text.
```

## If Flow says "unusual activity"
Switch off the Flow Connector extension (`chrome://extensions`), wait ~10 minutes, reload Flow, try once more. Nothing is charged for a refused generation.
