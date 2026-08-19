#!/usr/bin/env python3
"""
Trade landing page content.

THE ANTI-DOORWAY RULE. Google's doorway-page policy exists precisely to catch what
a lazy version of this file would be: ten pages identical but for a find-and-replace
on the trade name. That is a penalty, not a strategy — and it also does not work,
because a plumber can tell in one paragraph whether the person writing knew anything
about plumbing.

So every trade below has genuinely different content:
  * pain points that are actually specific to that trade's billing (a roofer's
    problem is deposits on a $14k job; a handyman's problem is that a $90 call-out
    is not worth 20 minutes of paperwork; these are not the same problem)
  * line items with realistic units and real price ranges for that trade
  * FAQs a person in that trade would actually ask
  * a different angle on why voice / AI / offline matters for THEIR day

If you add a trade, write it properly or do not add it. A thin eleventh page drags
down the ten good ones.

Price ranges are illustrative US market ranges for EXAMPLE line items — they are
labelled as examples on the page, not quoted as market rates, because we are not a
pricing authority and pretending to be one would be its own kind of dishonesty.
"""

TRADES = {

    # ---------------------------------------------------------------- plumbers --
    "plumbers": {
        "name": "Plumbers",
        "singular": "plumber",
        "title": "Invoice App for Plumbers | Toolbelt",
        "desc": ("Quote and invoice plumbing jobs from the van. Voice input, AI line-item "
                 "descriptions, works with no signal in a basement. Free to start."),
        "h1": "The invoice app for plumbers",
        "keyword": "invoice app for plumbers",
        "intro": [
            "Plumbing is the trade where the paperwork is furthest from the desk. You are "
            "under a sink, in a crawlspace, or in a basement with three feet of concrete "
            "between you and the nearest cell tower. The job is done, the customer wants a "
            "number, and the invoice gets written that evening — if it gets written at all.",
            "Toolbelt is built for exactly that gap. Speak the work into your phone while "
            "you are packing up, let it turn \"replaced the wax ring and the supply line, "
            "snaked the main\" into line items a homeowner will read without arguing, and "
            "send it before you get back in the van. No signal required.",
        ],
        "pains": [
            ("The emergency call-out that never gets billed properly",
             "A burst pipe at 11pm is the most profitable work you do and the worst-tracked. "
             "You are not stopping to write down the fittings you used. By the time you "
             "invoice on Thursday, the after-hours premium is a guess and the parts list is "
             "whatever you can remember. Voice-note the job while you are still standing in "
             "the puddle and the line items are already written."),
            ("No signal where the work is",
             "Basements, crawlspaces, mechanical rooms, new-builds with no service yet — "
             "plumbing happens in the parts of a building that block phone signal. An "
             "invoicing app that needs a connection is an invoicing app you cannot use at "
             "the exact moment you have five free minutes."),
            ("Describing the work so it doesn't get argued with",
             "\"Fixed leak — $340\" invites a phone call. \"Diagnosed and repaired leaking "
             "compression fitting under kitchen sink; replaced supply line and shut-off "
             "valve; tested under pressure\" does not. The second one takes ten minutes to "
             "write at the end of a long day, which is why most people write the first one."),
            ("Parts markup that quietly disappears",
             "The trip to the supply house, the fittings from the van stock, the fixture you "
             "fronted — if they are not on the invoice within a day of the job they get "
             "under-billed or forgotten entirely. That is real money, every week."),
        ],
        "features": [
            ("Voice input for hands you can't use",
             "Your hands are wet, filthy, or holding a pipe wrench. Hit record, say what you "
             "did, and it becomes line items. This is the single feature plumbers keep."),
            ("AI descriptions that sound like a professional wrote them",
             "Say \"snaked main line, cleared roots, ran camera\" and get back a description "
             "that explains to a homeowner what they paid for — which is what stops the "
             "\"why was it $450?\" call three days later."),
            ("Offline, genuinely",
             "Build the whole quote in a basement with zero bars. It syncs when you come "
             "back up the stairs."),
        ],
        "line_items": [
            ("Emergency call-out (after hours)", "flat", "$150 – $350"),
            ("Standard service call / diagnostic", "flat", "$75 – $150"),
            ("Labour — journeyman plumber", "per hour", "$75 – $130"),
            ("Drain snaking / auger, main line", "flat", "$150 – $400"),
            ("Water heater replacement (40–50 gal, tank)", "flat", "$1,200 – $2,500"),
            ("Toilet reset / wax ring replacement", "flat", "$130 – $280"),
            ("Supply line + shut-off valve replacement", "each", "$90 – $180"),
            ("Camera inspection of main line", "flat", "$200 – $450"),
        ],
        "faqs": [
            ("Can I invoice a plumbing job with no cell signal?",
             "Yes — this is the reason a lot of plumbers use Toolbelt. Quotes and invoices "
             "are created and stored on the phone. Nothing needs a connection until you send "
             "it, and it syncs by itself when you have signal again."),
            ("Can I add the parts I used from van stock?",
             "Yes. Add them as line items with your own markup, and save the ones you use "
             "constantly so they are two taps next time."),
            ("Will it handle after-hours or emergency rates?",
             "Save an emergency call-out as a saved line item at your rate and drop it on "
             "the invoice. The app does not set your prices — you do."),
            ("Can I send a quote and turn it into an invoice when the job's done?",
             "Yes, and that is the normal flow: quote on site, customer accepts, convert to "
             "an invoice when the work is finished. You are not retyping anything."),
        ],
        "payment": [
            "Plumbing splits into two payment realities. Emergency and service work should be paid on completion, on site, before you leave — the customer's motivation to pay is never higher than the moment the water stops. Take the card there and then, or send the invoice from the driveway with a payment link while gratitude is still fresh.",
            'Fixture installs and re-pipes are different: they carry real material cost, and you should not be funding a $1,800 water heater out of your own pocket. Ask for a deposit that covers materials — 30–50% is normal and nobody will blink — and invoice the balance on completion. If a customer refuses any deposit on a job with significant materials, that is information about how the final invoice is going to go.',
        ],
        "checklist": [
            'The specific fixture or section of pipe you worked on, named',
            'Whether it was a repair or a replacement',
            'Parts used, listed separately from labour',
            'Emergency or after-hours premium, shown as its own line',
            'Any code-required work you had to do that they did not ask for',
            'Warranty on the work, in writing',
        ],
        "siblings": ["hvac", "electricians", "handymen"],
    },

    # ------------------------------------------------------------ electricians --
    "electricians": {
        "name": "Electricians",
        "singular": "electrician",
        "title": "Invoice & Quote App for Electricians | Toolbelt",
        "desc": ("Send electrical quotes and invoices from the job. Voice input, AI "
                 "descriptions, offline mode. Built for sparkies on iPhone. Free to start."),
        "h1": "The quote and invoice app for electricians",
        "keyword": "electrician quote app iphone",
        "intro": [
            "Electrical work is quoted more than almost any other trade. A panel upgrade, a "
            "rewire, a new circuit for a hot tub — the customer wants a number in writing "
            "before you touch anything, and the quote you send is competing with two others "
            "that landed the same day.",
            "Toolbelt is built so the quote goes out while you are still in the driveway, "
            "not three days later when the customer has already booked someone else. Speak "
            "the scope, let the app write it up properly, send it as a clean PDF, and turn "
            "it into an invoice with one tap when the job is done.",
        ],
        "pains": [
            ("The quote that goes out three days late and loses the job",
             "You did the site visit on Tuesday. You wrote the quote on Friday night. By "
             "then the homeowner had two other numbers and picked one. Speed is not a nice-"
             "to-have in electrical quoting; it is most of the win."),
            ("Explaining code-required work to a customer who thinks you're padding",
             "AFCI breakers, a bonded ground, a dedicated circuit — the homeowner did not "
             "ask for any of it and suspects you invented it. A line item that says "
             "\"AFCI/GFCI breaker, required by code for this circuit\" ends that conversation "
             "before it starts. A line item that says \"breaker — $95\" starts it."),
            ("Panel and permit work priced from memory",
             "Permit fees, inspection call-backs, the second trip because the inspector "
             "wanted something moved — these get eaten because they were never on the "
             "original quote and it feels awkward to add them after."),
            ("Quoting from a job site with no service",
             "New construction has no power and often no signal. That is exactly where you "
             "are doing rough-in walkthroughs and pricing the job."),
        ],
        "features": [
            ("Quote on site, invoice on completion",
             "Build the quote in the driveway, send it before you drive away. When the work "
             "is done, convert the same document to an invoice — no retyping the scope."),
            ("AI descriptions that explain code work",
             "Describe it plainly — \"added dedicated 20A circuit for the garage freezer, "
             "AFCI breaker\" — and get a description the customer understands well enough "
             "not to phone you about it."),
            ("Voice input with gloved hands",
             "Speak the scope while you are coiling up. Line items get written for you."),
        ],
        "line_items": [
            ("Service call / diagnostic", "flat", "$90 – $180"),
            ("Labour — licensed electrician", "per hour", "$85 – $150"),
            ("Panel upgrade, 100A to 200A", "flat", "$1,800 – $4,000"),
            ("New dedicated 20A circuit", "each", "$250 – $600"),
            ("AFCI / GFCI breaker (code-required)", "each", "$60 – $140"),
            ("Recessed light install (per fixture)", "each", "$120 – $250"),
            ("EV charger install (Level 2, 240V)", "flat", "$600 – $1,600"),
            ("Permit + inspection fee (pass-through)", "flat", "at cost"),
        ],
        "faqs": [
            ("Can I send a quote and convert it to an invoice later?",
             "Yes — this is the core flow. Quote on the site visit, and when the customer "
             "says go and the work is finished, the same document becomes the invoice."),
            ("Can I show permit fees as a pass-through?",
             "Yes. Add it as a line item at cost and label it as such — customers are far "
             "happier about a fee they can see is not marked up."),
            ("Does it work on a new-build with no power or signal?",
             "Yes. Everything works offline and syncs later."),
            ("Can I put my licence number on the document?",
             "Yes — your business details, licence number and logo go on every quote and "
             "invoice you send."),
        ],
        "payment": [
            'Electrical quoting is a speed game, but payment is a staging game. On anything above a service call, structure it: a deposit on acceptance, a payment at rough-in, and the balance on final inspection. That way you are never more than one stage out of pocket, and the customer has a clear reason to keep the job moving.',
            'The specific thing that costs electricians money is the permit and inspection cycle. Quote the permit as a pass-through line at cost, and state plainly that a re-inspection caused by something outside your control is billable. Say it up front, on the quote, and it is a term. Say it afterwards, on the invoice, and it is a fight.',
        ],
        "checklist": [
            'The circuits, panel or fixtures you actually worked on',
            'Code-required items, explicitly labelled as code-required',
            'Permit and inspection fees, shown at cost as a pass-through',
            'Your licence number',
            'Materials separated from labour',
            'Whether the work has passed inspection, and when',
        ],
        "siblings": ["plumbers", "hvac", "general-contractors"],
    },

    # -------------------------------------------------------------------- hvac --
    "hvac": {
        "name": "HVAC Contractors",
        "singular": "HVAC contractor",
        "title": "Invoice App for HVAC Contractors | Toolbelt",
        "desc": ("Quote installs, bill service calls and invoice maintenance plans from the "
                 "truck. Voice input, AI descriptions, offline. Free to start."),
        "h1": "The invoice app for HVAC contractors",
        "keyword": "hvac invoicing software",
        "intro": [
            "HVAC has two completely different billing problems in one business. The service "
            "side is high-volume and low-value: twelve calls a week, each one a diagnostic "
            "fee plus parts, all of which needs to be invoiced fast or not at all. The "
            "install side is the opposite: a $9,000 system replacement that lives or dies on "
            "a quote the customer will compare against two others.",
            "Toolbelt handles both without making the service call feel like filling in a "
            "form. Speak the diagnostic and the parts on the way back to the truck; build "
            "the install quote on the spot while the customer is still standing next to the "
            "old furnace.",
        ],
        "pains": [
            ("Twelve service calls, twelve invoices, none of them written",
             "The maintenance and service side of HVAC only works if the invoice goes out "
             "the same day. Twelve calls in a week is twelve invoices, and if they pile up "
             "to Friday you will get half of them wrong and send the rest late."),
            ("Seasonal cash flow that punishes slow invoicing",
             "You make your year in two windows — the first heatwave and the first freeze. "
             "In those weeks you cannot afford to be doing paperwork at 10pm, and you "
             "absolutely cannot afford to be invoicing three weeks late when the money is "
             "needed to buy the next unit."),
            ("System replacement quotes that need to look serious",
             "Nobody signs a $9,000 furnace-and-coil job off the back of a handwritten note. "
             "The quote has to look like it came from a real business, itemised, with the "
             "model numbers on it — and it has to arrive while you are still the person they "
             "remember."),
            ("Attics in August, crawlspaces in January",
             "The work happens in the least connected, least comfortable parts of a house. "
             "You are not doing careful data entry up there."),
        ],
        "features": [
            ("Voice input between calls",
             "Speak the diagnostic and the parts while you walk back to the truck. The "
             "invoice for the last call is written before you start the next one."),
            ("Itemised install quotes that look like a real business sent them",
             "Model numbers, labour, permits, disposal of the old unit — all as separate "
             "line items on a branded PDF."),
            ("Photos on the document",
             "Attach the photo of the cracked heat exchanger to the quote. It is the single "
             "most persuasive thing on the page, and it stops the \"do I really need this?\" "
             "conversation."),
        ],
        "line_items": [
            ("Diagnostic / service call fee", "flat", "$85 – $180"),
            ("Labour — HVAC technician", "per hour", "$80 – $150"),
            ("Furnace replacement (80% AFUE, installed)", "flat", "$3,000 – $6,500"),
            ("AC condenser replacement (2–3 ton, installed)", "flat", "$3,500 – $7,500"),
            ("Annual maintenance plan (2 visits)", "per year", "$150 – $350"),
            ("Refrigerant recharge (per lb, R-410A)", "per lb", "$70 – $160"),
            ("Capacitor / contactor replacement", "each", "$150 – $400"),
            ("Duct cleaning / sealing", "flat", "$400 – $1,200"),
        ],
        "faqs": [
            ("Can I bill a maintenance plan on a schedule?",
             "You can save the plan as a line item and invoice it each time it comes round. "
             "Toolbelt does not run automatic recurring billing — if that is essential to "
             "your business, a field-service platform like Jobber will serve you better and "
             "we would rather tell you that than sell you the wrong tool."),
            ("Can I attach a photo of the failed part?",
             "Yes, and you should. A photo of a cracked heat exchanger on the quote does "
             "more selling than any wording you can write."),
            ("Can I quote a full system install with model numbers?",
             "Yes — as many itemised lines as you need, on a branded PDF."),
            ("Does it work in an attic with no signal?",
             "Yes. Everything works offline."),
        ],
        "payment": [
            'The service side should be paid on the day. A diagnostic fee plus parts, invoiced from the truck, paid before you drive off. If you let those accumulate you will be chasing forty small amounts at the end of the month, and the effort of chasing will exceed the value of several of them.',
            'System installs need a deposit — a full furnace-and-coil replacement can be five figures of equipment ordered on your credit before a single hour is billed. Take 30–50% on signing to cover the equipment, and invoice the balance on commissioning. In peak season this is not optional: it is the difference between taking the next job and telling someone you cannot afford to start it.',
        ],
        "checklist": [
            'Model and serial numbers of any equipment installed',
            'Diagnostic findings, in plain language',
            'Refrigerant added, by type and weight (you may be legally required to log this)',
            'Labour separated from parts',
            'Warranty terms on both the equipment and your labour',
            'The date of the next recommended service',
        ],
        "siblings": ["plumbers", "electricians", "general-contractors"],
    },

    # --------------------------------------------------------------- carpenters --
    "carpenters": {
        "name": "Carpenters",
        "singular": "carpenter",
        "title": "Invoice App for Carpenters | Toolbelt",
        "desc": ("Quote and invoice carpentry work — trim, framing, decks, built-ins — from "
                 "the job. Voice input, AI descriptions, offline. Free to start."),
        "h1": "The invoice app for carpenters",
        "keyword": "invoice app for carpenters",
        "intro": [
            "Carpentry bills in a way most invoicing apps do not understand. The job is "
            "rarely one line. It is materials at one markup, labour at another, a change the "
            "customer asked for halfway through, and a finish detail that took a day longer "
            "than anyone expected because the walls were not square.",
            "Toolbelt lets you itemise all of that properly and quickly, so the invoice "
            "reflects what you actually did rather than a round number you picked because "
            "writing it out felt like too much work.",
        ],
        "pains": [
            ("Materials and labour blurred into one number",
             "When \"build the deck — $6,400\" is the whole invoice, every conversation about "
             "it becomes a negotiation. Split the lumber, the fasteners, the labour and the "
             "finish, and there is nothing to argue with — each line is either right or it "
             "is not."),
            ("Scope creep with no paper trail",
             "\"While you're here, could you just...\" is how carpenters lose a day a week. "
             "If it is not on a document the moment it is agreed, it is free work."),
            ("Waste, offcuts and the second trip to the lumber yard",
             "The material you bought and the material you used are not the same number, and "
             "the difference is yours to eat unless it is priced in."),
            ("Quoting custom work you have never built before",
             "Every built-in is a one-off. There is no price book. The quote has to be "
             "itemised enough that you can defend it and detailed enough that you do not "
             "under-price your own time."),
        ],
        "features": [
            ("Line items that separate materials from labour",
             "Bill the lumber at your markup, the hours at your rate, and the finish work "
             "separately. The customer sees where the money went."),
            ("Voice-note the change the moment it's agreed",
             "The customer asks for an extra shelf while you have a nail gun in your hand. "
             "Speak it into the phone. It is on the document before you forget it existed."),
            ("Photos of the finished work on the invoice",
             "A photo of the finished trim on the invoice is a quiet argument for the price, "
             "and it is the thing they will forward to a friend who needs a carpenter."),
        ],
        "line_items": [
            ("Labour — finish carpenter", "per hour", "$55 – $110"),
            ("Labour — framing carpenter", "per hour", "$50 – $95"),
            ("Deck build (pressure-treated, per sq ft, installed)", "per sq ft", "$25 – $50"),
            ("Interior trim / baseboard install", "per linear ft", "$3 – $10"),
            ("Crown moulding install", "per linear ft", "$6 – $16"),
            ("Custom built-in / shelving unit", "flat", "$800 – $4,000"),
            ("Interior door hang (pre-hung)", "each", "$120 – $300"),
            ("Materials — lumber and fasteners", "at cost + markup", "cost + 10–25%"),
        ],
        "faqs": [
            ("Can I bill materials and labour separately?",
             "Yes, and for carpentry you should. Separate lines make the invoice defensible "
             "and stop the whole job being treated as one negotiable number."),
            ("How do I handle a change the customer asked for mid-job?",
             "Add it as a line item the moment it is agreed — voice input takes about ten "
             "seconds — and send an updated quote. Verbal changes are unpaid changes."),
            ("Can I attach photos of the finished work?",
             "Yes. Photos on the invoice are the cheapest marketing you will ever do."),
            ("Can I save line items I use on every job?",
             "Yes — save your hourly rates and standard items once and reuse them."),
        ],
        "payment": [
            'Carpentry is the trade where scope creep does the most damage, so your payment structure has to make changes visible. Deposit on acceptance to cover materials, a progress payment at an agreed midpoint on anything running more than a week, balance on completion. The midpoint payment is the important one — it is a natural checkpoint where any changes get documented and re-priced rather than absorbed.',
            "Never carry the lumber. Material prices move, and you have no business taking that risk on someone else's project. A deposit that covers materials is standard, defensible, and the single easiest thing to ask for.",
        ],
        "checklist": [
            'Materials listed separately, with the markup either shown or built in consistently',
            'Labour by hour or by stage — pick one and be consistent',
            'Any change the customer asked for, with the date it was agreed',
            'What is NOT included (finishing, painting, hardware) so it cannot be assumed',
            'Photos of the finished work',
        ],
        "siblings": ["general-contractors", "drywall", "painters"],
    },

    # ----------------------------------------------------------------- painters --
    "painters": {
        "name": "Painters",
        "singular": "painter",
        "title": "Invoice App for Painters | Toolbelt",
        "desc": ("Quote by the square foot, bill by the room, invoice from the job. Voice "
                 "input, AI descriptions, works offline. Free to start."),
        "h1": "The invoice app for painters",
        "keyword": "invoice app for painters",
        "intro": [
            "Painting is quoted on a walkthrough and won or lost on how fast the number "
            "arrives. You walk a house, count the rooms, look at the ceilings, notice the "
            "sixteen-foot stairwell that is going to need scaffolding — and the customer "
            "wants a price. If it takes you until the weekend to send it, you are not in the "
            "running.",
            "Toolbelt is designed so the quote leaves before you do. Speak the rooms as you "
            "walk them, let it write up the prep and the coats properly, and send a clean "
            "PDF from the driveway.",
        ],
        "pains": [
            ("Prep work that never makes it onto the quote",
             "Sanding, filling, caulking, masking, priming the patch — prep is most of a "
             "good paint job and the first thing that gets left off the estimate. Then the "
             "customer compares your number to a cheaper quote from someone who is not going "
             "to do any of it, and you look expensive."),
            ("Quoting a whole house from memory in the truck",
             "By the third bedroom you have lost count of the closets. Speak each room into "
             "the phone as you walk it and the quote writes itself."),
            ("Coats, primer and the difference between them",
             "\"Two coats\" and \"primer plus two coats\" are different jobs at different "
             "prices, and if the quote does not say which one you sold, the customer will "
             "assume the more expensive one."),
            ("Getting paid for the ceiling nobody mentioned",
             "The ceilings, the trim, the closet interiors, the inside of the front door — "
             "all of it gets assumed into the price unless the document is explicit."),
        ],
        "features": [
            ("Voice-quote room by room",
             "Walk the house talking: \"master bedroom, walls and ceiling, two coats, "
             "patch the corner.\" You get an itemised quote instead of a number scrawled on "
             "the back of a business card."),
            ("Prep as its own line item",
             "Put the sanding, filling and masking on the page where the customer can see "
             "it. It is the single best defence against the cheaper quote from someone who "
             "is going to skip it."),
            ("Photos before and after",
             "Attach the before photo to the quote and the after photo to the invoice."),
        ],
        "line_items": [
            ("Interior painting — walls (per sq ft, 2 coats)", "per sq ft", "$2 – $6"),
            ("Interior painting — per room (10x12, walls only)", "per room", "$300 – $800"),
            ("Ceiling paint", "per sq ft", "$1 – $3"),
            ("Trim, baseboard and door casing", "per linear ft", "$2 – $6"),
            ("Prep — sanding, filling, caulking, masking", "per hour", "$40 – $75"),
            ("Primer coat (new drywall or heavy patch)", "per sq ft", "$0.60 – $1.50"),
            ("Exterior painting (per sq ft, 2 coats)", "per sq ft", "$2 – $5"),
            ("Materials — paint and sundries", "at cost + markup", "cost + 10–20%"),
        ],
        "faqs": [
            ("Can I quote by the square foot and by the room?",
             "Yes — mix units freely on the same document. Square feet for the walls, a flat "
             "rate for the stairwell, hours for the prep."),
            ("How do I stop losing jobs to cheaper quotes?",
             "Itemise the prep. Most cheap quotes are cheap because they are not doing it, "
             "and a customer who can see the difference on paper will often pay for it."),
            ("Can I add before-and-after photos?",
             "Yes, on both the quote and the invoice."),
            ("Does it work outside with no signal?",
             "Yes. Exterior jobs, rural properties, new builds — it all works offline."),
        ],
        "payment": [
            'For interior repaints, a deposit covers your paint and gets you a customer with skin in the game. For anything over a few days, bill progressively — by room or by floor — rather than waiting until the end. A painter who invoices only on completion is financing the job and taking all the risk of a customer who decides, at the very end, that they do not like the colour they chose.',
            'The single most useful term you can put on a painting quote: what counts as done. "Two coats, cut in, one touch-up visit within 30 days" is a finish line. Without one, you will be back three times.',
        ],
        "checklist": [
            'The rooms and surfaces covered — walls, ceilings, trim, doors, closets, each named',
            'Number of coats, and whether primer is included',
            'Prep work as its own line, so its value is visible',
            'Paint brand, line and finish (customers care, and it protects you)',
            'What counts as complete, and the touch-up policy',
        ],
        "siblings": ["drywall", "carpenters", "handymen"],
    },

    # ------------------------------------------------------------- landscapers --
    "landscapers": {
        "name": "Landscapers",
        "singular": "landscaper",
        "title": "Invoice App for Landscapers | Toolbelt",
        "desc": ("Bill recurring maintenance and one-off installs from the truck. Voice "
                 "input, AI descriptions, works with no signal. Free to start."),
        "h1": "The invoice app for landscapers",
        "keyword": "landscaping invoice app",
        "intro": [
            "Landscaping bills in two shapes that fight each other. There is the maintenance "
            "round — the same forty lawns every fortnight, small amounts, high volume, and "
            "utterly unforgiving of slow invoicing. And there is the install: a patio, a "
            "retaining wall, a full re-turf, quoted like a construction job.",
            "Toolbelt is fast enough for the round and detailed enough for the install. Speak "
            "each property as you leave it and the invoices are written by the time you are "
            "back at the yard.",
        ],
        "pains": [
            ("Forty small invoices are worse than one big one",
             "A $60 lawn cut is not worth ten minutes of paperwork — which is exactly why "
             "maintenance invoicing slips, and why landscapers end up chasing a month of "
             "small money all at once."),
            ("Weather chaos in the schedule and the billing",
             "Rain moves everything. The job you did was not the job you planned, and the "
             "invoice has to reflect what actually happened, not the schedule."),
            ("Install quotes competing on price alone",
             "A patio quote with one line on it is competing purely on the number. Itemise "
             "the excavation, the base, the materials and the labour and you are competing "
             "on what the customer actually gets."),
            ("Materials by volume, priced badly",
             "Mulch by the yard, stone by the ton, sod by the roll — get the volume wrong on "
             "the quote and you eat the difference."),
        ],
        "features": [
            ("Invoice the round from the truck",
             "Speak the property and the work as you pull away. The invoice is done before "
             "the next driveway."),
            ("Save your regulars as reusable line items",
             "The fortnightly cut, the hedge trim, the leaf clear — saved once, two taps "
             "thereafter."),
            ("Itemised install quotes",
             "Excavation, base, materials, labour, disposal, each on its own line."),
        ],
        "line_items": [
            ("Lawn maintenance — mow, edge, blow", "per visit", "$40 – $90"),
            ("Labour — landscape crew", "per hour", "$45 – $90"),
            ("Mulch supply and spread", "per cu yd", "$70 – $140"),
            ("Sod supply and lay", "per sq ft", "$1.50 – $4"),
            ("Paver patio (installed, incl. base)", "per sq ft", "$15 – $35"),
            ("Retaining wall (block, installed)", "per face ft", "$25 – $60"),
            ("Hedge and shrub trimming", "per hour", "$50 – $95"),
            ("Green waste haul-away and disposal", "per load", "$60 – $200"),
        ],
        "faqs": [
            ("Can I invoice a recurring maintenance customer quickly?",
             "Yes — save their standard visit as a line item and it is two taps. Toolbelt "
             "does not auto-bill on a schedule; if fully automatic recurring billing is the "
             "core of your business, a field-service platform is a better fit and we will "
             "say so."),
            ("Can I quote a patio or wall install properly?",
             "Yes — itemise excavation, base, materials, labour and disposal on a branded "
             "PDF."),
            ("Does it work at a rural property with no signal?",
             "Yes. Everything works offline and syncs later."),
            ("Can I bill by volume — cubic yards, tons, rolls?",
             "Yes, any unit you like, on any line."),
        ],
        "payment": [
            'Maintenance rounds should be billed on a fixed cycle and, ideally, paid automatically. The economics of a $60 lawn cut do not survive a two-week chase. Get the round onto a regular invoice the customer expects, and be ruthless about sending it the same day every time.',
            "Installs are construction jobs and should be treated like them: deposit covering materials, progress payment if it runs long, balance on completion. Stone, sod and plants are paid for before they arrive — do not let a customer's cash flow become yours.",
        ],
        "checklist": [
            'The property address, if you service several for one owner',
            'The date of the visit — critical when you are billing a round',
            'Materials by volume: yards of mulch, tons of stone, rolls of sod',
            'Disposal and haul-away as a separate line',
            'Any plant warranty or replacement policy',
        ],
        "siblings": ["handymen", "general-contractors", "carpenters"],
    },

    # ---------------------------------------------------------------- handymen --
    "handymen": {
        "name": "Handymen",
        "singular": "handyman",
        "title": "Invoice App for Handymen | Toolbelt",
        "desc": ("Six jobs a day, six invoices, none of them at 9pm. Voice input, AI "
                 "descriptions, works offline. Free for 3 documents a month."),
        "h1": "The invoice app for handymen",
        "keyword": "handyman invoice app",
        "intro": [
            "The handyman billing problem is not complexity — it is volume and size. Six "
            "jobs in a day, none of them big enough to justify twenty minutes of paperwork, "
            "all of them needing an invoice. So the invoices pile up, and Sunday evening "
            "gets eaten by admin for work you did on Tuesday and can barely remember.",
            "Toolbelt exists to make the invoice cost less time than the job is worth. Speak "
            "it in the driveway, send it before you pull away, and get your Sunday back.",
        ],
        "pains": [
            ("The $90 job that isn't worth the paperwork",
             "When the invoice takes ten minutes and the job was worth ninety dollars, you "
             "have just cut your effective rate. Most handymen respond by batching the "
             "paperwork — and batched paperwork is late, wrong, and sometimes never done."),
            ("Six different jobs, six different customers, one memory",
             "By Thursday you genuinely cannot remember whether the Wilsons' job included "
             "the door handle or not. That uncertainty costs money in both directions."),
            ("Wildly varied work with no price book",
             "A day might be a leaking tap, a fence panel, a TV mount and a sticking door. "
             "There is no standard price list for that, and every invoice is written from "
             "scratch."),
            ("Getting paid on the spot",
             "For small jobs the best moment to be paid is while you are still standing "
             "there. That requires the invoice to exist while you are still standing there."),
        ],
        "features": [
            ("Invoice in the driveway, before you drive away",
             "Voice input plus AI wording means the whole invoice takes under a minute. "
             "That is the entire product proposition for a handyman."),
            ("A saved list of everything you actually do",
             "Build up your own list of common jobs and rates. After a few weeks most of "
             "your invoices are taps, not typing."),
            ("Photos as your receipt",
             "A photo of the finished work attached to the invoice ends most disputes before "
             "they start."),
        ],
        "line_items": [
            ("Call-out / minimum charge (first hour)", "flat", "$75 – $150"),
            ("Labour — handyman", "per hour", "$50 – $100"),
            ("TV wall mount (incl. bracket fitting)", "flat", "$100 – $250"),
            ("Door adjustment / re-hang", "each", "$75 – $200"),
            ("Fence panel repair or replacement", "per panel", "$80 – $250"),
            ("Tap / faucet replacement", "each", "$90 – $220"),
            ("Furniture assembly", "per hour", "$45 – $85"),
            ("Materials and parts", "at cost + markup", "cost + 10–20%"),
        ],
        "faqs": [
            ("How fast can I actually send an invoice?",
             "Under a minute for a typical small job once you have your common items saved. "
             "That is the point — if it takes longer than that, you will not do it on site, "
             "and if you do not do it on site it will slip."),
            ("Is there a free version?",
             "Yes — 3 documents per month, free forever, with every feature on. No "
             "card required. If you send more than that, it is $14.99/mo or $99.99/yr."),
            ("Can I take a deposit for a bigger job?",
             "Yes — put a deposit line on the quote and invoice the balance on completion."),
            ("Can I charge a minimum call-out?",
             "Yes. Save it as a line item at your rate and it goes on every job."),
        ],
        "payment": [
            'Get paid on site. This is the whole strategy. For jobs of this size, the moment the customer is happiest and most willing is the moment you finish — and every hour after that reduces both. An invoice sent from the driveway with a payment link is worth more than a better invoice sent on Sunday.',
            'For anything above a few hundred dollars in materials, take a deposit. It is not about the money so much as the commitment: a customer who has paid a deposit does not cancel on you the morning of.',
        ],
        "checklist": [
            'A clear description of each separate job — not one lumped line',
            'Your minimum call-out charge, if it applied',
            'Materials you supplied, at cost or with markup',
            'Photos of the completed work',
            'How to pay, on the invoice, with as little friction as possible',
        ],
        "siblings": ["carpenters", "painters", "plumbers"],
    },

    # ------------------------------------------------------- general contractors --
    "general-contractors": {
        "name": "General Contractors",
        "singular": "general contractor",
        "title": "Invoice App for General Contractors | Toolbelt",
        "desc": ("Progress billing, deposits and change orders on jobs that run for months. "
                 "Voice input, AI descriptions, offline. Free to start."),
        "h1": "The invoice app for general contractors",
        "keyword": "general contractor invoicing software",
        "intro": [
            "A general contractor's billing problem is time. The job runs for six weeks or "
            "six months, the money comes in stages, subs need paying before the client pays "
            "you, and the scope changes twice a month. The invoice is not an event at the "
            "end — it is a running account.",
            "Toolbelt handles the documents: the deposit, the progress bills, the change "
            "orders and the final invoice, all itemised and all sent from wherever you "
            "happen to be standing. It is deliberately not a project management platform, "
            "and if that is what you need we will point you at one.",
        ],
        "pains": [
            ("Financing the job out of your own pocket",
             "You pay the subs and the supply house on your terms and get paid on the "
             "client's. Every week that an invoice sits unwritten is a week you are lending "
             "the client money at zero percent."),
            ("Change orders agreed verbally and never billed",
             "This is where GCs lose the most money. A change agreed on site and not "
             "documented within the day is a change you did for free, and on a long job "
             "there will be a dozen of them."),
            ("Progress billing that the client disputes",
             "\"Stage two — $18,000\" invites a fight. An itemised progress bill showing "
             "exactly what was completed in that stage does not."),
            ("Deposits that aren't taken, or aren't big enough",
             "The deposit is what stops you funding the materials on your own credit. If it "
             "is not on the quote it is very hard to introduce later."),
        ],
        "features": [
            ("Deposits and progress bills as first-class documents",
             "Quote with a deposit line. Invoice each stage as it completes, itemised."),
            ("Document the change the day it happens",
             "Speak it into the phone on site and send a revised quote the same afternoon. "
             "The discipline matters more than the tool, but the tool is what makes the "
             "discipline survive a bad week."),
            ("Every document branded and consistent",
             "On a six-figure job the paperwork is part of how the client decides whether "
             "you are a real business."),
        ],
        "line_items": [
            ("Deposit / mobilisation (on signing)", "% of contract", "10 – 30%"),
            ("Progress billing — stage completion", "per stage", "as scheduled"),
            ("Labour — general contractor / PM", "per hour", "$75 – $150"),
            ("Subcontractor cost (pass-through + markup)", "at cost + markup", "cost + 10–20%"),
            ("Materials (pass-through + markup)", "at cost + markup", "cost + 10–20%"),
            ("Change order — additional scope", "per order", "priced per change"),
            ("Permit and inspection fees", "at cost", "at cost"),
            ("Site clean-up and disposal", "flat", "$300 – $1,500"),
        ],
        "faqs": [
            ("Can I do progress billing?",
             "Yes — invoice each stage as its own itemised document against the original "
             "quote."),
            ("Does Toolbelt do formal change-order tracking?",
             "Not as a dedicated workflow. You can document a change and send a revised "
             "quote in under a minute, which covers most one- and two-person GCs. If you "
             "need a formal change-order register with approvals, Joist's Elite tier or a "
             "full PM platform will serve you better — see our "
             "<a href=\"../../compare/toolbelt-vs-joist/\">Joist comparison</a>."),
            ("Can I show subcontractor costs as pass-through?",
             "Yes, with or without your markup shown as a separate line."),
            ("Can I take a deposit before starting?",
             "Yes, and you should. Put it on the quote as a line item so it is agreed up "
             "front rather than negotiated later."),
        ],
        "payment": [
            "Progress billing is the whole job. A schedule of values agreed before you start — deposit, stages tied to milestones, retainage if applicable, final payment on completion — is what keeps you from financing someone's renovation out of your own line of credit. Agree the stages in writing on the quote, and invoice the moment each one completes, not at the end of the month.",
            'The killer is change orders. On a long job you will have a dozen, each one agreed in a two-minute conversation on site. Every one of them that is not documented and priced the same day is money you have donated. Make it a rule that no change proceeds without a revised quote sent, even a one-line one.',
        ],
        "checklist": [
            'The stage being billed and what it covered, itemised',
            'The original contract value and what remains',
            'Change orders as separate, dated, individually-priced lines',
            'Subcontractor costs and whether markup is included',
            'Permit and inspection fees, at cost',
            'Retainage held, if applicable',
        ],
        "siblings": ["carpenters", "electricians", "roofers"],
    },

    # ----------------------------------------------------------------- roofers --
    "roofers": {
        "name": "Roofers",
        "singular": "roofer",
        "title": "Invoice App for Roofers | Toolbelt",
        "desc": ("Quote roofs by the square, take deposits, invoice on completion. Voice "
                 "input, AI descriptions, works offline. Free to start."),
        "h1": "The invoice app for roofers",
        "keyword": "roofing invoice app",
        "intro": [
            "Roofing is a big-ticket, one-shot sale. The customer is spending five figures "
            "with someone they met once, usually under time pressure because there is water "
            "coming in, and often with an insurance company involved. The quote is doing an "
            "enormous amount of work — it has to justify the number, look like it came from "
            "a business that will still exist in ten years, and arrive before the other two.",
            "Toolbelt gets that document out fast and makes it look serious: itemised by "
            "square, with the tear-off, the underlayment, the flashing and the disposal all "
            "priced separately, and photos of the damage attached.",
        ],
        "pains": [
            ("A five-figure quote that has to be trusted on sight",
             "Nobody hands over $14,000 on the basis of a number written on a notepad. The "
             "quote is the entire trust-building exercise, and it is competing against two "
             "others that landed the same week."),
            ("Deposits, because you cannot float the materials",
             "A roof's worth of shingles is thousands of dollars of your money before a "
             "single nail goes in. No deposit means you are financing the job."),
            ("Insurance jobs with their own paperwork logic",
             "When there is a claim involved, the document needs to be itemised in a way an "
             "adjuster can read — line by line, with the damage photographed."),
            ("Storm season: quoting ten roofs a week",
             "After a hailstorm the work is there for the taking and it goes to whoever gets "
             "the quote out first. That is a speed problem, not a sales problem."),
        ],
        "features": [
            ("Photos of the damage attached to the quote",
             "The photo from the ridge is the most persuasive thing you have. Put it on the "
             "document."),
            ("Itemise by square, not by guess",
             "Tear-off, decking repair, underlayment, shingles, ridge, flashing, disposal — "
             "each on its own line so the number is defensible."),
            ("Deposit on the quote, balance on completion",
             "Get the materials funded before you buy them."),
        ],
        "line_items": [
            ("Asphalt shingle roof (installed, per square)", "per square (100 sq ft)",
             "$350 – $700"),
            ("Tear-off and disposal of old roof", "per square", "$100 – $250"),
            ("Decking / sheathing replacement", "per sheet", "$60 – $150"),
            ("Underlayment (synthetic / ice & water shield)", "per square", "$40 – $120"),
            ("Ridge vent installation", "per linear ft", "$8 – $20"),
            ("Step / chimney flashing replacement", "each", "$200 – $600"),
            ("Deposit on signing", "% of contract", "25 – 50%"),
            ("Skip / dumpster and haul-away", "flat", "$400 – $900"),
        ],
        "faqs": [
            ("Can I take a deposit before ordering materials?",
             "Yes — put the deposit on the quote as its own line so it is agreed before you "
             "spend your own money on shingles."),
            ("Can I attach photos of the roof damage?",
             "Yes, to both quotes and invoices — and for insurance work you should attach "
             "as many as you can."),
            ("Does it price by the square?",
             "Yes, any unit you like. Squares, linear feet, sheets, flat rates — mix them on "
             "one document."),
            ("Can I quote from the roof with no signal?",
             "Yes. Build the whole thing offline; it syncs when you are back on the ground."),
        ],
        "payment": [
            "Roofing has the biggest deposit requirement of any trade on this list, and the strongest justification for it. A roof's worth of materials is thousands of dollars delivered to a driveway before you have earned a penny. A deposit of 25–50% on signing is standard, and a customer who refuses one is telling you something.",
            "On insurance work, the payment structure is different again: the carrier often pays in two parts, holding back depreciation until the work is complete and documented. Itemise the quote so it maps to the adjuster's scope, photograph everything, and invoice in a way that lets the homeowner claim the second cheque without a fight.",
        ],
        "checklist": [
            'The measured roof area, in squares',
            'Tear-off and disposal, priced separately',
            'Materials by name — shingle brand, underlayment type, ridge and flashing',
            "The manufacturer's warranty AND your workmanship warranty, both stated",
            'Photos of the damage and of the completed roof',
            "For insurance jobs: line items that map to the adjuster's scope",
        ],
        "siblings": ["general-contractors", "hvac", "carpenters"],
    },

    # ----------------------------------------------------------------- drywall --
    "drywall": {
        "name": "Drywall Contractors",
        "singular": "drywall contractor",
        "title": "Invoice App for Drywall Contractors | Toolbelt",
        "desc": ("Bill by the board, the square foot or the finish level. Voice input, AI "
                 "descriptions, works offline. Free to start."),
        "h1": "The invoice app for drywall contractors",
        "keyword": "drywall contractor invoice app",
        "intro": [
            "Drywall is priced in units nobody outside the trade understands — boards, square "
            "feet, and finish levels from 0 to 5 — and that gap is where the arguments come "
            "from. A homeowner who thinks they bought \"drywall\" and receives a Level 3 "
            "finish is going to be unhappy, and the only thing that protects you is a "
            "document that said so up front.",
            "Toolbelt lets you write that document in the time it takes to walk back to the "
            "truck, with the finish level, the board count and the taping all itemised.",
        ],
        "pains": [
            ("Finish levels the customer has never heard of",
             "Level 3, Level 4, Level 5 — these are the whole price difference and they are "
             "invisible to a homeowner. If the quote does not name the level, you will be "
             "asked to sand it again for free."),
            ("Hang, tape, mud, sand — one job or four?",
             "Bidding it as one number hides the labour, and the labour is the job. Broken "
             "out, the price makes sense; lumped together, it looks like a lot of money for "
             "some board."),
            ("The patch job that is worth less than the drive",
             "A single small repair has a minimum price and customers hate it. It needs to be "
             "on the document as a minimum charge, not sprung on them."),
            ("New-build sites with no power and no signal",
             "Drywall goes in before the building has anything. That includes cell service."),
        ],
        "features": [
            ("Name the finish level on the document",
             "Put \"Level 4 finish\" on the quote in writing. It is the single most valuable "
             "line on the page, and it is the one that keeps you off the hook later."),
            ("Bill by board, square foot or stage",
             "Hang, tape, mud and sand as separate lines — or one price with the stages "
             "listed underneath. Either way the customer can see what they bought."),
            ("Offline on new-build sites",
             "No power, no signal, no problem."),
        ],
        "line_items": [
            ("Drywall hang and finish (per sq ft, Level 4)", "per sq ft", "$1.50 – $3.50"),
            ("Board supply and hang only", "per board (4x8)", "$12 – $30"),
            ("Taping and mudding", "per sq ft", "$0.60 – $1.50"),
            ("Level 5 finish upgrade", "per sq ft", "+$0.50 – $1.50"),
            ("Ceiling hang (extra labour)", "per sq ft", "+$0.30 – $0.90"),
            ("Small patch repair (minimum charge)", "flat", "$150 – $400"),
            ("Texture / knockdown finish", "per sq ft", "$0.50 – $1.50"),
            ("Waste and debris disposal", "flat", "$100 – $400"),
        ],
        "faqs": [
            ("Should I put the finish level on the quote?",
             "Always. It is the difference between a Level 3 and a Level 5 price, and it is "
             "the thing customers dispute when it is not written down."),
            ("Can I bill by the board and by the square foot?",
             "Yes, on the same document if the job calls for it."),
            ("Can I set a minimum charge for small patches?",
             "Yes — save it as a line item so it appears every time and never has to be "
             "explained on the phone."),
            ("Does it work on a site with no power or signal?",
             "Yes. Everything is created offline and syncs later."),
        ],
        "payment": [
            'Drywall usually sits mid-chain on a bigger job, which means you are often being paid by a general contractor rather than a homeowner — and GCs pay on their schedule, not yours. Agree the terms before you hang a single board, and put them on the quote: net 15 or net 30, and what happens after that.',
            'For direct-to-homeowner work, take a deposit that covers board and compound. Materials for a full basement are not trivial, and you should not be fronting them.',
        ],
        "checklist": [
            'The finish level — Level 3, 4 or 5 — stated explicitly. This is the most important line on the document',
            'Square footage or board count',
            'Hang, tape, mud and sand broken out, or clearly stated as one price covering all four',
            'Texture, if any, named',
            'Whether disposal of offcuts is included',
            'Payment terms, especially if you are billing a GC',
        ],
        "siblings": ["painters", "carpenters", "general-contractors"],
    },
}
