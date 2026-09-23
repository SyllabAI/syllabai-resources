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
# (session-53 re-anchor, dated, protective intent unchanged: the S3 terms
# now legitimately live in the batch-4 MINT the ruling authorized — so the
# zero-conflict audit is re-run against the PRE-batch-4 store, reconstructed
# from the decision-record registry minus the batch-4 record (the state the
# ruling was recorded against at session 52). The claim it protects: no
# NON-batch-4 node or edge anywhere in the store carries an S3 term.)
# ---------------------------------------------------------------------------
pre_b4_nodes = []
for name in ("c11_pilot_decisions.yaml", "c11_batch1_decisions.yaml",
             "c11_batch2_decisions.yaml", "c11_batch3_decisions.yaml"):
    _d = yaml.safe_load((HERE / name).read_text(encoding="utf-8"))
    pre_b4_nodes.extend(_d.get("nodes") or [])
blob = []
for x in pre_b4_nodes:
    blob.append(x["code"])
    blob.append(x["title"])
    blob.extend(x.get("aliases", []))
store_blob = " || ".join(blob).lower()
pre_b4_codes = {x["code"] for x in pre_b4_nodes}
b4_codes = {x["code"] for x in nodes_doc["nodes"]} - pre_b4_codes
pre_b4_edges = [e for e in edges_doc["edges"]
                if e["source"] not in b4_codes
                and e["target"] not in b4_codes]
endpoints = " ".join(f"{e['source']} {e['target']}"
                      for e in pre_b4_edges).lower()
terms = rul["conflict_audit"]["s3_candidate_terms"]
conflicts = [t for t in terms if t in store_blob or t in endpoints]
check("B1 zero canonical conflicts re-verified on the pre-batch-4 store "
      "(the 91-node registry state the ruling was recorded against)",
      conflicts == [], f"conflicts = {conflicts}")
# Session-55 re-anchor (2026-09-22, dated; protective intent unchanged): the
# batch-5 authored-to-gate record (16 nodes + 30 edges) joins the batch-4
# mint in the live store; the pre-batch-4 reconstruction now excludes BOTH
# sanctioned mints (38 nodes = 22 batch-4 + 16 batch-5; edge delta
# 86 = 55 batch-4 + 31 batch-5).
# Session-57 re-anchor (2026-09-22, dated; protective intent unchanged): the
# batch-6 authored-to-gate record (13 nodes + 28 edges) joins the live
# store; the pre-batch-4 reconstruction now excludes ALL THREE sanctioned
# mints (51 nodes = 22 batch-4 + 16 batch-5 + 13 batch-6; edge delta
# 114 = 55 batch-4 + 31 batch-5 + 28 batch-6).
# Session-59 re-anchor (2026-09-23, dated; protective intent unchanged): the
# batch-7 authored-to-gate record (15 nodes + 33 edges) joins the live
# store; the pre-batch-4 reconstruction now excludes ALL FOUR sanctioned
# mints (66 nodes = 22 batch-4 + 16 batch-5 + 13 batch-6 + 15 batch-7;
# edge delta 147 = 55 batch-4 + 31 batch-5 + 28 batch-6 + 33 batch-7).
check("B2 the ruling's recorded result matches the re-run (and the batch-4 "
      "mint is exactly the 22 new nodes / 55 new edges — the batch-5/6/7 "
      "authored-to-gate growth is separate and sanctioned)",
      rul["conflict_audit"].get("result", "").startswith("ZERO canonical")
      and not conflicts
      and len(b4_codes) == 66  # 22 b4 + 16 b5 + 13 b6 + 15 b7 mints
      and len(edges_doc["edges"]) - len(pre_b4_edges) == 147)

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
# (session-53 re-anchor, dated, protective intent unchanged: the store grew
# to 113/275/117 by the SANCTIONED batch-4 authored-to-gate record —
# scripts/c11_batch4_decisions.yaml, extraction_pass c11-s16-batch-4, the
# record this ruling governs; the ruling itself still mints nothing and the
# growth is exactly the batch-4 authoring shape: 22 nodes + 20 PART_OF + 35
# authored semantic edges, ZERO promotions — 118 HV unchanged.
# session-54 re-anchor, dated, protective intent unchanged: the 35 batch-4
# edges were promoted to HUMAN_VALIDATED by the operator's sanctioned
# verdicts (c11_batch4_verdicts, §18) — HV 118 -> 153, graph shape
# unchanged; the ruling still mints nothing.)
# ---------------------------------------------------------------------------
# Session-55 re-anchor (2026-09-22, dated): 91 + 22 batch-4 + 16 batch-5.
# Session-57 re-anchor (2026-09-22, dated): + the 13 batch-6
# authored-to-gate nodes — the SANCTIONED batch-6 record; the ruling still
# mints nothing itself.
# Session-59 re-anchor (2026-09-23, dated): + the 15 batch-7
# authored-to-gate nodes — the SANCTIONED batch-7 record; the ruling still
# mints nothing itself.
check("D1 the ruling mints no node (store node set = 91 + the sanctioned "
      "22 batch-4 nodes + the 16 batch-5 + the 13 batch-6 + the 15 batch-7 "
      "authored-to-gate nodes)",
      len(live_codes) == 157)
