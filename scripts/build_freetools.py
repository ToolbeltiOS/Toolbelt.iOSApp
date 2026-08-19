#!/usr/bin/env python3
"""
The two link-magnet pages:

    /templates/free-contractor-invoice-template/   PDF + DOCX, generic + 10 trades
    /tools/contractor-hourly-rate-calculator/      a real calculator, no signup

    python3 scripts/build_freetools.py

These are the only two pages on the site with a realistic chance of earning links
passively, so two rules govern them:

  1. NO EMAIL GATE. A free template behind a form is not free, and nobody links to
     a form. The download is a direct link to a file.
  2. THE PAGE MUST BE USEFUL WITHOUT THE APP. If the only value is "and now install
     Toolbelt", it is an ad, and people link to tools, not ads. The calculator
     works entirely client-side and gives you a real number even if you never hear
     of us again.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "content"))

import seo_config as C   # noqa: E402
import shell as S        # noqa: E402
from trades import TRADES  # noqa: E402

TRADE_NAV = [(slug, t["name"]) for slug, t in TRADES.items()]


def write(relpath, content):
    full = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)
    import re
    m = re.search(r"<main>(.*?)</main>", content, re.S)
    body = m.group(1) if m else content
    return relpath, len(re.sub(r"<[^>]+>", " ", body).split())


# --------------------------------------------------------------- templates ----
def build_templates_page():
    depth = 2
    d = "../../templates/downloads"
    gdoc = C.GOOGLE_DOCS_TEMPLATE_URL

    rows = "".join(
        f'<tr><td><strong>{t["name"]}</strong></td>'
        f'<td><a href="{d}/{slug}-invoice-template.pdf" download>PDF</a></td>'
        f'<td><a href="{d}/{slug}-invoice-template.docx" download>Word / Google Docs</a></td>'
        f'<td><a href="../../for/{slug}/">Invoicing guide for {t["name"].lower()}</a></td></tr>'
        for slug, t in TRADES.items())

    gdoc_line = (f'<a class="btn secondary" href="{gdoc}">Open in Google Docs</a>'
                 if gdoc else
                 '<span class="small" style="color:var(--text-muted);font-size:14px">'
                 'The .docx opens directly in Google Docs (File &rarr; Open), Word and '
                 'Pages.</span>')

    body = f"""<div class="prose">
<p>A blank contractor invoice template, free, in PDF and Word. No email address, no
signup, no watermark, no "free trial" that expires. Download it, use it, keep it,
send it to someone else. If you never install our app, that is genuinely fine.</p>

<div class="card" style="text-align:center">
  <h3 style="margin-top:0">Generic contractor invoice template</h3>
  <p>Blank line items. Works for any trade.</p>
  <p>
    <a class="btn" href="{d}/contractor-invoice-template.pdf" download>Download PDF</a>
    &nbsp;
    <a class="btn secondary" href="{d}/contractor-invoice-template.docx" download>Download Word (.docx)</a>
  </p>
  <p style="margin-bottom:0">{gdoc_line}</p>
</div>

<h2>Trade-specific versions</h2>
<p>These are not the same file with a different title. Each one comes with the line
items that trade actually bills for already typed into the description column — a
plumber's starts with an emergency call-out and a drain snake, a roofer's starts with
tear-off and squares — so you are filling in numbers, not staring at a blank grid.</p>
<div class="tablewrap">
<table>
<thead><tr><th>Trade</th><th>PDF</th><th>Editable</th><th>Guide</th></tr></thead>
<tbody>{rows}</tbody>
</table>
</div>

<h2>What has to be on a contractor invoice</h2>
<p>An invoice is a demand for money, and the ones that get paid without a phone call
all contain the same things. Missing any of these is how a two-week payment becomes a
two-month one.</p>
<ul>
  <li><strong>Your business details and licence number.</strong> Name, address, phone,
  email. If your trade is licensed, the number goes on every document — it is a
  credibility signal and in some states a legal requirement.</li>
  <li><strong>The client's name and the job address.</strong> These are often different
  from each other, and the job address is what the client's memory keys off.</li>
  <li><strong>An invoice number.</strong> Sequential. This matters more than it seems:
  it is how you refer to the document on the phone, and how your accountant finds it.</li>
  <li><strong>The date, and the due date.</strong> "Due on receipt" is not a due date,
  it is a hope. Put a real one on it.</li>
  <li><strong>Itemised line items.</strong> The single biggest factor in whether the
  invoice gets queried. "Bathroom work — $1,900" starts an argument. Six lines naming
  the fixtures, the labour and the parts do not.</li>
  <li><strong>Labour separated from materials.</strong> It shows where the money went
  and it makes the number defensible.</li>
  <li><strong>Subtotal, tax, deposit already paid, and the total due.</strong> Show the
  deposit as a deduction — a client who has forgotten they paid it will call you.</li>
  <li><strong>Payment terms and accepted methods.</strong> Net 15, net 30, whatever you
  use, plus what happens if it is late. Terms you did not state are terms you do not
  have.</li>
