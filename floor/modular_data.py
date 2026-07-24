"""Bench 7, THE IDENTITY CARD — S, T, and Verlinde: the circle closes.

The anyon's full papers, computed from what the workshop already earned:
fusion rules -> (pentagon) -> golden F -> (hexagon) -> braiding phases ->
twists -> S-matrix -> (Verlinde) -> ... the fusion rules again.

Claims checked:

(1) S FROM THE TWISTS. Using only the fusion rules, the quantum dimensions
    (1, phi), and the hexagon's twist theta_t = e^{-4 pi i/5}, the standard
    formula S_ab = (1/D) sum_c N_ab^c d_c theta_c/(theta_a theta_b) is
    evaluated — and the imaginary parts CANCEL EXACTLY, leaving the real
    golden S-matrix (1/D)[[1, phi],[phi, -1]], D = sqrt(2 + phi).

(2) MODULARITY. S is symmetric and unitary with S^2 = I (trivial charge
    conjugation); with T = diag(1, theta_t), the relation
    (S T)^3 = lambda S^2 holds to machine zero with |lambda| = 1, and
    lambda equals the normalized Gauss sum p_+/D — from which the chiral
    central charge is read off: c = -14/5 (mod 8) for our chirality
    (+14/5 for the mirror twin), the known Fibonacci value. Also
    p_+ p_- = D^2 (Gauss-sum duality), checked.

(3) VERLINDE'S FORMULA AS ARITHMETIC. N_ab^c = sum_x S_ax S_bx S*_cx / S_0x
    is evaluated and returns the fusion rules EXACTLY (every entry 0 or 1
    to 1e-12). The circle closes: grammar -> coherence -> braiding -> spins
    -> modular representation -> grammar. Asked for its papers, the play
    hands back its own grammar. The self-excited circuit, in miniature,
    with every arrow machine-checked.

Status: exact.
"""
import numpy as np

PHI = (1 + np.sqrt(5)) / 2
D = np.sqrt(1 + PHI ** 2)
DIMS = np.array([1.0, PHI])
THETA = np.array([1.0 + 0j, np.exp(-4j * np.pi / 5)])   # our chirality


def N(a, b, c):
    """Fibonacci fusion multiplicities."""
    if a == 0:
        return 1 if c == b else 0
    if b == 0:
        return 1 if c == a else 0
    return 1 if c in (0, 1) else 0  # tau x tau = 1 + tau


def demonstrate(say):
    # (1) S from the twists
    S = np.zeros((2, 2), dtype=complex)
    for a in range(2):
        for b in range(2):
            S[a, b] = sum(N(a, b, c) * DIMS[c] * THETA[c]
                          / (THETA[a] * THETA[b]) for c in range(2)) / D
    S_closed = np.array([[1, PHI], [PHI, -1]]) / D
    imag_norm = np.linalg.norm(S.imag)
    say(f"  S computed from fusion + dimensions + the hexagon's twists:")
    say(f"    imaginary parts cancel to {imag_norm:.1e}; S = (1/D)[[1,phi],"
        f"[phi,-1]] to {np.linalg.norm(S - S_closed):.1e}")
    assert imag_norm < 1e-12 and np.linalg.norm(S - S_closed) < 1e-12
    S = S.real

    # (2) modularity
    assert np.linalg.norm(S - S.T) < 1e-12
    assert np.linalg.norm(S @ S.conj().T - np.eye(2)) < 1e-12
    assert np.linalg.norm(S @ S - np.eye(2)) < 1e-12
    T = np.diag(THETA)
    M = np.linalg.matrix_power(S @ T, 3)
    S2 = S @ S
    lam = np.trace(M @ np.linalg.inv(S2)) / 2
    assert np.linalg.norm(M - lam * S2) < 1e-12 and abs(abs(lam) - 1) < 1e-12
    p_plus = sum(DIMS[a] ** 2 * THETA[a] for a in range(2))
    p_minus = sum(DIMS[a] ** 2 / THETA[a] for a in range(2))
    assert abs(lam - p_plus / D) < 1e-12
    assert abs(p_plus * p_minus - D ** 2) < 1e-12
    c = np.angle(lam) * 8 / (2 * np.pi) % 8
    say(f"  modularity: S symmetric, unitary, S^2 = I; (ST)^3 = lambda S^2")
    say(f"    with lambda = p+/D (Gauss sum), |lambda| = 1; p+ p- = D^2.")
    say(f"    chiral central charge c = {c:.4f} (mod 8) = "
        f"{'-' if c > 4 else '+'}14/5 — the Fibonacci value; the mirror")
    say(f"    chirality gives the other sign.")
    assert abs(c - (8 - 14 / 5)) < 1e-9 or abs(c - 14 / 5) < 1e-9

    # (3) Verlinde closes the circle
    worst = 0.0
    for a in range(2):
        for b in range(2):
            for cc in range(2):
                v = sum(S[a, x] * S[b, x] * np.conj(S[cc, x]) / S[0, x]
                        for x in range(2))
                worst = max(worst, abs(v - N(a, b, cc)))
    say(f"  Verlinde: N_ab^c = sum_x S_ax S_bx S*_cx / S_0x reproduces the")
    say(f"    fusion rules exactly (worst deviation {worst:.1e}).")
    assert worst < 1e-12
    say("  moral: grammar -> coherence -> braiding -> spins -> modular data ->")
    say("         grammar. The identity card, asked for, hands back the rules")
    say("         that issued it. The circle closes, every arrow checked.")


if __name__ == "__main__":
    demonstrate(print)
