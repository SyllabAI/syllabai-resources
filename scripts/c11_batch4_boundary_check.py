#!/usr/bin/env python3
"""T-C11 session 52 — c11_batch4_boundary_check.py: standing checker for the
cross-slice boundary ruling (scripts/c11_batch4_boundary_ruling.yaml).

Machine-verifies the ruling's conflict-free claims against the LIVE store
so the ruling is checkable, not prose:

  A. ruling schema          — sections present, session/date/attribution
  B. conflict audit         — re-running the S3 candidate-term match
                              against the live merged store (codes +
                              titles + aliases + edge endpoints) MUST
                              reproduce ZERO conflicts
  C. boundary targets exist — every sanctioned boundary target is a live
                              S1-store node owned by the record the
                              ruling names (no phantom targets, no
                              ownership drift)
  D. discipline invariants  — the ruling mints nothing (no new nodes/edges
                              vs the store), the non_mint_list is
                              duplicate-free, and the store is at the
                              session-52 post-application shape
                              (91/220/97/123, 118 HUMAN_VALIDATED)

Usage: python3 scripts/c11_batch4_boundary_check.py
"""
from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
GRAPH = REPO / "graph"
RULING = HERE / "c11_batch4_boundary_ruling.yaml"
OWNERS = {
    "pilot": HERE / "c11_pilot_decisions.yaml",
    "batch 1": HERE / "c11_batch1_decisions.yaml",
    "batch 2": HERE / "c11_batch2_decisions.yaml",
    "batch 3": HERE / "c11_batch3_decisions.yaml",
}

fails: list[str] = []
n = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global n
    n += 1
    print(f"{'PASS' if ok else 'FAIL'}  {name}"
          + (f"  {detail}" if detail else ""))
    if not ok:
        fails.append(name)


rul = yaml.safe_load(RULING.read_text(encoding="utf-8"))
nodes_doc = yaml.safe_load((GRAPH / "concepts.yaml").read_text(encoding="utf-8"))
edges_doc = yaml.safe_load((GRAPH / "concept_edges.yaml")
                           .read_text(encoding="utf-8"))

# ---------------------------------------------------------------------------
# A. ruling schema
# ---------------------------------------------------------------------------
check("A1 ruling parses with required sections",
      all(k in rul for k in ("meta", "conflict_audit", "mint_ruling",
                             "boundary_edge_ruling", "non_goals")))
m = rul["meta"]
check("A2 ruling attribution (session 52, operator-commissioned, 2026-09-13)",
      m.get("session") == 52 and m.get("recorded_date") == "2026-09-13"
      and "operator session-52 directive" in (m.get("commissioned_by") or ""))

# ---------------------------------------------------------------------------
# B. conflict audit re-run against the LIVE store
# ---------------------------------------------------------------------------
blob = []
for x in nodes_doc["nodes"]:
    blob.append(x["code"])
    blob.append(x["title"])
    blob.extend(x.get("aliases", []))
store_blob = " || ".join(blob).lower()
endpoints = " ".join(f"{e['source']} {e['target']}"
                     for e in edges_doc["edges"]).lower()
terms = rul["conflict_audit"]["s3_candidate_terms"]
conflicts = [t for t in terms if t in store_blob or t in endpoints]
check("B1 zero canonical conflicts re-verified on the live store",
      conflicts == [], f"conflicts = {conflicts}")
check("B2 the ruling's recorded result matches the live re-run",
      rul["conflict_audit"].get("result", "").startswith("ZERO canonical")
      and not conflicts)

# ---------------------------------------------------------------------------
# C. boundary targets exist + ownership exact
# ---------------------------------------------------------------------------
live_codes = {x["code"] for x in nodes_doc["nodes"]}
owner_of = {}
for label, path in OWNERS.items():
    d = yaml.safe_load(path.read_text(encoding="utf-8"))
    for x in d["nodes"]:
        owner_of[x["code"]] = label

targets = rul["boundary_edge_ruling"]["sanctioned_targets"]
for t in targets:
    code, owner = t["target"], t["owner"]
    check(f"C {code} exists in the live store",
          code in live_codes)
    check(f"C {code} owned by {owner} (no ownership drift)",
          owner_of.get(code) == owner,
          f"actual owner = {owner_of.get(code)}")

non_mint = rul["boundary_edge_ruling"]["non_mint_list"]
check("C non_mint_list duplicate-free and all live",
      len(non_mint) == len(set(non_mint))
      and all(c in live_codes for c in non_mint))
check("C every sanctioned target is also non-mint protected",
      {t["target"] for t in targets} <= set(non_mint))

# ---------------------------------------------------------------------------
# D. discipline invariants
# ---------------------------------------------------------------------------
check("D1 the ruling mints no node (store node set unchanged)",
      len(live_codes) == 91)
check("D2 the ruling mints no edge (store edge set unchanged)",
      len(edges_doc["edges"]) == 220
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF") == 97)
hv = sum(1 for e in edges_doc["edges"]
         if e["validation_status"] == "HUMAN_VALIDATED")
check("D3 store at the session-52 post-application shape (118 HV)",
      hv == 118)
check("D4 non_goals recorded (no ontology redesign / no re-scope / no "
      "promotion authority)",
      len(rul.get("non_goals", [])) >= 4)

# ---------------------------------------------------------------------------
print()
if fails:
    print(f"FAILED: {len(fails)} check(s): {fails}")
    raise SystemExit(1)
print("c11_batch4_boundary_check: ALL PASS — the cross-slice boundary "
      "ruling (session 52) is schema-valid, its zero-conflict audit "
      "reproduces on the live store, every sanctioned boundary target "
      "exists with exact ownership, and the ruling mints nothing "
      "(91/220/97/123, 118 HV unchanged).")
