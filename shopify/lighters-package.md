# Lighters package — A1 + A2 + C2

Fixes the worst-performing money page on the site in one pass.

**Why this page:** `/collections/custom-bic-lighters` sits at **position 47** with **0 referring
domains** and **3 clicks in 3 months**. It ranks for **zero** US organic keywords — it does not
appear anywhere in a live pull of every lighter-related term the site ranks for.

Meanwhile the DIY blog posts rank well for lighter terms. Buyers searching lighter keywords land
on a how-to craft guide instead of the product page. That is the whole problem, and it is fixable.

---

## Part A1 — Title tag (2 minutes)

Current title renders at **82 characters** and is double-branded, because the theme appends the
shop name when it is not already present in the title.

**Shopify Admin → Products → Collections → Custom Bic Lighters → Edit website SEO → Page title:**

```
Custom Bic & Clipper Lighters | Roll Your Own Papers
```

52 characters, brand appears once. Because the brand is now inside the title, the theme will not
append it a second time.

**While you're there — Trays** (currently 65 chars, truncates in Google):

```
Custom Rolling Trays | Wholesale | Roll Your Own Papers
```

55 characters. **Cones is fine at 60 — leave it.**

**Verify:** view the live page source, or use Google's preview. Title ≤60 characters, brand once.

---

## Part A2 — Alt text

The plan said Trays 11 / Cones 6 / Lighters 3 images. Live Site Audit reports **6 pages** total
with missing alt text sitewide — smaller than expected, so this is a short job.

**Shopify Admin → Products → [product] → click image → Edit alt text**

Pattern: `Custom [material/format] [product] with branded logo print`

| Product type | Example alt text |
|---|---|
| Lighter | `Custom Bic lighter with full-colour branded logo print` |
| Tray | `Custom tin rolling tray with full-colour logo print` |
| Cone | `Custom pre-rolled cone in branded retail packaging` |

Write what the image actually shows. Do not stuff keywords — describe it for someone who cannot
see it, and the keyword lands naturally.

---

## Part C2 — Point the DIY posts at the collection

These are the exact posts and what they currently rank for. All URLs verified live.

### Post 1 — `/blogs/the-roll-your-own-papers-blog/how-to-make-custom-lighters-ultimate-diy-guide`

**The big one.** Ranks for 9 lighter keywords:

| Keyword | Position | Vol |
|---|---|---|
| make custom lighters | **#2** | 30 |
| diy custom lighters | **#4** | 30 |
| how to make custom lighters | #6 | 100 |
| how to make a custom lighter | #7 | 70 |
| how to customize lighters | #9 | 20 |
| make your own lighters | #9 | 20 |
| diy lighters | #9 | 20 |
| diy custom lighter | #9 | 10 |
| build your own lighter kit | #10 | 20 |

### Post 2 — `/blogs/.../how-to-make-custom-lighters-with-cricut-complete-2026-guide`

| Keyword | Position | Vol |
|---|---|---|
| how to make lighter wraps | #4 | 20 |
| how to make custom lighter wraps | #5 | 20 |
| **how to make custom bic lighters** | **#7** | 20 |

That third one matters — it is a *bic lighter* term held by a blog post while the bic lighter
collection ranks for nothing.

### Post 3 — `/blogs/.../how-to-make-custom-lighters-with-pictures-your-ultimate-diy-guide`

| Keyword | Position | Vol |
|---|---|---|
| how to make custom lighters with pictures | #3 | 30 |
| how to make your own lighter | #5 | 10 |
| make picture lighter | #9 | 10 |

### The CTA block

Paste **near the top** of each post — after the intro, before the first how-to step. Readers
who want to buy rather than craft should not have to scroll a whole tutorial to find out you
sell them.

Paste in **HTML view (`<>`)**.

```html
<div style="background-color: #f4fdf4; padding: 40px 20px; border-radius: 12px; text-align: center; font-family: Arial,sans-serif; margin: 30px 0;">
<h2 style="font-size: 28px; color: #2e7d32; margin-bottom: 15px;">🔥 Need More Than One? We Print Them.</h2>
<p style="font-size: 18px; color: #333; max-width: 800px; margin: 0 auto 20px;">DIY is great for a single lighter. If you need a hundred with your logo on them — for a shop, an event, or a brand giveaway — we print <a href="/collections/custom-bic-lighters">custom Bic lighters</a> and Clipper lighters direct from the factory, no craft supplies required.</p>
<ul style="list-style: none; padding: 0; font-size: 17px; color: #444; line-height: 1.7; max-width: 700px; margin: 0 auto 25px;">
<li>✔️ Your logo printed, not stickered — it won't peel</li>
<li>✔️ Bic and Clipper, full colour, low minimums</li>
<li>✔️ Free design — send artwork, we build the print file</li>
<li>✔️ Free mock-up before you commit</li>
</ul>
<a href="/collections/custom-bic-lighters" style="display: inline-block; background-color: #43a047; color: #fff; font-size: 18px; font-weight: bold; padding: 15px 30px; border-radius: 8px; text-decoration: none; margin: 0 6px 12px;">🛒 See Custom Lighters</a>
<a href="/pages/get-a-free-mock-up" style="display: inline-block; background-color: #fff; color: #2e7d32; font-size: 18px; font-weight: bold; padding: 13px 28px; border: 2px solid #43a047; border-radius: 8px; text-decoration: none; margin: 0 6px 12px;">🎨 Get a Free Mock-Up</a>
<p style="font-size: 16px; color: #666; margin-top: 20px;">🏭 <strong>Factory direct since 2011</strong> | 🚚 <strong>Free worldwide shipping</strong> | 🎨 <strong>Free design</strong></p>
</div>
```

Note the **in-sentence link** on "custom Bic lighters" as well as the button. The text link
carries the keyword anchor; the button carries the clicks. Text link first — Google credits the
first link to a URL on a page.

---

## Bonus — the same pattern on matchbooks

Identical shape, and it should move faster because the matchbooks collection **already ranks**.

| Post / page | Term | Position |
|---|---|---|
| `/blogs/.../custom-matchbooks-with-logo-the-cool-way-to-spark-your-brand-in-2026` | logo matchbooks | **#3** |
| `/blogs/.../how-to-make-custom-matchboxes-7-easy-diy-methods-2025-guide` | how to make custom matchbooks | #7 |
| `/collections/custom-matchbooks` | custom matchbooks low minimum | **#8** ✅ |

Point both posts at `/collections/custom-matchbooks` with a **"custom matchbooks"** anchor. Same
block as above, swapping the product words and both hrefs.

---

## What to watch

The signal is simple: does `/collections/custom-bic-lighters` start appearing in Ahrefs Site
Explorer for **any** keyword? It currently ranks for zero, so zero → anything proves the links
registered.

Allow **4–8 weeks**. This page has 0 referring domains, so internal links are doing all the work —
it will move slower than the wholesale page did.

**Caveat:** internal links alone may not be enough here. Lighters ranks #47 with **zero** external
links, and the refdomain/position correlation across your money pages is close to perfect
(196→#13, 20→#15, 10→#18, 0→#47). This package removes the cannibalisation and fixes the on-page,
which is necessary — but D1 (backlinks) is what lifts the ceiling.
