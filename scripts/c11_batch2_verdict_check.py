#!/usr/bin/env python3
"""T-C11 session 50 — c11_batch2_verdict_check.py: standing checker for the
batch-2 operator verdict record (scripts/c11_batch2_verdicts.yaml) and its
application state.

Checks (all fail-closed; every group must pass):
  A. schema          — sections, row ids in order, vocabulary, the verbatim
                       operator ruling ("CONFIRM all") + decided_by/date;
                       NO rr_settlement section (batch 2 authored zero RR
                       edges)
  B. verdict shape   — 23 edge CONFIRM / 14 node CONFIRM / 4 KEEP_AS_IS /
                       held appendix (10) acknowledged; reconciliation
                       against the batch-2 decision record (triples, node
                       codes, the B2-N-08 enrichment operator_decision
                       block)
  C. application     — three-way set equality: verdict CONFIRM set ==
                       live batch-2 HUMAN_VALIDATED set == batch-2 entries
                       in the promotion store (23 each, operator
                       attribution, the B2 diff-review bundle as
                       review_reference); nothing outside the CONFIRM set
                       was promoted
  D. invariants      — the pilot and batch-1 slices are intact (28+28
                       HUMAN_VALIDATED; 3 pilot operator-HOLD SUGGESTED;
                       both RR edges REVIEW_REQUIRED); store total 79;
                       4.15 negative control uncovered; no PART_OF
                       promoted; no batch-2 node HUMAN_VALIDATED

Usage: python3 scripts/c11_batch2_verdict_check.py
"""
from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
GRAPH = REPO / "graph"
VERDICTS = HERE / "c11_batch2_verdicts.yaml"
DECISIONS = HERE / "c11_batch2_decisions.yaml"
B1_VERDICTS = HERE / "c11_batch1_verdicts.yaml"
B1_DECISIONS = HERE / "c11_batch1_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"

BUNDLE_REF = "graph/reports/C11_DIFF_REVIEW_B2_2026-09-12.md"
B1_RR_TRIPLE = ("4CH1-CON-CRYSTALLISATION REQUIRES_PREREQUISITE "
                "4CH1-CON-SOLUTION")
PILOT_RR_TRIPLE = ("4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE "
                   "4CH1-CON-AVOGADRO-LAW")

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
check("A2 verbatim operator ruling recorded (CONFIRM all, session 50)",
      r.get("statement") == "CONFIRM all" and r.get("session") == 50
      and r.get("decided_by") == "operator"
      and r.get("decided_date") == "2026-09-12")
check("A3 edge rows B2-E-01..B2-E-23 sequential, complete",
      [x["id"] for x in ev] == [f"B2-E-{i:02d}" for i in range(1, 24)])
check("A4 node rows B2-N-01..12 + B2-M-01/02 sequential, complete",
      [x["id"] for x in nv] == [f"B2-N-{i:02d}" for i in range(1, 13)]
      + ["B2-M-01", "B2-M-02"])
check("A5 identity rows B2-ID-01..04 sequential, complete",
      [x["id"] for x in ids] == [f"B2-ID-{i:02d}" for i in range(1, 5)])
V_EDGE = {"CONFIRM", "REJECT", "HOLD", "MERGE", "SPLIT"}
V_ID = {"MERGE", "SPLIT", "KEEP_AS_IS"}
check("A6 all verdicts in vocabulary, none empty",
      all(x["verdict"] in V_EDGE for x in ev)
      and all(x["verdict"] in V_EDGE for x in nv)
      and all(x["verdict"] in V_ID for x in ids))

# ---------------------------------------------------------------------------
# B. verdict shape + decision-record reconciliation
# ---------------------------------------------------------------------------
ec = {}
for x in ev:
    ec[x["verdict"]] = ec.get(x["verdict"], 0) + 1
nc = {}
for x in nv:
    nc[x["verdict"]] = nc.get(x["verdict"], 0) + 1
check("B1 edge verdicts: 23 CONFIRM / 0 others",
      ec == {"CONFIRM": 23}, f"{ec}")
check("B2 node verdicts: 14 CONFIRM / 0 others",
      nc == {"CONFIRM": 14}, f"{nc}")
check("B3 identity decisions: 4 x KEEP_AS_IS",
      [x["verdict"] for x in ids] == ["KEEP_AS_IS"] * 4)
check("B4 batch 2 authored ZERO RR edges (no settlement row needed)",
      not any(e["validation_status"] == "REVIEW_REQUIRED"
              for e in dec["edges"]))
check("B5 held appendix acknowledged (10 preserved, no reopening)",
      held_ack.get("acknowledged") is True
      and len(dec["held"]) == 10
      and all(h["status"] == "held" for h in dec["held"]))

b_suggested = {triple(e) for e in dec["edges"]
               if e["validation_status"] == "SUGGESTED"}
check("B6 verdict triples = the batch-2 decision record's 23 SUGGESTED edges",
      {x["triple"] for x in ev} == b_suggested and len(b_suggested) == 23)
