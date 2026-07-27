#!/bin/sh
# audit/plant_s7_courier.sh — NORM 16 harness for the Round-3 courier repair.
#
# An instrument you have not seen FAIL is not yet your instrument. This
# harness bites the two S7c gates AND the extractor repair itself, in both
# directions, on scratch copies only — it never touches the shipped tree.
#
# ADJUDICATOR DECLARATION (norm 15):
#   WHAT THIS CHECKS — five plants, each RED-then-GREEN:
#     P1 purity gate:      append a prose line to the statements copy
#                          -> purity FAILS naming it; remove -> PASSES.
#     P2 transcription T2: inject a bodyless `def PLANT : Zi`
#                          -> T2 FAILS naming it; remove -> PASSES.
#     P3 transcription T1: re-extract from a MUTATED kernel copy
#                          -> fidelity FAILS; true kernel -> PASSES.
#     P4 extractor R1:     revert comment-awareness (the depth map)
#                          -> the 16-line S5 prose leak returns, purity RED.
#     P5 extractor R2:     revert the binder-aware proof cut
#                          -> the two `let eta` theorems truncate, T2 RED.
#   P4 and P5 are the important ones: they plant against the REPAIR, not
#   just against the gates, so a silently-reverted fix cannot pass unseen.
#   WHAT IT DOES NOT CHECK: truth of any statement (seat B / census).
#
# USAGE:  sh audit/plant_s7_courier.sh
# Exit 0 iff every plant bit and every restore passed.
set -u
LC_ALL=C; export LC_ALL
SELF_DIR=$(dirname "$0")
EXP=$(cd "$SELF_DIR/.." && pwd)
KERNEL="$EXP/seatP/Zi.lean"
EXTRACT="$EXP/courier/extract_statements.py"
SF="$EXP/courier/Zi_statements_v8.txt"
TAG="v8 (S1..S7)"
PURITY="$EXP/audit/s7c_statements_purity.sh"
TRANS="$EXP/audit/s7c_transcription.sh"

WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT
fail=0

say() { printf '  %s\n' "$*"; }
# expect <want-rc> <label> <command...>
expect() {
    want=$1; label=$2; shift 2
    "$@" >"$WORK/o.txt" 2>&1
    got=$?
    if [ "$got" -eq "$want" ]; then
        say "$label ... OK (exit $got)"
    else
        say "$label ... UNEXPECTED (exit $got, wanted $want)"
        sed 's/^/      /' "$WORK/o.txt" | head -12
        fail=1
    fi
}

echo "======================================================================"
echo "NORM 16 — plants for the Round-3 courier repair (both directions)"
echo "======================================================================"

# ---- P1: purity gate bites a planted prose line -------------------------
echo "-- P1 purity gate, planted prose line --"
cp "$SF" "$WORK/p1.txt"
printf '    the ledger is called "the" indicator, not a footnote.\n' >> "$WORK/p1.txt"
expect 1 "planted prose  -> purity RED " sh "$PURITY" "$WORK/p1.txt"
cp "$SF" "$WORK/p1.txt"
expect 0 "restored        -> purity GREEN" sh "$PURITY" "$WORK/p1.txt"

# ---- P2: transcription T2 bites a planted bodyless def ------------------
echo "-- P2 transcription T2, planted bodyless def --"
cp "$SF" "$WORK/p2.txt"
printf '\ndef PLANT_bodyless : Zi\n\ntheorem PLANT_after : one = one\n' >> "$WORK/p2.txt"
expect 1 "planted def    -> T2 RED   " sh "$TRANS" "$WORK/p2.txt" "$KERNEL"
cp "$SF" "$WORK/p2.txt"
expect 0 "restored       -> T2 GREEN " sh "$TRANS" "$WORK/p2.txt" "$KERNEL"

# ---- P3: transcription T1 bites a mutated kernel ------------------------
echo "-- P3 transcription T1, mutated kernel (re-extraction fidelity) --"
sed 's/^theorem mul_comm /theorem mul_comm_PLANT /' "$KERNEL" > "$WORK/k3.lean"
expect 1 "mutated kernel -> T1 RED   " sh "$TRANS" "$SF" "$WORK/k3.lean"
expect 0 "true kernel    -> T1 GREEN " sh "$TRANS" "$SF" "$KERNEL"

# ---- P4: revert extractor R1 (comment awareness) ------------------------
echo "-- P4 extractor R1 reverted (comment awareness) --"
sed 's/^    if depths\[i\] > 0:.*$/    if False:/' "$EXTRACT" > "$WORK/ex4.py"
if cmp -s "$EXTRACT" "$WORK/ex4.py"; then
    say "R1 revert did not apply — plant is INERT ... FAIL"; fail=1
else
    python3 "$WORK/ex4.py" "$KERNEL" "$WORK/p4.txt" "$TAG" >/dev/null 2>&1
    expect 1 "R1 reverted    -> purity RED  " sh "$PURITY" "$WORK/p4.txt"
    python3 "$EXTRACT" "$KERNEL" "$WORK/p4.txt" "$TAG" >/dev/null 2>&1
    expect 0 "R1 restored    -> purity GREEN" sh "$PURITY" "$WORK/p4.txt"
fi

# ---- P5: revert extractor R2 (binder-aware proof cut) -------------------
echo "-- P5 extractor R2 reverted (binder-aware proof cut) --"
sed "s/^        if not BINDER_HEAD.search(line\[:k\].rstrip()):$/        if True:/" \
    "$EXTRACT" > "$WORK/ex5.py"
if cmp -s "$EXTRACT" "$WORK/ex5.py"; then
    say "R2 revert did not apply — plant is INERT ... FAIL"; fail=1
else
    python3 "$WORK/ex5.py" "$KERNEL" "$WORK/p5.txt" "$TAG" >/dev/null 2>&1
    expect 1 "R2 reverted    -> T2 RED   " sh "$TRANS" "$WORK/p5.txt" "$KERNEL"
    python3 "$EXTRACT" "$KERNEL" "$WORK/p5.txt" "$TAG" >/dev/null 2>&1
    expect 0 "R2 restored    -> T2 GREEN " sh "$TRANS" "$WORK/p5.txt" "$KERNEL"
fi

echo "----------------------------------------------------------------------"
if [ "$fail" -eq 0 ]; then
    echo "RESULT: PASS — 5 plants bitten, 5 restores clean (10 checks)"
    exit 0
else
    echo "RESULT: FAIL"
    exit 1
fi
