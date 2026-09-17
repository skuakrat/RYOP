#!/usr/bin/env python3
"""
RYOP - Append a matched CTA block to the end of each of the top 20 blog posts.

Each post is matched by its handle. The CTA block is appended to the post's
body_html. A hidden marker comment (<!-- ryop-cta-v1 -->) is embedded so the
script is SAFE TO RE-RUN: a post that already has the block is skipped, never
duplicated.

The button uses the theme's .btn class so it inherits site styling.

HOW TO RUN (Windows PowerShell):
    python get_token.py                 # get a fresh token if needed (~24h)
    # then either set the env var:
    $env:SHOPIFY_TOKEN = "shpat_xxx"
    # or hardcode it below in TOKEN = "..."

    python apply_cta_blocks.py --dry-run   # preview: shows which posts get a block
    python apply_cta_blocks.py             # apply for real
"""
import os, sys, time, json, urllib.request, urllib.error

STORE   = "customrollingpaper.myshopify.com"
DRY_RUN = "--dry-run" in sys.argv
API     = "2024-01"
BASE    = f"https://{STORE}/admin/api/{API}"
TOKEN   = os.environ.get("SHOPIFY_TOKEN", "")   # or paste: TOKEN = "shpat_xxx"
HEADERS = {}

MARKER = "<!-- ryop-cta-v1 -->"

def cta(headline, body, href, label):
    """Build one CTA block. Marker comment makes re-runs idempotent."""
    return (
        f'\n{MARKER}\n'
        '<div style="border: 2px solid #41ad54; background: #f4faf5; '
        'padding: 24px; margin: 32px 0; text-align: center;">\n'
        f'  <p style="font-weight: 700; font-size: 1.1em; margin-bottom: 8px;">{headline}</p>\n'
        f'  <p style="margin-bottom: 16px;">{body}</p>\n'
        f'  <a href="{href}" class="btn">{label}</a>\n'
        '</div>\n'
    )

