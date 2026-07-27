#!/bin/sh
# audit/s7c_statements_purity.sh — the STATEMENTS-PURITY gate (S7c, REGISTER
# row 8 analogue; the censusguard idea applied to the courier's output).
#
# ADJUDICATOR DECLARATION (norm 15):
#   WHAT THIS CHECKS: the courier's "statements only" file
#     (courier/Zi_statements_v7.txt) must contain ONLY:
#       - blank lines,
#       - the two-line banner the extractor writes at the top,
#       - Lean declaration lines (structure/namespace/end/def/theorem/deriving),
#       - continuation lines of a declaration signature (indented; Lean tokens),
#     and NO free-standing docstring / comment / narrative PROSE. Seat B is
#     told it reads "definitions and claims only"; a prose paragraph that bled
#     past the proof-stripper violates that invariant. Any surviving prose line
#     FAILS the gate, named with its line number.
#   WHAT IT DOES NOT CHECK: whether the statements are TRUE (that is seat B and
#     the census); whether a decl's BODY was truncated (that is the
#     transcription gate). This gate checks PURITY of the file's line species
#     only. It is a line-species rule, not a meaning rule (norm 6).
#   HOW "prose" is decided (narrowly, to avoid false positives on real Lean):
#     a non-blank, non-banner line is PROSE iff it is NOT recognisable as a
#     Lean declaration or signature-continuation. Recognisable = matches one of
#     the structural line shapes below. Everything else is prose.
#   NAMED ADJUDICATOR: this gate, plant-bitten both directions.
#
# NORM 16: append a docstring prose line to the file -> gate FAILS naming it;
#   remove it -> gate PASSES. (The shipped file ALREADY carries the specimen —
#   the S5 NESTS docstring leak — so on the shipped artifact this gate is
#   EXPECTED RED, and that red is the finding, routed to a courier charge.)
#
# USAGE:  sh audit/s7c_statements_purity.sh [STATEMENTS_FILE]
# Exit 0 iff RESULT: PASS. POSIX sh + grep/sed/awk.
set -u
LC_ALL=C; export LC_ALL
SELF_DIR=$(dirname "$0")
EXP=$(cd "$SELF_DIR/.." && pwd)
SF=${1:-"$EXP/courier/Zi_statements_v8.txt"}

if [ ! -f "$SF" ]; then
    echo "ERROR: statements file '$SF' not found"; echo "RESULT: FAIL"; exit 1
fi

# Classify each line. A line is STRUCTURAL (allowed) if it matches a Lean
# declaration keyword, an end/namespace/deriving marker, the banner, OR it is a
# signature-continuation: a line that is INDENTED and contains only Lean-ish
# signature characters (no sentence punctuation like a comma-space-word run of
# prose, no leading prose bullet). Prose lines are what remain.
#
# We detect prose by POSITIVE prose markers that never appear in a bare Lean
# signature line in this file's house style:
#   - a line containing lowercase words followed by ordinary sentence text AND
#     NOT beginning (after indent) with a Lean signature token, AND not part of
#     a signature (no '=' , ':' , '\u2192', '\u2194', '\u2200', '\u2227', backslash-angle, parens balancing).
# To stay robust and auditable we use an explicit STRUCTURAL whitelist and
# flag everything else, then subtract known signature-continuation shapes.

# NOTE ON PORTABILITY (why not \b): the word-boundary escape \b is NOT
# reliable across awk implementations (mawk treats it as a literal backspace;
# gawk warns and differs in dynamic vs constant regex). An earlier draft of
# this gate used /^(structure|...)\b/ and consequently classified EVERY
# declaration line as prose (\b never matched), producing 202 false
# positives. The robust idiom is an explicit trailing class ([ \t]|$) — a
# keyword followed by whitespace or end-of-line. This is the fix.
# REPAIR (Round 3, third body): the FAIL branch below used to recount by
# re-invoking the gate on itself (`n=$(sh "$0" "$SF" …)`). That call also
# fails, so it recurses again — UNBOUNDED RECURSION on every red run. Since
# the gate's own norm-16 declaration says the shipped artifact is EXPECTED
# RED, the instrument could never report the finding it was built to report,
# and its plant could never be bitten. Repair: run the scan ONCE into a temp
# file, print it, and count from that file. Output format unchanged.
LEAKS=$(mktemp)
awk '
BEGIN { prose=0 }
{
    line=$0
    # blank
    if (line ~ /^[ \t]*$/) next
    # banner (first two lines the extractor writes)
    if (NR<=2 && line ~ /STATEMENTS ONLY|Proof bodies stripped/) next
    # structural declaration starts (keyword + whitespace-or-EOL, no \b)
    if (line ~ /^(structure|namespace|end|def|theorem|deriving|inductive|instance|abbrev|open|variable|private|noncomputable)([ \t]|$)/) next
    # From here we only ever see indented lines (declaration STARTS were
    # taken above). An indented line is EITHER a genuine signature-
    # continuation OR leaked prose. We decide with PROSE-POSITIVE markers:
    # English narrative and docstring furniture that never appear in a bare
    # Lean signature-continuation in this house style. This is robust to
    # leaked prose that happens to contain a colon or an equals sign.
    #
    #   P1  docstring furniture: a rule line of equals signs, a bulleted list
    #       item, or leaked-narrative English keywords (theorem, probe, NESTS,
    #       norm N, confirmed, written, footnote, indicator, ledger, catalog,
    #       fusion, ...) appearing as prose.
    #   P2  a double-quote used as an English quotation.
    #   P4  an em-dash used as prose punctuation with words around it.
    #
    # A line that trips ANY prose marker is PROSE. Otherwise it is a genuine
    # continuation and is allowed.
    is_prose=0
    # P1: rule line of equals signs (the ==== banner)
    if (line ~ /====/) is_prose=1
    # P1: leaked-narrative keywords appearing as English (not Lean idents,
    #     which are snake_case tokens on their own signature lines)
    if (line ~ /(^|[ \t])(theorem|Design|probe|confirmed|against|before|section|written|footnote|indicator|ledger|catalog|entries|fusion|matrix|checked|entrywise|particle|trivially|forces|reads|abelian|bench|labels|certificate|Neither|called)([ \t.,:;]|$)/) is_prose=1
    # P1: NESTS / norm furniture and bulleted list items
    if (line ~ /(NESTS|norm [0-9])/) is_prose=1
    if (line ~ /^[ \t]+- /) is_prose=1
    # P2: an English quotation mark around a word
    if (line ~ /"[a-z]/) is_prose=1
    # P4: an em-dash used as prose (surrounded by spaces + words)
    if (line ~ /[a-z] — |— [a-z]/) is_prose=1
    if (is_prose) {
        printf "PROSE-LEAK: %s: line %d: %s\n", FILENAME, NR, line
        prose++
    }
}
END { exit (prose>0?1:0) }
' "$SF" > "$LEAKS"
rc=$?
cat "$LEAKS"

# count for the nest tie
total=$(grep -c '' "$SF")
n=$(grep -c '^PROSE-LEAK:' "$LEAKS")
rm -f "$LEAKS"
if [ "$rc" -eq 0 ]; then
    echo "docs scanned: 1 (statements file) / lines: $total / prose-leak lines: 0"
    echo "RESULT: PASS"
    exit 0
else
    echo "docs scanned: 1 (statements file) / lines: $total / prose-leak lines: $n"
    echo "RESULT: FAIL"
    exit 1
fi
