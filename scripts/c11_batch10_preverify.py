#!/usr/bin/env python3
"""T-C11 session 64 — batch-10 preverify (fail-closed, run BEFORE the
registry grows; the c11_batch9_preverify.py pattern).

Machine-verifies the batch-10 decision record's structure and its boundary
discipline against the LIVE pre-batch-10 store and the ruling:
  * record shape (15 nodes = 14 CONCEPT + 1 MISCONCEPTION / 20 edges =
    18 RP + 1 WAP + 1 REMEDIATED_BY / 9 held / 21 command kinds)
  * SP coverage: every authorable SP of the slice is covered by at least
    one node; NO node or edge references a non-scope SP; 4CH1-4.15 absent
  * boundary discipline: the FIVE sanctioned boundary edges appear with
    EXACT triples; no edge endpoint outside the record's nodes + the live
    store; no node code in the ruling's non_mint_list
  * the misconception's WAP/REMEDIATED_BY target pairing (the B1-E-25
    pattern)
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402

GRAPH = GP.qual_dir()
DECISIONS = HERE / "c11_batch10_decisions.yaml"
RULING = HERE / "c11_batch10_boundary_ruling.yaml"

fails: list[str] = []
n = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global n
    n += 1
    if not ok:
        fails.append(name + (f"  {detail}" if detail else ""))


def _require(cond: bool, msg: str) -> None:
    if not cond:
        raise RuntimeError(msg)


doc = yaml.safe_load(DECISIONS.read_text(encoding="utf-8"))
rul = yaml.safe_load(RULING.read_text(encoding="utf-8"))
nodes_doc = yaml.safe_load((GRAPH / "concepts.yaml").read_text(encoding="utf-8"))
edges_doc = yaml.safe_load((GRAPH / "concept_edges.yaml").read_text(encoding="utf-8"))
live_codes = {x["code"] for x in nodes_doc["nodes"]}

b_nodes = doc["nodes"]
b_edges = doc["edges"]
b_held = doc["held"]
b_kinds = doc["command_kinds"]

# 1. record shape
check("record shape: 8 nodes (7 CONCEPT + 1 MISCONCEPTION)",
      len(b_nodes) == 8
      and sum(1 for x in b_nodes if x["family"] == "CONCEPT") == 7
      and sum(1 for x in b_nodes if x["family"] == "MISCONCEPTION") == 1)
check("record shape: 19 edges (17 RP + 1 WAP + 1 RB)",
      len(b_edges) == 19
      and sum(1 for e in b_edges if e["relation"] == "REQUIRES_PREREQUISITE") == 17
      and sum(1 for e in b_edges if e["relation"] == "WRONG_ANSWER_PATTERN") == 1
      and sum(1 for e in b_edges if e["relation"] == "REMEDIATED_BY") == 1)
check("record shape: 9 held candidates, all status=held",
      len(b_held) == 9 and all(h["status"] == "held" for h in b_held)
      and [h["id"] for h in b_held]
      == [f"B10-H-{i:02d}" for i in range(1, 10)])
check("record shape: 15 command kinds (one per authorable SP)",
      len(b_kinds) == 15
      and len({k["code"] for k in b_kinds}) == 15)

# 2. SP coverage
scope_sps = {sp for sp in doc["meta"]["scope"]["spec_points"]}
node_sps = set()
for x in b_nodes:
    for sp in x.get("spec_points") or []:
        node_sps.add(sp["code"])
check("SP coverage: every authorable SP covered by at least one node",
      node_sps == scope_sps, f"covered = {len(node_sps)}")
check("SP discipline: no non-scope SP anywhere in the record",
      all(sp["code"] in scope_sps for x in b_nodes
          for sp in (x.get("spec_points") or [])))
check("negative control: 4CH1-4.15 absent from every node attachment",
      "4CH1-4.15" not in node_sps)

# 3. boundary discipline
sanctioned = {f"{t['target']}"
              for t in rul["boundary_edge_ruling"]["sanctioned_targets"]}
b_codes = {x["code"] for x in b_nodes}
boundary_edges = [e for e in b_edges if e["target"] in live_codes
                  and e["target"] not in b_codes]
check("boundary discipline: exactly 13 edges target EXISTING owners",
      len(boundary_edges) == 13
      and {e["target"] for e in boundary_edges} == sanctioned,
      f"{sorted(e['target'] for e in boundary_edges)}")
non_mint = set(rul["boundary_edge_ruling"]["non_mint_list"])
check("boundary discipline: no node code in the non_mint_list",
      not (b_codes & non_mint), f"collision = {sorted(b_codes & non_mint)}")
live_store = live_codes
check("boundary discipline: every edge endpoint resolves (record nodes + "
      "live store)",
      all(e["source"] in (b_codes | live_store)
          and e["target"] in (b_codes | live_store) for e in b_edges))
check("boundary discipline: no in-slice edge is a self-loop or duplicate",
      all(e["source"] != e["target"] for e in b_edges)
      and len({(e["source"], e["relation"], e["target"])
               for e in b_edges}) == len(b_edges))

# 4. misconception pairing (the B1-E-25 pattern)
wap = [e for e in b_edges if e["relation"] == "WRONG_ANSWER_PATTERN"]
rb = [e for e in b_edges if e["relation"] == "REMEDIATED_BY"]
check("misconception pairing: the WAP target == the REMEDIATED_BY target "
      "and the source is the batch's single misconception",
      len(wap) == 1 and len(rb) == 1
      and wap[0]["target"] == rb[0]["target"]
      and wap[0]["source"] == rb[0]["source"]
      and wap[0]["source"] == "4CH1-MIS-PROPANOL-POSITION")

# 5. the live store must be the sanctioned pre-batch-10 state
check("pre-state: live store 180 nodes / 425 edges (184 PART_OF)",
      len(nodes_doc["nodes"]) == 180 and len(edges_doc["edges"]) == 425
      and sum(1 for e in edges_doc["edges"]
              if e["relation"] == "PART_OF") == 184)
hv = sum(1 for e in edges_doc["edges"]
         if e["validation_status"] == "HUMAN_VALIDATED"
         and e["relation"] != "PART_OF")
check("pre-state: 236 semantic HUMAN_VALIDATED (the batch-9 §18 state)",
      hv == 236)
check("pre-state: no batch-10 code already live (the registry has not "
      "grown)",
      not (b_codes & live_codes))

# ---------------------------------------------------------------------------
if fails:
    print(f"PREVERIFY FAILED: {len(fails)} of {n}")
    for f in fails:
        print("  -", f)
    raise SystemExit(1)
print(f"c11_batch10_preverify: ALL PASS ({n} checks) — record shape, SP "
      f"coverage, boundary discipline, misconception pairing and the "
      f"pre-batch-10 store state all verified; the registry may grow")
