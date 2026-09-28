# looot plugin

The looot plugin for Claude Code, Codex and Cursor: the looot MCP server (https://api.looot.ai/mcp,
browser sign-in, no key in any file) plus skills that take an agent from sign-in to a paid result.

Proprietary, all rights reserved. Not open source. This repository is private.

## Install (Claude Code)

```text
/plugin marketplace add walidboulanouar/looot-plugin
/plugin install looot@looot
/mcp   (pick plugin:looot:looot, then Authenticate)
```

Then run `/looot:setup`, and try `/looot:find-email Patrick Collison stripe.com` or
`/looot:research-company stripe.com`.

Codex and Cursor install steps, the skill list and the commands are in [PLUGIN-README.md](PLUGIN-README.md).

## Layout

| Path | What |
|---|---|
| `.claude-plugin/marketplace.json` | Claude Code marketplace (one plugin: `looot`) |
| `.agents/plugins/marketplace.json` | Codex marketplace |
| `.cursor-plugin/marketplace.json` | Cursor marketplace |
| `plugins/claude-code/looot/` | Claude Code plugin: `.mcp.json` and 7 skills |
| `plugins/codex/looot/` | Codex plugin |
| `plugins/cursor/looot/` | Cursor plugin |

These files are generated. Change them at the source and run `scripts/sync-from-monorepo.sh`, never by hand.

## Status

Installs tested by hand in Claude Code and Codex (up to "waiting for sign-in"). Cursor follows its
published format and is not tested yet.
