#!/usr/bin/env python3
"""T-SPECS-CIE-REJOIN-GATE-1 — disposition applier (runs ONLY after
cie_rejoin_gate_verify.py verdict PASS; refuses otherwise).

Promotes the REJOIN-1 resolutions in the 22 touched sidecars:
  - review_state.rejoin.state  SUGGESTED -> ACCEPTED
  - additive acceptance payload INSIDE the rejoin block:
    gate / accepted_utc / accepted_by / verification
    (every pre-existing rejoin key byte-preserved; items/codes/pending/
     totals/anchors untouched — enforced by the RJG battery's deep-equal)
  - manifest.json: cie_rejoin.state -> ACCEPTED + the same additive keys;
    NEW top-level cie_rejoin_gate block appended LAST (append-only order)

Idempotent: re-running on ACCEPTED sidecars with identical metadata rewrites
byte-identical files (sha256-stable). Fixed stamp for determinism.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path("/home/z/my-project/syllabai-resources")
SL = REPO / "spec-links"
GATE = "T-SPECS-CIE-REJOIN-GATE-1"
STAMP = "2026-10-20T12:00:00Z"
TRACE = "1a155ee451def291"
DIRECTIVE = "re-join against the index, further re-gates"
BASE_COMMIT = "0fe5f77210f74aaeb3f6c491dfe0263d12db738c"
VERIFY = REPO / "graph" / "reports" / "T_SPECS_CIE_REJOIN_GATE_1_VERIFY.json"

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

ACCEPTED_BY = (f"operator directive '{DIRECTIVE}' (gateway trace {TRACE}, "
               "2026-10-20, zai-web)")


def dump(d) -> str:
    return json.dumps(d, indent=1, ensure_ascii=False) + "\n"


def main() -> int:
    verify = json.loads(VERIFY.read_text(encoding="utf-8"))
    if verify.get("verdict") != "PASS":
        print(f"REFUSED: verifier verdict = {verify.get('verdict')!r} — "
              "the gate does not promote on a FAIL verdict")
        return 1

    verification = {
        "pairs": verify["verified"],
        "code_entries": verify["code_entries_total"],
        "verified": verify["verified"],
        "failed": verify["failed"],
        "ambiguous_stay_quarantined": verify["ambiguous_stay_quarantined"],
    }

    changed = 0
    for l in LANES:
        f = SL / f"{l}.json"
        d = json.loads(f.read_text(encoding="utf-8"))
        rs = d.get("review_state") or {}
        rj = rs.get("rejoin")
        if not isinstance(rj, dict):
            print(f"FAIL {l}: no review_state.rejoin block", file=sys.stderr)
            return 1
        if rj.get("state") == "ACCEPTED" and rj.get("gate") == GATE:
            # idempotence target: rewrite byte-identical
            pass
        elif rj.get("state") != "SUGGESTED":
            print(f"FAIL {l}: unexpected rejoin state {rj.get('state')!r}",
                  file=sys.stderr)
            return 1
        rj["state"] = "ACCEPTED"
        rj["gate"] = GATE
        rj["accepted_utc"] = STAMP
        rj["accepted_by"] = ACCEPTED_BY
        rj["verification"] = dict(verification)
        f.write_text(dump(d), encoding="utf-8")
        changed += 1

    mpath = SL / "manifest.json"
    manifest = json.loads(mpath.read_text(encoding="utf-8"))
    rj = manifest.get("cie_rejoin")
    if not isinstance(rj, dict):
        print("FAIL manifest: no cie_rejoin block", file=sys.stderr)
        return 1
    rj["state"] = "ACCEPTED"
    rj["gate"] = GATE
    rj["accepted_utc"] = STAMP
    rj["accepted_by"] = ACCEPTED_BY
    rj["verification"] = dict(verification)
    manifest["cie_rejoin_gate"] = {
        "gate": GATE,
        "state": "ACCEPTED",
        "accepted_utc": STAMP,
        "accepted_by": ACCEPTED_BY,
        "fires": "T-SPECS-CIE-REJOIN-1 record NEXT #1",
        "base_commit": BASE_COMMIT,
        "gateway_trace": TRACE,
        "lanes": len(LANES),
        "tier_policy": dict(rj["tier_policy"]),
        "verification": dict(verification),
        "note": ("the R41-shaped re-gate of the re-join chain (REJOIN-1 "
                 "NEXT #1): all 634 identity-grade resolutions independently "
                 "re-fired and verified 634/634 before promotion; the 166 "
                 "quarantines stay out; items/codes/pending/anchors "
                 "byte-preserved (K2 deep-equal); record-less pairs stay "
                 "pending honestly (AGENT.md rule 3)"),
    }
    mpath.write_text(dump(manifest), encoding="utf-8")

    print(f"promoted sidecars: {changed}/{len(LANES)}; "
          f"manifest cie_rejoin state -> ACCEPTED; "
          f"cie_rejoin_gate block appended")
    return 0


if __name__ == "__main__":
    sys.exit(main())
