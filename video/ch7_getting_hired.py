from common import *


class Ch7GettingHired(NarratedScene):
    chapter_label = "7 · How people get hired"

    def construct(self):
        self.play(FadeIn(chapter_card(7, "How people get hired",
                                      "What actually works, and a plan for you")))
        self.say("""Chapter seven. How people actually get startup jobs. The short version:
        startups hire very differently from big companies, and the front door, the online
        application, is the least effective way in.""")
        self.done()
        self.clear_all()

        # ---- funnel ----
        self.say("""Here's roughly how well different approaches work. A cold application
        on a careers page is the weakest, because a small startup might get hundreds of
        applicants for one role, and nobody's job is to read them carefully. A short,
        specific message straight to a founder or an engineering lead works much better,
        because at a startup, those people are the ones hiring, and they read their own
        email. A referral from someone inside is even better. And the strongest of all is
        when they come to you, because they saw something you built or wrote.""")
        h = title("Ways in, weakest to strongest", size=50)
        rungs = [("Cold application on a careers page", RED_, 5.0),
                 ("Direct message to a founder / eng lead", ORANGE_, 7.0),
                 ("Referral from someone inside", GREEN_, 9.0),
                 ("They find you through your work", YELLOW_, 11.0)]
        bars = VGroup()
        for i, (txt, c, w) in enumerate(rungs):
            r = RoundedRectangle(corner_radius=0.12, width=w, height=0.85, stroke_width=0,
                                 fill_color=c, fill_opacity=0.85)
            t = T(txt, size=30, color=BG, weight=BOLD).move_to(r)
            bars.add(VGroup(r, t))
        bars.arrange(DOWN, buff=0.25).shift(DOWN * 0.4)
        self.play(Write(h))
        for b in bars:
            self.play(GrowFromCenter(b), run_time=0.7)
            self.wait(min(7, max(0.1, self.left() / 5)))
        self.done()
        self.clear_all()

        # ---- where jobs are ----
        self.say("""Where do you find the openings? A few places worth knowing.
        Y Combinator's job board, Work at a Startup, lists jobs at hundreds of Y.C.
        companies and lets you message founders directly. Wellfound, which used to be
        AngelList, is the other big startup job board. Hacker News has a "who's hiring"
        thread on the first weekday of every month, where founders post themselves. And a
        lot of A.I. hiring happens on X, where founders tweet "we're hiring" and engineers
        show off what they've built. Also, check the portfolio pages of good venture
        firms, which list every company they've funded. Just remember the incentive point
        from earlier: a V.C. listing a company is not an endorsement of the job.""")
        h = title("Where to look", size=56)
        b = bullets([
            "YC's Work at a Startup  (message founders directly)",
            "Wellfound (formerly AngelList Talent)",
            "Hacker News \"Who's hiring?\" (1st weekday of each month)",
            "X / Twitter: founders post roles, engineers post work",
            "VC portfolio pages: lists of funded companies",
        ], size=34).next_to(h, DOWN, buff=0.6)
        self.play(Write(h))
        for r in b:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(min(7, max(0.1, self.left() / 6)))
        self.done()
        self.clear_all()

        # ---- proof of work ----
        self.say("""The single biggest lever, though, is proof of work. Startups are
        hiring people who will ship from week one. A public project that shows you can
        build something real with A.I. beats a perfect résumé. And you already have the
        raw material. You've built L.L.M. agent trading experiments and looked at LLM
        coordination for drone fleets. Pick one, clean it up, and make it public: a
        README with a short demo video, and most importantly, a write up of what didn't
        work and how you measured it. That last part, the evaluation, is exactly what A.I.
        startups struggle with, and seeing that you think about it is a strong signal.""")
        h = title("Proof of work beats a résumé", size=52)
        steps = VGroup(
            card(["1. Pick one project", "agent trading", "or drone-LLM coordination"], width=4, color=BLUE_, size=28),
            card(["2. Make it public", "clean repo, README", "2-minute demo video"], width=4, color=GREEN_, size=28),
            card(["3. Write it up", "what failed, what you", "measured, what you'd do next"], width=4, color=YELLOW_, size=28),
        ).arrange(RIGHT, buff=0.3).shift(DOWN * 0.3)
        self.play(Write(h))
        for s in steps:
            self.play(FadeIn(s, shift=UP * 0.3), run_time=0.7)
            self.wait(min(10, max(0.1, self.left() / 4)))
        self.done()
        self.clear_all()

        # ---- the message ----
        self.say("""Now the direct message. Keep it to four or five sentences. One: who you
        are, in a single line. Two: something specific about their product that shows you
        actually used it or thought about it. Three: a link to the most relevant thing you
        built. Four: a clear, small ask, like "would you be open to a fifteen minute call
        about the backend role?" No long cover letter. Founders get many of these, and the
        short specific ones are the ones that get answered.""")
        h = title("The cold message: 4–5 sentences", size=50)
        msg = VGroup(
            T("1.  Who you are, in one line", size=36),
            T("2.  Something specific about their product", size=36),
            T("3.  Link to your most relevant project", size=36),
            T("4.  A small, clear ask (15-min call?)", size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        box = SurroundingRectangle(msg, color=BLUE_, buff=0.4, corner_radius=0.15)
        g = VGroup(box, msg).shift(DOWN * 0.3)
        self.play(Write(h), Create(box))
        for m in msg:
            self.play(FadeIn(m, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(min(7, max(0.1, self.left() / 5)))
        self.done()
        self.clear_all()

        # ---- interviews ----
        self.say("""What are startup interviews like? Usually more practical than big
        tech. There's often still a coding screen, so your interview prep isn't wasted.
        But you'll also see take home projects, pair programming on something like their
        real codebase, and system design focused on the actual product. Some A.I.
        companies do a paid work trial, a day or even a week working with the team. And the
        part you dislike, behavioral, usually shows up as a conversation with a founder.
        The good news is it's less "tell me about a time" and more "what have you built,
        why did you make those choices, and why us." If you've done the proof of work
        step, you're just telling the story of your project.""")
        h = title("Startup interviews", size=56)
        g = VGroup(
            card(["Coding screen", "still common", "your prep still counts"], width=3.9, color=BLUE_, size=28),
            card(["Practical rounds", "take-home, pairing,", "product system design"], width=3.9, color=GREEN_, size=28),
            card(["Founder chat", "what you built and why", "why this company"], width=3.9, color=YELLOW_, size=28),
        ).arrange(RIGHT, buff=0.3).shift(DOWN * 0.3)
        trial = T("Some AI startups: a paid work trial (a day to a week)", size=30, color=DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h))
        for c_ in g:
            self.play(FadeIn(c_, shift=UP * 0.3), run_time=0.7)
            self.wait(min(10, max(0.1, self.left() / 4)))
        self.play(FadeIn(trial))
        self.done()
        self.clear_all()

        # ---- your edge ----
        self.say("""Let's talk about your edge. Coming from a Defense Department role is
        not a weakness. Defense tech startups specifically want engineers who understand
        how government programs work, who've dealt with security constraints, and who
        can talk to military customers in their language. More broadly, a lot of A.I.
        startups now sell to big, regulated customers like banks, hospitals, and
        government, and experience shipping in that kind of environment, where
        reliability and security really matter, is something many startup engineers don't
        have. And being close to New York helps. It has one of the largest A.I. startup
        scenes outside the Bay Area, especially in finance, legal, and media A.I.""")
        h = title("Your edge", size=60)
        b = bullets([
            ("Defense tech wants DoD experience", YELLOW_),
            ("Regulated customers: security & reliability", FG),
            ("NYC: a big applied-AI startup scene", FG),
            ("Real projects with LLM agents", FG),
        ], size=40).next_to(h, DOWN, buff=0.7)
        self.play(Write(h))
        for r in b:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(min(10, max(0.1, self.left() / 5)))
        self.done()
        self.clear_all()

        # ---- 30-day plan ----
        self.say("""So here's a concrete thirty day plan. Week one: pick your target tier
        and make a list of twenty companies, using the who, what, how filter from the last
        chapter. Week two: polish one project and publish the write up. Week three: send
        ten short, specific messages to founders or engineering leads, and ask people you
        know for two or three referrals. Week four: run interviews in parallel, not one at
        a time, because overlapping offers give you leverage, and use the questions from
        chapters one and two to compare them.""")
        h = title("A 30-day plan", size=56)
        weeks = VGroup(
            card(["Week 1", "list 20 companies", "who · what · how"], width=2.95, color=BLUE_, size=26),
            card(["Week 2", "publish one project", "+ write-up"], width=2.95, color=GREEN_, size=26),
            card(["Week 3", "10 direct messages", "2–3 referrals"], width=2.95, color=ORANGE_, size=26),
            card(["Week 4", "interviews in parallel", "compare offers"], width=2.95, color=YELLOW_, size=26),
        ).arrange(RIGHT, buff=0.22).shift(DOWN * 0.3)
        fit(weeks, 13)
        self.play(Write(h))
        for w_ in weeks:
            self.play(FadeIn(w_, shift=UP * 0.3), run_time=0.6)
            self.wait(min(8, max(0.1, self.left() / 5)))
        self.done()

        self.say("""And one point on negotiating. Startups usually have some flexibility,
        and many will let you choose between more salary or more equity. Given everything
        in chapters one and two, a reasonable default is to get the salary to a level you're happy
        with first, then ask about equity, and always ask about the exercise window and
        refreshers, because those can be easier for them to change than the headline
        numbers.""")
        self.done()
        self.clear_all()
