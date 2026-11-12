# Music

Background beds for the narrated videos. The pipeline picks one per video by
mood (the list lives in `studio/config.py`), and `plan.json` can be edited to
pick a different one before approving.

## YouTube Audio Library only

Every track here is from YouTube's own catalogue, so it cannot be Content ID
claimed on YouTube.

| Track | Length | Mood |
|---|---|---|
| Sunset Strut — Dan Lebowitz | 1:58 | relaxed, sits well back under a voice |
| 35,000 Feet — The Mini Vandals | 2:20 | light, hopeful |
| Country Rough — Everet Almond | 2:40 | rustic, outdoor, timber and land work |
| (Put On Your) Dancing Pants — Reed Mathis | 2:39 | playful |
| Double You — The Mini Vandals | 2:43 | upbeat, busy |
| Star Spangled Banner — Cooper Cannell | 2:06 | guitar instrumental |
| Get Tough — TrackTribe | 2:23 | driving rock, big machinery |
| Big 10 — TrackTribe | 1:58 | loud, triumphant |
| Greaser — TrackTribe | 1:32 | punchy rock; loops on a long video |

Tracks shorter than the video loop. Two minutes or more avoids an audible
loop on most videos.

## Levels

`finish.py` sets the bed 12 dB under the narration, measured from both files
(`--music-under-voice`), and ducks it a further 11 dB while the voice is
speaking. Tracks arrive anywhere from −8 to −16 LUFS, so a fixed gain would
bury the voice on one track and lose the music on another.

## Adding tracks

Download from the Audio Library (YouTube Studio → Audio Library), drop the
file in here, and add a line with its mood to `MUSIC_LIBRARY` in
`studio/config.py`. Some tracks ask for attribution — check the Audio Library
entry and add the credit to the description if so.

## Licensing

Audio Library tracks are licensed for **YouTube**. Posting the same video to
TikTok or Instagram is outside that licence and those platforms run their own
audio matching — use their own music libraries when cross-posting.

A download button on a "free music" site is not a licence, and "royalty free"
does not mean "not registered in Content ID". A track removed from this folder
earlier was registered by a rights holder and produced a claim on a real
upload.
