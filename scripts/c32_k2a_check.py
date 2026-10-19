#!/usr/bin/env python3
"""c32_k2a_check.py — T-C32 (K2-A) Lane A machine verification for igcse-maths-a.

Verifies the Lane A build (operator gate K2-A of the C31 K2 scope) against
the live repo. Zero-LLM, deterministic; READ-ONLY toward the graph, the
corpora and the parsed canonical plane — it writes only its own report
(graph/reports/C32_K2A_CHECK.json).

  G1  artifact_schema_counts     the derived join artifact re-censused from
                                 its own rows: 203 anchors == joins +
                                 unresolved; 202 joined / 1 unresolved /
                                 111 distinct codes; tier splits recomputed
  G2  provenance_verbatim        every join row's copied fields byte-equal
                                 to the live resolution substrate row
                                 (the sme_notes_chem_join.py 1:1 rule);
                                 input sha pins match
  G3  store_agreement            every resolved_code in the canonical 188
                                 (foreign = hard FAIL); store_row_code and
                                 store_global_order agree with the live K1
                                 store; per-row wording_check class
                                 recomputed and equal
  G4  residual_not_fabricated    exactly 1 unresolved anchor, no resolved
                                 code anywhere on it, PROPOSAL-ONLY method
                                 string, top proposal below the chemistry
                                 0.75 auto-join floor -> operator
                                 adjudication required
  G5  freeze_integrity           HEAD == the T-C31 landing baseline; git
                                 status shows NO tracked modifications and
                                 NO untracked paths outside the T-C32
                                 footprint — corpora, canonical parsed
                                 bundle, chemistry and maths-a stores are
                                 byte-identical to baseline
  G6  no_store_or_registry_change registry sha unchanged; graph/ tree
                                 unchanged (Lane A earns no store bytes — P3)
  G7  standing_checkers_green    graph_check.py and check_no_hardcode.py
                                 exit 0 on the post-build tree

Usage:
    python3 scripts/c32_k2a_check.py
    # emits graph/reports/C32_K2A_CHECK.json; exit 0 iff all gates PASS
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QUAL = "igcse-maths-a"
COURSE = "igcse-maths-a-18-higher"
ARTIFACT = ("Official-Specifications/parsed/_derived/notes-join/"
            "igcse-maths-a-18-higher.json")
RESOLUTION = f"SME-ExamQuestion/{COURSE}/spec_point_resolution.json"
SP_STORE = f"graph/{QUAL}/specification_points.yaml"
LEDGER = "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"
REPORT = REPO / "graph" / "reports" / "C32_K2A_CHECK.json"

BASELINE_HEAD = "49d71ba"  # T-C31 K2 SCOPED landing (short sha; G5 compares prefix)

T_C32_FOOTPRINT = {
    "scripts/c32_notes_maths_a_join.py",
    "scripts/c32_k2a_check.py",
    ARTIFACT,
    "graph/reports/C32_IGCSE_MATHS_A_K2A_LANE_A_RECORD.md",
    "graph/reports/C32_IGCSE_MATHS_A_K2A_LANE_A_RECORD.json",
    "graph/reports/C32_K2A_CHECK.json",
}

COPIED_FIELDS = ["resolved_code", "official_id", "official_wording",
                 "sme_name", "sme_definition", "tier", "method", "score",
                 "unit", "referenced_by_parts"]


def sha16(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:16]


def read_bytes(rel: str) -> bytes:
    """disk-first with git-show fallback (the C28-F1 sparse-workspace
    mechanism — the EQ corpus is not materialized in this checkout)."""
    p = REPO / rel
    if p.is_file():
        return p.read_bytes()
    out = subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{rel}"],
                         capture_output=True)
    if out.returncode != 0:
        raise FileNotFoundError(rel)
    return out.stdout


def norm(s: str) -> str:
    return " ".join((s or "").split())


def main() -> int:
    gates: dict[str, dict] = {}

    def gate(g: str, ok: bool, detail: dict) -> None:
        gates[g] = {"status": "PASS" if ok else "FAIL", **detail}

    head = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    artifact = json.loads((REPO / ARTIFACT).read_text(encoding="utf-8"))
    resolution = json.loads(read_bytes(RESOLUTION).decode("utf-8"))
    sp = yaml.safe_load((REPO / SP_STORE).read_text(encoding="utf-8"))
    ledger_rows = json.loads((REPO / LEDGER).read_text(encoding="utf-8"))["rows"]

    # ---- G1: artifact schema + re-census ------------------------------------
    try:
        joins = artifact["joins"]
        unresolved = artifact["unresolved"]
        d_codes = sorted({j["resolved_code"] for j in joins})
        by_code = {row["official_code"]: row for row in
                   next(v for v in sp.values()
                        if isinstance(v, list) and v and isinstance(v[0], dict))}
        tier = {}
        for code in d_codes:
            t = (by_code[code].get("applicability") or {}).get("tier")
            tier[t] = tier.get(t, 0) + 1
        obs = {
            "anchors_total": len(joins) + len(unresolved),
            "joined": len(joins),
            "unresolved": len(unresolved),
            "distinct_codes": len(d_codes),
            "tier_split": tier,
            "foreign": sorted(set(d_codes) - set(by_code)),
        }
        declared = artifact["counts"]
        checks = {
            "schema": artifact.get("schema") == "syllabai.notes-spec-point-join/1.0",
            "task": "T-C32" in str(artifact.get("task", "")),
            "anchors_203": obs["anchors_total"] == 203,
            "joined_202": obs["joined"] == 202,
            "unresolved_1": obs["unresolved"] == 1,
            "distinct_111": obs["distinct_codes"] == 111,
            "declared_matches_observed":
                declared["joined"] == obs["joined"]
                and declared["unresolved_recorded"] == obs["unresolved"]
                and declared["distinct_official_codes"] == obs["distinct_codes"],
            "tier_split_matches_scoping": tier == {"Foundation": 57, "Higher": 54},
            "foreign_zero": not obs["foreign"],
            "validation_tier_present": "INHERITED" in artifact.get("validation_tier", "")
                and "NO HUMAN_VALIDATED claim" in artifact.get("validation_tier", ""),
        }
        gate("G1_artifact_schema_counts", all(checks.values()),
             {"observed": obs, "checks": checks})
    except Exception as exc:  # noqa: BLE001
        gate("G1_artifact_schema_counts", False, {"error": repr(exc)})
        joins, unresolved, by_code = [], [], {}

    # ---- G2: provenance verbatim --------------------------------------------
    try:
        res_map = {x["id"]: x for x in resolution.get("resolved") or []}
        mismatches, checked = [], 0
        for j in joins:
            row = res_map.get(j["anchor_id"])
            if row is None:
                mismatches.append({"anchor_id": j["anchor_id"], "err": "absent"})
                continue
            checked += 1
            for f in COPIED_FIELDS:
                if j.get(f) != row.get(f):
                    mismatches.append({"anchor_id": j["anchor_id"],
                                       "field": f,
                                       "artifact": j.get(f),
                                       "substrate": row.get(f)})
        pins = {
            "resolution_pin": artifact["inputs"]["resolution"]["sha256_16"]
            == sha16(read_bytes(RESOLUTION)),
            "fuzzy_false": all(j["provenance"]["fuzzy_matching_used"] is False
                               for j in joins),
            "copied_1to1_true": all(j["provenance"]["copied_1to1"] is True
                                    for j in joins),
        }
        gate("G2_provenance_verbatim", not mismatches and all(pins.values()),
             {"rows_checked": checked, "field_mismatches": mismatches[:10],
              "pins": pins})
    except Exception as exc:  # noqa: BLE001
        gate("G2_provenance_verbatim", False, {"error": repr(exc)})

    # ---- G3: store agreement + wording classes -------------------------------
    try:
        ledger_map = {x["official_code"]: x for x in ledger_rows}
        bad, wc_bad = [], []
        for j in joins:
            row = by_code.get(j["resolved_code"])
            if row is None:
                bad.append({"code": j["resolved_code"], "err": "not canonical"})
                continue
            if j["store_row_code"] != row["code"] or \
                    j["store_global_order"] != row["global_order"]:
                bad.append({"code": j["resolved_code"], "err": "store row drift"})
            rw = norm(j.get("official_wording"))
            sw = norm(row.get("official_wording"))
            if rw == sw:
                wc = "EXACT"
            else:
                lrow = ledger_map.get(j["resolved_code"])
                wc = "LEDGER_EXPLAINABLE" if lrow and \
                    rw == norm(lrow["foundation"]["text"]) and \
                    sw == norm(lrow["higher"]["text"]) else "DIVERGENT"
            if wc != j["wording_check"]:
                wc_bad.append({"code": j["resolved_code"],
                               "recorded": j["wording_check"],
                               "recomputed": wc})
        gate("G3_store_agreement", not bad and not wc_bad,
             {"rows_checked": len(joins), "store_disagreements": bad[:10],
              "wording_class_disagreements": wc_bad[:10],
              "wording_census_recorded": artifact["counts"]["wording_check_census"]})
    except Exception as exc:  # noqa: BLE001
        gate("G3_store_agreement", False, {"error": repr(exc)})

    # ---- G4: residual not fabricated -----------------------------------------
    try:
        u = unresolved[0] if unresolved else {}
        props = (u.get("disposition_proposals") or [{}])[0]
        tops = props.get("top_candidates") or []
        checks = {
            "exactly_one": len(unresolved) == 1,
            "anchor_id": u.get("anchor_id") == "spcpt_QWXhzVp2S3VYZdZc",
            "sme_name": u.get("sme_name") == "Discrete & Continuous Data",
            "no_resolved_code": not any(k in u for k in
                                        ("resolved_code", "official_id",
                                         "official_wording")),
            "status_recorded": "UNRESOLVED" in u.get("status", "")
                and "NEVER FABRICATED" in u.get("status", ""),
            "proposal_only": "PROPOSAL-ONLY" in props.get("method", ""),
            "top_below_auto_join_floor":
                bool(tops) and tops[0]["score"] < 0.75,
        }
        gate("G4_residual_not_fabricated", all(checks.values()),
             {"checks": checks,
              "top_proposal": {"code": tops[0]["official_code"],
                               "score": tops[0]["score"],
                               "margin": props.get("top_score_margin")}
              if tops else None,
              "ruling": "operator adjudication required; the anchor stays "
                        "unresolved in the artifact"})
    except Exception as exc:  # noqa: BLE001
        gate("G4_residual_not_fabricated", False, {"error": repr(exc)})

    # ---- G5: freeze integrity -------------------------------------------------
    try:
        status = subprocess.run(
            ["git", "-C", str(REPO), "status", "--porcelain", "-uall"],
            capture_output=True, text=True).stdout.splitlines()
        mods, unexpected = [], []
        for line in status:
            x, path = line[:2], line[3:].strip()
            if x.strip() == "M" or x in ("MM", "AM", "MD"):
                mods.append(path)
            if path not in T_C32_FOOTPRINT:
                unexpected.append(f"{x} {path}")
        corpus_touched = [p for p in status
                          if "SME-RevisionNotes/" in p or "SME-ExamQuestion/" in p
                          or "parsed/igcse-maths-a/" in p
                          or "graph/igcse-chemistry/" in p
                          or "graph/igcse-maths-a/" in p]
        gate("G5_freeze_integrity",
             head.startswith(BASELINE_HEAD) and not mods and not unexpected
             and not corpus_touched,
             {"head": head, "baseline_prefix": BASELINE_HEAD,
              "tracked_modifications": mods,
              "unexpected_paths": unexpected[:10],
              "guarded_dir_entries": corpus_touched,
              "t_c32_footprint": sorted(T_C32_FOOTPRINT)})
    except Exception as exc:  # noqa: BLE001
        gate("G5_freeze_integrity", False, {"error": repr(exc)})

    # ---- G6: no store or registry change --------------------------------------
    try:
        reg_sha = sha16((REPO / "scripts/graph_paths.yaml").read_bytes())
        status = subprocess.run(
            ["git", "-C", str(REPO), "status", "--porcelain", "-uall"],
            capture_output=True, text=True).stdout.splitlines()
        graph_status = [line[3:].strip() for line in status
                        if line[3:].strip().startswith("graph/")]
        allowed = {"graph/reports/C32_IGCSE_MATHS_A_K2A_LANE_A_RECORD.md",
                   "graph/reports/C32_IGCSE_MATHS_A_K2A_LANE_A_RECORD.json",
                   "graph/reports/C32_K2A_CHECK.json"}
        beyond = [p for p in graph_status if p not in allowed]
        gate("G6_no_store_or_registry_change",
             reg_sha == "e38965001ade4417" and not beyond,
             {"registry_sha256_16": reg_sha,
              "registry_expected": "e38965001ade4417",
              "graph_status_entries": graph_status[:10],
              "beyond_c32_records": beyond[:10]})
    except Exception as exc:  # noqa: BLE001
        gate("G6_no_store_or_registry_change", False, {"error": repr(exc)})

    # ---- G7: standing checkers green ------------------------------------------
    try:
        g = subprocess.run([sys.executable, "scripts/graph_check.py"],
                           capture_output=True, text=True)
        h = subprocess.run([sys.executable, "scripts/check_no_hardcode.py"],
                           capture_output=True, text=True)
        gate("G7_standing_checkers_green",
             g.returncode == 0 and h.returncode == 0,
             {"graph_check_exit": g.returncode,
              "graph_check_tail": g.stdout.strip().splitlines()[-1][:160]
              if g.stdout.strip() else "",
              "no_hardcode_exit": h.returncode,
              "no_hardcode_tail": h.stdout.strip().splitlines()[-1][:160]
              if h.stdout.strip() else ""})
    except Exception as exc:  # noqa: BLE001
        gate("G7_standing_checkers_green", False, {"error": repr(exc)})

    report = {
        "schema": "syllabai.c32-k2a-check/1.0",
        "task": "T-C32 (K2-A Lane A machine verification, igcse-maths-a)",
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "baseline_head": head,
        "artifact": ARTIFACT,
        "gates": gates,
        "notes": [
            "Zero-LLM, deterministic, read-only toward graph/, corpora and the",
            "parsed canonical plane; the only write is this report. The hard",
            "FAIL classes: foreign official_codes, provenance mismatches, any",
            "guarded-plane byte change, unresolved-anchor fabrication.",
        ],
    }
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                      encoding="utf-8")
    failed = [g for g, v in gates.items() if v["status"] != "PASS"]
    print(f"C32 K2-A check: {len(gates) - len(failed)}/{len(gates)} gates PASS")
    for g, v in gates.items():
        print(f"  {g}: {v['status']}")
    if failed:
        print("FAILED:", ", ".join(failed))
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
