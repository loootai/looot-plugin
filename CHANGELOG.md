# Changelog

## 0.2.0 (2026-10-07)

- First public release under the MIT license.
- Install from `loootai/looot-plugin`.

## 0.1.0

- Plugin shell: `plugin.json`, `marketplace.json`, `.mcp.json` pointing at the hosted MCP
  server with OAuth.
- The generated plugin for Claude Code, Codex and Cursor: 7 skills, the looot MCP with browser sign-in.
- `scripts/sync-from-monorepo.sh` copies the generated plugin, drops owner emails, and leak-scans.
- `tests/validate_plugin.py` checks the manifests and the MCP endpoint's 401.
