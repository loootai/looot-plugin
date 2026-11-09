<p align="center"><img src="assets/hero.png" alt="looot-plugin: looot for Claude Code, Codex and Cursor" width="100%"></p>

# looot plugin

[![License](https://img.shields.io/github/license/loootai/looot-plugin)](LICENSE) [![Docs](https://img.shields.io/badge/docs-docs.looot.ai-12A06A)](https://docs.looot.ai)

The looot plugin for Claude Code, Codex and Cursor: the looot MCP server (`https://api.looot.ai/mcp`,
browser sign-in, no key in any file) plus one skill, so your agent can find emails, enrich companies,
pull Google results and more from 4,200+ data API operations across 300+ providers on one prepaid
balance.

## Quickstart (Claude Code)

1. Add the marketplace: `/plugin marketplace add loootai/looot-plugin`
2. Install the plugin: `/plugin install looot@looot`
3. Run `/mcp`, pick `plugin:looot:looot` and choose Authenticate. Then ask for a job in plain
   words, as in the example below. The skill also runs as `/looot:looot`.

Codex and Cursor install steps, the skill and the commands are in [PLUGIN-README.md](PLUGIN-README.md).
Replit users can add the looot MCP server alone (browser sign-in, no token): [![Add to Replit](https://replit.com/badge?caption=Add%20to%20Replit)](https://replit.com/integrations?mcp=eyJkaXNwbGF5TmFtZSI6Imxvb290IiwiYmFzZVVybCI6Imh0dHBzOi8vYXBpLmxvb290LmFpL21jcCJ9)

## Example

Ask your agent:

```text
Use looot to find the work email of Patrick Collison at stripe.com
```

It calls `search` first, which is free. This is the real answer from 2026-11-09, trimmed:

```text
job people.email.find, 29 endpoints
kittai-find-email           Kitt AI        $0.005 per call   works 54% of 12,023 runs, median 4.0 s
companyenrich-people-email  CompanyEnrich  $0.098 per call   no runs yet
fundable-person-email       Fundable       $0.25 per call    no runs yet
```

Then it runs `job:people.email.find` with fallback. looot tries the next provider on a miss and the
result carries the email and the price charged.

## Free to try

Search and inspect are free and need no balance. Paid runs are billed per call at the price
`inspect` shows first, and a failed call costs nothing. A new workspace starts at $0; top up from $5
when you want the first paid result.

## Where it's listed

[![ClawHub](https://img.shields.io/badge/ClawHub-walidboulanouar%2Flooot-12A06A)](https://clawhub.ai/walidboulanouar/looot)
[![skills.sh](https://img.shields.io/badge/skills.sh-loootai%2Flooot--skills-12A06A)](https://skills.sh/loootai/looot-skills)
[![npm pi-looot](https://img.shields.io/npm/v/pi-looot?label=npm%20pi-looot)](https://www.npmjs.com/package/pi-looot)
[![MCP Registry](https://img.shields.io/badge/MCP_Registry-ai.looot%2Flooot-12A06A)](https://registry.modelcontextprotocol.io/v0/servers?search=ai.looot/looot)
[![Glama](https://img.shields.io/badge/Glama-looot-12A06A)](https://glama.ai/mcp/connectors/ai.looot/looot)
[![LobeHub](https://img.shields.io/badge/LobeHub-looot-12A06A)](https://lobehub.com/mcp/loootai-looot-mcp)
[![Appside](https://img.shields.io/badge/Appside-looot-12A06A)](https://mcp.appside.build/mcp-servers/looot/)
[![Dify](https://img.shields.io/badge/Dify_Marketplace-looot-12A06A)](https://marketplace.dify.ai/plugins/looot/looot)
[![VS Code Marketplace](https://img.shields.io/badge/VS_Code_Marketplace-looot.looot-007ACC)](https://marketplace.visualstudio.com/items?itemName=looot.looot)

Also on [cursor.directory](https://cursor.directory/plugins/looot).

See also: [awesome-looot-use-cases](https://github.com/loootai/awesome-looot-use-cases) (copy-paste recipes) and [awesome-gtm](https://github.com/loootai/awesome-gtm) (open-source GTM tools).

MIT licensed. The hosted looot service it connects to has its own terms: https://looot.ai/terms

## Layout

| Path | What |
|---|---|
| `.claude-plugin/marketplace.json` | Claude Code marketplace (one plugin: `looot`) |
| `.agents/plugins/marketplace.json` | Codex marketplace |
| `.cursor-plugin/marketplace.json` | Cursor marketplace |
| `plugins/claude-code/looot/` | Claude Code plugin: `.mcp.json` and the `looot` skill |
| `plugins/codex/looot/` | Codex plugin |
| `plugins/cursor/looot/` | Cursor plugin |

These files are generated. Change them at the source and run `scripts/sync-from-monorepo.sh`, never by hand.

## Status

Installs tested by hand in Claude Code and Codex (up to "waiting for sign-in"). Cursor follows its
published format and is not tested yet.
