#!/usr/bin/env python3
"""T-C11 session 43 — batch forecasting instrumentation.

Emits graph/reports/C11_BATCH_FORECAST.json: the machine-computed pilot
baseline, the §16 documented projection (C11_S16_GATE_REPORT.md item 14,
PROPOSAL — not executed), a predicted-vs-actual calibration of the projection
model against the pilot's own actuals, the review rates with documented
formulas, the false-positive categories observed across the pilot's review
history, and the empty future-batch record list that §16 batches append to.

READ-ONLY with respect to the graph: writes only its own report. No
promotion, no graph modification, no §16 action (the projection figures are
referenced, never executed).
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
REPORTS = REPO / "graph" / "reports"

dec = yaml.safe_load((HERE / "c11_pilot_decisions.yaml").read_text(encoding="utf-8"))
graph_edges = yaml.safe_load((REPO / "graph" / "concept_edges.yaml")
                             .read_text(encoding="utf-8"))["edges"]
promo = yaml.safe_load((HERE / "c11_promotions.yaml").read_text(encoding="utf-8"))

nodes = dec["nodes"]
edges = dec["edges"]
held = dec["held"]
sps = dec["meta"]["scope"]["spec_points"]

n_nodes = len(nodes)
n_authored = len(edges)
n_part_of = sum(1 for e in graph_edges if e["relation"] == "PART_OF")
n_total = len(graph_edges)
n_held = sum(1 for h in held if h["status"] == "held")
n_rejected = sum(1 for h in held if h["status"] == "rejected")
n_promoted = len(promo.get("promotions", []))
n_hv = sum(1 for e in graph_edges if e["validation_status"] == "HUMAN_VALIDATED")

# The 31 SUGGESTED authored edges awaiting per-row confirmation
# (29 unmarked + 2 PENDING-gated; the REVIEW_REQUIRED operator-HOLD edge is
# excluded from the per-row surface — it already carries an operator verdict).
suggested_authored = [e for e in edges if e["validation_status"] == "SUGGESTED"]

# --- §16 documented projection (PROPOSAL — referenced, never executed) ------
S16_SOURCE = ("graph/reports/C11_S16_GATE_REPORT.md item 14 "
              "(PROPOSAL — not executed; §16 not authorized)")
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
        "meaning": "0 by design this round: nothing is ratified until the "
                   "operator records verdicts (this package's purpose)",
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
     "current_state": "flagged in the session-43 package appendix; §19 text "
                      "unchanged (documentation-only finding)",
     "mitigation": "machine-counted failure_class fields in expansion-round "
                   "held entries (§19 already mandates this for expansion)"},
]

out = {
    "task": "T-C11",
    "instrument": "batch-forecast",
    "session": 43,
    "generated": "2026-09-12",
    "baselines": {"resources": "3b70dde", "syllabai": "6d36fb0"},
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
        "total_edges": n_total,
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
        "status": "PROPOSAL ONLY — §16 NOT authorized; nothing executed",
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
    "future_batch_records": [],
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
