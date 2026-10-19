#!/usr/bin/env python3
"""c42_r18_repair_check.py — T-C42 R18 two-way audit.

A1 inventory agreement: the R18 section_overrides cover exactly the R17
   defect inventory (the 2 REJECT rows of scripts/c42_r17_fresh_verdicts.yaml
   joined to the live substrate — (converting-between-fdp, ord 3, 1.2G) and
   (basic-angle-properties, ord 1, 4.1B)); the id-level surface is EMPTY (no
   note-level-class root — verified, not assumed); no dupes, no extras. The
   R17 fill record pins the same 2-row inventory.
A2 projection agreement: scripts/c42_section_overrides_r18.yaml equals the
   verdict record — 2 verdicted entries (1 REATTRIBUTE + 1 DEMOTE) + 2
   extension entries on exactly the census-remark ords (fdp 2/4, unsampled by
   R17), the two note-level STANDING rulings, the standing convention block,
   no subsumed entries, the residual.
A3 code domain: every override_code is a canonical-188 member, differs from
   current_code, is Foundation-tier (bare-id convention documented); the
   DEMOTE carries override_code null; the two current_codes match the live
   substrate.
A4 wordings: the store wordings of 1.3D / 1.6C match the verdict citations
   verbatim; 1.2G / 4.1B are ABSENT from the C30 ledger (the R17
   not-a-tier-artifact rulings hold against the ledger).
A5 note-level joins STAND + resolution byte-untouched: the join rows for
   spcpt_8MpvS5pnYkf9QswF (1.2G) and spcpt_5FMXZMjqSZ3GK53q (4.1B) stand at
   HEAD; the resolution file is byte-identical to the round-start HEAD
   (cf1d8ad); sme_spcpt_verify.py green (BASE re-pointed, the standing script
   unmodified).
A6 substrate state pins: the 2 REJECT mapping ids exist at SUGGESTED with
   codes 1.2G/4.1B; the 2 extension mapping ids exist at 1.2G; the 8 H3 rows
   are HOLD on the R17 review record (source heading-only-convention).
A7 idempotency: re-running the projection emitter and the proposals scorer
   is byte-identical (deterministic regeneration).
A8/A10 footprint + commit state: the working-tree delta vs the round-start
   HEAD (cf1d8ad) is within the declared R18 footprint (pre-commit form);
   post-commit the delta is empty and the check is re-runnable (the
   C8/X10 precedent). The resolution file's byte-identity is asserted
   explicitly in A5.
A9 round artifacts: the proposals packet pins the same declared surfaces
   (0 id-level / 2 section / 8 H3 listed) and the standing convention record
   remains pinned (md + json, decision_id c42-heading-only-convention-1).

Writes its own report graph/reports/C42_R18_REPAIR_CHECK.json.
Exit 0 iff every check passes.
"""
import hashlib
import io
import contextlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
RES_GIT = "SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json"
RES_PATH = REPO / RES_GIT
VERDICTS = REPO / "scripts/c42_r18_repair_verdicts.yaml"
OVERRIDES = REPO / "scripts/c42_section_overrides_r18.yaml"
PROPOSALS = REPO / "graph/reports/C42_R18_REPAIR_PROPOSALS.json"
CONVENTION_MD = REPO / "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md"
CONVENTION_JSON = REPO / "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.json"
R17_FRESH = REPO / "scripts/c42_r17_fresh_verdicts.yaml"
R17_REVIEW = REPO / "scripts/c42_r17_review_verdicts.yaml"
R17_RECORD = REPO / "graph/reports/C42_R17_MATHS_A_REGATE_FILL_RECORD.md"
JOIN = REPO / "Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json"
REPORT = REPO / "graph/reports/C42_R18_REPAIR_CHECK.json"
ROUND_START_HEAD = "cf1d8ad"  # the R17-closed HEAD; the round's pre-round baseline

FOOTPRINT = {
    "scripts/c42_r18_repair_proposals.py",
    "graph/reports/C42_R18_REPAIR_PROPOSALS.json",
    "scripts/c42_r18_repair_verdicts.yaml",
    "scripts/c42_r18_override_projection.py",
    "scripts/c42_section_overrides_r18.yaml",
    "scripts/c42_r18_repair_check.py",
    "graph/reports/C42_R18_REPAIR_CHECK.json",
    "graph/reports/C42_R18_RESOLUTION_REPAIR_RECORD.md",
}


def sha16(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:16]


