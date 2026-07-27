#!/bin/sh
# audit/plant_s7_slice.sh — NORM 16 harness for the S7a slice lemma.
#
# Charge §5.4 requires plants in BOTH directions: the instruments must fail on
# a planted defect and pass on byte-identical restore. This bites the kernel
# proof AND the blind verifier, on scratch copies only — the shipped tree is
# never modified.
#
# ADJUDICATOR DECLARATION (norm 15):
#   WHAT THIS CHECKS — six plants, each RED-then-GREEN:
#     K1 kernel, the witness: drop the `conj` from sliceGauge's η(0,1)
#        -> the slice lemma no longer compiles (the gauge stops inverting).
#     K2 kernel, a nest count: claim 31 cocycles instead of 32
#        -> `decide` refuses; the nest cannot be edited to taste.
#     K3 kernel, the class label: use F(1,1,1) alone instead of
#        F(1,1,1)·F(1,0,0)·F(0,0,1) -> the lemma breaks.
#     V1 verifier, the witness: same conj drop in seat B's transcription
#        -> `sliceGauge_normalizes_every_cocycle` goes RED.
#     V2 verifier, the parametrization: corrupt cochainOf's (1,0,1) slot
#        -> `parametrization_is_exact` goes RED.
#     V3 kernel label (norm 6): rename the lemma to say U1
#        -> the verifier's label audit goes RED.
#   Restores are byte-identical (checked by sha256, not by eye).
#   WHAT IT DOES NOT CHECK: courier fidelity (that is plant_s7_courier.sh).
#
# The kernel plants need Lean. Set LEAN=/path/to/lean, or have `lean` on PATH.
# Without it the K plants are reported SKIPPED and the run FAILS — a plant
# that cannot run is not a plant that bit.
#
# USAGE:  LEAN=/path/to/lean sh audit/plant_s7_slice.sh
# Exit 0 iff every plant bit and every restore passed.
set -u
LC_ALL=C; export LC_ALL
SELF_DIR=$(dirname "$0")
EXP=$(cd "$SELF_DIR/.." && pwd)
KERNEL="$EXP/seatP/Zi.lean"
VERIFIER="$EXP/seatB/verify_zi_s7.py"
LEANBIN=${LEAN:-lean}

WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT
fail=0
BASE_KERNEL=$(sha256sum "$KERNEL" | cut -d' ' -f1)
BASE_VERIF=$(sha256sum "$VERIFIER" | cut -d' ' -f1)

say() { printf '  %s\n' "$*"; }

# lean_is_silent <file> : 0 iff exit 0 AND zero bytes (norm 10)
lean_is_silent() {
    "$LEANBIN" "$1" > "$WORK/lean.txt" 2>&1
    rc=$?
    [ "$rc" -eq 0 ] && [ ! -s "$WORK/lean.txt" ]
}

# kplant <label> <sed-expr>
kplant() {
    label=$1; expr=$2
    sed "$expr" "$KERNEL" > "$WORK/k.lean"
    if cmp -s "$KERNEL" "$WORK/k.lean"; then
        say "$label: plant did not apply — INERT ... FAIL"; fail=1; return
    fi
    if lean_is_silent "$WORK/k.lean"; then
        say "$label: planted kernel still compiles SILENT ... FAIL"; fail=1
    else
        say "$label: planted kernel REJECTED by Lean ... OK"
    fi
}

# vplant <label> <sed-expr> <check-name-expected-red>
vplant() {
    label=$1; expr=$2; want=$3
    sed "$expr" "$VERIFIER" > "$WORK/v.py"
    if cmp -s "$VERIFIER" "$WORK/v.py"; then
        say "$label: plant did not apply — INERT ... FAIL"; fail=1; return
    fi
    python3 "$WORK/v.py" > "$WORK/v.txt" 2>&1
    rc=$?
    if [ "$rc" -ne 0 ] && grep -q "^FAIL  $want" "$WORK/v.txt"; then
        say "$label: verifier exit 1, poisoned check named ($want) ... OK"
    else
        say "$label: verifier did not bite (exit $rc) ... FAIL"
        grep '^FAIL' "$WORK/v.txt" | head -3 | sed 's/^/      /'
        fail=1
    fi
}

echo "======================================================================"
echo "NORM 16 — plants for the S7a slice lemma (both directions)"
echo "======================================================================"

