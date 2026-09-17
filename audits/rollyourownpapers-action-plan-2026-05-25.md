# RYOP Action Plan & Blog Audit — 2026-05-25
**Based on:** GSC Coverage export (May 25, 2026) + Theme v4 export + GSC 6-month + Ahrefs daily data
**Supersedes:** All previous reports on this topic.

---

## 🚨 New Finding: Google Is Actively De-Indexing the Site

This is the most urgent data point from today's upload.

### Indexed Pages — 3-Month Collapse

| Date | Indexed | Not Indexed | Daily Impressions |
|------|--------:|------------:|------------------:|
| Feb 24, 2026 | **1,014** | 2,847 | 43,960 |
| Mar 18, 2026 | 1,029 | 2,806 | 40,756 (temporary peak) |
| Apr 21, 2026 | **955** | 2,423 | 30,484 ← **cliff** |
| May 5, 2026 | **876** | 2,350 | 27,217 ← **second cliff** |
| May 12, 2026 | **839** | 2,307 | 21,788 |
| May 18, 2026 | **850** | 2,283 | 20,027 |

**Net loss in 3 months:**
- **-164 indexed pages (-16%)** — Google actively removed them
- **-728 total pages from Google's known universe** — Googlebot stopped even discovering them
- **-54% daily impressions** — from 43,960 to 20,027

### What the "Critical Issues" Tell You

| Issue | Pages | What it means |
|-------|------:|---------------|
| **Crawled — currently not indexed** | **1,782** | Google visited, judged as low quality, refused to index |
| Not found (404) | 256 | Broken URLs — wasted crawl budget |
| Alternate page w/ canonical | 79 | Duplicates handled (mostly correct) |
| Excluded by noindex tag | 70 | Tag/filter pages — correct |
| Page with redirect | 42 | Some redirect chains |
| Duplicate without canonical | 30 | Needs fixing |
| Blocked by robots.txt | 17 | Verify these should be blocked |

**The 1,782 "Crawled – currently not indexed" is the crisis.** That is Google's quality
verdict on the blog: *"I can reach these pages, but they are not worth ranking."*
This is 63% of all non-indexed pages. As long as this number stays above ~200, the
commercial pages cannot rank at their ceiling.

### The Two Cliff Dates

- **April 21**: Indexed dropped 26 in a single day, impressions fell 31% overnight.
  This aligns with **Google's April 2026 algorithm activity** (rolling core signals).
- **May 5**: Another -36 indexed pages, impressions -12%.
  Continued de-indexation of low-quality blog content.

---

## Theme v4 Status — What You Fixed

### ✅ `| within: collection` URL bug — FIXED

The highest-priority technical fix is now confirmed resolved in v4. All 8 instances
across 5 files have been corrected. Product URLs from collection pages now point to the
canonical `/products/y` path instead of `/collections/x/products/y`. This stops the
equity splitting. Google will consolidate ranking signals to product pages over the next
4–8 weeks as it recrawls.

### ✅ Author metaobject system — Upgraded in v4

The `metaobject-author.liquid` section now includes a proper Shopify rich-text renderer
for the `author_page` field (replaces the unreliable `metafield_tag` filter). The
JavaScript renderer correctly handles paragraphs, headings, lists, bold, italic, and
links. The Person JSON-LD schema is intact and correct.

---

## Priority Action List — Ranked by Impact

### 🔴 URGENT (Do this week)

**1. Stop publishing new consumer/DIY/alternatives blog posts immediately.**
Every new post dilutes topical authority further. Google is already removing 5–10 pages
per week. Stop adding fuel.

**2. Fix the 256 broken 404 pages.**
Export the "Not found (404)" list from GSC Coverage → Pages. For each:
- If a better page exists: 301 redirect to it
- If the topic is dead: submit for removal in GSC (URL Removal tool)
256 broken URLs waste crawl budget that should go to commercial pages.

**3. Fix the 30 "Duplicate without canonical" pages.**
These tell Google you have duplicate content with no authority signal. Add
`<link rel="canonical">` to the preferred version. Likely caused by URL parameters
(sort, filter variants without proper noindex/canonical).

**4. Upload v4 theme to Shopify and publish it.**
The `| within: collection` fix needs to go live so Google can recrawl corrected URLs.

**5. Create Author metaobject entries in Shopify Admin.**
Go to Admin → Content → Metaobjects → Author → Add entry. Without real entries,
all 684 blog posts still show anonymous authorship to Google. This is the single
most impactful E-E-A-T action available.

---

### 🟠 HIGH PRIORITY (Weeks 1–3)

