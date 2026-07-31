# Option 2 — Sandboxed Multi-Agent Antifragility Simulation

## Pre-flight (self-reference / error observation)
- [x] Acknowledge word-count self-reference issue (user's illustrative point)
- [x] Fix REAL byte-level errors found in report (literal \u2014, \", \u2248, \u2192 over-escapes) — 4 codepoints, ~9 occurrences
- [x] Make word-count note self-aware (range, not stale integer)
- [x] Decide whether to adjust simulation design in light of Deep-research findings (document decision; no-change is valid)

## Design decision (Phase 0)
- [x] Record which Implementation-Engineer build requirements to honour and any adjustments

## Build (Phase 1)
- [x] antifragile_sim.py — three-layer model: kernel / arena / engine
  - [x] Kernel: 7 seed rules as invariants + amendment gate (super-majority threshold + time-delay)
  - [x] Arena: N polycentric human-AI units, overlapping jurisdictions, heterogeneous "genomes"
  - [x] Engine: vary / select-under-exposure / retain-with-degeneracy loop
  - [x] Degeneracy metric: operational "structurally different" distance (behavioural disagreement on probe set)
  - [x] Variety-budget vital signs: optionality, reversibility, exposure symmetry
- [x] Shock generator: tunable magnitude Delta, novel (off-distribution) shocks
- [x] System-level performance functional f(state)
- [x] Convexity test: Delta-sweep -> H = 1/2[f(a-D)+f(a+D)] - f(a) at institution level
- [x] Baselines to compare against the antifragile design:
  - [x] Monoculture (single optimized unit, no degeneracy)
  - [x] Redundant (identical copies, no degeneracy)
  - [x] Antifragile (full three-layer design)
- [x] Red-team probes: evolution-selects-misalignment; silent variety-collapse detection

## Run & measure (Phase 2)
- [x] Run Delta-sweep for all three architectures (multiple seeds)
- [x] Compute H(Delta) curves; classify convex/robust/fragile
- [x] Log variety-budget trajectories and collapse-detection events
- [x] Save raw results to CSV/JSON

## Visualize & report (Phase 3)
- [x] Plot: H(Delta) convexity curves per architecture
- [x] Plot: performance under shock over time
- [x] Plot: variety-budget (optionality/reversibility/exposure) trajectories
- [x] Plot: misalignment / variety-collapse red-team outcomes
- [x] Write Simulation_Report.md interpreting results honestly (incl. where design FAILS)

## Package (Phase 4)
- [x] Deliver code + data + figures + report via ask
