from common import *


class Ch0Basics(NarratedScene):
    chapter_label = "0 · The basics"

    def construct(self):
        self.say("""Hey Albert. This is a video about one question: if you left your
        current job for an A.I. startup, what would you actually get, and how would it
        ever turn into money? It's built for the car, so you don't need to watch.
        Everything important is in the audio, and the screen is a bonus. Before we get to
        startup offers, we'll spend a few minutes on the basics, the handful of finance
        ideas everything else builds on. If you've taken a personal finance course,
        some of this will be review, but startups use these ideas in ways that are a bit
        different from your four oh one k.""")
        self.play(FadeIn(chapter_card(0, "The basics",
                                      "The finance ideas the rest of the video builds on")))
        self.done()
        self.clear_all()

        # ---- shares ----
        self.say("""Idea one: a company is cut into shares. Owning a share means owning a
        tiny slice of the company. Picture a pizza cut into a hundred slices. If you own
        one slice, you own one percent. Real companies are cut into millions or billions
        of slices, but the idea is the same. Your slice of the company is called equity.
        So when a startup offers you equity, it's offering you slices of the pizza.""")
        h = title("Idea 1: a company is cut into shares", size=50)
        pizza = VGroup(*[Sector(radius=2.2, angle=TAU / 12, start_angle=i * TAU / 12,
                                stroke_color=BG, stroke_width=4, fill_color=ORANGE_, fill_opacity=0.85)
                         for i in range(12)]).shift(LEFT * 3 + DOWN * 0.4)
        lbl = VGroup(
            T("shares = slices", size=40, weight=BOLD),
            T("own 1 of 100 slices = own 1%", size=34, color=DIM),
            T("your slice is called equity", size=34, color=YELLOW_),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(pizza, RIGHT, buff=1.0)
        self.play(Write(h))
        self.play(LaggedStart(*[FadeIn(s, scale=0.8) for s in pizza], lag_ratio=0.08), run_time=2)
        self.play(pizza[0].animate.shift(RIGHT * 0.35 + UP * 0.1).set_fill(YELLOW_), FadeIn(lbl[0]))
        self.wait(min(8, max(0.1, self.left() / 3)))
        self.play(FadeIn(lbl[1]))
        self.wait(min(8, max(0.1, self.left() / 2)))
        self.play(FadeIn(lbl[2]))
        self.done()
        self.clear_all()

        # ---- valuation ----
        self.say("""Idea two: a company's value, which people call its valuation, is just
        the price of one share times the number of shares. If a share costs ten dollars
        and there are a hundred million shares, the company is valued at one billion
        dollars. That works the other way too. If you know the valuation and the number
        of shares, you can figure out what one share costs. We'll use that trick a lot.""")
        h = title("Idea 2: valuation = price per share × shares", size=46)
        eq = VGroup(
            T("$10 per share  ×  100,000,000 shares", size=44),
            T("= $1 billion valuation", size=64, color=GREEN_, weight=BOLD),
        ).arrange(DOWN, buff=0.6).shift(DOWN * 0.3)
        self.play(Write(h))
        self.play(FadeIn(eq[0]))
        self.wait(min(8, max(0.1, self.left() / 3)))
        self.play(FadeIn(eq[1], scale=1.1))
        self.done()
        self.clear_all()

        # ---- public vs private ----
        self.say("""Idea three, and this is the big one: public versus private companies.
        The stocks in your four oh one k or an index fund are public companies, like Apple
        or Google. Their shares trade on a stock exchange every day. If you own Apple
        stock, you can sell it this afternoon and have cash in your account in a day or
        two. That's called being liquid. Startups are private companies. There's no stock
        exchange for their shares. You can't just click sell. So startup shares are
        illiquid: they may be worth a lot on paper, but turning them into cash is hard
        until something special happens, like the company being bought or going public.
        Going public, by the way, is called an I.P.O., an initial public offering: the
        day a private company's shares start trading on the stock exchange.""")
        h = title("Idea 3: public vs. private", size=52)
        cmp = VGroup(
            card(["Public company", "Apple, Google, your index fund", "trades on a stock exchange",
                  "sell any day: liquid"], width=5.9, color=GREEN_, size=28),
            card(["Private company", "startups", "no stock exchange",
                  "hard to sell: illiquid"], width=5.9, color=RED_, size=28),
        ).arrange(RIGHT, buff=0.5).shift(DOWN * 0.2)
        ipo = T("IPO = the day a private company starts trading publicly", size=32, color=YELLOW_).to_edge(DOWN, buff=0.5)
        self.play(Write(h))
        self.play(FadeIn(cmp[0], shift=UP * 0.2))
        self.wait(min(15, max(0.1, self.left() / 3)))
        self.play(FadeIn(cmp[1], shift=UP * 0.2))
        self.wait(min(15, max(0.1, self.left() / 2)))
        self.play(FadeIn(ipo))
        self.done()
        self.clear_all()

        # ---- paper value ----
        self.say("""That leads to idea four: paper value versus cash. Since nobody trades
        private shares every day, how do we know what they're worth? Mostly from the last
        time investors bought some. If an investor paid ten dollars a share last year,
        people say the shares are worth ten dollars. But that's a guess based on one
        sale. It's paper value. Cash is money in your bank account that you can spend.
        A lot of this video is about the gap between those two things.""")
        h = title("Idea 4: paper value ≠ cash", size=52)
        two = VGroup(
            card(["Paper value", "what the last investor", "paid, times your shares", "can't spend it"], width=5.6, color=YELLOW_, size=30),
            card(["Cash", "money in your", "bank account", "can spend it"], width=5.6, color=GREEN_, size=30),
        ).arrange(RIGHT, buff=0.6).shift(DOWN * 0.3)
        self.play(Write(h))
        self.play(FadeIn(two[0], shift=UP * 0.2))
        self.wait(min(12, max(0.1, self.left() / 2.5)))
        self.play(FadeIn(two[1], shift=UP * 0.2))
        self.done()
        self.clear_all()

        # ---- how startups get money ----
        self.say("""Idea five: where startups get money. A startup usually doesn't earn
        enough to pay its bills yet. Instead of borrowing from a bank, it sells slices of
        itself to investors. The main investors are venture capital firms, or V.C.s. A V.C.
        firm collects money from pension funds, universities, and wealthy people, and
        invests it in many startups. This isn't a loan. If the startup fails, the
        investors just lose their money, and nobody pays it back. V.C.s expect most of
        their startups to fail, and they make all their returns from the one or two that
        become huge. Each time a startup sells slices to investors, that's called a funding
        round, and it sets a new price per share.""")
        h = title("Idea 5: startups sell slices to investors", size=48)
        lp = card(["Pensions, universities,", "wealthy people"], width=4.0, color=DIM, size=28)
        vc = card(["VC firm", "pools the money"], width=3.3, color=BLUE_, size=28)
        st = card(["Startups", "sell slices", "for cash"], width=3.3, color=GREEN_, size=28)
        row = VGroup(lp, vc, st).arrange(RIGHT, buff=0.8).shift(DOWN * 0.1)
        fit(row, 13)
        a1 = Arrow(lp.get_right(), vc.get_left(), buff=0.1, color=DIM)
        a2 = Arrow(vc.get_right(), st.get_left(), buff=0.1, color=DIM)
        note = T("not a loan: if the startup fails, the money is just gone", size=30, color=RED_).to_edge(DOWN, buff=0.7)
        self.play(Write(h))
        self.play(FadeIn(lp))
        self.play(GrowArrow(a1), FadeIn(vc))
        self.play(GrowArrow(a2), FadeIn(st))
        self.wait(min(15, max(0.1, self.left() / 3)))
        self.play(FadeIn(note))
        self.done()
        self.clear_all()

        self.say("""And that's why startups pay employees partly in equity. They're short on
        cash, so they offer slices instead, and it gives employees the same reason to
        work hard that the founders have: if the company wins, everyone with slices wins.""")
        self.done()

        # ---- taxes ----
        self.say("""Idea six: two kinds of tax. Your salary is ordinary income, taxed at
        your normal income tax rate. When you sell something for more than you paid for
        it, the profit is a capital gain. If you held it for more than a year before
        selling, it's a long term capital gain, taxed at a lower rate, for most people
        fifteen percent federally. If you held it a year or less, it's taxed like ordinary
        income. What you originally paid is called your cost basis. Startup equity can be
        taxed either way depending on how and when you do things, and that difference can
        be tens of thousands of dollars. That's why chapter two spends time on it.""")
        h = title("Idea 6: two kinds of tax", size=52)
        tx = VGroup(
            card(["Ordinary income", "salary, bonuses", "your normal tax rate"], width=5.6, color=ORANGE_, size=30),
            card(["Capital gains", "profit when you sell", "held > 1 year: lower rate", "(often 15% federal)"], width=5.6, color=GREEN_, size=30),
        ).arrange(RIGHT, buff=0.6).shift(DOWN * 0.2)
        basis = T("cost basis = what you originally paid", size=32, color=DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h))
        self.play(FadeIn(tx[0], shift=UP * 0.2))
        self.wait(min(10, max(0.1, self.left() / 3)))
        self.play(FadeIn(tx[1], shift=UP * 0.2))
        self.wait(min(12, max(0.1, self.left() / 2)))
        self.play(FadeIn(basis))
        self.done()
        self.clear_all()

        # ---- diversification / average vs typical ----
        self.say("""Idea seven: concentration and risk. Your index fund owns hundreds of
        companies. If one fails, you barely notice. That's diversification. Startup equity
        is the opposite: it's all one company, and that company is also the one paying
        your salary. If it fails, you lose your job and your equity at the same time. And
        startups follow what's called a power law: most of them fail or barely return
        anything, and a tiny number return enormous amounts. That means the average outcome
        and the typical outcome are very different, which we'll see with real numbers in
        chapter two.""")
        h = title("Idea 7: one company, not hundreds", size=50)
        idx = VGroup(*[Square(0.32, fill_color=BLUE_, fill_opacity=0.7, stroke_width=0) for _ in range(100)]).arrange_in_grid(10, 10, buff=0.06)
        one = Square(3.5, fill_color=YELLOW_, fill_opacity=0.7, stroke_width=0)
        g = VGroup(VGroup(idx, T("index fund: hundreds of companies", size=28, color=BLUE_)).arrange(DOWN, buff=0.35),
                   VGroup(one, T("startup equity: one company", size=28, color=YELLOW_)).arrange(DOWN, buff=0.35)).arrange(RIGHT, buff=1.4).shift(DOWN * 0.3)
        fit(g, 12.5, 5.6)
        self.play(Write(h))
        self.play(FadeIn(g[0]))
        self.wait(min(8, max(0.1, self.left() / 3)))
        self.play(FadeIn(g[1]))
        self.done()
        self.clear_all()

        # ---- roadmap ----
        self.say("""That's the foundation: shares, valuation, public versus private, paper
        value versus cash, how startups raise money, two kinds of tax, and concentration.
        With those seven ideas, everything else will make sense. Here's where we're going.""")
        chap = [("1", "Your offer, decoded"), ("2", "Turning equity into cash"),
                ("3", "Seed to IPO: the stages"), ("4", "How we got here"),
                ("5", "The landscape today"), ("6", "Who, what, and how"),
                ("7", "How people get hired"), ("8", "Is it a greater fool game?")]
        rows = VGroup(*[
            VGroup(T(n, size=38, color=YELLOW_, weight=BOLD), T(s, size=38))
            .arrange(RIGHT, buff=0.4) for n, s in chap
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.2).shift(DOWN * 0.45)
        hdr = title("The road map")
        self.play(Write(hdr), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rows], lag_ratio=0.25), run_time=3)
        self.done()
        self.clear_all()
