import math

from common import *


class Ch5Landscape(NarratedScene):
    chapter_label = "5 · The landscape today"

    def layer(self, name, sub, examples, color, width=12.4):
        box = RoundedRectangle(corner_radius=0.15, width=width, height=1.05,
                               stroke_color=color, stroke_width=3,
                               fill_color=color, fill_opacity=0.10)
        n = T(name, size=34, color=color, weight=BOLD)
        s = T(sub, size=22, color=DIM)
        left = VGroup(n, s).arrange(DOWN, aligned_edge=LEFT, buff=0.06)
        ex = T(examples, size=24)
        left.move_to(box.get_left() + RIGHT * 0.3, aligned_edge=LEFT)
        ex.move_to(box.get_right() + LEFT * 0.3, aligned_edge=RIGHT)
        if ex.width > width - left.width - 1:
            ex.scale_to_fit_width(width - left.width - 1)
            ex.move_to(box.get_right() + LEFT * 0.3, aligned_edge=RIGHT)
        return VGroup(box, left, ex)

    def construct(self):
        self.play(FadeIn(chapter_card(5, "The landscape today",
                                      "Who builds what, who's worth what, and where the talent goes")))
        self.say("""Chapter five. The landscape today. The easiest way to understand A.I.
        startups is as a stack of layers, like a building. Each layer depends on the one
        below it, and the money and the risk look very different on each floor.""")
        self.done()
        self.clear_all()

        layers = [
            ("Applications", "products people use", "Cursor · Harvey · Perplexity · ElevenLabs · Abridge", GREEN_),
            ("Dev tools & infra", "help others build with AI", "inference clouds · evals · agents frameworks · vector DBs", TEAL_),
            ("Data & labeling", "training data, human feedback", "Scale AI · Surge · Mercor", ORANGE_),
            ("Frontier labs", "train the giant models", "OpenAI · Anthropic · Google DeepMind · xAI · Mistral", BLUE_),
            ("Compute", "chips, data centers", "Nvidia · CoreWeave · Lambda · Crusoe", PURPLE_),
        ]
        stack = VGroup(*[self.layer(*l) for l in layers]).arrange(DOWN, buff=0.15).shift(DOWN * 0.15)
        fit(stack, 12.8, 6.4)
        order = [4, 3, 2, 1, 0]

        self.say("""At the bottom is compute: the chips and the data centers. Nvidia makes
        the chips, and newer cloud companies like CoreWeave and Crusoe rent them out. This
        layer is capital heavy. It's real estate and electricity as much as software.""")
        self.play(FadeIn(stack[4], shift=UP * 0.3))
        self.done()

        self.say("""Above that are the frontier labs, the companies that train the giant
        models. OpenAI, Anthropic, Google DeepMind, x A I, and in Europe, Mistral. Plus a
        newer group people call neo labs, started by famous researchers who left the big
        labs, like Thinking Machines and Safe Superintelligence. Training a top model now
        costs billions, so this layer is a small club with enormous funding.""")
        self.play(FadeIn(stack[3], shift=UP * 0.3))
        self.done()

        self.say("""Next, data. Models learn from data and human feedback, and companies
        like Scale A.I., Surge, and Mercor sell that, often by hiring huge networks of
        experts, from coders to doctors, to grade and write examples.""")
        self.play(FadeIn(stack[2], shift=UP * 0.3))
        self.done()

        self.say("""Then developer tools and infrastructure. These help everyone else build
        with A.I.: running models cheaply and quickly, testing whether an A.I. feature
        actually works, connecting models to company data, and frameworks for agents. This
        is where a lot of classic, hard software engineering lives.""")
        self.play(FadeIn(stack[1], shift=UP * 0.3))
        self.done()

        self.say("""And on top, applications: products for real users. Coding tools like
        Cursor and Cognition. Legal A.I. like Harvey. Search like Perplexity. Voice like
        ElevenLabs. Medical note taking like Abridge. Customer support agents like Sierra
        and Decagon. This is the biggest and most crowded floor.""")
        self.play(FadeIn(stack[0], shift=UP * 0.3))
        self.done()

        self.say("""Two more neighborhoods sit a little outside the stack, and one of them
        is especially relevant to you. Robotics, like Figure and Physical Intelligence,
        putting models into machines. And defense technology: Anduril, Shield A.I.,
        Saronic, Applied Intuition. Defense tech is one of the fastest growing corners of
        venture funding, and engineers who already understand government customers,
        security requirements, and how the Defense Department buys things are rare and
        valuable there. If you hold, or could hold, a clearance, that's a real edge.""")
        self.play(stack.animate.scale(0.62).to_edge(LEFT, buff=0.4).shift(DOWN * 0.2))
        side = VGroup(
            card(["Robotics", "Figure · Physical Intelligence"], width=5.0, color=RED_, size=26),
            card(["Defense tech", "Anduril · Shield AI · Saronic", "← your DoD background"], width=5.0, color=YELLOW_, size=26),
        ).arrange(DOWN, buff=0.4).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.2)
        self.play(FadeIn(side[0], shift=LEFT * 0.3))
        self.wait(min(6, max(0.1, self.left() / 3)))
        self.play(FadeIn(side[1], shift=LEFT * 0.3))
        self.done()
        self.clear_all()

        # ---- valuations ----
        self.say("""Now, who's worth what. These are the last reported valuations, from
        funding announcements, filings, and wire reporting, as of October twenty twenty
        six. The bar lengths are on a stretched scale: every step is ten times bigger than
        the last, otherwise the small ones would be invisible.""")
        data = [
            ("Anthropic", 965, "Series H, May 2026", BLUE_),
            ("OpenAI", 852, "Mar 2026", BLUE_),
            ("xAI", 250, "merged into SpaceX, 2026", BLUE_),
            ("Cursor", 60, "SpaceX all-stock deal", GREEN_),
            ("Figure", 39, "Sept 2025 round", RED_),
            ("Anduril", 30.5, "June 2025 round", YELLOW_),
            ("Cognition", 26, "reported, 2026", GREEN_),
            ("Perplexity", 20, "Sept 2025 round", GREEN_),
            ("Mistral", 14, "Sept 2025 round", BLUE_),
            ("Thinking Machines", 12, "2025 seed round", BLUE_),
        ]
        hdr = title("Last reported valuations, $ billions", size=46)
        sub = T("log scale · approximate · Oct 2026", size=24, color=DIM).next_to(hdr, DOWN, buff=0.15)
        self.play(Write(hdr), FadeIn(sub))
        rows = VGroup()
        for i, (name, v, note, c) in enumerate(data):
            y = 1.75 - i * 0.52
            w = 5.4 * math.log10(v) / 3.0
            lab = T(name, size=26).move_to(np.array([-3.6, y, 0]), aligned_edge=RIGHT)
            bar = Rectangle(width=w, height=0.38, fill_color=c, fill_opacity=0.9,
                            stroke_width=0).move_to(np.array([-3.35, y, 0]), aligned_edge=LEFT)
            val = T(f"${v:g}B", size=26, color=c, weight=BOLD).next_to(bar, RIGHT, buff=0.15)
            nt = T(note, size=19, color=DIM).next_to(val, RIGHT, buff=0.2)
            rows.add(VGroup(lab, bar, val, nt))
        self.play(LaggedStart(*[AnimationGroup(FadeIn(r[0]), GrowFromEdge(r[1], LEFT), FadeIn(r[2]), FadeIn(r[3]))
                                for r in rows], lag_ratio=0.25), run_time=min(8, max(3, self.left() - 1)))
        self.done()

        self.say("""The pattern: a handful of labs worth hundreds of billions, a few dozen
        application and infrastructure companies worth tens of billions, and then
        thousands of startups worth under a billion, most of which you've never heard of.
        Most job openings are in that long tail. And the value is extremely concentrated at
        the top, which is the power law from chapter two, at the scale of whole
        companies.""")
        self.done()
        self.clear_all()

        # ---- how valuations are set ----
        self.say("""How do companies get valued so high? Mostly as a multiple of revenue,
        and a bet on growth. Anthropic reported a revenue run rate of about forty seven
        billion dollars a year in May, and reports say it rose to around sixty five billion
        by summer. Divide a nine hundred sixty five billion dollar valuation by sixty five
        billion and you get about fifteen times revenue. For a normal company that's high.
        For one growing several times per year, investors think it's cheap. Smaller hot A.I.
        startups regularly raise at fifty or even a hundred times their revenue, which only
        works out if they keep growing very fast for years.""")
        h = title("Valuation ≈ revenue × multiple", size=52)
        eq = VGroup(
            T("$965B  ÷  ~$65B run-rate", size=50),
            T("≈ 15× revenue", size=80, color=YELLOW_, weight=BOLD),
            T("hot early-stage AI: often 50–100×", size=40, color=RED_),
        ).arrange(DOWN, buff=0.5).shift(DOWN * 0.3)
        self.play(Write(h))
        self.play(FadeIn(eq[0]))
        self.wait(min(10, max(0.1, self.left() * 0.35)))
        self.play(FadeIn(eq[1], scale=1.2))
        self.wait(min(6, max(0.1, self.left() * 0.4)))
        self.play(FadeIn(eq[2]))
        self.done()
        self.clear_all()

        # ---- where the best people work ----
        self.say("""Where do the best people work? Three clusters. One, the frontier labs.
        They pay the most, often well into the hundreds of thousands per year in total
        compensation for engineers, mostly in stock, and they hire a lot of regular
        software engineers for infrastructure and product, not just researchers. Two, the
        neo labs and the very best application companies, small teams of very strong
        people, often founded by alumni of the big labs. Three, a scattering of tiny early
        teams where two or three exceptional founders are working on something before
        anyone else noticed. That third group is where the biggest equity percentages
        are, and also where most companies fail.""")
        h = title("Where top people cluster", size=52)
        cl = VGroup(
            card(["Frontier labs", "highest pay", "big, liquid-ish equity", "very selective"], width=4.0, color=BLUE_, size=28),
            card(["Neo-labs & top apps", "small, dense teams", "lab alumni founders", "fast growth"], width=4.0, color=GREEN_, size=28),
            card(["Tiny early teams", "biggest % ownership", "highest failure rate", "learn the most, fastest"], width=4.0, color=YELLOW_, size=28),
        ).arrange(RIGHT, buff=0.3).shift(DOWN * 0.3)
        fit(cl, 13)
        self.play(Write(h))
        for c_ in cl:
            self.play(FadeIn(c_, shift=UP * 0.3), run_time=0.7)
            self.wait(min(10, max(0.1, self.left() / 4)))
        self.done()

        self.say("""A useful idea here is talent density. One great engineer learning
        next to ten great engineers improves fast. So when people say the best people work
        somewhere, what they really mean is that the people there make each other better.
        That's worth more to your career than any one equity grant, and it's the main
        theme of the next chapter.""")
        self.done()
        self.clear_all()

        # ---- money by tier ----
        self.say("""Last part of the landscape: what the money looks like on each tier,
        for someone like you. At a big lab worth hundreds of billions, your equity might
        be large in dollars and fairly safe, with regular tender offers, but the company
        probably can't grow another hundred times. At a growth stage company worth one to
        fifty billion, equity is meaningful and there's real upside, plus a real risk that
        the labs build your product themselves. At an early startup, your percentage is
        biggest and the outcome is most likely zero, with a small chance of life changing.""")
        h = title("Risk and upside by tier", size=50)
        ax = Axes(x_range=[0, 10, 1], y_range=[0, 10, 1], x_length=8.5, y_length=5,
                  axis_config={"color": DIM, "include_ticks": False}, tips=True).shift(DOWN * 0.5 + LEFT * 0.5)
        xl = T("chance your equity is worth $0 →", size=24, color=DIM).next_to(ax.x_axis, DOWN, buff=0.2)
        yl = T("upside multiple →", size=24, color=DIM).rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.2)
        pts = [(2, 2.5, "Frontier lab", BLUE_), (5, 5.5, "Growth-stage app", GREEN_),
               (8.3, 8.8, "Seed / Series A", YELLOW_)]
        self.play(Write(h), Create(ax), FadeIn(xl), FadeIn(yl))
        for x, y, n, c in pts:
            d = Dot(ax.c2p(x, y), radius=0.16, color=c)
            l = T(n, size=30, color=c, weight=BOLD).next_to(d, RIGHT, buff=0.2)
            self.play(GrowFromCenter(d), FadeIn(l), run_time=0.7)
            self.wait(min(8, max(0.1, self.left() / 4)))
        self.done()

        self.say("""There's no free lunch on this chart. Higher upside always comes with a
        higher chance of zero. Which tier is right depends on your savings, your risk
        tolerance, and what you want to learn. A common, sensible path is to start at a
        growth stage company with real revenue, learn how a fast company works, and go
        earlier once you know what great looks like.""")
        self.done()
        self.clear_all()
