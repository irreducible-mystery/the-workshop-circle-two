#!/usr/bin/env python3
"""SEAT B — blind exact reimplementation of the S5 statements
(Zi_statements_v6.txt, sha256 1071e8541e39…8735), statements only.

The twist layer. Method as S1–S4: exact integer arithmetic, no floats.
Symbolic claims (the ribbon identity, the fork locus, the char-poly
factorization) verified coefficientwise in the polynomial ring
Z[i][rr, ri] (r = rr + ri·i, two commuting indeterminates); the
fork-locus iff additionally re-derived through an INDEPENDENT
coordinate route (expand both ledgers in re/im and compare — not seat
P's cancellation route). Finite nests (4 fusion cells per particle,
the 4-entry catalog fork, the 2×2 fusion matrix) exhausted and tied
per norm 9.

Definitions transcribed from statements v6 ALONE: twist r a = Rz2 r a a,
nuFS r = mul r r, nuML r = mul r (conj r), with Rz2/conj/mul from the
def-blocks the courier shipped. Blindness boundary held: definitions
and claims in, verdicts out.
"""
import sys

CHECKS = []


def check(name, ok, note=""):
    CHECKS.append((name, bool(ok)))
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  — {note}" if note else ""))


# ── exact Gaussian integers ─────────────────────────────────────────────────
def gadd(z, w):
    return (z[0] + w[0], z[1] + w[1])

def gneg(z):
    return (-z[0], -z[1])

def gsub(z, w):
    return gadd(z, gneg(w))

def gmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])

def gconj(z):
    return (z[0], -z[1])

def gnorm(z):
    return z[0] * z[0] + z[1] * z[1]

G_ZERO, G_ONE, G_I = (0, 0), (1, 0), (0, 1)
G_MONE, G_MI = (-1, 0), (0, -1)


# ── polynomials over Z[i] in TWO indeterminates rr, ri ──────────────────────
def pclean(p):
    return {k: v for k, v in p.items() if v != G_ZERO}

def pconst(g):
    return {(0, 0): g} if g != G_ZERO else {}

P_ZERO, P_ONE = {}, pconst(G_ONE)
P_R = {(1, 0): G_ONE, (0, 1): G_I}          # r = rr + ri·i
P_RCONJ = {(1, 0): G_ONE, (0, 1): G_MI}     # conj r = rr − ri·i

