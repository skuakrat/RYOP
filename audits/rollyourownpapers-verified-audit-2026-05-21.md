# Verified SEO Audit — rollyourownpapers.com
**Date:** 2026-05-21
**Basis:** Real data — Shopify theme export, homepage HTML source, Google Search Console
performance export (Feb 19–May 19, 2026, "Last 3 months")
**Supersedes:** The March 16 and May 21 *external-inference* reports. Where they conflict,
**this report is correct** — it is built on first-party data, not search-result guesses.

---

## ⚠️ Corrections to the Earlier Reports

The March/May audits were done with no access to the site (HTTP 403). Several of their
"critical" findings were wrong. With real data:

| Earlier claim | Reality (verified) |
|---------------|--------------------|
| "No schema markup" | ❌ Wrong — `WebSite` + `Product` JSON-LD exist; GSC shows Merchant listings at pos 3.2 |
| "Meta descriptions missing" | ❌ Wrong — homepage has a proper, well-written meta description |
| "robots.txt 403 = critical Googlebot crawl risk" | ❌ Overstated — Google crawls fine: 3.17M impressions, 980+ pages indexed. The 403 only blocks the audit sandbox (and possibly AI crawlers) |
| "Tag/filter pages wrongly indexed" | ❌ Wrong — theme correctly applies `noindex, follow` to tag pages (`theme.liquid:12-14`) |
| "Homepage title bloated" | ❌ Already fine — `Custom Rolling Papers & Pre-Rolled Cones \| Low Minimums` |
| "`\| within: collection` URL bug" | ✅ **Confirmed** — 8 instances in the theme |
| "Blog is too consumer-focused" | ✅ Confirmed — and **far worse than estimated** (see below) |

**Net:** the earlier reports inflated technical/infrastructure problems and under-weighted
the one structural problem that actually explains everything. That problem is below.

---

## The Real Diagnosis: A Traffic–Intent Mismatch

RYOP does **not** have a traffic problem. In the last 3 months it got **~45,500 organic
clicks** on **3.17M impressions**. It has a **monetization problem**: the traffic is
going to the wrong pages, for the wrong queries, from the wrong audience.

### Where the 45,500 clicks actually land (GSC Pages export)

| Page type | Pages indexed | Clicks (3 mo) | Share |
|-----------|--------------:|--------------:|------:|
| **Blog posts** | 684 | **42,134** | **92.5%** |
| Homepage | 1 | 2,079 | 4.6% |
| Product pages | 256 | 942 | 2.1% |
| Collection pages | 46 | 612 | 1.3% |

**92.5% of all organic traffic goes to informational blog content. The pages that
actually sell — collections + products — pull 3.4% combined.**

### The blog isn't just consumer-focused — it's anti-commercial

The single biggest page on the entire site:

> `/blogs/.../what-to-use-as-rolling-paper-when-you-re-out-of-papers-10-handy-alternatives`
> — **10,544 clicks, 352,162 impressions.**

That post teaches people how to *avoid buying rolling papers*. The rest of the top blog
pages are the same: "how to make a joint without rolling paper", "alternatives to rolling
paper", "can you use parchment paper / toilet paper / gum wrappers", "how to make rolling
paper at home", "how much is a bag of weed", "can you fly with weed". This pulls in
hobbyist consumers — **none of whom will ever place a 150-booklet custom B2B order.**

### The result: Google has miscategorized the site

With 684 informational posts vs. 92 commercial pages, Google reads rollyourownpapers.com
as an **informational blog about rolling-paper alternatives and weed culture** — not a
**B2B custom manufacturer**. The site's topical authority, internal links, and crawl
budget are all concentrated in the wrong place.

---

## The "custom rolling paper / papers" Keywords — Verified Numbers

You asked specifically about these. Here is the GSC truth (3-month average position):

