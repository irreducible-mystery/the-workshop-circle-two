# DUAL-SEAT EXPERIMENT — SUB-ROUND 7 REPORT: THE META-AUDIT AND THE GATE-SCOPE EXTENSION (S7c)

**Quarantined per norm 16; REGISTER row 7. This sub-round is the work of
the SECOND instance of the meta-auditor seat, picking the experiment up from
the predecessor's Round-Three handoff.**

**SANCTIONED SCOPE DIVERGENCE, recorded loudest-first (norm 4).** The
predecessor's `HANDOFF-ROUND3.md` recommended **S7a-first** — prove the G1c
slice lemma before touching the prose gates. This seat, after the stranger
audit, recommended **S7c-first**: the row-8 characterization slip the audit
flagged lives where no instrument scans, so the scanning gap is the sharper
thing to close first. Kelly chose this seat's recommendation verbatim —
*"charge for Round Three — S7c+S7a (your rec) please."* This divergence is
recorded here, in the source header of every changed gate, and in the
S7c corrections letter.

## What S7 is (this report covers the meta-audit and S7c)

Three movements, shipped in order.

**The inheritance verification (Phase 0).** Every mechanical claim in the
handoff was measured, not trusted: the pins match to 64 characters, the
kernel compiles at exit 0 and zero bytes (norm 10), the axiom census is
161/161 covered with 0 sorryAx and 0 Classical.choice, the courier
re-extraction is byte-identical, all six blind verifiers exit 0, and the
norm-16 plant/restore bites the capstone and restores clean. Recorded in
`STRANGER-WORKLOG.md`. Inheritance verified with no discrepancy.

**The stranger audit (Phase 1).** Statements read before prose; an
independent blind verifier (`seatMETA/verify_stranger.py`, 27/27, own routes,
which caught three of my OWN bugs before it caught anything else) written
before the six seat-B verifiers were opened; then the prose read in handoff
order and audited. Verdict in `STRANGER-AUDIT-ROUND3.md`: the REGISTER row-8
prediction is CONFIRMED — a characterization slip does exist, in the
front-door `README.md` ("the Z₂ catalog **complete over Z[i]**", an unearned
universal in a true-shaped sentence), and the courier's truncation of
inline-`let` statements (findings F1/F2) is a shared blind spot no report or
letter mentions. No mathematical defect; the bench negative control
(worst residual = 4 exactly) passed clean.

**S7c — the gate-scope extension.** The front-door prose gates
(`c2_pointers`, `c2_numerals`, `c2_views/censusguard`) scanned only
top-level `*.md` + `letters/**`; `experiment/**` — the row-8 boundary, 37
markdown files, 110+ tracked files — was scanned by nothing. S7c moves the
boundary to include `experiment/**`, taught (not brute-forced) to resolve the
experiment's own citations.

## How S7c was built (norm 15 first, norm 16 both directions)

Design measured BEFORE any edit. `audit/probes/s7c_scope_probe.sh` and
`audit/probes/S7C-DESIGN-NOTE.md` record the blast radius and name the
adjudicator (the four gates themselves, run on the extended scope). The
design note declares, up front, what the extension does NOT do: the gates are
resolve/value/proximity-level and cannot judge meaning.

The pointer gate was taught the experiment's resolution sources so grounded
citations resolve mechanically rather than by exemption: Lean declaration
names harvested from `experiment/**/*.lean`; artifact pins harvested from the
experiment pin ledger `experiment/PIN-TRACKER.md` with BIDIRECTIONAL prefix
agreement (a report cites the full 64-char hash, the ledger records a 12-char
prefix — same pin, two lengths); and slashed paths resolved relative to both
the experiment root and the directory of the citing document. The
overwhelming majority of citations cleared this way; the small remainder
carry reasoned exemptions, each naming why the reference is not an in-tree
artifact (Lean stdlib vocabulary, external tools, git branch names, courier
zips, cross-references to the absent front-door tree, historical names from
superseded sub-rounds, evidentiary hashes of build products deliberately not
tracked, and prose-elision fragments).

The numeral gate harvests the experiment's own instrument values (verifier
and census output logs, the pin ledger, the statements files) into its known
set, and its line-citation stripper was extended for `file.ext:line` and
`L`-prefixed forms. Every number that could not be sourced from an instrument
carries a reasoned exemption, and **every exempted number was verified true
before it was exempted** — the cumulative blind-check total was verified equal
to the sum of the six verifiers' rendered counts (47+24+32+36+25+23 = 187);
the v7 statements line count was verified by `wc -l` (615); the census split
was verified internally consistent (68 axiom-free + 93 rest = 161 total).

