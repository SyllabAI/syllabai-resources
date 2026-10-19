#!/usr/bin/env python3
"""c42_r10_resolution_repair_check.py — T-C42 R10 two-way audit.

C1 verdicts<->file agreement (2 CORRECT with prior preserved, residual marker)
   — baseline-free: prior values are checked against the R9-recorded wrong
   codes and the repair blocks, not against a moving HEAD.
C2 counts consistency (222 / 214 / 8; ZERO newly-cleared ids this round).
C3 zero-drift: all 219 non-surface rows byte-identical to the PRE-R10 blob
   (a872cdd's resolution file — the R6-repaired state).
C4 code domain: every non-null resolved_code is a member of the canonical 188.
C5 top-level: R10 repair block (with the R1+R6 blocks preserved in
   repair_history), validation clause, convention + adjudication references.
C6 idempotency: re-running the apply verifies and does not rewrite.
C7 downstream: sme_spcpt_verify.py green; the R12 override projection equals
   the verdict record (7 verdicted REATTRIBUTE + 1 verdicted
   DEMOTE_TO_WORKLIST, the note-level adjudication, no subsumed entries).
C8 commit state: the resolution file and the R10 round artifacts are committed
   (git-clean) — the check is post-commit-runnable.
C9 round artifacts: the proposals packet pins the same declared surfaces
   (3 id-level anchors scored incl. the related-calculations note-level
   question, 7 section rows, 13 heading-only rows listed) and the convention
   record (+ JSON mirror) pins c42-heading-only-convention-1.

Writes its own report graph/reports/C42_R10_RESOLUTION_REPAIR_CHECK.json.
Exit 0 iff every check passes.
"""
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
RES_GIT = "SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json"
RES_PATH = REPO / RES_GIT
VERDICTS = REPO / "scripts/c42_r10_repair_verdicts.yaml"
OVERRIDES = REPO / "scripts/c42_section_overrides_r10.yaml"
PROPOSALS = REPO / "graph/reports/C42_R10_REPAIR_PROPOSALS.json"
CONVENTION = REPO / "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md"
CONVENTION_JSON = REPO / "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.json"
REPORT = REPO / "graph/reports/C42_R10_RESOLUTION_REPAIR_CHECK.json"
PRE_R10_COMMIT = "a872cdd"  # the R9-era HEAD; its resolution blob is the R6-repaired baseline
R9_WRONG_CODES = {
    # anchor_id -> the wrong code the R9 fresh verdicts rejected (prior values)
    "spcpt_GVgyB5BVfNDYGf8M": "2.2E",
    "spcpt_pqWsmktWyMCRfTk6": "1.2A",
}


