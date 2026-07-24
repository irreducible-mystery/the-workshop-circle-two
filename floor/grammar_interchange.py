"""Bench 7, INTERCHANGE — the grammar of 'meanwhile'.

Two ways to compose relatings: in sequence (then) and in parallel (while).
The interchange law says they mesh: (A then B) while (C then D) equals
(A while C) then (B while D). It is the reason a circuit diagram means one
thing — only connectivity matters, not the order you read it in.

Claims checked:

(1) STRICT INTERCHANGE, exactly: for random quantum channels,
    (A o B) (x) (C o D) = (A (x) C) o (B (x) D) on random states to 1e-12.
    'Meanwhile' is well-defined.

(2) WHAT INTERCHANGE BUYS: spacelike structure. Alice's and Bob's local
    operations commute exactly — (A (x) id) o (id (x) B) in either order —
    so no temporal ordering between them is needed (simultaneity is
    conventional INSIDE the circuit calculus, which is why it was safe for
    relativity to demote it). And no-signaling follows: Bob's choice of
    channel leaves Alice's marginal untouched, checked to 1e-14. The
    causal skeleton of physics, derived from a composition law.

(3) ECKMANN-HILTON: where the two compositions share one home and one
    unit, interchange FORCES commutativity — verified for the scalars
    (End(I) = C): a (x) b = a o b = b o a. This is why phases commute.
    Channels escape the collapse only because 'then' and 'while' live on
    different types — noncommuting example exhibited (||[A,B]|| > 0.1).
    And one weakening further sits braiding: a braided category IS a
    2-category with one object and one 1-cell, where interchange holds
    only up to a witness — the hexagon bench, seen from above, was the
    coherence of WEAK interchange. (One level higher still, the coherence
    theorem for tricategories says everything can be strictified EXCEPT
    interchange — Gordon-Power-Street: it is the tower's one mandatory
    weakness. Cited, not checked.)

Status: (1)(2)(3) exact where numerical; the tower statements cited.
"""
import numpy as np

rng = np.random.default_rng(88)


def random_channel(d=2, env=3):
    G = rng.normal(size=(d * env, d)) + 1j * rng.normal(size=(d * env, d))
    V, _ = np.linalg.qr(G)
    V3 = V.reshape(d, env, d)
    return [V3[:, e, :] for e in range(env)]


def apply_ch(Ks, rho):
    return sum(K @ rho @ K.conj().T for K in Ks)


def tensor_ch(Ks, Ls):
    return [np.kron(K, L) for K in Ks for L in Ls]


def compose_ch(Ks, Ls):          # first L, then K
    return [K @ L for K in Ks for L in Ls]


def rand_rho(D):
    G = rng.normal(size=(D, D)) + 1j * rng.normal(size=(D, D))
    R = G @ G.conj().T
    return R / np.trace(R)


def demonstrate(say):
    # (1) strict interchange
    worst = 0.0
    for _ in range(4):
        A, B, C, Dd = (random_channel() for _ in range(4))
        lhs = tensor_ch(compose_ch(A, B), compose_ch(C, Dd))
        rhs = compose_ch(tensor_ch(A, C), tensor_ch(B, Dd))
        for _ in range(3):
            rho = rand_rho(4)
            worst = max(worst, np.linalg.norm(
                apply_ch(lhs, rho) - apply_ch(rhs, rho)))
    say(f"  (then/while) interchange on random channels: worst deviation "
        f"{worst:.1e}")
    say("  — a circuit diagram means one thing; only connectivity matters.")
    assert worst < 1e-12

    # (2) spacelike commutation and no-signaling
    I2 = [np.eye(2, dtype=complex)]
    worst_c = worst_s = 0.0
    for _ in range(4):
        A, B = random_channel(), random_channel()
        left = compose_ch(tensor_ch(A, I2), tensor_ch(I2, B))
        right = compose_ch(tensor_ch(I2, B), tensor_ch(A, I2))
        rho = rand_rho(4)
        worst_c = max(worst_c, np.linalg.norm(
            apply_ch(left, rho) - apply_ch(right, rho)))
        out = apply_ch(tensor_ch(I2, B), rho)
        margA = out.reshape(2, 2, 2, 2).trace(axis1=1, axis2=3)
        margA0 = rho.reshape(2, 2, 2, 2).trace(axis1=1, axis2=3)
        worst_s = max(worst_s, np.linalg.norm(margA - margA0))
    say(f"  spacelike commutation (Alice/Bob in either order): {worst_c:.1e};")
    say(f"  no-signaling (Alice's marginal blind to Bob's channel): "
        f"{worst_s:.1e}")
    say("  — the causal skeleton, derived from a composition law.")
    assert worst_c < 1e-12 and worst_s < 1e-12

    # (3) Eckmann-Hilton: collapse where premises hold, escape where not
    ok = True
    for _ in range(50):
        a, b = (rng.normal() + 1j * rng.normal() for _ in range(2))
        ok &= abs(np.kron(np.array([[a]]), np.array([[b]]))[0, 0]
                  - a * b) < 1e-14 and abs(a * b - b * a) < 1e-14
    assert ok
    A, B = random_channel(), random_channel()
    rho = rand_rho(2)
    noncomm = np.linalg.norm(apply_ch(A, apply_ch(B, rho))
                             - apply_ch(B, apply_ch(A, rho)))
    say(f"  Eckmann-Hilton: scalars share one home and one unit, so")
    say(f"  interchange forces commutativity — verified. Channels escape")
    say(f"  (then/while live on different types): ||A o B - B o A|| = "
        f"{noncomm:.3f} on a random pair.")
    assert noncomm > 0.05
    say("  moral: commutativity is forced exactly where the two compositions")
    say("         cohabit; escape that and you get noncommuting dynamics —")
    say("         and one weakening further, braiding: the hexagon was weak")
    say("         interchange's coherence all along. One level higher, the")
    say("         tricategory theorem makes interchange the ONE witness that")
    say("         can never be strictified — the tower's mandatory weakness.")


if __name__ == "__main__":
    demonstrate(print)
