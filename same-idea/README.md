# same-idea/

Drop a DIY video you want to remake with Luna here (mp4/mov/webm), then run `/same-idea`.

Optional: put your wishes in a text file with the **same name** as the video, e.g.
`cool-planter.mp4` + `cool-planter.txt` containing "make it gold, use a bucket".

What happens:
1. Claude studies the video shot by shot (`tools/analyze_ref.py`) and saves the analysis in `same-idea/_analysis/<video>/`.
2. Claude writes a matching project for Luna in `projects/NNN-…/`: same shots and order, our character, place and design changes, our title/hook/music.
3. The usual flow continues: `/luna-generate` makes the frames, you make the clips, Claude edits.

Rule: copy the **format**, change the **look**. Their footage, music and text are never reused.
