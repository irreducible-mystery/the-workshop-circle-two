#!/bin/sh
# ---------------------------------------------------------------------------
# THE WORKSHOP -> CIRCLE TWO.  audit/c2_numerals.sh -- the numeral gate.
# Ported from Circle One's numerals.sh (round-8 graduated design): every
# BARE-ASSERTED multi-digit number in the ledger prose must be sourced from
# an instrument or carry a labeled exemption.
#
# ADJUDICATOR DECLARATION (norm 15, this artifact's own entry):
#   WHAT THIS CHECKS: every bare-asserted number with two or more digits in
#     the DOCS prose matches (a) a number derived from or appearing in an
#     instrument artifact of THIS tree -- the certificate's source
#     (audit/c2_gift_certificates.py, which carries the G6 cost table and
#     every certified count), the floor's rendered output
#     (floor/WELD_REPORT.txt), the bench count computed from run_all.py's
#     BENCHES list (29 at port time), and the certificate's PASS capacity
#     computed from its check() call sites (70 at port time) -- or
#     (b) a labeled exemption in audit/c2_numerals_exempt.txt.
#     A bare number matching neither FAILS the gate.
#   WHAT IT DOES NOT CHECK:
#     - single-digit numbers;
#     - whether a sourced number is the RIGHT one for its sentence: matching
#       is value-level, not meaning-level (Circle One's stated boundary --
#       a number can match an instrument value and still be miscited; that
#       is the audit loop's class, not this gate's).  In particular a value
#       that occurs in the certificate SOURCE (including its docstring's
#       historical "0.53") passes even where a fresh assertion of it would
#       be wrong;
#     - numbers inside inline `code`, fenced ``` blocks, or "double quotes"
#       (quotations -- discussing a value is not asserting it; Circle One's
#       graduation lesson: quoting history cannot defuse a fresh BARE count,
#       which still fails);
#     - spelled-out numbers ("sixteen specimens", "twenty-two seats");
#     - the STRUCTURAL contexts defined narrowly below.
#   STRUCTURAL CONTEXTS (class c), each defined narrowly and stripped
#   before extraction:
#     c1  inline code spans `...`   (stripped FIRST -- the imageCount_eq_32
#         lesson: identifiers are never read as counts)
#     c2  "double-quoted" spans     (quotations)
#     c3  ISO dates YYYY-MM-DD
#     c4  toolchain version tokens  vN.N[.N]   (e.g. v4.32.0)
#     c5  line-number citations     line/lines[- ]N   (C1's index-convention
#         rule makes these bench pointers, not counts)
#     c6  cross-reference citations into frozen enumerations:
#         norm/row/round/class/item/flag/step[s|es][- ]N[-N]
#         (the numbering is frozen by NORMS.md; "norm 13" is a pointer)
#     c7  markdown ordered-list markers at line start ("13. ...")
#     c8  identifier words mixing letters and digits (x86_64, sha256sum,
#         commit ids 32a6b0c/b8eea58, G1h, 1e-12) and the literal SHA-256
#   Anything surviving all of the above is BARE-ASSERTED prose and must be
#   sourced or exempt.  Commas inside numbers are merged (1,560 -> 1560);
#   digit runs are compared as strings, so 70/70 checks 70 twice and
#   0.527864 checks the run 527864.
#
# EXEMPTIONS: audit/c2_numerals_exempt.txt, beside this script.  One entry
# per line: <token><TAB><reason>.  A line with no TAB-separated reason FAILS
# the gate (exit 1) -- an unlabeled exemption is an unlabeled number.
# Unused entries are printed as NOTEs (reviewable, per the dead-entry lesson).
#
# Usage:  sh audit/c2_numerals.sh [REPO_ROOT]     (default ".")
# Exit:   0 iff every bare-asserted prose numeral is sourced or labeled
#         (machine-readable pass line: "RESULT: ... PASS.");  1 otherwise.
# ---------------------------------------------------------------------------
# NORM 16
#   Bitten before trusted: append to any scanned document a sentence
#   carrying a fresh bare numeral that no instrument produces (e.g.
#   "the floor ran 8675309 benches"), run this gate, watch it name the
#   document and exit 1; then restore and confirm PASS.
#
#   KNOWN BOUNDARY, and it has cost twice: this gate sees DIGITS only.
#   A spelled-out number ("thirty-one") is invisible to it, and that
#   boundary carried a real specimen in each of rounds 2's two halves.
#   Scored in REGISTER row 9; not fixed here, declared here.
#
set -u

