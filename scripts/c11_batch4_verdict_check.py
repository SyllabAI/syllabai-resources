#!/usr/bin/env python3
"""T-C11 session 54 — c11_batch4_verdict_check.py: standing checker for the
batch-4 operator verdict record (scripts/c11_batch4_verdicts.yaml) and its
application state.

Checks (all fail-closed; every group must pass):
  A. schema          — sections, row ids in order, vocabulary, the verbatim
                       operator verdict policy (session-54 practical
                       verdict policy) + decided_by/date; NO rr_settlement
                       section (batch 4 authored zero RR edges)
  B. verdict shape   — 35 edge CONFIRM / 22 node CONFIRM (17 CONCEPT +
                       5 MISCONCEPTION) / 6 KEEP_AS_IS / held appendix
                       (14) acknowledged; reconciliation against the
                       batch-4 decision record (triples, node codes, NO
                       operator_decision blocks — identity decisions are
                       all KEEP_AS_IS, so no §7 re-authoring was
                       sanctioned)
  C. application     — three-way set equality: verdict CONFIRM set ==
                       live batch-4 HUMAN_VALIDATED set == batch-4 entries
                       in the promotion store (35 each, operator
                       attribution, the B4 diff-review bundle as
                       review_reference); nothing outside the CONFIRM set
                       was promoted
  D. invariants      — the pilot, batch-1, batch-2 and batch-3 slices are
                       intact (28+28+23+39 HUMAN_VALIDATED; 3 pilot
                       operator-HOLD SUGGESTED; both RR edges
                       REVIEW_REQUIRED); store total 153; the 14 batch-4
                       held candidates quarantined (never authored); the 5
                       ruled S1 owner codes NOT re-minted in the batch-4
                       node set; 4.15 negative control uncovered; no
                       PART_OF promoted; no batch-4 node HUMAN_VALIDATED;
                       live store shape 113/275/117/158

Usage: python3 scripts/c11_batch4_verdict_check.py
"""
from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
GRAPH = REPO / "graph"
VERDICTS = HERE / "c11_batch4_verdicts.yaml"
DECISIONS = HERE / "c11_batch4_decisions.yaml"
B1_VERDICTS = HERE / "c11_batch1_verdicts.yaml"
B1_DECISIONS = HERE / "c11_batch1_decisions.yaml"
B2_VERDICTS = HERE / "c11_batch2_verdicts.yaml"
B2_DECISIONS = HERE / "c11_batch2_decisions.yaml"
B3_VERDICTS = HERE / "c11_batch3_verdicts.yaml"
B3_DECISIONS = HERE / "c11_batch3_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"

BUNDLE_REF = "graph/reports/C11_DIFF_REVIEW_B4_2026-09-13.md"
B1_RR_TRIPLE = ("4CH1-CON-CRYSTALLISATION REQUIRES_PREREQUISITE "
                "4CH1-CON-SOLUTION")
PILOT_RR_TRIPLE = ("4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE "
                   "4CH1-CON-AVOGADRO-LAW")
# the session-52 cross-slice boundary ruling's five sanctioned S1 owners
RULED_S1_OWNERS = {
    "4CH1-CON-MOLE", "4CH1-CON-COVALENT-BOND", "4CH1-CON-CONCENTRATION",
    "4CH1-CON-EQ-SYMBOL", "4CH1-CON-WATER-CRYST",
}

fails: list[str] = []
n = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global n
    n += 1
    if ok:
        print(f"PASS  {name}" + (f"  {detail}" if detail else ""))
    else:
        print(f"FAIL  {name}" + (f"  {detail}" if detail else ""))
        fails.append(name)


def triple(e) -> str:
    return f"{e['source']} {e['relation']} {e['target']}"


vd = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
dec = yaml.safe_load(DECISIONS.read_text(encoding="utf-8"))
b1_vd = yaml.safe_load(B1_VERDICTS.read_text(encoding="utf-8"))
b1_dec = yaml.safe_load(B1_DECISIONS.read_text(encoding="utf-8"))
b2_vd = yaml.safe_load(B2_VERDICTS.read_text(encoding="utf-8"))
b2_dec = yaml.safe_load(B2_DECISIONS.read_text(encoding="utf-8"))
b3_vd = yaml.safe_load(B3_VERDICTS.read_text(encoding="utf-8"))
b3_dec = yaml.safe_load(B3_DECISIONS.read_text(encoding="utf-8"))
edges_doc = yaml.safe_load((GRAPH / "concept_edges.yaml")
                           .read_text(encoding="utf-8"))
