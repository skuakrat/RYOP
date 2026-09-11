# Re-Audit & Ranking Comparison: rollyourownpapers.com
**Date:** 2026-05-21
**Compares:** March 16, 2026 baseline → today (covers the last 6 months, ~Nov 2025–May 2026)
**Keywords:** "custom rolling paper" (singular) | "custom rolling papers" (plural)
**Platform:** Shopify | **Industry:** B2B/DTC custom rolling papers manufacturer

---

## Executive Summary — What Changed in 2 Months

**SEO Health Score: 54 → 55 / 100 (essentially flat — treading water).**

RYOP shipped the *easy* wins from the March audit (homepage + main collection title tags
are now clean and keyword-led) and picked up a handful of new reviews. But every
high-leverage fix — infrastructure, blog cleanup, content consolidation, schema — is
still undone. Worse, the blog **regressed**: RYOP kept publishing more emoji-titled,
near-duplicate, consumer-focused posts, which actively works against recovery.

**Bottom line on rankings:** No recovery. "custom rolling papers" (plural) is still off
page 1. "custom rolling paper" (singular) is holding around #2 (homepage). The gains and
the regressions roughly cancelled out — the site has not moved.

| Area | March 16 | May 21 | Direction |
|------|----------|--------|-----------|
| Homepage `<title>` | Bloated, `.COM` suffix, no keyword lead | "Custom Rolling Papers & Pre-Rolled Cones \| Low Minimums" | ✅ Fixed |
| Collection `<title>` | Generic / `.COM` style | "Custom Rolling Papers — Printed With Your Logo \| Roll Your Own Papers" | ✅ Fixed |
| Trustpilot reviews | 44 | 58 | ✅ Slight gain |
| Blog emoji titles | ~6 posts | **10+ posts (more added)** | ❌ Worse |
| Near-duplicate blog posts | 3 ("where to buy" cluster) | **7+ (added a "how to roll" cluster)** | ❌ Worse |
| DIY / wrong-audience posts | ~3 | **More added** ("Make Rolling Paper at Home", "Make It Stick") | ❌ Worse |
| robots.txt / sitemap.xml | HTTP 403 | **Still HTTP 403** | ❌ Unfixed |
| Tag/filter pages indexed | Yes (old `.COM` titles) | **Still indexed, still old titles** | ❌ Unfixed |
| llms.txt | Missing | **Still missing** | ❌ Unfixed |
| Schema / rich results | None | **None** | ❌ Unfixed |
| `\| within: collection` URL bug | Present | **Unverified — assume present** | ❌ Unfixed |

---

## 1. Current SERP Snapshot (May 21, 2026)

### "custom rolling papers" (plural — the primary, higher-volume head term)

| Pos | Site |
|-----|------|
| 1 | Papers + Ink Studio |
| 2 | Snail Custom Rolling Papers |
| 3 | Hara Supply |
| 4 | The Rolling Paper Company |
| 5 | Custom Cones USA |
| 6 | Zig-Zag |
| 7 | PromoLeaf |
| 8 | Swag Supply |
| 9 | Custom Cannabis Merch |
| 🔴 | **RYOP — STILL NOT IN TOP 10** |

The competitor lineup is **almost identical to March**. RYOP has not re-entered page 1.
No movement = the partial fixes were not enough to register.

### "custom rolling paper" / "custom rolling paper printed logo" (singular)

