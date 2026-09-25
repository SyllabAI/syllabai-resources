#!/usr/bin/env python3
"""T-C11 session 67 — c11_batch11_verdict_check.py: standing checker for the
batch-11 operator verdict record (scripts/c11_batch11_verdicts.yaml) and its
application state.

Checks (all fail-closed; every group must pass):
  A. schema          — sections, row ids in order, vocabulary, the verbatim
                       operator verdict (session 67: PASS WITH NOTES / Batch
                       11: ACCEPTED) + decided_by/date; the session-67
                       intake record (GITHUB-DIRECT sheet review + INLINE
                       operator verdict via the zai-web chat lane; the
                       batch-9/10 restatement lane does NOT apply — the
                       CONFORMANCE gate applies and passed at intake by
                       scripts/c11_batch11_intake_drift_check.py) + the
                       operator's REPORTED-state caveat (ee0524d machine
                       verification closed the gap on the operator's
                       behalf); NO rr_settlement section (batch 11 authored
                       zero RR edges)
  B. verdict shape   — 17 edge CONFIRM / 5 node CONFIRM (4 CONCEPT + 1
                       MISCONCEPTION) / 4 KEEP_AS_IS / held appendix (10)
                       acknowledged at RANGE level (no per-candidate
                       dispositions recorded, none invented);
                       reconciliation against the batch-11 decision record
                       (triples, node codes, NO operator_decision blocks —
                       identity decisions are all KEEP_AS_IS, so no §7
                       re-authoring was sanctioned); NO CONFIRM_WITH_NOTE
                       value used (the NOTES in PASS WITH NOTES are the
                       sheet-level REPORTED caveat + the scoped-RP
                       semantic guardrail + the anti-duplication
                       guardrail, carried in meta.operator_ruling); the
                       EIGHT route-dependent rows carry the SCOPED-RP
                       GUARDRAIL note (the operator's route-specific
                       interpretation invariant); the TWELVE sanctioned
                       boundary rows carry the ownership/retention note
  C. application     — three-way set equality: verdict CONFIRM set ==
                       live batch-11 HUMAN_VALIDATED set == batch-11
                       entries in the promotion store (17 each, operator
                       attribution 2026-09-25, the B11 diff-review bundle
                       as review_reference); nothing outside the CONFIRM
                       set was promoted
  D. invariants      — the pilot + batch-1..10 slices are intact
                       (28+28+23+39+35+18+16+19+10+20+19 HUMAN_VALIDATED;
                       the 3 pilot operator-HOLD SUGGESTED — the ONLY live
                       SUGGESTED semantic surface now that the batch-11
                       verdicts are applied; both RR edges
                       REVIEW_REQUIRED); store total 272, all operator;
                       the 10 batch-11 held candidates quarantined (never
                       authored — ZERO triple coincidences with the store
                       this batch: every held triple absent); the 50 ruled
                       non-mint owner codes NOT re-minted in the batch-11
                       node set; 4.15 negative control uncovered; no
                       PART_OF promoted through §18 (the batch-11 PART_OF
                       rows stay SUGGESTED pending their own lane); no
                       batch-11 node is HUMAN_VALIDATED (nodes have no §18
                       pathway; 'Authority SUGGESTED'); live store shape
                       193/488 (211 PART_OF + 277 semantic); the 12
                       boundary edges HUMAN_VALIDATED into EXACTLY their
                       TEN existing owners (ALCOHOLS x2 + CARBOXYLIC-ACIDS
                       x2 make the 12-vs-10 count intentional; no batch-11
                       mint as target)

Usage: python3 scripts/c11_batch11_verdict_check.py
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
VERDICTS = HERE / "c11_batch11_verdicts.yaml"
DECISIONS = HERE / "c11_batch11_decisions.yaml"
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
B10_VERDICTS = HERE / "c11_batch10_verdicts.yaml"
B10_DECISIONS = HERE / "c11_batch10_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"

BUNDLE_REF = "graph/reports/C11_DIFF_REVIEW_B11_2026-09-25.md"
B1_RR_TRIPLE = ("4CH1-CON-CRYSTALLISATION REQUIRES_PREREQUISITE "
                "4CH1-CON-SOLUTION")
PILOT_RR_TRIPLE = ("4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE "
                   "4CH1-CON-AVOGADRO-LAW")
# the session-66 cross-slice boundary ruling's non-mint owner codes,
# loaded from the ruling itself (50 recorded; asserted, not trusted)
B11_RULING = HERE / "c11_batch11_boundary_ruling.yaml"
# the TWELVE sanctioned cross-section boundary edges (session-66
# ruling): all into EXISTING owners — TEN distinct targets (batch-10
# CON-ALCOHOLS x2, CON-CARBOXYLIC-ACIDS x2, CON-ALKENES; batch-9
# CON-ORGANIC-FORMULAE, CON-IUPAC-NAMING, CON-ORGANIC-REACTION-CLASSES,
# CON-CO-POISONING; batch-5 CON-CO2-GREENHOUSE; batch-1
# CON-SIMPLE-DISTILLATION; batch-7 CON-ACID-REACTIONS — the two
# double-targeted owners carry the batch-5 x2 precedent)
BOUNDARY_EDGES_EXISTING = (
    "4CH1-CON-ESTERS REQUIRES_PREREQUISITE 4CH1-CON-ALCOHOLS",
    "4CH1-CON-ESTERS REQUIRES_PREREQUISITE 4CH1-CON-CARBOXYLIC-ACIDS",
    "4CH1-CON-ESTERS REQUIRES_PREREQUISITE 4CH1-CON-ORGANIC-FORMULAE",
    "4CH1-CON-ESTERS REQUIRES_PREREQUISITE 4CH1-CON-IUPAC-NAMING",
    "4CH1-PR-12 REQUIRES_PREREQUISITE 4CH1-CON-SIMPLE-DISTILLATION",
    "4CH1-PR-12 REQUIRES_PREREQUISITE 4CH1-CON-ACID-REACTIONS",
    "4CH1-CON-ADDITION-POLYMERS REQUIRES_PREREQUISITE 4CH1-CON-ALKENES",
    "4CH1-CON-ADDITION-POLYMERS REQUIRES_PREREQUISITE "
    "4CH1-CON-ORGANIC-REACTION-CLASSES",
    "4CH1-CON-POLYMER-DISPOSAL REQUIRES_PREREQUISITE "
    "4CH1-CON-CO2-GREENHOUSE",
    "4CH1-CON-POLYMER-DISPOSAL REQUIRES_PREREQUISITE "
    "4CH1-CON-CO-POISONING",
    "4CH1-CON-CONDENSATION-POLYMERS REQUIRES_PREREQUISITE "
    "4CH1-CON-CARBOXYLIC-ACIDS",
    "4CH1-CON-CONDENSATION-POLYMERS REQUIRES_PREREQUISITE "
    "4CH1-CON-ALCOHOLS",
)
BOUNDARY_OWNERS = {
    "4CH1-CON-ALCOHOLS", "4CH1-CON-CARBOXYLIC-ACIDS",
    "4CH1-CON-ORGANIC-FORMULAE", "4CH1-CON-IUPAC-NAMING",
    "4CH1-CON-SIMPLE-DISTILLATION", "4CH1-CON-ACID-REACTIONS",
    "4CH1-CON-ALKENES", "4CH1-CON-ORGANIC-REACTION-CLASSES",
    "4CH1-CON-CO2-GREENHOUSE", "4CH1-CON-CO-POISONING",
}
# the EIGHT route-dependent rows carrying the SCOPED-RP GUARDRAIL (the
# operator's four scoping groups: esterification x2, the C=C
# addition-polymer route x1, the taught incineration/combustion surface
# x2, the polyester route x3)
SCOPED_ROWS = {"B11-E-01", "B11-E-02", "B11-E-08", "B11-E-13",
               "B11-E-14", "B11-E-15", "B11-E-16", "B11-E-17"}
# the four §6 identity decisions (KEEP_AS_IS per the vocabulary rule)
# and the nodes they rule
IDENTITY_LINK = {
    "4CH1-CON-ESTERS": "B11-ID-01",
    "4CH1-CON-ADDITION-POLYMERS": "B11-ID-02",
    "4CH1-CON-CONDENSATION-POLYMERS": "B11-ID-03",
    "4CH1-MIS-POLYMER-DOUBLE-BOND": "B11-ID-04",
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
rul = yaml.safe_load(B11_RULING.read_text(encoding="utf-8"))
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
b10_vd = yaml.safe_load(B10_VERDICTS.read_text(encoding="utf-8"))
b10_dec = yaml.safe_load(B10_DECISIONS.read_text(encoding="utf-8"))
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
check("A2 operator verdict recorded verbatim (session 67: PASS WITH "
      "NOTES / Batch 11: ACCEPTED) + decided_by/date + the scoped-RP "
      "semantic guardrail + the boundary-preservation ruling + the "
      "route-specific reconciliation invariant + 'Nothing is promoted'",
      "PASS WITH NOTES" in (r.get("statement") or "")
      and "Batch 11: ACCEPTED" in (r.get("statement") or "")
      and "Nothing is promoted by this review"
      in (r.get("statement") or "")
      and "scoped teaching/route dependency"
      in (r.get("statement") or "")
      and "Ester → alcohols/carboxylic acids: scoped to esterification"
      in (r.get("statement") or "")
      and ("Addition polymers → alkenes: scoped to the C=C "
           "addition-polymer route") in (r.get("statement") or "")
      and ("Polymer disposal → CO₂/CO: scoped to the taught "
           "incineration/combustion surface") in (r.get("statement") or "")
      and ("Condensation polymers → esters/carboxylic acids/alcohols: "
           "scoped to the polyester route") in (r.get("statement") or "")
      and "Retain all 12 sanctioned cross-section edges"
      in (r.get("statement") or "")
      and "do not mint duplicates for existing owners"
      in (r.get("statement") or "")
      and ("the route-specific interpretation of the prerequisite edges")
      in (r.get("statement") or "")
      and r.get("session") == 67
      and r.get("decided_by") == "operator"
      and r.get("decided_date") == "2026-09-25")
check("A3 the session-67 intake record present (GITHUB-DIRECT sheet "
      "review + INLINE operator verdict via the zai-web chat lane; no "
      "restatement blocks claimed; the CONFORMANCE gate applies) + the "
      "operator's REPORTED-state caveat recorded verbatim (the ee0524d "
      "machine verification closed the gap on the operator's behalf)",
      "GITHUB-DIRECT" in (r.get("completed_sheet") or "").upper()
      and "zai-web" in (r.get("completed_sheet") or "")
      and "CONFORMANCE" in (r.get("completed_sheet") or "").upper()
      and "REPORTED / VERIFIED BY SUBMITTED ARTIFACT"
      in (r.get("reported_state_caveat") or "")
      and "193-node / 488-edge" in (r.get("reported_state_caveat") or "")
      and "ee0524d" in (r.get("reported_state_caveat") or ""))
check("A4 edge rows B11-E-01..B11-E-17 sequential, complete",
      [x["id"] for x in ev] == [f"B11-E-{i:02d}" for i in range(1, 18)])
check("A5 node rows B11-N-01..04 + B11-M-01 sequential, complete",
      [x["id"] for x in nv] == [f"B11-N-{i:02d}" for i in range(1, 5)]
      + ["B11-M-01"])
check("A6 identity rows B11-ID-01..04 sequential, complete",
      [x["id"] for x in ids] == [f"B11-ID-{i:02d}" for i in range(1, 5)])
V_EDGE = {"CONFIRM", "REJECT", "HOLD", "MERGE", "SPLIT"}
V_ID = {"MERGE", "SPLIT", "KEEP_AS_IS"}
check("A7 all verdicts in vocabulary, none empty",
      all(x["verdict"] in V_EDGE for x in ev)
      and all(x["verdict"] in V_EDGE for x in nv)
      and all(x["verdict"] in V_ID for x in ids))
check("A8 template consumed (fill + rename per the gate pathway)",
      not (HERE / "c11_batch11_verdicts_template.yaml").exists()
      and VERDICTS.exists())
check("A9 encoding mapping records the universal-ruling encoding + the "
      "scoped-RP guardrail encoding + the no-WITH_NOTE rule + the "
      "TRIPLE-keying identity-safety rule + the node-authority rule + "
      "the §18 application-state rule",
      "cover the entire coded surface" in (r.get("mapping") or "")
      or "universal rulings" in (r.get("mapping") or "")
      and "no WITH_NOTE value" in (r.get("mapping") or "")
      and "TRIPLE — never by row id" in (r.get("mapping") or "")
      and "node authority is NOT changed" in (r.get("mapping") or "")
      and "c11_promotions.yaml" in (r.get("mapping") or ""))

# ---------------------------------------------------------------------------
# B. verdict shape + decision-record reconciliation
# ---------------------------------------------------------------------------
ec = {}
for x in ev:
    ec[x["verdict"]] = ec.get(x["verdict"], 0) + 1
nc = {}
for x in nv:
    nc[x["verdict"]] = nc.get(x["verdict"], 0) + 1
check("B1 edge verdicts: 17 CONFIRM / 0 others",
      ec == {"CONFIRM": 17}, f"{ec}")
check("B2 node verdicts: 5 CONFIRM / 0 others",
      nc == {"CONFIRM": 5}, f"{nc}")
check("B3 identity decisions: 4 x KEEP_AS_IS (the operator's 'The four "
      "identity decisions are KEEP_AS_IS' ruling)",
      [x["verdict"] for x in ids] == ["KEEP_AS_IS"] * 4
      and all("KEEP_AS_IS" in x["notes"] for x in ids))
check("B4 batch 11 authored ZERO RR edges (no settlement row needed)",
      not any(e["validation_status"] == "REVIEW_REQUIRED"
              for e in dec["edges"]))
check("B5 held appendix acknowledged (10 preserved, quarantined at "
      "RANGE level — no per-candidate dispositions recorded, none "
      "invented; the abstention/failure-class provenance rule recorded)",
      held_ack.get("acknowledged") is True
      and len(dec["held"]) == 10
      and all(h["status"] == "held" for h in dec["held"])
      and "RANGE-level acknowledgment" in (held_ack.get("notes") or "")
      and "All ten remain quarantined" in (held_ack.get("notes") or "")
      and "No held candidate should be reopened"
      in (held_ack.get("notes") or "")
      and "none are invented" in (held_ack.get("notes") or ""))

b_suggested = {triple(e) for e in dec["edges"]
               if e["validation_status"] == "SUGGESTED"}
check("B6 verdict triples = the batch-11 record's 17 SUGGESTED edges",
      {x["triple"] for x in ev} == b_suggested and len(b_suggested) == 17)
check("B7 verdict node codes = the batch-11 record's 5 node codes "
      "(4 CONCEPT + 1 MISCONCEPTION)",
      {x["code"] for x in nv} == {c["code"] for c in dec["nodes"]}
      and len(dec["nodes"]) == 5
      and sum(1 for c in dec["nodes"] if c["family"] == "CONCEPT") == 4
      and sum(1 for c in dec["nodes"]
              if c["family"] == "MISCONCEPTION") == 1)
check("B8 NO operator_decision blocks in the batch-11 record (none "
      "sanctioned: no RR, no ENRICHMENT node, all identity KEEP_AS_IS)",
      sum(1 for x in dec["nodes"] + dec["edges"]
          if "operator_decision" in x) == 0)
check("B9 no ENRICHMENT-scoped node in batch 11 (none to scope)",
      not any(sp.get("role") == "ENRICHMENT"
              for x in dec["nodes"] for sp in x.get("spec_points", [])))
check("B10 NO WITH_NOTE value used — the operator ruled 17/17 CONFIRM "
      "with the NOTES carried at sheet level (the REPORTED caveat + the "
      "scoped-RP semantic guardrail + the anti-duplication guardrail in "
      "meta.operator_ruling)",
      all(x["verdict"] == "CONFIRM" for x in ev)
      and "no WITH_NOTE value" in (r.get("mapping") or "")
      and "scoped" in (r.get("mapping") or "")
      and "REPORTED / VERIFIED BY SUBMITTED ARTIFACT"
      in (r.get("reported_state_caveat") or ""))
# the EIGHT route-dependent rows carry the SCOPED-RP GUARDRAIL note
scoped = [x for x in ev if x["id"] in SCOPED_ROWS]
check("B11 the EIGHT route-dependent rows carry the SCOPED-RP GUARDRAIL "
      "note (REQUIRES_PREREQUISITE is a scoped teaching/route "
      "dependency, not a universal ontological prerequisite; the "
      "operator's route-specific interpretation invariant preserved "
      "during reconciliation)",
      len(scoped) == 8
      and all("SCOPED-RP GUARDRAIL" in x["notes"]
              and "scoped teaching/route dependency" in x["notes"]
              and "route-specific interpretation invariant"
              in x["notes"]
              for x in scoped))
# the TWELVE boundary rows carry the ownership/retention note
bnd_rows = [x for x in ev if x["triple"] in BOUNDARY_EDGES_EXISTING]
check("B12 the TWELVE sanctioned boundary rows carry the "
      "ownership/retention note (session-66 ruling targets; the "
      "operator's 'Retain all 12 sanctioned cross-section edges and do "
      "not mint duplicates for existing owners' ruling; the 12-vs-10 "
      "count explained)",
      len(bnd_rows) == 12
      and all("Sanctioned cross-section boundary edge" in x["notes"]
              and "Retain all 12 sanctioned" in x["notes"]
              and "12-vs-10" in x["notes"]
              for x in bnd_rows))
e10 = next(x for x in ev if x["id"] == "B11-E-10")
check("B13 the E-10 note carries the pinned Alkenes MS Q2(c) / Synthetic "
      "Polymers MS Q4(c) Reject record ('Any double-bonded product "
      "scores 0/2'; B11-ID-04 linkage)",
      "Any double-bonded product scores 0/2" in e10["notes"]
      and "B11-ID-04" in e10["notes"])
check("B14 the four identity-linked nodes carry their B11-ID linkage in "
      "notes (the three one-family consolidations + the misconception "
      "mint); the fifth node (CON-POLYMER-DISPOSAL — no identity "
      "decision) carries none",
      all(iid in next(x["notes"] for x in nv if x["code"] == code)
          for code, iid in IDENTITY_LINK.items())
      and sum(1 for x in nv if x["notes"] == "") == 1
      and next(x for x in nv if x["code"] == "4CH1-CON-POLYMER-DISPOSAL"))

# ---------------------------------------------------------------------------
# C. application (three-way set equality; session-67 §18 application)
# ---------------------------------------------------------------------------
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
b_triples = {triple(e) for e in dec["edges"]}
b_hv = {t for t in hv if t in b_triples}
confirms = {x["triple"] for x in ev if x["verdict"] == "CONFIRM"}
store_map = {" ".join((p["edge"]["source"], p["edge"]["relation"],
                       p["edge"]["target"])): p
             for p in promo["promotions"]}
check("C1 live batch-11 HUMAN_VALIDATED set = the 17 CONFIRM verdicts",
      b_hv == confirms and len(b_hv) == 17,
      f"live = {len(b_hv)}, verdicts = {len(confirms)}")
check("C2 promotion store = exactly the 17 batch-11 CONFIRM entries",
      set(store_map) & b_triples == confirms)
b_store = {k: p for k, p in store_map.items() if k in b_triples}
check("C3 batch-11 store entries carry operator attribution + 2026-09-25",
      all(p.get("validated_by") == "operator"
          and p.get("validated_date") == "2026-09-25"
          for p in b_store.values()), f"entries = {len(b_store)}")
check("C4 batch-11 store entries reference the B11 diff-review bundle",
      all(p.get("review_reference") == BUNDLE_REF
          for p in b_store.values()))
check("C5 no REJECT/HOLD/MERGE/SPLIT verdicts left un-applied",
      all(x["verdict"] == "CONFIRM" for x in ev))
check("C6 the TWELVE sanctioned cross-section boundary edges are "
      "HUMAN_VALIDATED (session-66 ruling applied, not re-minted)",
      all(any(triple(e) == t and e["validation_status"] == "HUMAN_VALIDATED"
              for e in sem)
          for t in BOUNDARY_EDGES_EXISTING))
check("C7 boundary ownership exact: ALL TWELVE boundary edges target "
      "EXISTING owners ABSENT from the batch-11 mint — exactly the TEN "
      "ruled owners (batch-10 CON-ALCOHOLS x2, CON-CARBOXYLIC-ACIDS x2, "
      "CON-ALKENES; batch-9 CON-ORGANIC-FORMULAE, CON-IUPAC-NAMING, "
      "CON-ORGANIC-REACTION-CLASSES, CON-CO-POISONING; batch-5 "
      "CON-CO2-GREENHOUSE; batch-1 CON-SIMPLE-DISTILLATION; batch-7 "
      "CON-ACID-REACTIONS; the 12-vs-10 count is intentional)",
      all(t.split()[2] not in {c["code"] for c in dec["nodes"]}
          for t in BOUNDARY_EDGES_EXISTING)
      and {t.split()[2] for t in BOUNDARY_EDGES_EXISTING}
      == BOUNDARY_OWNERS
      and len(BOUNDARY_OWNERS) == 10)

# ---------------------------------------------------------------------------
# D. invariants (pilot + batch-1..10 slices, store total, negative control,
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
check("D2 the 3 pilot operator HOLDs stay SUGGESTED (un-promoted) and "
      "the live SUGGESTED semantic surface is EXACTLY the pilot HOLDs "
      "(the batch-10 authored edges were promoted through §18 at "
      "session 65 and the batch-11 authored edges were promoted by the "
      "operator's verdicts through §18 at session 67 — the batch-11 "
      "gate residue is gone)",
      pilot_holds <= live_sugg and not (pilot_holds & hv)
      and live_sugg == pilot_holds
      and {triple(e) for e in b9_dec["edges"]} <= hv
      and {triple(e) for e in b10_dec["edges"]} <= hv
      and b_triples <= hv,
      f"live SUGGESTED = {len(live_sugg)}")
pilot_rr = [e for e in sem if triple(e) == PILOT_RR_TRIPLE]
check("D3 the pilot RR edge stays REVIEW_REQUIRED (operator HOLD)",
      len(pilot_rr) == 1
      and pilot_rr[0]["validation_status"] == "REVIEW_REQUIRED")
# batch-1..10 slices
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
b10_triples = {triple(e) for e in b10_dec["edges"]}
b10_hv = {t for t in hv if t in b10_triples}
b10_confirms = {x["triple"] for x in b10_vd["edge_verdicts"]
                if x["verdict"] == "CONFIRM"}
check("D14 batch-10 slice intact: 19 batch-10 CONFIRM still "
      "HUMAN_VALIDATED",
      b10_hv == b10_confirms and len(b10_hv) == 19)
check("D15 store total 272 (28+28+23+39+35+18+16+19+10+20+19+17), all "
      "operator",
      len(store_map) == 272
      and all(p.get("validated_by") == "operator"
              for p in store_map.values()))
n415 = [x for x in nodes_doc["nodes"]
        if any(sp.get("code") == "4CH1-4.15"
               for sp in x.get("spec_points", []))]
e415 = [e for e in edges_doc["edges"]
        if any("4.15" in a.get("file", "") for a in e.get("evidence", []))]
check("D16 negative control 4CH1-4.15: zero node/edge attachments",
      len(n415) == 0 and len(e415) == 0,
      f"nodes = {len(n415)}, edges = {len(e415)}")
check("D17 no PART_OF edge promoted through the §18 record "
      "(PART_OF HV rows exist only via the later T-C19 G19 record; the "
      "batch-11 PART_OF rows stay SUGGESTED pending their own lane)",
      not any(p.get("relation") == "PART_OF"
              for p in (promo.get("promotions") or []))
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF"
              and e["validation_status"] == "HUMAN_VALIDATED") == 117
      and all(e["validation_status"] == "SUGGESTED"
              for e in edges_doc["edges"]
              if e["relation"] == "PART_OF"
              and e["validation_status"] != "HUMAN_VALIDATED"))
check("D18 no batch-11 node is HUMAN_VALIDATED (nodes have no §18 "
      "pathway; the §6 confirmations do not promote nodes — 'Authority "
      "SUGGESTED')",
      not any(x.get("validation_status") == "HUMAN_VALIDATED"
              for x in nodes_doc["nodes"]))
check("D19 live store shape 193 nodes / 488 edges (211 PART_OF + 277 "
      "semantic) — verdicts move statuses only, never shape",
      len(nodes_doc["nodes"]) == 193 and len(edges_doc["edges"]) == 488
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF") == 211)
# boundary mint discipline (the session-66 cross-slice ruling)
non_mint = set(rul["boundary_edge_ruling"]["non_mint_list"])
b11_codes = {c["code"] for c in dec["nodes"]}
check("D20 zero ruled non-mint owner re-minted in the batch-11 node set "
      "(the ruling's non_mint_list codes absent from the mint)",
      len(non_mint) == 50 and not (b11_codes & non_mint),
      f"non_mint = {len(non_mint)}, collision = "
      f"{sorted(b11_codes & non_mint)}")
# the sanctioned boundary targets exist exactly once in the live store
# (no duplicate mint by the boundary edges' application)
for t in BOUNDARY_EDGES_EXISTING:
    hits = [e for e in edges_doc["edges"] if triple(e) == t]
    check(f"D21 boundary target authored exactly once: {t}",
          len(hits) == 1 and hits[0]["validation_status"] == "HUMAN_VALIDATED")
# the 10 held candidates were never authored FROM the held record -> the
# held surface contributes nothing to the store. ZERO triple
# coincidences this batch (cleaner than the batch-10 B10-H-04 == B10-E-18
# single-coincidence case): every held triple is absent from the store,
# the boundary-preservation ruling's BOUNDARY-TARGETS-ONCE held rows
# name targets whose edges exist but at DIFFERENT triples than the held
# candidates.
import re as _re
held_triples = set()
for h in dec["held"]:
    m = _re.match(r"(\w+)\(([^,]+), ([^)]+)\)", h["candidate"])
    if m:
        rel, a, b = m.group(1), m.group(2).strip(), m.group(3).strip()
        held_triples.add(f"4CH1-{a} {rel} 4CH1-{b}")
store_triples = {triple(e) for e in edges_doc["edges"]}
overlap = held_triples & store_triples
check("D22 the 10 batch-11 held candidates stay quarantined (recorded, "
      "never authored; ZERO held-triple overlaps with the store — every "
      "held triple absent; the abstention/failure-class provenance "
      "preserved)",
      len(held_triples) == 10 and overlap == set(),
      f"overlap = {sorted(overlap)}")

# ---------------------------------------------------------------------------
print()
if fails:
    print(f"FAILED: {len(fails)} check(s): {fails}")
    raise SystemExit(1)
print(f"c11_batch11_verdict_check: ALL PASS — batch-11 operator verdict "
      f"layer (17+5+4 rows, the session-67 operator verdict: PASS WITH "
      f"NOTES / Batch 11: ACCEPTED; zero RR authored; UNIVERSAL rulings "
      f"with the SCOPED-RP semantic guardrail on the EIGHT route-"
      f"dependent rows; the session-67 intake record — GITHUB-DIRECT "
      f"sheet review + INLINE operator verdict via the zai-web chat "
      f"lane, the CONFORMANCE gate — + the operator's REPORTED-state "
      f"caveat with the ee0524d machine verification) schema-valid, "
      f"record-reconciled, application-reconciled (17 §18 promotions = "
      f"the CONFIRM set; no operator_decision blocks; pilot + "
      f"batch-1..10 slices intact; 272 store entries total; the TWELVE "
      f"boundary targets applied with exact ownership — all existing "
      f"owners, TEN distinct (ALCOHOLS x2 + CARBOXYLIC-ACIDS x2 make "
      f"the 12-vs-10 count intentional), zero re-mint; 50 non-mint "
      f"owners respected; the 10 held candidates quarantined at RANGE "
      f"level with zero store overlaps).")
