#!/usr/bin/env python3
"""T-C11 session 43 — batch forecasting instrumentation.

Emits graph/reports/C11_BATCH_FORECAST.json: the machine-computed pilot
baseline, the §16 documented projection (C11_S16_GATE_REPORT.md item 14),
a predicted-vs-actual calibration of the projection
model against the pilot's own actuals, the review rates with documented
formulas, the false-positive categories observed across the pilot's review
history, and the empty future-batch record list that §16 batches append to.

READ-ONLY with respect to the graph: writes only its own report. No
promotion, no graph modification, no §16 action (the projection figures are
referenced, never executed).

Session-46 (2026-09-12): §16 is now AUTHORIZED by explicit operator decision
(scripts/c11_s16_authorization.yaml) — the projection below is the sanctioned
execution shape, still not executed: no batch has run; future_batch_records
stays empty until the first authorized batch completes.
"""
from __future__ import annotations

import json
from pathlib import Path

import sys
import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
# Session-55 repair (2026-09-22, dated): store paths resolve through the
# C28 registry (post-stage-2 layout graph/igcse-chemistry/); graph/reports/
# is unchanged.
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402  # C28 §3.2 path registry
REPORTS = GP.reports_dir()

dec = yaml.safe_load((HERE / "c11_pilot_decisions.yaml").read_text(encoding="utf-8"))
graph_edges = yaml.safe_load(GP.store("concept_edges")
                             .read_text(encoding="utf-8"))["edges"]
promo = yaml.safe_load((HERE / "c11_promotions.yaml").read_text(encoding="utf-8"))

nodes = dec["nodes"]
edges = dec["edges"]
held = dec["held"]
sps = dec["meta"]["scope"]["spec_points"]

n_nodes = len(nodes)
n_authored = len(edges)
# session-47: the live store spans the decision-record REGISTRY (pilot +
# §16 batches). The pilot_baseline counts are PILOT-scoped (batch 0's own
# actuals — the calibration baseline); store-wide counts feed the live rates.
PILOT_SPS = set(sps)
pilot_edges = [e for e in graph_edges
               if e["relation"] == "PART_OF" and e["target"] in PILOT_SPS]
n_part_of = len(pilot_edges)
n_total = len(graph_edges)
n_held = sum(1 for h in held if h["status"] == "held")
n_rejected = sum(1 for h in held if h["status"] == "rejected")
n_promoted = len(promo.get("promotions", []))
n_hv = sum(1 for e in graph_edges if e["validation_status"] == "HUMAN_VALIDATED")

# The 31 SUGGESTED authored edges awaiting per-row confirmation
# (29 unmarked + 2 PENDING-gated; the REVIEW_REQUIRED operator-HOLD edge is
# excluded from the per-row surface — it already carries an operator verdict).
suggested_authored = [e for e in edges if e["validation_status"] == "SUGGESTED"]

# --- §16 documented projection (referenced, never executed) ----------------
# Session-46 (2026-09-12): §16 AUTHORIZED (scripts/c11_s16_authorization.yaml) —
# the item-14 proposal is now the sanctioned execution shape. Still not executed.
S16_SOURCE = ("graph/reports/C11_S16_GATE_REPORT.md item 14 "
              "(the sanctioned §16 execution shape — authorized 2026-09-12, "
              "session 46, scripts/c11_s16_authorization.yaml; batch 1 "
              "authored session 47, pending its operator review gate)")
s16_model = {"nodes_per_sp": 2.4, "authored_edges_per_sp": 2.75, "held_per_sp": 1.0}
s16_totals = {"nodes": [380, 450], "authored_edges": [420, 510], "held": [160, 180]}
s16_batches = {"count": 14, "approx_sp_per_batch": 12,
               "per_batch": {"nodes": 30, "authored_edges": 33, "held": 12}}

# --- predicted-vs-actual calibration: model applied to the pilot's 12 SPs ---
rows = []
for metric, actual, per_sp in (
        ("nodes", n_nodes, s16_model["nodes_per_sp"]),
        ("authored_edges", n_authored, s16_model["authored_edges_per_sp"]),
        ("held_candidates", len(held), s16_model["held_per_sp"])):
    predicted = round(per_sp * len(sps), 1)
    delta = round(actual - predicted, 1)
    pct = round(100.0 * delta / predicted, 1) if predicted else 0.0
    rows.append({"metric": metric, "predicted": predicted, "actual": actual,
                 "delta": delta, "pct_error": pct})

# --- review rates (formulas documented so future batches are comparable) ---
denominator = n_authored + len(held)
operator_rows = len(suggested_authored) + len(nodes)
rates = {
    "held_rate": {
        "value": round(len(held) / denominator, 4),
        "formula": "held_candidates / (authored_edges + held_candidates)",
        "inputs": f"{len(held)} / {denominator}",
        "meaning": "fraction of candidate semantic relations abstained at generation",
    },
    "rejection_rate": {
        "value": round(n_rejected / denominator, 4),
        "formula": "rejected_candidates / (authored_edges + held_candidates)",
        "inputs": f"{n_rejected} / {denominator}",
        "meaning": "fraction of candidates permanently refused (HELD-09 negative "
                   "control; HELD-13 operator REJECT)",
    },
    "promotion_rate": {
        "value": round(n_promoted / n_total, 4) if n_total else 0.0,
        "formula": "promoted / total_edges",
        "inputs": f"{n_promoted} / {n_total}",
        # Session-46 (2026-09-12): the meaning text is state-dependent — 0 at the
        # session-43 pre-verdict state by design; 28/65 since the session-45 §18
        # promotions. The rate is a pure function of the live store (the §18
        # channel is the only sanctioned way it moves).
        "meaning": "the fraction of live edges carrying HUMAN_VALIDATED — 0 by "
                   "design at the session-43 pre-verdict state (nothing is "
                   "ratified until the operator records verdicts); since session "
                   "45 it is the §18 promotion fraction (operator-ratified "
                   "identities only, never batch/node/relation-wide)",
    },
    "operator_review_rate": {
        "value": round(operator_rows / (n_authored + len(nodes)), 4),
        "formula": "operator-verdict-requiring rows / (authored_edges + nodes)",
        "inputs": f"{operator_rows} / ({n_authored} + {len(nodes)})",
        "meaning": "the per-row surface BEFORE machine pre-triage grouping; "
                   "the session-43 package reduces the effective decision "
                   "load to ~7 (see C11_REVIEW_PACKAGE.md §8)",
    },
    "quarantine_rate": {
        "value": round((sum(1 for e in edges
                            if e["validation_status"] == "REVIEW_REQUIRED")
                        + sum(1 for h in held if h["status"] == "held"))
                       / denominator, 4),
        "formula": "(REVIEW_REQUIRED edges + held candidates) / "
                   "(authored_edges + held_candidates)",
        "inputs": f"(1 + {n_held}) / {denominator}",
        "meaning": "everything not yet promoted and not yet operator-settled",
    },
}

