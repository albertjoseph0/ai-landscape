from common import *


class Ch1Offer(NarratedScene):
    chapter_label = "1 · Your offer, decoded"

    def construct(self):
        self.play(FadeIn(chapter_card(1, "Your offer, decoded",
                                      "What the letter says, and what it's worth")))
        self.say("""Chapter one. Your offer, decoded.""")
        self.done()
        self.clear_all()

        # ---- three parts ----
        self.say("""A startup offer has three parts. First, base salary: real money,
        every two weeks, same as now. Second, equity: a slice of ownership in the company,
        which is worth nothing today in your bank account and could be worth a lot, or
        exactly zero, later. Third, everything else: benefits, a signing bonus sometimes,
        and almost never the kind of annual cash bonus or pension you might be used to.""")
        hdr = title("Three parts of an offer")
        parts = VGroup(
            card(["Salary", "cash, every", "paycheck"], width=3.8, color=GREEN_),
            card(["Equity", "ownership,", "illiquid"], width=3.8, color=YELLOW_),
            card(["Other", "benefits,", "maybe a bonus"], width=3.8, color=DIM),
        ).arrange(RIGHT, buff=0.45).shift(DOWN * 0.3)
        self.play(Write(hdr), run_time=0.8)
        for p in parts:
            self.play(FadeIn(p, shift=UP * 0.3), run_time=0.8)
            self.wait(min(2.5, max(0.2, self.left() / 4)))
        self.done()

        self.say("""The salary part is easy. At a well funded A.I. startup, a mid level
        engineer in the New York area often sees something in the range of one fifty to
        two twenty five thousand a year in base pay. Top labs pay more. Very early
        startups can pay less and make it up in equity. Whatever the number, the rule is
        simple: the salary alone should be a deal you'd happily take. Everything else is
        upside.""")
        rng = VGroup(
            T("Typical base, mid-level, NYC area", size=36, color=DIM),
            T("≈ $150K – $225K", size=84, color=GREEN_, weight=BOLD),
            T("Top labs: more  ·  very early: often less", size=34, color=DIM),
        ).arrange(DOWN, buff=0.45).shift(DOWN * 0.2)
        self.play(FadeOut(parts), FadeIn(rng[0]), run_time=0.8)
        self.play(Write(rng[1]), run_time=1.2)
        self.play(FadeIn(rng[2]), run_time=0.8)
        self.wait(max(0.1, self.left() - 4))
        rule = T("Rule 1: the salary alone should be a yes.", size=44,
                 color=YELLOW_, weight=BOLD).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(rule, shift=UP * 0.2))
        self.done()
        self.clear_all()

        # ---- the letter itself ----
        self.say("""Let's start with the actual document. When a startup makes you an
        offer, you usually get a phone call first, then an offer letter, a two or three
        page P.D.F. you sign electronically. Here's what's in it, in roughly the order
        you'll see it.""")
        h = title("What's in the offer letter", size=52)
        paper = RoundedRectangle(corner_radius=0.1, width=7.6, height=5.6, stroke_color=FG,
                                 stroke_width=2, fill_color="#1A1F2B", fill_opacity=1).shift(DOWN * 0.45)
        items = [
            ("Title, start date, manager", DIM),
            ("Base salary: $190,000 / year", GREEN_),
            ("Signing bonus (sometimes)", DIM),
            ("Equity: \"an option to purchase 40,000", YELLOW_),
            ("  shares of Common Stock...\"", YELLOW_),
            ("Benefits: health, 401(k), PTO", DIM),
            ("At-will employment", DIM),
            ("Must sign: confidentiality + invention", RED_),
            ("  assignment agreement (PIIA)", RED_),
            ("Offer expires on: ...", DIM),
        ]
        lines = VGroup(*[T(t, size=26, color=c) for t, c in items]).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        lines.move_to(paper)
        self.play(Write(h), FadeIn(paper))
        self.play(LaggedStart(*[FadeIn(l, shift=RIGHT * 0.1) for l in lines], lag_ratio=0.15), run_time=3)
        self.done()

        self.say("""Notice what the equity line says, and what it doesn't. It gives a number
        of shares, forty thousand. It usually does not tell you a dollar value, the
        percentage of the company, or even the exact strike price, because the strike is set
        later, on the day the board of directors officially approves your grant. Weeks
        after you start, you'll get a separate grant notice, an option agreement, and the
        company's equity plan, usually through a website called Carta or a similar tool.
        That's where your vesting schedule and strike price actually live.""")
        hl = SurroundingRectangle(VGroup(lines[3], lines[4]), color=YELLOW_, buff=0.1)
        self.play(Create(hl))
        side = VGroup(
            T("Says: number of shares", size=28, color=GREEN_),
            T("Usually missing:", size=28, color=RED_),
            T("· dollar value", size=26, color=FG),
            T("· % of company", size=26, color=FG),
            T("· exact strike price", size=26, color=FG),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        self.play(VGroup(paper, lines, hl).animate.shift(LEFT * 2.6))
        side.next_to(paper, RIGHT, buff=0.4)
        self.play(FadeIn(side, shift=LEFT * 0.2))
        self.done()

        self.say("""Also look at the agreement you'll be asked to sign, the confidentiality
        and invention assignment agreement. It says that what you build at work belongs to
        the company, and sometimes it reaches further, into things you build on your own
        time. Since you have side projects, like your trading and agent experiments, list
        them on the "prior inventions" section so they stay yours. It's a normal request,
        and it's much easier to do before you sign than after.""")
        tip = card(["Tip:", "list your side projects", "under \"prior inventions\"", "before you sign"],
                   width=4.6, color=RED_, size=28)
        tip.next_to(paper, RIGHT, buff=0.35)
        self.play(FadeOut(side), FadeIn(tip, shift=LEFT * 0.2))
        self.done()
        self.clear_all()

        # ---- a sample offer ----
        self.say("""So let's make it concrete. Here's a made up but realistic offer from
        a Series B A.I. startup. One hundred ninety thousand dollars base. Forty thousand
        stock options, with a strike price of two dollars and fifty cents. Vesting over
        four years, with a one year cliff. Every one of those words matters, so let's go
        through them.""")
        hdr = title("A sample offer · Series B AI startup")
        lines = VGroup(
            VGroup(T("Base salary", size=44, color=DIM), T("$190,000", size=48, color=GREEN_, weight=BOLD)),
            VGroup(T("Stock options", size=44, color=DIM), T("40,000", size=48, color=YELLOW_, weight=BOLD)),
            VGroup(T("Strike price", size=44, color=DIM), T("$2.50 / share", size=48, color=YELLOW_, weight=BOLD)),
            VGroup(T("Vesting", size=44, color=DIM), T("4 years, 1-year cliff", size=48, color=BLUE_, weight=BOLD)),
        )
        for l in lines:
            l.arrange(RIGHT, buff=0.6)
        lines.arrange(DOWN, buff=0.5, aligned_edge=LEFT).shift(DOWN * 0.3)
        for l in lines:
            l[1].align_to(lines, RIGHT)
        self.play(Write(hdr), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(l, shift=UP * 0.2) for l in lines],
                              lag_ratio=0.5), run_time=4)
        self.done()
        self.offer = VGroup(hdr, lines)

        # ---- options ----
        self.say("""First, what's a stock option? It's not a share. It's the right to
        buy a share later at a fixed price, the strike price. Your strike is two fifty.
        If the company's shares later become worth ten dollars, each option lets you pay
        two fifty for something worth ten. Your profit is the gap, seven fifty a share.
        If the shares never get above two fifty, the options are worth nothing. Using that
        right, actually paying the two fifty per share to buy the stock, is called
        exercising, and the money comes from your own pocket. Chapter two walks through
        exactly how that works.""")
        self.clear_all()
        axis = NumberLine(x_range=[0, 12, 2], length=10, color=DIM).shift(DOWN * 1.2)
        axis.add(*[T(str(v), size=28, color=DIM).next_to(axis.n2p(v), DOWN, buff=0.2)
                   for v in range(0, 13, 2)])
        axis_lbl = T("share price ($)", size=28, color=DIM).next_to(axis, DOWN, buff=0.3)
        strike = axis.n2p(2.5)
        value = axis.n2p(10)
        s_line = DashedLine(strike + UP * 3, strike, color=YELLOW_)
        s_lbl = T("strike $2.50", size=32, color=YELLOW_).next_to(s_line, UP)
        v_line = DashedLine(value + UP * 3, value, color=GREEN_)
        v_lbl = T("worth $10", size=32, color=GREEN_).next_to(v_line, UP)
        gap = DoubleArrow(strike + UP * 1.5, value + UP * 1.5, color=GREEN_, buff=0)
        g_lbl = T("your gain: $7.50 / share", size=36, color=GREEN_, weight=BOLD).next_to(gap, UP)
        h = title("An option = the right to buy at a fixed price", size=48)
        self.play(Write(h), Create(axis), FadeIn(axis_lbl), run_time=1.5)
        self.play(Create(s_line), FadeIn(s_lbl))
        self.wait(max(0.1, self.left() * 0.35))
        self.play(Create(v_line), FadeIn(v_lbl))
        self.play(GrowFromCenter(gap), FadeIn(g_lbl))
        self.done()

        self.say("""Late stage companies often give R.S.U.s instead, restricted stock
        units. Those are just shares handed to you, no strike price to pay. Same idea,
        simpler math. At private companies, R.S.U.s are usually "double trigger": they
        need time served, and also a sale or I.P.O., before they really vest. That's
        actually nice, because it means you don't owe tax on them until there's cash to
        pay it with.""")
        self.clear_all()
        cmp = VGroup(
            card(["Options", "pay the strike to buy", "early-stage, common"], width=5.6, color=YELLOW_),
            card(["RSUs", "shares granted outright", "late-stage, common"], width=5.6, color=BLUE_),
        ).arrange(RIGHT, buff=0.6)
        self.play(FadeIn(cmp[0], shift=RIGHT * 0.3), FadeIn(cmp[1], shift=LEFT * 0.3), run_time=1.2)
        self.done()

        self.say("""If you get options, your paperwork will say whether they're I.S.O.s,
        incentive stock options, or N.S.O.s, non qualified stock options. Employees usually
        get I.S.O.s. The difference is all about taxes, and we'll get to it in chapter two.
        For now, just know the letters, so they don't confuse you on the grant notice.""")
        kinds = VGroup(
            T("ISO  = incentive stock option  (usual for employees)", size=32, color=YELLOW_),
            T("NSO = non-qualified stock option  (advisors, some employees)", size=32, color=DIM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(DOWN, buff=0.7)
        self.play(cmp.animate.shift(UP * 0.6), FadeIn(kinds, shift=UP * 0.2))
        self.done()
        self.clear_all()

        # ---- vesting ----
        self.say("""Vesting means you earn your equity over four years. With a one year
        cliff, you get nothing for the first twelve months. Leave at month eleven, you
        walk away with zero. At month twelve, a quarter of it, ten thousand options,
        lands all at once. After that, it trickles in monthly, about eight hundred thirty
        options a month, until year four.""")
        h = title("Vesting: 4 years, 1-year cliff", size=52)
        ax = Axes(x_range=[0, 48, 12], y_range=[0, 40000, 10000], x_length=10.5,
                  y_length=4.6, axis_config={"color": DIM, "include_ticks": True},
                  tips=False).shift(DOWN * 0.5)
        xl = VGroup(*[T(f"yr {i}", size=28, color=DIM).next_to(ax.c2p(12 * i, 0), DOWN)
                      for i in range(1, 5)])
        yl = VGroup(*[T(f"{v//1000}K", size=28, color=DIM).next_to(ax.c2p(0, v), LEFT)
                      for v in (10000, 20000, 30000, 40000)])
        def vested(m):
            return 0 if m < 12 else 10000 + (m - 12) * 30000 / 36
        pts = [ax.c2p(0, 0), ax.c2p(12, 0), ax.c2p(12, 10000), ax.c2p(48, 40000)]
        curve = VMobject(color=YELLOW_, stroke_width=7).set_points_as_corners(pts)
        self.play(Write(h), Create(ax), FadeIn(xl), FadeIn(yl), run_time=1.5)
        self.play(Create(curve), run_time=max(2, min(6, self.left() * 0.5)), rate_func=linear)
        cliff = T("the cliff", size=34, color=RED_).next_to(ax.c2p(12, 10000), LEFT, buff=0.4).shift(UP * 0.4)
        self.play(FadeIn(cliff), Flash(ax.c2p(12, 10000), color=RED_))
        self.done()

        self.say("""One more thing on this slide. Most companies give refreshers, extra
        grants each year if you're doing well, so a strong performer's equity keeps
        stacking. Ask about the refresher policy. It's a big deal by year three.""")
        self.done()
        self.clear_all()

        # ---- what fraction of the company ----
        self.say("""Now the most important question, and the one people forget to ask.
        Forty thousand options sounds like a lot. But forty thousand out of what? You
        need the total number of shares, called the fully diluted share count. Say it's
        one hundred million. Then you own forty thousand divided by one hundred million,
        which is zero point zero four percent of the company.""")
        h = title("Forty thousand out of what?", size=56)
        big = Square(side_length=5, color=DIM, stroke_width=3).shift(DOWN * 0.4 + LEFT * 2.5)
        grid = VGroup(*[Square(side_length=0.5, stroke_width=1, stroke_color=DIM,
                                fill_opacity=0) for _ in range(100)]).arrange_in_grid(10, 10, buff=0)
        grid.move_to(big)
        pct = VGroup(T("40,000 ÷ 100,000,000", size=40),
                     T("= 0.04%", size=72, color=YELLOW_, weight=BOLD),
                     T("of the company", size=36, color=DIM)).arrange(DOWN, buff=0.35)
        pct.next_to(big, RIGHT, buff=0.9)
        self.play(Write(h), Create(big), FadeIn(grid), run_time=1.5)
        self.wait(max(0.1, self.left() * 0.4))
        self.play(Write(pct[0]))
        self.play(FadeIn(pct[1], scale=1.2), FadeIn(pct[2]))
        tiny = Square(side_length=0.5 * np.sqrt(0.04), color=YELLOW_, fill_opacity=1,
                      stroke_width=0).move_to(grid[0].get_corner(UL), aligned_edge=UL)
        self.play(grid[0].animate.set_fill(BLUE_, 0.5))
        zoomlbl = T("1% of the company is one small square.\nYour slice is 1/25 of that.", size=28,
                    color=DIM).next_to(big, DOWN, buff=0.3)
        self.play(FadeIn(zoomlbl), FadeIn(tiny))
        self.done()

        self.say("""So, what's that worth? Startups price themselves when they raise
        money. If the last round valued the company at one billion dollars, with one
        hundred million shares, investors paid about ten dollars a share. On paper, your
        forty thousand options are worth ten minus your two fifty strike, times forty
        thousand. That's three hundred thousand dollars, over four years. About seventy
        five thousand a year, on paper.""")
        self.clear_all()
        h = title("Paper value", size=56)
        eq = VGroup(
            T("($10 − $2.50) × 40,000", size=52),
            T("= $300,000", size=88, color=YELLOW_, weight=BOLD),
            T("over 4 years  ≈  $75K / year on paper", size=40, color=DIM),
        ).arrange(DOWN, buff=0.5)
        self.play(Write(h))
        self.play(Write(eq[0]), run_time=1.5)
        self.play(FadeIn(eq[1], scale=1.2))
        self.play(FadeIn(eq[2]))
        self.done()

        self.say("""And here's where "on paper" really matters. Why is your strike
        price two fifty when investors paid ten? Because investors buy preferred stock,
        which comes with protections, and you get common stock. An outside appraisal,
        called a four oh nine A valuation, prices common stock lower, often a quarter to a
        third of the preferred price. Lower strike is good for you. But it's also a hint:
        your shares are not the same as the investors' shares.""")
        self.clear_all()
        two = VGroup(
            card(["Preferred", "investors buy these", "~$10 / share", "come with protections"], width=5.6, color=BLUE_),
            card(["Common", "you get these", "409A ≈ $2.50", "paid after investors"], width=5.6, color=YELLOW_),
        ).arrange(RIGHT, buff=0.6)
        self.play(FadeIn(two[0], shift=RIGHT * 0.3), run_time=1)
        self.wait(max(0.1, self.left() * 0.4))
        self.play(FadeIn(two[1], shift=LEFT * 0.3), run_time=1)
        self.done()
        self.clear_all()

        # ---- annualize ----
        self.say("""So how should you put this offer next to what you make now? Here's
        the simple way. Take the base salary. Then take the paper value of the equity,
        divide by four for the four years, and decide how much you believe it. A
        conservative habit is to count it as zero when you decide whether you can afford
        the job, and then count it at its paper value only when you're dreaming about
        upside. So this offer is one ninety, guaranteed, plus a ticket that says
        seventy five a year on paper. Chapter two is about how that ticket turns into
        money, and why paper value is usually optimistic.""")
        h = title("Comparing to your current job", size=52)
        rows = VGroup(
            VGroup(T("Guaranteed", size=40, color=DIM), T("$190K / yr", size=52, color=GREEN_, weight=BOLD)).arrange(RIGHT, buff=0.6),
            VGroup(T("Equity, on paper", size=40, color=DIM), T("+ $75K / yr", size=52, color=YELLOW_, weight=BOLD)).arrange(RIGHT, buff=0.6),
            VGroup(T("To decide if you can afford it", size=40, color=DIM), T("count equity = $0", size=52, color=RED_, weight=BOLD)).arrange(RIGHT, buff=0.6),
        ).arrange(DOWN, buff=0.6, aligned_edge=RIGHT).shift(DOWN * 0.3)
        fit(rows)
        self.play(Write(h))
        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.2), run_time=0.7)
            self.wait(min(8, max(0.1, self.left() / 4)))
        self.done()
        self.clear_all()
