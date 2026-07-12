#!/usr/bin/env python3
"""
Generates every Phase 2 page from the content data files.

    python3 scripts/build_pages.py

Emits:
    /for/                                 trades hub
    /for/<trade>/                         10 trade landing pages
    /compare/                             comparison hub
    /compare/toolbelt-vs-<x>/             5 comparison pages
    /templates/free-contractor-invoice-template/
    /tools/contractor-hourly-rate-calculator/

Content lives in scripts/content/{trades,competitors}.py. This file is the renderer
and holds no facts of its own — so a price change is one edit in seo_config.py and
a re-run, never a search-and-replace across 18 HTML files.

Word counts are asserted at the end: the brief calls for 900+ words of genuinely
useful content per page, and a generator that quietly emits a 400-word page is a
generator that is building doorway pages.
"""
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "content"))

import seo_config as C          # noqa: E402
import shell as S               # noqa: E402
from trades import TRADES       # noqa: E402
from competitors import COMPETITORS, VERIFIED_ON  # noqa: E402

TRADE_NAV = [(slug, t["name"]) for slug, t in TRADES.items()]


def write(relpath, content):
    full = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    # Count ONLY the <main> content. Counting the nav and footer too would inflate
    # every page by ~150 words and let a genuinely thin page pass the 900-word bar —
    # which is exactly the self-deception this check exists to prevent.
    m = re.search(r"<main>(.*?)</main>", content, re.S)
    body = m.group(1) if m else content
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    return relpath, words


def esc(s):
    return html.escape(s, quote=False)


# ---------------------------------------------------------------- trade pages --
def build_trade(slug, t):
    depth = 2
    url = f"/for/{slug}/"
    sibs = [(s, TRADES[s]["name"]) for s in t["siblings"] if s in TRADES]

    pains = "".join(
        f'<div class="card"><h3>{esc(h)}</h3><p>{esc(b)}</p></div>'
        for h, b in t["pains"])

    feats = "".join(
        f"<h3>{esc(h)}</h3><p>{esc(b)}</p>" for h, b in t["features"])

    rows = "".join(
        f'<tr><td>{esc(item)}</td><td>{esc(unit)}</td><td class="num">{esc(rng)}</td></tr>'
        for item, unit, rng in t["line_items"])

    faqs = "".join(
        f'<p class="faq-q">{esc(q)}</p><p>{a}</p>' for q, a in t["faqs"])

    sib_tiles = "".join(
        f'<a class="tile" href="../{s}/">Invoicing for {n.lower()}'
        f'<small>How {n.lower()} quote, bill and get paid — and where the money leaks.</small></a>'
        for s, n in sibs)

    body = f"""<div class="prose">
{''.join(f'<p>{esc(p)}</p>' for p in t["intro"])}

<h2>What actually goes wrong when {t["name"].lower()} invoice</h2>
<p>These are the four billing problems we hear most often from {t["name"].lower()}.
None of them is about not knowing how to do the work — they are all about the gap
between finishing a job and getting paid for it.</p>
{pains}

<h2>How Toolbelt fits a {t["singular"]}'s day</h2>
{feats}

<h2>Example {t["singular"]} invoice line items</h2>
<p>These are example line items with typical US market ranges, to show how a
{t["singular"]}'s invoice breaks down. <strong>They are illustrations, not our
recommended prices</strong> — your rates depend on your market, your licence, your
overhead and your reputation, and nobody on the internet should be setting them
for you.</p>
<div class="tablewrap">
<table>
<thead><tr><th>Line item</th><th>Unit</th><th class="num">Typical range</th></tr></thead>
<tbody>{rows}</tbody>
</table>
</div>
<p>In Toolbelt you save the ones you use constantly, so after a couple of weeks
most of an invoice is taps rather than typing. You can read more on structuring a
document properly in our
<a href="../../blog/professional-invoice-template-guide.html">invoice template guide</a>,
or start from our
<a href="../../templates/free-contractor-invoice-template/">free contractor invoice template</a>.</p>

<h2>Pricing</h2>
<p>Toolbelt is <strong>free for {C.FREE_TIER_DOCS_PER_MONTH} invoices or quotes a
month</strong>, with every feature switched on and no card required. Past that it
is <strong>${C.PRICE_MONTHLY}/month</strong> or <strong>${C.PRICE_YEARLY}/year</strong>
— one price, everything included. If you are weighing it against the alternatives,
we keep <a href="../../compare/">honest comparison pages</a> that tell you where the
other apps beat us.</p>

<h2>Getting paid: deposits and terms for {t["name"].lower()}</h2>
{''.join(f'<p>{esc(p)}</p>' for p in t["payment"])}
<p>More on this in our guides to
<a href="../../blog/contractor-deposit-and-payment-terms.html">deposits and payment terms</a>
and <a href="../../blog/get-paid-faster-as-contractor.html">getting paid faster</a>.</p>

<h2>What to put on a {t["singular"]} invoice</h2>
<p>The difference between an invoice that gets paid and one that gets a phone call is
almost always detail. For {t["name"].lower()} specifically, make sure these are on it:</p>
<ul>{''.join(f'<li>{esc(x)}</li>' for x in t["checklist"])}</ul>

<h2>{t["name"]} FAQ</h2>
{faqs}

<h2>Related trades</h2>
<div class="grid">{sib_tiles}</div>

{S.cta(depth,
       f"Invoice your next {t['singular']} job from the truck",
       f"Free for {C.FREE_TIER_DOCS_PER_MONTH} documents a month. No card. iPhone.",
       "website", "trade", slug)}
</div>"""

    return write(f"for/{slug}/index.html", S.page(
        depth=depth, title=t["title"], desc=t["desc"], url_path=url,
        kicker=f"For {t['name'].lower()}", h1=t["h1"],
        standfirst=t["desc"], body=body, trades=TRADE_NAV,
        breadcrumb=S.breadcrumb_html(depth, [
            ("Home", "../../index.html"), ("Trades", "../"), (t["name"], None)]),
        jsonld=[
            S.breadcrumb_ld([("Home", "/"), ("Trades", "/for/"), (t["name"], url)]),
            S.faq_ld(t["faqs"]),
        ],
    ))


