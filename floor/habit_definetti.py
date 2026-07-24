"""Bench 3 — THE HABIT (the risk-budget bench).

Claim checked, in rigorous miniature: 'eternal hidden law' and 'pure precedent
with nothing behind it' can be provably the SAME world. The Polya urn is
exchangeable; each history congeals its own constant (the limiting fraction);
de Finetti's theorem says the process is equivalent to sampling a hidden
parameter theta and flipping i.i.d. coins — yet no theta appears anywhere in
the mechanism. The 'law' is a representation artifact of the process's
symmetry. Also shown: young histories are sloppy and old ones frozen (habit
hardening), and the past legislates the future (precedent).

Status: honest toy — but every statement it makes is a theorem; checked
statistically here, exactly in the literature.
"""
import numpy as np

rng = np.random.default_rng(1313)


def polya_ensemble(M, N, checkpoints):
    f_at = {n: np.empty(M) for n in checkpoints}
    red10 = np.empty(M, dtype=int)
    for m in range(M):
        r, b = 1, 1
        u = rng.random(N)
        for n in range(1, N + 1):
            if u[n - 1] < r / (r + b):
                r += 1
            else:
                b += 1
            if n == 10:
                red10[m] = r - 1
            if n in f_at:
                f_at[n][m] = (r - 1) / n
    return f_at, red10


def demonstrate(say):
    M, N = 4000, 1500
    f_at, red10 = polya_ensemble(M, N, [10, 20, 750, 1500])

    early = float(np.median(np.abs(f_at[20] - f_at[10])))
    late = float(np.median(np.abs(f_at[1500] - f_at[750])))
    say(f"  habit hardening: median swing over one doubling of history —")
    say(f"    young world (10->20 draws): {early:.3f}   old world (750->1500): {late:.3f}")
    assert early > 5 * late

    lim = np.sort(f_at[1500])
    ks = float(np.max(np.abs(lim - (np.arange(1, M + 1) - 0.5) / M)))
    say(f"  each history congealed its own constant; the ensemble of constants vs")
    say(f"  Uniform(0,1) — the exact de Finetti measure: KS deviation {ks:.3f}")
    assert ks < 0.06

    # the mirage: urn (no parameter anywhere) vs hidden-parameter world
    M2, n2 = 20000, 20
    urn_counts = np.empty(M2, dtype=int)
    for m in range(M2):
        r, b = 1, 1
        for _ in range(n2):
            if rng.random() < r / (r + b):
                r += 1
            else:
                b += 1
        urn_counts[m] = r - 1
    theta = rng.random(M2)
    hid_counts = rng.binomial(n2, theta)
    pu = np.bincount(urn_counts, minlength=n2 + 1) / M2
    ph = np.bincount(hid_counts, minlength=n2 + 1) / M2
    tv_uh = float(0.5 * np.abs(pu - ph).sum())
    tv_ex = float(0.5 * np.abs(pu - 1.0 / (n2 + 1)).sum())
    say(f"  precedent-world vs hidden-law-world, red-count law after {n2} draws:")
    say(f"    TV distance {tv_uh:.3f} (theory: identical — both exactly uniform;")
    say(f"    urn vs exact uniform: {tv_ex:.3f})")
    assert tv_uh < 0.05 and tv_ex < 0.05

    sel = red10 >= 8
    cond = float(f_at[1500][sel].mean())
    say(f"  precedent binds: histories opening >=8/10 red end at mean fraction "
        f"{cond:.3f}")
    say(f"    (posterior arithmetic predicts ~0.833; unconditioned mean: "
        f"{float(f_at[1500].mean()):.3f})")
    assert 0.76 < cond < 0.90
    say("  moral: the 'law' theta is nowhere in the mechanism — it is sediment.")
    say("         'Hidden constant' and 'self-similar habit' are two descriptions")
    say("         of one world; and young worlds are visibly sloppier than old ones.")


if __name__ == "__main__":
    demonstrate(print)
