#!/usr/bin/env python3
"""c31_k2_scope_check.py — T-C31 K2 scoping preflight for igcse-maths-a.

The operator directive "want K2 scoped" commissions the SCOPE of K2 (ratified
enrichment, C28 spec §6 row: the chemistry sequence replayed per qual), not its
execution. This checker machine-verifies, against the live repo at the scoping
baseline, every factual claim the scope record will make:

  G1  k1_stores_present        the T-C30 K1 landing is the standing substrate
                               (5 ratified spec-text stores via the C28
                               registry; 188 rows; the 8 parse-flagged codes
                               alive and flagged; K1 record + check + ledger)
  G2  lane_a_substrate         the notes↔SP join substrate the K0 record
                               called missing: SME-ExamQuestion/
                               igcse-maths-a-18-higher/spec_point_resolution.
                               json (222 ids / 218 resolved / 4 unresolved,
                               AI_VALIDATED operator-delegated) + the notes
                               corpus manifest (191 pages / 203 anchors)
  G3  anchor_join_census       deterministic id-level census of the notes'
                               spec_point_ids against the resolution file:
                               distinct ids, hits, EQ-unresolved, absent,
                               resolved official_codes vs the canonical 188
                               (foreign codes are a hard FAIL)
  G4  wording_crosscheck       for every notes-anchored resolution row:
                               whitespace-normalised official_wording vs the
                               K1 store wording — exact / tier-dedupe-
                               ledger-explainable / divergent (census; the
                               ledger explains the expected Foundation/Higher
                               split, nothing is repaired here)
  G5  batch_forecast_recompute the §16 batch plan the scope will prescribe,
                               recomputed from the live store (451/517 pilot;
                               188/301 adjusted; 16 batches @ 12 SP)
  G6  registry_k2_target_shape registry today: maths-a exactly the 5 K1
                               stores; chemistry the full 10-store shape; the
                               4 K2-delta stores and relationships absent for
                               maths-a (P3: stores arrive when earned)
  G7  state_snapshot           baseline pin + graph/ top-level shape +
                               chemistry untouched (this battery is READ-ONLY
                               toward graph/, corpora and parsed/**; it
                               writes only its own report)

Sparse-workspace note (C28-F1 mechanism): reads are disk-first with a
`git show HEAD:` fallback; every read records which method served it.

Usage:
    python3 scripts/c31_k2_scope_check.py
    # emits graph/reports/C31_K2_SCOPE_CHECK.json; exit 0 iff all gates PASS
"""
from __future__ import annotations

import hashlib
import json
import math
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QUAL = "igcse-maths-a"
COURSE = "igcse-maths-a-18-higher"
REPORT = REPO / "graph" / "reports" / "C31_K2_SCOPE_CHECK.json"

BASELINE_HEAD = "2e57663f16a478c8a0f6670140e469c2bd902ac5"

EXPECTED_FLAGGED = {"4.5D", "3.1A", "3.2B", "3.2D", "3.3A", "3.3B", "3.3E", "4.6C"}
FLAG_TAG = "math-fragment-assembly"

K1_STORES = ["specification_points", "topics", "practicals",
             "assessment_objectives", "command_words"]
K2_DELTA = ["concepts", "concept_edges", "spec_chunk_mappings", "spec_command_kinds"]
CHEM_STORES = sorted(K1_STORES + K2_DELTA + ["relationships"])

RESOLUTION = f"SME-ExamQuestion/{COURSE}/spec_point_resolution.json"
NOTES_MANIFEST = f"SME-RevisionNotes/{COURSE}/manifest.json"
LEDGER = "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"

# --- the scope-estimate model (C28 spec §6-K0(iv); c11 forecast) -----------
PILOT_NODES_PER_SP = 2.4
PILOT_EDGES_PER_SP = 2.75
ADJUSTED_NODES_PER_SP = 1.0
ADJUSTED_EDGES_PER_SP = 1.6
SP_PER_BATCH = 12


