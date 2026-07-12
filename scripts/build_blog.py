#!/usr/bin/env python3
"""
Builds the three new blog posts.

    python3 scripts/build_blog.py

The five existing posts keep their own hand-written design and are left alone —
they were fixed in Phase 1 (canonical, OG, Twitter, BlogPosting + BreadcrumbList,
and real dates recovered from git). These three use the shared shell, which means
they inherit the site nav and the new footer, so the internal linking works.

Every post links to at least one TRADE page and one TEMPLATE/TOOL page in context —
not in a "related posts" box at the bottom, which nobody reads and which Google
weights accordingly, but inside the sentence where the link is actually the useful
next thing to click.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "content"))

import seo_config as C  # noqa: E402
import shell as S       # noqa: E402
from trades import TRADES  # noqa: E402

TRADE_NAV = [(slug, t["name"]) for slug, t in TRADES.items()]
PUBLISHED = "2026-07-12"

POSTS = {}

# ---------------------------------------------------------------------------- 1
POSTS["how-to-write-an-invoice-as-a-contractor"] = {
    "title": "How to Write an Invoice as a Contractor",
    "desc": ("A field guide to writing a contractor invoice that gets paid without a "
             "phone call — every field, why it's there, and what happens when it's not."),
    "h1": "How to write an invoice as a contractor",
    "standfirst": ("Every field, why it is there, and what it costs you when it is "
                   "missing."),
    "body": """
<p>An invoice is not paperwork. It is a demand for money, and how you write it decides
how fast that money arrives — or whether the phone rings first with a question you then
spend twenty unpaid minutes answering.</p>
<p>The difference between an invoice that gets paid quietly and one that gets queried is
almost never the total. It is the detail underneath it. Here is what goes on the document
and, more usefully, what happens when each piece is missing.</p>

<h2>1. Your business details, including your licence number</h2>
<p>Name, address, phone, email. If your trade is licensed, put the licence number on it —
in several states it is a legal requirement on contracts and invoices, and everywhere else
it is a free credibility signal that costs you one line.</p>
<p><strong>What happens without it:</strong> you look like a guy with a truck rather than a
business, and "a guy with a truck" gets paid last, after the utility bill and the credit
card.</p>

<h2>2. The client's name and the job address — which are often different</h2>
<p>The billing name might be a company, a landlord, or a spouse who was not there. The job
address is what everyone actually remembers. Put both on it.</p>
<p><strong>What happens without it:</strong> on a property manager's desk with eleven other
invoices, yours is the one that cannot be matched to a job, so it goes to the bottom of the
pile while someone works out what it was for.</p>

<h2>3. A sequential invoice number</h2>
<p>Not the date. Not a random number. A sequence you keep. It is how you refer to the
document on the phone, how your accountant finds it in April, and how you know whether
INV-0117 was ever paid.</p>
<p><strong>What happens without it:</strong> you cannot chase what you cannot name. "The
invoice I sent you last month" is not a document reference, it is an argument.</p>

<h2>4. A date, and a real due date</h2>
<p>"Due on receipt" is not a due date. It is a wish. Put a calendar date on it: net 14, net
30, whatever you have agreed, expressed as an actual day.</p>
<p><strong>What happens without it:</strong> the invoice is never late, because it was never
due. You have no moment at which you are entitled to follow up, and you will feel awkward
doing it — so you will not.</p>

<h2>5. Itemised line items — the field that decides everything</h2>
<p>This is the one. If you change nothing else after reading this, change this.</p>
<p>"Bathroom work — $1,900" is a single number, and a single number is a single thing to
argue with. The customer has no way to evaluate it except by feel, and their feel is
uninformed and probably optimistic.</p>
<p>Now itemise it. Supply and fit vanity unit. Supply and fit mixer tap. Remove and dispose
of old suite. Labour, twelve hours. Waste disposal. Suddenly there is nothing to argue with:
each line is either right or it is not, and every one of them is right. The total has not
changed. The conversation has.</p>
<p>Say what you did in words a homeowner understands, not trade shorthand. "Diagnosed and
repaired leaking compression fitting under kitchen sink; replaced supply line and isolation
valve; pressure-tested" tells them what they bought. "Fixed leak" tells them nothing and
invites them to decide for themselves what it was worth.</p>