ROOT="${1:-.}"
SELF_DIR=$(dirname "$0")
EXEMPT_FILE="$SELF_DIR/c2_numerals_exempt.txt"
CERT="$ROOT/audit/c2_gift_certificates.py"
WELD="$ROOT/floor/WELD_REPORT.txt"
RUNALL="$ROOT/floor/run_all.py"
WORK="${TMPDIR:-/tmp}/c2_numerals_$$"
mkdir -p "$WORK" || exit 1
trap 'rm -rf "$WORK"' EXIT

# The DOCS set: DISCOVERED at runtime (r2 quarantine-review fix) — every
# top-level *.md and every *.md under letters/ (recursive), so a future
# ROUND2.md or PROOFS.md is scanned the day it lands instead of silently
# skipped.  floor/*.md is inherited C1 material, out of scope by design.
DOCS=$(cd "$ROOT" 2>/dev/null && ls *.md 2>/dev/null)
LETTERS=$(cd "$ROOT" 2>/dev/null && find letters -name '*.md' 2>/dev/null | sort)

echo "=============================================================="
echo " C2 NUMERAL GATE -- bare-asserted numbers vs instrument values"
echo "=============================================================="
echo " checks:  bare-asserted multi-digit numbers in DOCS prose"
echo " allows:  code, \"quotations\", dates, versions, line/norm/row refs,"
echo "          identifiers; sourced or labeled numbers"
echo " GATE:    exit 1 on any bare-asserted numeral that is not sourced"
echo "=============================================================="

# ---------------------------------------------------------------------------
# 1. THE KNOWN SET -- numbers the instruments themselves carry or imply.
# ---------------------------------------------------------------------------
: > "$WORK/known.txt"

# (a) every digit run in the certificate's own source (G6 cost table, the
#     certified counts, the ranges) and in the floor's rendered WELD report.
#     Identifier words (letters+digits) are stripped first so a check NAME
#     is never read as a number; thousands-commas are merged.
harvest() {
  sed -e 's/[vV][0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*/ /g' \
      -e 's/[A-Za-z_][A-Za-z0-9_]*[0-9][A-Za-z0-9_]*/ /g' \
      -e 's/[0-9][0-9]*[A-Za-z_][A-Za-z0-9_]*/ /g' \
      -e 's/\([0-9]\),\([0-9][0-9][0-9]\)/\1\2/g' \
      -e 's/\([0-9]\),\([0-9][0-9][0-9]\)/\1\2/g' "$1" \
    | grep -oE '[0-9]{2,}'
}
n_cert=0; n_weld=0
if [ -f "$CERT" ]; then
  harvest "$CERT" > "$WORK/h_cert.txt"; n_cert=$(sort -u "$WORK/h_cert.txt" | wc -l | tr -d ' ')
  cat "$WORK/h_cert.txt" >> "$WORK/known.txt"
else
  echo "  NOTE: $CERT missing -- certificate numbers cannot be sourced"
fi
if [ -f "$WELD" ]; then
  harvest "$WELD" > "$WORK/h_weld.txt"; n_weld=$(sort -u "$WORK/h_weld.txt" | wc -l | tr -d ' ')
  cat "$WORK/h_weld.txt" >> "$WORK/known.txt"
else
  echo "  NOTE: $WELD missing -- bench-printed values cannot be sourced"
fi

# (b) the floor bench count, computed from the BENCHES list itself
#     (nest: one "(...)" entry per bench inside the list literal).
benches=""
if [ -f "$RUNALL" ]; then
  benches=$(awk '/^BENCHES = \[/{f=1;next} f&&/^\]/{exit} f&&/^[[:space:]]*\(/{n++} END{print n+0}' "$RUNALL")
  [ "$benches" -gt 0 ] 2>/dev/null && echo "$benches" >> "$WORK/known.txt"
