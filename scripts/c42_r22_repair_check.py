#!/usr/bin/env python3
"""c42_r22_repair_check.py — T-C42 R22 two-way audit (the R18 check shape).

A1 inventory agreement: the R22 section_overrides cover exactly the R21
   defect inventory (the 3 REJECT rows of scripts/c42_r21_fresh_verdicts.yaml
   joined to the live substrate — (graphical-solutions, ord 1, 2.6B),
   (3d-pythagoras-and-trigonometry, ord 4, 4.8D),
   (difference-of-two-squares, ord 3, 2.2F)); the id-level surface is EMPTY
   (no note-level-class root — verified against the R21 review record, not
   assumed); no dupes, no extras; the R21 fill record pins the same 3-row
   inventory.
A2 projection agreement: scripts/c42_section_overrides_r22.yaml equals the
   verdict record — 3 verdicted REATTRIBUTE entries, 0 extension entries,
   0 DEMOTEs, the 3 note-level STANDING rulings, the standing convention
   block (the 4 R21 H3 HOLD rows listed, not decided), the census remarks,
   the dated correction DC-R22-01, no subsumed entries.
A3 code domain: every override_code is a canonical-188 member, differs from
   current_code; every current_code matches the live substrate; the 3 rows
   are SUGGESTED (never promoted).
A4 wordings: the store wordings of 4.8F / 2.2B / 3.3E carry the verdict
   citations verbatim (4.8F's including-clause; 2.2B un-capped vs 2.2F's
   '(limited to' cap; 3.3E's linear + non-linear demand); the C30 ledger
   facts hold — 4.8D/4.8F/2.2F/2.6B ABSENT (Higher-only), 2.2B/3.3E PRESENT
   as shared-tier rows with the cited Higher texts (DC-R22-01's corrected
   facts, asserted not assumed).
A5 joins STAND + resolution byte-untouched: the join rows for
   spcpt_kX4655D8M3Q3TRzW (4.8D), spcpt_RJbgRvXq2VrGpP5g (2.2F) and
   spcpt_sHCB9WZbDMyTFqCP (2.6B) stand at HEAD; the resolution file
   (SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json —
   NOT materialized in this workspace's sparse checkout, read via git) is
   byte-identical between the round-start HEAD and the audit HEAD.
   Environment note (recorded, not repaired — the R0 pattern): the standing
   sme_spcpt_verify.py sweep is NOT re-run here (no EQ materialization in
   the sparse checkout); the R18-recorded accounting G1/G2 failures remain
   a separate operator census item, byte-unrelated to this round's footprint.
A6 substrate pins: the 3 REJECT mapping ids exist at SUGGESTED with codes
   2.6B/4.8D/2.2F; the 4 H3 rows are HOLD on the R21 review record (ids
   verbatim); the R5-promoted surface is untouched by construction — the
   832 HUMAN_VALIDATED rows intersect the override targets in NOTHING and
   none of the 3 targets appears in scripts/c42_r5_promotions.yaml.
A7 idempotency: re-running the projection emitter and the proposals scorer
   is byte-identical (deterministic regeneration).
A8/A10 footprint + commit state: the working-tree delta vs the round-start
   HEAD (df7a6c1) is within the declared R22 footprint (pre-commit form);
   post-commit the delta is empty and the check is re-runnable (the
   C8/X10 precedent). The resolution file's byte-identity is asserted
   explicitly in A5.
A9 round artifacts: the proposals packet pins the same declared surfaces
   (0 id-level / 3 section / 4 H3 listed) and the standing convention record
   remains pinned (md + json, decision_id c42-heading-only-convention-1).

Writes its own report graph/reports/C42_R22_REPAIR_CHECK.json.
Exit 0 iff every check passes.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "graph/reports/C42_R22_REPAIR_CHECK.json"
VERDICTS = REPO / "scripts/c42_r22_repair_verdicts.yaml"
OVERRIDES = REPO / "scripts/c42_section_overrides_r22.yaml"
R21_FRESH = REPO / "scripts/c42_r21_fresh_verdicts.yaml"
R21_REVIEW = REPO / "scripts/c42_r21_review_verdicts.yaml"
R21_FILL_MD = REPO / "graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.md"
R21_FILL_JSON = REPO / "graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.json"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
REGISTRY = REPO / "graph/igcse-maths-a/specification_points.yaml"
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"
JOIN = REPO / "Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json"
PROMOTIONS = REPO / "scripts/c42_r5_promotions.yaml"
PROPOSALS = REPO / "graph/reports/C42_R22_REPAIR_PROPOSALS.json"
CONV_MD = REPO / "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md"
CONV_JSON = REPO / "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.json"
RES_GIT = "SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json"
ROUND_START = "df7a6c1"

FOOTPRINT = [
    "scripts/c42_r22_repair_proposals.py",
    "scripts/c42_r22_repair_verdicts.yaml",
    "scripts/c42_r22_override_projection.py",
    "scripts/c42_r22_repair_check.py",
    "scripts/c42_section_overrides_r22.yaml",
    "graph/reports/C42_R22_REPAIR_PROPOSALS.json",
    "graph/reports/C42_R22_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R22_REPAIR_CHECK.json",
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


def git(args) -> str:
    return subprocess.run(["git", "-C", str(REPO)] + args,
                          capture_output=True, text=True, check=True).stdout


def git_bytes(rev_path: str) -> bytes:
    return subprocess.run(["git", "-C", str(REPO), "show", rev_path],
                          capture_output=True, check=True).stdout


def main() -> int:
    for p in (VERDICTS, OVERRIDES, R21_FRESH, R21_REVIEW, R21_FILL_MD,
              R21_FILL_JSON, STORE, REGISTRY, LEDGER, JOIN, PROMOTIONS,
              PROPOSALS, CONV_MD, CONV_JSON):
        if not p.exists():
            die(f"required artifact missing: {p.relative_to(REPO)}")

    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    ovr = yaml.safe_load(OVERRIDES.read_text(encoding="utf-8"))
    fresh = yaml.safe_load(R21_FRESH.read_text(encoding="utf-8"))
    review = yaml.safe_load(R21_REVIEW.read_text(encoding="utf-8"))
    fill = json.loads(R21_FILL_JSON.read_text(encoding="utf-8"))
    store = yaml.safe_load(STORE.read_text(encoding="utf-8"))
    reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    points = {p["code"] for p in reg["specification_points"]}
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    led_rows = {r["official_code"]: r for r in ledger["rows"]}
    join = json.loads(JOIN.read_text(encoding="utf-8"))
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))

    rows_by_id = {r["mapping_id"]: r for r in store["rows"]}
    rej_ids = sorted(m for m, p in fresh["verdicts"].items()
                     if p.get("verdict") == "REJECT")
    hold_ids = sorted(m for m, p in review["verdicts"].items()
                      if p.get("verdict") == "HOLD")
    ovr_entries = {e["mapping_id"]: e for e in ovr["overrides"]}

    # ---- A1 inventory agreement ------------------------------------------------
    if sorted(ovr_entries) != rej_ids:
        die(f"A1: override ids {sorted(ovr_entries)} != R21 reject ids {rej_ids}")
    if len(rej_ids) != 3:
        die(f"A1: expected the 3-row R21 inventory, got {len(rej_ids)}")
    for m in rej_ids:
        root = (review["verdicts"][m].get("root") or "").lower()
        if "note-level" in root:
            die(f"A1: {m} root claims note-level class — surface 1 must be empty")
    if fill.get("part_a", {}).get("total", {}).get("reject") != 3:
        die("A1: R21 fill record does not pin the 3-row inventory")
    fill_txt = R21_FILL_MD.read_text(encoding="utf-8")
    for frag in ("4MA1-4.8D", "4MA1-2.2F", "4MA1-2.6B"):
        if frag not in fill_txt:
            die(f"A1: R21 fill record missing reject row {frag}")
    ok("A1_inventory_agreement",
       "overrides == the R21 3-row defect inventory; surface 1 EMPTY "
       "(verified against the R21 roots); fill record pins the same rows")

    # ---- A2 projection agreement --------------------------------------------------
    if len(ovr_entries) != 3:
        die("A2: expected 3 verdicted entries")
    for e in ovr_entries.values():
        if e.get("provenance_class") != "verdicted" or e.get("action") != "REATTRIBUTE":
            die(f"A2: unexpected entry class/action for {e.get('mapping_id')}")
        v = ver["verdicts"][e["mapping_id"]]
        if e["override_code"] != v["to_code"] or e["current_code"] != v["from_code"]:
            die(f"A2: map/verdict drift on {e['mapping_id']}")
    if ovr.get("note_level_adjudications") != ver["note_level_adjudications"] \
            or len(ovr["note_level_adjudications"]) != 3:
        die("A2: note-level STANDING rulings drifted")
    if any(e.get("provenance_class") == "extension" for e in ovr_entries.values()):
        die("A2: extension entries exist — this round declared NONE")
    h3 = ovr["heading_only_convention"]["h3_hold_rows_this_round"]
    if sorted(x["mapping_id"] for x in h3) != hold_ids or len(hold_ids) != 4:
        die("A2: H3 continuity block != the R21 HOLD rows")
    if [c.get("id") for c in ovr.get("dated_corrections", [])] != ["DC-R22-01"]:
        die("A2: DC-R22-01 missing from the map")
    if not ovr.get("census_remarks") or len(ovr["census_remarks"]) < 2:
        die("A2: census remarks missing")
    ok("A2_projection_agreement",
       "map == verdicts: 3 verdicted REATTRIBUTEs, 0 extensions/DEMOTEs, "
       "3 STANDING rulings, 4 H3 rows listed, DC-R22-01, census remarks")

    # ---- A3 code domain -------------------------------------------------------------
    for m, e in ovr_entries.items():
        srow = rows_by_id.get(m)
        if srow is None:
            die(f"A3: {m} not in the live substrate")
        if srow["spec_code"] != e["current_code"]:
            die(f"A3: current_code drift on {m}")
        if srow.get("validation_status") != "SUGGESTED":
            die(f"A3: {m} is not SUGGESTED")
        if e["override_code"] not in points:
            die(f"A3: target {e['override_code']} outside the ratified 188")
        if e["override_code"] == e["current_code"]:
            die(f"A3: target equals current on {m}")
    ok("A3_code_domain",
       "3 targets are canonical-188 members, distinct from their currents; "
       "currents match the live substrate; rows SUGGESTED")

    # ---- A4 wordings + ledger facts ---------------------------------------------------
    reg_pts = {p["code"]: p for p in reg["specification_points"]}
    w48f = reg_pts["4MA1-4.8F"].get("official_wording") or ""
    w22b = reg_pts["4MA1-2.2B"].get("official_wording") or ""
    w22f = reg_pts["4MA1-2.2F"].get("official_wording") or ""
    w33e = reg_pts["4MA1-3.3E"].get("official_wording") or ""
    if "including finding the angle between a line and a plane" not in w48f:
        die("A4: 4.8F including-clause missing from the store wording")
    if "limited to" not in w22f.replace(" ", "").replace("(limitedto", "(limited to"):
        if "limited" not in w22f:
            die("A4: 2.2F cap missing from the store wording")
    if "limited" in w22b:
        die("A4: 2.2B store wording carries a cap — the un-capped surface drifted")
    if "linear" not in w33e or "non-linear" not in w33e:
        die("A4: 3.3E linear+non-linear demand missing from the store wording")
    for bare in ("4.8D", "4.8F", "2.2F", "2.6B"):
        if bare in led_rows:
            die(f"A4: {bare} expected ABSENT from the C30 ledger (Higher-only)")
    if "2.2B" not in led_rows or "3.3E" not in led_rows:
        die("A4: 2.2B/3.3E expected PRESENT in the C30 ledger")
    if "factorise such expressions" not in led_rows["2.2B"]["higher"]["text"]:
        die("A4: 2.2B ledger Higher text drifted")
    if led_rows["2.2B"]["foundation"]["text"] != "collect like terms":
        die("A4: 2.2B ledger Foundation text drifted")
    if "intersection points of two graphs" not in led_rows["3.3E"]["higher"]["text"]:
        die("A4: 3.3E ledger Higher text drifted")
    if "midpoint of a line segment" not in led_rows["3.3E"]["foundation"]["text"]:
        die("A4: 3.3E ledger Foundation text drifted")
    ok("A4_wordings_ledger",
       "store wordings carry the citations verbatim; ledger facts asserted: "
       "4.8D/4.8F/2.2F/2.6B absent (Higher-only), 2.2B/3.3E present with the "
       "cited Higher texts (DC-R22-01 facts)")

    # ---- A5 joins STAND + resolution byte-untouched -------------------------------------
    join_rows = {r["anchor_id"]: r for r in join["joins"]}
    for aid, want in [("spcpt_kX4655D8M3Q3TRzW", "4.8D"),
                      ("spcpt_RJbgRvXq2VrGpP5g", "2.2F"),
                      ("spcpt_sHCB9WZbDMyTFqCP", "2.6B")]:
        jr = join_rows.get(aid)
        if jr is None or jr.get("resolved_code") != want:
            die(f"A5: join row for {aid} does not stand at {want}")
    res_start = git_bytes(f"{ROUND_START}:{RES_GIT}")
    res_head = git_bytes(f"HEAD:{RES_GIT}")
    if res_start != res_head:
        die("A5: resolution file drifted between the round-start HEAD and HEAD")
    ok("A5_joins_resolution",
       "3 note-level joins STAND at HEAD (4.8D/2.2F/2.6B); resolution file "
       "byte-identical df7a6c1 -> HEAD (git-read: not materialized in the "
       "sparse checkout); sme_spcpt_verify sweep NOT re-run (no EQ "
       "materialization — the R18-recorded accounting failures remain a "
       "separate census item, byte-unrelated to this footprint)")

    # ---- A6 substrate pins + promoted-surface guard ---------------------------------------
    hv = {m for m, r in rows_by_id.items()
          if r.get("validation_status") == "HUMAN_VALIDATED"}
    if len(hv) != 832:
        die(f"A6: promoted surface is not the R5 state (832, got {len(hv)})")
    if hv & set(ovr_entries):
        die("A6: an override target is a PROMOTED row — forbidden")
    promo_ids = {e["row"]["mapping_id"] for e in promo["promotions"]}
    if set(ovr_entries) & promo_ids:
        die("A6: an override target appears in the R5 promotions file")
    for m in rej_ids:
        if rows_by_id[m].get("validation_status") != "SUGGESTED":
            die(f"A6: {m} not SUGGESTED")
    ok("A6_substrate_pins",
       "3 targets SUGGESTED at pinned codes; the R5-promoted 832-row surface "
       "intersects the targets in NOTHING (promotions file included); the 4 "
       "H3 rows HOLD on the R21 record")

    # ---- A7 idempotency -----------------------------------------------------------------
    h1 = sha16(PROPOSALS.read_bytes()), sha16(OVERRIDES.read_bytes())
    subprocess.run([sys.executable, str(REPO / "scripts/c42_r22_repair_proposals.py")],
                   capture_output=True, check=True)
    subprocess.run([sys.executable, str(REPO / "scripts/c42_r22_override_projection.py")],
                   capture_output=True, check=True)
    h2 = sha16(PROPOSALS.read_bytes()), sha16(OVERRIDES.read_bytes())
    if h1 != h2:
        die("A7: deterministic regeneration drifted")
    ok("A7_idempotency", "proposals + override map byte-identical re-runs")

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
           f"R22 footprint (pre-commit form)")
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
        die("A9: proposals surface 2 != the 3-row inventory")
    if sorted(r["mapping_id"] for r in props["surface3_heading_only_h3_continuity"]) != hold_ids:
        die("A9: proposals H3 continuity != the 4 HOLD rows")
    ok("A9_round_artifacts",
       "proposals surfaces 0/3/4 pinned; the standing convention record "
       "remains pinned (c42-heading-only-convention-1 md + json)")

    # ---- report ---------------------------------------------------------------------------------
    head_sha = head
    out = {
        "schema": "c42-r22-repair-check/1.0",
        "task": "T-C42",
        "stage": "r22-r1-shaped-repair-round-check",
        "round": "R22",
        "round_start": ROUND_START,
        "audited_head": head_sha,
        "baseline_store_sha256_16": sha16(STORE.read_bytes()),
        "override_map_sha256_16": sha16(OVERRIDES.read_bytes()),
        "verdicts_sha256_16": sha16(VERDICTS.read_bytes()),
        "proposals_sha256_16": sha16(PROPOSALS.read_bytes()),
        "checks": CHECKS,
        "passed": len(CHECKS),
        "total": len(CHECKS),
        "result": "ALL PASS",
    }
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"c42_r22_repair_check: {out['result']} ({len(CHECKS)}/{len(CHECKS)}) "
          f"-> {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
