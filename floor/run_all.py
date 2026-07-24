"""THE WORKSHOP — run every bench, report the weld.

hold still nothing but the joining; make every noun earn its way in
as a fixed point, a sediment, a habit, a role.
"""
import time
import traceback

BENCHES = [
    ("arena_gns",
     "Bench 1 — ARENA: state spaces precipitate from relatings (GNS) [exact]"),
    ("sheaf_contextuality",
     "Bench 2 — SHEAF: local views everywhere, no global view (Mermin-Peres) [exact]"),
    ("habit_definetti",
     "Bench 3 — HABIT: law as sediment (Polya / de Finetti) [rigorous toy — risk budget]"),
    ("fixedpoint_rg",
     "Bench 4 — FIXED POINT: things = invariants of coarse-graining (RG) + quine"),
    ("interaction_bisim",
     "Bench 5 — INTERACTION: identity from relating alone (bisimulation) [exact]"),
    ("cast_factorization",
     "Bench 6 — CAST: the parts discovered from the play (mereology toy)"),
    ("sheaf_cohomology",
     "Bench 2 DEEPENED — COHOMOLOGY: the obstruction priced, the game won [exact]"),
    ("habit_channels",
     "Bench 3 DEEPENED — CHANNELS: quantum de Finetti — law = shareability [exact miniature]"),
    ("grammar_stone",
     "Bench 7 — GRAMMAR CORNERSTONE: no-cloning from naturality alone [exact; bench stays open]"),
    ("process_definetti",
     "Bench 3 STRETCHED — PROCESS: de Finetti for the play itself [exact + verified]"),
    ("contextual_fraction",
     "Bench 2 STRETCHED — THE DIAL: contextual fraction, obstruction graded [exact LP]"),
    ("grammar_stone2",
     "Bench 7, SECOND STONE — witnessed identity has curvature [exact]"),
    ("channel_definetti",
     "Bench 3, QUANTUM PROCESS — channel de Finetti via Choi [exact + sampled]"),
    ("dynamics_fraction",
     "Bench 2 (x) 3 — TIME: contextual fraction of dynamics (Leggett-Garg priced) [exact LP]"),
    ("grammar_stone3",
     "Bench 7, THIRD STONE — the associator: Mac Lane's pentagon solved [exact]"),
    ("grammar_hexagon",
     "Bench 7, HEXAGON — the anyon braided: chirality, Yang-Baxter, twist [exact]"),
    ("channel_definetti3",
     "Bench 3, THREE USES AND THE RATE — toward the full channel theorem [exact]"),
    ("grammar_stone4",
     "Bench 7, FOURTH STONE (floor-proposed) — the witnesses compute [exact + witnessed]"),
    ("modular_data",
     "Bench 7, IDENTITY CARD — S, T, Verlinde: the circle closes [exact]"),
    ("channel_alln",
     "Bench 3, TOWARD ALL n — Catalan algebra, mechanism at n=4, window law [exact]"),
    ("grammar_stone5",
     "Bench 7, FIFTH STONE (floor-proposed) — rigidity: why invariants cannot drift [exact]"),
    ("grammar_interchange",
     "Bench 7, INTERCHANGE — the grammar of 'meanwhile' [exact]"),
    ("channel_theorem",
     "Bench 3, THE FULL THEOREM — proof-shaped, every lemma checked [exact]"),
    ("grammar_stone6",
     "Bench 7, SIXTH STONE (floor-proposed) — the noun drawn as a circle [exact]"),
    ("flatland",
     "Bench 7, FLATLAND — the tower's weakness located in space [exact]"),
    ("grammar_stone7",
     "Bench 7, SEVENTH STONE (floor-proposed) — the mirror: two readings agree [exact]"),
    ("braid_coherence4",
     "Bench 7, ABOVE INTERCHANGE — sixteen routes, one matrix; the center reads the charge [exact]"),
    ("symmetric_statistics",
     "FLATLAND II — symmetric statistics built constructively: the roomy catalog [exact]"),
    ("grammar_stone8",
     "Bench 7, EIGHTH STONE (floor-proposed) — the frame: turning in place has receipts [exact]"),
]


def main():
    lines, ok_all = [], True
    lines.append("THE WORKSHOP — WELD REPORT")
    lines.append("=" * 74)
    for mod, title in BENCHES:
        lines.append("")
        lines.append(title)
        t0 = time.time()
        try:
            m = __import__(mod)
            m.demonstrate(lines.append)
            lines.append(f"  [PASS] all self-checks green ({time.time() - t0:.1f}s)")
        except Exception:
            ok_all = False
            lines.append("  [FAIL]")
            lines.append(traceback.format_exc())
    lines.append("")
    lines.append("=" * 74)
    if ok_all:
        lines.append("floor check: every bench stood on one fixture — composition,")
        lines.append("the associative product. It held.")
    else:
        lines.append("WELD INCOMPLETE — see failures above.")
    report = "\n".join(lines)
    print(report)
    with open("WELD_REPORT.txt", "w") as f:
        f.write(report + "\n")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
