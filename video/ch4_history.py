from common import *


def timeline_event(xpos, yr, a, b, c, up):
    d = Dot(np.array([xpos, -0.2, 0]), radius=0.11, color=c)
    g = VGroup(T(yr, size=32, color=c, weight=BOLD), T(a, size=24), T(b, size=21, color=DIM))
    g.arrange(DOWN, buff=0.08)
    g.next_to(d, UP if up else DOWN, buff=0.35)
    stem = Line(d.get_center(), g.get_bottom() if up else g.get_top(), color=c, stroke_width=2)
    return VGroup(stem, d, g)


class Ch4History(NarratedScene):
    chapter_label = "4 · How we got here"

    def construct(self):
        self.play(FadeIn(chapter_card(4, "How we got here",
                                      "Three eras of AI startups, 2012 to now")))
        self.say("""Chapter four. How we got here. A quick history, because it explains
        why the A.I. startup world looks so lopsided today. I'll tell it in three eras.""")
        self.done()
        self.clear_all()

        line = Line(LEFT * 6.4, RIGHT * 6.4, color=DIM, stroke_width=3).shift(DOWN * 0.2)
        self.play(Create(line), run_time=1)
        xs = np.linspace(-5.8, 5.8, 9)

        def show(i, yr, a, b, c):
            e = timeline_event(xs[i], yr, a, b, c, i % 2 == 0)
            self.play(FadeIn(e, shift=UP * 0.1), run_time=0.8)
            return e

        era1 = T("Era 1 · the research era", size=34, color=BLUE_, weight=BOLD).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(era1))
        self.say("""Era one, the research era, roughly twenty twelve to twenty twenty one.
        In twenty twelve, a neural network called AlexNet crushed an image recognition
        contest using graphics cards, and suddenly deep learning worked. Google bought
        DeepMind in twenty fourteen for around half a billion dollars. OpenAI started in
        twenty fifteen as a nonprofit. And in twenty seventeen, Google researchers
        published the transformer, the design behind every large language model since.
        Several of those authors left to found startups, like Cohere and Character dot
        A.I. In this era, A.I. startups were mostly research teams, and the way they paid
        off was getting bought by Google, Facebook, or Microsoft.""")
        show(0, "2012", "AlexNet", "deep learning works", BLUE_)
        self.wait(min(3, self.left() / 5))
        show(1, "2014", "Google buys DeepMind", "~$500M", BLUE_)
        self.wait(min(3, self.left() / 4))
        show(2, "2015", "OpenAI founded", "as a nonprofit", BLUE_)
        self.wait(min(3, self.left() / 3))
        show(3, "2017", "The transformer", "\"Attention Is All You Need\"", BLUE_)
        self.done()

        era2 = T("Era 2 · the ChatGPT shock", size=34, color=YELLOW_, weight=BOLD).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(era1, era2))
        self.say("""Era two, the ChatGPT shock. In late twenty twenty two, ChatGPT became
        the fastest growing consumer app ever at the time. Microsoft put about ten billion
        dollars into OpenAI. Thousands of startups appeared, and a lot of them were thin
        layers on top of OpenAI's model: a nice interface and a clever prompt. Many of those
        got crushed within a year or two, because the model makers kept adding the same
        features themselves. That's where the insult "G.P.T. wrapper" comes from. Keep it
        in mind. It comes back in chapter six.""")
        show(4, "2022", "ChatGPT launches", "the starting gun", YELLOW_)
        self.wait(min(4, self.left() / 3))
        show(5, "2023", "Microsoft ~$10B", "into OpenAI", YELLOW_)
        self.done()

        era3 = T("Era 3 · the scale era", size=34, color=GREEN_, weight=BOLD).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(era2, era3))
        self.say("""Era three, the scale era, twenty twenty four to now. Two things
        happened. First, the labs started raising unbelievable amounts of money to pay
        for computing power. Anthropic was valued around three hundred eighty billion in
        February twenty twenty six, and then nine hundred sixty five billion in its Series
        H round in May, according to Reuters and Bloomberg. OpenAI was at eight hundred
        fifty two billion in March and is reportedly raising again at over a trillion.
        Second, the products started making real money, especially coding tools. Cursor
        went from a tiny team to a sixty billion dollar all stock acquisition by SpaceX,
        which had itself merged with Elon Musk's x A I and then gone public in June, in the
        largest I.P.O. ever.""")
        show(6, "2024–25", "Coding tools take off", "Cursor, Cognition, Claude Code", GREEN_)
        self.wait(min(6, self.left() / 3))
        show(7, "May 2026", "Anthropic Series H", "$965B post-money", GREEN_)
        self.wait(min(6, self.left() / 2))
        show(8, "Jun 2026", "SpaceX IPO", "then buys Cursor for $60B", GREEN_)
        self.done()
        self.clear_all()

        # ---- the odd exits ----
        self.say("""There's one more piece of recent history that matters for you
        specifically, as a future employee. Starting in twenty twenty four, big companies
        found a new way to grab A.I. startups without technically buying them. They
        license the technology and hire the founders and the top researchers. Microsoft
        did it with Inflection. Google did it with Character dot A.I., and later with the
        coding startup Windsurf. Meta bought forty nine percent of Scale A.I. and hired its
        C.E.O.""")
        h = title("The new exit: license + hire", size=52)
        deals = VGroup(
            card(["Inflection", "→ Microsoft, 2024"], width=3.6, color=PURPLE_, size=32),
            card(["Character.AI", "→ Google, 2024"], width=3.6, color=PURPLE_, size=32),
            card(["Windsurf", "→ Google, 2025"], width=3.6, color=PURPLE_, size=32),
            card(["Scale AI", "→ Meta, 49%, 2025"], width=3.6, color=PURPLE_, size=32),
        ).arrange_in_grid(2, 2, buff=0.45).shift(DOWN * 0.4)
        self.play(Write(h))
        for d in deals:
            self.play(FadeIn(d, shift=UP * 0.2), run_time=0.6)
            self.wait(min(3, max(0.1, self.left() / 6)))
        self.done()

        self.say("""In these deals, the outcome for employees varied a lot. In some, the
        buyer paid out employee stock. In others, the people who stayed behind were left
        at a company whose founders had just walked out the door. Windsurf is the famous
        example: Google hired the leaders, and the remaining team was bought days later by
        Cognition, with reports of very different outcomes depending on who you were. The
        lesson isn't "avoid startups." It's: the size of the exit is only half the
        story. The shape of the exit decides who gets paid.""")
        lesson = T("Size of exit = half the story. Shape decides who gets paid.",
                   size=36, color=YELLOW_, weight=BOLD).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(lesson, shift=UP * 0.2))
        self.done()
        self.clear_all()

        # ---- sources ----
        self.say("""Before we look at today's landscape, a word on sources, because you
        asked about this, and you're right to. Most of what you read about A.I. startups is
        written by venture capitalists. They're smart, but they have an incentive. Their
        portfolio is marked at the valuation of the last round, and good press helps those
        companies raise the next round and hire. So V.C. content tilts optimistic. Founders
        are more raw, but mostly in specific places: post mortems after a company dies,
        podcasts after they've exited, and private conversations. While they're raising
        money or recruiting, founders are selling too. The most honest sources tend to be
        the boring ones: S.E.C. filings, which have legal liability attached; wire
        reporting from Reuters and Bloomberg; compensation data from Carta and levels dot
        f y i; and ex employees talking to each other.""")
        h = title("Who's talking, and why?", size=52)
        grid = VGroup(
            card(["VC blogs & podcasts", "incentive: marks, deal flow", "tilts optimistic"], width=5.8, color=RED_, size=30),
            card(["Founders, while raising", "incentive: recruit, fundraise", "also selling"], width=5.8, color=ORANGE_, size=30),
            card(["Post-mortems, ex-employees", "little left to sell", "most candid"], width=5.8, color=GREEN_, size=30),
            card(["Filings, wires, comp data", "legal liability, data", "most reliable numbers"], width=5.8, color=BLUE_, size=30),
        ).arrange_in_grid(2, 2, buff=0.35).shift(DOWN * 0.4)
        fit(grid, 13, 5.6)
        self.play(Write(h))
        for g in grid:
            self.play(FadeIn(g, shift=UP * 0.2), run_time=0.6)
            self.wait(min(8, max(0.1, self.left() / 5)))
        self.done()

        self.say("""In this video, the valuation and revenue numbers come from reporting
        on funding rounds and from S.E.C. filings, like SpaceX's. Where a number only showed
        up in one place, I'll call it reported, and you should treat it as approximate. And
        all of it is as of October twenty twenty six. These numbers change every few
        months.""")
        self.done()
        self.clear_all()