def build_trades_hub():
    depth = 1
    tiles = "".join(
        f'<a class="tile" href="{slug}/">{t["name"]}'
        f'<small>{esc(t["desc"][:88])}…</small></a>'
        for slug, t in TRADES.items())
    body = f"""<div class="prose">
<p>Every trade bills differently. A roofer's problem is funding five figures of
shingles before a nail goes in. A handyman's problem is that a $90 job is not worth
twenty minutes of paperwork. A drywall contractor's problem is that the customer has
never heard of a Level 4 finish and is about to argue about it.</p>
<p>So rather than one generic page, here is what we have learned about how each trade
quotes, invoices and gets paid — and where the money leaks out.</p>
<div class="grid">{tiles}</div>

<h2>What they all have in common</h2>
<p>Three things, and they are the reason Toolbelt exists. The work happens away from a
desk. The paperwork happens hours later, when you are tired and the details have gone
fuzzy. And the gap between those two facts is where money quietly disappears — in
under-billed parts, forgotten change orders, and invoices sent so late that the customer
has stopped feeling grateful.</p>
<p>Toolbelt closes that gap by making the document cheap to produce at the moment the job
ends: speak it, let the app write it up, send it before you drive away. It is
<a href="../templates/free-contractor-invoice-template/">free to try</a>, and there is a
<a href="../tools/contractor-hourly-rate-calculator/">rate calculator</a> if you are not
sure you are charging enough in the first place.</p>

{S.cta(depth, "Pick your trade, or just start invoicing",
       f"Free for {C.FREE_TIER_DOCS_PER_MONTH} documents a month. No card required.",
       "website", "trades-hub")}
</div>"""
    return write("for/index.html", S.page(
        depth=depth,
        title="Invoicing by Trade | Toolbelt",
        desc=("Invoice and quote guides for plumbers, electricians, HVAC, roofers, "
              "carpenters, painters, landscapers, handymen, drywall and GCs."),
        url_path="/for/", kicker="By trade",
        h1="Invoicing, by trade",
        standfirst="Ten trades, ten different billing problems. Find yours.",
        body=body, trades=TRADE_NAV,
        breadcrumb=S.breadcrumb_html(depth, [("Home", "../index.html"), ("Trades", None)]),
        jsonld=[S.breadcrumb_ld([("Home", "/"), ("Trades", "/for/")])],
    ))