# --- false-positive categories observed across the pilot review history ----
# (pass-2 findings + session-40/41/42 history; categories future batches
#  count against — the forecast's quality feedback loop)
fp_categories = [
    {"id": "FP-1", "category": "anchor-direction overstatement",
     "instances_pilot": 1,
     "detail": "MOLAR-GAS-VOL EXPLAINED_BY AVOGADRO-LAW: the anchored quote "
               "supports molar-volume→formula, not law→molar-volume",
     "current_state": "PENDING operator judgment (medium confidence, "
                      "recommendation HOLD)",
     "mitigation": "confidence cap at medium + PENDING gate + 10-field "
                   "presentation before any promotion"},
    {"id": "FP-2", "category": "split-artifact multiplicity (same-anchor "
                               "operand pairs)",
     "instances_pilot": "2 edges + 3 nodes",
     "detail": "PERCENT-YIELD → {YIELD, THEOR-YIELD} same-anchor pair; the "
               "yield-triple nodes — all vanish under an operator merge",
     "current_state": "resolved by OD-1 (stays split) — PENDING operator "
                      "ratification (session-43 package §6)",
     "mitigation": "OD-1 generalized operand rule for §16"},
    {"id": "FP-3", "category": "granularity mismatch",
     "instances_pilot": 1,
     "detail": "REACTING-MASS → EQ-SYMBOL: operative dependency is on "
               "interpreting a given equation; the single slice concept also "
               "covers writing/balancing",
     "current_state": "pass-2 CONFIRM at high confidence with granularity note",
     "mitigation": "boundary-minting policy in the expansion round"},
    {"id": "FP-4", "category": "implicit-use emission (OD-2 class)",
     "instances_pilot": "1 emitted-then-rejected + 1 quarantined",
     "detail": "PR-03 → CON-MOLE emitted on a table-row label (operator "
               "REJECT, HELD-13, permanent); GAS-VOL-CALC → AVOGADRO-LAW "
               "quarantined REVIEW_REQUIRED (operator HOLD)",
     "current_state": "both operator-settled; OD-2 codifies the rule",
     "mitigation": "OD-2 evidence admissibility (PENDING ratification) + "
                   "IMPLICIT_USE derivation cap at medium"},
    {"id": "FP-5", "category": "report/data drift (process-level)",
     "instances_pilot": "3 report artifacts + 1 renderer literal",
     "detail": "the 'aximum yield' corruption was reported in three reports "
               "and a renderer literal but never existed in any committed "
               "data revision — the defect description itself was the defect",
     "current_state": "corrected session 43 (renderer + reports); the true "
                      "issue (unevidenced 'maximum yield' alias) is in the "
                      "session-43 alias audit",
     "mitigation": "defect records must cite byte-verified store reads; "
                   "renderers compute from the store"},
    {"id": "FP-6", "category": "taxonomy coverage gap (report-level)",
     "instances_pilot": 1,
     "detail": "HELD-08 (residual-class discipline) is unassigned in the §19 / "
               "§16-item-6 failure-class distributions (2+4+5+1 = 12 of 13 "
               "entries counted); it belongs to FC-2",
     "current_state": "remediated session 44 (operator-directed, report-only): "
                     "HELD-08 assigned FC-2 in architecture §19 and the §16 "
                     "report item 6 — the distributions now count 13 of 13 "
                     "entries; HELD-08's verdict unchanged (HELD)",
     "mitigation": "machine-counted failure_class fields in expansion-round "
                   "held entries (§19 already mandates this for expansion)"},
]

