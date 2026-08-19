#!/usr/bin/env python3
"""IndexNow submitter for toolbelt.pro.

ORIGIN: ported from ~/Desktop/safenest-web-reports/tools/indexnow/submit.py
(SafeNest's IndexNow submitter). Logic is copied verbatim; only the host, key,
sitemap, and User-Agent are Toolbelt's. Two small repos beat one shared
framework — this is a copy with a header, not an import.

WHY THIS EXISTS: Google discovery on a young domain is weeks, not days, and there
is no API to hurry it (the Indexing API accepts only JobPosting and
BroadcastEvent; "Request Indexing" is a manual UI action). IndexNow is the lever
that IS available — Bing, Yandex, Seznam and Naver accept it, it needs no account
or verification beyond hosting the key file, and Bing's index is the route into
several AI answer surfaces.

  python3 submit.py --all              every URL in the live sitemap
  python3 submit.py URL [URL ...]      specific URLs
  python3 submit.py --all --dry-run    print what would be sent

THE KEY FILE MUST BE LIVE BEFORE SUBMITTING. IndexNow fetches
https://toolbelt.pro/<key>.txt and refuses the batch if it does not match. This
script verifies that itself rather than assuming it. Per the standing rule,
IndexNow pings run only AFTER liveness is verified — never chained to the push.
"""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, os, pathlib, sys, urllib.request, urllib.error, xml.etree.ElementTree as ET

HOST = "toolbelt.pro"
KEY = "1248e2aacfb9642e24087113d56658a3"
KEY_URL = f"https://{HOST}/{KEY}.txt"
SITEMAP = f"https://{HOST}/sitemap.xml"
ENDPOINT = "https://api.indexnow.org/indexnow"
BATCH = 10000   # protocol maximum


def _get(url: str, timeout: int = 20) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "toolbelt-indexnow/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def verify_key() -> bool:
    """The key file must be live and must contain exactly the key."""
    try:
        got = _get(KEY_URL).decode("utf-8", "replace").strip()
    except Exception as e:
        print(f"  key file UNREACHABLE at {KEY_URL}: {type(e).__name__}")
        return False
    if got != KEY:
        print(f"  key file CONTENT MISMATCH at {KEY_URL}: got {got[:24]!r}")
        return False
    print(f"  key file verified live at {KEY_URL}")
    return True


def sitemap_urls() -> list[str]:
    root = ET.fromstring(_get(SITEMAP))
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [e.text.strip() for e in root.findall(".//s:url/s:loc", ns) if e.text]


LOG_PATH = os.environ.get("INDEXNOW_LOG", str(pathlib.Path(__file__).resolve().parent
                                              / "submissions.jsonl"))


def _batch_id(chunk: list[str], stamp: str) -> str:
    """Stable id for one POST: content-addressed, so re-running the same batch at
    a different time is visibly a different submission of the same URL set."""
    h = hashlib.sha256(("\n".join(chunk)).encode()).hexdigest()[:12]
    return f"{stamp[:10].replace('-', '')}-{h}"


def _log(records: list[dict]) -> None:
    """Append-only submission ledger — URL, timestamp, batch id, outcome.

    JSONL and append-only on purpose. A submission log that can be rewritten is
    not evidence, and the whole point is that a later verification can trust what
    was actually submitted rather than using the current sitemap as a proxy for a
    past submission (which mis-states the baseline the moment the sitemap changes).
    Refusals are logged too — a successes-only ledger would let a verification
    pass conclude "submitted, never indexed" about URLs never actually accepted.
    """
    with open(LOG_PATH, "a", encoding="utf-8") as fh:
        for r in records:
            fh.write(json.dumps(r, sort_keys=True) + "\n")


def submit(urls: list[str], dry: bool = False) -> int:
    if not urls:
        print("  nothing to submit"); return 0
    sent = 0
    for i in range(0, len(urls), BATCH):
        chunk = urls[i:i + BATCH]
        stamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
        bid = _batch_id(chunk, stamp)
        payload = {"host": HOST, "key": KEY, "keyLocation": KEY_URL, "urlList": chunk}
        if dry:
            print(f"  DRY RUN: would submit {len(chunk)} URL(s) as batch {bid}; "
                  f"first 3: {chunk[:3]}")
            sent += len(chunk); continue
        req = urllib.request.Request(
            ENDPOINT, data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json; charset=utf-8",
                     "User-Agent": "toolbelt-indexnow/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                # 200 accepted · 202 accepted, key validation pending
                print(f"  submitted {len(chunk)} URL(s) -> HTTP {r.status}  batch={bid}")
                _log([{"url": u, "submitted_at": stamp, "batch_id": bid,
                       "http_status": r.status, "outcome": "accepted"} for u in chunk])
                sent += len(chunk)
        except urllib.error.HTTPError as e:
            # 400 bad request · 403 key invalid · 422 URL/host mismatch · 429 too many
            body = e.read()[:160]
            print(f"  REFUSED {len(chunk)} URL(s) -> HTTP {e.code}: {body!r}  batch={bid}")
            _log([{"url": u, "submitted_at": stamp, "batch_id": bid,
                   "http_status": e.code, "outcome": "refused"} for u in chunk])
            return sent
    return sent


def main() -> int:
    ap = argparse.ArgumentParser(description="IndexNow submitter for toolbelt.pro")
    ap.add_argument("urls", nargs="*")
    ap.add_argument("--all", action="store_true", help="submit every URL in the live sitemap")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if not verify_key():
        print("  ABORTING — IndexNow would refuse the batch and we would not know why.")
        return 1
    urls = sitemap_urls() if a.all else a.urls
    if not urls:
        print("  no URLs given (use --all or pass URLs)"); return 2
    print(f"  {len(urls)} URL(s) to submit")
    n = submit(urls, dry=a.dry_run)
    print(f"  done: {n} URL(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
