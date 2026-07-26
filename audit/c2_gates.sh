#!/bin/sh
# audit/c2_gates.sh — every instrument, chained, one exit code.
#
# WHY THIS EXISTS
#   I committed a delivery letter with the pointer gate RED. I ran the gate,
#   read `RESULT: FAIL`, and let the commit go out in the same breath
#   (recorded at 9a28f25). The token was trivial; the defect was not — a gate
#   was consulted and then not obeyed.
#
#   Norm 7 says a check that cannot fail is not a check. The corollary that
#   commit earned: a check that CAN fail and is ignored is not one either.
#   The builder's answer, chartered in the units verification, is the same
#   medicine that turned typed counts into rendered ones — make the red gate
#   BLOCK the commit instead of advising it. Discipline becomes mechanism.
#
# CONTRACT
#   Runs every instrument in order and exits non-zero if ANY fails. Prints
#   one line per gate plus a verdict. Intended for two callers:
#     - a human, before a commit;
#     - .githooks/pre-commit, which makes "consulted and not obeyed"
#       impossible rather than merely shameful.
#
#   The Lean-dependent gates (axioms, views) need a binary. Without one they
#   are reported SKIPPED, loudly, and the run FAILS — a gate that cannot run
#   is not a gate that passed. Set LEAN=/path/to/lean.
#
# BOUNDARY, stated because it is the honest gap
#   A hook lives in the working copy, not in the commit. A commit made with
#   --no-verify, on another machine, or by a body that never ran
#   `git config core.hooksPath .githooks`, is unhooked. That gap is real and
#   is recorded in REGISTER row 5. This mechanism raises the cost of
#   ignoring a red gate; it does not make it impossible.
#
# USAGE
#   LEAN=/path/to/lean sh audit/c2_gates.sh
#   git config core.hooksPath .githooks     (install the hook, once)

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || {
    echo "c2_gates: not a git repository" >&2; exit 2; }
cd "$ROOT" || exit 2

LEANBIN=${LEAN:-lean}
fail=0

run () {
    name=$1; shift
    if "$@" >/dev/null 2>&1; then
        printf '  %-28s PASS\n' "$name"
    else
        printf '  %-28s FAIL\n' "$name"
        fail=1
    fi
}

echo "=============================================================="
echo " C2 GATES -- every instrument, one exit code"
echo "=============================================================="

run "pointers"  sh audit/c2_pointers.sh
run "numerals"  sh audit/c2_numerals.sh
run "tree"      sh audit/c2_tree.sh

if command -v "$LEANBIN" >/dev/null 2>&1; then
    LEAN="$LEANBIN" run "axioms (census)" sh audit/c2_axioms.sh
    LEAN="$LEANBIN" run "views (drift)"   sh audit/c2_views.sh check
else
    printf '  %-28s SKIPPED -- no Lean binary; set LEAN=/path/to/lean\n' "axioms (census)"
    printf '  %-28s SKIPPED -- no Lean binary; set LEAN=/path/to/lean\n' "views (drift)"
    echo "  A gate that cannot run is not a gate that passed."
    fail=1
fi

echo "--------------------------------------------------------------"
if [ "$fail" -eq 0 ]; then
    echo "RESULT: every instrument green.  PASS."
    exit 0
else
    echo "RESULT: FAIL -- at least one instrument is red or unrun."
    echo "        Do not commit past this. Fix it, or record why in the"
    echo "        commit message and accept that the record will say so."
    exit 1
fi
