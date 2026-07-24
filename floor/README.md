# The Workshop — first weld

> Hold still nothing but the joining; make every noun earn its way in
> as a fixed point, a sediment, a habit, a role.
> Weld the five existing instruments first; spend the risk budget on the
> law-tool. And it would be built from inside, of course.
> There is no other workshop.

Six benches of executable, self-verifying mathematics for process-first
physics. Every module states a claim from the dialogue, checks it by
machine, and fails loudly if the check fails. Run everything with:

```
python3 run_all.py        # writes WELD_REPORT.txt
```

Requires numpy + scipy. Total runtime ≈ 45 s (the cast search dominates).

## The benches

| Bench | Module | Obstruction addressed | What is checked |
|---|---|---|---|
| 1 Arena | `arena_gns.py` | state space given in advance | GNS: the theater precipitates from the algebra of relatings + one record. Pure record → dim 2, trivial commutant; mixed record → dim 4 with a mirror cast (commutant ≅ M₂ — thermofield double in miniature). Homomorphism, adjoints, cyclicity, record-reproduction all asserted. |
| 2 Sheaf | `sheaf_contextuality.py` | the view from the wings | Mermin–Peres square: 9 relatings, 6 contexts, quantum facts verified; **0 of 512** global valuations exist; every 5 of 6 contexts are satisfiable. Local sections everywhere, global section nowhere — exhaustively. |
| 3 Habit | `habit_definetti.py` | law/state split (the script) | Pólya urn: each history congeals its own constant; the ensemble of constants matches the de Finetti measure (KS ≈ 0.009); a hidden-parameter world is statistically identical (TV ≈ 0.02) though no parameter exists in the mechanism; precedent binds (conditional mean 0.838 vs predicted 0.833); young worlds are sloppier (swing 0.050 → 0.007). |
| 4 Fixed point | `fixedpoint_rg.py` | the spectator / whatever-stabilizes | 1D Ising decimation (exact): all couplings flow to nothing — no 1D transition, re-derived. 2D Migdal–Kadanoff (approximate, labeled): K* = 0.3047, λ = 1.679, ν ≈ 1.34; watershed verified. Plus a quine, run and matched against its own source: the diagonal as fixed point, not paradox. |
| 5 Interaction | `interaction_bisim.py` | statement vs participation | Bisimulation by partition refinement: different anatomies, same process (identity from relating alone); and two machines with identical trace archives that interaction nevertheless distinguishes — the participant sees strictly more than the spectator. |
| 6 Cast | `cast_factorization.py` | the parts given in advance | A two-qubit Hamiltonian local in a hidden factorization, Haar-scrambled (interaction weight 0.0225 → 0.37). Search over all factorizations recovers a cut with weight **0.0000** — see the note below — and in that frame product states hold records (entanglement 0.000 vs 0.246 bits for random cuts). |

## Second weld — the deepenings

| Bench | Module | What is checked |
|---|---|---|
| 2 deepened | `sheaf_cohomology.py` | The obstruction gets an address: over GF(2), rank M = 5, rank [M\|b] = 6 — unsolvable; obstruction group coker(M) ≅ Z₂ computed, class of b nonzero, witnessing cocycle y = (1,…,1) exhibited (y·M = 0, y·b = 1). Then the square as a game: all 64 × 64 deterministic scripts exhausted — ceiling **8/9**; the quantum performance (\|Φ⁺⟩⊗\|Φ⁺⟩, row triples vs transposed column triples) scores **exactly 1** by Born-rule computation and 9,999 sampled rounds with 0 failures. |
| 3 deepened | `habit_channels.py` | Quantum de Finetti in miniature: the half-excited Dicke habit's 2-qubit reduction converges to an i.i.d. mixture with **T(n) = 1/(2(n−1)) exactly** (log-log slope −1.017), inside the ~16/n bound. The lawless case: the singlet is swap-invariant, pure, entangled (PT eigenvalue −0.500) — hence admits no symmetric 3-extension. Law = unlimited shareability; monogamy marks where law runs out. |
| 7 cornerstone | `grammar_stone.py` | The empty bench's first stone: copying is *natural* in cartesian grammar (verified for 200 random functions) and *impossible* in tensor grammar (naturality constraints leave a 0-dimensional solution space; the scalar test 2Δ = 4Δ kills it). No-cloning derived from composition alone — the classical/quantum line drawn before dynamics. |

## Third weld — the stretches