<h2>6. Labour separated from materials</h2>
<p>Show where the money went. It makes the invoice defensible and it makes your markup a
normal part of doing business rather than something discovered.</p>
<p>Different trades draw this line differently, and you should draw it the way your trade
does — the <a href="../for/carpenters/">carpentry</a> and
<a href="../for/roofers/">roofing</a> pages go into how each one handles materials, markup
and disposal.</p>

<h2>7. Subtotal, tax, deposit paid, total due</h2>
<p>Show the deposit as a deduction on the face of the invoice. Not in a note. On the maths.</p>
<p><strong>What happens without it:</strong> the client sees the full job price on an invoice
after they have already given you money, and their first instinct — every time — is that
you are double-billing them. Now you are on the phone explaining, and the trust you spent
three weeks earning has a dent in it.</p>

<h2>8. Payment terms and how to actually pay you</h2>
<p>State the terms, the accepted methods, and what happens if it is late. Terms you did not
state are terms you do not have: you cannot charge a late fee you never mentioned, and you
will not enforce one you feel sheepish about.</p>
<p>And make paying you frictionless. Every extra step between "I should pay this" and "done"
is a step at which they get distracted and it slips another week.</p>

<h2>9. Send it immediately. This is worth more than everything above.</h2>
<p>The value of your work, in a customer's mind, decays. On the day you finish, they can see
the new water heater and they are grateful. Three weeks later it is just a thing in their
basement that they now have to pay for.</p>
<p>Invoice from the driveway. Not that evening, not Sunday, not "when I catch up on
paperwork". If your invoicing takes long enough that you cannot do it on site, that is the
problem to fix — and it is exactly the problem
<a href="../templates/free-contractor-invoice-template/">a good template</a> or an app that
lets you speak the line items is there to solve.</p>

<h2>A checklist you can steal</h2>
<ul>
  <li>Business name, address, phone, email, licence number</li>
  <li>Client name <em>and</em> job address</li>
  <li>Sequential invoice number</li>
  <li>Invoice date and a real due date</li>
  <li>Itemised lines, in plain English, naming what you actually did</li>
  <li>Labour separate from materials</li>
  <li>Subtotal, tax, deposit deducted, total due</li>
  <li>Payment terms, accepted methods, late-payment policy</li>
  <li>Sent the same day the work finished</li>
</ul>
<p>Our <a href="../templates/free-contractor-invoice-template/">free contractor invoice
template</a> has all of it laid out already, in PDF and Word, with trade-specific versions.
No email required.</p>
""",
    "trade_link": "carpenters",
}

# ---------------------------------------------------------------------------- 2
POSTS["contractor-deposit-and-payment-terms"] = {
    "title": "Contractor Deposits & Payment Terms: A Guide",
    "desc": ("How much deposit to ask for, when to ask, and the payment terms that stop "
             "you financing your customer's project out of your own pocket."),
    "h1": "Contractor deposits and payment terms",
    "standfirst": ("How much to ask for, when to ask, and how to stop financing other "
                   "people's projects."),
    "body": """
<p>Here is the thing almost nobody says out loud: if you do the work first and get paid
later, you are a lender. You have extended credit — unsecured, interest-free, to someone
whose finances you know nothing about, on terms you did not negotiate.</p>
<p>Most contractors have never thought about it that way, which is why so many of them are
quietly running a small bank on the side while wondering where the money went.</p>

<h2>Why a deposit is not rude</h2>
<p>New contractors are shy about deposits. They shouldn't be. A deposit is completely
standard, every established business in the trades takes one, and the customer has almost
certainly paid one before.</p>
<p>A deposit does three things at once. It funds your materials, so you are not putting
thousands of dollars of someone else's shingles on your own credit card. It commits the
customer, so they do not cancel on you the morning of — a job with a deposit on it is a job
that is actually happening. And it filters. A customer who will not pay any deposit on a job
with real material costs is telling you something about how the final invoice is going to
go, and you should listen.</p>

