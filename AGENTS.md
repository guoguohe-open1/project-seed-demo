# Instructions for AI Coding Agents

## Purpose
This repository maintains reusable project-seed templates and the bootstrap script. Do not treat it as an application project.

## Before editing
- Read `README.md` and `docs/SEED_DESIGN.md`.
- Inspect the relevant template and `scripts/bootstrap.py` together.
- If changing generated output, add or update a test in `tests/`.

## Change boundaries
- Keep the seed minimal. Add a file only when it has a distinct owner and repeated practical value.
- Do not duplicate the same rule across `AGENTS.md`, `README.md`, and every template. Link to the canonical owner instead.
- Keep `AGENTS.md` focused on durable instructions, not the full project manual.
- Never silently overwrite non-empty target directories in the bootstrap script.
- Do not add third-party dependencies without a concrete need.
- Do not claim tests passed unless you ran them and observed the result.

## Verification
For changes to `scripts/bootstrap.py` or `templates/`, run:

```bash
python -m unittest discover -s tests -v
python scripts/bootstrap.py --help
```

Review generated output for placeholder replacement, file layout, and accidental overwrite behavior.

## Completion report
Summarize changed files, verification actually performed, and known limitations. Stop after the requested change; do not start unrelated cleanup.
