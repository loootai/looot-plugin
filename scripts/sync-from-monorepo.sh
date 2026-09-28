#!/usr/bin/env bash
# Copy the generated plugin into this repo, drop owner/author emails, then leak-scan.
# Usage: scripts/sync-from-monorepo.sh <path to the generated plugin folder>
set -euo pipefail
SRC="${1:?path to the generated plugin folder}"
cd "$(dirname "$0")/.."
rm -rf .claude-plugin .agents .cursor-plugin plugins
cp -R "$SRC/.claude-plugin" "$SRC/.agents" "$SRC/.cursor-plugin" "$SRC/plugins" .
cp "$SRC/README.md" PLUGIN-README.md
python3 - <<'PY'
import json, glob
for f in glob.glob('**/*.json', recursive=True):
    if '/.git/' in f: continue
    try: d = json.load(open(f))
    except Exception: continue
    def strip(o):
        if isinstance(o, dict):
            o.pop('email', None); [strip(v) for v in o.values()]
        elif isinstance(o, list):
            [strip(v) for v in o]
    strip(d); json.dump(d, open(f, 'w'), indent=2); open(f, 'a').write('\n')
PY
bash scripts/leak-scan.sh .