</ul>
<p>Our <a href="../../blog/professional-invoice-template-guide.html">invoice template
guide</a> goes through each field and what happens when it is missing, and the
<a href="../../blog/contractor-deposit-and-payment-terms.html">deposits and payment terms
guide</a> covers what to ask for up front.</p>

<h2>How to use the template</h2>
<p>The PDF is for printing or filling in on a computer. The .docx is the one to take if
you want to change it: open it in Word, Pages, or Google Docs (File &rarr; Open &rarr;
upload), put your logo at the top, save it as your own, and reuse it forever.</p>
<p>Two suggestions from watching a lot of contractors do this. First, build your standard
line items into your copy once — your call-out fee, your hourly rate, the three things you
do most weeks — so you are never writing them from scratch. Second, save it somewhere you
can reach from your phone, because the invoice you send from the driveway gets paid faster
than the one you write on Sunday night.</p>

<h2>Invoice, quote, estimate — which one are you sending?</h2>
<p>These get used interchangeably and they are not the same document, which is how
contractors end up committed to a price they only meant to indicate.</p>
<ul>
  <li><strong>An estimate</strong> is your best guess. It is not binding, and it should
  say so on its face. Use it when the scope genuinely is not knowable yet — you have not
  opened the wall.</li>
  <li><strong>A quote</strong> is a fixed price for a defined scope. Once the customer
  accepts it, you are on the hook for that number for that work. This is the one to send
  when you know what the job is.</li>
  <li><strong>An invoice</strong> is a demand for payment for work already done. It should
  reference the quote it came from, and any change orders agreed along the way.</li>
</ul>
<p>The expensive mistake is sending an estimate that reads like a quote and then trying to
raise the number later. Our
<a href="../../blog/quote-vs-invoice-when-to-use.html">quote vs invoice guide</a> goes
through it properly.</p>

<h2>Four mistakes that keep the invoice unpaid</h2>
<ul>
  <li><strong>One line for the whole job.</strong> A single number is a single thing to
  argue with. Itemised, each line is either right or it is not.</li>
  <li><strong>No due date.</strong> "Due on receipt" is not enforceable and not a deadline.
  Put a date on it.</li>
  <li><strong>Sending it days later.</strong> The value of your work in a customer's mind
  decays fast. Invoice while they can still see what you did.</li>
  <li><strong>Not showing the deposit.</strong> If they paid one and it is not deducted on
  the page, you will get the phone call — and it undermines every other number on it.</li>
</ul>

<h2>When a template stops being enough</h2>
<p>Honestly: a template is fine, and plenty of contractors run entire businesses on one.
It stops being enough at a predictable point — when you are sending more than a handful a
month, when you keep forgetting which invoice numbers you have used, or when the gap
between finishing a job and writing the paperwork has started costing you real money in
forgotten parts and unbilled changes.</p>
<p>That is the point where an app earns its keep, and it is the point where Toolbelt is
worth a look: you speak the job, it writes the line items, and it sends before you leave
the driveway. It is free for {C.FREE_TIER_DOCS_PER_MONTH} documents a month, so you can
find out on a real job without paying anyone.</p>

{S.cta(depth, "Or skip the paperwork entirely",
       f"Free for {C.FREE_TIER_DOCS_PER_MONTH} documents a month. No card required.",
       "website", "template", "invoice-template")}
