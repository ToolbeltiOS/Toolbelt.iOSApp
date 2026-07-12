#!/usr/bin/env python3
"""
The shared page shell: nav, footer, CSS, head tags, JSON-LD.

Every generated page (trade, comparison, template, tool, hub) goes through here,
so the design system exists in ONE place. The homepage keeps its own hand-written
CSS — it is a bespoke landing page and rewriting it was not the job — but the
tokens below are lifted from it verbatim so the generated pages are the same site,
not a lookalike.

`depth` is how many directories deep the page is, used to build relative paths
(`../../`). GitHub Pages has no server-side rewriting, so relative paths are the
only thing that works reliably from /for/plumbers/ and from /.
"""
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo_config as C  # noqa: E402

# Lifted verbatim from index.html so the generated pages are the same site.
CSS = """
:root{
  --orange:#E8732C; --orange-light:#F5923D; --orange-glow:rgba(232,115,44,.35);
  --surface:#0c0f14; --surface-raised:rgba(255,255,255,.04);
  --surface-hover:rgba(255,255,255,.07);
  --border:rgba(255,255,255,.08); --border-hover:rgba(255,255,255,.15);
  --text-white:#f0f0f2; --text-light:rgba(240,240,242,.75);
  --text-muted:rgba(240,240,242,.45);
  --radius-sm:10px; --radius-md:16px; --radius-lg:24px;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Outfit',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--surface);
  color:var(--text-light);line-height:1.7;font-size:17px;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{color:var(--text-white);line-height:1.2;font-weight:700}
h1{font-size:clamp(32px,5vw,52px);letter-spacing:-.02em}
h2{font-size:clamp(26px,3.4vw,36px);margin:52px 0 18px;letter-spacing:-.01em}
h3{font-size:21px;margin:32px 0 10px}
p{margin-bottom:18px}
a{color:var(--orange-light);text-decoration:none}
a:hover{text-decoration:underline}
.container{max-width:1100px;margin:0 auto;padding:0 24px}
.prose{max-width:760px;margin:0 auto;padding:0 24px}
ul,ol{margin:0 0 20px 22px}
li{margin-bottom:9px}
strong{color:var(--text-white)}

nav{position:sticky;top:0;z-index:100;background:rgba(12,15,20,.85);backdrop-filter:blur(14px);
  border-bottom:1px solid var(--border)}
nav .container{display:flex;align-items:center;justify-content:space-between;padding:14px 24px}
.logo{display:flex;align-items:center;gap:11px;text-decoration:none}
.logo img{width:38px;height:38px;border-radius:9px}
.logo-text{font-family:'Bebas Neue',sans-serif;font-size:25px;letter-spacing:.08em;
  color:var(--text-white)}
.nav-links{display:flex;gap:26px;align-items:center}
.nav-links a{color:var(--text-light);font-size:15px;font-weight:500;text-decoration:none}
.nav-links a:hover{color:var(--orange-light)}
@media(max-width:760px){.nav-links{gap:15px;font-size:13px}.nav-links a{font-size:13px}}

header.page{padding:70px 0 44px;border-bottom:1px solid var(--border);
  background:radial-gradient(ellipse at top,rgba(232,115,44,.10),transparent 62%)}
header.page .kicker{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.22em;
  text-transform:uppercase;color:var(--orange);font-weight:500}
header.page h1{margin:14px 0 14px}
header.page .standfirst{font-size:19px;color:var(--text-light);max-width:640px}
main{padding:14px 0 80px}

.breadcrumb{font-size:14px;color:var(--text-muted);padding:16px 0 0}
.breadcrumb a{color:var(--text-muted)}
.breadcrumb a:hover{color:var(--orange-light)}

table{width:100%;border-collapse:collapse;margin:24px 0;font-size:15.5px;
  background:var(--surface-raised);border:1px solid var(--border);
  border-radius:var(--radius-md);overflow:hidden}
th,td{padding:12px 15px;text-align:left;border-bottom:1px solid var(--border);vertical-align:top}
thead th{background:rgba(255,255,255,.06);color:var(--text-white);font-size:13px;
  letter-spacing:.05em;text-transform:uppercase;font-weight:600}
tbody tr:last-child td{border-bottom:none}
td.num,th.num{text-align:right;white-space:nowrap}
.tablewrap{overflow-x:auto}

.card{background:var(--surface-raised);border:1px solid var(--border);
  border-radius:var(--radius-md);padding:24px 26px;margin:20px 0}
.card h3{margin-top:0}
.note{background:rgba(232,115,44,.07);border-left:3px solid var(--orange);
  border-radius:0 var(--radius-sm) var(--radius-sm) 0;padding:16px 20px;margin:24px 0}
.note p:last-child{margin-bottom:0}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px;margin:24px 0}
.grid a.tile{display:block;background:var(--surface-raised);border:1px solid var(--border);
  border-radius:var(--radius-md);padding:20px 22px;text-decoration:none;color:var(--text-white);
  font-weight:600;transition:border-color .15s,transform .15s}
.grid a.tile:hover{border-color:var(--orange);transform:translateY(-2px);text-decoration:none}
.grid a.tile small{display:block;font-weight:400;color:var(--text-muted);font-size:13.5px;
  margin-top:5px;line-height:1.5}

.btn{display:inline-block;background:var(--orange);color:#fff;font-weight:700;
  padding:14px 30px;border-radius:999px;text-decoration:none;font-size:16px;
  box-shadow:0 8px 26px var(--orange-glow)}
.btn:hover{background:var(--orange-light);text-decoration:none}
.btn.secondary{background:transparent;border:1px solid var(--border-hover);
  color:var(--text-white);box-shadow:none}
.cta{background:linear-gradient(135deg,rgba(232,115,44,.13),rgba(232,115,44,.04));
  border:1px solid rgba(232,115,44,.25);border-radius:var(--radius-lg);
  padding:36px 34px;margin:56px 0 0;text-align:center}
.cta h2{margin:0 0 10px}
.cta p{color:var(--text-light);margin-bottom:22px}

.faq-q{color:var(--text-white);font-weight:600;font-size:17.5px;margin:26px 0 6px}
.win{border-left:3px solid #3ba55d}
.lose{border-left:3px solid var(--orange)}

footer{background:#080a0e;border-top:1px solid var(--border);padding:48px 0 34px;
  color:var(--text-muted);font-size:14.5px}
.footer-cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:28px;
  margin-bottom:30px}
.footer-cols h4{color:var(--text-white);font-size:13px;letter-spacing:.1em;text-transform:uppercase;
  margin-bottom:12px}
.footer-cols a{display:block;color:var(--text-muted);margin-bottom:7px;font-size:14.5px}
.footer-cols a:hover{color:var(--orange-light)}
.footer-bottom{border-top:1px solid var(--border);padding-top:20px;display:flex;
  justify-content:space-between;flex-wrap:wrap;gap:10px}
"""