def padd(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = gadd(out.get(k, G_ZERO), v)
    return pclean(out)

def pneg(p):
    return {k: gneg(v) for k, v in p.items()}

def psub(p, q):
    return padd(p, pneg(q))

def pmul(p, q):
    out = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = (k1[0] + k2[0], k1[1] + k2[1])
            out[k] = gadd(out.get(k, G_ZERO), gmul(v1, v2))
    return pclean(out)

def peq(p, q):
    return pclean(p) == pclean(q)


# ── S5 definitions, transcribed from statements v6 ──────────────────────────
def Rz2(r, x, y):
    """def Rz2: if x = 1 ∧ y = 1 then r else one — concrete Gaussian"""
    return r if (x == 1 and y == 1) else G_ONE

def Rz2_poly(rp, x, y):
    return rp if (x == 1 and y == 1) else P_ONE

def twist(r, a):
    """def twist r a = Rz2 r a a"""
    return Rz2(r, a, a)

def twist_poly(rp, a):
    return Rz2_poly(rp, a, a)

def nuFS(r):
    """def nuFS r = mul r r"""
    return gmul(r, r)

def nuML(r):
    """def nuML r = mul r (conj r)"""
    return gmul(r, gconj(r))

CATALOG = {"boson": (G_ONE, G_ONE), "fermion": (G_ONE, G_MONE),
           "semion": (G_MONE, G_I), "anti-semion": (G_MONE, G_MI)}

# ═══ twist values per particle ══════════════════════════════════════════════
print("-- twist values --")
check("twist_catalog_label1",
      twist(G_ONE, 1) == G_ONE and twist(G_MONE, 1) == G_MONE and
      twist(G_I, 1) == G_I and twist(G_MI, 1) == G_MI,
      "θ = R at label 1: +1, −1, +i, −i")
check("twist_catalog_label0",
      all(twist(r, 0) == G_ONE for _, (f, r) in CATALOG.items()),
      "θ trivial at the vacuum label")
check("twist_fermion_minus_one", twist(G_MONE, 1) == G_MONE,
      "THE sign — the fermion's twist is −1")

# ═══ the ribbon identity — symbolic route ═══════════════════════════════════
print("\n-- ribbon (symbolic in r) --")
# θ((a+b)%2) = θ(a)·θ(b)·R(a,b)² on the 4 fusion cells; three cells are
# polynomial identities in r, the (1,1) cell reads 1 = r⁴
trivial_cells, forcing_cells = [], []
for a in range(2):
    for b in range(2):
        lhs = twist_poly(P_R, (a + b) % 2)
        rab = Rz2_poly(P_R, a, b)
        rhs = pmul(pmul(twist_poly(P_R, a), twist_poly(P_R, b)),
                   pmul(rab, rab))
        (trivial_cells if peq(lhs, rhs) else forcing_cells).append((a, b))
check("ribbon_nest_3_plus_1",
      len(trivial_cells) == 3 and forcing_cells == [(1, 1)],
      f"trivial cells {trivial_cells}; forcing cell {forcing_cells} — "
      "3 + 1 = 4")
# the forcing cell is exactly 1 = r⁴:
R4 = pmul(pmul(P_R, P_R), pmul(P_R, P_R))
lhs11 = twist_poly(P_R, 0)
rhs11 = pmul(pmul(twist_poly(P_R, 1), twist_poly(P_R, 1)),
             pmul(Rz2_poly(P_R, 1, 1), Rz2_poly(P_R, 1, 1)))
check("ribbon_forcing_cell_is_r4",
      peq(lhs11, P_ONE) and peq(rhs11, R4),
      "(1,1) cell: lhs = 1, rhs = r⁴ coefficientwise")

# catalog_r_fourth: r² = f ∧ f² = 1 ⟹ r⁴ = 1 — substitution chain,
# verified on all four catalog pairs AND symbolically ((r²)² = r⁴):
check("catalog_r_fourth",
      peq(pmul(pmul(P_R, P_R), pmul(P_R, P_R)), R4) and
      all(gmul(gmul(r, r), gmul(r, r)) == G_ONE
          for _, (f, r) in CATALOG.items()) and
      all(gmul(r, r) == f and gmul(f, f) == G_ONE
          for _, (f, r) in CATALOG.items()),
      "r² = f, f² = 1 hold per particle; r⁴ = (r²)² = f² = 1 — the "
      "ribbon hypothesis discharged by the S3+S4 layers")

# live ribbon, all four particles, all cells:
ribbon_live_ok = all(
    twist(r, (a + b) % 2)
    == gmul(gmul(twist(r, a), twist(r, b)),
            gmul(Rz2(r, a, b), Rz2(r, a, b)))
    for _, (f, r) in CATALOG.items() for a in range(2) for b in range(2))
check("live_ribbon_all_four", ribbon_live_ok,
      "4 particles × 4 cells = 16 ribbon instances, all exact")

# ═══ the two ν-ledgers and the fork ═════════════════════════════════════════
print("\n-- the fork (charter flag 3) --")
check("nu_survivors_plus_one",
      nuFS(G_ONE) == nuML(G_ONE) == G_ONE and
      nuFS(G_MONE) == nuML(G_MONE) == G_ONE,
      "both ledgers +1 on boson and fermion")
check("nu_fork_on_semions",
      nuFS(G_I) == G_MONE and nuML(G_I) == G_ONE and
      nuFS(G_MI) == G_MONE and nuML(G_MI) == G_ONE,
      "ν_FS = −1 vs ν_ML = +1 on BOTH semions — the fork, exact")
agree = [n for n, (f, r) in CATALOG.items() if nuFS(r) == nuML(r)]
diverge = [n for n, (f, r) in CATALOG.items() if nuFS(r) != nuML(r)]
check("fork_nest_2_plus_2",
      len(agree) == 2 and len(diverge) == 2 and
      sorted(agree) == ["boson", "fermion"],
      f"agree {sorted(agree)} + diverge {sorted(diverge)} = 4")

# fork locus — INDEPENDENT coordinate route (not seat P's cancellation):
# nuFS − nuML = r² − r·conj(r) = r(r − conj r) = r · (0, 2·im)
# = (−2·re·im·i·i? ...) expand coefficientwise:
diff = psub(pmul(P_R, P_R), pmul(P_R, P_RCONJ))
# expected: r·(r − conj r) = (rr + ri·i)(2·ri·i) = 2·rr·ri·i + 2·ri²·i²
#         = −2·ri² + 2·rr·ri·i
expected = {(0, 2): (-2, 0), (1, 1): (0, 2)}
check("fork_locus_coordinate_route",
      peq(diff, expected),
      "ν_FS − ν_ML = −2·ri² + 2·rr·ri·i coefficientwise — vanishes iff "
      "ri = 0 (both coords zero ⟺ ri² = 0 ∧ rr·ri = 0 ⟺ ri = 0, no "
      "nonzero-r needed for THIS direction); independent of seat P's "
      "cancellation route")
# the iff as stated (with r ≠ 0), checked on a grid + the zero control:
grid_ok = all(
    ((nuFS((x, y)) == nuML((x, y))) == (y == 0))
    for x in range(-5, 6) for y in range(-5, 6) if (x, y) != (0, 0))
check("fork_locus_is_real_locus_grid", grid_ok,
      "for r ≠ 0 on [−5,5]²: ledgers agree ⟺ im = 0 — 120 points, "
      "secondary to the coordinate route")
check("filter_closes_fork",
      all(nuFS((x, 0)) == nuML((x, 0)) for x in range(-10, 11)),
      "conj-fixed r (real) ⟹ ledgers coincide — the filter closes "
      "the fork")

# nuML is the norm:
check("nuML_is_normSq",
      all(nuML((x, y)) == (gnorm((x, y)), 0)
          for x in range(-5, 6) for y in range(-5, 6)) and
      peq(pmul(P_R, P_RCONJ), {(2, 0): G_ONE, (0, 2): G_ONE}),
      "r·conj(r) = rr² + ri² coefficientwise (= ⟨N(r), 0⟩) — the "
      "mirror ledger IS the norm")
check("nuML_blind_on_units",
      all(nuML(r) == G_ONE for _, (f, r) in CATALOG.items()),
      "ν_ML = +1 on all four norm-1 units — structurally blind to the "
      "semions; only ν_FS separates")

# ═══ spin-statistics seed ═══════════════════════════════════════════════════
print("\n-- spin-statistics seed --")
check("spin_statistics_seed",
      twist(G_MONE, 1) == G_MONE and
      gmul(G_MONE, twist(G_MONE, 1)) == G_ONE and
      gmul(G_ONE, twist(G_ONE, 1)) == G_ONE,
      "θ_f = −1; R·θ = +1 on both survivors — the seed, exact")
check("spin_equals_statistics",
      all(twist(r, 1) == r for _, (f, r) in CATALOG.items()),
      "θ = R per particle: spin and statistics are the same Gaussian "
      "integer (abelian collapse)")
Nf = [[0, 1], [1, 0]]
Nf2 = [[sum(Nf[i][k] * Nf[k][j] for k in range(2)) for j in range(2)]
       for i in range(2)]
check("fusion_matrix_squares_to_identity",
      Nf2 == [[1, 0], [0, 1]] and 1 * 1 + 1 * 1 == 2,
      "N_f² = I entrywise; D² = 1² + 1² = 2")
# char-poly factorization x² − 1 = (x−1)(x+1) symbolically over Z[i][x]:
P_X = {(1, 0): G_ONE}
cp_lhs = psub(pmul(P_X, P_X), P_ONE)
cp_rhs = pmul(psub(P_X, P_ONE), padd(P_X, P_ONE))
check("dimension_charpoly_factors", peq(cp_lhs, cp_rhs),
      "x² − 1 = (x−1)(x+1) coefficientwise over Z[i][x]")

# ═══ live off-catalog + negative controls ═══════════════════════════════════
print("\n-- live + controls --")
check("live_fork_off_catalog",
      nuFS((1, 1)) == (0, 2) and nuML((1, 1)) == (2, 0),
      "r = 1+i: ν_FS = 2i ≠ 2 = ν_ML — the locus theorem live off the "
      "catalog (non-unit, non-real)")
check("control_fork_locus_needs_nonzero",
      nuFS(G_ZERO) == nuML(G_ZERO) == G_ZERO and gconj(G_ZERO) == G_ZERO,
      "r = 0: both ledgers vanish; cancellation needs the domain — "
      "the r ≠ 0 hypothesis earns its keep")
check("control_wrong_twist_breaks_ledger",
      gmul(G_I, gconj(G_MONE)) == G_MI != G_ONE,
      "θ = F (wrong) on the semion: R·conj(θ) = −i ≠ +1 — a wrong "
      "twist is visible in the ledger")
r2 = (2, 0)
check("control_ribbon_forcing_bites",
      twist(r2, 0) != gmul(gmul(twist(r2, 1), twist(r2, 1)),
                           gmul(Rz2(r2, 1, 1), Rz2(r2, 1, 1))) and
      twist(r2, 1) == gmul(gmul(twist(r2, 0), twist(r2, 1)),
                           gmul(Rz2(r2, 0, 1), Rz2(r2, 0, 1))),
      "r = 2: the (1,1) cell fails (1 ≠ 16) while (0,1) holds — the "
      "forcing cell carries content")
check("control_nuFS_separates",
      nuFS(G_ONE) == nuFS(G_MONE) == G_ONE and
      nuFS(G_I) == nuFS(G_MI) == G_MONE,
      "ν_FS: {+1, +1, −1, −1} — separates survivors from semions, the "
      "separation ν_ML cannot make")

# ═══ PLANT (norm 16 hygiene) ════════════════════════════════════════════════
print("\n-- plant --")
# mutated twist: θ_a = R(a, 0) — trivial everywhere; the semion's
# ν_FS would become i·1 = i, not −1: the instrument must notice
def twist_mutant(r, a):
    return Rz2(r, a, 0)

mutant_fork_visible = (gmul(G_I, twist_mutant(G_I, 1)) == G_MONE)
check("plant_mutant_twist_caught", not mutant_fork_visible,
      "θ = R(a,0) mutant gives semion R·θ = i ≠ −1 — a wrong twist "
      "definition cannot reproduce the fork values; the instrument bites")

# ── verdict ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 68)
npass = sum(1 for _, ok in CHECKS if ok)
nfail = len(CHECKS) - npass
print(f"checks run: {len(CHECKS)};  passed: {npass};  failed: {nfail}")
if nfail == 0:
    print("VERDICT: every S5 claim re-derived — ribbon and char-poly")
    print("         coefficientwise in Z[i][rr, ri]; the fork locus by an")
    print("         independent coordinate route (ν_FS − ν_ML expanded,")
    print("         not cancelled); both ledgers named apart and computed;")
    print("         nests exhausted and tied; the plant bitten.")
    print("EXIT: 0")
    sys.exit(0)
else:
    print("VERDICT: NOT CLEAN")
    print("EXIT: 1")
    sys.exit(1)
