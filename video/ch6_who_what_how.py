from common import *


class Ch6WhoWhatHow(NarratedScene):
    chapter_label = "6 · Who, what, and how"

    def construct(self):
        self.play(FadeIn(chapter_card(6, "Who, what, and how",
                                      "The three choices that decide how a startup job goes")))
        self.say("""Chapter six. Who you work with, what you work on, and how you work
        on it. You've heard this framing, and it's a good one. Here's how to actually use
        it when you're choosing between offers.""")
        self.done()
        self.clear_all()

        self.say("""Think of the result of a startup job as the product of three numbers,
        not the sum. Who, times what, times how. If any one of them is close to zero, the
        whole thing is close to zero, no matter how good the other two are. A brilliant
        team on a dead end product goes nowhere. A great product with a toxic team burns
        you out. And a great team and product with a broken way of working ships nothing.""")
        eq = VGroup(
            T("Outcome", size=60, weight=BOLD),
            T("≈", size=60, color=DIM),
            T("Who", size=60, color=BLUE_, weight=BOLD),
            T("×", size=60, color=DIM),
            T("What", size=60, color=GREEN_, weight=BOLD),
            T("×", size=60, color=DIM),
            T("How", size=60, color=YELLOW_, weight=BOLD),
        ).arrange(RIGHT, buff=0.35)
        self.play(Write(eq), run_time=2)
        self.wait(min(6, max(0.1, self.left() * 0.4)))
        zero = T("any one ≈ 0  →  everything ≈ 0", size=44, color=RED_).next_to(eq, DOWN, buff=0.8)
        self.play(FadeIn(zero, shift=UP * 0.2))
        self.done()
        self.clear_all()

        # ---- WHO ----
        h = title("Who", size=72, color=BLUE_)
        self.play(Write(h))
        self.say("""Who. This one matters most early in your career, because the people
        around you set your learning rate. At a fifty person startup, you're not
        protected by layers of process. You'll copy the habits of whoever you sit next to,
        good or bad. So, three questions. First, the founders. Have they built something
        before? Do they understand the customer? Do strong people choose to follow them,
        meaning, did good engineers leave good jobs to join? Second, your actual manager
        or tech lead. That one person shapes your day more than the C.E.O. does. Ask to
        meet them before you sign. Third, the bar. Are the engineers you interview with
        people you'd be proud to be compared to? If you walk out of the interviews
        thinking "I'd learn a lot from these people," that's the strongest positive
        signal you'll get.""")
        b = bullets([
            "Founders: track record? understand the customer?",
            "Did strong people leave good jobs to join?",
            "Meet your actual manager / tech lead",
            "Would you learn a lot from your interviewers?",
        ], size=38).next_to(h, DOWN, buff=0.7)
        for r in b:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(min(12, max(0.1, self.left() / 5)))
        self.done()

        self.say("""A practical trick. Look up the engineers on LinkedIn or GitHub. Where
        did they come from, and how long do people stay? If engineers keep leaving after a
        year, ask why. And ask the people interviewing you, "why did you join, and what
        would make you leave?" The answers are surprisingly honest.""")
        self.done()
        self.clear_all()

        # ---- WHAT ----
        h = title("What", size=72, color=GREEN_)
        self.play(Write(h))
        self.say("""What. Two levels here: what the company works on, and what you work on
        inside it. For the company, the key A.I. specific question is this: when the
        models get better, does this product get better, or does it get replaced? Think
        about it this way. A company whose product is just a nice wrapper around a model
        gets eaten every time OpenAI or Anthropic ships a feature. A company that owns
        something the model makers don't, like proprietary data, deep workflow inside a
        specific industry, a distribution channel, or hard engineering around reliability,
        gets a free upgrade every time models improve.""")
        two = VGroup(
            card(["Gets replaced", "thin wrapper on a model", "labs ship your feature", "no data, no workflow"], width=5.6, color=RED_, size=30),
            card(["Gets a free upgrade", "owns data / workflow", "deep in one industry", "hard reliability work"], width=5.6, color=GREEN_, size=30),
        ).arrange(RIGHT, buff=0.5).shift(DOWN * 0.4)
        self.play(FadeIn(two[0], shift=RIGHT * 0.3))
        self.wait(min(15, max(0.1, self.left() * 0.5)))
        self.play(FadeIn(two[1], shift=LEFT * 0.3))
        self.done()

        self.say("""And the other big "what" question: is anyone actually paying? Real
        revenue from real customers, growing month over month, and customers who stay
        and pay more over time. You can ask about that in interviews. Something like,
        "how's revenue trending, and how many customers renew?" A good company will be
        proud to tell you, at least roughly.""")
        self.play(FadeOut(two))
        q = card(["Ask: is anyone paying?", "revenue trend?", "do customers renew and expand?"],
                 width=8, color=GREEN_, size=34).shift(DOWN * 0.4)
        self.play(FadeIn(q, shift=UP * 0.3))
        self.done()

        self.say("""Then, what you would personally work on. At an A.I. company, you
        don't need to be a researcher. A huge amount of the valuable work is regular,
        excellent software engineering: making inference fast and cheap, building
        evaluation systems so you know if a change made the model better or worse,
        integrating with messy customer systems, and making agent products reliable.
        Choose a role where you'll be close to the core product and close to users, not
        an isolated side project. Skills like evals, inference, and agent reliability are
        valuable at every company on that landscape map.""")
        self.play(FadeOut(q))
        b = bullets([
            ("Inference: fast, cheap model serving", FG),
            ("Evals: measuring if changes help", FG),
            ("Integrations with messy real systems", FG),
            ("Agent reliability & safety", FG),
        ], size=38, dot_color=GREEN_).next_to(h, DOWN, buff=0.7)
        for r in b:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(min(8, max(0.1, self.left() / 5)))
        self.done()
        self.clear_all()

        # ---- HOW ----
        h = title("How", size=72, color=YELLOW_)
        self.play(Write(h))
        self.say("""How. This is the culture and the way work gets done day to day. Some
        A.I. startups right now openly run very intense schedules, long days, six days a
        week, in the office. Others are remote and calmer. Neither is wrong, but you should
        choose on purpose. Ask how often they ship to customers. Ask who decides what gets
        built, and how much an engineer like you gets to decide. Ask what a normal week
        looks like, and what happened the last time something broke in production. Fast
        shipping, real ownership, and honest postmortems are the signs of a healthy
        "how." Chaos with no learning, and heroics as the default, are warning signs.""")
        two = VGroup(
            card(["Green flags", "ships to users weekly", "engineers own outcomes", "blameless postmortems"], width=5.6, color=GREEN_, size=30),
            card(["Red flags", "constant firefighting", "decisions by one person", "heroics as the plan"], width=5.6, color=RED_, size=30),
        ).arrange(RIGHT, buff=0.5).shift(DOWN * 0.4)
        self.play(FadeIn(two[0], shift=RIGHT * 0.3))
        self.wait(min(15, max(0.1, self.left() * 0.5)))
        self.play(FadeIn(two[1], shift=LEFT * 0.3))
        self.done()
        self.clear_all()

        # ---- great people vs fast growth vs the right thing ----
        self.say("""Now the question you've been wrestling with, because it's the real
        one. There are three popular heuristics, and they seem to point different ways.
        One: work with great people, because learning from the best compounds over a
        career. Two: just join whatever is growing fastest. Sheryl Sandberg's famous
        advice was, if you're offered a seat on a rocket ship, don't ask which seat. And
        three: work on the right thing. Your example is a sharp one. A principal engineer
        at Google can be one of the best engineers alive and still make far less than a
        college dropout who happened to be building the right thing at the right time.""")
        h = title("Great people · fast growth · the right thing", size=44)
        three = VGroup(
            card(["Great people", "skills compound", "hard to measure", "from outside"], width=3.9, color=BLUE_, size=28),
            card(["Fast growth", "\"rocket ship\"", "measurable", "but can be hype"], width=3.9, color=GREEN_, size=28),
            card(["The right thing", "where value is created", "biggest payoff", "hardest to know early"], width=3.9, color=YELLOW_, size=28),
        ).arrange(RIGHT, buff=0.3).shift(DOWN * 0.3)
        self.play(Write(h))
        for c_ in three:
            self.play(FadeIn(c_, shift=UP * 0.3), run_time=0.7)
            self.wait(min(10, max(0.1, self.left() / 4)))
        self.done()

        self.say("""Here's how I'd reconcile them. Being great at something is your skill.
        Working on the right thing is your leverage. What you earn is roughly skill times
        leverage. The Google principal has huge skill but sits on a mature product, so
        each extra unit of their skill moves the company a little. The dropout has less
        skill, but is pointed at something that's about to grow a thousandfold, so the same
        effort is multiplied enormously. That's why money follows position more than
        ability.""")
        self.clear_all()
        eq = VGroup(T("payoff", size=56, weight=BOLD), T("≈", size=56, color=DIM),
                    T("skill", size=56, color=BLUE_, weight=BOLD), T("×", size=56, color=DIM),
                    T("leverage", size=56, color=YELLOW_, weight=BOLD)).arrange(RIGHT, buff=0.35).shift(UP * 1.4)
        ex = VGroup(
            VGroup(T("Google principal:", size=34, color=DIM), T("skill 10 × leverage 1 = 10", size=38)).arrange(RIGHT, buff=0.3),
            VGroup(T("Dropout at the frontier:", size=34, color=DIM), T("skill 4 × leverage 20 = 80", size=38, color=YELLOW_)).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).shift(DOWN * 0.8)
        self.play(Write(eq))
        self.wait(min(12, max(0.1, self.left() / 2.5)))
        for e in ex:
            self.play(FadeIn(e, shift=UP * 0.2), run_time=0.7)
            self.wait(min(6, max(0.1, self.left() / 3)))
        self.done()

        self.say("""But be careful with the dropout story, because of survivorship bias.
        For every dropout who picked the right thing, there are hundreds who were just as
        sure and picked something that went nowhere. You hear about the winner. Nobody
        makes a video about the rest. So "work on the right thing" is great advice in
        hindsight, and very hard advice to follow in advance, because everyone thinks
        their thing is the right one.""")
        surv = T("you only hear from the winners", size=40, color=RED_, weight=BOLD).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(surv, shift=UP * 0.2))
        self.done()
        self.clear_all()

        self.say("""Which is why fast growth is such a good heuristic. It's the market's
        vote on what the right thing is, made by customers paying money, not by you
        guessing. And fast growth also solves the great people problem over time, in two
        ways. Growing companies attract strong people, because strong people also want to
        be on rocket ships. And growing companies have more problems than people, so you
        get handed bigger responsibilities before you feel ready. That's where most real
        learning happens. Mentorship from great people speeds you up. Hard problems with
        real stakes are what actually make you good.""")
        h = title("Why fast growth is a good proxy", size=50)
        b = bullets([
            ("Growth = customers voting on \"the right thing\"", GREEN_),
            ("Growth attracts great people over time", BLUE_),
            ("More problems than people → you get big scope early", YELLOW_),
        ], size=36).next_to(h, DOWN, buff=0.7)
        self.play(Write(h))
        for r in b:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(min(12, max(0.1, self.left() / 4)))
        self.done()

        self.say("""Two caveats. First, measure growth in revenue and usage, not in
        valuation or headcount. Valuation growth can be pure hype, and that's the greater
        fool problem from chapter eight. Second, growth without good people around you can
        still teach you bad habits, chaos, and heroics. So here's the combined filter.
        Step one, only consider companies whose real revenue or usage is growing fast.
        That handles "the right thing" as well as anyone can. Step two, among those, pick
        the one with the people you'd learn the most from. Step three, inside it, ask for
        the role closest to whatever is growing fastest. Growth picks the field. People
        pick the team. Position picks the seat.""")
        self.clear_all()
        h = title("A combined filter", size=56)
        steps = VGroup(
            card(["1. Growth", "real revenue / usage", "growing fast"], width=3.9, color=GREEN_, size=28),
            card(["2. People", "who would you", "learn most from?"], width=3.9, color=BLUE_, size=28),
            card(["3. Position", "the seat closest to", "what's growing"], width=3.9, color=YELLOW_, size=28),
        ).arrange(RIGHT, buff=0.3).shift(DOWN * 0.2)
        tag = T("growth picks the field · people pick the team · position picks the seat", size=28, color=DIM).to_edge(DOWN, buff=0.5)
        self.play(Write(h))
        for st in steps:
            self.play(FadeIn(st, shift=UP * 0.3), run_time=0.7)
            self.wait(min(12, max(0.1, self.left() / 4)))
        self.play(FadeIn(tag))
        self.done()
        self.clear_all()

        self.say("""Here's a simple way to use all this. For each company you're
        considering, give it a score from one to five on who, what, and how, and multiply.
        Imagine Company A: famous brand, great product, but you'd be on a small side team
        with a manager you didn't click with. Who two, what four, how three. That's
        twenty four. Company B: less famous, but you loved the team, the product has
        paying customers, and they ship constantly. Who five, what four, how four.
        Eighty. That gap is bigger than any difference in equity grants between them,
        and it's your best predictor of how much you'll grow.""")
        h = title("Score each offer, then multiply", size=50)
        def row(name, a, b, c, col):
            return VGroup(T(name, size=38, weight=BOLD, color=col),
                          T(f"{a}", size=44, color=BLUE_), T("×", size=40, color=DIM),
                          T(f"{b}", size=44, color=GREEN_), T("×", size=40, color=DIM),
                          T(f"{c}", size=44, color=YELLOW_), T("=", size=40, color=DIM),
                          T(f"{a*b*c}", size=56, color=col, weight=BOLD)).arrange(RIGHT, buff=0.4)
        hdrs = VGroup(T("", size=30), T("who", size=28, color=BLUE_), T("", size=28),
                      T("what", size=28, color=GREEN_), T("", size=28), T("how", size=28, color=YELLOW_))
        r1 = row("Company A", 2, 4, 3, ORANGE_)
        r2 = row("Company B", 5, 4, 4, GREEN_)
        tbl = VGroup(r1, r2).arrange(DOWN, buff=0.8, aligned_edge=LEFT).shift(DOWN * 0.3)
        self.play(Write(h))
        self.wait(min(4, max(0.1, self.left() * 0.15)))
        self.play(FadeIn(r1, shift=UP * 0.2))
        self.wait(min(12, max(0.1, self.left() * 0.45)))
        self.play(FadeIn(r2, shift=UP * 0.2))
        self.done()
        self.clear_all()
