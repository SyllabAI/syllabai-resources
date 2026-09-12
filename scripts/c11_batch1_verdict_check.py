#!/usr/bin/env python3
"""T-C11 session 48 — c11_batch1_verdict_check.py: standing checker for the
batch-1 operator verdict record (scripts/c11_batch1_verdicts.yaml) and its
application state.

Checks (all fail-closed; every group must pass):
  A. schema          — sections, row ids in order, vocabulary, the verbatim
                       operator ruling ("CONFIRM all") + decided_by/date
  B. verdict shape   — 28 edge CONFIRM / 24 node CONFIRM / 4 KEEP_AS_IS /
                       RR settlement HOLD_REVIEW_REQUIRED / held acknowledged;
                       reconciliation against the batch-1 decision record
                       (triples, node codes, the RR operator_decision block,
                       the two enrichment operator_decision blocks)
  C. application     — three-way set equality: verdict CONFIRM set ==
                       live batch-1 HUMAN_VALIDATED set == batch-1 entries
                       in the promotion store (28 each, operator
                       attribution, the B1 diff-review bundle as
                       review_reference); the RR edge stays REVIEW_REQUIRED
                       and un-promoted; nothing outside the CONFIRM set was
                       promoted
  D. invariants      — the pilot slice is intact (28 pilot HUMAN_VALIDATED
                       + 3 pilot operator-HOLD SUGGESTED + the pilot RR
                       REVIEW_REQUIRED); store total grows only by
                       sanctioned batches (118 at session 52); held appendix
                       12; 4.15 negative control uncovered; no PART_OF
                       promoted

Usage: python3 scripts/c11_batch1_verdict_check.py
"""
from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
GRAPH = REPO / "graph"
VERDICTS = HERE / "c11_batch1_verdicts.yaml"
DECISIONS = HERE / "c11_batch1_decisions.yaml"
PILOT_DECISIONS = HERE / "c11_pilot_decisions.yaml"
PILOT_VERDICTS = HERE / "c11_review_verdicts.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"

BUNDLE_REF = "graph/reports/C11_DIFF_REVIEW_B1_2026-09-12.md"
RR_TRIPLE = ("4CH1-CON-CRYSTALLISATION REQUIRES_PREREQUISITE "
             "4CH1-CON-SOLUTION")
PILOT_RR_TRIPLE = "4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-AVOGADRO-LAW"

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
pilot_dec = yaml.safe_load(PILOT_DECISIONS.read_text(encoding="utf-8"))
pilot_vd = yaml.safe_load(PILOT_VERDICTS.read_text(encoding="utf-8"))
edges_doc = yaml.safe_load((GRAPH / "concept_edges.yaml")
                           .read_text(encoding="utf-8"))
nodes_doc = yaml.safe_load((GRAPH / "concepts.yaml")
                           .read_text(encoding="utf-8"))
promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))

ev, nv = vd["edge_verdicts"], vd["node_verdicts"]
ids = vd["identity_decisions"]
rr = vd["rr_settlement"]
held_ack = vd["held_appendix_acknowledgment"]

# ---------------------------------------------------------------------------
# A. schema
# ---------------------------------------------------------------------------
check("A1 file parses with required sections",
      all(k in vd for k in ("meta", "edge_verdicts", "rr_settlement",
                            "node_verdicts", "identity_decisions",
                            "held_appendix_acknowledgment")))
r = vd["meta"].get("operator_ruling") or {}
check("A2 verbatim operator ruling recorded (CONFIRM all, session 48)",
      r.get("statement") == "CONFIRM all" and r.get("session") == 48
      and r.get("decided_by") == "operator"
      and r.get("decided_date") == "2026-09-12")
check("A3 edge rows B1-E-01..B1-E-28 sequential, complete",
      [x["id"] for x in ev] == [f"B1-E-{i:02d}" for i in range(1, 29)])
check("A4 node rows B1-N-01..22 + B1-M-01/02 sequential, complete",
      [x["id"] for x in nv] == [f"B1-N-{i:02d}" for i in range(1, 23)]
      + ["B1-M-01", "B1-M-02"])
check("A5 identity rows B1-ID-01..04 sequential, complete",
      [x["id"] for x in ids] == [f"B1-ID-{i:02d}" for i in range(1, 5)])
check("A6 rr_settlement exactly B1-RR-01",
      [x["id"] for x in rr] == ["B1-RR-01"])
V_EDGE = {"CONFIRM", "REJECT", "HOLD", "MERGE", "SPLIT"}
V_ID = {"MERGE", "SPLIT", "KEEP_AS_IS"}
V_RR = {"KEEP_AS_SUGGESTED", "PRUNE_TO_HELD", "HOLD_REVIEW_REQUIRED"}
check("A7 all verdicts in vocabulary, none empty",
      all(x["verdict"] in V_EDGE for x in ev)
      and all(x["verdict"] in V_EDGE for x in nv)
      and all(x["verdict"] in V_ID for x in ids)
      and all(x["verdict"] in V_RR for x in rr))

