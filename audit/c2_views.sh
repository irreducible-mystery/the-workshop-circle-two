#!/bin/sh
# audit/c2_views.sh — the view renderer and its gate (REGISTER row 11).
#
# WHY THIS EXISTS
#   Four times in one round, a hand-typed count or scope claim went stale:
#   593/594, then 929/930; "twelve live instances" when there were
#   seventeen; and twice a boundary bullet that denied a section the same
#   file had just delivered — the second time inside the commit that
#   repaired the first. Every one of them was a number or a scope claim
#   typed by a hand after the file had already moved.
#
#   Circle One's law for exactly this: a count is a VIEW. It is rendered by
#   an instrument from the artifact, never typed beside it, and a gate
#   checks that the rendered view in the tree still matches the artifact.
#   Chartered by the builder in the S3 verification, crop #1.
#
# THE SECOND GATE, added later (REGISTER row 14)
#   The renderer above kills stale counts in the LEDGER. It did nothing for
#   the artifact's own prose, and that is where the largest stale count in
#   this tree lived: lean/Zi.lean's header spelled out the whole axiom
#   census — theorem total, axiom-free count, propext count, Quot.sound
#   count broken down by section — and every figure was stale. It survived
#   every instrument, because the numeral gate's territory is the DOCS
#   (top-level *.md and letters/) and this gate's territory was the
#   rendered view. The artifact's own prose was scanned by neither.
#
#   `censusguard` closes that gap, narrowly: in the COMMENT PROSE of
#   lean/Zi.lean, no bare multi-digit numeral may stand in a paragraph that
#   also uses census vocabulary (theorem/axiom/depend/propext/Quot.sound/
#   sorryAx/Classical.choice/census). The artifact may point at the census;
#   it may not restate it. That is norm 19 applied to the artifact rather
#   than to the record.
#
#   WHAT IT DOES NOT CHECK, declared per norm 15: it is a proximity rule,
#   not a meaning rule. A census figure written far from every census word
#   passes; a mathematical constant written next to the word "theorem"
#   fails and needs a labeled exemption. It also sees DIGITS only — the
#   spelled-out door is the numeral gate's row-8 boundary and is guarded
#   there, not here. (An earlier draft of this line said "row-9". Row 9 is
#   multi-seat workflow audits; the same miscitation stood in the numeral
#   gate's own header for several crates.)
#
# CONTRACT
#   render      : write VIEWS.md from the artifacts (default, no argument)
#   check       : re-render into a temp file and diff against the committed
#                 VIEWS.md; any drift prints the diff and exits 1. Also
#                 runs `censusguard`.
#   censusguard : the artifact-prose rule above, on its own.
#   The census figures need a Lean binary. Without one they are rendered as
#   "not measured (no Lean binary)" — an honest absence, never a stale
#   number carried over from a previous run.
#
# BOUNDARY
#   A view can only be as true as its extraction. This script counts
#   declarations by the same comment-stripped rule audit/c2_axioms.sh uses,
#   and if that rule is wrong the view is confidently wrong. It also cannot
#   know that a section HEADING is honest — only that the section exists
#   and how many theorems it holds. What it kills is staleness, not error.
#
# NORM 16
#   Bitten before trusted, both gates:
#     - edit one number in VIEWS.md and run `check` — it must print the
#       drift and exit 1; restore, and it must pass;
#     - write "115 theorems depend on propext" into lean/Zi.lean's header
#       and run `censusguard` — it must name the paragraph and exit 1;
#       remove it, and it must pass.
#
# EXEMPTIONS: audit/c2_censusguard_exempt.txt, one entry per line,
#   <token><TAB><reason>. An entry with no TAB-separated reason FAILS the
#   gate — an unlabeled exemption is an unlabeled number.
#
# USAGE
#   sh audit/c2_views.sh render
#   LEAN=/path/to/lean sh audit/c2_views.sh check
#   sh audit/c2_views.sh censusguard

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || {
    echo "c2_views: not a git repository" >&2; exit 2; }
cd "$ROOT" || exit 2

MODE=${1:-render}
LEANBIN=${LEAN:-lean}
SRC=lean/Zi.lean

[ -f "$SRC" ] || { echo "c2_views: no $SRC" >&2; exit 2; }