check("B7 verdict node codes = the batch-2 record's 14 node codes",
      {x["code"] for x in nv} == {c["code"] for c in dec["nodes"]}
      and len(dec["nodes"]) == 14)

n08 = next(x for x in dec["nodes"] if x["code"] == "4CH1-CON-METALLOID")
od_n08 = n08.get("operator_decision") or {}
check("B8 enrichment od block on B2-N-08 (CONFIRM, operator, 2026-09-12)",
      od_n08.get("verdict") == "CONFIRM"
      and od_n08.get("decided_by") == "operator"
      and od_n08.get("decided_date") == "2026-09-12"
      and n08["spec_points"][0]["role"] == "ENRICHMENT"
      and n08["spec_points"][0]["code"] == "4CH1-1.21")
check("B9 enrichment scoping preserved (no syllabus-authority conversion)",
      "ENRICHMENT" in od_n08.get("note", "")
      and "operator" == od_n08.get("decided_by"))
check("B10 exactly one operator_decision block in the batch-2 record",
      sum(1 for x in dec["nodes"] + dec["edges"]
          if "operator_decision" in x) == 1)

# ---------------------------------------------------------------------------
# C. application (three-way set equality; session-50 §18 application)
# ---------------------------------------------------------------------------
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
b_triples = {triple(e) for e in dec["edges"]}
b_hv = {t for t in hv if t in b_triples}
confirms = {x["triple"] for x in ev if x["verdict"] == "CONFIRM"}
store_map = {" ".join((p["edge"]["source"], p["edge"]["relation"],
                       p["edge"]["target"])): p
             for p in promo["promotions"]}
check("C1 live batch-2 HUMAN_VALIDATED set = the 23 CONFIRM verdicts",
      b_hv == confirms and len(b_hv) == 23,
      f"live = {len(b_hv)}, verdicts = {len(confirms)}")
check("C2 promotion store = exactly the 23 batch-2 CONFIRM entries",
      set(store_map) & b_triples == confirms)
b_store = {k: p for k, p in store_map.items() if k in b_triples}
check("C3 batch-2 store entries carry operator attribution + 2026-09-12",
      all(p.get("validated_by") == "operator"
          and p.get("validated_date") == "2026-09-12"
          for p in b_store.values()), f"entries = {len(b_store)}")
check("C4 batch-2 store entries reference the B2 diff-review bundle",
      all(p.get("review_reference") == BUNDLE_REF
          for p in b_store.values()))
check("C5 no REJECT/HOLD/MERGE/SPLIT verdicts left un-applied",
      all(x["verdict"] == "CONFIRM" for x in ev))

# ---------------------------------------------------------------------------
# D. invariants (pilot + batch-1 slices, store total, negative control)
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
check("D2 the 3 pilot operator HOLDs stay SUGGESTED (un-promoted)",
      pilot_holds <= live_sugg and not (pilot_holds & hv))
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
check("D6 store total 79 (28 pilot + 28 batch-1 + 23 batch-2), all operator",
      len(store_map) == 79
      and all(p.get("validated_by") == "operator"
              for p in store_map.values()))
n415 = [x for x in nodes_doc["nodes"]
        if any(sp.get("code") == "4CH1-4.15"
               for sp in x.get("spec_points", []))]
e415 = [e for e in edges_doc["edges"]
        if any("4.15" in a.get("file", "") for a in e.get("evidence", []))]
check("D7 negative control 4CH1-4.15: zero node/edge attachments",
      len(n415) == 0 and len(e415) == 0,
      f"nodes = {len(n415)}, edges = {len(e415)}")
check("D8 no PART_OF edge promoted (node pathway not built)",
      not any(e["relation"] == "PART_OF"
              and e["validation_status"] == "HUMAN_VALIDATED"
              for e in edges_doc["edges"]))
check("D9 no batch-2 node is HUMAN_VALIDATED (nodes have no §18 pathway)",
      not any(x.get("validation_status") == "HUMAN_VALIDATED"
              for x in nodes_doc["nodes"]))
# session-51 re-anchor (dated, protective intent unchanged): batch 3 grew
# the merged store to 91/220/97 (24 batch-3 nodes + 25 PART_OF + 39 authored
# semantic edges, all SUGGESTED awaiting the batch-3 operator gate); the
# batch-2 slice below is preserved exactly inside the grown store.
check("D10 live store shape 91 nodes / 220 edges (97 PART_OF + 123 semantic)",
      len(nodes_doc["nodes"]) == 91 and len(edges_doc["edges"]) == 220
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF") == 97)

# ---------------------------------------------------------------------------
print()
if fails:
    print(f"FAILED: {len(fails)} check(s): {fails}")
    raise SystemExit(1)
print(f"c11_batch2_verdict_check: ALL PASS — batch-2 operator verdict layer "
      f"(23+14+4 rows, ruling 'CONFIRM all' session 50; zero RR authored) "
      f"schema-valid, record-reconciled, application-reconciled (23 §18 "
      f"promotions = the CONFIRM set; B2-N-08 enrichment scoping recorded; "
      f"pilot + batch-1 slices intact; 79 store entries total).")