| Query | Position | Clicks | Impressions |
|-------|---------:|-------:|------------:|
| custom rolling papers | **9.45** | 385 | 2,891 |
| custom rolling papers low minimum | 9.29 | 63 | 290 |
| custom rolling papers with logo | 7.43 | 22 | 144 |
| custom rolling paper | **12.61** | 40 | 418 |
| branded rolling papers | 16.55 | 17 | 541 |
| custom printed rolling papers | 16.18 | 14 | 363 |
| custom rolling papers wholesale | 15.69 | 5 | 136 |
| custom rolling paper manufacturer | 5.25 | 9 | 107 |

And the page that *should* own these terms:

> `/collections/custom-rolling-papers` — **position 18.5**, 101 clicks, 8,139 impressions.

**This is the core finding.** "custom rolling papers" sits at position **9.45** (bottom of
page 1) — but it's being carried by the **homepage**, not the product collection. The
collection page built to rank for that exact term is stuck on **page 2 (pos 18.5)**.

You don't have a penalty. You have a **starved commercial page** competing — weakly —
against rivals (Papers+Ink, Snail, Hara, The Rolling Paper Company) who run dedicated,
content-rich, well-linked custom-rolling-paper pages. RYOP's equivalent page is
out-resourced by its own 684-post blog.

### Is it a "drop"? — Honest answer

The GSC export was set to **"Last 3 months"** (Feb 19–May 19). Within that window,
performance is **stable** — ~500–750 clicks/day, average position 4.2–5.6, no cliff.
**I cannot see your 6-month trend** from this file. If you want the true 6-month
comparison, re-export GSC with a **custom 6-month (or 16-month) date range**.

But the structural read is clear regardless: "custom rolling papers" at pos 9.45 with the
collection page at 18.5 is not a sudden algorithmic collapse — it's a page that was
**never built to win**. Any drift from, say, pos 6–7 to pos 9–10 is competitors
strengthening while RYOP's commercial pages stood still.

---

## Confirmed Technical Issues (from the theme export)

### 🔴 1. The `| within: collection` URL-splitting bug — CONFIRMED

Every product link from a collection points to a non-canonical URL
(`/collections/x/products/y` instead of `/products/y`), splitting ranking signals.
Found in **8 places**:

| File | Line(s) |
|------|---------|
| `sections/featured-collection.liquid` | 68 |
| `snippets/product-grid-item.liquid` | 82, 337 |
| `snippets/product-grid-item-video.liquid` | 82, 340 |
| `snippets/product-template.liquid` | 66, 662 |
| `snippets/onboarding-product-grid-item.liquid` | 3 |

**Fix:** in each, change `{{ product.url | within: collection }}` →  `{{ product.url }}`
(and `{{ variant.url | within: collection }}` → `{{ variant.url }}`). The canonical tag
already points to the clean URL, so this just stops leaking link equity.

### 🟠 2. Homepage H1 is the logo

`Homepage line 1052`: the `<h1>` wraps the site logo (`<span class="visually-hidden">Roll
Your Own Papers</span>`). A second `<h1>` ("Bring your…") sits in the AI-generated hero.
The primary H1 should be a descriptive, keyword-bearing heading like *"Custom Rolling
Papers & Pre-Roll Cones — Low Minimums, Factory Direct"*, with only one H1 per page.

### 🟡 3. Schema is present but thin

- ✅ `WebSite` JSON-LD exists — but bare (no `SearchAction`/sitelinks search box).
- ✅ `Product` + `Offer` JSON-LD on featured products.
- ❌ No `Organization` JSON-LD (only legacy microdata on the logo, using insecure
  `http://schema.org`). Add a full `Organization` block: founding date, logo, `sameAs`
  (Trustpilot, Instagram), and the TÜV SÜD credential.
- ❌ No `BreadcrumbList` on collection/product pages.

### 🟡 4. Product snippets rank at position 59

GSC "Search appearance": Product snippets show **15,214 impressions at average position
59.4** — essentially invisible. Merchant listings do better (pos 3.2) but only 992
impressions. Product pages need the same content/linking investment as collections.

### ℹ️ 5. robots.txt / sitemap.xml 403

