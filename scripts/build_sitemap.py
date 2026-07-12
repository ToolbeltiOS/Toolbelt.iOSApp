#!/usr/bin/env python3
"""
Regenerates sitemap.xml and robots.txt by walking the repo.

    python3 scripts/build_sitemap.py

There is no build step on this site — it is hand-written static HTML on GitHub
Pages — so the sitemap cannot regenerate itself. Run this after adding or
removing any page. It walks the filesystem rather than reading a hand-kept list,
because a hand-kept list is a list that will eventually be wrong.

lastmod comes from git (the file's last commit date), not from the filesystem
mtime, which is meaningless after a fresh clone — every file would claim to have
been modified the day you cloned.

Pages carrying <meta name="robots" content="noindex"> are excluded: asking Google
to crawl a page you have told it to ignore is a contradiction it will hold
against you.
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo_config as C  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "scripts"}

# Priority by shape of URL, not hand-assigned per page. Homepage first, money
# pages next, legal boilerplate last.
def priority(url_path):
    if url_path == "/":
        return "1.0"
    if url_path.startswith(("/for/", "/compare/", "/templates/", "/tools/")):
        return "0.9"
    if url_path == "/blog/":
        return "0.8"
    if url_path.startswith("/blog/"):
        return "0.7"
    if url_path in ("/support.html",):
        return "0.5"
    return "0.3"


def changefreq(url_path):
    if url_path in ("/", "/blog/"):
        return "weekly"
    if url_path.startswith("/blog/"):
        return "yearly"
    return "monthly"


def git_lastmod(rel):
    try:
        d = subprocess.run(["git", "-C", ROOT, "log", "--format=%as", "-1", "--", rel],
                           capture_output=True, text=True, check=True).stdout.strip()
        return d or None
    except Exception:
        return None


def url_for(rel):
    """index.html -> /   |   blog/index.html -> /blog/   |   x.html -> /x.html"""
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel


def main():
    entries = []
    for dirpath, dirnames, files in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in sorted(files):
            if not f.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, f), ROOT)
            src = open(os.path.join(ROOT, rel), encoding="utf-8", errors="ignore").read()
            if re.search(r'<meta[^>]+name="robots"[^>]+content="[^"]*noindex', src, re.I):
                print(f"  skip (noindex): {rel}")
                continue
            path = url_for(rel)
            entries.append((path, git_lastmod(rel)))

    entries.sort(key=lambda e: (priority(e[0]) != "1.0", e[0]))

    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, lastmod in entries:
        out.append("  <url>")
        out.append(f"    <loc>{C.SITE_URL}{path}</loc>")
        if lastmod:
            out.append(f"    <lastmod>{lastmod}</lastmod>")
        out.append(f"    <changefreq>{changefreq(path)}</changefreq>")
        out.append(f"    <priority>{priority(path)}</priority>")
        out.append("  </url>")
    out.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(out) + "\n")
    print(f"wrote sitemap.xml — {len(entries)} URLs")

    robots = f"""# robots.txt for {C.SITE_URL}
User-agent: *
Allow: /

# Confirmation page — no search value, and indexing it would put a dead-end page
# in front of someone searching for the product.
Disallow: /thanks.html

Sitemap: {C.SITE_URL}/sitemap.xml
"""
    open(os.path.join(ROOT, "robots.txt"), "w").write(robots)
    print("wrote robots.txt")


if __name__ == "__main__":
    main()
