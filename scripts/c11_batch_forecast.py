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
    "session": 52,
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
                   "family; authoring to the operator gate is the next "
                   "session's extraction); batches 5-14 not started"),
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
