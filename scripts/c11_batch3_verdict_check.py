#!/usr/bin/env python3
"""T-C11 session 52 — c11_batch3_verdict_check.py: standing checker for the
batch-3 operator verdict record (scripts/c11_batch3_verdicts.yaml) and its
application state.

Checks (all fail-closed; every group must pass):
  A. schema          — sections, row ids in order, vocabulary, the verbatim
                       operator verdict policy (session-52 practical-review
                       directive) + decided_by/date; NO rr_settlement
                       section (batch 3 authored zero RR edges)
  B. verdict shape   — 39 edge CONFIRM / 24 node CONFIRM / 7 KEEP_AS_IS /
                       held appendix (14) acknowledged; reconciliation
                       against the batch-3 decision record (triples, node
                       codes, NO operator_decision blocks — the §7
                       application is the header note only: no RR
                       settlement, no ENRICHMENT node, no MERGE/SPLIT)
  C. application     — three-way set equality: verdict CONFIRM set ==
                       live batch-3 HUMAN_VALIDATED set == batch-3 entries
                       in the promotion store (39 each, operator
                       attribution, the B3 diff-review bundle as
                       review_reference); nothing outside the CONFIRM set
                       was promoted
  D. invariants      — the pilot, batch-1 and batch-2 slices are intact
                       (28+28+23 HUMAN_VALIDATED; 3 pilot operator-HOLD
                       SUGGESTED; both RR edges REVIEW_REQUIRED); store
                       total 118; 4.15 negative control uncovered; no
                       PART_OF promoted; no batch-3 node HUMAN_VALIDATED;
                       live store shape 91/220/97/123

Usage: python3 scripts/c11_batch3_verdict_check.py
"""
from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
GRAPH = REPO / "graph"
VERDICTS = HERE / "c11_batch3_verdicts.yaml"
DECISIONS = HERE / "c11_batch3_decisions.yaml"
B1_VERDICTS = HERE / "c11_batch1_verdicts.yaml"
B1_DECISIONS = HERE / "c11_batch1_decisions.yaml"
B2_VERDICTS = HERE / "c11_batch2_verdicts.yaml"
B2_DECISIONS = HERE / "c11_batch2_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"

BUNDLE_REF = "graph/reports/C11_DIFF_REVIEW_B3_2026-09-13.md"
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
b2_vd = yaml.safe_load(B2_VERDICTS.read_text(encoding="utf-8"))
b2_dec = yaml.safe_load(B2_DECISIONS.read_text(encoding="utf-8"))
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
check("A2 operator verdict policy recorded verbatim (session 52)",
      "evidence clearly supports the authored relationship: CONFIRM" in
      (r.get("statement") or "")
      and "not turn ordinary ontology imperfection" in (r.get("statement") or "")
      and r.get("session") == 52
      and r.get("decided_by") == "operator"
      and r.get("decided_date") == "2026-09-13")
check("A3 edge rows B3-E-01..B3-E-39 sequential, complete",
      [x["id"] for x in ev] == [f"B3-E-{i:02d}" for i in range(1, 40)])
check("A4 node rows B3-N-01..20 + B3-M-01..04 sequential, complete",
      [x["id"] for x in nv] == [f"B3-N-{i:02d}" for i in range(1, 21)]
      + [f"B3-M-{i:02d}" for i in range(1, 5)])
check("A5 identity rows B3-ID-01..07 sequential, complete",
      [x["id"] for x in ids] == [f"B3-ID-{i:02d}" for i in range(1, 8)])
V_EDGE = {"CONFIRM", "REJECT", "HOLD", "MERGE", "SPLIT"}
V_ID = {"MERGE", "SPLIT", "KEEP_AS_IS"}
check("A6 all verdicts in vocabulary, none empty",
      all(x["verdict"] in V_EDGE for x in ev)
      and all(x["verdict"] in V_EDGE for x in nv)
      and all(x["verdict"] in V_ID for x in ids))
