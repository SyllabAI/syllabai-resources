#!/usr/bin/env python3
"""
T-SPECS-CIE-GATE-1 — disposition applier (run ONLY after cie_gate_verify.py
verdict PASS): promotes the 44 spec-links/cie-*.json sidecars from SUGGESTED
to ACCEPTED per the operator directive 'review/promotion gate proceed'
(gateway trace 1a150fee04d54d6d, 2026-10-19, zai-web).

Changes ONLY the review_state value of each sidecar (items/codes/pending/
totals/anchors are byte-preserved — enforced afterwards by K2 deep-equal vs
the pre-gate HEAD blobs) and appends the cie_gate block to
spec-links/manifest.json. Idempotent: re-running on ACCEPTED sidecars with
identical gate metadata is a no-op rewrite.

Tier policy (recorded, per AGENT.md rule 1 — authoritative only at the
explicit validation state):
  T1_verbatim  -> authoritative (independently re-verified 3547/3547)
  T2_near      -> accepted-near; NON-authoritative hint (lower-bound audited)
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

REPO = Path("/home/z/my-project/syllabai-resources")
SL = REPO / "spec-links"
GATE = "T-SPECS-CIE-GATE-1"
TRACE = "1a150fee04d54d6d"


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    verify = json.loads((REPO / "graph" / "reports" /
                         "T_SPECS_CIE_GATE_1_VERIFY.json").read_text())
    if verify.get("verdict") != "PASS":
        print(f"REFUSED: verifier verdict = {verify.get('verdict')!r} — "
              "the gate does not promote on a FAIL verdict")
        return 1

    changed = 0
    for f in sorted(SL.glob("cie-*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        rs = d.get("review_state") or {}
        if rs.get("state") == "ACCEPTED" and rs.get("gate") == GATE:
            continue  # already promoted by this gate
        d["review_state"] = {
            "state": "ACCEPTED",
            "lane": "T-SPECS-CIE-JOIN-1",
            "gate": GATE,
            "accepted_utc": stamp,
            "accepted_by": ("operator directive 'review/promotion gate "
                            f"proceed' (gateway trace {TRACE}, 2026-10-19, "
                            "zai-web)"),
            "tier_policy": {
                "T1_verbatim": "authoritative (gate-verified)",
                "T2_near": ("accepted-near; non-authoritative hint "
                            "(lower-bound audited)"),
            },
            "note": ("promoted from SUGGESTED by T-SPECS-CIE-GATE-1 after "
                     "V1 battery + independent V2/V3 re-verification with "
                     "zero defects; items/codes/pending byte-identical to "
                     "the join-lane output; unresolved anchors stay pending "
                     "(AGENT.md rules 1-3)"),
        }
        f.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n",
                     encoding="utf-8")
        changed += 1

    mpath = SL / "manifest.json"
    manifest = json.loads(mpath.read_text(encoding="utf-8"))
    manifest["cie_gate"] = {
        "gate": GATE,
        "state": "ACCEPTED",
        "accepted_utc": stamp,
        "accepted_by": f"operator directive 'review/promotion gate proceed' (gateway trace {TRACE})",
        "lanes": 44,
        "tier_policy": {"T1_verbatim": "authoritative",
                        "T2_near": "accepted-near; non-authoritative hint"},
        "verification": {"v2_t1": verify["v2_t1"], "v3_t2": verify["v3_t2"],
                         "defects": 0},
    }
    mpath.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n",
                     encoding="utf-8")
    print(f"promoted sidecars: {changed}/44; manifest cie_gate block set")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
