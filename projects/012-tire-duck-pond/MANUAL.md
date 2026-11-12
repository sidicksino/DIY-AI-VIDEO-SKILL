# 012 — make it in Flow by hand

**Video:** These Ducklings Had Nowhere to Swim… So I Used an Old Tire 🦆

Open a **new Flow project** for this video. Save every download into this project folder exactly as named below. Watermarks are fine; Claude removes them.

## Part A — Images

**Settings for every image:** Image → **Nano Banana 2** · **9:16** · **x1**.

### A1. The hero (do this first, alone)
Attach `brand/luna-sheet.png` and `brand/luna-garden.png`, paste the prompt, generate.
Save the download as **`frames/raw/H-hero.jpg`**, then **tell Claude** "hero ready". Claude checks it and makes the clean `frames/H-hero.png` that every other image is built from.
```
Real smartphone photo, vertical, shot on an iPhone on a low tripod about 70 cm off the ground and 1.5 m away, slightly off-centre framing. Left of centre, a small round garden pond about 75 cm across set into the lawn left of centre beside the stone path, its rim covered in rounded grey and tan river stones set in grey mortar, a flat stone ramp on the right side leading into the water, clear water with three green water-lily pads. Three small fluffy yellow ducklings with orange bills and feet paddle in the water, small ripples around them. On the right, Luna (the woman in the first reference image) kneels on the stone path smiling at the ducklings, a little dried mortar on her jeans. Luna, a woman in her mid-twenties with light-brown skin, long curly dark-brown hair with caramel highlights pulled into a high ponytail, freckles across her nose and cheeks, brown eyes, small gold hoop earrings, a bright friendly smile and a fit, athletic figure. She wears a fitted sage-green ribbed cropped tank top with a small white leaf logo on the chest, high-waisted light-blue denim jeans, a brown leather tool belt and tan leather work boots. Grey work gloves when handling concrete. Setting: a sunny cottage backyard with a weathered wooden workbench, a white picket fence, lavender and pink hydrangea beds, a stone path and a small garden shed, warm late-afternoon sunlight; slightly uneven lawn with clover and a few fallen leaves, fence with peeling paint. Late-afternoon sun from camera left, soft natural shadows falling to the right, contact shadows under every object, true-to-life colors, no color grading. Realistic skin with visible pores, light freckles and stray flyaway hairs. Natural phone camera look with slight sensor noise and mild lens distortion at the edges. No text, no watermark.
```

### A2. The other frames (after Claude says the hero is good)
For each one: attach **`frames/H-hero.png`** (the clean one Claude made) plus the refs listed, paste the prompt, generate, save as `frames/raw/<name>.jpg`.
When all are saved, **tell Claude** "frames ready": Claude runs the pixel-level review and tells you if any frame must be redone **before** you spend credits on clips.

#### R-dry — the problem (hook)
Attach `frames/H-hero.png` · save as **`frames/raw/R-dry.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: it is a grey, overcast morning with no sunshine and soft shadows. Luna and the pond are gone; there is only a plain patch of lawn where the pond was. The same three small fluffy yellow ducklings stand on the grass around a tiny empty, dented metal dish, looking into it.
```

#### S1-tire — tire on the lawn
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S1-tire.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the pond, water, stones and ducklings are gone. In the same spot an old black car tire about 65 cm wide lies flat on a shallow round patch of dug soil, dusty with worn tread. Luna kneels on the right in grey work gloves holding a folded black rubber pond liner above the tire, focused, not smiling.
```

#### S2-lined — liner inside the tire
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S2-lined.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the pond, water, stones and ducklings are gone. In the same spot an old black car tire about 65 cm wide lies flat in the soil, lined with a black rubber pond liner pressed into its centre, the liner's edges folded over the tire's rim. Luna kneels on the right in grey work gloves, pressing the liner down into the middle with both hands.
```

#### S3-mortar — first stones in the mortar
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S3-mortar.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the water and ducklings are gone; the pond is empty, showing the black liner inside. The tire's rim is covered in a thick band of wet grey mortar with river stones pressed into only the left third of it; the rest of the mortar is bare. A black bucket of river stones sits beside Luna. Luna kneels on the right in grey work gloves, holding one rounded river stone above the bare mortar.
```

#### S4-stones — rim fully stoned, empty
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S4-stones.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the water and ducklings are gone; the pond is empty and dry, showing the black liner inside. A few mortar crumbs on the grass. Luna kneels on the right in grey work gloves, both hands resting on her knees, looking at the finished stone rim.
```

