#!/usr/bin/env python3
"""T-C11 session 62 — c11_batch9_boundary_check.py: standing checker for the
cross-slice boundary ruling (scripts/c11_batch9_boundary_ruling.yaml).

Machine-verifies the ruling's claims against the LIVE store so the ruling is
checkable, not prose (the c11_batch8_boundary_check.py pattern):

  A. ruling schema          — sections present, session/date/attribution
  B. conflict audit         — re-running the S4-a/b/c candidate-term match
                              against the PRE-batch-9 store (registry minus
                              the batch-9 record when it exists, the live
                              store otherwise) reproduces the recorded
                              46-match set
  C. boundary targets exist — every sanctioned boundary target is a live
                              node owned by the record the ruling names
  D. discipline invariants  — the ruling mints nothing beyond the sanctioned
                              batch-9 authoring (checked post-authoring), the
                              non_mint_list is duplicate-free + covered, the
                              semantic HV count is the operator promotions
                              (236 after the session-63 §18 application;
                              PART_OF HV rides the later T-C19 G19
                              record)

Usage: python3 scripts/c11_batch9_boundary_check.py
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
RULING = HERE / "c11_batch9_boundary_ruling.yaml"
OWNERS = {
    "pilot": HERE / "c11_pilot_decisions.yaml",
    "batch 1": HERE / "c11_batch1_decisions.yaml",
    "batch 2": HERE / "c11_batch2_decisions.yaml",
    "batch 3": HERE / "c11_batch3_decisions.yaml",
    "batch 4": HERE / "c11_batch4_decisions.yaml",
    "batch 5": HERE / "c11_batch5_decisions.yaml",
    "batch 6": HERE / "c11_batch6_decisions.yaml",
    "batch 7": HERE / "c11_batch7_decisions.yaml",
    "batch 8": HERE / "c11_batch8_decisions.yaml",
}
B9_RECORD = HERE / "c11_batch9_decisions.yaml"
B10_RECORD = HERE / "c11_batch10_decisions.yaml"

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
check("A2 ruling attribution (session 62, operator-commissioned, 2026-09-24)",
      m.get("session") == 62 and m.get("recorded_date") == "2026-09-24"
      and "commission a new section" in (m.get("commissioned_by") or ""))
check("A3 the 4.15 negative-control carve-out recorded in the ruling",
      "4CH1-4.15" in (m.get("scope_sp_note") or "")
      and "CARVED OUT" in (m.get("scope_sp_note") or ""))

# ---------------------------------------------------------------------------
# B. conflict audit re-run against the PRE-batch-9 store
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
b9_codes = {x["code"] for x in nodes_doc["nodes"]} - pre_codes
pre_edges = [e for e in edges_doc["edges"]
             if e["source"] not in b9_codes and e["target"] not in b9_codes]
endpoints = " ".join(f"{e['source']} {e['target']}"
                     for e in pre_edges).lower()
terms = rul["conflict_audit"]["s4_candidate_terms"]
matched = [t for t in terms if t in store_blob or t in endpoints]
check("B1 the recorded 46-match audit reproduces on the pre-batch-9 store "
      "(registry state the ruling was recorded against)",
      len(matched) == 46, f"matched = {len(matched)}")
check("B2 the ruling records a disposition for every matched term",
      {d["term"] for d in rul["match_dispositions"]} == set(matched)
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
check("C max_boundary_edges honoured (exactly 5 sanctioned targets)",
      len(targets) == 5
      and rul["boundary_edge_ruling"]["max_boundary_edges"] == 5)

# ---------------------------------------------------------------------------
# D. discipline invariants
# ---------------------------------------------------------------------------
expected_nodes = 165 + (15 if B9_RECORD.exists() else 0) \
+ (8 if B10_RECORD.exists() else 0)
expected_edges = 384 + (41 if B9_RECORD.exists() else 0) \
+ (34 if B10_RECORD.exists() else 0)
expected_partof = 163 + (21 if B9_RECORD.exists() else 0) \
+ (15 if B10_RECORD.exists() else 0)
check("D1 the ruling mints no node beyond the sanctioned batch-9 authoring",
      len(live_codes) == expected_nodes,
      f"live = {len(live_codes)}, expected = {expected_nodes}")
check("D2 the ruling mints no edge beyond the sanctioned batch-9 authoring",
      len(edges_doc["edges"]) == expected_edges
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF") == expected_partof)
hv = sum(1 for e in edges_doc["edges"]
         if e["validation_status"] == "HUMAN_VALIDATED"
         and e["relation"] != "PART_OF")
# session-63 re-anchor (dated): the batch-9 verdicts were APPLIED through
# §18 at session 63 (20 operator promotions, c11_batch9_verdicts, via the
# B9 diff-review bundle — the operator's completed-sheet §6/§7 verdict:
# PASS WITH NOTES); the semantic HV count moved 216 -> 236; the ruling's
# protected property is unchanged (it still mints nothing).
check("D3 semantic HV at the operator-promoted count (236; the batch-9 "
      "authoring promoted nothing and the ruling itself still mints "
      "nothing — promotion happened only at the operator's verdict gate "
      "via §18 at session 63; PART_OF HV rides the T-C19 G19 record)",
      hv == 236)
check("D4 non_goals recorded (no ontology redesign / no re-opening / no "
      "re-scope / no promotion authority / no direct writes)",
      len(rul.get("non_goals", [])) >= 5)
# the negative control stays untouched by the ruling and the batch
n415_nodes = [x for x in nodes_doc["nodes"]
              if any(sp.get("code") == "4CH1-4.15"
                     for sp in x.get("spec_points", []))]
n415_edges = [e for e in edges_doc["edges"]
              if any("4.15" in a.get("file", "")
                     for a in e.get("evidence", []))]
check("D5 the 4CH1-4.15 negative control stays uncovered (zero node/edge "
      "attachments through the ruling and the batch)",
      len(n415_nodes) == 0 and len(n415_edges) == 0)

# ---------------------------------------------------------------------------
print()
if fails:
    print(f"FAILED: {len(fails)} check(s): {fails}")
    raise SystemExit(1)
print(f"c11_batch9_boundary_check: ALL PASS — the cross-slice boundary "
      f"ruling (session 62) is schema-valid, its 46-match dispositioned "
      f"audit reproduces on the pre-batch-9 store, every sanctioned "
      f"boundary target exists with exact ownership, and the ruling mints "
      f"and promotes nothing beyond the sanctioned batch-9 "
      f"authored-to-gate record.")
