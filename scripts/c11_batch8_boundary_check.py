#!/usr/bin/env python3
"""T-C11 session 61 — c11_batch8_boundary_check.py: standing checker for the
cross-slice boundary ruling (scripts/c11_batch8_boundary_ruling.yaml).

Machine-verifies the ruling's claims against the LIVE store so the ruling is
checkable, not prose (the c11_batch7_boundary_check.py pattern):

  A. ruling schema          — sections present, session/date/attribution
  B. conflict audit         — re-running the S2-h candidate-term match
                              against the PRE-batch-8 store (registry minus
                              the batch-8 record when it exists, the live
                              store otherwise) reproduces the recorded
                              53-match set
  C. boundary targets exist — every sanctioned boundary target is a live
                              node owned by the record the ruling names
  D. discipline invariants  — the ruling mints nothing beyond the sanctioned
                              batch-8 authoring (checked post-authoring), the
                              non_mint_list is duplicate-free + covered, the
                              semantic HV count is the operator promotions
                              (206; PART_OF HV rides the later T-C19 G19
                              record)

Usage: python3 scripts/c11_batch8_boundary_check.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402  # C28 §3.2 path registry

REPO = HERE.parent
GRAPH = GP.qual_dir()
RULING = HERE / "c11_batch8_boundary_ruling.yaml"
OWNERS = {
    "pilot": HERE / "c11_pilot_decisions.yaml",
    "batch 1": HERE / "c11_batch1_decisions.yaml",
    "batch 2": HERE / "c11_batch2_decisions.yaml",
    "batch 3": HERE / "c11_batch3_decisions.yaml",
    "batch 4": HERE / "c11_batch4_decisions.yaml",
    "batch 5": HERE / "c11_batch5_decisions.yaml",
    "batch 6": HERE / "c11_batch6_decisions.yaml",
    "batch 7": HERE / "c11_batch7_decisions.yaml",
}
B8_RECORD = HERE / "c11_batch8_decisions.yaml"

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
edges_doc = yaml.safe_load((GRAPH / "concept_edges.yaml").read_text(encoding="utf-8"))

# ---------------------------------------------------------------------------
# A. ruling schema
# ---------------------------------------------------------------------------
check("A1 ruling parses with required sections",
      all(k in rul for k in ("meta", "conflict_audit", "mint_ruling",
                             "boundary_edge_ruling", "future_boundary_notes",
                             "non_goals")))
m = rul["meta"]
check("A2 ruling attribution (session 61, operator-commissioned, 2026-09-24)",
      m.get("session") == 61 and m.get("recorded_date") == "2026-09-24"
      and "Proceed with batch 8" in (m.get("commissioned_by") or ""))

# ---------------------------------------------------------------------------
# B. conflict audit re-run against the PRE-batch-8 store
# (the ruling was recorded against the live 157-node post-batch-7 state; once
# the batch-8 record enters the registry, the audit re-runs on the registry
# minus batch 8 — the state the ruling was recorded against. The claim it
# protects: no NON-batch-8 node or edge anywhere in the store carries an
# UNDISPOSITIONED S2-h term; the 53 recorded matches reproduce.)
# ---------------------------------------------------------------------------
pre_nodes = []
for label, path in OWNERS.items():
    d = yaml.safe_load(path.read_text(encoding="utf-8"))
    for x in d["nodes"]:
        pre_nodes.append((label, x))
blob = []
for _label, x in pre_nodes:
    blob.append(x["code"])
    blob.append(x["title"])
    blob.extend(x.get("aliases", []))
store_blob = " || ".join(blob).lower()
pre_codes = {x["code"] for _l, x in pre_nodes}
b8_codes = {x["code"] for x in nodes_doc["nodes"]} - pre_codes
pre_edges = [e for e in edges_doc["edges"]
             if e["source"] not in b8_codes and e["target"] not in b8_codes]
endpoints = " ".join(f"{e['source']} {e['target']}"
                     for e in pre_edges).lower()
terms = rul["conflict_audit"]["s2_candidate_terms"]
matched = [t for t in terms if t in store_blob or t in endpoints]
check("B1 the recorded 53-match audit reproduces on the pre-batch-8 store "
      "(registry state the ruling was recorded against)",
      len(matched) == 53, f"matched = {len(matched)}")
check("B2 the ruling records a disposition for every matched term",
      len(rul["match_dispositions"]) >= 53
      and rul["conflict_audit"].get("result", "").startswith("NO UNHANDLED"))

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
    check(f"C {code} exists in the live store", code in live_codes)
    check(f"C {code} owned by {owner} (no ownership drift)",
          owner_of.get(code) == owner, f"actual owner = {owner_of.get(code)}")

non_mint = rul["boundary_edge_ruling"]["non_mint_list"]
check("C non_mint_list duplicate-free and all live",
      len(non_mint) == len(set(non_mint))
      and all(c in live_codes for c in non_mint))
check("C every sanctioned EXISTING-OWNER target is non-mint protected",
      {t["target"] for t in targets} <= set(non_mint))
check("C max_boundary_edges honoured (exactly 3 sanctioned targets)",
      len(targets) == 3
      and rul["boundary_edge_ruling"]["max_boundary_edges"] == 3)

# ---------------------------------------------------------------------------
# D. discipline invariants
# (session-61 authoring re-anchor, dated, protective intent unchanged: the
# store grows by the SANCTIONED batch-8 authored-to-gate record —
# scripts/c11_batch8_decisions.yaml, extraction_pass c11-s16-batch-8, the
# record this ruling governs — 8 nodes (6 CONCEPT + 2 MISCONCEPTION) + 10
# authored semantic edges (6 RP/RELATED_TO + 2 WAP + 2 REMEDIATED_BY) + the 7
# derived PART_OF rows (CON-FLAME-TEST attaches 2.45 AND 2.46), ZERO
# promotions: 206 SEMANTIC HV unchanged. The ruling itself still mints
# nothing and promotes nothing.)
# ---------------------------------------------------------------------------
B9_RECORD = HERE / "c11_batch9_decisions.yaml"
B10_RECORD = HERE / "c11_batch10_decisions.yaml"
expected_nodes = 157 + (8 if B8_RECORD.exists() else 0) \
    + (15 if B9_RECORD.exists() else 0) \
    + (8 if B10_RECORD.exists() else 0)
expected_edges = 367 + (17 if B8_RECORD.exists() else 0) \
    + (41 if B9_RECORD.exists() else 0) \
    + (34 if B10_RECORD.exists() else 0)
expected_partof = 156 + (7 if B8_RECORD.exists() else 0) \
    + (21 if B9_RECORD.exists() else 0) \
    + (15 if B10_RECORD.exists() else 0)
check("D1 the ruling mints no node beyond the sanctioned batch-8 authoring",
      len(live_codes) == expected_nodes,
      f"live = {len(live_codes)}, expected = {expected_nodes}")
check("D2 the ruling mints no edge beyond the sanctioned batch-8 authoring",
      len(edges_doc["edges"]) == expected_edges
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF") == expected_partof)
hv = sum(1 for e in edges_doc["edges"]
         if e["validation_status"] == "HUMAN_VALIDATED"
         and e["relation"] != "PART_OF")
# session-62 re-anchor (dated): the batch-8 verdicts WERE APPLIED through
# §18 at session 62 (10 operator promotions, c11_batch8_verdicts, via the
# B8 diff-review bundle — the operator's completed-sheet §6/§7 verdict:
# PASS WITH NOTES); the semantic HV count moved 206 -> 216 and the ruling's
# protected property is unchanged (it still mints nothing).
# session-63 re-anchor (dated): the batch-9 §18 application (20 operator
# promotions, c11_batch9_verdicts, 2026-09-25) moved the semantic HV count
# 216 -> 236; the protected property is unchanged.
# session-65 re-anchor (2026-09-25, dated): the batch-10 §18 application
# (19 operator promotions, c11_batch10_verdicts, the B10 diff-review
# bundle) moved the semantic HV count 236 -> 255; the protected property
# is unchanged.
check("D3 semantic HV at the operator-promoted count (255; the 10 "
      "batch-8 authored edges were promoted by the operator's §6/§7 "
      "verdicts via §18 at session 62, the 20 batch-9 authored edges "
      "likewise at session 63, and the 19 batch-10 authored edges "
      "likewise at session 65; PART_OF HV rides the T-C19 G19 "
      "record)",
      hv == 255)
check("D4 non_goals recorded (no ontology redesign / no re-opening / no "
      "re-scope / no promotion authority / no direct writes)",
      len(rul.get("non_goals", [])) >= 5)

# ---------------------------------------------------------------------------
print()
if fails:
    print(f"FAILED: {len(fails)} check(s): {fails}")
    raise SystemExit(1)
print("c11_batch8_boundary_check: ALL PASS — the cross-slice boundary ruling "
      "(session 61) is schema-valid, its 53-match dispositioned audit "
      "reproduces on the pre-batch-8 store, every sanctioned boundary target "
      "exists with exact ownership, and the ruling mints and promotes nothing "
      "beyond the sanctioned batch-8 authored-to-gate record.")
