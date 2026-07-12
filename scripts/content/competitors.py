#!/usr/bin/env python3
"""
Competitor data for the /compare/ pages.

THE RULE THAT GOVERNS THIS FILE: we publish a competitor's price only when we
verified it on that competitor's own pricing page, and we record the URL and the
date we checked. Where we could not verify it, we say so on the page and link out
instead of printing a number.

That is not squeamishness. A comparison page with a wrong price is worse than no
comparison page: it is the single fastest way to get a "misleading comparison"
complaint, it is trivially disprovable by any reader who clicks through, and it
poisons every other claim on the page. Three of the five competitors here make
their pricing genuinely hard to verify — QuickBooks is mid-increase, Invoice
Simple blocks automated access to its pricing page, Invoice2go hides prices behind
a currency selector — and the honest response is to report that, not to guess.

Prices below are USD, and every page that renders them stamps VERIFIED_ON and
tells the reader to check before deciding. Re-verify at least quarterly.
"""

VERIFIED_ON = "2026-07-12"

# `price_verified: False` means: DO NOT print a hard number on the page. Describe
# the plan structure (which we can verify) and link to their pricing page.
COMPETITORS = {
    "joist": {
        "name": "Joist",
        "slug": "toolbelt-vs-joist",
        "title": "Toolbelt vs Joist: Honest Comparison (2026)",
        "desc": ("Toolbelt vs Joist for contractor invoicing: real pricing, what each does "
                 "well, and where Joist genuinely beats us. Updated July 2026."),
        "pricing_url": "https://www.joist.com/pricing/",
        "price_verified": True,
        "platforms": "iOS, Android, web",
        "free_plan": False,
        "trial": "14-day free trial (Pro or Elite)",
        "plans": [
            ("Basics", "$10/mo", "$100/yr", "Up to 5 documents per month"),
            ("Pro", "$17/mo", "$170/yr", "Unlimited documents and clients"),
            ("Elite", "$32/mo", "$320/yr", "Adds business reports and change orders"),
        ],
        # What they are genuinely better at. Every comparison page must have this
        # section and it must be true — a page where the competitor loses on every
        # row is a page nobody believes.
        "they_win": [
            ("Android and web", "Joist runs on Android and in a browser. Toolbelt is "
             "iPhone-only. If your crew is on Android, or you do your paperwork on a "
             "desktop at the end of the week, Joist covers a case we simply do not."),
            ("Homeowner financing", "Joist can offer your customer financing at the point "
             "of the estimate, which for a $12,000 roof or a full re-pipe can be the "
             "difference between a signed job and a maybe. Toolbelt has nothing like it."),
            ("Change orders on Elite", "Formal change-order tracking is built in at the "
             "Elite tier. If you routinely run jobs where scope creeps and you need a "
             "paper trail for it, that is a real feature and we do not match it."),
        ],
        "we_win": [
            ("Price", "Toolbelt is $14.99/mo or $99.99/yr for everything. Joist's "
             "unlimited-document tier starts at $17/mo — and their $10 tier caps you at "
             "5 documents a month, which is a slow week for most trades."),
            ("A real free tier", "Toolbelt gives you 3 documents a month free, forever, "
             "with every feature switched on. Joist has a 14-day trial and then a bill."),
            ("Voice input", "Speak the line item; it gets written up. Nobody else in this "
             "list does this, and it is the difference between invoicing from the truck "
             "and invoicing at 9pm from the kitchen table."),
            ("Genuinely offline", "Toolbelt builds and stores documents with no signal at "
             "all — basements, new-builds, rural jobs — and syncs when you surface."),
        ],
        "switching": [
            'If you are already on Joist and it is working, the honest answer is that switching to save $70 a year is not a good use of your week. The case for moving is specific: you are on Joist Basics, you keep hitting the 5-document cap, and the upgrade to Pro at $17/mo is the thing that pushed you to look around. In that situation Toolbelt is cheaper and gives you voice input on top.',
            'Practically, there is no data migration and there does not need to be. Your old invoices stay in Joist and remain valid documents — you do not need them in a new app to have sent them. Set your business details and logo up in Toolbelt once, rebuild your five or six most common line items (about ten minutes), and run the next job through it. Keep both for a month if you want to; the free tier means that costs you nothing.',
        ],
        "verdict": ("Joist if you need Android, a desktop browser, or customer financing. "
                    "Toolbelt if you are on an iPhone, want to invoice by voice from the "
                    "job site, and would rather pay $99.99 a year than $170."),
    },

    "invoice-simple": {
        "name": "Invoice Simple",
        "slug": "toolbelt-vs-invoice-simple",
        "title": "Toolbelt vs Invoice Simple: Honest Comparison",
        "desc": ("Toolbelt vs Invoice Simple for trades: what each does well, where each "
                 "falls short, and why we won't print their price without verifying it."),
        "pricing_url": "https://www.invoicesimple.com/pricing/",
        "price_verified": False,
        "price_note": ("Invoice Simple's pricing page blocks automated access, and the "
                       "third-party sites that quote it disagree with each other — we saw "
                       "the entry tier listed at both $4.99 and $6.99 a month. Rather than "
                       "print a number we cannot stand behind, we are linking you to their "
                       "page. Check it yourself; that is what we would do."),
        "platforms": "iOS, Android, web",
        "free_plan": "Free to create; paid to send beyond a limit",
        "trial": "14-day trial of the top tier",
        "plans": [],
        "they_win": [
            ("Android and web", "Same story as Joist. Invoice Simple is everywhere; "
             "Toolbelt is iPhone-only."),
            ("Dead simple for non-trades", "It is a general-purpose invoice maker and it is "
             "very good at that. If you are a freelancer or a shop owner rather than a "
             "contractor, its generic approach is a feature, not a bug."),
            ("Longer track record", "It has been around a long time with a large user base "
             "and the stability that implies."),
        ],
        "we_win": [
            ("Built for trades, not for everyone", "Invoice Simple is a general invoice "
             "app. It has no concept of a quote that becomes an invoice when the job is "
             "won, no trade line items, and nothing that understands a job site."),
            ("Voice input and AI descriptions", "Describe the work in your own words; "
             "Toolbelt writes it up properly. Invoice Simple gives you a blank text box."),
            ("Offline by design", "Toolbelt is built to work with no signal at all."),
            ("Flat, published price", "$14.99/mo or $99.99/yr, all features. No tier maze."),
        ],
        "switching": [
            "The reason people move from Invoice Simple to Toolbelt is almost always the same: they started as a general small business and became a trade business. Invoice Simple is built to invoice anything. Once your invoices are consistently 'labour, materials, call-out, deposit', a generic tool starts adding friction on every single document.",
            'Switching costs you nothing but setup time. There is no migration — your sent invoices live in your email and your accounting, not in the app. Set up your business profile, save the six or seven line items you actually use, and run one job through Toolbelt end to end before you commit to it.',
        ],
        "verdict": ("Invoice Simple if you need Android or web, or if you are not really a "
                    "contractor. Toolbelt if you are in a trade, on an iPhone, and want the "
                    "app to understand what a quote and a job site are."),
    },

    "jobber": {
        "name": "Jobber",
        "slug": "toolbelt-vs-jobber",
        "title": "Toolbelt vs Jobber: Which Do You Actually Need?",
        "desc": ("Jobber is field-service management. Toolbelt is invoicing. Real prices, "
                 "and an honest answer about which one your business actually needs."),
        "pricing_url": "https://www.getjobber.com/pricing/",
        "price_verified": True,
        "platforms": "iOS, Android, web",
        "free_plan": False,
        "trial": "14-day free trial",
        "plans": [
            ("Core", "$49/mo", "$29/mo billed annually", "1 user; quotes, invoicing, booking"),
            ("Connect", "$139/mo", "$99/mo billed annually", "Adds automation, QuickBooks sync"),
            ("Grow", "$199/mo", "$149/mo billed annually", "Adds job costing, two-way SMS"),
            ("Plus", "$499/mo", "$399/mo billed annually", "15 users, marketing suite"),
        ],
        "they_win": [
            ("It is a different class of product", "This is the honest headline. Jobber is "
             "field-service management: scheduling, dispatching a crew, routing, client "
             "portals, job costing, QuickBooks sync, 100+ integrations. Toolbelt does not "
             "do any of that and does not pretend to."),
            ("Crews", "If you are dispatching three vans tomorrow morning, you need "
             "Jobber's scheduling. An invoicing app cannot help you with that."),
            ("Integrations", "QuickBooks Online sync, payment automation, a real API "
             "ecosystem. Toolbelt has none of this."),
        ],
        "we_win": [
            ("Price, by a wide margin", "Jobber's entry plan is $49/mo month-to-month "
             "($29/mo if you commit to a year, and additional users are $29/mo each). "
             "Toolbelt is $14.99/mo, or $99.99 for the year, one price."),
            ("You may not need any of it", "If you are a one-person operation who wants to "
             "send a quote, win the job, and invoice it, most of what you are paying Jobber "
             "for is scheduling and dispatch software you will never open."),
            ("Speed to first invoice", "Toolbelt is an app you open on the drive home. "
             "Jobber is a system you implement."),
        ],
        "switching": [
            'Do not switch from Jobber to Toolbelt to save money if you are actually using Jobber. If you have your schedule in it, your crew on it, and QuickBooks synced to it, you are not paying for invoicing — you are paying for the operating system of your business, and ripping that out to save $30 a month is a bad trade.',
            'The switch makes sense in one situation, and it is a common one: you signed up for Jobber because it is what serious contractors use, and eleven months later you are still a one-person operation who only ever opens it to send invoices. That is a $49/mo invoicing app. If that description stings a little, try Toolbelt free for a month alongside it and see whether you miss anything.',
        ],
        "verdict": ("Genuinely: if you run a crew and need scheduling and dispatch, buy "
                    "Jobber — we are not the right tool and we will not pretend otherwise. "
                    "If you are a one- or two-person operation and 'software' means 'get "
                    "the invoice out before I forget', Toolbelt costs a fifth as much and "
                    "does that job."),
    },

    "quickbooks": {
        "name": "QuickBooks",
        "slug": "toolbelt-vs-quickbooks",
        "title": "Toolbelt vs QuickBooks for Contractors",
        "desc": ("QuickBooks is accounting software. Toolbelt is an invoicing app. Most "
                 "contractors end up needing one of each — here's why, and what each costs."),
        "pricing_url": "https://quickbooks.intuit.com/pricing/",
        "price_verified": False,
        "price_note": ("QuickBooks pricing is mid-change: increases took effect on 1 August "
                       "2026 and the figures being quoted around the web do not agree with "
                       "each other. As a rough guide, the entry Simple Start tier has been "
                       "in the region of $38/mo and the mid tiers well north of that — but "
                       "we are not going to print a precise number we cannot verify today. "
                       "Check their pricing page."),
        "platforms": "iOS, Android, web",
        "free_plan": False,
        "trial": "30-day trial, or a promotional discount — usually not both",
        "plans": [],
        "they_win": [
            ("It is actual accounting, and you will probably need it", "QuickBooks does "
             "your books: expenses, mileage, payroll, sales tax, bank reconciliation, and "
             "the reports your accountant asks for in April. Toolbelt does none of that. "
             "This is not a close call — they are different tools."),
            ("Your accountant already speaks it", "That has real value and it is worth "
             "money at tax time."),
            ("Everything in one ledger", "Invoices, expenses and payments in a single "
             "system, which is genuinely simpler at the year end."),
        ],
        "we_win": [
            ("Invoicing from a job site is not what QuickBooks is for", "It is a "
             "desk-and-browser product with a mobile app bolted on. Getting a quote out of "
             "it while standing in someone's crawlspace is not a pleasant experience."),
            ("Price, for the invoicing job alone", "$14.99/mo or $99.99/yr against a "
             "QuickBooks tier that costs multiples of that — most of which you are paying "
             "for bookkeeping features, not invoicing ones."),
            ("Voice, AI descriptions, offline", "None of which QuickBooks offers."),
        ],
        "switching": [
            'This is rarely a switch, and you should be suspicious of anyone who tells you it is. QuickBooks is where your books live. Toolbelt is where your invoices get created. Most of the contractors who use both send the quote and the invoice from Toolbelt because they are standing in a driveway, then record the payment in QuickBooks because that is where their accountant looks.',
            "The one genuine 'switch' case: you pay for QuickBooks purely because you needed to send invoices, you do not do your own books, and your accountant is working from a shoebox of receipts anyway. In that case you are paying accounting-software prices for an invoicing feature, and you should stop.",
        ],
        "verdict": ("This is not really either/or. Plenty of contractors quote and invoice "
                    "in Toolbelt because it is fast on site, and keep QuickBooks for the "
                    "books because their accountant wants it. If you can only have one and "
                    "you have an accountant, keep QuickBooks. If you can only have one and "
                    "your books are a shoebox, Toolbelt will at least get you paid."),
    },

    "invoice2go": {
        "name": "Invoice2go",
        "slug": "toolbelt-vs-invoice2go",
        "title": "Toolbelt vs Invoice2go: Honest Comparison",
        "desc": ("Toolbelt vs Invoice2go for contractors: plan limits, card fees, what each "
                 "does well, and the pricing they don't show you until you pick a currency."),
        "pricing_url": "https://invoice.2go.com/pricing/",
        "price_verified": False,
        "price_note": ("Invoice2go does not show a price on its pricing page until you "
                       "select a currency, so we cannot quote you a verified figure here. "
                       "What we can tell you is the shape of the plans, which is the part "
                       "that actually catches people out: the tiers are limited by how many "
                       "invoices you send per YEAR."),
        "platforms": "iOS, Android, web",
        "free_plan": False,
        "trial": "30-day free trial (card details required)",
        "plans": [
            ("Starter", "see their site", "—", "30 invoices per year · 3.5% card fee"),
            ("Professional", "see their site", "—", "100 invoices per year · 3% card fee"),
            ("Premium", "see their site", "—", "Unlimited invoices · 2.9% card fee"),
        ],
        "they_win": [
            ("Android and web", "Again: Toolbelt is iPhone-only. Invoice2go is not."),
            ("Payments and card processing built in", "Card payment acceptance is baked "
             "into the plans, with the fee dropping as you move up the tiers."),
            ("Accounting integrations", "QuickBooks and Xero sync on the middle tier up."),
        ],
        "we_win": [
            ("No annual invoice cap", "Read the Invoice2go tiers again: 30 invoices a "
             "year on Starter, 100 on Professional. Thirty invoices is under three a "
             "month. Most working contractors will blow through that and get pushed up a "
             "tier. Toolbelt's paid plan has no cap at all."),
            ("A price you can see without a sales funnel", "$14.99/mo, $99.99/yr, on the "
             "page, in public."),
            ("Voice, AI descriptions, offline", "Speak the line item, let the app write it properly, and do it all with no signal. Invoice2go has none of these."),
            ("Built for trades specifically", "Not a general-purpose invoice tool with a contractor template bolted on."),
        ],
        "switching": [
            'The thing that pushes people off Invoice2go is the annual invoice cap. Thirty invoices a year on the entry tier is fewer than three a month — a slow month for most trades — and one hundred on the tier above it is still a ceiling you can see from where you are standing. Getting metered on the core action of your business is an unpleasant way to run it.',
            'If you switch, nothing needs migrating. Your history is in your email and your bank statements. Rebuild your standard line items in Toolbelt — ten minutes — and run the next job through it. The free tier gives you three documents a month indefinitely, which is enough to test it properly on real jobs before you pay anyone anything.',
        ],
        "verdict": ("Invoice2go if you need Android, web, or integrated card processing. "
                    "Toolbelt if you send more than a couple of invoices a month and would "
                    "rather not be metered by the year."),
    },
}
