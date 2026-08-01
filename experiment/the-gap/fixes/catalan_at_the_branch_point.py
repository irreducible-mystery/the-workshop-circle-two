#!/usr/bin/env python3
"""The repair for GAP/sweeps/sweep15.py (sweeps 44-46).

The sweep builds ~14 Catalan numbers and then asks for 1000 of them, so it
raises IndexError before printing its own result. It also runs a 200,000-
iteration loop whose body is `pass`. Both cosmetic; the mathematics is right.

What it was trying to show: the root of x^2 = x + G, expanded as a series,
IS the Catalan generating function — and evaluated at its own branch point
x = 1/4 (that is, G = -1/4) it equals 1/2, the double root.
"""
import math
N = 1200
cat = [1]
for n in range(1, N):
    cat.append(cat[-1] * 2 * (2 * n - 1) // (n + 1))

print("  sum_{n>=1} C_{n-1} / 4^n   ->   1/2   (the double root at G = -1/4)")
for k in (10, 100, 1000):
    s = sum(cat[n - 1] / 4 ** n for n in range(1, k + 1))
    err = 0.5 - s
    print(f"    k={k:>5}  partial = {s:.6f}   err = {err:.6f}   "
          f"err*2*sqrt(pi*k) = {err * 2 * math.sqrt(math.pi * k):.4f}")
print("    the last column is ~1.00: the error decays as 1/(2*sqrt(pi*k)),")
print("    which is the n^(-3/2) tail of a square-root branch point.")
print("    The series converges ON its radius, but only just.")