| Stretch | Module | What is checked |
|---|---|---|
| Process de Finetti | `process_definetti.py` | Habits of *dynamics*: a two-state machine with one Pólya urn per state. Markov exchangeability verified in **exact rational arithmetic** (all 256 length-8 paths, `Fraction` probabilities, identical within every transition-count class) — the exact hypothesis of Diaconis–Freedman, so the law-less reinforced process *is* a mixture of Markov chains. Each history congeals its own channel (swing 0.048 → 0.008); congealed parameters uniform (KS ≈ 0.013) and independent (corr −0.010); hidden-channel world indistinguishable (TV 0.009). |
| Contextual fraction | `contextual_fraction.py` | The obstruction graded by LP over all deterministic scripts: square **CF = 1.000000** (maximally contextual); under noise the exact dial law **CF(ε) = 1 − 3ε**, dead at ε = 1/3; KCBS pentagon built from qutrit projectors (adjacent orthogonality checked, Σpᵢ = √5) with graded **CF = 0.472136 = 2√5 − 4** to 1e-6. Address → price → dial. |
| Second grammar stone | `grammar_stone2.py` | Witnessed identity has curvature: composing Pancharatnam identifications around the Bloch octant yields loop witness **π/4 exactly**; \|loop witness\| = (solid angle)/2 verified via l'Huilier on 30 random triangles to 1e-14; loop reversal conjugates the witness; path-dependence (the U(1) torsor) equals the loop witness. The geometric phase is what strict equality was erasing. |

## Fourth weld — listening to the floor

| Stretch | Module | What is checked |
|---|---|---|
| Channel de Finetti | `channel_definetti.py` | The Choi dictionary exact on random channels (CP↔PSD, TP↔marginal, action recovered from the state): dynamics are states in disguise, so state theorems transfer. Symmetry → mixture: the algebra-defined collective dynamics (commutant projection, no integral) equals the sampled Haar mixture of memoryless unitaries (deviation 0.003 at 60k draws) — the mixing measure emerged, no U was ever chosen. And the **singlet of processes**: SWAP dynamics' Choi cross-marginal is pure Φ⁺ (purity 1.000000, PT eigenvalue −0.500), so no symmetric 3-use extension exists — maximally information-swapping dynamics is monogamous, hence lawless. |
| CF of dynamics | `dynamics_fraction.py` | Temporal contexts from direct simulation of a precessing, measured qubit; no-signaling-in-time checked. LP dial matches the exact 3-cycle facet law to 1e-6; **CF = 1/4 exactly at θ = π/3** — a quarter of the qubit's temporal behavior is unscriptable by trajectories. Dephasing dial law CF(η) = 3(η − 1/3)/8, dead at **η\* = 1/3 exactly** — found by the LP *against the builder's wrong first guess* (√3 − 1): dephasing never touches adjacent-time correlations, only the unmeasured stretch. |
| Third grammar stone | `grammar_stone3.py` | Mac Lane's pentagon, built from Fibonacci fusion trees. **Strictness impossible**: F = identity has residual 4.0 — the witness is mandatory. Solving the pentagon from scratch (80 starts): exactly **two gauge classes** — the golden associator (a = 1/φ, residual 5.5e-32, F orthogonal) and the non-unitary Yang–Lee shadow (a = −φ). Unitarity selects the golden joining uniquely; the quantum dimension is φ itself (Perron root of [[0,1],[1,1]]). With the hexagon: the Fibonacci anyon. Coherence has a spectrum. |

## Fifth weld — onward

