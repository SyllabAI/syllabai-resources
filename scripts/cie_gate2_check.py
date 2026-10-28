#!/usr/bin/env python3
"""
T-SPECS-CIE-GATE-2 battery — GT1-GT7 for the wave-2 AS review/promotion
gate. The base state is read from HEAD (the VERDICT-2 landing b97a80c72,
pre-gate); the staged promotion is never trusted as its own input.

Output: graph/reports/T_SPECS_CIE_GATE_2_CHECK.json; exit 0 iff ALL PASS.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "graph" / "reports" / "T_SPECS_CIE_GATE_2_CHECK.json"
GATE = "T-SPECS-CIE-GATE-2"
BASE = "b97a80c72bcba64546b376746efac76fd7847737"
LANES = [
    "cie-as-chemistry-25", "cie-as-physics-25", "cie-as-business-23",
    "cie-as-computer-science-19", "cie-as-maths-20-pure-1",
    "cie-as-maths-20-pure-2", "cie-as-maths-20-mechanics",
    "cie-as-maths-20-probability-and-statistics-1",
]
REJOIN_LANES = [l for l in LANES if l != "cie-as-maths-20-pure-2"]
VERDICT_LANES = ["cie-as-business-23", "cie-as-chemistry-25"]
DECLARED = ({f"spec-links/{l}.json" for l in LANES}
            | {"spec-links/manifest.json",
               "scripts/cie_gate2_verify.py",
               "scripts/cie_gate2_apply.py",
               "scripts/cie_gate2_check.py",
               "graph/reports/T_SPECS_CIE_GATE_2_RECORD.md",
               "graph/reports/T_SPECS_CIE_GATE_2_VERIFY.json",
               "graph/reports/T_SPECS_CIE_GATE_2_CHECK.json"})

results: list[dict] = []


def check(cid: str, fn) -> None:
    try:
        detail = fn()
        results.append({"id": cid, "pass": True, "detail": detail})
        print(f"GT{cid} PASS: {detail}")
    except AssertionError as exc:
        results.append({"id": cid, "pass": False, "detail": str(exc)})
        print(f"GT{cid} FAIL: {exc}")


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def base_json(path: str):
    return json.loads(subprocess.run(
        ["git", "-C", str(REPO), "show", f"{BASE}:{path}"],
        capture_output=True, check=True).stdout.decode("utf-8"))


def staged_bytes(path: str) -> bytes:
    ls = subprocess.run(["git", "-C", str(REPO), "ls-files", "-s", "--", path],
                        capture_output=True, check=True).stdout.decode().split()
    if len(ls) < 2:
        raise AssertionError(f"{path} not in index")
    return subprocess.run(["git", "-C", str(REPO), "cat-file", "-p", ls[1]],
                          capture_output=True, check=True).stdout


VERIFY = json.loads((REPO / "graph" / "reports"
                     / "T_SPECS_CIE_GATE_2_VERIFY.json").read_text())
STAGED = {l: json.loads(staged_bytes(f"spec-links/{l}.json")) for l in LANES}
BASED = {l: base_json(f"spec-links/{l}.json") for l in LANES}
VKEYS = ("gate", "accepted_utc", "accepted_by", "verification")


def gt1() -> str:
    require(VERIFY["verdict"] == "PASS", "verifier verdict != PASS")
    require(VERIFY["base_commit"] == BASE, "verify base != gate base")
    require(VERIFY["verified"] == 191 and VERIFY["failed"] == 0,
            "verify counters")
    require(VERIFY["verified_by_class"] == {"V": 18, "J": 124, "T2": 49},
            "verify class counters")
    return (f"verifier PASS precondition: 191/191 verified "
            f"(V 18 + J 124 + T2 49), base {BASE[:12]}")


def gt2() -> str:
    def chk_block(bh: dict, bn: dict, path: str,
                  skip: tuple = ("state", "gate")) -> None:
        require(list(bn.keys()) == list(bh.keys())
                + [x for x in VKEYS if x not in bh],
                f"{path} keys")
        for kk in bh:
            if kk in skip:
                continue
            require(bn[kk] == bh[kk], f"{path}.{kk} drifted")
        require(bn["state"] == "ACCEPTED", f"{path} state")
        require(bn.get("gate") == GATE, f"{path} gate id")

    for l in LANES:
        h, n = BASED[l], STAGED[l]
        require(list(n.keys()) == list(h.keys()), f"{l} top keys")
        for k in ("schema", "generated_utc", "course", "qual", "board",
                  "registry", "items", "totals", "anchors"):
            require(n[k] == h[k], f"{l} {k} drifted (gate must touch ONLY "
                                  "review_state)")
        # the rejoin/verdict sub-blocks gain their own acceptance keys —
        # excluded here, checked by their own chk_block calls below
        chk_block(h["review_state"], n["review_state"],
                  f"{l} review_state",
                  skip=("state", "gate", "rejoin", "verdict"))
        for blk in ("rejoin", "verdict"):
            if blk in h["review_state"]:
                chk_block(h["review_state"][blk],
                          n["review_state"][blk],
                          f"{l} review_state.{blk}")
    return ("mutation discipline: items/codes/pending/totals/anchors "
            "deep-equal to the base; only review_state (+ its rejoin/"
            "verdict blocks) promoted with additive acceptance keys")


def gt3() -> str:
    ver = VERIFY
    for l in LANES:
        rs = STAGED[l]["review_state"]
        require(rs["state"] == "ACCEPTED", f"{l} state")
        require(rs["gate"] == GATE, f"{l} gate id")
        require(rs["accepted_utc"] and TRACE_TAG in rs["accepted_by"],
                f"{l} accepted_by trace")
        require(rs["verification"]["pairs"] == ver["verified"],
                f"{l} verification payload")
        if l in REJOIN_LANES:
            require(rs["rejoin"]["state"] == "ACCEPTED"
                    and rs["rejoin"]["gate"] == GATE,
                    f"{l} rejoin promotion")
        else:
            require("rejoin" not in rs, f"{l} unexpected rejoin")
        if l in VERDICT_LANES:
            require(rs["verdict"]["state"] == "ACCEPTED"
                    and rs["verdict"]["gate"] == GATE,
                    f"{l} verdict promotion")
        else:
            require("verdict" not in rs, f"{l} unexpected verdict")
    return (f"8/8 sidecars promoted (rejoin x{len(REJOIN_LANES)}, verdict "
            f"x{len(VERDICT_LANES)}); acceptance payload consistent with "
            f"the verifier")


TRACE_TAG = "1a183e66619bd6dd"


def gt4() -> str:
    m = base_json("spec-links/manifest.json")
    nm = json.loads(staged_bytes("spec-links/manifest.json"))
    require(list(nm.keys()) == list(m.keys()) + ["cie_gate_wave2as"],
            "manifest top keys (additive, appended last)")
    for key in ("cie_join_wave2as", "cie_rejoin_wave2as",
                "cie_verdict_wave2as"):
        blk, nb = m[key], nm[key]
        st = "review_state" if key == "cie_join_wave2as" else "state"
        require(nb[st] == "ACCEPTED", f"{key} {st}")
        for k in blk:
            if k == st:
                continue
            require(nb[k] == blk[k], f"{key}.{k} drifted")
    g = nm["cie_gate_wave2as"]
    require(g["gate"] == GATE and g["state"] == "ACCEPTED"
            and g["lanes"] == 8 and g["base_commit"] == BASE,
            "cie_gate_wave2as block")
    for row_l, row in m["courses"].items():
        require(nm["courses"][row_l] == row, f"course row {row_l} drifted")
    return ("manifest discipline: three chain blocks -> ACCEPTED, all "
            "pre-existing blocks/rows deep-equal, cie_gate_wave2as "
            "appended last")


def gt5() -> str:
    st = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                        capture_output=True, check=True).stdout.decode()
    seen = {line[3:].strip().strip('"') for line in st.splitlines()}
    extra = sorted(seen - DECLARED)
    require(not extra, f"undeclared paths: {extra[:8]}")
    delta = subprocess.run(
        ["git", "-C", str(REPO), "diff", BASE, "--name-only", "--",
         "spec-links/"], capture_output=True, check=True
    ).stdout.decode().splitlines()
    require(set(delta) == {f"spec-links/{l}.json" for l in LANES}
            | {"spec-links/manifest.json"},
            f"spec-links delta != 8 sidecars + manifest: "
            f"{sorted(set(delta))[:6]}")
    for guard in ("SME-ExamQuestion/", "SME-RevisionNotes/",
                  "Official-Specifications/", "SME-Flashcards/"):
        bad = [p for p in seen if p.startswith(guard)]
        require(not bad, f"{guard} touched: {bad[:5]}")
    return (f"footprint {len(seen)} paths subset-of declared; spec-links "
            f"delta == 8 sidecars + manifest; guards intact")


def gt6() -> str:
    before = {l: hashlib.sha256(
        staged_bytes(f"spec-links/{l}.json")).hexdigest() for l in LANES}
    before_m = hashlib.sha256(
        staged_bytes("spec-links/manifest.json")).hexdigest()
    r = subprocess.run([sys.executable,
                        str(REPO / "scripts" / "cie_gate2_apply.py")],
                       capture_output=True, text=True)
    require(r.returncode == 0, f"apply re-run failed: {r.stderr[-300:]}")
    for l in LANES:
        require(hashlib.sha256(
            staged_bytes(f"spec-links/{l}.json")).hexdigest() == before[l],
            f"{l} re-run byte drift")
    require(hashlib.sha256(
        staged_bytes("spec-links/manifest.json")).hexdigest() == before_m,
        "manifest re-run drift")
    return ("apply idempotence: re-run byte-identical "
            "(8 sidecars + manifest, sha256)")


def gt7() -> str:
    def codes(d):
        c = {}
        for it in d["items"].values():
            for x in (it.get("codes") or []):
                c[(x.get("method"), x.get("tier"))] = \
                    c.get((x.get("method"), x.get("tier")), 0) + 1
        return c
    for l in LANES:
        require(codes(STAGED[l]) == codes(BASED[l]),
                f"{l} codes census drifted (gate touches no codes)")
        require(sum(len(it.get("pending") or [])
                    for it in STAGED[l]["items"].values())
                == sum(len(it.get("pending") or [])
                       for it in BASED[l]["items"].values()),
                f"{l} pending census drifted")
    total_codes = sum(sum(codes(STAGED[l]).values()) for l in LANES)
    require(total_codes == 1759, f"total codes {total_codes} != 1759")
    dup = 0
    for l in LANES:
        for it in STAGED[l]["items"].values():
            ids = [c.get("official_id") for c in (it.get("codes") or [])
                   if c.get("method") == "cie_index_rejoin_wave2as"]
            if len(ids) != len(set(ids)):
                dup += 1
    require(dup == 11, f"inherited dup census {dup} != 11")
    return ("cross-foots: codes census unchanged through the gate "
            f"({total_codes} entries; dup census still 11 — the disclosed "
            "REJOIN-2 known defect, consume dedups)")


check("1", gt1)
check("2", gt2)
check("3", gt3)
check("4", gt4)
check("5", gt5)
check("6", gt6)
check("7", gt7)

all_pass = all(r["pass"] for r in results)
OUT.write_text(json.dumps({
    "battery": "T-SPECS-CIE-GATE-2",
    "all_pass": all_pass,
    "checks": results,
}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"\nALL {'PASS' if all_pass else 'FAIL'} "
      f"({sum(r['pass'] for r in results)}/{len(results)})")
return_value = 0 if all_pass else 1
sys.exit(return_value)