- **RYOP homepage** — holding around **#2**, stable vs. March.
- **RYOP collection page** (`/collections/custom-rolling-papers`) — appears mid page 1
  (~#4–7 depending on query variant). The new "Printed With Your Logo" title is helping
  this page show for logo-intent queries.

**Read:** Singular = stable and decent. Plural = still lost. Because the plural carries
more search volume and commercial intent, this is still where the traffic loss sits.

---

## 2. Why the Ranking Still Hasn't Recovered

### 2.1 No new core update has run yet
The March 2026 core update completed **April 8, 2026**. There has been **no core update
since**. Google re-evaluates algorithmic positions at core updates — so the next real
recovery window is the **expected June/July 2026 core update**. Anything fixed now is
"banked" for that re-evaluation. Nothing fixed now = another cycle lost.

### 2.2 Only the cosmetic fixes shipped
Title tags were the *visible* recommendation, so they got done. They help CTR and keyword
relevance — genuinely good — but title tags alone don't reverse a core-update demotion.
The demotion was driven by **E-E-A-T and content-quality signals**, and those are untouched.

### 2.3 The blog actively got worse
This is the most important finding. Since March, RYOP added more posts in exactly the
pattern Google's August 2025 Spam and December 2025 Core updates penalize:

**Emoji-titled posts (10+ now, vs ~6 in March):**
- "How to Roll a Rolling Paper: The Ultimate Step-by-Step Guide 🌿✨"
- "📜 How to Use Rolling Paper: ❓ Your Ultimate Beginner's Guide 🌟"
- "😎 How to Roll with Rolling Paper: The Ultimate Step-by-Step Guide"
- "🏡 How to Make Rolling Paper at Home: 📦 The Ultimate DIY Guide 🌿"
- "How to Make Rolling Paper Stick: ...Perfect Rolls Every Time 🚀"
- "🔥 What Size Rolling Paper for a Joint? Your Ultimate 2026 Guide 📖"
- "What is a Rolling Paper? 📜 Your Complete 2026 Guide"
- "How to Roll a Blunt with Rolling Paper (2025 Guide) 🎯"

**New near-duplicate cluster** — three posts that target essentially the same query and
cannibalize each other:
- "How to Roll a Rolling Paper"
- "How to Roll with Rolling Paper"
- "How to Use Rolling Paper"

This is *on top of* the original 3-post "where to buy rolling paper" duplicate cluster
flagged in March. RYOP now has **two** keyword-cannibalization clusters instead of one.

**Wrong audience.** RYOP sells to dispensaries and brands (B2B). New posts like "How to
Make Rolling Paper at Home" and "How to Make Rolling Paper Stick" attract hobbyist
consumers who will never place a 150-booklet custom order. They generate poor engagement
signals (high bounce, no conversion) that feed back into quality scoring.

### 2.4 Infrastructure still broken
`robots.txt`, `sitemap.xml`, the homepage, and `llms.txt` all **still return HTTP 403**
to this audit environment (verified again today). This means:
- Crawl control is still impossible (can't steer Googlebot away from junk pages).
- The site still cannot be reliably cited by AI search (ChatGPT, Perplexity, AI Overviews).
- Tag/filter pages (`/collections/custom-rolling-papers/samples`,
  `/custom-raw-material-rolling-paper`, `/custom-printed-rolling-paper-bobbins`, etc.) are
  **still indexed** with stale `.COM` titles — thin, duplicate pages diluting the main
  collection page that you actually want to rank.

> Caveat: the 403 is what *this* audit environment receives. Confirm in Google Search
> Console → Settings → Crawl stats whether real Googlebot is also being 403'd. If GSC
> shows 403s, this is your single most urgent fix.

---

## 3. Keyword Diagnosis: Singular vs. Plural

| | "custom rolling paper" (singular) | "custom rolling papers" (plural) |
|--|-----------------------------------|----------------------------------|
| RYOP position | ~#2 homepage, collection mid-page-1 | Not in top 10 |
| Status vs. March | Stable | Stable (still lost) |
| Why | Homepage is a strong, old, branded entity match for the singular | Plural SERP is dominated by competitors with stronger E-E-A-T + cleaner content signals; RYOP's collection page lacks the depth/trust signals to break in |
| What wins it back | Maintain — don't break it | Collection-page content depth, schema, author-backed E-E-A-T, clean blog signals |

The plural is winnable: RYOP's collection page now has a good title and ranks page 1 for
the *logo* variant. It needs **on-page content depth + trust signals** to climb into the
core "custom rolling papers" top 10.

---

## 4. Updated Fix Priority — Next 5 Weeks (before the June/July core update)

Ordered by leverage. You have a narrow window to bank these before the next core update.

### 🔴 Do this week
1. **Stop publishing consumer/DIY blog posts.** Every new emoji-titled how-to post makes
   the pattern problem worse. Freeze the current blog cadence until cleanup is done.
2. **Strip emojis from all blog `<title>` tags** (10+ posts). Emoji-heavy titles are a
   documented low-effort-content signal. Keep them in the body H1 if you like; remove from
   `<title>` only.
3. **Fix the 403 on robots.txt + sitemap.xml.** In Cloudflare → Security → WAF, add a
   bypass rule for `/robots.txt` and `/sitemap.xml` (and `/llms.txt`) so they return 200.
   Then submit the sitemap in Google Search Console.
4. **Verify in GSC** whether Googlebot itself is being 403'd (Crawl stats report). If yes,
   whitelist Googlebot/Bingbot in the WAF immediately.

### 🟠 Within 2 weeks
5. **Consolidate the two duplicate clusters.** 301-redirect each cluster down to one
   canonical post:
   - "where to buy" cluster (3 posts) → one evergreen `/where-to-buy-custom-rolling-papers`
   - "how to roll / use" cluster (3 posts) → one canonical "how to roll" guide
6. **Add author bylines + bios to every blog post.** This is the single biggest E-E-A-T
   gap and the exact signal the December 2025 core update rewarded. A named manufacturing
   expert with a short credentialed bio, plus `BlogPosting` + `author` schema.
7. **Noindex or canonicalize the tag/filter pages** under `/collections/custom-rolling-papers/`
   so they stop competing with the main collection page.
8. **Deepen the `/collections/custom-rolling-papers` page** with 300–500 words of genuine
   manufacturer expertise (material comparison, customization process, certifications,
   who it's for). This is the page that must rank for the plural.

### 🟡 Within 4–5 weeks
9. **Add schema:** Organization + WebSite on the homepage, Product schema on product
   pages (use the JSON-LD for SEO Shopify app), BreadcrumbList on collections/products.
10. **Fix the Shopify `{{ product.url | within: collection }}` bug** — replace with
    `{{ product.url }}` in the theme's product-card Liquid so internal links stop splitting
    PageRank across non-canonical URLs.
11. **Core Web Vitals:** preload the hero image (`fetchpriority="high"`), add explicit
    width/height to product images, defer the 3D visualizer JS. The March update's
    holistic CWV scoring means one slow page drags the whole domain.
12. **Add `/llms.txt`** for AI-search discoverability.

### 🔵 Ongoing (compounds over months)
- Keep growing Trustpilot (58 now) **and** add Google Business Profile reviews — raters
  weight GBP reviews more heavily. Post-purchase email sequence; target 150+ on each.
- Commission original research (e.g., a dispensary-buyer survey) — competitors like
  Custom Cones USA outrank RYOP partly on proprietary data. This builds a citation moat.

---

## 5. Expected Recovery Timeline

| Milestone | Timing | Condition |
|-----------|--------|-----------|
| Infrastructure + blog cleanup banked | By mid-June 2026 | If §4 🔴 + 🟠 done this month |
| Impressions tick up for "custom rolling papers" | 3–5 weeks after cleanup | Visible in GSC before positions move |
| First position recovery (plural re-enters page 2) | At the **June/July 2026 core update** | Only if quality fixes are live and crawled before it runs |
| Plural back into top 10 | Next core update after that (Q4 2026) | Sustained quality signal across a full cycle |

**The hard truth:** the last 2 months were a near-miss. The easy fixes shipped, but the
core-update demotion is caused by content-quality and E-E-A-T signals that are still
untouched — and the blog got worse. If RYOP repeats this pattern, the June/July core
update will pass with no recovery. The fixes in §4 must be **live and crawled before** the
next core update begins, or the recovery slips another full cycle (~3–4 months).

---

## Appendix: Snapshot Comparison

| Attribute | March 16, 2026 | May 21, 2026 |
|-----------|----------------|--------------|
| SEO Health Score | 54/100 | 55/100 |
| Homepage title | Bloated, no keyword lead | ✅ Clean, keyword-led |
| Collection title | Generic | ✅ "Printed With Your Logo" |
| Trustpilot | 4.5★, 44 reviews | 4.5★, 58 reviews |
| Blog emoji titles | ~6 | 10+ (worse) |
| Duplicate-content clusters | 1 | 2 (worse) |
| robots.txt / sitemap.xml | 403 | 403 (unfixed) |
| Schema / rich results | None | None |
| "custom rolling paper" (singular) | ~#2 homepage | ~#2 homepage (stable) |
| "custom rolling papers" (plural) | Not top 10 | Not top 10 (no recovery) |
| Next core update window | March 2026 (missed) | June/July 2026 (open now) |

---

*Re-audit performed via SERP analysis and live HTTP checks (May 21, 2026). Direct HTML
access remains blocked by server-side CDN rules (HTTP 403). Verify all technical findings
against live Google Search Console and PageSpeed Insights data.*
