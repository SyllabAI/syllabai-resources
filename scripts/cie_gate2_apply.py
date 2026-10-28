#!/usr/bin/env python3
"""T-SPECS-CIE-GATE-2 — disposition applier (runs ONLY after
cie_gate2_verify.py verdict PASS; refuses otherwise).

Promotes the wave-2 AS chain in the 8 sidecars (the REJOIN-GATE-1 shape):
  - review_state.state   SUGGESTED -> ACCEPTED (the JOIN-2 top-level state);
    review_state.gate "pending" -> the gate id; additive acceptance payload
    (accepted_utc / accepted_by / verification) INSIDE the top-level block
  - review_state.rejoin.state  SUGGESTED -> ACCEPTED (7 touched lanes;
    pure-2 carries no rejoin block — honest zero)
  - review_state.verdict.state SUGGESTED -> ACCEPTED (2 touched lanes)
    every pre-existing key byte-preserved; items/codes/pending/totals/
    anchors untouched (enforced by the gate battery's deep-equal)
  - manifest.json: cie_join_wave2as.review_state -> ACCEPTED,
    cie_rejoin_wave2as.state -> ACCEPTED, cie_verdict_wave2as.state ->
    ACCEPTED (each + the same additive keys); NEW top-level
    cie_gate_wave2as block appended LAST (append-only order)

Idempotent: re-running on ACCEPTED sidecars with identical metadata
rewrites byte-identical files (sha256-stable). Fixed stamp for determinism.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/z/my-project/syllabai-resources")
SL = REPO / "spec-links"
GATE = "T-SPECS-CIE-GATE-2"
STAMP = "2026-10-29T14:00:00Z"
TRACE = "1a183e66619bd6dd"
DIRECTIVE = "verdict fills -> review gate -> v2 consume"
BASE_COMMIT = "b97a80c72bcba64546b376746efac76fd7847737"
FIRES = ("T-SPECS-CIE-REJOIN-2 record NEXT #2 / T-SPECS-CIE-VERDICT-2 "
         "record NEXT #2 (the JOIN-2 chain of record, stage #2)")
VERIFY = REPO / "graph" / "reports" / "T_SPECS_CIE_GATE_2_VERIFY.json"

LANES = [
    "cie-as-chemistry-25", "cie-as-physics-25", "cie-as-business-23",
    "cie-as-computer-science-19", "cie-as-maths-20-pure-1",
    "cie-as-maths-20-pure-2", "cie-as-maths-20-mechanics",
    "cie-as-maths-20-probability-and-statistics-1",
]
REJOIN_LANES = [l for l in LANES if l != "cie-as-maths-20-pure-2"]
VERDICT_LANES = ["cie-as-business-23", "cie-as-chemistry-25"]

ACCEPTED_BY = (f"operator directive '{DIRECTIVE}' (gateway trace {TRACE}, "
               "2026-10-29, zai-web)")


def dump(d) -> str:
    return json.dumps(d, indent=1, ensure_ascii=False) + "\n"


def main() -> int:
    verify = json.loads(VERIFY.read_text(encoding="utf-8"))
    if verify.get("verdict") != "PASS":
        print(f"REFUSED: verifier verdict = {verify.get('verdict')!r} — "
              "the gate does not promote on a FAIL verdict")
        return 1
    if verify.get("base_commit") != BASE_COMMIT:
        print(f"REFUSED: verify base {verify.get('base_commit', '')[:12]} != "
              f"gate base {BASE_COMMIT[:12]}")
        return 1

    verification = {
        "pairs": verify["verified"],
        "verified": verify["verified"],
        "failed": verify["failed"],
        "verified_by_class": dict(verify["verified_by_class"]),
        "totals_by_class": dict(verify["totals_by_class"]),
        "ambiguous_stay_quarantined": dict(
            verify["ambiguous_stay_quarantined"]),
        "inherited_dup_items_pinned": verify["inherited_dup_items_pinned"],
    }

    def promote(block: dict, where: str) -> None:
        if block.get("state") == "ACCEPTED" and block.get("gate") == GATE:
            return  # idempotence target: rewrite byte-identical
        if block.get("state") != "SUGGESTED":
            print(f"FAIL {where}: unexpected state {block.get('state')!r}",
                  file=sys.stderr)
            sys.exit(1)
        block["state"] = "ACCEPTED"
        block["gate"] = GATE
        block["accepted_utc"] = STAMP
        block["accepted_by"] = ACCEPTED_BY
        block["verification"] = dict(verification)

    for l in LANES:
        f = SL / f"{l}.json"
        d = json.loads(f.read_text(encoding="utf-8"))
        rs = d.get("review_state") or {}
        if "state" not in rs:
            print(f"FAIL {l}: no top-level review_state", file=sys.stderr)
            return 1
        promote(rs, f"{l}:review_state")
        if l in REJOIN_LANES:
            if "rejoin" not in rs:
                print(f"FAIL {l}: expected rejoin block", file=sys.stderr)
                return 1
            promote(rs["rejoin"], f"{l}:review_state.rejoin")
        if l in VERDICT_LANES:
            if "verdict" not in rs:
                print(f"FAIL {l}: expected verdict block", file=sys.stderr)
                return 1
            promote(rs["verdict"], f"{l}:review_state.verdict")
        f.write_text(dump(d), encoding="utf-8")

    mpath = SL / "manifest.json"
    manifest = json.loads(mpath.read_text(encoding="utf-8"))
    jw = manifest.get("cie_join_wave2as")
    if not isinstance(jw, dict) or "review_state" not in jw:
        print("FAIL manifest: no cie_join_wave2as block", file=sys.stderr)
        return 1
    if jw["review_state"] != "ACCEPTED":
        if jw["review_state"] != "SUGGESTED":
            print(f"FAIL manifest: unexpected join state "
                  f"{jw['review_state']!r}", file=sys.stderr)
            return 1
        jw["review_state"] = "ACCEPTED"
    jw["gate"] = GATE
    jw["accepted_utc"] = STAMP
    jw["accepted_by"] = ACCEPTED_BY
    jw["verification"] = dict(verification)
    for key in ("cie_rejoin_wave2as", "cie_verdict_wave2as"):
        blk = manifest.get(key)
        if not isinstance(blk, dict):
            print(f"FAIL manifest: no {key} block", file=sys.stderr)
            return 1
        promote(blk, f"manifest:{key}")
    manifest["cie_gate_wave2as"] = {
        "gate": GATE,
        "state": "ACCEPTED",
        "accepted_utc": STAMP,
        "accepted_by": ACCEPTED_BY,
        "fires": FIRES,
        "base_commit": BASE_COMMIT,
        "gateway_trace": TRACE,
        "lanes": len(LANES),
        "verification": dict(verification),
        "note": ("the wave-2 AS chain's review/promotion gate (the JOIN-2 "
                 "chain of record stage #2): all 191 resolutions of the "
                 "three classes independently re-fired and verified "
                 "191/191 before promotion (V 18 + J 124 + T2 49); the 609 "
                 "quarantines stay out; items/codes/pending/anchors "
                 "byte-preserved; the 11 inherited REJOIN-2 in-item "
                 "duplicates stay pinned as the disclosed known defect "
                 "(consume dedups per official_id); record-less pairs stay "
                 "pending honestly (AGENT.md rule 3)"),
    }
    mpath.write_text(dump(manifest), encoding="utf-8")

    # stage the promotion (the lane engines' staging pattern)
    for l in LANES:
        subprocess.run(["git", "-C", str(REPO), "add", "--",
                        f"spec-links/{l}.json"], check=True)
    subprocess.run(["git", "-C", str(REPO), "add", "--",
                    "spec-links/manifest.json"], check=True)

    print(f"promoted sidecars: {len(LANES)}/{len(LANES)} "
          f"(rejoin x{len(REJOIN_LANES)}, verdict x{len(VERDICT_LANES)}); "
          f"manifest states -> ACCEPTED; cie_gate_wave2as block appended")
    return 0


if __name__ == "__main__":
    sys.exit(main())