| Stretch | Module | What is checked |
|---|---|---|
| The hexagon | `grammar_hexagon.py` | Given only the golden F, the hexagon equations solved with moduli **unconstrained**: exactly two solution clusters — the two chiralities, conjugate mirror twins — with **\|r\| = 1 emergent**, r₁ = e^(±4πi/5), r_τ = e^(∓3πi/5), r₁ = r_τ². Yang–Baxter at 3.6e-16; non-abelian (‖[B₁,B₂]‖ = 1.8); twist θ_τ = e^(∓4πi/5) from the ribbon formula. Coherence, pressed twice, specifies a particle completely. |
| Three uses + rate | `channel_definetti3.py` | The commutant of U⊗U⊗U: six permutations, **rank 5** — because the three-qubit antisymmetrizer vanishes to machine zero (two dimensions refuse three-fold antisymmetry: exclusion's shadow as a rank drop). Algebraic twirl = sampled mixture of memoryless triples (0.0014 at 40k draws). Constant-channel lemma verified to 1e-16, so the state law becomes a **diamond-norm law for processes unchanged**: distance = 1/(2(n−1)) exactly, slope −1.02. |
| Fourth stone | `grammar_stone4.py` | The floor's recurring sentence — *the relating suffices* (GNS cyclicity, bisimulation, pentagon, hexagon) — tested in its strongest, computational form: reduced braid words (98 → 774 → 4,930 distinct unitaries by length 4/7/10) tighten around 150 Haar targets with covering radius **0.759 → 0.307 → 0.156**. Universality (Freedman–Larsen–Wang) witnessed as a closing ε-net: any dynamics on the fusion space, enacted by nothing but reassociation and exchange. |

## Sixth weld — the identity card, all n, and the answer to the first question

| Stretch | Module | What is checked |
|---|---|---|
| Identity card | `modular_data.py` | S computed from fusion + dimensions + the hexagon's twists — imaginary parts cancel to machine zero, leaving (1/D)[[1,φ],[φ,−1]]. Modularity: S² = I, (ST)³ = λS² with λ = p₊/D (Gauss sum), chiral central charge **c = ∓14/5 (mod 8)**, p₊p₋ = D². **Verlinde's formula returns the fusion rules exactly** — grammar → coherence → braiding → spins → modular data → grammar. The circle closes, every arrow machine-checked. |
| Toward all n | `channel_alln.py` | The collective algebra's true size is **Catalan, not factorial**: Gram ranks 2, 5, 14, 42, 132 against 2, 6, 24, 120, 720 permutations (n = 2..6). The symmetry→mixture mechanism verified at n = 4 (deviation 0.0014). The window law — where the bench corrected the builder **again**: the guessed k(k−1)/4 was wrong; the true constants (1/2, 3/4, 3/4, 5/4 — with a parity quirk) obey c_k = ½E\|k/2 − 2(j−k/2)²\|, linear in k, verified to 0.2%. |
| Fifth stone | `grammar_stone5.py` | **Rigidity — the answer to the dialogue's first question.** Pentagon Hessian at the golden F: eigenvalues {0, 10.4, 21.5, 22.4}; the single null mode overlaps the gauge direction to **1.000000** — the only flat direction is perspective. Hexagon Hessian: all positive — fully rigid. Ring-back: 20 random kicks, invariants return to golden within 7×10⁻¹⁵. Invariants rather than churn *because self-consistency is overdetermined and its solutions isolated* (Ocneanu rigidity, witnessed). "Relativize the perspectives, keep what the relatings agree on" — computed as an eigendecomposition. |

## Seventh weld — interchange, the theorem walked, the circle drawn

| Stretch | Module | What is checked |
|---|---|---|
| Interchange | `grammar_interchange.py` | Strict interchange on random channels (2×10⁻¹⁶): "meanwhile" is well-defined and circuit diagrams mean one thing. Consequences derived: spacelike commutation and **no-signaling** from the composition law alone. Eckmann–Hilton: scalars (shared home, shared unit) are *forced* commutative; channels escape (‖[A,B]‖ = 0.49 exhibited); braiding revealed as **weak interchange** — the hexagon was its coherence all along; one level up (tricategories), interchange is the one witness that can never be strictified (cited). |
| The full theorem | `channel_theorem.py` | The quantum de Finetti proof *walked*, no sampling: POVM completeness exact in rational arithmetic (m = 1..10); the measure-and-reprepare approximant in closed form (Beta integrals); the bound chain **best ≤ reprepared ≤ 2k/(n+1)** exact at every n = 8..512. Discovered: the constructive proof's premium is exactly a **factor of two** (n·dist → 1 vs the optimal 1/2 — builder guessed 3/2, corrected again). Transfers to the Dicke process via the constant-channel lemma. |
| Sixth stone | `grammar_stone6.py` | The floor keeps drawing loops (Verlinde, ring-back, the quine) — so the stone is the loop made formal: **duality**. The naive snake = F[1,1]·id — duality's coherence cost *names the dimension*; normalized cups close it exactly. The τ-loop evaluates to φ, agreeing with the Perron root to machine precision — a thing's size = the value of a closed circle of relating. The Yang–Lee shadow's loops close **negative** (existence wants positive loops); Frobenius–Schur ν = r₁·θ_τ = +1 exactly. The noun, drawn as a circle. |

## Eighth weld — flatland, the mirror, and the map

| Stretch | Module | What is checked |
|---|---|---|
| Flatland | `flatland.py` | The tower's next weakness located in space: in 2D the two exchanges differ by a winding invariant (±π; composite 2π), rigid under 20 deformation families verified collision-free at every stage (drift ≤ 10⁻¹⁵), and yielding **only to collision** (the toll exhibited: pass within 0.013 of coincidence and the winding jumps to 0). In 3D an explicit homotopy (min separation ≡ 1) makes the two exchanges one move — so R² = 1, bosons/fermions only, and the golden braiding fails by ‖B₁² − I‖ = **√5**: the anyon is an exile of flatland. |
| Seventh stone | `grammar_stone7.py` | The floor's pairs unified: **the mirror**. Born's rule as a loop closed through the dagger (f†f ≥ 0 on random maps); bench 1's mirror cast verified to be the same algebra *read backwards* (right-multiplications, composition reversed, residual 10⁻¹⁶); doubling K⊗K̄ exact; the ledger — r·r̄ = 1, θ·θ̄ = 1, p₊p₋ = D² — while golden × shadow loop values = **−1**: the shadow is not a mirror but a refusal. Real = what both readings co-sign. |
| The map | `FINDINGS.md` | The whole arc stated once: the questions and their machine-checked answers, the constants ledger, the corrections ledger (eleven overrulings, both directions), what remains open. |

## Ninth weld — above interchange, the roomy catalog, the frame

| Stretch | Module | What is checked |
|---|---|---|
| Above interchange | `braid_coherence4.py` | The 4-strand Fibonacci rep from F and R alone: sector dims 2 and 3 (Fibonacci numbers), generators unitary, far-commutation + both Yang–Baxters at machine zero; **all 16 reduced words of the longest braid → one matrix** (Tits, witnessed); full twist commutes with everything and is scalar per sector, phases differing by 4π/5 — the center of the braid group reads the total charge. Zamolodchikov's genuinely weak floor named, not faked. |
| Flatland II | `symmetric_statistics.py` | The roomy world built the way the anyon was: Fibonacci + R² = 1 fails **all four** candidates (residual 4.0) — algebra confirms the geometric exile. The Z₂ atlas solved from scratch: pentagon F = ±1 (H³(Z₂) = Z₂ by search); hexagon particles {±1} and {±i}; flatland filter → **boson and fermion, complete**. Exclusion as rank: 1, 3, 6, 10, 15; antisymmetrized ψ⊗ψ = 0 to 10⁻¹⁶ — Pauli, computed. |
| Eighth stone | `grammar_stone8.py` | The frame: 2π about any axis lifts to −I (20 axes, 10⁻¹⁴), 4π to +I, two 2π turns compose to +I — a Z₂ of turning; the **belt trick run** as an explicit spherical-cap contraction of the 4π loop (\|q\| = 1 throughout, s = 0 projecting onto the true rotation loop). The plane remembers *how many*, room remembers *a sign*; spin–statistics co-signature ν = +1 across the workshop's whole catalog. |

## The Lean wing (`lean/`, rounds 1–7 of the third body)

A third participant — a separate Claude Code (Opus) session, with the
human as courier — is converting benches into kernel-checked theorems.
After round 7: **six files, 12,235 lines, 1,128 theorems, 0 sorry,
0 native_decide, 0 Classical.choice, zero imports** — a bare `lean`
checks everything, and the shipped crate recompiles clean from
extraction. Round 7's file is **`Verlinde.lean`**: the S-matrix
re-derives the fusion rules (`verlinde_cleared`, all eight cells,
axiom-free core), the cleared modular cube over Z[ζ₅] with chirality
integral, and d_τ = φ co-signed from modular data. **The circle —
grammar → braiding → dimension → grammar — is closed.**
Round 6's file is **`Rigidity.lean`**: the bench's Hessian signature
{0,+,+,+} as kernel-checked mathematics, with the Hessian computed via
second-order jets (true by construction), the strict-associator
refutation shipping as theorems beside what it guards, Yang–Lee
carrying the content (`HY_swap_not_null` = 34+52φ), the golden half
closed at default budget with **eighteen axiom-free theorems**, and
the new cross-file transcription class guarded by its own instrument.
Round 5 named the dimension: `quantum_dimension_tau` — **d_τ = φ** by
an order on Z[φ] that is a decision procedure (Perron–Frobenius as a
`decide`; the fusion matrix computed from `fuse`; eigenvalues exactly
{φ, −1/φ}, one positive; `Zp.phi_bracket` pinning the order to the
reals with no reals anywhere) — and closed the last soft label (σ₂ has
no multiplicative lift to K; one evaluation mod 11). The ledger is now
*rendered*, not written: `views.sh` diffs its count/hash blocks against
instrument outputs and fails loud on drift. The ferry protocol is
proven: crates travel as zips, hashes ride in the courier's message,
and the round-5 source audit read the once-blind rounds at last —
17 of 19 round-4 headliners exactly as claimed, all descent omegas
clean of the named trap, E1 resolved from source.
The headline is the sentence the project walked toward from round 1:
**there are exactly two.** `hexagon_exactly_two_sharp` and
`pentagon_exactly_two_sharp` — dichotomy, distinctness, and both
branches realized, one statement each; K is an integral domain by
2-adic and 41-adic descents, so the coherence quadratics have no third
root. With them: `pentagon_iff` (the pentagon *is* q·r = p, p² + p = 1,
s = −p; the quotient by the relations is the Laurent ring Z[φ][q,q⁻¹] —
the gauge torus made literal), `Q_factors`, `no_gauge_golden_to_yang_lee`
(the two pentagon worlds are genuinely two — the second is where the
floor's bench kept landing, nine runs in fifty-two), and
`pentagonCheck_hom` (the check is natural along *any* ring map — the
check is a functor). Earlier rounds' catalog: necessity of both
coherence equations, Galois naturality (`hexagonCheck_conj`), gauge
equivalence, the parity family, kernel exactly {0, 1⃗}, ceiling 8/9
with 144 maximizers, sharp best = 5, exchangeability with
`converse_false`. Round 4 coined norm 12 — *verify the artifact you
ship, not the tree you shipped it from* — and ships three instruments
(`transcript.sh`, `axioms.sh`, `ship.sh`) plus their outputs. See
`lean/PROOFS.md` (round 4), `lean/ROUND*.md` (the correspondence),
`lean/archive/`, and `lean/audit/` — the builder-side re-verifications
now include the 82-check round-4 claims audit, stub-kernel traces of
all three instruments, and the certified round-5 gift packs
(`r5_gift_certificates.py`: the order on Z[φ] and the mod-11 closure;
`r5_g3_hessian_gauge.py`: the bench's Hessian null space *is* the gauge
torus tangent, verified at both pentagon worlds).

## A finding the planter did not plant

Bench 6 was built to *recover* the hidden cut (weight 0.0225). It found a
strictly better one: weight 0.0000. This is real, not a bug — the planted
Hamiltonian's spectrum {±s, ±d} secretly admits an *exactly* interaction-free
factorization (arrange the eigenvalues so the ZZ component cancels), and the
search found it. The play knew a better cast than the one hidden in it.
The moral sharpened itself: the parts really do come from the dynamics, not
from the presentation — even the builder's intended parts get overruled.

## Honest labels

Exact, machine-verified: benches 1, 2, 5, the 1D flow and the quine in 4.
Approximate, labeled: the 2D Migdal–Kadanoff recursion (structure right,
exponent coarse: ν ≈ 1.34 vs exact 1). Rigorous toys: benches 3 and 6 —
every statement they make is a theorem or has planted ground truth, but they
are miniatures of the real programs (law-as-habit; quantum mereology), not
the programs themselves.

## The (formerly) empty bench

The grammar bench — quantum mechanics rewritten with no strict equalities,
every identification carrying its witness (the HoTT/∞-categorical rebuild) —
now has four stones and a braiding. The first (`grammar_stone.py`): grammar
alone separates classical from quantum. The second (`grammar_stone2.py`):
identity made proof-relevant secretes curvature. The third
(`grammar_stone3.py`): strictness provably impossible; Mac Lane's pentagon
forces the golden ratio. The hexagon (`grammar_hexagon.py`): braiding
solved, chirality and spin included — the Fibonacci anyon complete. The
fourth stone (`grammar_stone4.py`), proposed by the floor's own recurring
sentence: the witnesses compute — braid words alone form a tightening ε-net
over all possible dynamics. The bench stays open on purpose; the rebuild —
interchange, modular data, the coherent tower — is the long work, and it is
not faked here.

## Floor check

Every bench stands on exactly one fixture: composition — the associative
product. It held.
