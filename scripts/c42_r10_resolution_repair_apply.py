#!/usr/bin/env python3
"""c42_r10_resolution_repair_apply.py — T-C42 R10 gated merge point.

The R10 lane is the third R1-shaped verdict round (scope §7 loop), fired by the
operator directive "an R1-shaped round over the R9 inventory (then R7/R8/R9
again), the heading-only-chunk convention decision" (2026-10-03, zai-web) over
the R9 re-gate's defect inventory.

Consumes the operator-owned verdict record
(scripts/c42_r10_repair_verdicts.yaml) and amends EXACTLY ONE FILE in place:
SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json
(the T-SPEC in-house precedent + the C31 §4.4 dated-exception path; the R1/R6
amendments of the same file are the standing precedents for this round).

Fail-closed preconditions:
  P1 baseline file == the pinned git blob sha256_16 466250eaa21fada2 (the
     R6-repaired file at a872cdd); idempotent skip: if the file already
     carries the R10 round marker, verify verdicts<->file agreement and exit 0
     without rewriting;
  P2 verdicts cover exactly the 2 id-level anchors of the R9 defect inventory
     (recomputed from scripts/c42_r9_fresh_verdicts.yaml roots
     {note-level-class} via the join), no dupes, no extras;
  P3 every corrected_code is a member of the canonical 188 and differs from
     the prior code; UNRESOLVED rows clear (none this round);
  P4 every ledger-cited code (id-level or section-level) exists in the C30
     tier-dedupe ledger;
  P5 the 8 section override keys match the R9 section surface exactly
     (slug+ordinal = the 7 section-level roots + the 1 unresolved-class
     section root), REATTRIBUTE codes in the 188 and != current_code, and the
     DEMOTE_TO_WORKLIST row carries override_code null;
  P6 the residual verdict is present and keeps the anchor UNRESOLVED;
  P7 the heading-only convention decision is present and pins
     c42-heading-only-convention-1 with its record reference.

Row mutation matrix (nothing else changes):
  CORRECT     2 rows: resolved_code/official_id/official_wording re-pointed
              (store-sourced; Higher codes take the H- id); repair provenance
              preserves the prior values verbatim (a pre-existing repair
              block, if any, moves to repair_history).
  UNRESOLVED  0 rows this round (the counts stay 222/214/8).
  residual    1 row: marker only (stays UNRESOLVED per its R1 adjudication).

Top-level: the R6 repair block moves to repair_history, a new R10 repair block
is written (recording the convention decision and the note-level adjudication),
a dated clause is appended to "validation", and "counts" recompute (unchanged
at 222/214/8 — nothing cleared).

Also writes the R12-facing projection scripts/c42_section_overrides_r10.yaml
(derived, deterministic from the verdict record; carries the 7 verdicted
REATTRIBUTE + 1 verdicted DEMOTE_TO_WORKLIST entries, the note-level
adjudication the R12 build must honor, and the observations). The derived
projection is re-emitted on EVERY run (including the idempotent verify-only
path) — only the resolution file is write-once.

Usage: python3 scripts/c42_r10_resolution_repair_apply.py [--check-only]
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
VERDICTS = REPO / "scripts/c42_r10_repair_verdicts.yaml"
R9_FRESH = REPO / "scripts/c42_r9_fresh_verdicts.yaml"
JOIN = REPO / "Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json"
OVERRIDES_OUT = REPO / "scripts/c42_section_overrides_r10.yaml"
BASELINE_BLOB_SHA16 = "466250eaa21fada2"

TASK = "T-C42"
ROUND = "R10"
DATE = "2026-10-03"
RECORD_REF = "graph/reports/C42_R10_RESOLUTION_REPAIR_RECORD.md"


def sha16(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:16]


def load_store() -> dict:
    pts = yaml.safe_load((REPO / "graph/igcse-maths-a/specification_points.yaml").read_text())["specification_points"]
    return {p["code"]: p for p in pts}


def load_ledger() -> dict:
    led = json.loads((REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json").read_text())
    return {r["official_code"]: r for r in led["rows"]}


def r9_surface():
    """(id anchors, section keys) derived deterministically from the R9 fresh
    verdict record — the round's declared surface. The join may be any
    post-R10 refresh: anchors changed by R10 live in the join's rows."""
    fresh = yaml.safe_load(R9_FRESH.read_text())["verdicts"]
    join = json.loads(JOIN.read_text())
    jrows = {r["note_path"]: r for r in join["joins"]}
    for u in join.get("unresolved", []):
        jrows.setdefault(u["note_path"], u)
    anchors = set()
    sections = set()
    for x in fresh.values():
        if x["verdict"] != "REJECT":
            continue
        root = x.get("root")
        if root in ("note-level", "note-level-class"):
            anchors.add(jrows[x["note_path"]]["anchor_id"])
        elif root in ("section-level", "unresolved-class section"):
            sections.add((x["note_path"].split("/")[-1].replace(".json", ""), x["chunk_ordinal"]))
    return anchors, sorted(sections)


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
    convention = verdicts.get("heading_only_convention", {})
    adjudications = verdicts.get("note_level_adjudications", {})
    store = load_store()
    ledger = load_ledger()
    anchors, sections = r9_surface()

    # P2 surface coverage
    if set(vv) != anchors:
        print(f"FAIL P2: verdict anchors != R9 id surface "
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
    # P4 ledger coverage for ledger-cited rows (id-level and section-level)
    for aid, x in vv.items():
        if x.get("tier_wording_source") == "ledger":
            bare = x["corrected_code"].split("-", 1)[1]
            if bare not in ledger:
                print(f"FAIL P4 {aid}: {bare} absent from the tier-dedupe ledger"); return 1
    for k, x in overrides.items():
        if x.get("tier_wording_source") == "ledger":
            bare = x["override_code"].split("-", 1)[1]
            if bare not in ledger:
                print(f"FAIL P4 {k}: {bare} absent from the tier-dedupe ledger"); return 1
    # P5 section surface: the 8 keys match the R9 section surface
    ov_norm = sorted((k.split("::")[0], int(k.split("::")[1])) for k in overrides)
    if ov_norm != sections:
        print(f"FAIL P5: override keys {ov_norm} != R9 section surface {sections}")
        return 1
    for k, x in overrides.items():
        d = x["disposition"]
        if d == "REATTRIBUTE":
            oc = x.get("override_code")
            if not oc or oc not in store or oc == x["current_code"]:
                print(f"FAIL P5 {k}: invalid REATTRIBUTE"); return 1
        elif d == "DEMOTE_TO_WORKLIST":
            if x.get("override_code") is not None:
                print(f"FAIL P5 {k}: DEMOTE must carry override_code null"); return 1
        else:
            print(f"FAIL P5 {k}: unknown disposition {d}"); return 1
    # P6 residual
    if residual["disposition"] != "KEEP_UNRESOLVED":
        print("FAIL P6: residual must stay UNRESOLVED"); return 1
    # P7 convention decision present
    if convention.get("decision") != "c42-heading-only-convention-1" or \
            "C42_R10_HEADING_ONLY_CONVENTION.md" not in str(convention.get("record", "")):
        print("FAIL P7: the heading-only convention decision must pin "
              "c42-heading-only-convention-1 with its record reference"); return 1

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
        print("idempotent skip: R10 round marker present — verifying agreement")
        ok, bad = verify(res, vv, residual)
        print("verify:", "OK" if ok else f"MISMATCH {bad}")
        emit_projection(res, verdicts, overrides, convention, adjudications)
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
            row["status"] = ("UNRESOLVED — RECORDED, NEVER FABRICATED (T-C42 R10: no canonical "
                             "row teaches the note's content; the wrong code was cleared, never "
                             "forced)")
            row["reason"] = ("T-C42 R10 operator-delegate verdict: no canonical row teaches this "
                             "note's content — the prior code was a T-SPEC resolution error; "
                             "cleared, never forced (evidence in scripts/c42_r10_repair_verdicts.yaml)")
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
        "verdicts_record": "scripts/c42_r10_repair_verdicts.yaml",
        "section_overrides_record": "scripts/c42_section_overrides_r10.yaml",
        "proposals_record": "graph/reports/C42_R10_REPAIR_PROPOSALS.json (PROPOSAL-ONLY, binds nothing)",
        "convention_record": "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md "
                             "(c42-heading-only-convention-1 — the heading-only chunk class "
                             "resolved by the round's convention decision, not by per-row re-points)",
        "inventory_source": "the R9 re-gate defect inventory (scripts/c42_r9_fresh_verdicts.yaml, "
                            "10 reject rows; the R9 gate FAILED at exact-stratum 76.8% < 90%)",
        "record": RECORD_REF,
        "counts_delta": {"corrected": n_corr, "cleared_unresolved": n_unres, "residual_kept": 1,
                         "section_overrides": {"reattribute": 7, "demote_to_worklist": 1,
                                               "retain": 0, "extension_rows": 0},
                         "note_level_adjudications": 1,
                         "heading_only_convention": "c42-heading-only-convention-1"},
        "notes": [
            "the R10 lane is the third R1-shaped verdict round of the scope §7 loop — fired "
            "by explicit operator instruction over the R9 defect inventory; lane numbering "
            "follows the iteration-2 precedent (this round is R10; the join re-run is R11, "
            "the substrate re-build is R12, the re-gate is R13; R5 stays reserved)",
            "the T-C32 join and the chunk substrate are now STALE relative to this file by "
            "design — they refresh at R11/R12; the R13 re-gate re-renders the review surface",
            "the related-calculations NOTE-LEVEL join was adjudicated and STANDS on the "
            "note's ord-3 estimation-to-check surface — the R9 root's name-fragment "
            "suspicion is examined and rejected; only the ord-2 section DEMOTEs to the "
            "worklist (the scope §4 R1 menu's DEMOTE action, exercised for the first time)",
            "the heading-only chunk class (~204 of 862 anchored rows) is resolved by "
            "c42-heading-only-convention-1 (H1 verdict standing / H2 content standing / "
            "H3 fail-closed HOLD) — a structural class treatment, not per-row re-points; "
            "the human operator retains final sign-off and may reverse before R5",
            "0 anchors cleared this round — the counts stay 222/214/8",
        ],
    }
    clause = (f"; T-C42 R10 R1-shaped verdict round over the R9 defect inventory ({DATE}, "
              f"operator-delegate under the fired R10 directive; human operator sign-off "
              f"retained): 2 id-level codes corrected (expanding-triple-brackets 2.2E -> 2.2A; "
              f"algebraic-fractions 1.2A -> 2.2C), 0 cleared (counts unchanged 222/214/8), "
              f"the C32 residual re-affirmed KEPT UNRESOLVED, 7 section-level REATTRIBUTE "
              f"dispositions + 1 DEMOTE-to-worklist (related-calculations ord 2 — the "
              f"note-level join adjudicated and STANDING) recorded for the R12 override map, "
              f"and the heading-only chunk class resolved by c42-heading-only-convention-1")
    res["validation"] = res.get("validation", "") + clause

    body = json.dumps(res, indent=1, ensure_ascii=False)
    if raw.endswith(b"\n"):
        body += "\n"
    RES_PATH.write_bytes(body.encode())

    emit_projection(res, verdicts, overrides, convention, adjudications)

    print(f"applied: {n_corr} corrected, {n_unres} cleared, residual kept; "
          f"counts -> {res['counts']}")
    print(f"file: {RES_PATH.relative_to(REPO)} (read via {read_method})")
    print(f"overrides -> {OVERRIDES_OUT.relative_to(REPO)}")
    return 0


