#!/bin/sh
# ---------------------------------------------------------------------------
# THE WORKSHOP -> SYSTEM RECORD.  system/audit/s_append_only.sh
# The append-only gate for the system record's constitution.
#
# ADJUDICATOR DECLARATION (norm 15's discipline, inherited):
#   WHAT THIS CHECKS: no committed line of SYSTEM-REGISTER.md or
#     SYSTEM-NORMS.md is ever modified or deleted.  The register and the
#     norms grow by appending; a correction is a NEW row or entry pointing
#     at the old one — the circles' own law, mechanized at the one surface
#     whose single live write path could otherwise rewrite bought law
#     silently between crossings.
#     Method: diff HEAD's copy of each guarded file against the working
#     copy; any deletion hunk (a line present at HEAD and absent now) is
#     a violation.  Pure additions produce no deletion hunks and pass.
#   WHAT IT DOES NOT CHECK:
#     - the TRUTH of any row or norm — appending a false row passes; the
#       adjudicator for content is the non-author seat, per the register's
#       own header;
#     - files other than the two named — the crossing artifacts are
#       byte-exact ferried material guarded by their pins, not by this;
#     - history rewrites (rebase, force-push) — a hook lives in the
#       working copy; the honest gap of REGISTER row 5 applies here whole.
#   STATUS AT FOUNDING: QUARANTINED under norm 16 — written at the
#     founding, bitten on a planted modification and passed on a clean
#     tree (both transcripts in the founding letter), with each plant's
#     landing SHOWN by pin-before-and-after per the plant-application
#     row.  NOT yet wired into any hook: the circle's pre-commit chain is
#     an instrument of record, and instruments of record change only on
#     both seats' words.  Wiring is proposed in the founding letter and
#     awaits the system builder's word.
#
# USAGE:  sh system/audit/s_append_only.sh        (from the repo root)
# EXIT:   0 = append-only holds;  1 = a guarded line changed;  2 = cannot run
# ---------------------------------------------------------------------------

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || {
    echo "s_append_only: not a git repository" >&2; exit 2; }
cd "$ROOT" || exit 2

fail=0
for f in system/SYSTEM-REGISTER.md system/SYSTEM-NORMS.md; do
    # A file not yet at HEAD is being born: nothing to preserve, pass.
    if ! git cat-file -e "HEAD:$f" 2>/dev/null; then
        printf '  %-32s BORN THIS COMMIT (nothing to preserve)\n' "$f"
        continue
    fi
    # Deletion hunks = lines present at HEAD and gone from the working copy.
    deletions=$(git diff HEAD -- "$f" | grep -c '^-[^-]')
    if [ "$deletions" -eq 0 ]; then
        printf '  %-32s APPEND-ONLY HOLDS\n' "$f"
    else
        printf '  %-32s VIOLATION: committed lines modified or deleted\n' "$f"
        git diff HEAD -- "$f" | grep '^-[^-]' | head -5 | sed 's/^/      /'
        fail=1
    fi
done

if [ "$fail" -eq 0 ]; then
    echo "RESULT: the constitution grew by appending only.  PASS."
else
    echo "RESULT: a committed row or norm was changed in place.  FAIL."
    echo "        Corrections are NEW rows pointing at old ones — the"
    echo "        circles' own law.  Revert the modification and append."
fi
exit "$fail"
