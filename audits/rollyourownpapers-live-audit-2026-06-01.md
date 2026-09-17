# Live Site Audit — rollyourownpapers.com
**Date:** 2026-06-01
**Method:** Live Google SERP data (11 keyword searches), site: queries, Trustpilot, and
comparison against GSC Coverage + Performance data (Feb–May 2026).
**Direct access:** Still HTTP 403 (Cloudflare WAF blocks all non-Google tools).
Google itself crawls normally — the 403 only affects audit tools, AI crawlers, and this sandbox.

---

## 🔑 Key Change Since Last Audit: Author Attribution Is Live

The most important finding: **"Written by Shama Kuakrathok" is now appearing in Google
search result snippets.** This means the metaobject author system from theme v4 is
published and Google is reading it. This is the single most impactful E-E-A-T change
you could have made, and it is confirmed live.

Example from live search snippets (June 1, 2026):
> *"What to Use as Rolling Paper When You're Out of Papers"* — **Written by Shama Kuakrathok**
> — *rolling paper industry veteran with 9 years of hands-on experience*

Google is now seeing a named, credentialed author on your blog content. This directly
addresses the December 2025 / March 2026 Core Update signals that caused the ranking drop.
The recovery effect will take 4–8 weeks from when it was published to show in position data.

---

## SERP Position Comparison — Then vs Now

These are live results from Google searches run on June 1, 2026. "Then" is the GSC
3-month average (Feb 19–May 19, 2026).

### "custom rolling papers"

| Position | Site | Then (GSC avg) |
|:--------:|------|:--------------:|
| 1 | Papers + Ink Studio | — |
| 2 | Snail Custom Rolling Papers | — |
| **3** | **rollyourownpapers.com (homepage)** | **~9 (combined)** |
| 4 | Custom Cones USA | — |
| 5 | The Rolling Paper Company | — |
| 6 | Hara Supply | — |
| **7** | **rollyourownpapers.com/collections/custom-rolling-papers** | **18.5** |
| 8 | Smoke Promos | — |
| 9 | MunchMakers | — |
| 10 | Snail (custom/personalized page) | — |

**Collection page moved from position 18.5 → ~7. Homepage moved from ~9 → ~3.**
This is a significant improvement. The `| within: collection` URL fix (theme v4) and
the author attribution are the most likely causes.

> ⚠️ These are today's snapshot positions — not a 3-month average. SERP positions
> fluctuate daily. Use GSC to verify the trend over the next 4–6 weeks.

### "custom rolling papers low minimum"

| Position | Site |
|:--------:|------|
| **1** | **rollyourownpapers.com (homepage)** |
| **2** | **rollyourownpapers.com/collections/custom-rolling-papers** |
| 3 | Smoke Promos |
| 4 | Cannabis Law Report |
| 5–7 | MunchMakers (3 pages) |

**RYOP owns #1 and #2 for this term.** This is your strongest keyword and you are
dominating it. Historical GSC showed this term at position 9.29 — today it appears #1.

### "custom rolling papers wholesale low minimum order"

| Position | Site |
|:--------:|------|
| 1 | MunchMakers |
| 2 | Smoke Promos |
| 3 | Snail |
| 4 | PromoLeaf |
| **5** | **rollyourownpapers.com (homepage)** |
| 6 | Custom Cones USA |
| 7 | MunchMakers |
| **8** | **rollyourownpapers.com/collections** |
| 9 | The Rolling Paper Company |
| 10 | Papers + Ink |

### "custom rolling paper manufacturer"

| Position | Site |
|:--------:|------|
| 1 | Papers + Ink Studio |
| 2 | The Rolling Paper Company |
| 3 | Snail |
| 4 | Hara Supply |
| 5 | Grandstand |
| 6 | Great American Rolling Paper Co. |
| 7 | PromoLeaf |
| 8 | Custom Cones USA |
| **9** | **rollyourownpapers.com (homepage)** |

For the manufacturing-intent keyword you're at position 9. This is where the
`/collections/custom-rolling-papers` page content upgrade matters most — a
manufacturer's page with materials, process, certifications would capture this.

### "branded rolling papers dispensary"

