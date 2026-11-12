# Luna Upcycles

AI-generated garden upcycling Shorts for YouTube and TikTok. Luna turns junk
into concrete garden pieces; every video ends on an animal enjoying it.

## Layout

```
brand/      channel.md (setup + copy), luna.md (character prompts),
            realism-playbook.md, logo, watermark, banner, avatar
ideas/      log.md (every idea ever, never repeat), shortlist-*.md, ideas.md
projects/   one folder per video: plan.md, edit.json, frames/, clips/, output/
tools/      assemble.py (edit), review.py (frame-by-frame check), branding.py, ...
music/      YouTube Audio Library tracks only
```

## Skills

- **/luna-ideas** (`.claude/skills/luna-ideas/`) — researches breakout DIY
  Shorts on vidIQ and saves a ranked shortlist of original Luna ideas. Ideas only.
- **/luna-plan** (`.claude/skills/luna-plan/`) — turns a picked idea into
  projects/NNN-slug/plan.md (hero + stage images, one-action clip prompts) and
  edit.json. Planning only.
- **/luna-generate** (`.claude/skills/luna-generate/`) — runs plan.md in Google
  Flow via flow-auto: hero (approve) → stage frames (approve) → Veo clips,
  each checked and saved into the project. Free plan: keep the Flow tab visible
  and the Flow Connector side panel open.

## Making a video

1. Pick an idea from `ideas/ideas.md`; its prompts go in
   `projects/<id>/prompts.md`.
2. In Google Flow, for each clip: start image with **Nano Banana 2** (x1,
   9:16, Luna character), then **Veo 3.1 Fast** (x1, 9:16, 8 s) from that
   image. Download to `projects/<id>/clips/c1.mp4`, `c2.mp4`, …
3. Adjust the trims in `projects/<id>/edit.json`, then:

   ```sh
   python3 tools/assemble.py projects/<id>
   ```

   → `projects/<id>/output/final.mp4`: 1080×1920, music bed, logo, −14 LUFS.
4. Upload to YouTube **Private** first, wait for the copyright check, then
   schedule it. Mark *Altered or synthetic content: Yes*. Post the same file
   to TikTok with *AI-generated content* on.

## Credits

Flow: Veo 3.1 Fast = 20 credits per clip, Quality = 100. A 5-clip video is
~100 credits. From October, Higgsfield's official MCP
(`claude mcp add --transport http higgsfield https://mcp.higgsfield.ai/mcp`)
lets the clips be generated from here.
