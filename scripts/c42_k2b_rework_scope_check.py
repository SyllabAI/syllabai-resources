#!/usr/bin/env python3
"""c42_k2b_rework_scope_check.py — T-C42 verification battery.

Zero-LLM, deterministic, read-only toward graph/, the SME corpora and
parsed/** (the resolution substrate is read through the persistent git-show
channel; the sparse corpus is not required on disk). Writes exactly one file:
its own report, graph/reports/C42_K2B_REWORK_SCOPE_CHECK.json.

Gates:
  G1 baseline_state        HEAD == 720b86b; maths-a registry == the 9-store K2
                           exit shape; predecessor records present with pinned
                           sha256_16s.
  G2 defect_inventory      the C40 verdict record re-census: 468 rows, 351/117,
                           roots 101 note-level + 16 section-level, 45 distinct
                           defective joins / 45 notes / 36 codes, section-level
                           over 10 notes; fill-record JSON agrees; gate FAIL.
  G3 resolution_substrate  counts 222/218/4 == observed (4 null-code rows);
                           validation string carries AI_VALIDATED +
                           operator-delegated + T-SPEC-10 + PMT-excluded; all
                           45 defective anchors resolve in the file; every
                           currently resolved code is in the canonical 188.
  G4 blast_radius          40/45 ids with referenced_by_parts>0, sum == 996;
                           build_learner_spec_links.py consumes the maths-a
                           resolution file.
  G5 store_surface         939 rows == 860 anchored + 2 anchor-unresolved +
                           77 unmapped-SP; 189 rows on the 45 notes; 59 rows
                           on the 10 section-level notes; every row SUGGESTED;
                           111 codes covered.
  G6 protected_surfaces    concepts 82 / concept_edges 157 (84 PART_OF + 73
                           semantic, all 73 HUMAN_VALIDATED) / kinds 72; C41
                           promotions contract 73/73; chemistry 10-store shape
                           present.
  G7 scope_self_consistency the scope JSON's stages, gates and inventory
                           numbers equal the live census of G2/G5; state
                           snapshot recorded.

Exit 0 iff every gate PASS.
"""
import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
REPORT = REPO / "graph/reports/C42_K2B_REWORK_SCOPE_CHECK.json"
SCOPE_JSON = REPO / "graph/reports/C42_IGCSE_MATHS_A_K2B_REWORK_SCOPE.json"
VERDICTS = REPO / "scripts/c40_maths_a_substrate_review_verdicts.yaml"
FILL_JSON = REPO / "graph/reports/C40_MATHS_A_K2B_REVIEW_FILL_RECORD.json"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
JOIN = REPO / "Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json"
K1 = REPO / "graph/igcse-maths-a/specification_points.yaml"
RESOLUTION_GIT = "SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json"

PINS = {
    "graph/reports/C39_IGCSE_MATHS_A_K2C_APPLY_RECORD.md": "8ca58016bcf03bed",
    "graph/reports/C40_IGCSE_MATHS_A_K2B_LANE_B_RECORD.md": "9c36b38342930e93",
    "graph/reports/C40_MATHS_A_CHUNK_SP_SUBSTRATE_REPORT.md": "ab7e15cb0ffa7f50",
    "graph/reports/C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md": "c625b4b06025dc7f",
    "graph/reports/C40_MATHS_A_K2B_REVIEW_FILL_RECORD.md": "c7545e154c4a10ed",
    "scripts/c40_maths_a_substrate_review_verdicts.yaml": "2d1aef1e95109da9",
    "graph/reports/C40_MATHS_A_K2B_LAND_CHECK.json": "1a8190738980e1d0",
    "graph/reports/C41_MATHS_A_S18_PROMOTION_RECORD.md": "402750d1c4908b10",
    "scripts/c41_maths_a_promotions.yaml": "9b40e07010cb10eb",
    "graph/reports/C41_MATHS_A_S18_PROMOTION_CHECK.json": "83e12eb6b40fa730",
    "graph/reports/C31_IGCSE_MATHS_A_K2_SCOPE.md": "8817fe36a38d93cd",
}