# ----------------------------------------------------------- comparison pages --
def build_compare(key, c):
    depth = 2
    url = f"/compare/{c['slug']}/"

    if c["price_verified"] and c["plans"]:
        rows = "".join(
            f'<tr><td>{esc(n)}</td><td class="num">{esc(m)}</td>'
            f'<td class="num">{esc(y)}</td><td>{esc(note)}</td></tr>'
            for n, m, y, note in c["plans"])
        pricing = f"""<div class="tablewrap">
<table>
<thead><tr><th>{esc(c["name"])} plan</th><th class="num">Monthly</th>
<th class="num">Annual</th><th>Notes</th></tr></thead>
<tbody>{rows}</tbody>
</table>
</div>
<p class="small">Prices taken from <a href="{c['pricing_url']}" rel="nofollow noopener"
target="_blank">{esc(c["name"])}'s own pricing page</a> and verified on {VERIFIED_ON}.
Pricing changes — check before you decide.</p>"""
    else:
        plan_rows = ""
        if c["plans"]:
            plan_rows = "<div class=\"tablewrap\"><table><thead><tr><th>Plan</th>" \
                        "<th>What you get</th></tr></thead><tbody>" + "".join(
                f'<tr><td>{esc(n)}</td><td>{esc(note)}</td></tr>'
                for n, _m, _y, note in c["plans"]) + "</tbody></table></div>"
        pricing = f"""<div class="note">
<p><strong>We are not going to print a price for {esc(c["name"])}, and here is why.</strong></p>
<p>{esc(c["price_note"])}</p>
<p>Check it yourself: <a href="{c['pricing_url']}" rel="nofollow noopener"
target="_blank">{esc(c["name"])} pricing</a>. We would rather send you to the source than
publish a number we cannot stand behind — a comparison page with a wrong price in it is
worth less than no comparison page at all.</p>
</div>
{plan_rows}"""

    they = "".join(
        f'<div class="card win"><h3>{esc(h)}</h3><p>{esc(b)}</p></div>'
        for h, b in c["they_win"])
    we = "".join(
        f'<div class="card lose"><h3>{esc(h)}</h3><p>{esc(b)}</p></div>'
        for h, b in c["we_win"])

    faq_pairs = [
        (f"Is Toolbelt cheaper than {c['name']}?",
         (f"Toolbelt is ${C.PRICE_MONTHLY}/month or ${C.PRICE_YEARLY}/year for everything, "
          f"with a free tier of {C.FREE_TIER_DOCS_PER_MONTH} documents a month. "
          + ("Compare that against the plan table above — but check their page before you "
             "decide, because prices move."
             if c["price_verified"] else
             f"We could not verify {c['name']}'s current pricing from their own site, so we "
             f"are not going to claim we are cheaper without checking. Their pricing page is "
             f"linked above."))),
        (f"Can I use Toolbelt if I'm on Android?",
         "No. Toolbelt is iPhone only. If your phone is an Android, "
         f"{c['name']} covers you and we do not — that is the end of the decision, and no "
         "feature table changes it."),
        (f"Does {c['name']} have voice input or AI descriptions?",
         f"Not as of {VERIFIED_ON}, based on their published feature set. This is the "
         "clearest functional difference between the two products: with Toolbelt you speak "
         "the work and it gets written up as line items."),
        ("Do I have to migrate my old invoices?",
         "No, and you generally should not bother trying. Invoices you have already sent "
         "live in your email, your accounting and your customers' inboxes — they are valid "
         "documents wherever the app that made them ends up. Set up your business details "
         "and your common line items, and start with your next job."),
    ]
    cmp_faqs = "".join(
        f'<p class="faq-q">{esc(q)}</p><p>{esc(a)}</p>' for q, a in faq_pairs)

    body = f"""<div class="prose">
<div class="note">
<p><strong>How we write these.</strong> Every comparison page on this site names what the
other product does better, in its own section, first. Not as a courtesy — because a
comparison page where the competitor loses every round is a page no one believes, and
because you are going to find out anyway the moment you download the thing. Prices are
taken from the competitor's own pricing page and stamped with the date we checked them.</p>
</div>

<h2>What {esc(c["name"])} does better than Toolbelt</h2>
{they}

<h2>What Toolbelt does better than {esc(c["name"])}</h2>
{we}

<h2>{esc(c["name"])} pricing</h2>
{pricing}

<h2>Toolbelt pricing</h2>
<div class="tablewrap">
<table>
<thead><tr><th>Toolbelt plan</th><th class="num">Price</th><th>What you get</th></tr></thead>
<tbody>
<tr><td>Free</td><td class="num">$0</td><td>{C.FREE_TIER_DOCS_PER_MONTH} invoices or quotes
per month, every feature on, no card required</td></tr>
<tr><td>Monthly</td><td class="num">${C.PRICE_MONTHLY}/mo</td><td>Unlimited invoices and
quotes, voice input, AI descriptions, offline, custom PDF templates</td></tr>
<tr><td>Yearly</td><td class="num">${C.PRICE_YEARLY}/yr</td><td>Same as monthly, cheaper
per month</td></tr>
</tbody>
</table>
</div>
<p>Platforms: <strong>iPhone only</strong>. {esc(c["name"])} runs on {esc(c["platforms"])}.
That is a real gap and it is the first thing on this page you should weigh — if you are on
Android, this decision is already made for you.</p>

<h2>Feature by feature</h2>
<div class="tablewrap">
<table>
<thead><tr><th>&nbsp;</th><th>Toolbelt</th><th>{esc(c["name"])}</th></tr></thead>
<tbody>
<tr><td>Platforms</td><td>iPhone only</td><td>{esc(c["platforms"])}</td></tr>
<tr><td>Free tier</td><td>{C.FREE_TIER_DOCS_PER_MONTH} documents/month, forever, all features</td>
<td>{esc(str(c["free_plan"])) if c["free_plan"] else "None"}</td></tr>
<tr><td>Trial</td><td>Not needed — the free tier is permanent</td><td>{esc(c["trial"])}</td></tr>
<tr><td>Voice input</td><td>Yes</td><td>No</td></tr>
<tr><td>AI-written descriptions</td><td>Yes</td><td>No</td></tr>
<tr><td>Works fully offline</td><td>Yes</td><td>Limited or no</td></tr>
<tr><td>Paid price</td><td>${C.PRICE_MONTHLY}/mo or ${C.PRICE_YEARLY}/yr, one tier</td>
<td>{"See table above" if c["price_verified"] else "Not published without a currency or a signup — see above"}</td></tr>
</tbody>
</table>
</div>
<p>The "No" rows above are statements about {esc(c["name"])}'s published feature set as of
{VERIFIED_ON}. If they ship voice input tomorrow, this page is wrong until we update it —
tell us and we will.</p>

<h2>What neither of us does well</h2>
<p>Worth saying plainly, because every comparison page on the internet pretends its two
subjects cover the whole world between them. Neither Toolbelt nor {esc(c["name"])} is a
substitute for an accountant. Neither will chase a customer who has decided not to pay you.
And neither one fixes a pricing problem — if your rates are too low, better invoices will
just help you go broke more efficiently. If that is the real issue, start with our
<a href="../../tools/contractor-hourly-rate-calculator/">hourly rate calculator</a> instead of
either app.</p>

<h2>Should you switch — and how?</h2>
{''.join(f'<p>{esc(p)}</p>' for p in c["switching"])}

<h2>The honest verdict</h2>
<p>{esc(c["verdict"])}</p>

<h2>Common questions</h2>
{cmp_faqs}

<h2>Other comparisons</h2>
<div class="grid">{"".join(
    f'<a class="tile" href="../{o["slug"]}/">Toolbelt vs {esc(o["name"])}'
    f'<small>{esc(o["desc"][:78])}…</small></a>'
    for k, o in COMPETITORS.items() if k != key)}</div>

{S.cta(depth, "Try Toolbelt free",
       f"{C.FREE_TIER_DOCS_PER_MONTH} documents a month, free, forever. No card required.",
       "website", "compare", key)}
</div>"""

    return write(f"compare/{c['slug']}/index.html", S.page(
        depth=depth, title=c["title"], desc=c["desc"], url_path=url,
        kicker="Comparison", h1=f"Toolbelt vs {c['name']}",
        standfirst=c["desc"], body=body, trades=TRADE_NAV,
        breadcrumb=S.breadcrumb_html(depth, [
            ("Home", "../../index.html"), ("Compare", "../"),
            (f"vs {c['name']}", None)]),
        jsonld=[S.breadcrumb_ld([("Home", "/"), ("Compare", "/compare/"),
                                 (f"Toolbelt vs {c['name']}", url)]),
                S.faq_ld(faq_pairs)],
    ))


