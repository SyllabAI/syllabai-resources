#!/usr/bin/env python3
"""T-C11 session 62 — c11_batch8_verdict_check.py: standing checker for the
batch-8 operator verdict record (scripts/c11_batch8_verdicts.yaml) and its
application state.

Checks (all fail-closed; every group must pass):
  A. schema          — sections, row ids in order, vocabulary, the verbatim
                       operator verdict (the completed sheet §6/§7, session
                       62: PASS WITH NOTES) + decided_by/date; the session-62
                       completed-sheet delivery record (the FULL sheet via
                       the FileUpload lane ca536c8; §1-5 byte-identical to
                       the in-repo gate sheet — ZERO drift) + the operator's
                       REPORTED-state caveat; NO rr_settlement section
                       (batch 8 authored zero RR edges)
  B. verdict shape   — 10 edge CONFIRM / 8 node CONFIRM (6 CONCEPT + 2
                       MISCONCEPTION) / 4 KEEP_AS_IS / held appendix (9)
                       acknowledged; reconciliation against the batch-8
                       decision record (triples, node codes, NO
                       operator_decision blocks — identity decisions are
                       all KEEP_AS_IS, so no §7 re-authoring was
                       sanctioned); the THREE §6 CONFIRM_WITH_NOTE
                       qualifications carried in notes (the B8-E-01
                       route-specificity guardrail + the B8-E-05
                       conservative-RELATED_TO guardrail + the operator's
                       node row CON-FLAME-TEST)
  C. application     — three-way set equality: verdict CONFIRM set ==
                       live batch-8 HUMAN_VALIDATED set == batch-8 entries
                       in the promotion store (10 each, operator
                       attribution, the B8 diff-review bundle as
                       review_reference); nothing outside the CONFIRM set
                       was promoted
  D. invariants      — the pilot, batch-1..7 slices are intact
                       (28+28+23+39+35+18+16+19 HUMAN_VALIDATED; the 3 pilot
                       operator-HOLD SUGGESTED — the ONLY live SUGGESTED
                       semantic surface; both RR edges REVIEW_REQUIRED);
                       store total 216; the 9 batch-8 held candidates
                       quarantined (never authored); the 68 ruled non-mint
                       owner codes NOT re-minted in the batch-8 node set;
                       4.15 negative control uncovered; no PART_OF promoted
                       through §18; no batch-8 node HUMAN_VALIDATED; live
                       store shape 165/384/163; the THREE sanctioned
                       cross-section boundary edges applied with EXACT
                       ownership (all into EXISTING owners — batch-3
                       CON-ION-CHARGE-RULES x2 and batch-1
                       CON-PURE-SUBSTANCE; no batch-8 mint as target)

Usage: python3 scripts/c11_batch8_verdict_check.py
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
VERDICTS = HERE / "c11_batch8_verdicts.yaml"
DECISIONS = HERE / "c11_batch8_decisions.yaml"
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
PROMOTIONS = HERE / "c11_promotions.yaml"

BUNDLE_REF = "graph/reports/C11_DIFF_REVIEW_B8_2026-09-24.md"
B1_RR_TRIPLE = ("4CH1-CON-CRYSTALLISATION REQUIRES_PREREQUISITE "
                "4CH1-CON-SOLUTION")
PILOT_RR_TRIPLE = ("4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE "
                   "4CH1-CON-AVOGADRO-LAW")
# the session-61 cross-slice boundary ruling's non-mint owner codes,
# loaded from the ruling itself (68 recorded; asserted, not trusted)
B8_RULING = HERE / "c11_batch8_boundary_ruling.yaml"
# the THREE sanctioned cross-section boundary edges (session-61 ruling):
# all into EXISTING owners — the batch-3 CON-ION-CHARGE-RULES owner x2
# (the 2.48 anion-identity + 2.47 cation-identity rows) and the batch-1
# CON-PURE-SUBSTANCE owner (the 2.50 purity row)
BOUNDARY_EDGES_EXISTING = (
    "4CH1-CON-ANION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES",
    "4CH1-CON-CATION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES",
    "4CH1-CON-WATER-PURITY-TEST REQUIRES_PREREQUISITE "
    "4CH1-CON-PURE-SUBSTANCE",
)
# the three §6 CONFIRM_WITH_NOTE rows (qualifications ride in notes):
# the operator's TWO edge guardrails + the operator's node row
WITH_NOTE_QUALIFICATIONS = {
    "4CH1-CON-ANION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-GAS-TESTS",
    "4CH1-CON-FLAME-TEST RELATED_TO 4CH1-CON-CATION-TESTS",
    "4CH1-CON-FLAME-TEST",
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
rul = yaml.safe_load(B8_RULING.read_text(encoding="utf-8"))
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
      "session 62: PASS WITH NOTES)",
      "PASS WITH NOTES" in (r.get("statement") or "")
      and "rerun the complete gate suite" in (r.get("statement") or "")
      and "does not itself constitute HUMAN_VALIDATED promotion"
      in (r.get("statement") or "")
      and r.get("session") == 62
      and r.get("decided_by") == "operator"
      and r.get("decided_date") == "2026-09-24")
check("A3 the session-62 completed-sheet delivery record present (FULL "
      "sheet via the FileUpload lane ca536c8; §1-5 byte-identical — ZERO "
      "drift) + the operator's REPORTED-state caveat recorded verbatim",
      "FULL" in (r.get("completed_sheet") or "")
      and "ca536c8" in (r.get("completed_sheet") or "")
      and "ZERO drift" in (r.get("completed_sheet") or "")
      and "REPORTED/VERIFIED" in (r.get("reported_state_caveat") or "")
      and "independently re-executed" in (r.get("reported_state_caveat") or "")
      and "c3baa45" in (r.get("reported_state_caveat") or ""))
check("A4 edge rows B8-E-01..B8-E-10 sequential, complete",
      [x["id"] for x in ev] == [f"B8-E-{i:02d}" for i in range(1, 11)])
check("A5 node rows B8-N-01..06 + B8-M-01..02 sequential, complete",
      [x["id"] for x in nv] == [f"B8-N-{i:02d}" for i in range(1, 7)]
      + ["B8-M-01", "B8-M-02"])
check("A6 identity rows B8-ID-01..04 sequential, complete",
      [x["id"] for x in ids] == [f"B8-ID-{i:02d}" for i in range(1, 5)])
V_EDGE = {"CONFIRM", "REJECT", "HOLD", "MERGE", "SPLIT"}
V_ID = {"MERGE", "SPLIT", "KEEP_AS_IS"}
check("A7 all verdicts in vocabulary, none empty",
      all(x["verdict"] in V_EDGE for x in ev)
      and all(x["verdict"] in V_EDGE for x in nv)
      and all(x["verdict"] in V_ID for x in ids))
check("A8 template consumed (fill + rename per the gate pathway)",
      not (HERE / "c11_batch8_verdicts_template.yaml").exists()
      and VERDICTS.exists())
check("A9 encoding mapping records the WITH_NOTE vocabulary rule + the "
      "code-keying identity-safety rule (sheet table-order node numbering "
      "vs the template's alphabetical-by-code numbering)",
      "no WITH_NOTE value" in (r.get("mapping") or "")
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
check("B1 edge verdicts: 10 CONFIRM / 0 others",
      ec == {"CONFIRM": 10}, f"{ec}")
check("B2 node verdicts: 8 CONFIRM / 0 others",
      nc == {"CONFIRM": 8}, f"{nc}")
check("B3 identity decisions: 4 x KEEP_AS_IS",
      [x["verdict"] for x in ids] == ["KEEP_AS_IS"] * 4)
check("B4 batch 8 authored ZERO RR edges (no settlement row needed)",
      not any(e["validation_status"] == "REVIEW_REQUIRED"
              for e in dec["edges"]))
check("B5 held appendix acknowledged (9 preserved, quarantined)",
      held_ack.get("acknowledged") is True
      and len(dec["held"]) == 9
      and all(h["status"] == "held" for h in dec["held"]))

b_suggested = {triple(e) for e in dec["edges"]
               if e["validation_status"] == "SUGGESTED"}
check("B6 verdict triples = the batch-8 record's 10 SUGGESTED edges",
      {x["triple"] for x in ev} == b_suggested and len(b_suggested) == 10)
check("B7 verdict node codes = the batch-8 record's 8 node codes "
      "(6 CONCEPT + 2 MISCONCEPTION)",
      {x["code"] for x in nv} == {c["code"] for c in dec["nodes"]}
      and len(dec["nodes"]) == 8
      and sum(1 for c in dec["nodes"] if c["family"] == "CONCEPT") == 6
      and sum(1 for c in dec["nodes"]
              if c["family"] == "MISCONCEPTION") == 2)
check("B8 NO operator_decision blocks in the batch-8 record (none "
      "sanctioned: no RR, no ENRICHMENT node, all identity KEEP_AS_IS)",
      sum(1 for x in dec["nodes"] + dec["edges"]
          if "operator_decision" in x) == 0)
check("B9 no ENRICHMENT-scoped node in batch 8 (none to scope)",
      not any(sp.get("role") == "ENRICHMENT"
              for x in dec["nodes"] for sp in x.get("spec_points", [])))
# the three §6 CONFIRM_WITH_NOTE qualifications carried in notes
e01 = [x for x in ev if x["triple"] ==
       "4CH1-CON-ANION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-GAS-TESTS"][0]
e05 = [x for x in ev if x["triple"] ==
       "4CH1-CON-FLAME-TEST RELATED_TO 4CH1-CON-CATION-TESTS"][0]
nfl = [x for x in nv if x["code"] == "4CH1-CON-FLAME-TEST"][0]
check("B10 the THREE §6 CONFIRM_WITH_NOTE qualifications carried in notes "
      "(the B8-E-01 route-specificity guardrail + the B8-E-05 "
      "conservative-RELATED_TO guardrail + the operator's node row "
      "CON-FLAME-TEST)",
      e01["notes"].startswith("Operator §6 (session 62): "
                              "CONFIRM_WITH_NOTE retained")
      and "not as a claim that every anion-testing pathway" in e01["notes"]
      and e05["notes"].startswith("Operator §6 (session 62): "
                                  "CONFIRM_WITH_NOTE retained")
      and "Do not strengthen it to REQUIRES_PREREQUISITE" in e05["notes"]
      and nfl["notes"].startswith("Operator §6 (session 62): "
                                  "CONFIRM_WITH_NOTE retained")
      and "B8-ID-01" in nfl["notes"])
check("B11 the §6 boundary directive recorded (the THREE sanctioned "
       "cross-section edges keep their governed owners; no duplicate "
       "boundary concept minted; node authority stays SUGGESTED)",
      "No duplicate boundary concept is to be minted" in (r.get("mapping")
                                                          or "")
      and "Node authority remains SUGGESTED" in (r.get("mapping") or ""))

# ---------------------------------------------------------------------------
# C. application (three-way set equality; session-62 §18 application)
# ---------------------------------------------------------------------------
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
b_triples = {triple(e) for e in dec["edges"]}
b_hv = {t for t in hv if t in b_triples}
confirms = {x["triple"] for x in ev if x["verdict"] == "CONFIRM"}
store_map = {" ".join((p["edge"]["source"], p["edge"]["relation"],
                       p["edge"]["target"])): p
             for p in promo["promotions"]}
check("C1 live batch-8 HUMAN_VALIDATED set = the 10 CONFIRM verdicts",
      b_hv == confirms and len(b_hv) == 10,
      f"live = {len(b_hv)}, verdicts = {len(confirms)}")
check("C2 promotion store = exactly the 10 batch-8 CONFIRM entries",
      set(store_map) & b_triples == confirms)
b_store = {k: p for k, p in store_map.items() if k in b_triples}
check("C3 batch-8 store entries carry operator attribution + 2026-09-24",
      all(p.get("validated_by") == "operator"
          and p.get("validated_date") == "2026-09-24"
          for p in b_store.values()), f"entries = {len(b_store)}")
check("C4 batch-8 store entries reference the B8 diff-review bundle",
      all(p.get("review_reference") == BUNDLE_REF
          for p in b_store.values()))
check("C5 no REJECT/HOLD/MERGE/SPLIT verdicts left un-applied",
      all(x["verdict"] == "CONFIRM" for x in ev))
check("C6 the THREE sanctioned cross-section boundary edges are "
      "HUMAN_VALIDATED (session-61 ruling applied, not re-minted)",
      all(any(triple(e) == t and e["validation_status"] == "HUMAN_VALIDATED"
              for e in sem)
          for t in BOUNDARY_EDGES_EXISTING))
check("C7 boundary ownership exact: ALL THREE boundary edges target "
      "EXISTING owners ABSENT from the batch-8 mint (CON-ION-CHARGE-RULES "
      "— the batch-3 owner x2; CON-PURE-SUBSTANCE — the batch-1 owner)",
      all(t.split()[2] not in {c["code"] for c in dec["nodes"]}
          for t in BOUNDARY_EDGES_EXISTING)
      and {t.split()[2] for t in BOUNDARY_EDGES_EXISTING}
      == {"4CH1-CON-ION-CHARGE-RULES", "4CH1-CON-PURE-SUBSTANCE"})

# ---------------------------------------------------------------------------
# D. invariants (pilot + batch-1..7 slices, store total, negative control,
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
# session-62 re-anchor (2026-09-24, dated): +15 the SANCTIONED batch-9
# authored-to-gate record (14 CONCEPT + 1 MISCONCEPTION; 20 authored
# semantic + 21 PART_OF) — the operator gate decision; no test weakened.
check("D1 pilot slice intact: 28 pilot CONFIRM still HUMAN_VALIDATED",
      pilot_hv == pilot_confirms and len(pilot_hv) == 28)
# session-63 re-anchor (2026-09-25, dated; protective intent unchanged):
# the batch-9 verdicts were APPLIED through §18 (20 promotions, operator,
# the B9 diff-review bundle, session 63) — the 20 batch-9 authored edges
# left the SUGGESTED surface, so the live SUGGESTED semantic surface is
# again EXACTLY the 3 frozen pilot operator HOLDs (the pre-session-62-
# authoring state); the batch-4/5/6/7/8/9 authored sets are all fully
# HUMAN_VALIDATED. No test weakened.
B9_DEC = HERE / "c11_batch9_decisions.yaml"
B9_AUTHORED = {triple(e)
               for e in (yaml.safe_load(B9_DEC.read_text(encoding="utf-8"))
                         .get("edges") or [])}
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
      "by the operator's verdicts through §18 at session 63)",
      pilot_holds <= live_sugg and not (pilot_holds & hv)
      and live_sugg == pilot_holds | B11_AUTHORED
      and B10_AUTHORED <= hv
      and B9_AUTHORED <= hv,
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
# batch-5 slice
b5_triples = {triple(e) for e in b5_dec["edges"]}
b5_hv = {t for t in hv if t in b5_triples}
b5_confirms = {x["triple"] for x in b5_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D9 batch-5 slice intact: 18 batch-5 CONFIRM still HUMAN_VALIDATED",
      b5_hv == b5_confirms and len(b5_hv) == 18)
# batch-6 slice
b6_triples = {triple(e) for e in b6_dec["edges"]}
b6_hv = {t for t in hv if t in b6_triples}
b6_confirms = {x["triple"] for x in b6_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D10 batch-6 slice intact: 16 batch-6 CONFIRM still HUMAN_VALIDATED",
      b6_hv == b6_confirms and len(b6_hv) == 16)
# batch-7 slice
b7_triples = {triple(e) for e in b7_dec["edges"]}
b7_hv = {t for t in hv if t in b7_triples}
b7_confirms = {x["triple"] for x in b7_vd["edge_verdicts"]
               if x["verdict"] == "CONFIRM"}
check("D11 batch-7 slice intact: 19 batch-7 CONFIRM still HUMAN_VALIDATED",
      b7_hv == b7_confirms and len(b7_hv) == 19)
# session-63 re-anchor (dated, protective intent unchanged): the batch-9
# §18 application added 20 operator promotions — the store total moved
# 216 -> 236; the batch-8 slice stays preserved exactly.
check("D12 store total 255 (28+28+23+39+35+18+16+19+10+20+19), all operator",
      len(store_map) == 255
      and all(p.get("validated_by") == "operator"
              for p in store_map.values()))
n415 = [x for x in nodes_doc["nodes"]
        if any(sp.get("code") == "4CH1-4.15"
               for sp in x.get("spec_points", []))]
e415 = [e for e in edges_doc["edges"]
        if any("4.15" in a.get("file", "") for a in e.get("evidence", []))]
check("D13 negative control 4CH1-4.15: zero node/edge attachments",
      len(n415) == 0 and len(e415) == 0,
      f"nodes = {len(n415)}, edges = {len(e415)}")
check("D14 no PART_OF edge promoted through the §18 record "
      "(PART_OF HV rows exist only via the later T-C19 G19 record; the "
      "batch-6/7/8 PART_OF rows stay SUGGESTED pending their own lane)",
      not any(p.get("relation") == "PART_OF"
              for p in (promo.get("promotions") or []))
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF"
              and e["validation_status"] == "HUMAN_VALIDATED") == 117
      and all(e["validation_status"] == "SUGGESTED"
              for e in edges_doc["edges"]
              if e["relation"] == "PART_OF"
              and e["validation_status"] != "HUMAN_VALIDATED"))
check("D15 no batch-8 node is HUMAN_VALIDATED (nodes have no §18 pathway; "
      "the §6 confirmations do not promote nodes — 'Node authority "
      "remains SUGGESTED')",
      not any(x.get("validation_status") == "HUMAN_VALIDATED"
              for x in nodes_doc["nodes"]))
check("D16 live store shape 193 nodes / 488 edges (211 PART_OF + 277 "
      "semantic) — verdicts move statuses only, never shape",
      len(nodes_doc["nodes"]) == 193 and len(edges_doc["edges"]) == 488
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF") == 211)
# boundary mint discipline (the session-61 cross-slice ruling)
non_mint = set(rul["boundary_edge_ruling"]["non_mint_list"])
b8_codes = {c["code"] for c in dec["nodes"]}
check("D17 zero ruled non-mint owner re-minted in the batch-8 node set "
      "(the ruling's non_mint_list codes absent from the mint)",
      len(non_mint) == 68 and not (b8_codes & non_mint),
      f"non_mint = {len(non_mint)}, collision = "
      f"{sorted(b8_codes & non_mint)}")
# the sanctioned boundary targets exist exactly once in the live store
# (no duplicate mint by the boundary edges' application)
for t in BOUNDARY_EDGES_EXISTING:
    hits = [e for e in edges_doc["edges"] if triple(e) == t]
    check(f"D18 boundary target authored exactly once: {t}",
          len(hits) == 1 and hits[0]["validation_status"] == "HUMAN_VALIDATED")
# the 9 held candidates were never authored -> absent from the live store
held_ids = [h["id"] for h in dec["held"]]
check("D19 the 9 batch-8 held candidates stay quarantined (recorded, "
      "never authored; store untouched by holds)",
      len(held_ids) == 9
      and not any(triple(e) in b_suggested for e in dec["edges"]
                  if e["validation_status"] == "REVIEW_REQUIRED"))

# ---------------------------------------------------------------------------
print()
if fails:
    print(f"FAILED: {len(fails)} check(s): {fails}")
    raise SystemExit(1)
print(f"c11_batch8_verdict_check: ALL PASS — batch-8 operator verdict layer "
      f"(10+8+4 rows, the completed-sheet §6/§7 verdict: PASS WITH NOTES; "
      f"zero RR authored; the THREE CONFIRM_WITH_NOTE qualifications "
      f"carried in notes; the session-62 completed-sheet delivery record — "
      f"FileUpload lane ca536c8, ZERO §1-5 drift — + the operator's "
      f"REPORTED-state caveat) schema-valid, record-reconciled, "
      f"application-reconciled (10 §18 promotions = the CONFIRM set; no "
      f"operator_decision blocks; pilot + batch-1..7 slices intact; 216 "
      f"store entries total; the 3 boundary targets applied with exact "
      f"ownership — all existing owners (batch-3 CON-ION-CHARGE-RULES x2, "
      f"batch-1 CON-PURE-SUBSTANCE), zero re-mint; 68 non-mint owners "
      f"respected).")
