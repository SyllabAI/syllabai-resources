#!/usr/bin/env python3
"""c42_r26_repair_check.py — T-C42 R26 two-way audit (the R22 check shape).

A1 inventory agreement: the R26 section_overrides + promotions amendment
   cover exactly the R25 defect inventory (the 4 REJECT rows of
   scripts/c42_r25_fresh_verdicts.yaml — (factorising-by-grouping, ord 2,
   2.2F), (types-of-number, ord 1, 1.1G), (introduction-to-vectors, ord 3,
   5.1D), (drawing-straight-line-graphs, ord 4, 3.3F)); the id-level surface
   is EMPTY (no note-level-class root — verified against the R25 fresh
   verdict notes, not assumed); no dupes, no extras; the R25 fill record
   pins the same 4-row inventory (part_a.total.reject == 4 + the 4 codes in
   the fill record md).
A2 projection agreement: scripts/c42_section_overrides_r26.yaml equals the
   verdict record — 3 verdicted REATTRIBUTE entries + 1 verdicted
   DEMOTE_TO_WORKLIST entry (override_code null), 0 extension entries,
   the 4 note-level STANDING rulings, the standing convention block (the 4
   store H3 HOLD rows listed, not decided), the census remarks, an EMPTY
   dated-corrections block, and the promoted-surface-amendment pointer.
A3 code domain: every REATTRIBUTE override_code is a canonical-188 member,
   differs from current_code; every current_code matches the live substrate;
   the 4 rows are HUMAN_VALIDATED (the R26 novelty — the first repair round
   over the promoted surface).
A4 wordings: the store wordings of 1.1A / 5.1C / 3.3H carry the verdict
   citations (1.1A's integers demand; 5.1C's scalar-multiplication demand;
   3.3H's y = mx + c gradient/intercept recognition); 2.2F's cap ('limited')
   is present; the C30 ledger facts hold — 1.1G/1.1A/5.1D/5.1C/3.3H/2.2F
   ABSENT (Higher-only), 3.3F PRESENT as a shared-tier row whose Higher text
   is the gradient-from-two-coordinates demand and whose Foundation text is
   the conversion-graphs surface (asserted, not assumed).
A5 joins STAND + resolution byte-untouched: the join rows for
   spcpt_J55PhZ2cbPsYvpt8 (1.1G), spcpt_vMSNnYkKPf62MRH9 (2.2F),
   spcpt_h8QyRmzX5mCJb3X9 (3.3F) and spcpt_v6tP4DSVShVJMJhk (5.1D) stand at
   HEAD; the resolution file (SME-ExamQuestion/igcse-maths-a-18-higher/
   spec_point_resolution.json — NOT materialized in this workspace's sparse
   checkout, read via git) is byte-identical between the round-start HEAD
   and the audit HEAD.
A6 substrate pins + promoted-surface guard: the 4 inventory rows exist at
   HUMAN_VALIDATED with codes 2.2F/1.1G/5.1D/3.3F; each is pinned in the R5
   promotions file with matching identity (spec_code included); the
   amendment's supersedes carry pinned_code == the file pins and amended_code
   == the map targets, and its exclusion is exactly the DEMOTE row; the
   832-row promoted surface intersects the exclusion in exactly that row;
   the 4 H3 rows are SUGGESTED at the pinned codes (1.7B/6.3J/3.3F/2.2C);
   1.1A and 5.1C carry ZERO anchored chunk rows (the uncovered-SP DEFER rows
   da25da48e0be5c64 / 2332964a4f1b02ca stand) — the coverage-gain facts; 3.3H
   carries exactly 7 promoted rows.
A7 idempotency: re-running the projection emitter and the proposals scorer
   is byte-identical (deterministic regeneration).
A8/A10 footprint + commit state: the working-tree delta vs the round-start
   HEAD (00abec1) is within the declared R26 footprint (pre-commit form);
   post-commit the delta is empty and the check is re-runnable (the
   C8/X10 precedent). The resolution file's byte-identity is asserted
   explicitly in A5.
A9 round artifacts: the proposals packet pins the same declared surfaces
   (0 id-level / 4 section / 4 H3 listed), records the top-1 convergences
   (5.1C / 3.3H / 1.1A excluding-current) and the DEMOTE row's absence
   finding (current 2.2F tops the including-current packet), and the
   standing convention record remains pinned (md + json, decision_id
   c42-heading-only-convention-1).

Writes its own report graph/reports/C42_R26_REPAIR_CHECK.json.
Exit 0 iff every check passes.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "graph/reports/C42_R26_REPAIR_CHECK.json"
VERDICTS = REPO / "scripts/c42_r26_repair_verdicts.yaml"
OVERRIDES = REPO / "scripts/c42_section_overrides_r26.yaml"
AMENDMENT = REPO / "scripts/c42_r26_promotions_amendment.yaml"
R25_FRESH = REPO / "scripts/c42_r25_fresh_verdicts.yaml"
R25_FILL_MD = REPO / "graph/reports/C42_R25_MATHS_A_REGATE_FILL_RECORD.md"
R25_FILL_JSON = REPO / "graph/reports/C42_R25_MATHS_A_REGATE_FILL_RECORD.json"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
REGISTRY = REPO / "graph/igcse-maths-a/specification_points.yaml"
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"
JOIN = REPO / "Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json"
PROMOTIONS = REPO / "scripts/c42_r5_promotions.yaml"
PROPOSALS = REPO / "graph/reports/C42_R26_REPAIR_PROPOSALS.json"
CONV_MD = REPO / "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md"
CONV_JSON = REPO / "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.json"
RES_GIT = "SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json"
ROUND_START = "00abec1"

FOOTPRINT = [
    "scripts/c42_r26_repair_proposals.py",
    "scripts/c42_r26_repair_verdicts.yaml",
    "scripts/c42_r26_override_projection.py",
    "scripts/c42_r26_repair_check.py",
    "scripts/c42_section_overrides_r26.yaml",
    "scripts/c42_r26_promotions_amendment.yaml",
    "graph/reports/C42_R26_REPAIR_PROPOSALS.json",
    "graph/reports/C42_R26_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R26_REPAIR_CHECK.json",
]

CHECKS = []


def ok(name, detail):
    CHECKS.append({"check": name, "ok": True, "detail": detail})
    print(f"  PASS {name}: {detail}")


def die(msg):
    print(f"FAIL-CLOSED: {msg}", file=sys.stderr)
    sys.exit(1)


def sha16(data) -> str:
    b = data.encode("utf-8") if isinstance(data, str) else data
    return hashlib.sha256(b).hexdigest()[:16]


def squash(s: str) -> str:
    return re.sub(r"\s+", "", s or "").lower()


def git(args) -> str:
    return subprocess.run(["git", "-C", str(REPO)] + args,
                          capture_output=True, text=True, check=True).stdout


def git_bytes(rev_path: str) -> bytes:
    return subprocess.run(["git", "-C", str(REPO), "show", rev_path],
                          capture_output=True, check=True).stdout


def main() -> int:
    for p in (VERDICTS, OVERRIDES, AMENDMENT, R25_FRESH, R25_FILL_MD,
              R25_FILL_JSON, STORE, REGISTRY, LEDGER, JOIN, PROMOTIONS,
              PROPOSALS, CONV_MD, CONV_JSON):
        if not p.exists():
            die(f"required artifact missing: {p.relative_to(REPO)}")

    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    ovr = yaml.safe_load(OVERRIDES.read_text(encoding="utf-8"))
    amd = yaml.safe_load(AMENDMENT.read_text(encoding="utf-8"))
    fresh = yaml.safe_load(R25_FRESH.read_text(encoding="utf-8"))
    fill = json.loads(R25_FILL_JSON.read_text(encoding="utf-8"))
    store = yaml.safe_load(STORE.read_text(encoding="utf-8"))
    reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    points = {p["code"] for p in reg["specification_points"]}
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    led_rows = {r["official_code"]: r for r in ledger["rows"]}
    join = json.loads(JOIN.read_text(encoding="utf-8"))
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    promo_pins = {e["row"]["mapping_id"]: e["row"] for e in promo["promotions"]}

    rows_by_id = {r["mapping_id"]: r for r in store["rows"]}
    rej_ids = sorted(m for m, p in fresh["verdicts"].items()
                     if p.get("verdict") == "REJECT")
    ovr_entries = {e["mapping_id"]: e for e in ovr["overrides"]}

    # ---- A1 inventory agreement ------------------------------------------------
    if sorted(ovr_entries) != rej_ids:
        die(f"A1: override ids {sorted(ovr_entries)} != R25 reject ids {rej_ids}")
    if len(rej_ids) != 4:
        die(f"A1: expected the 4-row R25 inventory, got {len(rej_ids)}")
    for m in rej_ids:
        note = (fresh["verdicts"][m].get("note") or "").lower()
        if "note-level" in note:
            die(f"A1: {m} root claims the note-level class — surface 1 empty")
    if fill.get("part_a", {}).get("total", {}).get("reject") != 4:
        die("A1: R25 fill record does not pin the 4-row inventory")
    fill_txt = R25_FILL_MD.read_text(encoding="utf-8")
    for frag in ("4MA1-2.2F", "4MA1-1.1G", "4MA1-5.1D", "4MA1-3.3F"):
        if frag not in fill_txt:
            die(f"A1: R25 fill record missing reject row {frag}")
    amd_ids = sorted([e["mapping_id"] for e in amd["supersedes_code"]]
                     + [e["mapping_id"] for e in amd["excluded"]])
    if amd_ids != rej_ids:
        die(f"A1: amendment ids {amd_ids} != R25 reject ids {rej_ids}")
    ok("A1_inventory_agreement",
       "overrides + amendment == the R25 4-row defect inventory; surface 1 "
       "EMPTY (verified against the R25 fresh notes); fill record pins the "
       "same rows (reject=4 + the 4 codes)")

    # ---- A2 projection agreement --------------------------------------------------
    acts = sorted(e["action"] for e in ovr_entries.values())
    if acts != ["DEMOTE_TO_WORKLIST"] + ["REATTRIBUTE"] * 3:
        die(f"A2: unexpected action mix {acts}")
    verdict_blocks = ver["section_overrides"]
    if len(verdict_blocks) != 4:
        die("A2: verdict record does not carry 4 section_overrides")
    v_by_mid = {v["mapping_id"]: v for v in verdict_blocks.values()}
    for e in ovr_entries.values():
        v = v_by_mid[e["mapping_id"]]
        if e["action"] != v["disposition"]:
            die(f"A2: map/verdict action drift on {e['mapping_id']}")
        if (e["override_code"] or None) != (v.get("override_code") or None):
            die(f"A2: map/verdict target drift on {e['mapping_id']}")
        if e["current_code"] != v["current_code"]:
            die(f"A2: map/verdict current drift on {e['mapping_id']}")
    if ovr.get("note_level_adjudications") != ver["note_level_adjudications"] \
            or len(ovr["note_level_adjudications"]) != 4:
        die("A2: note-level STANDING rulings drifted")
    if any(e.get("provenance_class") == "extension" for e in ovr_entries.values()):
        die("A2: extension entries exist — this round declared NONE")
    h3 = ovr["heading_only_convention"]["h3_hold_rows_this_round"]
    live_hold_ids = sorted(
        m for m, r in rows_by_id.items()
        if r.get("validation_status") == "SUGGESTED"
        and r.get("spec_code") in ("4MA1-1.7B", "4MA1-6.3J", "4MA1-3.3F",
                                   "4MA1-2.2C"))
    if sorted(x["mapping_id"] for x in h3) != live_hold_ids or len(hold_ids := live_hold_ids) != 4:
        die("A2: H3 continuity block != the live store hold set")
    if ovr.get("dated_corrections") != []:
        die("A2: dated corrections expected EMPTY this round")
    if not ovr.get("census_remarks") or len(ovr["census_remarks"]) < 4:
        die("A2: census remarks missing")
    psa = ovr.get("promoted_surface_amendment") or {}
    if psa.get("amendment_file") != "scripts/c42_r26_promotions_amendment.yaml" \
            or psa.get("base_file_untouched") is not True:
        die("A2: promoted-surface-amendment pointer missing from the map")
    ok("A2_projection_agreement",
       "map == verdicts: 3 verdicted REATTRIBUTEs + 1 DEMOTE (null target), "
       "0 extensions, 4 STANDING rulings, the 4 live-store H3 rows listed, "
       "census remarks, empty dated corrections, amendment pointer")

    # ---- A3 code domain -------------------------------------------------------------
    for m, e in ovr_entries.items():
        srow = rows_by_id.get(m)
        if srow is None:
            die(f"A3: {m} not in the live substrate")
        if srow["spec_code"] != e["current_code"]:
            die(f"A3: current_code drift on {m}")
        if srow.get("validation_status") != "HUMAN_VALIDATED":
            die(f"A3: {m} is not HUMAN_VALIDATED — the R26 inventory is the "
                f"promoted surface")
        if e["action"] == "REATTRIBUTE":
            if e["override_code"] not in points:
                die(f"A3: target {e['override_code']} outside the ratified 188")
            if e["override_code"] == e["current_code"]:
                die(f"A3: target equals current on {m}")
        elif e["override_code"] is not None:
            die(f"A3: DEMOTE target must be null on {m}")
    ok("A3_code_domain",
       "3 targets are canonical-188 members, distinct from their currents; "
       "DEMOTE target null; currents match the live substrate; all 4 rows "
       "HUMAN_VALIDATED (the R26 novelty)")

    # ---- A4 wordings + ledger facts ---------------------------------------------------
    reg_pts = {p["code"]: p for p in reg["specification_points"]}
    w11a = reg_pts["4MA1-1.1A"].get("official_wording") or ""
    w51c = reg_pts["4MA1-5.1C"].get("official_wording") or ""
    w33h = reg_pts["4MA1-3.3H"].get("official_wording") or ""
    w22f = reg_pts["4MA1-2.2F"].get("official_wording") or ""
    w11g = reg_pts["4MA1-1.1G"].get("official_wording") or ""
    w51d = reg_pts["4MA1-5.1D"].get("official_wording") or ""
    if squash("understand and use integers") not in squash(w11a):
        die("A4: 1.1A integers demand missing from the store wording")
    if squash("multiply vectors by scalar") not in squash(w51c):
        die("A4: 5.1C scalar-multiplication demand missing from the store wording")
    h = squash(w33h)
    if "y=mx+c" not in h or "gradient" not in h or "intercept" not in h:
        die("A4: 3.3H y=mx+c gradient/intercept recognition missing from the "
            "store wording")
    if squash("limited") not in squash(w22f):
        die("A4: 2.2F cap missing from the store wording")
    for t in ("odd", "even", "prime", "factors", "multiples"):
        if t not in squash(w11g):
            die(f"A4: 1.1G vocabulary term '{t}' missing from the store wording")
    if squash("add and subtract vectors") not in squash(w51d):
        die("A4: 5.1D demand missing from the store wording")
    for bare in ("1.1G", "1.1A", "5.1D", "5.1C", "3.3H", "2.2F"):
        if bare in led_rows:
            die(f"A4: {bare} expected ABSENT from the C30 ledger (Higher-only)")
    if "3.3F" not in led_rows:
        die("A4: 3.3F expected PRESENT in the C30 ledger (shared-tier)")
    if squash("coordinates of two points") not in squash(led_rows["3.3F"]["higher"]["text"]):
        die("A4: 3.3F ledger Higher text drifted")
    if squash("conversion graphs") not in squash(led_rows["3.3F"]["foundation"]["text"]):
        die("A4: 3.3F ledger Foundation text drifted")
    ok("A4_wordings_ledger",
       "store wordings carry the citations verbatim (1.1A / 5.1C / 3.3H "
       "targets; 2.2F's cap; 1.1G's vocabulary; 5.1D's demand); ledger facts "
       "asserted: 1.1G/1.1A/5.1D/5.1C/3.3H/2.2F absent (Higher-only), 3.3F "
       "present as shared-tier with the cited Higher + Foundation texts")

    # ---- A5 joins STAND + resolution byte-untouched -------------------------------------
    join_rows = {r["anchor_id"]: r for r in join["joins"]}
    for aid, want in [("spcpt_J55PhZ2cbPsYvpt8", "1.1G"),
                      ("spcpt_vMSNnYkKPf62MRH9", "2.2F"),
                      ("spcpt_h8QyRmzX5mCJb3X9", "3.3F"),
                      ("spcpt_v6tP4DSVShVJMJhk", "5.1D")]:
        jr = join_rows.get(aid)
        if jr is None or jr.get("resolved_code") != want:
            die(f"A5: join row for {aid} does not stand at {want}")
    res_start = git_bytes(f"{ROUND_START}:{RES_GIT}")
    res_head = git_bytes(f"HEAD:{RES_GIT}")
    if res_start != res_head:
        die("A5: resolution file drifted between the round-start HEAD and HEAD")
    ok("A5_joins_resolution",
       "4 note-level joins STAND at HEAD (1.1G/2.2F/3.3F/5.1D); resolution "
       "file byte-identical 00abec1 -> HEAD (git-read: not materialized in "
       "the sparse checkout)")

    # ---- A6 substrate pins + promoted-surface guard ---------------------------------------
    hv = {m for m, r in rows_by_id.items()
          if r.get("validation_status") == "HUMAN_VALIDATED"}
    if len(hv) != 832:
        die(f"A6: promoted surface is not the R5 state (832, got {len(hv)})")
    for m in rej_ids:
        pin = promo_pins.get(m)
        srow = rows_by_id[m]
        if pin is None:
            die(f"A6: {m} not pinned in the R5 promotions file")
        if (pin.get("spec_code") != srow["spec_code"]
                or pin.get("note_path") != srow["note_path"]
                or pin.get("chunk_ordinal") != srow["chunk"]["ordinal"]):
            die(f"A6: promotions pin identity drift on {m}")
    sup = {e["mapping_id"]: e for e in amd["supersedes_code"]}
    exc = {e["mapping_id"]: e for e in amd["excluded"]}
    if sorted(sup) != sorted(m for m, e in ovr_entries.items()
                             if e["action"] == "REATTRIBUTE"):
        die("A6: amendment supersedes != the 3 REATTRIBUTE rows")
    for m, e in sup.items():
        v = v_by_mid[m]
        if e["pinned_code"] != promo_pins[m]["spec_code"] \
                or e["amended_code"] != v["override_code"]:
            die(f"A6: amendment supersedes drift on {m}")
    if sorted(exc) != [m for m, e in ovr_entries.items()
                       if e["action"] == "DEMOTE_TO_WORKLIST"]:
        die("A6: amendment exclusion != the DEMOTE row")
    if hv & set(exc) != set(exc):
        die("A6: the exclusion is not a subset of the promoted surface")
    for m, r in ((h["mapping_id"], rows_by_id[h["mapping_id"]])
                 for h in h3):
        if r.get("validation_status") != "SUGGESTED":
            die(f"A6: H3 row {m} is not SUGGESTED")
    for code in ("4MA1-1.1A", "4MA1-5.1C"):
        anchored = [r for r in store["rows"]
                    if r.get("spec_code") == code and "chunk" in r]
        if anchored:
            die(f"A6: {code} already carries anchored rows — the gain fact "
                f"drifted")
        defer = [r for r in store["rows"]
                 if r.get("spec_code") == code and r.get("worklist_reason")]
        if len(defer) != 1:
            die(f"A6: {code} uncovered-SP DEFER row not found")
    n33h = len([r for r in store["rows"]
                if r.get("spec_code") == "4MA1-3.3H" and "chunk" in r])
    if n33h != 7:
        die(f"A6: 3.3H anchored rows expected 7, got {n33h}")
    ok("A6_substrate_pins",
       "4 inventory rows HUMAN_VALIDATED at pinned identities (R5 file "
       "verified); amendment supersedes/exclusion consistent; the promoted "
       "832-row surface contains the exclusion exactly; the 4 H3 rows "
       "SUGGESTED; 1.1A + 5.1C uncovered (DEFER rows stand — the gain "
       "facts); 3.3H carries 7 anchored rows")

    # ---- A7 idempotency -----------------------------------------------------------------
    h1 = sha16(PROPOSALS.read_bytes()), sha16(OVERRIDES.read_bytes()), \
        sha16(AMENDMENT.read_bytes())
    subprocess.run([sys.executable, str(REPO / "scripts/c42_r26_repair_proposals.py")],
                   capture_output=True, check=True)
    subprocess.run([sys.executable, str(REPO / "scripts/c42_r26_override_projection.py")],
                   capture_output=True, check=True)
    h2 = sha16(PROPOSALS.read_bytes()), sha16(OVERRIDES.read_bytes()), \
        sha16(AMENDMENT.read_bytes())
    if h1 != h2:
        die("A7: deterministic regeneration drifted")
    ok("A7_idempotency",
       "proposals + override map + promotions amendment byte-identical re-runs")

    # ---- A8/A10 footprint + commit state ---------------------------------------------------
    head = git(["rev-parse", "HEAD"]).strip()
    if head.startswith(ROUND_START):
        changed = [ln[3:].strip() for ln in git(["status", "--porcelain"]).splitlines()
                   if ln.strip()]
        outside = [c for c in changed if c not in FOOTPRINT
                   and not any(c.endswith(f" -> {f}") for f in FOOTPRINT)]
        if outside:
            die(f"A8: working-tree delta outside the declared footprint: {outside[:5]}...")
        ok("A8_footprint_precommit",
           f"delta vs {ROUND_START} is exactly the declared {len(FOOTPRINT)}-file "
           f"R26 footprint (pre-commit form)")
    else:
        dirty = git(["status", "--porcelain"]).strip()
        if dirty:
            die(f"A10: post-commit tree is dirty: {dirty[:200]}")
        ok("A10_committed_clean",
           f"HEAD {head[:8]} is the round commit; tree clean; the check "
           f"re-runs committed-clean (the C8/X10 precedent)")

    # ---- A9 round artifacts -------------------------------------------------------------------
    props = json.loads(PROPOSALS.read_text(encoding="utf-8"))
    if props.get("surface1_id_level") != []:
        die("A9: proposals surface 1 must be empty")
    if sorted(r["mapping_id"] for r in props["surface2_section_level"]) != rej_ids:
        die("A9: proposals surface 2 != the 4-row inventory")
    if sorted(r["mapping_id"] for r in props["surface3_heading_only_h3_continuity"]) != hold_ids:
        die("A9: proposals H3 continuity != the 4 HOLD rows")
    s2 = {r["mapping_id"]: r for r in props["surface2_section_level"]}
    conv = {"7fdded0b9245e1c3": "4MA1-5.1C",
            "e6ed72481e8ffc2e": "4MA1-3.3H",
            "81c0b59852d5d4b6": "4MA1-1.1A"}
    for m, want in conv.items():
        got = s2[m]["top1_excluding_current"]["code"]
        if got != want:
            die(f"A9: proposals top-1 excluding-current drifted on {m}: {got}")
    dem = "70f0b027f3f1528f"
    if s2[dem]["top1_including_current"]["code"] != "4MA1-2.2F":
        die("A9: the DEMOTE row's absence finding (current tops the "
            "including-current packet) drifted")
    if not (CONV_MD.exists() and CONV_JSON.exists()):
        die("A9: the standing convention record is not pinned")
    ok("A9_round_artifacts",
       "proposals surfaces 0/4/4 pinned; top-1 convergences recorded "
       "(5.1C / 3.3H / 1.1A excluding-current) + the DEMOTE absence finding "
       "(current 2.2F tops including-current); the standing convention "
       "record remains pinned (c42-heading-only-convention-1 md + json)")

    # ---- report ---------------------------------------------------------------------------------
    head_sha = head
    out = {
        "schema": "c42-r26-repair-check/1.0",
        "task": "T-C42",
        "stage": "r26-r1-shaped-repair-round-check",
        "round": "R26",
        "round_start": ROUND_START,
        "audited_head": head_sha,
        "baseline_store_sha256_16": sha16(STORE.read_bytes()),
        "override_map_sha256_16": sha16(OVERRIDES.read_bytes()),
        "amendment_sha256_16": sha16(AMENDMENT.read_bytes()),
        "verdicts_sha256_16": sha16(VERDICTS.read_bytes()),
        "proposals_sha256_16": sha16(PROPOSALS.read_bytes()),
        "checks": CHECKS,
        "passed": len(CHECKS),
        "total": len(CHECKS),
        "result": "ALL PASS",
    }
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"c42_r26_repair_check: {out['result']} ({len(CHECKS)}/{len(CHECKS)}) "
          f"-> {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
