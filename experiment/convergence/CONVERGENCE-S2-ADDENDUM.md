# CONVERGENCE S2 — ADDENDUM: provenance correction, one conviction of my own report, and the builder's nine specimens

**Meta-auditor (REGISTER row 7), quarantined per norm 16. This amends
`CONVERGENCE-REPORT-S2.md` (pre-amendment pin `f57582c63dbc…`) and is
recorded loudest-first: my correction leads, the provenance note
follows, the cross-map of the builder's crop comes last.**

New input: Fable's actual S2 verification letter
(`ROUND2S2VERIFICATION.md`, pin `511fb865056c…`, nine specimens,
Q6/Q7 ruled, S3 GO) plus Kelly's provenance correction on the S2
transcripts.

---

## 1. CORRECTION — my report verified the portability fix from a warm container. The verification was false.

My S2 report (§1, Phase A) claimed their census portability fix
"repairs exactly the failure I reported at S1," verified "from a cold
start." **Both halves are wrong, and Fable's specimen #2 is what
exposed it.** Re-measured here, properly this time:

- My container was not cold. At S1 I had run
  `elan default leanprover/lean4:v4.32.0` to work around the original
  failure; that default persisted through my S2 run. The census passed
  because of *my* S1 workaround, not their fix. I credited the pass to
  the wrong cause — the exact species my own P3 refutation named the
  same day (inferring mechanism from surface text instead of severing
  the confound).
- **The real falsifier, run now** (elan default removed from
  `~/.elan/settings.toml`, `elan show` → "no active toolchain"): their
  fixed census on their crate **FAILS, exit 1, "no default toolchain
  configured"** (`mech/census_nodefault_out.txt`). Fable's #2
  confirmed on a third container.
- **Fable's mechanism diagnosis reproduces**: a probe file with
  `lean-toolchain` beside it fails when lean is invoked from outside
  its directory and compiles silently from inside — elan resolves the
  pin from the *working directory*, not the file's location
  (`mech/pin_resolution_probe.txt`). The pin travels but is never
  read.
- **Fable's proposed one-line repair verified**: patching the census
  so the generated copy is compiled from *within* the temp directory
  (subshell `cd`) → **PASS, exit 0, 76 = 24 + 40 + 12, with no elan
  default configured** (`mech/census_fixed_nodefault.txt`). The repair
  closes the condition; the artifact here is the pre-verification the
  third body can cite when they ship it.

The amendment to the report is in place (§1, marked `[AMENDED]`), and
the report's new pin rides in the tracker. What survives untouched:
the census *digits* (24/40/12) were measured by my own instrument
independently and are unaffected; only the portability *attribution*
was false.

Scored against myself: my S1 convergence report's operational note
("fails LOUD, their alarm works") was correct; my S2 upgrade of that
note to "fix verified" was manufactured by a warm container. An
instrument that changes gets re-bitten — and **a container that
changes is an instrument.** That sentence is the protocol amendment
(§4).

## 2. PROVENANCE CORRECTION — the S2 transcripts were swapped at upload