fi

# (c) the certificate's PASS capacity, computed from its check() call sites
#     (nest: call sites, minus the except-branch `False, repr(e)` aliases
#     that fire only on failure, plus the G0 loop's per-bench multiplicity).
#     This needs a multi-line regex over the G0 block; python3 is the
#     chartered fallback for exactly this.
capacity=""
if [ -f "$CERT" ] && command -v python3 >/dev/null 2>&1; then
  capacity=$(python3 -c '
import re, sys
src = open(sys.argv[1]).read()
sites = re.findall(r"\bcheck\(\s*f?\"", src)
exc   = re.findall(r"\bcheck\(\s*f?\"[^\"]*\",\s*False,\s*repr\(e\)\)", src)
m = re.search(r"for bench, must in \[(.*?)\n\]:", src, re.S)
g0 = len(re.findall(r"\(\s*\"[^\"]+\.py\"", m.group(1))) if m else 0
print(len(sites) - len(exc) + (g0 - 1 if g0 else 0))' "$CERT" 2>/dev/null)
  case "$capacity" in *[!0-9]*|"") capacity="" ;; *) echo "$capacity" >> "$WORK/known.txt" ;; esac
fi
sort -u "$WORK/known.txt" -o "$WORK/known.txt"
echo "  known set: $(wc -l < "$WORK/known.txt" | tr -d ' ') values" \
     "($n_cert certificate-source, $n_weld weld-report," \
     "bench count=${benches:-UNDERIVED}, PASS capacity=${capacity:-UNDERIVED})"

# ---------------------------------------------------------------------------
# 2. THE EXEMPTION LIST -- <token><TAB><reason>; any entry missing its
#    reason fails the gate.
# ---------------------------------------------------------------------------
: > "$WORK/exempt.txt"
if [ -f "$EXEMPT_FILE" ]; then
  if ! awk -F'\t' -v OUT="$WORK/exempt.txt" '
    /^[[:space:]]*#/ || /^[[:space:]]*$/ { next }
    NF < 2 || $1 !~ /^[0-9]+$/ || $2 ~ /^[[:space:]]*$/ {
      printf("  MALFORMED EXEMPTION line %d: %s\n", NR, $0); bad = 1; next }
    { print $1 >> OUT }
    END { exit bad }' "$EXEMPT_FILE"; then
    echo "RESULT: exemption list malformed -- every entry needs <token><TAB><reason>.  FAIL (gate)."
    exit 1
  fi
  sort -u "$WORK/exempt.txt" -o "$WORK/exempt.txt"
  echo "  exemptions: $(wc -l < "$WORK/exempt.txt" | tr -d ' ') labeled entries ($EXEMPT_FILE)"
else
  echo "  NOTE: no exemption file at $EXEMPT_FILE -- running with an empty list"
fi

# ---------------------------------------------------------------------------
# 3. THE SCAN -- strip the structural contexts, extract what remains,
#    demand a source or a label for every multi-digit run.
# ---------------------------------------------------------------------------
DOCFILES=""
for d in $DOCS $LETTERS; do
  [ -f "$ROOT/$d" ] && DOCFILES="$DOCFILES $ROOT/$d"
done