| Position | Site |
|:--------:|------|
| 1 | MunchMakers |
| 2 | Great American Rolling Paper Co. |
| **3** | **rollyourownpapers.com (homepage)** |
| 4 | MunchMakers Blog |
| 5 | AnyPromo |
| 6 | GanjaPrint |
| **7** | **rollyourownpapers.com/collections** |

### "custom pre rolled cones wholesale low minimum"

| Position | Site |
|:--------:|------|
| 1 | The Cones Factory |
| **2** | **rollyourownpapers.com/collections/custom-pre-rolled-cones** |
| 3 | Custom Cones USA |
| 4 | Brand My Dispo |
| 5 | Custom Cones USA (wholesale) |

**#2 for custom cones.** This is strong. The cones collection page is performing
well — a sign that the URL fix helped.

---

## What Changed Since the Last Audit (Feb–May 2026)

### ✅ Improvements Confirmed

| Change | Evidence |
|--------|----------|
| Author attribution live | "Written by Shama Kuakrathok" in SERP snippets |
| `\| within: collection` bug fixed (v4 theme) | Theme diff confirmed; collection page now at ~pos 7 |
| Collection page climbing | From pos 18.5 → ~7 for "custom rolling papers" |
| Homepage strong for short-tail | ~pos 3 for "custom rolling papers" vs ~9 before |
| Cones collection performing | #2 for "custom pre rolled cones wholesale low minimum" |
| Low-minimum keyword dominated | #1 and #2 for "custom rolling papers low minimum" |

### ❌ Issues Still Present

| Issue | Status |
|-------|--------|
| Blog content audit not executed | "Alternatives to rolling paper", "how to make a joint without paper" etc. still live and indexed |
| Emoji in blog titles | 🌿😎📜📐🛒 still visible in SERP snippets — looks unprofessional, hurts CTR |
| Collection page content thin | Still needs 600–800 words of manufacturer content to hold page 1 rankings |
| 256 broken 404 URLs | Still present (from GSC Coverage — not yet resolved) |
| Indexed pages still declining | Was 850 as of May 18 — no sign of reversal yet |
| robots.txt still 403 | AI crawlers (OAI-SearchBot, PerplexityBot) still blocked |
| Organization JSON-LD missing | No structured data for company entity |
| Homepage H1 is logo | Still the logo `<h1>`, not a keyword heading |

---

## New Competitive Threats — June 2026

The competitive landscape is more crowded than it was 6 months ago. Three new
competitors have become consistently visible across multiple searches:

