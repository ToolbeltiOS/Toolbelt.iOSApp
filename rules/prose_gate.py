"""THE Toolbelt prose gate. One law, one enforcement.

ORIGIN: ported from ~/Desktop/safenest-web-reports/rules/prose_gate.py. Same
architecture — two composed sources (rules.json literal banned phrases +
claim-SHAPE regexes), scan() returning tagged findings, scan_html() stripping
scripts/styles/tags, and a runnable self_test() with ALLOWED/FORBIDDEN fixtures
and an exit-code contract. SafeNest's crime rules, its SUBCITY_CLAIM regex, and
the Swift-snapshot / display_place pieces are REPLACED with Toolbelt's own claim
set, derived from brain/claims.md (owner-ratified 2026-08-18).

THE DISTINCTION THAT MATTERS — we forbid CLAIMING superiority, inventing social
proof, and asserting unverified features, NOT the vocabulary:

    ALLOWED  "Invoice #123 is now overdue."            (an invoice number)
    ALLOWED  "Mistake #1: not itemizing your work."    (an ordinal)
    ALLOWED  "Invoice2go has card processing built in." (describing a competitor)
    ALLOWED  "Toolbelt is iPhone and iPad only."        (the true platform)
    FAILS    "The #1 invoice app for contractors."
    FAILS    "Trusted by 10,000 contractors."
    FAILS    "Toolbelt accepts card payments."

The shapes match ASSERTION, and the ordinal / competitor / true-platform forms
are pinned by regression tests in self_test(). A gate that failed the ALLOWED
set would teach the next person to delete honest copy to get a green build.

  python3 rules/prose_gate.py        -> self_test  (exit 1 on any leak/false-positive)
  python3 rules/prose_gate.py --all  -> scan every built .html; exit 1 on any finding
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))

from rules import harness  # noqa: E402

# Claim SHAPES — each ASSERTS something; none fires on bare vocabulary, an
# ordinal ("#1" / "no. 1" not followed by a product word), or an invoice number.
CLAIM_SHAPES = [
    ("rankingClaim", re.compile(r"#1\s+(?:invoice|app|rated|contractor|choice|pick)", re.I)),
    ("rankingClaim", re.compile(r"\bthe\s+#1\b", re.I)),
    ("rankingClaim", re.compile(r"\bno\.?\s*1\s+(?:invoice|app|rated|choice|contractor)\b", re.I)),
    ("rankingClaim", re.compile(r"\bnumber\s+one\s+(?:invoice|app|choice|rated|contractor)\b", re.I)),
    ("inventedCount", re.compile(
        r"\b(?:trusted|used|loved)\s+by\s+(?:over\s+)?[\d,]+\+?\s+"
        r"(?:contractors|tradespeople|trades|users|pros|professionals|businesses|customers)\b", re.I)),
    ("inventedCount", re.compile(
        r"\bjoin\s+(?:over\s+)?[\d,]+\+?\s+(?:contractors|tradespeople|users|pros)\b", re.I)),
    ("inventedCount", re.compile(
        r"\b(?:thousands|millions|hundreds\s+of\s+thousands)\s+of\s+"
        r"(?:contractors|tradespeople|users|downloads|pros)\b", re.I)),
    ("inventedReview", re.compile(r"\b[\d,]+\+?\s+(?:5[- ]star|five[- ]star)\s+reviews?\b", re.I)),
    ("inventedReview", re.compile(r"\b(?:rated|scored)\s+[\d.]+\s*(?:stars?|/\s*5|out\s+of\s+5)\b", re.I)),
    ("unverifiedPayment", re.compile(
        r"\btoolbelt\s+(?:can\s+|now\s+)?(?:accept|process|take|collect)s?\s+"
        r"(?:card\s+|online\s+)?payments?\b", re.I)),
]


def scan(text: str) -> list[str]:
    """Every violation in `text`. Empty list = clean. Findings are tagged strings
    so the two sources are distinguishable in a log:
        "bannedClaim:top-rated"          <- rules.json literal list
        "rankingClaim:'#1 invoice'"      <- assertion shape
    """
    out = [f"{kind}:{phrase}"
           for kind, phrase in harness.scan_prohibited(text, harness.load_rules())]
    for kind, rx in CLAIM_SHAPES:
        out += [f"{kind}:{m.group(0).strip()!r}" for m in rx.finditer(text or "")]
    return out


def scan_html(html: str) -> list[str]:
    """Same gate over rendered page text. Scripts and styles are stripped first so
    a JSON-LD block or a CSS rule cannot trip a prose check."""
    import html as _html
    t = re.sub(r"<script.*?</script>", " ", html or "", flags=re.S | re.I)
    t = re.sub(r"<style.*?</style>", " ", t, flags=re.S | re.I)
    return scan(_html.unescape(re.sub(r"<[^>]+>", " ", t)))


# ── regression tests, runnable: python3 rules/prose_gate.py ─────────────────

ALLOWED = [
    "Invoice #123 is now overdue — please let me know if you have questions.",
    "Mistake #1: Not itemizing your work.",
    "Late payments are the biggest cash flow killer for contractors.",
    "Toolbelt is iPhone and iPad only. If your crew is on Android, Joist covers you.",
    "Invoice2go has card payment acceptance built in; Toolbelt does not.",
    "How to get paid faster as a contractor.",
    "Create up to 3 documents per month, with a free tier of 3 documents a month.",
    "Describe the job in your words and AI turns it into professional invoice wording.",
]

FORBIDDEN = [
    "The #1 invoice app for contractors.",
    "Toolbelt is the #1 choice for contractors.",
    "The number one invoice app for the trades.",
    "Top-rated by contractors everywhere.",
    "The most popular invoice app for contractors.",
    "Trusted by 10,000 contractors.",
    "Join thousands of contractors on Toolbelt.",
    "Rated 4.9 stars by users.",
    "Contractors are switching to Toolbelt.",
    "Get paid in the app with built-in card payments.",
    "Toolbelt accepts card payments.",
    "Toolbelt is iPhone only.",
]


def self_test() -> int:
    bad = 0
    print("ALLOWED (honest copy — must PASS):")
    for t in ALLOWED:
        hits = scan(t)
        if hits:
            bad += 1
            print(f"  FAIL {t[:60]!r}\n       -> {hits}")
        else:
            print(f"  ok   {t[:60]!r}")
    print("\nFORBIDDEN (a claim we cannot make — must FAIL):")
    for t in FORBIDDEN:
        hits = scan(t)
        if not hits:
            bad += 1
            print(f"  LEAK {t[:60]!r}")
        else:
            print(f"  ok   {t[:60]!r}  -> {hits[0]}")
    print(f"\n{'ALL PASS' if not bad else str(bad) + ' PROBLEM(S)'}")
    return 1 if bad else 0


def scan_all() -> int:
    """Lint every built page. The enforcement surface: run before a push."""
    root = _HERE.parent
    bad = 0
    for p in sorted(root.rglob("*.html")):
        if ".git" in p.parts:
            continue
        hits = scan_html(p.read_text(encoding="utf-8", errors="replace"))
        if hits:
            bad += 1
            print(f"  {p.relative_to(root)}")
            for h in hits:
                print(f"      {h}")
    print(f"\n{'CLEAN — no prohibited claims in any page' if not bad else str(bad) + ' page(s) with findings'}")
    return 1 if bad else 0


if __name__ == "__main__":
    if "--all" in sys.argv:
        raise SystemExit(scan_all())
    raise SystemExit(self_test())