The censusguard, whose front-door subject `lean/Zi.lean` is absent on this
branch, now falls back to the experiment's prover artifact
`experiment/seatP/Zi.lean`. It passes clean there (the header points at the
census rather than restating it) and its six proximity false-positives — a
vertex label, the certified antisymmetrizer ranks [1,3,6,10,15], line-range
tails — are each labeled with a verified reason.

**Every extended instrument was planted and restored (norm 16, both
directions), the plants placed INSIDE `experiment/**`:** a dangling theorem
name and a bogus pin for the pointer gate; a bare unsourced count for the
numeral gate; a fabricated stale census in the Lean header for censusguard.
Each was bitten (exit 1, named finding); each restore was verified clean and
byte-identical. Two near-misses on my OWN instruments are recorded in the
corrections letter loudest-first (a `/tmp`-run empty-exemption forecast; an
apostrophe in an awk comment that crashed the gate into a false PASS).

## The result

On this tree: **pointers PASS** (every doc scanned, zero unresolved),
**numerals PASS** (zero unsourced), **censusguard PASS** on the experiment
prover artifact,
**tree PASS**. The two Lean-binary gates (`c2_axioms`, the `c2_views` ledger
renderer) are SKIPPED→FAIL by the chain's own rule "a gate that cannot run is
not a gate that passed," because the front-door `lean/` wing is absent on
this branch — a pre-existing branch condition, not an S7c change.

## The honest boundary — what S7c does NOT close

There are TWO gaps, and S7c closes only one.

The **scanning gap** (closed): `experiment/**` prose was under no instrument;
it is now under the resolve/value/proximity gates, for the classes those
gates can check. Findings F1/F2's "never scanned" surface is scanned.

The **meaning gap** (NOT closed, and not closeable by scope): the row-8 slip
"complete over Z[i]" lives in the top-level `README.md`, which was ALREADY in
scope before S7c. The gates scanned that line and passed it, because every
token resolves, every number sources, and no proximity trips — the slip is a
MEANING miss, an unearned universal in a true-shaped sentence. No scope change
confers meaning-checking. That miss stays with the audit loop (REGISTER class
7), where it belongs. Gates green does not mean characterization sound, and
this report says so plainly so no reader mistakes the one for the other.

## Pins (full 64-char)

| artifact | sha256 |
|---|---|
| `audit/c2_pointers.sh` (S7c) | see PIN-TRACKER block below |
| `audit/c2_numerals.sh` (S7c) | see PIN-TRACKER block below |
| `audit/c2_views.sh` (S7c) | see PIN-TRACKER block below |
| `seatP/Zi.lean` (unchanged, Phase-0 verified) | `b7ef35425e13b740e253892916fffb8a6ed5adddaa08a1bbe01360b77fcdba5e` |
| `seatMETA/verify_stranger.py` | `cf603918357dd97cc902a40f8c8e99b0e82c6e2e6ec87d92751b7f03c8720efe` |

Full 64-char hashes of the changed gates are listed in the PIN-TRACKER Round
Three block, measured on the shipped artifacts. No statement in
`seatP/Zi.lean` changed; its pin before and after the censusguard plant/restore
is identical, and identical to the Phase-0 inheritance pin.

## S7a (the stretch goal) — COMPLETE

S7a asked for a precise Z[i]-level form of the G1c slice lemma "every class
meets the normalized slice" in zero-import Lean, OR a measured impossibility
note plus the sharpest reachable fragment. The result is **both**, and that
combination is exactly the valid S7a outcome the handoff sanctioned (norm 6:
never a weak statement wearing a strong name).

### The design probe (norm 15) and its verdict

Three standalone zero-import Lean probes (`seatP/probes/s7a_design_probe.lean`,
`seatP/probes/s7a_design_probe2.lean`, `seatP/probes/s7a_design_probe3.lean`,
each compiled exit 0 / 0 stderr bytes) measured the reach before any theorem
was written:

The full sentence — "every gauge class of pentagon solutions has a normalized
representative," equivalently the H³(Z₂)=Z₂ statement — IS statable
machinery-free (probe 1 type-checks `everyClassMeetsSlice`). Its combinatorial
skeleton is finite and provable: 8 live slots, 1 free at (1,1,1), 7 pinned by
normalization, 4 gauge degrees of freedom (probe 2, all by `decide`). But the
full sentence over ALL of Z[i] needs the surjectivity of the 3-coboundary onto
the 7 pinned slots for an arbitrary pentagon solution — that IS the vanishing
of H³(Z₂,U(1)), cohomology machinery outside zero-import reach.

