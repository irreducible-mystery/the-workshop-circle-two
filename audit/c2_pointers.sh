#!/bin/sh
# audit/c2_pointers.sh — the pointer gate (Circle Two port of Circle One's
# pointers gate; REGISTER row 8 housekeeping, chartered for round 2).
#
# CONTRACT
#   Every backtick-quoted pointer token in the repo's prose documents must
#   resolve to something this repo (or its exemption record) knows:
#     (a) a file or directory path, as given relative to the repo root;
#     (b) a function/def name defined in floor/*.py or audit/*.py;
#     (b2) a Lean declaration in lean/*.lean -- theorem/def/abbrev/structure/
#         inductive/instance names and structure fields, accepted bare or
#         namespace-qualified (`mul_comm`, `Zi.mul`, `GZ.re`). Harvested from
#         the sources at run time, never hardcoded, so a new theorem is
#         citable the moment it compiles. Added when the Lean wing landed.
#     (c) an identifier appearing literally (word-bounded) in
#         audit/c2_gift_certificates.py — check names, env knobs;
#     (d) a git object this repo knows: 7-40 char hex tokens are tried with
#         `git cat-file -e` (abbreviated commit ids count);
#     (e) a bare filename (no slash) that exists somewhere in the tree
#         (.git and __pycache__ excluded);
#     (f/g) an entry in the exemptions file beside this script,
#         c2_pointers_exempt.txt — one entry per line, <token><TAB><reason>,
#         reason MANDATORY (this gate exits 1 on any reasonless line).
#         The circle-one artifact whitelist (sealed-record names such as
#         HANDOFF.md, CLOSING.md, axioms.sh) lives there, each carrying the
#         reason "circle-one artifact, lives in the sealed record".
#   Elided pins (hex prefix + ellipsis, e.g. `fb3a1809…` or `fb3a1809…8501b6`)
#   count as pin references: the prefix is resolved against git objects (d)
#   and, by prefix match, against hex entries in the exemptions file
#   (recorded artifact SHA-256 pins and courier-side commit pins).
#
# DOCS LIST
#   Enumerated from a glob at run time so new letters are covered
#   automatically, front doors included:
#     README.md CHARTER.md NORMS.md REGISTER.md ROUND1.md letters/*.md
#
# IN-SCOPE TOKEN SHAPE (defined narrowly; everything else is a code
# fragment, not a pointer, and belongs to other gates):
#   - text between single backticks on a line NOT inside a fenced code
#     block (``` / ~~~ fences are stripped before scanning);
#   - length >= 2 (single characters are bound variables, not pointers);
#   - no whitespace, and only the characters [A-Za-z0-9_./:@-] plus at
#     most one ellipsis (…) marking an elided hex pin;
#   - does not begin with '-' (command-line flags are code fragments);
#   - contains at least one letter, or is an elided/whole hex pin of
#     >= 7 hex chars (pure numerals are the numerals gate's territory);
#   - tokens beginning with '/' (machine-local absolute paths) are NOT
#     probed against the local filesystem — they must be exempted, so the
#     gate's verdict never depends on state outside the repo.
#
# OUTPUT
#   One "UNRESOLVED: <doc>: `<token>`" line per dangling pointer (per
#   document), then a summary whose counts tie to their nests:
#     docs scanned / in-scope pointer occurrences (doc x token pairs) /
#     unique tokens / unresolved occurrences,
#   then the machine-readable verdict line:  RESULT: PASS  or  RESULT: FAIL
#   Exit 0 iff RESULT: PASS.
#
# NORM 16
#   Bitten before trusted. Two plants, because this gate has two ways to be
#   wrong: append to any scanned document a line citing `phantom_bench.py`
#   (a dangling path -> must FAIL), and a line citing `Zi.no_such_theorem`
#   (a well-formed but non-existent Lean name -> must also FAIL, proving
#   rule (b2) resolves real declarations rather than anything dotted).
#   Restore both, confirm PASS. An alarm you have not seen fire is not an
#   alarm.
#
# USAGE:  sh audit/c2_pointers.sh [REPO_ROOT]      (default ".")
# Runs in well under 15 s. POSIX sh + grep/sed/awk/sort only.

set -u
LC_ALL=C
export LC_ALL

ROOT=${1:-.}
SELF_DIR=$(dirname "$0")
EXEMPT="$SELF_DIR/c2_pointers_exempt.txt"
TAB=$(printf '\t')

fail=0

if [ ! -d "$ROOT" ]; then
    echo "ERROR: repo root '$ROOT' is not a directory"
    echo "RESULT: FAIL"
    exit 1
fi

TMP="${TMPDIR:-/tmp}/c2ptr.$$"
mkdir "$TMP" || exit 1
trap 'rm -rf "$TMP"' 0

