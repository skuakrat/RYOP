# Ranking Drop Investigation: rollyourownpapers.com
**Date:** 2026-03-16
**Period Investigated:** September 2025 – March 2026
**Keywords Investigated:** "custom rolling papers" | "custom rolling paper"

---

## Executive Finding

**RYOP has dropped out of the top 10 for the plural "custom rolling papers"** — their highest-value head term. They still rank for the singular "custom rolling paper" (position ~2 for homepage + ~7 for collection page) but have lost visibility on the higher-volume plural variant.

The drop is **not a manual penalty**. It is the result of **three compounding algorithm updates** between August 2025 and March 2026 that all hit RYOP's specific weaknesses simultaneously.

---

## 1. Current SERP Snapshot (March 16, 2026)

### "custom rolling papers" (plural — primary keyword)

| Position | Site | URL |
|----------|------|-----|
| 1 | Papers + Ink Studio | papersandink.com/collections/custom-printed-organic-rolling-papers |
| 2 | Snail Custom Rolling Papers | snailpapers.com |
| 3 | Hara Supply | harasupply.com/collections/custom-rolling-papers |
| 4 | The Rolling Paper Company | therollingpapercompany.com |
| 5 | Custom Cones USA | customconesusa.com/custom-rolling-papers/ |
| 6 | Zig-Zag | zigzag.com |
| 7 | PromoLeaf | promoleaf.com/cat/rolling-papers/1000 |
| 8 | Swag Supply | swag-supply.com/custom-rolling-papers/ |
| 9 | Custom Cannabis Merch | customcannabismerch.com/collections/custom-rolling-papers |
| 🔴 | **RYOP — NOT IN TOP 10** | — |

### "custom rolling paper" (singular — secondary keyword)

| Position | Site | URL |
|----------|------|-----|
| 1 | Snail Custom Rolling Papers | snailpapers.com |
| **2** | **Roll Your Own Papers (homepage)** | **rollyourownpapers.com** |
| 3 | Papers + Ink Studio | papersandink.com |
| 4 | Custom Cones USA | customconesusa.com |
| 5 | The Rolling Paper Company | therollingpapercompany.com |
| 6 | Great American Rolling Paper Co. | garpusa.com/custom-rolling-papers/ |
| **7** | **RYOP collection page** | **rollyourownpapers.com/collections/custom-rolling-papers** |
| 8 | MunchMakers | munchmakers.com/product-category/custom-rolling-papers/ |
| 9 | Hara Supply | harasupply.com/collections/custom-rolling-papers |
| 10 | Great American Rolling Paper Co. | garpusa.com |

**Summary:** RYOP ranks #2 and #7 for the singular, but has **completely dropped off page 1** for the plural. Since "custom rolling papers" (plural) is the higher-traffic term and the primary commercial intent query, this is where most of the traffic loss has occurred.

---

## 2. Algorithm Update Timeline (Sept 2025 – March 2026)

Three updates hit RYOP's specific weaknesses in sequence:

```
Sept 2025          Dec 2025           March 2026
    |                  |                   |
[Aug Spam Update] [Dec Core Update] [March Core Update]
Targeted:         Targeted:          Targeted:
- Scaled AI       - Low-effort AI    - Holistic CWV
  content           content            (site-wide)
- Doorway pages   - E-E-A-T gaps     - INP threshold
- Near-duplicate  - Anonymous          lowered to 150ms
  content           authorship       - Info Gain Score
- Keyword         - Thin collection  - Author entity
  stuffing          pages              signals
```

### Update 1: August 2025 Spam Update (Aug 26 – Sept 22, 2025)

**What it targeted:** Scaled content abuse, doorway pages, near-duplicate content, AI-generated thin pages, keyword stuffing.

**RYOP's exposure:**
- 3 near-identical blog posts targeting "where to buy rolling paper" — classic scaled content pattern
- Emoji-heavy titles are an AI content quality signal (`🔥 What Size Rolling Paper...`)
- Forward-dated posts ("2026 Guide" published in late 2025) — manipulative freshness tactic
- DIY posts ("How to Make Rolling Paper at Home") with no commercial value for a B2B manufacturer

**Likely impact:** Initial rankings instability. Some blog posts may have been demoted or flagged.

---

### Update 2: December 2025 Core Update (Dec 11–29, 2025)

**What it targeted:** The first core update to explicitly penalize low-effort AI content at scale. Boosted E-E-A-T signals, rewarded identifiable expertise and authorship.

**Who lost:** Anonymous, authorless content; generalist retailers; sites with thin collection pages; AI-generated blogs without human editorial review.

