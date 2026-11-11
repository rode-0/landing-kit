#!/usr/bin/env bash
# Runs every check the release depends on. Exit code is non-zero on any failure.
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1
cd "$(dirname "$0")/.."
echo "== behaviors.js logic"
node tests/test_behaviors.js
echo "== paste bundle is current and loads"
node -e "require('fs'); new Function(require('fs').readFileSync('claude/library/behaviors-paste.js','utf8')+'; if(typeof lpkStatus!==\'function\')throw new Error(\'missing lpkStatus\')')()"
grep -q "lpkNextClass" claude/library/behaviors-paste.js
echo "== checker passes a good page"
python3 claude/check_page.py tests/fixtures/good.html
echo "== checker fails a bad page"
if python3 claude/check_page.py tests/fixtures/bad.html; then echo "expected the bad page to fail"; exit 1; fi
echo "== checker catches each planted layout fault"
out=$(python3 claude/check_page.py tests/fixtures/bad-layout.html || true)
for want in "no element has id" "scroll sideways" "same color" "JavaScript error"; do echo "$out" | grep -q "$want" || { echo "checker missed: $want"; exit 1; }; done
echo "== tool pages, demos and paste bundle"
for f in tools/index.html tools/setup/index.html tools/intake/index.html tools/pricing/index.html tools/invoice/index.html; do test -s "$f"; done
python3 tests/test_kit.py
echo "== tracker matches what Claude pastes"
python3 tests/test_tracker.py
echo "== posting queue safety"
python3 extras/scheduler/test_post_queue.py
echo "All checks passed."
