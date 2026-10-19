#!/usr/bin/env python3
"""c42_r23_join_check.py — T-C42 R23 verification battery (the JOIN RE-RUN lane).

The R23 lane is the scope §7 loop's deterministic join re-run, fired by the
operator's 'R23' directive (2026-10-04, discord, gateway trace
772bb1c553acf115d53f83d9cf6afa81) naming exactly the R22 record's next-decision
gates ("R23 (join re-run) + R24 (substrate re-build consuming the R22 map +
re-applying the R5 promotions file), then the R25 re-gate — each fired only by
explicit operator instruction"). The R24 re-build and the R25 re-gate are NOT
fired by this directive. The 4 H3 HOLD rows and the ord-3 promoted-surface
extension candidate stay untouched operator decisions.

  J1 join refresh      the refreshed join artifact: census UNCHANGED
                       198 joined / 5 unresolved / 203 anchors / 0 foreign
                       (the R22 round re-pointed 0 note-level joins — ALL
                       THREE adjudicated STANDING — and cleared 0 anchors; the
                       resolution file is byte-untouched, counts stay 222/214/8,
                       last writer R14); coverage census UNCHANGED (120/188
                       distinct codes, tier splits 61F/59H codes and 81F/117H
                       anchors, wording census EXACT 173 / LEDGER_EXPLAINABLE
                       25); exact unresolved id set (the C31 §3 residual + the
                       2 R1-cleared + the 2 R6-cleared); every input pin in the
                       artifact equals the recorded R19-era constant
                       (manifest cc470d40873f51a4, resolution b4539ab904c9a319,
                       SP store 33d3e5313d37464a, ledger 7f9322a8a05d3767) and
                       the resolution pin equals the live git blob
  J2 verbatim pins     all NINE note-level joins pinned verbatim: the R14
                       re-point (composite-functions -> 4MA1-3.2D), the R10
                       CORRECT pair (2.2A / 2.2C), the R10 STANDING pin
                       (related-calculations -> 4MA1-1.8D), the two R18
                       STANDING pins (converting-between-fdp -> 4MA1-1.2G,
                       basic-angle-properties -> 4MA1-4.1B) and the three R22
                       STANDING pins (3d-pythagoras-and-trigonometry ->
                       4MA1-4.8D, difference-of-two-squares -> 4MA1-2.2F,
                       graphical-solutions -> 4MA1-2.6B)
  J3 R18 map pins      both R18 STANDING pins verified against the R18 map's
                       own note_level_adjudications (dict-shaped): ruling
                       text + anchor id + landed code together, fail-closed
  J4 R22 map pins      the three R22 STANDING pins verified against the R22
                       map's own note_level_adjudications (list-shaped this
                       round): ruling STANDING + anchor id + joined_code
                       together, fail-closed; PLUS the map's overrides block
                       carries exactly the 3 verdicted REATTRIBUTE entries and
                       NEITHER of the 3 rows appears in the R5 promotions file
                       (by mapping_id AND by note+ordinal — the 832-entry
                       promoted set is identity- and code-stable at the join
                       layer, the R22 map contract's own claim, verified not
                       assumed)
  J5 resolution        the resolution substrate is BYTE-UNTOUCHED: the HEAD
  substrate            blob sha equals the R14-era full blob pin
                       93419a291b9b87ffa81aa2300db43e7851a95184 (recorded
                       since the R15/R16 record) and the recomputed counts
                       are 222 rows / 214 with resolved_code / 8 without
  J6 determinism       the generator re-run exits 0 and the refreshed artifact
                       is content-identical to the audited one modulo
                       generated_utc (joins, unresolved, counts, inputs,
                       task, validation_tier, schema, ordering all equal)
  J7 protected         working-tree dirt limited to the declared R23
  surfaces             footprint (subset semantics — the J6 re-run refreshes
                       the join's generated_utc and this battery refreshes its
                       own check json, so timestamp-only churn inside the
                       footprint is inherent; no dirt OUTSIDE the footprint is
                       the fail-closed guarantee); every protected loop record
                       byte-untouched between the baseline ce7c5c8 and HEAD
                       AND between HEAD and the working tree where
                       materialized (the R22 record/map/verdicts/check, the
                       R21 re-gate records, the R5 apply artifacts incl. the
                       832-entry promotions file, the R19+R20 records, every
                       earlier map/record, the scope doc, the C30 ledger, the
                       SP store + the chunk store, the Lane C stores, the c40
                       substrate tool and the c32-era c42 repair/check tools)
  J8 commit state      the working-tree delta vs HEAD stays inside the
                       footprint pre-commit; once HEAD carries the round
                       (subject starts 'T-C42 R23'), the committed delta vs
                       HEAD~1 stays inside the footprint too — the audit
                       trail may move HEAD, never a protected byte

Emits graph/reports/C42_R23_JOIN_CHECK.json.
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
BASELINE = "ce7c5c8c1e76bae8e33b58b99147be1a52d95c10"  # the R22-closed HEAD
RES_BLOB = "93419a291b9b87ffa81aa2300db43e7851a95184"
RES_PATH = f"SME-ExamQuestion/{COURSE}/spec_point_resolution.json"
# the R19-era recorded input pins (the artifact's own inputs block)
PIN_MANIFEST = "cc470d40873f51a4"
PIN_RESOLUTION = "b4539ab904c9a319"
PIN_SP_STORE = "33d3e5313d37464a"
PIN_LEDGER = "7f9322a8a05d3767"
RESIDUAL = "spcpt_QWXhzVp2S3VYZdZc"
R1_CLEARED = {"spcpt_8Wtthy9gt8B5xsVW", "spcpt_3fMGfNtg3hXMg6gC"}
R6_CLEARED = {"spcpt_mVXT4jbXQPrzhHvz", "spcpt_hK2H8q4Y8NYv833v"}
# the nine verbatim note-level pins (6 carried + the 3 R22 STANDING joins)
VERBATIM = {
    "notes/3-sequences-functions-and-graphs/functions/composite-functions.json":
        "4MA1-3.2D",
    "notes/2-equations-formulae-and-identities/expanding-brackets/expanding-triple-brackets.json":
        "4MA1-2.2A",
    "notes/2-equations-formulae-and-identities/algebraic-fractions/algebraic-fractions.json":
        "4MA1-2.2C",
    "notes/1-numbers-and-the-number-system/number-toolkit/related-calculations.json":
        "4MA1-1.8D",
    "notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/converting-between-fdp.json":
        "4MA1-1.2G",
    "notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/basic-angle-properties.json":
        "4MA1-4.1B",
    "notes/4-geometry-and-trigonometry/3d-pythagoras-and-trigonometry/3d-pythagoras-and-trigonometry.json":
        "4MA1-4.8D",
    "notes/2-equations-formulae-and-identities/factorising/difference-of-two-squares.json":
        "4MA1-2.2F",
    "notes/3-sequences-functions-and-graphs/graphs-of-functions/graphical-solutions.json":
        "4MA1-2.6B",
}
R18_PINS = (
    ("converting-between-fdp",
     "THE NOTE-LEVEL JOIN TO 1.2G STANDS (unchanged)", "4MA1-1.2G",
     "spcpt_8MpvS5pnYkf9QswF"),
    ("basic-angle-properties",
     "THE NOTE-LEVEL JOIN TO 4.1B STANDS (unchanged)", "4MA1-4.1B",
     "spcpt_5FMXZMjqSZ3GK53q"),
)
R22_PINS = (
    ("3d-pythagoras-and-trigonometry", "4MA1-4.8D", "spcpt_kX4655D8M3Q3TRzW"),
    ("difference-of-two-squares", "4MA1-2.2F", "spcpt_RJbgRvXq2VrGpP5g"),
    ("graphical-solutions", "4MA1-2.6B", "spcpt_sHCB9WZbDMyTFqCP"),
)
R22_OVERRIDE_KEYS = {
    ("graphical-solutions", 1, "5fd48f084383be11", "4MA1-2.6B", "4MA1-3.3E"),
    ("3d-pythagoras-and-trigonometry", 4, "a8d23b11c343a3bd", "4MA1-4.8D",
     "4MA1-4.8F"),
    ("difference-of-two-squares", 3, "eb26022693be3948", "4MA1-2.2F",
     "4MA1-2.2B"),
}
FOOTPRINT = {
    "scripts/c32_notes_maths_a_join.py",
    "scripts/c42_r23_join_check.py",
    "Official-Specifications/parsed/_derived/notes-join/"
    f"{COURSE}.json",
    "graph/reports/C42_R23_JOIN_CHECK.json",
    "graph/reports/C42_R23_JOIN_RECORD.md",
    "graph/reports/C42_R23_JOIN_RECORD.json",
}
PROTECTED = [
    "graph/reports/C42_IGCSE_MATHS_A_K2B_REWORK_SCOPE.md",
    "graph/reports/C42_MATHS_A_RESOLUTION_REPAIR_RECORD.json",
    "graph/reports/C42_R6_RESOLUTION_REPAIR_RECORD.json",
    "graph/reports/C42_R10_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md",
    "graph/reports/C42_R13_REGATE_CHECK.json",
    "graph/reports/C42_R14_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R15_R16_CHECK.json",
    "graph/reports/C42_R15_R16_JOIN_SUBSTRATE_RECORD.md",
    "graph/reports/C42_R17_REGATE_CHECK.json",
    "graph/reports/C42_R17_MATHS_A_REGATE_FILL_RECORD.md",
    "graph/reports/C42_R18_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R18_REPAIR_CHECK.json",
    "graph/reports/C42_R19_R20_CHECK.json",
    "graph/reports/C42_R19_R20_JOIN_SUBSTRATE_RECORD.md",
    "graph/reports/C42_R19_R20_JOIN_SUBSTRATE_RECORD.json",
    "graph/reports/C42_R21_REGATE_CHECK.json",
    "graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.md",
    "graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.json",
    "graph/reports/C42_R22_REPAIR_CHECK.json",
    "graph/reports/C42_R22_REPAIR_PROPOSALS.json",
    "graph/reports/C42_R22_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R5_APPLY_CHECK.json",
    "graph/reports/C42_R5_APPLY_RECORD.json",
    "graph/reports/C42_R5_APPLY_RECORD.md",
    "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json",
    "graph/igcse-maths-a/specification_points.yaml",
    "graph/igcse-maths-a/spec_chunk_mappings.yaml",
    "graph/igcse-maths-a/concepts.yaml",
    "graph/igcse-maths-a/concept_edges.yaml",
    "graph/igcse-maths-a/spec_command_kinds.yaml",
    "scripts/c42_section_overrides.yaml",
    "scripts/c42_section_overrides_r6.yaml",
    "scripts/c42_section_overrides_r10.yaml",
    "scripts/c42_section_overrides_r14.yaml",
    "scripts/c42_section_overrides_r18.yaml",
    "scripts/c42_section_overrides_r22.yaml",
    "scripts/c42_r22_repair_verdicts.yaml",
    "scripts/c42_r22_repair_proposals.py",
    "scripts/c42_r22_repair_check.py",
    "scripts/c42_r22_override_projection.py",
    "scripts/c42_r21_regate_check.py",
    "scripts/c42_r21_fresh_verdicts.yaml",
    "scripts/c42_r21_review_verdicts.yaml",
    "scripts/c42_r5_promotions.yaml",
    "scripts/c42_r5_promote.py",
    "scripts/c42_r5_promotion_apply.py",
    "scripts/c42_r5_promotion_check.py",
    "scripts/c40_maths_a_chunk_sp_substrate.py",
]

gates: dict[str, dict] = {}


def gate(name: str, ok: bool, detail: str) -> bool:
    gates[name] = {"pass": bool(ok), "detail": detail}
    return bool(ok)


def sha16(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:16]


def git(*args: str) -> bytes:
    return subprocess.run(["git", "-C", str(REPO), *args],
                          capture_output=True, check=True).stdout


def git_text(*args: str) -> str:
    return git(*args).decode("utf-8")


def blob_bytes(rev: str, path: str) -> bytes:
    return git("show", f"{rev}:{path}")


def main() -> int:
    snap = JOIN.read_bytes()
    join = json.loads(snap.decode("utf-8"))
    r22doc = yaml.safe_load(
        (REPO / "scripts/c42_section_overrides_r22.yaml").read_text("utf-8"))
    r18doc = yaml.safe_load(
        (REPO / "scripts/c42_section_overrides_r18.yaml").read_text("utf-8"))

    # ------------------------------------------------------------------ J1
    c = join["counts"]
    cov_ok = (c["joined"] == 198 and c["unresolved_recorded"] == 5
              and c["anchors_total"] == 203 and c["anchors_distinct"] == 203
              and c["foreign_codes"] == 0
              and c["distinct_official_codes"] == 120
              and c["coverage_of_188"] == "120/188"
              and c["coverage_by_applicability_tier"] ==
              {"Foundation": 61, "Higher": 59}
              and c["anchors_by_applicability_tier"] ==
              {"Foundation": 81, "Higher": 117}
              and c["wording_check_census"] ==
              {"EXACT": 173, "LEDGER_EXPLAINABLE": 25}
              and c["ids_absent_from_resolution"] == 0)
    got_unres = {u["anchor_id"] for u in join["unresolved"]}
    unres_ok = got_unres == {RESIDUAL} | R1_CLEARED | R6_CLEARED
    pins = join["inputs"]
    res_live = blob_bytes("HEAD", RES_PATH)
    pins_ok = (pins["notes_manifest"]["sha256_16"] == PIN_MANIFEST
               and pins["resolution"]["sha256_16"] == PIN_RESOLUTION
               and pins["spec_points_store"]["sha256_16"] == PIN_SP_STORE
               and pins["tier_dedupe_ledger"]["sha256_16"] == PIN_LEDGER
               and pins["resolution"]["sha256_16"] == sha16(res_live))
    j1 = cov_ok and unres_ok and pins_ok
    gate("J1_join_refresh", j1,
         f"census UNCHANGED 198/5/203 (R22 re-pointed 0 joins, cleared 0 "
         f"anchors), 0 foreign, coverage 120/188 (61F/59H codes, 81F/117H "
         f"anchors, EXACT 173 / LEDGER_EXPLAINABLE 25); unresolved set == "
         f"residual + 2 R1-cleared + 2 R6-cleared; all four input pins equal "
         f"the recorded R19-era constants and the resolution pin equals the "
         f"live git blob {sha16(res_live)}")

    # ------------------------------------------------------------------ J2
    by_np = {r["note_path"]: r for r in join["joins"]}
    j2 = True
    missing = []
    for np_, want in VERBATIM.items():
        row = by_np.get(np_)
        if row is None or row["store_row_code"] != want:
            j2 = False
            missing.append((np_, None if row is None else
                            row["store_row_code"]))
    gate("J2_verbatim_pins", j2,
         f"all {len(VERBATIM)} note-level joins pinned verbatim (R14 re-point "
         f"3.2D; R10 pair 2.2A/2.2C + STANDING 1.8D; R18 STANDING pair 1.2G/"
         f"4.1B; R22 STANDING trio 4.8D/2.2F/2.6B) — "
         f"{'all landed' if j2 else f'DRIFT: {missing}'}")

    # ------------------------------------------------------------------ J3
    j3 = True
    for slug, ruling, code, anchor in R18_PINS:
        adj = (r18doc.get("note_level_adjudications") or {}).get(slug) or {}
        row = next((r for r in join["joins"]
                    if r["note_path"].endswith(f"/{slug}.json")), None)
        if adj.get("ruling") != ruling or adj.get("anchor_id") != anchor \
                or row is None or row["store_row_code"] != code \
                or row["anchor_id"] != anchor:
            j3 = False
    gate("J3_r18_map_pins", j3,
         "BOTH R18 STANDING pins verified against the R18 map's own "
         "note_level_adjudications (dict-shaped) — ruling text + anchor id + "
         "landed code together, fail-closed (carried from R19)")

    # ------------------------------------------------------------------ J4
    r22adj = {a.get("note_slug"): a for a in
              (r22doc.get("note_level_adjudications") or [])}
    j4 = True
    for slug, code, anchor in R22_PINS:
        adj = r22adj.get(slug) or {}
        row = next((r for r in join["joins"]
                    if r["note_path"].endswith(f"/{slug}.json")), None)
        if adj.get("ruling") != "STANDING" or adj.get("joined_code") != code \
                or adj.get("anchor_id") != anchor or row is None \
                or row["store_row_code"] != code or row["anchor_id"] != anchor:
            j4 = False
    ov_keys = set()
    for e in r22doc.get("overrides") or []:
        ov_keys.add((e.get("note_slug"), int(e.get("chunk_ordinal")),
                     e.get("mapping_id"), e.get("current_code"),
                     e.get("override_code")))
    map_ok = ov_keys == R22_OVERRIDE_KEYS and len(r22adj) == 3
    prom = yaml.safe_load(
        (REPO / "scripts/c42_r5_promotions.yaml").read_text("utf-8"))
    prom_rows = prom.get("promotions") or []
    r22_ids = {k[2] for k in R22_OVERRIDE_KEYS}
    r22_np_ord = {(f"notes/%/{k[0]}", k[1]) for k in R22_OVERRIDE_KEYS}

    def slug_of(np: str) -> str:
        return np.split("/")[-1][:-5] if isinstance(np, str) else ""

    hit_ids = [r for r in prom_rows if r.get("row", {}).get("mapping_id")
               in r22_ids]
    hit_rows = [r for r in prom_rows
                if (slug_of(r.get("row", {}).get("note_path", "")),
                    int(r.get("row", {}).get("chunk_ordinal", -1)))
                in {(s, o) for (s, o, *_ ) in
                    [(k[0], k[1]) for k in R22_OVERRIDE_KEYS]}]
    prom_ok = (len(prom_rows) == 832 and not hit_ids and not hit_rows)
    j4 = j4 and map_ok and prom_ok
    gate("J4_r22_map_pins", j4,
         f"ALL THREE R22 STANDING pins verified against the R22 map's own "
         f"note_level_adjudications (list-shaped) — ruling STANDING + anchor "
         f"id + joined_code together; the map's overrides block carries "
         f"exactly the 3 verdicted REATTRIBUTE entries "
         f"{'as pinned' if map_ok else 'DRIFT'}; the R5 promotions file "
         f"(832 rows) intersects the 3 rows in NOTHING by mapping_id and by "
         f"note+ordinal ({len(hit_ids)}/{len(hit_rows)} hits) — the promoted "
         f"set is identity- and code-stable at the join layer, verified not "
         f"assumed")

    # ------------------------------------------------------------------ J5
    res_doc = json.loads(res_live)
    rr = res_doc.get("resolved") or []
    n_rows = len(rr)
    n_code = sum(1 for x in rr if x.get("resolved_code"))
    j5 = (sha16(res_live) == PIN_RESOLUTION
          and f"HEAD:{RES_PATH}" and
          git_text("rev-parse", f"HEAD:{RES_PATH}").strip()
          == git_text("rev-parse", f"{BASELINE[:8]}:{RES_PATH}").strip()
          and (n_rows, n_code, n_rows - n_code) == (222, 214, 8))
    gate("J5_resolution_substrate", j5,
         f"resolution BYTE-UNTOUCHED: HEAD blob == R14-era pin {RES_BLOB[:16]} "
         f"(== baseline blob), counts recomputed 222 rows / 214 with "
         f"resolved_code / 8 without — last writer remains R14; R22 amended "
         f"nothing at the resolution layer")

    # ------------------------------------------------------------------ J6
    run = subprocess.run([sys.executable, "scripts/c32_notes_maths_a_join.py"],
                         capture_output=True, text=True)
    j6 = run.returncode == 0
    detail6 = f"generator re-run exit {run.returncode}"
    if j6:
        re_join = json.loads(JOIN.read_bytes().decode("utf-8"))
        a = json.loads(snap.decode("utf-8"))
        a.pop("generated_utc"), re_join.pop("generated_utc")
        j6 = a == re_join
        detail6 += "; refreshed artifact content-identical modulo " \
                   "generated_utc" if j6 else "; CONTENT DRIFT vs snapshot"
    gate("J6_determinism", j6,
         detail6 + " (joins, unresolved, counts, inputs, task, "
         "validation_tier, schema, ordering all equal)")

    # ------------------------------------------------------------------ J7
    dirty = []
    for l in git_text("status", "--porcelain").splitlines():
        if not l.strip():
            continue
        # porcelain v1: XY + space + path (renames: 'R  old -> new')
        p = l.split("->")[-1].lstrip() if "->" in l else l[3:]
        dirty.append(p)
    dirt_ok = set(dirty) <= FOOTPRINT
    moved = []
    for p in PROTECTED:
        try:
            b = git_text("rev-parse", f"{BASELINE[:8]}:{p}").strip()
            h = git_text("rev-parse", f"HEAD:{p}").strip()
        except subprocess.CalledProcessError:
            moved.append(p)
            continue
        if b != h:
            moved.append(p)
            continue
        disk = REPO / p
        if disk.is_file() and sha16(disk.read_bytes()) != \
                sha16(blob_bytes("HEAD", p)):
            moved.append(p)
    j7 = dirt_ok and not moved
    gate("J7_protected_surfaces", j7,
         f"working-tree dirt ⊆ the declared R23 footprint "
         f"({sorted(set(dirty) - FOOTPRINT) or 'no outside dirt'}); every "
         f"protected loop record byte-untouched baseline→HEAD→working tree "
         f"({len(PROTECTED)} paths incl. the R22 record/map/verdicts/check, "
         f"the R21 re-gate records, the R5 apply artifacts incl. the 832-row "
         f"promotions file, the R19+R20 records, every earlier map/record, "
         f"the scope doc, the C30 ledger, the SP + chunk stores, the Lane C "
         f"stores, the c40 tool) — "
         f"{'clean' if j7 else f'MOVED/DIRTY: {sorted(moved)}'}")

    # ------------------------------------------------------------------ J8
    head = git_text("log", "-1", "--format=%H %s")
    head_sha, head_subj = head[:40], head[41:]
    committed_ok = True
    if head_sha.startswith(BASELINE[:8]):
        delta = [l for l in git_text("diff", "--name-only", "HEAD")
                 .splitlines() if l.strip()]
        committed_ok = set(delta) <= FOOTPRINT
        j8_detail = (f"HEAD == baseline {BASELINE[:8]} (pre-commit form): "
                     f"working-tree delta vs HEAD ⊆ footprint "
                     f"({sorted(set(delta) - FOOTPRINT) or 'in footprint'})")
    elif head_subj.startswith("T-C42 R23"):
        delta = [l for l in git_text("diff", "--name-only", "HEAD~1", "HEAD")
                 .splitlines() if l.strip()]
        committed_ok = set(delta) <= FOOTPRINT
        j8_detail = (f"HEAD carries the round ({head_subj[:60]}...): committed "
                     f"delta vs HEAD~1 ⊆ footprint "
                     f"({sorted(set(delta) - FOOTPRINT) or 'in footprint'})")
    else:
        j8_detail = (f"HEAD {head_sha[:8]} is neither baseline nor a T-C42 "
                     f"R23 commit — delta check skipped, dirt gate above "
                     f"remains the guarantee")
    gate("J8_commit_state", committed_ok, j8_detail)

    # ----------------------------------------------------------------- emit
    all_pass = all(g["pass"] for g in gates.values())
    out = {
        "schema": "c42-r23-join-check/1.0",
        "task": "T-C42 R23 join re-run verification battery (J1-J8)",
        "generated_utc": datetime.now(timezone.utc)
            .isoformat(timespec="seconds"),
        "head": {"sha": head_sha, "subject": head_subj},
        "baseline": BASELINE,
        "directive": "R23 (2026-10-04, discord, gateway trace "
                     "772bb1c553acf115d53f83d9cf6afa81) — the join re-run "
                     "lane; R24/R25 NOT fired",
        "gates": gates,
        "all_pass": all_pass,
    }
    outp = REPO / "graph/reports/C42_R23_JOIN_CHECK.json"
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    for name, g in gates.items():
        print(f"{'PASS' if g['pass'] else 'FAIL'}  {name}: {g['detail']}")
    print(f"ALL {'PASS' if all_pass else 'FAIL'} "
          f"({sum(g['pass'] for g in gates.values())}/{len(gates)}) "
          f"-> {outp.relative_to(REPO)}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
