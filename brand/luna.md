# Luna — character bible

Every prompt uses these exact words. Consistency is the brand: the viewer
should recognise Luna and her garden in the first frame.

## Luna

```
Luna, a woman in her mid-twenties with light-brown skin, long curly dark-brown
hair with caramel highlights pulled into a high ponytail, freckles across her
nose and cheeks, brown eyes, small gold hoop earrings, a bright friendly smile
and a fit, athletic figure. She wears a fitted sage-green ribbed cropped tank
top with a small white leaf logo on the chest, high-waisted light-blue denim
jeans, a brown leather tool belt and tan leather work boots. Grey work gloves
when handling concrete.
```

Locked 2026-09-14 from the ChatGPT sheet (`brand/luna-sheet.png`). Don't
generate new faces — always use the sheet as the reference.

She never speaks and never looks into the camera for long. No dialogue.

**Attractive, not suggestive.** Camera on her face, hands and the project;
full-body shots from the front or side. No low angles on her hips, no body
close-ups — those get Shorts limited ads or age-restricted and keep TikTok
videos out of the For You feed.

## Luna's garden (the recurring set)

```
a sunny cottage backyard with a weathered wooden workbench, a white picket
fence, lavender and pink hydrangea beds, a stone path and a small garden shed,
warm late-afternoon sunlight
```

## Look

```
photorealistic, vertical 9:16, shot like a smartphone video, natural light,
shallow depth of field, no text, no subtitles, no music
```

---

## Making the brand images — ChatGPT

Do all four in **one ChatGPT chat**, in this order, so it remembers Luna from
the first image and keeps her face the same. No text in any image — the name
goes on the banner afterwards, in `tools/branding.py`.

If Luna's face drifts in 3 or 4, upload `luna-sheet.png` back into the chat and
say *"use exactly this woman"*. Download the largest size offered.

### 1. Character sheet → `brand/luna-sheet.png`

```
Create a photorealistic character reference sheet, portrait orientation, of one woman shown three times side by side on a plain light-grey studio background: front view, three-quarter view, and full body.

Her name is Luna. She is in her mid-twenties with long wavy chestnut-brown hair tied in a high ponytail, light olive skin, light freckles, natural makeup and a friendly, focused expression. She wears a sage-green short-sleeve t-shirt with a small white leaf logo on the chest, a beige canvas work apron, dark olive cargo pants and tan leather work boots.

Even soft lighting, the same face and outfit in all three views, no text or labels anywhere.
```

### 2. Luna's garden → `brand/luna-garden.png`

```
Now create a photorealistic image, portrait orientation, of Luna's garden where she does all her projects: a sunny cottage backyard with a weathered wooden workbench, a white picket fence, lavender and pink hydrangea beds, a stone path and a small garden shed. Warm late-afternoon sunlight, smartphone photo look, no people, no text.
```

### 3. Avatar → `brand/avatar-raw.png`

```
Now create a square, photorealistic close-up portrait of the same woman, Luna, exactly as in the character sheet: same face, curly hair, gold hoop earrings and sage-green tank top. She is smiling warmly and holding a small grey concrete planter with a green succulent. Her face is centred and fills most of the frame, with her garden blurred behind her. No text.
```

### 4. Banner background → `brand/banner-raw.png`

```
Now create a wide landscape photorealistic image of Luna's garden: the weathered wooden workbench covered in handmade concrete planters and a yellow bird bath, sparrows on the bird bath, lavender and pink hydrangea beds, white picket fence, warm late-afternoon light. Keep the middle of the image calm and uncluttered (soft blurred greenery) so text can sit there. No people, no text.
```

### Then

```sh
.venv/bin/python tools/branding.py
```

→ `avatar.png` (800×800), `watermark.png` (150×150, Studio's *Video
watermark*), `banner.png` (2560×1440, name inside the area every device
shows) and `banner-phone-preview.png`. Upload in **Studio → Customisation →
Profile**, then **Publish**.

---

## Using Luna in Flow (video clips)

1. Upload `luna-sheet.png` in **Characters** and name it **Luna**; keep
   `luna-garden.png` handy as a scene reference.
2. Set outputs to **x1** — x2 doubles what every generation costs.
3. Per clip: start image with **Nano Banana 2** (9:16, Luna as reference), then
   **Veo 3.1 Fast** (9:16, 8 s) from that image. The prompts for each video
   live in `projects/<id>/prompts.md`.
