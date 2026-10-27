#!/usr/bin/env python3
"""
T-SPECS-CIE-TRANCHE1-T2NEAR-1 — operator-verdict fill engine (tranche-1).

Fires tranche1_t2NearVerdicts of the anchor-gap census receipt of record
(.syllabai/receipts/CIE-INTEGRATION/cie-anchor-gap-census-r0.json) on the
operator's order 'tranche-1' (gateway trace 1a15e4200e6af579, 2026-10-21,
zai-web).

What this lane does (and ONLY this):
  The census receipt's tranche-1 queue — 155 unanchored question_part items
  (codes[] empty on the committed maps) whose sole join state is the
  GATE-1-accepted near hint carried as items[].t2HintCodes (161 entries).
  Each sheet row re-tiers that EXISTING sidecar entry:

      tier:   T2_near            ->  V6_near_text_verdict
      method: cie_*_text_join    ->  operator_verdict

  No code is invented (ADR-030): every promoted (official_id, official_code)
  pair is byte-verified to already exist on the item as an accepted-near
  entry AND in the lane's parsed registry. No join is re-derived. No pending
  anchor is touched. The gate's ACCEPTED state and provenance are preserved;
  the tranche blocks are ADDITIVE (AGENT.md rules 1-4).

The V6 class (disclosed, additive to the VERDICT-1 ladder V1-V5):
  V6_near_text_verdict — the operator ratifies a GATE-1-audited accepted-near
  text join as authoritative for this item (the T2 tier was audited 584/584
  lower-bound with zero defects; the census receipt proved the t2HintCodes
  law end-to-end). Prior method recorded verbatim per row in the sheet.

Deterministic: fixed stamp, sorted iteration, in-place field replacement
(codes[] order preserved), byte-idempotent re-run.

Usage:
  python3 cie_tranche1_t2near_fill.py            # validate + apply + emit
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SL = REPO / "spec-links"
REPORTS = REPO / "graph" / "reports"
SHEET = REPO / "scripts" / "cie_tranche1_t2near_verdicts.yaml"

LANE_ID = "T-SPECS-CIE-TRANCHE1-T2NEAR-1"
STAMP = "2026-10-21T12:40:00Z"
DIRECTIVE = ("operator order 'tranche-1' (gateway trace 1a15e4200e6af579, 2026-10-21, "
             "zai-web) — fires tranche1_t2NearVerdicts of the anchor-gap census "
             "receipt of record (cie-anchor-gap-census-r0.json)")
NEW_TIER = "V6_near_text_verdict"
NEW_METHOD = "operator_verdict"
PRIOR_TIER = "T2_near"
PRIOR_METHODS = ("cie_definition_text_join", "cie_text_join")
TIER_SEMANTICS = ("authoritative (operator ratifies the GATE-1-audited accepted-near "
                  "text join for this item; prior method recorded verbatim in the "
                  "verdict sheet)")

# the receipt queue of record (cross-foot target; computed by
# scripts/tranche1_inventory_r0.py lane-side, both cross-foots GREEN)
RECEIPT_QUEUE = {
    "cie-a-level-biology-25": 37,
    "cie-a-level-chemistry-25": 25,
    "cie-a-level-physics-25": 15,
    "cie-igcse-business-23": 41,
    "cie-igcse-computer-science-23": 6,
    "cie-igcse-physics-23": 7,
    "cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry": 15,
    "cie-igcse-science-combined-science-23-biology": 6,
    "cie-igcse-science-combined-science-23-chemistry": 3,
}
RECEIPT_PARTS = 155
RECEIPT_ENTRIES = 161


def die(msg):
    print(f"ABORT: {msg}", flush=True)
    sys.exit(1)


def registry_points(qual: str) -> dict:
    man = json.loads((REPO / "Official-Specifications" / "manifest.json").read_text())
    for q in man["qualifications"]:
        if q["slug"] == qual:
            pdf = Path(q["pdf"]).stem
            reg = json.loads(
                (REPO / "Official-Specifications" / "parsed" / qual / f"{pdf}.parsed.json")
                .read_text())
            return {p["id"]: str(p.get("official_code")) for p in reg["spec_points"]}
    die(f"qual {qual} not in manifest")


def main() -> int:
    sheet = yaml.safe_load(SHEET.read_text())
    rows = sheet["verdicts"]

    # ---------------- sheet shape ------------------------------------------
    if sheet.get("lane") != LANE_ID:
        die(f"sheet lane {sheet.get('lane')!r} != {LANE_ID}")
    if len(rows) != RECEIPT_ENTRIES:
        die(f"sheet rows {len(rows)} != {RECEIPT_ENTRIES}")
    seen = set()
    for r in rows:
        k = (r["lane"], r["item"], r["official_id"])
        if k in seen:
            die(f"duplicate sheet key {k}")
        seen.add(k)
        if r.get("tier") != NEW_TIER:
            die(f"{k}: sheet tier {r.get('tier')!r}")
        if r.get("prior", {}).get("tier") != PRIOR_TIER:
            die(f"{k}: prior tier {r.get('prior', {}).get('tier')!r}")
        if r.get("prior", {}).get("method") not in PRIOR_METHODS:
            die(f"{k}: prior method {r.get('prior', {}).get('method')!r}")
        if not r.get("spine_code"):
            die(f"{k}: missing spine_code")

    per_lane_rows = {}
    for r in rows:
        per_lane_rows.setdefault(r["lane"], []).append(r)
    if set(per_lane_rows) != set(RECEIPT_QUEUE):
        die(f"sheet lanes {sorted(per_lane_rows)} != receipt queue lanes")

    # ---------------- fail-closed validation against base state -------------
    errors = []
    for lane, lrows in sorted(per_lane_rows.items()):
        d = json.loads((SL / f"{lane}.json").read_text())
        if (d.get("review_state") or {}).get("state") != "ACCEPTED":
            errors.append(f"{lane}: sidecar not ACCEPTED")
        items = d["items"]
        id2code = registry_points(d["registry"]["id"])
        parts = {r["item"] for r in lrows}
        if len(parts) != RECEIPT_QUEUE[lane]:
            errors.append(f"{lane}: parts {len(parts)} != receipt {RECEIPT_QUEUE[lane]}")
        for r in lrows:
            k = (lane, r["item"], r["official_id"])
            it = items.get(r["item"])
            if it is None or it.get("kind") != "question_part":
                errors.append(f"{k}: item missing or kind drift")
                continue
            entries = it.get("codes") or []
            hit = [e for e in entries
                   if e.get("official_id") == r["official_id"]
                   and e.get("official_code") == r["official_code"]
                   and e.get("tier") == PRIOR_TIER
                   and e.get("method") == r["prior"]["method"]]
            if len(hit) != 1:
                errors.append(f"{k}: expected exactly 1 {PRIOR_TIER} entry, found {len(hit)}")
                continue
            if id2code.get(r["official_id"]) != r["official_code"]:
                errors.append(f"{k}: registry mismatch")
        # queue-definition guard: no non-T2 codes on any queued item
        for iid in parts:
            if any(e.get("tier") != PRIOR_TIER for e in (items[iid].get("codes") or [])):
                errors.append(f"{lane}/{iid}: non-{PRIOR_TIER} code present (queue def violated)")
    if errors:
        for e in errors:
            print("FAIL-CLOSED:", e, flush=True)
        return 1

    # ---------------- apply (in-place re-tier; codes[] order preserved) -----
    fill_summary = {}
    for lane, lrows in sorted(per_lane_rows.items()):
        d = json.loads((SL / f"{lane}.json").read_text())
        items = d["items"]
        promoted_entries = 0
        for r in lrows:
            it = items[r["item"]]
            for e in it["codes"]:
                if (e.get("official_id") == r["official_id"]
                        and e.get("official_code") == r["official_code"]
                        and e.get("tier") == PRIOR_TIER
                        and e.get("method") == r["prior"]["method"]):
                    e["tier"] = NEW_TIER
                    e["method"] = NEW_METHOD
                    promoted_entries += 1
        if promoted_entries != len(lrows):
            die(f"{lane}: promoted {promoted_entries} != sheet rows {len(lrows)}")

        # totals recompute + UNCHANGED assertion (these items were already
        # counted as coded — the T2 entries lived in codes[] pre-promotion)
        t = d["totals"]
        by = {"notes": 0, "question_parts": 0, "flashcards": 0}
        coded = {"notes": 0, "question_parts": 0, "flashcards": 0}
        for it in items.values():
            by[it["kind"] + "s"] += 1
            coded[it["kind"] + "s"] += 1 if it["codes"] else 0
        new_items_with_codes = sum(coded.values())
        if (t["items"], t["items_with_codes"], t["by_kind"], t["coded_by_kind"]) != \
           (sum(by.values()), new_items_with_codes, by, coded):
            die(f"{lane}: totals drift under recompute (structural law violated)")
        t["by_kind"] = by
        t["coded_by_kind"] = coded

        # additive blocks (provenance preserved; nothing pre-existing rewritten)
        n_parts = len({r["item"] for r in lrows})
        d["anchors"]["tranche1"] = {
            "lane": LANE_ID, "applied_utc": STAMP,
            "promoted_entries": promoted_entries,
            "promoted_parts": n_parts,
            "scope": ("question_part items whose codes[] were T2_near-only "
                      "(the anchor-gap census receipt's tranche-1 queue); "
                      "pending anchors untouched"),
        }
        rs = d["review_state"]
        rs["tranche1"] = {
            "lane": LANE_ID, "directive": DIRECTIVE, "applied_utc": STAMP,
            "base_commit": sheet["base_commit"],
            "method": NEW_METHOD, "tier": NEW_TIER,
            "tier_semantics": TIER_SEMANTICS,
            "parts": n_parts, "entries": promoted_entries,
            "note": ("tranche-1 of the anchor-gap completion program: the 155-part "
                     "T2_near review queue promoted to the V* authoritative class; "
                     "no code invented (ADR-030), no join re-derived, the gate's "
                     "ACCEPTED state and provenance preserved; pending anchors and "
                     "the notes/flashcards axis untouched"),
        }
        (SL / f"{lane}.json").write_text(
            json.dumps(d, indent=1, ensure_ascii=False) + "\n")
        fill_summary[lane] = {
            "promoted_parts": len({r["item"] for r in lrows}),
            "promoted_entries": promoted_entries,
        }

    # ---------------- manifest (additive blocks; pre-existing values intact) -
    mpath = SL / "manifest.json"
    manifest = json.loads(mpath.read_text())
    for lane, s in fill_summary.items():
        row = manifest["courses"].get(lane)
        if row is None:
            die(f"manifest row missing for {lane}")
        row["tranche1"] = {
            "lane": LANE_ID, "promoted_parts": s["promoted_parts"],
            "promoted_entries": s["promoted_entries"],
        }
    manifest["cie_tranche1"] = {
        "lane": LANE_ID, "applied_utc": STAMP, "directive": DIRECTIVE,
        "base_commit": sheet["base_commit"],
        "lanes": len(fill_summary),
        "promoted_parts_total": sum(s["promoted_parts"] for s in fill_summary.values()),
        "promoted_entries_total": sum(s["promoted_entries"] for s in fill_summary.values()),
        "tier_policy": {NEW_TIER: TIER_SEMANTICS},
        "note": ("tranche-1 operator verdicts: the anchor-gap census receipt's 155-part "
                 "T2_near review queue promoted to the V* authoritative class; the "
                 "VERDICT-1 acceptance states and gate provenance are preserved"),
    }
    mpath.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")

    # ---------------- machine record ----------------------------------------
    machine = {
        "lane": LANE_ID, "generated_utc": STAMP, "directive": DIRECTIVE,
        "base_commit": sheet["base_commit"],
        "method": NEW_METHOD, "tier": NEW_TIER,
        "tier_semantics": TIER_SEMANTICS,
        "prior_methods": sorted(PRIOR_METHODS),
        "receipt_of_record": ".syllabai/receipts/CIE-INTEGRATION/cie-anchor-gap-census-r0.json",
        "sheet": "scripts/cie_tranche1_t2near_verdicts.yaml",
        "expected_landing": {
            "question_level_closure_prediction": 116,
            "note": ("distinct fully-unmapped parent questions of the 155 parts, "
                     "computed lane-side from the committed bundles; the census "
                     "re-pin after the consume re-run is the of-record number"),
        },
        "lanes": fill_summary,
    }
    (REPORTS / "T_SPECS_CIE_TRANCHE1_T2NEAR_FILL.json").write_text(
        json.dumps(machine, indent=1, ensure_ascii=False) + "\n")

    tot_p = sum(s["promoted_parts"] for s in fill_summary.values())
    tot_e = sum(s["promoted_entries"] for s in fill_summary.values())
    print(f"LANES {len(fill_summary)}  promoted_parts {tot_p}  promoted_entries {tot_e}")
    for lane, s in fill_summary.items():
        print(f"  {lane:64s} parts={s['promoted_parts']:3d} entries={s['promoted_entries']:3d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