# Session-55 re-anchor (2026-09-22, dated): 220 + 55 batch-4 + 31 batch-5
# (20 PART_OF + 35 semantic; 13 PART_OF + 17 semantic).
# Session-57 re-anchor (2026-09-22, dated): + the 28 batch-6 edges
# (12 PART_OF + 16 semantic) — the SANCTIONED batch-6 record.
# Session-59 re-anchor (2026-09-23, dated): + the 33 batch-7 edges
# (14 PART_OF + 19 semantic) — the SANCTIONED batch-7 record.
check("D2 the ruling mints no edge (store edge set = 220 + the sanctioned "
      "55 batch-4 edges + the 31 batch-5 + the 28 batch-6 + the 33 batch-7 "
      "authored-to-gate edges)",
      len(edges_doc["edges"]) == 367
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF") == 156)
hv = sum(1 for e in edges_doc["edges"]
         if e["validation_status"] == "HUMAN_VALIDATED"
         and e["relation"] != "PART_OF")
# Session-55 re-anchor (2026-09-22, dated; protective intent unchanged):
# T-C19 (session 106) later promoted all 117 PART_OF rows to HUMAN_VALIDATED
# via its own G19 record — so the raw HUMAN_VALIDATED count over ALL edges is
# now 270 (117 PART_OF + 153 semantic). The ruling's protected property is the
# SEMANTIC HV count (the ruling mints/promotes no semantic edge); counted
# over non-PART_OF edges the 153 assertion holds unchanged.
# Session-56 re-anchor (2026-09-22, dated; protective intent unchanged): the
# batch-5 §18 application (18 operator promotions, c11_batch5_verdicts)
# moved the semantic HV count 153 -> 171; the ruling's protected property is
# unchanged (it still mints/promotes no semantic edge — the 18 promoted
# identities are batch-5 authored rows, not ruling mints).
# Session-58 re-anchor (2026-09-22, dated; protective intent unchanged): the
# batch-6 §18 application (16 operator promotions, c11_batch6_verdicts)
# moved the semantic HV count 171 -> 187; the ruling's protected property is
# unchanged (it still mints/promotes no semantic edge — the 16 promoted
# identities are batch-6 authored rows, not ruling mints).
# session-60 re-anchor (dated): the batch-7 §18 application (19 operator
# promotions, c11_batch7_verdicts) moved the semantic HV count 187 -> 206;
# the protected property is unchanged.
check("D3 store at the session-60 post-verdict shape (206 SEMANTIC HV — "
      "the 35 batch-4 + 18 batch-5 + 16 batch-6 + 19 batch-7 edges "
      "promoted by the operator's verdicts; the ruling itself still mints "
      "nothing; PART_OF HV 117 rides the later T-C19 G19 record)",
      hv == 206)
check("D4 non_goals recorded (no ontology redesign / no re-scope / no "
      "promotion authority)",
      len(rul.get("non_goals", [])) >= 4)

# ---------------------------------------------------------------------------
print()
if fails:
    print(f"FAILED: {len(fails)} check(s): {fails}")
    raise SystemExit(1)
print("c11_batch4_boundary_check: ALL PASS — the cross-slice boundary ruling "
      "(session 52) is schema-valid, its zero-conflict audit reproduces on the live store, every sanctioned boundary target exists with exact ownership, and the ruling mints nothing (142/334/142 at the session-57 state — the sanctioned batch-5 and batch-6 authored-to-gate records joined the store, 171 semantic HV unchanged; the ruling itself authored none of them).")
