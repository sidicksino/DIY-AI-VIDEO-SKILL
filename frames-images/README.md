# frames-images/

Drop a **step-by-step image** here (a collage with numbered steps, like the
ones from DIY pages), then run:

```
/luna-steps frames-images/<image>.jpeg
```

Optional: a text file with the same name (`<image>.txt`) with your changes,
e.g. "make it white marble, put it in the bedroom".

What happens: Claude reads the steps, plans 4–6 clips of 8 s (one action
each, written second by second so the whole clip is usable), writes our own
frames with Luna, and the usual flow continues (`/luna-generate`, then you
make the clips, then Claude edits).

Rule: copy the **idea and the steps**, never the image. Their picture is
never uploaded to Flow and never shown in our video.