Kelly's correction: what I received labelled "Fable S2 transcript" was
Fable's S1-verification message; the other file was Code's (the third
body's) S2 build transcript. Consequences audited line-by-line against
my report:

- **Unaffected**: every Phase A–D measurement (they ran against pinned
  artifacts, not transcripts); the convergence map; the axiom series;
  the predictions and their scoring.
- **Affected, minor**: §5's process notes drew on "both transcripts"
  as if they bracketed S2 from two seats. In fact I had the third
  body's S2 seat and the *builder's S1* seat; Fable's S2-side process
  (the verification ladder, the falsifier they ran that I didn't) is
  only now in evidence — and §3 below is what it changes.
- The uploaded-artifact pins were never transcript-dependent; all
  reconfirmed.

Rule adopted into the protocol: transcripts are pinned and attributed
at Phase 0 like any artifact, and authorship is a recorded claim, not
an assumption from a filename.

## 3. THE BUILDER'S NINE SPECIMENS × MY REPORT — the cross-map

Two audits of the same delivery, run blind to each other (Fable's
letter and my report were written concurrently). The overlap is the
calibration datum:

| Fable's specimen | my report | verdict on the comparison |
|---|---|---|
| #1 stale "Nothing here proves S2" label (PROOFS.md:338) | **MISSED** | my Phase E reads delivery letters + transcripts, not the full ledger; the sharpest specimen of the round was outside my read surface. Protocol widened (§4). |
| #2 portability fix doesn't fix; falsifier never run | **WORSE than missed — contradicted.** My report *endorsed* the fix from a warm container. §1 above. | the round's loudest lesson, and it is mine |
| #3–#5 three certificate miscitations, exactly where their prediction pointed | MISSED — certificate citation edges were outside my chartered scope | verified here independently by reading the three check bodies: the booleans contain what Fable says and not what the rows cite. Their prediction (S3 form, "the accounting of which theorem is licensed by which check") confirmed one crate early; scope added to protocol (§4). |
| #6 "the census names every one" — it names two | **COMPLEMENT**: my instrument's artifact `census_their_s2_out.txt` (pin `223024bfff0e…`) ships exactly the named list of 12 their #6 asks for | the fix their crop requests already exists in my mech/ directory; offered |
| #7 "593 lines" vs 594 measured | **CONVERGENT** — my report §0, found independently | two auditors, two instruments, same defect: the count-in-prose species is now cross-lineage-confirmed twice over |
| #8 DecidableEq disclosure cites correction #3 (wrong home) | MISSED — same read-surface gap as #1 | verified here: header says #3; #3 is the half-control repair |
| #9 Fable's own S1 advice was the wrong repair, implemented faithfully | outside my scope (their internal ledger) | noted: the corrections law crossing seats *within* their lineage, same shape as it crossing lineages here |

Tally: of the seven specimens inside any reasonable shared scope, I
found one (convergent), complemented one, missed four, and got one
*backwards*. Fable's three-seat pass plus a real falsifier beat my
protocol's prose pass decisively this round. That asymmetry is itself
the round's finding: **my protocol was strong where instruments run
(Phases A–D: everything reproduced, and my verifier proved the domain
on the second prong) and weak where reading is the instrument
(Phase E).** The amendment follows.

## 4. PROTOCOL AMENDMENTS (CONVERGENCE-PROTOCOL.md updated in the same commit)

1. **Cold means cold.** Before crediting any environment/portability
   claim, *remove the masking condition* and run the actual falsifier
   (for toolchain claims: delete the elan default, show "no active
   toolchain" in the transcript, then run). A pass under a warm
   container verifies nothing. A container that changes is an
   instrument that changed: re-bite.
2. **Read surface = the whole crate.** Phase E's prose pass covers the
   ledger and file headers end-to-end, not just delivery letters and
   transcripts — the stale-label species lives at maximum distance
   from the section being shipped.
3. **Citation edges are in scope.** For every certificate check cited
   by a new-layer table row, read the check's *tested boolean* and
   confirm it contains what the row claims (printed strings are not
   checks — their B#1 ruling, now protocol).
4. **Transcripts are artifacts.** Pinned and author-attributed at
   Phase 0; attribution is a claim.

## 5. WHAT THIS ADDENDUM CHANGES ABOUT "WHAT EMERGES"

The S2 report's thesis stands, but it gains a fourth clause: the
comparison instrument itself obeys the corrections law. My report
found their prose defect (594) while manufacturing one of its own (the
warm-container endorsement) — *an auditor misses things at exactly the
moment they are being most careful*, their B#7 finding, now
demonstrated on the auditor of both lineages. The loop is the auditor;
nobody stands outside it.

---

## Appendix — new pins

| artifact | sha256 |
|---|---|
| `ROUND2S2VERIFICATION.md` (Fable's letter, external reference) | `511fb865056c308f4f4ea7bec643b4e117539d41ab766c6e05a37ff9ae9145ca` |
| `mech/census_nodefault_out.txt` (real falsifier: their fix FAILS cold, exit 1) | pinned at ship |
| `mech/census_fixed_nodefault.txt` (Fable's repair: PASS cold, exit 0) | pinned at ship |
| `mech/pin_resolution_probe.txt` (elan reads cwd, not file location) | pinned at ship |
| `CONVERGENCE-REPORT-S2.md` (amended §1) | re-pinned at ship |
