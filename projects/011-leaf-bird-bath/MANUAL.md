# 011 — make it in Flow by hand

**Video:** I Pressed Concrete Over a Giant Leaf… The Birds Love It 🍃🐦

Open a **new Flow project** for this video. Save every download into this project folder exactly as named below. Watermarks are fine; Claude removes them.

## Part A — Images

**Settings for every image:** Image → **Nano Banana 2** · **9:16** · **x1**.

### A1. The hero (do this first, alone)
Attach `brand/luna-sheet.png` and `brand/luna-garden.png`, paste the prompt, generate.
Save the download as **`frames/raw/H-hero.jpg`**, then **tell Claude** "hero ready". Claude checks it and makes the clean `frames/H-hero.png` that every other image is built from.
```
Real smartphone photo, vertical, shot on an iPhone on a low tripod about 70 cm off the ground and 1.5 m away, slightly off-centre framing. On the stone path beside the pink hydrangea bed, left of centre, stands a leaf-shaped concrete bird bath about 60 cm long and 45 cm wide, a shallow bowl in the exact outline of a giant rhubarb leaf with deep vein lines, painted mossy green with soft gold on the veins, resting on a short round grey stone pedestal about 40 cm tall on the stone path left of centre, filled with clear water that reflects the sky. A European robin with an orange-red breast, brown back and grey-white belly stands in the shallow water, wings slightly open mid-splash, droplets in the air. On the right, Luna (the woman in the first reference image) kneels on the path smiling at the bird, a little dried concrete on her jeans. Luna, a woman in her mid-twenties with light-brown skin, long curly dark-brown hair with caramel highlights pulled into a high ponytail, freckles across her nose and cheeks, brown eyes, small gold hoop earrings, a bright friendly smile and a fit, athletic figure. She wears a fitted sage-green ribbed cropped tank top with a small white leaf logo on the chest, high-waisted light-blue denim jeans, a brown leather tool belt and tan leather work boots. Grey work gloves when handling concrete. Setting: a sunny cottage backyard with a weathered wooden workbench, a white picket fence, lavender and pink hydrangea beds, a stone path and a small garden shed, warm late-afternoon sunlight; slightly uneven lawn with clover and a few fallen leaves, fence with peeling paint. Late-afternoon sun from camera left, soft natural shadows falling to the right, contact shadows under every object, true-to-life colors, no color grading. Realistic skin with visible pores, light freckles and stray flyaway hairs. Natural phone camera look with slight sensor noise and mild lens distortion at the edges. No text, no watermark.
```

### A2. The other frames (after Claude says the hero is good)
For each one: attach **`frames/H-hero.png`** (the clean one Claude made) plus the refs listed, paste the prompt, generate, save as `frames/raw/<name>.jpg`.
When all are saved, **tell Claude** "frames ready": Claude runs the pixel-level review and tells you if any frame must be redone **before** you spend credits on clips.

#### S1-leaf — leaf on the sand mound
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S1-leaf.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the bird bath, pedestal and robin are gone. On a plywood board on the stone path lies a low dome of damp sand about 50 cm across, covered by one giant fresh green rhubarb leaf about 60 × 45 cm laid vein-side up, its edges drooping onto the board. A black bucket of wet grey concrete sits beside the board. Luna kneels on the right in grey work gloves holding a trowel loaded with wet concrete above the leaf, focused, not smiling.
```

#### S2-coated — concrete over the leaf
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S2-coated.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the bird bath, pedestal and robin are gone. On a plywood board on the stone path, a giant rhubarb leaf on a low sand dome is now covered by a 3 cm layer of wet grey concrete that follows the leaf's outline exactly, the green leaf tips just showing at the edges. A black bucket of concrete beside the board. Luna kneels on the right in grey work gloves caked with concrete, pressing the concrete smooth with both hands.
```

#### S3-peel — peeling the leaf off
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S3-peel.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the bird bath, pedestal and robin are gone. On the plywood board lies the hardened concrete leaf, flipped over so its hollow side faces up, the sand dome gone. Luna kneels close in grey work gloves, peeling the green rhubarb leaf off the concrete with one hand, the leaf half lifted, revealing sharp vein lines printed in the raw grey concrete underneath.
```

#### S4-raw — raw leaf bowl on the pedestal
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S4-raw.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the robin and the water are gone. The bird bath is still raw, unpainted light-grey concrete with sharp vein lines, the same leaf shape and size on the same pedestal. Luna kneels on the right with bare hands, holding a small paintbrush dipped in mossy green paint over a small open tin of green paint on the path.
```

