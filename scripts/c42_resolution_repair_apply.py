#!/usr/bin/env python3
"""c42_resolution_repair_apply.py — T-C42 R1 gated merge point.

Consumes the operator-owned verdict record
(scripts/c42_repair_verdicts.yaml) and amends EXACTLY ONE FILE in place:
SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json
(the T-SPEC series in-house precedent + the C31 §4.4 dated-exception path;
the C42 scope §4 R1 names this amendment).

Fail-closed preconditions:
  P1 baseline file == the pinned git blob sha256_16 3a0b5dc48a65fb54
     (idempotent skip: if the file already carries the R1 repair marker,
     verify verdicts<->file agreement and exit 0 without rewriting);
  P2 verdicts cover exactly the 45 defective anchors (recomputed from the
     C40 verdict record + the C32 join), no dupes, no extras;
  P3 every corrected_code is a member of the canonical 188 and differs from
     the prior code; AFFIRM rows change no code; UNRESOLVED rows clear;
  P4 every ledger-cited code exists in the C30 tier-dedupe ledger;
  P5 the 16 section override keys match the C40 verdict record's
     section-level rows exactly (slug+ordinal), REATTRIBUTE codes in the 188;
  P6 the residual verdict is present and keeps the anchor UNRESOLVED.

Row mutation matrix (nothing else changes):
  CORRECT    22 rows: resolved_code/official_id/official_wording re-pointed
             (store-sourced verdicts follow the store row + its tier
             convention; ledger-sourced verdicts re-point to the Foundation
             statement: bare official_id + ledger foundation.text); repair
             provenance preserves the prior values verbatim.
  AFFIRM     21 rows: code UNCHANGED; the statement re-pointed to the
             Foundation wording (bare id + ledger foundation.text) so the
             row is self-consistent with the affirmation evidence.
  UNRESOLVED  2 rows: code/id/wording cleared to null + recorded reason;
             repair provenance preserves the prior wrong values.
  residual    1 row: marker only (stays UNRESOLVED per its PDF-verified reason).

Top-level: adds a "repair" block, appends a dated clause to "validation",
recomputes "counts" (218 -> 216 resolved, 4 -> 6 unresolved), and appends the
two cleared ids to "unresolved_allowlist_note".

Also writes the R3-facing projection scripts/c42_section_overrides.yaml
(derived, deterministic from the verdict record).

Usage: python3 scripts/c42_resolution_repair_apply.py [--check-only]
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
VERDICTS = REPO / "scripts/c42_repair_verdicts.yaml"
OVERRIDES_OUT = REPO / "scripts/c42_section_overrides.yaml"
BASELINE_BLOB_SHA16 = "3a0b5dc48a65fb54"

TASK = "T-C42"
ROUND = "R1"
DATE = "2026-10-02"
RECORD_REF = "graph/reports/C42_MATHS_A_RESOLUTION_REPAIR_RECORD.md"


def sha16(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:16]


def load_store() -> dict:
    pts = yaml.safe_load((REPO / "graph/igcse-maths-a/specification_points.yaml").read_text())["specification_points"]
    return {p["code"]: p for p in pts}


def load_ledger() -> dict:
    led = json.loads((REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json").read_text())
    return {r["official_code"]: r for r in led["rows"]}


def load_join_pairs_and_sections():
    verdicts = yaml.safe_load((REPO / "scripts/c40_maths_a_substrate_review_verdicts.yaml").read_text())["verdicts"]
    join = json.loads((REPO / "Official-Specifications/parsed/_derived/notes-join/"
                       "igcse-maths-a-18-higher.json").read_text())
    jrows = {r["note_path"]: r for r in join["joins"]}
    nl = [x for x in verdicts.values() if x["verdict"] == "REJECT" and x.get("root") == "note-level"]
    anchors = {}
    for x in nl:
        anchors[jrows[x["note_path"]]["anchor_id"]] = x["spec_code"]
    sl = [x for x in verdicts.values() if x["verdict"] == "REJECT" and x.get("root") == "section-level"]
    sections = sorted(set((x["note_path"].split("/")[-1].replace(".json", ""), x["chunk_ordinal"])
                          for x in sl))
    return anchors, sections


def statement_fields(code: str, source: str, store: dict, ledger: dict):
    """(official_id, official_wording) for the repaired statement."""
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
    store = load_store()
    ledger = load_ledger()
    anchors, sections = load_join_pairs_and_sections()

    # P2 surface coverage
    if set(vv) != set(anchors):
        print(f"FAIL P2: verdict anchors != defective surface "
              f"({len(vv)} vs {len(anchors)}; missing={set(anchors)-set(vv)}; extra={set(vv)-set(anchors)})")
        return 1
    # P3 code sanity
    for aid, x in vv.items():
        d = x["disposition"]
        if d == "CORRECT":
            cc = x["corrected_code"]
            if cc not in store or cc == x["prior_code"]:
                print(f"FAIL P3 {aid}: corrected_code {cc} invalid"); return 1
        elif d == "AFFIRM":
            if x.get("corrected_code") is not None:
                print(f"FAIL P3 {aid}: AFFIRM must not carry corrected_code"); return 1
        elif d == "UNRESOLVED":
            if x.get("corrected_code") is not None:
                print(f"FAIL P3 {aid}: UNRESOLVED must not carry corrected_code"); return 1
        else:
            print(f"FAIL P3 {aid}: unknown disposition {d}"); return 1
    # P4 ledger coverage for ledger-sourced + AFFIRM re-points
    for aid, x in vv.items():
        src = x.get("tier_wording_source")
        code = x["corrected_code"] if x["disposition"] == "CORRECT" else x["prior_code"]
        bare = code.split("-", 1)[1]
        if src == "ledger" or x["disposition"] == "AFFIRM":
            if bare not in ledger:
                print(f"FAIL P4 {aid}: {bare} absent from the tier-dedupe ledger"); return 1
    # P5 section surface (normalize "slug::ordinal" keys to (slug, int) tuples)
    ov_norm = sorted((k.split("::")[0], int(k.split("::")[1])) for k in overrides)
    if ov_norm != sections:
        print(f"FAIL P5: override keys {ov_norm} != C40 section surface {sections}")
        return 1
    for k, x in overrides.items():
        if x["disposition"] == "REATTRIBUTE":
            if x.get("override_code") not in store:
                print(f"FAIL P5 {k}: override_code invalid"); return 1
        elif x["disposition"] == "RETAIN":
            if x.get("override_code"):
                print(f"FAIL P5 {k}: RETAIN must not carry override_code"); return 1
        else:
            print(f"FAIL P5 {k}: unknown disposition"); return 1
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
    if "repair" in res:
        print("idempotent skip: repair marker present — verifying agreement")
        ok, bad = verify(res, vv, residual, store, ledger)
        print("verify:", "OK" if ok else f"MISMATCH {bad}")
        return 0 if ok else 1
    if sha16(raw) != BASELINE_BLOB_SHA16:
        print(f"FAIL P1: baseline blob {sha16(raw)} != {BASELINE_BLOB_SHA16}")
        return 1
    if check_only:
        print("check-only: all preconditions PASS (baseline untouched)")
        return 0

    # ---- mutate exactly the surface rows ----
    n_corr = n_aff = n_unres = 0
    for aid, x in vv.items():
        row = next(r for r in res["resolved"] if r["id"] == aid)
        prior = {"code": row.get("resolved_code"), "official_id": row.get("official_id"),
                 "official_wording": row.get("official_wording")}
        d = x["disposition"]
        repair = {"task": TASK, "round": ROUND, "date": DATE, "disposition": d,
                  "prior": prior, "verdict_ref": aid, "review_reference": RECORD_REF,
                  "evidence": x["evidence"]}
        if d == "CORRECT":
            oid, wording = statement_fields(x["corrected_code"], x.get("tier_wording_source", "store"),
                                            store, ledger)
            row["resolved_code"] = x["corrected_code"].split("-", 1)[1]
            row["official_id"] = oid
            row["official_wording"] = wording
            n_corr += 1
        elif d == "AFFIRM":
            bare = x["prior_code"].split("-", 1)[1]
            row["official_id"] = "IGCSE_MATHS_A:" + bare
            row["official_wording"] = ledger[bare]["foundation"]["text"]
            repair["statement_repointed"] = True
            n_aff += 1
        else:  # UNRESOLVED
            row["resolved_code"] = None
            row["official_id"] = None
            row["official_wording"] = None
            row["status"] = "UNRESOLVED — RECORDED, NEVER FABRICATED (T-C42 R1: no canonical " \
                            "row teaches the note's content; the wrong code was cleared, never forced)"
            row["reason"] = ("T-C42 R1 operator-delegate verdict: no canonical row teaches this "
                             "note's content — the prior code was a T-SPEC resolution error; "
                             "cleared, never forced (evidence in scripts/c42_repair_verdicts.yaml)")
            n_unres += 1
        row["repair"] = repair
    rrow = next(r for r in res["resolved"] if r["id"] == residual["anchor_id"])
    rrow["repair"] = {"task": TASK, "round": ROUND, "date": DATE,
                      "disposition": "KEEP_UNRESOLVED", "verdict_ref": residual["anchor_id"],
                      "review_reference": RECORD_REF, "evidence": residual["evidence"]}

    # ---- top-level ----
    res["repair"] = {
        "task": TASK, "round": ROUND, "date": DATE,
        "directive": verdicts["directive"],
        "reviewer": verdicts["reviewer"],
        "verdicts_record": "scripts/c42_repair_verdicts.yaml",
        "section_overrides_record": "scripts/c42_section_overrides.yaml",
        "record": RECORD_REF,
        "counts_delta": {"corrected": n_corr, "affirmed_statement_repointed": n_aff,
                         "cleared_unresolved": n_unres, "residual_kept": 1,
                         "section_overrides": {"reattribute": 12, "retain": 4}},
        "notes": [
            "R4's re-fill MUST consult both tier wordings (store operative + ledger "
            "foundation.text per code) or it will re-reject the affirmed joins",
            "the C32 notes-join and the C40 substrate are now STALE relative to this file "
            "by design — they refresh at R2/R3; spec-links refresh is a separate follow-up",
            "16 legacy rows carry bare ids for Higher-store codes (pre-existing convention "
            "drift, outside this round's surface, recorded not repaired)",
        ],
    }
    clause = (f"; T-C42 R1 resolution-repair round ({DATE}, operator-delegate under the fired "
              f"R1 directive; human operator sign-off retained): 22 id-level codes corrected, "
              f"2 cleared UNRESOLVED, 21 affirmed with statements re-pointed to the Foundation "
              f"wording per the C30 tier-dedupe ledger, the C32 residual kept UNRESOLVED, and 16 "
              f"section-level dispositions recorded for the R3 override map")
    res["validation"] = res.get("validation", "") + clause
    null_ids = [r["id"] for r in res["resolved"] if not r.get("resolved_code")]
    res["counts"] = {"ids": len(res["resolved"]), "resolved": len(res["resolved"]) - len(null_ids),
                     "unresolved": len(null_ids)}
    res["unresolved_allowlist_note"] = (res.get("unresolved_allowlist_note", "") +
                                        f" | T-C42 R1 ({DATE}): cleared to UNRESOLVED — "
                                        f"{', '.join(sorted(null_ids))} (no canonical row; never forced)")

    body = json.dumps(res, indent=1, ensure_ascii=False)
    if raw.endswith(b"\n"):
        body += "\n"
    RES_PATH.write_bytes(body.encode())

    # ---- R3-facing override projection ----
    proj = {
        "schema": "c42-r3-section-overrides/1.0",
        "task": TASK, "round": ROUND, "generated": DATE,
        "source": "scripts/c42_repair_verdicts.yaml (section_overrides)",
        "contract": "consumed fail-closed by scripts/c40_maths_a_chunk_sp_substrate.py at R3: "
                    "an override naming a code outside the ratified 188 fails the build",
        "overrides": [
            {"note_slug": k.split("::")[0], "chunk_ordinal": int(k.split("::")[1]),
             "current_code": x["current_code"],
             "action": x["disposition"],
             "override_code": x.get("override_code"),
             "evidence": x["evidence"]}
            for k, x in sorted(overrides.items())
        ],
    }
    OVERRIDES_OUT.write_text(yaml.safe_dump(proj, sort_keys=False, allow_unicode=True))

    print(f"applied: {n_corr} corrected, {n_aff} affirmed+repointed, {n_unres} cleared, "
          f"residual kept; counts -> {res['counts']}")
    print(f"file: {RES_PATH.relative_to(REPO)} (read via {read_method})")
    print(f"overrides -> {OVERRIDES_OUT.relative_to(REPO)}")
    return 0


def verify(res, vv, residual, store, ledger) -> tuple:
    """idempotent-state verification: every verdict row's state matches the file."""
    by_id = {r["id"]: r for r in res["resolved"]}
    bad = []
    for aid, x in vv.items():
        row = by_id.get(aid)
        if not row or "repair" not in row:
            bad.append(f"{aid}: no repair marker"); continue
        d = x["disposition"]
        if d == "CORRECT" and row.get("resolved_code") != x["corrected_code"].split("-", 1)[1]:
            bad.append(f"{aid}: code != corrected")
        if d == "UNRESOLVED" and row.get("resolved_code") is not None:
            bad.append(f"{aid}: not cleared")
        if d == "AFFIRM" and row.get("repair", {}).get("disposition") != "AFFIRM":
            bad.append(f"{aid}: affirm marker missing")
    rrow = by_id.get(residual["anchor_id"], {})
    if rrow.get("repair", {}).get("disposition") != "KEEP_UNRESOLVED":
        bad.append("residual marker missing")
    return (not bad), bad


if __name__ == "__main__":
    sys.exit(main())
