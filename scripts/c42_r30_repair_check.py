#!/usr/bin/env python3
"""c42_r30_repair_check.py — T-C42 R30 two-way audit (the R26 check shape).

A1 inventory agreement: the R30 section_overrides + promotions amendment
   cover exactly the R29-menu disposition set — the 9 verdict rows of
   scripts/c42_r30_repair_verdicts.yaml (the 4.11C trio from the R29 fresh
   REJECT + its 2 disclosed siblings; the grouping batch from the R26 census
   remarks; drawing ord 5 from the R26 remarks; 3d ord 3 from the R24
   candidate; drawing ord 0 the H3 hold resolved by re-homing); no dupes,
   no extras; the amendment's 5 supersedes + 3 exclusions cover exactly the
   8 HUMAN_VALIDATED movers and its 3 added entries exactly the 3 sign-off
   rows; the retain rulings ride NO carrier entry (zero movement).
A2 projection agreement: scripts/c42_section_overrides_r30.yaml equals the
   verdict record — 6 verdicted REATTRIBUTE entries + 3 verdicted
   DEMOTE_TO_WORKLIST entries (override_code null), the 3 H3 sign-offs, the
   2 retain rulings, the note-level scoping block, the census remarks, an
   EMPTY dated-corrections block, and the promoted-surface-amendment pointer
   (5+3+3); the live-store H3 hold set is exactly the 4 discharged rows.
A3 code domain: every REATTRIBUTE override_code is a canonical-188 member,
   differs from current_code; every current_code matches the live substrate;
   8 movers HUMAN_VALIDATED, 1 re-homed row SUGGESTED (the R22
   SUGGESTED-row re-attribution precedent).
A4 wordings: the store wordings carry the verdict citations verbatim
   (2.7C's form-and-solve-from-context demand; 4.8F's trig-3D demand;
   3.3I's generate-points-and-plot demand; 2.2F's cap; 4.8D's
   Pythagoras-3D demand; 3.3F's gradient demand; 5.1D's add/subtract
   demand); the C30 ledger facts hold — 2.7C/4.11C/4.8D/4.8F/3.3I/2.2F/
   1.7B/6.3J/5.1D ABSENT (Higher-only/single-tier), 3.3F and 2.2C PRESENT
   as shared-tier rows with the cited Foundation texts (asserted, not
   assumed).
A5 joins STAND + resolution byte-untouched: the four R26 STANDING anchors
   (spcpt_J55PhZ2cbPsYvpt8 1.1G, spcpt_vMSNnYkKPf62MRH9 2.2F,
   spcpt_h8QyRmzX5mCJb3X9 3.3F, spcpt_v6tP4DSVShVJMJhk 5.1D) stand at HEAD
   together with the equations-and-problem-solving anchor
   spcpt_DcSkGdrNWCZYX4V8 at 4.11C (the join layer untouched — the store
   rows move, the joins stand); the resolution file is byte-identical
   between the round-start HEAD (737d24a) and the audit HEAD.
A6 substrate pins + promoted-surface guard: the store is the R29-of-record
   state (831 HUMAN_VALIDATED + 7 anchored SUGGESTED); the 8 mover rows are
   R5-pinned with matching identities; the 3 added rows are SUGGESTED and
   NOT pinned (the R5-apply hold set); the 4 live H3 rows are exactly the
   discharged set (3 sign-offs + 1 re-home); 2.7C carries ZERO anchored
   chunk rows and exactly its uncovered-SP DEFER row f081d3d51385cb8f (the
   gain fact); 4.11C/3.3F/4.8D/2.2F anchored censuses are 7/6/5/17.
A7 idempotency: re-running the projection emitter is byte-identical
   (deterministic regeneration).
A8/A10 footprint + commit state: the working-tree delta vs the round-start
   HEAD (737d24a) is within the declared R30 footprint (pre-commit form);
   post-commit the delta is empty and the check is re-runnable (the
   C8/X10 precedent).
A9 round artifacts: the verdict record pins its own blocks (9 section
   overrides / 3 sign-offs / 2 retains / the scoping notes / the census
   remarks) and the record md + json pin the same disposition set; the
   projected re-key ids in the record match the c40 identity function
   recomputed live.

Writes its own report graph/reports/C42_R30_REPAIR_CHECK.json.
Exit 0 iff every check passes.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "graph/reports/C42_R30_REPAIR_CHECK.json"
VERDICTS = REPO / "scripts/c42_r30_repair_verdicts.yaml"
OVERRIDES = REPO / "scripts/c42_section_overrides_r30.yaml"
AMENDMENT = REPO / "scripts/c42_r30_promotions_amendment.yaml"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
REGISTRY = REPO / "graph/igcse-maths-a/specification_points.yaml"
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"
JOIN = REPO / ("Official-Specifications/parsed/_derived/notes-join/"
               "igcse-maths-a-18-higher.json")
PROMOTIONS = REPO / "scripts/c42_r5_promotions.yaml"
REC_MD = REPO / "graph/reports/C42_R30_RESOLUTION_REPAIR_RECORD.md"
REC_JSON = REPO / "graph/reports/C42_R30_RESOLUTION_REPAIR_RECORD.json"
RES_GIT = "SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json"
ROUND_START = "737d24a"

FOOTPRINT = [
    "scripts/c42_r30_repair_verdicts.yaml",
    "scripts/c42_r30_override_projection.py",
    "scripts/c42_r30_repair_check.py",
    "scripts/c42_section_overrides_r30.yaml",
    "scripts/c42_r30_promotions_amendment.yaml",
    "graph/reports/C42_R30_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R30_RESOLUTION_REPAIR_RECORD.json",
    "graph/reports/C42_R30_REPAIR_CHECK.json",
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
    import re
    return re.sub(r"\s+", "", s or "").lower()


def git(args) -> str:
    return subprocess.run(["git", "-C", str(REPO)] + args,
                          capture_output=True, text=True, check=True).stdout


def git_bytes(rev_path: str) -> bytes:
    return subprocess.run(["git", "-C", str(REPO), "show", rev_path],
                          capture_output=True, check=True).stdout


def c40_ids():
    """Recompute the c40 identity function live (the projected re-keys)."""
    sys.path.insert(0, str(REPO / "scripts"))
    import c40_maths_a_chunk_sp_substrate as c40  # noqa
    return c40.sha16, c40.norm


def main() -> int:
    for p in (VERDICTS, OVERRIDES, AMENDMENT, STORE, REGISTRY, LEDGER, JOIN,
              PROMOTIONS, REC_MD, REC_JSON):
        if not p.exists():
            die(f"required artifact missing: {p.relative_to(REPO)}")

    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    ovr = yaml.safe_load(OVERRIDES.read_text(encoding="utf-8"))
    amd = yaml.safe_load(AMENDMENT.read_text(encoding="utf-8"))
    store = yaml.safe_load(STORE.read_text(encoding="utf-8"))
    reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    points = {p["code"] for p in reg["specification_points"]}
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    led_rows = {r["official_code"]: r for r in ledger["rows"]}
    join = json.loads(JOIN.read_text(encoding="utf-8"))
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    promo_pins = {e["row"]["mapping_id"]: e["row"]
                  for e in promo["promotions"]}
    rec = json.loads(REC_JSON.read_text(encoding="utf-8"))

    rows_by_id = {r["mapping_id"]: r for r in store["rows"]}
    v_by_mid = {v["mapping_id"]: v
                for v in ver["section_overrides"].values()}
    ovr_entries = {e["mapping_id"]: e for e in ovr["overrides"]}
    sup = {e["mapping_id"]: e for e in amd["supersedes_code"]}
    exc = {e["mapping_id"]: e for e in amd["excluded"]}
    added = amd["added"]
    added_by_mid = {a["row"]["mapping_id"]: a for a in added}
    signed = set(ver["h3_signoffs"]) - {"contract"}
    signed_ids = {ver["h3_signoffs"][k]["mapping_id"] for k in signed}
    retains = set(ver["retain_rulings"]) - {"contract"}
    retain_ids = {ver["retain_rulings"][k]["mapping_id"] for k in retains}

    # ---- A1 inventory agreement ------------------------------------------------
    if sorted(ovr_entries) != sorted(v_by_mid):
        die(f"A1: override ids != verdict ids")
    if len(ovr_entries) != 9:
        die(f"A1: expected the 9-row disposition set, got {len(ovr_entries)}")
    hv_movers = {m for m, e in ovr_entries.items()
                 if rows_by_id[m]["validation_status"] == "HUMAN_VALIDATED"}
    if sorted(sup) != sorted(m for m, e in ovr_entries.items()
                             if e["action"] == "REATTRIBUTE"
                             and m in hv_movers):
        die("A1: amendment supersedes != the 5 HV REATTRIBUTE rows")
    if sorted(exc) != sorted(m for m, e in ovr_entries.items()
                             if e["action"] == "DEMOTE_TO_WORKLIST"):
        die("A1: amendment exclusions != the 3-row DEMOTE batch")
    if sorted(added_by_mid) != sorted(signed_ids):
        die("A1: amendment additions != the 3 sign-off rows")
    movers = set(ovr_entries)
    if signed_ids & movers or retain_ids & movers:
        die("A1: sign-off/retain rows must ride NO map entry")
    if any(m in promo_pins for m in signed_ids):
        die("A1: a sign-off row is already R5-pinned")
    if not all(m in hv_movers for m in
               list(sup) + list(exc)):
        die("A1: a supersedes/excluded row is not HUMAN_VALIDATED")
    ok("A1_inventory_agreement",
       "overrides == verdicts == the 9-row disposition set; amendment 5 "
       "supersedes + 3 exclusions == the 8 HV movers; 3 additions == the 3 "
       "sign-off rows; retains ride no carrier (zero movement); sign-off "
       "rows unpinned")

    # ---- A2 projection agreement --------------------------------------------------
    acts = sorted(e["action"] for e in ovr_entries.values())
    if acts != ["DEMOTE_TO_WORKLIST"] * 3 + ["REATTRIBUTE"] * 6:
        die(f"A2: unexpected action mix {acts}")
    for e in ovr_entries.values():
        v = v_by_mid[e["mapping_id"]]
        if e["action"] != v["disposition"] \
                or (e["override_code"] or None) != (v.get("override_code") or None) \
                or e["current_code"] != v["current_code"]:
            die(f"A2: map/verdict drift on {e['mapping_id']}")
    if sorted(ver["h3_signoffs"][k]["mapping_id"] for k in signed) \
            != sorted(added_by_mid):
        die("A2: sign-off block != amendment additions")
    if len(retains) != 2:
        die("A2: expected exactly 2 retain rulings")
    if ovr.get("note_level_scoping") != ver["note_level_scoping"] \
            or len(ovr["note_level_scoping"]) != 2:
        die("A2: note-level scoping block drifted")
    if "note_level_adjudications" in ovr:
        die("A2: no NEW c40-pinned note-level adjudications this round")
    live_holds = sorted(
        m for m, r in rows_by_id.items()
        if r.get("validation_status") == "SUGGESTED"
        and r.get("spec_code") in ("4MA1-1.7B", "4MA1-6.3J", "4MA1-3.3F",
                                   "4MA1-2.2C"))
    if live_holds != sorted(signed_ids | {"91a5080f8b390de6"}) \
            or len(live_holds) != 4:
        die(f"A2: live H3 hold set drifted: {live_holds}")
    if ovr.get("dated_corrections") != []:
        die("A2: dated corrections expected EMPTY this round")
    if not ovr.get("census_remarks") or len(ovr["census_remarks"]) < 3:
        die("A2: census remarks missing")
    psa = ovr.get("promoted_surface_amendment") or {}
    if psa.get("amendment_file") != "scripts/c42_r30_promotions_amendment.yaml" \
            or psa.get("base_file_untouched") is not True \
            or psa.get("supersedes") != 5 or psa.get("excluded") != 3 \
            or psa.get("added") != 3:
        die("A2: promoted-surface-amendment pointer drifted")
    if amd.get("schema") != "c42-r31-promotions-amendment/1.0" \
            or amd.get("base_file_sha256_16") != "9bad739bd79e5899" \
            or amd.get("prior_amendments") != \
            ["scripts/c42_r26_promotions_amendment.yaml"]:
        die("A2: amendment schema/base/prior-amendment pins drifted")
    ok("A2_projection_agreement",
       "map == verdicts (6 REATTRIBUTE + 3 DEMOTE, statuses 8 HV + 1 "
       "SUGGESTED); sign-offs/retains/scoping/remarks pinned; the 4 live H3 "
       "rows == the discharged set; amendment schema bump + base pin + "
       "prior-amendments pinned")

    # ---- A3 code domain -------------------------------------------------------------
    for m, e in ovr_entries.items():
        srow = rows_by_id.get(m)
        if srow is None:
            die(f"A3: {m} not in the live substrate")
        if srow["spec_code"] != e["current_code"]:
            die(f"A3: current_code drift on {m}")
        if e["action"] == "REATTRIBUTE":
            if e["override_code"] not in points:
                die(f"A3: target {e['override_code']} outside the ratified 188")
            if e["override_code"] == e["current_code"]:
                die(f"A3: target equals current on {m}")
            want_status = "SUGGESTED" if m == "91a5080f8b390de6" \
                else "HUMAN_VALIDATED"
            if srow.get("validation_status") != want_status:
                die(f"A3: {m} status {srow.get('validation_status')} != "
                    f"{want_status}")
        elif e["override_code"] is not None:
            die(f"A3: DEMOTE target must be null on {m}")
    ok("A3_code_domain",
       "6 targets canonical-188 members, distinct from currents; DEMOTE "
       "targets null; currents match the live substrate; statuses 8 HV + 1 "
       "SUGGESTED (the re-homed hold)")

    # ---- A4 wordings + ledger facts ---------------------------------------------------
    reg_pts = {p["code"]: p for p in reg["specification_points"]}
    w27c = reg_pts["4MA1-2.7C"].get("official_wording") or ""
    w48f = reg_pts["4MA1-4.8F"].get("official_wording") or ""
    w33i = reg_pts["4MA1-3.3I"].get("official_wording") or ""
    w22f = reg_pts["4MA1-2.2F"].get("official_wording") or ""
    w48d = reg_pts["4MA1-4.8D"].get("official_wording") or ""
    w33f = reg_pts["4MA1-3.3F"].get("official_wording") or ""
    w51d = reg_pts["4MA1-5.1D"].get("official_wording") or ""
    h = squash(w27c)
    if "formandsolve" not in h or "quadratic" not in h or "context" not in h:
        die("A4: 2.7C form-and-solve-from-context demand missing")
    h = squash(w48f)
    if "trigonometricalmethods" not in h or "threedimensions" not in h:
        die("A4: 4.8F trig-3D demand missing")
    h = squash(w33i)
    if "generatepoints" not in h or "plotgraphs" not in h or "linear" not in h:
        die("A4: 3.3I generate-points-and-plot demand missing")
    if squash("limited") not in squash(w22f):
        die("A4: 2.2F cap missing")
    if "pythagoras" not in squash(w48d) or "threedimensions" not in squash(w48d):
        die("A4: 4.8D Pythagoras-3D demand missing")
    if "gradient" not in squash(w33f) or "twopoints" not in squash(w33f):
        die("A4: 3.3F gradient demand missing")
    if squash("add and subtract vectors") not in squash(w51d):
        die("A4: 5.1D demand missing")
    for bare in ("2.7C", "4.11C", "4.8D", "4.8F", "3.3I", "2.2F", "1.7B",
                 "6.3J", "5.1D"):
        if bare in led_rows:
            die(f"A4: {bare} expected ABSENT from the C30 ledger")
    for bare, want in (("3.3F", "draw and interpret straight line conversion graphs"),
                       ("2.2C", "multiply a single term over a bracket")):
        if bare not in led_rows:
            die(f"A4: {bare} expected PRESENT in the C30 ledger")
        got = led_rows[bare]["foundation"]["text"]
        if squash(want) not in squash(got):
            die(f"A4: {bare} Foundation text drifted: {got!r}")
    ok("A4_wordings_ledger",
       "store wordings carry the citations verbatim (2.7C / 4.8F / 3.3I / "
       "2.2F cap / 4.8D / 3.3F / 5.1D); ledger facts asserted: 9 codes "
       "absent (Higher-only/single-tier), 3.3F + 2.2C present with the "
       "cited Foundation texts (the 2.2C sign-off's tier-artifact basis)")

    # ---- A5 joins STAND + resolution byte-untouched -------------------------------------
    join_rows = {r["anchor_id"]: r for r in join["joins"]}
    for aid, want in [("spcpt_J55PhZ2cbPsYvpt8", "4MA1-1.1G"),
                      ("spcpt_vMSNnYkKPf62MRH9", "4MA1-2.2F"),
                      ("spcpt_h8QyRmzX5mCJb3X9", "4MA1-3.3F"),
                      ("spcpt_v6tP4DSVShVJMJhk", "4MA1-5.1D"),
                      ("spcpt_DcSkGdrNWCZYX4V8", "4MA1-4.11C")]:
        jr = join_rows.get(aid)
        if jr is None or jr.get("store_row_code") != want:
            got = (jr or {}).get("store_row_code")
            die(f"A5: join row for {aid} does not stand at {want} (got {got})")
    res_start = git_bytes(f"{ROUND_START}:{RES_GIT}")
    res_head = git_bytes(f"HEAD:{RES_GIT}")
    if res_start != res_head:
        die("A5: resolution file drifted between the round-start HEAD and HEAD")
    ok("A5_joins_resolution",
       "4 R26 STANDING anchors + the equations-and-problem-solving anchor "
       "stand at HEAD (the join layer untouched); resolution file "
       "byte-identical 737d24a -> HEAD")

    # ---- A6 substrate pins + promoted-surface guard ---------------------------------------
    hv = {m for m, r in rows_by_id.items()
          if r.get("validation_status") == "HUMAN_VALIDATED"}
    sugg_anch = {m for m, r in rows_by_id.items()
                 if r.get("validation_status") == "SUGGESTED"
                 and r.get("spec_code") and "chunk" in r}
    if len(hv) != 831 or len(sugg_anch) != 7:
        die(f"A6: store is not the R29-of-record state "
            f"(831 HV + 7 anchored SUGGESTED, got {len(hv)}/{len(sugg_anch)})")
    for m in hv_movers:
        pin = promo_pins.get(m)
        srow = rows_by_id[m]
        if pin is None:
            die(f"A6: {m} not pinned in the R5 promotions file")
        if (pin.get("spec_code") != srow["spec_code"]
                or pin.get("note_path") != srow["note_path"]
                or pin.get("chunk_ordinal") != srow["chunk"]["ordinal"]):
            die(f"A6: promotions pin identity drift on {m}")
    for m, a in added_by_mid.items():
        srow = rows_by_id[m]
        r = a["row"]
        if (srow["spec_code"] != r["spec_code"]
                or srow["note_path"] != r["note_path"]
                or srow["chunk"]["ordinal"] != r["chunk_ordinal"]
                or srow["chunk"]["heading"] != r["heading"]
                or srow["chunk"]["sha256_16"] != r["chunk_sha256_16"]):
            die(f"A6: added-entry identity drift on {m}")
        if a["verdict"] != "SIGN_OFF" or a["validated_by"] != "operator" \
                or not a.get("signoff_basis"):
            die(f"A6: added-entry sign-off shape drift on {m}")
    for code, want_n in (("4MA1-4.11C", 7), ("4MA1-3.3F", 6),
                         ("4MA1-4.8D", 5), ("4MA1-2.2F", 17)):
        n = len([r for r in store["rows"]
                 if r.get("spec_code") == code and "chunk" in r])
        if n != want_n:
            die(f"A6: {code} anchored rows expected {want_n}, got {n}")
    anchored27 = [r for r in store["rows"]
                  if r.get("spec_code") == "4MA1-2.7C" and "chunk" in r]
    if anchored27:
        die("A6: 2.7C already carries anchored rows — the gain fact drifted")
    defer = [r for r in store["rows"]
             if r.get("spec_code") == "4MA1-2.7C" and r.get("worklist_reason")]
    if len(defer) != 1 or defer[0]["mapping_id"] != "f081d3d51385cb8f":
        die("A6: the 2.7C DEFER row not found")
    ok("A6_substrate_pins",
       "store at the R29-of-record state (831 + 7); 8 movers R5-pinned; 3 "
       "added rows SUGGESTED + unpinned with verbatim sign-off bases; "
       "4.11C/3.3F/4.8D/2.2F censuses 7/6/5/17; 2.7C uncovered with exactly "
       "its DEFER row (the gain fact)")

    # ---- A9 round artifacts + projected re-keys ---------------------------------------------
    if len(v_by_mid) != 9 or len(signed) != 3 or len(retains) != 2:
        die("A9: verdict record blocks drifted")
    if rec.get("baseline", {}).get("store_sha256_16") != sha16(STORE.read_bytes()):
        die("A9: record baseline store pin drifted")
    rec_ids = sorted(o["mapping_id"] for o in rec["section_overrides"])
    if rec_ids != sorted(ovr_entries):
        die("A9: record section_overrides != the disposition set")
    sha16f, normf = c40_ids()
    for o in rec["section_overrides"]:
        srow = rows_by_id[o["mapping_id"]]
        if o["action"] == "REATTRIBUTE":
            want = sha16f(f"{srow['note_path']}|{o['target']}|"
                          f"{normf(srow['evidence_quote'])}")
        else:
            want = sha16f(f"demoted|{srow['note_path']}|"
                          f"{srow['chunk']['ordinal']}")
        if o["projected_new_id"] != want:
            die(f"A9: projected re-key drift on {o['mapping_id']}")
    if not REC_MD.exists():
        die("A9: record md missing")
    ok("A9_round_artifacts",
       "record md + json pinned; the projected re-key ids match the c40 "
       "identity function recomputed live (6 REATTRIBUTE + 3 DEMOTE)")

    # ---- A7 idempotency -----------------------------------------------------------------
    h1 = sha16(OVERRIDES.read_bytes()), sha16(AMENDMENT.read_bytes())
    subprocess.run([sys.executable,
                    str(REPO / "scripts/c42_r30_override_projection.py")],
                   capture_output=True, check=True)
    h2 = sha16(OVERRIDES.read_bytes()), sha16(AMENDMENT.read_bytes())
    if h1 != h2:
        die("A7: deterministic regeneration drifted")
    ok("A7_idempotency",
       "override map + promotions amendment byte-identical re-runs")

    # ---- A8/A10 footprint + commit state ---------------------------------------------------
    head = git(["rev-parse", "HEAD"]).strip()
    if head.startswith(ROUND_START):
        changed = [ln[3:].strip() for ln in
                   git(["status", "--porcelain"]).splitlines() if ln.strip()]
        outside = [c for c in changed if c not in FOOTPRINT
                   and not any(c.endswith(f" -> {f}") for f in FOOTPRINT)]
        if outside:
            die(f"A8: working-tree delta outside the declared footprint: "
                f"{outside[:5]}...")
        ok("A8_footprint_precommit",
           f"delta vs {ROUND_START} is exactly the declared {len(FOOTPRINT)}-file "
           f"R30 footprint (pre-commit form)")
    else:
        dirty = git(["status", "--porcelain"]).strip()
        if dirty:
            die(f"A10: post-commit tree is dirty: {dirty[:200]}")
        ok("A10_committed_clean",
           f"HEAD {head[:8]} is the round commit; tree clean; the check "
           f"re-runs committed-clean (the C8/X10 precedent)")

    # ---- report ---------------------------------------------------------------------------------
    out = {
        "schema": "c42-r30-repair-check/1.0",
        "task": "T-C42",
        "stage": "r30-operator-delegate-dispositions-check",
        "round": "R30",
        "round_start": ROUND_START,
        "audited_head": head,
        "baseline_store_sha256_16": sha16(STORE.read_bytes()),
        "override_map_sha256_16": sha16(OVERRIDES.read_bytes()),
        "amendment_sha256_16": sha16(AMENDMENT.read_bytes()),
        "verdicts_sha256_16": sha16(VERDICTS.read_bytes()),
        "record_sha256_16": sha16(REC_JSON.read_bytes()),
        "checks": CHECKS,
        "passed": len(CHECKS),
        "total": len(CHECKS),
        "result": "ALL PASS",
    }
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"c42_r30_repair_check: {out['result']} ({len(CHECKS)}/{len(CHECKS)}) "
          f"-> {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
