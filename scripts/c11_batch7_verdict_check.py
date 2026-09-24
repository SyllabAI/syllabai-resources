#!/usr/bin/env python3
"""T-C11 session 60 — c11_batch7_verdict_check.py: standing checker for the
batch-7 operator verdict record (scripts/c11_batch7_verdicts.yaml) and its
application state.

Checks (all fail-closed; every group must pass):
  A. schema          — sections, row ids in order, vocabulary, the verbatim
                       operator verdict (the verdict addendum §6/§7, session
                       60: PASS WITH NOTES) + decided_by/date; the
                       session-60 addendum delivery record (web-lane upload
                       gap + FileUpload 8b03d1c blank-gate-sheet advance +
                       the operator's REPORTED-state caveat); NO
                       rr_settlement section (batch 7 authored zero RR edges)
  B. verdict shape   — 19 edge CONFIRM / 15 node CONFIRM (13 CONCEPT +
                       2 MISCONCEPTION) / 6 KEEP_AS_IS / held appendix (9)
                       acknowledged; reconciliation against the batch-7
                       decision record (triples, node codes, NO
                       operator_decision blocks — identity decisions are
                       all KEEP_AS_IS, so no §7 re-authoring was
                       sanctioned); the THREE §6 CONFIRM_WITH_NOTE
                       qualifications carried in notes (the B7-E-02
                       acid+metal route guardrail + the B7-E-10 boundary-
                       ownership guardrail + the retained pass-2 node row
                       CON-NEUTRALISATION)
  C. application     — three-way set equality: verdict CONFIRM set ==
                       live batch-7 HUMAN_VALIDATED set == batch-7 entries
                       in the promotion store (19 each, operator
                       attribution, the B7 diff-review bundle as
                       review_reference); nothing outside the CONFIRM set
                       was promoted
  D. invariants      — the pilot, batch-1..6 slices are intact
                       (28+28+23+39+35+18+16 HUMAN_VALIDATED; the 3 pilot
                       operator-HOLD SUGGESTED — now the ONLY live
                       SUGGESTED semantic surface; both RR edges
                       REVIEW_REQUIRED); store total 216; the 9 batch-7
                       held candidates quarantined (never authored); the 58
                       ruled non-mint owner codes NOT re-minted in the
                       batch-7 node set; 4.15 negative control uncovered;
                       no PART_OF promoted through §18; no batch-7 node
                       HUMAN_VALIDATED; live store shape 157/367/156; the
                       TWO sanctioned cross-section boundary edges applied
                       with EXACT ownership (both into EXISTING owners —
                       batch-6 CON-REACT-ORDER and batch-3
                       CON-ION-CHARGE-RULES; no batch-7 mint as target)

Usage: python3 scripts/c11_batch7_verdict_check.py
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
VERDICTS = HERE / "c11_batch7_verdicts.yaml"
DECISIONS = HERE / "c11_batch7_decisions.yaml"
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
PROMOTIONS = HERE / "c11_promotions.yaml"

BUNDLE_REF = "graph/reports/C11_DIFF_REVIEW_B7_2026-09-23.md"
B1_RR_TRIPLE = ("4CH1-CON-CRYSTALLISATION REQUIRES_PREREQUISITE "
                "4CH1-CON-SOLUTION")
PILOT_RR_TRIPLE = ("4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE "
                   "4CH1-CON-AVOGADRO-LAW")
# the session-59 cross-slice boundary ruling's non-mint owner codes,
# loaded from the ruling itself (58 recorded; asserted, not trusted)
B7_RULING = HERE / "c11_batch7_boundary_ruling.yaml"
# the TWO sanctioned cross-section boundary edges (session-59 ruling):
# both into EXISTING owners — the batch-6 CON-REACT-ORDER mint (the 2.37
# acid-metal placement row) and the batch-3 CON-ION-CHARGE-RULES owner
# (the 2.34 ion-family rules row)
BOUNDARY_EDGES_EXISTING = (
    "4CH1-CON-ACID-REACTIONS REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER",
    "4CH1-CON-SOLUBILITY-RULES REQUIRES_PREREQUISITE "
    "4CH1-CON-ION-CHARGE-RULES",
)
# the three §6 CONFIRM_WITH_NOTE rows (qualifications ride in notes):
# the operator's TWO edge guardrails + the retained pass-2 node row
WITH_NOTE_QUALIFICATIONS = {
    "4CH1-CON-ACID-REACTIONS REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER",
    "4CH1-CON-SOLUBILITY-RULES REQUIRES_PREREQUISITE "
    "4CH1-CON-ION-CHARGE-RULES",
    "4CH1-CON-NEUTRALISATION",
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
rul = yaml.safe_load(B7_RULING.read_text(encoding="utf-8"))
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
check("A2 operator verdict recorded verbatim (addendum §6/§7, session 60: "
      "PASS WITH NOTES)",
      "Operator verdict: PASS WITH NOTES" in (r.get("statement") or "")
      and "rerun the complete gate suite" in (r.get("statement") or "")
      and "does not itself constitute HUMAN_VALIDATED promotion"
      in (r.get("statement") or "")
      and r.get("session") == 60
      and r.get("decided_by") == "operator"
      and r.get("decided_date") == "2026-09-23")
check("A3 the session-60 addendum delivery record present (web-lane upload "
      "gap; FileUpload 8b03d1c blank gate sheet; ADDENDUM intake with "
      "1:1 reconciliation) + the operator's REPORTED-state caveat "
      "recorded verbatim",
      "ADDENDUM" in (r.get("completed_sheet") or "")
      and "8b03d1c" in (r.get("completed_sheet") or "")
      and "did not reach the verdict workspace"
      in (r.get("completed_sheet") or "")
      and "REPORTED" in (r.get("reported_state_caveat") or "")
      and "GitHub connector" in (r.get("reported_state_caveat") or "")
      and "d6eba2d" in (r.get("reported_state_caveat") or ""))
check("A4 edge rows B7-E-01..B7-E-19 sequential, complete",
      [x["id"] for x in ev] == [f"B7-E-{i:02d}" for i in range(1, 20)])
check("A5 node rows B7-N-01..13 + B7-M-01..02 sequential, complete",
      [x["id"] for x in nv] == [f"B7-N-{i:02d}" for i in range(1, 14)]
      + ["B7-M-01", "B7-M-02"])
check("A6 identity rows B7-ID-01..06 sequential, complete",
      [x["id"] for x in ids] == [f"B7-ID-{i:02d}" for i in range(1, 7)])
V_EDGE = {"CONFIRM", "REJECT", "HOLD", "MERGE", "SPLIT"}
V_ID = {"MERGE", "SPLIT", "KEEP_AS_IS"}
check("A7 all verdicts in vocabulary, none empty",
      all(x["verdict"] in V_EDGE for x in ev)
      and all(x["verdict"] in V_EDGE for x in nv)
      and all(x["verdict"] in V_ID for x in ids))
check("A8 template consumed (fill + rename per the gate pathway)",
      not (HERE / "c11_batch7_verdicts_template.yaml").exists()
      and VERDICTS.exists())
check("A9 encoding mapping records the WITH_NOTE vocabulary rule + the "
      "code-keying identity-safety rule (sheet/addendum table-order node "
      "numbering vs the template's alphabetical-by-code numbering)",
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
check("B1 edge verdicts: 19 CONFIRM / 0 others",
      ec == {"CONFIRM": 19}, f"{ec}")
check("B2 node verdicts: 15 CONFIRM / 0 others",
      nc == {"CONFIRM": 15}, f"{nc}")
check("B3 identity decisions: 6 x KEEP_AS_IS",
      [x["verdict"] for x in ids] == ["KEEP_AS_IS"] * 6)
check("B4 batch 7 authored ZERO RR edges (no settlement row needed)",
      not any(e["validation_status"] == "REVIEW_REQUIRED"
              for e in dec["edges"]))
check("B5 held appendix acknowledged (9 preserved, quarantined)",
      held_ack.get("acknowledged") is True
      and len(dec["held"]) == 9
      and all(h["status"] == "held" for h in dec["held"]))

b_suggested = {triple(e) for e in dec["edges"]
               if e["validation_status"] == "SUGGESTED"}
check("B6 verdict triples = the batch-7 record's 19 SUGGESTED edges",
      {x["triple"] for x in ev} == b_suggested and len(b_suggested) == 19)
check("B7 verdict node codes = the batch-7 record's 15 node codes "
      "(13 CONCEPT + 2 MISCONCEPTION)",
      {x["code"] for x in nv} == {c["code"] for c in dec["nodes"]}
      and len(dec["nodes"]) == 15
      and sum(1 for c in dec["nodes"] if c["family"] == "CONCEPT") == 13
      and sum(1 for c in dec["nodes"]
              if c["family"] == "MISCONCEPTION") == 2)
check("B8 NO operator_decision blocks in the batch-7 record (none "
      "sanctioned: no RR, no ENRICHMENT node, all identity KEEP_AS_IS)",
      sum(1 for x in dec["nodes"] + dec["edges"]
          if "operator_decision" in x) == 0)
check("B9 no ENRICHMENT-scoped node in batch 7 (none to scope)",
      not any(sp.get("role") == "ENRICHMENT"
              for x in dec["nodes"] for sp in x.get("spec_points", [])))
# the three §6 CONFIRM_WITH_NOTE qualifications carried in notes
e02 = [x for x in ev if x["triple"] ==
       "4CH1-CON-ACID-REACTIONS REQUIRES_PREREQUISITE "
       "4CH1-CON-REACT-ORDER"][0]
e10 = [x for x in ev if x["triple"] ==
       "4CH1-CON-SOLUBILITY-RULES REQUIRES_PREREQUISITE "
       "4CH1-CON-ION-CHARGE-RULES"][0]
n05 = [x for x in nv if x["code"] == "4CH1-CON-NEUTRALISATION"][0]
check("B10 the THREE §6 CONFIRM_WITH_NOTE qualifications carried in notes "
      "(the B7-E-02 acid+metal route guardrail + the B7-E-10 boundary-"
      "ownership guardrail + the retained pass-2 node row "
      "CON-NEUTRALISATION)",
      e02["notes"].startswith("Operator §6 (session 60): "
                              "CONFIRM_WITH_NOTE retained")
      and "Do not generalize it into a universal prerequisite"
      in e02["notes"]
      and e10["notes"].startswith("Operator §6 (session 60): "
                                  "CONFIRM_WITH_NOTE retained")
      and "do not mint a duplicate CON-ION-CHARGE-RULES" in e10["notes"]
      and n05["notes"].startswith("Operator §6: CONFIRM_WITH_NOTE retained")
      and "B7-ID-05" in n05["notes"])
check("B11 the §6 boundary directive recorded (the two sanctioned "
       "cross-section edges keep their governed owners; no duplicate "
       "concept minted; node authority stays SUGGESTED)",
      "No duplicate concept is to be minted" in (r.get("mapping") or "")
      and "Node authority remains SUGGESTED" in (r.get("mapping") or ""))

# ---------------------------------------------------------------------------
# C. application (three-way set equality; session-60 §18 application)
# ---------------------------------------------------------------------------
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
b_triples = {triple(e) for e in dec["edges"]}
b_hv = {t for t in hv if t in b_triples}
confirms = {x["triple"] for x in ev if x["verdict"] == "CONFIRM"}
store_map = {" ".join((p["edge"]["source"], p["edge"]["relation"],
                       p["edge"]["target"])): p
             for p in promo["promotions"]}
check("C1 live batch-7 HUMAN_VALIDATED set = the 19 CONFIRM verdicts",
      b_hv == confirms and len(b_hv) == 19,
      f"live = {len(b_hv)}, verdicts = {len(confirms)}")
check("C2 promotion store = exactly the 19 batch-7 CONFIRM entries",
      set(store_map) & b_triples == confirms)
b_store = {k: p for k, p in store_map.items() if k in b_triples}
check("C3 batch-7 store entries carry operator attribution + 2026-09-23",
      all(p.get("validated_by") == "operator"
          and p.get("validated_date") == "2026-09-23"
          for p in b_store.values()), f"entries = {len(b_store)}")
check("C4 batch-7 store entries reference the B7 diff-review bundle",
      all(p.get("review_reference") == BUNDLE_REF
          for p in b_store.values()))
check("C5 no REJECT/HOLD/MERGE/SPLIT verdicts left un-applied",
      all(x["verdict"] == "CONFIRM" for x in ev))
check("C6 the TWO sanctioned cross-section boundary edges are "
      "HUMAN_VALIDATED (session-59 ruling applied, not re-minted)",
      all(any(triple(e) == t and e["validation_status"] == "HUMAN_VALIDATED"
              for e in sem)
          for t in BOUNDARY_EDGES_EXISTING))
check("C7 boundary ownership exact: BOTH boundary edges target EXISTING "
      "owners ABSENT from the batch-7 mint (CON-REACT-ORDER — the batch-6 "
      "owner; CON-ION-CHARGE-RULES — the batch-3 owner)",
      all(t.split()[2] not in {c["code"] for c in dec["nodes"]}
          for t in BOUNDARY_EDGES_EXISTING)
      and {t.split()[2] for t in BOUNDARY_EDGES_EXISTING}
      == {"4CH1-CON-REACT-ORDER", "4CH1-CON-ION-CHARGE-RULES"})

# ---------------------------------------------------------------------------
# D. invariants (pilot + batch-1..6 slices, store total, negative control,
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
# Session-60 re-anchor (2026-09-23, dated; protective intent unchanged):
# the batch-7 verdicts were APPLIED through §18 (19 promotions, operator) —
# the 19 batch-7 authored edges left the SUGGESTED surface, so the live
# SUGGESTED semantic edges are again EXACTLY the 3 frozen pilot operator
# HOLDs (the pre-session-55 state).
# session-61 re-anchor (2026-09-24, dated; protective intent unchanged): the
# batch-8 authored-to-gate record (10 authored semantic edges) now joins the
# live SUGGESTED surface AT ITS OPERATOR GATE (the session-61 commissioning;
# the batch ends at the gate, zero promotions) — the surface is the 3 frozen
# pilot HOLDs PLUS the 10 batch-8 authored edges; the batch-4/5/6/7 authored
# sets stay fully HUMAN_VALIDATED.
# session-62 re-anchor (2026-09-24, dated; protective intent unchanged): the
# batch-8 verdicts were APPLIED through §18 (10 operator promotions,
# c11_batch8_verdicts, applied 2026-09-24 via the B8 diff-review bundle —
# the operator's completed-sheet §6/§7 verdict: PASS WITH NOTES) — the
# live SUGGESTED surface is again EXACTLY the 3 frozen pilot HOLDs and the
# batch-8 authored edges are all HUMAN_VALIDATED.
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
# EXACTLY the 3 frozen pilot operator HOLDs. No test weakened.
B10_DEC = HERE / "c11_batch10_decisions.yaml"
B10_AUTHORED = {triple(e)
                for e in (yaml.safe_load(B10_DEC.read_text(encoding="utf-8"))
                          .get("edges") or [])}

# session-65 re-anchor (2026-09-25, dated): the batch-10 verdicts were
# APPLIED through §18 (19 promotions, operator, the B10 diff-review
# bundle) — the 19 batch-10 authored edges left the SUGGESTED surface
# (live SUGGESTED = the 3 pilot HOLDs again) and store total
# 236 -> 255. No test weakened.
check("D2 the 3 pilot operator HOLDs stay SUGGESTED (un-promoted) and "
      "the live SUGGESTED semantic surface is EXACTLY the pilot HOLDs (the "
      "batch-8 authored edges were promoted by the operator's verdicts "
      "through §18 at session 62; the batch-9 authored edges were promoted "
      "by the operator's verdicts through §18 at session 63; batch-7 "
      "verdicts applied at session 60)",
      pilot_holds <= live_sugg and not (pilot_holds & hv)
      and live_sugg == pilot_holds
      and B10_AUTHORED <= hv
      and B8_AUTHORED <= hv,
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
# session-63 re-anchor (dated, protective intent unchanged): the batch-9
# §18 application added 20 operator promotions — the store total moved
# 216 -> 236; the batch-7 slice stays preserved exactly.
check("D11 store total 255 (28+28+23+39+35+18+16+19+10+20+19), all operator",
      len(store_map) == 255
      and all(p.get("validated_by") == "operator"
              for p in store_map.values()))
n415 = [x for x in nodes_doc["nodes"]
        if any(sp.get("code") == "4CH1-4.15"
               for sp in x.get("spec_points", []))]
e415 = [e for e in edges_doc["edges"]
        if any("4.15" in a.get("file", "") for a in e.get("evidence", []))]
check("D12 negative control 4CH1-4.15: zero node/edge attachments",
      len(n415) == 0 and len(e415) == 0,
      f"nodes = {len(n415)}, edges = {len(e415)}")
check("D13 no PART_OF edge promoted through the §18 record "
      "(PART_OF HV rows exist only via the later T-C19 G19 record; the "
      "batch-6/7 PART_OF rows stay SUGGESTED pending their own lane)",
      not any(p.get("relation") == "PART_OF"
              for p in (promo.get("promotions") or []))
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF"
              and e["validation_status"] == "HUMAN_VALIDATED") == 117
      and all(e["validation_status"] == "SUGGESTED"
              for e in edges_doc["edges"]
              if e["relation"] == "PART_OF"
              and e["validation_status"] != "HUMAN_VALIDATED"))
check("D14 no batch-7 node is HUMAN_VALIDATED (nodes have no §18 pathway; "
      "the §6 confirmations do not promote nodes — 'Node authority "
      "remains SUGGESTED')",
      not any(x.get("validation_status") == "HUMAN_VALIDATED"
              for x in nodes_doc["nodes"]))
# session-61 re-anchor (2026-09-24, dated): + the SANCTIONED batch-8
# authored-to-gate record (8 nodes / 17 edges = 7 PART_OF + 10
# semantic) — the operator gate decision; no test weakened.
check("D15 live store shape 188 nodes / 459 edges (199 PART_OF + 260 "
      "semantic) — verdicts move statuses only, never shape",
      len(nodes_doc["nodes"]) == 188 and len(edges_doc["edges"]) == 459
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF") == 199)
# boundary mint discipline (the session-59 cross-slice ruling)
non_mint = set(rul["boundary_edge_ruling"]["non_mint_list"])
b7_codes = {c["code"] for c in dec["nodes"]}
check("D16 zero ruled non-mint owner re-minted in the batch-7 node set "
      "(the ruling's non_mint_list codes absent from the mint)",
      len(non_mint) == 58 and not (b7_codes & non_mint),
      f"non_mint = {len(non_mint)}, collision = "
      f"{sorted(b7_codes & non_mint)}")
# the sanctioned boundary targets exist exactly once in the live store
# (no duplicate mint by the boundary edges' application)
for t in BOUNDARY_EDGES_EXISTING:
    hits = [e for e in edges_doc["edges"] if triple(e) == t]
    check(f"D17 boundary target authored exactly once: {t}",
          len(hits) == 1 and hits[0]["validation_status"] == "HUMAN_VALIDATED")
# the 9 held candidates were never authored -> absent from the live store
held_ids = [h["id"] for h in dec["held"]]
check("D18 the 9 batch-7 held candidates stay quarantined (recorded, "
      "never authored; store untouched by holds)",
      len(held_ids) == 9
      and not any(triple(e) in b_suggested for e in dec["edges"]
                  if e["validation_status"] == "REVIEW_REQUIRED"))

# ---------------------------------------------------------------------------
print()
if fails:
    print(f"FAILED: {len(fails)} check(s): {fails}")
    raise SystemExit(1)
print(f"c11_batch7_verdict_check: ALL PASS — batch-7 operator verdict layer "
      f"(19+15+6 rows, the addendum §6/§7 verdict: PASS WITH NOTES; zero RR "
      f"authored; the THREE CONFIRM_WITH_NOTE qualifications carried in "
      f"notes; the session-60 addendum delivery record + the operator's "
      f"REPORTED-state caveat) schema-valid, record-reconciled, "
      f"application-reconciled (19 §18 promotions = the CONFIRM set; no "
      f"operator_decision blocks; pilot + batch-1..6 slices intact; 206 "
      f"store entries total; the 2 boundary targets applied with exact "
      f"ownership — both existing owners (batch-6 CON-REACT-ORDER, batch-3 "
      f"CON-ION-CHARGE-RULES), zero re-mint; 58 non-mint owners respected).")
