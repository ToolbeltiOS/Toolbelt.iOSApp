"""Toolbelt prohibited-claim scanner (rules.json loader).

ORIGIN: ported from ~/Desktop/safenest-web-reports/rules/harness.py. Kept the
rules.json-driven literal banned-phrase scan (load_rules + scan_prohibited).
DROPPED SafeNest's Swift-snapshot drift guard and its crime-domain categories
(verdict / jurisdiction / coverage) — Toolbelt's authority is brain/claims.md
(an owner-ratified doc), not pinned Swift source. Two small repos beat one
shared framework: this is a copy with a header, not an import.
"""
from __future__ import annotations

import json
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_RULES = _HERE / "rules.json"


def load_rules() -> dict:
    with open(_RULES, encoding="utf-8") as f:
        return json.load(f)


def scan_prohibited(text: str, rules: dict | None = None) -> list[tuple[str, str]]:
    """Returns [(kind, phrase)] for every literal banned phrase found. Empty = clean.

    Literal, lowercased substring match — the narrow, unambiguous half. The
    shape-aware half (superiority / invented-count / payment ASSERTIONS) lives in
    prose_gate.CLAIM_SHAPES, so bare vocabulary and ordinals ("Invoice #123",
    "Mistake #1") are not caught here either.
    """
    rules = rules or load_rules()
    pc = rules["prose_checker"]
    low = (text or "").lower()
    out: list[tuple[str, str]] = []
    for entry in pc.get("banned_phrases", []):
        if entry["pattern"] in low:
            out.append(("bannedClaim", entry["pattern"]))
    return out
