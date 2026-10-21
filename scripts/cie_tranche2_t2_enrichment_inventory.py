#!/usr/bin/env python3
"""T-SPECS-CIE-TRANCHE2-T2ENRICH-1 — verdict sheet GENERATOR (tranche-2 round-1).

Computes the residual T2_near census fleet-wide (all 44 CIE sidecars) and
emits scripts/cie_tranche2_t2_enrichment_verdicts.yaml — one row per entry,
keyed (lane, item, official_id), with the verbatim prior state recorded.

Fleet census pinned at build time (cross-checked by the battery):
  total 423 = anchored_class 196 (question_part 151 + note 45)
            + t2only_class 227 (question_part 162 + note 65)
  methods: cie_definition_text_join 299 + cie_text_join 124
  lanes: 15
Every promoted (official_id, official_code) pair already exists on the item
as a GATE-1-accepted near entry (tier T2_near) — nothing is invented
(ADR-030); this lane re-tiers existing entries exactly as tranche-1 did.

Read-only on the sidecars; writes ONLY the sheet yaml.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SL = REPO / "spec-links"
SHEET = REPO / "scripts" / "cie_tranche2_t2_enrichment_verdicts.yaml"

LANE_ID = "T-SPECS-CIE-TRANCHE2-T2ENRICH-1"
DIRECTIVE = ("operator order 'Tranche-2' (gateway trace 1a15f8160e677949, "
             "2026-10-22, zai-web) — fires tranche2_verdictProgram of the "
             "anchor-gap census receipt of record "
             "(cie-anchor-gap-census-r0.json): the residual T2_near census "
             "promotion (this sheet) + the per-bank name-phrase verdict "
             "sheet program")

# fleet census of record (computed 2026-10-22 from the sidecars at the lane
# base; cross-checked by cie_tranche2_t2_enrichment_check.py)
PIN_TOTAL = 423
PIN_SPLIT = {"anchored": {"question_part": 151, "note": 45},
             "t2only": {"question_part": 162, "note": 65}}
PIN_METHODS = {"cie_definition_text_join": 299, "cie_text_join": 124}
PIN_LANES = {"cie-a-level-biology-25": 114, "cie-a-level-chemistry-25": 2,
             "cie-a-level-physics-25": 1, "cie-as-environmental-management-20": 21,
             "cie-igcse-biology-23": 3, "cie-igcse-business-23": 20,
             "cie-igcse-chemistry-23": 6, "cie-igcse-computer-science-23": 75,
             "cie-igcse-economics-20": 15, "cie-igcse-geography-20": 78,
             "cie-igcse-physics-23": 39,
             "cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry": 36,
             "cie-igcse-science-combined-science-23-biology": 8,
             "cie-igcse-science-combined-science-23-chemistry": 3,
             "cie-igcse-science-combined-science-23-physics": 2}


def die(msg):
    print(f"ABORT: {msg}", flush=True)
    sys.exit(1)


def main() -> int:
    base_commit = __import__("subprocess").run(
        ["git", "rev-parse", "HEAD"], capture_output=True, text=True,
        cwd=REPO).stdout.strip()

    rows = []
    split = Counter()
    methods = Counter()
    lanes = Counter()
    for f in sorted(SL.glob("cie-*.json")):
        d = json.loads(f.read_text())
        items = d.get("items") or {}
        iters = items.items() if isinstance(items, dict) else ((None, x) for x in items)
        for iid, it in iters:
            if not isinstance(it, dict):
                continue
            codes = it.get("codes") or []
            t2 = [c for c in codes if c.get("tier") == "T2_near"]
            if not t2:
                continue
            other = [c for c in codes if c.get("tier") != "T2_near"]
            cls = "anchored" if other else "t2only"
            for c in t2:
                oid = c.get("official_id")
                ocode = c.get("official_code")
                if not oid or not ocode:
                    die(f"{f.stem}/{iid}: T2 entry missing official_id/official_code")
                prior_method = c.get("method")
                if prior_method not in PIN_METHODS:
                    die(f"{f.stem}/{iid}: prior method {prior_method!r} not in the of-record families")
                rows.append({
                    "lane": f.stem,
                    "item": iid,
                    "kind": it.get("kind"),
                    "cls": cls,
                    "official_id": oid,
                    "official_code": ocode,
                    "spine_code": ocode,
                    "tier": "V6_near_text_verdict",
                    "prior": {"tier": "T2_near", "method": prior_method},
                })
                split[(cls, it.get("kind"))] += 1
                methods[prior_method] += 1
                lanes[f.stem] += 1

    # cross-foot against the pinned fleet census
    total = len(rows)
    if total != PIN_TOTAL:
        die(f"total {total} != pinned {PIN_TOTAL}")
    for cls, kinds in PIN_SPLIT.items():
        for k, n in kinds.items():
            if split[(cls, k)] != n:
                die(f"split {(cls, k)} = {split[(cls, k)]} != pinned {n}")
    if dict(methods) != PIN_METHODS:
        die(f"methods {dict(methods)} != pinned {PIN_METHODS}")
    if dict(lanes) != PIN_LANES:
        die(f"lanes {dict(lanes)} != pinned {PIN_LANES}")

    sheet = {
        "lane": LANE_ID,
        "generated_utc": "2026-10-22T05:00:00Z",
        "directive": DIRECTIVE,
        "base_commit": base_commit,
        "header": (
            "Tranche-2 round-1 — the residual T2_near census promoted to the V* "
            "authoritative class, fleet-wide (44 CIE sidecars, 15 lanes with T2 "
            "residue). Every row re-tiers an EXISTING GATE-1-accepted near entry "
            "(tier T2_near -> V6_near_text_verdict, method cie_*_text_join -> "
            "operator_verdict, prior recorded verbatim). cls=anchored rows are "
            "items that ALSO carry non-T2 authoritative codes (the census "
            "receipt's tranche-2-scope enrichment — no gap movement); cls=t2only "
            "rows are items whose ONLY codes are the near entries (162 part "
            "entries in 8 lanes the census receipt's tranche-1 queue did not "
            "cover — the census receipt's queue figure 155/161 stays "
            "historical-of-record; the fleet T2 census of record is THIS sheet, "
            "computed) plus 65 note entries (the census receipt's notes-axis "
            "scope). No code invented (ADR-030); no join re-derived; pending "
            "anchors untouched."),
        "fleet_census": {
            "total": total,
            "by_class_kind": {f"{cls}.{k}": n for (cls, k), n in sorted(split.items())},
            "by_method": dict(sorted(methods.items())),
            "by_lane": dict(sorted(lanes.items())),
        },
        "verdicts": rows,
    }
    SHEET.write_text(yaml.safe_dump(sheet, sort_keys=False, allow_unicode=True,
                                    width=100))
    print(f"sheet written: {SHEET.name} rows={total}")
    print(f"  cls/kind: {dict(split)}")
    print(f"  lanes: {len(lanes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
