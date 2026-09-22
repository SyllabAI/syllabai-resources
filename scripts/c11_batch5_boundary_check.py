#!/usr/bin/env python3
"""T-C11 session 55 — c11_batch5_boundary_check.py: standing checker for the
cross-slice boundary ruling (scripts/c11_batch5_boundary_ruling.yaml).

Machine-verifies the ruling's claims against the LIVE store so the ruling is
checkable, not prose (the c11_batch4_boundary_check.py pattern):

  A. ruling schema          — sections present, session/date/attribution
  B. conflict audit         — re-running the S2 candidate-term match against
                              the PRE-batch-5 store (registry minus the
                              batch-5 record when it exists, the live store
                              otherwise) reproduces the recorded match set
  C. boundary targets exist — every sanctioned boundary target is a live
                              node owned by the record the ruling names
  D. discipline invariants  — the ruling mints nothing beyond the sanctioned
                              batch-5 authoring (checked post-authoring), the
                              non_mint_list is duplicate-free + covered, the
                              semantic HV count is the operator promotions
                              (171 after the session-56 §18 application;
                              PART_OF HV rides the later T-C19 G19
                              record)

Usage: python3 scripts/c11_batch5_boundary_check.py
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
RULING = HERE / "c11_batch5_boundary_ruling.yaml"
OWNERS = {
    "pilot": HERE / "c11_pilot_decisions.yaml",
    "batch 1": HERE / "c11_batch1_decisions.yaml",
    "batch 2": HERE / "c11_batch2_decisions.yaml",
    "batch 3": HERE / "c11_batch3_decisions.yaml",
    "batch 4": HERE / "c11_batch4_decisions.yaml",
}
B5_RECORD = HERE / "c11_batch5_decisions.yaml"

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
check("A2 ruling attribution (session 55, operator-commissioned, 2026-09-22)",
      m.get("session") == 55 and m.get("recorded_date") == "2026-09-22"
      and "run batch 5" in (m.get("commissioned_by") or ""))

# ---------------------------------------------------------------------------
# B. conflict audit re-run against the PRE-batch-5 store
# (the ruling was recorded against the live 113-node post-batch-4 state; once
# the batch-5 record enters the registry, the audit re-runs on the registry
# minus batch 5 — the state the ruling was recorded against. The claim it
# protects: no NON-batch-5 node or edge anywhere in the store carries an
# UNDISPOSITIONED S2 term; the 27 recorded matches reproduce.)
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
b5_codes = {x["code"] for x in nodes_doc["nodes"]} - pre_codes
pre_edges = [e for e in edges_doc["edges"]
             if e["source"] not in b5_codes and e["target"] not in b5_codes]
endpoints = " ".join(f"{e['source']} {e['target']}"
                     for e in pre_edges).lower()
terms = rul["conflict_audit"]["s2_candidate_terms"]
matched = [t for t in terms if t in store_blob or t in endpoints]
check("B1 the recorded 27-match audit reproduces on the pre-batch-5 store "
      "(registry state the ruling was recorded against)",
      len(matched) == 27, f"matched = {len(matched)}")
check("B2 the ruling records a disposition for every matched term",
      len(rul["match_dispositions"]) >= 27
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
check("C every sanctioned target is also non-mint protected",
      {t["target"] for t in targets} <= set(non_mint))
check("C max_boundary_edges honoured (at most 3 sanctioned targets)",
      len(targets) <= rul["boundary_edge_ruling"]["max_boundary_edges"] == 3)

# ---------------------------------------------------------------------------
# D. discipline invariants
# (session-55 authoring re-anchor, dated, protective intent unchanged: the
# store grew by the SANCTIONED batch-5 authored-to-gate record —
# scripts/c11_batch5_decisions.yaml, extraction_pass c11-s16-batch-5, the
# record this ruling governs — 16 nodes + 13 PART_OF + 18 authored semantic
# edges, ZERO promotions: 153 SEMANTIC HV unchanged. The ruling itself still
# mints nothing and promotes nothing.
# session-56 re-anchor, dated, protective intent unchanged: the operator's
# batch-5 verdicts (c11_batch5_verdicts, completed sheet §6) were APPLIED
# through §18 — the 18 batch-5 authored semantic edges promoted to
# HUMAN_VALIDATED (153 -> 171 semantic HV); the ruling's protected property
# is unchanged: it still mints nothing, and every promoted identity is a
# batch-5 authored row, not a ruling mint.)
# ---------------------------------------------------------------------------
# session-57 re-anchor (dated, protective intent unchanged): the store also
# grew by the SANCTIONED batch-6 authored-to-gate record (13 nodes + 12
# PART_OF + 16 authored semantic edges, ZERO promotions) once that record
# entered the registry — the batch-5 protected property (its sanctioned
# authoring shape) is unchanged.
# session-58 re-anchor (dated, protective intent unchanged): the operator's
# batch-6 verdicts (c11_batch6_verdicts, completed sheet §6) were APPLIED
# through §18 — the 16 batch-6 authored semantic edges promoted to
# HUMAN_VALIDATED (171 -> 187 semantic HV); the batch-5 protected property
# is unchanged: its 18 promotions stay exact, and every promoted identity
# is an operator-verdict row, not a ruling mint.)
B6_RECORD = HERE / "c11_batch6_decisions.yaml"
expected_nodes = 113 + (16 if B5_RECORD.exists() else 0) \
    + (13 if B6_RECORD.exists() else 0)
expected_edges = 275 + (31 if B5_RECORD.exists() else 0) \
    + (28 if B6_RECORD.exists() else 0)
expected_partof = 117 + (13 if B5_RECORD.exists() else 0) \
    + (12 if B6_RECORD.exists() else 0)
check("D1 the ruling mints no node beyond the sanctioned batch-5 authoring",
      len(live_codes) == expected_nodes,
      f"live = {len(live_codes)}, expected = {expected_nodes}")
check("D2 the ruling mints no edge beyond the sanctioned batch-5 authoring",
      len(edges_doc["edges"]) == expected_edges
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF") == expected_partof)
hv = sum(1 for e in edges_doc["edges"]
         if e["validation_status"] == "HUMAN_VALIDATED"
         and e["relation"] != "PART_OF")
check("D3 semantic HV at the operator-promoted count (187 = 153 + the 18 "
      "batch-5 §18 promotions applied at session 56 + the 16 batch-6 §18 "
      "promotions applied at session 58; the ruling itself still mints "
      "nothing; PART_OF HV rides the T-C19 G19 record)",
      hv == 187)
check("D4 non_goals recorded (no ontology redesign / no re-opening / no "
      "re-scope / no promotion authority / no direct writes)",
      len(rul.get("non_goals", [])) >= 5)

# ---------------------------------------------------------------------------
print()
if fails:
    print(f"FAILED: {len(fails)} check(s): {fails}")
    raise SystemExit(1)
print("c11_batch5_boundary_check: ALL PASS — the cross-slice boundary ruling "
      "(session 55) is schema-valid, its 27-match dispositioned audit "
      "reproduces on the pre-batch-5 store, every sanctioned boundary target "
      "exists with exact ownership, and the ruling mints and promotes nothing "
      "beyond the sanctioned batch-5 authored-to-gate record.")
