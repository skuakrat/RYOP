#!/usr/bin/env python3
"""
Delete 173 REMOVE blog posts via Shopify Admin API.

Usage:
    export SHOPIFY_STORE=rollyourownpapers.myshopify.com
    export SHOPIFY_TOKEN=shpat_xxxxxxxxxxxxxxxxxxxx
    python3 scripts/delete-blog-posts.py [--dry-run]

The script reads slugs from audits/shopify-redirects-remove-240.csv,
finds each post by handle via the API, and deletes it.
"""
import csv
import os
import sys
import time
import urllib.request
import urllib.error
import json

STORE   = os.environ.get("SHOPIFY_STORE", "")
TOKEN   = os.environ.get("SHOPIFY_TOKEN", "")
DRY_RUN = "--dry-run" in sys.argv

API_VERSION = "2024-01"
BASE = f"https://{STORE}/admin/api/{API_VERSION}"
HEADERS = {
    "X-Shopify-Access-Token": TOKEN,
    "Content-Type": "application/json",
}

def shopify_get(path):
    req = urllib.request.Request(f"{BASE}{path}", headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def shopify_delete(path):
    req = urllib.request.Request(f"{BASE}{path}", method="DELETE", headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return r.status

def load_slugs():
    slugs = set()
    with open("audits/shopify-redirects-remove-240.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            url = row["Redirect from"]
            slug = url.split("/")[-1].split("?")[0]
            if not slug.endswith(".atom"):
                slugs.add(slug)
    return sorted(slugs)

def get_blog_id():
    data = shopify_get("/blogs.json")
    for blog in data["blogs"]:
        if "roll-your-own" in blog["handle"] or "the-roll" in blog["handle"]:
            return blog["id"]
    # fall back to first blog
    return data["blogs"][0]["id"]

def main():
    if not STORE or not TOKEN:
        print("ERROR: Set SHOPIFY_STORE and SHOPIFY_TOKEN environment variables.")
        sys.exit(1)

    slugs = load_slugs()
    print(f"Loaded {len(slugs)} slugs to delete.")
    if DRY_RUN:
        print("DRY RUN — no deletions will be made.\n")

    blog_id = get_blog_id()
    print(f"Blog ID: {blog_id}\n")

    deleted = 0
    not_found = 0
    errors = 0

    for i, slug in enumerate(slugs, 1):
        try:
            data = shopify_get(f"/blogs/{blog_id}/articles.json?handle={slug}&limit=1")
            articles = data.get("articles", [])
            if not articles:
                print(f"[{i}/{len(slugs)}] NOT FOUND: {slug}")
                not_found += 1
                continue

            article = articles[0]
            article_id = article["id"]
            title = article["title"]

            if DRY_RUN:
                print(f"[{i}/{len(slugs)}] WOULD DELETE: {title}")
            else:
                shopify_delete(f"/blogs/{blog_id}/articles/{article_id}.json")
                print(f"[{i}/{len(slugs)}] DELETED: {title}")
                deleted += 1
                time.sleep(0.5)  # stay within 2 req/sec rate limit

        except urllib.error.HTTPError as e:
            print(f"[{i}/{len(slugs)}] HTTP ERROR {e.code}: {slug}")
            errors += 1
            time.sleep(2)
        except Exception as e:
            print(f"[{i}/{len(slugs)}] ERROR: {slug} — {e}")
            errors += 1

    print(f"\nDone. Deleted: {deleted} | Not found: {not_found} | Errors: {errors}")

if __name__ == "__main__":
    main()