nodes_doc = yaml.safe_load((GRAPH / "concepts.yaml")
                           .read_text(encoding="utf-8"))
promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))

ev, nv = vd["edge_verdicts"], vd["node_verdicts"]
ids = vd["identity_decisions"]
held_ack = vd["held_appendix_acknowledgment"]

# ---------------------------------------------------------------------------
# A. schema
# ---------------------------------------------------------------------------
check("A1 file parses with required sections (no rr_settlement)",
      all(k in vd for k in ("meta", "edge_verdicts", "node_verdicts",
                            "identity_decisions",
                            "held_appendix_acknowledgment"))
      and "rr_settlement" not in vd)
r = vd["meta"].get("operator_ruling") or {}
check("A2 operator verdict policy recorded verbatim (session 54)",
      "substantively supports the relationship/node" in
      (r.get("statement") or "")
      and "Do not turn normal ontology ambiguity into a blocking issue" in
      (r.get("statement") or "")
      and r.get("session") == 54
      and r.get("decided_by") == "operator"
      and r.get("decided_date") == "2026-09-13")
check("A3 edge rows B4-E-01..B4-E-35 sequential, complete",
      [x["id"] for x in ev] == [f"B4-E-{i:02d}" for i in range(1, 36)])
check("A4 node rows B4-N-01..17 + B4-M-01..05 sequential, complete",
      [x["id"] for x in nv] == [f"B4-N-{i:02d}" for i in range(1, 18)]
      + [f"B4-M-{i:02d}" for i in range(1, 6)])
check("A5 identity rows B4-ID-01..06 sequential, complete",
      [x["id"] for x in ids] == [f"B4-ID-{i:02d}" for i in range(1, 7)])
V_EDGE = {"CONFIRM", "REJECT", "HOLD", "MERGE", "SPLIT"}
V_ID = {"MERGE", "SPLIT", "KEEP_AS_IS"}
check("A6 all verdicts in vocabulary, none empty",
      all(x["verdict"] in V_EDGE for x in ev)
      and all(x["verdict"] in V_EDGE for x in nv)
      and all(x["verdict"] in V_ID for x in ids))
check("A7 template consumed (fill + rename per the gate pathway)",
      not (HERE / "c11_batch4_verdicts_template.yaml").exists()
      and VERDICTS.exists())

# ---------------------------------------------------------------------------
# B. verdict shape + decision-record reconciliation
# ---------------------------------------------------------------------------
ec = {}
for x in ev:
    ec[x["verdict"]] = ec.get(x["verdict"], 0) + 1
nc = {}
for x in nv:
    nc[x["verdict"]] = nc.get(x["verdict"], 0) + 1
check("B1 edge verdicts: 35 CONFIRM / 0 others",
      ec == {"CONFIRM": 35}, f"{ec}")
check("B2 node verdicts: 22 CONFIRM / 0 others",
      nc == {"CONFIRM": 22}, f"{nc}")
check("B3 identity decisions: 6 x KEEP_AS_IS",
      [x["verdict"] for x in ids] == ["KEEP_AS_IS"] * 6)
check("B4 batch 4 authored ZERO RR edges (no settlement row needed)",
      not any(e["validation_status"] == "REVIEW_REQUIRED"
              for e in dec["edges"]))
check("B5 held appendix acknowledged (14 preserved, quarantined)",
      held_ack.get("acknowledged") is True
      and len(dec["held"]) == 14
      and all(h["status"] == "held" for h in dec["held"]))

b_suggested = {triple(e) for e in dec["edges"]
               if e["validation_status"] == "SUGGESTED"}
check("B6 verdict triples = the batch-4 record's 35 SUGGESTED edges",
      {x["triple"] for x in ev} == b_suggested and len(b_suggested) == 35)
check("B7 verdict node codes = the batch-4 record's 22 node codes "
      "(17 CONCEPT + 5 MISCONCEPTION)",
      {x["code"] for x in nv} == {c["code"] for c in dec["nodes"]}
      and len(dec["nodes"]) == 22
      and sum(1 for c in dec["nodes"] if c["family"] == "CONCEPT") == 17
      and sum(1 for c in dec["nodes"]
              if c["family"] == "MISCONCEPTION") == 5)
check("B8 NO operator_decision blocks in the batch-4 record (none "
      "sanctioned: no RR, no ENRICHMENT node, all identity KEEP_AS_IS)",
      sum(1 for x in dec["nodes"] + dec["edges"]
          if "operator_decision" in x) == 0)
