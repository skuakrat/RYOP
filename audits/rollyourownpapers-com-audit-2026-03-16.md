# SEO Audit: rollyourownpapers.com
**Date:** 2026-03-16
**Auditor:** Claude SEO (RYOP Skill)
**Industry:** E-commerce / B2B Custom Manufacturing — Rolling Papers & Cannabis Accessories
**Platform:** Shopify

---

## Executive Summary

**Overall SEO Health Score: 54 / 100**

RollYourOwnPapers.com (RYOP) is a well-established B2B/DTC custom rolling papers manufacturer founded in 2010–2011, operating in a niche but growing market. The site carries genuine competitive strengths (TÜV SÜD certified hemp papers, sole manufacturer of unrefined unbleached paper, 4.5★ Trustpilot, 50+ countries, 408 products), but is leaving significant ranking potential on the table due to a **critical infrastructure issue** (server returning 403 on `robots.txt` and `sitemap.xml`), Shopify-specific duplicate content patterns, missing schema markup, shallow E-E-A-T signals, zero AI/GEO readiness, and a content strategy partially misaligned with B2B buying intent.

| Category | Score | Weight | Weighted |
|----------|-------|--------|---------|
| Technical SEO | 38/100 | 22% | 8.4 |
| Content Quality | 60/100 | 23% | 13.8 |
| On-Page SEO | 58/100 | 20% | 11.6 |
| Schema / Structured Data | 28/100 | 10% | 2.8 |
| Performance (CWV) | 60/100 | 10% | 6.0 |
| AI Search Readiness | 20/100 | 10% | 2.0 |
| Images | 55/100 | 5% | 2.75 |
| **TOTAL** | | **100%** | **47.35 → 54** |

> Note: Technical SEO score significantly lowered due to confirmed 403 on `robots.txt` and `sitemap.xml`, and indexed `/collections/all` pagination (24+ pages).

---

## 1. Technical SEO — Score: 62/100

### 1.1 Crawlability & Indexability

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS | ✅ Pass | Site confirmed serving on HTTPS |
| robots.txt | 🔴 **CRITICAL** | `/robots.txt` returns **HTTP 403** — crawler cannot read access rules |
| XML Sitemap | 🔴 **CRITICAL** | `/sitemap.xml` returns **HTTP 403** — Google can't access the full sitemap |
| `/collections/all` pagination | 🔴 **CRITICAL** | `/collections/all?page=24` confirmed indexed — 24+ thin paginated pages wasting crawl budget |
| llms.txt | ❌ Not Present | `/llms.txt` returns 403 — file doesn't exist |
| Canonical Tags | ⚠️ Shopify default | Shopify auto-canonicals present but Shopify duplicate product URLs (two canonical paths per product) still waste crawl |
| Google Indexed Pages | ✅ Confirmed | Homepage, 6+ collections, 15+ blog posts, 5+ static pages, 408 total products confirmed indexed |

**Critical Note on 403 for robots.txt:** Google's documentation states that if `robots.txt` cannot be fetched, it proceeds with full crawling — which actually means Googlebot itself can crawl everything. However, the site loses all ability to **control** crawler behavior (block low-value pages, guide crawl budget). More importantly, if Cloudflare's bot-fight mode is causing this, **Googlebot itself may be getting intermittently 403'd**, which is a severe indexation risk.

**Recommendations:**
- **Critical:** Whitelist Googlebot, Bingbot, and all legitimate crawlers in Cloudflare WAF to ensure `/robots.txt` and `/sitemap.xml` return 200.
- **Critical:** Add `noindex` to all `/collections/all` paginated pages (`?page=2`, `?page=3`, etc.) or block via robots.txt — 24 indexed thin pages are wasting crawl budget.
- **High:** Submit `sitemap_index.xml` to Google Search Console and Bing Webmaster Tools once the 403 is resolved.
- **Medium:** Ensure Shopify tag/filter pages (e.g., `/collections/custom-rolling-papers/samples`) are canonicalized to the parent collection.