# handle -> CTA block. Top 20 KEEP-CTA posts by GSC clicks (last 6 months).
BLOCKS = {
 "can-you-smoke-the-yellow-paper-in-rolling-papers": cta(
   "Want papers you never have to second-guess?",
   "RYOP papers are TÜV SÜD certified — pure natural paper, safe-to-consume Arabic gum, soy ink. We custom print them with your logo from just 150 booklets, with free design and free worldwide shipping.",
   "/collections/custom-rolling-papers", "See Custom Rolling Papers →"),
 "where-to-get-rolling-paper-near-me": cta(
   "Skip the store run — get papers made for you.",
   "RYOP ships TÜV SÜD certified rolling papers worldwide, free. Want your own brand on them? Custom printing starts at just 150 booklets with no setup fees.",
   "/collections/custom-rolling-papers", "Shop Rolling Papers →"),
 "how-to-use-tips-with-rolling-paper": cta(
   "Never fold another tip by hand.",
   "RYOP makes custom printed tips and pre-rolled crutches — branded with your logo, ready to use. Booklets with built-in tips start at 132 booklets.",
   "/collections/custom-joint-tips", "See Custom Tips →"),
 "how-to-roll-rolling-paper-into-a-cone": cta(
   "Or skip the rolling entirely.",
   "RYOP manufactures custom pre-rolled cones — perfectly shaped every time, with your branding on the packaging. Factory-direct, TÜV SÜD certified paper, free worldwide shipping.",
   "/collections/custom-pre-rolled-cones", "See Custom Pre-Rolled Cones →"),
 "how-to-make-a-filter-out-of-rolling-paper": cta(
   "DIY filters work — ready-made crutches work better.",
   "RYOP booklets come with custom printed tips built in, so you never tear a card again. From 132 booklets with your branding, free design included.",
   "/collections/custom-joint-tips", "See Tips &amp; Crutches →"),
 "why-is-my-rolling-paper-not-sticking": cta(
   "Tired of gum that won't stick?",
   "RYOP papers use 100% pure Arabic gum — the same natural adhesive premium brands use, TÜV SÜD certified safe to consume. It seals on the first lick, every time.",
   "/collections/custom-rolling-papers", "Try Papers That Stick →"),
 "how-old-do-you-have-to-be-to-buy-rolling-papers": cta(
   "Run a smoke shop or dispensary?",
   "Stock your own house-brand papers instead of someone else's. RYOP custom prints rolling papers with your logo from 150 booklets — factory-direct pricing, free worldwide shipping.",
   "/collections/custom-rolling-papers", "Create Your House Brand →"),
 "whats-the-best-rolling-paper": cta(
   "The best rolling paper is the one made your way.",
   "Choose your material — rice, natural fibre, or unbleached wood pulp — your size, and your design. RYOP prints it from 150 booklets. Not sure yet? Order a sample pack and test them all.",
   "/products/free-rolling-paper-samples-pay-for-shipping-only", "Order a Sample Pack →"),
 "what-is-the-healthiest-rolling-paper": cta(
   "Want proof, not promises?",
   "RYOP papers are TÜV SÜD Germany certified: pure natural paper, safe-to-consume Arabic gum, and soy ink. See the actual certificates — then get them printed with your own brand.",
   "/pages/product-certifications", "See Our Certifications →"),
 "what-rolling-paper-burns-the-slowest": cta(
   "Slow burn, your brand.",
   "Our 13.5 GSM white rice paper burns slow and clean — the same class as Elements. RYOP custom prints it with your logo from 150 booklets, free design and worldwide shipping included.",
   "/collections/custom-rolling-papers", "See Slow-Burn Papers →"),
 "how-much-is-rolling-paper-at-a-gas-station": cta(
   "Factory-direct beats gas station prices.",
   "RYOP makes papers in our own facility — no middlemen, no markup. Custom printed booklets from 150 units with free worldwide shipping, and a price match guarantee.",
   "/collections/custom-rolling-papers", "See Factory Pricing →"),
 "top-10-other-uses-of-rolling-paper": cta(
   "Here's use #11: the cleverest business card ever made.",
   "RYOP prints rolling paper business cards, wedding invitations, and event giveaways — your design on real, usable papers. From 150 booklets, free mockup before you commit.",
   "/products/custom-rolling-paper-business-cards", "See Rolling Paper Business Cards →"),
 "which-side-of-the-rolling-paper-do-you-lick": cta(
   "Now that you know which side — make it your side.",
   "RYOP custom prints rolling papers with your logo, edge to edge, on TÜV SÜD certified paper with pure Arabic gum. From 150 booklets, free design service.",
   "/collections/custom-rolling-papers", "Design Your Papers →"),
 "can-pre-rolls-go-bad": cta(
   "Keep pre-rolls fresh with packaging built for it.",
   "RYOP makes custom pre-roll packaging — smell-proof, child-resistant, and branded with your logo. Plus custom pre-rolled cones to fill them with.",
   "/collections/pre-rolled-cone-packaging", "See Pre-Roll Packaging →"),
 "what-is-weed-rolling-paper-called": cta(
   "Whatever you call them, we'll put your name on them.",
   "RYOP custom prints rolling papers, cones, and tips with your brand — factory-direct since 2011, TÜV SÜD certified, from just 150 booklets.",
   "/collections/custom-rolling-papers", "See Custom Papers →"),
 "what-size-is-1-1-4-rolling-paper": cta(
   "1¼ is our most popular custom size.",
   "RYOP prints 1¼ booklets (77×44 mm) with your logo — plus King Slim, Single Wide, and fully custom dimensions. From 150 booklets with free design and worldwide shipping.",
   "/products/custom-printed-booklets-in-one-and-a-quarter-size", "See 1¼ Custom Booklets →"),
 "where-to-buy-rolling-paper-near-me": cta(
   "The best papers aren't at the corner store.",
   "RYOP ships TÜV SÜD certified papers worldwide for free — stock designs or fully custom with your own branding from 150 booklets.",
   "/collections/custom-rolling-papers", "Shop Rolling Papers →"),
 "how-to-get-rolling-paper-to-stick": cta(
   "Solution #16: papers with gum that actually works.",
   "Every RYOP paper uses 100% pure Arabic gum — TÜV SÜD certified, safe to consume, seals first time. Custom printed with your brand from 150 booklets.",
   "/collections/custom-rolling-papers", "See Our Papers →"),
 "is-rolling-paper-harmful": cta(
   "Don't take a brand's word for it — check the certificate.",
   "RYOP papers are independently certified by TÜV SÜD Germany: pure natural paper, safe-to-consume Arabic gum, soy ink. The certificates are public — see for yourself.",
   "/pages/product-certifications", "View Certifications →"),
 "what-is-the-thinnest-rolling-paper": cta(
   "Ultra-thin, ultra-custom.",
   "RYOP's unbleached wood pulp paper is just 12.5 GSM — RAW Brown class — and we print your brand on it from 150 booklets. Order a sample pack to feel the difference first.",
   "/products/free-rolling-paper-samples-pay-for-shipping-only", "Order Samples →"),
}