# ---------------------------------------------------------------- exemptions
# Format: <token><TAB><reason>. Blank lines and #-comments allowed.
# A line whose reason is missing or blank is itself a gate failure.
EXTOK="$TMP/extok"          # exact-match exemption tokens
EXHEX="$TMP/exhex"          # hex exemption tokens (artifact/commit pins)
: > "$EXTOK"; : > "$EXHEX"
if [ -f "$EXEMPT" ]; then
    lineno=0
    while IFS= read -r line || [ -n "$line" ]; do
        lineno=$((lineno + 1))
        case $line in ''|'#'*) continue ;; esac
        tok=${line%%"$TAB"*}
        reason=${line#*"$TAB"}
        if [ "$reason" = "$line" ]; then
            echo "EXEMPT-FORMAT: $EXEMPT line $lineno: no <TAB>reason on entry '$line'"
            fail=1
            continue
        fi
        case $reason in
            *[!\ $TAB]*) : ;;                       # reason has substance
            *) echo "EXEMPT-FORMAT: $EXEMPT line $lineno: empty reason for token '$tok'"
               fail=1
               continue ;;
        esac
        printf '%s\n' "$tok" >> "$EXTOK"
        # pure-hex entries of >=7 chars also serve as pin prefixes
        case $tok in
            *[!0-9a-f]*) : ;;
            ???????*) printf '%s\n' "$tok" >> "$EXHEX" ;;
        esac
    done < "$EXEMPT"
else
    echo "NOTE: no exemptions file at $EXEMPT (running with an empty list)"
fi

# ---------------------------------------------------------------- DOCS list
DOCLIST="$TMP/docs"
: > "$DOCLIST"
# r2 quarantine-review fix: docs are DISCOVERED, not enumerated — every
# top-level *.md and every *.md under letters/ (recursive), so a future
# ROUND2.md or PROOFS.md is scanned the day it lands instead of silently
# skipped.  floor/*.md is inherited C1 material, out of scope by design
# (class 1/6 per REGISTER).
for f in "$ROOT"/*.md; do
    [ -f "$f" ] && printf '%s\n' "$f" >> "$DOCLIST"
done
find "$ROOT/letters" -name '*.md' -print 2>/dev/null | sort >> "$DOCLIST"
ndocs=$(awk 'END{print NR}' "$DOCLIST")
if [ "$ndocs" -eq 0 ]; then
    echo "ERROR: no prose documents found under $ROOT"
    echo "RESULT: FAIL"
    exit 1
fi

# ------------------------------------------------- file inventory (for (a),(e))
# Basenames of everything in the tree, .git and __pycache__ pruned.
BASENAMES="$TMP/basenames"
find "$ROOT" \( -name .git -o -name __pycache__ \) -prune -o -print 2>/dev/null \
    | awk -F/ 'NF { print $NF }' | sort -u > "$BASENAMES"

# ------------------------------------- extract in-scope tokens from the docs
# Output: <doc-relative-path><TAB><token>   (ellipsis already canonized to ~)
PAIRS="$TMP/pairs"
: > "$PAIRS"
while IFS= read -r doc; do
    rel=${doc#"$ROOT"/}
    sed 's/\xe2\x80\xa6/~/g' "$doc" | awk -v doc="$rel" '
        /^[ \t]*(```|~~~)/ { inblock = !inblock; next }
        inblock { next }
        {
            line = $0
            while (match(line, /`[^`]+`/)) {
                tok = substr(line, RSTART + 1, RLENGTH - 2)
                line = substr(line, RSTART + RLENGTH)
                # ---- in-scope shape (see header) ----
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
                printf "%s\t%s\n", doc, tok
            }
        }' >> "$PAIRS"
done < "$DOCLIST"

sort -u "$PAIRS" > "$PAIRS.u"
npairs=$(awk 'END{print NR}' "$PAIRS.u")
cut -f2 "$PAIRS.u" | sort -u > "$TMP/tokens"
ntok=$(awk 'END{print NR}' "$TMP/tokens")

# --------------------------------------------------------------- resolution
CERT="$ROOT/audit/c2_gift_certificates.py"
GITOK=0
git -C "$ROOT" rev-parse --git-dir >/dev/null 2>&1 && GITOK=1

# (b2) Lean declaration names in lean/*.lean, bare and namespace-qualified.
# Added when the Lean wing landed (S1): a prose file that cites a theorem by
# name is pointing at a real declaration, and the gate must be able to say so
# rather than demanding an exemption per theorem. Harvested, never hardcoded.
LEANDEFS="$TMP/leandefs"
: > "$LEANDEFS"
for lf in "$ROOT"/lean/*.lean; do
    [ -f "$lf" ] || continue
    # Namespace-AWARE: an earlier version cross-produced every declaration
    # against every namespace in the file, so in a two-namespace file `A.two`
    # resolved even though `two` lived in B. One namespace hid the bug; the
    # adversarial audit found it anyway. Now the scanner tracks the namespace
    # stack, and a name resolves only under the namespace it is actually in.
    awk '
      function emit(n) { if (n != "") { print n; if (nsdepth > 0) print prefix "." n } }
      { line = $0
        sub(/--.*/, "", line)
        if (line ~ /^[ \t]*namespace[ \t]+/) {
          nm = line; sub(/^[ \t]*namespace[ \t]+/, "", nm); sub(/[ \t].*/, "", nm)
          nsdepth++; stack[nsdepth] = nm
          prefix = ""
          for (k = 1; k <= nsdepth; k++) prefix = (k == 1 ? stack[k] : prefix "." stack[k])
          next }
        if (line ~ /^[ \t]*end[ \t]+/) {
          if (nsdepth > 0) nsdepth--
          prefix = ""
          for (k = 1; k <= nsdepth; k++) prefix = (k == 1 ? stack[k] : prefix "." stack[k])
          next }
        if (line ~ /^[ \t]*(@\[[^]]*\][ \t]*)*(private[ \t]+|protected[ \t]+|nonrec[ \t]+)*(theorem|def|abbrev|structure|inductive|instance)[ \t]+/) {
          d = line
          sub(/^[ \t]*(@\[[^]]*\][ \t]*)*(private[ \t]+|protected[ \t]+|nonrec[ \t]+)*(theorem|def|abbrev|structure|inductive|instance)[ \t]+/, "", d)
          sub(/[^A-Za-z0-9_'"'"'].*/, "", d)
          emit(d)
          if (line ~ /^[ \t]*structure[ \t]+/) { instruct = 1; sname = d } else { instruct = 0 }
          next }
        if (instruct && line ~ /^[ \t]+[A-Za-z_][A-Za-z0-9_]*[ \t]*:/) {
          f = line; sub(/^[ \t]+/, "", f); sub(/[ \t]*:.*/, "", f)
          if (f != "") { emit(f); emit(sname "." f) }
          next }
        if (instruct && line !~ /^[ \t]/ && line !~ /^[ \t]*$/) { instruct = 0 }
      }' "$lf" >> "$LEANDEFS"
