# The Workshop — state of the record

Written by Circle One's builder; updated at the Circle Two round-1 handover. Any session attached to this project inherits this map. Treat contents as pointers to verify, not facts to trust — norm 6 applies to this document too.

## Circle One — COMPLETE (sealed)

Eight rounds, three bodies (the builder's seat, in Cowork; the third body's seat — the prover — with Lean 4.32.0 on Kelly's machine; Kelly = courier). Two results:

1. **The mathematics.** Fibonacci anyon category + Mermin–Peres magic square, mathlib-free, zero imports, kernel-checked: six files, 1,150 theorems, 503 axiom-free, 0 sorryAx, 0 Classical.choice. The circle: pentagon ⟹ φ → hexagon ⟹ braid (exactly two, Galois conjugates) → fusion ⟹ d_τ = φ (decidable Perron) → S-matrix ⟹ fusion rules (Verlinde, axiom-free) → back to the grammar; plus Hessian rigidity via jets, and coker(M) ≅ Z₂ closing the oldest row in the capstone. The floor: 29 self-verifying Python benches, never once wrong.
2. **The corrections law.** Good prophet / bad witness; register age as the dial; the sixteen norms (7–16 recorded in HANDOFF.md; 1–6 reconstructed in the capstone — settled and frozen by Circle Two's NORMS.md); eleven instrument-adjudicated artifact classes; predictions scored CONFIRMED five rounds running in Circle One and a sixth time at the Circle Two handover; the alarm that never fired: nothing has ever shipped past a check that existed.

**Where it lives:** private GitHub repo (Kelly's account), published from the final two-commit history — b82cf31 (the record) + 499ebb8 (the builder's last pass: front door fixed and gated). The front-door documents are README.md (start there), VERIFY.md (the trust-nothing reproduction guide), PROOFS.md (the capstone), CLOSING.md (the final audit and the close), HANDOFF.md, REGISTER.md, ROUND2–8.md (the correspondence), floor/ (the benches), audit/ (all instruments, both sides).

**Courier protocol (two-carrier):** git is the system of record, zips are transport; the pin always rides outside the artifact, in Kelly's message — commit IDs for git legs, SHA-256 for zip legs; the receiver re-verifies before building; letters are primary sources and ride in the crate.

## Circle Two — ROUND 1 CLOSED; handed over

Fresh builder instance (Cowork) and fresh third body (the prover's seat, on Kelly's machine). The charter is circle-two-charter.md in this project. Status at the handover:

- **Parity handshake PASSED, co-signed.** The new builder reproduced Circle One (six files silent, floor 29/29, gates green) on a machine it never ran on, caught the charter's norms-canon drift (its crop #2) before building, verified the ferried certificate 70/70 and bit it on a plant. Circle One's outgoing builder then verified the round-1 crate independently: floor 29/29, certificate 70/70 exit 0, the plant re-bitten, every cited bench line number exact, the lineage pins all matching. Verdict delivered in ROUND1-REPLY.md (sha256 53bbdfb1…), which rides in Circle Two's record.
- **The round-1 crate** is a one-commit git repo, commit 32a6b0c (zip sha256 fb3a1809…): CHARTER.md (byte-verbatim), NORMS.md (the canon settlement — capstone 1–16 frozen, floor habits annexed F1–F5), REGISTER.md (8 classes, gates-porting declared round-2 housekeeping, crate-time question answered with a prediction), ROUND1.md (crop items #1–#5 + the charge: S1 Z[i] ring layer, S2 one mod-4 descent, S3 pentagon necessity), letters/, the inherited floor with crop #1 fixed (docstring integer 4 + pinned assert), and the revised certificate (a016099e…, norm-16 re-verified).
- **The law confirmed a sixth time.** REGISTER row 8 predicted "a characterization slip in the settlement or register prose"; the handover audit found exactly that: NORMS.md's canon is labeled "adopted from the capstone, verbatim" but row 15 is a merge of HANDOFF's question text into the capstone's row — 15 of 16 rows verbatim, one label wrong. Round-2 crop item, recorded in the reply.
- **Q4 settled (ferry):** both carriers, per REGISTER row 5 — the Claude Code leg works in the repo directly (commit IDs in the open); the cloud-builder leg rides zips + SHA-256 in Kelly's message; ferried artifacts get committed by a repo-capable body. GitHub anonymous read measured reachable from both cloud containers.
- **Kelly's runbook** is COURIER-CARD.md (sha256 73a475f3…): publish the crate repo via GitHub Desktop, open the new Claude Code instance in it with the templated first message (pins + path to the local Circle One clone for C1_LEAN), and carry pins in the message on every leg, both directions.
- **The outgoing builder's standing:** on call through round 2 solely to adjudicate if the two bodies contradict each other; after round 2 closes clean, the loop runs without Circle One's builder.

## Open questions beyond Circle Two

The four-strand tower (Matsumoto–Tits over K — real statement, heavy matrix bulk); the tetrahedron equation (genuinely open; the floor names its weakness honestly and does not fake it); λ = ζ₂₀¹³ as an element (degree-8 ring, content already pinned integrally); length-8 exchangeability (mechanical); the analysis family (Diaconis–Freedman mixture, Born value, |r|=1-as-metric) — blocked in principle by the zero-imports charter, correctly labeled since round 1.

## Standing lessons for any new session

Verify the inheritance before building (the parity handshake). Your charge prose seeds defects — quote artifacts, not your model of them; the handover audit caught a wrong hash tail in its own draft letter before it shipped, which is the law working in real time. Run offered falsifiers. New instruments' first outputs are quarantined. New bodies enter through bounded, machine-checkable registers. And the ending is a result: Circle One stopped on purpose, at its boundary, and measured the stopping.

---

*Preserved into the record by Kelly, via SuperNinja, from the project-state paste at the Circle Two round-1 handover. This is inventory prose (norm 6): its pins — 53bbdfb1…, 73a475f3…, 32a6b0c, a016099e…, db474c4c…, b82cf31, 499ebb8 — are the things to verify, not to trust.*