check("B9 no ENRICHMENT-scoped node in batch 4 (none to scope)",
      not any(sp.get("role") == "ENRICHMENT"
              for x in dec["nodes"] for sp in x.get("spec_points", [])))

# ---------------------------------------------------------------------------
# C. application (three-way set equality; session-54 §18 application)
# ---------------------------------------------------------------------------
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
b_triples = {triple(e) for e in dec["edges"]}
b_hv = {t for t in hv if t in b_triples}
confirms = {x["triple"] for x in ev if x["verdict"] == "CONFIRM"}
store_map = {" ".join((p["edge"]["source"], p["edge"]["relation"],
                       p["edge"]["target"])): p
             for p in promo["promotions"]}
check("C1 live batch-4 HUMAN_VALIDATED set = the 35 CONFIRM verdicts",
      b_hv == confirms and len(b_hv) == 35,
      f"live = {len(b_hv)}, verdicts = {len(confirms)}")
check("C2 promotion store = exactly the 35 batch-4 CONFIRM entries",
      set(store_map) & b_triples == confirms)
b_store = {k: p for k, p in store_map.items() if k in b_triples}
check("C3 batch-4 store entries carry operator attribution + 2026-09-13",
      all(p.get("validated_by") == "operator"
          and p.get("validated_date") == "2026-09-13"
          for p in b_store.values()), f"entries = {len(b_store)}")
check("C4 batch-4 store entries reference the B4 diff-review bundle",
      all(p.get("review_reference") == BUNDLE_REF
          for p in b_store.values()))
check("C5 no REJECT/HOLD/MERGE/SPLIT verdicts left un-applied",
      all(x["verdict"] == "CONFIRM" for x in ev))
check("C6 the five sanctioned cross-section boundary edges are "
      "HUMAN_VALIDATED (session-52 ruling applied, not re-minted)",
      all(any(triple(e) == t and e["validation_status"] == "HUMAN_VALIDATED"
              for e in sem)
          for t in ("4CH1-CON-MOLAR-ENTHALPY REQUIRES_PREREQUISITE "
                    "4CH1-CON-MOLE",
                    "4CH1-CON-BOND-ENERGY-CALC REQUIRES_PREREQUISITE "
                    "4CH1-CON-COVALENT-BOND",
                    "4CH1-CON-RATE-FACTORS REQUIRES_PREREQUISITE "
                    "4CH1-CON-CONCENTRATION",
                    "4CH1-CON-REVERSIBLE REQUIRES_PREREQUISITE "
                    "4CH1-CON-EQ-SYMBOL",
                    "4CH1-CON-REVERSIBLE-EXAMPLES REQUIRES_PREREQUISITE "
                    "4CH1-CON-WATER-CRYST")))

# ---------------------------------------------------------------------------
# D. invariants (pilot + batch-1 + batch-2 + batch-3 slices, store total,
#    negative control, boundary mint discipline)
# ---------------------------------------------------------------------------
# pilot slice
pilot_dec = yaml.safe_load((HERE / "c11_pilot_decisions.yaml")
                           .read_text(encoding="utf-8"))
pilot_vd = yaml.safe_load((HERE / "c11_review_verdicts.yaml")
                          .read_text(encoding="utf-8"))
pilot_triples = {triple(e) for e in pilot_dec["edges"]}
pilot_hv = {t for t in hv if t in pilot_triples}
pilot_confirms = {x["triple"] for x in pilot_vd["edge_verdicts"]
                  if x["verdict"] == "CONFIRM"}
pilot_holds = {x["triple"] for x in pilot_vd["edge_verdicts"]
               if x["verdict"] == "HOLD"}
live_sugg = {triple(e) for e in sem
             if e["validation_status"] == "SUGGESTED"}
check("D1 pilot slice intact: 28 pilot CONFIRM still HUMAN_VALIDATED",
      pilot_hv == pilot_confirms and len(pilot_hv) == 28)
check("D2 the 3 pilot operator HOLDs stay SUGGESTED (un-promoted); they "
      "are the ONLY live SUGGESTED semantic edges (batch-4 promoted)",
      pilot_holds <= live_sugg and not (pilot_holds & hv)
      and live_sugg == pilot_holds, f"live SUGGESTED = {len(live_sugg)}")
pilot_rr = [e for e in sem if triple(e) == PILOT_RR_TRIPLE]
check("D3 the pilot RR edge stays REVIEW_REQUIRED (operator HOLD)",
      len(pilot_rr) == 1
      and pilot_rr[0]["validation_status"] == "REVIEW_REQUIRED")
