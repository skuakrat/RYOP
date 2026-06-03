#!/usr/bin/env python3
"""
RYOP — Set 173 old blog posts to DRAFT (unpublish). Nothing is deleted.

This is fully self-contained. You do NOT need the repo or any CSV.
Just save this file anywhere and run it.

HOW TO RUN (Mac/Linux terminal, or Windows Command Prompt):

    1. Save this file as  draft_posts.py  on your Desktop
    2. Open Terminal and go to the Desktop:
           cd ~/Desktop          (Mac/Linux)
           cd %USERPROFILE%\\Desktop   (Windows)
    3. Set your token and run a safe preview first:
           SHOPIFY_TOKEN=shpat_xxx python3 draft_posts.py --dry-run
       (Windows Command Prompt:
           set SHOPIFY_TOKEN=shpat_xxx
           python draft_posts.py --dry-run )
    4. If the preview looks right, run for real (remove --dry-run):
           SHOPIFY_TOKEN=shpat_xxx python3 draft_posts.py
"""
import os, sys, time, json, urllib.request, urllib.error, urllib.parse

STORE     = "customrollingpaper.myshopify.com"
DRY_RUN   = "--dry-run" in sys.argv
API       = "2024-01"
BASE      = f"https://{STORE}/admin/api/{API}"

