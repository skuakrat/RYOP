#!/usr/bin/env python3
"""
RYOP - Remove emoji from PRODUCT titles via Shopify Admin API.

Only the title text is changed. The product's handle/URL stays the same,
so there is no SEO/redirect impact. Variant names that include the product
title update automatically in Shopify.

Examples of what gets cleaned:
    "Custom Pink Rolling Paper 💖"        -> "Custom Pink Rolling Paper"
    "Custom Black Rolling Papers 🖤"      -> "Custom Black Rolling Papers"
    "Custom Rolling Paper BUSINESS CARDS 🤗" -> "Custom Rolling Paper BUSINESS CARDS"

HOW TO RUN (Windows PowerShell):
    # get a fresh token first if needed (tokens expire after ~24h):
    python get_token.py
    $env:SHOPIFY_TOKEN = "shpat_xxx"

    python clean_product_titles.py --dry-run   # preview changes
    python clean_product_titles.py             # apply changes
"""
import os, re, sys, time, json, urllib.request, urllib.error

STORE   = "customrollingpaper.myshopify.com"
DRY_RUN = "--dry-run" in sys.argv
API     = "2024-01"
BASE    = f"https://{STORE}/admin/api/{API}"
TOKEN   = os.environ.get("SHOPIFY_TOKEN", "")
HEADERS = {}

# Broad emoji / pictograph / symbol ranges, plus variation selectors and ZWJ.
EMOJI = re.compile(
    "["
    "\U0001F000-\U0001FAFF"  # most emoji & pictographs
    "\U00002600-\U000026FF"  # misc symbols
    "\U00002700-\U000027BF"  # dingbats
    "\U00002B00-\U00002BFF"  # arrows/stars
    "\U00002190-\U000021FF"  # arrows
    "\U0001F1E6-\U0001F1FF"  # regional indicators (flags)
    "\U0000FE00-\U0000FE0F"  # variation selectors
    "\U0000200D"             # zero-width joiner
    "\U00002B50\U00002B55"   # star, circle
    "\U0000203C\U00002049"   # !! ?!
    "\U00002122\U00002139"   # tm, info
    "\U000024C2"
    "]+",
    flags=re.UNICODE,
)

def clean(title):
    t = EMOJI.sub("", title)
    t = re.sub(r"\s{2,}", " ", t)            # collapse double spaces left behind
    t = re.sub(r"\s+([:?!.,])", r"\1", t)    # fix space before punctuation
    return t.strip(" -–—|").strip()

def get(path):
    req = urllib.request.Request(f"{BASE}{path}", headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def put(path, payload):
    body = json.dumps(payload).encode()
    req = urllib.request.Request(f"{BASE}{path}", data=body, method="PUT", headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return r.status

def all_products():
    """Paginate through every product in the store (any status)."""
    products = []
    since_id = 0
    while True:
        data = get(f"/products.json?limit=250&since_id={since_id}&fields=id,title,handle")
        batch = data.get("products", [])
        if not batch:
            break
        products.extend(batch)
        since_id = batch[-1]["id"]
        if len(batch) < 250:
            break
        time.sleep(0.3)
    return products

def main():
    global HEADERS
    if not TOKEN:
        print("ERROR: Set SHOPIFY_TOKEN first (run get_token.py).")
        sys.exit(1)
    HEADERS = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}

    products = all_products()
    print(f"Scanned {len(products)} products.\n")
    if DRY_RUN:
        print("DRY RUN - nothing will change.\n")

    changed = errors = 0
    for p in products:
        old = p["title"]
        new = clean(old)
        if new == old:
            continue
        if not new:                      # safety: never blank a title
            print(f"SKIP (would be empty): {old!r}")
            continue
        try:
            if DRY_RUN:
                print(f"WOULD CHANGE:\n  {old!r}\n  -> {new!r}\n")
                changed += 1
            else:
                put(f"/products/{p['id']}.json",
                    {"product": {"id": p["id"], "title": new}})
                print(f"UPDATED:\n  {old!r}\n  -> {new!r}\n")
                changed += 1
                time.sleep(0.5)
        except urllib.error.HTTPError as e:
            print(f"HTTP {e.code} on: {old!r}")
            errors += 1
            time.sleep(2)

    verb = "Would change" if DRY_RUN else "Changed"
    print(f"Done. {verb}: {changed} | Errors: {errors}")

if __name__ == "__main__":
    main()
