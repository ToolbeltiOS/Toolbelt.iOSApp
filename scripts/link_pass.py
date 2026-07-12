#!/usr/bin/env python3
"""
The internal-linking pass over the HAND-WRITTEN pages.

    python3 scripts/link_pass.py --dry-run
    python3 scripts/link_pass.py

The generated pages (trades, comparisons, templates, tools, new blog posts) already
carry the full nav and footer, because they come out of scripts/shell.py. This script
brings the older hand-written pages — the homepage, the five original blog posts and
the blog index — up to the same standard:

  * nav gains Trades / Compare / Templates
  * footer gains the trades hub and the free tools
  * each original blog post gets a contextual link to one TRADE page and one
    TEMPLATE/TOOL page, placed inside the relevant paragraph rather than dumped in a
    "related posts" box at the bottom, which nobody clicks
  * the blog index gets cards for the three new posts
  * the "Jan 2025" date shown on the blog cards is corrected to 2026 — the same
    year error that was in the schema

Idempotent: every insertion checks for itself first.
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import seo_config as C  # noqa: E402

# post -> (paragraph-anchor substring, contextual sentence to append to it)
# The anchor is a phrase already in the post, so the link lands somewhere it makes
# sense rather than being bolted onto the end.
BLOG_LINKS = {
    "blog/get-paid-faster-as-contractor.html": (
        "<p>",
        ' If you want the mechanics of the document itself, our '
        '<a href="../templates/free-contractor-invoice-template/">free contractor invoice '
        'template</a> lays out every field, and the '
        '<a href="../for/handymen/">guide for handymen</a> covers why fast invoicing '
        'matters most when the jobs are small and numerous.'),
    "blog/invoicing-mistakes-contractors-make.html": (
        "<p>",
        ' Most of these disappear if you start from a document that already has the right '
        'fields on it — take our '
        '<a href="../templates/free-contractor-invoice-template/">free invoice template</a>, '
        'or read how <a href="../for/plumbers/">plumbers</a> handle parts and call-out fees.'),
    "blog/quote-vs-invoice-when-to-use.html": (
        "<p>",
        ' Quoting is where <a href="../for/electricians/">electricians</a> win or lose most '
        'of their work, and our '
        '<a href="../templates/free-contractor-invoice-template/">free template</a> includes '
        'both document types.'),
    "blog/professional-invoice-template-guide.html": (
        "<p>",
        ' You can skip straight to the finished article: our '
        '<a href="../templates/free-contractor-invoice-template/">free contractor invoice '
        'template</a> is available in PDF and Word, with versions for ten trades including '
        '<a href="../for/roofers/">roofers</a>.'),
    "blog/contractor-tax-deductions-guide.html": (
        "<p>",
        ' Deductions only work if your records do, which starts with itemised invoices — see '
        'our <a href="../templates/free-contractor-invoice-template/">free template</a>. And '
        'if you are not sure your rates cover your overhead in the first place, the '
        '<a href="../tools/contractor-hourly-rate-calculator/">hourly rate calculator</a> '
        'will tell you.'),
}

NEW_CARDS = """
            <!-- New: written 2026-07 -->
            <a href="how-to-write-an-invoice-as-a-contractor.html" class="blog-card reveal">
                <div class="blog-card-image img-warning">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
                </div>
                <div class="blog-card-content">
                    <span class="blog-card-category">Invoicing</span>
                    <h2>How to Write an Invoice as a Contractor</h2>
                    <p>Every field, why it is there, and exactly what it costs you when it is missing. The field guide to an invoice that gets paid without a phone call.</p>
                    <div class="blog-card-meta">
                        <span>Jul 2026</span>
                        <span>7 min read</span>
                        <span class="read-more">Read More &rarr;</span>
                    </div>
                </div>
            </a>

            <a href="contractor-deposit-and-payment-terms.html" class="blog-card reveal">
                <div class="blog-card-image img-money">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg>
                </div>
                <div class="blog-card-content">
                    <span class="blog-card-category">Getting paid</span>
                    <h2>Contractor Deposits &amp; Payment Terms</h2>
                    <p>If you do the work first and get paid later, you are a lender. How much deposit to ask for, when, and the terms that stop you financing someone else's project.</p>
                    <div class="blog-card-meta">
                        <span>Jul 2026</span>
                        <span>7 min read</span>
                        <span class="read-more">Read More &rarr;</span>
                    </div>
                </div>
            </a>

            <a href="quote-follow-up-templates-that-win-jobs.html" class="blog-card reveal">
                <div class="blog-card-image img-warning">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                </div>
                <div class="blog-card-content">
                    <span class="blog-card-category">Winning work</span>
                    <h2>Quote Follow-Up Templates That Win Jobs</h2>
                    <p>Most quotes are lost to silence, not to price. Four messages to send, when to send them, and why the second one wins the most work.</p>
                    <div class="blog-card-meta">
                        <span>Jul 2026</span>
                        <span>8 min read</span>
                        <span class="read-more">Read More &rarr;</span>
                    </div>
                </div>
            </a>