#### S5-painted — painted, empty
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S5-painted.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the robin and the water are gone; the bowl is empty and dry. Luna kneels on the right with bare hands, a small paintbrush resting on a tin of green paint beside her, looking at the finished bowl.
```

#### S6-pour — filling with water
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S6-pour.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the robin is gone and the bowl is only a quarter full. Luna kneels on the right holding a galvanised metal watering can tilted over the bowl, a stream of clear water pouring into the centre of the leaf.
```

#### S7-robin — robin on the rim
Attach `frames/H-hero.png` + `brand/luna-sheet.png` · save as **`frames/raw/S7-robin.jpg`**
```
Keep everything exactly the same — same camera angle, framing, light, colors, Luna's face and every other object — and keep the natural smartphone-photo look of the original exactly: same softness, grain and color, no extra sharpening, no HDR, no glow, no sparkles. Change only this: the robin is no longer in the water: the same robin is perched on the rim of the leaf bowl at its left tip, looking at the water. The bowl is full of still, clear water. Luna kneels on the right, watching quietly.
```

## Part B — Clips (only after Claude approves the frames)

**Settings for every clip:** Video → **Frames** · **Veo 3.1 Fast** (use **Veo 3.1 Quality** for the REVEAL/PAYOFF clip) · **9:16** · **x1** · 8 s · **resolution 1080p, set BEFORE you generate** (click "720p" in the composer and pick 1080p; 4K if your plan offers it). Download at that same size.
Pick **Start** (and **End** where given) from the clean `frames/*.png` files. Watch each clip once in Flow; regenerate once if something is clearly broken. 
Save as **`clips/raw/<clip>.mp4`**, then tell Claude "clips ready".

### C1 — spread concrete over the leaf
**Start:** `S1-leaf` · **End:** `S2-coated` · save as **`clips/raw/C1.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. Luna spreads thick wet grey concrete over the giant rhubarb leaf on the sand mound with a trowel and her gloved hand, pressing it down in an even layer that follows the leaf's outline; the heavy concrete slumps slightly and sticks. The leaf, sand mound and board stay in exactly the same place. Natural motion blur, true-to-life colors, no color grading, late-afternoon sun from camera left. SFX: trowel scraping, wet concrete slaps. Ambient: birds, light breeze. No music, no voices, no on-screen text.
```

### C2 — peel the leaf off
**Start:** `S3-peel` · **End:** none · save as **`clips/raw/C2.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. Luna peels the green rhubarb leaf off the hardened concrete in one slow pull; the soft leaf bends and tears slightly as it comes away, revealing sharp vein lines printed in the grey concrete. She lifts the leaf clear. The concrete leaf does not move and keeps exactly the same shape and size. Natural motion blur, true-to-life colors, no color grading, late-afternoon sun from camera left. SFX: leaf peeling and tearing softly. Ambient: birds, light breeze. No music, no voices, no on-screen text.
```

### C3 — paint it mossy green
**Start:** `S4-raw` · **End:** `S5-painted` · save as **`clips/raw/C3.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. Luna brushes mossy green paint across the raw concrete leaf bowl with a small brush, working outward along the veins until the whole bowl is green with soft gold on the veins; she sets the brush down on the tin. The bowl and pedestal keep exactly the same shape and position. Natural motion blur, true-to-life colors, no color grading, late-afternoon sun from camera left. SFX: brush bristles on rough concrete, brush tapped on a tin. Ambient: birds, light breeze. No music, no voices, no on-screen text.
```

### C4 — fill it with water
**Start:** `S6-pour` · **End:** none · save as **`clips/raw/C4.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. Luna pours clear water from a galvanised watering can into the leaf-shaped bowl; the water spreads into the vein lines and rises until the bowl is full, and she lifts the can away. The bowl, pedestal and Luna stay in the same place. Natural motion blur, true-to-life colors, no color grading, late-afternoon sun from camera left. SFX: water pouring and splashing gently. Ambient: birds, light breeze. No music, no voices, no on-screen text.
```

### C5 — PAYOFF: robin splashes
**Start:** `S7-robin` · **End:** `H-hero` · ⭐ use **Veo 3.1 Quality** here if you have the credits · save as **`clips/raw/C5.mp4`**
```
Vertical smartphone video, handheld with subtle natural shake, real-time speed, one continuous shot. The robin hops from the rim into the shallow water and splashes, ruffling its feathers and flicking droplets; Luna, kneeling beside it, breaks into a big smile. The bowl, pedestal and Luna stay the same shape and size. Natural motion blur, true-to-life colors, no color grading, late-afternoon sun from camera left. SFX: small wing flutters, water splashing. Ambient: birds, light breeze. No music, no voices, no on-screen text.
```

## If Flow says "unusual activity"
Switch off the Flow Connector extension (`chrome://extensions`), wait ~10 minutes, reload Flow, try once more. Nothing is charged for a refused generation.