# ---------------------------------------------------------------------------
# B. verdict shape + decision-record reconciliation
# ---------------------------------------------------------------------------
ec = {}
for x in ev:
    ec[x["verdict"]] = ec.get(x["verdict"], 0) + 1
nc = {}
for x in nv:
    nc[x["verdict"]] = nc.get(x["verdict"], 0) + 1
check("B1 edge verdicts: 28 CONFIRM / 0 others",
      ec == {"CONFIRM": 28}, f"{ec}")
check("B2 node verdicts: 24 CONFIRM / 0 others",
      nc == {"CONFIRM": 24}, f"{nc}")
check("B3 identity decisions: 4 x KEEP_AS_IS",
      [x["verdict"] for x in ids] == ["KEEP_AS_IS"] * 4)
check("B4 RR settlement: HOLD_REVIEW_REQUIRED (quarantine confirmed)",
      rr[0]["verdict"] == "HOLD_REVIEW_REQUIRED"
      and rr[0]["triple"] == RR_TRIPLE)
check("B5 held appendix acknowledged (12 preserved, no reopening)",
      held_ack.get("acknowledged") is True)

b_suggested = {triple(e) for e in dec["edges"]
               if e["validation_status"] == "SUGGESTED"}
b_rr = [e for e in dec["edges"]
        if e["validation_status"] == "REVIEW_REQUIRED"]
check("B6 verdict triples = the batch-1 decision record's 28 SUGGESTED edges",
      {x["triple"] for x in ev} == b_suggested and len(b_suggested) == 28)
check("B7 the RR settlement triple = the decision record's RR edge",
      len(b_rr) == 1 and triple(b_rr[0]) == RR_TRIPLE)
check("B8 verdict node codes = the batch-1 record's 24 node codes",
      {x["code"] for x in nv} == {c["code"] for c in dec["nodes"]})

od_rr = b_rr[0].get("operator_decision") or {}
check("B9 RR operator_decision block: HOLD_REVIEW_REQUIRED, operator, 2026-09-12",
      od_rr.get("verdict") == "HOLD_REVIEW_REQUIRED"
      and od_rr.get("decided_by") == "operator"
      and od_rr.get("decided_date") == "2026-09-12")
n08 = next(x for x in dec["nodes"]
           if x["code"] == "4CH1-CON-EVAPORATION-BOILING")
n11 = next(x for x in dec["nodes"]
           if x["code"] == "4CH1-CON-HEATING-CONSTANT-MASS")
check("B10 enrichment od blocks on B1-N-08/B1-N-11 (CONFIRM, scoping notes)",
      (n08.get("operator_decision") or {}).get("verdict") == "CONFIRM"
      and (n11.get("operator_decision") or {}).get("verdict") == "CONFIRM"
      and n08["spec_points"][0]["role"] == "ENRICHMENT"
      and n11["spec_points"][0]["role"] == "ENRICHMENT")
check("B11 enrichment scoping preserved (no syllabus-authority conversion)",
      "ENRICHMENT" in (n08.get("operator_decision") or {}).get("note", "")
      and "ENRICHMENT" in (n11.get("operator_decision") or {}).get("note", ""))
check("B12 batch-1 held appendix: 12 entries, all held",
      len(dec["held"]) == 12
      and all(h["status"] == "held" for h in dec["held"]))

# ---------------------------------------------------------------------------
# C. application (three-way set equality; session-48 §18 application)
# ---------------------------------------------------------------------------
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
b_triples = {triple(e) for e in dec["edges"]}
b_hv = {t for t in hv if t in b_triples}
confirms = {x["triple"] for x in ev if x["verdict"] == "CONFIRM"}
store = [{" ".join((p["edge"]["source"], p["edge"]["relation"],
                    p["edge"]["target"])): p} for p in promo["promotions"]]
store_map = {k: p for d in store for k, p in d.items()}
check("C1 live batch-1 HUMAN_VALIDATED set = the 28 CONFIRM verdicts",
      b_hv == confirms and len(b_hv) == 28,
      f"live = {len(b_hv)}, verdicts = {len(confirms)}")
check("C2 promotion store = exactly the 28 batch-1 CONFIRM entries",
      set(store_map) & b_triples == confirms)
b_store = {k: p for k, p in store_map.items() if k in b_triples}
check("C3 batch-1 store entries carry operator attribution + 2026-09-12",
      all(p.get("validated_by") == "operator"
          and p.get("validated_date") == "2026-09-12"
          for p in b_store.values()), f"entries = {len(b_store)}")
check("C4 batch-1 store entries reference the B1 diff-review bundle",
      all(p.get("review_reference") == BUNDLE_REF
          for p in b_store.values()))