</div>"""

    url = "/templates/free-contractor-invoice-template/"
    return write("templates/free-contractor-invoice-template/index.html", S.page(
        depth=depth,
        title="Free Contractor Invoice Template (PDF & Word)",
        desc=("Free contractor invoice template in PDF and Word — plus versions for "
              "plumbers, electricians, roofers and 7 more trades. No email required."),
        url_path=url, kicker="Free template",
        h1="Free contractor invoice template",
        standfirst="PDF and Word. Ten trade-specific versions. No email, no signup, no watermark.",
        body=body, trades=TRADE_NAV,
        breadcrumb=S.breadcrumb_html(depth, [
            ("Home", "../../index.html"), ("Templates", None),
            ("Contractor invoice template", None)]),
        jsonld=[
            S.breadcrumb_ld([("Home", "/"), ("Templates", "/templates/"),
                             ("Contractor invoice template", url)]),
            {"@context": "https://schema.org", "@type": "HowTo",
             "name": "How to fill in a contractor invoice",
             "description": "The fields a contractor invoice needs in order to get paid "
                            "without a follow-up phone call.",
             "step": [
                 {"@type": "HowToStep", "name": "Add your business details",
                  "text": "Business name, address, phone, email and licence number."},
                 {"@type": "HowToStep", "name": "Add the client and the job address",
                  "text": "These are often different; the job address is what the client "
                          "remembers."},
                 {"@type": "HowToStep", "name": "Number and date it",
                  "text": "A sequential invoice number, the date, and a real due date."},
                 {"@type": "HowToStep", "name": "Itemise the work",
                  "text": "Separate lines for labour, materials and any call-out fee. This "
                          "is the single biggest factor in whether the invoice is queried."},
                 {"@type": "HowToStep", "name": "Total it and state your terms",
                  "text": "Subtotal, tax, any deposit already paid deducted, total due, "
                          "payment terms and accepted methods."},
             ]},
        ],
    ))


# -------------------------------------------------------------- calculator ----
CALC_JS = """<script>
(function(){
  var $ = function(id){ return document.getElementById(id); };
  var money = function(n){
    return '$' + n.toLocaleString('en-US', {minimumFractionDigits:0, maximumFractionDigits:0});
  };

  function calc(){
    var target   = Math.max(0, parseFloat($('target').value)   || 0);
    var overhead = Math.max(0, parseFloat($('overhead').value) || 0);
    var weeks    = Math.min(52, Math.max(1, parseFloat($('weeks').value) || 48));
    var hours    = Math.min(80, Math.max(1, parseFloat($('hours').value) || 40));
    var billable = Math.min(100, Math.max(1, parseFloat($('billable').value) || 65));
    var margin   = Math.min(90, Math.max(0, parseFloat($('margin').value) || 20));

    var totalHours    = weeks * hours;
    var billableHours = totalHours * (billable / 100);
    var costBase      = target + overhead;
    var breakeven     = billableHours > 0 ? costBase / billableHours : 0;
    var rate          = margin < 100 ? breakeven / (1 - margin / 100) : breakeven;

    $('billableHours').textContent = Math.round(billableHours).toLocaleString() + ' hrs/yr';
    $('breakeven').textContent = money(breakeven) + '/hr';
    $('rate').textContent = money(rate);
    $('revenue').textContent = money(rate * billableHours);
    $('unbilled').textContent = Math.round(totalHours - billableHours).toLocaleString() + ' hrs/yr';
  }

  ['target','overhead','weeks','hours','billable','margin'].forEach(function(id){
    var el = $(id);
    el.addEventListener('input', calc);
    el.addEventListener('change', calc);
  });
  calc();
})();
</script>"""

CALC_CSS = """<style>
.calc{background:var(--surface-raised);border:1px solid var(--border);
  border-radius:var(--radius-lg);padding:28px;margin:28px 0}
.calc label{display:block;color:var(--text-white);font-weight:600;font-size:15px;
  margin-bottom:5px}
.calc .hint{color:var(--text-muted);font-size:13.5px;font-weight:400;margin-bottom:7px}
.calc .field{margin-bottom:20px}
.calc input{width:100%;padding:12px 14px;background:rgba(0,0,0,.35);
  border:1px solid var(--border-hover);border-radius:var(--radius-sm);
  color:var(--text-white);font-size:16px;font-family:'Outfit',sans-serif}
.calc input:focus{outline:none;border-color:var(--orange)}
.calc-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:18px}
.result{background:linear-gradient(135deg,rgba(232,115,44,.16),rgba(232,115,44,.05));
  border:1px solid rgba(232,115,44,.3);border-radius:var(--radius-md);
  padding:26px;margin-top:22px;text-align:center}
.result .big{font-size:52px;font-weight:800;color:var(--orange-light);line-height:1.1}
.result .lbl{color:var(--text-muted);font-size:13px;letter-spacing:.14em;
  text-transform:uppercase;margin-bottom:6px}
.subresults{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));
  gap:14px;margin-top:22px}
.subresult{background:rgba(0,0,0,.25);border:1px solid var(--border);
  border-radius:var(--radius-sm);padding:14px}
.subresult b{display:block;color:var(--text-white);font-size:19px;margin-top:3px}
.subresult span{color:var(--text-muted);font-size:12.5px}
</style>"""


def build_calculator():
    depth = 2
    url = "/tools/contractor-hourly-rate-calculator/"

    calc = """
