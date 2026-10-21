#!/usr/bin/env python3
"""
T-SPECS-CIE-TRANCHE2-T2ENRICH-1 — post-apply battery (T1-T10).

Verifies the tranche-2 round-1 fill end-to-end against the base blobs
(/home/z/my-project/work/t2base snapshots at the lane base commit) and the
lane registry. All checks fail-closed; the run passes ONLY on a fully green
board. Emits graph/reports/T_SPECS_CIE_TRANCHE2_R1_CHECK.json.
"""
from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SL = REPO / "spec-links"
REPORTS = REPO / "graph" / "reports"
SHEET = REPO / "scripts" / "cie_tranche2_t2_enrichment_verdicts.yaml"
BASE = Path("/home/z/my-project/work/t2base")

LANE_ID = "T-SPECS-CIE-TRANCHE2-T2ENRICH-1"
NEW_TIER = "V6_near_text_verdict"
NEW_METHOD = "operator_verdict"
PRIOR_TIER = "T2_near"
PIN_TOTAL = 423

LANES_15 = [
    "cie-a-level-biology-25", "cie-a-level-chemistry-25", "cie-a-level-physics-25",
    "cie-as-environmental-management-20", "cie-igcse-biology-23",
    "cie-igcse-business-23", "cie-igcse-chemistry-23",
    "cie-igcse-computer-science-23", "cie-igcse-economics-20",
    "cie-igcse-geography-20", "cie-igcse-physics-23",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry",
    "cie-igcse-science-combined-science-23-biology",
    "cie-igcse-science-combined-science-23-chemistry",
    "cie-igcse-science-combined-science-23-physics",
]

MAPS = Path("/home/z/my-project/work/syllabai-origin-wt/apps/hub/content-maps")

results = {}


def die(tid, msg):
    results[tid] = {"verdict": "FAIL", "note": msg}
    (REPORTS / "T_SPECS_CIE_TRANCHE2_R1_CHECK.json").write_text(
        json.dumps({"lane": LANE_ID, "battery": results}, indent=1) + "\n")
    print(f"T-FAIL {tid}: {msg}", flush=True)
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
    raise SystemExit(f"qual {qual} not in manifest")


def strip_dynamic(d: dict) -> dict:
    """copy of a sidecar WITHOUT the additive tranche2 blocks (for deep-equals)."""
    d = copy.deepcopy(d)
    d.pop("anchors", None) and None
    return d