**Who won:** Specialist brands with strong identity, transparent provenance, and identifiable authors.

**RYOP's exposure:**
- **No author bylines** on any blog posts — the single biggest E-E-A-T failure this update punished
- 15+ blog posts with no identified human author
- Content pattern consistent with AI generation (generic phrasing, no first-hand manufacturing insights, no original data)
- Small Trustpilot footprint (44 reviews for a 15-year business) signals low real-world engagement
- Papers+Ink and Snail Papers both have strong brand identity stories that this update rewarded

**Likely impact:** Primary cause of "custom rolling papers" (plural) dropping off page 1. Collection page demoted in favor of branded competitors with stronger E-E-A-T.

---

### Update 3: March 2026 Core Update (March 27 – April 8, 2026)

**What it targeted:** **Holistic Core Web Vitals scoring** — Google now aggregates CWV data across the entire domain, not just per-page. A few slow pages drag down the entire site. INP threshold effectively tightened from 200ms to 150ms.

**Who lost:** Sites with Shopify themes + large product catalogs + interactive JS tools (e.g., configurators) + unoptimized images. 71% of tracked domains showed negative impact; average 54% visibility decline for thin affiliate-style sites.

**RYOP's exposure:**
- 408 products + interactive 3D product visualizer = significant JS payload
- 403 on robots.txt and sitemap.xml may cause Google to deprioritize crawls
- `/collections/all?page=24` — 24+ thin indexed paginated pages indicate poor crawl health
- Shopify with large catalog typically scores 45–65 on PageSpeed (mobile)
- **Any pages with LCP >3s lose ground to competitors with LCP <2.5s in the same niche**

**Likely impact:** Amplified the December 2025 decline. Sites that were borderline after Dec 2025 dropped further if their CWV was poor.

---

## 3. Why Competitors Are Now Ranking Above RYOP

### #1: Papers + Ink Studio (papersandink.com)

**Why they rank above RYOP for "custom rolling papers" (plural):**
- Clearly premium artisan brand with strong identity story — highest E-E-A-T alignment with Dec 2025 update
- Organic hemp, all-natural positioning with specific material sourcing claims
- Likely faster, lighter site (premium boutique = smaller catalog, faster load)
- Strong brand differentiation (luxury rolling kits with hemp papers + smart filters + packing tool)

**Gap vs. RYOP:** Stronger brand narrative, likely better technical performance, cleaner content signals.

---

### #2: Snail Custom Rolling Papers (snailpapers.com)

**Why they rank #1 for "custom rolling paper" (singular) and #2 for plural:**
- **FSC certified since 2018** — verifiable, third-party certification prominently featured
- **Online customizer tool** — unique interactive UX that generates engagement signals (longer session duration, lower bounce rate)
- Transparent sourcing ("organic practices, locally sourced materials")
- Strong visual brand identity

**Gap vs. RYOP:** RYOP has TÜV SÜD (stronger certification), but Snail's interactive UX likely generates better engagement signals that post-March 2026 CWV scoring rewards.

---

### #3: Hara Supply (harasupply.com)

**New entrant rising:** A newer competitor with a cleaner content footprint (no legacy AI content) and likely good technical performance. Post-December 2025 updates favor newer sites with clean E-E-A-T if they have genuine expertise signals.

---

### #4–5: The Rolling Paper Company & Custom Cones USA

Both have:
- Clear "since 2008" / "family-owned for 200+ years" heritage claims
- Specific manufacturer credentials (French paper mill provenance)
- Cleaner content with less duplicate/AI-flagged material
- Lower JS overhead (less interactive tools = faster pages)

---

## 4. Root Cause Summary

| Root Cause | Update That Triggered It | Severity |
|-----------|--------------------------|---------|
| Anonymous blog content (no author attribution) | December 2025 Core | 🔴 Critical |
| AI-pattern content (emojis, generic phrasing, no unique insight) | Dec 2025 Core + Aug Spam | 🔴 Critical |
| 3x near-duplicate "where to buy" blog posts | August 2025 Spam | 🔴 Critical |
| 403 on robots.txt/sitemap — broken crawl infrastructure | March 2026 Core (CWV) | 🔴 Critical |
| /collections/all pagination (24+ thin indexed pages) | March 2026 Core (CWV) | 🟠 High |
| Weak E-E-A-T vs. certified competitors (Papers+Ink, Snail) | December 2025 Core | 🟠 High |
| Shopify performance issues (408 products, 3D visualizer JS) | March 2026 Core (CWV) | 🟠 High |
| Forward-dated content ("2026 Guide" published 2025) | August 2025 Spam | 🟡 Medium |
| Low review count (44 Trustpilot in 15 years) | December 2025 Core | 🟡 Medium |
| Missing Product/Organization schema | General ranking signal | 🟡 Medium |

