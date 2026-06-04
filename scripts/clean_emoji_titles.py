#!/usr/bin/env python3
"""
RYOP - Remove emoji from PUBLISHED blog post titles via Shopify Admin API.

Only the title text is changed. The post's handle/URL stays the same,
so there is no SEO/redirect impact. Drafted (hidden) posts are skipped.

HOW TO RUN (Windows PowerShell):
    # get a fresh token first if needed:
    python get_token.py
    $env:SHOPIFY_TOKEN = "shpat_xxx"

    python clean_emoji_titles.py --dry-run   # preview changes
    python clean_emoji_titles.py             # apply changes
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
    "\U0000FE0F"
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

def blog_id():
    data = get("/blogs.json")
    for b in data["blogs"]:
        if "roll-your-own" in b["handle"] or "the-roll" in b["handle"]:
            return b["id"]
    return data["blogs"][0]["id"]

def all_published_articles(bid):
    """Paginate through every published article in the blog."""
    articles = []
    since_id = 0
    while True:
        data = get(f"/blogs/{bid}/articles.json?limit=250&since_id={since_id}&published_status=published")
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
        print("ERROR: Set SHOPIFY_TOKEN first (run get_token.py).")
        sys.exit(1)
    HEADERS = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}

    bid = blog_id()
    print(f"Blog ID: {bid}")
    articles = all_published_articles(bid)
    print(f"Scanned {len(articles)} published posts.\n")
    if DRY_RUN:
        print("DRY RUN - nothing will change.\n")

    changed = errors = 0
    for a in articles:
        old = a["title"]
        new = clean(old)
        if new == old:
            continue
        if not new:                      # safety: never blank a title
            print(f"SKIP (would be empty): {old!r}")
            continue
        try:
            if DRY_RUN:
                print(f"WOULD CHANGE:\n  {old!r}\n  -> {new!r}\n")
            else:
                put(f"/blogs/{bid}/articles/{a['id']}.json",
                    {"article": {"id": a["id"], "title": new}})
                print(f"UPDATED:\n  {old!r}\n  -> {new!r}\n")
                changed += 1
                time.sleep(0.5)
        except urllib.error.HTTPError as e:
            print(f"HTTP {e.code} on: {old!r}")
            errors += 1
            time.sleep(2)

    verb = "Would change" if DRY_RUN else "Changed"
    print(f"Done. {verb}: {changed if not DRY_RUN else 'see above'} | Errors: {errors}")

if __name__ == "__main__":
    main()