out = {
    "task": "T-C11",
    "instrument": "batch-forecast",
    # session-48 (2026-09-12): instrument advanced — batch-1 operator gate
    # SETTLED (verdicts recorded + applied); baselines stay pinned to the
    # session-46 authorization state they anchor.
    # session-49 (2026-09-12): batch-2 AUTHORED to its operator gate
    # (future_batch_records[1]); baselines unchanged.
    # session-51 (2026-09-12): batch-3 AUTHORED to its operator gate
    # (future_batch_records[2]; the full S1 remainder — operator-commissioned
    # 24-SP batch); baselines unchanged.
    # session-50 (2026-09-12): batch-2 operator gate SETTLED — verdicts
    # recorded (ruling "CONFIRM all") and applied through §18 (23
    # promotions, operator); baselines unchanged.
    # session-52 (2026-09-13): batch-3 operator gate SETTLED — verdicts
    # recorded (the practical-review policy: 39 edge CONFIRM / 24 node
    # CONFIRM / 7 KEEP_AS_IS / 14 held acknowledged) and applied through
    # §18 (39 promotions, operator; store total 118); baselines unchanged.
    # session-53 (2026-09-13): batch-4 AUTHORED to its operator gate
    # (future_batch_records[3]; Section 3 Physical Chemistry 3.1-3.22C, 22
    # SPs + PR-09/10/11, under the session-52 cross-slice boundary ruling);
    # baselines unchanged.
    # session-54 (2026-09-13): batch-4 operator gate SETTLED — verdicts
    # recorded (the practical verdict policy: 35 edge CONFIRM / 22 node
    # CONFIRM / 6 KEEP_AS_IS / 14 held acknowledged; FP-B4-1 + FP-B4-2
    # special attention, evidence inspected) and applied through §18 (35
    # promotions, operator; store total 153); baselines unchanged.
    # session-56 (2026-09-22): batch-5 operator gate SETTLED — the
    # completed review sheet §6 verdict (18 edge CONFIRM / 16 node
    # CONFIRM / 6 KEEP_AS_IS / 14 held acknowledged; zero RR) recorded in
    # c11_batch5_verdicts.yaml and applied through §18 (18 promotions,
    # operator; store total 171); baselines unchanged.
    # session-57 (2026-09-22): batch-6 AUTHORED to its operator gate
    # (future_batch_records[5]; S2 Inorganic second slice — the operator's
    # "commission batch 6" directive); baselines unchanged.
    # session-58 (2026-09-22): the batch-6 operator gate SETTLED — the
    # operator's completed review sheet §6 verdict (PASS WITH NOTE) applied
    # through §18 (16 promotions, operator; c11_batch6_verdicts.yaml; store
    # total 187); baselines unchanged; top-level session advances with the
    # settling session (the session-56 precedent).
    # session-59 (2026-09-23): batch-7 AUTHORED to its operator gate
    # (future_batch_records[6]; S2 Inorganic third slice — the operator's
    # "Proceed with batch 7" directive); baselines unchanged.
    "session": 59,
    "generated": "2026-09-13",
    "baselines": {"resources": "9ce37bc", "syllabai": "26adfee"},
    "purpose": "predicted-vs-actual instrumentation for the §16 expansion "
               "batches. The pilot is batch 0 (baseline). Each authorized §16 "
               "batch appends a record to future_batch_records so forecast "
               "error, rates and false-positive categories are measured, not "
               "assumed. This file never authorizes anything.",
    "pilot_baseline": {
        "spec_points": len(sps),
        "notes": len(dec["meta"]["scope"]["notes"]),
        "mark_schemes_pinned": len(dec["meta"]["scope"]["mark_scheme_evidence"]),
        "nodes": n_nodes,
        "concepts": sum(1 for n in nodes if n["family"] == "CONCEPT"),
        "misconceptions": sum(1 for n in nodes if n["family"] == "MISCONCEPTION"),
        "authored_edges": n_authored,
        "part_of_edges": n_part_of,
        "total_edges": n_authored + n_part_of,
        "held_candidates": len(held),
        "held": n_held,
        "rejected": n_rejected,
        "promoted": n_promoted,
        "human_validated": n_hv,
        "operator_review_surface": {
            "suggested_authored_edges": len(suggested_authored),
            "nodes": len(nodes),
            "pending_medium_confidence_judgments": 2,
            "od_ratifications": 2,
            "alias_policy_plus_special_case": 2,
        },
        "ratios_per_sp": {
            "nodes": round(n_nodes / len(sps), 3),
            "authored_edges": round(n_authored / len(sps), 3),
            "held": round(len(held) / len(sps), 3),
        },
    },
    "s16_projection": {
        "source": S16_SOURCE,
        # Session-46 (2026-09-12): §16 AUTHORIZED (operator, session 46) — status
        # updated from the pre-authorization proposal wording; nothing executed yet.
        # Session-47 (2026-09-12): batch 1 AUTHORED (extraction_pass
        # c11-s16-batch-1, commissioned by the operator's 'run batch 1');
        # its content is SUGGESTED/REVIEW_REQUIRED pending the per-batch
        # operator gate — no batch-1 promotion yet; 13 batches remain.
        # Session-48 (2026-09-12): batch 1 SETTLED — the operator ruled
        # 'CONFIRM all' on the review sheet; verdicts recorded
        # (scripts/c11_batch1_verdicts.yaml) and applied (28 edge CONFIRM
        # promoted via §18; RR quarantine settled HOLD_REVIEW_REQUIRED;
        # 4 identity decisions KEEP_AS_IS).
        # Session-50 (2026-09-12): batch 2 SETTLED — the operator ruled
        # 'CONFIRM all' on the session-49 review sheet; verdicts recorded
        # (scripts/c11_batch2_verdicts.yaml) and applied (23 edge CONFIRM
        # promoted via §18; zero RR authored, so no settlement row; 4
        # identity decisions KEEP_AS_IS; B2-N-08 enrichment scoping).
        # Session-52 (2026-09-13): batch 3 SETTLED — the operator's
        # practical-review policy applied (CONFIRM where evidence clearly
        # supports; ordinary ontology imperfection not a blocker); verdicts
        # recorded (scripts/c11_batch3_verdicts.yaml) and applied (39 edge
        # CONFIRM promoted via §18; zero RR authored; 7 identity decisions
        # KEEP_AS_IS; 14 held preserved — clean quarantine).
        "status": ("§16 AUTHORIZED 2026-09-12 (session 46, operator — "
                   "scripts/c11_s16_authorization.yaml); batch 1 AUTHORED "
                   "2026-09-12 (session 47: 12 SPs / 24 nodes / 29 authored "
                   "edges / 12 held / 1 RR quarantine), SETTLED 2026-09-12 "
                   "(session 48: operator ruling 'CONFIRM all' — 28 edge "
                   "CONFIRM promoted via §18, store total 56; RR settled "
                   "HOLD_REVIEW_REQUIRED; verdict record "
                   "scripts/c11_batch1_verdicts.yaml); batch 2 AUTHORED "
                   "2026-09-12 (session 49: 12 SPs / 14 nodes / 23 authored "
                   "edges / 10 held / 0 RR; 5 cross-boundary edges), SETTLED "
                   "2026-09-12 (session 50: operator ruling 'CONFIRM all' — "
                   "23 edge CONFIRM promoted via §18, store total 79; zero "
                   "RR authored, so no settlement row; verdict record "
                   "scripts/c11_batch2_verdicts.yaml); batch 3 AUTHORED "
                   "2026-09-12 (session 51: the full S1 remainder "
                   "4CH1-1.37-1.60C, 24 SPs / 24 nodes / 39 authored "
                   "edges / 14 held / 0 RR, 6 cross-boundary edges + 3 "
                   "Paper-2 MS pins — FN-B2-1 closed; awaiting its operator "
                   "gate; Section 1 coverage complete), SETTLED 2026-09-13 "
                   "(session 52: the operator's practical-review policy — "
                   "39 edge CONFIRM promoted via §18, store total 118; "
                   "zero RR authored; 7 identity decisions KEEP_AS_IS; "
                   "14 held preserved — clean quarantine; verdict record "
                   "scripts/c11_batch3_verdicts.yaml); batch 4 (S3 "
                   "Physical) COMMISSIONED + STARTED session 52 (the "
                   "cross-slice boundary ruling recorded + machine-checked; "
                   "the S3 Paper-2 MS set pinned: ENERGETICS/RATES/RRE_MS_P2 "
                   "— all three families covered, zero unpinned Paper-2 "
                   "family), AUTHORED to its operator gate 2026-09-13 "
                   "(session 53: 22 SPs / 22 nodes / 35 authored edges / "
                   "14 held / 0 RR, 5 sanctioned cross-section boundary "
                   "edges), SETTLED 2026-09-13 (session 54: the operator's "
                   "practical verdict policy — 35 edge CONFIRM promoted "
                   "via §18, store total 153; zero RR authored; 6 identity "
                   "decisions KEEP_AS_IS; 14 held preserved — quarantined; "
                   "verdict record scripts/c11_batch4_verdicts.yaml; "
                   "Section 3 coverage settled — S1 60 + S3 22 = 82 of 182 "
                   "SPs); batch 5 (S2 Inorganic, FIRST slice) COMMISSIONED + "
                   "STARTED session 55 (2026-09-22, the operator's 'run "
                   "batch 5' directive; the S1<->S2 + S3<->S2 cross-slice "
                   "boundary ruling recorded + machine-checked — 27 term "
                   "matches all dispositioned, TWO sanctioned boundary "
                   "targets; the S2 Paper-2 MS set pinned: "
                   "GROUP1/GROUP7/GASES_MS_P2 — all three families "
                   "covered), AUTHORED to its operator gate 2026-09-22 "
                   "(session 55: 14 SPs 4CH1-2.1-2.14 / 16 nodes / 17 "
                   "authored edges / 14 held / 0 RR, 3 sanctioned "
                   "cross-section boundary edges into exactly the ruled "
                   "owners — CON-ELECTRONIC-CONFIGURATION (batch 2, x2) "
                   "and CON-EXO-ENDO (batch 4); awaiting its operator "
                   "gate), SETTLED 2026-09-22 (session 56: the completed "
                   "sheet §6 verdict — 18 edge CONFIRM promoted via §18, "
                   "store total 171; zero RR; 6 identity KEEP_AS_IS; 14 "
                   "held preserved; verdict record "
                   "scripts/c11_batch5_verdicts.yaml); batch 6 (S2 "
                   "Inorganic, SECOND slice) COMMISSIONED + STARTED "
                   "session 57 (2026-09-22, the operator's 'commission "
                   "batch 6' directive; the S2-d/e cross-slice boundary "
                   "ruling recorded + machine-checked — 45 term matches "
                   "all dispositioned, FOUR sanctioned boundary targets "
                   "incl. the TWO batch-5 deferral closures; the "
                   "Reactivity Paper-2 MS pinned — the extraction family "
                   "is UNPINNED, no PMT MS exists in any unit), AUTHORED "
                   "to its operator gate 2026-09-22 (session 57: 13 SPs "
                   "4CH1-2.15-2.27 / 13 nodes / 16 authored edges / 9 "
                   "held / 0 RR, 4 sanctioned cross-section boundary "
                   "edges; awaiting its operator gate; batches 7-14 not "
                   "started)"),
        "scope_sp": 170,
        "batches": s16_batches,
        "totals": s16_totals,
        "model_ratios": s16_model,
    },
    "predicted_vs_actual_pilot_calibration": {
        "note": "the §16 ratio model applied to the pilot's own 12 spec points "
                "versus the pilot's actuals — the calibration baseline future "
                "batches are measured against",
        "rows": rows,
    },
    "rates": rates,
    "false_positive_categories": fp_categories,
    "future_batch_records": [
        {
            "batch_id": "c11-s16-batch-1",
            "session": 47,
            "commissioned": "operator ('run batch 1', 2026-09-12)",
            "scope": "S1 remainder, first 12 SPs (4CH1-1.1-1.12) + PR-01",
            "spec_points": 12,
            "notes": 10,
            "mark_schemes_pinned": 2,
            "predicted": {"nodes": 28.8, "authored_edges": 33.0,
                          "held_candidates": 12.0},
            "actual": {"nodes": 24, "authored_edges": 29,
                       "held_candidates": 12},
            "delta_pct": {"nodes": -16.7, "authored_edges": -12.1,
                          "held_candidates": 0.0},
            "rates": {
                "held_rate": 0.2927,
                "rejection_rate": 0.0,
                # session-48: 28 of the 29 authored edges promoted via §18
                # (the 29th is the RR quarantine, settled HOLD_REVIEW_REQUIRED)
                "promotion_rate": 0.9655,
                "operator_review_rate": 1.0,
            },
            "false_positive_categories_observed": [
                "FP-2 (split-artifact candidates: states/particle-model pair, "
                "solution triple, pure-substance granularity — operator "
                "identity decisions)",
                "FP-3 (granularity notes: pure-substance node, 1.1 energy "
                "boundary)",
                "FP-4 (quarantine discipline applied at authoring: "
                "CRYSTALLISATION->SOLUTION RR, subsumption class)",
            ],
            "operator_verdicts": {"confirm": 28, "reject": 0, "hold": 0,
                                  "merge": 0, "split": 0},
            "notes_text": ("pred-vs-act: the slice is terminology/technique-"
                           "heavy rather than calculation-heavy — fewer "
                           "separable procedures than the pilot's "
                           "mole/stoichiometry backbone, hence nodes "
                           "-16.7% / edges -12.1% vs the 2.4/2.75 model; "
                           "held exactly on model (12). 1 pass-1 self-"
                           "quarantine (subsumption-class RR) + 1 pass-2 "
                           "concordant HOLD on it; zero pass-2 demotions of "
                           "asserted edges (abstention landed at authoring). "
                           "operator_verdicts all zero: the per-batch "
                           "operator gate is PENDING (sheet: "
                           "C11_BATCH1_REVIEW_SHEET.md; template: "
                           "scripts/c11_batch1_verdicts_template.yaml). "
                           "Mark-scheme mining: 2 of 4 slice-relevant "
                           "Unit-1-P1 MS files pinned (SOM, ECM2); ECM1/ECM3 "
                           "+ Paper-2 remain for later passes (FN-B1-1). "
                           "Session-48 (2026-09-12): gate SETTLED — operator "
                           "ruling 'CONFIRM all' recorded in "
                           "scripts/c11_batch1_verdicts.yaml (28 edge "
                           "CONFIRM / 24 node CONFIRM / 4 KEEP_AS_IS / RR "
                           "HOLD_REVIEW_REQUIRED / held acknowledged) and "
                           "applied through §18 (28 promotions, operator; "
                           "the RR quarantine stays un-promoted)."),
        },
        {
            "batch_id": "c11-s16-batch-2",
            "session": 49,
            "commissioned": "operator ('run batch 2', 2026-09-12)",
            "scope": "S1 remainder, second 12 SPs (4CH1-1.13-1.24) + PR-02",
            "spec_points": 12,
            "notes": 7,
            "mark_schemes_pinned": 6,
            "predicted": {"nodes": 28.8, "authored_edges": 33.0,
                          "held_candidates": 13.0},
            "actual": {"nodes": 14, "authored_edges": 23,
                       "held_candidates": 10},
            "delta_pct": {"nodes": -51.4, "authored_edges": -30.3,
                          "held_candidates": -23.1},
            "rates": {
                "held_rate": 0.3030,
                "rejection_rate": 0.0,
                "promotion_rate": 1.0,
                "operator_review_rate": 1.0,
            },
            "false_positive_categories_observed": [
                "FP-2 (split-artifact candidates: subatomic particle triple, "
                "periodic-table arrangement+group+period, metal/non-metal "
                "1.20/1.21 — operator identity decisions)",
                "FP-B2-2 (relation-class choices: the two EXPLAINED_BY "
                "edges + the CON-AR->CON-ISOTOPES boundary reading)",
                "FP-B2-3 (first COMMONLY_CONFUSED_WITH deployment)",
            ],
            "operator_verdicts": {"confirm": 23, "reject": 0, "hold": 0,
                                  "merge": 0, "split": 0},
            "notes_text": ("pred-vs-act: nodes -51.4% / edges -30.3% vs the "
                           "2.4/2.75 model — the delta is the BOUNDARY "
                           "DISCIPLINE, not thin coverage: the Ar term was "
                           "not re-minted (the pilot CON-AR owns it; 1.16's "
                           "Ar definition reached via the CON-ISOTOPES "
                           "attachment + the boundary edge), and 1.13 "
                           "attaches no batch-2 node (its concept content is "
                           "the batch-1 chromatography triplet reached via "
                           "the sanctioned PR-02 boundary edges). 5 "
                           "cross-boundary edges into earlier-record nodes; "
                           "zero RR authored (every doubt held or resolved "
                           "on explicit evidence); 10 held; two "
                           "mark-scheme-documented misconceptions (isotopes-"
                           "differ-in-protons, RAM-vs-mass-number — both "
                           "REJECT-column layout-verified). "
                           "Session-50 (2026-09-12): operator gate SETTLED — "
                           "ruling \"CONFIRM all\" recorded in "
                           "scripts/c11_batch2_verdicts.yaml (23 edge "
                           "CONFIRM / 14 node CONFIRM / 4 KEEP_AS_IS / held "
                           "acknowledged) and applied through §18 (23 "
                           "promotions, operator, review_ref = the B2 "
                           "diff-review bundle; promotion_rate 1.0 — zero RR "
                           "authored, so every authored edge was promotable "
                           "post-verdict). Mark-scheme mining: 6 pins "
                           "(ATOM1-3, PT, ECM1/ECM3 — the ECM pins close "
                           "the batch-1 FN-B1-1 remainder); Paper-2 variants "
                           "remain (FN-B2-1)."),
        },
        {
            "batch_id": "c11-s16-batch-3",
            "session": 51,
            "commissioned": "operator (session-51 move-forward directive, 2026-09-12)",
            "scope": "the FULL S1 remainder, 24 SPs (4CH1-1.37-1.60C) + PR-04",
            "spec_points": 24,
            "notes": 14,
            "mark_schemes_pinned": 3,
            "predicted": {"nodes": 57.6, "authored_edges": 66.0,
                          "held_candidates": 24.0},
            "actual": {"nodes": 24, "authored_edges": 39,
                       "held_candidates": 14},
            "delta_pct": {"nodes": -58.3, "authored_edges": -40.9,
                          "held_candidates": -41.7},
            "rates": {
                "held_rate": 0.2642,
                "rejection_rate": 0.0,
                # session-52: gate SETTLED — 39 authored edges CONFIRMed and
                # promoted via §18 (zero RR authored, so every authored
                # edge was promotable post-verdict)
                "promotion_rate": 1.0,
                "operator_review_rate": 1.0,
            },
            "false_positive_categories_observed": [
                "FP-B3-1 (know/understand dual-attachment split candidates: "
                "1.43+1.56C, 1.44+1.45, 1.51+1.55C, 1.52C+1.53C — operator "
                "identity decisions)",
                "FP-B3-2 (relation-class choices: the EXPLAINED_BY "
                "metal-properties edge + the ELECTROLYSIS->IONIC-BOND "
                "reachable-ne-redundant density flag)",
                "FP-B3-3/4 (first RELATED_TO + second COMMONLY_CONFUSED_WITH "
                "deployments)",
            ],
            "operator_verdicts": {"confirm": 39, "reject": 0, "hold": 0,
                                  "merge": 0, "split": 0},
            "notes_text": ("pred-vs-act: nodes -58.3% / edges -40.9% vs the "
                           "2.4/2.75 model — the deltas are the boundary "
                           "discipline AND the commissioned 24-SP scope: no "
                           "batch-2 identity re-minted (ATOM / "
                           "ELECTRONIC-CONFIGURATION / MOLECULE reached via 6 "
                           "sanctioned boundary edges); the spec's own "
                           "know/understand pairs merged as dual attachments "
                           "(4 pairs); the bonding families mint one node "
                           "per SP-family rather than per term (the "
                           "solution-triple granularity); 1.60C attaches no "
                           "concept node (the practical owns it — the 1.13 "
                           "precedent). Zero RR authored (every doubt held "
                           "or resolved on explicit evidence); 14 held; four "
                           "misconceptions (1 examiner-tip erroneous belief + "
                           "3 mark-scheme wrong answers, REJECT columns "
                           "layout-verified). FN-B2-1 CLOSED: 3 Paper-2 pins "
                           "(IONIC/COVALENT/CFEC); coverage fact — PMT "
                           "publishes no metallic-bonding/electrolysis MS "
                           "(B3-H-11/H-12). "
                           "Session-52 (2026-09-13): operator gate SETTLED — "
                           "the practical-review policy applied per row "
                           "(scripts/c11_batch3_verdicts.yaml: 39 edge "
                           "CONFIRM / 24 node CONFIRM / 7 identity decisions "
                           "KEEP_AS_IS / 14 held acknowledged — a clean "
                           "quarantine) and applied through §18 (39 "
                           "promotions, operator, review_ref = the B3 "
                           "diff-review bundle; promotion_rate 1.0 — zero RR "
                           "authored, so every authored edge was promotable "
                           "post-verdict). Section 1 coverage COMPLETE "
                           "(pilot + batches 1-3 = all 60 S1 SPs)."),
        },
        {
            "batch_id": "c11-s16-batch-4",
            "session": 53,
            "commissioned": ("operator (session-53 batch-4 directive, "
                             "2026-09-13: 'Execute Batch 4 using the "
                             "established Batch-1/2/3 machinery.'"),
            "scope": ("Section 3 — Physical Chemistry, 22 SPs "
                      "(4CH1-3.1-3.22C: Energetics / Rates of Reaction / "
                      "Reversibility & Equilibria) + PR-09/PR-10/PR-11"),
            "spec_points": 22,
            "notes": 15,
            "mark_schemes_pinned": 3,
            "predicted": {"nodes": 52.8, "authored_edges": 60.5,
                          "held_candidates": 22.0},
            "actual": {"nodes": 22, "authored_edges": 35,
                       "held_candidates": 14},
            "delta_pct": {"nodes": -58.3, "authored_edges": -42.1,
                          "held_candidates": -36.4},
            "rates": {
                "held_rate": 0.2857,
                "rejection_rate": 0.0,
                # session-54: gate SETTLED — the operator's batch-4 verdicts
                # applied through §18 (35 promotions, operator); zero RR
                # authored, so every authored edge was promotable
                # post-verdict
                "promotion_rate": 1.0,
                "operator_review_rate": 1.0,
            },
            "false_positive_categories_observed": [
                "FP-B4-1 (boundary-evidence asymmetry: the bond-energy -> "
                "covalent-bond edge rests on the worked-example bond set + "
                "the ruling, the note says 'chemical bond' — confidence "
                "medium, flagged for the operator)",
                "FP-B4-2 (evidence-strength: two medium-confidence "
                "misconception rows — the antonym-attributed pressure reject "
                "+ the two-source bond-count tip/MS pair)",
                "FP-B4-3 (dual attachments: 3.12+3.13, 3.19C+3.20C, "
                "3.21C+3.22C know pairs + the 3.14C dual node attachment — "
                "operator identity decisions B4-ID-01..04)",
                "FP-B4-4 (family shape: the 3.9/3.10/3.11 "
                "experiment/describe/explain triple minted as three nodes "
                "with one EXPLAINED_BY and no prereqs among them; B4-ID-05/06)",
            ],
            "operator_verdicts": {"confirm": 35, "reject": 0, "hold": 0,
                                  "merge": 0, "split": 0},
            "notes_text": ("pred-vs-act: nodes -58.3% / edges -42.1% vs "
                           "the 2.4/2.75 model — the same per-SP yield band "
                           "as batch 3 (nodes/SP 1.0, edges/SP 1.6): the "
                           "boundary discipline and SP-family granularity "
                           "again, not thin coverage. No S1 identity "
                           "re-minted — the FIVE ruled targets (CON-MOLE, "
                           "CON-COVALENT-BOND, CON-CONCENTRATION, "
                           "CON-EQ-SYMBOL, CON-WATER-CRYST) reached via "
                           "exactly 5 sanctioned cross-section boundary "
                           "edges (a considered sixth — the gas-molecule "
                           "counting operand — held as B4-H-14 for the "
                           "operator, not silently authored); 3.8/3.15/3.16 "
                           "attach no concept node (the practicals own "
                           "them — the 1.13/1.60C precedent); the spec's "
                           "know pairs merged as dual attachments (3.12+3.13, "
                           "3.19C+3.20C, 3.21C+3.22C). Zero RR authored; 14 "
                           "held (including the four CLASSIC misconceptions "
                           "refused for missing documentation — static "
                           "equilibrium, consumed catalyst, catalyst-shifts-"
                           "position, bond-breaking exo/endo swap — the "
                           "session-53 Step-3 rule); five misconceptions "
                           "minted, all mark-scheme-documented (the catalyst "
                           "particle-energy cap in BOTH S3 Paper-2 MS; the "
                           "equilibrium reject/accept antonym pairs; the "
                           "J-to-kJ partial-credit rule; the bond-count "
                           "deduction + tip). FULL S3 Paper-2 MS coverage "
                           "for the first time (all three families pinned; "
                           "the RATES and RRE pins overlap — recorded). "
                           "Session-54 (2026-09-13): operator gate SETTLED — "
                           "the practical verdict policy applied with the "
                           "two §3 special-attention rulings recorded "
                           "(FP-B4-1: the bond-energy -> covalent-bond "
                           "boundary row's evidence inspected and found "
                           "sufficient — the note's own dependency "
                           "statement + all-covalent worked examples + the "
                           "displayed-formula tip + the session-52 ruling; "
                           "FP-B4-2: both medium-confidence misconception "
                           "rows' MS evidence inspected — the per-mistake "
                           "deduction + tip naming, the byte-verified "
                           "reject entry) in scripts/c11_batch4_verdicts.yaml "
                           "(35 edge CONFIRM / 22 node CONFIRM / 6 identity "
                           "decisions KEEP_AS_IS / 14 held acknowledged — "
                           "quarantined, a held record is a valid outcome) "
                           "and applied through §18 (35 promotions, "
                           "operator, review_ref = the B4 diff-review "
                           "bundle; promotion_rate 1.0; store total 153). "
                           "Section 3 coverage SETTLED (S1 60 + S3 22 = 82 "
                           "of 182 SPs)."),
        },
        {
            # session-55 (2026-09-22): batch-5 AUTHORED to its operator gate
            # — the descriptive S2 slice runs lighter than the 2.4/2.75
            # model, exactly as the item-14 plan anticipated for S2
            # ("descriptive-heavy; expected lighter on procedures").
            "batch_id": "c11-s16-batch-5",
            "session": 55,
            "commissioned": ("operator ('run batch 5', 2026-09-22, session "
                             "55) under the session-46 §16 authorization"),
            "scope": ("Section 2 — Inorganic Chemistry FIRST slice, 14 SPs "
                      "(4CH1-2.1-2.14: a Group 1 Alkali Metals / b Group 7 "
                      "Halogens / c Gases in the Atmosphere) + PR-05"),
            "spec_points": 14,
            "notes": 9,
            "mark_schemes_pinned": 3,
            "predicted": {"nodes": 33.6, "authored_edges": 38.5,
                          "held_candidates": 14.0},
            "actual": {"nodes": 16, "authored_edges": 18,
                       "held_candidates": 14},
            "delta_pct": {"nodes": -52.4, "authored_edges": -53.2,
                          "held_candidates": 0.0},
            "rates": {
                "held_rate": 0.2917,
                "rejection_rate": 0.0,
                # session-56: gate SETTLED — the operator's batch-5 verdicts
                # applied through §18 (18 promotions, operator); zero RR
                # authored, so every authored edge was promotable
                # post-verdict
                "promotion_rate": 1.0,
                "operator_review_rate": 1.0,
            },
            "false_positive_categories_observed": [
                "FP-B5-1 (trend-direction symmetry: the 2.4C/2.8C "
                "explanations minted as SEPARATE nodes — electron loss vs "
                "gain, opposite directions; identity decision B5-ID-01)",
                "FP-B5-2 (misconception discipline: three MS-documented "
                "wrong-answer patterns minted — the GROUP1 IGNORE/award "
                "rules, the GROUP7 halogen/halide Reject column, the GASES "
                "CuO-colour Reject column; the near-misses held, not "
                "minted — B5-H-04/H-05/H-06)",
                "FP-B5-3 (boundary discipline: exactly 3 sanctioned "
                "boundary edges into 2 ruled owners; the redox-in-"
                "displacement surface is MS-only and OD-2-incidental in "
                "the 2.11 tip — held B5-H-08/H-11 for the operator)",
                "FP-B5-4 (family shape: composition/determination minted "
                "as know-facts vs method with one EXPLAINED_BY grounding "
                "edge; the practical owns 2.14 with a practical->concept "
                "edge — B5-ID-02/03)",
            ],
            "operator_verdicts": {"confirm": 18, "reject": 0, "hold": 0,
                                  "merge": 0, "split": 0},
            "notes_text": ("pred-vs-act: nodes -52.4% / edges -53.2% vs "
                           "the 2.4/2.75 model — the lightest yield band so "
                           "far (nodes/SP 1.14, edges/SP 1.29): the "
                           "descriptive-heavy S2 families mint fewer, "
                           "self-contained nodes (the plan's own S2 "
                           "anticipation), and the boundary discipline "
                           "abstains where the notes re-teach inline (the "
                           "B5-H-02/H-03 holds). No S1/S3 identity "
                           "re-minted — the TWO ruled targets reached via "
                           "exactly 3 sanctioned cross-section boundary "
                           "edges (2.4C + 2.8C -> CON-ELECTRONIC-"
                           "CONFIGURATION; 2.11 -> CON-EXO-ENDO); 2.14 "
                           "attaches no concept node (PR-05 owns it — the "
                           "1.13/1.60C precedent) with the practical->"
                           "concept edge authored. Zero RR authored; 14 "
                           "held (the ≈1-per-SP band; every classic "
                           "misconception without pinned documentation "
                           "refused — the session-53 Step-3 rule); three "
                           "misconceptions minted, all mark-scheme-"
                           "documented (IGNORE/award-restriction, Reject "
                           "columns). FULL batch-5 Paper-2 MS coverage (all "
                           "three families pinned — as in batch 4). "
                           "Section 2 candidate coverage: 14 of 50 S2 SPs "
                           "(96 of 182 total at candidate level). "
                           "Session-56 (2026-09-22): operator gate SETTLED — "
                           "the completed review sheet §6 verdict applied: "
                           "18 edge CONFIRM promoted via §18 (store total "
                           "171; zero RR authored; 6 identity decisions "
                           "KEEP_AS_IS; 14 held preserved — quarantined; the "
                           "B5-E-01 grounding-relation qualification and the "
                           "four pass-2 WITH_NOTE node qualifications "
                           "recorded in the verdict notes; verdict record "
                           "scripts/c11_batch5_verdicts.yaml). "
                           "session-56 CORRECTION (dated): the record's "
                           "actual authored_edges was appended as 17 at the "
                           "session-55 gate — the authoritative count is 18 "
                           "(the decision record, the review JSON pass1, the "
                           "sheet §1, and the store all carry 18; the "
                           "record's own held_rate 14/48 already assumed 18); "
                           "corrected here with the matching delta_pct and "
                           "edges/SP rate.)"),
        },
        {
            # session-57 (2026-09-22): batch-6 AUTHORED to its operator
            # gate — the S2-d/e slice runs in the descriptive band like
            # batch 5; the unpinned extraction family caps the
            # misconception mining at the one clean Reject column.
            "batch_id": "c11-s16-batch-6",
            "session": 57,
            "commissioned": ("operator ('commission batch 6', 2026-09-22, "
                             "session 57) under the session-46 §16 "
                             "authorization"),
            "scope": ("Section 2 — Inorganic Chemistry SECOND slice, 13 SPs "
                      "(4CH1-2.15-2.27: d Reactivity Series / e Extraction "
                      "& Uses of Metals) + PR-06"),
            "spec_points": 13,
            "notes": 10,
            "mark_schemes_pinned": 1,
            "predicted": {"nodes": 31.2, "authored_edges": 35.8,
                          "held_candidates": 13.0},
            "actual": {"nodes": 13, "authored_edges": 16,
                       "held_candidates": 9},
            "delta_pct": {"nodes": -58.3, "authored_edges": -55.3,
                          "held_candidates": -30.8},
            "rates": {
                "held_rate": 0.2368,
                "rejection_rate": 0.0,
                # session-58: gate SETTLED — the operator's batch-6 verdicts
                # (completed review sheet §6, PASS WITH NOTE) applied through
                # §18 (16 promotions, operator); zero RR authored, so every
                # authored edge was promotable post-verdict
                "promotion_rate": 1.0,
                "operator_review_rate": 1.0,
            },
            "false_positive_categories_observed": [
                "FP-B6-1 (identity overlap: the 2.20 term-family node vs "
                "the batch-3 CON-REDOX-ELECTRONS owner — the broader "
                "demand + the note's inline electron-framework teaching; "
                "identity decision B6-ID-01, no boundary edge, no "
                "re-mint)",
                "FP-B6-2 (misconception evidence asymmetry: the ONE clean "
                "Reject-column mint vs the unpinned extraction family — "
                "no PMT MS exists in any unit; the Q1ai IGNORE class "
                "held B6-H-03)",
                "FP-B6-3 (boundary discipline: exactly 4 sanctioned "
                "boundary edges into 4 ruled targets — 2 existing owners "
                "+ the 2 deferral closures the batch-5 ruling explicitly "
                "deferred to 'the batch that mints it')",
                "FP-B6-4 (family shape: method-vs-evaluation split "
                "B6-ID-02, the trio/conditions/definition splits "
                "B6-ID-03..05, the single-Reject-column mint B6-ID-06; "
                "the practical owns 2.21 with a practical->concept "
                "edge)",
            ],
            "operator_verdicts": {"confirm": 16, "reject": 0, "hold": 0,
                                  "merge": 0, "split": 0},
            "notes_text": ("pred-vs-act: nodes -58.3% / edges -55.3% vs "
                           "the 2.4/2.75 model — the S2 descriptive band "
                           "(nodes/SP 1.0, edges/SP 1.23): the one-"
                           "node-per-SP-family shape held exactly (12 "
                           "concept-bearing SPs + the PR-06-owned "
                           "practical), and the boundary discipline "
                           "abstains where the notes re-teach inline "
                           "(B6-H-01/02/06/08). No existing identity "
                           "re-minted — the FOUR ruled targets reached "
                           "via exactly 4 sanctioned cross-section "
                           "boundary edges (2.23C -> CON-ELECTROLYSIS; "
                           "2.25C -> CON-METAL-PROPERTIES; the batch-5 "
                           "deferral closures 2.12 -> CON-REACT-ORDER "
                           "and 2.10 -> CON-RUSTING, closing held "
                           "B5-H-10 and the iron-route note verbatim); "
                           "2.21 attaches no concept node (PR-06 owns "
                           "it — the 1.13/1.60C/2.14 precedent) with "
                           "the practical->concept edge authored. Zero "
                           "RR authored; 9 held. ONE misconception "
                           "minted, mark-scheme-documented (the "
                           "REACTIVITY MS Q2a Reject column — the "
                           "MIS-CUO-COLOUR-class narrow-but-exact "
                           "pattern). PARTIAL Paper-2 MS coverage: the "
                           "Reactivity family pinned; the extraction "
                           "family UNPINNED (no PMT MS in any unit — "
                           "the batch-1..3 convention, recorded in "
                           "meta.ms_coverage_note). One pass-2 finding "
                           "re-authored before the gate (FP-B6-5, a "
                           "non-load-bearing 2-word evidence fragment "
                           "replaced by order-relative facts). Section "
                           "2 candidate coverage: 27 of 50 S2 SPs (109 "
                           "of 182 total at candidate level). "
                           "Session-58 (2026-09-22): operator gate "
                           "SETTLED — the completed review sheet §6 "
                           "verdict applied (PASS WITH NOTE): 16 edge "
                           "CONFIRM promoted via §18 (store total 187; "
                           "zero RR authored; 6 identity decisions "
                           "KEEP_AS_IS; 9 held preserved — quarantined; "
                           "the B6-E-09 route-specific guardrail "
                           "qualification and the three pass-2 WITH_NOTE "
                           "node qualifications recorded in the verdict "
                           "notes; the completed sheet's §1-5 carried "
                           "exactly FOUR machine-checked typographic "
                           "drift lines against the in-repo gate sheet — "
                           "zero verdict-relevant change; verdict record "
                           "scripts/c11_batch6_verdicts.yaml)."),
        },
        {
            # session-59 (2026-09-23): batch-7 AUTHORED to its operator
            # gate — the S2-f/g slice (acids/alkalis/salt prep); FULL
            # Paper-2 MS coverage (both families pinned — the best of any
            # slice), TWO clean documented WAP mints.
            "batch_id": "c11-s16-batch-7",
            "session": 59,
            "commissioned": ("operator ('Proceed with batch 7', 2026-09-23, "
                             "session 59) under the session-46 §16 "
                             "authorization"),
            "scope": ("Section 2 — Inorganic Chemistry THIRD slice, 16 SPs "
                      "(4CH1-2.28-2.43C: f Acids, Alkalis & Titrations / "
                      "g Acids, Bases & Salt Preparations) + PR-07/PR-08"),
            "spec_points": 16,
            "notes": 12,
            "mark_schemes_pinned": 2,
            "predicted": {"nodes": 38.7, "authored_edges": 42.7,
                          "held_candidates": 17.3},
            "actual": {"nodes": 15, "authored_edges": 19,
                       "held_candidates": 9},
            "delta_pct": {"nodes": -61.2, "authored_edges": -55.5,
                          "held_candidates": -48.0},
            "rates": {
                "held_rate": 0.2093,
                "rejection_rate": 0.0,
                # session-59: the batch ends at its operator gate — zero
                # promotions exist at authoring; promotion rides the
                # operator's §18 verdict session
                "promotion_rate": 0.0,
                "operator_review_rate": 1.0,
            },
            "false_positive_categories_observed": [
                "FP-B7-1 (identity shape: the 2.35/2.36 proton-transfer "
                "family as ONE node attaching both SPs — the note's own "
                "extend-the-earlier-definition structure; B7-ID-01)",
                "FP-B7-2 (edge-evidence asymmetry: the titration->indicators "
                "pair carries method-step + suitability-teaching anchors "
                "complementarily)",
                "FP-B7-3 (WAP-target reading: the endpoint misconception "
                "anchored at CON-NEUTRALISATION (the completion surface), "
                "the temperature-experiment context recorded, not dropped "
                "(the S3 3.8/PR-09 future_boundary_note))",
                "FP-B7-4 (source-note conflict RE-AUTHORED BEFORE the "
                "gate: the lead-sulfate note's 'Wash filtrate' line "
                "conflicts with the pinned Salt-Prep MS Q7a(iii) — the "
                "PR-08 anchors swapped to the aim + filtration sentences)",
                "FP-B7-5 (G04 discipline: the hydronium MS anchor moved "
                "out of the 2.36 CONCEPT attachment — MARK_SCHEME anchors "
                "are misconception-class-only on concept attachments)",
            ],
            "operator_verdicts": {"confirm": 0, "reject": 0, "hold": 0,
                                  "merge": 0, "split": 0},
            "notes_text": ("pred-vs-act: nodes -61.2% / edges -55.5% vs "
                           "the 2.4/2.75 model — the S2 descriptive band "
                           "(nodes/SP 0.94, edges/SP 1.19): 13 concept-"
                           "bearing SP-families (2.35+2.36 as ONE family "
                           "node) + the PR-07/PR-08-owned practicals, and "
                           "the boundary discipline abstains where the "
                           "notes re-teach the separation steps inline "
                           "(the S1 filtration/crystallisation/evaporation/"
                           "saturation owners untouched). No existing "
                           "identity re-minted — the TWO ruled targets "
                           "reached via exactly 2 sanctioned cross-section "
                           "boundary edges (2.37 -> CON-REACT-ORDER, the "
                           "batch-6 owner; 2.34 -> CON-ION-CHARGE-RULES, "
                           "the batch-3 owner); 2.42/2.43C attach no "
                           "concept node (PR-07/PR-08 own them — the "
                           "1.13/1.60C/2.14/2.21 precedent) with the "
                           "practical->concept edges authored. Zero RR "
                           "authored; 9 held (B7-H-04 the insufficient-"
                           "characterization refusal; B7-H-06 the "
                           "note-anchored ERRONEOUS_BELIEF lane held for "
                           "operator ruling). TWO misconceptions minted, "
                           "both mark-scheme-documented (the Titrations "
                           "MS Q2a(iv) Reject column and the Salt-Prep MS "
                           "Q2a(iii) class). FULL Paper-2 MS coverage — "
                           "both families pinned (the best of any slice; "
                           "meta.ms_coverage_note). One pass-2 finding "
                           "re-authored before the gate (FP-B7-4). "
                           "Section 2 candidate coverage: 43 of 50 S2 SPs "
                           "(125 of 182 total at candidate level). "
                           "NEXT: the batch-7 operator verdict session "
                           "(fill scripts/c11_batch7_verdicts_template.yaml "
                           "-> rename); the remaining S2-h family "
                           "(2.44-2.50 chemical tests) is batch 8."),
        },
    ],
    "future_batch_record_schema": {
        "batch_id": "c11-s16-batch-N (extraction_pass id)",
        "spec_points": "count in the batch scope",
        "predicted": {"nodes": "model ratio x SP count",
                      "authored_edges": "...", "held_candidates": "..."},
        "actual": {"nodes": "...", "authored_edges": "...",
                   "held_candidates": "..."},
        "delta_pct": {"nodes": "...", "authored_edges": "...",
                      "held_candidates": "..."},
        "rates": {"held_rate": "...", "rejection_rate": "...",
                  "promotion_rate": "...", "operator_review_rate": "..."},
        "false_positive_categories_observed": ["FP-1", "..."],
        "operator_verdicts": {"confirm": 0, "reject": 0, "hold": 0,
                              "merge": 0, "split": 0},
        "notes": "per-batch anomalies, ODs invoked, boundary minting decisions",
    },
}

(REPORTS / "C11_BATCH_FORECAST.json").write_text(
    json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("wrote", REPORTS / "C11_BATCH_FORECAST.json")
print("pilot:", json.dumps(out["pilot_baseline"]["ratios_per_sp"]))
print("calibration:", json.dumps(rows))
print("rates:", json.dumps({k: v["value"] for k, v in rates.items()}))