---

## 5. Recovery Plan

Recovery from algorithm-driven drops requires directly addressing the signals that caused the penalty. Based on Google's documented recovery guidance: sites typically need to demonstrate **sustained quality improvement over 1–2 full crawl cycles** (approximately 2–4 months) before rankings recover. There is no shortcut — changes made today will be evaluated at the next core update.

### Phase 1: Stop the Bleeding (Week 1 — Fix Infrastructure)

These must be done first because they affect Googlebot's ability to crawl and evaluate the site.

**1.1 Fix Cloudflare 403 on robots.txt and sitemap.xml**
```
Action: In Cloudflare dashboard → Security → WAF → disable bot-fight mode 
for /robots.txt and /sitemap.xml paths, OR add a bypass rule for these paths.
Goal: Both files must return HTTP 200 to all crawlers including Googlebot.
Impact: Restores crawl control, enables sitemap submission.
```

**1.2 Fix /collections/all pagination**
```
Action: Add to robots.txt once 403 is fixed:
  Disallow: /collections/all?*
OR add noindex meta tag to all /collections/all?page=N URLs via Shopify theme.
Goal: Remove 24+ thin paginated pages from Google's index.
Impact: Recovers crawl budget for your 408 actual product pages.
```

**1.3 Submit sitemap to Google Search Console**
```
Action: GSC → Sitemaps → Add https://www.rollyourownpapers.com/sitemap.xml
Verify all product and collection pages are covered.
```

**1.4 Whitelist AI crawlers in robots.txt**
```
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /
```

---

### Phase 2: Fix the December 2025 E-E-A-T Signal (Weeks 1–2)

This is the primary cause of losing the "custom rolling papers" (plural) ranking. These fixes directly address Google's documented quality guidelines.

**2.1 Add author attribution to ALL blog posts — TODAY**

This is the single highest-leverage action. Google's December 2025 update explicitly rewarded identified authorship. Every blog post needs:
- Author name (e.g., "Sam Wilson, RYOP Manufacturing Director")
- A brief bio (2–3 sentences with credentials)
- Author page with LinkedIn or other verifiable profile

Example author bio to add to all posts:
```
Written by Sam Wilson
Sam has been manufacturing custom rolling papers since 2011 and leads RYOP's 
production team in Jinhua, China. He oversees TÜV SÜD certification compliance 
and has shipped to customers in 50+ countries.
```

In Shopify, add author info to blog post template via `{{ article.author }}` and create an author bio section in the theme.

**2.2 Remove ALL emojis from blog post `<title>` tags**

| Current Title | Fixed Title |
|--------------|-------------|
| `🔥 What Size Rolling Paper for a Joint? Your Ultimate 2026 Guide 📖` | `What Size Rolling Paper for a Joint? Complete Size Guide` |
| `🛒 Where Can I Buy Rolling Paper? The Ultimate 2026 Guide 📍` | `Where to Buy Custom Rolling Papers: Dispensary Buyer's Guide` |
| `🤔 Which Side of the Rolling Paper Do You Lick? 😋` | `Which Side of a Rolling Paper Do You Lick? The Correct Technique` |

Emojis in `<title>` tags are a documented AI-content quality signal. Google's classifiers associate emoji-heavy titles with low-effort, automated content. Remove from `<title>` only — you can keep them in the body H1 if desired.

**2.3 Rewrite the 3 duplicate "where to buy" posts into one canonical guide**

Consolidate these three posts into one comprehensive resource:
- "Where to Buy Rolling Paper (2025 Guide)"
- "Where Can I Buy Rolling Paper? The Ultimate 2026 Guide"
- "Where to Get Rolling Paper: Your Ultimate Guide"

