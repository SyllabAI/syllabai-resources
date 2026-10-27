#!/usr/bin/env python3
"""c42_r6_resolution_repair_apply.py — T-C42 R6 gated merge point.

The R6 lane is the second R1-shaped verdict round (scope §7 loop), fired by the
operator directive "R1-shaped verdict round over this inventory (then R2/R3/R4
re-run)" (2026-10-02, zai-web) over the R4 re-gate's defect inventory.

Consumes the operator-owned verdict record
(scripts/c42_r6_repair_verdicts.yaml) and amends EXACTLY ONE FILE in place:
SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json
(the T-SPEC in-house precedent + the C31 §4.4 dated-exception path; the R1
amendment of the same file is the standing precedent for this round).

Fail-closed preconditions:
  P1 baseline file == the pinned git blob sha256_16 05a57b056874e8dd (the
     R1-repaired file at d141c59); idempotent skip: if the file already
     carries the R6 round marker, verify verdicts<->file agreement and exit 0
     without rewriting;
  P2 verdicts cover exactly the 10 id-level anchors of the R4 defect
     inventory (recomputed from scripts/c42_r4_fresh_verdicts.yaml roots
     {note-level, note-level-class} via the join), no dupes, no extras;
  P3 every corrected_code is a member of the canonical 188 and differs from
     the prior code; UNRESOLVED rows clear;
  P4 every ledger-cited code exists in the C30 tier-dedupe ledger;
  P5 the 4 section override keys match the R4 section-level surface exactly
     (slug+ordinal), REATTRIBUTE codes in the 188; the 3 extension rows
     validate separately (targets in the 188; current_code == the post-R6
     join-derived code, computed deterministically);
  P6 the residual verdict is present and keeps the anchor UNRESOLVED.

Row mutation matrix (nothing else changes):
  CORRECT     8 rows: resolved_code/official_id/official_wording re-pointed
              (store-sourced; Foundation codes take the bare id, Higher codes
              the H- id); repair provenance preserves the prior values
              verbatim (a pre-existing repair block, if any, moves to
              repair_history).
  UNRESOLVED  2 rows: code/id/wording cleared to null + recorded reason;
              repair provenance preserves the prior wrong values.
  residual    1 row: marker only (stays UNRESOLVED per its R1 adjudication).

Top-level: the R1 repair block moves to repair_history, a new R6 repair block
is written, a dated clause is appended to "validation", "counts" recompute
(216 -> 214 resolved, 6 -> 8 unresolved), and the two cleared ids append to
"unresolved_allowlist_note".

Also writes the R8-facing projection scripts/c42_section_overrides_r6.yaml
(derived, deterministic from the verdict record; carries the 4 verdicted + 3
extension entries, the subsumption registry, and the observations). The
derived projection is re-emitted on EVERY run (including the idempotent
verify-only path) — only the resolution file is write-once.

Usage: python3 scripts/c42_r6_resolution_repair_apply.py [--check-only]
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
RES_PATH = REPO / "SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json"
RES_GIT = "SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json"
VERDICTS = REPO / "scripts/c42_r6_repair_verdicts.yaml"
R4_FRESH = REPO / "scripts/c42_r4_fresh_verdicts.yaml"
JOIN = REPO / "Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json"
OVERRIDES_OUT = REPO / "scripts/c42_section_overrides_r6.yaml"
BASELINE_BLOB_SHA16 = "05a57b056874e8dd"

TASK = "T-C42"
ROUND = "R6"
DATE = "2026-10-02"
RECORD_REF = "graph/reports/C42_R6_RESOLUTION_REPAIR_RECORD.md"


def sha16(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:16]


def load_store() -> dict:
    pts = yaml.safe_load((REPO / "graph/igcse-maths-a/specification_points.yaml").read_text())["specification_points"]
    return {p["code"]: p for p in pts}


def load_ledger() -> dict:
    led = json.loads((REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json").read_text())
    return {r["official_code"]: r for r in led["rows"]}


def r4_surface():
    """(id anchors, section keys) derived deterministically from the R4 fresh
    verdict record — the round's declared surface. The join may be any
    post-R6 refresh: anchors cleared by R6 live in its `unresolved` list."""
    fresh = yaml.safe_load(R4_FRESH.read_text())["verdicts"]
    join = json.loads(JOIN.read_text())
    jrows = {r["note_path"]: r for r in join["joins"]}
    for u in join.get("unresolved", []):
        jrows.setdefault(u["note_path"], u)
    anchors = set()
    for x in fresh.values():
        if x["verdict"] == "REJECT" and x.get("root") in ("note-level", "note-level-class"):
            anchors.add(jrows[x["note_path"]]["anchor_id"])
    sections = sorted(set((x["note_path"].split("/")[-1].replace(".json", ""), x["chunk_ordinal"])
                          for x in fresh.values()
                          if x["verdict"] == "REJECT" and x.get("root") == "section-level"))
    return anchors, sections


def statement_fields(code: str, source: str, store: dict, ledger: dict):
    p = store[code]
    tier = (p.get("applicability") or {}).get("tier")
    if source == "ledger":
        lr = ledger[code.split("-", 1)[1]]
        return "IGCSE_MATHS_A:" + code.split("-", 1)[1], lr["foundation"]["text"]
    if tier == "Higher":
        return "IGCSE_MATHS_A:H-" + code.split("-", 1)[1], p["official_wording"]
    return "IGCSE_MATHS_A:" + code.split("-", 1)[1], p["official_wording"]


def main() -> int:
    check_only = "--check-only" in sys.argv
    verdicts = yaml.safe_load(VERDICTS.read_text())
    vv = verdicts["verdicts"]
    residual = verdicts["residual"]
    overrides = verdicts["section_overrides"]
    ext_overrides = verdicts.get("extension_section_overrides", {})
    subsumed = verdicts.get("subsumed_r1_entries", {}).get("entries", [])
    store = load_store()
    ledger = load_ledger()
    anchors, sections = r4_surface()

    # P2 surface coverage
    if set(vv) != anchors:
        print(f"FAIL P2: verdict anchors != R4 id surface "
              f"({len(vv)} vs {len(anchors)}; missing={anchors - set(vv)}; extra={set(vv) - anchors})")
        return 1
    # P3 code sanity
    for aid, x in vv.items():
        d = x["disposition"]
        if d == "CORRECT":
            cc = x["corrected_code"]
            if cc not in store or cc == x["prior_code"]:
                print(f"FAIL P3 {aid}: corrected_code {cc} invalid"); return 1
        elif d == "UNRESOLVED":
            if x.get("corrected_code") is not None:
                print(f"FAIL P3 {aid}: UNRESOLVED must not carry corrected_code"); return 1
        else:
            print(f"FAIL P3 {aid}: unknown disposition {d}"); return 1
    # P4 ledger coverage for ledger-sourced rows (none expected at R6)
    for aid, x in vv.items():
        if x.get("tier_wording_source") == "ledger":
            bare = x["corrected_code"].split("-", 1)[1]
            if bare not in ledger:
                print(f"FAIL P4 {aid}: {bare} absent from the tier-dedupe ledger"); return 1
    # P5 section surface: the 4 verdicted keys match the R4 section surface
    ov_norm = sorted((k.split("::")[0], int(k.split("::")[1])) for k in overrides)
    if ov_norm != sections:
        print(f"FAIL P5: override keys {ov_norm} != R4 section surface {sections}")
        return 1
    for k, x in overrides.items():
        if x["disposition"] != "REATTRIBUTE" or x.get("override_code") not in store:
            print(f"FAIL P5 {k}: invalid REATTRIBUTE"); return 1
    # P5b extension rows: targets in the 188; current_code == post-R6 join-derived
    new_codes = {aid: (x["corrected_code"].split("-", 1)[1] if x["disposition"] == "CORRECT" else None)
                 for aid, x in vv.items()}
    join = json.loads(JOIN.read_text())
    jp = {r["note_path"]: r for r in join["joins"]}
    for u in join.get("unresolved", []):
        jp.setdefault(u["note_path"], u)
    np_by_slug = {}
    for np_, jr in jp.items():
        np_by_slug[np_.split("/")[-1].replace(".json", "")] = np_
    for k, x in ext_overrides.items():
        if "::" not in k:
            continue  # the contract note key
        slug, ordn = k.split("::")[0], int(k.split("::")[1])
        if x.get("override_code") not in store:
            print(f"FAIL P5b {k}: override_code invalid"); return 1
        anchor = jp[np_by_slug[slug]]["anchor_id"]
        expected = new_codes.get(anchor) or jp[np_by_slug[slug]]["resolved_code"]
        if x.get("current_code") != "4MA1-" + expected:
            print(f"FAIL P5b {k}: current_code {x.get('current_code')} != post-R6 join-derived "
                  f"4MA1-{expected}"); return 1
    # P6 residual
    if residual["disposition"] != "KEEP_UNRESOLVED":
        print("FAIL P6: residual must stay UNRESOLVED"); return 1

    # P1 baseline / idempotency
    if RES_PATH.exists():
        raw = RES_PATH.read_bytes()
        read_method = "disk"
    else:
        raw = subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{RES_GIT}"],
                             capture_output=True, check=True).stdout
        read_method = "git-show"
    res = json.loads(raw)
    if res.get("repair", {}).get("round") == ROUND:
        print("idempotent skip: R6 round marker present — verifying agreement")
        ok, bad = verify(res, vv, residual)
        print("verify:", "OK" if ok else f"MISMATCH {bad}")
        emit_projection(res, vv, overrides, ext_overrides, subsumed)
        print(f"derived projection re-emitted -> {OVERRIDES_OUT.relative_to(REPO)}")
        return 0 if ok else 1
    if sha16(raw) != BASELINE_BLOB_SHA16:
        print(f"FAIL P1: baseline blob {sha16(raw)} != {BASELINE_BLOB_SHA16}")
        return 1
    if check_only:
        print("check-only: all preconditions PASS (baseline untouched)")
        return 0

    # ---- mutate exactly the surface rows ----
    n_corr = n_unres = 0
    for aid, x in vv.items():
        row = next(r for r in res["resolved"] if r["id"] == aid)
        prior = {"code": row.get("resolved_code"), "official_id": row.get("official_id"),
                 "official_wording": row.get("official_wording")}
        d = x["disposition"]
        repair = {"task": TASK, "round": ROUND, "date": DATE, "disposition": d,
                  "prior": prior, "verdict_ref": aid, "review_reference": RECORD_REF,
                  "evidence": x["evidence"]}
        if "repair" in row:  # fail-safe: never lose prior provenance
            row.setdefault("repair_history", []).append(row["repair"])
        if d == "CORRECT":
            oid, wording = statement_fields(x["corrected_code"], x.get("tier_wording_source", "store"),
                                            store, ledger)
            row["resolved_code"] = x["corrected_code"].split("-", 1)[1]
            row["official_id"] = oid
            row["official_wording"] = wording
            n_corr += 1
        else:  # UNRESOLVED
            row["resolved_code"] = None
            row["official_id"] = None
            row["official_wording"] = None
            row["status"] = ("UNRESOLVED — RECORDED, NEVER FABRICATED (T-C42 R6: no canonical "
                             "row teaches the note's content; the wrong code was cleared, never forced)")
            row["reason"] = ("T-C42 R6 operator-delegate verdict: no canonical row teaches this "
                             "note's content — the prior code was a T-SPEC resolution error "
                             "(unsampled at C40, caught by the R4 re-gate); cleared, never forced "
                             "(evidence in scripts/c42_r6_repair_verdicts.yaml)")
            n_unres += 1
        row["repair"] = repair
    rrow = next(r for r in res["resolved"] if r["id"] == residual["anchor_id"])
    rrow["repair"] = {"task": TASK, "round": ROUND, "date": DATE,
                      "disposition": "KEEP_UNRESOLVED", "verdict_ref": residual["anchor_id"],
                      "review_reference": RECORD_REF, "evidence": residual["evidence"]}

    # ---- top-level ----
    prev = res.pop("repair", None)
    if prev is not None:
        res["repair_history"] = [prev] + list(res.get("repair_history", []))
    res["repair"] = {
        "task": TASK, "round": ROUND, "date": DATE,
        "directive": verdicts["directive"],
        "reviewer": verdicts["reviewer"],
        "verdicts_record": "scripts/c42_r6_repair_verdicts.yaml",
        "section_overrides_record": "scripts/c42_section_overrides_r6.yaml",
        "proposals_record": "graph/reports/C42_R6_REPAIR_PROPOSALS.json (PROPOSAL-ONLY, binds nothing)",
        "inventory_source": "the R4 re-gate defect inventory (scripts/c42_r4_fresh_verdicts.yaml, "
                            "19 reject rows; the R4 gate FAILED at exact-stratum 80.4% < 90%)",
        "record": RECORD_REF,
        "counts_delta": {"corrected": n_corr, "cleared_unresolved": n_unres, "residual_kept": 1,
                         "section_overrides": {"reattribute": len(overrides), "retain": 0,
                                               "extension_rows": len([k for k in ext_overrides if "::" in k])},
                         "subsumed_r1_entries": len(subsumed)},
        "notes": [
            "the R6 lane is the second R1-shaped verdict round of the scope §7 loop — fired "
            "by explicit operator instruction over the R4 defect inventory",
            "the T-C32 join and the chunk substrate are now STALE relative to this file by "
            "design — they refresh at R7/R8; the R9 re-gate re-renders the review surface",
            "2 R1 override entries (solving-linear-inequalities ord 3, basic-fractions ord 6) "
            "are SUBSUMED by the note-level repairs they anticipated — the R8 build verifies "
            "and records them, it does not re-apply them as no-ops",
            "3 extension section rows (area ord 7 — R4-sampled with its own root naming the "
            "4.9D surface; area ord 6; basic-fractions ord 2 — heading-verbatim) are recorded "
            "with per-row sampling labels, transparently outside the 4 verdicted section rows",
            "2 observations recorded for the operator (drawing-straight-line-graphs note-join "
            "question; scorer noise) — nothing self-repairs beyond this round's surface",
        ],
    }
    clause = (f"; T-C42 R6 R1-shaped verdict round over the R4 defect inventory ({DATE}, "
              f"operator-delegate under the fired R6 directive; human operator sign-off "
              f"retained): 8 id-level codes corrected, 2 cleared UNRESOLVED (never forced), "
              f"the C32 residual re-affirmed KEPT UNRESOLVED, 4 section-level REATTRIBUTE "
              f"dispositions + 3 labeled extension rows recorded for the R8 override map, and "
              f"2 R1 override entries subsumed by the note-level repairs")
    res["validation"] = res.get("validation", "") + clause
    null_ids = [r["id"] for r in res["resolved"] if not r.get("resolved_code")]
    res["counts"] = {"ids": len(res["resolved"]), "resolved": len(res["resolved"]) - len(null_ids),
                     "unresolved": len(null_ids)}
    res["unresolved_allowlist_note"] = (res.get("unresolved_allowlist_note", "") +
                                        f" | T-C42 R6 ({DATE}): cleared to UNRESOLVED — "
                                        f"{', '.join(sorted(null_ids))} (no canonical row; never forced)")

    body = json.dumps(res, indent=1, ensure_ascii=False)
    if raw.endswith(b"\n"):
        body += "\n"
    RES_PATH.write_bytes(body.encode())

    emit_projection(res, verdicts, overrides, ext_overrides, subsumed)

    print(f"applied: {n_corr} corrected, {n_unres} cleared, residual kept; "
          f"counts -> {res['counts']}")
    print(f"file: {RES_PATH.relative_to(REPO)} (read via {read_method})")
    print(f"overrides -> {OVERRIDES_OUT.relative_to(REPO)}")
    return 0


def emit_projection(res, verdicts, overrides, ext_overrides, subsumed) -> None:
    """The derived R8-facing override map — deterministic from the verdict
    record; re-emitted on every run (the resolution file is the write-once
    artifact, this projection is not)."""
    proj = {
        "schema": "c42-r8-section-overrides/1.0",
        "task": TASK, "round": ROUND, "generated": DATE,
        "source": "scripts/c42_r6_repair_verdicts.yaml (section_overrides + "
                  "extension_section_overrides + subsumed_r1_entries)",
        "contract": "consumed fail-closed by scripts/c40_maths_a_chunk_sp_substrate.py at R8 "
                    "TOGETHER WITH scripts/c42_section_overrides.yaml (R1): an override naming "
                    "a code outside the ratified 188 fails the build; current_code must equal "
                    "the join-derived code; entries in subsumed_r1_entries are verified and "
                    "recorded as provenance.override_subsumed, not re-applied",
        "overrides": [
            {"note_slug": k.split("::")[0], "chunk_ordinal": int(k.split("::")[1]),
             "current_code": x["current_code"], "provenance_class": "verdicted",
             "action": x["disposition"], "override_code": x.get("override_code"),
             "evidence": x["evidence"]}
            for k, x in sorted(overrides.items())
        ] + [
            {"note_slug": k.split("::")[0], "chunk_ordinal": int(k.split("::")[1]),
             "current_code": x["current_code"], "provenance_class": "extension",
             "action": x["disposition"], "override_code": x.get("override_code"),
             "evidence": x["evidence"]}
            for k, x in sorted(ext_overrides.items()) if "::" in k
        ],
        "subsumed_r1_entries": subsumed,
        "observations": verdicts.get("observations"),
    }
    OVERRIDES_OUT.write_text(yaml.safe_dump(proj, sort_keys=False, allow_unicode=True))


def verify(res, vv, residual) -> tuple:
    by_id = {r["id"]: r for r in res["resolved"]}
    bad = []
    for aid, x in vv.items():
        row = by_id.get(aid)
        if not row or (row.get("repair") or {}).get("round") != ROUND:
            bad.append(f"{aid}: no R6 repair marker"); continue
        d = x["disposition"]
        if d == "CORRECT" and row.get("resolved_code") != x["corrected_code"].split("-", 1)[1]:
            bad.append(f"{aid}: code != corrected")
        if d == "UNRESOLVED" and row.get("resolved_code") is not None:
            bad.append(f"{aid}: not cleared")
    rrow = by_id.get(residual["anchor_id"], {})
    if (rrow.get("repair") or {}).get("disposition") != "KEEP_UNRESOLVED":
        bad.append("residual marker missing")
    return (not bad), bad


if __name__ == "__main__":
    sys.exit(main())
