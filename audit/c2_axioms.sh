#!/bin/sh
# audit/c2_axioms.sh — the proof-term hygiene census (REGISTER row 4),
# Circle Two's re-instantiation of Circle One's axioms.sh.
#
# WHY THIS EXISTS
#   A green kernel says the proof term type-checks. It does not say WHAT the
#   proof term leaned on. Circle One's census is the instrument that turns
#   "it compiled" into "it compiled, and here is every axiom it used" — and
#   it is the instrument that catches the trap HANDOFF.md records being
#   bitten by twice: an `omega` aimed at a conjunctive goal silently pulls
#   in `Classical.choice`. This census is how that stays caught.
#
# CONTRACT
#   For every theorem in the Lean tree, ask the kernel `#print axioms` and
#   tabulate. The gate FAILS (exit 1) on either of two findings:
#     - any `sorryAx`          — a hole, marked or not, reached the record;
#     - any `Classical.choice` — the trap, or an unannounced use of choice.
#   Everything else is reported, never judged: `propext` and `Quot.sound`
#   are ordinary kernel axioms and a theorem using them is not defective.
#   The census does NOT re-prove anything; it reads what the kernel says.
#
#   METHOD, stated because it matters for what the numbers mean: the census
#   compiles a GENERATED COPY of each source file with `#print axioms` lines
#   appended — the shipped file stays silent (norm 10), and the census still
#   measures the shipped file's own theorems, because the copy is the file
#   plus queries and nothing else. The copy is written to a temp directory
#   and removed; it is never committed (see audit/c2_tree.sh).
#
#   The compile guard matches `error:` AND `error(`: Lean 4.32.0 reports an
#   unknown constant as `error(lean.unknownIdentifier):`, so a guard keyed to
#   `error:` alone was dead for precisely the failure this census can cause (a
#   query naming a theorem that does not exist). Found by the adversarial audit.
#
# BOUNDARY
#   It censuses `theorem` declarations only — `def`s carry no proof
#   obligation, and a `example` has no name to ask about. It cannot see a
#   theorem whose STATEMENT is wrong, which is norm 6's territory and class
#   6's, not this instrument's. And it trusts the toolchain it is pointed at.
#
#   ONE NAMESPACE PER FILE. Queries are qualified with the file's FIRST
#   `namespace`, so a file opening two namespaces produces a query naming a
#   constant that does not exist. That is not silent: the compile guard above
#   catches it and the census exits 1 (measured, with a two-namespace plant).
#   Loud-and-wrong is the acceptable failure here; silent-and-wrong is not.
#   When a second namespace is genuinely needed, teach the harvest to track
#   the namespace stack — do not relax the guard.
#
# NORM 16
#   Bitten before trusted: append `theorem plant : False := by sorry` to a
#   scratch copy of a Lean file, run this census, watch it name `sorryAx`
#   and exit 1. An alarm you have not seen fire is not an alarm.
#
# USAGE
#   sh audit/c2_axioms.sh              (uses `lean` from PATH)
#   The query copy is compiled INSIDE a temp directory holding a copy of the
#   repo's lean-toolchain, so a toolchain manager resolving the pin from the
#   working directory finds the record's pin rather than the machine's
#   default. Copying the pin is necessary but not sufficient — the compile
#   must happen there too. LEAN=<abs path> bypasses PATH resolution entirely.
#   FALSIFIER (norm 14, and it must actually be run): invoke this script with
#   a `lean` that has no default toolchain configured. Before the compile-from-
#   inside fix the census failed with "no default toolchain configured"; after
#   it, the census PASSES.
#   LEAN=/path/to/lean sh audit/c2_axioms.sh
#   C2_LEAN_DIR=lean sh audit/c2_axioms.sh    (default: the repo's lean/)

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || {
    echo "c2_axioms: not a git repository" >&2; exit 2; }
cd "$ROOT" || exit 2

LEANBIN=${LEAN:-lean}
LEANDIR=${C2_LEAN_DIR:-lean}

