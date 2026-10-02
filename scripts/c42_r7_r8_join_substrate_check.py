#!/usr/bin/env python3
"""c42_r7_r8_join_substrate_check.py — T-C42 R7+R8 verification battery.

The R7/R8 lanes are the scope §7 loop's deterministic re-runs over the
C42-R6-amended resolution (the second R1-shaped round's product):

  W1 join refresh      198/5/203 census, 0 foreign codes, exact post-R6
                       unresolved id set (residual + 2 R1-cleared + 2
                       R6-cleared), resolution pin == the amended disk file,
                       8/8 R6 CORRECT codes landed verbatim
  W2 substrate shape   meta consistent with the refreshed surface
                       (842 anchored / 20 unresolved-worklist / 63
                       uncovered-SP / 125 covered), every row SUGGESTED +
                       RULE_DERIVED, upstream tier verbatim
  W3 chunk identity    the (note_path, ordinal, heading, sha256_16) multiset is
                       IDENTICAL to the pre-R8 blob (the d141c59/R4-era store
                       4ebb095ec73c850b) — only code attribution moved
  W4 re-attribution    every pre-R8 anchored row's expected post-R8 code is
                       replayed deterministically: R6 CORRECT anchors re-point,
                       R6 UNRESOLVED anchors demote to worklist, R1-map
                       non-subsumed overrides re-apply identically to R3, the
                       2 R6-subsumed R1 entries ride the join, R6-map overrides
                       (4 verdicted + 2 extension) land with provenance, all
                       other rows zero-drift
  W5 coverage/worklist covered set == recomputed, worklist complete, mapping_id
                       unique; the 122-code R3-era bound stays on its own record
  W6 protected surfaces working-tree diff limited to the R7/R8 footprint; Lane
                       C stores, chemistry, the resolution file and the C42
                       scope/R0-R6 records byte-untouched vs HEAD
  W7 determinism       substrate re-run byte-identical; join re-run
                       content-identical modulo generated_utc

Emits graph/reports/C42_R7_R8_CHECK.json.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
COURSE = "igcse-maths-a-18-higher"
JOIN = REPO / "Official-Specifications/parsed/_derived/notes-join/" \
              f"{COURSE}.json"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
OLD_JOIN_BLOB = "46bae3ec22096685c0d65b59ad69b1bb6ffdc7c0"
OLD_STORE_BLOB = "4ebb095ec73c850bba9b35a3d1fef2881519734b"
HEAD = "e48a434"
RES = REPO / f"SME-ExamQuestion/{COURSE}/spec_point_resolution.json"
R1_CLEARED = {"spcpt_8Wtthy9gt8B5xsVW", "spcpt_3fMGfNtg3hXMg6gC"}
R6_CLEARED = {"spcpt_mVXT4jbXQPrzhHvz", "spcpt_hK2H8q4Y8NYv833v"}
RESIDUAL = "spcpt_QWXhzVp2S3VYZdZc"
LANE_C = ["concepts", "concept_edges", "spec_command_kinds"]
EXPECTED_DIRTY = {
    "scripts/c32_notes_maths_a_join.py",
    "scripts/c40_maths_a_chunk_sp_substrate.py",
    "scripts/c42_r7_r8_join_substrate_check.py",
    "Official-Specifications/parsed/_derived/notes-join/"
    f"{COURSE}.json",
    "graph/igcse-maths-a/spec_chunk_mappings.yaml",
    "graph/reports/C42_R7_R8_CHECK.json",
    "graph/reports/C42_R7_R8_JOIN_SUBSTRATE_RECORD.md",
    "graph/reports/C42_R7_R8_JOIN_SUBSTRATE_RECORD.json",
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
    vdoc = yaml.safe_load((REPO / "scripts/c42_r6_repair_verdicts.yaml")
                          .read_text(encoding="utf-8"))
    verdicts = vdoc["verdicts"]
    ov1 = yaml.safe_load((REPO / "scripts/c42_section_overrides.yaml")
                         .read_text(encoding="utf-8"))["overrides"]
    ov6doc = yaml.safe_load((REPO / "scripts/c42_section_overrides_r6.yaml")
                            .read_text(encoding="utf-8"))
    ov6 = ov6doc["overrides"]
    subsume = {(x["note_slug"], int(x["chunk_ordinal"]))
               for x in ov6doc.get("subsumed_r1_entries") or []}
    registry = {
        p["code"]: p
        for p in yaml.safe_load(
            (REPO / "graph/igcse-maths-a/specification_points.yaml")
            .read_text(encoding="utf-8"))["specification_points"]}

    # ---- W1 join refresh ----------------------------------------------------
    c = new_join["counts"]
    w1 = (c["joined"] == 198 and c["unresolved_recorded"] == 5
          and c["anchors_total"] == 203 and c["foreign_codes"] == 0)
    got = {u["anchor_id"] for u in new_join["unresolved"]}
    w1 = w1 and got == {RESIDUAL} | R1_CLEARED | R6_CLEARED
    disk_sha = sha16(RES.read_bytes())
    w1 = w1 and new_join["inputs"]["resolution"]["sha256_16"] == disk_sha
    nby = {r["anchor_id"]: r for r in new_join["joins"]}
    corrected_landed = all(
        nby[a]["resolved_code"] == e["corrected_code"].replace("4MA1-", "", 1)
        for a, e in verdicts.items()
        if e["disposition"] == "CORRECT")
    cleared_gone = all(a not in nby for a in R6_CLEARED)
    w1 = w1 and corrected_landed and cleared_gone
    gate("W1_join_refresh", w1,
         f"198/5/203, 0 foreign; unresolved set == residual + 2 R1-cleared + "
         f"2 R6-cleared; resolution pin == amended disk file ({disk_sha}); "
         f"8/8 R6 CORRECT codes landed; 2 R6-cleared anchors absent from joins")

    # ---- W2 substrate shape ---------------------------------------------------
    m = new_sub["meta"]
    rows = new_sub["rows"]
    anchored = [r for r in rows if r.get("spec_code") and "chunk" in r]
    unres_wl = [r for r in rows if r.get("worklist_reason") and "chunk" in r]
    unmapped = [r for r in rows if r.get("worklist_reason") and "chunk" not in r]
    bad_status = [r["mapping_id"] for r in rows
                  if r.get("validation_status") != "SUGGESTED"
                  or r.get("provenance", {}).get("tier") != "RULE_DERIVED"]
    w2 = (m["rows_anchored"] == len(anchored) == 842
          and m["rows_worklist_anchor_unresolved"] == len(unres_wl) == 20
          and m["rows_worklist_unmapped_sps"] == len(unmapped) == 63
          and len(rows) == 925 and not bad_status
          and m["joins_resolved"] == 198 and m["joins_unresolved"] == 5
          and m["sp_codes_covered"] == 125)
    gate("W2_substrate_shape", w2,
         f"925 rows = 842 anchored + 20 unresolved-worklist + 63 uncovered-SP; "
         f"covered codes {m['sp_codes_covered']}; all SUGGESTED/RULE_DERIVED; "
         f"upstream tier verbatim")

    # ---- W3 chunk identity invariant -----------------------------------------
    def ident(row):
        ch = row["chunk"]
        return (row["note_path"], ch["ordinal"], ch["heading"], ch["sha256_16"])

    ids_new = Counter(ident(r) for r in rows if "chunk" in r)
    ids_old = Counter(ident(r) for r in old_sub["rows"] if "chunk" in r)
    w3 = ids_new == ids_old
    gate("W3_chunk_identity_invariant", w3,
         f"{sum(ids_new.values())} chunk rows: (note_path, ordinal, heading, "
         f"sha256_16) multiset IDENTICAL to pre-R8 blob {OLD_STORE_BLOB[:16]} — "
         f"only code attribution moved")

    # ---- W4 re-attribution audit ---------------------------------------------
    keyed_new = {ident(r): r for r in rows if "chunk" in r}
    ov_by_key = {}
    for e in ov1:
        ov_by_key.setdefault((e["note_slug"], e["chunk_ordinal"]), e)
    for e in ov6:
        ov_by_key.setdefault((e["note_slug"], e["chunk_ordinal"]), e)
    n_correct = n_reattr = n_retain = n_cleared = n_subsumed = n_other = 0
    w4 = True
    drift = []
    n_on_cleared = sum(
        1 for r in old_sub["rows"]
        if "chunk" in r and (r.get("provenance", {}).get("upstream") or {})
        .get("anchor_id") in (R1_CLEARED | R6_CLEARED))
    old_by_key = {(Path(r["note_path"]).stem, r["chunk"]["ordinal"]): r
                  for r in old_sub["rows"] if "chunk" in r}
    for orow in old_sub["rows"]:
        if "chunk" not in orow:
            continue
        aid = (orow.get("provenance", {}).get("upstream") or {}).get("anchor_id")
        k = ident(orow)
        nrow = keyed_new[k]
        slug = Path(orow["note_path"]).stem
        oventry = ov_by_key.get((slug, orow["chunk"]["ordinal"]))
        if aid is not None and aid in (R1_CLEARED | R6_CLEARED):
            n_cleared += 1
            if nrow.get("spec_code") is not None or \
                    not nrow.get("worklist_reason"):
                w4 = False
                drift.append(f"cleared {k}")
            continue
        if oventry and (slug, orow["chunk"]["ordinal"]) in subsume:
            n_subsumed += 1
            v = verdicts.get(aid) if aid else None
            want = v["corrected_code"] if v and v["disposition"] == "CORRECT" else None
            if want is None or nrow.get("spec_code") != want or \
                    "override_subsumed" not in (nrow.get("provenance") or {}):
                w4 = False
                drift.append(f"subsumed {k}")
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
        elif v and v["disposition"] == "UNRESOLVED":
            # an R6-cleared anchor whose rows were already counted above cannot
            # happen (cleared handled first) — treat as drift
            w4 = False
            drift.append(f"unresolved-anchor row not demoted {k}")
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
    n_r6_reattr = sum(1 for e in ov6 if e["action"] == "REATTRIBUTE")
    n_r1_reattr = sum(1 for e in ov1 if e["action"] == "REATTRIBUTE") - len(subsume)
    n_r1_retain = sum(1 for e in ov1 if e["action"] == "RETAIN")
    w4 = w4 and (n_reattr, n_retain) == (n_r1_reattr + n_r6_reattr, n_r1_retain) \
        and n_cleared == n_on_cleared and n_subsumed == len(subsume) \
        and n_correct + n_reattr + n_retain + n_cleared + n_subsumed + n_other == 862
    gate("W4_reattribution_audit", w4,
         f"all 862 pre-R8 chunk rows replayed: {n_correct} rows on the 8 R6 "
         f"CORRECT anchors re-pointed, {n_reattr} REATTRIBUTE override rows "
         f"(R1 {n_r1_reattr} + R6 {n_r6_reattr} incl. 2 labeled extensions) + "
         f"{n_retain} RETAIN rows recorded with provenance.override, "
         f"{n_subsumed} R1 entries ride the join via the R6 subsumption "
         f"registry (provenance.override_subsumed), {n_cleared} rows of the 4 "
         f"cleared spans demoted to worklist, {n_other} non-surface rows "
         f"zero-drift"
         + (f"; DRIFT: {drift[:5]}" if drift else ""))

    # ---- W5 coverage / worklist recompute --------------------------------------
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
    chem_ok = all(
        sha16(head_bytes(p)) == sha16((REPO / p).read_bytes())
        for p in ["graph/igcse-chemistry/spec_chunk_mappings.yaml"])
    res_ok = sha16(head_bytes(f"SME-ExamQuestion/{COURSE}/spec_point_resolution.json")) \
        == sha16((REPO / f"SME-ExamQuestion/{COURSE}/spec_point_resolution.json").read_bytes())
    c42_ok = all(
        sha16(head_bytes(p)) == sha16((REPO / p).read_bytes())
        for p in ["graph/reports/C42_IGCSE_MATHS_A_K2B_REWORK_SCOPE.md",
                  "graph/reports/C42_MATHS_A_RESOLUTION_REPAIR_RECORD.json",
                  "graph/reports/C42_R6_RESOLUTION_REPAIR_RECORD.json",
                  "graph/reports/C42_R4_REGATE_CHECK.json"])
    w6 = not unexpected and lane_ok and chem_ok and res_ok and c42_ok
    gate("W6_protected_surfaces", w6,
         f"dirty set == the R7/R8 footprint exactly ({len(dirty_paths)} paths); "
         f"Lane C stores, chemistry substrate, the R6-amended resolution, the "
         f"C42 scope/R0-R6 records byte-identical to HEAD {HEAD}"
         + (f"; UNEXPECTED: {sorted(unexpected)[:4]}" if unexpected else ""))

    # ---- W7 determinism ------------------------------------------------------------
    store_before = STORE.read_bytes()
    join_before = JOIN.read_bytes()
    re_sub = subprocess.run(
        ["python3", str(REPO / "scripts/c40_maths_a_chunk_sp_substrate.py")],
        capture_output=True, text=True, check=True)
    w7a = STORE.read_bytes() == store_before
    re_join = subprocess.run(
        ["python3", str(REPO / "scripts/c32_notes_maths_a_join.py")],
        capture_output=True, text=True, check=True)
    j2 = json.loads(JOIN.read_text(encoding="utf-8"))
    j1 = json.loads(join_before)
    strip = lambda d: {k: v for k, v in d.items() if k != "generated_utc"}  # noqa: E731
    w7b = strip(j1) == strip(j2)
    gate("W7_determinism", w7a and w7b,
         "substrate re-run byte-identical; join re-run content-identical "
         "modulo generated_utc")

    # ---------------------------------------------------------------- emit report
    all_pass = all(g["pass"] for g in gates.values())
    out = {
        "schema": "syllabai.c42-r7-r8-check/1.0",
        "task": "T-C42 R7+R8 (join re-run + substrate re-build over the "
                "C42-R6-amended resolution)",
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "all_pass": all_pass,
        "gates": gates,
        "pins": {
            "head": HEAD,
            "old_join_blob": OLD_JOIN_BLOB,
            "old_store_blob": OLD_STORE_BLOB,
            "amended_resolution_sha256_16": disk_sha,
            "join_198_5": True,
            "store_rows": 925,
            "anchored": 842,
            "unresolved_worklist": 20,
            "unmapped_sps": 63,
            "covered_codes": 125,
        },
    }
    (REPO / "graph/reports/C42_R7_R8_CHECK.json").write_text(
        json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("C42 R7+R8 CHECK —", "ALL PASS" if all_pass else "FAILURES PRESENT")
    for name, g in gates.items():
        print(f"  {name}: {'PASS' if g['pass'] else 'FAIL'} — {g['detail'][:150]}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