def rel(depth):
    return "../" * depth if depth else ""


def nav(depth):
    r = rel(depth)
    return f"""<nav>
  <div class="container">
    <a href="{r}index.html" class="logo">
      <img src="{r}toolbelt-logo.png" alt="Toolbelt invoice app logo">
      <span class="logo-text">TOOLBELT</span>
    </a>
    <div class="nav-links">
      <a href="{r}for/">Trades</a>
      <a href="{r}compare/">Compare</a>
      <a href="{r}templates/free-contractor-invoice-template/">Templates</a>
      <a href="{r}tools/contractor-hourly-rate-calculator/">Rate calculator</a>
      <a href="{r}blog/">Blog</a>
    </div>
  </div>
</nav>"""


def footer(depth, trades=None):
    r = rel(depth)
    trades = trades or []
    trade_links = "".join(
        f'<a href="{r}for/{t}/">{n}</a>' for t, n in trades[:6])
    return f"""<footer>
  <div class="container">
    <div class="footer-cols">
      <div>
        <h4>By trade</h4>
        {trade_links}
        <a href="{r}for/">All trades &rarr;</a>
      </div>
      <div>
        <h4>Free tools</h4>
        <a href="{r}templates/free-contractor-invoice-template/">Free invoice template</a>
        <a href="{r}tools/contractor-hourly-rate-calculator/">Hourly rate calculator</a>
        <a href="{r}blog/">Blog</a>
      </div>
      <div>
        <h4>Compare</h4>
        <a href="{r}compare/">All comparisons</a>
        <a href="{r}compare/toolbelt-vs-joist/">vs Joist</a>
        <a href="{r}compare/toolbelt-vs-jobber/">vs Jobber</a>
        <a href="{r}compare/toolbelt-vs-quickbooks/">vs QuickBooks</a>
      </div>
      <div>
        <h4>Company</h4>
        <a href="{r}support.html">Support</a>
        <a href="{r}privacy.html">Privacy Policy</a>
        <a href="{r}terms.html">Terms of Service</a>
        <a href="{C.APPSTORE_URL}">Download on iOS</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Toolbelt. All rights reserved.</span>
      <span>Invoicing built for the job site.</span>
    </div>
  </div>
</footer>"""