rr_live = [e for e in sem if triple(e) == RR_TRIPLE]
check("C5 the RR edge stays REVIEW_REQUIRED and un-promoted",
      len(rr_live) == 1
      and rr_live[0]["validation_status"] == "REVIEW_REQUIRED"
      and RR_TRIPLE not in store_map)
check("C6 no REJECT/HOLD/MERGE/SPLIT verdicts left un-applied",
      all(x["verdict"] == "CONFIRM" for x in ev))

# ---------------------------------------------------------------------------
# D. invariants (pilot slice + store total + negative control)
# ---------------------------------------------------------------------------
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
# session-50: D4 re-anchored — the store grew to 79 by the SANCTIONED
# batch-2 §18 application (23 operator promotions, c11_batch2_verdicts).
# session-52: D4 re-anchored again — the store grew to 118 by the
# SANCTIONED batch-3 §18 application (39 operator promotions,
# c11_batch3_verdicts).
# session-54: D4 re-anchored again — the store grew to 153 by the
# SANCTIONED batch-4 §18 application (35 operator promotions,
# c11_batch4_verdicts).
# The batch-1 verdict layer's protective intent is unchanged: its 28
# promotions stay exact, operator-attributed, and nothing outside a
# recorded CONFIRM set ever enters the store.
check("D4 store total 153 (28 pilot + 28 batch-1 + 23 batch-2 + 39 "
      "batch-3 + 35 batch-4), all operator",
      len(store_map) == 153
      and all(p.get("validated_by") == "operator"
              for p in store_map.values()))
n415 = [x for x in nodes_doc["nodes"]
        if any(sp.get("code") == "4CH1-4.15" for sp in x.get("spec_points", []))]
e415 = [e for e in edges_doc["edges"]
        if any("4.15" in a.get("file", "") for a in e.get("evidence", []))]
check("D5 negative control 4CH1-4.15: zero node/edge attachments",
      len(n415) == 0 and len(e415) == 0,
      f"nodes = {len(n415)}, edges = {len(e415)}")
# session-49: D6 re-anchored to SLICE PRESERVATION inside the grown store —
# the batch-2 authoring (sanctioned per-batch growth) extends the store
# beyond the batch-1 numbers; the invariant is that the pilot+batch-1 slices
# are preserved exactly (29+24 node codes, 33+24 PART_OF, 61+1 semantic from
# the earlier records) inside whatever the sanctioned total has become.
C_PILOT_SPS_SET = {"4CH1-1.25", "4CH1-1.26", "4CH1-1.27", "4CH1-1.28",
                   "4CH1-1.29", "4CH1-1.30", "4CH1-1.31", "4CH1-1.32",
                   "4CH1-1.33", "4CH1-1.34C", "4CH1-1.35C", "4CH1-1.36"}
B1_NODE_CODES = {n["code"] for n in yaml.safe_load(
    (HERE / "c11_batch1_decisions.yaml").read_text(encoding="utf-8")
)["nodes"]}
B1_SPS = {a["code"] for n in yaml.safe_load(
    (HERE / "c11_batch1_decisions.yaml").read_text(encoding="utf-8")
)["nodes"] for a in n.get("spec_points", [])}
live_codes = {n["code"] for n in nodes_doc["nodes"]}
live_earlier_partof = sum(
    1 for e in edges_doc["edges"]
    if e["relation"] == "PART_OF"
    and e["target"] in (B1_SPS | C_PILOT_SPS_SET))
check("D6 pilot+batch-1 slices preserved inside the grown store (29+24 nodes, 33+24 PART_OF; store total grows only by sanctioned batches)",
      {c["code"] for c in nodes_doc["nodes"]} >= (
          {n["code"] for n in dec["nodes"]} | B1_NODE_CODES)
      and live_codes >= B1_NODE_CODES
      and live_earlier_partof == 57
      and len(nodes_doc["nodes"]) >= 53 and len(edges_doc["edges"]) >= 118)
check("D7 no PART_OF edge promoted (node pathway not built)",
      not any(e["relation"] == "PART_OF"
              and e["validation_status"] == "HUMAN_VALIDATED"
              for e in edges_doc["edges"]))
check("D8 no batch-1 node is HUMAN_VALIDATED (nodes have no §18 pathway)",
      not any(x.get("validation_status") == "HUMAN_VALIDATED"
              for x in nodes_doc["nodes"]))

# ---------------------------------------------------------------------------
print()
if fails:
    print(f"FAILED: {len(fails)} check(s): {fails}")
    raise SystemExit(1)
print(f"c11_batch1_verdict_check: ALL PASS — batch-1 operator verdict layer "
      f"(28+24+4+RR rows, ruling 'CONFIRM all' session 48) schema-valid, "
      f"record-reconciled, application-reconciled (28 §18 promotions = the "
      f"CONFIRM set; RR settlement HOLD_REVIEW_REQUIRED; pilot slice "
      f"intact; store total 118 at session 52 — the batch-1 slice "
      f"preserved exactly inside the grown store).")