# Either provide a ready access token (SHOPIFY_TOKEN), OR provide a
# Client ID + Client Secret and the script will exchange them for a
# short-lived token via the client_credentials grant (new Dev Dashboard).
TOKEN         = os.environ.get("SHOPIFY_TOKEN", "")
CLIENT_ID     = os.environ.get("SHOPIFY_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("SHOPIFY_CLIENT_SECRET", "")

def fetch_token():
    """Exchange client_id + client_secret for an access token."""
    url = f"https://{STORE}/admin/oauth/access_token"
    data = urllib.parse.urlencode({
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }).encode()
    req = urllib.request.Request(url, data=data, method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req) as r:
        body = json.loads(r.read())
    return body["access_token"]

HEADERS = {}  # set after we have a token


SLUGS = [
    "2019-novel-coronavirus-production-delays",
    "2021-the-year-of-the-ox",
    "4-20-promotional-products",
    "4-20-swag",
    "5-luxury-herb-promo-gifts-for-the-sophisticated-stoner",
    "8-cool-hacks-to-grind-herbal-without-a-grinder",
    "amazon-pre-rolled-cones",
    "are-infused-pre-rolls-worth-it-the-ultimate-guide-to-enhanced-pre-roll",
    "are-pre-rolls-any-good-the-honest-truth-about-quality-value-amp-what-to-expect",
    "are-pre-rolls-legal-in-2025-a-friendly-no-stress-guide",
    "are-pre-rolls-worth-buying-the-complete-truth-about-value-quality",
    "can-i-bring-a-weed-grinder-on-a-plane-complete-tsa-guide-2025",
    "can-i-leave-weed-in-my-grinder-2025-guide",
    "can-weed-expire-in-a-bag-here-s-what-you-need-to-know",
    "can-you-bring-a-rolling-tray-on-a-plane-the-ultimate-travel-guide",
    "can-you-bring-a-weed-grinder-on-a-plane",
    "can-you-bring-pre-rolls-in-a-checked-bag-know-before-you-fly",
    "can-you-bring-weed-gummies-in-a-checked-bag-2025-traveler-s-guide",
    "can-you-fly-with-weed-gummies-in-checked-bag-2025-tsa-rules",
    "can-you-put-weed-in-a-checked-bag-the-essential-guide-for-u-s-travelers",
    "can-you-use-a-spice-grinder-for-weed-the-real-scoop",
    "can-you-use-parchment-paper-as-rolling-paper-here-s-why-you-should-think-twice",
    "can-you-use-seaweed-as-rolling-paper",
    "can-you-use-toilet-paper-as-rolling-paper-2025-guide",
    "cannabis-packaging",
    "cannabis-promotional-products",
    "cannabis-swag",
    "chinese-new-years-2022-the-year-of-the-tiger",
    "custom-cannabis-promo",
    "custom-printed-pre-roll-cones",
    "custom-printed-rolling-papers",
    "custom-rolling-papers",
    "custom-rolling-papers-manufacturer",
    "custom-rolling-tray",
    "differentiating-good-and-bad-quality-herb-buds",
    "dispensary-promotional-products",
    "do-gas-stations-sell-pre-rolls-the-truth-nobodys-telling-you",
    "do-pre-rolls-have-nicotine-the-ultimate-truth-you-need-to-know",
    "do-smell-proof-bags-for-herb-work",
    "do-smoke-shops-sell-pre-rolls-the-complete-insiders-guide",
    "dream-it-and-we-can-make-it",
    "f-k-covid-19-we-back",
    "herb-packaging-how-to-keep-your-herb-fresh",
    "how-big-is-a-rolling-tray-your-complete-size-guide-2025",
    "how-do-you-clean-a-weed-grinder-without-overthinking-it",
    "how-does-a-weed-grinder-work-the-complete-guide-youve-been-looking-for",
    "how-high-rolling-tray-the-fun-handy-tray-that-levels-up-your-ritual",
    "how-long-do-pre-rolls-last",
    "how-long-is-weed-good-in-a-plastic-bag-the-complete-2025-storage-guide",
    "how-many-grams-are-in-a-bag-of-weed-2025-update-slang",
    "how-many-grams-is-a-bag-of-weed-a-no-stress-2025-guide",
    "how-much-are-pre-rolls-in-dispensary-real-world-price-guide-ways-to-save",
    "how-much-are-pre-rolls-in-texas-real-prices-where-to-buy-2026-guide",
    "how-much-are-pre-rolls-in-the-usa-2025-average-prices-by-state-what-affects-the-cost",
    "how-much-do-pre-rolls-cost-in-2025-a-real-world-guide-to-prices-packs-and-savings",
    "how-much-does-a-quarter-bag-of-weed-weigh",
    "how-much-does-a-weed-grinder-cost-2025-price-guide",
    "how-much-is-a-bag-of-weed-your-complete-price-guide-for-2025",
    "how-much-is-a-dime-bag-of-weed-the-2025-complete-guide",
    "how-much-is-a-rolling-tray-in-2025-a-friendly-guide-to-prices-materials-creative-uses",
    "how-often-should-i-clean-my-weed-grinder-your-complete-maintenance-guide",
    "how-old-do-you-have-to-be-to-buy-a-rolling-tray-age-laws-faqs-2025",
    "how-to-bag-weed-a-complete-guide-to-keeping-your-stash-fresh-and-discreet",
    "how-to-clean-a-herb-grinder-the-ultimate-guide-that-actually-works",
    "how-to-clean-a-metal-rolling-tray-the-ultimate-step-by-step-guide",
    "how-to-clean-a-metal-weed-grinder-ultimate-guide-2025",
    "how-to-clean-a-rolling-tray-the-ultimate-guide-to-a-spotless-tray",
    "how-to-clean-a-weed-grinder-make-it-like-new",
    "how-to-clean-a-weed-grinder-with-hot-water-easy-steps-for-a-spotless-tool",
    "how-to-clean-glass-filter-tips-2025-guide",
    "how-to-clean-herb-grinder-easy-steps-for-a-sparkly-clean-tool",
    "how-to-clean-weed-grinder-fast-safe-and-like-new",
    "how-to-clean-your-weed-grinder-without-alcohol",
    "how-to-enjoy-weed-without-bong-or-rolling-paper-15-creative-methods-that-actually-work",
    "how-to-fix-a-broken-cigarette-without-rolling-paper-7-genius-hacks",
    "how-to-get-every-last-bit-from-your-grinder",
    "how-to-grind-up-sticky-weed-without-a-grinder",
    "how-to-grind-weed-if-you-dont-have-a-grinder-10-clever-hacks",
    "how-to-grind-weed-with-a-grinder-your-ultimate-guide",
    "how-to-grind-weed-without-a-grinder-10-clever-diy-methods",
    "how-to-grind-weed-without-grinder-12-genius-hacks-you-need-to-know",
    "how-to-maintain-your-resin-rolling-tray-faq-complete-care-guide-2025",
    "how-to-make-a-custom-glitter-rolling-tray-diy-guide",
    "how-to-make-a-cute-rolling-tray-in-2025-super-easy-actually-adorable-diy-ideas",
    "how-to-make-a-dice-rolling-tray-2025-diy-guide",
    "how-to-make-a-grinder-for-weed-diy-herb-grinder-guide",
    "how-to-make-a-homemade-weed-grinder-12-safe-and-clever-methods",
    "how-to-make-a-joint-without-rolling-paper",
    "how-to-make-a-rolling-tray-diy-and-how-they-re-made-industrially",
    "how-to-make-a-rolling-tray-with-resin-your-complete-diy-guide-2025",
    "how-to-make-a-smell-proof-bag-for-weed-your-ultimate-diy-guide",
    "how-to-make-a-weed-grinder-out-of-wood",
    "how-to-make-a-wooden-rolling-tray-the-ultimate-diy-guide-for-2025",
    "how-to-make-an-led-rolling-tray-step-by-step-diy-guide",
    "how-to-make-custom-rolling-tray-sets-9-creative-diy-methods-2026-guide",
    "how-to-make-custom-rolling-trays",
    "how-to-make-custom-rolling-trays-the-ultimate-diy-guide-in-2025",
    "how-to-make-hemp-rolling-paper-at-home-a-step-by-step-diy-guide",
    "how-to-make-rolling-paper-at-home-the-ultimate-diy-guide",
    "how-to-make-rolling-paper-from-leaves-easy-natural-diy-methods-that-actually-work",
    "how-to-make-rolling-paper-from-rice-the-complete-diy-guide",
    "how-to-open-a-weed-grinder-15-easy-methods-that-actually-work",
    "how-to-put-a-picture-on-a-rolling-tray-5-easy-methods-that-actually-work",
    "how-to-roll-a-joint-without-rolling-paper-15-creative-alternatives-that-actually-work",
    "how-to-roll-glass-tips-the-complete-2025-guide",
    "how-to-roll-glass-tips-the-complete-2025-guide-for-perfect-sessions-every-time",
    "how-to-ship-glass-jars-safely-packaging-tips",
    "how-to-smoke-pre-rolls-your-first-timers-guide-21",
    "how-to-smoke-weed-if-you-dont-have-rolling-paper",
    "how-to-smoke-weed-without-pipe-or-rolling-paper-smart-creative-amp-real-world-alternatives",
    "how-to-smoke-weed-without-rolling-paper-2025-guide",
    "how-to-smoke-weed-without-rolling-paper-or-bong-13-clever-hacks-for-when-you-re-all-out",
    "how-to-stop-weed-smelling-in-a-bag-without-losing-your-mind-or-your-herb",
    "how-to-use-a-rolling-tray-2025-guide-clean-organized-effortless-rolls",
    "how-to-use-a-weed-grinder-step-by-step-guide",
    "how-to-use-glass-filter-tips-2025-guide",
    "how-to-use-glass-tips-for-blunts-the-ultimate-2025-guide",
    "how-to-use-herb-grinder-2025-guide-clean-consistent-quiet",
    "how-to-use-herb-grinder-with-teeth-the-ultimate-2026-guide",
    "how-to-use-pre-rolls-the-ultimate-guide-for-perfect-sessions-every-time",
    "important-notice-welcoming-the-year-of-the-dragon",
    "is-a-herb-overdose-possible",
    "is-it-safe-to-use-gum-wrappers-as-rolling-paper",
    "mid-autumn-festival-holidays-2020-yay",
    "mylar-bags",
    "pre-rolled-cones",
    "pre-rolled-cones-factory",
    "rolling-in-style-a-guide-to-the-best-rolling-trays-for-home-rollers",
    "rolling-paper-size",
    "rolling-papers-in-thailand",
    "smell-proof-mylar-bags",
    "super-sexy-roach-book-1-1",
    "thailand-dispensaries",
    "the-best-rolling-trays-reviewed-which-one-is-right-for-you",
    "the-difference-between-vaporizing-and-smoking-herb",
    "the-pros-and-cons-of-using-a-custom-rolling-tray",
    "the-secret-to-storing-herb-long-term-and-preserve-the-freshness",
    "the-ultimate-guide-to-marijuana-accessories-in-2026",
    "the-ultimate-guide-to-using-a-herb-grinder",
    "top-10-ways-to-use-herb",
    "what-all-do-you-need-to-make-a-rolling-tray-the-complete-2025-guide",
    "what-are-glass-tips-the-ultimate-2025-guide-you-need-to-read",
    "what-are-glass-tips-used-for-the-ultimate-2025-guide",
    "what-are-infused-pre-rolls-the-ultimate-guide-2025-to-enhanced-pre-rolls",
    "what-are-the-safest-alternatives-to-rolling-paper-2025-guide",
    "what-can-i-use-as-a-rolling-tray-25-smart-alternatives-pro-tips-a-10-diy-blueprint",
    "what-can-i-use-as-rolling-paper-15-safe-and-creative-alternatives-you-can-try",
    "what-do-glass-tips-do-for-joints-the-ultimate-2025-guide",
    "what-if-tsa-finds-weed-in-my-bag-the-real-deal-on-flying-with-your-stash",
    "what-is-a-rolling-tray-for-the-ultimate-guide-youve-been-waiting-for",
    "what-is-a-rolling-tray-used-for",
    "what-is-a-rolling-tray-your-ultimate-guide-to-rolling-trays-in-2025",
    "what-is-a-smell-proof-mylar-bag-and-how-do-you-get-one",
    "what-is-the-best-grinder-for-weed-your-ultimate-2025-guide",
    "what-is-the-best-weed-grinder-ultimate-2026-guide",
    "what-is-the-weed-at-the-bottom-of-a-grinder-called-your-chill-guide-to-that-golden-dust",
    "what-s-the-best-weed-grinder-in-2025-the-friendly-no-nonsense-guide",
    "what-to-use-as-a-rolling-tray-7-creative-household-alternatives-the-handy-options",
    "what-to-use-as-rolling-paper-when-you-re-out-of-papers-10-handy-alternatives",
    "what-type-of-rolling-tray-is-the-best-for-you",
    "when-was-the-weed-grinder-invented-1905-origin-modern-evolution",
    "when-will-pre-rolls-be-available-in-ohio-your-2025-guide-to-the-hottest-roll-up-trend",
    "where-can-i-buy-a-rolling-tray-your-complete-2026-shopping-guide",
    "where-to-buy-a-weed-grinder-your-ultimate-guide-for-2026",
    "where-to-buy-pre-rolls-near-me-your-ultimate-guide",
    "where-to-buy-pre-rolls-your-complete-2025-buying-guide",
    "where-to-buy-rolling-tray-near-me-your-ultimate-guide-to-finding-the-perfect-one",
    "where-to-buy-weed-grinder-2025-buyer-s-guide",
    "where-to-get-pre-rolls-in-2025-local-delivery-online",
    "who-invented-the-weed-grinder-the-untold-story-behind-your-favorite-tool",
    "why-use-a-rolling-tray-the-complete-guide",
    "www-rollyourownpapers-com"
]

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

def main():
    global HEADERS
    token = TOKEN
    if not token:
        if CLIENT_ID and CLIENT_SECRET:
            print("Exchanging Client ID + Secret for an access token...")
            try:
                token = fetch_token()
                print("Got access token.\n")
            except urllib.error.HTTPError as e:
                print(f"ERROR getting token: HTTP {e.code} - {e.read().decode()[:300]}")
                sys.exit(1)
        else:
            print("ERROR: Provide either SHOPIFY_TOKEN, or both")
            print("SHOPIFY_CLIENT_ID and SHOPIFY_CLIENT_SECRET.")
            sys.exit(1)

    HEADERS = {"X-Shopify-Access-Token": token, "Content-Type": "application/json"}

    print(f"Loaded {len(SLUGS)} posts to set to draft.")
    if DRY_RUN:
        print("DRY RUN - nothing will change.\n")

    bid = blog_id()
    print(f"Blog ID: {bid}\n")

    drafted = already = missing = errors = 0
    for i, slug in enumerate(SLUGS, 1):
        try:
            data = get(f"/blogs/{bid}/articles.json?handle={slug}&limit=1")
            arts = data.get("articles", [])
            if not arts:
                print(f"[{i}/{len(SLUGS)}] NOT FOUND: {slug}")
                missing += 1
                continue
            a = arts[0]
            if a.get("published_at") is None:
                print(f"[{i}/{len(SLUGS)}] ALREADY DRAFT: {a['title']}")
                already += 1
                continue
            if DRY_RUN:
                print(f"[{i}/{len(SLUGS)}] WOULD DRAFT: {a['title']}")
            else:
                put(f"/blogs/{bid}/articles/{a['id']}.json",
                    {"article": {"id": a["id"], "published": False}})
                print(f"[{i}/{len(SLUGS)}] SET TO DRAFT: {a['title']}")
                drafted += 1
                time.sleep(0.5)
        except urllib.error.HTTPError as e:
            print(f"[{i}/{len(SLUGS)}] HTTP {e.code}: {slug}")
            errors += 1
            time.sleep(2)
        except Exception as e:
            print(f"[{i}/{len(SLUGS)}] ERROR: {slug} - {e}")
            errors += 1

    print(f"\nDone. Drafted: {drafted} | Already draft: {already} | "
          f"Not found: {missing} | Errors: {errors}")

if __name__ == "__main__":
    main()