The way through: the units of Z[i] are the finite group {1, i, −1, −i}
(`norm_one_units`, already in the record). Restricted to unit-valued gauges,
the whole slice/gauge question becomes a finite enumeration and is decided
completely (probe 3). That is the sharpest reachable fragment.

### What shipped

Eleven theorems appended to `seatP/Zi.lean` (161 → 172 total), inside
`namespace Zi`, reusing `norm_one_units`, `detaNum`, `detaDen`, `normSq`, `mul`
with no re-derivation. The core is `s7a_unit_slice_iff_symmetric`: over all
4⁴ = 256 unit-valued vertex gauges, the (1,1,1)-slot motion is trivial IF AND
ONLY IF the gauge is slice-symmetric (η01 = η10). This is strictly stronger
than the existing `gauge_slot_invariant` on the unit locus — it adds the
converse, which is the honest content of "meets": no unit gauge can move a
symbol off the two-class slice without also moving the slot. It is supported by
a live witness (η11 = i, `s7a_live_unit_gauge`, norm 3), a negative control
(`s7a_control_asymmetric_unit_moves_slot`, norm 5), the finite nest
(`s7a_live_slot_count`/`s7a_free_slot_count`/`s7a_pinned_slot_count` = 8/1/7,
norm 9), and the measured-impossibility marker (`s7a_nonunit_outside_alphabet`:
the non-unit value ⟨2,0⟩, norm 4, sits outside the decided locus).

### The honest boundary — what S7a does NOT prove

The full "every class meets the slice" sentence over arbitrary (non-unit)
pentagon solutions is NOT proven and is explicitly disclaimed in Zi.lean's S7a
header. That step is the H³ vanishing that needs cohomology machinery this
zero-import ring does not carry. S7a proves the unit locus, completely, and
says so in every theorem name.

### Acceptance gates (all met, all measured on the shipped file)

Compile: `lean Zi.lean` exit 0, 0 stderr bytes (2080 lines). Axiom census
(`axioms_zi.sh`): PASS, 172/172 covered, 77 axiom-free, 0 sorryAx, 0
Classical.choice — the Classical.choice trap the record warns of is avoided.
Norm 16 (Lean, both directions): plant #1 (slot count 8→9) and plant #2 (the
core iff RHS → a vacuous truth) each bitten exit 1; restore clean exit 0 / 0
bytes; census plant (a `sorry`) triggers the sorryAx ALARM. Norm 16 (seat B,
both directions): `seatB/verify_zi_s7a.py` reproduces all 11 claims blind from
the mechanically-extracted statements (`courier/Zi_statements_v8.txt`), 11/11
PASS exit 0; planted defect (drop `I` from the unit alphabet) → 9/11 FAIL exit
1; restore → 11/11. Seat B's independent sweep found 64 slot-fixed = 64
symmetric of 256 — the iff tight on both sides, matching Lean's `decide`.

Full detail, named adjudicator, and pins: `seatMETA/S7A-DESIGN-NOTE.md`.
Honest near-misses (loudest-first): `seatMETA/CORRECTIONS-LETTER-S7a.md`.

### S7a pins (measured on shipped artifacts)

| artifact | sha256 |
|---|---|
| `seatP/Zi.lean` (with S7a) | `d1f3617baaefcbb85b049709ffee600dbdc6a20b8748edcb637fea4d8291145d` |
| `seatP/axioms-zi.txt` | `1de8439c2de3477099aa7315166186671b0885cad0f44925ac693fef5c7c3599` |
| `courier/Zi_statements_v8.txt` | `914a80d58d710de0d3273ca144d5e2e44966bb295e65c5f0791c6b8a02e1d5b5` |
| `seatB/verify_zi_s7a.py` | `077fb33e25a9684c46065837900e16fb8e1eb6be4a33d72febbed61b4ce7dbe0` |
| `seatB/s7a_seatB_out.txt` | `4e741fbbe5c97f68769f44b1abb7995d97bc78711fd068bf1aca45897482b308` |
| `seatP/probes/s7a_design_probe.lean` | `ac16c2e33906148473acbbd6484c9fa757871d4ee57e7e479d72642c52cef51c` |
| `seatP/probes/s7a_design_probe2.lean` | `67689c2ed8ffda72806c58fc61d0d6c078abec35ce6b444e73f377ca49cb32a3` |
| `seatP/probes/s7a_design_probe3.lean` | `a643cfb4371b9229113ec67ccb26f95454dae62849f659ed6170956fe3b519e7` |
| `seatMETA/S7A-DESIGN-NOTE.md` | measured at delivery (PIN-TRACKER) |
| `seatMETA/CORRECTIONS-LETTER-S7a.md` | measured at delivery (PIN-TRACKER) |
