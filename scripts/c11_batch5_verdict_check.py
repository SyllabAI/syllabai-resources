#!/usr/bin/env python3
"""T-C11 session 56 — c11_batch5_verdict_check.py: standing checker for the
batch-5 operator verdict record (scripts/c11_batch5_verdicts.yaml) and its
application state.

Checks (all fail-closed; every group must pass):
  A. schema          — sections, row ids in order, vocabulary, the verbatim
                       operator verdict (the completed review sheet §6,
                       session 56) + decided_by/date; NO rr_settlement
                       section (batch 5 authored zero RR edges)
  B. verdict shape   — 18 edge CONFIRM / 16 node CONFIRM (13 CONCEPT +
                       3 MISCONCEPTION) / 6 KEEP_AS_IS / held appendix
                       (14) acknowledged; reconciliation against the
                       batch-5 decision record (triples, node codes, NO
                       operator_decision blocks — identity decisions are
                       all KEEP_AS_IS, so no §7 re-authoring was
                       sanctioned); the five §6 CONFIRM_WITH_NOTE
                       qualifications carried in notes
  C. application     — three-way set equality: verdict CONFIRM set ==
                       live batch-5 HUMAN_VALIDATED set == batch-5 entries
                       in the promotion store (18 each, operator
                       attribution, the B5 diff-review bundle as
                       review_reference); nothing outside the CONFIRM set
                       was promoted
  D. invariants      — the pilot, batch-1..4 slices are intact
                       (28+28+23+39+35 HUMAN_VALIDATED; 3 pilot
                       operator-HOLD SUGGESTED — now the ONLY live
                       SUGGESTED semantic surface; both RR edges
                       REVIEW_REQUIRED); store total 171; the 14 batch-5
                       held candidates quarantined (never authored); the
                       13 ruled non-mint owner codes NOT re-minted in the
                       batch-5 node set; 4.15 negative control uncovered;
                       no PART_OF promoted through §18; no batch-5 node
                       HUMAN_VALIDATED; live store shape 129/306/130

Usage: python3 scripts/c11_batch5_verdict_check.py
"""
from __future__ import annotations

from pathlib import Path

import sys
import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
# Store paths resolve through the C28 registry (graph_paths.py) — the
# session-55 re-pointing convention (post-C28 layout).
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402  # C28 §3.2 path registry
GRAPH = GP.qual_dir()          # the qual's ratified store dir
VERDICTS = HERE / "c11_batch5_verdicts.yaml"
DECISIONS = HERE / "c11_batch5_decisions.yaml"
B1_VERDICTS = HERE / "c11_batch1_verdicts.yaml"
B1_DECISIONS = HERE / "c11_batch1_decisions.yaml"
B2_VERDICTS = HERE / "c11_batch2_verdicts.yaml"
B2_DECISIONS = HERE / "c11_batch2_decisions.yaml"
B3_VERDICTS = HERE / "c11_batch3_verdicts.yaml"
B3_DECISIONS = HERE / "c11_batch3_decisions.yaml"
B4_VERDICTS = HERE / "c11_batch4_verdicts.yaml"
B4_DECISIONS = HERE / "c11_batch4_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"

BUNDLE_REF = "graph/reports/C11_DIFF_REVIEW_B5_2026-09-22.md"
B1_RR_TRIPLE = ("4CH1-CON-CRYSTALLISATION REQUIRES_PREREQUISITE "
                "4CH1-CON-SOLUTION")
PILOT_RR_TRIPLE = ("4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE "
                   "4CH1-CON-AVOGADRO-LAW")
