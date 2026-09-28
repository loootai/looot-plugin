---
name: setup
description: "Connect looot and get it ready for a first paid run. Use when the looot tools are missing or answer 401, when the user asks to sign in, set up or connect looot, or before the first paid run in a new workspace (check the balance, then get a top-up link)."
---

# Set up looot

looot is one MCP server at https://api.looot.ai/mcp. Sign-in is OAuth in the browser. Nobody copies a key.

## 1. Sign in

The plugin adds an MCP server named `looot`. `codex mcp list` shows it as "Not logged in" until the user signs in with `codex mcp login looot`. The browser opens looot.ai, the user signs in, picks the organization to bill and clicks Connect.

Never ask the user to paste a token into the chat, and never put one in a URL or a file you write. A header token (`Authorization: Bearer <agent token>`) is only for CI and headless agents. The user creates it at https://looot.ai/settings and sets it in the client's own config.

## 2. Check the connection

Call the free overview. It lists categories with endpoint counts:

```tool
catalog_overview
```

## 3. Check the balance

```tool
balance
```

Read `available` (USD you can spend), `reserved` (held by runs in flight) and `topUpLink.minimumUsd`. A new workspace starts at $0. There is no trial credit. Searching, inspecting and the overview are free; runs are paid.

## 4. Top up when the balance is short

```tool
top_up {"amountUsd": 5}
```

Leave `amountUsd` out to get the suggested amount. It is never below `topUpLink.minimumUsd` ($5 when this was written); a lower amount is refused with `top_up_amount_out_of_range`. The answer carries `checkoutUrl`, a Stripe page. Show it to the user as a link and wait. You never enter card details. When they say they paid, call `balance` again.

If `checkoutUrl` is null, the answer has a `reason` and a `dashboardUrl` where the user can top up by hand.

Amount the user asked for, if any: the details the user gave with the request

## 5. First run

Go to the find-and-run skill. A cheap first run is verifying one email address, or turning one web page into markdown.

More: https://looot.ai/docs. Agent docs: https://api.looot.ai/llms.txt.
