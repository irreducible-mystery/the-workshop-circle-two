#!/bin/sh
# hookcheck.sh — is the gate chain ACTUALLY WIRED in this clone?
#
#   THE DEFECT THIS EXISTS FOR, and it is the deepest instance of this record's
#   recurring species that I have measured:
#
#     `.githooks/pre-commit` sitting in the tree is a MARKER.
#     "the gates run on commit" is the PROPERTY.
#     They are connected by ONE command that a seat must remember to type,
#     once per clone:   git config core.hooksPath .githooks
#
#   The hook's own header says so ("Install once, per clone"). Nothing in any
#   repository can detect that it was not done. A fresh container gets a fresh
#   clone, and a fresh clone has NO GATES AT ALL while looking exactly like a
#   clone that has all of them.
#
#   MEASURED 2026-08-01, in the container this was written in, all three clones:
#       the-workshop              core.hooksPath = UNSET
#       the-workshop-circle-two   core.hooksPath = UNSET
#       the-workshop-circle-four  core.hooksPath = UNSET
#
#   This gate cannot repair that — nothing inside a repository can, which is the
#   finding. What it can do is make the absence LOUD and make it the first thing
#   a seat runs in a new container, instead of a thing a seat remembers.
#
#   HONEST LIMIT: a seat must run this to learn the hooks are off, and a seat
#   who would run it is a seat who would have run the config command. It closes
#   nothing on its own. It is worth having only if it is the FIRST line of a
#   circle's start-here document, and that is a courier's call, not a gate's.
#
#   USAGE:  sh autopsy-evidence/c4-prover/hookcheck.sh [repo-root]
#           exit 0 = wired.  exit 1 = the tree has hooks that will never fire.

ROOT=${1:-.}
cd "$ROOT" || exit 2

git rev-parse --git-dir >/dev/null 2>&1 || { echo "hookcheck: not a git tree"; exit 2; }

CONFIGURED=$(git config --get core.hooksPath 2>/dev/null)
PRESENT=""
[ -f .githooks/pre-commit ] && PRESENT=".githooks/pre-commit"

printf '  %-26s %s\n' "hooks present in tree:" "${PRESENT:-none}"
printf '  %-26s %s\n' "core.hooksPath:" "${CONFIGURED:-UNSET}"

if [ -z "$PRESENT" ]; then
    echo "hookcheck: this tree ships no pre-commit hook. Nothing to wire."
    exit 0
fi

if [ "$CONFIGURED" = ".githooks" ]; then
    echo "hookcheck: WIRED -- .githooks/pre-commit will fire on commit."
    exit 0
fi

echo ""
echo "hookcheck: RED -- this tree ships gates that WILL NOT RUN."
echo "  The tree looks protected. It is not. Fix, in this clone:"
echo "      git config core.hooksPath .githooks"
exit 1