<h2>How much to ask for</h2>
<p>It depends almost entirely on how much of your own money the job requires up front.</p>
<ul>
  <li><strong>Small jobs, minimal materials</strong> — no deposit needed. Just get paid on
  completion, on site, before you leave.</li>
  <li><strong>Jobs with real material cost</strong> (a water heater, a fixture package) —
  ask for enough to cover the materials. 30&ndash;50% is normal and nobody will blink.</li>
  <li><strong>Big-ticket material-heavy jobs</strong> — <a href="../for/roofers/">roofing</a>
  is the clearest case. A roof's worth of shingles arrives in the driveway before you have
  earned a cent. 25&ndash;50% on signing is standard and entirely defensible.</li>
  <li><strong>Long jobs</strong> — a deposit plus progress payments tied to stages. See
  below.</li>
</ul>
<p>Be aware that some states cap the deposit a contractor may take on residential work, and a
few require specific contract language alongside it. Check your state's rules before setting
a policy — this is one of the few areas where a well-meaning policy can put you on the wrong
side of a licensing board.</p>

<h2>Progress billing: the fix for long jobs</h2>
<p>On anything running more than a couple of weeks, do not wait until the end. Agree a
schedule of values before you start: a deposit, payments tied to milestones, and a final
payment on completion.</p>
<p>Tie each stage to something visible and undeniable — "on completion of rough-in", "on
completion of drywall" — not to a date, and not to a percentage that is a matter of opinion.
A milestone the customer can walk over and look at is a milestone they cannot argue with.</p>
<p>This is the whole discipline of <a href="../for/general-contractors/">general
contracting</a>, and it is what separates a GC who is solvent in March from one who is
waiting on three clients to pay so they can pay their subs.</p>

<h2>Net 30 is a habit, not a law</h2>
<p>Somewhere along the line "net 30" became the default, and most contractors adopted it
without asking why. For a residential customer, there is usually no reason for it at all.
They are not running an accounts-payable department. They can pay you today.</p>
<p><strong>Net 7, or due on receipt, is entirely reasonable for residential work.</strong>
For commercial clients and property managers, net 30 may genuinely be their process and you
will not change it — but know that you are choosing to finance them for a month, and price
accordingly.</p>

<h2>Late fees you will actually enforce</h2>
<p>State a late fee. 1.5% per month is typical, subject to your state's usury limits, and it
must be on the document before the work starts — you cannot invent it at the point you are
annoyed.</p>
<p>Two honest observations. First, most late fees are never collected; their value is that
they exist and create a deadline in the customer's mind. Second, a late fee you feel
awkward charging is a late fee that does nothing. If you will not enforce it, do not rely on
it — rely on invoicing immediately and following up early instead.</p>

<h2>Getting paid on the day</h2>
<p>For most residential work, the best payment terms in the world are: <em>now, while I am
standing here.</em></p>
<p>The customer's willingness to pay is at its absolute peak in the ten minutes after you
finish. They can see the work. It is fixed. They are grateful. Every hour after that, that
feeling fades and the invoice becomes just another bill competing with the others.</p>
<p>This is why invoicing speed is not an administrative detail — it is a cash-flow strategy.
An invoice handed over on site gets paid at a dramatically higher rate than one emailed on
Sunday, and it is why <a href="../for/handymen/">handymen</a>, whose jobs are small and
numerous, benefit more from fast invoicing than from almost anything else they could change.</p>

<h2>Put it in writing, every time</h2>
<p>Deposit amount, payment schedule, terms, late fee, and what counts as "complete". All of
it on the quote, before anyone starts. A term agreed in a friendly conversation in a driveway
is not a term — it is a memory, and memories differ conveniently.</p>
<p>Our <a href="../templates/free-contractor-invoice-template/">free contractor invoice
template</a> has a payment terms block on it for exactly this reason, and the
<a href="../tools/contractor-hourly-rate-calculator/">rate calculator</a> will tell you
whether the number you are putting on these documents is high enough to be worth
collecting.</p>
""",
    "trade_link": "roofers",
}

# ---------------------------------------------------------------------------- 3
POSTS["quote-follow-up-templates-that-win-jobs"] = {
    "title": "Quote Follow-Up Templates That Win Jobs",
    "desc": ("Most quotes are lost to silence, not to price. Four follow-up messages you "
             "can send, when to send them, and why the second one wins the most work."),
    "h1": "Quote follow-up templates that win jobs",
    "standfirst": ("Most quotes are lost to silence, not to price. Here is what to send, "
                   "and when."),
    "body": """
