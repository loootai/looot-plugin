"""Checks the plugin layout: every marketplace entry points at a plugin folder with a manifest and skills."""
import json, pathlib, sys

root = pathlib.Path(__file__).resolve().parent.parent
errors = []
market = json.loads((root / ".claude-plugin/marketplace.json").read_text())
for p in market["plugins"]:
    folder = root / p["source"]
    if not (folder / ".claude-plugin/plugin.json").exists():
        errors.append(f"missing plugin.json in {folder}")
    mcp = json.loads((folder / ".mcp.json").read_text())
    text = json.dumps(mcp)
    if "https://api.looot.ai/mcp" not in text: errors.append(".mcp.json does not point at the looot MCP")
    if "Authorization" in text or "Bearer" in text: errors.append(".mcp.json must not carry a token")
    if len(list((folder / "skills").glob("*/SKILL.md"))) < 5: errors.append("expected at least 5 skills")
for f in root.rglob("*.json"):
    if ".git" in f.parts: continue
    if "@" in f.read_text() and "email" in f.read_text(): errors.append(f"email field left in {f}")
print("\n".join(errors) or "plugin layout ok")
sys.exit(1 if errors else 0)
