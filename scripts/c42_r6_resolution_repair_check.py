#!/usr/bin/env python3
"""c42_r6_resolution_repair_check.py — T-C42 R6 two-way audit.

C1 verdicts<->file agreement (8 CORRECT with prior preserved, 2 UNRESOLVED
   cleared with prior preserved, residual marker) — baseline-free: prior
   values are checked against the R4-recorded wrong codes and the repair
   blocks, not against a moving HEAD.
C2 counts consistency (222 / 214 / 8; the 2 newly cleared ids enumerated).
C3 zero-drift: all 211 non-surface rows byte-identical to the PRE-R6 blob
   (d141c59's resolution file) — the R1-repaired state.
C4 code domain: every non-null resolved_code is a member of the canonical 188.
C5 top-level: R6 repair block (with the R1 block preserved in repair_history),
   validation clause, allowlist note.
C6 idempotency: re-running the apply verifies and does not rewrite.
C7 downstream: sme_spcpt_verify.py green; the R8 override projection equals
   the verdict record (4 verdicted + 3 labeled extension entries, the
   subsumption registry).
C8 commit state: the resolution file and the R6 round artifacts are committed
   (git-clean) — the check is post-commit-runnable.

Writes nothing. Exit 0 iff every check passes.
"""
import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
RES_GIT = "SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json"
RES_PATH = REPO / RES_GIT
VERDICTS = REPO / "scripts/c42_r6_repair_verdicts.yaml"
OVERRIDES = REPO / "scripts/c42_section_overrides_r6.yaml"
PRE_R6_COMMIT = "d141c59"  # the R4-era HEAD; its resolution blob is the R1-repaired baseline
R4_WRONG_CODES = {
    # anchor_id -> the wrong code the R4 fresh verdicts rejected (prior values)
    "spcpt_4ZdHtGPdDjYdR6rK": "4.4C", "spcpt_2nCMJhvvGsW7vMcV": "2.8D",
    "spcpt_SYHWnwMWKxDNg9s8": "2.4B", "spcpt_hrv7F8zpDwRXmcNg": "3.3I",
    "spcpt_zrrC3yxSp579jY7k": "3.4C", "spcpt_pSX9GyS8bW7N5CH7": "4.8E",
    "spcpt_X8CSxK2dhn5rX34f": "2.8D", "spcpt_339DNssRW9x2NPKk": "1.2I",
    "spcpt_mVXT4jbXQPrzhHvz": "4.11C", "spcpt_hK2H8q4Y8NYv833v": "5.1G",
}


