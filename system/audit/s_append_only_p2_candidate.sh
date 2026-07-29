#!/bin/sh
# ---------------------------------------------------------------------------
# CANDIDATE — NOT OF RECORD, NOT WIRED.  system/audit/s_append_only_p2_candidate.sh
#
# P2's prefix strengthening, authored by the Circle Four prover against the
# builder's falsifier list stated in advance (C4-R1-BUILDER-REPLY.md,
# "e6f4584f…", filed byte-exact).  QUARANTINED under norm 16: these bytes
# enter no chain until both seats have bitten them at this file's couriered
# pin.  The shipped gate (s_append_only.sh) remains the wired instrument.
#
# WHAT THIS CHECKS: HEAD's copy of each guarded file must be a BYTE-PREFIX
#   of the working copy — "grow by appending" enforced at the letter.
#   Catches every mode both seats have planted: in-place modification,
#   heading deletion, mid-file insertion (the builder's plant 3), bullet
#   deletion (SR18), blank-line deletion (SR21) — one test, no regex.
# THE NEWLINE-BOUNDARY CLAUSE (the builder's): if the working copy is
#   longer than HEAD's copy, HEAD's copy must end in a newline — otherwise
#   the "append" extends the last committed line in place, a modification
#   wearing an append's shape.  Both guarded files end in a newline at HEAD
#   today; this clause closes the door before anything is behind it.
# SCOPE: the guarded files only.  The prefix law is NOT general — the live
#   tree holds a lawful mid-file insertion in an unguarded file (the
#   SUPERSEDED banner added to CIRCLE-FOUR-CHARGE-DRAFT.md at "f236c7e…").
# WHAT IT DOES NOT CHECK: the TRUTH of any row (the non-author seat does);
#   files other than the two named; history rewrites (row 5's honest gap);
#   a symlinked guarded file (closed by the -L test above; measured by
#   plant, builder's bite, 2026-07-29); a mode-bit-only change (pointed,
#   uncured — the guarded files' law does not live in their execute bit).
#
# USAGE:  sh system/audit/s_append_only_p2_candidate.sh   (from the repo root)
# EXIT:   0 = prefix law holds;  1 = violation;  2 = cannot run
# ---------------------------------------------------------------------------

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || {
    echo "s_append_only_p2: not a git repository" >&2; exit 2; }
cd "$ROOT" || exit 2

TMP=$(mktemp -d) || exit 2
trap 'rm -rf "$TMP"' 0

fail=0
for f in system/SYSTEM-REGISTER.md system/SYSTEM-NORMS.md; do
    # A file not yet at HEAD is being born: nothing to preserve, pass.
    if ! git cat-file -e "HEAD:$f" 2>/dev/null; then
        printf '  %-32s BORN THIS COMMIT (nothing to preserve)\n' "$f"
        continue
    fi
    if [ ! -f "$f" ]; then
        printf '  %-32s VIOLATION: guarded file missing from working copy\n' "$f"
        fail=1
        continue
    fi
    if [ -L "$f" ]; then
        printf '  %-32s VIOLATION: guarded file is a symlink\n' "$f"
        fail=1
        continue
    fi
    git show "HEAD:$f" > "$TMP/head" || {
        echo "s_append_only_p2: cannot read HEAD:$f" >&2; exit 2; }
    n=$(wc -c < "$TMP/head")
    m=$(wc -c < "$f")
    if [ "$m" -lt "$n" ]; then
        printf '  %-32s VIOLATION: working copy shorter than HEAD (%s < %s bytes)\n' "$f" "$m" "$n"
        fail=1
        continue
    fi
    head -c "$n" "$f" > "$TMP/pref"
    if ! cmp -s "$TMP/head" "$TMP/pref"; then
        printf '  %-32s VIOLATION: HEAD copy is not a byte-prefix of the working copy\n' "$f"
        cmp "$TMP/head" "$TMP/pref" 2>/dev/null | head -1 | sed 's/^/      /'
        fail=1
        continue
    fi
    if [ "$m" -gt "$n" ]; then
        last=$(tail -c 1 "$TMP/head" | od -An -tx1 | tr -d ' \n')
        if [ "$last" != "0a" ]; then
            printf '  %-32s VIOLATION: append extends the last committed line (HEAD lacks trailing newline)\n' "$f"
            fail=1
            continue
        fi
    fi
    printf '  %-32s PREFIX LAW HOLDS\n' "$f"
done

if [ "$fail" -eq 0 ]; then
    echo "RESULT: the constitution grew by appending only (prefix law).  PASS."
else
    echo "RESULT: the prefix law was broken.  FAIL."
    echo "        Corrections are NEW rows pointing at old ones — the"
    echo "        circles' own law.  Revert and append."
fi
exit "$fail"
