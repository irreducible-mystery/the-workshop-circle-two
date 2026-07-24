"""Bench 3, DEEPENED — CHANNELS (quantum de Finetti).

The urn showed: 'hidden eternal law' and 'pure precedent' can be one world.
The quantum deepening asks WHEN a habit amounts to a law, and answers:
exactly when the habit is unboundedly shareable.

(1) Law emerging, with a measured rate. The n-qubit half-excited Dicke state
    is permutation-invariant (a pure habit, no parameter anywhere). Its
    two-qubit reduction converges to a mixture of i.i.d. states — spin-
    coherent states around the equator, mixed uniformly: a 'hidden law'
    theta = phi that is, again, only a representation artifact. The trace
    distance obeys T(n) = 1/(2(n-1)) — discovered here numerically, slope -1
    on the log-log line — comfortably inside the quantum de Finetti bound
    (~ 2kd^2/n). Habit-formation has a rate, and we measured it.

(2) The lawless case: monogamy. The two-qubit singlet is swap-invariant
    (a habit at n=2) yet admits NO symmetric extension to three parties:
    it is pure (Tr rho^2 = 1, checked), so any extension factorizes as
    singlet (x) rho_C, forcing the other marginal to be product — but the
    singlet is entangled (partial-transpose eigenvalue -1/2 < 0, checked).
    Unshareable, therefore lawless: no de Finetti mixture exists for it.

Moral: in the quantum case 'having a law behind you' = being infinitely
extendable = unlimited shareability of the pattern. The unshareable is the
indexical — and it is exactly where law runs out. (Channels reading: via
Choi, exchangeable uses of a process = mixture of memoryless processes;
the full channel-de Finetti is the next stretch, noted, not faked.)

Status: exact miniature; every number checked against closed form.
"""
import numpy as np


def dicke_rdm2(n):
    """Exact 2-qubit reduced state of |D_n^{n/2}> in basis 00,01,10,11."""
    k = n // 2
    denom = n * (n - 1)
    p00 = (n - k) * (n - k - 1) / denom
    p11 = k * (k - 1) / denom
    pc = k * (n - k) / denom
    rho = np.zeros((4, 4))
    rho[0, 0] = p00
    rho[3, 3] = p11
    rho[1, 1] = rho[2, 2] = rho[1, 2] = rho[2, 1] = pc
    return rho


def equatorial_mixture(grid=2048):
    """sigma = avg over phi of |psi_phi><psi_phi|^{x2},
    psi_phi = (|0> + e^{i phi}|1>)/sqrt(2). Also known in closed form."""
    sigma = np.zeros((4, 4), dtype=complex)
    for phi in np.linspace(0, 2 * np.pi, grid, endpoint=False):
        psi = np.array([1.0, np.exp(1j * phi)]) / np.sqrt(2)
        v = np.kron(psi, psi)
        sigma += np.outer(v, v.conj())
    return sigma / grid


def trace_distance(a, b):
    w = np.linalg.eigvalsh(a - b)
    return 0.5 * float(np.abs(w).sum())


def demonstrate(say):
    # closed form for the limit, verified against the numerical average
    sigma = np.zeros((4, 4), dtype=complex)
    sigma[0, 0] = sigma[3, 3] = 0.25
    sigma[1, 1] = sigma[2, 2] = sigma[1, 2] = sigma[2, 1] = 0.25
    assert np.linalg.norm(sigma - equatorial_mixture()) < 1e-12

    ns = [8, 16, 32, 64, 128, 256, 512, 1024, 4096]
    Ts = []
    for n in ns:
        T = trace_distance(dicke_rdm2(n), sigma.real)
        Ts.append(T)
        assert abs(2 * (n - 1) * T - 1.0) < 1e-9      # exact law T = 1/(2(n-1))
        assert T <= 16.0 / n                           # de Finetti-type bound
    slope = np.polyfit(np.log(ns), np.log(Ts), 1)[0]
    say("  law emerging: T(n) = dist(2-qubit habit, best i.i.d.-mixture):")
    say("    " + "  ".join(f"n={n}: {T:.2e}" for n, T in zip(ns[:4], Ts[:4])))
    say(f"    measured: T(n) = 1/(2(n-1)) exactly; log-log slope = {slope:.3f}")
    say(f"    (quantum de Finetti bound ~16/n respected at every n)")
    assert -1.05 < slope < -0.95

    # the lawless case
    singlet = np.zeros(4, dtype=complex)
    singlet[1], singlet[2] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    rho = np.outer(singlet, singlet.conj())
    SWAP = np.eye(4)[[0, 2, 1, 3]]
    assert np.linalg.norm(SWAP @ rho @ SWAP - rho) < 1e-12       # a habit at n=2
    assert abs(np.trace(rho @ rho) - 1.0) < 1e-12                # pure
    pt = rho.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)
    min_eig = float(np.linalg.eigvalsh(pt).min())
    say(f"  the unshareable: singlet is swap-invariant, pure, and entangled")
    say(f"    (partial-transpose eigenvalue {min_eig:.3f} < 0) — purity forces any")
    say(f"    3-party extension to decouple, so no symmetric extension exists:")
    say(f"    a habit that cannot be shared, and therefore never becomes a law.")
    assert min_eig < -0.49

    say("  moral: law = unlimited shareability of the habit (de Finetti);")
    say("         monogamy marks the lawless — the unshareable indexical.")
    say("         The urn was the classical case; this is the quantum one.")


if __name__ == "__main__":
    demonstrate(print)