Still 403 to non-Google tools. Google itself is unaffected (the crawl data proves it).
Lower priority than the earlier reports claimed — but still worth fixing so AI crawlers
(OAI-SearchBot, PerplexityBot) and your own audit tools can access the site.

---

## The Fix Plan — Reprioritized Around the Real Problem

The earlier plans led with "fix robots.txt / add schema." That was wrong. The real
priority is **shifting equity from the blog to the commercial pages.**

### 🔴 Phase 1 — Redirect the equity you already have (Weeks 1–3)

1. **Rebuild `/collections/custom-rolling-papers` into a real ranking page.** Add
   500–800 words of genuine manufacturer content above/below the grid: materials (hemp /
   rice / unbleached), the customization process, MOQs, certifications, who it's for.
   This is the page that must climb from pos 18.5 → page 1.
2. **Internally link the blog → commercial pages.** Your 684 blog posts get 42,000
   clicks/quarter. Right now that funnel is broken. Add a contextual, descriptive-anchor
   link (and a CTA block) from every relevant post to `/collections/custom-rolling-papers`
   and related collections. Even a 2–3% capture is meaningful revenue.
3. **Fix the `| within: collection` bug** (8 lines, listed above). Stops product link
   equity from splitting.
4. **Resolve homepage-vs-collection cannibalization.** Decide which page targets "custom
   rolling papers." Recommended: homepage stays brand/overview, collection page owns the
   commercial term — then link the homepage hero straight to the collection.

### 🟠 Phase 2 — Stop the topical dilution (Weeks 2–6)

5. **Freeze new consumer/DIY/"alternatives" blog posts.** Every one further tilts
   Google's view of the site away from "manufacturer."
6. **Prune or consolidate the weakest informational posts.** 684 posts is a liability at
   this ratio. Consolidate near-duplicates (multiple "how to roll", "where to buy",
   "alternatives" posts) into fewer strong pages; 301 the rest.
7. **Add genuinely commercial content** — buyer guides aimed at dispensaries/brands:
   "How to order custom rolling papers", MOQ/lead-time comparisons, branding case studies.

### 🟡 Phase 3 — Technical polish (Weeks 4–8)

8. Add `Organization` + `BreadcrumbList` JSON-LD; add `SearchAction` to `WebSite`.
9. Give product pages real content depth (they rank at pos 59).
10. Fix the homepage H1; one descriptive H1 per page.
11. Fix the robots.txt/sitemap 403 at the WAF; whitelist AI crawlers; add `/llms.txt`.
12. Run PageSpeed Insights on homepage + collection page (mobile) and address LCP/CLS.

---

## Expected Impact

| Action | What moves | Timeframe |
|--------|-----------|-----------|
| Collection page content + internal links | `/collections/custom-rolling-papers` 18.5 → page 1; "custom rolling papers" 9.45 → 5–7 | 6–12 weeks |
| `\| within: collection` fix | Product pages consolidate equity; pos 59 → improving | 4–8 weeks (recrawl) |
| Blog → commercial internal linking | Conversion of existing 42k clicks/qtr; revenue before rankings move | 2–6 weeks |
| Stop dilution + prune | Google re-reads site as a manufacturer | 1–2 core-update cycles |

**The opportunity:** you already have the hard part — 45,500 clicks a quarter and a
crawled, indexed site. You're routing almost none of it to pages that sell. Fix the
internal routing and the commercial pages, and you convert existing demand without
needing a single new visitor.

---

## What I Still Can't See / Recommended Next Uploads

- **6-month trend** — re-export GSC with a custom 6-month range (this file was 3 months).
- **Collection & product page HTML** — to verify on-page content depth directly.
- **GSC Coverage / Indexing report** — to confirm what's indexed vs. excluded.
- **PageSpeed Insights** results for homepage + `/collections/custom-rolling-papers`.

---

*Audit based on first-party data: Shopify theme export, homepage HTML source, and Google
Search Console performance export (Feb 19–May 19, 2026). This is the authoritative report.*