**6. Rebuild `/collections/custom-rolling-papers` into a real ranking page.**
Currently at position 18.5 with 101 clicks despite 8,139 impressions. Add
600–800 words of genuine manufacturer content: materials (hemp/rice/unbleached),
minimum order quantities, customization process, certifications (TÜV SÜD),
turnaround times, who it's for (dispensaries, brands, events). This is the page
that must climb to page 1.

**7. Add internal links from high-traffic blog posts to commercial pages.**
Your blog sends 42,000 clicks/quarter to informational content with zero
commercial routing. Add a contextual CTA block to every post with >500 clicks
linking to `/collections/custom-rolling-papers`. Even 1% conversion rate =
meaningful B2B leads.

**8. Fix the homepage H1.**
Currently the `<h1>` wraps the logo. Add a single, keyword-bearing H1:
*"Custom Rolling Papers & Pre-Roll Cones — Factory Direct, Low Minimums"*.

---

### 🟡 MEDIUM PRIORITY (Weeks 3–6)

**9. Prune and consolidate weak blog content** (see Blog Audit below).

**10. Add `Organization` JSON-LD** with TÜV SÜD credential, founding year,
`sameAs` (Trustpilot, Instagram, LinkedIn).

**11. Add `BreadcrumbList` schema** on collection and product pages.

**12. Add `SearchAction` to `WebSite` schema** for sitelinks search box eligibility.

**13. Fix robots.txt/sitemap 403** so AI crawlers (OAI-SearchBot, PerplexityBot)
and your own audit tools can access the site.

---

## Blog Content Audit — Keep, Improve, or Remove

You have ~684 blog posts. 1,782 of your pages are "Crawled – not indexed."
The path back is reducing low-quality page count, not adding more.

**Decision framework: ask three questions about each post.**
1. Could a potential wholesale customer or dispensary buyer land on this and become a lead?
2. Does it demonstrate expertise about rolling paper manufacturing?
3. Does it have >200 clicks in the last 6 months?

Any post answering No to all three should be removed or redirected.

---

### ✅ KEEP & IMPROVE — Commercial or Near-Commercial Content

These posts belong on a B2B rolling paper manufacturer site. Improve with:
author attribution, deeper content (1,500+ words), internal links to collections,
and genuine expert perspective.

| Topic type | Action |
|-----------|--------|
| "Custom rolling papers for brands / events / dispensaries" | Keep — expand to 1,500+ words, add case study or example |
| "Wholesale rolling papers" / MOQ guides | Keep — add specific pricing tiers, lead time |
| "How to brand rolling papers" / private label | Keep — this is a B2B buyer query |
| "Hemp / rice / unbleached rolling paper differences" | Keep — add manufacturer perspective |
| "Custom pre-rolled cones" / joint tubes | Keep — directly supports product pages |
| "Rolling paper certifications" / TÜV SÜD | Keep — E-E-A-T gold |
| Comparison posts: your products vs competitors | Keep — add schema markup |

---

### ⚠️ KEEP & ADD CTA — High-Traffic Consumer Posts (Bridge Strategy)

These posts pull real traffic but from the wrong audience. You can't kill them
without losing ~30,000 clicks/quarter. Instead: keep them live, but add a
prominent CTA block and a genuine contextual link to the commercial collection.

**Example CTA block to add to every post in this category:**
> **Running low on papers?** Roll Your Own Papers makes custom-branded rolling papers
> for dispensaries, brands, and events. [View custom options →](/collections/custom-rolling-papers)

| Post (by topic) | Clicks (3 mo) | Why keep | What to add |
|----------------|:-------------:|----------|-------------|
| "10 alternatives to rolling papers when you run out" | ~10,544 | #1 traffic driver — can't 301 it without losing 10k clicks | CTA block + internal links to hemp/rice papers as better alternatives |
| "How to roll a joint" variations | ~3,000–5,000 est. | High volume | CTA: "Roll with quality papers — see our selection" |
| "Best rolling papers" comparisons | ~2,000+ est. | Commercial intent adjacent | Add RYOP products to comparison; link to shop |
| "How to roll a blunt" | High volume | Can bridge to cones/wraps | CTA to pre-rolled cones collection |
| "What is rolling paper made of" | Moderate | Material education | Manufacturer angle: link to your materials page |

---

### 🗑️ REMOVE (301 Redirect or Delete) — Anti-Commercial Content

These actively harm the site's topical authority signal. Google reads them and
concludes: "this is a lifestyle blog, not a manufacturer." Each one is a vote
against your B2B positioning.

**Redirect all of these to the most relevant remaining post or to the homepage.**
Do not leave them as 404s — always 301.