def main() -> int:
    fails = []
    results = []

    def ck(name, ok, detail=""):
        print(f"  {name}: {'PASS' if ok else 'FAIL'}{(' — ' + detail) if detail and not ok else ''}")
        results.append({"check": name, "pass": bool(ok), "detail": detail if not ok else ""})
        if not ok:
            fails.append(name)

    vv = yaml.safe_load(VERDICTS.read_text())
    verdicts, residual = vv["verdicts"], vv["residual"]
    sec_ov = vv["section_overrides"]
    adjud = vv.get("note_level_adjudications", {})
    convention = vv.get("heading_only_convention", {})
    disk = json.loads(RES_PATH.read_text())
    head = json.loads(subprocess.run(
        ["git", "-C", str(REPO), "show", f"{PRE_R10_COMMIT}:{RES_GIT}"],
        capture_output=True, check=True).stdout)
    disk_by = {r["id"]: r for r in disk["resolved"]}
    head_by = {r["id"]: r for r in head["resolved"]}
    store = {p["code"]: p for p in yaml.safe_load(
        (REPO / "graph/igcse-maths-a/specification_points.yaml").read_text())["specification_points"]}
    ledger = {r["official_code"]: r for r in json.loads(
        (REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json").read_text())["rows"]}

    # C1
    bad = []
    for aid, x in verdicts.items():
        r, hp = disk_by[aid], head_by[aid]
        d = x["disposition"]
        rep = r.get("repair") or {}
        if rep.get("round") != "R10" or rep.get("disposition") != d:
            bad.append(f"{aid}: marker {rep.get('round')}/{rep.get('disposition')} != R10/{d}")
        if rep.get("prior", {}).get("code") != hp.get("resolved_code") or \
                rep.get("prior", {}).get("code") != R9_WRONG_CODES[aid]:
            bad.append(f"{aid}: prior code not preserved (want the R9-recorded wrong code "
                       f"{R9_WRONG_CODES[aid]})")
        if d == "CORRECT":
            bare = x["corrected_code"].split("-", 1)[1]
            if r.get("resolved_code") != bare:
                bad.append(f"{aid}: code {r.get('resolved_code')} != {bare}")
            higher = store[x["corrected_code"]]["applicability"]["tier"] == "Higher"
            want = ("IGCSE_MATHS_A:H-" + bare) if higher else "IGCSE_MATHS_A:" + bare
            if r.get("official_id") != want:
                bad.append(f"{aid}: id {r.get('official_id')} != {want}")
            wording = ledger[bare]["foundation"]["text"] if x.get("tier_wording_source") == "ledger" \
                else store[x["corrected_code"]]["official_wording"]
            if r.get("official_wording") != wording:
                bad.append(f"{aid}: wording not re-pointed")
        elif d == "UNRESOLVED":
            if r.get("resolved_code") is not None or r.get("official_wording") is not None:
                bad.append(f"{aid}: not cleared")
    rr = disk_by[residual["anchor_id"]]
    if (rr.get("repair") or {}).get("round") != "R10" or \
       (rr.get("repair") or {}).get("disposition") != "KEEP_UNRESOLVED" or \
       rr.get("resolved_code") is not None:
        bad.append("residual: marker/cleanliness")
    ck("C1 verdicts<->file agreement", not bad, "; ".join(bad[:4]))

    # C2 (zero clears this round)
    nulls = sorted(r["id"] for r in disk["resolved"] if not r.get("resolved_code"))
    head_nulls = sorted(r["id"] for r in head["resolved"] if not r.get("resolved_code"))
    cleared = sorted(set(nulls) - set(head_nulls))
    ck("C2 counts (222/214/8, zero cleared)", disk["counts"] == {"ids": 222, "resolved": 214, "unresolved": 8}
       and cleared == [] and len(nulls) == 8,
       f"counts={disk.get('counts')} cleared={cleared}")

    # C3 zero-drift on non-surface rows (vs the R6-repaired pre-R10 blob)
    surface = set(verdicts) | {residual["anchor_id"]}
    drift = [rid for rid, hr in head_by.items()
             if rid not in surface and disk_by[rid] != hr]
    ck("C3 zero-drift (219 non-surface rows)", not drift and len(head_by) - len(surface) == 219,
       f"{len(drift)} drifted: {drift[:3]}")

    # C4 code domain
    foreign = [r["resolved_code"] for r in disk["resolved"]
               if r.get("resolved_code") and f"4MA1-{r['resolved_code']}" not in store]
    ck("C4 code domain (0 foreign)", not foreign, str(foreign[:4]))

    # C5 top-level
    rep = disk.get("repair") or {}
    hist = disk.get("repair_history") or []
    ck("C5 top-level R10 block + R1/R6 history + clause + convention refs",
       rep.get("round") == "R10"
       and rep.get("counts_delta", {}).get("corrected") == 2
       and rep.get("counts_delta", {}).get("cleared_unresolved") == 0
       and rep.get("counts_delta", {}).get("section_overrides", {}).get("demote_to_worklist") == 1
       and any(h.get("round") == "R1" for h in hist) and any(h.get("round") == "R6" for h in hist)
       and "T-C42 R10 R1-shaped verdict round over the R9 defect inventory" in disk.get("validation", "")
       and "c42-heading-only-convention-1" in disk.get("validation", "")
       and rep.get("convention_record", "").startswith("graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md"))

    # C6 idempotency
    before = RES_PATH.read_bytes()
    r = subprocess.run(["python3", str(REPO / "scripts/c42_r10_resolution_repair_apply.py")],
                       capture_output=True, text=True)
    after = RES_PATH.read_bytes()
    ck("C6 idempotency (verify-only re-run)", r.returncode == 0 and before == after,
       r.stdout.strip()[-80:])

    # C7 downstream + projection
    proj = yaml.safe_load(OVERRIDES.read_text())
    p_ov = proj["overrides"]
    proj_verd = sorted((o["note_slug"], o["chunk_ordinal"], o["action"]) for o in p_ov)
    want_verd = sorted((k.split("::")[0], int(k.split("::")[1]), x["disposition"])
                       for k, x in sec_ov.items())
    adjud_ok = (proj.get("note_level_adjudications", {}).get("related-calculations", {}).get("ruling")
                == adjud.get("related-calculations-note-join", {}).get("ruling") == "THE NOTE-LEVEL JOIN STANDS")
    conv_ok = proj.get("heading_only_convention", {}).get("decision_id") == \
        convention.get("decision") == "c42-heading-only-convention-1"
    sub_ok = proj.get("subsumed_r1_entries") == []
    # sme_spcpt_verify.py hardcodes the legacy workspace BASE; run its unmodified
    # logic with BASE re-pointed at this repo (the R1 precedent mechanism)
    src = (REPO / "scripts/sme_spcpt_verify.py").read_text().replace(
        'BASE = Path("/home/z/my-project/download/syllabai-resources")',
        f'BASE = Path("{REPO}")')
    import io
    import contextlib
    buf = io.StringIO()
    ns = {"__name__": "__spcpt_verify__", "__file__": str(REPO / "scripts/sme_spcpt_verify.py")}
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            exec(compile(src, "sme_spcpt_verify.py", "exec"), ns)
        sp_rc, sp_tail = 0, buf.getvalue().strip()[-120:]
    except SystemExit as e:
        sp_rc = int(e.code or 0)
        sp_tail = buf.getvalue().strip()[-160:]
    ck("C7 override projection + adjudication + convention + sme_spcpt_verify (BASE re-pointed)",
       proj_verd == want_verd and adjud_ok and conv_ok and sub_ok and sp_rc == 0,
       f"spcpt_verify rc={sp_rc} tail={sp_tail}")

    # C8 commit state: the R10 round is committed and git-clean
    st = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                        capture_output=True, text=True).stdout.splitlines()
    dirty = sorted(l[3:].strip() for l in st if l.strip())
    r10_files_clean = not any(RES_GIT in p or "c42_r10" in p or "C42_R10" in p
                              or p == "scripts/c42_section_overrides_r10.yaml" for p in dirty)
    ck("C8 R10 round committed and git-clean", r10_files_clean, str(dirty[:6]))

    # proposals + convention artifacts exist and pin the same surfaces
    prop = json.loads(PROPOSALS.read_text())
    art_ok = (len(prop["surface1_id_level"]) == 3 and len(prop["surface2_section_level"]) == 7
              and len(prop["surface3_heading_only_inventory"]) == 13
              and CONVENTION.exists() and CONVENTION_JSON.exists()
              and json.loads(CONVENTION_JSON.read_text())["decision_id"] == "c42-heading-only-convention-1")
    ck("C9 round artifacts (proposals surfaces 3/7/13 + convention record)",
       art_ok, f"s1={len(prop['surface1_id_level'])} s2={len(prop['surface2_section_level'])} "
               f"s3={len(prop['surface3_heading_only_inventory'])}")

    print("ALL PASS" if not fails else f"FAILURES: {fails}")
    report = {
        "schema": "c42-r10-resolution-repair-check/1.0",
        "task": "T-C42", "round": "R10",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        "pre_r10_baseline_commit": PRE_R10_COMMIT,
        "baseline_blob_sha16": "466250eaa21fada2",
        "checks": results,
        "all_pass": not fails,
        "exit": 0 if not fails else 1,
    }
    REPORT.write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n")
    print("report ->", REPORT.relative_to(REPO))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