#### S5-fill — filling with the hose
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S5-fill.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the ducklings and water-lily pads are gone and the pond is only a quarter full of clear water. Luna kneels on the right with bare hands, holding a green garden hose with water flowing from it into the pond.
```

#### S6-full — full, ready
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S6-full.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the ducklings are gone. The pond is full of clear, still water with the three water-lily pads. Luna kneels on the right with bare hands, the garden hose lying coiled on the path beside her.
```

#### S7-ducks — ducklings on the ramp
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S7-ducks.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the ducklings are no longer in the water: the same three ducklings stand on the flat stone ramp at the pond's right edge, looking at the water. Luna kneels on the right, watching quietly.
```

## Part B — Clips (only after Claude approves the frames)

**Settings for every clip:** Video → **Frames** · **Veo 3.1 Fast** (use **Veo 3.1 Quality** for the REVEAL/PAYOFF clip) · **9:16** · **x1** · 8 s · **resolution 1080p, set BEFORE you generate** (click "720p" in the composer and pick 1080p; 4K if your plan offers it). Download at that same size.
Pick **Start** (and **End** where given) from the clean `frames/*.png` files. Watch each clip once in Flow; regenerate once if something is clearly broken. 
Save as **`clips/raw/<clip>.mp4`**, then tell Claude "clips ready".

### C0 — ducklings at the empty dish
**Start:** `R-dry` · **End:** none · save as **`clips/raw/C0.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. The three small fluffy yellow ducklings peck at the tiny empty metal dish on the grass and look up, confused, one taking a small wobbly step. The ducklings keep the same size and markings and stay near the dish. Natural motion blur, true-to-life colors, no color grading, grey overcast light. SFX: tiny duckling peeps, a soft tap on metal. Ambient: soft wind. No music, no voices, no on-screen text.
```

### C1 — lay the liner
**Start:** `S1-tire` · **End:** `S2-lined` · save as **`clips/raw/C1.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. Luna unfolds the black rubber pond liner and lays it into the old tire, pressing it down into the centre with both gloved hands so it lines the inside, the edges folding over the rim. The tire stays in exactly the same place and keeps its round shape. Natural motion blur, true-to-life colors, no color grading, late-afternoon sun from camera left. SFX: rubber liner rustling, soft thumps. Ambient: birds, light breeze. No music, no voices, no on-screen text.
```

### C2 — press in the river stones
**Start:** `S3-mortar` · **End:** `S4-stones` · save as **`clips/raw/C2.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. Luna presses rounded river stones one by one into the wet grey mortar on the tire's rim, working around the circle until the whole rim is covered in stones. The pond keeps exactly the same round shape, size and position. Natural motion blur, true-to-life colors, no color grading, late-afternoon sun from camera left. SFX: stones clicking, mortar squelching. Ambient: birds, light breeze. No music, no voices, no on-screen text.
```

### C3 — fill it with the hose
**Start:** `S5-fill` · **End:** `S6-full` · save as **`clips/raw/C3.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. Clear water flows from the garden hose into the stone-rimmed pond and rises until it is full, the surface settling; Luna lays the hose down. The pond and its stone rim keep exactly the same shape and position. Natural motion blur, true-to-life colors, no color grading, late-afternoon sun from camera left. SFX: water gushing and filling. Ambient: birds, light breeze. No music, no voices, no on-screen text.
```

### C4 — PAYOFF: ducklings hop in
**Start:** `S7-ducks` · **End:** `H-hero` · ⭐ use **Veo 3.1 Quality** here if you have the credits · save as **`clips/raw/C4.mp4`**
```
Vertical smartphone video, handheld with subtle natural shake, real-time speed, one continuous shot. The three fluffy yellow ducklings hop off the flat stone ramp into the water one after another and paddle across the pond; Luna, kneeling beside it, breaks into a big smile. The pond, stones and Luna stay the same shape and size. Natural motion blur, true-to-life colors, no color grading, late-afternoon sun from camera left. SFX: small splashes, happy duckling peeps. Ambient: birds, light breeze. No music, no voices, no on-screen text.
```

## If Flow says "unusual activity"
Switch off the Flow Connector extension (`chrome://extensions`), wait ~10 minutes, reload Flow, try once more. Nothing is charged for a refused generation.