# ---- kernel plants ------------------------------------------------------
echo "-- kernel plants (seat P) --"
if command -v "$LEANBIN" >/dev/null 2>&1; then
    if lean_is_silent "$KERNEL"; then
        say "baseline: shipped kernel compiles SILENT ... OK"
    else
        say "baseline: shipped kernel is NOT silent ... FAIL"; fail=1
    fi
    kplant "K1 witness (conj dropped from η01)" \
        's|else if a = 0 ∧ b = 1 then conj (F 0 0 1) else one|else if a = 0 ∧ b = 1 then F 0 0 1 else one|'
    kplant "K2 nest count (32 -> 31)" \
        's|slotList.length = 8 ∧ cocycleTriples.length = 32|slotList.length = 8 ∧ cocycleTriples.length = 31|'
    kplant "K3 class label (F(1,1,1) alone)" \
        's|refine ⟨sliceGauge F, mul (mul (F 1 1 1) (F 1 0 0)) (F 0 0 1), ?_, ?_, ?_⟩|refine ⟨sliceGauge F, F 1 1 1, ?_, ?_, ?_⟩|'
    if lean_is_silent "$KERNEL"; then
        say "restore: shipped kernel compiles SILENT again ... OK"
    else
        say "restore: shipped kernel is NOT silent ... FAIL"; fail=1
    fi
else
    say "K1/K2/K3: SKIPPED — no Lean binary; set LEAN=/path/to/lean"
    say "A plant that cannot run is not a plant that bit."
    fail=1
fi

# ---- verifier plants ----------------------------------------------------
echo "-- verifier plants (seat B) --"
python3 "$VERIFIER" > "$WORK/v0.txt" 2>&1
if [ $? -eq 0 ]; then
    say "baseline: shipped verifier exits 0 ... OK"
else
    say "baseline: shipped verifier does NOT exit 0 ... FAIL"; fail=1
fi

vplant "V1 witness (conj dropped from η01)" \
    's|(0, 1): gconj(F\[(0, 0, 1)\])|(0, 1): F[(0, 0, 1)]|' \
    "sliceGauge_normalizes_every_cocycle"
vplant "V2 parametrization ((1,0,1) corrupted)" \
    's|(1, 0, 1): gmul(q, p)|(1, 0, 1): gmul(q, q)|' \
    "parametrization_is_exact"

# V3: plant the LABEL in the kernel, watch the verifier's norm-6 audit bite
echo "-- label plant (norm 6), kernel -> verifier --"
sed 's|^theorem slice_lemma_over_zi_units |theorem slice_lemma_over_U1 |' \
    "$KERNEL" > "$WORK/klabel.lean"
if cmp -s "$KERNEL" "$WORK/klabel.lean"; then
    say "V3: plant did not apply — INERT ... FAIL"; fail=1
else
    cp "$KERNEL" "$WORK/kernel.bak"
    cp "$WORK/klabel.lean" "$KERNEL"
    python3 "$VERIFIER" > "$WORK/v3.txt" 2>&1
    rc=$?
    cp "$WORK/kernel.bak" "$KERNEL"
    if [ "$rc" -ne 0 ] && grep -q '^FAIL  label_no_U1_in_theorem_names' "$WORK/v3.txt"; then
        say "V3: a lemma renamed to U1 -> label audit RED ... OK"
    else
        say "V3: label audit did not bite (exit $rc) ... FAIL"; fail=1
    fi
fi

# ---- byte-identical restore (measured, not eyeballed) -------------------
echo "-- restore, byte-identical (norm 12) --"
NOW_KERNEL=$(sha256sum "$KERNEL" | cut -d' ' -f1)
NOW_VERIF=$(sha256sum "$VERIFIER" | cut -d' ' -f1)
if [ "$NOW_KERNEL" = "$BASE_KERNEL" ]; then
    say "kernel   restored byte-identical ... OK"
else
    say "kernel   NOT restored ($BASE_KERNEL -> $NOW_KERNEL) ... FAIL"; fail=1
fi
if [ "$NOW_VERIF" = "$BASE_VERIF" ]; then
    say "verifier restored byte-identical ... OK"
else
    say "verifier NOT restored ($BASE_VERIF -> $NOW_VERIF) ... FAIL"; fail=1
fi

echo "----------------------------------------------------------------------"
if [ "$fail" -eq 0 ]; then
    echo "RESULT: PASS — 6 plants bitten; baselines and restores clean"
    exit 0
else
    echo "RESULT: FAIL"
    exit 1
fi
