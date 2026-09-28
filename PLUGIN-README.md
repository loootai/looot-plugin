# looot plugin

<!-- Generated file. Do not edit by hand; change the source and run the generator. -->

Find, price and run data APIs for SEO, enrichment, email verification and social from one account. Pay per call, no provider keys.

The plugin bundles the looot MCP server (https://api.looot.ai/mcp) and skills that teach an agent the whole flow: sign in, top up, search by job, run with fallback, read receipts, and fix errors. Sign-in is OAuth in the browser; no key is stored in these files.

## Install

Claude Code, from this folder or its repository:

```text
/plugin marketplace add <path or owner/repo>
/plugin install looot@looot
/mcp   (pick plugin:looot:looot, then Authenticate)
```

Codex:

```bash
codex plugin marketplace add <path or owner/repo>
codex plugin add looot@looot
codex mcp login looot
```

Cursor: copy `plugins/cursor/looot` into `~/.cursor/plugins/local` and reload the window; the Cursor Marketplace takes a public repository at cursor.com/marketplace/publish.

Tested by hand: the Claude Code and Codex installs (marketplace add, install, the server waiting for sign-in). Cursor follows its published format and is not tested yet.

## Skills

| Skill | Loads | What it does |
|---|---|---|
| `find-and-run` | automatic | Find and run paid data APIs through looot (SEO and SERP data, keyword volume, backlinks, people and company enrichment, email finding and verification, social profiles, web scraping). Use whenever a task needs external or live data. Search by the job in plain words, read the job's inputs and coverage, run the job with fallback, then read who answered and what it cost. |
| `setup` | automatic | Connect looot and get it ready for a first paid run. Use when the looot tools are missing or answer 401, when the user asks to sign in, set up or connect looot, or before the first paid run in a new workspace (check the balance, then get a top-up link). |
| `money` | automatic | How looot charges. Use before a paid run or a batch of runs, when the user asks what something will cost, sets a budget, runs out of credit, or wants receipts. Covers quotes, holds, what is refused for free, the fallback.maxCostUsd cap, top-ups and where receipts live. |
| `recipes` | automatic | Step lists for common looot jobs. Use to enrich a lead list (find and verify work emails), research a company from its domain, check SEO and GEO (AI answer) visibility for a keyword, turn a web page into markdown, or look up a LinkedIn, TikTok or Instagram profile. |
| `troubleshooting` | automatic | Fix a looot run or tool call that failed or came back empty. Use when a looot result carries needs_input, no_supply_for_job, no_runnable_provider, unknown_job, invalid_input, route_capped, route_no_fit, validation_error, insufficient_balance, idempotency_conflict, too_many_inflight_runs, forbidden, a 401, or outcome miss. |
| `find-email` | command only | Find and verify the work email of one person, or of every person in a list, through looot. Run it with a name and a company domain, a LinkedIn URL, or a file of leads. |
| `research-company` | command only | Write a short account brief on a company from its domain through looot, with its profile, tech stack, recent news and known contacts, each fact tied to the provider that returned it. |

In Claude Code every skill is also a slash command: `/looot:setup`, `/looot:find-email`, `/looot:research-company`.

## Layout

| Path | For |
|---|---|
| `.claude-plugin/marketplace.json`, `plugins/claude-code/` | Claude Code |
| `.agents/plugins/marketplace.json`, `plugins/codex/` | Codex and ChatGPT (Agent Plugins format) |
| `.cursor-plugin/marketplace.json`, `plugins/cursor/` | Cursor |

Website: https://looot.ai. Docs: https://looot.ai/docs. Privacy: https://looot.ai/privacy. Terms: https://looot.ai/terms.
