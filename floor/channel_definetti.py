"""Bench 3, STRETCHED FURTHER — QUANTUM PROCESS: channel de Finetti via Choi.

Three claims, all checked:

(1) DYNAMICS ARE STATES IN DISGUISE — the Choi dictionary, exactly.
    For random channels built from random Stinespring isometries:
    complete positivity <-> the Choi state is PSD (checked);
    trace preservation <-> its output-marginal is maximally mixed (checked);
    and the channel's entire action is recovered from the state by
    Lambda(rho) = d * tr_in[ J (I x rho^T) ] (checked). Every state
    theorem — de Finetti included — therefore transfers to processes.

(2) SYMMETRY PRODUCES THE MIXTURE. Define the collective two-use dynamics
    purely algebraically, with NO integral and NO hidden parameter: project
    onto the commutant of the collective rotation U x U (the span of
    {identity, SWAP} — Schur-Weyl). Claim of the channel de Finetti: this
    symmetry-defined dynamics EQUALS a mixture of memoryless unitary
    evolutions, mixed by a measure (Haar) that emerges rather than being
    inserted. Checked: the algebraic projection agrees with the sampled
    Haar mixture of U-channel x U-channel on random states. Nothing ever
    chose a U; every marginal behaves as if one fixed U had been drawn and
    applied memorylessly. Hidden-law-of-dynamics as representation artifact,
    now in the quantum case.

(3) THE SINGLET OF PROCESSES — channel monogamy. The two-use SWAP dynamics
    (out1 = in2, out2 = in1) is exchange-symmetric, but its Choi state has a
    PURE maximally entangled cross-marginal (out1 with in2: purity = 1,
    checked; entangled: partial-transpose eigenvalue -1/2, checked). Purity
    forces any extension to decouple, so no symmetric three-use extension
    exists: dynamics that maximally swaps information across its uses cannot
    be shared across more uses — and therefore can never look memoryless.
    Law-of-process = unlimited shareability of the process. Same identity,
    one level up.

Status: (1),(3) exact; (2) exact algebra vs Monte-Carlo Haar (agreement at
sampling error). The full exchangeable-channel theorem is the road onward.
"""
import numpy as np

rng = np.random.default_rng(31)

I2 = np.eye(2, dtype=complex)
I4 = np.eye(4, dtype=complex)
SWAP = np.eye(4)[[0, 2, 1, 3]].astype(complex)


def haar(n):
    G = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Q, R = np.linalg.qr(G)
    return Q @ np.diag(np.diag(R) / np.abs(np.diag(R)))


def random_channel(d=2, env=3):
    G = rng.normal(size=(d * env, d)) + 1j * rng.normal(size=(d * env, d))
    V, _ = np.linalg.qr(G)                       # isometry C^d -> C^d (x) C^env
    V3 = V.reshape(d, env, d)
    Ks = [V3[:, e, :] for e in range(env)]
    assert np.linalg.norm(sum(K.conj().T @ K for K in Ks) - np.eye(d)) < 1e-10
    return Ks


def apply_channel(Ks, rho):
    return sum(K @ rho @ K.conj().T for K in Ks)


def choi(Ks, d=2):
    v = np.zeros(d * d, dtype=complex)
    for i in range(d):
        v[i * d + i] = 1 / np.sqrt(d)
    P = np.outer(v, v.conj())
    return sum(np.kron(K, np.eye(d)) @ P @ np.kron(K, np.eye(d)).conj().T
               for K in Ks)


def rand_rho(d=2):
    G = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    R = G @ G.conj().T
    return R / np.trace(R)


def dictionary(say):
    for _ in range(4):
        Ks = random_channel()
        J = choi(Ks)
        assert np.linalg.eigvalsh(J).min() > -1e-10           # CP <-> PSD
        # tr over out (first factor): sum_o J[(o,i),(o,i')]
        tr_out = np.einsum("oioj->ij", J.reshape(2, 2, 2, 2))
        assert np.linalg.norm(tr_out - I2 / 2) < 1e-10        # TP <-> marginal
        rho = rand_rho()
        # recovery: Lambda(rho)[o,o'] = d * sum_{i,i'} J[(o,i),(o',i')] rho[i,i']
        Jt = J.reshape(2, 2, 2, 2)
        out = 2 * np.einsum("oipj,ij->op", Jt, rho)
        assert np.linalg.norm(out - apply_channel(Ks, rho)) < 1e-10
    say("  (1) Choi dictionary exact on random channels: CP<->PSD, TP<->marginal,")
    say("      full action recovered from the state. Dynamics are states in disguise;")
    say("      every state theorem — de Finetti included — transfers to processes.")


