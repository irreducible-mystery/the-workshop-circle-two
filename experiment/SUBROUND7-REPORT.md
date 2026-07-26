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

## S7a (the stretch goal) — status

S7a (a precise Z[i]-level form of the G1c slice lemma "every class meets the
normalized slice," in zero-import Lean, or a measured impossibility note) is
the remaining Round-Three charge and is addressed separately; if it proves out
of zero-import reach, the report on it will carry the sharpest reachable
fragment and a measured note rather than an overclaim.
