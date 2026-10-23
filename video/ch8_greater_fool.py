from common import *


class Ch8GreaterFool(NarratedScene):
    chapter_label = "8 · Is it a greater fool game?"

    def construct(self):
        self.play(FadeIn(chapter_card(8, "Is it a greater fool game?",
                                      "Taleb's critique, taken seriously")))
        self.say("""Chapter eight. Is it all a greater fool game? Nassim Taleb has argued
        that a lot of modern startups aren't built to produce profits, they're built to be
        sold. Let's take that seriously, and then weigh it against the evidence.""")
        self.done()
        self.clear_all()

        # ---- the idea ----
        self.say("""First, the term. The greater fool theory says you can make money buying
        something overpriced, as long as a greater fool will buy it from you at an even
        higher price later. It doesn't matter what the thing is actually worth, only that
        someone else will pay more. The game ends when you run out of fools, and whoever
        is holding it last loses.""")
        h = title("The greater fool chain", size=56)
        names = ["Founders", "Seed VC", "Growth fund", "Crossover fund", "Public market"]
        cols = [YELLOW_, ORANGE_, BLUE_, PURPLE_, RED_]
        boxes = VGroup(*[card([n], width=2.3, color=c, size=26, height=1.1) for n, c in zip(names, cols)])
        boxes.arrange(RIGHT, buff=0.35).shift(DOWN * 0.2)
        fit(boxes, 13)
        arrows = VGroup(*[Arrow(boxes[i].get_right(), boxes[i + 1].get_left(), buff=0.05,
                                color=DIM, stroke_width=4, max_tip_length_to_length_ratio=0.3)
                          for i in range(len(boxes) - 1)])
        price = T("each pays a higher price than the last", size=30, color=DIM).next_to(boxes, UP, buff=0.6)
        self.play(Write(h))
        self.play(FadeIn(boxes[0]))
        for i in range(1, len(boxes)):
            self.play(GrowArrow(arrows[i - 1]), FadeIn(boxes[i]), run_time=0.6)
        self.play(FadeIn(price))
        self.done()

        self.say("""Taleb's version of the critique, roughly: a company that's designed
        from the start to be flipped is like a hotel built to be sold rather than to have
        guests. Founders raise money at a high price. Venture capitalists mark up their
        portfolios and raise their next fund on those markups, earning fees either way.
        Each round sells to a bigger buyer, and the final buyer is the public, often
        through index funds, who end up holding a company that never really learned to
        make money. In his language, the people passing it along don't have enough skin in
        the game, because they get paid even if the last holder loses.""")
        last = T("left holding it", size=30, color=RED_, weight=BOLD).next_to(boxes[-1], DOWN, buff=0.4)
        fees = T("fees + markups paid along the way", size=30, color=ORANGE_).next_to(boxes[1:4], DOWN, buff=0.4)
        self.wait(min(10, max(0.1, self.left() * 0.35)))
        self.play(FadeIn(fees))
        self.wait(min(10, max(0.1, self.left() * 0.6)))
        self.play(FadeIn(last), boxes[-1].animate.set_color(RED_))
        self.done()
        self.clear_all()

        # ---- the case for ----
        self.say("""And there's real evidence for this. Let's start with the case that
        Taleb is right.""")
        h = title("The case that Taleb is right", size=52, color=RED_)
        self.play(Write(h))
        self.done()

        self.say("""One. History. WeWork was valued at forty seven billion dollars
        privately, then collapsed when it tried to go public, and went bankrupt. The
        twenty twenty one wave produced hundreds of unicorns, and many of them have since
        raised money at lower valuations, or quietly sold for a fraction of their peak.""")
        b = VGroup()
        items = [
            "WeWork: $47B private → bankruptcy",
            "2021 unicorns: many down rounds, quiet fire sales",
            "Circular AI deals: investors' money returns as revenue",
            "Huge spending on chips vs. much smaller revenue",
            "Private longer, public later: the public buys last",
        ]
        for it in items:
            b.add(VGroup(Dot(radius=0.08, color=RED_), T(it, size=34)).arrange(RIGHT, buff=0.3))
        b.arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(h, DOWN, buff=0.6)
        fit(b)
        self.play(FadeIn(b[0], shift=RIGHT * 0.2))
        self.wait(min(8, max(0.1, self.left() / 2)))
        self.play(FadeIn(b[1], shift=RIGHT * 0.2))
        self.done()

        self.say("""Two. Circular deals in A.I. today. A chip maker or cloud provider
        invests billions in an A.I. lab, and the lab spends that money buying chips or cloud
        time from the same investor. The investor books it as revenue, and the lab's
        valuation goes up. Money is moving in a circle, and it makes everyone's numbers
        look better than the underlying demand might justify. Three. The scale of
        spending. Tech companies are spending hundreds of billions a year on data centers,
        far more than A.I. products currently earn.""")
        self.play(FadeIn(b[2], shift=RIGHT * 0.2))
        self.wait(min(12, max(0.1, self.left() / 2)))
        self.play(FadeIn(b[3], shift=RIGHT * 0.2))
        self.done()

        self.say("""And four, the newest twist, which is what that Casual Finance video,
        "The Stock Market Is Being Used as a Dumping Ground," is about. Its argument is that
        companies now stay private longer and go public later, so the public gets the
        leftovers. When Amazon went public in nineteen ninety seven, it was worth around
        four hundred thirty million dollars, and a thousand dollars invested at the I.P.O.
        would be worth over three million today. SpaceX went public in June at a valuation
        of just under one point eight trillion, more than four thousand times bigger at the
        starting line. For an Amazon style return, it would have to become a company worth
        several quadrillion dollars, which is more than all the wealth on Earth.""")
        self.play(FadeIn(b[4], shift=RIGHT * 0.2))
        self.done()
        self.clear_all()

        h = title("Private longer, public later", size=54)
        ax_y = DOWN * 2.3
        amzn = Rectangle(width=2.6, height=0.05, fill_color=GREEN_, fill_opacity=1, stroke_width=0).move_to(ax_y + LEFT * 3, aligned_edge=DOWN)
        spx = Rectangle(width=2.6, height=4.3, fill_color=RED_, fill_opacity=0.9, stroke_width=0).move_to(ax_y + RIGHT * 3, aligned_edge=DOWN)
        al = VGroup(T("Amazon IPO, 1997", size=30), T("~$0.43B", size=36, color=GREEN_, weight=BOLD)).arrange(DOWN, buff=0.1).next_to(amzn, UP, buff=0.3)
        sl = VGroup(T("SpaceX IPO, 2026", size=30), T("~$1,800B", size=36, color=RED_, weight=BOLD)).arrange(DOWN, buff=0.1).next_to(spx, LEFT, buff=0.3)
        base = Line(ax_y + LEFT * 6, ax_y + RIGHT * 6, color=DIM)
        cap = T("value on day one of public trading", size=26, color=DIM).next_to(base, DOWN, buff=0.25)
        self.play(Write(h), Create(base), FadeIn(cap))
        self.say("""The video lays out why this changed, and it's three rule changes
        stacking up. A nineteen ninety six law let pension funds and endowments pour money
        into private funds, so startups no longer needed the stock market for cash. The
        twenty twelve JOBS Act raised the shareholder count that forces a company to publish
        its financials from five hundred to two thousand, and stopped counting employees who
        got stock as pay. That's the rule that pushed Microsoft, Google, and Facebook to go
        public while they still had most of their growth ahead. And tender offers let
        employees cash out without an I.P.O. Stripe, for example, has stayed private for
        sixteen years, running tender offers that valued it at about sixty five billion in
        twenty twenty four and around one hundred fifty nine billion recently.""")
        self.play(GrowFromEdge(amzn, DOWN), FadeIn(al))
        self.wait(min(8, max(0.1, self.left() / 3)))
        self.play(GrowFromEdge(spx, DOWN), FadeIn(sl), run_time=1.5)
        self.done()
        self.clear_all()

        self.say("""So the asymmetric bet, risk a little for a shot at a lot, used to be
        offered to the public at the I.P.O. Now most of it happens in private. Anthropic was
        valued at sixty one and a half billion dollars in March twenty twenty five, and
        nine hundred sixty five billion in May twenty twenty six, fifteen times more, all of
        it in private markets. Add the twenty twenty six Nasdaq rule that lets giant new
        listings into the Nasdaq one hundred within about fifteen trading days, so index
        funds have to buy them, and you can see the dumping ground worry. The people
        holding these shares at the I.P.O. price might be the last buyers in the chain.""")
        h = title("Where the asymmetric bet went", size=50)
        rows = VGroup(
            VGroup(T("Then", size=40, color=GREEN_, weight=BOLD), T("public buys early: small risk, huge upside", size=34)).arrange(RIGHT, buff=0.5),
            VGroup(T("Now", size=40, color=RED_, weight=BOLD), T("growth happens privately; public buys late", size=34)).arrange(RIGHT, buff=0.5),
            VGroup(T("Anthropic", size=40, color=BLUE_, weight=BOLD), T("$61.5B (Mar 2025) → $965B (May 2026), all private", size=32)).arrange(RIGHT, buff=0.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).shift(DOWN * 0.3)
        fit(rows)
        self.play(Write(h))
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(min(10, max(0.1, self.left() / 4)))
        self.done()

        self.say("""And here's the twist that matters most for you. If the growth now
        happens before the I.P.O., who gets to own it? Mostly venture funds and wealthy,
        accredited investors. And one other group: employees. A startup job is one of
        the very few ways a regular person can own pre I.P.O. equity in a fast growing
        company. That doesn't make the equity safe. But it does mean the dumping ground
        argument cuts both ways. If you're on the inside before the growth, you're on the
        side of the fence where, as the venture firm Andreessen Horowitz itself put it,
        the high growth now happens.""")
        insider = card(["The twist for you", "growth now happens before the IPO",
                        "who can own it? VCs, the wealthy... and employees"], width=10, color=YELLOW_, size=32)
        insider.to_edge(DOWN, buff=0.3)
        self.play(rows.animate.scale(0.7).shift(UP * 0.6), FadeIn(insider, shift=UP * 0.2))
        self.done()
        self.clear_all()

        # ---- the case against ----
        self.say("""Now the other side. A greater fool asset is one with no real cash
        flows, where the only reason to own it is to sell it. Tulips. Many crypto tokens.
        The question for A.I. is whether there are real customers paying real money, and
        the answer, at least at the top, is clearly yes.""")
        h = title("The case that it's real", size=52, color=GREEN_)
        self.play(Write(h))
        self.done()

        self.say("""Anthropic's annualized revenue was reported at around nine billion
        dollars at the end of twenty twenty five, and around forty seven billion by May
        twenty twenty six, according to the company. That's paid usage from businesses,
        not users on a free app. Cursor reportedly passed a billion dollars in annual
        revenue in under three years. Coding agents, customer support agents, and medical
        note taking are being bought because they save companies money, and companies
        renew.""")
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 50, 10], x_length=6.5, y_length=4.2,
                  axis_config={"color": DIM, "include_ticks": False}, tips=False).shift(DOWN * 0.6 + LEFT * 2.6)
        bars = VGroup()
        for i, (v, lbl) in enumerate([(9, "end 2025"), (30, "Apr 2026"), (47, "May 2026")]):
            r = Rectangle(width=1.3, height=ax.c2p(0, v)[1] - ax.c2p(0, 0)[1], fill_color=GREEN_,
                          fill_opacity=0.85, stroke_width=0)
            r.move_to(ax.c2p(i + 0.6, 0), aligned_edge=DOWN)
            l = T(lbl, size=24, color=DIM).next_to(r, DOWN, buff=0.15)
            vl = T(f"${v}B", size=28, color=GREEN_, weight=BOLD).next_to(r, UP, buff=0.12)
            bars.add(VGroup(r, l, vl))
        cap = T("Anthropic revenue run-rate (reported)", size=26, color=DIM).next_to(ax, UP, buff=0.3)
        side = VGroup(
            T("Cursor: >$1B ARR", size=34, color=GREEN_),
            T("in under 3 years (reported)", size=26, color=DIM),
            T("Customers renew", size=34, color=GREEN_),
            T("because it saves them money", size=26, color=DIM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(ax, RIGHT, buff=0.9)
        self.play(Create(ax), FadeIn(cap))
        for br in bars:
            self.play(GrowFromEdge(br[0], DOWN), FadeIn(br[1]), FadeIn(br[2]), run_time=0.7)
        self.wait(min(8, max(0.1, self.left() / 3)))
        self.play(FadeIn(side, shift=LEFT * 0.2))
        self.done()
        self.clear_all()

        # ---- bubble vs fraud: railroads ----
        self.say("""So here's the distinction that helps me. A bubble is not the same as a
        greater fool game. In the eighteen forties, Britain had a railway mania. Investors
        poured money into railways, most of those companies went bust, and lots of people
        lost money. But the railways got built and transformed the economy. The same thing
        happened with the dot com crash. Pets dot com died, but Amazon survived the crash
        and became one of the most valuable companies on Earth. Real technology plus too
        much money at once produces a bubble. Some investors are fools and some are early.
        Usually, you can only tell which, afterward.""")
        h = title("Bubble ≠ nothing real", size=56)
        hist = VGroup(
            card(["1840s railway mania", "most companies failed", "the railways stayed"], width=5.8, color=BLUE_, size=30),
            card(["2000 dot-com crash", "Pets.com died", "Amazon survived"], width=5.8, color=BLUE_, size=30),
        ).arrange(RIGHT, buff=0.5).shift(DOWN * 0.2)
        concl = T("real technology + too much money at once = bubble", size=34, color=YELLOW_).to_edge(DOWN, buff=0.6)
        self.play(Write(h))
        self.play(FadeIn(hist[0], shift=UP * 0.3))
        self.wait(min(12, max(0.1, self.left() / 3)))
        self.play(FadeIn(hist[1], shift=UP * 0.3))
        self.wait(min(10, max(0.1, self.left() / 2)))
        self.play(FadeIn(concl))
        self.done()
        self.clear_all()

        # ---- balanced verdict ----
        self.say("""My balanced take. Both things are true at once. At the top of the
        market, the frontier labs and the best applications, there's real, fast growing
        revenue, and the open question is only whether the price is too high, which is a
        normal investing question. Further down, there are lots of companies that really
        are built to be flipped: thin wrappers on someone else's model, with revenue
        from experiments that won't renew, kept alive by the next round. Taleb's critique
        fits that part of the market very well.""")
        h = title("Both are true", size=60)
        spec = Rectangle(width=12, height=0.7, stroke_width=0)
        spec.set_fill(color=[GREEN_, YELLOW_, RED_], opacity=0.9)
        spec.shift(DOWN * 0.2)
        l1 = T("real revenue, renewing customers", size=28, color=GREEN_).next_to(spec, DOWN, buff=0.3).align_to(spec, LEFT)
        l2 = T("built to be flipped", size=28, color=RED_).next_to(spec, DOWN, buff=0.3).align_to(spec, RIGHT)
        u = T("The AI market today", size=34, color=DIM).next_to(spec, UP, buff=0.4)
        self.play(Write(h))
        self.play(GrowFromEdge(spec, LEFT), FadeIn(u), run_time=1.2)
        self.play(FadeIn(l1))
        self.wait(min(12, max(0.1, self.left() / 2)))
        self.play(FadeIn(l2))
        self.done()
        self.clear_all()

        # ---- the questions ----
        self.say("""So as a job seeker, you want to tell which end of that spectrum a
        company is on. Four questions do most of the work. Who pays, and would they keep
        paying if the startup's free credits or discounts ran out? Do customers renew and
        expand, or churn after the pilot? What are the margins after paying for the models?
        Some A.I. products lose money on every customer, because each request costs more in
        inference than the customer pays. And: if OpenAI or Anthropic launched this as a
        feature tomorrow, what would be left? A company with good answers is building
        something. A company that dodges them might be building something to sell.""")
        h = title("Is this company building, or flipping?", size=48)
        b = bullets([
            "Who pays? Would they pay full price?",
            "Do customers renew and expand?",
            "Margins after model costs?",
            "If a lab shipped this as a feature, what's left?",
        ], size=38).next_to(h, DOWN, buff=0.7)
        self.play(Write(h))
        for r in b:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(min(10, max(0.1, self.left() / 5)))
        self.done()
        self.clear_all()

        # ---- barbell ----
        self.say("""And here's the most useful idea from Taleb, applied to you: the barbell.
        Put most of your weight on something very safe, and a small amount on something
        with huge upside, and avoid the fragile middle. For a startup job, the safe side is
        a salary you're happy to live on and skills that stay valuable whatever happens to
        the company. The upside side is the equity: a small option that costs you little
        and could pay off big. Notice what that means. Even if the whole sector turns out to
        be a bubble, you keep the salary and the skills. You only lose if you bet your
        savings on exercising, or count the paper equity as money you have. That way,
        you're never anybody's greater fool.""")
        h = title("Taleb's barbell, applied to you", size=50)
        bar = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=10, color=DIM).shift(DOWN * 0.3)
        left_w = card(["Safe", "salary you're happy with", "skills that transfer"], width=4.6, color=GREEN_, size=28)
        right_w = card(["Upside", "the equity", "small cost, big payoff"], width=4.6, color=YELLOW_, size=28)
        left_w.move_to(bar.get_left()).shift(LEFT * 0.4)
        right_w.move_to(bar.get_right()).shift(RIGHT * 0.4)
        mid = T("avoid: betting savings\non illiquid paper", size=26, color=RED_).next_to(bar, DOWN, buff=0.4)
        g = VGroup(bar, left_w, right_w, mid)
        fit(g, 13.2)
        self.play(Write(h))
        self.play(Create(bar))
        self.play(FadeIn(left_w, shift=RIGHT * 0.2))
        self.wait(min(12, max(0.1, self.left() / 3)))
        self.play(FadeIn(right_w, shift=LEFT * 0.2))
        self.wait(min(10, max(0.1, self.left() / 2)))
        self.play(FadeIn(mid))
        self.done()
        self.clear_all()

        # ---- wrap ----
        self.say("""Let's wrap up the whole video. A startup offer is a salary plus a
        lottery ticket, and you now know how to read the ticket: shares, strike,
        percentage, preferences, and the ways it can turn into cash. Each funding stage means a different
        team size and a very different job. The A.I. landscape is a
        stack, with a few giant labs at the bottom and thousands of applications on top, and
        a strong defense tech corner where your background is an asset. Choose by who,
        what, and how, multiplied together. Get in through proof of work and short, direct
        messages, not cold applications. And keep Taleb's barbell in mind, so that whether
        this is a boom or a bubble, you come out ahead. Good luck, Albert. Enjoy the
        drive.""")
        recap = VGroup(
            T("1-2  Salary + a lottery ticket: read the ticket", size=34),
            T("3     Each stage: different money, team, and work", size=34),
            T("4-5  A few giant labs, thousands of apps", size=34),
            T("6     Who × What × How", size=34),
            T("7     Proof of work + direct messages", size=34),
            T("8     Barbell: never be the greater fool", size=34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        h = title("Recap", size=60)
        self.play(Write(h))
        for r in recap:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(min(8, max(0.1, self.left() / 6)))
        self.done()
        self.clear_all()
