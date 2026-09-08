# Fixing the orphaned wholesale page

`/pages/wholesale-rolling-papers` — **0 incoming internal links** where every other
money page has 932. It is a fully built 1,510-word page targeting "wholesale rolling
papers" (vol 250), and it ranks for nothing, while the term itself sits at **#7 on
desktop** held by a different URL.

Two problems, both cheap to fix: it is orphaned, and it has 3 H1s.

---

## Part A — the H1 fix (do this first, 5 minutes)

Current state, from live crawl:

| H1 | Action |
|---|---|
| `Wholesale Rolling Papers` | **Keep as the only H1** |
| `Why Brands Switch From Generic Wholesale to Custom` | Change to `<h2>` |
| `Low Minimum Custom Rolling Paper Booklets For SWAG!` | Change to `<h2>` |

**Note — this third H1 also appears on the homepage** (it is one of the homepage's three
H1s). The same string on two pages means it is a **shared theme section**, not page
content. Fix it in the section file and both pages are corrected at once. Look for the
section that renders that heading and change its wrapper tag from `h1` to `h2`; if the
section has a heading-level setting in the theme editor, use that instead of editing code.

A page should have exactly one H1, and it should contain the target term. "Wholesale
Rolling Papers" already does — nothing else needs rewriting.

---

## Part B — the internal link plan

Vary the anchor text. Using the identical exact-match phrase on every link reads as
manipulation; a natural mix of exact, partial and branded anchors is both safer and
more effective.

### Tier 1 — highest authority (do these four)

**1. Footer link — sitewide, biggest single win**
A footer link appears on every page, so this alone takes the page from 0 incoming links
to site-wide coverage.
Menu item text: **Wholesale**
Target: `/pages/wholesale-rolling-papers`
*(Shopify Admin → Content → Menus → Footer menu → Add menu item)*

**2. From the rolling-papers collection description**
You control this content already. Add near the end of the description on
`/collections/custom-rolling-papers`:

```html
<p>Ordering at volume for retail? See our <a href="/pages/wholesale-rolling-papers">wholesale rolling papers</a> pricing and bulk terms.</p>
```

**3. From the manufacturer page**
Manufacturer and wholesale are a natural pair, and this page has 932 incoming links to
pass along. Add to `/pages/custom-rolling-paper-manufacturer`:

```html
<p>Buying for resale? We supply <a href="/pages/wholesale-rolling-papers">rolling papers wholesale</a> direct from our own factory, with the same certifications and no distributor markup.</p>
```

**4. From the homepage body**
Add a sentence in the existing body copy — not a nav item, an in-content link, which
carries more weight:

```html
<p>Retailers and distributors can <a href="/pages/wholesale-rolling-papers">buy rolling papers wholesale</a> direct from the factory.</p>
```

### Tier 2 — main navigation

Add **Wholesale** to the main menu, ideally under a B2B or "For Business" grouping if
one exists. If the nav is already crowded, the footer link in Tier 1 does most of the
work — do not force it.

### Tier 3 — re-point two blog CTAs

Two of the 20 CTA blocks in `shopify/blog-cta-blocks.html` carry **wholesale intent**
but currently point at the papers collection. Send them here instead:

| Post | Clicks/6mo | Current CTA target | Change to |
|---|---|---|---|
| `how-old-do-you-have-to-be-to-buy-rolling-papers` | 1,064 | `/collections/custom-rolling-papers` | `/pages/wholesale-rolling-papers` |
| `how-much-is-rolling-paper-at-a-gas-station` | 436 | `/collections/custom-rolling-papers` | `/pages/wholesale-rolling-papers` |

Both already speak to shop owners ("Run a smoke shop or dispensary?" and "Factory-direct
beats gas station prices"), so the copy needs no change — only the `href` and the button
label:

```html
<a href="/pages/wholesale-rolling-papers" class="btn">See Wholesale Pricing →</a>
```

---

## Anchor-text summary

Seven links, deliberately varied:

| Source | Anchor text | Type |
|---|---|---|
| Footer (sitewide) | Wholesale | branded/nav |
| Collection description | wholesale rolling papers | exact |
| Manufacturer page | rolling papers wholesale | exact, reordered |
| Homepage body | buy rolling papers wholesale | partial |
| Main nav | Wholesale | branded/nav |
| Blog CTA (age limits) | See Wholesale Pricing | partial |
| Blog CTA (gas station) | See Wholesale Pricing | partial |

Roughly one third exact-match, two thirds natural variation.

---

## What to expect

This is a low-risk, uncontested fix — the page currently ranks for nothing, so there is
no position to lose. "wholesale rolling papers" already sits at **#7 on desktop** via
another URL, which means the site has the authority to rank for it; the question is
only which page Google picks.

Allow **3–6 weeks**. The signal to watch: does `/pages/wholesale-rolling-papers` begin
appearing in Ahrefs Site Explorer for any keyword at all? Going from zero keywords to
any keyword is the proof the links registered.

**Caveat:** the nav and footer structure could not be verified from here (the live site
is blocked by this environment's network egress restriction). Confirm the menu names in
Shopify Admin before adding items.