def get(path):
    req = urllib.request.Request(f"{BASE}{path}", headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def put(path, payload):
    body = json.dumps(payload).encode()
    req = urllib.request.Request(f"{BASE}{path}", data=body, method="PUT", headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return r.status

def blog_id():
    data = get("/blogs.json")
    for b in data["blogs"]:
        if "roll-your-own" in b["handle"] or "the-roll" in b["handle"]:
            return b["id"]
    return data["blogs"][0]["id"]

def all_articles(bid):
    articles, since_id = [], 0
    while True:
        data = get(f"/blogs/{bid}/articles.json?limit=250&since_id={since_id}&fields=id,title,handle,body_html")
        batch = data.get("articles", [])
        if not batch:
            break
        articles.extend(batch)
        since_id = batch[-1]["id"]
        if len(batch) < 250:
            break
        time.sleep(0.3)
    return articles

def main():
    global HEADERS
    if not TOKEN:
        print("ERROR: Set SHOPIFY_TOKEN first (run get_token.py), or hardcode TOKEN.")
        sys.exit(1)
    HEADERS = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}

    bid = blog_id()
    print(f"Blog ID: {bid}")
    articles = all_articles(bid)
    by_handle = {a["handle"]: a for a in articles}
    print(f"Scanned {len(articles)} posts. Targeting {len(BLOCKS)} CTA blocks.\n")
    if DRY_RUN:
        print("DRY RUN - nothing will change.\n")

    added = skipped = missing = errors = 0
    for handle, block in BLOCKS.items():
        a = by_handle.get(handle)
        if not a:
            print(f"NOT FOUND: {handle}  (check the handle/blog)")
            missing += 1
            continue
        body = a.get("body_html") or ""
        if MARKER in body:
            print(f"ALREADY HAS CTA, skipping: {handle}")
            skipped += 1
            continue
        new_body = body + block
        try:
            if DRY_RUN:
                print(f"WOULD ADD CTA -> {handle}")
                added += 1
            else:
                put(f"/blogs/{bid}/articles/{a['id']}.json",
                    {"article": {"id": a["id"], "body_html": new_body}})
                print(f"ADDED CTA -> {handle}")
                added += 1
                time.sleep(0.5)
        except urllib.error.HTTPError as e:
            print(f"HTTP {e.code} on: {handle}")
            errors += 1
            time.sleep(2)

    verb = "Would add" if DRY_RUN else "Added"
    print(f"\nDone. {verb}: {added} | Already had: {skipped} | Not found: {missing} | Errors: {errors}")

if __name__ == "__main__":
    main()
