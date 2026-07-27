#!/bin/sh
# audit/s7c_transcription.sh — the TRANSCRIPTION / COURIER-FIDELITY gate (S7c).
# Catches SPECIMEN B: declarations whose statement was TRUNCATED by the
# proof-stripper (the courier), so seat B is shown an incomplete claim.
#
# ADJUDICATOR DECLARATION (norm 15):
#   WHAT THIS CHECKS — two independent sub-checks:
#     T1 (re-extraction fidelity, norm 12): re-run the courier extractor on
#        the CURRENT kernel and require the fresh output to be BYTE-IDENTICAL
#        to the shipped statements file. This proves the shipped artifact is
#        the script's genuine output, not hand-edited.
#     T2 (truncation detection, specimen B): a declaration in the statements
#        file is TRUNCATED iff it is structurally incomplete:
#          (a) a `theorem NAME :` whose captured statement reduces to a
#              dangling binder `let ID` with NO following proposition (the
#              extractor cut at the let-binder's ':=' instead of the proof's);
#          (b) a `def SIG : TYPE` line carrying NEITHER a ':=' body NOR a
#              `where` — a bodyless def (the extractor dropped its body).
#   WHAT IT DOES NOT CHECK: truth of the statements (seat B / census); prose
#     purity of the file (that is the purity gate). This gate checks that each
#     shown declaration is a COMPLETE transcription of a kernel declaration.
#   NAMED ADJUDICATOR: this gate + the courier extractor it re-runs (T1) +
#     the structural rule T2, plant-bitten both directions.
#
# NORM 16: (T2) inject a bodyless `def PLANT : Zi` -> gate FAILS naming it;
#   remove it -> the ONLY remaining flags are the shipped specimens (the two
#   `let eta` theorems + `def twist`). (T1) mutate the kernel copy used for
#   re-extraction -> fidelity FAILS; use the true kernel -> PASSES.
#   NOTE: the shipped file ALREADY carries specimen B, so on the shipped
#   artifact T2 is EXPECTED RED, and that red is the finding -> courier charge.
#
# USAGE:  sh audit/s7c_transcription.sh [STATEMENTS_FILE] [KERNEL_FILE] [TAG]
# Exit 0 iff RESULT: PASS. POSIX sh + python3 (extractor) + awk.
set -u
LC_ALL=C; export LC_ALL
SELF_DIR=$(dirname "$0")
EXP=$(cd "$SELF_DIR/.." && pwd)
SF=${1:-"$EXP/courier/Zi_statements_v8.txt"}
KERNEL=${2:-"$EXP/seatP/Zi.lean"}
# the extraction TAG is a parameter, not a literal: it moves with the kernel
# version, and a stale literal here would fail T1 for the wrong reason.
TAG=${3:-"v8 (S1..S7)"}
EXTRACT="$EXP/courier/extract_statements.py"

fail=0

# ---- T1: re-extraction fidelity (norm 12) --------------------------------
echo "-- T1 re-extraction fidelity (norm 12) --"
if [ ! -f "$EXTRACT" ]; then
    echo "  T1: ERROR extractor not found: $EXTRACT"; fail=1
elif [ ! -f "$KERNEL" ]; then
    echo "  T1: ERROR kernel not found: $KERNEL"; fail=1
else
    FRESH=$(mktemp)
    python3 "$EXTRACT" "$KERNEL" "$FRESH" "$TAG" >/dev/null 2>&1
    if diff -q "$SF" "$FRESH" >/dev/null 2>&1; then
        echo "  T1: fresh extraction BYTE-IDENTICAL to shipped file .... PASS"
    else
        echo "  T1: fresh extraction DIFFERS from shipped file ......... FAIL"
        diff "$SF" "$FRESH" | head -20
        fail=1
    fi
    rm -f "$FRESH"
fi

# ---- T2: truncation detection (specimen B) -------------------------------
echo "-- T2 truncation detection (specimen B) --"
TRUNC=$(awk '
{
    lines[NR]=$0
}
END {
    n=0
    for (i=1;i<=NR;i++) {
        L=lines[i]
        # (a) theorem NAME : whose next non-blank captured line is a dangling
        #     "let ID" and the FOLLOWING line is blank/next-decl (no proposition)
        if (L ~ /^theorem [A-Za-z0-9_]+ :[ \t]*$/) {
            k=i+1
            while (k<=NR && lines[k] ~ /^[ \t]*$/) k++     # skip blanks
            if (k<=NR && lines[k] ~ /^[ \t]+let [A-Za-z0-9_]+[ \t]*$/) {
                m=k+1
                # is there a real proposition line after the dangling let?
                if (m>NR || lines[m] ~ /^[ \t]*$/ || lines[m] ~ /^(theorem|def|structure|namespace|end) /) {
                    printf "TRUNC(theorem-let): line %d: %s  [dangling let at line %d: %s]\n", i, L, k, lines[k]
                    n++
                }
            }
        }
        # (b) def SIG : TYPE with NO ":=" and NO "where" on the line, AND whose
        #     body was NOT continued on the following lines. A COMPLETE def
        #     whose body is off-line takes one of two shapes we must NOT flag:
        #       - a pattern-match / equation block: next non-blank line is "| ..."
        #       - an indented term continuation: next non-blank line is indented
        #         and is not itself a new declaration.
        #     It is TRUNCATED (bodyless) iff the next non-blank line is a NEW
        #     declaration (def/theorem/structure/namespace/end) or EOF.
        if (L ~ /^def / && L !~ /:=/ && L !~ /where/ && L ~ /:/) {
            k=i+1
            while (k<=NR && lines[k] ~ /^[ \t]*$/) k++      # skip blanks
            bodyless=0
            if (k>NR) bodyless=1
            else if (lines[k] ~ /^(def|theorem|structure|namespace|end|deriving|instance|abbrev) /) bodyless=1
            # else: "| arm", or indented continuation -> COMPLETE, do not flag
            if (bodyless) {
                printf "TRUNC(def-bodyless): line %d: %s\n", i, L
                n++
            }
        }
    }
    exit (n>0?1:0)
}
' "$SF")
if [ -n "$TRUNC" ]; then
    echo "$TRUNC" | sed 's/^/  /'
    nt=$(printf '%s\n' "$TRUNC" | grep -c '^TRUNC')
    echo "  T2: $nt truncated declaration(s) ...................... FAIL"
    fail=1
else
    echo "  T2: no truncated declarations ........................ PASS"
fi

echo "----------------------------------------------------------------------"
if [ "$fail" -eq 0 ]; then
    echo "RESULT: PASS"
    exit 0
else
    echo "RESULT: FAIL"
    exit 1
fi
