# Maintaining the kit

Technical notes for whoever maintains this repo. Users don't need this file.

## Layout
- `plugin/skills/landing-kit/SKILL.md`: the instructions Claude follows. The repo is a plugin marketplace (`.claude-plugin/marketplace.json`) with one plugin in `plugin/`; users add `rode-0/landing-kit` in Claude (Customize > Plugins).
- `plugin/skills/landing-kit/scripts/`: `check_page.py` (page checks), `behaviors.js` + generated `behaviors-paste.js`, `photo_tools.py`, `make_preview.py` (must match `tools/preview/preview.js`; tested).
- `plugin/skills/landing-kit/references/`: the business guide, templates, playbooks and design directions. `plugin/skills/landing-kit/assets/tracker.xlsx` is the only tracker copy; releases copy it to the tools site and the ZIP.
- `tools/`: standalone HTML tools (no build step) and the tracker spreadsheet.
- `tests/`: `run_tests.sh` runs everything; `test_behaviors.js` tests the library logic; `fixtures/` holds a page the checker must pass and one it must fail.
- `eval/`: the time study (dataset, method, results).

## Branches and releases
- Work happens on `dev`. Every push runs the **Checks** workflow (`tests/run_tests.sh`).
- `main` is what users get. Only the **Release** workflow moves it.
- To release: GitHub, then **Actions**, then **Release**, then **Run workflow**. Enter a version (like 1.1.0) and
  optional notes. Leave **Dry run** ticked to test it first; untick it to publish. It runs the checks, moves `main`
  up to `dev`, tags `vX.Y.Z`, and publishes a GitHub Release with a ZIP of the user-facing files.
- Run all checks locally with `./tests/run_tests.sh`.

## Before changing PROMPT.md or the library
1. Run `node tests/test_behaviors.js`.
2. Run the checker on a known-good page.
3. Re-run at least part of the time study (`eval/README.md`) and compare quality and time against the last results.

## Conventions
- User-facing text is plain language. No technical terms in `README.md` or the guide and templates under `references/`.
- Pages must work as a single `index.html` with no build step.
- `behaviors.js` comments must never contain a literal script tag; the checker fails pages that paste one.