<p>You send a quote. You hear nothing. You assume they went with someone cheaper, you feel
slightly insulted, and you move on.</p>
<p>Usually that is not what happened. What happened is that they got busy, your quote slid
down the inbox, and they never made a decision at all. Nobody won that job — it just
evaporated. And the contractor who follows up is the one who gets it, not because they were
cheaper, but because they were the one still there when the customer finally had a free
Tuesday to think about it.</p>
<p>Following up feels like nagging. It is not. From the customer's side it reads as
organised, which is exactly the quality they are trying to assess in you.</p>

<h2>The timing that works</h2>
<ul>
  <li><strong>Day 0</strong> — send the quote. Same day as the visit, ideally from the
  driveway. Speed is itself a signal of how the job will go.</li>
  <li><strong>Day 2&ndash;3</strong> — a short "did that arrive, any questions?" Low
  pressure, purely a bump.</li>
  <li><strong>Day 7</strong> — the one that wins the work. Add something: a detail, an
  option, an availability.</li>
  <li><strong>Day 14</strong> — the polite close. You are not chasing; you are freeing your
  calendar.</li>
  <li><strong>Day 30+</strong> — the long-shot revive. Costs you nothing.</li>
</ul>

<h2>Template 1 — the bump (day 2&ndash;3)</h2>
<div class="card">
<p>Hi [Name],</p>
<p>Just checking the quote for the [job] came through OK — sometimes they land in spam.</p>
<p>Happy to walk through any of it, or adjust the scope if you want to look at options.</p>
<p>[Your name], [Business]</p>
</div>
<p>That is the whole message. Do not re-sell. Do not apologise for contacting them. You are
confirming receipt, which is a normal thing a professional does.</p>

<h2>Template 2 — the one that wins jobs (day 7)</h2>
<div class="card">
<p>Hi [Name],</p>
<p>I've got a slot open the week of [date] and wanted to check whether you'd like me to hold
it for the [job].</p>
<p>One thing I should have mentioned: [specific, useful detail — the material lead time, why
you priced a particular element the way you did, a cheaper option if they want it].</p>
<p>If you've gone another way, no problem at all — just let me know and I'll release the
slot.</p>
<p>[Your name]</p>
</div>
<p>This message does three things and every one of them matters.</p>
<p><strong>It creates a real, honest deadline.</strong> Not a fake "prices go up Friday" —
an actual slot in an actual calendar. That gives them a reason to decide now rather than
eventually.</p>
<p><strong>It adds value instead of asking for a decision.</strong> The specific detail is
the point. It proves you have thought about their job since you left, which is more than the
other two quotes have done.</p>
<p><strong>It gives them a graceful exit.</strong> Counter-intuitively, this is why it works.
Most silence is embarrassment — they do not know how to say no. Give them an easy no, and a
surprising number of them say yes instead. And the ones who do say no have told you, which
means you can stop wondering and go win something else.</p>

<h2>Template 3 — the polite close (day 14)</h2>
<div class="card">
<p>Hi [Name],</p>
<p>I'm going to take the [job] off my pending list so I'm not holding time — but the quote
stands if you want to pick it up later. Just reply and we'll go from there.</p>
<p>Thanks for thinking of us.</p>
<p>[Your name]</p>
</div>
<p>This is not a defeat. It reads as busy and organised, and it is astonishing how often the
"I'm closing this off" message is the one that gets an immediate reply. People respond to a
door closing.</p>

<h2>Template 4 — the revive (day 30&ndash;60)</h2>
<div class="card">
<p>Hi [Name],</p>
<p>I was working nearby and thought of the [job] we quoted back in [month]. If it's still on
your list, I have some availability in [month] and I'm happy to honour the original price.</p>
<p>[Your name]</p>
</div>
<p>Costs you two minutes. A meaningful share of dead quotes come back this way — the job did
not stop being necessary, it just stopped being urgent.</p>

<h2>What actually loses quotes</h2>
<p>It is worth being clear about this, because contractors reflexively assume it is price.
Usually it is not. In rough order:</p>
<ul>
  <li><strong>The quote arrived too late.</strong> By the time you sent it on Friday, they
  had two numbers already and had emotionally picked one.</li>
  <li><strong>The quote was one line.</strong> A number with no breakdown gives them nothing
  to compare except the number — so they compare only the number, and you lose to whoever is
  cheapest.</li>
  <li><strong>Nobody followed up.</strong> The job died of neglect.</li>
  <li><strong>The quote looked unprofessional.</strong> Fair or not, a scruffy document
  suggests scruffy work.</li>
  <li><em>Then</em> price.</li>
