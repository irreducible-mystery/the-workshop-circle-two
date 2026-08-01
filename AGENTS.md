# AGENTS.md

This file gives automation agents a safe operating guide for this repository.

## Read first

1. `/home/runner/work/the-workshop-circle-two/the-workshop-circle-two/INHERITANCE.md`
2. `/home/runner/work/the-workshop-circle-two/the-workshop-circle-two/README.md`
3. `/home/runner/work/the-workshop-circle-two/the-workshop-circle-two/NORMS.md`

## Repository facts

- This repository carries Circle Two and Circle Three records.
- Main mathematical artifact: `lean/Zi.lean`.
- Main verification chain: `audit/c2_gates.sh`.
- `VIEWS.md` is rendered by `audit/c2_views.sh`; do not hand-edit it.

## Editing rules

- Make minimal, targeted changes only.
- Keep corrections explicit and localized; do not silently rewrite history.
- Treat `CHARTER.md` as a couriered primary source (byte-verbatim); record corrections in separate documents when needed.
- Do not introduce new dependencies or tooling unless explicitly required.

## Verification commands

Run from repository root unless noted:

1. Floor benches:
   - `cd floor && python3 run_all.py`
2. Certificate (requires paths):
   - `C2_WORKSHOP=/home/runner/work/the-workshop-circle-two/the-workshop-circle-two/floor C1_LEAN=/absolute/path/to/circle-one-clone python3 audit/c2_gift_certificates.py`
3. Gate chain:
   - `LEAN=/absolute/path/to/lean sh audit/c2_gates.sh`
4. Lean artifact:
   - `lean lean/Zi.lean`

If `C1_LEAN` is unavailable, the certificate’s Circle-One calibrator checks will fail by name; treat that as expected environment limitation, not a silent pass.

## Commit hygiene

- Do not commit generated caches or build artifacts.
- Before committing, ensure only intended files changed.
- Keep commit messages specific to the change made.
