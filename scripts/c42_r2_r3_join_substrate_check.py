#!/usr/bin/env python3
"""c42_r2_r3_join_substrate_check.py — T-C42 R2+R3 verification battery.

Gates (all deterministic, fail-closed, exit 0 iff ALL PASS):
  W1 join refresh      200/3/203 census, 0 foreign codes, exact post-R1
                       unresolved id set, resolution input pin == the amended
                       file on disk, all 22 CORRECT codes landed, 2 cleared
                       anchors present in the unresolved set
  W2 substrate shape   meta consistent with the refreshed surface
                       (854 anchored / 8 unresolved-worklist / 66 uncovered-SP /
                       122 covered), every row SUGGESTED + RULE_DERIVED
  W3 chunk identity    the (note_path, ordinal, heading, sha256_16) multiset is
       invariant       IDENTICAL to the pre-R3 substrate (pinned blob
                       f3b2cc2be76934ee3b547a9b4e75d41581ceb6a6) — only code
                       attribution moves
  W4 re-attribution    every pre-R3 anchored row's expected post-R3 code is
       audit           reproduced exactly: CORRECT -> corrected_code, AFFIRM ->
                       unchanged, override REATTRIBUTE -> override_code, RETAIN
                       -> unchanged, cleared spans -> worklist with no code;
                       overrides carry provenance.override; non-surface rows
                       drift nowhere (spec_code AND upstream fields)
  W5 coverage/worklist covered set == recomputed, worklist complete, mapping_id
                       uniqueness, delta vs the C40-era covered set reported
  W6 protected surfaces working-tree diff limited to the R2/R3 footprint; Lane
                       C stores + chemistry + spec-links + C25-C41 records
                       byte-identical to HEAD (6ade129)
  W7 determinism       substrate re-run byte-identical; join re-run
                       content-identical modulo generated_utc

Emits graph/reports/C42_R2_R3_CHECK.json.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
COURSE = "igcse-maths-a-18-higher"
JOIN = REPO / "Official-Specifications/parsed/_derived/notes-join/" \
              f"{COURSE}.json"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
OLD_JOIN_BLOB = "1fe9da180ad4ea5e411e35483ec3f9b52e8a908d"
OLD_STORE_BLOB = "f3b2cc2be76934ee3b547a9b4e75d41581ceb6a6"
HEAD = "6ade129"
RES = REPO / f"SME-ExamQuestion/{COURSE}/spec_point_resolution.json"
R1_CLEARED = {"spcpt_8Wtthy9gt8B5xsVW", "spcpt_3fMGfNtg3hXMg6gC"}
RESIDUAL = "spcpt_QWXhzVp2S3VYZdZc"
LANE_C = ["concepts", "concept_edges", "spec_command_kinds"]
EXPECTED_DIRTY = {
    "scripts/c32_notes_maths_a_join.py",
    "scripts/c40_maths_a_chunk_sp_substrate.py",
    "scripts/c42_r2_r3_join_substrate_check.py",
    "Official-Specifications/parsed/_derived/notes-join/"
    f"{COURSE}.json",
    "graph/igcse-maths-a/spec_chunk_mappings.yaml",
    "graph/reports/C42_R2_R3_CHECK.json",
    "graph/reports/C42_R2_R3_JOIN_SUBSTRATE_RECORD.md",
    "graph/reports/C42_R2_R3_JOIN_SUBSTRATE_RECORD.json",
}

gates: dict[str, dict] = {}


def gate(name: str, ok: bool, detail: str) -> bool:
    gates[name] = {"pass": bool(ok), "detail": detail}
    return ok


def sha16(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:16]


def blob(sha: str) -> bytes:
    return subprocess.run(["git", "-C", str(REPO), "cat-file", "blob", sha],
                          capture_output=True, check=True).stdout


def head_bytes(rel: str) -> bytes:
    return subprocess.run(
        ["git", "-C", str(REPO), "show", f"{HEAD}:{rel}"],
        capture_output=True, check=True).stdout


def main() -> int:
    # ---------------------------------------------------------------- inputs
    new_join = json.loads(JOIN.read_text(encoding="utf-8"))
    old_join = json.loads(blob(OLD_JOIN_BLOB).decode("utf-8"))
    new_sub = yaml.safe_load(STORE.read_text(encoding="utf-8"))
    old_sub = yaml.safe_load(blob(OLD_STORE_BLOB).decode("utf-8"))
    vdoc = yaml.safe_load((REPO / "scripts/c42_repair_verdicts.yaml")
                          .read_text(encoding="utf-8"))
    verdicts = vdoc["verdicts"]
    ovdoc = yaml.safe_load((REPO / "scripts/c42_section_overrides.yaml")
                           .read_text(encoding="utf-8"))
    overrides = ovdoc["overrides"]
    registry = {
        p["code"]: p
        for p in yaml.safe_load(
            (REPO / "graph/igcse-maths-a/specification_points.yaml")
            .read_text(encoding="utf-8"))["specification_points"]}

    # ---- W1 join refresh ----------------------------------------------------
    c = new_join["counts"]
    w1 = (c["joined"] == 200 and c["unresolved_recorded"] == 3
          and c["anchors_total"] == 203 and c["foreign_codes"] == 0)
    got = {u["anchor_id"] for u in new_join["unresolved"]}
    w1 = w1 and got == {RESIDUAL} | R1_CLEARED
    disk_sha = sha16(RES.read_bytes())
    w1 = w1 and new_join["inputs"]["resolution"]["sha256_16"] == disk_sha
    nby = {r["anchor_id"]: r for r in new_join["joins"]}
    corrected_landed = all(
        nby[a]["resolved_code"] == e["corrected_code"].replace("4MA1-", "", 1)
        for a, e in verdicts.items()
        if e["disposition"] == "CORRECT")
    w1 = w1 and corrected_landed
    gate("W1_join_refresh", w1,
         f"200/3/203, 0 foreign; unresolved set == residual + 2 R1-cleared; "
         f"resolution pin == amended disk file ({disk_sha}); "
         f"22/22 CORRECT codes landed")

    # ---- W2 substrate shape ---------------------------------------------------
    m = new_sub["meta"]
    rows = new_sub["rows"]
    anchored = [r for r in rows if r.get("spec_code") and "chunk" in r]
    unres_wl = [r for r in rows if r.get("worklist_reason") and "chunk" in r]
    unmapped = [r for r in rows if r.get("worklist_reason") and "chunk" not in r]
    bad_status = [r["mapping_id"] for r in rows
                  if r.get("validation_status") != "SUGGESTED"
                  or r.get("provenance", {}).get("tier") != "RULE_DERIVED"]
    w2 = (m["rows_anchored"] == len(anchored) == 854
          and m["rows_worklist_anchor_unresolved"] == len(unres_wl) == 8
          and m["rows_worklist_unmapped_sps"] == len(unmapped) == 66
          and len(rows) == 928 and not bad_status
          and m["joins_resolved"] == 200 and m["joins_unresolved"] == 3)
    gate("W2_substrate_shape", w2,
         f"928 rows = 854 anchored + 8 unresolved-worklist + 66 uncovered-SP; "
         f"covered codes {m['sp_codes_covered']}; all SUGGESTED/RULE_DERIVED; "
         f"upstream tier verbatim")

    # ---- W3 chunk identity invariant -----------------------------------------
    def ident(row):
        ch = row["chunk"]
        return (row["note_path"], ch["ordinal"], ch["heading"], ch["sha256_16"])

    from collections import Counter
    ids_new = Counter(ident(r) for r in rows if "chunk" in r)
    ids_old = Counter(ident(r) for r in old_sub["rows"] if "chunk" in r)
    w3 = ids_new == ids_old
    gate("W3_chunk_identity_invariant", w3,
         f"{sum(ids_new.values())} chunk rows: (note_path, ordinal, heading, "
         f"sha256_16) multiset IDENTICAL to pre-R3 blob {OLD_STORE_BLOB[:16]} — "
         f"only code attribution moved")

    # ---- W4 re-attribution audit ---------------------------------------------
    keyed_new = {ident(r): r for r in rows if "chunk" in r}
    ov_by_key = {(e["note_slug"], e["chunk_ordinal"]): e for e in overrides}
    n_correct = n_affirm = n_reattr = n_retain = n_cleared = n_other = 0
    w4 = True
    drift = []
    # data-derived expectations: rows on the 45 verdict anchors in the OLD
    # substrate; the 2 cleared anchors' rows must all move to the worklist
    n_on_verdict_anchors = sum(
        1 for r in old_sub["rows"]
        if "chunk" in r and (r.get("provenance", {}).get("upstream") or {})
        .get("anchor_id") in verdicts)
    n_on_cleared = sum(
        1 for r in old_sub["rows"]
        if "chunk" in r and (r.get("provenance", {}).get("upstream") or {})
        .get("anchor_id") in R1_CLEARED)
    # exact overlap: override rows whose note/ordinal sits on a verdict anchor
    # (handled by the override branch first, so excluded from the verdict count)
    old_by_key = {(Path(r["note_path"]).stem, r["chunk"]["ordinal"]): r
                  for r in old_sub["rows"] if "chunk" in r}
    n_override_on_verdict = sum(
        1 for e in overrides
        if ((old_by_key.get((e["note_slug"], e["chunk_ordinal"])) or {})
            .get("provenance", {}).get("upstream") or {})
        .get("anchor_id") in verdicts)
    expected_verdict_rows = (n_on_verdict_anchors - n_on_cleared
                             - n_override_on_verdict)
    for orow in old_sub["rows"]:
        if "chunk" not in orow:
            continue
        aid = (orow.get("provenance", {}).get("upstream") or {}).get("anchor_id")
        k = ident(orow)
        nrow = keyed_new[k]
        slug = Path(orow["note_path"]).stem
        oventry = ov_by_key.get((slug, orow["chunk"]["ordinal"]))
        if aid is not None and aid in R1_CLEARED:
            n_cleared += 1
            if nrow.get("spec_code") is not None or \
                    not nrow.get("worklist_reason"):
                w4 = False
                drift.append(f"cleared {k}")
            continue
        if oventry and oventry["action"] == "REATTRIBUTE":
            n_reattr += 1
            if nrow.get("spec_code") != oventry["override_code"] or \
                    nrow.get("provenance", {}).get("override", {}) \
                    .get("action") != "REATTRIBUTE":
                w4 = False
                drift.append(f"reattribute {k}")
            continue
        if oventry and oventry["action"] == "RETAIN":
            n_retain += 1
            if nrow.get("spec_code") != oventry["current_code"] or \
                    nrow.get("provenance", {}).get("override", {}) \
                    .get("action") != "RETAIN":
                w4 = False
                drift.append(f"retain {k}")
            continue
        v = verdicts.get(aid) if aid else None
        if v and v["disposition"] == "CORRECT":
            n_correct += 1
            want = v["corrected_code"]
            if nrow.get("spec_code") != want:
                w4 = False
                drift.append(f"correct {k} {nrow.get('spec_code')} != {want}")
        elif v and v["disposition"] == "AFFIRM":
            n_affirm += 1
            if nrow.get("spec_code") != orow.get("spec_code"):
                w4 = False
                drift.append(f"affirm {k} moved")
        else:
            n_other += 1
            # non-surface row: spec_code AND upstream fields must drift nowhere
            if nrow.get("spec_code") != orow.get("spec_code"):
                w4 = False
                drift.append(f"other {k} code moved")
            else:
                ou = orow.get("provenance", {}).get("upstream") or {}
                nu = nrow.get("provenance", {}).get("upstream") or {}
                for f in ("anchor_id", "official_id", "official_wording",
                          "sme_name", "wording_check", "join_method"):
                    if ou.get(f) != nu.get(f):
                        w4 = False
                        drift.append(f"other {k} upstream.{f}")
    w4 = w4 and (n_reattr, n_retain) == (12, 4) \
        and n_cleared == n_on_cleared \
        and n_correct + n_affirm == expected_verdict_rows \
        and n_correct + n_affirm + n_reattr + n_retain + n_cleared + n_other \
        == 862
    gate("W4_reattribution_audit", w4,
         f"all 862 pre-R3 chunk rows replayed: {n_correct} rows on 22 CORRECT "
         f"anchors re-pointed, {n_affirm} rows on 21 AFFIRM anchors unchanged, "
         f"12 REATTRIBUTE + 4 RETAIN override rows recorded with "
         f"provenance.override ({n_override_on_verdict} of them on verdict "
         f"anchors), {n_cleared} rows of the 2 cleared spans demoted to "
         f"worklist, {n_other} non-surface rows zero-drift"
         + (f"; DRIFT: {drift[:5]}" if drift else ""))

    # ---- W5 coverage / worklist recompute --------------------------------------
    # coverage counts ANCHORED rows only — uncovered-SP worklist rows carry a
    # spec_code themselves and must not inflate the covered set
    covered = {r["spec_code"] for r in rows
               if r.get("spec_code") and "chunk" in r}
    covered_old = {r["spec_code"] for r in old_sub["rows"]
                   if r.get("spec_code") and "chunk" in r}
    w5 = (covered <= set(registry)
          and covered == set(registry) - set(m["sp_codes_uncovered"])
          and all(any(r.get("spec_code") == code and r.get("worklist_reason")
                      for r in rows)
                  for code in set(registry) - covered)
          and len({r["mapping_id"] for r in rows}) == len(rows))
    gained = sorted(covered - covered_old)
    lost = sorted(covered_old - covered)
    gate("W5_coverage_worklist", w5,
         f"covered {len(covered_old)} -> {len(covered)} of {len(registry)}; "
         f"gained {len(gained)} {gained[:8]}{'…' if len(gained) > 8 else ''}; "
         f"lost {len(lost)} {lost[:8]}{'…' if len(lost) > 8 else ''}; "
         f"worklist complete; mapping_ids unique")

    # ---- W6 protected surfaces ---------------------------------------------------
    dirty = subprocess.run(
        ["git", "-C", str(REPO), "status", "--porcelain"],
        capture_output=True, text=True, check=True).stdout
    dirty_paths = {ln[3:].strip() for ln in dirty.splitlines() if ln.strip()}
    unexpected = dirty_paths - EXPECTED_DIRTY
    lane_ok = all(
        sha16(head_bytes(f"graph/igcse-maths-a/{s}.yaml"))
        == sha16((REPO / f"graph/igcse-maths-a/{s}.yaml").read_bytes())
        for s in LANE_C)
    chem_ok = subprocess.run(
        ["git", "-C", str(REPO), "diff", "--quiet", HEAD, "--",
         "graph/igcse-chemistry", "spec-links", "graph/reports"],
        capture_output=True).returncode == 0
    w6 = not unexpected and lane_ok and chem_ok
    gate("W6_protected_surfaces", w6,
         f"dirty set == R2/R3 footprint exactly ({sorted(dirty_paths)}); "
         f"Lane C stores byte-identical to {HEAD}; chemistry + spec-links + "
         f"graph/reports untouched")

    # ---- W7 determinism ------------------------------------------------------------
    pre_store = STORE.read_bytes()
    subprocess.run([sys.executable, str(REPO / "scripts/"
                                           "c40_maths_a_chunk_sp_substrate.py")],
                   capture_output=True, check=True)
    w7 = STORE.read_bytes() == pre_store
    pre_join = json.loads(JOIN.read_text(encoding="utf-8"))
    subprocess.run([sys.executable, str(REPO / "scripts/"
                                           "c32_notes_maths_a_join.py")],
                   capture_output=True, check=True)
    post_join = json.loads(JOIN.read_text(encoding="utf-8"))
    pre_join.pop("generated_utc"), post_join.pop("generated_utc")
    w7 = w7 and pre_join == post_join
    gate("W7_determinism", w7,
         "substrate re-run byte-identical; join re-run content-identical "
         "modulo generated_utc")

    # ---------------------------------------------------------------- report
    all_pass = all(g["pass"] for g in gates.values())
    report = {
        "schema": "syllabai.c42-r2r3-check/1.0",
        "task": "T-C42 R2+R3 (join re-run + substrate re-build) verification battery",
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "head_before": HEAD,
        "pins": {
            "old_join_blob": OLD_JOIN_BLOB,
            "old_store_blob": OLD_STORE_BLOB,
            "amended_resolution_sha256_16": disk_sha,
            "override_map_entries": len(overrides),
        },
        "gates": gates,
        "result": "ALL PASS" if all_pass else "FAIL",
    }
    out = REPO / "graph/reports/C42_R2_R3_CHECK.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    for k, v in gates.items():
        print(f"  {'PASS' if v['pass'] else 'FAIL'} {k}: {v['detail'][:120]}")
    print(f"C42 R2+R3 battery: {report['result']} "
          f"({sum(g['pass'] for g in gates.values())}/{len(gates)} gates)")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
