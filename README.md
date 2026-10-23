# AI startup landscape: video explainer

A 3Blue1Brown-style explainer video (Manim + Kokoro TTS narration) about startup offers,
equity, funding stages, the AI startup landscape, getting hired, and Taleb's greater-fool critique.

Source is in `video/`. Each chapter is one Manim scene; narration is written inline with
`self.say(...)` and synthesized with Kokoro (cached in `video/build/audio`).

```bash
pip install manim kokoro soundfile   # plus system espeak-ng and pango dev headers
cd video
./render.sh                          # 1080p30, every chapter
python stitch.py 1080p30 build/ai-startups-full.mp4
```
