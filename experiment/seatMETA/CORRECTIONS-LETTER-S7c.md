# META-AUDITOR → THE RECORD: corrections letter, S7c (gate-scope extension)

*REGISTER row 7, second instance. Sanctioned scope divergence: the
predecessor's HANDOFF-ROUND3 recommended S7a-first; the meta-auditor
recommended S7c-first on the strength of the STRANGER-AUDIT finding that the
row-8 characterization slip lives where no instrument scans; Kelly chose
"S7c+S7a (your rec)". This divergence is recorded here, in the source header
of every changed gate, and in SUBROUND7-REPORT.md.*

Instruments extended: `audit/c2_pointers.sh`, `audit/c2_numerals.sh`,
`audit/c2_views.sh` (censusguard). Scope moved from `top-level *.md +
letters/**` to `+ experiment/**`. `floor/` stays out (inherited C1, REGISTER
class 1/6). Design measured before any edit in `audit/probes/S7C-DESIGN-NOTE.md`
and `audit/probes/s7c_scope_probe.sh` (norm 15). Every instrument run clean
AND bitten a plant inside `experiment/**` AND restored byte-identical (norm 16,
both directions). All exempted values VERIFIED true before exemption.

The crop — five items.

## 1. The scanning gap was real and large (the finding that justified S7c)

`experiment/**` carried thirty-seven markdown files and over one hundred
tracked files that NO gate scanned. The design probe
(`audit/probes/s7c_scope_probe.sh`) measured the blast radius of bringing
them in, at design time and before the meta-auditor's own Round-3 artifacts
were added to the tree — those measured figures are recorded verbatim in
`audit/probes/S7C-DESIGN-NOTE.md` §4. (The probe re-run today reports larger
figures, because the tree has since grown by exactly the STRANGER files, this
letter, and the PIN-TRACKER block; the design-note figures are the ones the
design was built against.) A naive glob flip would have reddened the pointer
gate with hundreds of unresolved occurrences and tempted a wall of reasonless
exemptions — the exact permissive failure the norms forbid. Instead the gates
were taught the experiment's OWN resolution sources, so grounded citations
resolve mechanically: the overwhelming majority cleared by resolution
(experiment Lean harvest, experiment pin ledger, doc-relative and
experiment-relative paths) and the small remainder by reasoned exemptions,
each naming why the reference is not an in-tree artifact. The exact counts
are in the design note and reproduced by re-running the probe against the
same commit.

## 2. Two near-misses on my own instruments (norm 16 working on the auditor)

Recorded loudest-first per norm 4, because they are the honest part.
(a) The first scope forecast ran a copy of the pointer gate from `/tmp`,
where its `$SELF_DIR`-relative exemption path found nothing — so it ran with
an EMPTY exemption list and produced a false unresolved figure inflated by
every already-exempt `letters/` token. Caught by noticing those exempt tokens
were flagged; the forecast was re-run from inside `audit/` and the true figure
recorded in the design note. (b) A comment
I added to the numeral gate's awk body contained an apostrophe (`c5'`), which
terminates the single-quoted awk program in `sh`; the gate crashed with a
syntax error and reported "0 unsourced" — a false PASS. Caught by reading the
stderr line, not the exit code; fixed to `c5b` with no apostrophes. Both are
instances of the same lesson the norms already carry: a check consulted must
be OBEYED and READ, not merely run.

## 3. The census guard had no subject on this branch until S7c

The front-door `lean/Zi.lean` is absent on `superninja/dual-seat-experiment-s1`,
so `censusguard` (and the axiom census, and the ledger renderer) had nothing
to scan and did nothing. censusguard is pure text and needs no Lean binary,
so it now falls back to `experiment/seatP/Zi.lean` when the front-door Lean is
absent. On the experiment's prover artifact it PASSES clean — the header
points at the census rather than restating it (the discipline the S6 letter
recorded) — and it BITES a planted stale census (a fabricated theorem total
and a fabricated propext-dependency count, both written into the header),
exit 1, both numerals named. The axiom census and the
ledger renderer genuinely need the Lean binary and are correctly left
SKIPPED→FAIL by the chain's own rule ("a gate that cannot run is not a gate
that passed"); that is a pre-existing branch condition, not an S7c change.

## 4. Six proximity false-positives in the prover artifact, each verified

censusguard on `experiment/seatP/Zi.lean` flagged six numerals sitting near
census vocabulary. Each was verified a non-census value and labeled:
the vertex label η₁₁ (unicode η stripped to `11`); the antisymmetrizer ranks
`10` and `15`, VERIFIED equal to the certificate's own
`G1f_antisymmetrizer_ranks_exact == [1,3,6,10,15]` (`c2_gift_certificates.py:654`,
the triangular numbers T(n)=n(n+1)/2 for m=2..6); and the tail of the line
citation `floor/symmetric_statistics.py LINES 37, 197-199`. The case of the
"LINES" keyword was made insensitive in the stripper so the leading term is
recognized as the line reference it is.

## 5. The meaning gap S7c does NOT close (the honest boundary)

The STRANGER-AUDIT flagged the row-8 slip "the Z₂ catalog **complete over
Z[i]**" (front-door `README.md`, lines 12-13): an unearned universal in a
true-shaped sentence. That line was ALREADY in the front-door gates' scope
before S7c; the gates scanned it and passed it, because every token resolves,
every number sources, and no proximity trips — the slip is MEANING-level.
S7c closes the SCANNING gap (experiment/** prose now under the checkable
gates); it does not and cannot close the MEANING gap. A true-shaped sentence
with an unearned universal passes every value/resolve/proximity gate whether
it lives in README.md or in experiment/**. That miss stays with the audit
loop (REGISTER class 7), where it belongs, and is named here so no reader
mistakes "gates green" for "characterization sound."

No statement in `seatP/Zi.lean` changed. The prover artifact's sha256 is
`b7ef35425e13b740e253892916fffb8a6ed5adddaa08a1bbe01360b77fcdba5e`, identical
before and after the plant/restore — the same pin verified in Phase 0.
