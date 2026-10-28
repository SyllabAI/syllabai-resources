#!/usr/bin/env python3
"""
T-SPECS-CIE-JOIN-2 — CIE wave-2 AS sidecar lane (the SME-WAVE2 r1 residual:
"the T-SPECS-CIE-JOIN sidecar lane" for the 8-bank anchor gap; operator order
gateway trace 1a180022cd3b552d).

Builds the learner spec-links sidecars `spec-links/cie-as-*.json` for the 8
wave-2 AS banks that serve zero spec anchors at the v2 census (as-biology-25
already serves 789 via the spine rekey ladder; as-accounting-21 is the honest
EQ stub — both outside this lane's order):

    cie-as-chemistry-25                      (9701-2025-2027)
    cie-as-physics-25                        (9702-2025-2027)
    cie-as-business-23                       (9609-2023-2025)
    cie-as-computer-science-19               (9618, parse 2024-2025)
    cie-as-maths-20-pure-1                   (9709-2023-2025)
    cie-as-maths-20-pure-2                   (9709-2023-2025)
    cie-as-maths-20-mechanics                (9709-2023-2025)
    cie-as-maths-20-probability-and-statistics-1 (9709-2023-2025)

Mechanism: EXACTLY the T-SPECS-CIE-JOIN-1 deterministic text join
(scripts/cie_spec_join.py — universe from the notes' embedded spec_point
blocks; candidates from the SME Cambridge path numbering; T1_verbatim /
T2_near text confirmation; pending otherwise, never invented), with ONE new
law — the AS scope law, sourced from the parsed registries' own printed
markers (the same basis as the SME-WAVE2 spine build scope_eq rules):

  - chemistry-25 / physics-25 / business-23: candidates restricted to the
    parse's `AS Level`-scoped points (204/356, 145/303, 62/116);
  - computer-science-19: the parse marks ONLY topics 13-20 `A Level`
    (66 rows); topics 1-12 are the shared AS & A Level content — the
    `A Level`-marked points are EXCLUDED, scope-less points retained (161);
  - the 9709 maths lanes: the registry carries no scope marks — no filter,
    mirroring the JOIN-1 semantics for the same qualification (the 9709
    component law is a spine-build law, not a sidecar-join law).

The SME substrate is name-only for these lanes (definitions null corpus-wide,
index harvest H4-verified) — the honest expectation is the JOIN-1 baseline:
a small T2 subsection-head yield and pending anchors carried verbatim.
Closure continues through the established operator-keyed chain of record
(index rejoin J1-J4 identity classes -> verdict fills -> review gate ->
v2 consume), exactly as the 44 evolved.

Outputs: 8 sidecars (review_state SUGGESTED, lane T-SPECS-CIE-JOIN-2, gate
pending) + spec-links/manifest.json (8 rows appended + additive
`cie_join_wave2as` block; every pre-existing row value-identical — hard
guard). Nothing else is touched.

Usage: python3 scripts/cie_spec_join_wave2as.py [--stamp <UTC>] [--lanes a,b,...]
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cie_spec_join as base  # the JOIN-1 machinery of record

REPO = base.REPO
SPEC_LINKS = base.SPEC_LINKS
LANE_2 = "T-SPECS-CIE-JOIN-2"

LANES_2 = [
    "cie-as-chemistry-25",
    "cie-as-physics-25",
    "cie-as-business-23",
    "cie-as-computer-science-19",
    "cie-as-maths-20-pure-1",
    "cie-as-maths-20-pure-2",
    "cie-as-maths-20-mechanics",
    "cie-as-maths-20-probability-and-statistics-1",
]

SCOPE_AS_ONLY = {"cie-as-chemistry-25", "cie-as-physics-25", "cie-as-business-23"}
SCOPE_DROP_ALEVEL = {"cie-as-computer-science-19"}


def scope_law_note(lane: str, full: int, kept: int) -> dict:
    if lane in SCOPE_AS_ONLY:
        return {
            "law": "candidates restricted to the parse's own 'AS Level'-scoped points "
                   "(the SME-WAVE2 spine build scope_eq basis)",
            "registry_points": full,
            "lane_points": kept,
        }
    if lane in SCOPE_DROP_ALEVEL:
        return {
            "law": "parse marks ONLY topics 13-20 'A Level'; topics 1-12 are the shared "
                   "AS & A Level content — 'A Level'-marked points excluded, scope-less retained",
            "registry_points": full,
            "lane_points": kept,
        }
    return {
        "law": "registry carries no scope marks — no filter (JOIN-1 semantics for this "
               "qualification; the 9709 component law is a spine-build law)",
        "registry_points": full,
        "lane_points": kept,
    }


def apply_scope(lane: str, reg: base.Registry) -> tuple:
    full = len(reg.points)
    if lane in SCOPE_AS_ONLY:
        reg.points = [p for p in reg.points if p.get("scope") == "AS Level"]
    elif lane in SCOPE_DROP_ALEVEL:
        reg.points = [p for p in reg.points if p.get("scope") != "A Level"]
    reg.by_id = {p["id"]: p for p in reg.points}
    return full, len(reg.points)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stamp", default=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    ap.add_argument("--lanes", default="")
    args = ap.parse_args()

    lane_to_qual, quals = base.load_manifest()
    lanes = list(LANES_2)
    if args.lanes:
        want = {x.strip() for x in args.lanes.split(",") if x.strip()}
        lanes = [l for l in lanes if l in want]
        unknown = want - set(LANES_2)
        if unknown:
            sys.exit(f"FATAL: unknown lanes for this lane class: {sorted(unknown)}")

    files = base.ls_tree()
    mpath = SPEC_LINKS / "manifest.json"
    manifest = json.loads(mpath.read_text(encoding="utf-8"))
    pre_courses = json.loads(json.dumps(manifest.get("courses", {})))
    pre_blocks = {k: v for k, v in manifest.items()
                  if k not in ("courses", "generated_utc")}

    tot = {}
    for lane in lanes:
        # idempotent re-runs rewrite this lane's OWN rows/files byte-identically
        # (the -1 contract); every row outside LANES_2 is guarded at the end.
        qual = quals[lane_to_qual[lane]]
        reg = base.Registry(qual)
        full, kept = apply_scope(lane, reg)
        if lane in SCOPE_AS_ONLY and kept == full:
            sys.exit(f"FATAL: scope law reduced nothing for {lane} — law not applied?")
        b = base.lane_bundle(lane, qual, reg, files, args.stamp)
        # registry block carries the FULL registry truth; the lane subset is
        # disclosed in the additive anchors.scope_law block
        b["registry"]["official_points"] = full
        b["anchors"]["scope_law"] = scope_law_note(lane, full, kept)
        b["review_state"] = {
            "state": "SUGGESTED",
            "lane": LANE_2,
            "gate": "pending",
            "note": "agent-generated mapping (AGENT.md rule 2); not authoritative "
                    "until the review/promotion gate accepts; unresolved anchors "
                    "stay pending (rule 3); AS scope law per the parse's printed "
                    "markers (SME-WAVE2 spine basis)",
        }
        (SPEC_LINKS / f"{lane}.json").write_text(
            json.dumps(b, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        manifest["courses"][lane] = {"qual": b["qual"], **b["totals"]}
        t = b["totals"]
        print(f"[{lane}] items={t['items']} coded={t['items_with_codes']} "
              f"(notes {t['coded_by_kind']['notes']}/{t['by_kind']['notes']}, "
              f"parts {t['coded_by_kind']['question_parts']}/{t['by_kind']['question_parts']}) "
              f"universe={b['anchors']['universe_ids']} "
              f"resolved={b['anchors']['universe_resolved']} "
              f"pending_refs={b['anchors']['pending_refs']}", flush=True)
        for k, v in t["by_kind"].items():
            tot[k] = tot.get(k, 0) + v
            tot[k + "_coded"] = tot.get(k + "_coded", 0) + t["coded_by_kind"][k]
        tot["items"] = tot.get("items", 0) + t["items"]
        tot["items_with_codes"] = tot.get("items_with_codes", 0) + t["items_with_codes"]

    manifest["generated_utc"] = args.stamp
    manifest["cie_join_wave2as"] = {
        "lane": LANE_2,
        "review_state": "SUGGESTED",
        # the class block describes the LANE CLASS (8 banks), never the
        # --lanes subset of the last invocation — subset re-runs (battery
        # J10) must leave this block value-identical
        "lanes": len(LANES_2),
        "scope_law": "parse-printed markers: AS Level-only (chem/phys/business), "
                     "A-Level-marked excluded (cs-19), unscoped (9709 maths x4)",
    }
    mpath.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n",
                     encoding="utf-8")

    changed = [k for k, v in pre_courses.items() if manifest["courses"].get(k) != v]
    drifted = [k for k, v in pre_blocks.items() if manifest.get(k) != v]
    print(f"TOTAL items={tot.get('items', 0)} coded={tot.get('items_with_codes', 0)} | "
          f"notes {tot.get('notes_coded', 0)}/{tot.get('notes', 0)}, "
          f"parts {tot.get('question_parts_coded', 0)}/{tot.get('question_parts', 0)} | "
          f"pre_existing_rows_changed={len(changed)} blocks_drifted={len(drifted)}")
    if changed:
        print("FATAL: pre-existing manifest rows changed:", changed)
        return 1
    if drifted:
        print("FATAL: pre-existing manifest blocks drifted:", drifted)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
