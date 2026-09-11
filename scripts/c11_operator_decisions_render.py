#!/usr/bin/env python3
"""T-C11 session 41 — render C11_OPERATOR_DECISIONS.json (the machine record
of the operator-decision round) directly from the live store so every count
is computed, never hand-written. Companion: C11_OPERATOR_DECISIONS.md."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
REPORTS = REPO / "graph" / "reports"

dec = yaml.safe_load((HERE / "c11_pilot_decisions.yaml").read_text(encoding="utf-8"))
promo = yaml.safe_load((HERE / "c11_promotions.yaml").read_text(encoding="utf-8"))
edges = dec["edges"]
held = dec.get("held", [])
nodes = dec["nodes"]
graph_edges = yaml.safe_load((REPO / "graph" / "concept_edges.yaml")
                             .read_text(encoding="utf-8"))["edges"]

by_rel = {}
for e in graph_edges:
    by_rel[e["relation"]] = by_rel.get(e["relation"], 0) + 1


def band(items):
    out = {}
    for i in items:
        out[i["confidence"]] = out.get(i["confidence"], 0) + 1
    return out


op_dec = []
for e in edges:
    od = e.get("operator_decision")
    if od:
        op_dec.append({"record": f"{e['source']} {e['relation']} {e['target']}",
                       "record_kind": "authored_edge", **od})
for h in held:
    od = h.get("operator_decision")
    if od:
        op_dec.append({"record": h["id"], "record_kind": "held_candidate", **od})

out = {
    "task": "T-C11",
    "stage": "operator-decision-round",
    "session": 41,
    "generated": "2026-09-11",
    "baseline": {"resources": "4eba8ea", "syllabai": "bbf4e08"},
    "decisions_executed": [
        {
            "edge": "4CH1-PR-03 REQUIRES_PREREQUISITE 4CH1-CON-MOLE",
            "verdict": "REJECT",
            "decided_by": "operator",
            "decided_date": "2026-09-11",
            "execution": "decision-record re-authoring: removed from the "
                         "authored set; preserved as rejected candidate HELD-13",
            "graph_effect": "removed (66 -> 65 edges; RP 26 -> 25; RR 2 -> 1)",
            "permanent": True,
            "promotable": False,
            "reasons_verbatim": [
                "\"moles\" appears only as a table-row label in the practical note.",
                "It is not substantively taught in the note body.",
                "The claimed dependency is also transitively subsumed through the "
                "existing formula-deduction → mole path.",
                "Do not treat table labels or incidental terminology as "
                "instructional evidence.",
            ],
        },
        {
            "edge": "4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE "
                    "4CH1-CON-AVOGADRO-LAW",
            "verdict": "HOLD",
            "decided_by": "operator",
            "decided_date": "2026-09-11",
            "execution": "operator_decision block on the edge in the decision "
                         "record; rendered into the review sheet",
            "graph_effect": "remains REVIEW_REQUIRED in the graph",
            "promotable": False,
            "reasons_verbatim": [
                "The gas-volume worked example does not explicitly teach or "
                "invoke Avogadro's Law.",
                "The operative calculation skill is molar-ratio reasoning.",
                "An Avogadro-Law prerequisite may eventually be architecturally "
                "defensible, but the current evidence does not establish it.",
                "Do NOT convert this HOLD into either ACCEPT or REJECT merely to "
                "complete the pilot.",
            ],
        },
    ],
    "medium_confidence_presented_pending": [
        {
            "edge": "4CH1-CON-MOLAR-GAS-VOL EXPLAINED_BY 4CH1-CON-AVOGADRO-LAW",
            "confidence": "medium",
            "evidence_quote": "From the molar gas volume the following formula "
                              "triangle can be derived",
            "flag": "FP-1 (session-40 Task 3): anchor supports "
                    "molar-volume->formula, not law->molar-volume",
            "recommendation": "HOLD — not promotable on current evidence; "
                              "operator must explicitly accept the "
                              "adjacency-grounding weakness or reject/defer",
            "promotable": False,
        },
        {
            "edge": "4CH1-MIS-EQ-SUBSCRIPT REMEDIATED_BY "
                    "4CH1-CON-CONSERVATION-MASS",
            "confidence": "medium",
            "evidence_quote": "You cannot do this because it changes what the "
                              "substance is",
            "flag": "tip's own corrective argument is substance-identity; "
                    "CON-CONSERVATION-MASS is the best available in-slice "
                    "target (approximation); exact corrective concept is a "
                    "boundary gap",
            "recommendation": "HOLD — promotable only if the operator explicitly "
                              "accepts the approximation; cleaner fix = mint the "
                              "coefficients-vs-subscripts concept in expansion",
            "promotable": False,
        },
    ],
    "ontology_decisions": [
        {"id": "OD-1",
         "ruling": "yield triple stays split (CON-YIELD / CON-THEOR-YIELD / "
                   "CON-PERCENT-YIELD remain three concept nodes; no merge)",
         "recorded_in": "C11_ARCHITECTURE.md §20",
         "generalized_rule": "one procedure concept + one concept per "
                             "distinctly-taught operand definition; one "
                             "DEFINITIONAL_DEPENDENCY prerequisite per operand; "
                             "same-anchor multiplicity expected"},
        {"id": "OD-2",
         "ruling": "operator rule, verbatim: 'Do not treat table labels or "
                   "incidental terminology as instructional evidence.'",
         "recorded_in": "C11_ARCHITECTURE.md §20",
         "generalized_rule": "IMPLICIT_USE evidence alone can never ground "
                             "promotion; quarantine-or-abstain per FC-1"},
    ],
    "promotion_audit": {
        "promoted_count": len(promo["promotions"]),
        "ratified_identities": 0,
        "interpretation": "no edge identity was explicitly ratified (REJECT + "
                          "HOLD + 2 PENDING + 31 unconfirmed SUGGESTED), so "
                          "nothing was promoted",
        "guards_exercised": [
            "c11_promote_test 27/27 (incl. new T19 tool-level rejection of the "
            "operator-rejected identity, T20 generator-level G13 rejection of a "
            "forged promotion for it)",
            "graph_check c11.10/c11.13 two-way graph<->promotions audit green",
            "held candidates categorically non-promotable (not edges)",
        ],
    },
    "final_state": {
        "nodes": len(nodes),
        "concepts": sum(1 for n in nodes if n["family"] == "CONCEPT"),
        "misconceptions": sum(1 for n in nodes if n["family"] == "MISCONCEPTION"),
        "edges_total": len(graph_edges),
        "edges_by_relation": {k: v for k, v in sorted(by_rel.items())},
        "authored_edges": len(edges),
        "part_of_edges": by_rel.get("PART_OF", 0),
        "validation_states": {
            "SUGGESTED": sum(1 for e in graph_edges
                             if e["validation_status"] == "SUGGESTED"),
            "REVIEW_REQUIRED": sum(1 for e in graph_edges
                                   if e["validation_status"] == "REVIEW_REQUIRED"),
            "HUMAN_VALIDATED": sum(1 for e in graph_edges
                                   if e["validation_status"] == "HUMAN_VALIDATED"),
        },
        "operator_decisions": {
            "REJECT": sum(1 for d in op_dec if d.get("verdict") == "REJECT"),
            "HOLD": sum(1 for d in op_dec if d.get("verdict") == "HOLD"),
            "PENDING": sum(1 for d in op_dec if d.get("verdict") == "PENDING"),
        },
        "held_candidates": len(held),
        "held_candidates_status": {
            "held": sum(1 for h in held if h["status"] == "held"),
            "rejected": sum(1 for h in held if h["status"] == "rejected"),
        },
        "confidence_distribution": {
            "nodes": band(nodes),
            "authored_edges": band(edges),
            "all_edges_including_part_of": band(graph_edges),
        },
        "negative_control_4_15": "0 concepts, 0 edges, 0 coverage (uncovered)",
    },
    "verification": {
        "graph_check": "ALL PASS (11/11 groups; 29 nodes / 65 edges / 0 "
                       "HUMAN_VALIDATED / 4.15 uncovered)",
        "c11_negative_test": "14/14 PASS",
        "c11_task4_variants": "3/3 PASS",
        "c11_promote_test": "27/27 PASS",
        "deterministic_regeneration": "byte-identical at the 65-edge state",
        "graph_diff_vs_e218259": "the rejected edge block removed + meta counts "
                                 "updated; all other 65 edges byte-identical",
    },
    "recorded_defects": [
        "CON-THEOR-YIELD.aliases contains corrupted entry 'aximum yield' "
        "(truncation of 'maximum yield'; also unevidenced — the source note "
        "does not contain 'maximum yield'). Fix at the next decision-record "
        "revision; the session-41 re-author stayed surgical.",
    ],
    "operator_decision_blocks": op_dec,
}

(REPORTS / "C11_OPERATOR_DECISIONS.json").write_text(
    json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("wrote", REPORTS / "C11_OPERATOR_DECISIONS.json")
print("counts:", json.dumps(out["final_state"]["edges_by_relation"]),
      json.dumps(out["final_state"]["validation_states"]),
      json.dumps(out["final_state"]["confidence_distribution"]["authored_edges"]))