results = []
checks = 0


def gate(gid, name, ok, detail):
    global checks
    results.append({"gate": gid, "name": name, "result": "PASS" if ok else "FAIL", "detail": detail})
    checks += 1
    print(f"  {gid} {name}: {'PASS' if ok else 'FAIL'}")
    return ok


def sha16_path(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16]


def git_show(path: str) -> bytes:
    r = subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{path}"], capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(f"git show failed for {path}: {r.stderr[:200]}")
    return r.stdout


def main() -> int:
    print("C42 K2-B rework scope check — baseline", end=" ")
    head = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                          capture_output=True, text=True, check=True).stdout.strip()
    print(head[:12])

    # ---------- G1 baseline_state ----------
    g1 = {}
    g1_ok = head.startswith("720b86b")
    g1["head"] = head[:12]
    reg = yaml.safe_load((REPO / "scripts/graph_paths.yaml").read_text())
    maths_stores = reg["quals"]["igcse-maths-a"]["stores"]
    g1["maths_a_registry_stores"] = len(maths_stores)
    g1_ok &= len(maths_stores) == 9
    pin_fails = []
    for rel, want in PINS.items():
        got = sha16_path(REPO / rel)
        if got != want:
            pin_fails.append(f"{rel}: {got} != {want}")
    g1["pin_failures"] = pin_fails
    g1_ok &= not pin_fails
    gate("G1", "baseline_state", g1_ok, g1)

    # ---------- G2 defect_inventory ----------
    v = yaml.safe_load(VERDICTS.read_text())["verdicts"].values()
    roots = Counter(x["verdict"] for x in v)
    nl = [x for x in v if x["verdict"] == "REJECT" and x.get("root") == "note-level"]
    sl = [x for x in v if x["verdict"] == "REJECT" and x.get("root") == "section-level"]
    nl_pairs = sorted(set((x["note_path"], x["spec_code"]) for x in nl))
    sl_pairs = sorted(set((x["note_path"], x["spec_code"]) for x in sl))
    g2 = {
        "verdict_rows": len(v), "confirm": roots.get("CONFIRM", 0), "reject": roots.get("REJECT", 0),
        "note_level_reject_rows": len(nl), "section_level_reject_rows": len(sl),
        "distinct_note_level_joins": len(nl_pairs), "distinct_note_level_notes": len(set(p[0] for p in nl_pairs)),
        "distinct_wrong_codes": len(set(p[1] for p in nl_pairs)),
        "section_level_notes": len(set(p[0] for p in sl_pairs)),
    }
    fill = json.loads(FILL_JSON.read_text())
    g2["fill_record_agrees"] = {
        "rows": fill["part_a"]["total"]["rows"] == len(v),
        "confirm": fill["part_a"]["total"]["confirm"] == roots.get("CONFIRM", 0),
        "reject": fill["part_a"]["total"]["reject"] == roots.get("REJECT", 0),
        "note_level": fill["part_a"]["note_level_rejects"] == len(nl_pairs),
        "section_level_rows": fill["part_a"]["section_level_rejects"] == len(sl),
        "gate_outcome": fill["gate"]["outcome"] == "FAIL",
    }
    g2_ok = (g2["verdict_rows"] == 468 and g2["confirm"] == 351 and g2["reject"] == 117
             and g2["note_level_reject_rows"] == 101 and g2["section_level_reject_rows"] == 16
             and g2["distinct_note_level_joins"] == 45 and g2["distinct_note_level_notes"] == 45
             and g2["distinct_wrong_codes"] == 36 and g2["section_level_notes"] == 10
             and all(g2["fill_record_agrees"].values()))
    gate("G2", "defect_inventory", g2_ok, g2)

    # ---------- G3 resolution_substrate ----------
    res = json.loads(git_show(RESOLUTION_GIT))
    rows = res["resolved"]
    null_code = [r for r in rows if not r.get("resolved_code")]
    counts = res["counts"]
    val = res.get("validation", "")
    join = json.loads(JOIN.read_text())
    jrows = {r["note_path"]: r for r in join["joins"]}
    anchor_ids = {jrows[np_]["anchor_id"] for np_, _ in nl_pairs if np_ in jrows}
    k1_codes = {r["code"] for r in yaml.safe_load(K1.read_text())["specification_points"]}
    foreign = [r["resolved_code"] for r in rows
               if r.get("resolved_code") and f"4MA1-{r['resolved_code']}" not in k1_codes]
    g3 = {
        "counts_declared": counts, "observed_rows": len(rows), "null_code_rows": len(null_code),
        "validation_string_has": {
            "AI_VALIDATED": "AI_VALIDATED" in val,
            "operator-delegated": "operator-delegated" in val,
            "T-SPEC-10": "T-SPEC-10" in val,
            "PMT excluded": "PMT excluded as source" in val,
        },
        "defective_anchors_resolved": len(anchor_ids),
        "foreign_codes_today": foreign,
    }
    g3_ok = (counts == {"ids": 222, "resolved": 218, "unresolved": 4}
             and len(rows) == 222 and len(null_code) == 4
             and all(g3["validation_string_has"].values())
             and g3["defective_anchors_resolved"] == 45
             and not foreign)
    gate("G3", "resolution_substrate", g3_ok, g3)

    # ---------- G4 blast_radius ----------
    by_id = {r["id"]: r for r in rows}
    rbp = [by_id[i].get("referenced_by_parts", 0) for i in anchor_ids if i in by_id]
    g4 = {"ids_with_parts": sum(1 for x in rbp if x > 0), "sum_parts": sum(rbp),
          "spec_links_consumer": "spec_point_resolution.json"
          in (REPO / "scripts/build_learner_spec_links.py").read_text()}
    g4_ok = g4["ids_with_parts"] == 40 and g4["sum_parts"] == 996 and g4["spec_links_consumer"]
    gate("G4", "blast_radius", g4_ok, g4)

    # ---------- G5 store_surface ----------
    store = yaml.safe_load(STORE.read_text())
    srows = store["rows"]
    anchored = [r for r in srows if not r.get("disposition")]
    wl = [r for r in srows if (r.get("disposition") or "").startswith("WORKLIST")]
    wl_anchor = [r for r in wl if not r.get("spec_code")]
    wl_unmapped = [r for r in wl if r.get("spec_code")]
    bad_notes = sorted(set(p[0] for p in nl_pairs))
    sec_notes = sorted(set(p[0] for p in sl_pairs))
    rows_on_bad = sum(1 for r in srows if r.get("note_path") in bad_notes)
    rows_on_sec = sum(1 for r in srows if r.get("note_path") in sec_notes)
    statuses = Counter(r.get("validation_status") for r in srows)
    covered = sorted(set(r["spec_code"] for r in anchored))
    g5 = {
        "rows_total": len(srows), "anchored": len(anchored), "worklist": len(wl),
        "worklist_anchor_unresolved": len(wl_anchor), "worklist_unmapped_sps": len(wl_unmapped),
        "rows_on_45_defective_notes": rows_on_bad, "rows_on_10_section_notes": rows_on_sec,
        "validation_statuses": dict(statuses), "codes_covered": len(covered),
    }
    g5_ok = (g5["rows_total"] == 939 and g5["anchored"] == 860 and g5["worklist"] == 79
             and g5["worklist_anchor_unresolved"] == 2 and g5["worklist_unmapped_sps"] == 77
             and rows_on_bad == 189 and rows_on_sec == 59
             and set(statuses) == {"SUGGESTED"} and len(covered) == 111)
    gate("G5", "store_surface", g5_ok, g5)

    # ---------- G6 protected_surfaces ----------
    concepts = yaml.safe_load((REPO / "graph/igcse-maths-a/concepts.yaml").read_text())
    edges = yaml.safe_load((REPO / "graph/igcse-maths-a/concept_edges.yaml").read_text())
    kinds = yaml.safe_load((REPO / "graph/igcse-maths-a/spec_command_kinds.yaml").read_text())
    promo = yaml.safe_load((REPO / "scripts/c41_maths_a_promotions.yaml").read_text())
    rel_c = Counter(e["relation"] for e in edges["edges"])
    hv = [e for e in edges["edges"]
          if e["relation"] != "PART_OF" and e.get("validation_status") == "HUMAN_VALIDATED"]
    chem_stores = reg["quals"]["igcse-chemistry"]["stores"]
    g6 = {
        "concept_nodes": len(concepts["nodes"]), "edge_rows": len(edges["edges"]),
        "relations": dict(rel_c), "human_validated_semantic": len(hv),
        "command_kinds": len(kinds["command_kinds"]), "promotions": len(promo["promotions"]),
        "chemistry_stores": len(chem_stores),
    }
    g6_ok = (g6["concept_nodes"] == 82 and g6["edge_rows"] == 157
             and rel_c.get("PART_OF") == 84 and rel_c.get("REQUIRES_PREREQUISITE") == 51
             and rel_c.get("WRONG_ANSWER_PATTERN") == 11 and rel_c.get("REMEDIATED_BY") == 11
             and g6["human_validated_semantic"] == 73 and g6["command_kinds"] == 72
             and g6["promotions"] == 73 and g6["chemistry_stores"] == 10)
    gate("G6", "protected_surfaces", g6_ok, g6)

    # ---------- G7 scope_self_consistency ----------
    scope = json.loads(SCOPE_JSON.read_text())
    lanes = sorted(scope.get("rework_lane", {}).keys())
    gates = scope.get("operator_gates", [])
    inv = scope.get("defect_inventory", {})
    g7 = {
        "stages": lanes,
        "operator_gates": [g.get("stage") for g in gates],
        "inventory_matches_live": {
            "part_a_rows": inv.get("part_a_rows") == 468,
            "note_level_joins": inv.get("note_level", {}).get("distinct_joins") == 45,
            "wrong_codes": inv.get("note_level", {}).get("distinct_wrong_codes") == 36,
            "store_rows_riding": inv.get("note_level", {}).get("store_rows_riding") == rows_on_bad,
            "section_store_rows": inv.get("section_level", {}).get("store_rows_on_those_notes") == rows_on_sec,
            "blast_radius_sum": scope.get("scoping_discovery", {}).get("blast_radius", {})
            .get("eq_part_references_on_45_ids") == g4["sum_parts"],
        },
        "state_snapshot": {"head": head[:12], "report": str(REPORT.relative_to(REPO))},
    }
    g7_ok = (lanes == sorted(["R0_eq_blast_radius_census", "R1_tspec_resolution_repair_round",
                              "R2_join_re_run", "R3_substrate_rebuild", "R4_re_gate",
                              "R5_s18_substrate_apply"])
             and [g.get("stage") for g in gates] == ["R1", "R4", "R5"]
             and all(g7["inventory_matches_live"].values()))
    gate("G7", "scope_self_consistency", g7_ok, g7)

    report = {
        "schema": "syllabai.c42-k2b-rework-scope-check/1.0",
        "task": "T-C42",
        "generated_utc": subprocess.run(["git", "-C", str(REPO), "log", "-1", "--format=%cI"],
                                        capture_output=True, text=True, check=True).stdout.strip(),
        "head": head,
        "gates": results,
        "all_pass": all(r["result"] == "PASS" for r in results),
        "gates_run": checks,
    }
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(f"report -> {REPORT.relative_to(REPO)}  all_pass={report['all_pass']}")
    return 0 if report["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
