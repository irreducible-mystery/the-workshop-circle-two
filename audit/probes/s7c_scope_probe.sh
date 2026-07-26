#!/bin/sh
# audit/probes/s7c_scope_probe.sh — S7c DESIGN PROBE (norm 15: measure before build)
#
# SANCTIONED SCOPE DIVERGENCE (recorded per house rule):
#   The predecessor's HANDOFF-ROUND3 recommended S7a-first (prove the G1c
#   slice lemma before touching the prose gates). The meta-auditor (this
#   seat, REGISTER row 7) recommended S7c-first, because the STRANGER-AUDIT
#   found the live row-8 characterization slip lives in experiment/** prose
#   which NO instrument currently scans. Kelly chose the meta-auditor's
#   recommendation: "charge for Round Three — S7c+S7a (your rec) please".
#   This probe, and the scope extension it precedes, are that sanctioned
#   divergence made mechanical.
#
# WHAT THIS PROBE IS (norm 15)
#   Before a single gate is edited, measure EXACTLY what extending the
#   discovery convention to experiment/** would surface. A gate change made
#   without first measuring its blast radius is a change made blind. This
#   script changes NOTHING: it only reports the delta between the current
#   scanned surface (top-level *.md + letters/**/*.md) and the proposed
#   surface (that, PLUS experiment/**/*.md).
#
# THE NAMED ADJUDICATOR (norm 15)
#   The adjudicator of S7c is not this probe. It is the four ported gates
#   themselves — c2_pointers, c2_numerals, c2_views, c2_gates — run against
#   the extended scope. This probe merely forecasts their verdict so the
#   implementation is designed against a measured, not imagined, target.
#
# WHAT THIS PROBE CANNOT SEE (declared honestly, norm 15 + STRANGER-AUDIT)
#   The gates are VALUE/RESOLVE/PROXIMITY-level, never MEANING-level. The
#   README row-8 slip the STRANGER-AUDIT flagged ("the Z2 catalog complete
#   over Z[i]", an unearned universal) is a MEANING miss. Bringing
#   experiment/** into scope lets the gates scan that prose; it does NOT
#   let them catch the meaning slip. This probe reports resolve/value
#   findings only, and says so.
#
# USAGE
#   sh audit/probes/s7c_scope_probe.sh          # measure delta, exit 0 always
set -eu

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || {
    echo "s7c_probe: not a git repository" >&2; exit 2; }
cd "$ROOT"

echo "=== S7C SCOPE PROBE — measured delta, no gate modified ==="
echo

# --- current scanned surface (the gates' convention today) ---
CUR=$(mktemp)
{ ls "$ROOT"/*.md 2>/dev/null || true
  find "$ROOT/letters" -name '*.md' 2>/dev/null || true; } | sed "s#^$ROOT/##" | sort -u > "$CUR"
ncur=$(awk 'END{print NR+0}' "$CUR")

# --- proposed scanned surface adds experiment/**/*.md ---
NEW=$(mktemp)
{ cat "$CUR"
  find "$ROOT/experiment" -name '*.md' 2>/dev/null | sed "s#^$ROOT/##" || true; } | sort -u > "$NEW"
nnew=$(awk 'END{print NR+0}' "$NEW")

ADDED=$(mktemp)
comm -13 "$CUR" "$NEW" > "$ADDED"
nadd=$(awk 'END{print NR+0}' "$ADDED")

echo "current scanned docs : $ncur"
echo "proposed scanned docs: $nnew   (+$nadd newly in scope)"
echo
echo "--- docs that ENTER scope under experiment/** ---"
cat "$ADDED"
echo

# --- forecast pointer-gate load on the new docs (in-scope backtick tokens) ---
# Same token shape as c2_pointers.sh, reused so the forecast matches the judge.
TOKENS=$(mktemp)
: > "$TOKENS"
while IFS= read -r rel; do
    doc="$ROOT/$rel"
    [ -f "$doc" ] || continue
    sed 's/\xe2\x80\xa6/~/g' "$doc" | awk '
        /^[ \t]*(```|~~~)/ { inblock = !inblock; next }
        inblock { next }
        {
            line = $0
            while (match(line, /`[^`]+`/)) {
                tok = substr(line, RSTART + 1, RLENGTH - 2)
                line = substr(line, RSTART + RLENGTH)
                if (length(tok) < 2) continue
                if (tok ~ /[^A-Za-z0-9_.\/:@~-]/) continue
                if (tok ~ /^-/) continue
                if (tok ~ /~/) {
                    p = tok; sub(/~.*/, "", p)
                    rest = tok; sub(/^[^~]*~/, "", rest)
                    if (length(p) < 7 || p ~ /[^0-9a-f]/) continue
                    if (rest != "" && rest ~ /[^0-9a-f]/) continue
                } else if (tok !~ /[A-Za-z]/) {
                    continue
                }
                print tok
            }
        }'
done < "$ADDED" | sort -u > "$TOKENS"
ntok=$(awk 'END{print NR+0}' "$TOKENS")
echo "--- pointer-gate forecast on NEW docs ---"
echo "unique in-scope backtick tokens introduced by experiment/**: $ntok"
echo "(these become resolve obligations: file / def / cert-literal / git"
echo " object / hex pin / reasoned exemption — else the extended gate reddens)"
echo

# --- forecast numeral-gate load on the new docs (bare multi-digit numerals) ---
NUMS=$(mktemp)
: > "$NUMS"
while IFS= read -r rel; do
    doc="$ROOT/$rel"
    [ -f "$doc" ] || continue
    # crude forecast: strip code fences + inline code + identifier words, then
    # find bare multi-digit runs. This is a forecast, not the judge.
    awk '
        /^[ \t]*(```|~~~)/ { inblock = !inblock; next }
        inblock { next }
        { line = $0
          gsub(/`[^`]*`/, " ", line)
          gsub(/[A-Za-z_][A-Za-z0-9_]*/, " ", line)   # drop identifier words
          n = split(line, a, /[^0-9]+/)
          for (i=1;i<=n;i++) if (length(a[i])>=2) print a[i]
        }' "$doc"
done < "$ADDED" | sort -u > "$NUMS"
nnum=$(awk 'END{print NR+0}' "$NUMS")
echo "--- numeral-gate forecast on NEW docs ---"
echo "distinct bare multi-digit numerals introduced by experiment/**: $nnum"
echo "(each becomes a value obligation: matches an instrument-derived value"
echo " or a reasoned exemption — else the extended gate reddens)"
echo

echo "=== MEANING-LEVEL CAVEAT (declared, norm 15) ==="
echo "This probe and the gates it forecasts are resolve/value-level. The"
echo "STRANGER-AUDIT row-8 slip (an unearned universal in a true-shaped"
echo "sentence) is MEANING-level and is NOT catchable by scope extension."
echo "S7c closes the 'never scanned' gap for the classes the gates CAN"
echo "check, and declares the residual meaning gap; it does not overclaim."
echo
echo "RESULT: PROBE COMPLETE (no gate modified; nothing asserted as passed)"

rm -f "$CUR" "$NEW" "$ADDED" "$TOKENS" "$NUMS"
exit 0
