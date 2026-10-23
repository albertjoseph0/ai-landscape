from common import *


class Ch2Cash(NarratedScene):
    chapter_label = "2 · Turning equity into cash"

    def construct(self):
        self.play(FadeIn(chapter_card(2, "Turning equity into cash",
                                      "Exercising, taxes, exits, and secondary markets")))
        self.say("""Chapter two. Turning equity into cash. This is the practical part: what
        you actually do, click by click and dollar by dollar, to get money out of startup
        stock.""")
        self.done()
        self.clear_all()
        # ---- how it becomes money ----
        self.say("""So how does any of this become actual money you can spend? There are
        exactly three ways. One. The company gets acquired, and the buyer pays cash or
        their own stock for your shares. Two. The company goes public in an I.P.O., and
        after a lockup, usually about six months, you can sell on the stock market. Three.
        A tender offer, where the company arranges for investors to buy some employee
        shares while it's still private. Without one of these three, your equity is a
        number on a website. You can't pay rent with it.""")
        h = title("Three ways equity becomes cash", size=52)
        ways = VGroup(
            card(["Acquisition", "someone buys", "the company"], width=3.9, color=GREEN_),
            card(["IPO", "go public, wait", "~6 mo lockup"], width=3.9, color=BLUE_),
            card(["Tender offer", "investors buy", "employee shares"], width=3.9, color=PURPLE_),
        ).arrange(RIGHT, buff=0.35).shift(DOWN * 0.3)
        self.play(Write(h))
        for w_ in ways:
            self.play(FadeIn(w_, shift=UP * 0.3), run_time=0.8)
            self.wait(min(3.5, max(0.2, self.left() / 5)))
        self.done()

        self.clear_all()

        # ---- acquisition detail ----
        self.say("""Let's take them one at a time, starting with an acquisition, since
        that's the most common good outcome. Say a big company buys your startup. Your
        vested options usually get cashed out: the buyer pays you the gap between the deal
        price per share and your strike, times your vested options, and you never have to
        put up money to exercise. Or, if it's a stock deal, your options get converted into
        the buyer's stock or options. Cursor's sale to SpaceX, for example, was paid in
        SpaceX stock, not cash.""")
        h = title("If the company is acquired", size=52)
        flow = VGroup(
            card(["Vested options", "cashed out: (deal price − strike) × shares", "or converted to buyer's stock"], width=10, color=GREEN_, size=32),
            card(["Unvested options", "usually converted, keep vesting", "sometimes cancelled. Read the plan."], width=10, color=ORANGE_, size=32),
        ).arrange(DOWN, buff=0.4).shift(DOWN * 0.4)
        self.play(Write(h))
        self.play(FadeIn(flow[0], shift=UP * 0.3))
        self.done()

        self.say("""Your unvested options are the trickier part. Usually the buyer takes
        them over and you keep vesting on their payroll, which is the buyer's way of
        making you stay. Some plans include acceleration, meaning some or all of your
        unvested equity vests instantly if the company is sold and you're let go. That's
        called double trigger acceleration. It's worth asking about, though employees
        below the executive level rarely get it.""")
        self.play(FadeIn(flow[1], shift=UP * 0.3))
        self.done()
        self.clear_all()

        # ---- IPO detail ----
        self.say("""Now an I.P.O. The day the company lists, your shares suddenly have a
        public price, but you usually can't sell yet. There's a lockup, typically about
        six months, so insiders don't flood the market. When the lockup ends, you can do
        what's called a cashless exercise, or "exercise and sell": you exercise and sell in
        the same transaction, and the broker takes the strike price and the tax out of the
        sale proceeds. You never had to write a check. And here's the uncomfortable part:
        the stock can drop a lot between the I.P.O. and the end of the lockup.""")
        h = title("If the company IPOs", size=52)
        ax = NumberLine(x_range=[0, 8, 1], length=11, color=DIM).shift(DOWN * 1.4)
        pts = {"IPO day": 0.5, "lockup ends (~6 mo)": 6.5}
        m1 = VGroup(Dot(ax.n2p(0.5), color=BLUE_, radius=0.12), T("IPO day: public price", size=28, color=BLUE_))
        m1[1].next_to(m1[0], UP, buff=0.3)
        lock = Rectangle(width=ax.n2p(6.5)[0] - ax.n2p(0.5)[0], height=0.5, stroke_width=0,
                         fill_color=RED_, fill_opacity=0.35)
        lock.move_to((ax.n2p(0.5) + ax.n2p(6.5)) / 2)
        lock_lbl = T("lockup: can't sell", size=28, color=RED_).next_to(lock, DOWN, buff=0.2)
        m2 = VGroup(Dot(ax.n2p(6.5), color=GREEN_, radius=0.12), T("exercise + sell same day", size=28, color=GREEN_))
        m2[1].next_to(m2[0], UP, buff=0.3)
        self.play(Write(h), Create(ax))
        self.play(FadeIn(m1))
        self.wait(min(5, max(0.1, self.left() / 4)))
        self.play(FadeIn(lock), FadeIn(lock_lbl))
        self.wait(min(6, max(0.1, self.left() / 3)))
        self.play(FadeIn(m2))
        self.done()
        self.clear_all()

        # ---- tender offers ----
        self.say("""The third way is a tender offer. The company itself arranges for
        investors to buy a limited amount of employee stock, at a set price, while the
        company is still private. Usually you need to have been there a certain amount of
        time, and you can only sell a portion, maybe a quarter of your vested shares.""")
        h = title("Tender offers", size=56)
        self.play(Write(h))
        self.done()

        self.say("""Real example. In April of twenty twenty six, Anthropic ran a tender
        offer for employees at a three hundred fifty billion dollar valuation. Investors
        lined up to buy around five to six billion dollars of employee stock. The
        interesting part: most employees chose not to sell, because they expected the
        stock to be worth more after an I.P.O. That's what equity at a winning company
        looks like, and they were right to hold: about seven weeks later, a new funding
        round valued Anthropic at nearly a trillion. At most startups, though, there's no
        tender offer at all.""")
        ex = card(["Anthropic tender offer · Apr 2026",
                   "valued at ~$350B", "investors ready to buy ~$5–6B",
                   "most employees kept their shares"], width=8, color=PURPLE_, size=36)
        ex.shift(DOWN * 0.3)
        self.play(FadeIn(ex, shift=UP * 0.3))
        self.done()
        self.clear_all()

        # ---- secondary markets ----
        self.say("""Now, the thing you asked about: Hiive. Hiive, Forge, and EquityZen are
        secondary marketplaces. Think of them as a stock exchange for private company
        shares. A current or former employee lists shares for sale, and accredited
        investors, meaning wealthy individuals or funds, bid on them. When the price is
        agreed, the trade goes to the company for approval.""")
        h = title("Secondary markets: Hiive, Forge, EquityZen", size=46)
        seller = card(["You", "own exercised", "common shares"], width=3.4, color=YELLOW_, size=28)
        market = card(["Hiive / Forge", "listing, bids,", "price agreed"], width=3.4, color=BLUE_, size=28)
        company = card(["The company", "approves, or uses", "right of first refusal"], width=3.4, color=RED_, size=28)
        buyer = card(["Buyer", "accredited investor", "or fund"], width=3.4, color=GREEN_, size=28)
        top = VGroup(seller, market, buyer).arrange(RIGHT, buff=0.9).shift(UP * 0.3)
        company.next_to(market, DOWN, buff=0.6)
        a1 = Arrow(seller.get_right(), market.get_left(), color=DIM, buff=0.1)
        a2 = Arrow(buyer.get_left(), market.get_right(), color=DIM, buff=0.1)
        a3 = Arrow(market.get_bottom(), company.get_top(), color=DIM, buff=0.1)
        g = VGroup(top, company, a1, a2, a3)
        fit(g, 13, 5.8)
        g.shift(DOWN * 0.3)
        self.play(Write(h))
        self.play(FadeIn(seller), GrowArrow(a1), FadeIn(market))
        self.wait(min(6, max(0.1, self.left() / 3)))
        self.play(FadeIn(buyer), GrowArrow(a2))
        self.wait(min(4, max(0.1, self.left() / 3)))
        self.play(GrowArrow(a3), FadeIn(company))
        self.done()

        self.say("""Four catches make this harder than it sounds. One: you can only sell
        shares, not options, so you have to exercise first, and pay for it. Two: almost
        every startup has a right of first refusal, meaning the company can step in and
        buy your shares at the agreed price instead, and the approval can take a month or
        more. Three: many companies simply ban or tightly limit these sales, especially
        hot ones like OpenAI, Anthropic, or SpaceX before its I.P.O. They'd rather run their
        own tender offers. And four: prices. Shares in the hottest companies can trade above
        the last round price. For an ordinary startup, buyers often demand a big discount,
        and for many companies there are no buyers at all. Fees run a few percent.""")
        self.clear_all()
        h = title("The catches", size=56)
        b = bullets([
            "Shares only, not options: exercise first",
            "Company approval + right of first refusal (weeks)",
            ("Many companies ban or limit it", RED_),
            "Hot names can trade at a premium; most at a discount",
            "Fees: a few percent",
        ], size=36).next_to(h, DOWN, buff=0.6)
        self.play(Write(h))
        for r in b:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(min(8, max(0.1, self.left() / 6)))
        self.done()

        self.say("""Here's a practical use of these sites even if you never sell. They
        publish indications of what private shares are trading for. Before you accept an
        offer, look the company up on Hiive or Forge, or on a data site like Caplight. If
        the company's shares trade well below its last round price, the market is telling
        you something that the recruiter won't.""")
        tip = card(["Use them as a price check", "secondary price ≪ last round price?", "the market is telling you something"],
                   width=9, color=BLUE_, size=32).to_edge(DOWN, buff=0.4)
        self.play(b.animate.scale(0.75).shift(UP * 0.5), FadeIn(tip, shift=UP * 0.2))
        self.done()
        self.clear_all()

        # ---- exercising ----
        self.say("""Which brings us to exercising, step by step. Exercising means paying
        the strike price to turn options into real shares. Practically, you log into Carta,
        pick how many vested options to exercise, and wire the money. Ten thousand options
        at a two fifty strike costs twenty five thousand dollars. Now you own ten thousand
        shares of common stock, which you still can't sell on the open market.""")
        h = title("Exercising, step by step", size=52)
        steps = VGroup(
            card(["1. Log in to Carta", "choose vested options"], width=3.9, color=BLUE_, size=28),
            card(["2. Pay the strike", "10,000 × $2.50", "= $25,000"], width=3.9, color=YELLOW_, size=28),
            card(["3. Own shares", "still private,", "still illiquid"], width=3.9, color=GREEN_, size=28),
        ).arrange(RIGHT, buff=0.35).shift(DOWN * 0.3)
        self.play(Write(h))
        for st in steps:
            self.play(FadeIn(st, shift=UP * 0.3), run_time=0.7)
            self.wait(min(5, max(0.1, self.left() / 4)))
        self.done()
        self.clear_all()

        self.say("""Then taxes, which is where people get hurt. The I.R.S. cares about the
        spread: the difference between your strike and the current fair market value when
        you exercise. Say the four oh nine A value has risen to six dollars. On ten thousand
        options, the spread is three fifty a share, thirty five thousand dollars. With
        N.S.O.s, that thirty five thousand counts as ordinary income, like salary, the year
        you exercise. With I.S.O.s, there's no regular income tax at exercise, but that
        spread counts toward something called the alternative minimum tax, the A.M.T.,
        which can produce a surprise bill. In both cases, you may owe real tax on stock you
        can't sell.""")
        h = title("The tax on the spread", size=52)
        nl = NumberLine(x_range=[0, 7, 1], length=10, color=DIM).shift(DOWN * 0.2)
        nl.add(*[T(f"${v}", size=26, color=DIM).next_to(nl.n2p(v), DOWN, buff=0.2) for v in range(0, 8)])
        s_ = Dot(nl.n2p(2.5), color=YELLOW_, radius=0.12)
        s_l = T("strike $2.50", size=28, color=YELLOW_).next_to(s_, UP, buff=0.5)
        f_ = Dot(nl.n2p(6), color=GREEN_, radius=0.12)
        f_l = T("409A today $6", size=28, color=GREEN_).next_to(f_, UP, buff=0.5)
        br = BraceBetweenPoints(nl.n2p(2.5), nl.n2p(6), direction=UP).shift(UP * 0.2)
        spread = T("spread $3.50 × 10,000 = $35,000", size=34, weight=BOLD).next_to(br, UP, buff=1.0)
        cmp = VGroup(
            card(["NSO", "$35K taxed as income", "the year you exercise"], width=5.6, color=ORANGE_, size=28),
            card(["ISO", "no regular tax now", "but counts toward AMT"], width=5.6, color=YELLOW_, size=28),
        ).arrange(RIGHT, buff=0.5).to_edge(DOWN, buff=0.35)
        self.play(Write(h), Create(nl))
        self.play(FadeIn(s_), FadeIn(s_l))
        self.play(FadeIn(f_), FadeIn(f_l))
        self.wait(min(8, max(0.1, self.left() / 5)))
        self.play(GrowFromCenter(br), FadeIn(spread))
        self.wait(min(10, max(0.1, self.left() / 3)))
        self.play(VGroup(nl, s_, s_l, f_, f_l, br, spread).animate.shift(UP * 0.9), FadeIn(cmp))
        self.done()
        self.clear_all()

        self.say("""So when should you exercise? There are three common strategies. Option
        one, wait. If you stay until an acquisition or I.P.O., you can usually exercise and
        sell at the same moment, never risking your own cash. This is what most people do.
        Option two, exercise early. Some companies let you exercise before you've even
        vested, when the spread is zero. You then file something called an eighty three B
        election with the I.R.S. within thirty days, and there's no tax at exercise, and
        your capital gains clock starts. You're risking the strike price, but if the company
        wins, the tax savings can be huge. There's even a provision called Q.S.B.S. that can
        make millions of dollars of gains federally tax free if you hold qualifying startup
        shares for five years. Option three, the forced one. You leave the company.""")
        h = title("When to exercise?", size=56)
        opts = VGroup(
            card(["Wait", "exercise + sell at exit", "no cash at risk", "most common"], width=3.9, color=GREEN_, size=27),
            card(["Exercise early", "+ 83(b) within 30 days", "risk the strike", "big tax wins (QSBS)"], width=3.9, color=BLUE_, size=27),
            card(["When you leave", "the 90-day clock", "pay up or lose it"], width=3.9, color=RED_, size=27),
        ).arrange(RIGHT, buff=0.3).shift(DOWN * 0.3)
        self.play(Write(h))
        for o in opts:
            self.play(FadeIn(o, shift=UP * 0.3), run_time=0.7)
            self.wait(min(15, max(0.1, self.left() / 3.2)))
        self.done()

        self.say("""That third one is the classic trap. Most option plans say that if you
        leave, you have ninety days to exercise your vested options or they disappear. So
        imagine you leave after two years with twenty thousand vested options, at a strike
        of two fifty, and a current value of eight dollars. To keep them you'd have to pay
        fifty thousand in strike, plus possibly tens of thousands in tax, within three
        months, for stock you can't sell. A lot of people just walk away from it. That's why
        you ask for an extended exercise window, five or ten years. Some companies offer it,
        and it's one of the most employee friendly terms there is. There are also firms
        that will lend you the exercise money in exchange for a share of the upside, but
        they take a big cut.""")
        self.clear_all()
        h = title("The 90-day trap", size=56)
        lines = VGroup(
            T("Leave after 2 years: 20,000 vested", size=40),
            T("Strike: 20,000 × $2.50 = $50,000", size=40, color=YELLOW_),
            T("Tax on spread: maybe $30–60K more", size=40, color=ORANGE_),
            T("Due within 90 days, for shares you can't sell", size=40, color=RED_, weight=BOLD),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).shift(DOWN * 0.2)
        fit(lines)
        fix = T("Fix: ask for a 5–10 year exercise window", size=40, color=GREEN_, weight=BOLD).to_edge(DOWN, buff=0.5)
        self.play(Write(h))
        for l in lines:
            self.play(FadeIn(l, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(min(8, max(0.1, self.left() / 6)))
        self.play(FadeIn(fix, shift=UP * 0.2))
        self.done()

        self.say("""And please, before you exercise anything, spend an hour with a tax
        advisor who works with startup employees. It's cheap compared to the mistakes.""")
        self.done()
        self.clear_all()

        # ---- dilution ----
        self.say("""Back to the bigger picture. Two forces shrink your slice before any exit happens. The first
        is dilution. Every time the company raises a new round, it creates new shares
        for the new investors. Your share count stays the same, but the pie gets more
        slices. A typical round dilutes everyone by around fifteen to twenty percent.
        After two more rounds, your zero point zero four percent might be closer to
        zero point zero three. That's fine if the company's value grew a lot more than
        that. It's the price of raising money.""")
        h = title("Dilution: same slice count, bigger pie", size=50)
        def pie(frac, label, color):
            c = Circle(radius=1.4, color=DIM, fill_opacity=0.15, stroke_width=3)
            s = Sector(radius=1.4, angle=TAU * frac, start_angle=PI / 2, color=color,
                       fill_opacity=0.9)
            l = T(label, size=30, color=FG).next_to(c, DOWN, buff=0.3)
            return VGroup(c, s, l)
        pies = VGroup(pie(0.30, "today", YELLOW_), pie(0.25, "after round C", YELLOW_),
                      pie(0.21, "after round D", YELLOW_)).arrange(RIGHT, buff=1.0).shift(DOWN * 0.2)
        note = T("(your wedge exaggerated so you can see it)", size=26, color=DIM).to_edge(DOWN, buff=0.4)
        self.play(Write(h))
        self.play(FadeIn(pies[0]), FadeIn(note))
        self.wait(max(0.1, self.left() * 0.3))
        self.play(TransformFromCopy(pies[0], pies[1]))
        self.play(TransformFromCopy(pies[1], pies[2]))
        self.done()
        self.clear_all()

        # ---- liquidation preference ----
        self.say("""The second force is the one that actually hurts people: liquidation
        preferences. Remember, investors hold preferred stock. When the company is sold,
        preferred shareholders typically get their money back first, before common
        stockholders like you see a dollar. Picture a company that raised three hundred
        million dollars total.""")
        h = title("Liquidation preference: investors are paid first", size=46)
        self.play(Write(h))
        self.done()

        self.say("""If it sells for two hundred million, investors take the whole two
        hundred million and you get nothing, even though two hundred million sounds like
        a great outcome. If it sells for six hundred million, investors take their three
        hundred back first, and the rest gets shared. If it sells for three billion, the
        preferences barely matter and everyone does well. So when a startup sells for a
        disappointing price, employees often get far less than the headlines suggest.""")
        base = DOWN * 2.6
        unit = 4.2 / 3000  # height per $M
        scen = [(200, "$200M sale"), (600, "$600M sale"), (3000, "$3B sale")]
        cols = VGroup()
        for i, (sale, lbl) in enumerate(scen):
            x = (i - 1) * 4.2
            pref = min(sale, 300)
            rest = sale - pref
            h_pref = max(pref * unit, 0.02) * (2.2 if sale < 3000 else 1)
            h_rest = rest * unit * (2.2 if sale < 3000 else 1)
            b1 = Rectangle(width=2.2, height=h_pref, fill_color=BLUE_, fill_opacity=0.9,
                           stroke_width=0).move_to(base + RIGHT * x, aligned_edge=DOWN)
            grp = VGroup(b1)
            if rest > 0:
                b2 = Rectangle(width=2.2, height=h_rest, fill_color=YELLOW_, fill_opacity=0.9,
                               stroke_width=0).next_to(b1, UP, buff=0)
                grp.add(b2)
            l = T(lbl, size=32).next_to(base + RIGHT * x, DOWN, buff=0.25)
            cols.add(VGroup(grp, l))
        legend = VGroup(
            VGroup(Square(0.3, fill_color=BLUE_, fill_opacity=1, stroke_width=0), T("investors' money back", size=28)).arrange(RIGHT, buff=0.2),
            VGroup(Square(0.3, fill_color=YELLOW_, fill_opacity=1, stroke_width=0), T("shared by everyone, incl. you", size=28)).arrange(RIGHT, buff=0.2),
        ).arrange(RIGHT, buff=0.8).next_to(h, DOWN, buff=0.35)
        zero = T("you: $0", size=36, color=RED_, weight=BOLD).next_to(cols[0][0], UP, buff=0.3)
        scale_note = T("(first two bars zoomed 2.2x)", size=24, color=DIM).to_edge(DOWN, buff=0.15).shift(LEFT * 3)
        self.play(FadeIn(legend))
        self.play(GrowFromEdge(cols[0][0], DOWN), FadeIn(cols[0][1]), FadeIn(scale_note))
        self.play(FadeIn(zero))
        self.wait(max(0.1, self.left() * 0.25))
        self.play(GrowFromEdge(cols[1][0], DOWN), FadeIn(cols[1][1]))
        self.wait(max(0.1, self.left() * 0.3))
        self.play(GrowFromEdge(cols[2][0], DOWN), FadeIn(cols[2][1]))
        self.done()
        self.clear_all()

        # ---- outcomes distribution ----
        self.say("""Now let's put it together and ask the honest question: what's this
        equity actually likely to be worth? Here's a rough, made up, but realistically
        shaped spread of outcomes for that Series B company. About two out of three times,
        it fails or sells for a disappointing price and your equity is worth zero. About
        one in five, it has a decent exit around a billion, and after dilution and the
        strike you clear maybe two hundred thousand before taxes. About one in ten, it
        does great, a five billion dollar outcome, worth roughly one point four million to
        you. And maybe two times in a hundred, it becomes a giant, and your grant is worth
        close to nine million.""")
        h = title("What is the equity likely worth?", size=52)
        rows_data = [("66%", "fails / small sale", "$0", RED_),
                     ("22%", "decent exit (~$1B)", "≈ $200K", ORANGE_),
                     ("10%", "great exit (~$5B)", "≈ $1.4M", GREEN_),
                     ("2%", "giant (~$30B)", "≈ $8.9M", YELLOW_)]
        tbl = VGroup()
        for p, d, v, c in rows_data:
            r = VGroup(T(p, size=44, color=c, weight=BOLD), T(d, size=38), T(v, size=44, color=c, weight=BOLD))
            tbl.add(r)
        for r in tbl:
            r[0].move_to(LEFT * 5)
            r[1].move_to(LEFT * 0.6)
            r[2].move_to(RIGHT * 4.6)
        tbl.arrange(DOWN, buff=0.5)
        for r in tbl:
            r[0].set_x(-5.2)
            r[1].set_x(-0.8)
            r[2].set_x(4.6)
        tbl.shift(DOWN * 0.3)
        self.play(Write(h))
        for r in tbl:
            self.play(FadeIn(r, shift=UP * 0.2), run_time=0.7)
            self.wait(min(5, max(0.2, self.left() / 5)))
        self.done()

        self.say("""Two numbers fall out of this. The average outcome is around three
        hundred and sixty thousand dollars, which sounds great. But the most likely
        outcome, the median, is zero. The average is propped up entirely by the rare huge
        wins. That's what people mean when they say startup equity is a lottery ticket.
        It's a lottery ticket with better odds than the real lottery, and you get to
        influence the odds a little by where you choose to work.""")
        res = VGroup(
            VGroup(T("average", size=40, color=DIM), T("≈ $360K", size=64, color=GREEN_, weight=BOLD)).arrange(DOWN),
            VGroup(T("most likely (median)", size=40, color=DIM), T("$0", size=64, color=RED_, weight=BOLD)).arrange(DOWN),
        ).arrange(RIGHT, buff=2).to_edge(DOWN, buff=0.4)
        self.play(tbl.animate.scale(0.75).shift(UP * 0.6), run_time=0.8)
        self.play(FadeIn(res[0], shift=UP * 0.2))
        self.wait(max(0.1, self.left() * 0.3))
        self.play(FadeIn(res[1], shift=UP * 0.2))
        self.done()
        self.clear_all()

        # ---- what to ask ----
        self.say("""So here's your checklist for any offer. Ask these, politely, once you
        have an offer in hand. They're normal questions and good companies answer them.
        What's the fully diluted share count, so I can compute my percentage? What was the
        price per share in the last round, and what's the current four oh nine A strike?
        How much has the company raised in total, and are there any unusual preferences?
        How long is the exercise window if I leave? Is there a refresher policy? And has
        the company ever done a tender offer? With those answers, you can do the math
        from this chapter yourself.""")
        h = title("Questions to ask about any offer", size=52)
        b = bullets([
            "Fully diluted share count?",
            "Last round's price per share? Current 409A strike?",
            "Total raised? Any unusual preferences?",
            "Exercise window if I leave?",
            "Refresher grants?",
            "Any tender offers so far?",
        ], size=38, buff=0.32)
        b.next_to(h, DOWN, buff=0.55)
        self.play(Write(h))
        for r in b:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(min(4, max(0.2, self.left() / 7)))
        self.done()

        self.say("""The big takeaway from these first two chapters. A startup offer is a salary you
        should be happy with on its own, plus a lottery ticket whose odds depend on the
        company. You make real money from startup equity when three things happen:
        you join early enough to own a meaningful slice, the company grows far beyond the
        valuation when you joined, and there's a way to actually sell. Next, let's look at
        which companies might be those winners, starting with how startups grow, stage by stage.""")
        self.clear_all()
        tk = VGroup(
            T("You make real money when:", size=44, color=DIM),
            T("1.  you own a meaningful slice", size=48, weight=BOLD),
            T("2.  value grows far past your entry price", size=48, weight=BOLD),
            T("3.  there's a way to sell", size=48, weight=BOLD),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        fit(tk)
        self.play(FadeIn(tk[0]))
        for r in tk[1:]:
            self.play(FadeIn(r, shift=RIGHT * 0.3), run_time=0.8)
            self.wait(min(3, max(0.2, self.left() / 5)))
        self.done()
        self.clear_all()

