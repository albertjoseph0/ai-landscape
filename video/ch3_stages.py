from common import *


STAGES = [
    # name, raise, post-money valuation, team, color
    ("Pre-seed / Seed", "$1–5M", "$10–30M", "2–15", YELLOW_),
    ("Series A", "$10–25M", "$40–150M", "15–50", ORANGE_),
    ("Series B", "$25–75M", "$150M–1B", "50–150", GREEN_),
    ("Series C+", "$50–500M+", "$1B+", "150–1,000+", BLUE_),
    ("IPO / public", "public market", "set by market", "1,000+", PURPLE_),
]


class Ch3Stages(NarratedScene):
    chapter_label = "3 · Seed to IPO: the stages"

    def construct(self):
        self.play(FadeIn(chapter_card(3, "Seed to IPO: the stages",
                                      "Funding, valuation, team size, and what the job is like")))
        self.say("""Chapter three. Seed to I.P.O. When people say a company is "Series B,"
        they're telling you a lot in two words: roughly how much money it has, how big the
        team is, and what the engineering job will feel like. Let's decode it.""")
        self.done()
        self.clear_all()

        # ---- what a round is ----
        self.say("""First, what's a round? A startup sells a chunk of itself to investors
        for cash, to fund the next stretch of growth. Two numbers define it. How much they
        raise, and the valuation. Say a seed round raises four million dollars at a twenty
        million dollar post money valuation, meaning the company is worth twenty million
        right after the cash comes in. The investors now own four divided by twenty, or
        twenty percent. Everyone else, founders and employees, got diluted by that twenty
        percent. Each later round repeats this, usually selling fifteen to twenty five
        percent, at a hopefully much higher price.""")
        h = title("What a funding round is", size=52)
        eq = VGroup(
            T("raise $4M at a $20M post-money valuation", size=40),
            T("investors own $4M ÷ $20M = 20%", size=52, color=YELLOW_, weight=BOLD),
            T("everyone else: diluted by 20%", size=36, color=DIM),
        ).arrange(DOWN, buff=0.5).shift(DOWN * 0.3)
        self.play(Write(h))
        self.play(FadeIn(eq[0]))
        self.wait(min(10, max(0.1, self.left() / 3)))
        self.play(FadeIn(eq[1], scale=1.1))
        self.wait(min(8, max(0.1, self.left() / 2)))
        self.play(FadeIn(eq[2]))
        self.done()

        self.say("""The money buys time, called runway. A startup burning a million dollars
        a month with eighteen million in the bank has eighteen months to hit the next
        milestone and raise again. Each round is a test: show enough progress to convince
        the next, bigger investor. That's the treadmill behind every startup, and it's
        useful to know where in the cycle a company is when you join. Ask, "how much
        runway do you have?" It's a normal question.""")
        self.play(FadeOut(eq))
        rw = VGroup(
            T("runway = cash in the bank ÷ monthly burn", size=44),
            T("$18M ÷ $1M / month = 18 months", size=52, color=GREEN_, weight=BOLD),
            T("ask: \"how much runway do you have?\"", size=36, color=DIM),
        ).arrange(DOWN, buff=0.5).shift(DOWN * 0.3)
        self.play(FadeIn(rw[0]))
        self.wait(min(8, max(0.1, self.left() / 3)))
        self.play(FadeIn(rw[1]))
        self.wait(min(10, max(0.1, self.left() / 2)))
        self.play(FadeIn(rw[2]))
        self.done()
        self.clear_all()

        # ---- staircase ----
        self.say("""Now the ladder. These are typical ranges for U.S. startups in general,
        and they vary a lot. A.I. companies run larger, which I'll come back to. At pre
        seed and seed, a company raises one to five million dollars, at a valuation of ten
        to thirty million, and has between two and fifteen people.""")
        h = title("The funding ladder (typical U.S. ranges)", size=46)
        hdr = VGroup(T("stage", size=26, color=DIM), T("raises", size=26, color=DIM),
                     T("valued at", size=26, color=DIM), T("team", size=26, color=DIM))
        xs = [-4.4, -0.7, 2.3, 5.1]
        for t_, x in zip(hdr, xs):
            t_.move_to(np.array([x, 2.0, 0]))
        rows = VGroup()
        for i, (n, r, v, team, c) in enumerate(STAGES):
            y = 1.25 - i * 0.82
            cells = VGroup(T(n, size=32, color=c, weight=BOLD), T(r, size=32), T(v, size=32), T(team, size=32))
            for t_, x in zip(cells, xs):
                t_.move_to(np.array([x, y, 0]))
            bg = RoundedRectangle(corner_radius=0.1, width=12.8, height=0.7, stroke_width=0,
                                  fill_color=c, fill_opacity=0.10).move_to(np.array([0.3, y, 0]))
            rows.add(VGroup(bg, cells))
        self.play(Write(h), FadeIn(hdr))
        self.play(FadeIn(rows[0], shift=UP * 0.2))
        self.done()

        self.say("""At Series A, roughly ten to twenty five million dollars raised, at a
        forty to one hundred fifty million valuation, with fifteen to fifty people. Series B,
        twenty five to seventy five million, valued at a hundred fifty million to a billion,
        and fifty to a hundred fifty people. Series C and beyond, the growth stage, raises
        fifty million to half a billion or more, and the company is usually worth over a
        billion, which is where the word unicorn comes from. Teams there run from a hundred
        fifty to over a thousand. And then, an I.P.O., where the public market sets the
        price.""")
        for r in rows[1:]:
            self.play(FadeIn(r, shift=UP * 0.2), run_time=0.7)
            self.wait(min(9, max(0.1, self.left() / 5)))
        self.done()

        self.say("""Now, A.I. has bent this ladder. Because training and running models is
        expensive, and investors are so eager, A.I. companies often raise far more at each
        stage. Some seed rounds today are bigger than the Series C rounds of ten years ago.
        Thinking Machines, started by OpenAI's former C.T.O., reportedly raised about two
        billion dollars as a seed round in twenty twenty five, at a twelve billion dollar
        valuation. And the frontier labs raise tens of billions at a time. So when an A.I.
        company says Series A, check the actual numbers, not just the letter.""")
        note = card(["AI bends the ladder", "Thinking Machines: ~$2B seed at ~$12B (2025)",
                     "frontier labs: tens of billions per round"], width=10, color=RED_, size=30)
        note.shift(DOWN * 0.4)
        self.play(FadeOut(rows), FadeOut(hdr), FadeIn(note, shift=UP * 0.2))
        self.done()
        self.clear_all()

        # ---- equity by stage ----
        self.say("""This ladder connects straight back to your offer. The earlier you join,
        the bigger your percentage, and the lower your strike price, because the company
        is cheaper. A first engineer at a seed company might get half a percent to two
        percent. At Series A, maybe a tenth to half a percent. At Series B, a few
        hundredths of a percent to about a tenth, like our example offer. At the growth
        stage, usually a few hundredths or less. And salaries move the other way: often
        below market at seed, and at or near big tech levels by the growth stage.""")
        h = title("What an engineer typically gets", size=50)
        data = [("Seed", "0.5–2%", "below market", YELLOW_),
                ("Series A", "0.1–0.5%", "near market", ORANGE_),
                ("Series B", "0.03–0.15%", "market", GREEN_),
                ("Series C+", "≤ 0.05%", "market, near big tech", BLUE_)]
        tbl = VGroup()
        for i, (n, e, s, c) in enumerate(data):
            y = 1.3 - i * 0.95
            row = VGroup(T(n, size=36, color=c, weight=BOLD).move_to(np.array([-4.3, y, 0])),
                         T(e, size=40, weight=BOLD).move_to(np.array([-0.2, y, 0])),
                         T(s, size=32, color=DIM).move_to(np.array([3.9, y, 0])))
            tbl.add(row)
        hh = VGroup(T("equity", size=26, color=DIM).move_to(np.array([-0.2, 2.1, 0])),
                    T("salary", size=26, color=DIM).move_to(np.array([3.9, 2.1, 0])))
        foot = T("rough ranges for a mid-level SWE; ask for your actual %", size=24, color=DIM).to_edge(DOWN, buff=0.4)
        self.play(Write(h), FadeIn(hh))
        for r in tbl:
            self.play(FadeIn(r, shift=UP * 0.2), run_time=0.6)
            self.wait(min(8, max(0.1, self.left() / 5)))
        self.play(FadeIn(foot))
        self.done()
        self.clear_all()

        # ---- roles & work at each stage ----
        self.say("""Now the part that affects your day to day the most: the job itself.
        At seed, there's usually no such thing as a role. You're a founding engineer. You
        build the whole product, frontend, backend, infrastructure, and you talk to
        customers directly. You'll be on call for everything, there's no code review
        process unless you create one, and nobody's going to teach you. You learn by doing
        and by watching the founders. The upside is enormous ownership. The downside is no
        mentorship and a high chance the company dies.""")
        h = title("What the job is like", size=52)
        self.play(Write(h))
        cards = VGroup(
            card(["Seed", "founding engineer: build everything", "talk to customers · no process, no mentor"], width=6.1, color=YELLOW_, size=26, title_size=32),
            card(["Series A", "early engineers, first eng manager", "ship fast to find fit · some code review"], width=6.1, color=ORANGE_, size=26, title_size=32),
            card(["Series B", "teams specialize: infra · product · ML", "first SRE + security · scaling, reliability"], width=6.1, color=GREEN_, size=26, title_size=32),
            card(["Series C+", "levels: senior, staff · dedicated teams", "on-call rotations · narrower scope"], width=6.1, color=BLUE_, size=26, title_size=32),
        ).arrange_in_grid(2, 2, buff=0.25).shift(DOWN * 0.45)
        fit(cards, 13.2, 5.9)
        self.play(FadeIn(cards[0], shift=UP * 0.3))
        self.done()

        self.say("""At Series A, there are a handful of early engineers and maybe a first
        engineering manager. The job is to ship fast while the company figures out exactly
        what customers will pay for. Code gets thrown away a lot. That's normal.""")
        self.play(FadeIn(cards[1], shift=UP * 0.3))
        self.done()

        self.say("""Around Series B, the product works and the job becomes scaling it.
        Teams start to specialize: infrastructure and platform, product engineering,
        machine learning engineering, the first dedicated reliability and security people.
        Big customers show up with requirements like audits, uptime promises, and security
        reviews. This is where someone with experience in careful, secure, regulated
        environments, like you, is especially useful.""")
        self.play(FadeIn(cards[2], shift=UP * 0.3))
        self.done()

        self.say("""From Series C onward, it starts to look like a big tech company. Levels
        like senior and staff engineer, career ladders, dedicated teams owning one piece of
        the product, on call rotations, planning cycles. Your scope gets narrower, but the
        mentorship, the stability, and the pay get better, and the equity is less likely to
        be zero.""")
        self.play(FadeIn(cards[3], shift=UP * 0.3))
        self.done()
        self.clear_all()

        # ---- the tradeoff curve ----
        self.say("""Put it on one picture. As a company moves up the ladder, your scope,
        your ownership percentage, and your risk all go down, while structure, mentorship,
        and cash pay go up. There's no best point on this line. It depends on what you
        want next. One common path is to join around Series A or B, when there's real
        traction but still lots of scope, so you get both real responsibility and decent
        odds.""")
        h = title("The tradeoff, stage by stage", size=50)
        ax = Axes(x_range=[0, 4, 1], y_range=[0, 10, 2], x_length=10, y_length=4.6,
                  axis_config={"color": DIM, "include_ticks": False}, tips=False).shift(DOWN * 0.6)
        xl = VGroup(*[T(n, size=24, color=DIM).next_to(ax.c2p(i, 0), DOWN, buff=0.25)
                      for i, n in enumerate(["Seed", "A", "B", "C+", "IPO"])])
        down = ax.plot(lambda x: 9 - 1.9 * x, x_range=[0, 4], color=YELLOW_, stroke_width=6)
        up = ax.plot(lambda x: 1.2 + 1.9 * x, x_range=[0, 4], color=BLUE_, stroke_width=6)
        dl = T("scope · ownership · risk", size=28, color=YELLOW_).next_to(ax.c2p(0.2, 9), RIGHT, buff=0.2)
        ul = T("structure · mentorship · cash", size=28, color=BLUE_).next_to(ax.c2p(2.4, 8.5), LEFT, buff=0.2)
        sweet = Rectangle(width=ax.c2p(2, 0)[0] - ax.c2p(1, 0)[0], height=4.6, stroke_width=0,
                          fill_color=GREEN_, fill_opacity=0.12).move_to(ax.c2p(1.5, 5))
        sl = T("a common sweet spot", size=26, color=GREEN_).next_to(sweet, UP, buff=0.1)
        self.play(Write(h), Create(ax), FadeIn(xl))
        self.play(Create(down), FadeIn(dl))
        self.wait(min(6, max(0.1, self.left() / 4)))
        self.play(Create(up), FadeIn(ul))
        self.wait(min(10, max(0.1, self.left() / 2)))
        self.play(FadeIn(sweet), FadeIn(sl))
        self.done()
        self.clear_all()
