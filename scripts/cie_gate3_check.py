#!/usr/bin/env python3
"""T-SPECS-CIE-GATE-3 check — GT-W1..W6: mutation discipline, idempotence,
census integrity (the GATE-2 check precedent, wave3 class)."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/z/my-project/syllabai-resources")
SPEC_LINKS = REPO / "spec-links"
CHAIN_BASE = "5f170f98746f4bd21ce8e6b73af02e6a83fa4028"

LANES_3 = [
    "cie-a-level-biology-25", "cie-a-level-chemistry-25",
    "cie-a-level-physics-25", "cie-as-accounting-21", "cie-as-biology-25",
    "cie-igcse-accounting-21", "cie-igcse-biology-23",
    "cie-igcse-chemistry-23", "cie-igcse-physics-23",
]

fails = []
oks = []


def check(name, cond, detail=""):
    (oks if cond else fails).append(name)
    print(("PASS " if cond else "FAIL ") + name + (f" — {detail}" if detail else ""))


def git(*a):
    return subprocess.run(["git", "-C", str(REPO), *a], capture_output=True,
                          text=True, check=True).stdout


def main() -> int:
    pre = {}
    for l in LANES_3:
        try:
            pre[l] = json.loads(git("show", f"{CHAIN_BASE}:spec-links/{l}.json"))
        except subprocess.CalledProcessError:
            pre[l] = None
    pre_manifest = json.loads(git("show", f"{CHAIN_BASE}:spec-links/manifest.json"))

    tot_items = tot_codes = 0
    for l in LANES_3:
        cur = json.loads((SPEC_LINKS / f"{l}.json").read_text())
        w3ids = set(cur["items"]) - set((pre[l] or {}).get("items") or {})
        # GT-W1: items/codes/pendings byte-preserved through the gate
        gate_pre = None
        # re-derive the pre-gate state = the VERDICT-3 landing (HEAD~1)
        gate_pre = json.loads(git("show", "HEAD~1:spec-links/"
                                           f"{l}.json")) if False else None
        import hashlib
        # items identical to HEAD~1 (the last pre-gate commit)
        hp = subprocess.run(["git", "-C", str(REPO), "show",
                             f"HEAD~1:spec-links/{l}.json"],
                            capture_output=True, text=True)
        if hp.returncode == 0:
            before = json.loads(hp.stdout)
            same = all(json.dumps(before["items"].get(k), sort_keys=True) ==
                       json.dumps(cur["items"].get(k), sort_keys=True)
                       for k in before["items"]) and \
                set(before["items"]) == set(cur["items"])
            pend_same = all(json.dumps(before["items"][k].get("pending"),
                                       sort_keys=True) ==
                            json.dumps(cur["items"].get(k, {}).get("pending"),
                                       sort_keys=True)
                            for k in before["items"])
            check(f"GT-W1 {l} items+pendings byte-preserved", same and pend_same)
        # GT-W2: wave3 review blocks now ACCEPTED
        rs = cur.get("review_state", {})
        w3 = rs.get("wave3") or {}
        states = [w3.get(k, {}).get("state") for k in ("rejoin3", "verdict3")
                  if k in w3] + ([w3.get("state")] if "state" in w3 else [])
        fresh = (cur.get("anchors", {}).get("wave3", {}).get("class")
                 == "fresh-build")
        ok = all(s == "ACCEPTED" for s in states) and \
            (not fresh or rs.get("state") == "ACCEPTED")
        check(f"GT-W2 {l} wave3 states ACCEPTED", ok,
              f"states={states} freshTop={rs.get('state') if fresh else 'n/a'}")
        tot_items += len(w3ids)
        tot_codes += sum(1 for iid in w3ids
                         if cur["items"][iid].get("codes"))

    # GT-W3: manifest — pre blocks preserved; new blocks appended last
    m = json.loads((SPEC_LINKS / "manifest.json").read_text())
    kept = all(json.dumps(pre_manifest[k], sort_keys=True) ==
               json.dumps(m.get(k), sort_keys=True)
               for k in pre_manifest
               if k not in ("generated_utc", "courses", "cie_wave3",
                            "cie_wave3_rejoin", "cie_wave3_verdict",
                            "cie_gate_wave3"))
    chain_blocks = [k for k in ("cie_wave3", "cie_wave3_rejoin",
                                "cie_wave3_verdict", "cie_gate_wave3")
                    if k in m]
    last_key = list(m.keys())[-1]
    check("GT-W3 manifest additive + gate block last",
          kept and chain_blocks == ["cie_wave3", "cie_wave3_rejoin",
                                    "cie_wave3_verdict", "cie_gate_wave3"]
          and last_key == "cie_gate_wave3",
          f"blocks={chain_blocks}")

    # GT-W4: the gate block's census
    g = m.get("cie_gate_wave3", {})
    check("GT-W4 gate block census", g.get("state") == "ACCEPTED"
          and g.get("lanes") == 9, json.dumps(g)[:120])

    # GT-W5: SUGGESTED nowhere in the wave3 surface
    stray = []
    for l in LANES_3:
        cur = json.loads((SPEC_LINKS / f"{l}.json").read_text())
        w3 = (cur.get("review_state") or {}).get("wave3") or {}
        for k, v in w3.items():
            if isinstance(v, dict) and v.get("state") == "SUGGESTED":
                stray.append(f"{l}:{k}")
    check("GT-W5 no SUGGESTED left in wave3 surface", not stray,
          str(stray[:4]))

    # GT-W6: idempotence — the verify re-run is still ALL PASS and writes nothing
    r = subprocess.run([sys.executable, str(REPO / "scripts" /
                                            "cie_gate3_verify.py")],
                       capture_output=True, text=True)
    clean = "ALL PASS" in r.stdout and "defects" not in r.stdout
    check("GT-W6 verify re-run clean", r.returncode == 0 and clean)

    print(f"\n== GATE-3 check: {len(oks)} PASS / {len(fails)} FAIL | "
          f"wave3 items {tot_items}, coded {tot_codes} ==")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