done
sort -u "$LEANDEFS" -o "$LEANDEFS" 2>/dev/null || true

UNTOK="$TMP/untok"   # unresolved unique tokens
: > "$UNTOK"
while IFS= read -r tok; do
    # (g)/(f) exact exemption match (checked against the ~-canonized form;
    # exemption entries are written without the ellipsis character)
    if grep -qxF -- "$tok" "$EXTOK"; then continue; fi

    # elided or whole hex pin?
    pin=""
    case $tok in
        *~*) pin=${tok%%~*} ;;
        *[!0-9a-f]*) : ;;
        ???????*) pin=$tok ;;
    esac
    if [ -n "$pin" ]; then
        # (d) git object (7-40 hex chars, abbreviated ids count)
        if [ "$GITOK" -eq 1 ] && [ "${#pin}" -ge 7 ] && [ "${#pin}" -le 40 ] \
           && git -C "$ROOT" cat-file -e "$pin^{object}" 2>/dev/null; then
            continue
        fi
        # recorded artifact/commit pin: prefix match against hex exemptions
        if grep -q -- "^$pin" "$EXHEX" 2>/dev/null; then continue; fi
    fi

    # (a) path as given, relative to repo root (never machine-absolute)
    case $tok in
        /*) : ;;
        *)  if [ -e "$ROOT/$tok" ]; then continue; fi ;;
    esac

    # (e) bare filename anywhere in the tree
    case $tok in
        */*) : ;;
        *)  if grep -qxF -- "$tok" "$BASENAMES"; then continue; fi ;;
    esac

    # (b) def name in floor/*.py or audit/*.py, (b2) Lean declaration name in
    # lean/*.lean, (c) identifier in the certificate — identifier-shaped only
    case $tok in
        [A-Za-z_]*)
            if printf '%s\n' "$tok" | grep -qxE '[A-Za-z_][A-Za-z0-9_]*'; then
                if grep -qE "def[[:space:]]+$tok[[:space:]]*\(" \
                        "$ROOT"/floor/*.py "$ROOT"/audit/*.py 2>/dev/null; then
                    continue
                fi
                if [ -f "$CERT" ] && grep -qwF -- "$tok" "$CERT"; then
                    continue
                fi
            fi
            # (b2) accepts the dotted form too, so `Zi.mul` resolves
            if printf '%s\n' "$tok" | grep -qxE "[A-Za-z_][A-Za-z0-9_']*(\.[A-Za-z_][A-Za-z0-9_']*)*"; then
                if grep -qxF -- "$tok" "$LEANDEFS" 2>/dev/null; then
                    continue
                fi
            fi
            ;;
    esac

    printf '%s\n' "$tok" >> "$UNTOK"
done < "$TMP/tokens"

# --------------------------------------------------------------- report
nunres_occ=0
if [ -s "$UNTOK" ]; then
    fail=1
    # print every (doc, token) occurrence of an unresolved token
    while IFS="$TAB" read -r doc tok; do
        if grep -qxF -- "$tok" "$UNTOK"; then
            display=$(printf '%s\n' "$tok" | sed 's/~/…/g')
            echo "UNRESOLVED: $doc: \`$display\`"
            nunres_occ=$((nunres_occ + 1))
        fi
    done < "$PAIRS.u"
fi

echo "pointer gate: $ndocs docs scanned; $npairs in-scope pointer occurrences ($ntok unique tokens); $nunres_occ unresolved"
if [ "$fail" -eq 0 ]; then
    echo "RESULT: PASS"
    exit 0
else
    echo "RESULT: FAIL"
    exit 1
fi
