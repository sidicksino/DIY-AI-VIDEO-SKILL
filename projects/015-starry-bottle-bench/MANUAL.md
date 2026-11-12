# 015 — make the clips in Flow by hand

**Video:** I Poured Concrete Over 42 Bottles… Wait Until Night 🌌

Claude generates and reviews all 8 frames first (Part A runs in Flow via the connector). When Claude says the frames are approved, do Part B.

## Part B — Clips

**Settings for every clip:** Video → **Frames** · **Veo 3.1 Fast** (use **Veo 3.1 Quality** for the REVEAL/PAYOFF clip) · **9:16** · **x1** · 8 s · **resolution 1080p, set BEFORE you generate** (click "720p" in the composer and pick 1080p; 4K if your plan offers it). Download at that same size. Switch off the Flow Connector extension first.
Pick **Start** (and **End** where given) from the clean `frames/*.png` files of this project. Watch each clip once; regenerate once if clearly broken. 
Save as **`clips/raw/<clip>.mp4`**, then tell Claude "clips ready".

### C1 — lay the bottles
**Start:** `S1-rows` · **End:** `S2-filled` · save as **`clips/raw/C1.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. Luna lays empty glass bottles one by one into the long plywood mould, each on its side with its bottom pressed against the front board, filling it until three neat rows are stacked inside; she rests her gloved hands on the mould edge. The mould stays exactly the same size and position. Natural motion blur, true-to-life colors, no color grading, midday sun from camera left. SFX: glass clinking, bottles rolling softly on wood. Ambient: street sounds far away, light breeze. No music, no voices, no on-screen text.
```

### C2 — pour the concrete
**Start:** `S2-filled` · **End:** `S3-poured` · save as **`clips/raw/C2.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. Luna tips a heavy black bucket and pours thick wet grey concrete over the bottles in the long plywood mould; the concrete flows between the bottles and rises until the mould is full, the bottles are covered and the surface settles flat. The mould stays exactly the same size and position. Natural motion blur, true-to-life colors, no color grading, midday sun from camera left. SFX: heavy concrete pouring, glooping, trowel scraping. Ambient: light breeze. No music, no voices, no on-screen text.
```

### C3 — pull the front board
**Start:** `S4-unmould` · **End:** none · save as **`clips/raw/C3.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. Luna pulls the long front board of the plywood mould away from the cured concrete bench with a firm tug; it comes free and she sets it down, revealing the whole front face with three rows of round glass bottle bottoms set in the dusty grey-white concrete. The bench does not move and keeps exactly the same shape and size. Natural motion blur, true-to-life colors, no color grading, midday sun from camera left. SFX: wood creaking and releasing, a soft thud. Ambient: light breeze. No music, no voices, no on-screen text.
```

### C4 — polish it
**Start:** `S5-raw` · **End:** `B-hero` · save as **`clips/raw/C4.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. Luna rubs the front face of the white concrete bench with a folded polishing cloth in firm circles, moving along the rows; the cement film comes away and each round glass bottle bottom turns clear and glossy in amber, green, clear and cobalt blue. The bench keeps exactly the same shape, size and position. Natural motion blur, true-to-life colors, no color grading, midday sun from camera left. SFX: cloth squeaking on glass, soft rubbing. Ambient: light breeze. No music, no voices, no on-screen text.
```

### C5 — switch it on
**Start:** `V1-off` · **End:** `H-hero` · save as **`clips/raw/C5.mp4`**
```
Vertical smartphone video on a tripod, fixed framing, real-time speed, one continuous shot. At dusk on a villa garden terrace, Luna presses the button on a small black switch box; warm light fills the white concrete bench against the hedge and all 42 round bottle bottoms glow at once in amber, green, clear and cobalt blue, throwing coloured light on the rug, and she breaks into a big smile. The bench, rug, table and olive trees keep exactly the same position. True-to-life colors, no color grading, blue-hour dusk light. SFX: a soft click, a gentle electric hum. Ambient: evening crickets. No music, no voices, no on-screen text.
```

### C6 — ENDING (pull-back, no Luna)
**Start:** `D-detail` · **End:** `H-wide` · ⭐ use **Veo 3.1 Quality** here if you have the credits · save as **`clips/raw/C6.mp4`**
```
Vertical smartphone video, smooth gimbal move, real-time speed, one continuous shot. The camera starts close on the glowing round bottle bottoms in the white concrete bench and pulls back and rises in one steady move, revealing the whole bench against the clipped hedge, the olive trees with uplights, the rug, the low table with two glasses of wine and the lantern, and the lit glass villa behind. Nobody is in the scene. The bench and everything around it keep their shape and position. True-to-life colors, no color grading, evening light. SFX: none. Ambient: evening crickets, a soft breeze in the hedge. No music, no voices, no on-screen text.
```