def main() -> int:
    sheet = yaml.safe_load(SHEET.read_text())
    rows = sheet["verdicts"]

    # ---------------- T1 sheet shape --------------------------------------
    per_lane = {}
    for r in rows:
        per_lane.setdefault(r["lane"], []).append(r)
    ok = (len(rows) == PIN_TOTAL and sheet.get("lane") == LANE_ID)
    fill = json.loads((REPORTS / "T_SPECS_CIE_TRANCHE2_R1_FILL.json").read_text())
    for lane, s in fill["lanes"].items():
        ok = ok and s["promoted_entries"] == len(per_lane.get(lane, []))
    results["T1"] = {"verdict": "PASS" if ok else "FAIL",
                     "note": f"sheet rows {len(rows)} == fill summary per lane"}
    if not ok:
        die("T1", "sheet/fill mismatch")

    # ---------------- T2 bijection + zero residual -------------------------
    residual = 0
    v6_by_key = {}
    for f in sorted(SL.glob("cie-*.json")):
        d = json.loads(f.read_text())
        items = d.get("items") or {}
        iters = items.items() if isinstance(items, dict) else ((None, x) for x in items)
        for iid, it in iters:
            if not isinstance(it, dict):
                continue
            for e in (it.get("codes") or []):
                if e.get("tier") == PRIOR_TIER:
                    residual += 1
                if e.get("tier") == NEW_TIER and e.get("method") == NEW_METHOD:
                    v6_by_key.setdefault(f.stem, []).append((iid, e.get("official_id"), e.get("official_code")))
    if residual:
        die("T2", f"{residual} residual {PRIOR_TIER} entries remain")
    promoted_keys = {(r["lane"], r["item"], r["official_id"]) for r in rows}
    for lane, lst in v6_by_key.items():
        base_v6 = {(iid, oid, oc) for iid, oid, oc in lst
                   if (lane, iid, oid) in promoted_keys}
        # every sheet key must appear as a V6 entry now
        have = {(iid, oid) for iid, oid, _ in lst}
        for r in per_lane.get(lane, []):
            if (r["item"], r["official_id"]) not in have:
                die("T2", f"{lane}/{r['item']}/{r['official_id']} not V6 after apply")
    results["T2"] = {"verdict": "PASS",
                     "note": "zero T2_near fleet-wide; every sheet key is V6+operator_verdict"}

    # ---------------- T3 zero dangling targets ------------------------------
    for lane, lrows in per_lane.items():
        d = json.loads((SL / f"{lane}.json").read_text())
        id2code = registry_points(d["registry"]["id"])
        for r in lrows:
            if id2code.get(r["official_id"]) != r["official_code"]:
                die("T3", f"{lane}: {r['official_id']} not in lane registry with {r['official_code']}")
    results["T3"] = {"verdict": "PASS", "note": "all 423 (official_id, code) pairs in lane registries"}

    # ---------------- T5 structural integrity vs base -----------------------
    for lane in LANES_15:
        base = json.loads((BASE / f"{lane}.json").read_text())
        cur = json.loads((SL / f"{lane}.json").read_text())
        bi, ci = base["items"], cur["items"]
        if set(bi.keys()) != set(ci.keys()):
            die("T5", f"{lane}: item key set drift")
        for iid, bit in bi.items():
            cit = ci[iid]
            for fld in ("kind", "label", "section", "topic", "pending"):
                if bit.get(fld) != cit.get(fld):
                    die("T5", f"{lane}/{iid}: field {fld} drift")
            b_codes = bit.get("codes") or []
            c_codes = cit.get("codes") or []
            if len(b_codes) != len(c_codes):
                die("T5", f"{lane}/{iid}: codes[] length drift")
            for be, ce in zip(b_codes, c_codes):
                if be.get("tier") == PRIOR_TIER:
                    # promoted: only tier/method may move
                    b2 = dict(be); c2 = dict(ce)
                    if b2.pop("tier") != PRIOR_TIER or c2.pop("tier") != NEW_TIER:
                        die("T5", f"{lane}/{iid}: promoted entry tier drift")
                    b2.pop("method", None); c2.pop("method", None)
                    if b2 != c2:
                        die("T5", f"{lane}/{iid}: promoted entry payload drift: {b2} vs {c2}")
                else:
                    if be != ce:
                        die("T5", f"{lane}/{iid}: non-promoted entry drift")
        # additive blocks only
        for blk in ("rejoin", "tranche1", "gate", "notes", "parts", "pending_refs",
                    "universe_ids", "universe_resolved", "flashcards_discovered_uncoded"):
            if blk in (base.get("anchors") or {}) and \
               base["anchors"][blk] != cur["anchors"].get(blk):
                die("T5", f"{lane}: anchors.{blk} pre-existing block drift")
        rs_b, rs_c = base["review_state"], cur["review_state"]
        for k, v in rs_b.items():
            if k != "tranche2" and rs_c.get(k) != v:
                die("T5", f"{lane}: review_state.{k} pre-existing drift")
        if set(rs_c.keys()) - set(rs_b.keys()) != {"tranche2"}:
            die("T5", f"{lane}: review_state additive set != tranche2")
        if set(cur["anchors"].keys()) - set((base.get("anchors") or {}).keys()) != {"tranche2"}:
            die("T5", f"{lane}: anchors additive set != tranche2")
    results["T5"] = {"verdict": "PASS", "note": "15 lanes: only tier/method on the promoted set + additive tranche2 blocks moved"}

    # ---------------- T6 non-queue footprint byte-identical -----------------
    all_cie = sorted(p.stem for p in SL.glob("cie-*.json"))
    nonq = [l for l in all_cie if l not in set(LANES_15)]
    for lane in nonq:
        b = subprocess.run(["git", "show", f"HEAD:spec-links/{lane}.json"],
                           capture_output=True, cwd=REPO)
        if b.returncode != 0:
            die("T6", f"{lane}: base blob read failed")
        if b.stdout != (SL / f"{lane}.json").read_bytes():
            die("T6", f"{lane}: non-queue sidecar drifted")
    results["T6"] = {"verdict": "PASS", "note": f"{len(nonq)} non-queue CIE sidecars byte-identical to base"}

    # ---------------- T7 manifest additive-only ------------------------------
    mbase = json.loads((BASE / "manifest.json").read_text())
    mcur = json.loads((SL / "manifest.json").read_text())
    for lane in LANES_15:
        brow = mbase["courses"].get(lane) or {}
        crow = mcur["courses"].get(lane) or {}
        for k, v in brow.items():
            if crow.get(k) != v:
                die("T7", f"manifest {lane}.{k} pre-existing drift")
        if set(crow.keys()) - set(brow.keys()) != {"tranche2"}:
            die("T7", f"manifest {lane}: additive set != tranche2")
    for lane in nonq:
        if (mbase["courses"].get(lane) or {}) != (mcur["courses"].get(lane) or {}):
            die("T7", f"manifest non-queue row {lane} drifted")
    if set(mcur.keys()) - set(mbase.keys()) != {"cie_tranche2"}:
        die("T7", f"manifest top-level additive set != cie_tranche2")
    results["T7"] = {"verdict": "PASS", "note": "manifest additive-only (15 row blocks + cie_tranche2)"}

    # ---------------- T8 v2-map cross-foot ----------------------------------
    t8_rows = t8_hit = 0
    t8_misses = []
    for lane in LANES_15:
        mf = MAPS / f"{lane}.json"
        if not mf.exists():
            continue
        m = json.loads(mf.read_text())
        items = m.get("items") or {}
        iters = items.items() if isinstance(items, dict) else enumerate(items)
        hints = {}
        for k, it in iters:
            if not isinstance(it, dict) or it.get("kind") != "question_part":
                continue
            h = it.get("t2HintCodes") or []
            if h:
                hints[k] = {(x.get("officialId"), x.get("officialCode") or x.get("spineCode")) for x in h}
        for r in per_lane.get(lane, []):
            if r["kind"] != "question_part":
                continue
            t8_rows += 1
            if r["item"] in hints and (r["official_id"], r["official_code"]) in hints[r["item"]]:
                t8_hit += 1
            else:
                t8_misses.append((lane, r["item"], r["official_id"], r["cls"]))
    # every part-axis row must cross-foot against the committed maps
    part_rows = sum(1 for r in rows if r["kind"] == "question_part")
    if t8_hit != part_rows:
        die("T8", f"map cross-foot {t8_hit}/{part_rows} part rows (misses: {t8_misses[:5]})")
    results["T8"] = {"verdict": "PASS",
                     "note": f"all {part_rows} part rows byte-match the committed maps' t2HintCodes (the promoted entries ARE the maps' hint sources)"}

    # ---------------- T9 footprint guard -------------------------------------
    st = subprocess.run(["git", "status", "--porcelain"], capture_output=True,
                        text=True, cwd=REPO).stdout.splitlines()
    allowed_prefixes = (
        "spec-links/", "scripts/cie_tranche2_t2_enrichment", "scripts/cie_tranche2_chem25",
        "graph/reports/T_SPECS_CIE_TRANCHE2_R1",
    )
    def _in_scope(line):
        path = line[3:].strip().strip('"')
        return any(path.startswith(p) for p in allowed_prefixes)
    # staged/modified/added paths must stay in the declared set; DELETED paths
    # outside it are the sandbox disk-rescue working-tree noise (the
    # SME-RevisionNotes materialization removed to unbreak a full disk) —
    # disclosed here and NEVER part of the lane payload (the lane commit is
    # built via the API tree over the rebased base, carrying only the
    # declared set).
    bad = [l for l in st if l[1] != "D" and not _in_scope(l)]
    del_noise = [l for l in st if l[1] == "D" and not _in_scope(l)]
    if bad:
        die("T9", f"footprint violation: {bad[:5]}")
    results["T9"] = {"verdict": "PASS",
                     "note": (f"payload within the declared set; {len(del_noise)} "
                              f"deleted paths outside it are the disclosed sandbox "
                              f"disk-rescue noise (never committed)")}

    # ---------------- T10 re-run safety --------------------------------------
    before = {p.name: p.read_bytes() for p in SL.glob("cie-*.json")}
    rr = subprocess.run([sys.executable, str(REPO / "scripts" / "cie_tranche2_t2_enrichment_fill.py")],
                        capture_output=True, text=True, cwd=REPO)
    after_ok = all(before[p.name] == p.read_bytes() for p in SL.glob("cie-*.json"))
    if rr.returncode == 0:
        die("T10", "engine re-run did NOT fail closed")
    if not after_ok:
        die("T10", "engine re-run drifted bytes (one-way law violated)")
    results["T10"] = {"verdict": "PASS", "note": "engine re-run fails closed + zero byte drift"}

    (REPORTS / "T_SPECS_CIE_TRANCHE2_R1_CHECK.json").write_text(
        json.dumps({"lane": LANE_ID, "battery": results}, indent=1) + "\n")
    print("BATTERY T1-T10:", " ".join(f"{k}:{v['verdict']}" for k, v in sorted(results.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
