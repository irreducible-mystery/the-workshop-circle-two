"""Bench 6 — THE CAST.

Claim checked: the division of the world into parts is not given with the
play; it can be discovered from the dynamics as the cut that stabilizes.
A two-qubit Hamiltonian, local in a hidden factorization (planted interaction
weight eps^2), is scrambled by a Haar-random change of basis: presented that
way, its interaction weight looks enormous and there are no 'parts' in sight.
Searching over all factorizations for the cut that minimizes interaction
weight rediscovers the hidden cast — and in the discovered frame, product
states barely entangle: the cut can hold records.

Status: honest toy of 'quantum mereology' (Carroll–Singh), with planted
ground truth; the optimizer must recover it or the assert fails.
"""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(42)

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
P = [I2, X, Y, Z]
BASIS = [(i, j, np.kron(P[i], P[j])) for i in range(4) for j in range(4)]
GENS = [np.kron(P[i], P[j]) for i in range(4) for j in range(4) if (i, j) != (0, 0)]


def weights(H):
    local = nonloc = 0.0
    for i, j, B in BASIS:
        c = float(np.real(np.trace(B @ H)) / 4)
        if (i == 0) != (j == 0):
            local += c * c
        elif i != 0 and j != 0:
            nonloc += c * c
    return local, nonloc


def expi(Hgen):
    w, V = np.linalg.eigh(Hgen)
    return V @ np.diag(np.exp(1j * w)) @ V.conj().T


def frame(theta):
    return expi(sum(t * G for t, G in zip(theta, GENS)))


def haar(n):
    G = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Q, R = np.linalg.qr(G)
    return Q @ np.diag(np.diag(R) / np.abs(np.diag(R)))


def entropy_A(psi):
    m = psi.reshape(2, 2)
    w = np.clip(np.linalg.eigvalsh(m @ m.conj().T), 1e-15, 1.0)
    w = w / w.sum()
    return float(-(w * np.log2(w)).sum())


def median_entanglement(H, t=0.4):
    w, V = np.linalg.eigh(H)
    U = V @ np.diag(np.exp(-1j * w * t)) @ V.conj().T
    ents = []
    for k in range(4):
        psi0 = np.zeros(4, dtype=complex)
        psi0[k] = 1.0
        ents.append(entropy_A(U @ psi0))
    return float(np.median(ents))


def demonstrate(say):
    H_true = 1.0 * np.kron(Z, I2) + 0.7 * np.kron(I2, Z) + 0.15 * np.kron(X, X)
    _, planted = weights(H_true)
    U = haar(4)
    H_scr = U @ H_true @ U.conj().T
    _, scrambled = weights(H_scr)
    say(f"  hidden cast: interaction weight eps^2 = {planted:.4f};")
    say(f"  scrambled presentation: {scrambled:.4f} "
        f"({scrambled / planted:.0f}x worse — no parts in sight)")

    def objective(theta):
        V = frame(theta)
        return weights(V @ H_scr @ V.conj().T)[1]

    best, best_theta = np.inf, None
    for _ in range(24):
        theta0 = rng.normal(scale=0.8, size=15)
        res = minimize(objective, theta0, method="Powell",
                       options={"maxiter": 4000, "xtol": 1e-8, "ftol": 1e-10})
        if res.fun < best:
            best, best_theta = float(res.fun), res.x
    say(f"  search over all factorizations: best interaction weight found = "
        f"{best:.4f} (planted: {planted:.4f})")
    assert best < planted * 1.5 + 1e-9

    Vb = frame(best_theta)
    e_found = median_entanglement(Vb @ H_scr @ Vb.conj().T)
    e_rand = float(np.median([median_entanglement(W @ H_scr @ W.conj().T)
                              for W in (haar(4) for _ in range(20))]))
    say(f"  records check: median entanglement of product states after t=0.4 —")
    say(f"    discovered cut: {e_found:.4f} bits   random cuts: {e_rand:.4f} bits")
    assert e_found < e_rand
    say("  moral: the parts were not in the presentation; they were in the play.")
    say("         The cast list is the cut that keeps composing — parts as")
    say("         stabilizations, selected by their ability to hold records.")


if __name__ == "__main__":
    demonstrate(print)