| Topic | Why remove |
|-------|-----------|
| "How to make rolling paper at home" | Teaches people not to buy your product |
| "How to make a joint without rolling paper" | Same — anti-purchase |
| "Can you use [parchment / toilet paper / gum wrappers / Bible pages]" | Alternatives to buying; zero commercial value |
| "How much does a bag of weed cost" / pricing posts | Completely unrelated to your product |
| "Can you fly with weed" / TSA cannabis posts | Completely unrelated — pure traffic dilution |
| "How to get high without weed" / drug substitutes | Reputational risk + zero relevance |
| "Weed slang / stoner culture" posts | Audience mismatch — no B2B buyer will ever convert |
| Near-duplicate "alternatives" posts (5+ on same topic) | Consolidate into one; 301 the rest |
| Near-duplicate "how to roll" posts (10+ on same topic) | Consolidate into one; 301 the rest |
| Thin posts under 400 words with <50 clicks | No value; reclaim crawl budget |

**Estimated removal target:** 200–300 posts (roughly 30–45% of blog).

---

### 🔀 CONSOLIDATE — Duplicate Clusters

You likely have multiple posts on the same topic. Merge these into single definitive
posts, redirect duplicates.

| Cluster | Estimated duplicates | Action |
|---------|--------------------:|--------|
| "Alternatives to rolling papers" variations | 5–10 posts | Merge into one 2,000-word definitive guide; 301 the rest |
| "How to roll a joint" step-by-step variants | 8–15 posts | One master post; 301 all others |
| "How to roll a blunt" variants | 5–8 posts | One master post; 301 all others |
| "Best rolling papers [year]" annual versions | 3–5 posts | Update the newest one; 301 older years |
| "Rolling paper brands" listicles | 4–6 posts | Consolidate into one comparison |

---

## New Commercial Content to Create (After Pruning)

Once the 200–300 bad posts are removed, Google's topical read of the site shifts.
Then these new posts will rank:

| Target keyword | Post type | Target audience |
|---------------|-----------|-----------------|
| "custom rolling papers for dispensaries" | Buyer guide | Dispensary purchasing managers |
| "branded rolling papers minimum order" | FAQ + guide | Brand/event organizers |
| "private label rolling papers manufacturer" | Landing page hybrid | B2B buyers |
| "custom pre-rolled cone packaging" | Product guide | Cannabis brands |
| "rolling paper supplier comparison" | Comparison | Procurement teams |
| "how long does custom rolling paper take" | FAQ | Any buyer with a deadline |
| "rolling paper certifications explained" | Expert post | Quality-conscious buyers |

---

## Expected Timeline and Outcomes

| Action | Expected result | Timeframe |
|--------|----------------|-----------|
| Publish v4 theme (`| within` fix) | Product page equity consolidation, pos 59 → improving | 4–8 weeks post-recrawl |
| Fix 256 × 404s | Crawl budget freed, fewer "not indexed" signals | 2–4 weeks |
| Create Author metaobjects | E-E-A-T signals activated on all 684 posts; AI Overview eligibility restored | 4–8 weeks |
| Rebuild `/collections/custom-rolling-papers` | Position 18.5 → page 1 for "custom rolling papers" | 6–12 weeks |
| Remove/redirect 200+ low-quality posts | 1,782 "crawled not indexed" drops sharply; domain quality rises | 1–2 core update cycles (3–6 months) |
| Add commercial CTA blocks to kept posts | Existing 42k clicks/qtr start converting | 2–6 weeks |
| Stop new consumer content | No further topical dilution | Immediate |

---

## The Honest Summary

The site is in a content quality death spiral driven by 3 months of continuous
de-indexation. Google has visited 1,782 pages and refused to index them. It is
crawling less of the site each week (total known pages fell by 728 in 3 months).
Impressions fell 54% while indexed pages fell 16%.

**The single fastest lever is the author metaobjects** — it changes Google's signal
on all 684 existing posts at once, costs no new content, and directly restores
AI Overview eligibility (which collapsed from 15 to 0).

**The single highest-ROI content action is CTA blocks** — you already have 42,000
clicks per quarter going to zero-revenue pages. Adding a CTA converts existing
traffic before rankings improve.

**The single most important structural action is removing 200–300 posts** — this
is painful but necessary. Every week those pages stay live, Google's quality
verdict on the domain gets slightly worse.

The `| within: collection` fix (v4) and the author system are already built.
Upload the theme, create the author entries, fix the 404s. Everything else
follows from there.

---

*Report generated: 2026-05-25. Based on GSC Coverage export (Feb 24–May 18, 2026),
GSC Performance 6-month export, Ahrefs daily overview, Shopify theme v4 export.*
