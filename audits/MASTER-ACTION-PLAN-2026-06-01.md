# RYOP Master Action Plan — What To Do Right Now
**Date:** 2026-06-01
**Purpose:** The single prioritized to-do list, consolidated from all audits.
**Rule:** Do these in order. Don't skip ahead. Each phase unlocks the next.

---

## The One-Sentence Diagnosis

Your rankings are recovering (collection page 18.5 → 7, author attribution live), but
**240 low-quality blog posts are dragging the whole domain down** — Google has refused
to index 1,782 of your pages and is removing ~10 indexed pages per week. **The #1 job
right now is cleaning the blog, not adding anything new.**

---

## 🥇 THE MAJORITY TASK: Clean Up the Blog (This Is 80% of the Win)

Everything else is secondary. Google is actively de-indexing the site because it reads
RYOP as a low-quality content farm. Until that stops, new pages won't reach their ceiling.

**The file is ready: `audits/blog-audit-2026-06-01.csv`** — every URL is pre-tagged.

### Step 1 — Delete/redirect the 68 tag & archive pages (fastest win, do first)
These are auto-generated pages like *"The ROLL YOUR OWN PAPERS Blog! Tagged 'Custom
Rolling Tray' Page 2"*. They have zero unique content and waste crawl budget.
- In the CSV, these are tagged `REMOVE` with titles containing "Tagged" or "Blog!"
- **Action:** In Shopify, these are blog tag pages — add `noindex` (your theme already
  noindexes tag pages per `theme.liquid:12-14`, so verify it's working) OR remove the
  tag associations. Confirm they drop out of the index in GSC.
- **Time:** 1–2 hours. **Impact:** Immediate crawl budget recovery.

### Step 2 — Fix the 256 broken 404 URLs
- In the CSV these are tagged `404-FIX`.
- **Action:** For each, add a 301 redirect (Shopify Admin → Navigation → URL Redirects)
  to the closest relevant live page. If no equivalent, redirect to the homepage or
  `/collections/all`.
- **Time:** 3–4 hours (or bulk-import via CSV in Shopify). **Impact:** Stops daily
  crawl-budget waste; removes "Not found" errors from GSC.

### Step 3 — Remove/redirect the 240 low-quality posts (the big one)
- In the CSV these are tagged `REMOVE`.
- **Categories being removed:** weed grinder content, rolling tray DIY, "alternatives to
  rolling paper", weed pricing/travel/TSA posts, stoner culture.
- **Action:** For each post — 301 redirect to the most relevant KEEP post, or to a
  collection. Do NOT just delete (that creates more 404s). Always redirect.
- **Do it in batches of ~40/week** so it's manageable and you can watch GSC react.
- **Time:** Spread over 4–6 weeks. **Impact:** This is what reverses the de-indexation.
  Google re-reads the site as a focused manufacturer, not a content farm.

### Step 4 — Remove emoji from the titles of all KEEP posts
- The 📜🌿😎📐🛒 in your SERP snippets look like AI spam and hurt click-through.
- **Action:** Edit the post title (and SEO title) for every `KEEP-COMMERCIAL` and
  `KEEP-CTA` post. Start with the top 30 by traffic.
- **Time:** 2–3 hours for top 30. **Impact:** Higher CTR on existing rankings.

> **This phase alone is the majority of the work and the majority of the result.**
> If you only do one thing, do Steps 1–3.

---

## 🥈 PHASE 2: Activate What's Already Built (Quick, High-Impact)

These are nearly done — you built the code, you just need to finish them in Admin.

### Step 5 — Create the Author metaobject entries
The theme code is live (confirmed: "Written by Shama Kuakrathok" shows in Google now).
But you need real entries for every author name.
- **Action:** Shopify Admin → Content → Metaobjects → Author → Add entry for each
  staff name. Fill: real name, credentials bio, headshot photo, LinkedIn URL.
- **Critical:** The entry handle must match `article.author | handleize` (e.g., staff
  name "Shama Kuakrathok" → handle `shama-kuakrathok`).
- **Time:** 30 min per author. **Impact:** E-E-A-T signal on all 250+ kept posts at
  once; restores AI Overview eligibility (which had collapsed 15 → 0).

### Step 6 — Add CTA blocks to the top KEEP-CTA posts
Your blog gets ~42,000 clicks/quarter but routes almost none to sales pages.
- **Action:** Add a contextual CTA block to the top 20 `KEEP-CTA` posts linking to
  `/collections/custom-rolling-papers`. Example:
  > **Need custom-branded papers?** RYOP makes them from 150 booklets, TÜV SÜD certified.
  > [See custom options →](/collections/custom-rolling-papers)
- **Time:** 2 hours. **Impact:** Converts existing traffic to leads *before* rankings move.

---

## 🥉 PHASE 3: Strengthen the Commercial Pages (The Growth Lever)

### Step 7 — Create the manufacturer landing page
You rank #9 for "custom rolling paper manufacturer" with no dedicated page. Your
TÜV SÜD certification is the strongest credential in the market and it's hidden.
- **Action:** Create `/pages/custom-rolling-paper-manufacturer` (full spec in the
  June 1 manufacturer plan). 800–1,000 words: process, materials, TÜV SÜD certs,
  factory-direct, MOQ, FAQ schema. 301 the existing blog post to it.
- **Time:** 4 hours. **Impact:** Position 9 → 3–5 in 6–10 weeks.

### Step 8 — Add content to the custom rolling papers collection page
It climbed to ~position 7 but has almost no text below the product grid.
- **Action:** Add 600–800 words: materials, customization process, MOQs, certifications,
  turnaround, who it's for. Surface the trust bar:
  `✓ TÜV SÜD Certified  ✓ Est. 2011  ✓ From 150 booklets  ✓ Ships in 2.5 weeks`
- **Time:** 3 hours. **Impact:** Holds page 1 and pushes past Papers+Ink / Snail.

### Step 9 — Update meta titles
- Collection: `Custom Rolling Papers | Factory-Direct Manufacturer | Roll Your Own Papers`
- **Time:** 15 min.

---

## PHASE 4: Technical Polish (Lower Priority, Do After 1–3)

### Step 10 — Add Organization + AggregateRating + FAQ schema
- `Organization` JSON-LD (founding 2011, TÜV SÜD credential, sameAs links)
- `AggregateRating` pulling Trustpilot (4.5 / 58) → star ratings in SERPs
- `FAQPage` on the manufacturer page
- **Time:** 2 hours.

### Step 11 — Fix the homepage H1
Currently the `<h1>` wraps the logo. Make it a descriptive keyword heading.
- **Time:** 30 min.

### Step 12 — Fix the robots.txt / sitemap 403
Whitelist AI crawlers (OAI-SearchBot, PerplexityBot) at the Cloudflare WAF. Add `/llms.txt`.
- **Time:** 1 hour (needs Cloudflare access).

### Step 13 — Request more Trustpilot reviews
58 reviews since 2011 is low. Build an automated post-purchase review request.
- **Time:** 1 hour setup. **Impact:** Compounds over time.

---

## The Complete Sequence at a Glance

| # | Task | Phase | Time | Priority |
|---|------|-------|------|----------|
| 1 | Noindex/remove 68 tag & archive pages | Blog cleanup | 1–2h | 🔴 NOW |
| 2 | 301-redirect 256 broken 404s | Blog cleanup | 3–4h | 🔴 NOW |
| 3 | 301-redirect 240 low-quality posts (batches) | Blog cleanup | 4–6 wks | 🔴 NOW |
| 4 | Remove emoji from KEEP post titles | Blog cleanup | 2–3h | 🔴 NOW |
| 5 | Create Author metaobject entries | Activate | 30m ea | 🟠 Week 1 |
| 6 | Add CTA blocks to top 20 posts | Activate | 2h | 🟠 Week 1 |
| 7 | Build manufacturer landing page | Commercial | 4h | 🟠 Week 2 |
| 8 | Add content to collection page | Commercial | 3h | 🟠 Week 2 |
| 9 | Update meta titles | Commercial | 15m | 🟠 Week 2 |
| 10 | Add Org/Rating/FAQ schema | Technical | 2h | 🟡 Week 3–4 |
| 11 | Fix homepage H1 | Technical | 30m | 🟡 Week 3–4 |
| 12 | Fix robots.txt 403 + AI crawlers | Technical | 1h | 🟡 Week 3–4 |
| 13 | Trustpilot review automation | Technical | 1h | 🟡 Week 3–4 |

---

## What Success Looks Like (How to Measure)

Check GSC weekly. You'll know it's working when:

1. **"Crawled – currently not indexed" drops** from 1,782 toward <500 (Steps 1–3)
2. **Indexed pages stop declining** and start rising from ~850 (Steps 1–3)
3. **Impressions reverse** from the current ~20,000/day downward trend (Steps 1–3)
4. **Author names appear** in more SERP snippets (Step 5)
5. **"custom rolling paper manufacturer"** moves from pos 9 toward pos 3–5 (Step 7)
6. **Star ratings appear** in your SERP listings (Step 10)

---

## The Bottom Line

**The majority task right now is Steps 1–3: clean the blog.** Everything else is
secondary until the de-indexation stops. You have the CSV — it tells you exactly which
of the 507 posts to remove (240), keep and improve (256), and the 256 broken URLs to
redirect. Work through it in batches, watch GSC react, and the rankings will follow.

The fixes you already shipped (URL bug, author attribution) prove the recipe works —
positions recovered. Now remove the dead weight so the whole domain can rise.

---

*Consolidated from: verified audit (May 21), final audit (May 21), action plan (May 25),
blog audit CSV (June 1), live SERP audit (June 1), manufacturer keyword analysis (June 1).*
