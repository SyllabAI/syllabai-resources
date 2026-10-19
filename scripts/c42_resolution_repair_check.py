#!/usr/bin/env python3
"""c42_resolution_repair_check.py — T-C42 R1 two-way audit.

C1 verdicts<->file agreement (22 CORRECT with prior preserved, 21 AFFIRM with
   statements re-pointed to the Foundation wording, 2 UNRESOLVED cleared with
   prior preserved, residual marker).
C2 counts consistency (222 / 216 / 6; the 6 unresolved ids enumerated).
C3 zero-drift: all 176 non-surface rows byte-identical to the HEAD blob.
C4 code domain: every non-null resolved_code is a member of the canonical 188.
C5 top-level: repair block, validation clause, allowlist note.
C6 idempotency: re-running the apply verifies and does not rewrite.
C7 downstream: sme_spcpt_verify.py green; the R3 override projection equals
   the 16 section verdicts; no other tracked file modified this round.
C8 diff surface: git status shows exactly the resolution file + the R1
   artifacts.

Writes nothing. Exit 0 iff every check passes.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
RES_GIT = "SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json"
RES_PATH = REPO / RES_GIT
VERDICTS = REPO / "scripts/c42_repair_verdicts.yaml"
OVERRIDES = REPO / "scripts/c42_section_overrides.yaml"


def main() -> int:
    fails = []

    def ck(name, ok, detail=""):
        print(f"  {name}: {'PASS' if ok else 'FAIL'}{(' — ' + detail) if detail and not ok else ''}")
        if not ok:
            fails.append(name)

    vv = yaml.safe_load(VERDICTS.read_text())
    verdicts, residual, overrides = vv["verdicts"], vv["residual"], vv["section_overrides"]
    disk = json.loads(RES_PATH.read_text())
    head = json.loads(subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{RES_GIT}"],
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
        if rep.get("disposition") != d:
            bad.append(f"{aid}: marker {rep.get('disposition')} != {d}")
        if rep.get("prior", {}).get("code") != hp.get("resolved_code"):
            bad.append(f"{aid}: prior code not preserved")
        if d == "CORRECT":
            bare = x["corrected_code"].split("-", 1)[1]
            if r.get("resolved_code") != bare:
                bad.append(f"{aid}: code {r.get('resolved_code')} != {bare}")
            want = ("IGCSE_MATHS_A:H-" + bare) if x.get("tier_wording_source") == "store" and \
                (store[x["corrected_code"]]["applicability"]["tier"] == "Higher") \
                else "IGCSE_MATHS_A:" + bare
            if r.get("official_id") != want:
                bad.append(f"{aid}: id {r.get('official_id')} != {want}")
            wording = ledger[bare]["foundation"]["text"] if x.get("tier_wording_source") == "ledger" \
                else store[x["corrected_code"]]["official_wording"]
            if r.get("official_wording") != wording:
                bad.append(f"{aid}: wording not re-pointed")
        elif d == "AFFIRM":
            bare = x["prior_code"].split("-", 1)[1]
            if r.get("resolved_code") != hp.get("resolved_code"):
                bad.append(f"{aid}: AFFIRM changed the code")
            if r.get("official_id") != "IGCSE_MATHS_A:" + bare or \
               r.get("official_wording") != ledger[bare]["foundation"]["text"]:
                bad.append(f"{aid}: statement not re-pointed to the Foundation wording")
        elif d == "UNRESOLVED":
            if r.get("resolved_code") is not None or r.get("official_wording") is not None:
                bad.append(f"{aid}: not cleared")
    rr = disk_by[residual["anchor_id"]]
    if (rr.get("repair") or {}).get("disposition") != "KEEP_UNRESOLVED" or rr.get("resolved_code") is not None:
        bad.append("residual: marker/cleanliness")
    ck("C1 verdicts<->file agreement", not bad, "; ".join(bad[:4]))

    # C2
    nulls = sorted(r["id"] for r in disk["resolved"] if not r.get("resolved_code"))
    head_nulls = sorted(r["id"] for r in head["resolved"] if not r.get("resolved_code"))
    cleared = sorted(set(nulls) - set(head_nulls))
    want_cleared = sorted(a for a, x in verdicts.items() if x["disposition"] == "UNRESOLVED")
    ck("C2 counts", disk["counts"] == {"ids": 222, "resolved": 216, "unresolved": 6}
       and cleared == want_cleared, f"counts={disk.get('counts')} cleared={cleared}")

    # C3 zero-drift on non-surface rows
    surface = set(verdicts) | {residual["anchor_id"]}
    drift = [rid for rid, hr in head_by.items()
             if rid not in surface and disk_by[rid] != hr]
    ck("C3 zero-drift (176 non-surface rows)", not drift, f"{len(drift)} drifted: {drift[:3]}")

    # C4 code domain
    foreign = [r["resolved_code"] for r in disk["resolved"]
               if r.get("resolved_code") and f"4MA1-{r['resolved_code']}" not in store]
    ck("C4 code domain (0 foreign)", not foreign, str(foreign[:4]))

    # C5 top-level
    rep = disk.get("repair") or {}
    ck("C5 top-level repair block + clause",
       rep.get("round") == "R1"
       and rep.get("counts_delta", {}).get("corrected") == 22
       and "T-C42 R1 resolution-repair round" in disk.get("validation", "")
       and "T-C42 R1 (2026-10-02)" in disk.get("unresolved_allowlist_note", ""))

    # C6 idempotency
    before = RES_PATH.read_bytes()
    r = subprocess.run(["python3", str(REPO / "scripts/c42_resolution_repair_apply.py")],
                       capture_output=True, text=True)
    after = RES_PATH.read_bytes()
    ck("C6 idempotency (verify-only re-run)", r.returncode == 0 and before == after,
       r.stdout.strip()[-80:])

    # C7 downstream + projection
    proj = yaml.safe_load(OVERRIDES.read_text())["overrides"]
    proj_keys = sorted((o["note_slug"], o["chunk_ordinal"]) for o in proj)
    sec_keys = sorted((k.split("::")[0], int(k.split("::")[1])) for k in overrides)
    # sme_spcpt_verify.py hardcodes the legacy workspace BASE
    # (/home/z/my-project/download/syllabai-resources — a stale copy); run its
    # unmodified logic with BASE re-pointed at this repo, mechanism recorded
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
    ck("C7 override projection + sme_spcpt_verify (BASE re-pointed)",
       proj_keys == sec_keys and sp_rc == 0,
       f"spcpt_verify rc={sp_rc} tail={sp_tail}")

    # C8 diff surface
    st = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                        capture_output=True, text=True).stdout.splitlines()
    modified = sorted(l[3:].strip() for l in st if l.startswith(" M") or l.startswith("M "))
    ck("C8 diff surface (only the resolution file modified)",
       modified == [RES_GIT], str(modified))

    print("ALL PASS" if not fails else f"FAILURES: {fails}")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