def symmetry_makes_mixture(say, N=60000):
    # exact: projection onto span{I4, SWAP} (commutant of UxU), no integral
    P = [I4, SWAP]
    G = np.array([[np.trace(a.conj().T @ b) for b in P] for a in P]).real
    Gi = np.linalg.inv(G)

    def twirl_exact(X):
        c = np.array([np.trace(a.conj().T @ X) for a in P])
        coef = Gi @ c
        return coef[0] * I4 + coef[1] * SWAP

    Xs = [rand_rho(4) for _ in range(3)]
    acc = [np.zeros((4, 4), dtype=complex) for _ in Xs]
    for _ in range(N):
        U = haar(2)
        W = np.kron(U, U)
        Wd = W.conj().T
        for k, X in enumerate(Xs):
            acc[k] += W @ X @ Wd
    worst = 0.0
    for k, X in enumerate(Xs):
        worst = max(worst, np.linalg.norm(acc[k] / N - twirl_exact(X)))
    say(f"  (2) symmetry -> mixture: the algebra-defined collective dynamics")
    say(f"      (projection onto the U x U commutant, no integral anywhere) vs the")
    say(f"      sampled mixture of memoryless unitary pairs ({N} Haar draws):")
    say(f"      worst deviation {worst:.4f} — sampling error only. The mixing")
    say(f"      measure emerged; no U was ever chosen. de Finetti, for dynamics.")
    assert worst < 0.05


def swap_monogamy(say):
    d4 = 4
    v = np.zeros(16, dtype=complex)
    for k in range(4):
        v[k * 4 + k] = 0.5                                   # |Phi+> on C4 x C4
    P = np.outer(v, v.conj())
    J = np.kron(SWAP, I4) @ P @ np.kron(SWAP, I4).conj().T   # Choi of SWAP dynamics
    J8 = J.reshape(2, 2, 2, 2, 2, 2, 2, 2)
    # indices: (o1,o2,i1c,i2c ; o1',o2',i1c',i2c'); keep (o1,i2c), trace (o2,i1c):
    M = np.einsum("abcdebch->adeh", J8).reshape(4, 4)
    purity = float(np.real(np.trace(M @ M)))
    phi = np.zeros(4, dtype=complex)
    phi[0], phi[3] = 1 / np.sqrt(2), 1 / np.sqrt(2)
    fid = float(np.real(phi.conj() @ M @ phi))
    pt = M.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)
    min_eig = float(np.linalg.eigvalsh(pt).min())
    say(f"  (3) the singlet of processes: SWAP dynamics' Choi cross-marginal")
    say(f"      (out1 with in2): purity {purity:.6f}, overlap with Phi+ {fid:.6f},")
    say(f"      partial-transpose eigenvalue {min_eig:.3f} < 0 — pure AND entangled.")
    say(f"      Purity decouples any extension, so no symmetric 3-use extension:")
    say(f"      maximally information-swapping dynamics is monogamous — unshareable,")
    say(f"      therefore lawless. Law-of-process = shareability of the process.")
    assert abs(purity - 1) < 1e-10 and abs(fid - 1) < 1e-10 and min_eig < -0.49


def demonstrate(say):
    dictionary(say)
    symmetry_makes_mixture(say)
    swap_monogamy(say)
    say("  moral: the play's quantum law is exactly as real as its shareability.")
    say("         Exchange symmetry manufactures the hidden memoryless law;")
    say("         monogamy marks where no such law can exist. Via Choi, this is")
    say("         the habit bench's identity, promoted to dynamics itself.")


if __name__ == "__main__":
    demonstrate(print)
