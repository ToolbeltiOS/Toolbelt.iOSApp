#!/usr/bin/env python3
"""
Technical SEO audit. Crawls every HTML file in the repo and prints the table.

    python3 scripts/seo_audit.py            # human table
    python3 scripts/seo_audit.py --json     # machine-readable

Read-only: it reports, it never edits. Re-run it after any change to see what
moved. Uses only the stdlib, so it works in CI with no install step.
"""
import argparse
import html.parser
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "scripts"}


class Page(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = None
        self._in_title = False
        self.meta_desc = None
        self.canonical = None
        self.h1s = []
        self._in_h1 = False
        self._h1_buf = []
        self.og = set()
        self.tw = set()
        self.imgs = []          # (src, alt-or-None)
        self.links = []         # href
        self.jsonld = []        # raw strings
        self._in_ld = False
        self._ld_buf = []
        self.text = []
        self._in_skip = 0
        self.videos = []
        self.lazy_imgs = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            name = (a.get("name") or "").lower()
            prop = (a.get("property") or "").lower()
            if name == "description":
                self.meta_desc = a.get("content", "")
            if prop.startswith("og:"):
                self.og.add(prop)
            if name.startswith("twitter:"):
                self.tw.add(name)
            if prop.startswith("twitter:"):   # some sites use property= for twitter
                self.tw.add(prop)
        elif tag == "link" and (a.get("rel") or "").lower() in ("canonical", "['canonical']"):
            self.canonical = a.get("href")
        elif tag == "link" and "canonical" in str(a.get("rel", "")).lower():
            self.canonical = a.get("href")
        elif tag == "h1":
            self._in_h1 = True
            self._h1_buf = []
        elif tag == "img":
            self.imgs.append((a.get("src", ""), a.get("alt")))
            if (a.get("loading") or "").lower() == "lazy":
                self.lazy_imgs += 1
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "script" and (a.get("type") or "").lower() == "application/ld+json":
            self._in_ld = True
            self._ld_buf = []
        elif tag in ("script", "style"):
            self._in_skip += 1
        elif tag == "video":
            self.videos.append(a)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "h1":
            self._in_h1 = False
            self.h1s.append("".join(self._h1_buf).strip())
        elif tag == "script" and self._in_ld:
            self._in_ld = False
            self.jsonld.append("".join(self._ld_buf))
        elif tag in ("script", "style") and self._in_skip:
            self._in_skip -= 1

    def handle_data(self, d):
        if self._in_title:
            self.title = (self.title or "") + d
        if self._in_h1:
            self._h1_buf.append(d)
        if self._in_ld:
            self._ld_buf.append(d)
        if not self._in_skip and not self._in_ld:
            self.text.append(d)


def word_count(p):
    return len(re.sub(r"\s+", " ", " ".join(p.text)).split())


def crawl():
    pages = {}
    for dirpath, dirnames, files in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in files:
            if not f.endswith(".html"):
                continue
            full = os.path.join(dirpath, f)
            rel = os.path.relpath(full, ROOT)
            p = Page()
            p.feed(open(full, encoding="utf-8", errors="ignore").read())
            pages[rel] = p
    return pages


def is_internal(href):
    return not re.match(r"^(https?:|mailto:|tel:|#|javascript:)", href.strip(), re.I)


def normalize(src, page_rel):
    """Resolve an internal href to a repo-relative html path, best effort."""
    h = src.split("#")[0].split("?")[0].strip()
    if not h:
        return None
    base = os.path.dirname(page_rel)
    path = os.path.normpath(os.path.join(base, h)) if not h.startswith("/") \
        else h.lstrip("/")
    if path in ("", "."):
        path = "index.html"
    if path.endswith("/"):
        path += "index.html"
    if not path.endswith(".html"):
        cand = path + "/index.html"
        if os.path.exists(os.path.join(ROOT, cand)):
            return cand
        if os.path.exists(os.path.join(ROOT, path + ".html")):
            return path + ".html"
        return path
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    pages = crawl()
    inbound = {k: 0 for k in pages}
    rows = []
    for rel, p in sorted(pages.items()):
        out_int = 0
        for href in p.links:
            if is_internal(href):
                out_int += 1
                tgt = normalize(href, rel)
                if tgt in inbound:
                    inbound[tgt] += 1
        rows.append({"page": rel, "p": p, "out_internal": out_int})

    data = []
    for r in rows:
        p, rel = r["p"], r["page"]
        title = (p.title or "").strip()
        desc = (p.meta_desc or "").strip()
        missing_alt = [s for s, a in p.imgs if a is None or not a.strip()]
        schemas = []
        for raw in p.jsonld:
            try:
                obj = json.loads(raw)
                for o in (obj if isinstance(obj, list) else [obj]):
                    t = o.get("@type")
                    schemas.extend(t if isinstance(t, list) else [t])
            except Exception:
                schemas.append("INVALID-JSON")
        data.append({
            "page": rel,
            "title": title, "title_len": len(title),
            "meta_desc": desc, "desc_len": len(desc),
            "canonical": p.canonical,
            "h1_count": len(p.h1s), "h1": p.h1s[0] if p.h1s else None,
            "words": word_count(p),
            "links_in": inbound[rel], "links_out": r["out_internal"],
            "images": len(p.imgs), "images_missing_alt": len(missing_alt),
            "missing_alt_srcs": missing_alt,
            "lazy_images": p.lazy_imgs,
            "og": bool(p.og), "og_tags": sorted(p.og),
            "twitter": bool(p.tw), "twitter_tags": sorted(p.tw),
            "jsonld": schemas,
            "videos": p.videos,
        })

    if args.json:
        print(json.dumps(data, indent=2))
        return

    def flag(cond, ok="✓", bad="✗"):
        return ok if cond else bad

    print(f"\n{len(data)} HTML pages\n")
    hdr = (f"{'PAGE':<42} {'TITLE':>5} {'DESC':>5} {'CAN':>4} {'H1':>3} "
           f"{'WORDS':>6} {'IN':>3} {'OUT':>4} {'IMG':>4} {'NOALT':>6} {'OG':>3} {'TW':>3} SCHEMA")
    print(hdr)
    print("-" * len(hdr))
    for d in data:
        print(f"{d['page']:<42} "
              f"{d['title_len']:>5} {d['desc_len']:>5} "
              f"{flag(d['canonical']):>4} {d['h1_count']:>3} "
              f"{d['words']:>6} {d['links_in']:>3} {d['links_out']:>4} "
              f"{d['images']:>4} {d['images_missing_alt']:>6} "
              f"{flag(d['og']):>3} {flag(d['twitter']):>3} "
              f"{','.join(s for s in d['jsonld'] if s) or '—'}")

    print("\nISSUES")
    issues = []
    for d in data:
        pg = d["page"]
        if not d["title"]:
            issues.append(f"{pg}: no <title>")
        elif d["title_len"] > 60:
            issues.append(f"{pg}: title {d['title_len']} chars (>60, truncates in SERP)")
        if not d["meta_desc"]:
            issues.append(f"{pg}: no meta description")
        elif d["desc_len"] > 155:
            issues.append(f"{pg}: meta description {d['desc_len']} chars (>155)")
        if not d["canonical"]:
            issues.append(f"{pg}: no canonical")
        if d["h1_count"] != 1:
            issues.append(f"{pg}: {d['h1_count']} H1s (must be exactly 1)")
        if not d["og"]:
            issues.append(f"{pg}: no Open Graph tags")
        if not d["twitter"]:
            issues.append(f"{pg}: no Twitter Card tags")
        if d["images_missing_alt"]:
            issues.append(f"{pg}: {d['images_missing_alt']} image(s) missing alt")
        if not [s for s in d["jsonld"] if s]:
            issues.append(f"{pg}: no JSON-LD structured data")
        if d["links_in"] == 0 and d["page"] != "index.html":
            issues.append(f"{pg}: ORPHAN — no internal links point to it")
    for i in issues:
        print(f"  • {i}")
    print(f"\n{len(issues)} issues")

    # asset audit
    print("\nASSETS")
    for f in sorted(os.listdir(ROOT)):
        full = os.path.join(ROOT, f)
        if not os.path.isfile(full):
            continue
        ext = os.path.splitext(f)[1].lower()
        if ext in (".jpg", ".jpeg", ".png", ".webp", ".mp4", ".mov", ".gif"):
            size = os.path.getsize(full)
            note = ""
            if ext == ".mp4" and size > 2 * 1024 * 1024:
                note = "  ← >2MB, must compress"
            if re.match(r"^[0-9]+\.|^[0-9A-F]{8}-", f, re.I):
                note += "  ← non-descriptive filename"
            print(f"  {f:<46} {size/1024/1024:>7.2f} MB{note}")
    for name in ("robots.txt", "sitemap.xml"):
        print(f"  {name:<46} {'PRESENT' if os.path.exists(os.path.join(ROOT, name)) else 'MISSING ✗'}")


if __name__ == "__main__":
    sys.exit(main())