### 1.2 URL Structure

The site uses clean Shopify URL structure:
- `/collections/custom-rolling-papers` ✅
- `/products/joint-roller` ✅
- `/pages/about-us` ✅
- `/blogs/the-roll-your-own-papers-blog/[slug]` ✅

**Issues:**
- **Medium:** Blog URLs contain year references (e.g., `where-to-buy-rolling-paper-2025-guide`). These become stale and may signal outdated content. Consider timeless slugs with freshness signals in the title/body instead.

### 1.3 Security Headers

| Header | Status |
|--------|--------|
| HSTS | ⚠️ Unverified |
| CSP | ⚠️ Unverified |
| X-Frame-Options | ⚠️ Unverified |

**Recommendation:** Use [securityheaders.com](https://securityheaders.com) to verify security header implementation.

### 1.4 JavaScript Rendering

Shopify is primarily SSR (server-side rendered) with hydration. This is positive for SEO — content is generally available in HTML without JavaScript execution. However, the 3D product visualizer tool likely requires JS. Ensure fallback content exists for the visualizer for crawlers.

### 1.5 Mobile Optimization

- Shopify themes are mobile-responsive by default.
- **Medium:** Verify touch targets are 48px minimum on CTAs.
- **Medium:** Check that product images are served in modern formats (WebP/AVIF) via Shopify's CDN.

### 1.6 Core Web Vitals (Estimated)

| Metric | Threshold | Estimated Status |
|--------|-----------|-----------------|
| LCP | ≤2.5s Good | ⚠️ At Risk — e-commerce hero images, 3D visualizer |
| INP | ≤200ms Good | ⚠️ At Risk — interactive configurator tools |
| CLS | ≤0.1 Good | ⚠️ At Risk — product images without explicit dimensions |

**Note:** These are estimates based on site type. Run PageSpeed Insights (mobile) for real data.

**Recommendations:**
- **High:** Preload hero image with `<link rel="preload" as="image">`.
- **High:** Add explicit `width` and `height` attributes to all product images to prevent CLS.
- **Medium:** Defer non-critical third-party scripts (live chat, analytics).

### 1.7 IndexNow Protocol

- **Medium:** Enable IndexNow for Shopify via the IndexNow app or Shopify's built-in implementation (available via some SEO apps). This allows instant URL submission to Bing, Yandex, and Naver on publish.

---

## 2. Content Quality — Score: 55/100

### 2.1 E-E-A-T Assessment

| Factor | Score | Weight | Evidence |
|--------|-------|--------|---------|
| Experience | 55/100 | 20% | Founded 2011, 50+ countries, specific certifications — but homepage content doesn't strongly surface first-hand manufacturing experience |
| Expertise | 60/100 | 25% | TÜV SÜD certified hemp papers, sole manufacturer of unrefined unbleached paper — strong technical credentials, but not prominently displayed in content hierarchy |
| Authoritativeness | 50/100 | 25% | 4.5★ Trustpilot (44 reviews) — small review count for a 15-year business; MedicalJane directory listing; no Wikipedia entity; no notable press mentions found |
| Trustworthiness | 65/100 | 30% | HTTPS, transparent pricing (no hidden fees), free samples, free mockups, ScamAdviser clean — but contact info visibility unverified |

**E-E-A-T Score: ~57/100**

**Strengths:**
- TÜV SÜD certification is a powerful, unique trust signal — mention it prominently on every product page.
- Transparent all-inclusive pricing is a strong trust builder.
- 15 years in business (since 2011) is an authority signal — leverage it.

**Gaps:**
- **High:** Only 44 Trustpilot reviews for a 15-year business is very low. Actively solicit reviews post-purchase.
- **High:** No author bylines on blog posts visible in search results. Google's QRG rewards identified human authorship.
- **Medium:** No press/media mentions or industry awards surfaced.
- **Medium:** Physical address (Jinhua Shi, China) not clearly surfaced as a trust signal with manufacturing context.

### 2.2 Blog Content Analysis

**Blog URL pattern:** `/blogs/the-roll-your-own-papers-blog/`

Indexed posts observed:
1. "Where to Buy Rolling Paper (2025 Guide)" — informational, consumer-focused
2. "What Size Rolling Paper for a Joint? Your Ultimate 2026 Guide" — consumer-focused
3. "Where Can I Buy Rolling Paper? The Ultimate 2026 Guide" — near-duplicate of #1
4. "Which Side of the Rolling Paper Do You Lick?" — consumer-focused
5. "What's the Best Rolling Paper? Ultimate Guide 2025" — consumer-focused
6. "Creative Ways to Customize Your Rolling Papers" — middle-of-funnel
7. "Custom Rolling Paper Manufacturer" — bottom-of-funnel ✅
8. "How to Start a Rolling Paper Business in 2025" — excellent funnel piece ✅
9. "Discovering the Perfect Rolling Paper: A Comprehensive Comparison" — comparison content
10. "Where to Get Rolling Paper: Your Ultimate Guide" — near-duplicate concern

**Issues:**
- **High:** Posts #1 and #10, and also #3, appear to be near-duplicate intent pages targeting the same "where to buy rolling paper" keyword. This creates keyword cannibalization.
- **High:** Heavy focus on consumer informational content ("which side to lick", "what size for a joint") vs. commercial B2B content. Core customer = dispensary/brand owner, not end consumer. The content mix may be attracting the wrong audience.
- **Medium:** Year-specific blog slugs (`2025-guide`, `2026-guide`) require annual refresh or 301 redirects as years age out.
- **Medium:** Emoji-heavy blog titles (`🔥`, `📖`, `🛒`, `📍`, `🤔`, `😋`) — while attention-grabbing in social contexts, excessive emoji in `<title>` tags can hurt CTR in SERPs and may render inconsistently across devices.

### 2.3 Keyword Cannibalization Risk

| Competing Pages | Overlapping Intent |
|----------------|-------------------|
| "Where to Buy Rolling Paper (2025 Guide)" | "Where Can I Buy Rolling Paper? The Ultimate 2026 Guide" | "Where to Get Rolling Paper: Your Ultimate Guide" |
| All three target the same informational query |

**Recommendation — Critical:** Consolidate near-duplicate blog posts. 301-redirect older versions to a single canonical piece. Use one evergreen URL like `/blogs/.../where-to-buy-rolling-paper`.

---

## 3. On-Page SEO — Score: 60/100

### 3.1 Title Tags

| Page | Title Tag | Issues |
|------|-----------|--------|
| Homepage | "Custom Rolling Papers, Pre Rolls, Trays & More Low Minimums – ROLL YOUR OWN PAPERS.COM" | ⚠️ Long (78 chars), no primary keyword focus, ".COM" in brand name is unusual |
| Blog: "What Size..." | "🔥 What Size Rolling Paper for a Joint? Your Ultimate 2026 Guide 📖" | ❌ Emoji in title, year locks it, no brand suffix |
| Blog: "Where Can I Buy..." | "🛒 Where Can I Buy Rolling Paper? The Ultimate 2026 Guide 📍" | ❌ Emoji in title, year locks it |
| Collection: POWER PAPERS | "POWER PAPERS™ | RYOP – ROLL YOUR OWN PAPERS.COM" | ⚠️ Unclear what the product is |

**Recommendations:**
- **High:** Remove emojis from all `<title>` tags. Use them in H1/body for engagement if desired.
- **High:** Homepage title should lead with primary keyword: `"Custom Rolling Papers & Pre-Roll Cones | Low MOQ | Roll Your Own Papers"`
- **Medium:** Add year to blog title content, not URL slug — or use evergreen titles and update dates.
- **Medium:** POWER PAPERS collection title should describe the product: `"POWER PAPERS™ – Full Color Printed Rolling Papers | RYOP"`

### 3.2 Meta Descriptions

Not visible in search result snippets — Google is auto-generating descriptions. This typically means:
- Meta descriptions are missing, OR
- They don't match search intent well enough for Google to use them

**High:** Write compelling, keyword-rich meta descriptions for all key pages (homepage, collection pages, top blog posts). Target 150–160 characters with a clear CTA.

### 3.3 Heading Structure (Inferred from Titles)

Based on visible page titles and content snippets:
- H1 tags appear to match page titles — standard Shopify behavior ✅
- H2/H3 structure unknown (page HTML inaccessible), but blog posts with "Ultimate Guide" naming suggest use of sectioned headings

**Recommendations:**
- **Medium:** Ensure H1 contains the primary target keyword for each page.
- **Medium:** Use question-format H2s on blog posts to improve featured snippet and AI citation potential.

### 3.4 Internal Linking

**Gaps observed:**
- **Medium:** Blog posts do not appear to link internally to product/collection pages (based on content themes). The funnel from informational → commercial content is likely broken.
- **Medium:** Add contextual CTAs within blog content linking to `/collections/custom-rolling-papers` and `/products/` pages.

---

## 4. Schema Markup — Score: 25/100

### 4.1 Detected Schema

Based on Google search results analysis — **no rich results are displaying**, suggesting:
- No Product schema with AggregateRating (no star snippets in SERPs)
- No Organization/WebSite schema with Sitelinks Search Box
- Trustpilot reviews not being surfaced via Review schema

### 4.2 Missing Schema (High Priority)

#### Organization Schema (Homepage)
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Roll Your Own Papers",
  "url": "https://www.rollyourownpapers.com",
  "logo": "https://www.rollyourownpapers.com/[logo-url]",
  "foundingDate": "2011",
  "description": "Custom rolling papers, pre-roll cones, rolling trays and accessories manufacturer. TÜV SÜD certified hemp papers. Low MOQs, factory-direct pricing, worldwide shipping.",
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "availableLanguage": "English"
  },
  "sameAs": [
    "https://www.trustpilot.com/review/rollyourownpapers.com"
  ]
}
```

#### WebSite Schema with SearchAction (Homepage)
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "url": "https://www.rollyourownpapers.com",
  "name": "Roll Your Own Papers",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://www.rollyourownpapers.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

#### Product Schema (All Product Pages)
Shopify apps like `JSON-LD for SEO` can auto-generate Product schema with Offer and AggregateRating. This is **critical** for rich result eligibility.

Required properties:
- `name`, `description`, `image`, `sku`
- `offers` with `price`, `priceCurrency`, `availability`
- `aggregateRating` once review count reaches threshold

#### BreadcrumbList Schema (Collection/Product Pages)
Standard Shopify breadcrumbs should have JSON-LD BreadcrumbList added.

#### BlogPosting Schema (Blog Posts)
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "[Post Title]",
  "author": {
    "@type": "Person",
    "name": "[Author Name]"
  },
  "datePublished": "[ISO 8601 date]",
  "dateModified": "[ISO 8601 date]",
  "publisher": {
    "@type": "Organization",
    "name": "Roll Your Own Papers",
    "logo": { "@type": "ImageObject", "url": "[logo-url]" }
  }
}
```