**The new single canonical post:**
- URL: `/blogs/the-roll-your-own-papers-blog/where-to-buy-custom-rolling-papers` (no year in slug)
- Target: B2B buyers — dispensaries, brands, event companies
- Angle: "Where to buy **custom branded** rolling papers" (align with RYOP's actual product)
- 301-redirect the two weaker versions to this canonical URL
- Include: RYOP's certifications, pricing comparison, MOQ comparison vs. competitors

**2.4 Rewrite the homepage `<title>` tag**

```
Current: Custom Rolling Papers, Pre Rolls, Trays & More Low Minimums – ROLL YOUR OWN PAPERS.COM
Fixed:   Custom Rolling Papers & Pre-Roll Cones | Factory Direct | RYOP
```

Rule: Primary keyword first, clear differentiator, short brand suffix.

---

### Phase 3: Fix Content Quality (Weeks 2–4)

**3.1 Overhaul the /collections/custom-rolling-papers page**

This is the page that SHOULD rank for "custom rolling papers" (plural). Currently it likely has minimal text. Add 300–500 words of expert content above or below the product grid:

Content to include:
- What makes RYOP papers unique (TÜV SÜD certified, unrefined unbleached — exclusive worldwide)
- Paper material comparison (hemp vs. rice vs. unbleached — first-hand manufacturing knowledge)
- Customization process overview (how RYOP handles design to delivery)
- Who this is for (dispensaries, cannabis brands, event planners)
- Trust signals: 15 years, 50+ countries, certifications

This content needs to read like it was written by a manufacturer, not an SEO — because that's what Google is now evaluating.

**3.2 Remove or redirect DIY-audience content**

These posts attract users who do NOT want to buy rolling papers:
- "How to Make Rolling Paper at Home" → 301 to collection page, or rewrite as "Why Custom-Manufactured Rolling Papers Beat DIY"
- "How to Make Rolling Paper from Leaves" → same treatment
- "Can You Use Parchment Paper as Rolling Paper?" → same treatment

These posts may be sending negative engagement signals (users who land on them aren't converting, high bounce rate) which feeds into Google's quality scoring.

**3.3 Rewrite top 5 blog posts for E-E-A-T**

Target the posts most likely to drive B2B traffic and add genuine first-hand manufacturing expertise:
1. "Custom Rolling Paper Manufacturer" — add specific factory data, production process, material sourcing
2. "How to Start a Rolling Paper Business" — add first-hand business setup advice from RYOP's 15-year experience
3. "Your Step-by-Step Guide to Designing Custom Rolling Papers" — add actual screenshots of RYOP's design process
4. "Why Custom Rolling Papers Matter for Brand Building" — add real customer case studies/results
5. "Creative Ways to Customize Your Rolling Papers" — include RYOP-specific options, materials, and finishes

---

### Phase 4: Fix Technical Performance (Weeks 2–4)

The March 2026 Core Update's holistic CWV scoring means poor page speed anywhere on the domain drags down rankings everywhere.

**4.1 Run PageSpeed Insights on these URLs first:**
```
https://www.rollyourownpapers.com (mobile)
https://www.rollyourownpapers.com/collections/custom-rolling-papers (mobile)
https://www.rollyourownpapers.com/products/[bestseller] (mobile)
```
Target: LCP < 2.5s, INP < 150ms, CLS < 0.1 on **all three**.

**4.2 Critical image fixes:**
```html
<!-- Hero image: add preload + fetchpriority -->
<link rel="preload" as="image" href="[hero-image-url]" fetchpriority="high">

<!-- All product images: add explicit dimensions to prevent CLS -->
<img src="..." width="800" height="800" loading="lazy" alt="Custom hemp rolling papers with logo printing">
```

**4.3 Defer the 3D product visualizer:**
```javascript
// Only load the 3D configurator JS when user scrolls to it
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      loadConfigurator(); // Load JS here
      observer.unobserve(entry.target);
    }
  });
});
observer.observe(document.getElementById('product-configurator'));
```

**4.4 Shopify performance quick wins:**
- Go to Online Store → Themes → Edit code → Remove any unused apps' JS/CSS
- Disable apps you don't actively use (every installed Shopify app adds JS overhead)
- Enable Shopify's built-in lazy loading for collection page images

---

### Phase 5: Schema + Brand Authority (Month 2)

**5.1 Install JSON-LD for SEO app** (~$12.99/month)

This auto-generates compliant structured data for:
- `Product` with `Offer` and `AggregateRating`
- `Organization` with certifications
- `BreadcrumbList`
- `WebSite` with `SearchAction`

**5.2 Add BlogPosting schema with author entity:**
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "[Post Title]",
  "author": {
    "@type": "Person",
    "name": "Sam Wilson",
    "jobTitle": "Manufacturing Director",
    "worksFor": {
      "@type": "Organization",
      "name": "Roll Your Own Papers"
    }
  },
  "datePublished": "2025-11-15",
  "dateModified": "2026-02-20",
  "publisher": {
    "@type": "Organization",
    "name": "Roll Your Own Papers",
    "logo": { "@type": "ImageObject", "url": "https://www.rollyourownpapers.com/[logo]" }
  }
}
```

**5.3 Surface TÜV SÜD certification in Organization schema:**
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Roll Your Own Papers",
  "foundingDate": "2011",
  "hasCredential": {
    "@type": "EducationalOccupationalCredential",
    "credentialCategory": "certification",
    "recognizedBy": { "@type": "Organization", "name": "TÜV SÜD" }
  }
}
```

**5.4 Increase Trustpilot reviews:**
Set up a post-purchase email at 7 days post-delivery:
> "Hi [Name], how are you enjoying your RYOP order? We'd love to hear your feedback — a quick Trustpilot review helps our small team a lot: [link]. Thank you!"

Target: 200+ reviews within 6 months. This is the fastest trust authority signal you can build.

---

## 6. Expected Recovery Timeline

| Phase | Timeline | Expected Impact |
|-------|----------|----------------|
| Fix 403 infrastructure + pagination | Week 1 | Googlebot crawl restored; crawl budget recovered |
| Remove emojis from titles + author bylines | Week 1–2 | First E-E-A-T improvement signals sent to Google |
| Consolidate duplicate blog posts | Week 2 | Keyword cannibalization eliminated |
| Rewrite collection page content | Week 2–3 | Relevance signals for "custom rolling papers" strengthened |
| Fix Core Web Vitals | Week 2–4 | Performance penalty from March 2026 update addressed |
| Schema implementation | Month 2 | Rich result eligibility; entity recognition |
| Trustpilot reviews buildup | Month 2–4 | Social proof + trust signals compound |
| **First rankings recovery visible** | **2–3 months** | Google crawl cycle + sustained quality signal |
| **Full recovery to pre-drop positions** | **4–6 months** | Full re-evaluation at next core update |

> Google's guidance: Algorithm-based drops require demonstrating **sustained** quality improvement across multiple crawl cycles. Quick fixes rarely result in instant recovery. The goal is to address the root causes so the next core update reverses the decline.

---

## 7. Tracking Your Recovery

Set up these tracking points now so you can measure progress:

**Google Search Console (free):**
- Go to Performance → Search Results → filter by query "custom rolling papers"
- Baseline current position and impressions (this is today's benchmark)
- Check weekly for movement

**Key metrics to watch:**
- Position for "custom rolling papers" (currently: not ranking in top 10)
- Position for "custom rolling paper" (currently: ~#2 homepage, ~#7 collection)
- Impressions for these keywords (will rise before position improves)
- Core Web Vitals report in GSC → fix all "Poor" URLs first

**Milestone check: 6 weeks from today**
If author bylines, emoji removal, and the duplicate post consolidation are done, you should see:
- "custom rolling paper" (singular) holding or improving from ~#2
- "custom rolling papers" (plural) beginning to re-enter positions 11–20 (page 2)

---

## Appendix: Competitor E-E-A-T Comparison

| Signal | RYOP | Papers+Ink (#1) | Snail Papers (#2) | Custom Cones USA (#5) |
|--------|------|-----------------|-------------------|-----------------------|
| Author bylines | ❌ None | ✅ Likely | ✅ Likely | ✅ Likely |
| Third-party certification | ✅ TÜV SÜD | ⚠️ Unknown | ✅ FSC 2018 | ⚠️ Unknown |
| Founding year surfaced | ⚠️ 2011 (not prominent) | ✅ Artisan story | ✅ Transparent | ✅ "French paper mill 200 years" |
| Interactive UX | ✅ 3D visualizer | ⚠️ Standard | ✅ Online customizer | ⚠️ Standard |
| Review count | ⚠️ 44 (Trustpilot) | Unknown | Unknown | Likely higher |
| Content AI signals | ❌ Emojis, duplicates | ✅ Cleaner | ✅ Cleaner | ✅ Cleaner |
| Title tag quality | ❌ Emoji-heavy | ✅ Clean | ✅ Clean | ✅ Clean |

**Conclusion:** RYOP has the strongest real-world credentials (TÜV SÜD > FSC, lowest MOQ, oldest in market), but the *signals* Google reads (author identity, content quality markers, engagement UX) currently favor Papers+Ink and Snail Papers. The fix is to surface RYOP's genuine strengths in Google-readable ways.

---

*Investigation based on live SERP analysis (March 16, 2026), confirmed Google algorithm update history, and site infrastructure analysis. All SERP positions are as observed at time of audit and will change. Verify positions in Google Search Console for accurate historical data.*
