# Toolbelt — Sanctioned Claims (claims.md)

> **STATUS: OWNER-RATIFIED 2026-08-18** (Luis Freyre, CHECKPOINT 0). Every claim on
> every future Toolbelt page must trace to a line in this file or to a dated
> competitor check. If it isn't here and it isn't a dated competitor fact, it doesn't ship.
>
> **Sources:** live App Store listing + iTunes lookup API for `id6757926789`,
> read **2026-08-18**, plus owner confirmation of shipped behaviour at CHECKPOINT 0.
> Re-verify before trusting after the next app release.
> **Truth law:** claims true of the *shipped* app today; no invented numbers; no
> "#1" / "top-rated" / "most popular"; no unsourced behaviour claims. Small lies: none.

---

## 1. App identity (verified — App Store)
- **App Store name:** Toolbelt - Invoice & Estimate
- **Subtitle:** Invoice App for Contractors
- **Product name in prose:** Toolbelt
- **App Store ID / URL:** 6757926789 — https://apps.apple.com/us/app/toolbelt-invoice-estimate/id6757926789
- **Bundle ID:** com.luis.ContractorPro
- **Developer / seller (as listed):** Luis Freyre
- **Category:** Business (primary); also surfaces under Productivity
- **Age rating:** 4+
- **Current version:** 1.06 — released 2026-02-13 (initial release 2026-01-22)

## 2. Platform (verified — App Store; iPad owner-confirmed at CHECKPOINT 0)
- **iOS app with real, working iPhone AND iPad support** (owner-confirmed). Requires
  **iOS 26.2 or later**. Both iPhone and iPad are first-class — do not say "iPhone-only."
- Also *runs on* Mac and Apple Vision via iOS-app compatibility (listing lists
  "iPhone, iPad, Mac, Apple Vision"). **Describe as an iOS/iPadOS app** — do NOT
  claim a purpose-built Mac, Vision, Android, or web version.
- No Android version, no web app.
- **Action (existing content):** the comparison pages' "Toolbelt is iPhone-only"
  concessions are now FALSE and must be corrected to "iPhone and iPad" — a competitor's
  Android/web is still a valid concession, but the iPad claim is not.

## 3. Pricing (verified — App Store, as of Aug 2026)
- **Free to download.**
- **Free tier:** **3 documents per month**, no credit card required. Owner-confirmed
  (paywall) 2026-08-18: a "document" is an invoice **or** a quote/estimate — either type
  counts toward the 3/month cap. Sanctioned unit = **documents** everywhere.
  - Note: the App Store *description* says "3 invoices per month," which is looser than
    the shipped paywall. That's a Phase 4 ASO alignment item (owner metadata edit), not
    a website claim — the website uses "3 documents."
- **Pro Monthly:** $14.99 / month.
- **Pro Yearly:** $99.99 / year.
  - Safe derived statement: yearly vs 12× monthly ($179.88) saves **$79.89/year**.
  - In-app purchases are both labelled "Toolbelt Pro" ($14.99 and $99.99).

## 4. Ratings (verified — App Store)
- **0 ratings.** Listing states it "hasn't received enough ratings or reviews to
  display an overview" (2026-08-18).
- **Consequences (binding):** no `aggregateRating` in schema; no review-count or
  star claims; **no "#1", "top-rated", "most popular", "contractors are switching"**
  anywhere. (Homepage H1 corrected to "The Invoice App Built for Contractors" on
  2026-08-18; the ported prose gate enforces this class going forward.)

## 5. Features shipped (verified — App Store description + v1.06 release notes)
Use these; phrase them plainly.
- Create professional invoices in ~30 seconds.
- **AI-written descriptions:** describe the job in plain words, AI turns it into
  professional invoice wording.
- **Voice input** (for hands-free/dirty-hands entry).
- **Works offline** (no signal needed on the job site).
- **Quotes / estimates** (the app is "Invoice & Estimate"; site says "Quote in Seconds").
- **Customizable PDF invoices.**
- **Client management** — save and reuse client details. (Describe minimally; see flags.)
- **Expenses** tracking (release notes back up "expenses").
- **Templates.**
- **Reminders** (payment/follow-up reminder settings; v1.06 "added reminders").
- **Backup & restore** — complete backup/restore of invoices, clients, profile,
  expenses, templates, and reminder settings (v1.06).
- **Photos on the invoice** — attach job-site photos to a document (owner-confirmed
  shipped at CHECKPOINT 0). Sanctioned.
- **Reusable / saved line items** — save a line item once and reuse it (owner-confirmed
  shipped at CHECKPOINT 0). Sanctioned.

## 6. DO-NOT-CLAIM / verify-before-use (unsure these are true of the shipped app)
- **In-app payment collection.** No evidence the app processes card/Stripe/ACH
  payments. It *creates and sends* invoices/quotes; getting paid happens outside the
  app. Do NOT write "get paid in the app," "accept payments," or "payment processing"
  until verified in the shipped app.
- **Accounting integrations / sync** (QuickBooks, Xero, exports). No evidence. Do not claim.
- **"Client management" depth** — CRM vs. a saved-contacts list is unknown; keep it modest.
- **AI model/specifics** — say "AI-generated wording"; name no model, cite no accuracy stat.
- **Mac / Apple Vision** as first-class platforms — compatibility only; don't headline it.
- **Company entity** — only "Luis Freyre" (developer) and "Toolbelt" (product) are
  verifiable. Do not invent an LLC/Inc., team size, "founded in," user counts, or
  "trusted by N contractors."
- **Apple Small Business Program economics** — a developer-side 15% detail, not
  customer-facing; keep it off pages entirely.

## 7. Cross-links / facts of record
- Website: https://toolbelt.pro (GitHub Pages, custom domain).
- Support: https://toolbelt.pro/support.html · Privacy: https://toolbelt.pro/privacy.html
- Analytics on site: Google Analytics `G-EJV1HLMC17`, Microsoft Clarity `v4peke782d`.
- **Enforcement:** `rules/prose_gate.py` is the gate for this file's prohibitions
  (§4, §6). `python3 rules/prose_gate.py --all` scans every built page and fails on
  any prohibited claim; `python3 rules/prose_gate.py` runs the fixture self-test.
  Ported from safenest-web-reports with a Toolbelt-authored `rules/rules.json`.

---
*Owner-ratified 2026-08-18 (Luis Freyre) at CHECKPOINT 0, in writing via the session
rulings. Free-tier unit = "documents" confirmed against the paywall.*
