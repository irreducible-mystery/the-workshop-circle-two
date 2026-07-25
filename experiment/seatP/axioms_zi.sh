#!/bin/sh
# axioms_zi.sh — axiom census for Zi.lean (Circle Two experiment article).
# Re-instantiation of Circle One's audit/axioms.sh pattern for this tree:
# copy the source, append one `#print axioms Zi.<name>` per theorem
# (namespace rebuilt from the file's single `namespace Zi` block), run
# lean once, tally. Norm 16: this instrument's first output is
# quarantined until it has failed on a plant and passed clean.
set -e
cd "$(dirname "$0")"
SRC=Zi.lean
TMP=/tmp/Zi_axioms.lean
cp "$SRC" "$TMP"
# every theorem in the file lives inside `namespace Zi`
names=$(grep '^theorem ' "$SRC" | sed 's/^theorem \([A-Za-z0-9_'"'"']*\).*/\1/')
count=$(echo "$names" | wc -l | tr -d ' ')
for n in $names; do
  echo "#print axioms Zi.$n" >> "$TMP"
done
out=$(lean "$TMP" 2>&1) || { echo "COMPILE FAILED"; echo "$out" | head -5; exit 1; }
total=$(echo "$out" | grep -c "depends on axioms\|does not depend on any axioms" || true)
free=$(echo "$out" | grep -c "does not depend on any axioms" || true)
sorryax=$(echo "$out" | grep -c "sorryAx" || true)
choice=$(echo "$out" | grep -c "Classical.choice" || true)
echo "theorems in source : $count"
echo "census lines       : $total"
echo "axiom-free         : $free"
echo "sorryAx            : $sorryax"
echo "Classical.choice   : $choice"
echo "--- per-theorem profile ---"
echo "$out" | grep "axioms"
[ "$count" = "$total" ] || { echo "ALARM: census does not cover every theorem"; exit 1; }
[ "$sorryax" = "0" ] || { echo "ALARM: sorryAx present"; exit 1; }
[ "$choice" = "0" ] || { echo "ALARM: Classical.choice present"; exit 1; }
echo "RESULT: PASS"
