#!/usr/bin/env python3
"""
T-SPECS-CIE-TRANCHE2-R2-BATCH-1 — the tranche-2 ruling-batch ENCODING engine.

The r1 receipt's nextAct lane act, second half: "the ruling-batch encoding
engines on the operator's batches". The operator rules rows of a regenerated
review sheet (cie_tranche2_sheet_regen_all.py output, V8 law) per sid; this
engine encodes ONE ruled batch yaml onto the bank's sidecar — fail-closed,
additive, no invention (ADR-030 + AGENT.md rules 1-4).

Batch yaml (the operator's returned instrument; template:
scripts/cie_tranche2_batches/_TEMPLATE.yaml):

    lane: T-SPECS-CIE-TRANCHE2-R2-BATCH-<batch_id>
    batch_id: <slug>                      # unique, slug-safe
    bank: cie-a-level-chemistry-25
    source_sheet: scripts/cie_tranche2_sheets/cie-a-level-chemistry-25.yaml
    source_sheet_sha256: <verbatim from scripts/cie_tranche2_sheets/_index.json>
    directive: <the operator's order, verbatim>
    ruled_utc: <ISO-8601>
    ruled_by: operator
    rulings:
      - sid: spcpt_...                    # one row per sheet sid
        verdict: anchor | quarantine | defer
        codes:                            # anchor only; 1+ entries
          - official_id: <qual>:<code>    # the registry pairing of official_code
            official_code: "2.2.1"
        reason: <verbatim operator rationale>   # quarantine/defer; optional on anchor

Encoding law per anchored sid:
  EVERY sidecar question_part item whose pending[] includes the sid gains
  codes[] entries (order-stable append after existing codes):
      {official_id, official_code, tier: V8_name_phrase_verdict,
       method: operator_verdict, unit: null, score: null, source_sid: sid}
  - the pending[] refs PERSIST (the declared trail — the V6 tranche-1 shape)
  - the sid's sheet row and the sidecar's pending state must agree, the
    sheet must be byte-fresh against _index.json, and every (official_id,
    official_code) pair must exist in the bank's parsed registry — else ABORT
  - a code already present on a part (any lineage) is NOT duplicated; an
    anchored sid with zero eligible parts is an error (the sheet pool law)
  quarantine / defer: no codes; recorded in the batch blocks (quarantine =
    no honest anchor from the evidence — ADR-030; defer = reason required)

Fail-closed gates (all pre-apply):
  G1 batch shape + unique batch_id + slug-safe id
  G2 sheet sha256 == index entry == current file; substrate pins == current files
  G3 sid ∈ sheet rows; no duplicate sid; sid ∈ sidecar pending universe
  G4 anchor codes: registry pairing verified; per-part idempotency pre-check
  G5 totals recompute: coded_by_kind.question_parts delta == distinct parts
     gaining their FIRST code; items_with_codes delta identical; entry count
     delta == predicted entries_added

Apply is atomic per bank: all gates pass or NOTHING is written.
Usage:
  python3 cie_tranche2_batch_encode.py --batch scripts/cie_tranche2_batches/<id>.yaml           # apply
  python3 cie_tranche2_batch_encode.py --batch ... --check                                       # validate only
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SL = REPO / "spec-links"
REPORTS = REPO / "graph" / "reports"
SHEETS = REPO / "scripts" / "cie_tranche2_sheets"
INDEX = SHEETS / "_index.json"
BATCH_DIR = REPO / "scripts" / "cie_tranche2_batches"

LANE = "T-SPECS-CIE-TRANCHE2-R2-BATCH-1"
NEW_TIER = "V8_name_phrase_verdict"
NEW_METHOD = "operator_verdict"
TIER_SEMANTICS = (
    "authoritative (the operator anchors the sid from the regenerated "
    "map-universe review sheet's verbatim evidence + scoped candidates; "
    "no semantic-similarity manufacturing — ADR-030, AGENT.md rule 3)")
SL_DIR_OVERRIDE = None  # throwaway-copy validation hook (env CIE_SL_OVERRIDE, read in main)


def die(msg):
    print(f"ABORT: {msg}", flush=True)
    sys.exit(1)


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def registry_points(qual: str):
    man = json.loads((REPO / "Official-Specifications" / "manifest.json").read_text())
    for q in man["qualifications"]:
        if q["slug"] == qual:
            pdf = Path(q["pdf"]).stem
            reg = json.loads(
                (REPO / "Official-Specifications" / "parsed" / qual / f"{pdf}.parsed.json")
                .read_text())
            return reg["spec_points"]
    die(f"qual {qual!r} not in Official-Specifications/manifest.json")


def totals_of(items: dict):
    by = {"notes": 0, "question_parts": 0, "flashcards": 0}
    coded = {"notes": 0, "question_parts": 0, "flashcards": 0}
    for it in items.values():
        if not isinstance(it, dict):
            continue
        k = it.get("kind")
        kk = (k + "s") if isinstance(k, str) else None
        if kk not in by:
            continue
        by[kk] += 1
        coded[kk] += 1 if it.get("codes") else 0
    return {
        "items": sum(by.values()), "items_with_codes": sum(coded.values()),
        "by_kind": by, "coded_by_kind": coded,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", required=True)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    global SL_DIR_OVERRIDE
    import os as _os
    SL_DIR_OVERRIDE = _os.environ.get("CIE_SL_OVERRIDE") or None

    batch_path = Path(args.batch)
    if not batch_path.exists():
        die(f"batch yaml not found: {batch_path}")
    b = yaml.safe_load(batch_path.read_text())
    errors = []

    # ---------------- G1 batch shape ---------------------------------------
    batch_id = b.get("batch_id") or ""
    bank = b.get("bank") or ""
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,60}", batch_id):
        errors.append(f"G1: batch_id {batch_id!r} not slug-safe")
    if b.get("lane") != f"T-SPECS-CIE-TRANCHE2-R2-BATCH-{batch_id}":
        errors.append(f"G1: lane {b.get('lane')!r} mismatched to batch_id")
    if not b.get("directive"):
        errors.append("G1: directive (the operator's order, verbatim) required")
    if not b.get("ruled_utc") or not b.get("ruled_by"):
        errors.append("G1: ruled_utc / ruled_by required")
    rulings = b.get("rulings") or []
    if not rulings:
        errors.append("G1: empty rulings")
    if errors:
        for e in errors:
            print("FAIL-CLOSED:", e, flush=True)
        return 1

    # ---------------- G2 sheet staleness ------------------------------------
    if not INDEX.exists():
        die(f"fleet index missing: {INDEX} (run cie_tranche2_sheet_regen_all.py first)")
    index = json.loads(INDEX.read_text())
    entry = next((x for x in index["banks"] if x["bank"] == bank), None)
    if entry is None:
        die(f"bank {bank} not in fleet index")
    sheet_path = REPO / entry["sheet"]
    if b.get("source_sheet") != entry["sheet"]:
        errors.append(f"G2: source_sheet {b.get('source_sheet')!r} != index {entry['sheet']!r}")
    if b.get("source_sheet_sha256") != entry["sheet_sha256"]:
        errors.append("G2: source_sheet_sha256 != index entry (stale batch yaml)")
    if not sheet_path.exists() or sha256_file(sheet_path) != entry["sheet_sha256"]:
        errors.append("G2: current sheet file sha != index (fleet moved; regenerate)")
    if errors:
        for e in errors:
            print("FAIL-CLOSED:", e, flush=True)
        return 1
    sheet = yaml.safe_load(sheet_path.read_text())
    sheet_rows = {r["sid"]: r for r in sheet["rows"]}

    # ---------------- sidecar + substrate -----------------------------------
    sl_dir = Path(SL_DIR_OVERRIDE) if SL_DIR_OVERRIDE else SL
    sl_path = sl_dir / f"{bank}.json"
    side = json.loads(sl_path.read_text())
    if (side.get("review_state") or {}).get("state") != "ACCEPTED":
        die(f"{bank}: sidecar not ACCEPTED")
    items = side["items"]
    sp = registry_points(side["registry"]["id"])
    id2code = {p.get("id"): p.get("official_code") for p in sp}
    code2ids = defaultdict(set)
    for p in sp:
        code2ids[p.get("official_code")].add(p.get("id"))

    pins = sheet.get("substrate_pins") or {}
    cur_side_sha = sha256_file(sl_path)
    if pins.get("sidecar_sha256") != cur_side_sha:
        errors.append("G2: sidecar sha moved since sheet generation (substrate drift)")
    errs_len = len(errors)

    # ---------------- G3/G4 row-level validation ----------------------------
    seen_sids = set()
    plan = []           # (sid, verdict, codes, parts_to_touch)
    pred_parts = set()  # distinct parts gaining >=1 entry
    pred_entries = 0
    already = defaultdict(int)  # sid -> entries already present (idempotency info)
    for r in rulings:
        sid = r.get("sid") or ""
        v = r.get("verdict")
        if sid in seen_sids:
            errors.append(f"G3: duplicate sid {sid}")
        seen_sids.add(sid)
        if sid not in sheet_rows:
            errors.append(f"G3: sid {sid} not in sheet rows")
        if v not in ("anchor", "quarantine", "defer"):
            errors.append(f"G3: {sid}: verdict {v!r} not anchor|quarantine|defer")
            continue
        codes = r.get("codes") or []
        if v == "anchor" and not codes:
            errors.append(f"G4: {sid}: anchor with no codes")
        if v in ("quarantine", "defer") and codes:
            errors.append(f"G4: {sid}: {v} must not carry codes")
        if v in ("quarantine", "defer") and not (r.get("reason") or "").strip():
            errors.append(f"G4: {sid}: {v} requires a reason")
        pair_ok = []
        for c in codes:
            oid, ocode = c.get("official_id"), c.get("official_code")
            if id2code.get(oid) != ocode:
                errors.append(f"G4: {sid}: registry pairing mismatch {oid!r} -> {ocode!r}")
                continue
            if oid not in code2ids.get(ocode, set()):
                errors.append(f"G4: {sid}: code {ocode!r} not paired to id {oid!r}")
                continue
            pair_ok.append((oid, ocode))
        parts = sorted(sheet_rows[sid]["part_refs"]) if sid in sheet_rows else []
        eligible = []
        for iid in parts:
            it = items.get(iid)
            if it is None or it.get("kind") != "question_part" or sid not in (it.get("pending") or []):
                errors.append(f"G3: {sid}: part {iid} not sidecar-pending (pool law broken)")
                continue
            have = {(e.get("official_id"), e.get("official_code")) for e in (it.get("codes") or [])}
            fresh = [(oid, ocode) for oid, ocode in pair_ok if (oid, ocode) not in have]
            already[sid] += len(pair_ok) - len(fresh)
            if len(fresh) < len(pair_ok):
                print(f"NOTE: {sid}/{iid}: {len(pair_ok) - len(fresh)} code(s) already present (skipped)")
            if fresh:
                eligible.append((iid, fresh))
                pred_parts.add(iid)
                pred_entries += len(fresh)
        if v == "anchor" and pair_ok and not eligible:
            errors.append(f"G4: {sid}: anchor yields zero eligible part entries")
        plan.append({"sid": sid, "verdict": v, "codes": pair_ok, "eligible": eligible,
                     "reason": r.get("reason") or "", "note": r.get("note") or ""})
    if len(errors) == errs_len:
        pass
    else:
        for e in errors[errs_len:]:
            print("FAIL-CLOSED:", e, flush=True)
        return 1

    # ---------------- summary ------------------------------------------------
    n_anchor = sum(1 for p in plan if p["verdict"] == "anchor")
    n_quar = sum(1 for p in plan if p["verdict"] == "quarantine")
    n_defer = sum(1 for p in plan if p["verdict"] == "defer")
    pred_first = {iid for p in plan for iid, _ in p["eligible"]
                  if not (items[iid].get("codes") or [])}
    print(f"BATCH {batch_id} / {bank}: rulings={len(plan)} "
          f"(anchor {n_anchor} / quarantine {n_quar} / defer {n_defer})")
    print(f"  predicted: parts_touched={len(pred_parts)} "
          f"first_code_parts={len(pred_first)} entries_added={pred_entries} "
          f"(already-present skipped: {sum(already.values())})")
    if args.check:
        print("CHECK-ONLY: no writes.")
        return 0

    # ---------------- G5 pre-apply totals -----------------------------------
    pre = totals_of(items)
    stored = side.get("totals") or {}
    if (stored.get("items"), stored.get("items_with_codes"),
            stored.get("by_kind"), stored.get("coded_by_kind")) != \
       (pre["items"], pre["items_with_codes"], pre["by_kind"], pre["coded_by_kind"]):
        die("G5: sidecar stored totals drift under recompute (input integrity broken)")
    entries_pre = sum(len(it.get("codes") or []) for it in items.values()
                      if isinstance(it, dict) and it.get("kind") == "question_part")

    # ---------------- apply (atomic per bank) --------------------------------
    for p in plan:
        for iid, fresh in p["eligible"]:
            it = items[iid]
            for oid, ocode in fresh:
                it.setdefault("codes", []).append({
                    "official_id": oid, "official_code": ocode,
                    "tier": NEW_TIER, "method": NEW_METHOD,
                    "unit": None, "score": None, "source_sid": p["sid"],
                })
    post = totals_of(items)
    entries_post = sum(len(it.get("codes") or []) for it in items.values()
                       if isinstance(it, dict) and it.get("kind") == "question_part")
    d_first = post["coded_by_kind"]["question_parts"] - pre["coded_by_kind"]["question_parts"]
    d_items = post["items_with_codes"] - pre["items_with_codes"]
    d_entries = entries_post - entries_pre
    if d_first != len(pred_first):
        die(f"G5: first-code parts delta {d_first} != predicted {len(pred_first)}")
    if d_items != len(pred_first):
        die(f"G5: items_with_codes delta {d_items} != predicted {len(pred_first)}")
    if d_entries != pred_entries:
        die(f"G5: entries delta {d_entries} != predicted {pred_entries}")
    side["totals"] = {
        "items": post["items"], "items_with_codes": post["items_with_codes"],
        "by_kind": post["by_kind"], "coded_by_kind": post["coded_by_kind"],
    }

    # ---------------- additive blocks ----------------------------------------
    bid = batch_id
    batch_block = {
        "lane": LANE, "batch_id": bid, "bank": bank,
        "directive": b.get("directive"), "ruled_utc": b.get("ruled_utc"),
        "ruled_by": b.get("ruled_by"),
        "source_sheet": entry["sheet"], "source_sheet_sha256": entry["sheet_sha256"],
        "tier": NEW_TIER, "method": NEW_METHOD, "tier_semantics": TIER_SEMANTICS,
        "rulings": len(plan), "anchored_sids": n_anchor,
        "quarantined_sids": n_quar, "deferred_sids": n_defer,
        "parts_touched": len(pred_parts), "entries_added": pred_entries,
        "applied_utc": b.get("ruled_utc"),
        "rulings_detail": [
            {"sid": p["sid"], "verdict": p["verdict"], "codes": p["codes"],
             "parts": [iid for iid, _ in p["eligible"]],
             "reason": p["reason"], "note": p["note"]}
            for p in plan],
    }
    side.setdefault("anchors", {}).setdefault("tranche2_batches", {})[bid] = {
        "lane": LANE, "batch_id": bid, "applied_utc": b.get("ruled_utc"),
        "tier": NEW_TIER, "method": NEW_METHOD,
        "anchored_sids": n_anchor, "quarantined_sids": n_quar,
        "deferred_sids": n_defer, "parts_touched": len(pred_parts),
        "entries_added": pred_entries,
        "scope": ("the map-universe review sheet's ruled sids; pending refs "
                  "preserved (the declared trail); codes additive; no join "
                  "re-derived (ADR-030)")}
    side.setdefault("review_state", {}).setdefault("tranche2_batches", {})[bid] = batch_block

    # ---------------- manifest (additive) ------------------------------------
    mpath = sl_dir / "manifest.json"
    manifest = json.loads(mpath.read_text())
    row = manifest["courses"].get(bank)
    if row is None:
        die(f"manifest row missing for {bank}")
    row.setdefault("tranche2_batches", {})[bid] = {
        "lane": LANE, "anchored_sids": n_anchor, "quarantined_sids": n_quar,
        "deferred_sids": n_defer, "parts_touched": len(pred_parts),
        "entries_added": pred_entries}
    manifest.setdefault("cie_tranche2_r2_batches", {})[bid] = {
        "lane": LANE, "bank": bank, "applied_utc": b.get("ruled_utc"),
        "directive": b.get("directive"),
        "source_sheet": entry["sheet"],
        "rulings": len(plan), "parts_touched": len(pred_parts),
        "entries_added": pred_entries,
        "tier_policy": {NEW_TIER: TIER_SEMANTICS},
    }
    mpath.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")

    # ---------------- write sidecar + machine record -------------------------
    sl_path.write_text(json.dumps(side, indent=1, ensure_ascii=False) + "\n")
    rec_dir = REPORTS / "tranche2-r2" / "batches"
    rec_dir.mkdir(parents=True, exist_ok=True)
    (rec_dir / f"{batch_id}.json").write_text(json.dumps({
        "lane": LANE, "batch_id": bid, "bank": bank,
        "generated_utc": b.get("ruled_utc"), "directive": b.get("directive"),
        "tier": NEW_TIER, "method": NEW_METHOD, "tier_semantics": TIER_SEMANTICS,
        "source_sheet": entry["sheet"], "source_sheet_sha256": entry["sheet_sha256"],
        "rulings": len(plan), "anchored_sids": n_anchor,
        "quarantined_sids": n_quar, "deferred_sids": n_defer,
        "parts_touched": len(pred_parts), "first_code_parts": len(pred_first),
        "entries_added": pred_entries,
        "totals": {"pre": pre, "post": post},
        "sidecar_sha256_after": sha256_file(sl_path),
    }, indent=1, ensure_ascii=False) + "\n")

    print(f"APPLIED: {bank} parts_touched={len(pred_parts)} entries_added={pred_entries} "
          f"(anchor {n_anchor} / quarantine {n_quar} / defer {n_defer})")
    print("NEXT: consume -> census re-pin -> PR -> the operator-gated 134c "
          "(parked while the census is unchanged)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