def main() -> int:
    fails = []

    def ck(name, ok, detail=""):
        print(f"  {name}: {'PASS' if ok else 'FAIL'}{(' — ' + detail) if detail and not ok else ''}")
        if not ok:
            fails.append(name)

    vv = yaml.safe_load(VERDICTS.read_text())
    verdicts, residual = vv["verdicts"], vv["residual"]
    sec_ov, ext_ov = vv["section_overrides"], vv["extension_section_overrides"]
    subsumed = vv["subsumed_r1_entries"]["entries"]
    disk = json.loads(RES_PATH.read_text())
    head = json.loads(subprocess.run(
        ["git", "-C", str(REPO), "show", f"{PRE_R6_COMMIT}:{RES_GIT}"],
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
        if rep.get("round") != "R6" or rep.get("disposition") != d:
            bad.append(f"{aid}: marker {rep.get('round')}/{rep.get('disposition')} != R6/{d}")
        if rep.get("prior", {}).get("code") != hp.get("resolved_code") or \
                rep.get("prior", {}).get("code") != R4_WRONG_CODES[aid]:
            bad.append(f"{aid}: prior code not preserved (want the R4-recorded wrong code "
                       f"{R4_WRONG_CODES[aid]})")
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
    if (rr.get("repair") or {}).get("round") != "R6" or \
       (rr.get("repair") or {}).get("disposition") != "KEEP_UNRESOLVED" or \
       rr.get("resolved_code") is not None:
        bad.append("residual: marker/cleanliness")
    ck("C1 verdicts<->file agreement", not bad, "; ".join(bad[:4]))

    # C2
    nulls = sorted(r["id"] for r in disk["resolved"] if not r.get("resolved_code"))
    head_nulls = sorted(r["id"] for r in head["resolved"] if not r.get("resolved_code"))
    cleared = sorted(set(nulls) - set(head_nulls))
    want_cleared = sorted(a for a, x in verdicts.items() if x["disposition"] == "UNRESOLVED")
    ck("C2 counts", disk["counts"] == {"ids": 222, "resolved": 214, "unresolved": 8}
       and cleared == want_cleared and len(nulls) == 8,
       f"counts={disk.get('counts')} cleared={cleared}")

    # C3 zero-drift on non-surface rows (vs the R1-repaired pre-R6 blob)
    surface = set(verdicts) | {residual["anchor_id"]}
    drift = [rid for rid, hr in head_by.items()
             if rid not in surface and disk_by[rid] != hr]
    ck("C3 zero-drift (211 non-surface rows)", not drift and len(head_by) - len(surface) == 211,
       f"{len(drift)} drifted: {drift[:3]}")

    # C4 code domain
    foreign = [r["resolved_code"] for r in disk["resolved"]
               if r.get("resolved_code") and f"4MA1-{r['resolved_code']}" not in store]
    ck("C4 code domain (0 foreign)", not foreign, str(foreign[:4]))

    # C5 top-level
    rep = disk.get("repair") or {}
    hist = disk.get("repair_history") or []
    ck("C5 top-level R6 block + R1 history + clause",
       rep.get("round") == "R6"
       and rep.get("counts_delta", {}).get("corrected") == 8
       and any(h.get("round") == "R1" for h in hist)
       and "T-C42 R6 R1-shaped verdict round over the R4 defect inventory" in disk.get("validation", "")
       and "T-C42 R6 (2026-10-02)" in disk.get("unresolved_allowlist_note", ""))

    # C6 idempotency
    import subprocess as sp
    before = RES_PATH.read_bytes()
    r = sp.run(["python3", str(REPO / "scripts/c42_r6_resolution_repair_apply.py")],
               capture_output=True, text=True)
    after = RES_PATH.read_bytes()
    ck("C6 idempotency (verify-only re-run)", r.returncode == 0 and before == after,
       r.stdout.strip()[-80:])

    # C7 downstream + projection
    proj = yaml.safe_load(OVERRIDES.read_text())
    p_ov = proj["overrides"]
    proj_verd = sorted((o["note_slug"], o["chunk_ordinal"]) for o in p_ov if o["provenance_class"] == "verdicted")
    proj_ext = sorted((o["note_slug"], o["chunk_ordinal"]) for o in p_ov if o["provenance_class"] == "extension")
    want_verd = sorted((k.split("::")[0], int(k.split("::")[1])) for k in sec_ov)
    want_ext = sorted((k.split("::")[0], int(k.split("::")[1])) for k in ext_ov if "::" in k)
    sub_ok = len(proj.get("subsumed_r1_entries") or []) == len(subsumed) == 2
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
    ck("C7 override projection + sme_spcpt_verify (BASE re-pointed)",
       proj_verd == want_verd and proj_ext == want_ext and sub_ok and sp_rc == 0,
       f"spcpt_verify rc={sp_rc} tail={sp_tail}")

    # C8 commit state: the R6 round is committed and git-clean
    st = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                        capture_output=True, text=True).stdout.splitlines()
    dirty = sorted(l[3:].strip() for l in st if l.strip())
    r6_files_clean = not any(RES_GIT in p or "c42_r6" in p or "C42_R6" in p
                             or p == "scripts/c42_section_overrides_r6.yaml" for p in dirty)
    ck("C8 R6 round committed and git-clean", r6_files_clean, str(dirty[:6]))

    print("ALL PASS" if not fails else f"FAILURES: {fails}")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
