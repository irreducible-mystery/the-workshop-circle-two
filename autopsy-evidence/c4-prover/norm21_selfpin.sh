#!/bin/sh
# norm21_selfpin.sh — norm 21, mechanized.
#
#   NORM 21 says a crate cannot carry its own pin.  This is the same theorem one
#   level down: A FILE CANNOT CARRY ITS OWN SHA-256.  Writing the correct value
#   into the file changes the value.  Such a field is not stale — it is
#   UNSATISFIABLE, and no amount of re-rendering will ever make it true.
#
#   BOUGHT BY:  rate/README.md merged into the-workshop's default branch on
#   2026-07-31 claiming its own hash as 6185bf7e…; measured 19d8611e….  Four
#   seats reviewed that artifact and the row survived, because a row that looks
#   like every other pin row does not read as impossible.  A human cannot see
#   this and a machine cannot miss it, which is the definition of a gate's job.
#
#   WHAT IT CHECKS: every tracked text file, for a line of `sha256sum` shape —
#   64 hex, whitespace, a filename token — where the filename token equals the
#   scanned file's own basename.  Any such row is RED.
#
#   WHAT IT DOES NOT CHECK, stated so nobody trusts it further than it goes:
#     - It cannot see a self-pin written in prose ("this file hashes to …")
#       rather than in sha256sum shape.  That is a real blind spot.
#     - KNOWN FALSE POSITIVE: file a/README.md legitimately pinning a DIFFERENT
#       directory's b/README.md fires this gate, because only the basename is
#       compared.  Pin such rows by path, not by bare basename, and the gate is
#       quiet.  This is a deliberate trade: a false positive costs a sentence,
#       a false negative merged into a sealed circle.
#
#   BITE (norm 16): plants/ carries three, and `plants/BITE.md` records the run.
#
#   USAGE:  sh autopsy-evidence/c4-prover/norm21_selfpin.sh  [root]
#           exit 0 = no file claims its own pin.  exit 1 = at least one does.

ROOT=${1:-.}
cd "$ROOT" || exit 2

RED=0

# Tracked files only. An untracked scratch file is not the record's problem, and
# scanning them made this gate's first run noisy with its own plants.
if git rev-parse --git-dir >/dev/null 2>&1; then
    LIST=$(git ls-files)
else
    LIST=$(find . -type f -not -path '*/.git/*' | sed 's|^\./||')
fi

for f in $LIST; do
    [ -f "$f" ] || continue
    # Binary files have no pin rows and choke grep in some locales.
    case "$f" in *.zip|*.png|*.jpg|*.pdf|*.olean) continue ;; esac

    base=$(basename "$f")

    # sha256sum shape: 64 hex, whitespace, then the name (sha256sum prints two
    # spaces or ' *'; a hand-written table may print one). The name may be bare
    # or path-qualified — we fire only when the trailing component is our own
    # basename AND the token has no directory part, per the false-positive note.
    hits=$(grep -nE '(^|[^0-9a-fA-F])[0-9a-fA-F]{64}[[:space:]]+\*?'"$(printf '%s' "$base" | sed 's/[.[\*^$]/\\&/g')"'([[:space:]]|$)' "$f" 2>/dev/null)
    [ -z "$hits" ] && continue

    actual=$(sha256sum "$f" | cut -d' ' -f1)
    echo "SELF-PIN in $f"
    echo "$hits" | while IFS= read -r line; do
        claimed=$(printf '%s' "$line" | grep -oE '[0-9a-fA-F]{64}' | head -1)
        if [ "$claimed" = "$actual" ]; then
            echo "    line ${line%%:*}: claimed $claimed  == measured  (a preimage was found, or the file was not saved after)"
        else
            echo "    line ${line%%:*}: claimed $claimed"
            echo "                measured $actual   <-- UNSATISFIABLE, not stale"
        fi
    done
    RED=1
done

if [ "$RED" -eq 0 ]; then
    echo "norm21_selfpin: clean -- no tracked file carries its own pin."
    exit 0
fi

echo ""
echo "norm21_selfpin: RED. A file cannot carry its own SHA-256."
echo "  The repair is to DELETE the row, not to correct it. Pin from outside:"
echo "  the pin rides in the courier's message, or in the file that carries it."
exit 1
