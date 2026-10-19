#!/usr/bin/env python3
"""c42_r11_r12_join_substrate_check.py — T-C42 R11+R12 verification battery.

The R11/R12 lanes are the scope §7 loop's deterministic re-runs over the
C42-R10-amended resolution (the third R1-shaped round's product; the operator
directive's "then R7/R8/R9 again"):

  W1 join refresh      198/5/203 census UNCHANGED (R10 cleared 0 anchors), 0
                       foreign codes, exact unresolved id set (residual + 2
                       R1-cleared + 2 R6-cleared), resolution pin == the
                       amended disk file, 2/2 R10 CORRECT codes landed
                       verbatim (2.2A / 2.2C) + the related-calculations
                       STANDING pin (1.8D)
  W2 substrate shape   meta consistent with the refreshed surface
                       (841 anchored / 21 unresolved-span worklist incl. the
                       loop's first DEMOTE / 61 uncovered-SP / 127 covered),
                       every row SUGGESTED + RULE_DERIVED
  W3 chunk identity    the (note_path, ordinal, heading, sha256_16) multiset is
                       IDENTICAL to the pre-R12 blob (the a26f3aa/R10-era
                       store 80c883dcde552485) — only code attribution moved
                       and one row moved to the worklist class with its chunk
                       block intact
  W4 re-attribution    every pre-R12 chunk row's expected post-R12 state is
                       replayed deterministically: R10 CORRECT anchors
                       re-point, the R10 DEMOTE row moves to the worklist with
                       provenance.override, R10-map REATTRIBUTE rows land,
                       R1/R6 rulings still stand (incl. the 2 subsumed entries
                       riding the join), the R6-cleared spans stay worklist,
                       all other rows zero-drift
  W5 coverage/worklist covered set == recomputed, worklist complete, mapping_id
                       unique; the 125-code R9-era bound stays on its own
                       record (gained/lost computed, never assumed)
  W6 protected surfaces working-tree diff limited to the R11/R12 footprint;
                       Lane C stores, chemistry, the R10-amended resolution
                       file and the C42 scope/R0-R10 records byte-untouched
                       vs HEAD
  W7 determinism       substrate re-run byte-identical; join re-run
                       content-identical modulo generated_utc

Emits graph/reports/C42_R11_R12_CHECK.json.
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
OLD_JOIN_BLOB = "a999481621d3bb3a47d72b8294b3a03bfbe416a2"
OLD_STORE_BLOB = "80c883dcde552485aa961d30585459dbc198c57f"
HEAD = "a26f3aa"
RES = REPO / f"SME-ExamQuestion/{COURSE}/spec_point_resolution.json"
R1_CLEARED = {"spcpt_8Wtthy9gt8B5xsVW", "spcpt_3fMGfNtg3hXMg6gC"}
R6_CLEARED = {"spcpt_mVXT4jbXQPrzhHvz", "spcpt_hK2H8q4Y8NYv833v"}
RESIDUAL = "spcpt_QWXhzVp2S3VYZdZc"
RC_ANCHOR = "spcpt_crKbmb6wVjM4yPJh"  # related-calculations — R10 STANDING
LANE_C = ["concepts", "concept_edges", "spec_command_kinds"]
EXPECTED_DIRTY = {
    "scripts/c32_notes_maths_a_join.py",
    "scripts/c40_maths_a_chunk_sp_substrate.py",
    "scripts/c42_r11_r12_join_substrate_check.py",
    "Official-Specifications/parsed/_derived/notes-join/"
    f"{COURSE}.json",
    "graph/igcse-maths-a/spec_chunk_mappings.yaml",
    "graph/reports/C42_R11_R12_CHECK.json",
    "graph/reports/C42_R11_R12_JOIN_SUBSTRATE_RECORD.md",
    "graph/reports/C42_R11_R12_JOIN_SUBSTRATE_RECORD.json",
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
    new_sub = yaml.safe_load(STORE.read_text(encoding="utf-8"))
    old_sub = yaml.safe_load(blob(OLD_STORE_BLOB).decode("utf-8"))
    vdoc = yaml.safe_load((REPO / "scripts/c42_r10_repair_verdicts.yaml")
                          .read_text(encoding="utf-8"))
    verdicts = vdoc["verdicts"]
    adjud = vdoc.get("note_level_adjudications", {})
    ov1 = yaml.safe_load((REPO / "scripts/c42_section_overrides.yaml")
                         .read_text(encoding="utf-8"))["overrides"]
    ov6doc = yaml.safe_load((REPO / "scripts/c42_section_overrides_r6.yaml")
                            .read_text(encoding="utf-8"))
    ov6 = ov6doc["overrides"]
    subsume = {(x["note_slug"], int(x["chunk_ordinal"]))
               for x in ov6doc.get("subsumed_r1_entries") or []}
    ov10doc = yaml.safe_load((REPO / "scripts/c42_section_overrides_r10.yaml")
                             .read_text(encoding="utf-8"))
    ov10 = ov10doc["overrides"]
    r6verdicts = yaml.safe_load((REPO / "scripts/c42_r6_repair_verdicts.yaml")
                                .read_text(encoding="utf-8"))["verdicts"]
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
    nby = {r["note_path"]: r for r in new_join["joins"]}
    corrected_landed = all(
        nby[np_]["resolved_code"] == e["corrected_code"].replace("4MA1-", "", 1)
        for np_, e in ((  # the 2 R10 CORRECT anchors, via their note paths
            "notes/2-equations-formulae-and-identities/expanding-brackets/expanding-triple-brackets.json",
            verdicts["spcpt_GVgyB5BVfNDYGf8M"]),
            ("notes/2-equations-formulae-and-identities/algebraic-fractions/algebraic-fractions.json",
             verdicts["spcpt_pqWsmktWyMCRfTk6"])))
    standing_pin = (nby["notes/1-numbers-and-the-number-system/number-toolkit/"
                        "related-calculations.json"]["resolved_code"] == "1.8D"
                    and adjud.get("related-calculations-note-join", {}).get("ruling")
                    == "THE NOTE-LEVEL JOIN STANDS")
    w1 = w1 and corrected_landed and standing_pin
    gate("W1_join_refresh", w1,
         f"198/5/203 census UNCHANGED (0 anchors cleared at R10), 0 foreign; "
         f"unresolved set == residual + 2 R1-cleared + 2 R6-cleared; resolution "
         f"pin == amended disk file ({disk_sha}); 2/2 R10 CORRECT codes landed "
         f"verbatim (H-2.2A / H-2.2C); related-calculations STANDING at 1.8D")

    # ---- W2 substrate shape ---------------------------------------------------
    m = new_sub["meta"]
    rows = new_sub["rows"]
    anchored = [r for r in rows if r.get("spec_code") and "chunk" in r]
    unres_wl = [r for r in rows if r.get("worklist_reason") and "chunk" in r]
    unmapped = [r for r in rows if r.get("worklist_reason") and "chunk" not in r]
    bad_status = [r["mapping_id"] for r in rows
                  if r.get("validation_status") != "SUGGESTED"
                  or r.get("provenance", {}).get("tier") != "RULE_DERIVED"]
    demoted = [r for r in unres_wl
               if (r.get("provenance", {}).get("override") or {}).get("action")
               == "DEMOTE_TO_WORKLIST"]
    w2 = (m["rows_anchored"] == len(anchored) == 841
          and m["rows_worklist_anchor_unresolved"] == len(unres_wl) == 21
          and m["rows_worklist_unmapped_sps"] == len(unmapped) == 61
          and len(rows) == 923 and not bad_status
          and m["joins_resolved"] == 198 and m["joins_unresolved"] == 5
          and m["sp_codes_covered"] == 127
          and len(demoted) == 1
          and demoted[0]["note_path"].endswith("related-calculations.json")
          and demoted[0]["chunk"]["ordinal"] == 2)
    gate("W2_substrate_shape", w2,
         f"923 rows = 841 anchored + 21 unresolved-span worklist (incl. the "
         f"loop's first DEMOTE: related-calculations ord 2, chunk identity "
         f"intact) + 61 uncovered-SP; covered codes {m['sp_codes_covered']}; "
         f"all SUGGESTED/RULE_DERIVED")

    # ---- W3 chunk identity invariant -----------------------------------------
    def ident(row):
        ch = row["chunk"]
        return (row["note_path"], ch["ordinal"], ch["heading"], ch["sha256_16"])

    ids_new = Counter(ident(r) for r in rows if "chunk" in r)
    ids_old = Counter(ident(r) for r in old_sub["rows"] if "chunk" in r)
    w3 = ids_new == ids_old
    gate("W3_chunk_identity_invariant", w3,
         f"{sum(ids_new.values())} chunk rows: (note_path, ordinal, heading, "
         f"sha256_16) multiset IDENTICAL to pre-R12 blob {OLD_STORE_BLOB[:16]} — "
         f"only code attribution moved; the DEMOTE kept its chunk block")

    # ---- W4 re-attribution audit ---------------------------------------------
    keyed_new = {ident(r): r for r in rows if "chunk" in r}
    ov_by_key = {}
    for e in ov1:
        ov_by_key.setdefault((e["note_slug"], e["chunk_ordinal"]), e)
    for e in ov6:
        ov_by_key.setdefault((e["note_slug"], e["chunk_ordinal"]), e)
    for e in ov10:
        ov_by_key.setdefault((e["note_slug"], e["chunk_ordinal"]), e)
    n_correct = n_reattr = n_retain = n_cleared = n_subsumed = n_demote = n_other = 0
    w4 = True
    drift = []
    n_on_cleared = sum(
        1 for r in old_sub["rows"]
        if "chunk" in r and (r.get("provenance", {}).get("upstream") or {})
        .get("anchor_id") in (R1_CLEARED | R6_CLEARED))
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
            v6 = r6verdicts.get(aid) if aid else None
            want = v6["corrected_code"] if v6 and v6["disposition"] == "CORRECT" else None
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
        if oventry and oventry["action"] == "DEMOTE_TO_WORKLIST":
            n_demote += 1
            ov = nrow.get("provenance", {}).get("override", {})
            if nrow.get("spec_code") is not None or \
                    not nrow.get("worklist_reason") or \
                    ov.get("action") != "DEMOTE_TO_WORKLIST":
                w4 = False
                drift.append(f"demote {k}")
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
        elif aid == RC_ANCHOR:
            n_other += 1
            # the R10 STANDING pin: the note keeps 1.8D on every non-demoted row
            if nrow.get("spec_code") != "4MA1-1.8D":
                w4 = False
                drift.append(f"standing {k} {nrow.get('spec_code')}")
        elif v and v["disposition"] == "UNRESOLVED":
            w4 = False
            drift.append(f"unresolved-anchor row not demoted {k}")
        else:
            n_other += 1
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
    n_r10_reattr = sum(1 for e in ov10 if e["action"] == "REATTRIBUTE")
    n_r6_reattr = sum(1 for e in ov6 if e["action"] == "REATTRIBUTE")
    n_r1_reattr = sum(1 for e in ov1 if e["action"] == "REATTRIBUTE") - len(subsume)
    n_r1_retain = sum(1 for e in ov1 if e["action"] == "RETAIN")
    w4 = w4 and (n_reattr, n_retain, n_demote) == \
        (n_r1_reattr + n_r6_reattr + n_r10_reattr, n_r1_retain, 1) \
        and n_cleared == n_on_cleared and n_subsumed == len(subsume) \
        and n_correct + n_reattr + n_retain + n_cleared + n_subsumed + n_demote + n_other == 862
    gate("W4_reattribution_audit", w4,
         f"all 862 pre-R12 chunk rows replayed: {n_correct} rows on the 2 R10 "
         f"CORRECT anchors re-pointed, {n_reattr} REATTRIBUTE override rows "
         f"(R1 {n_r1_reattr} + R6 {n_r6_reattr} + R10 {n_r10_reattr}) + "
         f"{n_retain} RETAIN rows recorded with provenance.override, "
         f"{n_subsumed} R1 entries ride the join via the R6 subsumption "
         f"registry, {n_demote} DEMOTE row in the worklist class with its "
         f"chunk identity, {n_cleared} rows of the 4 cleared spans worklist, "
         f"{n_other} non-surface rows zero-drift (incl. the related-"
         f"calculations STANDING rows)"
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
         f"gained {gained}; lost {lost}; worklist complete; mapping_ids unique")

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
                  "graph/reports/C42_R10_RESOLUTION_REPAIR_RECORD.md",
                  "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md",
                  "graph/reports/C42_R9_REGATE_CHECK.json"])
    w6 = not unexpected and lane_ok and chem_ok and res_ok and c42_ok
    gate("W6_protected_surfaces", w6,
         f"dirty set == the R11/R12 footprint exactly ({len(dirty_paths)} paths); "
         f"Lane C stores, chemistry substrate, the R10-amended resolution, the "
         f"C42 scope/R0-R10 records byte-identical to HEAD {HEAD}"
         + (f"; UNEXPECTED: {sorted(unexpected)[:4]}" if unexpected else ""))

    # ---- W7 determinism ------------------------------------------------------------
    store_before = STORE.read_bytes()
    join_before = JOIN.read_bytes()
    subprocess.run(
        ["python3", str(REPO / "scripts/c40_maths_a_chunk_sp_substrate.py")],
        capture_output=True, text=True, check=True)
    w7a = STORE.read_bytes() == store_before
    subprocess.run(
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
        "schema": "syllabai.c42-r11-r12-check/1.0",
        "task": "T-C42 R11+R12 (join re-run + substrate re-build over the "
                "C42-R10-amended resolution; the operator directive's "
                "'then R7/R8/R9 again')",
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "all_pass": all_pass,
        "gates": gates,
        "pins": {
            "head": HEAD,
            "old_join_blob": OLD_JOIN_BLOB,
            "old_store_blob": OLD_STORE_BLOB,
            "amended_resolution_sha256_16": disk_sha,
            "join_198_5": True,
            "store_rows": 923,
            "anchored": 841,
            "unresolved_span_worklist": 21,
            "demoted_worklist": 1,
            "unmapped_sps": 61,
            "covered_codes": 127,
        },
    }
    (REPO / "graph/reports/C42_R11_R12_CHECK.json").write_text(
        json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("C42 R11+R12 CHECK —", "ALL PASS" if all_pass else "FAILURES PRESENT")
    for name, g in gates.items():
        print(f"  {name}: {'PASS' if g['pass'] else 'FAIL'} — {g['detail'][:150]}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