CLARITY = """<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "v4peke782d");
</script>"""


def cta(depth, heading, sub, source, campaign, content=None):
    return f"""<div class="cta">
  <h2>{heading}</h2>
  <p>{sub}</p>
  <a class="btn" href="{C.appstore_url(source, campaign, content)}">Get Toolbelt on the App Store</a>
</div>"""


def page(*, depth, title, desc, url_path, body, jsonld=None, kicker="", h1="",
         standfirst="", breadcrumb="", trades=None, extra_head="", extra_js=""):
    r = rel(depth)
    canonical = C.SITE_URL + url_path
    ld = "\n".join(
        f'<script type="application/ld+json">\n{json.dumps(o, indent=2, ensure_ascii=False)}\n</script>'
        for o in (jsonld or []))

    header = ""
    if h1:
        header = f"""<header class="page">
  <div class="prose">
    {f'<span class="kicker">{kicker}</span>' if kicker else ''}
    <h1>{h1}</h1>
    {f'<p class="standfirst">{standfirst}</p>' if standfirst else ''}
  </div>
</header>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<link rel="canonical" href="{canonical}">
<meta name="description" content="{html.escape(desc, quote=True)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{C.SITE_NAME}">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{C.OG_IMAGE}">
<meta property="og:locale" content="{C.LOCALE}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title, quote=True)}">
<meta name="twitter:description" content="{html.escape(desc, quote=True)}">
<meta name="twitter:image" content="{C.OG_IMAGE}">
<link rel="icon" type="image/png" href="{r}toolbelt-logo.png">
<link rel="apple-touch-icon" href="{r}toolbelt-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Bebas+Neue&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
{CLARITY}
{ld}
{extra_head}
<style>{CSS}</style>
</head>
<body>
{nav(depth)}
<div class="container">{breadcrumb}</div>
{header}
<main>
{body}
</main>
{footer(depth, trades)}
{extra_js}
</body>
</html>
"""


def breadcrumb_html(depth, trail):
    """trail: [(name, href_or_None)] — last item has no link."""
    parts = []
    for i, (name, href) in enumerate(trail):
        if href and i < len(trail) - 1:
            parts.append(f'<a href="{href}">{html.escape(name)}</a>')
        else:
            parts.append(html.escape(name))
    return f'<p class="breadcrumb">{" / ".join(parts)}</p>'


def breadcrumb_ld(trail):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name,
             "item": C.SITE_URL + path}
            for i, (name, path) in enumerate(trail)
        ],
    }


def faq_ld(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer",
                                "text": __import__("re").sub(r"<[^>]+>", "", a)}}
            for q, a in faqs
        ],
    }
