# Maintaining the kit

Technical notes for whoever maintains this repo. Users don't need this file.

## Layout
- `claude/PROMPT.md`: the instructions Claude follows. Users drag `claude/` into a Claude Project.
- `claude/check_page.py`: static checks Claude runs on each page (`python3 check_page.py index.html`).
- `claude/library/`: `behaviors.js` (tested behavior code), `playbooks.md` (trade notes), `directions.md` (design directions).
- `tools/`: standalone HTML tools (no build step) and the tracker spreadsheet.
- `tests/test_behaviors.js`: logic tests for `behaviors.js`. Run `node tests/test_behaviors.js`.
- `eval/`: the time study (dataset, method, results).

## Before changing PROMPT.md or the library
1. Run `node tests/test_behaviors.js`.
2. Run the checker on a known-good page.
3. Re-run at least part of the time study (`eval/README.md`) and compare quality and time against the last results.

## Conventions
- User-facing text is plain language. No technical terms in `README.md`, `sop/` or `templates/`.
- Pages must work as a single `index.html` with no build step.
- `behaviors.js` comments must never contain a literal script tag; the checker fails pages that paste one.