class R:
    """disk-first / git-fallback reader with provenance tracking.

    git-fallback reads are served over ONE persistent `git cat-file --batch`
    process (a per-file `git show` spawn costs ~0.5s in this workspace, which
    made the 191-note walk time out; the persistent process serves the same
    bytes at ~1ms each). Every read still records which method served it:
    'disk' or 'git-show'.
    """

    def __init__(self):
        self.methods: dict[str, str] = {}
        self._cache: dict[str, bytes] = {}
        self._proc: subprocess.Popen | None = None

    def _show(self, rel: str) -> bytes:
        if self._proc is None:
            self._proc = subprocess.Popen(
                ["git", "-C", str(REPO), "cat-file", "--batch"],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        assert self._proc.stdin is not None and self._proc.stdout is not None
        self._proc.stdin.write(f"HEAD:{rel}\n".encode())
        self._proc.stdin.flush()
        header = self._proc.stdout.readline().decode()
        parts = header.split()
        if len(parts) < 3 or parts[1] == "missing":
            raise FileNotFoundError(rel)
        size = int(parts[2])
        body = self._proc.stdout.read(size)
        self._proc.stdout.read(1)  # trailing newline after the blob
        return body

    def close(self) -> None:
        if self._proc is not None:
            try:
                self._proc.stdin.close()
                self._proc.terminate()
            except Exception:  # noqa: BLE001
                pass
            self._proc = None

    def read_bytes(self, rel: str) -> bytes:
        if rel in self._cache:
            return self._cache[rel]
        p = REPO / rel
        if p.is_file():
            self.methods[rel] = "disk"
            data = p.read_bytes()
        else:
            self.methods[rel] = "git-show"
            data = self._show(rel)
        self._cache[rel] = data
        return data

    def read_json(self, rel: str):
        return json.loads(self.read_bytes(rel).decode("utf-8"))

    def read_text(self, rel: str) -> str:
        return self.read_bytes(rel).decode("utf-8")


def sha16(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:16]


def norm(s: str) -> str:
    return " ".join((s or "").split())


def rows_of(d: dict, candidates: list[str]) -> list:
    for k in candidates:
        v = d.get(k)
        if isinstance(v, list) and v and isinstance(v[0], dict):
            return v
    raise KeyError(f"no row list among {candidates}")


def main() -> int:
    r = R()
    gates: dict[str, dict] = {}

    def gate(g: str, ok: bool, detail: dict) -> None:
        gates[g] = {"status": "PASS" if ok else "FAIL", **detail}

    head = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()

    # ---- G1: K1 standing substrate -----------------------------------------
    try:
        reg = yaml.safe_load(r.read_text("scripts/graph_paths.yaml"))
        ma = (reg.get("quals") or {}).get(QUAL) or {}
        ma_store_keys = sorted((ma.get("stores") or {}).keys())
        g1_ok = ma_store_keys == sorted(K1_STORES)
        g1_detail: dict = {"registry_store_keys": ma_store_keys}

        sp_rel = ma["stores"]["specification_points"].replace("{QUAL}", QUAL)
        sp = yaml.safe_load(r.read_text(sp_rel))
        sp_rows = rows_of(sp, ["specification_points", "rows", "points"])
        codes = [row["official_code"] for row in sp_rows]
        flagged = sorted(row["official_code"] for row in sp_rows
                         if row.get("damage_flags")
                         and FLAG_TAG in row["damage_flags"])
        g1_detail.update({
            "spec_points_rows": len(sp_rows),
            "unique_official_codes": len(set(codes)),
            "flagged_rows": flagged,
            "flagged_expected": sorted(EXPECTED_FLAGGED),
        })
        g1_ok = g1_ok and len(sp_rows) == 188 and len(set(codes)) == 188 \
            and flagged == sorted(EXPECTED_FLAGGED)

        topics_rel = ma["stores"]["topics"].replace("{QUAL}", QUAL)
        tp = yaml.safe_load(r.read_text(topics_rel))
        topic_rows = [x for x in rows_of(tp, ["topics", "rows"])
                      if "-" not in str(x.get("code", "")).replace("4MA1-S", "")]
        sub_rows = rows_of(tp, ["subtopics", "sub_topics", "rows"]) \
            if "subtopics" in tp or "sub_topics" in tp else \
            [x for x in rows_of(tp, ["topics", "rows"])
             if x not in topic_rows]
        g1_detail["topics_store"] = {"topics": len(topic_rows),
                                     "subtopics": len(sub_rows)}
        g1_ok = g1_ok and len(topic_rows) == 6 and len(sub_rows) == 39

        for rel in ("graph/reports/C30_IGCSE_MATHS_A_K1_SPEC_STORE_BUILD_RECORD.md",
                    "graph/reports/C30_K1_CHECK.json", LEDGER):
            g1_detail[rel] = sha16(r.read_bytes(rel))
        gates_present = all(k in g1_detail for k in
                            ("graph/reports/C30_IGCSE_MATHS_A_K1_SPEC_STORE_BUILD_RECORD.md",
                             "graph/reports/C30_K1_CHECK.json", LEDGER))
        gate("G1_k1_stores_present", g1_ok and gates_present, g1_detail)
        registry, sp_store = reg, sp_rows
    except Exception as exc:  # noqa: BLE001
        gate("G1_k1_stores_present", False, {"error": repr(exc)})
        registry, sp_store = {}, []

    # ---- G2: Lane-A substrate ----------------------------------------------
    try:
        res = r.read_json(RESOLUTION)
        res_rows = res.get("resolved") or []
        with_code = [x for x in res_rows if x.get("resolved_code")]
        without = [x for x in res_rows if not x.get("resolved_code")]
        counts = res.get("counts") or {}
        validation = res.get("validation") or ""
        g2_detail = {
            "resolution_schema": res.get("schema"),
            "counts_declared": counts,
            "counts_observed": {"ids": len(res_rows),
                                "resolved": len(with_code),
                                "unresolved": len(without)},
            "validation_has_ai_validated": "AI_VALIDATED" in validation,
            "validation_has_operator_delegated": "operator-delegated" in validation,
            "validation_pmt_excluded": "PMT excluded" in validation,
            "sha16": sha16(r.read_bytes(RESOLUTION)),
        }
        g2_ok = (counts.get("ids") == 222 and counts.get("resolved") == 218
                 and counts.get("unresolved") == 4
                 and len(res_rows) == 222 and len(with_code) == 218
                 and len(without) == 4
                 and "AI_VALIDATED" in validation
                 and "operator" in validation)

        nm = r.read_json(NOTES_MANIFEST)
        nc = nm.get("counts") or {}
        g2_detail["notes_manifest"] = {
            "course_slug": nm.get("course_slug"),
            "counts": nc,
            "sha16": sha16(r.read_bytes(NOTES_MANIFEST)),
        }
        g2_ok = g2_ok and nm.get("course_slug") == COURSE \
            and nc.get("pages_scraped") == 191 and nc.get("fetch_failures") == 0 \
            and nc.get("spec_point_links") == 203
        gate("G2_lane_a_substrate", g2_ok, g2_detail)
        resolution, notes_manifest = res, nm
    except Exception as exc:  # noqa: BLE001
        gate("G2_lane_a_substrate", False, {"error": repr(exc)})
        resolution, notes_manifest = {}, {}

    # ---- G3: anchor join census --------------------------------------------
    try:
        pages = notes_manifest.get("pages") or []
        anchors_by_note: dict[str, list] = {}
        anchors_total = 0
        for p in pages:
            rel = f"SME-RevisionNotes/{COURSE}/{p['path']}"
            note = json.loads(r.read_bytes(rel).decode("utf-8"))
            ids = note.get("spec_point_ids") or []
            if ids:
                anchors_by_note[p["path"]] = [str(i) for i in ids]
                anchors_total += len(ids)
        distinct_ids = sorted({i for ids in anchors_by_note.values() for i in ids})

        res_map = {x["id"]: x for x in (resolution.get("resolved") or [])}
        hits, unresolved_ids, missing_ids = [], [], []
        for i in distinct_ids:
            row = res_map.get(i)
            if row is None:
                missing_ids.append(i)
            elif not row.get("resolved_code"):
                unresolved_ids.append({"id": i, "sme_name": row.get("sme_name")})
            else:
                hits.append(row)

        canonical = {row["official_code"] for row in sp_store}
        anchored_codes = sorted({x["resolved_code"] for x in hits})
        foreign = sorted(set(anchored_codes) - canonical)

        g3_detail = {
            "pages_with_anchors": len(anchors_by_note),
            "anchors_total": anchors_total,
            "distinct_anchor_ids": len(distinct_ids),
            "ids_resolved": len(hits),
            "ids_eq_unresolved": unresolved_ids,
            "ids_absent_from_resolution": missing_ids,
            "distinct_anchored_official_codes": len(anchored_codes),
            "canonical_sp_codes": len(canonical),
            "coverage_of_188": f"{len(anchored_codes)}/188",
            "foreign_codes": foreign,
        }
        gate("G3_anchor_join_census", not foreign, g3_detail)
    except Exception as exc:  # noqa: BLE001
        gate("G3_anchor_join_census", False, {"error": repr(exc)})
        hits, anchored_codes = [], []

    # ---- G4: wording crosscheck --------------------------------------------
    try:
        store_wording = {row["official_code"]: row.get("official_wording") or ""
                         for row in sp_store}
        ledger_rows = r.read_json(LEDGER).get("rows") or []
        ledger = {x["official_code"]: x for x in ledger_rows}

        exact, explainable, divergent = 0, 0, []
        for x in hits:
            code = x["resolved_code"]
            rw = norm(x.get("official_wording") or "")
            sw = norm(store_wording.get(code, ""))
            if rw == sw:
                exact += 1
                continue
            lrow = ledger.get(code)
            if lrow and rw == norm(lrow["foundation"]["text"]) \
                    and sw == norm(lrow["higher"]["text"]):
                explainable += 1
            else:
                divergent.append({"code": code, "resolution": rw[:120],
                                  "store": sw[:120]})
        g4_detail = {
            "anchored_rows_checked": len(hits),
            "exact": exact,
            "tier_dedupe_ledger_explainable": explainable,
            "divergent": divergent,
            "ledger_rows": len(ledger_rows),
            "note": "census gate — divergences are recorded, never repaired here",
        }
        gate("G4_wording_crosscheck", True, g4_detail)
    except Exception as exc:  # noqa: BLE001
        gate("G4_wording_crosscheck", False, {"error": repr(exc)})

    # ---- G5: batch forecast recompute ---------------------------------------
    try:
        sp_base = len(sp_store)
        pilot_nodes = int(sp_base * PILOT_NODES_PER_SP)
        pilot_edges = int(sp_base * PILOT_EDGES_PER_SP)
        adj_nodes = int(sp_base * ADJUSTED_NODES_PER_SP)
        adj_edges = round(sp_base * ADJUSTED_EDGES_PER_SP)
        batches = math.ceil(sp_base / SP_PER_BATCH)
        expected = {"pilot": (451, 517), "adjusted": (188, 301), "batches": 16}
        g5_detail = {
            "sp_base": sp_base,
            "pilot_nodes": pilot_nodes, "pilot_edges": pilot_edges,
            "adjusted_nodes": adj_nodes, "adjusted_edges": adj_edges,
            "batches": batches, "sp_per_batch": SP_PER_BATCH,
            "k0_record_figures": expected,
        }
        ok = (pilot_nodes, pilot_edges) == expected["pilot"] \
            and (adj_nodes, adj_edges) == expected["adjusted"] \
            and batches == expected["batches"] and sp_base == 188
        gate("G5_batch_forecast_recompute", ok, g5_detail)
    except Exception as exc:  # noqa: BLE001
        gate("G5_batch_forecast_recompute", False, {"error": repr(exc)})

    # ---- G6: registry K2 target shape ---------------------------------------
    try:
        chem = (registry.get("quals") or {}).get("igcse-chemistry") or {}
        chem_keys = sorted((chem.get("stores") or {}).keys())
        g6_detail = {
            "maths_a_stores": sorted((registry.get("quals") or {})
                                     .get(QUAL, {}).get("stores", {}).keys()),
            "chemistry_stores": chem_keys,
            "k2_delta_present_for_maths_a": [k for k in K2_DELTA
                                             if k in ma_store_keys],
            "relationships_present_for_maths_a": "relationships" in ma_store_keys,
            "reports_dir_shared": (ma.get("reports_dir") == chem.get("reports_dir")
                                   == "graph/reports/"),
        }
        ok = g6_detail["maths_a_stores"] == sorted(K1_STORES) \
            and chem_keys == CHEM_STORES \
            and not g6_detail["k2_delta_present_for_maths_a"] \
            and not g6_detail["relationships_present_for_maths_a"] \
            and g6_detail["reports_dir_shared"]
        gate("G6_registry_k2_target_shape", ok, g6_detail)
    except Exception as exc:  # noqa: BLE001
        gate("G6_registry_k2_target_shape", False, {"error": repr(exc)})

    # ---- G7: state snapshot --------------------------------------------------
    try:
        graph_top = sorted(p.name for p in (REPO / "graph").iterdir()
                           if p.is_dir())
        chem_dir = REPO / "graph" / "igcse-chemistry"
        chem_count = len([p for p in chem_dir.glob("*.yaml")]) \
            if chem_dir.is_dir() else None
        g7_detail = {
            "baseline_head": BASELINE_HEAD,
            "observed_head": head,
            "head_matches_baseline": head == BASELINE_HEAD,
            "graph_top_level": graph_top,
            "chemistry_store_files": chem_count,
            "battery_read_only_toward_graph_corpus_parsed": True,
            "writes": ["graph/reports/C31_K2_SCOPE_CHECK.json"],
        }
        ok = head == BASELINE_HEAD and chem_count == 10 \
            and graph_top == ["igcse-chemistry", "igcse-maths-a", "reports"]
        gate("G7_state_snapshot", ok, g7_detail)
    except Exception as exc:  # noqa: BLE001
        gate("G7_state_snapshot", False, {"error": repr(exc)})

    r.close()
    report = {
        "schema": "syllabai.c31-k2-scope-check/1.0",
        "task": "T-C31 (K2 scoping preflight, igcse-maths-a)",
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "baseline_head": head,
        "gates": gates,
        "read_methods": r.methods,
        "notes": [
            "Zero-LLM, deterministic, READ-ONLY toward graph/, SME corpora and",
            "parsed/**; the only write is this report. Foreign official_codes in",
            "G3 are the sole hard FAIL class in the census lanes; everything else",
            "the K2 scope record interprets.",
        ],
    }
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                      encoding="utf-8")

    failed = [g for g, v in gates.items() if v["status"] != "PASS"]
    print(f"C31 K2 scope preflight: {len(gates) - len(failed)}/{len(gates)} gates PASS")
    for g, v in gates.items():
        print(f"  {g}: {v['status']}")
    if failed:
        print("FAILED:", ", ".join(failed))
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
