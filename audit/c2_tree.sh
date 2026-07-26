#!/bin/sh
# audit/c2_tree.sh — the tree-hygiene gate (REGISTER row 10).
#
# WHY THIS EXISTS
#   Round 2 committed thirty compiled-bytecode cache files into the record
#   (a19fb4c, floor/__pycache__), and no instrument noticed: the prose gates
#   read prose, the certificate reads the benches, the floor reads its own
#   asserts. A defect in a class that had NO adjudicator — exactly where the
#   corrections law says defects must land. Chartered in the round-2
#   verification letter; the crop and its fix are b4328b2.
#
# CONTRACT
#   No build artifact is tracked in git. The tracked file list (`git ls-files`
#   — the index, so a staged artifact bites before it is ever committed) is
#   matched against the artifact patterns below; every hit prints its path and
#   the gate exits 1. Silence exits 0 (norm 10: the pass condition is silence).
#
# THE PATTERNS — and the boundary, stated plainly
#   (^|/)__pycache__/     Python bytecode cache directory, at any depth
#   *.pyc *.pyo           compiled Python bytecode
#   *.olean *.ilean       Lean build output. The charge ships their HASHES and
#                         the compile transcript — never the files themselves.
#   (^|/).lake/           Lean build directory (zero-imports forbids lake, so
#                         anything it leaves behind is artifact by definition)
#   *.o *.a *.so          object / archive / shared-object output
#   *.swp *.swo *.swn *~  editor swap and backup files
#   (^|/).DS_Store        macOS directory metadata
#   (^|/)Thumbs.db        Windows directory metadata
#
#   BOUNDARY (REGISTER row 10 says this too): patterns only. This gate cannot
#   know that a novel artifact type is an artifact — a new build product needs
#   a new pattern here, added in the same stroke as whatever produced it. It
#   also says nothing about whether a tracked SOURCE file belongs in the tree;
#   that is a human judgement no pattern encodes.
#
# NORM 16
#   Bitten before trusted: stage any file matching a pattern
#   (`touch floor/plant.pyc && git add -f floor/plant.pyc`), run this gate,
#   watch it exit 1 naming the path, then `git rm --cached floor/plant.pyc`
#   and delete it. An alarm you have not seen fire is not an alarm.
#
# USAGE
#   sh audit/c2_tree.sh        (run from anywhere inside the repository)

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || {
    echo "c2_tree: not a git repository — this gate reads \`git ls-files\`" >&2
    exit 2
}
cd "$ROOT" || exit 2

ARTIFACT_ERE='(^|/)__pycache__/|\.(pyc|pyo|olean|ilean|o|a|so|swp|swo|swn)$|~$|(^|/)\.lake/|(^|/)\.DS_Store$|(^|/)Thumbs\.db$'

echo "=============================================================="
echo " C2 TREE GATE -- build artifacts must never be tracked"
echo "=============================================================="

tracked=$(git ls-files | wc -l | tr -d ' ')
hits=$(git ls-files | grep -E "$ARTIFACT_ERE")
nhits=$(printf '%s' "$hits" | grep -c . )

if [ "$nhits" -gt 0 ]; then
    printf '%s\n' "$hits" | while IFS= read -r path; do
        [ -n "$path" ] && echo "ARTIFACT TRACKED: $path"
    done
fi

echo "  tracked files scanned: $tracked;  build artifacts tracked: $nhits"

if [ "$nhits" -eq 0 ]; then
    echo "RESULT: the tracked tree carries no build artifacts.  PASS."
    exit 0
else
    echo "RESULT: FAIL -- untrack the paths above (git rm --cached) and ignore them."
    exit 1
fi
