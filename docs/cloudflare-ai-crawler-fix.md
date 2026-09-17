# Cloudflare task: allow AI crawlers (fix 403)

**Domain:** rollyourownpapers.com
**Problem:** Cloudflare is returning HTTP 403 to AI search crawlers (GPTBot,
ClaudeBot, PerplexityBot, Google-Extended, etc.). This blocks the site from
being indexed and cited by AI search engines (ChatGPT, Claude, Perplexity,
Google AI Overviews). We *want* these crawlers allowed.

The site's robots.txt already explicitly allows these bots — but Cloudflare's
firewall blocks them before they ever read robots.txt. This needs a Cloudflare
change.

---

## Step 1 — Turn OFF Bot Fight Mode (most likely cause)

This is the #1 cause of AI crawler 403s, especially on the Free plan.

1. Cloudflare dashboard → select **rollyourownpapers.com**
2. Left sidebar: **Security → Bots** (older dashboards: **Security → Settings**)
3. If **Bot Fight Mode** is ON, turn it **OFF**
   - (If on Pro/Business with **Super Bot Fight Mode**: under "Verified bots"
     set the action to **Allow**, and do NOT block "Definitely automated"
     traffic that matches verified crawlers.)

For most sites, turning off Bot Fight Mode resolves the 403 immediately.

---

## Step 2 — Add an explicit allow rule (belt and suspenders)

Works on all plans, including Free.

1. Left sidebar: **Security → WAF → Custom rules**
2. Click **Create rule**
3. Rule name: `Allow AI crawlers`
4. Build the expression — set Field = **User Agent**, Operator = **contains**,
   and OR these values together:
   - GPTBot
   - ChatGPT-User
   - ClaudeBot
   - anthropic-ai
   - Google-Extended
   - PerplexityBot
   - Amazonbot
   - meta-externalagent
   - YouBot

   Or paste this directly using the **Edit expression** option:

   ```
   (http.user_agent contains "GPTBot") or
   (http.user_agent contains "ChatGPT-User") or
   (http.user_agent contains "ClaudeBot") or
   (http.user_agent contains "anthropic-ai") or
   (http.user_agent contains "Google-Extended") or
   (http.user_agent contains "PerplexityBot") or
   (http.user_agent contains "Amazonbot") or
   (http.user_agent contains "meta-externalagent") or
   (http.user_agent contains "YouBot")
   ```

5. **Action: Skip** → check **All remaining custom rules**, and under
   "More components to skip" also tick **Super Bot Fight Mode** if shown.
6. Deploy.

---

## Step 3 — Verify

From any terminal:

```
curl -A "GPTBot" -I https://www.rollyourownpapers.com/
curl -A "ClaudeBot" -I https://www.rollyourownpapers.com/
```

Both should return `HTTP/2 200`, NOT `403`.