render_to () {
    out=$1
    # comment-stripped body, so prose mentioning "theorem" is never counted
    stripped=$(mktemp)
    awk '
      { line = $0; res = ""; i = 1; n = length(line)
        while (i <= n) {
          c = substr(line, i, 2)
          if (depth == 0 && c == "--") { break }
          if (c == "/-") { depth++; i += 2; continue }
          if (c == "-/") { if (depth > 0) depth--; i += 2; continue }
          if (depth == 0) { res = res substr(line, i, 1) }
          i++
        }
        print res }' "$SRC" > "$stripped"

    nthm=$(grep -cE '^[[:space:]]*(@\[[^]]*\][[:space:]]*)*(private[[:space:]]+|protected[[:space:]]+|nonrec[[:space:]]+)*theorem[[:space:]]' "$stripped")
    ndef=$(grep -cE '^[[:space:]]*def[[:space:]]' "$stripped")
    nlines=$(wc -l < "$SRC" | tr -d ' ')
    nlive=$(grep -cE '^theorem live_' "$SRC")
    nctl=$(grep -cE '^theorem control_' "$SRC")
    ndec=$(grep -c ':= by decide' "$SRC")
    nimp=$(grep -cE '^import ' "$SRC")
    srchash=$(sha256sum "$SRC" | cut -d' ' -f1)
    tchash=$(sha256sum lean/lean-toolchain 2>/dev/null | cut -d' ' -f1)

    {
      echo "# VIEWS — rendered, never typed"
      echo
      echo "*Generated by \`audit/c2_views.sh\`. Do not hand-edit: \`check\` will"
      echo "fail. Every number below is read off the artifact at render time,"
      echo "which is the whole point — four stale counts in one round is what"
      echo "bought this file (REGISTER row 11).*"
      echo
      echo '```'
      printf 'source            %s\n' "$SRC"
      printf 'sha256            %s\n' "$srchash"
      printf 'toolchain pin     %s\n' "$(cat lean/lean-toolchain 2>/dev/null)"
      printf 'toolchain sha256  %s\n' "$tchash"
      echo
      printf 'theorems          %s\n' "$nthm"
      printf 'definitions       %s\n' "$ndef"
      printf 'lines             %s\n' "$nlines"
      printf 'live instances    %s\n' "$nlive"
      printf 'control theorems  %s\n' "$nctl"
      printf 'decide-settled    %s\n' "$ndec"
      printf 'import lines      %s   (zero imports is the charter)\n' "$nimp"
      echo '```'
      echo
      echo "## Sections present, and what each holds"
      echo
      echo '```'
      awk '
        /^\/-! ## / {
          if (name != "") printf "%-56s %3d theorems\n", name, cnt
          name = $0
          sub(/^\/-! ## /, "", name)
          sub(/[ \t]*-\/[ \t]*$/, "", name)
          sub(/[ \t]*$/, "", name)
          cnt = 0
          next
        }
        /^theorem / { if (name != "") cnt++ }
        END { if (name != "") printf "%-56s %3d theorems\n", name, cnt }
      ' "$SRC"
      echo '```'
      echo
      # The boundary sentence is DERIVED rather than templated: the section
      # count and the last section name are interpolated, so the words change
      # when the artifact changes. An earlier version echoed a fixed sentence
      # and the delivery letter still called it rendered. Template prose living
      # in a rendered file is not a rendered claim; the builder audit caught the
      # self-description, and this is the repair.
      nsec=$(grep -c "^/-! ## " "$SRC")
      lastsec=$(grep "^/-! ## " "$SRC" | tail -1 | sed -e "s|^/-! ## ||" -e "s|[[:space:]]*-/[[:space:]]*$||")
      printf "**The boundary, derived from the inventory above:** this file proves\n"
      printf "the %s sections listed and nothing else. The last of them is\n" "$nsec"
      printf "\"%s\".\n" "$lastsec"
      printf "Anything absent from that list is not proved here.\n"
      echo
      printf "What the derivation can and cannot do, carried in from the\n"
      printf "boundary note of the renderer: it knows a section EXISTS and how\n"
      printf "many theorems it holds. It cannot know a section HEADING is honest.\n"
      printf "It kills staleness, not error.\n"
      echo
      echo "## The census"
      echo
      echo '```'
      if command -v "$LEANBIN" >/dev/null 2>&1; then
          LEAN="$LEANBIN" sh audit/c2_axioms.sh 2>/dev/null \
            | grep -E '^(Zi|TOTAL|sorryAx|Classical.choice|file)' \
            | sed 's/[[:space:]]*$//'
          nq=$(LEAN="$LEANBIN" sh audit/c2_axioms.sh 2>/dev/null | grep -c 'quot:')
          printf 'Quot.sound carriers %s   (each named in the census output)\n' "$nq"
      else
          echo "not measured (no Lean binary; set LEAN=/path/to/lean)"
      fi
      echo '```'
    } > "$out"
    rm -f "$stripped"
}

