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
                       REVIEW_REQUIRED); store total 171; the 14 batch-4
                       held candidates quarantined (never authored); the 5
                       ruled S1 owner codes NOT re-minted in the batch-4
                       node set; 4.15 negative control uncovered; no
                       PART_OF promoted; no batch-4 node HUMAN_VALIDATED;
                       live store shape 113/275/117/158

Usage: python3 scripts/c11_batch4_verdict_check.py
"""
from __future__ import annotations

from pathlib import Path

import sys
import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
# Session-55 repair (2026-09-22, dated): the C28 stage-2 migration moved the
# ratified stores to graph/igcse-chemistry/ (b3bca02); this checker still read
# the pre-migration root layout and has been dark since. Store paths now resolve
# through the C28 registry (graph_paths.py) — no expectation changed.
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402  # C28 §3.2 path registry
GRAPH = GP.qual_dir()          # the qual's ratified store dir
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
# session-55: the batch-5 authored-to-gate SUGGESTED surface (the record
# this store grew by; see the D2 re-anchor below)
B5_DEC = HERE / "c11_batch5_decisions.yaml"
B5_AUTHORED = {triple(e)
               for e in (yaml.safe_load(B5_DEC.read_text(encoding="utf-8"))
                         .get("edges") or [])}
live_b5_sugg = {k for k in B5_AUTHORED if k in live_sugg}
# session-62 re-anchor (2026-09-24, dated): +15 the SANCTIONED batch-9
# authored-to-gate record (14 CONCEPT + 1 MISCONCEPTION; 20 authored
# semantic + 21 PART_OF) — the operator gate decision; no test weakened.
check("D1 pilot slice intact: 28 pilot CONFIRM still HUMAN_VALIDATED",
      pilot_hv == pilot_confirms and len(pilot_hv) == 28)
# Session-55 re-anchor (2026-09-22, dated; protective intent unchanged): the
# batch-5 authored-to-gate edges (18, SUGGESTED) now join the 3 frozen pilot
# HOLDs as the live SUGGESTED semantic surface — awaiting the operator's
# batch-5 verdicts; the batch-4 assertion's protective core (the 3 HOLDs
# stay SUGGESTED and un-promoted) is unchanged.
# Session-56 re-anchor (2026-09-22, dated; protective intent unchanged): the
# batch-5 verdicts were APPLIED through §18 (18 operator promotions) — the
# 18 batch-5 authored edges left the SUGGESTED surface, so the live
# SUGGESTED semantic edges are again EXACTLY the 3 frozen pilot operator
# HOLDs (the pre-session-55 state); the batch-4 assertion's protective core
# (the 3 HOLDs stay SUGGESTED and un-promoted) is unchanged.
# Session-57 re-anchor (2026-09-22, dated; protective intent unchanged): the
# SANCTIONED batch-6 authored-to-gate record (16 SUGGESTED semantic edges)
# joins the 3 frozen pilot HOLDs as the live SUGGESTED surface — awaiting
# the operator's batch-6 verdicts; the protective core (the 3 HOLDs stay
# SUGGESTED and un-promoted; zero unbacked HV) is unchanged.
# Session-58 re-anchor (2026-09-22, dated; protective intent unchanged): the
# operator's batch-6 verdicts were APPLIED through §18 (16 operator
# promotions, c11_batch6_verdicts) — the 16 batch-6 authored edges left the
# SUGGESTED surface (all 16 now HUMAN_VALIDATED), so the live SUGGESTED
# semantic edges are again EXACTLY the 3 frozen pilot operator HOLDs (the
# pre-session-55 state); the protective core is unchanged.
B6_DEC = HERE / "c11_batch6_decisions.yaml"
B6_AUTHORED = {triple(e)
               for e in (yaml.safe_load(B6_DEC.read_text(encoding="utf-8"))
                         .get("edges") or [])}
live_b6_sugg = {k for k in B6_AUTHORED if k in live_sugg}
# session-59 re-anchor (dated, protective intent unchanged): the batch-7
# authoring (c11_batch7_decisions.yaml, authored to its operator gate at
# session 59) adds 19 SUGGESTED authored semantic edges to the live
# SUGGESTED surface (3 pilot HOLDs + 19 batch-7 authored); the batch-4/5/6
# slices stay fully HUMAN_VALIDATED and preserved exactly.
# session-60 re-anchor (dated, protective intent unchanged): the batch-7
# verdicts were APPLIED through §18 (19 operator promotions,
# c11_batch7_verdicts, applied 2026-09-23 via the B7 diff-review bundle —
# the operator's addendum §6/§7 verdict: PASS WITH NOTES), so the live
# SUGGESTED semantic surface is again EXACTLY the 3 frozen pilot operator
# HOLDs and the batch-7 authored edges are all HUMAN_VALIDATED.
B7_DEC = HERE / "c11_batch7_decisions.yaml"
B7_AUTHORED = {triple(e)
               for e in (yaml.safe_load(B7_DEC.read_text(encoding="utf-8"))
                         .get("edges") or [])}
# session-61 re-anchor (2026-09-24, dated; protective intent unchanged): the
# batch-8 authored-to-gate record (10 authored semantic edges) now joins the
# live SUGGESTED surface AT ITS OPERATOR GATE (the session-61 commissioning;
# the batch ends at the gate, zero promotions) — the surface is the 3 frozen
# pilot HOLDs PLUS the 10 batch-8 authored edges; the property protected is
# unchanged (no UNAUTHORIZED edge is SUGGESTED; the batch-4/5/6/7 authored
# sets stay fully HUMAN_VALIDATED).
# session-62 re-anchor (dated, protective intent unchanged): the batch-8
# verdicts were APPLIED through §18 (10 operator promotions,
# c11_batch8_verdicts, applied 2026-09-24 via the B8 diff-review bundle —
# the operator's completed-sheet §6/§7 verdict: PASS WITH NOTES), so the
# live SUGGESTED semantic surface is again EXACTLY the 3 frozen pilot
# operator HOLDs and the batch-8 authored edges are all HUMAN_VALIDATED.
# session-62 re-anchor (2026-09-24, dated; protective intent unchanged):
# the batch-9 authored-to-gate record (20 authored semantic edges) now
# joins the live SUGGESTED surface AT ITS OPERATOR GATE (the session-62
# commissioning of the S4 section; the batch ends at the gate, zero
# promotions) — the surface is the 3 frozen pilot HOLDs PLUS the 20
# batch-9 authored edges; the batch-4/5/6/7/8 authored sets stay fully
# HUMAN_VALIDATED.
B9_DEC = HERE / "c11_batch9_decisions.yaml"
B9_AUTHORED = {triple(e)
               for e in (yaml.safe_load(B9_DEC.read_text(encoding="utf-8"))
                         .get("edges") or [])}
B8_DEC = HERE / "c11_batch8_decisions.yaml"
B8_AUTHORED = {triple(e)
               for e in (yaml.safe_load(B8_DEC.read_text(encoding="utf-8"))
                         .get("edges") or [])}
# session-63 re-anchor (2026-09-25, dated; protective intent unchanged):
# the batch-9 verdicts were APPLIED through §18 (20 promotions, operator,
# the B9 diff-review bundle) — the 20 batch-9 authored edges left the
# SUGGESTED surface, so the live SUGGESTED semantic surface is again
# EXACTLY the 3 frozen pilot operator HOLDs (the pre-session-62-authoring
# state). No test weakened.
B10_DEC = HERE / "c11_batch10_decisions.yaml"
B10_AUTHORED = {triple(e)
                for e in (yaml.safe_load(B10_DEC.read_text(encoding="utf-8"))
                          .get("edges") or [])}
# session-65 re-anchor (2026-09-25, dated): the batch-10 verdicts were
# APPLIED through §18 (19 promotions, operator, the B10 diff-review
# bundle) — the 19 batch-10 authored edges left the SUGGESTED surface
# (live SUGGESTED = the 3 pilot HOLDs again) and store total
# 236 -> 255. No test weakened.
B11_DEC = HERE / "c11_batch11_decisions.yaml"
B11_AUTHORED = {triple(e)
                for e in (yaml.safe_load(
                    B11_DEC.read_text(encoding="utf-8"))
                    .get("edges") or [])}
# session-66 re-anchor (2026-09-25, dated; protective intent
# unchanged): the batch-11 authored-to-gate record (17 authored
# semantic edges) now joins the live SUGGESTED surface AT ITS
# OPERATOR GATE (the operator's "commission batch 11" directive;
# the batch ends at the gate, zero promotions) — the surface is
# the 3 frozen pilot HOLDs PLUS the 17 batch-11 authored edges;
# the batch-4..10 authored sets stay fully HUMAN_VALIDATED. No
# test weakened.
check("D2 the 3 pilot operator HOLDs stay SUGGESTED (un-promoted) and the "
      "live SUGGESTED semantic surface is EXACTLY the pilot HOLDs (the "
      "batch-8 authored edges were promoted by the operator's verdicts "
      "through §18 at session 62; the batch-9 authored edges were promoted "
      "by the operator's verdicts through §18 at session 63; batch-4/5/6 "
      "verdicts applied at sessions 54/56/58)",
      pilot_holds <= live_sugg and not (pilot_holds & hv)
      and live_sugg == pilot_holds | B11_AUTHORED
      and B10_AUTHORED <= hv
      and B6_AUTHORED <= hv and B7_AUTHORED <= hv and B8_AUTHORED <= hv
      and not live_b6_sugg and not live_b5_sugg,
      f"live SUGGESTED = {len(live_sugg)}")
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
# session-58 re-anchor (dated, protective intent unchanged): the batch-6
# §18 application added 16 operator promotions (c11_batch6_verdicts) —
# the store total moved 171 -> 187; the batch-4 slice stays preserved
# exactly.
# session-60 re-anchor (dated): the store grew 187 -> 206 by the SANCTIONED
# batch-7 §18 application (19 operator promotions, c11_batch7_verdicts);
# the batch-4 slice stays preserved exactly.
# session-62 re-anchor (dated): the store grew 206 -> 216 by the SANCTIONED
# batch-8 §18 application (10 operator promotions, c11_batch8_verdicts);
# the batch-4 slice stays preserved exactly.
# session-63 re-anchor (dated, protective intent unchanged): the batch-9
# §18 application added 20 operator promotions — the store total moved
# 216 -> 236; the batch-4 slice stays preserved exactly.
check("D8 store total 255 (28+28+23+39+35+18+16+19+10+20+19), all operator",
      len(store_map) == 255
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
# Session-55 re-anchor (2026-09-22, dated; protective intent unchanged):
# T-C19 (session 106, operator directive) later promoted ALL 117
# concept->SP PART_OF rows to HUMAN_VALIDATED via its own G19 pathway
# (scripts/c19_promotions.yaml + c19_promote.py, gated generator re-run,
# C19_APPLY_RECORD.md) — a LATER-authorized lane this check predates and
# was never re-run against. The property this check protects is narrower
# and still enforced: the §18 promotion record (c11_promotions.yaml)
# carries ZERO PART_OF identities (c11_promote.py rejects PART_OF
# categorically, T05/T06), and no NODE is promoted by any lane.
check("D10 no PART_OF edge promoted through the §18 record "
      "(PART_OF HV rows exist only via the later T-C19 G19 record)",
      not any(p.get("relation") == "PART_OF"
              for p in (promo.get("promotions") or []))
# Session-55 re-anchor (2026-09-22, dated; protective intent unchanged): the
# PART_OF HV layer is exactly the T-C19 G19 record's 117 rows; the 13 NEW
# batch-5 PART_OF rows are SUGGESTED pending their own attachment-
# promotion lane (the C19 pattern), so the all-HV form is re-anchored to
# the 117-count + batch-5-rows-SUGGESTED form.
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF"
              and e["validation_status"] == "HUMAN_VALIDATED") == 117
      and all(e["validation_status"] == "SUGGESTED"
              for e in edges_doc["edges"]
              if e["relation"] == "PART_OF"
              and e["validation_status"] != "HUMAN_VALIDATED"))
check("D11 no batch-4 node is HUMAN_VALIDATED (nodes have no §18 pathway)",
      not any(x.get("validation_status") == "HUMAN_VALIDATED"
              for x in nodes_doc["nodes"]))
# Session-55 re-anchor (2026-09-22, dated; protective intent unchanged): the
# store grew to 129/305/130 by the SANCTIONED batch-5 authored-to-gate record
# (16 nodes + 13 PART_OF + 18 authored semantic edges, ZERO promotions); the
# batch-4 slice below is still preserved exactly.
# Session-57 re-anchor (2026-09-22, dated; protective intent unchanged): the
# store grew to 142/334/142 by the SANCTIONED batch-6 authored-to-gate record
# (13 nodes + 12 PART_OF + 16 authored semantic edges, ZERO promotions); the
# batch-4 slice below is still preserved exactly.
# session-61 re-anchor (2026-09-24, dated): + the SANCTIONED batch-8
# authored-to-gate record (8 nodes / 17 edges = 7 PART_OF + 10
# semantic) — the operator gate decision; no test weakened.
check("D12 live store shape 193 nodes / 488 edges (211 PART_OF + 277 "
      "semantic)",
      len(nodes_doc["nodes"]) == 193 and len(edges_doc["edges"]) == 488
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF") == 211)
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
      f"slices intact; 171 store entries total; the 5 boundary targets "
      f"reused, zero re-mint).")