</ul>
<h2>How to follow up without it eating your week</h2>
<p>The reason contractors do not follow up is not that they disagree with any of this. It is
that following up on eleven open quotes requires remembering eleven open quotes, and by
Thursday you are thinking about a boiler.</p>
<p>So make it mechanical rather than heroic. Keep one list of quotes you have sent, with the
date. Once a week — pick a fixed time, Friday morning with a coffee is as good as any — go
down the list and send the appropriate message from above to anything that has aged past its
next step. It takes about fifteen minutes for a full list, and it is almost certainly the
highest-paid quarter of an hour in your week: one recovered job pays for months of Fridays.</p>
<p>Do not automate it into something that reads like a robot wrote it. These messages work
because they sound like a person who remembers the job. A templated blast that says "Dear
Valued Customer" undoes the exact impression you are trying to make.</p>

<p>Three of those four are fixable this week without dropping your rate by a cent. Speed and
presentation are why <a href="../for/electricians/">electricians</a> — who quote more than
almost any other trade — get so much out of quoting on site rather than at the kitchen table
on Sunday.</p>
<p>Start from a document that looks like a real business sent it: our
<a href="../templates/free-contractor-invoice-template/">free template</a> is a reasonable
place to begin, and if you want to know whether the number on it is high enough in the first
place, the <a href="../tools/contractor-hourly-rate-calculator/">rate calculator</a> will
tell you.</p>
""",
    "trade_link": "electricians",
}


def build(slug, p):
    depth = 1
    url = f"/blog/{slug}.html"
    body = f'<div class="prose">{p["body"]}\n' + S.cta(
        depth, "Quote on site. Get the job.",
        f"Free for {C.FREE_TIER_DOCS_PER_MONTH} documents a month. No card required.",
        "website", "blog", slug) + "</div>"

    html_out = S.page(
        depth=depth, title=p["title"], desc=p["desc"], url_path=url,
        kicker="Guide", h1=p["h1"], standfirst=p["standfirst"],
        body=body, trades=TRADE_NAV,
        breadcrumb=S.breadcrumb_html(depth, [
            ("Home", "../index.html"), ("Blog", "./"), (p["title"], None)]),
        jsonld=[
            {"@context": "https://schema.org", "@type": "BlogPosting",
             "headline": p["h1"], "description": p["desc"],
             "datePublished": PUBLISHED, "dateModified": PUBLISHED,
             "author": {"@type": "Organization", "name": C.SITE_NAME, "url": C.SITE_URL},
             "publisher": {"@type": "Organization", "name": C.SITE_NAME, "url": C.SITE_URL,
                           "logo": {"@type": "ImageObject", "url": C.ORG_LOGO}},
             "image": C.OG_IMAGE,
             "mainEntityOfPage": {"@type": "WebPage", "@id": C.SITE_URL + url},
             "isAccessibleForFree": True},
            S.breadcrumb_ld([("Home", "/"), ("Blog", "/blog/"), (p["title"], url)]),
        ],
    )
    path = f"blog/{slug}.html"
    open(os.path.join(ROOT, path), "w", encoding="utf-8").write(html_out)
    m = re.search(r"<main>(.*?)</main>", html_out, re.S)
    words = len(re.sub(r"<[^>]+>", " ", m.group(1)).split())

    # Enforce the internal-linking rule rather than trusting myself to remember it.
    has_trade = "/for/" in html_out or "../for/" in html_out
    has_tool = ("templates/free-contractor-invoice-template" in html_out
                or "tools/contractor-hourly-rate-calculator" in html_out)
    return path, words, has_trade, has_tool


if __name__ == "__main__":
    for slug, p in POSTS.items():
        path, words, ht, hl = build(slug, p)
        flags = []
        if words < 900:
            flags.append("THIN")
        if not ht:
            flags.append("NO TRADE LINK")
        if not hl:
            flags.append("NO TEMPLATE/TOOL LINK")
        print(f"  {path:<52} {words:>5} words  "
              f"{'  '.join(flags) if flags else 'ok — links to trade + tool'}")
