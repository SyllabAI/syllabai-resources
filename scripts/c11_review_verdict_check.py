#!/usr/bin/env python3
"""T-C11 — c11_review_verdict_check.py: schema/integrity validation for the
OPERATOR-OWNED verdict record scripts/c11_review_verdicts.yaml (session 44).

Fail-closed gate for the verdict layer. Validates:

  A. schema: required sections, exact row surfaces (OD-1/OD-2; E-01..E-31;
     N-01..N-29), vocabulary conformance, decided_by/decided_date on OD rows;
  B. reconciliation against the live store: the 31 edge triples are exactly
     the 31 SUGGESTED semantic edges (no drift, no invented ID); the 29 node
     codes are exactly the store's codes; the RR edge (operator HOLD,
     session 41) is NOT a verdict row; the 13 held entries are 11 HOLD +
     2 REJECT (HELD-09 / HELD-13);
  C. decision-set shape: 28 edge CONFIRM + 3 HOLD (exactly E-08/E-26/E-29) +
     0 REJECT/MERGE/SPLIT; 29 node CONFIRM; OD-1 and OD-2 RATIFY by operator;
     enrichment notes exactly on N-08 and N-27; alias policy RETRIEVAL_EXEMPT
     with the four-rule discipline; 'maximum yield' = KEEP marked
     retrieval-only/unevidenced; held appendix acknowledged;
  D. zero-action invariants: promotion store empty; 0 HUMAN_VALIDATED; the
     RR edge still REVIEW_REQUIRED with its operator HOLD block intact;
  E. evidence integrity behind the note-carrying rows (E-08/E-26/E-29,
     N-08/N-27): every evidence quote re-byte-verified against the corpus
     under the T-C10 norm — verdicts must not rest on reinterpreted quotes.

Exit 0 = all checks pass; exit 1 = any failure (all printed).
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
GRAPH = REPO / "graph"
REPORTS = GRAPH / "reports"
NOTES = REPO / "Chemistry IGCSE Revision Notes"

VERDICTS = HERE / "c11_review_verdicts.yaml"
EDGES = GRAPH / "concept_edges.yaml"
NODES = GRAPH / "concepts.yaml"
DECISIONS = HERE / "c11_pilot_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"

EDGE_VOCAB = {"CONFIRM", "REJECT", "HOLD", "MERGE", "SPLIT"}
OD_VOCAB = {"RATIFY", "RATIFY_WITH_MODIFICATION", "REJECT", "DEFER"}
ALIAS_POLICY_VOCAB = {"EVIDENCE_REQUIRED_ALL", "EVIDENCE_REQUIRED_SPECIAL",
                      "RETRIEVAL_EXEMPT"}
ALIAS_DISP_VOCAB = {"DROP", "RE_EVIDENCE", "KEEP", "RENAME"}
RR_TRIPLE = "4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-AVOGADRO-LAW"

fails = []


def check(name: str, cond: bool, detail: str = ""):
    print(("PASS  " if cond else "FAIL  ") + name + (f"  {detail}" if detail else ""))
    if not cond:
        fails.append(name)


# --- T-C10 norm() convention (copied verbatim from c11_concept_pilot.py) ---
_TRANS = {ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = s.translate(_TRANS)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


_files = {}


def normed_file(rel: str) -> str:
    """rel is the repo-relative path exactly as recorded in evidence blocks."""
    if rel not in _files:
        p = REPO / rel
        _files[rel] = norm(p.read_text(encoding="utf-8")) if p.exists() else None
    return _files[rel]


def quote_verbatim(ev: dict) -> bool:
    body = normed_file(ev.get("file", ""))
    if body is None:
        return False
    return norm(ev.get("quote", "")) in body


vd = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
edges_doc = yaml.safe_load(EDGES.read_text(encoding="utf-8"))
nodes_doc = yaml.safe_load(NODES.read_text(encoding="utf-8"))
dec = yaml.safe_load(DECISIONS.read_text(encoding="utf-8"))
promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))

# ---------------------------------------------------------------------------
# A. schema
# ---------------------------------------------------------------------------
check("A1 file parses with required sections",
      all(k in vd for k in ("meta", "od_ratifications", "edge_verdicts",
                            "node_verdicts", "alias_policy",
                            "alias_dispositions", "held_appendix")))
check("A2 verdict stage recorded (session 44)",
      vd["meta"].get("stage") == "operator-verdicts"
      and vd["meta"].get("session") == 44)
ods = vd["od_ratifications"]
check("A3 OD rows exactly OD-1/OD-2", [r["id"] for r in ods] == ["OD-1", "OD-2"])
for r in ods:
    check(f"A4 {r['id']} vocabulary + decided_by/date",
          r["verdict"] in OD_VOCAB and r.get("decided_by") == "operator"
          and bool(r.get("decided_date")) and bool(r.get("notes")))
ev = vd["edge_verdicts"]
nv = vd["node_verdicts"]
check("A5 edge rows E-01..E-31 sequential, complete",
      [r["id"] for r in ev] == [f"E-{i:02d}" for i in range(1, 32)])
check("A6 node rows N-01..N-29 sequential, complete",
      [r["id"] for r in nv] == [f"N-{i:02d}" for i in range(1, 30)])
check("A7 all edge verdicts in vocabulary, none empty",
      all(r["verdict"] in EDGE_VOCAB for r in ev))
check("A8 all node verdicts in vocabulary, none empty",
      all(r["verdict"] in EDGE_VOCAB for r in nv))
ap = vd["alias_policy"]
check("A9 alias_policy verdict in vocabulary",
      ap["verdict"] in ALIAS_POLICY_VOCAB)
ads = vd["alias_dispositions"]
check("A10 alias_dispositions exactly the maximum-yield row",
      len(ads) == 1 and ads[0]["node"] == "4CH1-CON-THEOR-YIELD"
      and ads[0]["alias"] == "maximum yield"
      and ads[0]["disposition"] in ALIAS_DISP_VOCAB)

# ---------------------------------------------------------------------------
# B. reconciliation against the live store
# ---------------------------------------------------------------------------
def triple(e):
    return f"{e['source']} {e['relation']} {e['target']}"


semantic = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
suggested = [e for e in semantic if e["validation_status"] == "SUGGESTED"]
rr = [e for e in semantic if e["validation_status"] == "REVIEW_REQUIRED"]
hv = [e for e in semantic if e["validation_status"] == "HUMAN_VALIDATED"]
tmpl_triples = [r["triple"] for r in ev]
graph_triples = [triple(e) for e in suggested]

check("B1 store frozen: 65 edges (33 PART_OF + 32 semantic)",
      len(edges_doc["edges"]) == 65 and len(semantic) == 32
      and sum(1 for e in edges_doc["edges"] if e["relation"] == "PART_OF") == 33)
check("B2 verdict surface = the 31 SUGGESTED semantic edges, exactly",
      sorted(tmpl_triples) == sorted(graph_triples)
      and len(set(tmpl_triples)) == 31 and len(suggested) == 31)
check("B3 no PART_OF row on the verdict surface (derived edges carry no verdicts)",
      not any(" PART_OF " in t for t in tmpl_triples))
check("B4 RR edge excluded from the surface and still exactly the operator-HOLD edge",
      RR_TRIPLE not in tmpl_triples and len(rr) == 1 and triple(rr[0]) == RR_TRIPLE)
check("B5 0 HUMAN_VALIDATED in the store", len(hv) == 0)

node_codes = [n["code"] for n in nodes_doc["nodes"]]
check("B6 verdict node codes = the store's 29 codes, exactly",
      sorted(r["code"] for r in nv) == sorted(node_codes)
      and len(set(node_codes)) == 29 and len(nodes_doc["nodes"]) == 29)

held = dec["held"]
statuses = {h["id"]: h["status"] for h in held}
expected = {f"HELD-{i:02d}": "held" for i in range(1, 14)}
expected["HELD-09"] = "rejected"
expected["HELD-13"] = "rejected"
check("B7 held appendix unchanged: 13 entries, 11 held + 2 rejected @ 09/13",
      len(held) == 13 and statuses == expected)
h13 = next(h for h in held if h["id"] == "HELD-13")
check("B8 HELD-13 operator REJECT block intact (verdict + 4 verbatim reasons)",
      h13.get("operator_decision", {}).get("verdict") == "REJECT"
      and len(h13["operator_decision"].get("reasons", [])) == 4)

# ---------------------------------------------------------------------------
# C. decision-set shape (the operator's session-44 decision set)
# ---------------------------------------------------------------------------
ec: dict = {}
for r in ev:
    ec[r["verdict"]] = ec.get(r["verdict"], 0) + 1
nc: dict = {}
for r in nv:
    nc[r["verdict"]] = nc.get(r["verdict"], 0) + 1

check("C1 edge verdicts: 28 CONFIRM / 3 HOLD / 0 REJECT / 0 MERGE / 0 SPLIT",
      ec == {"CONFIRM": 28, "HOLD": 3}, str(ec))
hold_ids = [r["id"] for r in ev if r["verdict"] == "HOLD"]
check("C2 the three HOLDs are exactly E-08, E-26, E-29",
      hold_ids == ["E-08", "E-26", "E-29"])
check("C3 every HOLD row carries an operator rationale note",
      all(r["notes"].strip() for r in ev if r["verdict"] == "HOLD"))
check("C4 node verdicts: 29 CONFIRM / 0 HOLD / 0 REJECT",
      nc == {"CONFIRM": 29}, str(nc))
check("C5 OD-1 and OD-2 both RATIFY",
      all(r["verdict"] == "RATIFY" for r in ods))
check("C6 OD notes record the generalized split rule / the incidental rule",
      "ACTUAL_YIELD" in ods[0]["notes"] and "THEORETICAL_YIELD" in ods[0]["notes"]
      and "incidental" in ods[1]["notes"].lower())
enriched = [r["id"] for r in nv
            if "enrichment concept" in r.get("notes", "").lower()]
check("C7 enrichment notes exactly on N-08 and N-27",
      enriched == ["N-08", "N-27"], str(enriched))
n08 = next(r for r in nv if r["id"] == "N-08")
n27 = next(r for r in nv if r["id"] == "N-27")
check("C8 enrichment notes stay enrichment-scoped (no syllabus-authority claim)",
      "4CH1-1.27" in n08["notes"] and "1.35C" in n27["notes"]
      and "stronger syllabus-authority" in n08["notes"]
      and "stronger syllabus-authority" in n27["notes"])
check("C9 alias policy RETRIEVAL_EXEMPT with the four-rule discipline",
      ap["verdict"] == "RETRIEVAL_EXEMPT"
      and all(k in ap["notes"] for k in
              ("(1)", "(2)", "(3)", "(4)", "retrieval-only")))
check("C10 'maximum yield' = KEEP, marked retrieval-only / unevidenced",
      ads[0]["disposition"] == "KEEP"
      and "retrieval-only" in ads[0]["notes"]
      and "unevidenced" in ads[0]["notes"]
      and "NOT" in ads[0]["notes"])
check("C11 held appendix acknowledged",
      vd["held_appendix"].get("acknowledged") is True)

# ---------------------------------------------------------------------------
# D. zero-action invariants
# ---------------------------------------------------------------------------
check("D1 live promotion store empty (0 entries)",
      not promo.get("promotions"), f"entries={len(promo.get('promotions', []))}")
rr_dec = next(e for e in dec["edges"] if triple(e) == RR_TRIPLE)
check("D2 RR edge keeps its standing operator HOLD in the decision record",
      rr_dec.get("operator_decision", {}).get("verdict") == "HOLD")
check("D3 verdict record contains no promotion payload or promoted status",
      "promotions" not in vd
      and not any(r["verdict"] in ("HUMAN_VALIDATED", "PROMOTE") for r in ev + nv)
      and vd["meta"].get("stage") == "operator-verdicts")

# ---------------------------------------------------------------------------
# E. evidence integrity behind the note-carrying rows
# ---------------------------------------------------------------------------
note_rows = {"E-08", "E-26", "E-29", "N-08", "N-27"}
verdict_map = {r["id"]: r for r in ev}
node_map = {r["id"]: r for r in nv}
spot = []
for eid in ("E-08", "E-26", "E-29"):
    e = next(x for x in suggested if triple(x) == verdict_map[eid]["triple"])
    for evi in e.get("evidence", []):
        spot.append((eid, evi))
for nid in ("N-08", "N-27"):
    code = node_map[nid]["code"]
    n = next(x for x in nodes_doc["nodes"] if x["code"] == code)
    for sp in n.get("spec_points", []):
        for evi in sp.get("evidence", []):
            spot.append((nid, evi))
ok = all(quote_verbatim(evi) for _, evi in spot)
check(f"E1 evidence quotes behind note-carrying rows byte-verified "
      f"({len(spot)} quotes, T-C10 norm)", ok,
      "" if ok else "; ".join(f"{rid}:{evi.get('file', '?')}" for rid, evi in spot
                              if not quote_verbatim(evi)))

# --- 4.15 negative control unchanged (meta-only) ---
n415 = [e for e in edges_doc["edges"]
        if any("4.15" in ev.get("file", "") for ev in e.get("evidence", []))]
n415n = [n for n in nodes_doc["nodes"]
         if any("4.15" in ev.get("file", "")
                for sp in n.get("spec_points", []) for ev in sp.get("evidence", []))]
check("E2 negative control 4CH1-4.15: zero concept/edge evidence attachments",
      not n415 and not n415n)

print()
if fails:
    print(f"c11_review_verdict_check: {len(fails)} FAILURE(S): {fails}")
    sys.exit(1)
print("c11_review_verdict_check: ALL PASS — operator verdict layer "
      "(31+29 rows, 2 OD ratifications, alias policy + disposition, held "
      "appendix) schema-valid, store-reconciled, shape-exact, zero-action, "
      "evidence-verified.")