def emit_projection(res, verdicts, overrides, convention, adjudications) -> None:
    """The derived R12-facing override map — deterministic from the verdict
    record; re-emitted on every run (the resolution file is the write-once
    artifact, this projection is not)."""
    proj = {
        "schema": "c42-r12-section-overrides/1.0",
        "task": TASK, "round": ROUND, "generated": DATE,
        "source": "scripts/c42_r10_repair_verdicts.yaml (section_overrides + "
                  "note_level_adjudications + heading_only_convention)",
        "contract": "consumed fail-closed by scripts/c40_maths_a_chunk_sp_substrate.py at R12 "
                    "TOGETHER WITH scripts/c42_section_overrides.yaml (R1) and "
                    "scripts/c42_section_overrides_r6.yaml (R6): an override naming a code "
                    "outside the ratified 188 fails the build; current_code must equal the "
                    "join-derived code; a DEMOTE_TO_WORKLIST entry moves the chunk row to the "
                    "unresolved-span worklist with its recorded reason; the note-level "
                    "adjudication pins the related-calculations anchor as STANDING (no re-point)",
        "overrides": [
            {"note_slug": k.split("::")[0], "chunk_ordinal": int(k.split("::")[1]),
             "current_code": x["current_code"], "provenance_class": "verdicted",
             "action": x["disposition"], "override_code": x.get("override_code"),
             "evidence": x["evidence"]}
            for k, x in sorted(overrides.items())
        ],
        "note_level_adjudications": {
            "related-calculations": {
                "anchor_id": "spcpt_crKbmb6wVjM4yPJh",
                "ruling": adjudications.get("related-calculations-note-join", {}).get("ruling"),
                "evidence": adjudications.get("related-calculations-note-join", {}).get("evidence"),
            },
        },
        "heading_only_convention": {
            "decision_id": convention.get("decision"),
            "record": convention.get("record"),
            "ruling_summary": convention.get("ruling_summary"),
            "enforcement": "the R13 re-gate fill resolves heading-only rows via the "
                           "convention ladder; the R12 build itself needs no convention "
                           "wiring (chunk identity is untouched)",
        },
        "subsumed_r1_entries": [],
        "observations": verdicts.get("observations"),
    }
    OVERRIDES_OUT.write_text(yaml.safe_dump(proj, sort_keys=False, allow_unicode=True))


def verify(res, vv, residual) -> tuple:
    by_id = {r["id"]: r for r in res["resolved"]}
    bad = []
    for aid, x in vv.items():
        row = by_id.get(aid)
        if not row or (row.get("repair") or {}).get("round") != ROUND:
            bad.append(f"{aid}: no R10 repair marker"); continue
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
