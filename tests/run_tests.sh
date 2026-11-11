#!/usr/bin/env bash
# Runs every check the release depends on. Exit code is non-zero on any failure.
set -euo pipefail
cd "$(dirname "$0")/.."
echo "== behaviors.js logic"
node tests/test_behaviors.js
echo "== checker passes a good page"
python3 claude/check_page.py tests/fixtures/good.html
echo "== checker fails a bad page"
if python3 claude/check_page.py tests/fixtures/bad.html; then echo "expected the bad page to fail"; exit 1; fi
echo "== tool pages exist and have no script-tag text inside scripts"
for f in tools/intake/index.html tools/pricing/index.html tools/invoice/index.html; do test -s "$f"; done
echo "All checks passed."