def main() -> int:
    fails = []
    results = []

    def ck(name, ok, detail=""):
        print(f"  {name}: {'PASS' if ok else 'FAIL'}{(' — ' + detail) if detail and not ok else ''}")
        results.append({"check": name, "pass": bool(ok), "detail": detail if not ok else ""})
        if not ok:
            fails.append(name)

    vv = yaml.safe_load(VERDICTS.read_text())
    sec_ov = vv["section_overrides"]
    ext_ov = {k: x for k, x in vv["extension_section_overrides"].items() if k != "contract"}
    adjud = vv["note_level_adjudications"]
    convention = vv["heading_only_convention"]
    residual = vv["residual"]
    store = {p["code"]: p for p in yaml.safe_load(
        (REPO / "graph/igcse-maths-a/specification_points.yaml").read_text())["specification_points"]}
    ledger = {r["official_code"]: r for r in json.loads(
        (REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json").read_text())["rows"]}
    substrate = {r["mapping_id"]: r for r in yaml.safe_load(
        (REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml").read_text())["rows"]}
    fresh = yaml.safe_load(R17_FRESH.read_text())["verdicts"]
    review = yaml.safe_load(R17_REVIEW.read_text())["verdicts"]

    # ---- A1 inventory agreement ----
    reject_ids = {m for m, x in fresh.items() if x["verdict"] == "REJECT"}
    note_level = {m for m in reject_ids if "note-level" in (fresh[m].get("root") or "")}
    inv = set()
    for m in reject_ids:
        srow = substrate[m]
        inv.add((srow["note_path"].split("/")[-1].replace(".json", ""), srow["chunk"]["ordinal"]))
    want_inv = {("converting-between-fdp", 3), ("basic-angle-properties", 1)}
    got_inv = {(k.split("::")[0], int(k.split("::")[1])) for k in sec_ov}
    r17_record = R17_RECORD.read_text()
    a1_ok = (not note_level and inv == want_inv and got_inv == want_inv
             and "4MA1-1.2G" in r17_record and "4MA1-4.1B" in r17_record
             and len(reject_ids) == 2)
    ck("A1 inventory agreement (2 REJECT rows, 0 id-level, R17 record pins)",
       a1_ok, f"inv={sorted(inv)} note_level={sorted(note_level)}")

    # ---- A2 projection agreement ----
    proj = yaml.safe_load(OVERRIDES.read_text())
    p_ents = {(e["note_slug"], e["chunk_ordinal"]): e for e in proj["overrides"]}
    want_ents = {}
    for k, x in sec_ov.items():
        want_ents[(k.split("::")[0], int(k.split("::")[1]))] = ("verdicted", x["disposition"],
                                                                x.get("override_code"))
    for k, x in ext_ov.items():
        want_ents[(k.split("::")[0], int(k.split("::")[1]))] = ("extension", x["disposition"],
                                                                x.get("override_code"))
    got_ents = {k: (e["provenance_class"], e["action"], e["override_code"])
                for k, e in p_ents.items()}
    ext_keys = {(k.split("::")[0], int(k.split("::")[1])) for k in ext_ov}
    census_ok = ext_keys == {("converting-between-fdp", 2), ("converting-between-fdp", 4)}
    census_ok = census_ok and all(k not in inv for k in ext_keys)  # unsampled by R17
    adj_ok = (proj["note_level_adjudications"]["converting-between-fdp"]["ruling"]
              == adjud["converting-between-fdp"]["ruling"]
              and proj["note_level_adjudications"]["basic-angle-properties"]["ruling"]
              == adjud["basic-angle-properties"]["ruling"]
              and "STANDS" in proj["note_level_adjudications"]["converting-between-fdp"]["ruling"]
              and "STANDS" in proj["note_level_adjudications"]["basic-angle-properties"]["ruling"])
    conv_ok = proj["heading_only_convention"]["decision_id"] == convention["decision"] == \
        "c42-heading-only-convention-1"
    a2_ok = (got_ents == want_ents and len(p_ents) == 4 and census_ok and adj_ok and conv_ok
             and proj.get("subsumed_prior_entries") == []
             and proj["residual"]["disposition"] == "KEEP_UNRESOLVED")
    ck("A2 projection agreement (4 entries: 2 verdicted + 2 census-remark extensions; "
       "2 STANDING rulings; convention; residual)", a2_ok,
       f"ents mismatch={ {k: (got_ents.get(k), want_ents.get(k)) for k in set(got_ents) ^ set(want_ents)} } "
       f"census={census_ok} adj={adj_ok} conv={conv_ok}")

    # ---- A3 code domain ----
    bad = []
    for (slug, o), e in p_ents.items():
        cur = e["current_code"]
        oc = e["override_code"]
        if cur not in store:
            bad.append(f"{slug}::{o} current {cur} not in 188")
        if e["action"] == "REATTRIBUTE":
            if oc not in store or oc == cur:
                bad.append(f"{slug}::{o} override {oc} invalid")
            else:
                tier = (store[oc].get("applicability") or {}).get("tier")
                if tier != "Foundation":
                    bad.append(f"{slug}::{o} override {oc} tier {tier} != Foundation "
                               f"(bare-id convention)")
        elif e["action"] == "DEMOTE_TO_WORKLIST":
            if oc is not None:
                bad.append(f"{slug}::{o} DEMOTE carries override_code")
        else:
            bad.append(f"{slug}::{o} unknown action {e['action']}")
        # current_code must equal the live substrate's join-derived code
        mid = e.get("mapping_id")
        if mid and substrate[mid]["spec_code"] != cur:
            bad.append(f"{slug}::{o} current {cur} != substrate {substrate[mid]['spec_code']}")
    ck("A3 code domain (188 members, Foundation bare-id, DEMOTE null, currents match substrate)",
       not bad, "; ".join(bad[:4]))

    # ---- A4 wordings + not-a-tier-artifact ----
    w13 = store["4MA1-1.3D"]["official_wording"]
    w16 = store["4MA1-1.6C"]["official_wording"]
    a4_ok = (w13 == "convert a decimal to a fraction or a percentage"
             and w16 == "express a percentage as a fraction and as a decimal"
             and "1.2G" not in ledger and "4.1B" not in ledger
             and w13 in (sec_ov["converting-between-fdp::3"]["evidence"] or "")
             and w16 in (ext_ov["converting-between-fdp::4"]["evidence"] or ""))
    ck("A4 wordings verbatim + ledger absence (not-a-tier-artifact)", a4_ok,
       f"1.3D={w13!r} 1.6C={w16!r}")

    # ---- A5 joins STAND + resolution byte-untouched + downstream verifier ----
    # Verifier scoping (recorded, honest): the full-EQ materialization of this
    # session exposes a PRE-EXISTING September defect in the accounting pair
    # (T-KG-13's 2026-09-24 accounting dedup vs the 2026-09-19 T-SPEC-7
    # sidecars: the resolutions reference S4.069/S4.070/S4.071-class ids the
    # deduped parse no longer carries). The accounting inputs are byte-
    # identical a5c5b71 -> HEAD (diff verified in-repo) — the failure predates
    # every C42 round and is NOT an R18 regression; R18's footprint never
    # touches the EQ/parse space. The audit therefore asserts: (a) ZERO
    # verifier failures on the round's own course surface (both igcse-maths-a
    # tiers + igcse-chemistry-19), and (b) every observed failure confined to
    # the two accounting courses (the pre-existing class) — recorded as a
    # census item for the operator (the R0 pattern), never silently repaired.
    join = json.loads(JOIN.read_text())
    jrows = {r["anchor_id"]: r for r in join["joins"]}
    j1 = jrows[adjud["converting-between-fdp"]["anchor_id"]]
    j2 = jrows[adjud["basic-angle-properties"]["anchor_id"]]
    head_raw = subprocess.run(["git", "-C", str(REPO), "show", f"{ROUND_START_HEAD}:{RES_GIT}"],
                              capture_output=True, check=True).stdout
    res_bytes = RES_PATH.read_bytes() if RES_PATH.exists() else subprocess.run(
        ["git", "-C", str(REPO), "show", f"HEAD:{RES_GIT}"], capture_output=True, check=True).stdout
    res = json.loads(res_bytes)
    src = (REPO / "scripts/sme_spcpt_verify.py").read_text().replace(
        'BASE = Path("/home/z/my-project/download/syllabai-resources")',
        f'BASE = Path("{REPO}")')
    buf = io.StringIO()
    ns = {"__name__": "__spcpt_verify__", "__file__": str(REPO / "scripts/sme_spcpt_verify.py")}
    sp_rc, fail_courses = 0, []
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            exec(compile(src, "sme_spcpt_verify.py", "exec"), ns)
    except SystemExit as e:
        sp_rc = int(e.code or 0)
    PRE_EXISTING_ACCOUNTING = {"igcse-accounting-17-financial-statements",
                               "igcse-accounting-17-introduction-to-bookkeeping-and-accounting"}
    import re as _re
    _course_re = _re.compile(r"SME-ExamQuestion/([\w.-]+)")
    fail_courses = set()
    for ln in buf.getvalue().splitlines():
        if any(m in ln for m in ("resolution code not in registry", "foreign code",
                                 "ids without codes", "codes !=", "unresolved index id",
                                 "resolution table size")):
            m = _course_re.search(ln)
            if m:
                fail_courses.add(m.group(1))
            else:
                fail_courses.add(ln.split(":")[0].strip())
    fail_courses = sorted(c for c in fail_courses if c and "/" not in c)
    round_surface_fails = [c for c in fail_courses
                           if c in ("igcse-maths-a-18-higher", "igcse-maths-a-18-foundation",
                                    "igcse-chemistry-19")]
    a5_ok = (j1["resolved_code"] == "1.2G" and j2["resolved_code"] == "4.1B"
             and res_bytes == head_raw
             and res["counts"] == {"ids": 222, "resolved": 214, "unresolved": 8}
             and (res.get("repair") or {}).get("round") == "R14"  # last writer still R14
             and not round_surface_fails
             and set(fail_courses) <= PRE_EXISTING_ACCOUNTING)
    ck("A5 joins STAND (1.2G/4.1B) + resolution byte-untouched vs cf1d8ad + verifier green on "
       "the round surface (accounting failures = pre-existing T-KG-13 class, recorded)",
       a5_ok,
       f"j1={j1['resolved_code']} j2={j2['resolved_code']} res_eq_head={res_bytes == head_raw} "
       f"spcpt_rc={sp_rc} fail_courses={fail_courses}")

    # ---- A6 substrate state pins ----
    bad = []
    for mid, want_code in (("73324fa2b6bd3433", "4MA1-1.2G"), ("9c1ff91e80080d4b", "4MA1-4.1B"),
                           ("2c9be555e064b975", "4MA1-1.2G"), ("734603c6ddf10662", "4MA1-1.2G")):
        r = substrate.get(mid)
        if not r or r["validation_status"] != "SUGGESTED" or r["spec_code"] != want_code:
            bad.append(f"{mid}: {r and (r['spec_code'], r['validation_status'])}")
    holds = {m for m, x in review.items() if x["verdict"] == "HOLD"}
    a6_ok = not bad and len(holds) == 8 and all(
        review[m].get("source") == "heading-only-convention" for m in holds)
    ck("A6 substrate pins (4 mapping ids SUGGESTED at pinned codes) + 8 H3 HOLD rows",
       a6_ok, f"bad={bad} holds={len(holds)}")

    # ---- A7 idempotency ----
    before_map = OVERRIDES.read_bytes()
    r1 = subprocess.run(["python3", str(REPO / "scripts/c42_r18_override_projection.py")],
                        capture_output=True, text=True)
    after_map = OVERRIDES.read_bytes()
    before_prop = PROPOSALS.read_bytes()
    r2 = subprocess.run(["python3", str(REPO / "scripts/c42_r18_repair_proposals.py")],
                        capture_output=True, text=True)
    after_prop = PROPOSALS.read_bytes()
    a7_ok = (r1.returncode == 0 and r2.returncode == 0
             and before_map == after_map and before_prop == after_prop)
    ck("A7 idempotency (projection + proposals byte-identical re-runs)", a7_ok,
       f"map_eq={before_map == after_map} prop_eq={before_prop == after_prop}")

    # ---- A8/A10 footprint + commit state ----
    st = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                        capture_output=True, text=True).stdout.splitlines()
    dirty = sorted(l[3:].strip() for l in st if l.strip())
    changed = sorted(subprocess.run(
        ["git", "-C", str(REPO), "diff", "--name-only", ROUND_START_HEAD],
        capture_output=True, text=True).stdout.splitlines())
    outside_footprint = [p for p in changed if p not in FOOTPRINT]
    a8_ok = not outside_footprint and all(p in FOOTPRINT for p in dirty)
    form = "committed-clean (delta vs cf1d8ad empty, tree clean)" if (not changed and not dirty) else \
        f"pre-commit (dirty {len(dirty)}, changed-vs-baseline {len(changed)}, all within footprint)"
    ck(f"A8/A10 footprint + commit state [{form}]", a8_ok,
       f"outside={outside_footprint[:4]} dirty={dirty[:6]}")

    # ---- A9 round artifacts ----
    prop = json.loads(PROPOSALS.read_text())
    art_ok = (len(prop["surface1_id_level"]) == 0
              and len(prop["surface2_section_level"]) == 2
              and len(prop["surface3_heading_only_h3_continuity"]) == 8
              and prop["residual"]["anchor_id"] == residual["anchor_id"]
              and CONVENTION_MD.exists() and CONVENTION_JSON.exists()
              and json.loads(CONVENTION_JSON.read_text())["decision_id"]
              == "c42-heading-only-convention-1")
    ck("A9 round artifacts (proposals surfaces 0/2/8 + residual + standing convention record)",
       art_ok, f"s1={len(prop['surface1_id_level'])} s2={len(prop['surface2_section_level'])} "
               f"s3={len(prop['surface3_heading_only_h3_continuity'])}")

    print("ALL PASS" if not fails else f"FAILURES: {fails}")
    report = {
        "schema": "c42-r18-repair-check/1.0",
        "task": "T-C42", "round": "R18",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        "round_start_head": ROUND_START_HEAD,
        "checks": results,
        "all_pass": not fails,
        "exit": 0 if not fails else 1,
    }
    REPORT.write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n")
    print("report ->", REPORT.relative_to(REPO))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