<div class="calc">
  <div class="calc-grid">
    <div class="field">
      <label for="target">What you want to earn</label>
      <div class="hint">Your take-home pay, per year, before tax.</div>
      <input type="number" id="target" value="75000" min="0" step="1000">
    </div>
    <div class="field">
      <label for="overhead">Annual overhead</label>
      <div class="hint">Van, insurance, tools, phone, fuel, accountant, software.</div>
      <input type="number" id="overhead" value="18000" min="0" step="500">
    </div>
    <div class="field">
      <label for="weeks">Weeks you work</label>
      <div class="hint">52 minus holiday, sickness and the dead weeks.</div>
      <input type="number" id="weeks" value="48" min="1" max="52">
    </div>
    <div class="field">
      <label for="hours">Hours per week</label>
      <div class="hint">All of them — including the ones in the van.</div>
      <input type="number" id="hours" value="45" min="1" max="80">
    </div>
    <div class="field">
      <label for="billable">Billable hours (%)</label>
      <div class="hint">The honest number. Most trades land at 55&ndash;70%.</div>
      <input type="number" id="billable" value="65" min="1" max="100">
    </div>
    <div class="field">
      <label for="margin">Profit margin (%)</label>
      <div class="hint">On top of covering yourself. This is the bit that grows the business.</div>
      <input type="number" id="margin" value="20" min="0" max="90">
    </div>
  </div>

  <div class="result">
    <div class="lbl">Your hourly rate should be</div>
    <div class="big" id="rate">$0</div>
    <div class="subresults">
      <div class="subresult"><span>Billable hours</span><b id="billableHours">0</b></div>
      <div class="subresult"><span>Break-even rate</span><b id="breakeven">$0</b></div>
      <div class="subresult"><span>Revenue at this rate</span><b id="revenue">$0</b></div>
      <div class="subresult"><span>Unbilled hours</span><b id="unbilled">0</b></div>
    </div>
  </div>
</div>"""

    import re as _re
    rate_rows = ""
    for slug, t in TRADES.items():
        lab = next((li for li in t["line_items"]
                    if "per hour" in li[1] and "abour" in li[0]), None)
        if not lab:
            continue
        rate_rows += (f'<tr><td>{t["name"]}</td><td class="num">{lab[2]}</td>'
                      f'<td><a href="../../for/{slug}/">{t["name"]} invoicing guide</a></td></tr>')

    body = f"""<div class="prose">
<p>Most contractors set their hourly rate by asking what the other guy charges. That is
how an entire trade ends up underpriced together. This calculator works it out from the
only numbers that matter: what you need to earn, what it costs you to show up, and how
many hours you can actually bill.</p>
<p>Nothing is sent anywhere. It runs in your browser, there is no signup, and we cannot
see what you type.</p>

{calc}

<h2>The number that ruins most rates: billable hours</h2>
<p>This is where nearly everyone gets it wrong, so it is worth being blunt about it.</p>
<p>You work, say, 45 hours a week. You do not <em>bill</em> 45 hours a week. You bill the
hours you are on a job with a tool in your hand. You do not bill the drive between jobs,
the trip to the supply house, the quote you wrote that did not land, the hour on the phone
with a customer who is deciding, the invoicing on Sunday night, or the morning you spent
chasing an unpaid bill.</p>
<p>For most one-person trade businesses that lands somewhere between <strong>55% and
70%</strong>. If you have never measured it, start at 65% and be suspicious if you think
you are higher. A contractor who believes they bill 90% of their hours and actually bills
60% has set their rate a third too low — and will work themselves into the ground
wondering why the money never arrives.</p>

<h2>Overhead is not optional and it is not small</h2>
<p>Overhead is everything you pay for whether or not you work a single day this month. The
van and its payments, fuel, insurance (vehicle, liability, tools), your phone, tool
replacement and repair, licensing and continuing education, the accountant, software,
advertising, and the yard or storage if you have one.</p>
<p>Add it up honestly once a year. Most contractors underestimate it by thousands, and
every dollar you miss is a dollar you are paying out of what you thought was your wage.</p>

<h2>Why the profit margin is separate from your pay</h2>
<p>Your target earnings are your wage — what you take home for doing the work. Profit is
different: it is what the <em>business</em> makes on top of paying you and its costs. It is
what buys the second van, survives the slow February, replaces the compressor when it dies
on a Friday, and eventually pays you when you are not the one swinging the hammer.</p>
<p>A business with no margin is a job with extra paperwork and more risk. 15&ndash;25% is a
reasonable place to start.</p>

