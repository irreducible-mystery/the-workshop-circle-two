#!/bin/sh
# bite.sh — norm 16 for the two gates beside it. Runs the plants and ASSERTS.
#
#   The plants are MATERIALIZED into a scratch git tree rather than committed
#   beside the gates, and that is a deliberate choice worth its sentence:
#   a resident self-pin plant would make `norm21_selfpin.sh` permanently RED on
#   this repository, and the only cures for that are an exclusion list — which
#   is SR43's species, the hazard this record has named four times — or a gate
#   that lies. So the plant is reproducible instead of resident. Run this and
#   the bite happens in front of you; nothing is taken on the author's word.
#
#   USAGE:  sh autopsy-evidence/c4-prover/plants/bite.sh
#           exit 0 = every plant produced its expected verdict.
#           exit 1 = a gate failed its own bite. Do not trust its greens.

set -e
HERE=$(cd "$(dirname "$0")" && pwd)
GATE_PIN="$HERE/../norm21_selfpin.sh"
GATE_HOOK="$HERE/../hookcheck.sh"
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT
FAIL=0

expect () { # expect <label> <wanted-exit> <got-exit>
    if [ "$2" = "$3" ]; then printf '  %-46s exit %s  OK\n' "$1" "$3"
    else printf '  %-46s exit %s  WANTED %s  <-- FAILED\n' "$1" "$3" "$2"; FAIL=1; fi
}

cd "$WORK"
git init -q . && git config user.email b@b && git config user.name b

echo "PLANTS FOR norm21_selfpin.sh"

# P1 -- a file carrying its own basename against a 64-hex value. UNSATISFIABLE.
#       This is rate/README.md's exact shape. MUST go RED.
{ echo "# a manifest"; echo '```'
  echo "0000000000000000000000000000000000000000000000000000000000000000  P1.md"
  echo '```'; } > P1.md

# P2 -- a file pinning ANOTHER file. Ordinary, correct practice. MUST stay GREEN.
{ echo "# a manifest"; echo '```'
  echo "1111111111111111111111111111111111111111111111111111111111111111  other.lean"
  echo '```'; } > P2.md
echo "content" > other.lean

# P3 -- a bare 64-hex with no filename token, e.g. a commit pin in prose.
#       MUST stay GREEN, or every letter in the record goes red.
echo "committed at 2222222222222222222222222222222222222222222222222222222222222222 and sealed" > P3.md

# P4 -- the miraculous case: the row is TRUE. Still reported, because a true
#       self-pin means someone found a preimage or the file was not re-saved,
#       and both are worth a human's attention. MUST go RED (reported).
printf 'placeholder\n' > P4.md
H=$(sha256sum P4.md | cut -d' ' -f1)
printf '%s  P4.md\n' "$H" > P4.md   # now the row is stale by construction

git add -A && git commit -qm plants

set +e
sh "$GATE_PIN" "$WORK" > "$WORK/out.pin" 2>&1; E=$?
set -e
grep -q 'SELF-PIN in P1.md' "$WORK/out.pin" && P1=1 || P1=0
grep -q 'P2.md' "$WORK/out.pin" && P2=1 || P2=0
grep -q 'P3.md' "$WORK/out.pin" && P3=1 || P3=0
grep -q 'SELF-PIN in P4.md' "$WORK/out.pin" && P4=1 || P4=0

expect "P1 self-pin present  -> gate RED" 1 "$E"
expect "P1 named in output" 1 "$P1"
expect "P2 pins another file -> NOT flagged" 0 "$P2"
expect "P3 bare hex in prose -> NOT flagged" 0 "$P3"
# P4 was materialized by the first version of this bite and NOT asserted on --
# a plant planted and never read, which is this record's own recurring species
# committed inside an instrument built to catch it. Caught on the first run and
# fixed here rather than quietly dropped.
expect "P4 self-pin stale by construction -> flagged" 1 "$P4"

