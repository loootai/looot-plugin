---
name: looot-plugin
description: Maintain looot-plugin, the Claude Code plugin shell that bundles the hosted looot MCP server and the looot skill. Use when syncing the generated plugin into this repo, changing a manifest, or preparing a plugin release.
---

# looot-plugin

## What this repo is

The public home of the Claude Code plugin. The plugin files are generated elsewhere and copied
in; this repo holds the manifests, `.mcp.json` (remote MCP over HTTP with OAuth), the skill and
a validation test. The plugins live under `plugins/claude-code|codex|cursor/looot/`, with a marketplace file per client at the root.

## Build and test

```bash
python3 tests/validate_plugin.py
bash scripts/leak-scan.sh .
git config core.hooksPath .githooks
claude plugin marketplace add ./ && claude plugin install looot@looot   # local try-out
```

## Syncing

`scripts/sync-from-monorepo.sh <generated folder>` refreshes the plugin from its source:
it replaces `.claude-plugin/`, `.agents/`, `.cursor-plugin/` and `plugins/`, drops owner emails and
runs the scanner. Then run `python3 tests/validate_plugin.py` and `claude plugin validate .`, and have a
human read the diff before committing. Never copy anything else from the source.

## Release later (only after the owner says yes)

1. Bump `version` at the source (it flows to every `plugin.json` and `marketplace.json`) and sync.
2. Update `CHANGELOG.md`, tag `vX.Y.Z`, then submit to the plugin directory if wanted.

## Public looot surface this repo may use

`https://api.looot.ai/mcp`, `/skill.md`, `/llms.txt`, `/llms-full.txt`, `https://looot.ai/docs`.

## Never

- Bake a token or header into `.mcp.json`. The plugin signs in with OAuth.
- Copy source, prompts or internal docs from the private monorepo beyond the generated plugin files.
- Commit a secret, `.env` file, internal host, local path, customer or workspace id, or personal email.
- Name private repos or branches in anything public. The README status note must go before release.
