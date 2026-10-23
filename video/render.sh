#!/usr/bin/env bash
# Usage: ./render.sh [quality flags...]   e.g. ./render.sh -ql   or   ./render.sh (1080p30)
# Renders every chapter, then stitches them into one MP4 with chapter markers.
set -euo pipefail
cd "$(dirname "$0")"
Q=("$@"); [ ${#Q[@]} -eq 0 ] && Q=(-r 1920,1080 --frame_rate 30)
for f in ch*_*.py; do
  cls=$(grep -oP '^class \K\w+' "$f")
  manim "${Q[@]}" "$f" "$cls"
done