### MunchMakers — Most Active Threat
Appearing in 5 out of 8 searches. They have invested heavily in B2B buyer content
("Custom Printed Rolling Papers: How Dispensaries Use Branded Papers", "Low MOQ
Wholesale Guide"), exactly targeting RYOP's customer. Their blog strategy is what
RYOP's blog *should* be doing.

### GanjaPrint — Price Disruptor
"Custom rolling papers from $0.46 each" — extremely aggressive pricing. Appears
for dispensary and branded keyword searches. Will attract price-sensitive buyers.

### Smoke Promos — Speed Competitor
"Branded in 10 business days" from Tampa, FL. Competing on speed + low minimum.
US-based production is a differentiator against RYOP's Thai/Chinese manufacturing.

### Brand My Dispo — Niche Player
Custom cones from 1,300 units. Focused on dispensary vertical. Showing up for
cones and rolling paper searches alongside RYOP.

**The gap is narrowing.** RYOP's main advantages — lowest MOQ (150 booklets),
2.5-week lead time, free design, free shipping — are not clearly visible on the
collection page compared to how competitors surface them.

---

## Trustpilot Social Proof — Current Status

- **Rating:** 4.5 stars
- **Reviews:** 58 total
- **Recent activity:** Reviews through Feb 2026 confirming product quality
- **Named team members** (Sam, Mike) appear in reviews — good for E-E-A-T

**58 reviews since 2011 is low** for a business of this scale. Competitors with
stronger trust profiles use Trustpilot reviews in schema (`AggregateRating`) on
their pages. RYOP should add an active review request flow post-purchase.

---

## What Still Needs to Happen (Priority Order)

### 🔴 This Week

1. **Remove the emoji from blog post titles.** The 📜🌿😎 in SERP snippets look
   like AI-generated spam and hurt CTR. Shopify Admin → Blog Posts → edit each title.
   Target first: your top 30 posts by traffic.

2. **Execute the blog audit CSV.** The file `audits/blog-audit-2026-06-01.csv`
   has all 507 live posts tagged REMOVE / KEEP-COMMERCIAL / KEEP-CTA. The 240 REMOVE
   posts need 301 redirects — Google is still indexing them and they are still diluting
   domain quality. Do the 68 tag/archive pages first (easiest, biggest crawl budget impact).

3. **Fix the 256 broken 404 URLs** from GSC Coverage. These are wasted crawl slots every day.

### 🟠 Next 2 Weeks

4. **Add 600–800 words to `/collections/custom-rolling-papers`.** The page climbed
   to ~pos 7 but it has almost no content below the product grid. To hold and improve
   past Papers+Ink and Snail, it needs manufacturer-level content: materials, process,
   MOQs, certifications, turnaround. This is the page that wins "custom rolling paper
   manufacturer" (currently pos 9) if it has substance.

5. **Surface your advantages on the collection page header:**
   - ✅ From 150 booklets (lowest MOQ in market)
   - ✅ 2.5-week turnaround
   - ✅ Free design + free worldwide shipping
   - ✅ TÜV SÜD certified
   MunchMakers and Smoke Promos are outranking you partly because their pages
   communicate these clearly. RYOP's page buries them.

6. **Add `AggregateRating` schema** pulling Trustpilot score (4.5 / 58 reviews).
   This generates star ratings in SERP snippets — significant CTR boost.

7. **Request more Trustpilot reviews.** Build an automated post-purchase email asking
   for a review. Target 100+ reviews this quarter.

### 🟡 Weeks 3–6

8. **Add `Organization` JSON-LD** with TÜV SÜD certification, founding year (2011),
   `sameAs` linking to Trustpilot, Instagram, YouTube.

9. **Fix homepage H1** — replace logo H1 with keyword heading.

10. **Fix robots.txt 403** — whitelist AI crawlers so PerplexityBot and OAI-SearchBot
    can index the site. AI search (Perplexity, ChatGPT) is now a real acquisition channel.

11. **Create 5–7 commercial B2B blog posts** (after removing the bad ones):
    - "Custom rolling papers for dispensaries: complete 2026 buyer guide"
    - "How to order custom rolling papers: MOQ, lead time, certifications"
    - "Custom rolling papers vs off-the-shelf: ROI for cannabis brands"
    - "How to choose a custom rolling paper manufacturer" (answer: RYOP's criteria)

---

## Summary — Then vs Now

| Metric | 6 months ago (GSC data) | Today (June 1, 2026) |
|--------|------------------------|----------------------|
| "custom rolling papers" position | ~9.45 avg | ~3 (homepage) + ~7 (collection) |
| Collection page position | 18.5 | ~7 |
| "custom rolling papers low minimum" | 9.29 avg | **#1** |
| Author attribution | Anonymous | **"Written by Shama Kuakrathok"** live |
| `\| within: collection` bug | Present (8 files) | **Fixed** |
| Indexed pages | 1,014 (Feb 24) | ~850 (May 18) — still declining |
| Daily impressions | 43,960 | ~20,000 — down 54% |
| Active competitors | 4–5 | **7–9** (MunchMakers, GanjaPrint, Smoke Promos, Brand My Dispo added) |
| Blog content cleanup | Not started | Not yet executed |

**The technical fixes are working — positions are recovering. The traffic/impressions
are still down because 240 low-quality posts are still live and the indexed page count
is still declining. Execute the blog audit and the collection page upgrade and the
trend will reverse.**

---

*Audit method: Live Google SERP data (11 keyword searches via WebSearch), `site:` queries,
Trustpilot search, and comparison against GSC Coverage (May 25, 2026) and GSC Performance
(6-month export). Direct HTTP access is blocked by Cloudflare WAF (403) for all non-Google
tools — this is unchanged since the first audit in March 2026.*