census_guard () {
    EX=audit/c2_censusguard_exempt.txt
    bad=0
    # (1) the artifact's COMMENT prose: the exact complement of the census
    #     script's comment-stripped body. Blank lines separate paragraphs.
    prose=$(mktemp)
    awk '
      BEGIN { depth = 0 }
      { line = $0; out = ""; i = 1; n = length(line)
        while (i <= n) {
          c = substr(line, i, 2)
          if (depth == 0 && c == "--") { out = out substr(line, i + 2); break }
          if (c == "/-") { depth++; i += 2; continue }
          if (c == "-/") { if (depth > 0) depth--; i += 2; continue }
          if (depth > 0) { out = out substr(line, i, 1) }
          i++
        }
        printf "%d\t%s\n", NR, out }' "$SRC" > "$prose"

    # (2) strip the structural contexts, exactly the numeral gate's list:
    #     code spans, quotations, version tokens, identifier words, line
    #     citations, and cross-references into frozen enumerations.
    stripped=$(mktemp)
    sed -e 's/`[^`]*`/ /g' -e 's/"[^"]*"/ /g' \
        -e 's/[vV][0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*/ /g' \
        -e 's/[0-9][0-9]*[A-Za-z_][A-Za-z0-9_]*/ /g' \
        -e 's/[A-Za-z_][A-Za-z0-9_]*[0-9][A-Za-z0-9_]*/ /g' \
        -e 's/[Ll]ines\{0,1\} [0-9][0-9]*/ /g' \
        -e 's/\([Nn]orm\|NORM\|[Rr]ow\|ROW\|[Ss]ection\|SECTION\|[Rr]ound\|ROUND\|[Cc]lass\|[Ii]tem\|[Ss]tep\|[Cc]rop\) [0-9][0-9]*/ /g' \
        -e 's/^\([0-9]*\)\t! \{0,1\}## [0-9][0-9]*\./\1\t/' \
        "$prose" > "$stripped"

    # (3) paragraph sweep: a blank comment line ends a paragraph. A
    #     paragraph carrying census vocabulary may carry no bare numeral.
    #     The reported token is "<preceding word> <numeral>", so that an
    #     exemption names a PHRASE and not a digit run: "nest 16" may be
    #     labeled without "16 theorems" inheriting the licence.
    hits=$(awk -F'\t' '
      function flush(  j, n, a) {
        if (kw && nfound > 0)
          for (j = 1; j <= nfound; j++) printf "%s\t%s\n", firstline, found[j]
        kw = 0; nfound = 0; firstline = 0
      }
      { body = $2
        if (body ~ /^[ \t]*$/) { flush(); next }
        if (firstline == 0) firstline = $1
        if (body ~ /theorem|axiom|depend|propext|Quot\.sound|sorryAx|Classical\.choice|census/) kw = 1
        rest = body
        while (match(rest, /[0-9][0-9]+/)) {
          num = substr(rest, RSTART, RLENGTH)
          before = substr(rest, 1, RSTART - 1)
          gsub(/[^A-Za-z ]/, " ", before)
          nb = split(before, bw, " ")
          key = (nb > 0 ? tolower(bw[nb]) " " num : num)
          found[++nfound] = key
          rest = substr(rest, RSTART + RLENGTH)
        }
      }
      END { flush() }' "$stripped")
    rm -f "$prose" "$stripped"

    if [ -f "$EX" ]; then
        if grep -vE '^[[:space:]]*(#|$)' "$EX" | grep -qv "$(printf '\t')"; then
            echo "  censusguard: an exemption line carries no TAB-separated reason." >&2
            bad=1
        fi
    fi

    echo "$hits" | while IFS="$(printf '\t')" read -r ln tok; do
        [ -n "$tok" ] || continue
        if [ -f "$EX" ] && grep -q "^$tok$(printf '\t')" "$EX"; then continue; fi
        printf '  %s:%s  bare numeral "%s" in a paragraph using census vocabulary\n' \
            "$SRC" "$ln" "$tok"
    done > "$WORKHITS"

    if [ -s "$WORKHITS" ]; then
        echo "c2_views: the artifact's own prose restates a census figure:"
        cat "$WORKHITS"
        echo "RESULT: FAIL -- point at VIEWS.md, or label the numeral in $EX."
        bad=1
    else
        echo "c2_views: the artifact's prose states no census figure.  PASS."
    fi
    rm -f "$WORKHITS"
    return $bad
}

WORKHITS=$(mktemp)

case $MODE in
  censusguard)
      census_guard; exit $? ;;
  render)
      render_to VIEWS.md
      echo "c2_views: rendered VIEWS.md from the artifacts."
      exit 0 ;;
  check)
      [ -f VIEWS.md ] || { echo "c2_views: VIEWS.md missing — run 'render'"; exit 1; }
      tmp=$(mktemp)
      render_to "$tmp"
      if diff -u VIEWS.md "$tmp" > /dev/null 2>&1; then
          rm -f "$tmp"
          echo "c2_views: the rendered view matches the artifacts.  PASS."
          census_guard || exit 1
          exit 0
      else
          echo "c2_views: VIEWS.md has DRIFTED from the artifacts:"
          diff -u VIEWS.md "$tmp" | head -40
          rm -f "$tmp"
          echo "RESULT: FAIL -- re-render (sh audit/c2_views.sh render), never hand-edit."
          exit 1
      fi ;;
  *)
      echo "c2_views: unknown mode '$MODE' (render | check)" >&2
      exit 2 ;;
esac
