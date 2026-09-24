#!/usr/bin/env python3
"""T-C11 session 65 — c11_batch10_verdict_check.py: standing checker for the
batch-10 operator verdict record (scripts/c11_batch10_verdicts.yaml) and its
application state.

Checks (all fail-closed; every group must pass):
  A. schema          — sections, row ids in order, vocabulary, the verbatim
                       operator verdict (the completed sheet §6/§7, session
                       65: PASS WITH NOTES) + decided_by/date; the session-65
                       completed-sheet intake record (INLINE RESTATED sheet,
                       detail-preserving variant, via the zai-web chat lane;
                       the batch-5/6/8 byte-identity check does NOT apply —
                       the batch-9/10 CONFORMANCE gates apply and passed) +
                       the operator's REPORTED-state caveat; NO
                       rr_settlement section (batch 10 authored zero RR
                       edges)
  B. verdict shape   — 19 edge CONFIRM / 8 node CONFIRM (7 CONCEPT + 1
                       MISCONCEPTION) / 5 KEEP_AS_IS / held appendix (9)
                       acknowledged with the operator's per-candidate KEEP
                       HELD dispositions; reconciliation against the
                       batch-10 decision record (triples, node codes, NO
                       operator_decision blocks — identity decisions are
                       all KEEP_AS_IS, so no §7 re-authoring was
                       sanctioned); NO CONFIRM_WITH_NOTE exists in this
                       batch (the operator ruled universally; the NOTES in
                       PASS WITH NOTES are the sheet-level REPORTED caveat
                       + the anti-duplication guardrail, carried in
                       meta.operator_ruling); the THIRTEEN sanctioned
                       boundary rows carry the ownership/retention note
  C. application     — three-way set equality: verdict CONFIRM set ==
                       live batch-10 HUMAN_VALIDATED set == batch-10
                       entries in the promotion store (19 each, operator
                       attribution 2026-09-25, the B10 diff-review bundle
                       as review_reference); nothing outside the CONFIRM
                       set was promoted
  D. invariants      — the pilot + batch-1..9 slices are intact
                       (28+28+23+39+35+18+16+19+10+20 HUMAN_VALIDATED; the
                       3 pilot operator-HOLD SUGGESTED — the ONLY live
                       SUGGESTED semantic surface now that the batch-10
                       verdicts are applied; both RR edges
                       REVIEW_REQUIRED); store total 255, all operator;
                       the 9 batch-10 held candidates quarantined (never
                       authored FROM the held record — the single triple
                       coincidence B10-H-04 == the sanctioned boundary
                       edge B10-E-18 is the session-64 ruling's TARGET-2
                       x2 precedent, both surfaces explicitly ruled by
                       the operator); the 48 ruled non-mint owner codes
                       NOT re-minted in the batch-10 node set; 4.15
                       negative control uncovered; no PART_OF promoted
                       through §18 (the batch-9/10 PART_OF rows stay
                       SUGGESTED pending their own lane); no batch-10
                       node HUMAN_VALIDATED; live store shape 188/459/199;
                       the THIRTEEN sanctioned cross-section boundary
                       edges applied with EXACT ownership (all into
                       EXISTING owners — the batch-9 owners
                       CON-HOMOLOGOUS-SERIES x2, CON-ORGANIC-FORMULAE x2,
                       CON-HYDROCARBON, CON-ALKANES,
                       CON-ORGANIC-REACTION-CLASSES, CON-IUPAC-NAMING,
                       CON-CRACKING; batch-5 CON-COMBUSTION-O2; batch-6
                       CON-OX-RED-AGENTS; batch-1
                       CON-FRACTIONAL-DISTILLATION; batch-7
                       CON-ACID-REACTIONS; no batch-10 mint as target)

Usage: python3 scripts/c11_batch10_verdict_check.py
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
VERDICTS = HERE / "c11_batch10_verdicts.yaml"
DECISIONS = HERE / "c11_batch10_decisions.yaml"
B1_VERDICTS = HERE / "c11_batch1_verdicts.yaml"
B1_DECISIONS = HERE / "c11_batch1_decisions.yaml"
B2_VERDICTS = HERE / "c11_batch2_verdicts.yaml"
B2_DECISIONS = HERE / "c11_batch2_decisions.yaml"
B3_VERDICTS = HERE / "c11_batch3_verdicts.yaml"
B3_DECISIONS = HERE / "c11_batch3_decisions.yaml"
B4_VERDICTS = HERE / "c11_batch4_verdicts.yaml"
B4_DECISIONS = HERE / "c11_batch4_decisions.yaml"
B5_VERDICTS = HERE / "c11_batch5_verdicts.yaml"
B5_DECISIONS = HERE / "c11_batch5_decisions.yaml"
B6_VERDICTS = HERE / "c11_batch6_verdicts.yaml"
B6_DECISIONS = HERE / "c11_batch6_decisions.yaml"
B7_VERDICTS = HERE / "c11_batch7_verdicts.yaml"
B7_DECISIONS = HERE / "c11_batch7_decisions.yaml"
B8_VERDICTS = HERE / "c11_batch8_verdicts.yaml"
B8_DECISIONS = HERE / "c11_batch8_decisions.yaml"
B9_VERDICTS = HERE / "c11_batch9_verdicts.yaml"
B9_DECISIONS = HERE / "c11_batch9_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"

BUNDLE_REF = "graph/reports/C11_DIFF_REVIEW_B10_2026-09-25.md"
B1_RR_TRIPLE = ("4CH1-CON-CRYSTALLISATION REQUIRES_PREREQUISITE "
                "4CH1-CON-SOLUTION")
PILOT_RR_TRIPLE = ("4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE "
                   "4CH1-CON-AVOGADRO-LAW")
# the session-64 cross-slice boundary ruling's non-mint owner codes,
# loaded from the ruling itself (48 recorded; asserted, not trusted)
B10_RULING = HERE / "c11_batch10_boundary_ruling.yaml"
# the THIRTEEN sanctioned cross-section boundary edges (session-64
# ruling): all into EXISTING owners — the batch-9 owners x7 distinct
# (HOMOLOGOUS-SERIES x2, ORGANIC-FORMULAE x2, HYDROCARBON, ALKANES,
# ORGANIC-REACTION-CLASSES, IUPAC-NAMING, CRACKING), batch-5
# CON-COMBUSTION-O2, batch-6 CON-OX-RED-AGENTS, batch-1
# CON-FRACTIONAL-DISTILLATION, batch-7 CON-ACID-REACTIONS
BOUNDARY_EDGES_EXISTING = (
    "4CH1-CON-ALKENES REQUIRES_PREREQUISITE "
    "4CH1-CON-HOMOLOGOUS-SERIES",
    "4CH1-CON-ALKENES REQUIRES_PREREQUISITE 4CH1-CON-ORGANIC-FORMULAE",
    "4CH1-CON-ALKENES REQUIRES_PREREQUISITE 4CH1-CON-HYDROCARBON",
    "4CH1-CON-BROMINE-WATER-TEST REQUIRES_PREREQUISITE 4CH1-CON-ALKANES",
    "4CH1-CON-BROMINE-WATER-TEST REQUIRES_PREREQUISITE "
    "4CH1-CON-ORGANIC-REACTION-CLASSES",
    "4CH1-CON-ALCOHOLS REQUIRES_PREREQUISITE "
    "4CH1-CON-HOMOLOGOUS-SERIES",
    "4CH1-CON-ALCOHOLS REQUIRES_PREREQUISITE 4CH1-CON-IUPAC-NAMING",
    "4CH1-CON-ETHANOL-OXIDATION REQUIRES_PREREQUISITE "
    "4CH1-CON-COMBUSTION-O2",
    "4CH1-CON-ETHANOL-OXIDATION REQUIRES_PREREQUISITE "
    "4CH1-CON-OX-RED-AGENTS",
    "4CH1-CON-ETHANOL-MANUFACTURE REQUIRES_PREREQUISITE "
    "4CH1-CON-CRACKING",
    "4CH1-CON-ETHANOL-MANUFACTURE REQUIRES_PREREQUISITE "
    "4CH1-CON-FRACTIONAL-DISTILLATION",
    "4CH1-CON-CARBOXYLIC-ACIDS REQUIRES_PREREQUISITE "
    "4CH1-CON-ORGANIC-FORMULAE",
    "4CH1-CON-CARBOXYLIC-ACID-REACTIONS REQUIRES_PREREQUISITE "
    "4CH1-CON-ACID-REACTIONS",
)
# the five §6.1 identity decisions (ACCEPT -> KEEP_AS_IS per the
# vocabulary rule) and the nodes they rule
IDENTITY_LINK = {
    "4CH1-CON-ALKENES": "B10-ID-01",
    "4CH1-CON-BROMINE-WATER-TEST": "B10-ID-02",
    "4CH1-CON-ETHANOL-MANUFACTURE": "B10-ID-03",
    "4CH1-CON-CARBOXYLIC-ACIDS": "B10-ID-04",
    "4CH1-MIS-PROPANOL-POSITION": "B10-ID-05",
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
rul = yaml.safe_load(B10_RULING.read_text(encoding="utf-8"))
b1_vd = yaml.safe_load(B1_VERDICTS.read_text(encoding="utf-8"))
b1_dec = yaml.safe_load(B1_DECISIONS.read_text(encoding="utf-8"))
b2_vd = yaml.safe_load(B2_VERDICTS.read_text(encoding="utf-8"))
b2_dec = yaml.safe_load(B2_DECISIONS.read_text(encoding="utf-8"))
b3_vd = yaml.safe_load(B3_VERDICTS.read_text(encoding="utf-8"))
b3_dec = yaml.safe_load(B3_DECISIONS.read_text(encoding="utf-8"))
b4_vd = yaml.safe_load(B4_VERDICTS.read_text(encoding="utf-8"))
b4_dec = yaml.safe_load(B4_DECISIONS.read_text(encoding="utf-8"))
b5_vd = yaml.safe_load(B5_VERDICTS.read_text(encoding="utf-8"))
b5_dec = yaml.safe_load(B5_DECISIONS.read_text(encoding="utf-8"))
b6_vd = yaml.safe_load(B6_VERDICTS.read_text(encoding="utf-8"))
b6_dec = yaml.safe_load(B6_DECISIONS.read_text(encoding="utf-8"))
b7_vd = yaml.safe_load(B7_VERDICTS.read_text(encoding="utf-8"))
b7_dec = yaml.safe_load(B7_DECISIONS.read_text(encoding="utf-8"))
b8_vd = yaml.safe_load(B8_VERDICTS.read_text(encoding="utf-8"))
b8_dec = yaml.safe_load(B8_DECISIONS.read_text(encoding="utf-8"))
b9_vd = yaml.safe_load(B9_VERDICTS.read_text(encoding="utf-8"))
b9_dec = yaml.safe_load(B9_DECISIONS.read_text(encoding="utf-8"))
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
check("A2 operator verdict recorded verbatim (completed sheet §6/§7, "
      "session 65: PASS WITH NOTES) + decided_by/date",
      "PASS WITH NOTES" in (r.get("statement") or "")
      and "Encode the completed Batch 10 verdict surface"
      in (r.get("statement") or "")
      and "No node or edge is promoted by this review sheet itself"
      in (r.get("statement") or "")
      and r.get("session") == 65
      and r.get("decided_by") == "operator"
      and r.get("decided_date") == "2026-09-25")
check("A3 the session-65 completed-sheet intake record present (INLINE "
      "RESTATED sheet, detail-preserving variant, via the zai-web chat "
      "lane; byte-identity check does NOT apply; the batch-9/10 "
      "CONFORMANCE gates) + the operator's REPORTED-state caveat "
      "recorded verbatim",
      "RESTATED" in (r.get("completed_sheet") or "")
      and "zai-web" in (r.get("completed_sheet") or "")
      and "CONFORMANCE" in (r.get("completed_sheet") or "")
      and "REPORTED / VERIFIED BY SUBMITTED ARTIFACT"
      in (r.get("reported_state_caveat") or "")
      and "not been independently re-executed"
      in (r.get("reported_state_caveat") or "")
      and "5db5de1" in (r.get("reported_state_caveat") or ""))
check("A4 edge rows B10-E-01..B10-E-19 sequential, complete",
      [x["id"] for x in ev] == [f"B10-E-{i:02d}" for i in range(1, 20)])
check("A5 node rows B10-N-01..07 + B10-M-01 sequential, complete",
      [x["id"] for x in nv] == [f"B10-N-{i:02d}" for i in range(1, 8)]
      + ["B10-M-01"])
check("A6 identity rows B10-ID-01..05 sequential, complete",
      [x["id"] for x in ids] == [f"B10-ID-{i:02d}" for i in range(1, 6)])
V_EDGE = {"CONFIRM", "REJECT", "HOLD", "MERGE", "SPLIT"}
V_ID = {"MERGE", "SPLIT", "KEEP_AS_IS"}
check("A7 all verdicts in vocabulary, none empty",
      all(x["verdict"] in V_EDGE for x in ev)
      and all(x["verdict"] in V_EDGE for x in nv)
      and all(x["verdict"] in V_ID for x in ids))
check("A8 template consumed (fill + rename per the gate pathway)",
      not (HERE / "c11_batch10_verdicts_template.yaml").exists()
      and VERDICTS.exists())
check("A9 encoding mapping records the universal-ruling encoding + the "
      "ACCEPT->KEEP_AS_IS vocabulary mapping + the code-keying "
      "identity-safety rule (sheet table-order node numbering vs the "
      "template's alphabetical-by-code numbering)",
      "cover the entire coded surface" in (r.get("mapping") or "")
      and "KEEP_AS_IS" in (r.get("mapping") or "")
      and "keyed by CODE" in (r.get("mapping") or "")
      and "table order" in (r.get("mapping") or ""))

# ---------------------------------------------------------------------------
# B. verdict shape + decision-record reconciliation
# ---------------------------------------------------------------------------
ec = {}
for x in ev:
    ec[x["verdict"]] = ec.get(x["verdict"], 0) + 1
nc = {}
for x in nv:
    nc[x["verdict"]] = nc.get(x["verdict"], 0) + 1
check("B1 edge verdicts: 19 CONFIRM / 0 others",
      ec == {"CONFIRM": 19}, f"{ec}")
check("B2 node verdicts: 8 CONFIRM / 0 others",
      nc == {"CONFIRM": 8}, f"{nc}")
check("B3 identity decisions: 5 x KEEP_AS_IS (the §6.1 ACCEPT of each "
      "keep-as-ruled question)",
      [x["verdict"] for x in ids] == ["KEEP_AS_IS"] * 5
      and all("ACCEPT" in x["notes"] for x in ids))
check("B4 batch 10 authored ZERO RR edges (no settlement row needed)",
      not any(e["validation_status"] == "REVIEW_REQUIRED"
              for e in dec["edges"]))
check("B5 held appendix acknowledged (9 preserved, quarantined; the "
      "operator's NINE per-candidate KEEP HELD dispositions recorded "
      "verbatim; the §19 failure-class provenance rule recorded)",
      held_ack.get("acknowledged") is True
      and len(dec["held"]) == 9
      and all(h["status"] == "held" for h in dec["held"])
      and "catalyst mechanism not load-bearing"
      in (held_ack.get("notes") or "")
      and "exo/endo is enrichment, not load-bearing"
      in (held_ack.get("notes") or "")
      and "failure-class provenance" in (held_ack.get("notes") or ""))

b_suggested = {triple(e) for e in dec["edges"]
               if e["validation_status"] == "SUGGESTED"}
check("B6 verdict triples = the batch-10 record's 19 SUGGESTED edges",
      {x["triple"] for x in ev} == b_suggested and len(b_suggested) == 19)
check("B7 verdict node codes = the batch-10 record's 8 node codes "
      "(7 CONCEPT + 1 MISCONCEPTION)",
      {x["code"] for x in nv} == {c["code"] for c in dec["nodes"]}
      and len(dec["nodes"]) == 8
      and sum(1 for c in dec["nodes"] if c["family"] == "CONCEPT") == 7
      and sum(1 for c in dec["nodes"]
              if c["family"] == "MISCONCEPTION") == 1)
check("B8 NO operator_decision blocks in the batch-10 record (none "
      "sanctioned: no RR, no ENRICHMENT node, all identity KEEP_AS_IS)",
      sum(1 for x in dec["nodes"] + dec["edges"]
          if "operator_decision" in x) == 0)
check("B9 no ENRICHMENT-scoped node in batch 10 (none to scope)",
      not any(sp.get("role") == "ENRICHMENT"
              for x in dec["nodes"] for sp in x.get("spec_points", [])))
check("B10 NO CONFIRM_WITH_NOTE in this batch — the operator ruled "
      "universally (the NOTES in PASS WITH NOTES are the sheet-level "
      "REPORTED caveat + anti-duplication guardrail in "
      "meta.operator_ruling, not per-row qualifications)",
      "CONFIRM_WITH_NOTE" not in (r.get("statement") or "")
      and "no WITH_NOTE value" in (r.get("mapping") or "")
      and "anti-duplication guardrail" in (r.get("mapping") or "")
      and "REPORTED / VERIFIED BY SUBMITTED ARTIFACT"
      in (r.get("reported_state_caveat") or ""))
# the THIRTEEN boundary rows carry the ownership/retention note
bnd_rows = [x for x in ev if x["triple"] in BOUNDARY_EDGES_EXISTING]
check("B11 the THIRTEEN sanctioned boundary rows carry the "
      "ownership/retention note (session-64 ruling; 'retained exactly as "
      "ruled'; no duplicate mint)",
      len(bnd_rows) == 13
      and all("Sanctioned cross-section boundary edge" in x["notes"]
              and "retained exactly as ruled" in x["notes"]
              for x in bnd_rows))
e05 = next(x for x in ev if x["id"] == "B10-E-05")
check("B12 the E-05 note carries the pinned Alkenes MS Q4(b)(ii) Reject "
      "record (B10-ID-05 linkage)",
      "Reject propan-1-ol / 1-propanol" in e05["notes"]
      and "B10-ID-05" in e05["notes"])
check("B13 the five identity-linked nodes carry their B10-ID linkage in "
      "notes (the four one-family consolidations + the misconception "
      "mint); plain CONFIRM rows carry none",
      all(iid in next(x["notes"] for x in nv if x["code"] == code)
          for code, iid in IDENTITY_LINK.items())
      and sum(1 for x in nv if x["notes"] == "") == 3)

# ---------------------------------------------------------------------------
# C. application (three-way set equality; session-65 §18 application)
# ---------------------------------------------------------------------------
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
b_triples = {triple(e) for e in dec["edges"]}
b_hv = {t for t in hv if t in b_triples}
confirms = {x["triple"] for x in ev if x["verdict"] == "CONFIRM"}
store_map = {" ".join((p["edge"]["source"], p["edge"]["relation"],
                       p["edge"]["target"])): p
             for p in promo["promotions"]}
check("C1 live batch-10 HUMAN_VALIDATED set = the 19 CONFIRM verdicts",
      b_hv == confirms and len(b_hv) == 19,
      f"live = {len(b_hv)}, verdicts = {len(confirms)}")
check("C2 promotion store = exactly the 19 batch-10 CONFIRM entries",
      set(store_map) & b_triples == confirms)
b_store = {k: p for k, p in store_map.items() if k in b_triples}
check("C3 batch-10 store entries carry operator attribution + 2026-09-25",
      all(p.get("validated_by") == "operator"
          and p.get("validated_date") == "2026-09-25"
          for p in b_store.values()), f"entries = {len(b_store)}")
check("C4 batch-10 store entries reference the B10 diff-review bundle",
      all(p.get("review_reference") == BUNDLE_REF
          for p in b_store.values()))
check("C5 no REJECT/HOLD/MERGE/SPLIT verdicts left un-applied",
      all(x["verdict"] == "CONFIRM" for x in ev))
check("C6 the THIRTEEN sanctioned cross-section boundary edges are "
      "HUMAN_VALIDATED (session-64 ruling applied, not re-minted)",
      all(any(triple(e) == t and e["validation_status"] == "HUMAN_VALIDATED"
              for e in sem)
          for t in BOUNDARY_EDGES_EXISTING))
check("C7 boundary ownership exact: ALL THIRTEEN boundary edges target "
      "EXISTING owners ABSENT from the batch-10 mint (the batch-9 owners "
      "CON-HOMOLOGOUS-SERIES x2, CON-ORGANIC-FORMULAE x2, CON-HYDROCARBON, "
      "CON-ALKANES, CON-ORGANIC-REACTION-CLASSES, CON-IUPAC-NAMING, "
      "CON-CRACKING; batch-5 CON-COMBUSTION-O2; batch-6 CON-OX-RED-AGENTS; "
      "batch-1 CON-FRACTIONAL-DISTILLATION; batch-7 CON-ACID-REACTIONS)",
      all(t.split()[2] not in {c["code"] for c in dec["nodes"]}
          for t in BOUNDARY_EDGES_EXISTING)
      and {t.split()[2] for t in BOUNDARY_EDGES_EXISTING}
      == {"4CH1-CON-HOMOLOGOUS-SERIES", "4CH1-CON-ORGANIC-FORMULAE",
          "4CH1-CON-HYDROCARBON", "4CH1-CON-ALKANES",
          "4CH1-CON-ORGANIC-REACTION-CLASSES", "4CH1-CON-IUPAC-NAMING",
          "4CH1-CON-CRACKING", "4CH1-CON-COMBUSTION-O2",
          "4CH1-CON-OX-RED-AGENTS", "4CH1-CON-FRACTIONAL-DISTILLATION",
          "4CH1-CON-ACID-REACTIONS"})

# ---------------------------------------------------------------------------
# D. invariants (pilot + batch-1..9 slices, store total, negative control,
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
# session-65 re-anchor (2026-09-25, dated; protective intent unchanged):
# the batch-10 verdicts were APPLIED through §18 (19 promotions,
# operator) — the 19 batch-10 authored edges left the SUGGESTED surface,
# so the live SUGGESTED semantic surface is again EXACTLY the 3 frozen
# pilot operator HOLDs (the pre-session-64 authoring state). The
# batch-9 AND batch-10 authored sets are fully HUMAN_VALIDATED. No test
# weakened.
check("D2 the 3 pilot operator HOLDs stay SUGGESTED (un-promoted) and the "
      "live SUGGESTED semantic surface is EXACTLY the pilot HOLDs (the "
      "batch-9 authored edges were promoted at session 63 and the "
      "batch-10 authored edges were promoted by the operator's verdicts "
      "through §18 at session 65)",
      pilot_holds <= live_sugg and not (pilot_holds & hv)
      and live_sugg == pilot_holds
      and {triple(e) for e in b9_dec["edges"]} <= hv
      and b_triples <= hv,
      f"live SUGGESTED = {len(live_sugg)}")
pilot_rr = [e for e in sem if triple(e) == PILOT_RR_TRIPLE]
check("D3 the pilot RR edge stays REVIEW_REQUIRED (operator HOLD)",
      len(pilot_rr) == 1
      and pilot_rr[0]["validation_status"] == "REVIEW_REQUIRED")
# batch-1..9 slices
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
b2_triples = {triple(e) for e in b2_dec["edges"]}
b2_hv = {t for t in hv if t in b2_triples}
b2_confirms = {x["triple"] for x in b2_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D6 batch-2 slice intact: 23 batch-2 CONFIRM still HUMAN_VALIDATED",
      b2_hv == b2_confirms and len(b2_hv) == 23)
b3_triples = {triple(e) for e in b3_dec["edges"]}
b3_hv = {t for t in hv if t in b3_triples}
b3_confirms = {x["triple"] for x in b3_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D7 batch-3 slice intact: 39 batch-3 CONFIRM still HUMAN_VALIDATED",
      b3_hv == b3_confirms and len(b3_hv) == 39)
b4_triples = {triple(e) for e in b4_dec["edges"]}
b4_hv = {t for t in hv if t in b4_triples}
b4_confirms = {x["triple"] for x in b4_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D8 batch-4 slice intact: 35 batch-4 CONFIRM still HUMAN_VALIDATED",
      b4_hv == b4_confirms and len(b4_hv) == 35)
b5_triples = {triple(e) for e in b5_dec["edges"]}
b5_hv = {t for t in hv if t in b5_triples}
b5_confirms = {x["triple"] for x in b5_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D9 batch-5 slice intact: 18 batch-5 CONFIRM still HUMAN_VALIDATED",
      b5_hv == b5_confirms and len(b5_hv) == 18)
b6_triples = {triple(e) for e in b6_dec["edges"]}
b6_hv = {t for t in hv if t in b6_triples}
b6_confirms = {x["triple"] for x in b6_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D10 batch-6 slice intact: 16 batch-6 CONFIRM still HUMAN_VALIDATED",
      b6_hv == b6_confirms and len(b6_hv) == 16)
b7_triples = {triple(e) for e in b7_dec["edges"]}
b7_hv = {t for t in hv if t in b7_triples}
b7_confirms = {x["triple"] for x in b7_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D11 batch-7 slice intact: 19 batch-7 CONFIRM still HUMAN_VALIDATED",
      b7_hv == b7_confirms and len(b7_hv) == 19)
b8_triples = {triple(e) for e in b8_dec["edges"]}
b8_hv = {t for t in hv if t in b8_triples}
b8_confirms = {x["triple"] for x in b8_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D12 batch-8 slice intact: 10 batch-8 CONFIRM still HUMAN_VALIDATED",
      b8_hv == b8_confirms and len(b8_hv) == 10)
b9_triples = {triple(e) for e in b9_dec["edges"]}
b9_hv = {t for t in hv if t in b9_triples}
b9_confirms = {x["triple"] for x in b9_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D13 batch-9 slice intact: 20 batch-9 CONFIRM still HUMAN_VALIDATED",
      b9_hv == b9_confirms and len(b9_hv) == 20)
check("D14 store total 255 (28+28+23+39+35+18+16+19+10+20+19), all "
      "operator",
      len(store_map) == 255
      and all(p.get("validated_by") == "operator"
              for p in store_map.values()))
n415 = [x for x in nodes_doc["nodes"]
        if any(sp.get("code") == "4CH1-4.15"
               for sp in x.get("spec_points", []))]
e415 = [e for e in edges_doc["edges"]
        if any("4.15" in a.get("file", "") for a in e.get("evidence", []))]
check("D15 negative control 4CH1-4.15: zero node/edge attachments",
      len(n415) == 0 and len(e415) == 0,
      f"nodes = {len(n415)}, edges = {len(e415)}")
check("D16 no PART_OF edge promoted through the §18 record "
      "(PART_OF HV rows exist only via the later T-C19 G19 record; the "
      "batch-6/7/8/9/10 PART_OF rows stay SUGGESTED pending their own "
      "lane)",
      not any(p.get("relation") == "PART_OF"
              for p in (promo.get("promotions") or []))
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF"
              and e["validation_status"] == "HUMAN_VALIDATED") == 117
      and all(e["validation_status"] == "SUGGESTED"
              for e in edges_doc["edges"]
              if e["relation"] == "PART_OF"
              and e["validation_status"] != "HUMAN_VALIDATED"))
check("D17 no batch-10 node is HUMAN_VALIDATED (nodes have no §18 "
      "pathway; the §6 confirmations do not promote nodes — 'Authority "
      "remains SUGGESTED')",
      not any(x.get("validation_status") == "HUMAN_VALIDATED"
              for x in nodes_doc["nodes"]))
check("D18 live store shape 188 nodes / 459 edges (199 PART_OF + 260 "
      "semantic) — verdicts move statuses only, never shape",
      len(nodes_doc["nodes"]) == 188 and len(edges_doc["edges"]) == 459
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF") == 199)
# boundary mint discipline (the session-64 cross-slice ruling)
non_mint = set(rul["boundary_edge_ruling"]["non_mint_list"])
b10_codes = {c["code"] for c in dec["nodes"]}
check("D19 zero ruled non-mint owner re-minted in the batch-10 node set "
      "(the ruling's non_mint_list codes absent from the mint)",
      len(non_mint) == 48 and not (b10_codes & non_mint),
      f"non_mint = {len(non_mint)}, collision = "
      f"{sorted(b10_codes & non_mint)}")
# the sanctioned boundary targets exist exactly once in the live store
# (no duplicate mint by the boundary edges' application)
for t in BOUNDARY_EDGES_EXISTING:
    hits = [e for e in edges_doc["edges"] if triple(e) == t]
    check(f"D20 boundary target authored exactly once: {t}",
          len(hits) == 1 and hits[0]["validation_status"] == "HUMAN_VALIDATED")
# the 9 held candidates were never authored FROM the held record -> the
# held surface contributes nothing to the store. ONE documented triple
# coincidence exists: B10-H-04's candidate (CARBOXYLIC-ACIDS RP
# ORGANIC-FORMULAE) equals the sanctioned boundary edge B10-E-18 (the
# session-64 ruling's TARGET-2 second edge, the batch-5 x2 precedent;
# TARGET-2's for_sps explicitly includes 4CH1-4.35C). The gate sheet
# presents BOTH surfaces (§3 row 18 + §4 H-04) and the operator ruled on
# both: E-18 CONFIRM (§6.2) and H-04 KEEP HELD — 'existing formula
# boundary owner already available' (§6.3). The store contains the
# AUTHORED edge (promoted via the E-18 CONFIRM verdict), never a
# held-record promotion.
import re as _re
held_triples = set()
for h in dec["held"]:
    m = _re.match(r"(\w+)\(([^,]+), ([^)]+)\)", h["candidate"])
    if m:
        rel, a, b = m.group(1), m.group(2).strip(), m.group(3).strip()
        rel_full = {"REQUIRES_PREREQUISITE": "REQUIRES_PREREQUISITE",
                    "RELATED_TO": "RELATED_TO"}[rel]
        held_triples.add(f"4CH1-{a} {rel_full} 4CH1-{b}")
store_triples = {triple(e) for e in edges_doc["edges"]}
overlap = held_triples & store_triples
h04_triple = "4CH1-CON-CARBOXYLIC-ACIDS REQUIRES_PREREQUISITE " \
             "4CH1-CON-ORGANIC-FORMULAE"
e18_row = next(x for x in ev if x["id"] == "B10-E-18")
h04 = next(h for h in dec["held"] if h["id"] == "B10-H-04")
check("D21 the 9 batch-10 held candidates stay quarantined (recorded, "
      "never authored FROM the held record; the ONE triple coincidence "
      "B10-H-04 == the sanctioned boundary edge B10-E-18 is the "
      "session-64 ruling's TARGET-2 x2 precedent — both surfaces "
      "explicitly ruled by the operator; every OTHER held triple absent "
      "from the store)",
      len(held_triples) == 9
      and overlap == {h04_triple}
      and h04_triple == e18_row["triple"]
      and e18_row["verdict"] == "CONFIRM"
      and h04_triple in BOUNDARY_EDGES_EXISTING
      and "4CH1-4.35C" in next(s["for_sps"] for s in
                               rul["boundary_edge_ruling"]["sanctioned_targets"]
                               if s["target"] ==
                               "4CH1-CON-ORGANIC-FORMULAE")
      and "KEEP HELD" in (held_ack.get("notes") or "")
      and "existing formula boundary owner already available"
      in (held_ack.get("notes") or ""),
      f"overlap = {sorted(overlap)}")

# ---------------------------------------------------------------------------
print()
if fails:
    print(f"FAILED: {len(fails)} check(s): {fails}")
    raise SystemExit(1)
print(f"c11_batch10_verdict_check: ALL PASS — batch-10 operator verdict "
      f"layer (19+8+5 rows, the completed-sheet §6/§7 verdict: PASS WITH "
      f"NOTES; zero RR authored; UNIVERSAL rulings — no WITH_NOTE this "
      f"batch; the session-65 intake record — INLINE RESTATED sheet, "
      f"detail-preserving variant, via the zai-web chat lane, the "
      f"batch-9/10 CONFORMANCE gates — + the operator's REPORTED-state "
      f"caveat) schema-valid, record-reconciled, application-reconciled "
      f"(19 §18 promotions = the CONFIRM set; no operator_decision "
      f"blocks; pilot + batch-1..9 slices intact; 255 store entries "
      f"total; the THIRTEEN boundary targets applied with exact "
      f"ownership — all existing owners (the batch-9 owners x7 distinct "
      f"targets, batch-5 CON-COMBUSTION-O2, batch-6 CON-OX-RED-AGENTS, "
      f"batch-1 CON-FRACTIONAL-DISTILLATION, batch-7 CON-ACID-REACTIONS), "
      f"zero re-mint; 48 non-mint owners respected; the 9 held "
      f"candidates quarantined with per-candidate dispositions).")