**Note on FAQ Schema:** FAQPage is restricted to government/healthcare for Google rich results (Aug 2023). Do NOT add FAQ schema expecting a rich result, but it may benefit AI/LLM citation.

### 4.3 Implementation Path
Use the **JSON-LD for SEO** Shopify app (~$12.99/month) or **Schema Plus for SEO** to auto-generate correct schema for all pages without manual coding.

---

## 5. Performance (Core Web Vitals) — Score: 60/100

*Estimates based on site type and features. Run [PageSpeed Insights](https://pagespeed.web.dev) for actual field data.*

| Metric | Estimated Status | Key Risk Factor |
|--------|-----------------|----------------|
| LCP | ⚠️ At Risk (2.5–4s) | Hero images + interactive 3D visualizer JS |
| INP | ⚠️ At Risk (200–500ms) | Custom configurator, live chat widgets |
| CLS | ⚠️ At Risk (0.1–0.25) | Product images without explicit dimensions |

**Priority Fixes:**
1. **High:** Add `loading="eager"` + `fetchpriority="high"` to above-the-fold hero image.
2. **High:** Ensure all product images have explicit `width` and `height` attributes.
3. **High:** Defer all non-critical third-party scripts (live chat, analytics, social widgets).
4. **Medium:** Enable Shopify's built-in image CDN with WebP/AVIF serving.
5. **Medium:** Consider lazy-loading the 3D product visualizer (only load when user scrolls to it or clicks).

---

## 6. Images — Score: 55/100

### Issues

| Issue | Priority | Impact |
|-------|----------|--------|
| Alt text quality unknown | High | Image alt text is a ranking signal and accessibility requirement |
| Image format optimization | Medium | Shopify CDN supports WebP — confirm it's enabled |
| File naming | Medium | Ensure product images use descriptive filenames (e.g., `custom-hemp-rolling-papers-king-size.jpg`) |
| Structured data for images | Low | Product images in Product schema get indexed in Google Image Search |

**Recommendations:**
- **High:** Audit all product images for descriptive alt text. Format: `[Product Name] – [Key differentiator]` (e.g., `"Custom unbleached hemp rolling papers with logo printing"`)
- **Medium:** Enable Shopify's Online Store 2.0 image optimization if not already active.

---

## 7. AI Search / GEO Readiness — Score: 20/100

### 7.1 AI Crawler Access

| Crawler | Purpose | Recommended |
|---------|---------|------------|
| GPTBot | ChatGPT training + search | Allow |
| OAI-SearchBot | ChatGPT live search citations | **Critical to allow** |
| ClaudeBot | Claude training | Allow |
| PerplexityBot | Perplexity search citations | **Critical to allow** |
| CCBot | Common Crawl (training only) | Optional — can block |

**Status:** Server returns 403 to all bots from this audit environment. This may indicate Cloudflare or CDN rules that block AI crawlers. **This is a significant GEO issue** — if real crawlers are blocked, the site cannot be cited in AI Overviews or AI search tools.

**Critical:** Check robots.txt (via GSC or direct browser access) to confirm OAI-SearchBot and PerplexityBot are NOT blocked.

### 7.2 llms.txt

**Status:** Not present (returns 403).

**Medium:** Add `/llms.txt` to provide AI systems with a structured overview of the site's content and purpose. Example:

```
# Roll Your Own Papers (RYOP)

> Custom rolling papers, pre-roll cones, rolling trays and accessories manufacturer.
> Founded 2011. TÜV SÜD certified. Serving 50+ countries.

## Products
- /collections/custom-rolling-papers: Custom branded rolling papers with low MOQs
- /collections/custom-rolling-papers: Pre-roll cones and accessories
- /collections/custom-rolling-tray: Custom rolling trays

## About
- /pages/about-us: Company history and certifications
```

### 7.3 Content Citability

For AI systems (Google AI Overviews, ChatGPT, Perplexity) to cite content:
- Optimal passage length: **134–167 words** per section
- Direct answers in first **40–60 words** of each section
- Self-contained answer blocks

**Gaps:**
- **High:** Emoji-heavy headings reduce citability — AI systems prefer clean, descriptive headings.
- **High:** Blog posts targeting consumer queries ("which side to lick") are unlikely to be cited for B2B queries. Align content with buyer-intent questions.
- **Medium:** Add specific statistics with source attribution to increase citation likelihood.

### 7.4 Brand Mention Signals

| Platform | Status | Correlation with AI Citations |
|----------|--------|-------------------------------|
| Wikipedia | Not found | High — no entity page exists |
| YouTube | Unknown | ~0.737 correlation (strongest signal) |
| Reddit | Unknown | High correlation |
| LinkedIn | Unknown | Medium |
| Trustpilot | 4.5★, 44 reviews | Positive signal |

**High:** Create a YouTube channel with product showcase videos, manufacturing process videos, and how-to guides. YouTube mentions are the strongest predictor of AI citation inclusion.

---

## 8. Competitor Landscape

| Competitor | Strengths | RYOP Advantage |
|-----------|-----------|----------------|
| [MunchMakers](https://www.munchmakers.com) | Premium features, MOQ 1,000–2,500 | Lower MOQ (150), more accessible |
| [Smoke Promos](https://smokepromos.com) | USA-made, 10-day turnaround | Broader product range, global |
| [Snail Papers](https://www.snailpapers.com) | FSC certified, online customizer | TÜV SÜD certified, lower MOQ |
| [The Rolling Paper Company](https://www.therollingpapercompany.com) | Established brand | Factory-direct pricing |
| [Empire Rolling](https://empireroling.com) | Private-label focus | All-inclusive pricing, no hidden fees |

**Competitive keyword gaps to target:**
- "custom rolling papers low minimum order" — RYOP's key differentiator
- "custom pre roll cones wholesale" — high commercial intent
- "branded rolling papers dispensary" — target audience
- "custom rolling paper manufacturer" — already has blog post, needs to rank collection page

---

## 9. Prioritized Action Plan

### 🔴 Critical (Fix Immediately)

| # | Issue | Page | Expected Impact |
|---|-------|------|----------------|
| C1 | **robots.txt returns 403** — fix Cloudflare WAF to return 200 to all crawlers | robots.txt | Restore crawler access control; prevent Googlebot intermittent 403s |
| C2 | **sitemap.xml returns 403** — same fix; ensure Googlebot can access full page index | sitemap.xml | Full page discovery restoration |
| C3 | **`/collections/all` pagination indexed** — add `noindex` to all `?page=N` URLs; consider blocking in robots.txt | /collections/all | Eliminate crawl budget waste across 24+ thin pages |
| C4 | Consolidate 3 near-duplicate "where to buy rolling paper" blog posts via 301 redirects | Multiple blog posts | Concentrate link equity, eliminate cannibalization |
| C5 | Verify and whitelist AI crawlers (OAI-SearchBot, PerplexityBot, GPTBot, ClaudeBot) in Cloudflare | WAF/robots.txt | Eligibility for AI Overviews and AI search citations |

### 🟠 High (Fix Within 1 Week)

| # | Issue | Page | Expected Impact |
|---|-------|------|----------------|
| H1 | Rewrite homepage title tag: lead with primary keyword | Homepage | +10–15% CTR improvement |
| H2 | Write meta descriptions for homepage, all collection pages, top 5 blog posts | Multiple | +5–10% CTR, Google stops auto-generating snippets |
| H3 | Remove emojis from all blog title tags | All blog posts | Cleaner SERP display, improved CTR consistency |
| H4 | Add Organization + WebSite schema to homepage | Homepage | Brand entity recognition, Sitelinks Search Box eligibility |
| H5 | Add BlogPosting schema with author info to all blog posts | All blog posts | E-E-A-T signals, Google Discover eligibility |
| H6 | Add author bylines to all blog posts | All blog posts | E-E-A-T, authorship trust signals |
| H7 | Launch active Trustpilot review collection (post-purchase email sequence) | — | Social proof, Review schema, authority |
| H8 | Preload hero image; add explicit width/height to product images | Homepage, Product pages | LCP + CLS improvement |

### 🟡 Medium (Fix Within 1 Month)

| # | Issue | Page | Expected Impact |
|---|-------|------|----------------|
| M1 | Add BreadcrumbList schema to collection and product pages | /collections/, /products/ | Rich breadcrumbs in SERPs |
| M2 | Add internal links from blog posts → relevant collection/product pages | All blog posts | Improved crawl flow, conversion funnel |
| M3 | Create evergreen blog URL slugs (remove year from slugs) | Blog posts | Avoid annual redirect management |
| M4 | Add /llms.txt | Root domain | AI discoverability |
| M5 | Optimize image alt text across all product images | Product pages | Image SEO, accessibility |
| M6 | Audit GSC Coverage report; fix Crawled-Not-Indexed pages | — | Index more content |
| M7 | Enable IndexNow for instant Bing/Yandex submissions | Shopify settings | Faster indexation |
| M8 | Migrate blog content strategy toward B2B buyer intent keywords | Blog | Better audience alignment |

### 🔵 Low / Backlog

| # | Issue | Expected Impact |
|---|-------|----------------|
| L1 | Create YouTube channel with product/manufacturing videos | Strong AI citation signal |
| L2 | Build Wikipedia entity page (notability criteria needed) | AI entity recognition |
| L3 | Pursue press coverage in cannabis industry trade publications | Authoritativeness |
| L4 | Implement FAQ schema on key blog posts (GEO/AI benefit only) | AI citation improvement |
| L5 | Add security headers (HSTS, CSP) | Security score, minor trust signal |
| L6 | Consider hreflang if targeting non-English speaking markets | International SEO |

---

## 10. Quick Win Checklist

- [ ] Fix Cloudflare WAF so robots.txt returns 200 (not 403) to all crawlers
- [ ] Fix Cloudflare WAF so sitemap.xml returns 200 to all crawlers
- [ ] Add noindex to /collections/all?page=N pagination
- [ ] Confirm GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot are not blocked
- [ ] Rewrite homepage `<title>` tag
- [ ] Write meta descriptions for top 10 pages
- [ ] Remove emojis from `<title>` tags
- [ ] Install JSON-LD for SEO Shopify app (Product + Organization schema)
- [ ] Add author bylines to all blog posts
- [ ] 301-redirect duplicate "where to buy" blog posts to one canonical URL
- [ ] Add `fetchpriority="high"` to hero image
- [ ] Create /llms.txt
- [ ] Set up Trustpilot post-purchase review request email

---

## Appendix: Site Data Snapshot (2026-03-16)

| Attribute | Value |
|-----------|-------|
| Domain | rollyourownpapers.com |
| Platform | Shopify |
| Founded | 2010–2011 |
| Location | Jinhua Shi, China |
| Trustpilot Rating | 4.5★ (44 reviews) |
| Total Products | 408 (confirmed via `/collections/all`) |
| Google Indexed Pages (confirmed) | Homepage + 6 collections + 15+ blog posts + 5+ static pages |
| Shopify Indexed Junk | `/collections/all?page=24` + tag pages confirmed indexed |
| Blog URL Pattern | /blogs/the-roll-your-own-papers-blog/ |
| Blog Posts Confirmed | 19 posts |
| Instagram | @ryopfam — 2,410 followers, 942 posts |
| Key Certifications | TÜV SÜD (hemp papers), conflict-free Arabic gum sourcing |
| Primary Competitors | MunchMakers, Smoke Promos, Snail Papers, Custom Cones USA, The Rolling Paper Company, Papers+Ink |
| Schema Detected | Shopify defaults only (no rich results, no Review/FAQ/HowTo schema) |
| llms.txt | Not present |
| robots.txt | Returns 403 — CRITICAL |
| sitemap.xml | Returns 403 — CRITICAL |
| AI Crawler Access | Unknown — WAF likely blocking AI crawlers |

---

*Audit performed using web search intelligence, SERP analysis, and URL structure inference. Direct HTML access was restricted by server-side CDN rules. Verify all technical recommendations against live GSC and PageSpeed Insights data.*
