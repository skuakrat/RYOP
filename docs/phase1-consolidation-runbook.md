# Phase 1 — Consolidation runbook

Fixes the root cause: near-duplicate pages splitting authority and confusing Google
about which URL owns which term.

**Do not start Phase 2 (internal links / CTA blocks) until this is done.** Pointing
links at a page while duplicates of it still exist just feeds the duplicates.

---

## Pre-flight — do this first

I could not reach the live store when writing this (network egress restriction), so
**every handle below must be confirmed in Shopify Admin before you execute anything.**

For each URL in `shopify/redirects-phase1.csv`:

1. Open it in a browser. Confirm it resolves (200) and is the page you expect.
2. If a "Redirect from" URL 404s, delete that row — you do not need the redirect.
3. If a "Redirect to" URL 404s, **stop** — the target handle is wrong. Fix it before importing.

Then record a baseline so you can prove the effect later:
- Export the current keyword positions from Ahrefs Rank Tracker.
- Note current organic clicks/day (not per month — August was a 15-day partial in GSC).

---

## Shopify gotchas that will bite you

**1. Shopify will not redirect a URL that still resolves.**
A live collection wins over a redirect. Order of operations for every collection merge:

   a. Move/assign the products to the surviving collection first.
   b. Delete (or unpublish and change the handle of) the duplicate collection.
   c. *Then* create the redirect.

If you create the redirect first, it silently does nothing.

**2. Where redirects live.**
`Online Store → Navigation → URL Redirects` (older admin), or
`Content → Menus → URL redirects` (newer admin). There is a bulk **Import** button
that accepts the CSV in this repo.

**3. Tag-filter URLs cannot be redirected.**
`/collections/x/some-tag` is generated on the fly. Use the canonical fix
(`shopify/collection-tag-canonical.liquid`), not a redirect.

**4. Check internal links before deleting anything.**
Search the theme, navigation menus, footer, and blog content for links to the URL you
are about to remove. A redirect works, but a direct link to the survivor is better —
and a menu item pointing at a deleted collection looks broken in the nav editor.

**5. One cluster at a time.**
Do a cluster, wait, confirm nothing broke, then do the next. If rankings move the
wrong way you want to know which change caused it.

---

## Order of execution — lowest risk first

### Step 1 — Manufacturer page (zero risk, start here)

`/pages/custom-rolling-paper-manufacturer` currently ranks for **literally nothing**,
while the homepage ranks #8 (mobile) / #2 (desktop) for "custom rolling paper
manufacturer". There is a second, undisclosed duplicate at
`/blogs/the-roll-your-own-papers-blog/custom-rolling-paper-manufacturer` (1,322 words).

1. Confirm the blog duplicate exists and is not earning traffic.
2. Unpublish the blog post, then add the redirect (row 1 of the CSV).
3. Add internal links to `/pages/custom-rolling-paper-manufacturer` using the exact
   anchor text **"custom rolling paper manufacturer"** — from the homepage, the about
   page, and 2–3 relevant blog posts.

Nothing can be lost here, which is why it is the test case. If the page starts
picking up its target term within 3–4 weeks, the same pattern will work on the
collection.

### Step 2 — Collection tag URLs (theme change, no deletions)

Apply `shopify/collection-tag-canonical.liquid` to `layout/theme.liquid` — replace the
single existing canonical line. Keep the existing noindex snippet.

Verify after publishing: view source on
`/collections/custom-rolling-papers/samples` and confirm the canonical points to
`/collections/custom-rolling-papers`.

### Step 3 — Packaging collections (4 → 1)

Keep `/collections/custom-cannabis-packaging`. Merge the other three plus their
identical facet children (`/matchbox`, `/shatter`, `/flower-bag`, `/tincture-boxes`).

Follow the products-first, delete, then redirect order above.

### Step 4 — Grinders (2 → 1) and Matchbooks (2 → 1)

Keep `/collections/custom-grinders` and `/collections/custom-matchbooks`.
Same procedure. Note `/collections/custom-matchbooks` already ranks
("custom matchbooks low minimum" #8), so it is clearly the survivor.

### Step 5 — Case variants

301 every capitalised URL to its lowercase twin. Confirm which form is canonical in
the sitemap first and keep that one.

---

## Rolling-tray blog cluster — revised

**Correction to the earlier plan: do not merge 7 into 2.** Ranking data shows three of
these posts are earning and should be left alone.

**Keep — these rank and serve distinct intents:**

| Post | Why it survives |
|---|---|
| `what-to-use-as-a-rolling-tray-7-creative-household-alternatives…` | Strongest of the cluster — #1 "what can i use as a rolling tray", #2 "diy rolling trays", #3 "diy rolling tray ideas", #3 "rolling tray nearby" |
| `how-to-make-a-wooden-rolling-tray-the-ultimate-diy-guide-for-2025` | Owns the build intent — #8 "rolling tray diy", #10 "custom wood rolling tray", #11 "handmade wooden rolling tray" |
| `how-to-clean-a-rolling-tray-the-ultimate-guide-to-a-spotless-tray` | **Ranks #1** for its term and serves a completely separate intent. Do not touch it. |

**Merge — these overlap with the survivors:**

| Post | Merge into |
|---|---|
| `how-to-make-a-rolling-tray-with-resin-your-complete-diy-guide-2025` | wooden-rolling-tray (as a resin section) |
| `how-to-make-custom-rolling-tray-sets-9-creative-diy-methods-2026-guide` | what-to-use-as-a-rolling-tray |
| `6-easy-steps-to-manufacture-your-own-custom-rolling-tray` | → `/collections/custom-rolling-trays` (it is commercial intent wearing a blog URL) |

**Evaluate separately:** `where-to-buy-rolling-tray-near-me…` only holds #10 on a
10-volume term. Weak, but it is local-commercial intent — decide whether to strengthen
it or fold it into the collection.

Merging means: move the genuinely useful content into the survivor first, *then*
unpublish and redirect. Do not redirect a post whose content you have not moved.

---

## Verification after each step

- Fetch the changed URL and confirm the redirect returns **301** (not 302) and lands on
  the intended target in one hop.
- Confirm no redirect chains (A → B → C). Shopify allows them; Google dislikes them.
- Re-crawl in Ahrefs Site Audit and confirm the duplicate-content count falls.
- Watch for the leading signal: does `/collections/custom-rolling-papers` begin ranking
  for any commercial term, and does the dual-rank on "custom rolling papers low
  minimum" (collection #1 + homepage #3) resolve to one page?

Allow 3–6 weeks. Consolidation effects are not immediate.