# Resolve the binary to an absolute path now: the query copy is compiled from
# inside the temp directory (see below), and a relative LEANBIN would not
# survive that `cd`.
case $LEANBIN in
    /*) : ;;
    *)  _resolved=$(command -v "$LEANBIN" 2>/dev/null)
        [ -n "$_resolved" ] && LEANBIN=$_resolved ;;
esac

command -v "$LEANBIN" >/dev/null 2>&1 || {
    echo "c2_axioms: no Lean binary — set LEAN=/path/to/lean" >&2
    echo "           (this gate cannot be satisfied by assuming; it needs the kernel)" >&2
    exit 2; }

[ -d "$LEANDIR" ] || {
    echo "c2_axioms: no directory '$LEANDIR' — nothing to census." >&2
    echo "           REGISTER row 4 stays frontier until Lean sources land." >&2
    exit 2; }

files=$(find "$LEANDIR" -name '*.lean' | sort)
[ -n "$files" ] || {
    echo "c2_axioms: no .lean files under '$LEANDIR' — nothing to census." >&2
    exit 2; }

WORK=$(mktemp -d) || exit 2
trap 'rm -rf "$WORK"' EXIT INT TERM

echo "=============================================================="
echo " C2 AXIOM CENSUS -- what every proof term actually leaned on"
echo "=============================================================="
printf ' toolchain: %s\n' "$("$LEANBIN" --version 2>/dev/null | head -1)"
echo "--------------------------------------------------------------"
printf '%-20s %10s %12s %10s\n' "file" "theorems" "axiom-free" "rest"

tot_thm=0; tot_free=0; tot_rest=0; tot_sorry=0; tot_choice=0; hard_fail=0

for f in $files; do
    base=$(basename "$f" .lean)
    # the namespace, if the file opens exactly one at top level
    ns=$(grep -m1 '^namespace ' "$f" | awk '{print $2}')

    # ---- harvest, comment-stripped and modifier-tolerant --------------
    # An earlier version harvested with `grep '^theorem '` + a narrow sed.
    # It silently missed `@[simp] theorem`, `private theorem`, and any
    # indented declaration — and the consistency check below could not see
    # the omission, because both of its sides came from that same grep. A
    # census that can under-report without saying so is worse than no
    # census. Found by the adversarial audit of the S1 delivery.
    #
    # Comments are stripped first (nested `/- -/`, `/-! -/`, and `--` to
    # end of line) so that the word "theorem" in prose cannot be counted.
    # BOUNDARY: a `theorem` keyword inside a string literal would still be
    # seen. No file in this tree contains one; if one ever does, this is
    # where to fix it.
    stripped="$WORK/$base.stripped"
    awk '
      { line = $0; out = ""; i = 1; n = length(line)
        while (i <= n) {
          c = substr(line, i, 2)
          if (depth == 0 && c == "--") { break }
          if (c == "/-") { depth++; i += 2; continue }
          if (c == "-/") { if (depth > 0) depth--; i += 2; continue }
          if (depth == 0) { out = out substr(line, i, 1) }
          i++
        }
        print out }
    ' "$f" > "$stripped"

    DECLRE="^[[:space:]]*(@\\[[^]]*\\][[:space:]]*)*(private[[:space:]]+|protected[[:space:]]+|nonrec[[:space:]]+)*theorem[[:space:]]"
    ndecl=$(grep -cE "$DECLRE" "$stripped")
    names=$(grep -E "$DECLRE" "$stripped" \
            | sed -E "s/^[[:space:]]*(@\\[[^]]*\\][[:space:]]*)*(private[[:space:]]+|protected[[:space:]]+|nonrec[[:space:]]+)*theorem[[:space:]]+([A-Za-z_][A-Za-z0-9_']*).*/\\3/")
    nnames=$(printf '%s\n' "$names" | grep -c .)

    # detection and extraction are separate steps; if they disagree, a name
    # was lost and the census would silently under-report. Fail loudly.
    if [ "$ndecl" -ne "$nnames" ]; then
        echo "CENSUS ERROR in $f — $ndecl theorem declarations detected but"
        echo "  $nnames names extracted; the harvest lost a name. Fix the"
        echo "  extraction, never the count."
        hard_fail=1
        continue
    fi

    gen="$WORK/$base.lean"
    cp "$f" "$gen"
    # PORTABILITY (chartered in the builder's S1 verification): the query copy
    # is compiled in a temp directory, outside any lean-toolchain's reach. On a
    # container whose elan has no default configured, that made the census fail
    # with "no default toolchain configured" — loudly, which is the alarm
    # working, but its verdict depended on machine state outside the repo.
    # Carry the repo's pin to the copy so the census is pinned by the record
    # rather than by the machine.
    if [ -f "$LEANDIR/lean-toolchain" ]; then
        cp "$LEANDIR/lean-toolchain" "$WORK/lean-toolchain"
    fi
    # close the namespace before querying, then query with fully-qualified names
    printf '\n' >> "$gen"
    for n in $names; do
        if [ -n "$ns" ]; then
            printf '#print axioms %s.%s\n' "$ns" "$n" >> "$gen"
        else
            printf '#print axioms %s\n' "$n" >> "$gen"
        fi
    done

    # Compile FROM INSIDE the temp directory. elan resolves lean-toolchain
    # from the WORKING DIRECTORY and its parents, not from the source file's
    # location — so copying the pin beside the file (above) is necessary but
    # NOT sufficient; the compile has to happen there too. The first version
    # of this fix copied the pin and kept compiling from the repo root, which
    # left the pin travelling and never read. Caught by the builder's pass,
    # after its own falsifier (run with no elan default) was never run here —
    # norm 14's exact species, inside a repair about norm 16.
    out=$(cd "$WORK" && "$LEANBIN" "$base.lean" 2>&1)
    # a compile error in the generated copy is a census failure, loudly
    if printf '%s' "$out" | grep -qE 'error[:(]'; then
        echo "CENSUS ERROR in $f — the generated copy did not compile:"
        printf '%s\n' "$out" | grep -E 'error[:(]' | head -5
        hard_fail=1
        continue
    fi

    n_thm=$(printf '%s\n' "$names" | grep -c .)
    n_free=$(printf '%s\n' "$out" | grep -c 'does not depend on any axioms')
    n_rest=$(printf '%s\n' "$out" | grep -c 'depends on axioms')
    n_sorry=$(printf '%s\n' "$out" | grep -c 'sorryAx')
    n_choice=$(printf '%s\n' "$out" | grep -c 'Classical.choice')

    printf '%-20s %10s %12s %10s\n' "$base" "$n_thm" "$n_free" "$n_rest"

    # name the offenders, if any
    if [ "$n_sorry" -gt 0 ]; then
        printf '%s\n' "$out" | grep 'sorryAx' | sed 's/^/    SORRY: /'
    fi
    if [ "$n_choice" -gt 0 ]; then
        printf '%s\n' "$out" | grep 'Classical.choice' | sed 's/^/    CHOICE: /'
    fi
    # Name the Quot.sound carriers too. They are NOT defects — the contract
    # above says so — but an earlier delivery counted twelve of them and no
    # shipped document named one, while the file header cited this census for
    # "per-theorem answers" it did not print. A census that counts without
    # naming makes the reader take the count on faith, which is the thing
    # this house does not do. Found by the builder's pass (its crop #6).
    n_quot=$(printf '%s\n' "$out" | grep -c 'Quot.sound')
    if [ "$n_quot" -gt 0 ]; then
        printf '%s\n' "$out" | grep 'Quot.sound' | sed 's/^/    quot: /'
    fi

    tot_thm=$((tot_thm + n_thm)); tot_free=$((tot_free + n_free))
    tot_rest=$((tot_rest + n_rest)); tot_sorry=$((tot_sorry + n_sorry))
    tot_choice=$((tot_choice + n_choice))
done

echo "--------------------------------------------------------------"
printf '%-20s %10s %12s %10s\n' "TOTAL" "$tot_thm" "$tot_free" "$tot_rest"
printf '%-20s %10s\n' "sorryAx" "$tot_sorry"
printf '%-20s %10s\n' "Classical.choice" "$tot_choice"
echo "=============================================================="

if [ "$hard_fail" -ne 0 ]; then
    echo "RESULT: FAIL -- a generated census copy did not compile (see above)."
    exit 1
fi
if [ "$tot_thm" -ne $((tot_free + tot_rest)) ]; then
    echo "RESULT: FAIL -- $tot_thm theorems declared but $((tot_free + tot_rest)) answers"
    echo "        came back; a theorem the census could not ask about is a"
    echo "        theorem the census does not cover.  Fix the query, not the count."
    exit 1
fi
if [ "$tot_sorry" -gt 0 ] || [ "$tot_choice" -gt 0 ]; then
    echo "RESULT: FAIL -- sorryAx: $tot_sorry, Classical.choice: $tot_choice."
    exit 1
fi
echo "RESULT: no sorryAx, no Classical.choice; every theorem's axioms named.  PASS."
exit 0