# batch-1 slice
b1_triples = {triple(e) for e in b1_dec["edges"]}
b1_hv = {t for t in hv if t in b1_triples}
b1_confirms = {x["triple"] for x in b1_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D4 batch-1 slice intact: 28 batch-1 CONFIRM still HUMAN_VALIDATED",
      b1_hv == b1_confirms and len(b1_hv) == 28)
b1_rr = [e for e in sem if triple(e) == B1_RR_TRIPLE]
check("D5 the batch-1 RR settlement stays REVIEW_REQUIRED (HOLD_REVIEW_REQ)",
      len(b1_rr) == 1
      and b1_rr[0]["validation_status"] == "REVIEW_REQUIRED")
# batch-2 slice
b2_triples = {triple(e) for e in b2_dec["edges"]}
b2_hv = {t for t in hv if t in b2_triples}
b2_confirms = {x["triple"] for x in b2_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D6 batch-2 slice intact: 23 batch-2 CONFIRM still HUMAN_VALIDATED",
      b2_hv == b2_confirms and len(b2_hv) == 23)
# batch-3 slice
b3_triples = {triple(e) for e in b3_dec["edges"]}
b3_hv = {t for t in hv if t in b3_triples}
b3_confirms = {x["triple"] for x in b3_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D7 batch-3 slice intact: 39 batch-3 CONFIRM still HUMAN_VALIDATED",
      b3_hv == b3_confirms and len(b3_hv) == 39)
check("D8 store total 153 (28+28+23+39+35), all operator",
      len(store_map) == 153
      and all(p.get("validated_by") == "operator"
              for p in store_map.values()))
n415 = [x for x in nodes_doc["nodes"]
        if any(sp.get("code") == "4CH1-4.15"
               for sp in x.get("spec_points", []))]
e415 = [e for e in edges_doc["edges"]
        if any("4.15" in a.get("file", "") for a in e.get("evidence", []))]
check("D9 negative control 4CH1-4.15: zero node/edge attachments",
      len(n415) == 0 and len(e415) == 0,
      f"nodes = {len(n415)}, edges = {len(e415)}")
check("D10 no PART_OF edge promoted (node pathway not built)",
      not any(e["relation"] == "PART_OF"
              and e["validation_status"] == "HUMAN_VALIDATED"
              for e in edges_doc["edges"]))
check("D11 no batch-4 node is HUMAN_VALIDATED (nodes have no §18 pathway)",
      not any(x.get("validation_status") == "HUMAN_VALIDATED"
              for x in nodes_doc["nodes"]))
check("D12 live store shape 113 nodes / 275 edges (117 PART_OF + 158 "
      "semantic)",
      len(nodes_doc["nodes"]) == 113 and len(edges_doc["edges"]) == 275
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF") == 117)
# boundary mint discipline (the session-52 cross-slice ruling)
b4_codes = {c["code"] for c in dec["nodes"]}
check("D13 zero ruled S1 owner re-minted in the batch-4 node set "
      "(CON-MOLE / CON-COVALENT-BOND / CON-CONCENTRATION / CON-EQ-SYMBOL "
      "/ CON-WATER-CRYST absent from the mint)",
      not (b4_codes & RULED_S1_OWNERS), f"collision = "
      f"{sorted(b4_codes & RULED_S1_OWNERS)}")
# the 14 held candidates were never authored -> absent from the live store
held_ids = [h["id"] for h in dec["held"]]
check("D14 the 14 batch-4 held candidates stay quarantined (recorded, "
      "never authored; store untouched by holds)",
      len(held_ids) == 14
      and not any(triple(e) in b_suggested for e in dec["edges"]
                  if e["validation_status"] == "REVIEW_REQUIRED"))

# ---------------------------------------------------------------------------
print()
if fails:
    print(f"FAILED: {len(fails)} check(s): {fails}")
    raise SystemExit(1)
print(f"c11_batch4_verdict_check: ALL PASS — batch-4 operator verdict layer "
      f"(35+22+6 rows, the session-54 practical verdict policy; zero RR "
      f"authored; FP-B4-1 + FP-B4-2 special attention recorded in "
      f"meta.operator_ruling) schema-valid, record-reconciled, "
      f"application-reconciled (35 §18 promotions = the CONFIRM set; no "
      f"operator_decision blocks; pilot + batch-1 + batch-2 + batch-3 "
      f"slices intact; 153 store entries total; the 5 boundary targets "
      f"reused, zero re-mint).")