check("A7 template consumed (fill + rename per the gate pathway)",
      not (HERE / "c11_batch3_verdicts_template.yaml").exists()
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
check("B1 edge verdicts: 39 CONFIRM / 0 others",
      ec == {"CONFIRM": 39}, f"{ec}")
check("B2 node verdicts: 24 CONFIRM / 0 others",
      nc == {"CONFIRM": 24}, f"{nc}")
check("B3 identity decisions: 7 x KEEP_AS_IS",
      [x["verdict"] for x in ids] == ["KEEP_AS_IS"] * 7)
check("B4 batch 3 authored ZERO RR edges (no settlement row needed)",
      not any(e["validation_status"] == "REVIEW_REQUIRED"
              for e in dec["edges"]))
check("B5 held appendix acknowledged (14 preserved, no reopening)",
      held_ack.get("acknowledged") is True
      and len(dec["held"]) == 14
      and all(h["status"] == "held" for h in dec["held"]))

b_suggested = {triple(e) for e in dec["edges"]
               if e["validation_status"] == "SUGGESTED"}
check("B6 verdict triples = the batch-3 decision record's 39 SUGGESTED edges",
      {x["triple"] for x in ev} == b_suggested and len(b_suggested) == 39)
check("B7 verdict node codes = the batch-3 record's 24 node codes",
      {x["code"] for x in nv} == {c["code"] for c in dec["nodes"]}
      and len(dec["nodes"]) == 24)
check("B8 NO operator_decision blocks in the batch-3 record (none "
      "sanctioned: no RR, no ENRICHMENT node, all identity KEEP_AS_IS)",
      sum(1 for x in dec["nodes"] + dec["edges"]
          if "operator_decision" in x) == 0)
check("B9 the session-52 §7 header note is present (review state only)",
      "OPERATOR DECISIONS (session 52" in DECISIONS.read_text(
          encoding="utf-8"))
check("B10 no ENRICHMENT-scoped node in batch 3 (none to scope)",
      not any(sp.get("role") == "ENRICHMENT"
              for x in dec["nodes"] for sp in x.get("spec_points", [])))

# ---------------------------------------------------------------------------
# C. application (three-way set equality; session-52 §18 application)
# ---------------------------------------------------------------------------
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
b_triples = {triple(e) for e in dec["edges"]}
b_hv = {t for t in hv if t in b_triples}
confirms = {x["triple"] for x in ev if x["verdict"] == "CONFIRM"}
store_map = {" ".join((p["edge"]["source"], p["edge"]["relation"],
                       p["edge"]["target"])): p
             for p in promo["promotions"]}
check("C1 live batch-3 HUMAN_VALIDATED set = the 39 CONFIRM verdicts",
      b_hv == confirms and len(b_hv) == 39,
      f"live = {len(b_hv)}, verdicts = {len(confirms)}")
check("C2 promotion store = exactly the 39 batch-3 CONFIRM entries",
      set(store_map) & b_triples == confirms)
b_store = {k: p for k, p in store_map.items() if k in b_triples}
check("C3 batch-3 store entries carry operator attribution + 2026-09-13",
      all(p.get("validated_by") == "operator"
          and p.get("validated_date") == "2026-09-13"
          for p in b_store.values()), f"entries = {len(b_store)}")
check("C4 batch-3 store entries reference the B3 diff-review bundle",
      all(p.get("review_reference") == BUNDLE_REF
          for p in b_store.values()))
check("C5 no REJECT/HOLD/MERGE/SPLIT verdicts left un-applied",
      all(x["verdict"] == "CONFIRM" for x in ev))

# ---------------------------------------------------------------------------
# D. invariants (pilot + batch-1 + batch-2 slices, store total, negative
#    control)
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
# batch-2 slice
b2_triples = {triple(e) for e in b2_dec["edges"]}
b2_hv = {t for t in hv if t in b2_triples}
b2_confirms = {x["triple"] for x in b2_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D6 batch-2 slice intact: 23 batch-2 CONFIRM still HUMAN_VALIDATED",
      b2_hv == b2_confirms and len(b2_hv) == 23)
check("D7 store total 118 (28+28+23+39), all operator",
      len(store_map) == 118
      and all(p.get("validated_by") == "operator"
              for p in store_map.values()))
n415 = [x for x in nodes_doc["nodes"]
        if any(sp.get("code") == "4CH1-4.15"
               for sp in x.get("spec_points", []))]
e415 = [e for e in edges_doc["edges"]
        if any("4.15" in a.get("file", "") for a in e.get("evidence", []))]
check("D8 negative control 4CH1-4.15: zero node/edge attachments",
      len(n415) == 0 and len(e415) == 0,
      f"nodes = {len(n415)}, edges = {len(e415)}")
check("D9 no PART_OF edge promoted (node pathway not built)",
      not any(e["relation"] == "PART_OF"
              and e["validation_status"] == "HUMAN_VALIDATED"
              for e in edges_doc["edges"]))
check("D10 no batch-3 node is HUMAN_VALIDATED (nodes have no §18 pathway)",
      not any(x.get("validation_status") == "HUMAN_VALIDATED"
              for x in nodes_doc["nodes"]))
check("D11 live store shape 91 nodes / 220 edges (97 PART_OF + 123 "
      "semantic)",
      len(nodes_doc["nodes"]) == 91 and len(edges_doc["edges"]) == 220
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF") == 97)

# ---------------------------------------------------------------------------
print()
if fails:
    print(f"FAILED: {len(fails)} check(s): {fails}")
    raise SystemExit(1)
print(f"c11_batch3_verdict_check: ALL PASS — batch-3 operator verdict layer "
      f"(39+24+7 rows, the session-52 practical-review policy; zero RR "
      f"authored) schema-valid, record-reconciled, application-reconciled "
      f"(39 §18 promotions = the CONFIRM set; §7 header note only — no "
      f"operator_decision blocks; pilot + batch-1 + batch-2 slices intact; "
      f"118 store entries total).")
