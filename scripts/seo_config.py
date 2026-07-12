#!/usr/bin/env python3
"""
Single source of truth for everything that repeats across the site.

Change a price here, run the build scripts, and every page + every piece of
structured data updates. Nothing below should ever be typed into an HTML file by
hand — that is how a site ends up advertising $9.99 on one page, $14.99 on
another, and a third price in its schema.

Rule: if a number or URL appears on more than one page, it belongs in this file.
"""

# ---------------------------------------------------------------------- site --
SITE_URL = "https://toolbelt.pro"
SITE_NAME = "Toolbelt"
TAGLINE = "Invoice & Estimate App for Contractors"

# ------------------------------------------------------------------ app store --
APP_ID = "6757926789"
APPSTORE_URL = f"https://apps.apple.com/us/app/toolbelt-invoice-estimate/id{APP_ID}"

# Campaign tagging. Apple's attribution shows "untagged web referrer" for every
# link that arrives without these, which makes the website look like it converts
# nothing. Every App Store link the site emits should go through appstore_url().
def appstore_url(source="website", campaign="organic", content=None):
    """App Store link with Apple Ads / App Analytics campaign parameters.

    `pt` (provider token) is intentionally absent: it is account-specific and we
    do not have it. `ct` (campaign token) is what App Analytics groups on, and it
    works without `pt`.
    """
    ct = f"{source}-{campaign}" + (f"-{content}" if content else "")
    return f"{APPSTORE_URL}?ct={ct}&mt=8"


# -------------------------------------------------------------------- pricing --
# These MUST match what the pricing section of the homepage says. Structured data
# that disagrees with the visible page is a Google penalty risk, not a clever
# trick.
CURRENCY = "USD"
PRICE_MONTHLY = "14.99"
PRICE_YEARLY = "99.99"
FREE_TIER_DOCS_PER_MONTH = 3
FREE_TIER_DESC = (f"Free plan: up to {FREE_TIER_DOCS_PER_MONTH} invoices or quotes "
                  f"per month, all features included. No credit card required.")

# ------------------------------------------------------------------- identity --
ORG_LOGO = f"{SITE_URL}/toolbelt-logo.png"
OG_IMAGE = f"{SITE_URL}/toolbelt-og-card.png"
CONTACT_EMAIL = "support@toolbelt.pro"

# sameAs: only URLs we actually control and that actually exist. A sameAs list
# padded with profiles that 404 is worse than no sameAs at all.
SAME_AS = [
    APPSTORE_URL,
]

TWITTER_HANDLE = ""      # set when the account exists; blank = omit the tag

# --------------------------------------------------------------------- brand --
DEFAULT_OG_TYPE = "website"
LOCALE = "en_US"


# ------------------------------------------------------------ free templates --
# A Google Doc cannot be created by a script — it needs a Google account and a
# shared "make a copy" link, which is a human action. Until that link exists the
# templates page links the .docx (which Google Docs opens and converts natively).
# Paste the copy-link here and the page picks it up on the next build.
# Format: https://docs.google.com/document/d/<ID>/copy
GOOGLE_DOCS_TEMPLATE_URL = ""
