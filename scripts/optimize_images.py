#!/usr/bin/env python3
"""
Rename the image assets to descriptive names, resize them, and emit WebP with a
JPEG/PNG fallback. Rewrites every reference in the HTML.

    python3 scripts/optimize_images.py --dry-run
    python3 scripts/optimize_images.py

Idempotent: running it twice is a no-op.

WHY THE RENAME MATTERS. `3.jpg` and `B08867EB-3D4C-47F4-ADA9-14E851617D94.png`
tell Google nothing. The filename is a real (if minor) ranking signal for image
search, and image search is a live traffic source for "what does a contractor
invoice look like" queries. `contractor-invoice-voice-input.jpg` says what the
picture is; a UUID says nothing at all.

WHY THE RESIZE MATTERS MORE. The screenshots ship at ~800KB each and are
displayed a few hundred pixels wide. That is roughly 6MB of images on a page
aimed at contractors standing in a basement on one bar of signal. Resizing to the
width they are actually displayed at is the single biggest win available here.
"""
import argparse
import os
import re
import shutil
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("ERROR: Pillow is required.  pip3 install Pillow")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# old filename -> (new basename, alt text)
#
# The alt text is written to describe the screenshot AND carry the phrase a human
# would plausibly search for. It is not keyword stuffing: each one is a true
# sentence about what is in the image. Note that the old alt text was not just
# vague, it was WRONG — 6.jpg was labelled "Quotes" in one carousel and
# "Dashboard" in the other.
RENAMES = {
    "B08867EB-3D4C-47F4-ADA9-14E851617D94.png": (
        "toolbelt-logo.png",
        "Toolbelt invoice app logo"),
    "3.jpg": ("contractor-invoice-voice-input.jpg",
              "Contractor dictating an invoice line item by voice in the Toolbelt app"),
    "4.jpg": ("contractor-invoice-job-photos.jpg",
              "Job site photos attached to a contractor invoice in Toolbelt"),
    "5.jpg": ("contractor-invoicing-dashboard.jpg",
              "Toolbelt dashboard showing a contractor's paid and outstanding invoices"),
    "6.jpg": ("contractor-quote-estimate.jpg",
              "A contractor quote built in Toolbelt, ready to send to a client"),
    "7.jpg": ("contractor-invoice-line-items.jpg",
              "Itemised labour and materials line items on a contractor invoice"),
    "8.jpg": ("send-invoice-from-job-site.jpg",
              "Sending a finished invoice to a client from the job site"),
    "9.jpg": ("ai-invoice-description-writing.jpg",
              "AI turning a contractor's plain-English notes into professional invoice wording"),
}

# The screenshots render at ~300-400 CSS px in the phone mockups; 900px covers
# 2x retina with room to spare. The logo is small everywhere it appears.
MAX_WIDTH = {"default": 900, "toolbelt-logo.png": 512}
JPEG_QUALITY = 82
WEBP_QUALITY = 80

HTML_FILES = []
for dirpath, dirnames, files in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "scripts")]
    HTML_FILES += [os.path.join(dirpath, f) for f in files if f.endswith(".html")]


def target_width(name):
    return MAX_WIDTH.get(name, MAX_WIDTH["default"])


def process(dry):
    report = []
    for old, (new, _alt) in RENAMES.items():
        src = os.path.join(ROOT, old)
        dst = os.path.join(ROOT, new)
        webp = os.path.splitext(dst)[0] + ".webp"

        if not os.path.exists(src):
            if os.path.exists(dst):
                report.append(f"  {new}: already renamed")
                continue
            report.append(f"  {old}: MISSING (skipped)")
            continue

        before = os.path.getsize(src)
        im = Image.open(src)
        w = target_width(new)
        if im.width > w:
            im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)

        if dry:
            report.append(f"  {old} -> {new} (+ .webp), {before/1024:.0f}KB, "
                          f"{im.width}px  [dry-run]")
            continue

        if new.endswith(".png"):
            im.save(dst, "PNG", optimize=True)
        else:
            im.convert("RGB").save(dst, "JPEG", quality=JPEG_QUALITY, optimize=True,
                                   progressive=True)
        im.save(webp, "WEBP", quality=WEBP_QUALITY, method=6)

        if os.path.abspath(src) != os.path.abspath(dst):
            os.remove(src)

        after, aw = os.path.getsize(dst), os.path.getsize(webp)
        report.append(f"  {old:<42} -> {new:<38} "
                      f"{before/1024:>6.0f}KB -> {after/1024:>5.0f}KB "
                      f"(webp {aw/1024:>5.0f}KB, -{100 - aw*100/before:.0f}%)")
    return report


def rewrite_html(dry):
    """Point every reference at the new name and fix the alt text.

    Emits <picture> so the WebP is used where supported and the JPEG is the
    fallback — the brief asks for WebP *with fallbacks*, and a bare <img src=webp>
    would simply break on anything that cannot decode it.
    """
    changed = []
    for path in HTML_FILES:
        s = original = open(path, encoding="utf-8").read()

        for old, (new, alt) in RENAMES.items():
            if old in s:
                s = s.replace(old, new)

        # Upgrade every <img> that points at one of our renamed JPEGs into a
        # <picture>, with correct alt text and lazy-loading below the fold.
        def upgrade(m):
            tag = m.group(0)
            src_m = re.search(r'src="([^"]+)"', tag)
            if not src_m:
                return tag
            src = src_m.group(1)
            entry = next((v for k, v in RENAMES.items() if v[0] == src), None)
            if not entry or not src.endswith(".jpg"):
                return tag
            new_name, alt = entry
            webp = os.path.splitext(new_name)[0] + ".webp"
            # keep whatever class/style the original had
            keep = re.sub(r'\s(src|alt|loading)="[^"]*"', "", tag)
            keep = keep.replace("<img", "").replace(">", "").strip()
            attrs = (" " + keep) if keep else ""
            return (f'<picture>'
                    f'<source srcset="{webp}" type="image/webp">'
                    f'<img src="{new_name}" alt="{alt}" loading="lazy" '
                    f'decoding="async"{attrs}>'
                    f'</picture>')

        if "<picture>" not in s:
            s = re.sub(r'<img\b[^>]*>', upgrade, s)

        # Logo: not a <picture> (it is a PNG with transparency, and it is the LCP
        # element in the header — lazy-loading it would hurt, not help).
        s = re.sub(r'(<img[^>]*src="toolbelt-logo\.png"[^>]*?)alt="[^"]*"',
                   r'\1alt="Toolbelt invoice app logo"', s)

        if s != original:
            changed.append(os.path.relpath(path, ROOT))
            if not dry:
                open(path, "w", encoding="utf-8").write(s)
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    print("IMAGES")
    for line in process(a.dry_run):
        print(line)
    print("\nHTML REFERENCES")
    for f in rewrite_html(a.dry_run):
        print(f"  updated {f}")
    if a.dry_run:
        print("\n--dry-run: nothing written")


if __name__ == "__main__":
    main()
