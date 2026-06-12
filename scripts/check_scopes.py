#!/usr/bin/env python3
"""
RYOP - Show which Admin API scopes the current SHOPIFY_TOKEN actually has.

HOW TO RUN (Windows PowerShell):
    $env:SHOPIFY_TOKEN = "shpat_xxx"
    python check_scopes.py

If 'read_products' is missing from the output, the app's scope change
was not saved (or the token was generated before saving). Fix the scopes
in Shopify Admin, then run get_token.py again for a fresh token.
"""
import os, sys, json, urllib.request, urllib.error

STORE = "customrollingpaper.myshopify.com"
TOKEN = os.environ.get("SHOPIFY_TOKEN", "")

if not TOKEN:
    print("ERROR: Set SHOPIFY_TOKEN first (run get_token.py).")
    sys.exit(1)

req = urllib.request.Request(
    f"https://{STORE}/admin/oauth/access_scopes.json",
    headers={"X-Shopify-Access-Token": TOKEN},
)
try:
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
except urllib.error.HTTPError as e:
    print(f"HTTP {e.code} — the token itself is being rejected.")
    print("A 401/403 here means the token is expired or invalid: run get_token.py again.")
    sys.exit(1)

scopes = sorted(s["handle"] for s in data.get("access_scopes", []))
print("Token is valid. Granted scopes:")
for s in scopes:
    print(f"  - {s}")

needed = {"read_products", "write_products"}
missing = needed - set(scopes)
if missing:
    print(f"\nMISSING for product cleanup: {', '.join(sorted(missing))}")
    print("Fix: Shopify Admin > Settings > Apps and sales channels > Develop apps")
    print("     > your app > Configuration > Admin API integration > Edit")
    print("     > tick read_products + write_products > SAVE")
    print("     then: python get_token.py  (and set the new token)")
else:
    print("\nAll product scopes present — clean_product_titles.py should work.")