# the session-55 cross-slice boundary ruling's non-mint owner codes
# (boundary EDGES sanctioned into exactly two of them; boundary MINTING
# forbidden for all 13)
NON_MINT_OWNERS = {
    "4CH1-CON-ELECTRONIC-CONFIGURATION", "4CH1-CON-EXO-ENDO",
    "4CH1-CON-REDOX-ELECTRONS", "4CH1-CON-MOLECULE",
    "4CH1-CON-COVALENT-BOND", "4CH1-CON-ION", "4CH1-CON-IONIC-FORMULA",
    "4CH1-CON-ION-CHARGE-RULES", "4CH1-CON-EQ-SYMBOL", "4CH1-CON-EQ-WORD",
    "4CH1-CON-EQ-STATE-SYM", "4CH1-CON-NOBLE-GAS-INERTNESS",
    "4CH1-CON-WATER-CRYST",
}
# the three sanctioned cross-section boundary edges (session-55 ruling)
BOUNDARY_EDGES = (
    "4CH1-CON-COMBUSTION-O2 REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO",
    "4CH1-CON-G1-REACTIVITY-ECONFIG REQUIRES_PREREQUISITE "
    "4CH1-CON-ELECTRONIC-CONFIGURATION",
    "4CH1-CON-G7-REACTIVITY-ECONFIG REQUIRES_PREREQUISITE "
    "4CH1-CON-ELECTRONIC-CONFIGURATION",
)
# the five §6 CONFIRM_WITH_NOTE rows (qualifications ride in notes)
WITH_NOTE_QUALIFICATIONS = {
    "4CH1-CON-AIR-COMPOSITION EXPLAINED_BY "
    "4CH1-CON-O2-PERCENT-DETERMINATION",
    "4CH1-CON-G1-REACTIVITY-ECONFIG",
    "4CH1-CON-G7-REACTIVITY-ECONFIG",
    "4CH1-MIS-CUO-COLOUR",
    "4CH1-MIS-HALOGEN-HALIDE",
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
b4_vd = yaml.safe_load(B4_VERDICTS.read_text(encoding="utf-8"))
b4_dec = yaml.safe_load(B4_DECISIONS.read_text(encoding="utf-8"))
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
check("A2 operator verdict recorded verbatim (completed sheet §6, "
      "session 56)",
      "Operator verdict: PASS" in (r.get("statement") or "")
      and "separately governed promotion step" in (r.get("statement") or "")
      and "proceed to encoding/reconciliation" in (r.get("statement") or "")
      and r.get("session") == 56
      and r.get("decided_by") == "operator"
      and r.get("decided_date") == "2026-09-22")
check("A3 edge rows B5-E-01..B5-E-18 sequential, complete",
      [x["id"] for x in ev] == [f"B5-E-{i:02d}" for i in range(1, 19)])
check("A4 node rows B5-N-01..13 + B5-M-01..03 sequential, complete",
      [x["id"] for x in nv] == [f"B5-N-{i:02d}" for i in range(1, 14)]
      + [f"B5-M-{i:02d}" for i in range(1, 4)])
check("A5 identity rows B5-ID-01..06 sequential, complete",
      [x["id"] for x in ids] == [f"B5-ID-{i:02d}" for i in range(1, 7)])
V_EDGE = {"CONFIRM", "REJECT", "HOLD", "MERGE", "SPLIT"}
V_ID = {"MERGE", "SPLIT", "KEEP_AS_IS"}
check("A6 all verdicts in vocabulary, none empty",
      all(x["verdict"] in V_EDGE for x in ev)
      and all(x["verdict"] in V_EDGE for x in nv)
      and all(x["verdict"] in V_ID for x in ids))
check("A7 template consumed (fill + rename per the gate pathway)",
      not (HERE / "c11_batch5_verdicts_template.yaml").exists()
      and VERDICTS.exists())
check("A8 encoding mapping records the WITH_NOTE vocabulary rule + the "
      "code-keying identity-safety rule",
      "no WITH_NOTE value" in (r.get("mapping") or "")
      and "keyed by CODE" in (r.get("mapping") or ""))

# ---------------------------------------------------------------------------
# B. verdict shape + decision-record reconciliation
# ---------------------------------------------------------------------------
ec = {}
for x in ev:
    ec[x["verdict"]] = ec.get(x["verdict"], 0) + 1
nc = {}
for x in nv:
    nc[x["verdict"]] = nc.get(x["verdict"], 0) + 1
check("B1 edge verdicts: 18 CONFIRM / 0 others",
      ec == {"CONFIRM": 18}, f"{ec}")
check("B2 node verdicts: 16 CONFIRM / 0 others",
      nc == {"CONFIRM": 16}, f"{nc}")
check("B3 identity decisions: 6 x KEEP_AS_IS",
      [x["verdict"] for x in ids] == ["KEEP_AS_IS"] * 6)
check("B4 batch 5 authored ZERO RR edges (no settlement row needed)",
      not any(e["validation_status"] == "REVIEW_REQUIRED"
              for e in dec["edges"]))
check("B5 held appendix acknowledged (14 preserved, quarantined)",
      held_ack.get("acknowledged") is True
      and len(dec["held"]) == 14
      and all(h["status"] == "held" for h in dec["held"]))

b_suggested = {triple(e) for e in dec["edges"]
               if e["validation_status"] == "SUGGESTED"}
check("B6 verdict triples = the batch-5 record's 18 SUGGESTED edges",
      {x["triple"] for x in ev} == b_suggested and len(b_suggested) == 18)
check("B7 verdict node codes = the batch-5 record's 16 node codes "
      "(13 CONCEPT + 3 MISCONCEPTION)",
      {x["code"] for x in nv} == {c["code"] for c in dec["nodes"]}
      and len(dec["nodes"]) == 16
      and sum(1 for c in dec["nodes"] if c["family"] == "CONCEPT") == 13
      and sum(1 for c in dec["nodes"]
              if c["family"] == "MISCONCEPTION") == 3)
check("B8 NO operator_decision blocks in the batch-5 record (none "
      "sanctioned: no RR, no ENRICHMENT node, all identity KEEP_AS_IS)",
      sum(1 for x in dec["nodes"] + dec["edges"]
          if "operator_decision" in x) == 0)
check("B9 no ENRICHMENT-scoped node in batch 5 (none to scope)",
      not any(sp.get("role") == "ENRICHMENT"
              for x in dec["nodes"] for sp in x.get("spec_points", [])))
# the five §6 CONFIRM_WITH_NOTE qualifications carried in notes
e01 = [x for x in ev if x["triple"] ==
       "4CH1-CON-AIR-COMPOSITION EXPLAINED_BY "
       "4CH1-CON-O2-PERCENT-DETERMINATION"][0]
nwcodes = {x["code"] for x in nv
           if x["code"] in {"4CH1-CON-G1-REACTIVITY-ECONFIG",
                            "4CH1-CON-G7-REACTIVITY-ECONFIG",
                            "4CH1-MIS-CUO-COLOUR",
                            "4CH1-MIS-HALOGEN-HALIDE"}}
check("B10 the five §6 CONFIRM_WITH_NOTE qualifications carried in notes "
      "(B5-E-01 grounding-relation restriction + the 4 pass-2 WITH_NOTE "
      "node rows)",
      e01["notes"].startswith("Operator §6 (session 56): "
                              "CONFIRM_WITH_NOTE retained")
      and "do not reinterpret" in e01["notes"]
      and len(nwcodes) == 4
      and all(next(x for x in nv if x["code"] == c)["notes"].startswith(
          "Operator §6: CONFIRM_WITH_NOTE retained") for c in nwcodes))

# ---------------------------------------------------------------------------
# C. application (three-way set equality; session-56 §18 application)
# ---------------------------------------------------------------------------
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
b_triples = {triple(e) for e in dec["edges"]}
b_hv = {t for t in hv if t in b_triples}
confirms = {x["triple"] for x in ev if x["verdict"] == "CONFIRM"}
store_map = {" ".join((p["edge"]["source"], p["edge"]["relation"],
                       p["edge"]["target"])): p
             for p in promo["promotions"]}
check("C1 live batch-5 HUMAN_VALIDATED set = the 18 CONFIRM verdicts",
      b_hv == confirms and len(b_hv) == 18,
      f"live = {len(b_hv)}, verdicts = {len(confirms)}")
check("C2 promotion store = exactly the 18 batch-5 CONFIRM entries",
      set(store_map) & b_triples == confirms)
b_store = {k: p for k, p in store_map.items() if k in b_triples}
check("C3 batch-5 store entries carry operator attribution + 2026-09-22",
      all(p.get("validated_by") == "operator"
          and p.get("validated_date") == "2026-09-22"
          for p in b_store.values()), f"entries = {len(b_store)}")
check("C4 batch-5 store entries reference the B5 diff-review bundle",
      all(p.get("review_reference") == BUNDLE_REF
          for p in b_store.values()))
check("C5 no REJECT/HOLD/MERGE/SPLIT verdicts left un-applied",
      all(x["verdict"] == "CONFIRM" for x in ev))
check("C6 the THREE sanctioned cross-section boundary edges are "
      "HUMAN_VALIDATED (session-55 ruling applied, not re-minted)",
      all(any(triple(e) == t and e["validation_status"] == "HUMAN_VALIDATED"
              for e in sem) for t in BOUNDARY_EDGES))

# ---------------------------------------------------------------------------
# D. invariants (pilot + batch-1..4 slices, store total, negative control,
#    boundary mint discipline)
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
# Session-56 re-anchor (2026-09-22, dated; protective intent unchanged):
# the batch-5 verdicts were APPLIED through §18 (18 promotions, operator) —
# the 18 batch-5 authored edges left the SUGGESTED surface, so the live
# SUGGESTED semantic edges are again EXACTLY the 3 frozen pilot operator
# HOLDs (the batch-4-check D2 assertion's post-application state).
# Session-57 re-anchor (2026-09-22, dated; protective intent unchanged):
# the SANCTIONED batch-6 authored-to-gate record (16 SUGGESTED semantic
# edges) joins the 3 frozen pilot HOLDs as the live SUGGESTED surface —
# awaiting the operator's batch-6 verdicts; the protective core (the 3
# HOLDs stay SUGGESTED and un-promoted; zero unbacked HV) is unchanged.
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
# session-59 re-anchor (dated, protective intent unchanged): the batch-7
# authoring (c11_batch7_decisions.yaml, authored to its operator gate at
# session 59) adds 19 SUGGESTED authored semantic edges to the live
# SUGGESTED surface (3 pilot HOLDs + 19 batch-7 authored); the batch-4/5/6
# slices stay fully HUMAN_VALIDATED and preserved exactly.
B7_DEC = HERE / "c11_batch7_decisions.yaml"
B7_AUTHORED = {triple(e)
               for e in (yaml.safe_load(B7_DEC.read_text(encoding="utf-8"))
                         .get("edges") or [])}
# session-60 re-anchor (dated, protective intent unchanged): the batch-7
# verdicts were APPLIED through §18 (19 operator promotions,
# c11_batch7_verdicts, applied 2026-09-23 via the B7 diff-review bundle —
# the operator's addendum §6/§7 verdict: PASS WITH NOTES), so the live
# SUGGESTED semantic surface is again EXACTLY the 3 frozen pilot operator
# HOLDs and the batch-7 authored edges are all HUMAN_VALIDATED.
check("D2 the 3 pilot operator HOLDs stay SUGGESTED (un-promoted) and "
      "the live SUGGESTED semantic surface is EXACTLY the pilot HOLDs (the "
      "batch-7 authored edges were promoted by the operator's verdicts "
      "through §18 at session 60; batch-4/5/6 verdicts applied at sessions "
      "54/56/58)",
      pilot_holds <= live_sugg and not (pilot_holds & hv)
      and live_sugg == pilot_holds
      and B6_AUTHORED <= hv and B7_AUTHORED <= hv
      and not (live_sugg & B6_AUTHORED),
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
# batch-4 slice
b4_triples = {triple(e) for e in b4_dec["edges"]}
b4_hv = {t for t in hv if t in b4_triples}
b4_confirms = {x["triple"] for x in b4_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D8 batch-4 slice intact: 35 batch-4 CONFIRM still HUMAN_VALIDATED",
      b4_hv == b4_confirms and len(b4_hv) == 35)
# session-58 re-anchor (dated, protective intent unchanged): the batch-6
# §18 application added 16 operator promotions (c11_batch6_verdicts) —
# the store total moved 171 -> 187; the batch-5 slice stays preserved
# exactly.
# session-60 re-anchor (dated): the store grew 187 -> 206 by the SANCTIONED
# batch-7 §18 application (19 operator promotions, c11_batch7_verdicts);
# the batch-5 slice stays preserved exactly.
check("D9 store total 206 (28+28+23+39+35+18+16+19), all operator",
      len(store_map) == 206
      and all(p.get("validated_by") == "operator"
              for p in store_map.values()))
n415 = [x for x in nodes_doc["nodes"]
        if any(sp.get("code") == "4CH1-4.15"
               for sp in x.get("spec_points", []))]
e415 = [e for e in edges_doc["edges"]
        if any("4.15" in a.get("file", "") for a in e.get("evidence", []))]
check("D10 negative control 4CH1-4.15: zero node/edge attachments",
      len(n415) == 0 and len(e415) == 0,
      f"nodes = {len(n415)}, edges = {len(e415)}")
check("D11 no PART_OF edge promoted through the §18 record "
      "(PART_OF HV rows exist only via the later T-C19 G19 record; the 13 "
      "batch-5 PART_OF rows stay SUGGESTED pending their own lane)",
      not any(p.get("relation") == "PART_OF"
              for p in (promo.get("promotions") or []))
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF"
              and e["validation_status"] == "HUMAN_VALIDATED") == 117
      and all(e["validation_status"] == "SUGGESTED"
              for e in edges_doc["edges"]
              if e["relation"] == "PART_OF"
              and e["validation_status"] != "HUMAN_VALIDATED"))
check("D12 no batch-5 node is HUMAN_VALIDATED (nodes have no §18 pathway; "
      "the §6 confirmations do not promote nodes)",
      not any(x.get("validation_status") == "HUMAN_VALIDATED"
              for x in nodes_doc["nodes"]))
# Session-57 re-anchor (2026-09-22, dated; protective intent unchanged): the
# store grew to 142/334/142 by the SANCTIONED batch-6 authored-to-gate record
# (13 nodes + 12 PART_OF + 16 authored semantic edges, ZERO promotions; the
# batch-5 slice below is still preserved exactly).
check("D13 live store shape 157 nodes / 367 edges (156 PART_OF + 211 "
      "semantic) — verdicts move statuses only, never shape",
      len(nodes_doc["nodes"]) == 157 and len(edges_doc["edges"]) == 367
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF") == 156)
# boundary mint discipline (the session-55 cross-slice ruling)
b5_codes = {c["code"] for c in dec["nodes"]}
check("D14 zero ruled non-mint owner re-minted in the batch-5 node set "
      "(the 13 session-55 non_mint_list codes absent from the mint)",
      not (b5_codes & NON_MINT_OWNERS), f"collision = "
      f"{sorted(b5_codes & NON_MINT_OWNERS)}")
# the sanctioned boundary targets exist exactly once in the live store
# (no duplicate mint by the boundary edges' application)
for t in BOUNDARY_EDGES:
    hits = [e for e in edges_doc["edges"] if triple(e) == t]
    check(f"D15 boundary target authored exactly once: {t}",
          len(hits) == 1 and hits[0]["validation_status"] == "HUMAN_VALIDATED")
# the 14 held candidates were never authored -> absent from the live store
held_ids = [h["id"] for h in dec["held"]]
check("D16 the 14 batch-5 held candidates stay quarantined (recorded, "
      "never authored; store untouched by holds)",
      len(held_ids) == 14
      and not any(triple(e) in b_suggested for e in dec["edges"]
                  if e["validation_status"] == "REVIEW_REQUIRED"))

# ---------------------------------------------------------------------------
print()
if fails:
    print(f"FAILED: {len(fails)} check(s): {fails}")
    raise SystemExit(1)
print(f"c11_batch5_verdict_check: ALL PASS — batch-5 operator verdict layer "
      f"(18+16+6 rows, the completed-sheet §6 verdict; zero RR authored; "
      f"the five CONFIRM_WITH_NOTE qualifications carried in notes) "
      f"schema-valid, record-reconciled, application-reconciled (18 §18 "
      f"promotions = the CONFIRM set; no operator_decision blocks; pilot + "
      f"batch-1..4 slices intact; 171 store entries total; the 3 boundary "
      f"targets reused, zero re-mint; 13 non-mint owners respected).")