"""


def add_nav_links(s, prefix):
    """Insert Trades / Compare / Templates into an existing .nav-links block."""
    if 'href="' + prefix + 'for/"' in s:
        return s, False
    m = re.search(r'(<div class="nav-links">)(.*?)(</div>)', s, re.S)
    if not m:
        return s, False
    new = (m.group(1)
           + f'\n                <a href="{prefix}for/">Trades</a>'
             f'\n                <a href="{prefix}compare/">Compare</a>'
             f'\n                <a href="{prefix}templates/free-contractor-invoice-template/">Templates</a>'
           + m.group(2) + m.group(3))
    return s[:m.start()] + new + s[m.end():], True


def add_footer_links(s, prefix):
    """Add the hub links to an existing .footer-links block.

    The presence check must look INSIDE the footer block, not at the whole page —
    add_nav_links() runs first and puts a Templates link in the nav, which made a
    page-wide check see it and skip the footer entirely.
    """
    m = re.search(r'(<div class="footer-links">)(.*?)(</div>)', s, re.S)
    if not m:
        return s, False
    if 'href="' + prefix + 'templates/free-contractor-invoice-template/"' in m.group(2):
        return s, False
    new = (m.group(1)
           + f'\n                    <a href="{prefix}for/">Trades</a>'
             f'\n                    <a href="{prefix}compare/">Compare</a>'
             f'\n                    <a href="{prefix}templates/free-contractor-invoice-template/">Free invoice template</a>'
             f'\n                    <a href="{prefix}tools/contractor-hourly-rate-calculator/">Rate calculator</a>'
           + m.group(2) + m.group(3))
    return s[:m.start()] + new + s[m.end():], True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    changed = []

    # ---- homepage
    p = os.path.join(ROOT, "index.html")
    s = orig = open(p, encoding="utf-8").read()
    s, n1 = add_nav_links(s, "")
    s, n2 = add_footer_links(s, "")
    s = s.replace("&copy; 2025 Toolbelt", "&copy; 2026 Toolbelt")
    s = s.replace("© 2025 Toolbelt", "© 2026 Toolbelt")
    if s != orig:
        changed.append(("index.html", f"nav={n1} footer={n2} copyright-year"))
        if not a.dry_run:
            open(p, "w", encoding="utf-8").write(s)

    # ---- blog index: new cards, nav/footer, wrong year on the cards
    p = os.path.join(ROOT, "blog", "index.html")
    s = orig = open(p, encoding="utf-8").read()
    s, n1 = add_nav_links(s, "../")
    s, n2 = add_footer_links(s, "../")
    s = s.replace(">Jan 2025<", ">Jan 2026<")     # same year error as the schema had
    s = s.replace("&copy; 2025 Toolbelt", "&copy; 2026 Toolbelt")
    added_cards = False
    if "how-to-write-an-invoice-as-a-contractor.html" not in s:
        m = re.search(r'<div class="blog-grid">', s)
        if m:
            s = s[:m.end()] + NEW_CARDS + s[m.end():]
            added_cards = True
    if s != orig:
        changed.append(("blog/index.html",
                        f"nav={n1} footer={n2} cards={added_cards} dates"))
        if not a.dry_run:
            open(p, "w", encoding="utf-8").write(s)

    # ---- the five original posts
    for rel, (anchor, sentence) in BLOG_LINKS.items():
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            continue
        s = orig = open(p, encoding="utf-8").read()
        s, n1 = add_nav_links(s, "../")
        s, n2 = add_footer_links(s, "../")
        s = s.replace("&copy; 2025 Toolbelt", "&copy; 2026 Toolbelt")

        linked = "/for/" in s or "../for/" in s
        if not linked:
            # Append the contextual sentence to the LAST paragraph before the CTA/footer,
            # which is where a reader who finished the piece actually is.
            paras = list(re.finditer(r"</p>", s))
            if paras:
                # pick the last </p> that sits inside the article body, not the footer
                cut = s.rfind("<footer")
                body_paras = [m for m in paras if cut == -1 or m.end() < cut]
                if body_paras:
                    last = body_paras[-1]
                    s = s[:last.start()] + sentence + s[last.start():]
                    linked = True
        if s != orig:
            changed.append((rel, f"nav={n1} footer={n2} contextual-link={linked}"))
            if not a.dry_run:
                open(p, "w", encoding="utf-8").write(s)

    for rel, what in changed:
        print(f"  {rel:<48} {what}")
    print(f"\n{len(changed)} file(s) {'would be ' if a.dry_run else ''}updated")


if __name__ == "__main__":
    main()
