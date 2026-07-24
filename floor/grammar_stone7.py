"""Bench 7, SEVENTH STONE — proposed by the floor: THE MIRROR.

The listening. The floor has been producing PAIRS since the first weld:
the mixed record's theater came with a mirror cast (GNS commutant); the
hexagon returned two chiralities, conjugate twins; the pentagon a golden
solution and its shadow; the Gauss sums p+ and p-; r and r-bar; theta and
theta-bar. The proposal: the pairing itself — CONJUGATION, the dagger —
every relating can be read from the other side, and REALITY IS THE
AGREEMENT OF THE TWO READINGS.

Claims checked:

(1) PROBABILITY IS A LOOP THROUGH THE MIRROR. Born's rule p = <psi|P|psi>
    is a closed loop: the process psi, then the mirror-reading psi-dagger.
    Positivity is not an axiom on top: for any map f, the loop f-dagger o f
    has nonnegative spectrum — checked on random maps. Loops that close
    through the mirror cannot go negative; that is where probability
    comes from.

(2) THE MIRROR CAST IS THE SAME ALGEBRA READ BACKWARDS. The commutant
    that bench 1 found in the mixed record's theater is verified here to
    be exactly the RIGHT-multiplications: every commutant element is
    R_b(X) = X b for some b (residual 1e-15) — and the map b -> R_b
    REVERSES composition, R_{bc} = R_c R_b (checked): the second cast
    performs the same score backwards. One algebra, two readings; the
    theater of a mixed record is the stage on which both fit.

(3) DOUBLING: EVERY PROCESS TRAVELS WITH ITS MIRROR. The transfer matrix
    of K rho K-dagger is K (x) K-bar, verified exactly on random Kraus
    channels: mixed-state dynamics IS pure-state dynamics paired with its
    conjugate. (This is why the mixed record's theater was doubled and
    why classicality needed redundant records: the publicly real is what
    both readings co-sign.)

(4) THE LEDGER OF PAIRS, AUDITED. r1 * r1-bar = 1; theta * theta-bar = 1;
    p+ * p- = D^2 — every legitimate pair multiplies to a POSITIVE
    invariant. The one illegitimate pair: golden x shadow. Their loop
    values multiply to phi * (-1/phi) = -1 EXACTLY — the shadow is not
    the golden's mirror but its refusal, paired to -1 instead of +1.
    Unitarity, positivity, record-keeping: all one demand — that the two
    readings of every closed loop agree.

Status: exact. Seventh stone laid. A thing is a loop of relating (sixth
stone); the seventh adds: the loop is read twice, once from each side,
and what we call real is what both readings co-sign.
"""
import numpy as np

rng = np.random.default_rng(77)

PHI = (1 + np.sqrt(5)) / 2


def demonstrate(say):
    # (1) probability as a mirror-closed loop
    worst = 1.0
    for _ in range(30):
        f = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        worst = min(worst, float(np.linalg.eigvalsh(f.conj().T @ f).min()))
    psi = rng.normal(size=3) + 1j * rng.normal(size=3)
    psi /= np.linalg.norm(psi)
    P = np.zeros((3, 3)); P[0, 0] = 1
    p = np.real(psi.conj() @ P @ psi)
    say(f"  Born as a loop through the mirror: p = <psi|P|psi> = {p:.4f};")
    say(f"  min eigenvalue of f-dagger f over 30 random maps: {worst:.2e} >= 0")
    say(f"  — loops that close through the mirror cannot go negative.")
    assert worst > -1e-12 and 0 <= p <= 1

    # (2) the mirror cast reads the score backwards
    n = 2
    B = []
    for i in range(n):
        for j in range(n):
            E = np.zeros((n, n), dtype=complex); E[i, j] = 1
            B.append(E)

    def as_matrix(op):
        """4x4 matrix of a linear map on M_2 in the E_ij basis (HS o.n.)."""
        return np.array([[np.trace(B[r].conj().T @ op(B[c]))
                          for c in range(4)] for r in range(4)])

    left = [as_matrix(lambda X, a=a: a @ X) for a in B]
    right = [as_matrix(lambda X, b=b: X @ b) for b in B]
    # commutant of the left action (bench 1's mirror cast):
    I4 = np.eye(4)
    M = np.vstack([np.kron(I4, L) - np.kron(L.T, I4) for L in left])
    _, sv, Vh = np.linalg.svd(M)
    null = Vh[int(np.sum(sv > 1e-9 * sv.max())):]
    span_R = np.vstack([R.flatten() for R in right])
    worst_fit = 0.0
    for v in null:
        C = v.reshape(4, 4)
        coef, res, *_ = np.linalg.lstsq(span_R.T, C.flatten(), rcond=None)
        recon = (span_R.T @ coef).reshape(4, 4)
        worst_fit = max(worst_fit, np.linalg.norm(recon - C))
    say(f"  the mirror cast: every commutant element of the left action is a")
    say(f"  RIGHT-multiplication (fit residual {worst_fit:.1e});")
    assert worst_fit < 1e-10
    a, b = (rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
            for _ in range(2))
    Rab = as_matrix(lambda X: X @ (a @ b))
    RaRb = as_matrix(lambda X: X @ b) @ as_matrix(lambda X: X @ a)
    assert np.linalg.norm(Rab - RaRb) < 1e-10
    say(f"  and b -> R_b reverses composition (R_ab = R_b R_a, checked):")
    say(f"  the second cast performs the same score, read backwards.")

    # (3) doubling
    G = rng.normal(size=(6, 2)) + 1j * rng.normal(size=(6, 2))
    V, _ = np.linalg.qr(G)
    Ks = [V.reshape(2, 3, 2)[:, e, :] for e in range(3)]
    T = sum(np.kron(K, K.conj()) for K in Ks)
    rho = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    rho = rho @ rho.conj().T
    out1 = sum(K @ rho @ K.conj().T for K in Ks)
    out2 = (T @ rho.flatten()).reshape(2, 2)
    assert np.linalg.norm(out1 - out2) < 1e-12
    say(f"  doubling: the transfer matrix of K rho K-dagger is K (x) K-bar")
    say(f"  (exact on random channels) — every process travels with its")
    say(f"  mirror; mixed dynamics is pure dynamics co-signed by its twin.")

    # (4) the ledger of pairs
    r1, th = np.exp(4j * np.pi / 5), np.exp(-4j * np.pi / 5)
    p_plus = 1 + PHI ** 2 * th
    p_minus = 1 + PHI ** 2 * np.conj(th)
    D2 = 1 + PHI ** 2
    assert abs(r1 * np.conj(r1) - 1) < 1e-12
    assert abs(th * np.conj(th) - 1) < 1e-12
    assert abs(p_plus * p_minus - D2) < 1e-12
    pair = PHI * (-1 / PHI)
    say(f"  the ledger: r r-bar = 1, theta theta-bar = 1, p+ p- = D^2 —")
    say(f"  legitimate pairs multiply to positive invariants. Golden x shadow")
    say(f"  loop values: phi * (-1/phi) = {pair:.0f} — paired to -1, not +1:")
    say(f"  the shadow is not the golden's mirror but its refusal.")
    assert abs(pair + 1) < 1e-12
    say("  moral: the sixth stone drew the noun as a loop; the seventh adds")
    say("         that every loop is read twice, once from each side. What")
    say("         we call real — probability, record, objectivity — is what")
    say("         both readings co-sign. The mirror is not decoration; it is")
    say("         the difference between a value and a fact.")


if __name__ == "__main__":
    demonstrate(print)
