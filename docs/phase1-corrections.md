# Phase 1 — corrections after live Ahrefs verification (2026-09-08)

The original Phase 1 runbook was built from Site Audit crawl data that did **not**
distinguish 301-redirecting URLs from live duplicate pages. A targeted re-query proved
several of its premises wrong. This file records what changed and why.

---

## 1. The collection-duplication problem is already fixed

**14 of the 18 rows in the original `redirects-phase1.csv` have been removed.** They
would have been harmful or pointless.

| Group | What the runbook assumed | What is actually live |
|---|---|---|
| Packaging | 4 live duplicates; keep `custom-cannabis-packaging` | `custom-cannabis-packaging` and `custom-canna-packaging` **already 301 to `/collections/custom-packaging`**. The survivor is `custom-packaging` (200, self-canonical, 984 words, 932 internal links). `custom-packaging-flower-oil-pre-rolls` is not in the index at all. |
| Grinders | 2 live duplicates | `custom-herb-grinders` does not exist. `herb-grinders` **already 301s** to `custom-grinders`. Already consolidated. |
| Matchbooks | 2 live duplicates | `custom-matchboxes` **already 301s** to `custom-matchbooks`. Already consolidated. |
| Lighters | 2 live duplicates | `custom-lighters` **already 301s** to `custom-bic-lighters`. Already consolidated. |

**The original CSV would have redirected `/collections/custom-packaging` — the live
survivor holding 932 internal links — into a URL that already redirects back to it.**
That is a redirect loop. Do not use any copy of the pre-2026-09-08 CSV.

Root cause of the error: Ahrefs Site Audit lists 301'd URLs as rows in the crawl. Both
the verification agent and this plan read those rows as live duplicate pages. **Always
check `http_code` and `final_redirect` before treating a URL as a duplicate.**

---

## 2. The lost-rankings hypothesis was wrong

The plan assumed the 25 lost commercial keywords sat on duplicate URLs, making Phase 1
the recovery lever. The URL-level data does not support that.

**What the 14 checked keywords actually show:**

- **6 of 14 came from a single blog post** — `what-is-the-best-weed-grinder-ultimate-2026-guide`
  held *best herb grinders, best weed grinders, best cannabis grinder, best grinders for
  weed, best weed grinder, best herb grinder* and lost all six at once.
- **4 more sat on other informational blog posts** — rolling tray dimensions, rolling
  papers near me, gas station pre rolls, how much are prerolls.
- **Only 4 involved commercial pages**, and three of those **still rank on desktop**:
  custom rolling papers low minimum (desktop #2), custom rolling tray wholesale
  (desktop #6), custom printed rolling papers (desktop #6).

**The loss is substantially mobile-specific.** On desktop 3 of 14 still hold positions;
on mobile all 14 are null. This is not sitewide deindexing and it is not duplication —
it is concentrated in informational blog content, on mobile.

**Revised priority:** investigate the grinder guide post first. One URL losing six
rankings simultaneously is the largest single identifiable loss on the site.

---

## 3. Money-page on-page state is better than assumed

Only **2 of 7** money pages carry the multiple-H1 issue, and **none** has a duplicate
meta description:

| Page | H1s | Meta desc | Internal links |
|---|---|---|---|
| `/` (homepage) | **3** ⚠ | 1 | 932 |
| `/pages/wholesale-rolling-papers` | **3** ⚠ | 1 | **0** ⚠ |
| `/collections/custom-rolling-papers` | 1 ✓ | 1 ✓ | 932 |
| `/collections/custom-pre-rolled-cones` | 1 ✓ | 1 ✓ | 932 |
| `/collections/custom-joint-tips` | 1 ✓ | 1 ✓ | 932 |
| `/collections/custom-rolling-trays` | 1 ✓ | 1 ✓ | 932 |
| `/pages/custom-rolling-paper-manufacturer` | 1 ✓ | 1 ✓ | 932 |

The sitewide "380 multiple-H1 pages" figure is real but **does not hit the money pages**,
so it drops down the priority list.

**New finding: `/pages/wholesale-rolling-papers` is orphaned** — 0 incoming internal
links where every other money page has 932. It targets "wholesale rolling papers"
(vol 250). Adding internal links to it is cheap and uncontested.

---

## 4. Unresolved: which page owns the commercial terms

Two Ahrefs queries return **contradictory URL attribution for the same positions**.

- Earlier pull (`mode=subdomains`, reading `best_position_url`) → **the homepage** holds
  custom rolling papers #5, branded #3, wholesale #5, booklets #5, custom rolling
  paper #7, manufacturer #8.
- Later pull (`mode=exact` on the collection) → **`/collections/custom-rolling-papers`**
  holds custom rolling papers #5, branded #3, wholesale #5, booklets #5, custom rolling
  paper #7, manufacturer #8.

**The position numbers are identical in both.** One query is mis-attributing the URL.
The agent running the second pull independently flagged that its `where` filters were
returning padded, non-matching rows — so `mode=exact` leaking domain-level results is
the more likely explanation, but it is not proven.

A third data point (an independent pull on 2026-08-12) gave
`best_position_url = https://www.rollyourownpapers.com/` for "custom rolling papers",
supporting the homepage reading.

**This blocks Phase 2.** If the collection already owns the commercial terms, the
re-targeting work is unnecessary and would risk a structure that is already correct.

**Decisive re-query:** run `site-explorer-organic-keywords` with `mode=subdomains`,
`select=keyword,best_position,best_position_url`, filtered to the single keyword
`custom rolling papers`. One row, one authoritative URL. Cross-check against
`rank-tracker-overview` (project 1703417, both devices) reading the `url` column.

Confirmed regardless: **"custom rolling papers low minimum" genuinely dual-ranks** —
collection and homepage both appear in the same SERP on the same date.

---

## 5. Still valid from the original plan

- **Redirect the blog manufacturer duplicate.** Confirmed HTTP 200, self-canonical, not
  noindexed, **0 organic keywords and 0 traffic**. Safe to redirect, nothing to lose.
- **Tag-filter variants** — 35 URLs under `/collections/custom-rolling-papers/`, all
  `noindex:true`. Only `/samples` holds positions (7). Case-variant duplicates exist but
  already canonicalise to the lowercase form, so the canonical snippet is a smaller win
  than assumed. Worth applying; not urgent.
- **Rolling-tray blog merges** — unchanged; three posts rank and are kept, three merge.
  URLs in the CSV still need confirming against the live store.