awk -v KNOWN="$WORK/known.txt" -v EXEMPT="$WORK/exempt.txt" -v ROOT="$ROOT/" '
BEGIN {
  while ((getline l < KNOWN)  > 0) known[l] = 1
  while ((getline l < EXEMPT) > 0) exempt[l] = 1
  fail = 0
}
function report(f) {
  if (f != "") {
    sub("^" ROOT, "", f)
    printf("  %-34s %3d bare-asserted, %d unsourced\n", f, n_doc, bad_doc)
  }
}
FNR == 1 { report(prev); prev = FILENAME; code = 0; n_doc = 0; bad_doc = 0 }
/^[[:space:]]*```/ { code = !code; next }
code { next }
{
  line = $0
  sub(/^[[:space:]]*[0-9]+\.[[:space:]]/, " ", line)               # c7 list markers
  gsub(/`[^`]*`/, " ", line)                                       # c1 code spans FIRST
  gsub(/"[^"]*"/, " ", line)                                       # c2 quotations
  gsub(/[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]/, " ", line)    # c3 ISO dates
  gsub(/[vV][0-9]+\.[0-9]+(\.[0-9]+)?/, " ", line)                 # c4 version tokens
  gsub(/[Ll]ines?[- ][0-9]+((-|\xe2\x80\x93)[0-9]+)?/, " ", line)   # c5 line citations
  gsub(/[Nn]orms?[- #]*[0-9]+((-|\xe2\x80\x93)[0-9]+)?/, " ", line) # c6 enumeration refs
  gsub(/[Rr]ows?[- #]*[0-9]+((-|\xe2\x80\x93)[0-9]+)?/, " ", line)
  gsub(/[Rr]ounds?[- #]*[0-9]+((-|\xe2\x80\x93)[0-9]+)?/, " ", line)
  gsub(/[Cc]lass(es)?[- #]*[0-9]+((-|\xe2\x80\x93)[0-9]+)?/, " ", line)
  gsub(/[Ii]tems?[- #]*[0-9]+((-|\xe2\x80\x93)[0-9]+)?/, " ", line)
  gsub(/[Ff]lags?[- #]*[0-9]+((-|\xe2\x80\x93)[0-9]+)?/, " ", line)
  gsub(/[Ss]teps?[- #]*[0-9]+((-|\xe2\x80\x93)[0-9]+)?/, " ", line)
  gsub(/SHA-256|sha-256/, " ", line)                               # c8 algorithm name
  gsub(/[A-Za-z_][A-Za-z0-9_]*[0-9][A-Za-z0-9_]*/, " ", line)      # c8 identifiers
  gsub(/[0-9]+[A-Za-z_][A-Za-z0-9_]*/, " ", line)                  #    (digit-first)
  # merge thousands-commas: 1,560 -> 1560 (digit,DDD not followed by a digit)
  out = ""
  while (match(line, /[0-9],[0-9][0-9][0-9]/)) {
    nxt = substr(line, RSTART + RLENGTH, 1)
    if (nxt ~ /[0-9]/) { out = out substr(line, 1, RSTART); line = substr(line, RSTART + 1) }
    else { seg = substr(line, RSTART, RLENGTH); gsub(/,/, "", seg)
           out = out substr(line, 1, RSTART - 1) seg; line = substr(line, RSTART + RLENGTH) }
  }
  line = out line
  # extract every remaining run of 2+ digits
  while (match(line, /[0-9][0-9]+/)) {
    tok = substr(line, RSTART, RLENGTH); line = substr(line, RSTART + RLENGTH)
    n_doc++; n_total++
    fn = FILENAME; sub("^" ROOT, "", fn)
    if (tok in known) { }
    else if (tok in exempt) { used[tok] = 1 }
    else {
      printf("  UNSOURCED %-16s %s:%d  (bare-asserted; matches no instrument value, no exemption)\n", \
             tok, fn, FNR)
      bad_doc++; flagged++; fail = 1
    }
  }
}
END {
  report(prev)
  printf("  TOTAL %d bare-asserted numeral(s) across %d docs, %d unsourced\n", \
         n_total + 0, ARGC - 1, flagged + 0)
  for (t in exempt) if (!(t in used))
    printf("  NOTE: exemption entry never matched this run: %s (review it)\n", t)
  if (fail) {
    print ""
    print "RESULT: " flagged " bare-asserted numeral(s) unsourced.  FAIL (gate)."
    print "        Each is a bare number matching no instrument-derived value and no"
    print "        labeled exemption.  Source it from an instrument, quote it (inside"
    print "        \"...\") if it is a quotation, or add <token>\tTAB<reason> to"
    print "        audit/c2_numerals_exempt.txt."
    exit 1
  }
  print ""
  print "RESULT: every bare-asserted prose numeral is sourced or labeled.  PASS."
  exit 0
}' $DOCFILES
exit $?