<h2>What to do with the number</h2>
<p>Treat it as a floor, not a price list. It is the rate below which you are, arithmetically,
working for less than you decided you were worth. Above it, you have room to move — for a
job you want, a client who pays fast, or work in a season when you would otherwise be idle.</p>
<p>And do not quote it. The rate is for <em>you</em>, so you know what a job needs to earn.
Most customers should see a price for the job, not an hourly rate to argue with. Our
<a href="../../blog/how-to-write-an-invoice-as-a-contractor.html">guide to writing an
invoice</a> covers how to present it.</p>

<h2>A worked example</h2>
<p>Take a plumber who wants $75,000 take-home, has $18,000 of overhead, works 48 weeks at
45 hours, bills 65% of those hours, and wants a 20% margin.</p>
<p>That is 2,160 hours worked, of which 1,404 are billable. They need $93,000 to cover
their pay and their costs, which is about $66/hr just to break even. With a 20% margin,
the rate is roughly <strong>$83/hr</strong> — and every hour they bill under that is an
hour they are subsidising the customer.</p>
<p>Now look at the "unbilled hours" box in the calculator. That is 756 hours a year — about
19 working weeks — spent driving, quoting, invoicing and chasing. You cannot get rid of all
of it, but the invoicing and chasing part is the part you can shrink, and that is worth as
much to you as a rate rise.</p>

<h2>What the trades typically charge per hour</h2>
<p>For reference only — a sense check against the number above, not a target. These are
typical US market ranges for labour, and they vary enormously by region, licence and
demand. If the calculator says you need more than the top of your trade's range, that is
not necessarily wrong: it may mean your overhead is too high, your billable percentage is
too low, or you are in a market that will not support what you need. All three are worth
knowing.</p>
<div class="tablewrap">
<table>
<thead><tr><th>Trade</th><th class="num">Typical hourly labour rate</th><th>Guide</th></tr></thead>
<tbody>{rate_rows}</tbody>
</table>
</div>

<h2>Questions people ask about this</h2>
<p class="faq-q">Should I charge hourly or a flat price for the job?</p>
<p>Quote flat prices to customers wherever you can, and use your hourly rate privately to
check the job is worth doing. Customers hate an open-ended hourly meter, and it punishes
you for being fast — which, as you get better, you increasingly are.</p>
<p class="faq-q">My calculated rate is higher than everyone else in my area. Now what?</p>
<p>Then either your costs are higher than theirs, your billable percentage is worse, or
they are underpricing and do not know it. The third is more common than people think. Do
not automatically drop to match a number someone else picked out of the air.</p>
<p class="faq-q">Does this work for a crew, not just one person?</p>
<p>Roughly. Run it once per billable person, with that person's wage as the target and
their share of overhead. It gets less accurate the bigger you get — at that point you
need job costing, not a web calculator.</p>
<p class="faq-q">Is anything I type here stored?</p>
<p>No. It runs entirely in your browser. Nothing is sent to us, and there is no signup.</p>

{S.cta(depth, "Get the invoicing hours back",
       "Speak the job, send the invoice before you leave the driveway. "
       f"Free for {C.FREE_TIER_DOCS_PER_MONTH} documents a month.",
       "website", "tool", "rate-calculator")}
</div>"""

    return write("tools/contractor-hourly-rate-calculator/index.html", S.page(
        depth=depth,
        title="Contractor Hourly Rate Calculator (Free)",
        desc=("Work out what you should charge per hour. Free calculator using your "
              "target pay, overhead and real billable hours. No signup, nothing stored."),
        url_path=url, kicker="Free tool",
        h1="Contractor hourly rate calculator",
        standfirst=("What you should charge, from what you need to earn — not from what "
                    "the other guy is charging."),
        body=body, trades=TRADE_NAV, extra_head=CALC_CSS, extra_js=CALC_JS,
        breadcrumb=S.breadcrumb_html(depth, [
            ("Home", "../../index.html"), ("Tools", None),
            ("Hourly rate calculator", None)]),
        jsonld=[
            S.breadcrumb_ld([("Home", "/"), ("Tools", "/tools/"),
                             ("Hourly rate calculator", url)]),
            {"@context": "https://schema.org", "@type": "WebApplication",
             "name": "Contractor Hourly Rate Calculator",
             "url": C.SITE_URL + url,
             "applicationCategory": "BusinessApplication",
             "operatingSystem": "Any (runs in the browser)",
             "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
             "description": ("Calculates the hourly rate a contractor needs to charge, "
                             "from target earnings, overhead, working weeks and real "
                             "billable-hour percentage.")},
        ],
    ))


if __name__ == "__main__":
    for path, words in [build_templates_page(), build_calculator()]:
        flag = "  ← THIN" if words < 900 else ""
        print(f"  {path:<52} {words:>5} words{flag}")
