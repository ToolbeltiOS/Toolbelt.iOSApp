# SEO: what you have to do by hand

**Written 2026-07-12.** Everything in here needs a human with an account. Code cannot do any
of it, and none of the Phase 1/2 work pays off properly until most of it is done.

Ordered by impact per minute spent.

---

## 1. Google Search Console — 15 minutes, do it first

Nothing else on this list matters as much. Until this is done you are optimising blind.

1. Go to **[search.google.com/search-console](https://search.google.com/search-console)**.
2. Add a property. Choose **Domain** (`toolbelt.pro`), not URL-prefix — a domain property
   covers `www`, `http`, `https` and every subdomain in one go.
3. It will give you a **TXT record** to add to your DNS. Add it wherever `toolbelt.pro`'s DNS
   lives (the registrar, or Cloudflare if it is fronted). Verification usually lands within
   minutes but can take up to 24 hours.
4. Once verified: **Sitemaps → add** `https://toolbelt.pro/sitemap.xml`.
5. **URL Inspection → paste `https://toolbelt.pro/` → Request Indexing.** Do the same for
   `/for/`, `/compare/`, and `/templates/free-contractor-invoice-template/`. This is a nudge,
   not a guarantee, but it costs a minute.

**Then leave it alone for three weeks.** Nothing you do in week one will show. What to look
for when you come back:

- **Coverage/Pages:** are the new pages *Indexed*, or only *Discovered – currently not
  indexed*? "Discovered but not indexed" on the trade pages would be the first sign Google
  considers them thin — that is the number to watch.
- **Duplicate, Google chose a different canonical:** the specific failure mode for ten
  trade pages and five comparison pages built from one template. They are genuinely
  different from each other, which is why they should survive — but this is where you would
  find out if they do not.
- **Queries:** which non-brand phrases actually surface. This is what tells you which trade
  pages to expand and which were a waste of a page.

## 2. Bing Webmaster Tools — 5 minutes

Smaller, but free, and it also feeds ChatGPT search results, which increasingly matters.

1. **[bing.com/webmasters](https://www.bing.com/webmasters)**.
2. **Import from Google Search Console** — one click, no separate DNS verification. Do this
   *after* step 1.
3. Submit the same sitemap.

## 3. App Store ↔ website cross-linking — 10 minutes, and it is worth more than it sounds

Right now the App Store listing and the website are two islands. Apple's crawler and Google
both use these links to connect them.

1. **App Store Connect → your app → App Information.**
2. Set **Marketing URL** to `https://toolbelt.pro`.
3. Set **Support URL** to `https://toolbelt.pro/support.html`.
4. Set **Privacy Policy URL** to `https://toolbelt.pro/privacy.html`.
5. In the app description, include the URL as plain text (`toolbelt.pro`) — it is not a
   clickable link, but it is read.

**Why it matters beyond SEO:** an App Store listing with a real marketing site attached
converts better. Buyers check.

## 4. Campaign-tag every App Store link — this is already done in code, but you must finish it

Every App Store link the *website* emits now carries a campaign token, via
`seo_config.appstore_url()`. That is why App Analytics has been showing your web traffic as
an untagged referrer: nothing was tagged.

**What you still have to do:**

1. **App Store Connect → Analytics → Campaigns** — confirm the campaign tokens are arriving.
   The tokens the site sends are `website-organic`, `website-trade-<trade>`,
   `website-compare-<competitor>`, `website-template-…`, `website-tool-…`, `website-blog-…`.
2. **Anywhere you post a link by hand** — TikTok bio, Instagram, a Reddit comment, a forum
   signature — use a tagged link too, or that traffic stays invisible. Format:
   ```
   https://apps.apple.com/us/app/toolbelt-invoice-estimate/id6757926789?ct=SOURCE-CAMPAIGN&mt=8
   ```
   e.g. `?ct=tiktok-bio`, `?ct=reddit-hvac`, `?ct=email-signature`.
3. If you have a **provider token (`pt`)** from an Apple Search Ads account, add it — it
   improves attribution. Without it, `ct` still works.

**Once this is running for a month you will know, for the first time, whether the website
sends anyone.** Right now you genuinely do not.

## 5. The Google Docs template — 10 minutes

The templates page ships a real PDF and a real `.docx` for eleven variants. It does **not**
have a Google Docs "make a copy" link, because creating a Google Doc requires a Google
account and a human — a script cannot do it.

1. Open `templates/downloads/contractor-invoice-template.docx` in Google Docs
   (Drive → New → File upload → open with Google Docs).
2. Tidy anything the conversion mangled.
3. **Share → Anyone with the link → Viewer.**
4. Copy the URL and **change the tail from `/edit?usp=sharing` to `/copy`.** This is the bit
   people get wrong: `/copy` forces "Make a copy" instead of dumping the reader into a
   read-only doc they cannot use.
5. Paste it into `tools/seo_config.py` → `GOOGLE_DOCS_TEMPLATE_URL`, then re-run
   `python3 tools/build_freetools.py`. The button appears automatically.

---

## 6. Backlinks — the part that actually decides whether any of this ranks

Blunt truth: the technical work in Phase 1 and the pages in Phase 2 are table stakes. A site
with no links will not outrank Joist and Jobber for "invoice app for contractors" no matter
how good its schema is. The two free tools exist to earn links passively, but passive is
slow, and you need a starting push.

**The rule for all of the below: lead with the free thing, not the app.** Nobody links to an
app. People link to a free template with no email gate and a calculator that works.

### iOS app directories (easy, low value, do them once)

Submit once, forget. Each is a real link and takes minutes.

| Directory | Angle |
|---|---|
| Product Hunt | Launch it properly — pick a Tuesday, be around all day to answer comments. One shot. |
| AlternativeTo | List Toolbelt as an alternative to **Joist, Invoice Simple, Invoice2go**. Our comparison pages give you honest copy to paste. |
| Slant / SaaSHub / Capterra / GetApp | Software directories. Capterra and GetApp are where people actually shop for this. |
| There's An AI For That | The voice/AI angle is genuinely distinctive here — this is one of the few directories where we are not a me-too. |

### Contractor communities — where the templates get shared

**Read the rules of each before posting. Most ban self-promotion and will remove you, and a
removal costs you the community permanently.** The play is: be a member who is useful, and
share the free tool when it is genuinely the answer to someone's question.

| Community | The angle |
|---|---|
| r/Construction, r/Contractor, r/HVAC, r/Plumbing, r/electricians, r/Handyman | Do **not** post a link to the app. Ever. Answer invoicing/pricing questions properly, and link the **free template** or the **rate calculator** where it genuinely answers the question. r/electricians and r/HVAC are especially hostile to marketing and especially valuable. |
| Contractor Talk, Plumbing Zone, Electrician Talk | Old-school forums, still active, still indexed. A signature link is often allowed after N posts — check the rules. |
| Facebook trade groups | Enormous, and the free template gets shared organically here more than anywhere. Share the *template*, not the app. |
| r/smallbusiness, r/entrepreneur | The rate calculator plays better here than the template. |

The single highest-value post you can make: someone asks **"how much should I charge?"** —
which happens weekly in every one of those subs — and you reply with a real, useful answer
*and* the calculator. That is not spam; it is the answer.

### HARO / Featured / Qwoted — journalist requests

Sign up to **[Featured](https://featured.com)** and **[Qwoted](https://qwoted.com)** (HARO is
now Connectively; coverage has thinned but it is still free). Set alerts for:
`contractor`, `small business`, `invoicing`, `freelance`, `cash flow`, `trades`, `home
improvement`.

**The pitch angle that gets picked up:** you have data and a point of view nobody else does.

- *"Most contractors underprice because they think they bill 90% of their hours. It's
  55–70%."* — that is a quotable, specific, counter-intuitive claim, and it is true.
- *"The invoice sent from the driveway gets paid dramatically faster than the one sent on
  Sunday night."*
- *"A single-line invoice is a single thing to argue with."*

Respond within an hour of the request landing, answer the actual question in 100 words, and
do not pitch the app. The link comes with the credit.

### The one that is worth more than all of the above

**Get reviewed by a contractor with a YouTube channel or a TikTok following.** One genuine
review from someone the trades actually trust is worth more than fifty directory links. You
already do TikTok — the same instinct applies. Send the app to people who make content for
contractors, ask for nothing, and let them decide.

---

## 7. Things to check that I could not

- **`toolbelt.pro` DNS / GitHub Pages HTTPS** — confirm the custom domain has HTTPS enforced
  in the repo's Pages settings. An `http`-only site is a ranking and trust problem.
- **Google Analytics is installed but I did not touch it** (`G-EJV1HLMC17`). Confirm it is
  the property you actually read. Microsoft Clarity is also on the site
  (`v4peke782d`) — worth knowing you have session replay running.
- **The App Store screenshots and description** are outside this repo, and they are doing at
  least as much conversion work as the website. Worth the same honesty pass.

---

## What I would actually do this week

1. Search Console + Bing (20 minutes). Without this you are guessing.
2. App Store Connect marketing URL (10 minutes).
3. The Google Docs template link (10 minutes) — it makes the best link-magnet on the site
   materially more shareable.
4. Answer one "how much should I charge" thread properly, with the calculator.

Then leave it three weeks and read Search Console before touching anything else. The most
common SEO mistake is changing things faster than the feedback arrives.
