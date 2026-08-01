#!/bin/sh
# verdict_exit.sh — a check whose verdict is a STRING and whose exit is a CONSTANT.
#
#   THE SPECIMEN THIS EXISTS FOR, reproduced 2026-08-01 on the-workshop@origin/main:
#
#       $ python3 history/verification/independent_math_check.py
#       ...
#       FAIL rank M = 5 (GF2)
#       ...
#       All independent checks complete.
#       $ echo $?
#       0
#
#   The whole harness is one line — `independent_math_check.py:5`:
#
#       ok = lambda name, cond: print(("PASS " if cond else "FAIL ") + name)
#
#   No counter, no accumulator, no sys.exit. Twenty-six checks, any number of
#   which may fail, and the process always exits 0 and prints "complete". Put it
#   in CI and CI goes green while the script says FAIL out loud.
#
#   This is the record's recurring species — a MARKER standing in for a PROPERTY
#   — in its purest form: the verdict is a printed word, and the exit code, which
#   is the only thing another program reads, is a constant.
#
#   WHAT IT CHECKS: tracked *.py files that speak verdict vocabulary (PASS/FAIL/
#   OK/True/False/✓/✗/MISMATCH) but contain NO path to a non-zero exit — no
#   `sys.exit`, no bare `exit(`, no top-level `assert`, no `raise`.
#
#   WHAT IT MISSES, said plainly:
#     - `sys.exit(0)` unconditionally at the end still counts as an escape here
#       and should not. Presence of the token is not proof the exit is reachable
#       or correct; this gate is about the ABSENCE being provable, not the
#       presence being sound.
#     - A shell script with the same defect is not scanned. Python only, for now.
#     - A script that raises only on an unrelated error path passes. That is a
#       false negative and it is the gate's real limit.
#
#   BITE (norm 16): plants/bite.sh runs four plants against this gate.
#
#   USAGE:  sh autopsy-evidence/c4-prover/verdict_exit.sh [root]
#           exit 0 = every verdict-speaking script can reach a non-zero exit.
#           exit 1 = at least one cannot.

ROOT=${1:-.}
cd "$ROOT" || exit 2

if git rev-parse --git-dir >/dev/null 2>&1; then
    LIST=$(git ls-files '*.py')
else
    LIST=$(find . -name '*.py' -not -path '*/.git/*' | sed 's|^\./||')
fi

RED=0
for f in $LIST; do
    [ -f "$f" ] || continue
    # Archived snapshots are history, not live instruments.
    case "$f" in */floor-snapshots/*|*/inherited/*|*/as-received/*) continue ;; esac

    grep -qE '\b(PASS|FAIL|MISMATCH|GREEN|RED)\b|✓|✗|\bTrue\b|\bFalse\b' "$f" || continue
    grep -qE 'sys\.exit|(^|[^_a-zA-Z])exit\(|^[[:space:]]*assert[[:space:]]|(^|[^a-zA-Z])raise[[:space:]]' "$f" && continue

    echo "VERDICT-BY-PRINT: $f"
    echo "    speaks PASS/FAIL but has no path to a non-zero exit code."
    RED=1
done

if [ "$RED" -eq 0 ]; then
    echo "verdict_exit: clean -- every verdict-speaking script can fail loudly."
    exit 0
fi

echo ""
echo "verdict_exit: RED."
echo "  A check whose verdict is a printed word cannot be read by CI, by a hook,"
echo "  or by another script. The repair is one accumulator and one sys.exit."
exit 1
