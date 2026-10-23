"""Shared helpers: narration (Kokoro TTS, cached), styling, and layout pieces.

Every chapter scene subclasses NarratedScene and alternates:
    self.say("narration")   # starts the audio for this beat
    self.play(...)          # animations that run while it plays
    self.done()             # waits out whatever audio is left
"""
import hashlib
import os
import re
import wave

import numpy as np
from manim import *

ROOT = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(ROOT, "build", "audio")
VOICE = os.environ.get("KOKORO_VOICE", "af_heart")
SPEED = float(os.environ.get("KOKORO_SPEED", "1.0"))
GAP = 0.35  # breathing room after each beat, seconds

# Palette: dark background, high-contrast accents (phone in daylight).
BG = "#0E1117"
FG = "#F2F2F2"
DIM = "#9AA4B2"
BLUE_ = "#4FC3F7"
YELLOW_ = "#FFD54F"
GREEN_ = "#81C784"
RED_ = "#FF6E6E"
PURPLE_ = "#B39DDB"
ORANGE_ = "#FFB74D"
TEAL_ = "#4DD0C4"

FONT = "Inter"

config.background_color = BG

_pipeline = None


def _tts(text, path):
    global _pipeline
    if _pipeline is None:
        from kokoro import KPipeline
        _pipeline = KPipeline(lang_code="a", repo_id="hexgrad/Kokoro-82M")
    chunks = [a.numpy() if hasattr(a, "numpy") else a
              for _, _, a in _pipeline(text, voice=VOICE, speed=SPEED,
                                        split_pattern=r"\n+")]
    audio = np.concatenate(chunks)
    pcm = (np.clip(audio, -1, 1) * 32767).astype(np.int16)
    tmp = path + ".tmp"
    with wave.open(tmp, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(24000)
        w.writeframes(pcm.tobytes())
    os.replace(tmp, path)


def narration_audio(text):
    """Return (wav_path, seconds) for text, generating it once."""
    os.makedirs(AUDIO_DIR, exist_ok=True)
    clean = re.sub(r"\s+", " ", text).strip()
    key = hashlib.sha1(f"{VOICE}|{SPEED}|{clean}".encode()).hexdigest()[:16]
    path = os.path.join(AUDIO_DIR, f"{key}.wav")
    if not os.path.exists(path):
        _tts(clean, path)
    with wave.open(path) as w:
        return path, w.getnframes() / w.getframerate()


class NarratedScene(Scene):
    chapter_label = ""

    def setup(self):
        self._beat_end = 0.0
        self.script = []  # narration, written out as a transcript
        if self.chapter_label:
            self.tag = Text(self.chapter_label, font=FONT, font_size=20,
                            color=DIM).to_corner(UL, buff=0.2)
            self.add(self.tag)

    def now(self):
        return self.renderer.time

    def say(self, text):
        self.done()
        path, dur = narration_audio(text)
        self.add_sound(path)
        self._beat_end = self.now() + dur + GAP
        self.script.append(re.sub(r"\s+", " ", text).strip())
        return dur

    def left(self):
        return max(0.0, self._beat_end - self.now())

    def done(self):
        rem = self._beat_end - self.now()
        if rem > 0.02:
            self.wait(rem)

    def clear_all(self, run_time=0.6):
        mobs = [m for m in self.mobjects if m is not getattr(self, "tag", None)]
        if mobs:
            self.play(*[FadeOut(m) for m in mobs], run_time=run_time)

    def tear_down(self):
        self.done()
        self.wait(0.5)
        os.makedirs(os.path.join(ROOT, "build", "scripts"), exist_ok=True)
        with open(os.path.join(ROOT, "build", "scripts",
                               f"{type(self).__name__}.txt"), "w") as f:
            f.write("\n\n".join(self.script) + "\n")


# ---------- layout helpers ----------

def T(s, size=40, color=FG, weight=NORMAL, **kw):
    return Text(s, font=FONT, font_size=size, color=color, weight=weight, **kw)


def title(s, size=60, color=FG):
    t = T(s, size=size, color=color, weight=BOLD)
    if t.width > 12.6:
        t.scale_to_fit_width(12.6)
    return t.to_edge(UP, buff=0.75)


def bullets(items, size=40, color=FG, buff=0.38, dot_color=YELLOW_):
    rows = VGroup()
    for it in items:
        c = color
        if isinstance(it, tuple):
            it, c = it
        dot = Dot(radius=0.08, color=dot_color)
        txt = T(it, size=size, color=c)
        rows.add(VGroup(dot, txt).arrange(RIGHT, buff=0.3))
    rows.arrange(DOWN, aligned_edge=LEFT, buff=buff)
    return rows


def card(lines, width=5.5, color=BLUE_, size=36, height=None, title_size=None):
    """Rounded box with a header line and body lines."""
    head, *body = lines
    hdr = T(head, size=title_size or size + 4, color=color, weight=BOLD)
    txts = VGroup(*[T(b, size=size) for b in body]).arrange(DOWN, buff=0.18)
    content = VGroup(hdr, txts).arrange(DOWN, buff=0.3) if body else VGroup(hdr)
    box = RoundedRectangle(corner_radius=0.2,
                           width=max(width, content.width + 0.6),
                           height=height or content.height + 0.6,
                           stroke_color=color, stroke_width=4,
                           fill_color=color, fill_opacity=0.08)
    content.move_to(box)
    return VGroup(box, content)


def chapter_card(num, name, sub=""):
    n = T(f"Chapter {num}", size=36, color=YELLOW_)
    t = T(name, size=76, weight=BOLD)
    g = VGroup(n, t)
    if sub:
        g.add(T(sub, size=36, color=DIM))
    g.arrange(DOWN, buff=0.4)
    if g.width > 13:
        g.scale_to_fit_width(13)
    return g


def money(x):
    if x >= 1e9:
        return f"${x/1e9:,.0f}B" if x % 1e9 == 0 else f"${x/1e9:,.1f}B"
    if x >= 1e6:
        return f"${x/1e6:,.0f}M" if x % 1e6 == 0 else f"${x/1e6:,.1f}M"
    if x >= 1e3:
        return f"${x/1e3:,.0f}K"
    return f"${x:,.0f}"


def fit(m, w=12.5, h=6.2):
    if m.width > w:
        m.scale_to_fit_width(w)
    if m.height > h:
        m.scale_to_fit_height(h)
    return m
