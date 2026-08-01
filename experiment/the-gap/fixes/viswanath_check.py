#!/usr/bin/env python3
"""The repair for GAP/sweeps/sweep17.py, and its external check.

The sweep accumulates log|b| for the random-Fibonacci recurrence a,b = b, b+G*a
with G = +-1. Two problems, one visible:
  VISIBLE  b can be exactly 0 (when G=-1), so math.log(abs(b)) raises.
  REAL     (a,b) is a VECTOR. |b| alone is the growth of one COMPONENT, not of
           the norm — the wrong Lyapunov exponent. log 0 is only how the
           wrongness announced itself.
Repair: m = max(|a|,|b|). Checked against Viswanath's constant, which neither
party chose.
"""
import math, random, statistics
VIS = 1.1319882487943

def lyap(n, trials, use_norm):
    out = []
    for t in range(trials):
        r = random.Random(1000 + t); a = b = 1.0; s = 0.0
        for _ in range(n):
            G = 1.0 if r.random() < 0.5 else -1.0
            a, b = b, b + G * a
            m = max(abs(a), abs(b)) if use_norm else abs(b)
            if m > 1e12 or (0 < m < 1e-12):
                s += math.log(m); a /= m; b /= m
        tail = max(abs(a), abs(b)) if use_norm else abs(b)
        if tail == 0:
            return None                      # the original's crash, caught
        out.append((s + math.log(tail)) / n)
    return statistics.mean(out)

if __name__ == "__main__":
    print("repaired (vector norm):")
    for n in (400, 1600, 6400):
        v = lyap(n, 3000, True)
        print(f"  n={n:>5}  exp = {math.exp(v):.7f}   Viswanath = {VIS:.7f}   "
              f"err = {math.exp(v)-VIS:+.7f}")
    print("\noriginal (|b| only), on the seeds where it survives:")
    for n in (400, 1600):
        v = lyap(n, 3000, False)
        print(f"  n={n:>5}  " + ("CRASHED (b hit exactly 0)" if v is None
                                 else f"exp = {math.exp(v):.7f}   <- near-correct, wrong method"))