# Negative control: remove the only offending file, gate must go GREEN.
rm P1.md P4.md && git add -A && git commit -qm drop
set +e; sh "$GATE_PIN" "$WORK" >/dev/null 2>&1; E2=$?; set -e
expect "no self-pins        -> gate GREEN" 0 "$E2"

echo ""
echo "PLANTS FOR hookcheck.sh"

mkdir -p .githooks && printf '#!/bin/sh\nexit 0\n' > .githooks/pre-commit
git add -A && git commit -qm hook

git config --unset core.hooksPath 2>/dev/null || true
set +e; sh "$GATE_HOOK" "$WORK" >/dev/null 2>&1; H1=$?; set -e
expect "hook in tree, hooksPath UNSET -> RED" 1 "$H1"

git config core.hooksPath .githooks
set +e; sh "$GATE_HOOK" "$WORK" >/dev/null 2>&1; H2=$?; set -e
expect "hook in tree, hooksPath SET   -> GREEN" 0 "$H2"

git config core.hooksPath .wronghooks
set +e; sh "$GATE_HOOK" "$WORK" >/dev/null 2>&1; H3=$?; set -e
expect "hooksPath points elsewhere    -> RED" 1 "$H3"

rm -rf .githooks && git add -A && git commit -qm nohook
git config --unset core.hooksPath 2>/dev/null || true
set +e; sh "$GATE_HOOK" "$WORK" >/dev/null 2>&1; H4=$?; set -e
expect "no hook shipped               -> GREEN (nothing to wire)" 0 "$H4"

echo ""
echo "PLANTS FOR verdict_exit.sh"
GATE_VERDICT="$HERE/../verdict_exit.sh"

# V1 -- independent_math_check.py's exact shape: verdict is a print, exit is a
#       constant. MUST go RED.
cat > V1.py <<'EOF'
ok = lambda name, cond: print(("PASS " if cond else "FAIL ") + name)
ok("two plus two", 2 + 2 == 5)
print("All independent checks complete.")
EOF

# V2 -- same verdicts, but an assert can fail the process. MUST stay GREEN.
cat > V2.py <<'EOF'
print("PASS arithmetic")
assert 2 + 2 == 4
EOF

# V3 -- same verdicts, sys.exit escape. MUST stay GREEN.
cat > V3.py <<'EOF'
import sys
bad = 0
print("FAIL something" if bad else "PASS something")
sys.exit(1 if bad else 0)
EOF

# V4 -- no verdict vocabulary at all; a plain script. MUST stay GREEN.
cat > V4.py <<'EOF'
print("the sum is", 1 + 1)
EOF

git add -A && git commit -qm verdicts
set +e; sh "$GATE_VERDICT" "$WORK" > "$WORK/out.v" 2>&1; V=$?; set -e
grep -q 'V1.py' "$WORK/out.v" && v1=1 || v1=0
grep -q 'V2.py' "$WORK/out.v" && v2=1 || v2=0
grep -q 'V3.py' "$WORK/out.v" && v3=1 || v3=0
grep -q 'V4.py' "$WORK/out.v" && v4=1 || v4=0
expect "V1 print-only verdict         -> gate RED" 1 "$V"
expect "V1 named in output" 1 "$v1"
expect "V2 has assert                 -> NOT flagged" 0 "$v2"
expect "V3 has sys.exit               -> NOT flagged" 0 "$v3"
expect "V4 no verdict vocabulary      -> NOT flagged" 0 "$v4"

rm V1.py && git add -A && git commit -qm dropv1
set +e; sh "$GATE_VERDICT" "$WORK" >/dev/null 2>&1; V2E=$?; set -e
expect "V1 removed                    -> gate GREEN" 0 "$V2E"

echo ""
if [ "$FAIL" -eq 0 ]; then echo "BITE: all plants produced their expected verdict."; exit 0; fi
echo "BITE FAILED. A gate that cannot pass its own plants is not an instrument."
exit 1