def build_compare_hub():
    depth = 1
    tiles = "".join(
        f'<a class="tile" href="{c["slug"]}/">Toolbelt vs {esc(c["name"])}'
        f'<small>{esc(c["desc"][:84])}…</small></a>'
        for c in COMPETITORS.values())
    body = f"""<div class="prose">
<p>There are a lot of invoicing apps. Some of them are better than Toolbelt at things that
might matter more to you than the things we are good at — and we would rather tell you that
here than have you find out after you have paid us.</p>
<p>So each of these pages opens with what the other product does better. Prices come from
the competitor's own pricing page, with the date we checked. Where a competitor makes their
pricing hard to verify — and three of the five here do — we say so and link you to them
rather than printing a number we would have to guess at.</p>
<div class="grid">{tiles}</div>

<h2>The short version</h2>
<p>Toolbelt is an <strong>iPhone invoicing app for one- and two-person trade businesses</strong>.
It is fast on a job site, it works with no signal, you can talk to it instead of typing, and
it costs ${C.PRICE_MONTHLY} a month or ${C.PRICE_YEARLY} a year with a genuinely free tier.</p>
<p>It is <strong>not</strong> field-service management. It does not schedule your crew, route
your vans, or sync to your accounting. If you need those, Jobber does them properly and we
will happily point you at
<a href="toolbelt-vs-jobber/">our Jobber page</a>, which says exactly that. And if you are on
Android, none of this applies — we do not have an Android app, and no comparison table is
going to change that.</p>

{S.cta(depth, "Or just try it and see",
       f"Free for {C.FREE_TIER_DOCS_PER_MONTH} documents a month. No card required.",
       "website", "compare-hub")}
</div>"""
    return write("compare/index.html", S.page(
        depth=depth,
        title="Toolbelt vs the Alternatives | Honest Comparisons",
        desc=("Honest comparisons of Toolbelt against Joist, Jobber, QuickBooks, Invoice "
              "Simple and Invoice2go — including what they do better than us."),
        url_path="/compare/", kicker="Comparisons",
        h1="Toolbelt vs the alternatives",
        standfirst="Including, in every case, what they do better than us.",
        body=body, trades=TRADE_NAV,
        breadcrumb=S.breadcrumb_html(depth, [("Home", "../index.html"), ("Compare", None)]),
        jsonld=[S.breadcrumb_ld([("Home", "/"), ("Compare", "/compare/")])],
    ))


def main():
    out = []
    out.append(build_trades_hub())
    for slug, t in TRADES.items():
        out.append(build_trade(slug, t))
    out.append(build_compare_hub())
    for key, c in COMPETITORS.items():
        out.append(build_compare(key, c))

    print(f"{'PAGE':<52} WORDS")
    thin = []
    for path, words in out:
        flag = ""
        if words < 900 and not path.endswith(("for/index.html", "compare/index.html")):
            flag = "  ← THIN (<900)"
            thin.append(path)
        print(f"  {path:<50} {words:>5}{flag}")
    if thin:
        print(f"\n⚠ {len(thin)} page(s) under 900 words. A thin page is a doorway page.")
    else:
        print("\nAll landing pages 900+ words.")


if __name__ == "__main__":
    main()
