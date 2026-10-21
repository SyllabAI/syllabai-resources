#!/usr/bin/env python3
"""
T-SPECS-CIE-TRANCHE2-T2ENRICH-1 — operator-verdict fill engine (tranche-2
round-1).

Fires tranche2_verdictProgram of the anchor-gap census receipt of record
(.syllabai/receipts/CIE-INTEGRATION/cie-anchor-gap-census-r0.json) on the
operator's order 'Tranche-2' (gateway trace 1a15f8160e677949, 2026-10-22,
zai-web).

What this lane does (and ONLY this):
  The residual T2_near census fleet-wide — 423 entries in 15 of the 44 CIE
  sidecars (313 question_part + 110 note entries; 196 on items that ALSO
  carry non-T2 authoritative codes [the census receipt's tranche-2-scope
  enrichment], 227 on items whose ONLY codes are the near entries). Each
  sheet row re-tiers that EXISTING sidecar entry:

      tier:   T2_near            ->  V6_near_text_verdict
      method: cie_*_text_join    ->  operator_verdict

  No code is invented (ADR-030): every promoted (official_id, official_code)
  pair is byte-verified to already exist on the item as an accepted-near
  entry AND in the lane's parsed registry. No join is re-derived. No pending
  anchor is touched. The gate's ACCEPTED state and provenance are preserved;
  the tranche blocks are ADDITIVE (AGENT.md rules 1-4).

The V6 class (the tranche-1 class, same grounds):
  V6_near_text_verdict — the operator ratifies a GATE-1-audited accepted-near
  text join as authoritative for this item (the T2 tier was audited 584/584
  lower-bound with zero defects; tranche-1 promoted the census receipt's
  155-part queue on the same grounds; this round retires the RESIDUAL T2
  census — the census receipt's own tranche-2 scope, fleet-wide). Prior
  method recorded verbatim per row in the sheet.

Deterministic: fixed stamp, sorted iteration, in-place field replacement
(codes[] order preserved), byte-idempotent re-run (one-way: a re-run after
apply aborts).

Usage:
  python3 cie_tranche2_t2_enrichment_fill.py            # validate + apply + emit
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SL = REPO / "spec-links"
REPORTS = REPO / "graph" / "reports"
SHEET = REPO / "scripts" / "cie_tranche2_t2_enrichment_verdicts.yaml"

LANE_ID = "T-SPECS-CIE-TRANCHE2-T2ENRICH-1"
STAMP = "2026-10-22T05:30:00Z"
DIRECTIVE = ("operator order 'Tranche-2' (gateway trace 1a15f8160e677949, "
             "2026-10-22, zai-web) — fires tranche2_verdictProgram of the "
             "anchor-gap census receipt of record "
             "(cie-anchor-gap-census-r0.json)")
NEW_TIER = "V6_near_text_verdict"
NEW_METHOD = "operator_verdict"
PRIOR_TIER = "T2_near"
PRIOR_METHODS = ("cie_definition_text_join", "cie_text_join")
TIER_SEMANTICS = ("authoritative (operator ratifies the GATE-1-audited accepted-near "
                  "text join for this item; prior method recorded verbatim in the "
                  "verdict sheet)")

PIN_TOTAL = 423
PIN_SPLIT = {("t2only", "note"): 65, ("anchored", "note"): 45,
             ("anchored", "question_part"): 151, ("t2only", "question_part"): 162}


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
    if len(rows) != PIN_TOTAL:
        die(f"sheet rows {len(rows)} != {PIN_TOTAL}")
    seen = set()
    split = {}
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
        if r.get("kind") not in ("question_part", "note"):
            die(f"{k}: kind {r.get('kind')!r}")
        if r.get("cls") not in ("anchored", "t2only"):
            die(f"{k}: cls {r.get('cls')!r}")
        if not r.get("spine_code"):
            die(f"{k}: missing spine_code")
        ck = (r["cls"], r["kind"])
        split[ck] = split.get(ck, 0) + 1
    if split != PIN_SPLIT:
        die(f"sheet class/kind split {split} != pinned {PIN_SPLIT}")

    per_lane_rows = {}
    for r in rows:
        per_lane_rows.setdefault(r["lane"], []).append(r)

    # ---------------- fail-closed validation against base state -------------
    errors = []
    for lane, lrows in sorted(per_lane_rows.items()):
        d = json.loads((SL / f"{lane}.json").read_text())
        if (d.get("review_state") or {}).get("state") != "ACCEPTED":
            errors.append(f"{lane}: sidecar not ACCEPTED")
        items = d["items"]
        id2code = registry_points(d["registry"]["id"])
        for r in lrows:
            k = (lane, r["item"], r["official_id"])
            it = items.get(r["item"])
            if it is None or it.get("kind") != r["kind"]:
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
        # class guards
        for iid in {r["item"] for r in lrows}:
            entries = items[iid].get("codes") or []
            rcls = next(r["cls"] for r in lrows if r["item"] == iid)
            has_other = any(e.get("tier") != PRIOR_TIER for e in entries)
            if rcls == "anchored" and not has_other:
                errors.append(f"{lane}/{iid}: cls=anchored but no non-T2 code present")
            if rcls == "t2only" and has_other:
                errors.append(f"{lane}/{iid}: cls=t2only but non-T2 code present")
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

        # residual T2 guard: zero T2_near entries may remain in this lane
        for iid, it in items.items():
            if isinstance(it, dict) and any(
                    e.get("tier") == PRIOR_TIER for e in (it.get("codes") or [])):
                die(f"{lane}: residual {PRIOR_TIER} entry on {iid} after apply")

        # totals recompute + UNCHANGED assertion (every promoted item already
        # carried the T2 entries inside codes[] — the coded-item set is
        # invariant under re-tier by construction). A PRE-EXISTING drift in an
        # inherited base (the T-SPECS-CIE-COMPLETE-1 V7 lane left business-23's
        # totals stale: stored coded_by_kind.notes 34 vs recomputed 70) is
        # CORRECTED here, provably attributed: the drift delta must equal
        # EXACTLY the count of items whose ONLY codes are V7_agent_note_join
        # entries — anything else aborts hard.
        t = d["totals"]
        by = {"notes": 0, "question_parts": 0, "flashcards": 0}
        coded = {"notes": 0, "question_parts": 0, "flashcards": 0}
        v7_only = 0
        for it in items.values():
            by[it["kind"] + "s"] += 1
            cs = it["codes"]
            coded[it["kind"] + "s"] += 1 if cs else 0
            if cs and all(e.get("tier", "").startswith("V7") for e in cs):
                v7_only += 1
        new_items_with_codes = sum(coded.values())
        stored_with_codes = t["items_with_codes"]
        if stored_with_codes != new_items_with_codes:
            delta = new_items_with_codes - stored_with_codes
            if delta > 0 and delta == v7_only:
                print(f"NOTE {lane}: correcting inherited totals drift "
                      f"({stored_with_codes} -> {new_items_with_codes}, "
                      f"delta == V7-only items {v7_only}, the COMPLETE-1 lane's "
                      f"stale counters) — disclosed in the tranche-2 record",
                      flush=True)
            else:
                die(f"{lane}: totals drift ({stored_with_codes} vs "
                    f"{new_items_with_codes}) not attributable to V7-only items "
                    f"({v7_only}) — hard abort")
        if (t["items"], t["by_kind"]) != (sum(by.values()), by):
            die(f"{lane}: totals items/by_kind drift (structural law violated)")
        t["items_with_codes"] = new_items_with_codes
        t["by_kind"] = by
        t["coded_by_kind"] = coded

        # additive blocks (provenance preserved; nothing pre-existing rewritten)
        n_items = len({r["item"] for r in lrows})
        d["anchors"]["tranche2"] = {
            "lane": LANE_ID, "applied_utc": STAMP,
            "promoted_entries": promoted_entries,
            "promoted_items": n_items,
            "scope": ("the residual T2_near census fleet-wide (this lane's share); "
                      "pending anchors untouched; the T2_near class retires "
                      "fleet-wide with this round"),
        }
        rs = d["review_state"]
        rs["tranche2"] = {
            "lane": LANE_ID, "directive": DIRECTIVE, "applied_utc": STAMP,
            "base_commit": sheet["base_commit"],
            "method": NEW_METHOD, "tier": NEW_TIER,
            "tier_semantics": TIER_SEMANTICS,
            "items": n_items, "entries": promoted_entries,
            "note": ("tranche-2 round-1 of the anchor-gap completion program: the "
                     "residual T2_near census promoted to the V* authoritative "
                     "class (the census receipt's tranche-2 scope, fleet-wide); "
                     "no code invented (ADR-030), no join re-derived, the gate's "
                     "ACCEPTED state and provenance preserved; pending anchors "
                     "untouched"),
        }
        (SL / f"{lane}.json").write_text(
            json.dumps(d, indent=1, ensure_ascii=False) + "\n")
        fill_summary[lane] = {
            "promoted_items": n_items,
            "promoted_entries": promoted_entries,
        }

    # ---------------- manifest (additive blocks; pre-existing values intact) -
    mpath = SL / "manifest.json"
    manifest = json.loads(mpath.read_text())
    for lane, s in fill_summary.items():
        row = manifest["courses"].get(lane)
        if row is None:
            die(f"manifest row missing for {lane}")
        row["tranche2"] = {
            "lane": LANE_ID, "promoted_items": s["promoted_items"],
            "promoted_entries": s["promoted_entries"],
        }
    manifest["cie_tranche2"] = {
        "lane": LANE_ID, "applied_utc": STAMP, "directive": DIRECTIVE,
        "base_commit": sheet["base_commit"],
        "lanes": len(fill_summary),
        "promoted_items_total": sum(s["promoted_items"] for s in fill_summary.values()),
        "promoted_entries_total": sum(s["promoted_entries"] for s in fill_summary.values()),
        "tier_policy": {NEW_TIER: TIER_SEMANTICS},
        "note": ("tranche-2 round-1 operator verdicts: the residual T2_near census "
                 "fleet-wide promoted to the V* authoritative class; the T2_near "
                 "class retires fleet-wide; the VERDICT-1 acceptance states and "
                 "gate provenance are preserved"),
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
        "sheet": "scripts/cie_tranche2_t2_enrichment_verdicts.yaml",
        "fleet_census": {
            "residual_t2_total": PIN_TOTAL,
            "class_split": {f"{cls}.{kind}": n for (cls, kind), n in sorted(PIN_SPLIT.items())},
            "census_receipt_disclosure_reconciliation": (
                "total 423 == the post-tranche-1 t2Hints census of record EXACT "
                "(584 - 161 promoted by tranche-1); notes 110 == the census "
                "receipt's '~110 T2 hint entries' EXACT; anchored-class part "
                "entries 151 on 284-disclosed-parts' entry-count basis (the "
                "census receipt's '~284 parts' was approximate and "
                "parts-vs-entries conflated — this sheet's figures are the "
                "computed census)"),
            "census_queue_hole_disclosure": (
                "162 t2only question_part entries in 8 lanes (env-mgmt-20 8 / "
                "biology-23 2 / business-23 5 / chemistry-23 4 / cs-23 48 / "
                "economics-20 10 / geography-20 62 / physics-23 23) were NOT in "
                "the census receipt's tranche-1 queue (155 parts / 161 entries / "
                "9 lanes) although they carry the same GATE-1-accepted near "
                "evidence and sit in the v2 maps as t2HintCodes on codes-empty "
                "items (map hint arithmetic 313 == 151 + 162 EXACT per lane). "
                "The census receipt's queue figures stay historical-of-record "
                "(append-only); the fleet T2 census of record is THIS sheet"),
        },
        "expected_landing": {
            "gap_movement": ("cls=t2only question_part promotions (162 entries) "
                             "anchor their parts — the expQ re-pin after the "
                             "consume re-run is the of-record number (computed, "
                             "never transcribed); anchored-class and note "
                             "promotions do not move the question census (the "
                             "notes axis gains its accepted-near codes)"),
            "t2_class_retirement": "zero T2_near entries remain fleet-wide (battery-pinned)",
        },
        "lanes": fill_summary,
    }
    (REPORTS / "T_SPECS_CIE_TRANCHE2_R1_FILL.json").write_text(
        json.dumps(machine, indent=1, ensure_ascii=False) + "\n")

    tot_i = sum(s["promoted_items"] for s in fill_summary.values())
    tot_e = sum(s["promoted_entries"] for s in fill_summary.values())
    print(f"LANES {len(fill_summary)}  promoted_items {tot_i}  promoted_entries {tot_e}")
    for lane, s in fill_summary.items():
        print(f"  {lane:64s} items={s['promoted_items']:3d} entries={s['promoted_entries']:3d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
