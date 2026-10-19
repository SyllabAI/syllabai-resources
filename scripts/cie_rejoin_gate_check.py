#!/usr/bin/env python3
"""T-SPECS-CIE-REJOIN-GATE-1 battery — RJG1..RJG10, fail-closed, exit 0 iff
ALL PASS. Every base comparison reads HEAD blobs via `git show` (the K2
deep-equal discipline: items/codes/pending/totals/anchors byte-preserved).
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/z/my-project/syllabai-resources")
SL = REPO / "spec-links"
REPORTS = REPO / "graph" / "reports"
GATE = "T-SPECS-CIE-REJOIN-GATE-1"
STAMP = "2026-10-20T12:00:00Z"
CHECK_OUT = REPORTS / "T_SPECS_CIE_REJOIN_GATE_1_CHECK.json"
VERIFY_OUT = REPORTS / "T_SPECS_CIE_REJOIN_GATE_1_VERIFY.json"

LANES = [
    "cie-a-level-accounting-21", "cie-a-level-biology-25",
    "cie-a-level-chemistry-25", "cie-a-level-economics-23",
    "cie-a-level-physics-25", "cie-as-environmental-management-20",
    "cie-igcse-biology-23", "cie-igcse-business-23", "cie-igcse-business-25",
    "cie-igcse-chemistry-23", "cie-igcse-computer-science-23",
    "cie-igcse-economics-20", "cie-igcse-geography-20",
    "cie-igcse-geography-25", "cie-igcse-maths-25-core",
    "cie-igcse-maths-25-extended", "cie-igcse-physics-23",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-physics",
    "cie-igcse-science-combined-science-23-biology",
    "cie-igcse-science-combined-science-23-chemistry",
    "cie-igcse-science-combined-science-23-physics",
]
PAYLOAD_KEYS = ["gate", "accepted_utc", "accepted_by", "verification"]
CORE_KEYS = ["items", "codes", "pending", "totals", "anchors"]
PRESERVED_RJ_KEYS = ["lane", "directive", "gateway_trace", "applied_utc",
                     "base_commit", "method", "tiers", "note"]

FAILS: list[str] = []


def ok(cond, label, detail=""):
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}"
          + (f" — {detail}" if detail else ""), flush=True)
    if not cond:
        FAILS.append(label)


def git(*args: str) -> str:
    r = subprocess.run(["git", "-C", str(REPO), *args],
                       capture_output=True, check=True)
    return r.stdout.decode("utf-8", "replace")


def head_json(path: str):
    return json.loads(git("show", f"HEAD:{path}"))


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    import time
    t0 = time.time()
    stats = json.loads((REPORTS / "T_SPECS_CIE_REJOIN_1_STATS.json")
                       .read_text(encoding="utf-8"))
    detail = {d["lane"]: d for d in stats["lanes_detail"]}
    verify = json.loads(VERIFY_OUT.read_text(encoding="utf-8"))

    # ---- RJG1 footprint: pre-commit = exactly 23 modified paths; the
    #      committed-clean (audit) form = 0 modified with the 23 files
    #      blob-identical to HEAD (the audit convention branch)
    out = git("diff", "--name-status", "--no-renames", "HEAD",
              "--", "spec-links/")
    mod = {}
    for line in out.splitlines():
        st, _, p = line.partition("\t")
        mod[p] = st.strip().split()[-1]
    expect = {f"spec-links/{l}.json": "M" for l in LANES}
    expect["spec-links/manifest.json"] = "M"
    if not mod:
        clean_ok = all(
            (REPO / p).read_bytes() ==
            subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{p}"],
                           capture_output=True, check=True).stdout
            for p in expect)
        ok(clean_ok, "RJG1 committed-clean: 0 modified, 23 gate files "
                     "blob-identical to HEAD (audit form)",
           f"{len(expect)} files")
    else:
        ok(mod == expect, "RJG1 footprint == exactly 22 sidecars + manifest",
           f"{len(mod)} paths, statuses {sorted(set(mod.values()))}")

    # ---- RJG2/RJG3 per sidecar
    rj_ok = core_ok = True
    entries_total = 0
    per_lane = {}
    for l in LANES:
        new = json.loads((SL / f"{l}.json").read_text(encoding="utf-8"))
        old = head_json(f"spec-links/{l}.json")
        for k in CORE_KEYS:
            if new.get(k) != old.get(k):
                core_ok = False
                FAILS.append(f"RJG2 {l}: {k} drifted")
        rj_new, rj_old = new["review_state"]["rejoin"], old["review_state"]["rejoin"]
        for k in PRESERVED_RJ_KEYS:
            if rj_new.get(k) != rj_old.get(k):
                rj_ok = False
                FAILS.append(f"RJG3 {l}: rejoin.{k} drifted")
        if rj_new.get("state") != "ACCEPTED" or rj_new.get("gate") != GATE:
            rj_ok = False
            FAILS.append(f"RJG3 {l}: state/gate not promoted")
        for k in PAYLOAD_KEYS:
            if k not in rj_new:
                rj_ok = False
                FAILS.append(f"RJG3 {l}: missing payload key {k}")
        if rj_new.get("accepted_utc") != STAMP:
            rj_ok = False
            FAILS.append(f"RJG3 {l}: stamp drift")
        n = sum(1 for it in new["items"].values()
                for c in (it.get("codes") or [])
                if c.get("method") == "cie_index_rejoin")
        per_lane[l] = n
        entries_total += n
        if n != detail[l]["code_entries_added"]:
            rj_ok = False
            FAILS.append(f"RJG4 {l}: entries {n} != stats "
                         f"{detail[l]['code_entries_added']}")
    ok(core_ok, "RJG2 items/codes/pending/totals/anchors deep-equal vs HEAD "
                "(22 lanes; pendings byte-preserved incl. the 268 recordless)")
    ok(rj_ok, "RJG3 rejoin payload preserved + state ACCEPTED + gate payload")

    # ---- RJG4 census
    ok(entries_total == 2771 == stats["code_entries_added_total"],
       "RJG4 2,771 rejoin code entries recounted", str(entries_total))

    # ---- RJG5 manifest
    m_new = json.loads((SL / "manifest.json").read_text(encoding="utf-8"))
    m_old = head_json("spec-links/manifest.json")
    rjm, rjm_old = m_new["cie_rejoin"], m_old["cie_rejoin"]
    man_ok = (m_new["courses"] == m_old["courses"]
              and all(m_new[k] == m_old[k] for k in
                      ("schema", "generated_utc", "cie_join", "cie_gate",
                       "cie_verdict"))
              and all(rjm[k] == rjm_old[k] for k in
                      ("lane", "applied_utc", "directive", "gateway_trace",
                       "base_commit", "lanes", "resolved_pairs_total",
                       "code_entries_added_total", "tier_policy", "note"))
              and rjm["state"] == "ACCEPTED"
              and all(k in rjm for k in PAYLOAD_KEYS))
    keys = list(m_new.keys())
    ok(man_ok and keys[-1] == "cie_rejoin_gate"
       and keys[:-1] == list(m_old.keys()),
       "RJG5 manifest: rows/legacy blocks deep-equal, cie_rejoin promoted, "
       "cie_rejoin_gate appended LAST (append-only key order)",
       f"keys={keys}")

    # ---- RJG6 verifier reproduction (fresh re-run, byte-identical VERIFY)
    v_before = sha(VERIFY_OUT.read_bytes())
    r = subprocess.run([sys.executable, "scripts/cie_rejoin_gate_verify.py"],
                       capture_output=True, text=True, cwd=REPO, timeout=300)
    v_after = sha(VERIFY_OUT.read_bytes())
    ok(r.returncode == 0 and verify["verdict"] == "PASS"
       and v_before == v_after,
       "RJG6 verifier re-run PASS + VERIFY byte-identical (fixed stamp)",
       f"verified {verify['verified']}/{verify['sheet_verdicts']}")

    # ---- RJG7 idempotence: re-run applier, all 23 files sha-stable
    touched = [f"spec-links/{l}.json" for l in LANES] + ["spec-links/manifest.json"]
    before = {p: sha((REPO / p).read_bytes()) for p in touched}
    r = subprocess.run([sys.executable, "scripts/cie_rejoin_gate_apply.py"],
                       capture_output=True, text=True, cwd=REPO, timeout=300)
    after = {p: sha((REPO / p).read_bytes()) for p in touched}
    ok(r.returncode == 0 and before == after,
       "RJG7 applier re-run byte-identical (idempotence)")

    # ---- RJG8 honesty pins
    amb = sum(json.loads((SL / f"{l}.json").read_text(encoding="utf-8"))
              ["anchors"]["rejoin"]["ambiguous_pairs"] for l in LANES)
    ok(amb == stats["ambiguous_pairs_total"] == 166,
       "RJG8 166 quarantines intact (anchors.rejoin census byte-preserved)")
    ok(stats["stays"]["recordless_no_corpus_record"] == 268
       and verify["ambiguous_stay_quarantined"] == 166,
       "RJG8 268 record-less pairs still pinned pending")

    # ---- RJG9 format discipline
    fmt_ok = True
    for p in touched:
        d = json.loads((REPO / p).read_text(encoding="utf-8"))
        if (REPO / p).read_text(encoding="utf-8") != \
                json.dumps(d, indent=1, ensure_ascii=False) + "\n":
            fmt_ok = False
            FAILS.append(f"RJG9 {p}: serialization drift")
    ok(fmt_ok, "RJG9 round-trip serialization stable (indent=1, no-ascii-"
               "preserve, trailing newline)")

    # ---- RJG10 cross-foot
    vpay = verify
    gate_payload = m_new["cie_rejoin_gate"]["verification"]
    ok(vpay["verified"] == 634 == vpay["sheet_verdicts"]
       and vpay["code_entries_total"] == 2771
       and stats["resolved_pairs_total"] == 634
       and gate_payload == {"pairs": 634, "code_entries": 2771,
                            "verified": 634, "failed": 0,
                            "ambiguous_stay_quarantined": 166},
       "RJG10 cross-foot 634/2,771/166 coherent across sheet, VERIFY, STATS "
       "and the gate payload")

    results = {
        "gate": GATE, "generated_utc": STAMP,
        "verdict": "PASS" if not FAILS else "FAIL",
        "checks": ["RJG1", "RJG2", "RJG3", "RJG4", "RJG5",
                   "RJG6", "RJG7", "RJG8", "RJG9", "RJG10"],
        "fails": FAILS,
        "code_entries_total": entries_total,
        "touched_lanes": len(LANES),
        "elapsed_seconds": round(time.time() - t0, 1),
    }
    CHECK_OUT.write_text(json.dumps(results, ensure_ascii=False, indent=1)
                         + "\n")
    print(f"RESULT: {results['verdict']} "
          f"({10 - len([f for f in FAILS if True])} label fails: {len(FAILS)}) "
          f"exit {'0' if results['verdict'] == 'PASS' else '1'}")
    return 0 if results["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
