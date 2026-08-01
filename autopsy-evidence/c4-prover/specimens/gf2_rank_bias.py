#!/usr/bin/env python3
"""gf2_rank_bias.py -- the defect is not that it is wrong. It is WHICH WAY.

WHAT THIS REPRODUCES.  `history/verification/independent_math_check.py:108`
(the-workshop@origin/main) carries a GF(2) rank routine used to decide whether
the magic-square contextuality system is solvable.  META_AUDIT recorded that it
returns 6 where the true rank is 5.  It still does, today.

Run the script it lives in and you get, on stdout:

    FAIL rank M = 5 (GF2)
    ...
    All independent checks complete.

with exit code 0, because that file's entire harness is `line 5`:

    ok = lambda name, cond: print(("PASS " if cond else "FAIL ") + name)

WHAT THIS SCRIPT ADDS.  A wrong rank function could be wrong in either
direction.  Sweeping random matrices shows it is not:

    ~10% of random 6x9 GF(2) matrices disagree with the truth,
    and EVERY SINGLE DISAGREEMENT IS AN OVERCOUNT.  Never once low.

That direction is the whole finding.  Rank is compared against the augmented
rank to decide solvability; an overcounting rank makes rank(M) meet rank([M|b])
that it should not meet, so **the failure mode of this bug is declaring an
unsolvable system solvable** -- an obstruction quietly vanishing.  For a script
whose one job is to detect a cohomological obstruction, the bug points exactly
the wrong way.

WHY IT IS WRONG.  The pivot is chosen by VALUE and removed by VALUE:

    rows.remove(piv) if piv in rows else None

`list.remove` deletes the first element EQUAL to `piv`.  After the XOR step
another row can have become equal to it, so the wrong row is dropped, the pivot
survives into the next bit, and the rank counts it twice.  The correct routine
sitting in the same repository -- `floor/sheaf_cohomology.py:42` -- eliminates
by POSITION and returns 5.

RUN:  python3 gf2_rank_bias.py     exit 0 = the defect still reproduces
                                   exit 1 = it no longer does; re-read the source
"""
import random
import sys

WIDTH = 9


def gf2_rank_checker(rows):
    """history/verification/independent_math_check.py:108, verbatim in behaviour."""
    rows = [int(''.join(map(str, r)), 2) for r in rows]
    rank = 0
    for bit in reversed(range(WIDTH)):
        piv = next((r for r in rows if (r >> bit) & 1), None)
        if piv is None:
            continue
        rows = [r ^ piv if ((r >> bit) & 1 and r != piv) else r for r in rows]
        rows.remove(piv) if piv in rows else None
        rank += 1
    return rank


def gf2_rank_truth(rows):
    """Brute force: the span of the rows is a subspace; its size is 2**rank."""
    span = {0}
    for r in [int(''.join(map(str, x)), 2) for x in rows]:
        span |= {s ^ r for s in span}
    return len(span).bit_length() - 1


def magic_square():
    M = [[1 if i // 3 == r else 0 for i in range(9)] for r in range(3)]
    M += [[1 if i % 3 == c else 0 for i in range(9)] for c in range(3)]
    return M


def main():
    failures = []

    M = magic_square()
    got, want = gf2_rank_checker(M), gf2_rank_truth(M)
    print(f"the record's own matrix : checker={got}  truth={want}")
    if got == want:
        failures.append("the magic-square matrix now agrees -- the defect is gone")

    random.seed(20260801)
    n = over = under = 0
    N = 4000
    for _ in range(N):
        R = [[random.randint(0, 1) for _ in range(9)] for _ in range(6)]
        a, b = gf2_rank_checker(R), gf2_rank_truth(R)
        if a != b:
            n += 1
            over += a > b
            under += a < b
    print(f"random 6x9 sweep        : {n}/{N} disagree ({100*n/N:.1f}%)"
          f"   overcount={over}  undercount={under}")
    if under:
        failures.append(f"undercounts appeared ({under}) -- the bias claim no longer holds")
    if n == 0:
        failures.append("no disagreements -- the defect is gone")

    print()
    if failures:
        for f in failures:
            print("CHANGED:", f)
        print("This specimen has expired. Re-read the source before trusting it.")
        return 1
    print("defect reproduces: wrong ~10% of the time, and never in the safe direction.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
