"""Join the rendered chapter MP4s into one iPhone-friendly file with chapter markers.

Usage: python stitch.py <media quality dir name, e.g. 1080p30> <out.mp4>
"""
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
quality, out = sys.argv[1], sys.argv[2]

chapters = []
for f in sorted(glob.glob(os.path.join(ROOT, "ch*_*.py"))):
    src = open(f).read()
    cls = re.search(r"^class (\w+)", src, re.M).group(1)
    label = re.search(r'chapter_label = "(.+?)"', src).group(1)
    mod = os.path.splitext(os.path.basename(f))[0]
    mp4 = os.path.join(ROOT, "media", "videos", mod, quality, f"{cls}.mp4")
    chapters.append((label, mp4))


def duration(p):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", p]).decode().strip())


build = os.path.join(ROOT, "build")
os.makedirs(build, exist_ok=True)
lst = os.path.join(build, "concat.txt")
meta = os.path.join(build, "chapters.txt")
with open(lst, "w") as f:
    for _, p in chapters:
        f.write(f"file '{p}'\n")
t = 0.0
with open(meta, "w") as f:
    f.write(";FFMETADATA1\ntitle=AI Startups: Offers, Equity, and the Landscape\n")
    for label, p in chapters:
        d = duration(p)
        f.write(f"[CHAPTER]\nTIMEBASE=1/1000\nSTART={int(t*1000)}\nEND={int((t+d)*1000)}\ntitle={label}\n")
        t += d

# Re-encode so every chapter shares identical stream parameters, AAC audio,
# and moov atom up front for quick start on iPhone.
subprocess.check_call([
    "ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst,
    "-i", meta, "-map_metadata", "1", "-map_chapters", "1",
    "-c:v", "libx264", "-preset", "medium", "-crf", "22", "-pix_fmt", "yuv420p",
    "-profile:v", "high", "-tune", "animation",
    # Podcast-level loudness so it is audible over road noise.
    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
    "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-ac", "2",
    "-movflags", "+faststart", out])
print(f"wrote {out} ({t/60:.1f} min)")
