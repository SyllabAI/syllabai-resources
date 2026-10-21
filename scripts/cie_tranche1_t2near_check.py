#!/usr/bin/env python3
"""
T-SPECS-CIE-TRANCHE1-T2NEAR-1 — check battery (fail-closed, base-blob re-derivation).

Mirrors the T-SPECS-CIE-VERDICT-1 battery family (cie_verdict_check.py V1-V10).
Every check re-derives its truth from the BASE commit blobs named in the verdict
sheet (never from the engine's own outputs) plus the lane registry — the engine
is trusted for nothing.

Usage:
  python3 cie_tranche1_t2near_check.py
Env (optional, strengthens T8):
  V2_MAPS=/path/to/syllabai-v2/apps/hub/content-maps  (cross-foot spine codes)
Exit 0 iff every check passes; prints the machine JSON record path.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SL = REPO / "spec-links"
SHEET = REPO / "scripts" / "cie_tranche1_t2near_verdicts.yaml"
REPORTS = REPO / "graph" / "reports"

LANE_ID = "T-SPECS-CIE-TRANCHE1-T2NEAR-1"
NEW_TIER = "V6_near_text_verdict"
NEW_METHOD = "operator_verdict"
PRIOR_TIER = "T2_near"

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

DECLARED = [
    "spec-links/manifest.json", "spec-links/README.md",
    "scripts/cie_tranche1_t2near_verdicts.yaml",
    "scripts/cie_tranche1_t2near_fill.py",
    "scripts/cie_tranche1_t2near_check.py",
    "graph/reports/T_SPECS_CIE_TRANCHE1_T2NEAR_RECORD.md",
    "graph/reports/T_SPECS_CIE_TRANCHE1_T2NEAR_FILL.json",
    "graph/reports/T_SPECS_CIE_TRANCHE1_T2NEAR_CHECK.json",
] + [f"spec-links/cie-{s}.json" for s in []]  # lane files added below


def git_show(base: str, path: str) -> bytes:
    return subprocess.run(["git", "show", f"{base}:{path}"], cwd=REPO,
                          capture_output=True, check=True).stdout


def git_status() -> list:
    out = subprocess.run(["git", "status", "--porcelain"], cwd=REPO,
                         capture_output=True, text=True, check=True).stdout
    rows = []
    for line in out.splitlines():
        st, p = line[:2], line[3:].strip()
        if " -> " in p:
            p = p.split(" -> ")[1]
        rows.append((st, p))
    return rows


def main() -> int:
    sheet = yaml.safe_load(SHEET.read_text())
    base = sheet["base_commit"]
    rows = sheet["verdicts"]
    lanes = sorted({r["lane"] for r in rows})
    results = []

    def check(cid, name, ok, detail=""):
        results.append({"id": cid, "name": name, "ok": bool(ok), "detail": str(detail)[:400]})
        print(f"{'PASS' if ok else 'FAIL'} {cid}: {name}" + (f" — {detail}" if detail and not ok else ""))
        return ok

    # ---------------- T1: lanes well-formed + receipt-queue cross-foot ------
    ok = True
    detail = []
    for lane in lanes:
        d = json.loads((SL / f"{lane}.json").read_text())
        rs = d.get("review_state") or {}
        if rs.get("state") != "ACCEPTED":
            ok = False; detail.append(f"{lane}: state")
        if (rs.get("tranche1") or {}).get("lane") != LANE_ID:
            ok = False; detail.append(f"{lane}: review_state.tranche1")
        if (d.get("anchors") or {}).get("tranche1", {}).get("lane") != LANE_ID:
            ok = False; detail.append(f"{lane}: anchors.tranche1")
        parts = len({r["item"] for r in rows if r["lane"] == lane})
        entries = len([r for r in rows if r["lane"] == lane])
        if parts != RECEIPT_QUEUE[lane] or rs["tranche1"]["parts"] != parts \
           or rs["tranche1"]["entries"] != entries:
            ok = False; detail.append(f"{lane}: counts")
    check("T1", "9 lanes well-formed (ACCEPTED + additive blocks) + receipt-queue cross-foot "
          f"({sum(RECEIPT_QUEUE.values())} parts / {len(rows)} entries)", ok, "; ".join(detail))

    # ---------------- T2: bijection vs BASE blobs (independent re-derivation)
    ok = True; detail = []
    for lane in lanes:
        base_d = json.loads(git_show(base, f"spec-links/{lane}.json"))
        head_d = json.loads((SL / f"{lane}.json").read_text())
        promoted_expected = {(r["item"], r["official_id"], r["official_code"])
                             for r in rows if r["lane"] == lane}
        promoted_found = set()
        for iid in base_d["items"]:
            b_codes = base_d["items"][iid].get("codes") or []
            h_codes = head_d["items"][iid].get("codes") or []
            bmap = {(e.get("official_id"), e.get("official_code")): e for e in b_codes}
            hmap = {(e.get("official_id"), e.get("official_code")): e for e in h_codes}
            if set(bmap) != set(hmap):
                ok = False; detail.append(f"{lane}/{iid}: code-key set drift")
                continue
            for k, be in bmap.items():
                he = hmap[k]
                if be.get("tier") == PRIOR_TIER:
                    if (iid, k[0], k[1]) in promoted_expected:
                        promoted_found.add((iid, k[0], k[1]))
                        if he.get("tier") != NEW_TIER or he.get("method") != NEW_METHOD:
                            ok = False; detail.append(f"{lane}/{iid}/{k[1]}: not promoted")
                    else:
                        if he != be:
                            ok = False; detail.append(f"{lane}/{iid}/{k[1]}: changed outside sheet")
                else:
                    if he != be:
                        ok = False; detail.append(f"{lane}/{iid}/{k[1]}: non-T2 entry drift")
        if promoted_found != promoted_expected:
            ok = False
            detail.append(f"{lane}: bijection delta expected-found "
                          f"{sorted(promoted_expected - promoted_found)[:2]} {sorted(promoted_found - promoted_expected)[:2]}")
    check("T2", "bijection: promoted set (base T2 entries on sheet items) == sheet, per lane; "
          "zero other entry drift", ok, "; ".join(detail[:6]))

    # ---------------- T3: zero dangling targets (lane registry) -------------
    ok = True; detail = []
    man = json.loads((REPO / "Official-Specifications" / "manifest.json").read_text())
    byslug = {q["slug"]: q for q in man["qualifications"]}
    for lane in lanes:
        qual = json.loads((SL / f"{lane}.json").read_text())["registry"]["id"]
        pdf = Path(byslug[qual]["pdf"]).stem
        reg = json.loads((REPO / "Official-Specifications" / "parsed" / qual / f"{pdf}.parsed.json").read_text())
        id2code = {p["id"]: str(p.get("official_code")) for p in reg["spec_points"]}
        for r in rows:
            if r["lane"] != lane:
                continue
            if id2code.get(r["official_id"]) != r["official_code"]:
                ok = False; detail.append(f"{lane}:{r['official_id']}")
    check("T3", "zero dangling verdict targets (official_id AND official_code in the lane registry)",
          ok, "; ".join(detail[:4]))

    # ---------------- T4: vocabulary conformance ----------------------------
    # scope law: the tranche-1 verdict covers the 155 sheet ITEMS only — T2_near
    # hints on OTHER items of these lanes (the notes axis, tranche-2 scope per
    # the census receipt) legitimately remain; they stay non-authoritative.
    ok = True; detail = []
    sheet_items = {(r["lane"], r["item"]) for r in rows}
    for lane in lanes:
        head_d = json.loads((SL / f"{lane}.json").read_text())
        for iid, it in head_d["items"].items():
            for e in it.get("codes") or []:
                if e.get("tier") == NEW_TIER and e.get("method") != NEW_METHOD:
                    ok = False; detail.append(f"{lane}/{iid}: V6 without operator_verdict")
                if e.get("method") == NEW_METHOD and e.get("tier") != NEW_TIER:
                    ok = False; detail.append(f"{lane}/{iid}: operator_verdict without V6")
                if e.get("tier") == PRIOR_TIER and (lane, iid) in sheet_items:
                    ok = False; detail.append(f"{lane}/{iid}: T2_near survived on a sheet item")
    check("T4", "vocabulary conformance (V6+operator_verdict pairing; zero T2_near left on the "
          "155 sheet items; out-of-scope hints on other items untouched)", ok, "; ".join(detail[:4]))

    # ---------------- T5: structural integrity vs base ----------------------
    ok = True; detail = []
    for lane in lanes:
        base_d = json.loads(git_show(base, f"spec-links/{lane}.json"))
        head_d = json.loads((SL / f"{lane}.json").read_text())
        if set(base_d["items"]) != set(head_d["items"]):
            ok = False; detail.append(f"{lane}: item-id set"); continue
        for iid, bit in base_d["items"].items():
            hit = head_d["items"][iid]
            for f in ("kind", "label", "pending"):
                if bit.get(f) != hit.get(f):
                    ok = False; detail.append(f"{lane}/{iid}.{f}")
            if json.dumps(bit.get("smeSpecPointIds")) != json.dumps(hit.get("smeSpecPointIds")):
                ok = False; detail.append(f"{lane}/{iid}.smeSpecPointIds")
        for blk in ("registry", "qual", "board", "totals", "schema", "course"):
            if json.dumps(base_d.get(blk), sort_keys=True) != json.dumps(head_d.get(blk), sort_keys=True):
                ok = False; detail.append(f"{lane}.{blk}")
        # anchors/review_state: pre-existing fields only (drop additive blocks)
        for blk in ("anchors", "review_state"):
            b = {k: v for k, v in (base_d.get(blk) or {}).items() if k != "tranche1"}
            h = {k: v for k, v in (head_d.get(blk) or {}).items() if k != "tranche1"}
            if json.dumps(b, sort_keys=True) != json.dumps(h, sort_keys=True):
                ok = False; detail.append(f"{lane}.{blk} pre-existing drift")
    check("T5", "structural integrity vs base (items/kinds/labels/pending/totals/registry/"
          "pre-existing blocks byte-identical)", ok, "; ".join(detail[:6]))

    # ---------------- T6: all other sidecars byte-identical to base ---------
    ok = True; detail = []
    all_cie = [p.name for p in SL.glob("cie-*.json")]
    for name in sorted(all_cie):
        lane = name[:-5]
        if lane in lanes:
            continue
        if git_show(base, f"spec-links/{name}") != (SL / name).read_bytes():
            ok = False; detail.append(name)
    # Edexcel files
    edx = sorted(p.name for p in SL.glob("*.json")
                 if not p.name.startswith("cie-") and p.name not in ("manifest.json", "README.md"))
    for name in edx:
        if git_show(base, f"spec-links/{name}") != (SL / name).read_bytes():
            ok = False; detail.append(name)
    check("T6", f"non-verdict footprint byte-identical to base "
          f"({len(all_cie) - len(lanes)} CIE + {len(edx)} Edexcel sidecars)", ok, "; ".join(detail[:4]))

    # ---------------- T7: manifest additive-only vs base --------------------
    ok = True; detail = []
    bm = json.loads(git_show(base, "spec-links/manifest.json"))
    hm = json.loads((SL / "manifest.json").read_text())
    for k, v in bm.items():
        if k == "cie_tranche1":
            continue
        if k == "courses":
            for lane, row in v.items():
                hrow = hm["courses"].get(lane)
                if hrow is None:
                    ok = False; detail.append(f"courses.{lane}: missing"); continue
                for fk, fv in row.items():
                    if hrow.get(fk) != fv:
                        ok = False; detail.append(f"courses.{lane}.{fk}")
        elif json.dumps(v, sort_keys=True) != json.dumps(hm.get(k), sort_keys=True):
            ok = False; detail.append(f"top.{k}")
    if hm.get("cie_tranche1", {}).get("lane") != LANE_ID:
        ok = False; detail.append("top.cie_tranche1")
    for lane in lanes:
        if hm["courses"].get(lane, {}).get("tranche1", {}).get("lane") != LANE_ID:
            ok = False; detail.append(f"courses.{lane}.tranche1")
    check("T7", "manifest: pre-existing rows/fields value-identical + additive tranche1 blocks",
          ok, "; ".join(detail[:6]))

    # ---------------- T8: spine cross-foot (v2 maps, optional env) ----------
    v2maps = os.environ.get("V2_MAPS")
    if v2maps:
        ok = True; detail = []
        cache = {}
        for r in rows:
            mp = Path(v2maps) / f"{r['lane']}.json"
            if r["lane"] not in cache:
                cache[r["lane"]] = json.loads(mp.read_text())["items"]
            hints = cache[r["lane"]].get(r["item"], {}).get("t2HintCodes") or []
            if not any(h.get("officialId") == r["official_id"] and h.get("spineCode") == r["spine_code"]
                       for h in hints):
                ok = False; detail.append(f"{r['lane']}/{r['item']}/{r['official_id']}")
        check("T8", f"v2-map cross-foot: every row's (item, official_id, spine_code) matches the "
              f"committed t2HintCodes ({len(rows)} rows)", ok, "; ".join(detail[:4]))
    else:
        check("T8", "v2-map cross-foot SKIPPED (V2_MAPS not set)", True)

    # ---------------- T9: footprint guard -----------------------------------
    allowed = set(DECLARED) | {f"spec-links/{l}.json" for l in lanes}
    st_rows = git_status()
    outside = [f"{st} {p}" for st, p in st_rows if p not in allowed]
    check("T9", f"footprint guard: git status within the declared set ({len(st_rows)} paths, "
          f"{len(outside)} outside)", not outside, "; ".join(outside[:6]))

    # ---------------- T10: re-run safety (fail-closed, zero drift) ----------
    h_before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                for lane in lanes for p in [SL / f"{lane}.json"]}
    rc = subprocess.run([sys.executable, str(REPO / "scripts" / "cie_tranche1_t2near_fill.py")],
                        capture_output=True, text=True)
    h_after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
               for lane in lanes for p in [SL / f"{lane}.json"]}
    ok = rc.returncode != 0 and h_before == h_after and "already" not in rc.stdout.lower()
    check("T10", "re-run safety: engine re-run fail-closes (T2 entries consumed) AND zero byte drift",
          ok, f"rc={rc.returncode} drift={[k for k in h_before if h_before[k] != h_after[k]]}")

    passed = sum(1 for r in results if r["ok"])
    total = len(results)
    print(f"\nBATTERY {passed}/{total} " + ("GREEN" if passed == total else "RED"))
    record = {
        "lane": LANE_ID,
        "base_commit": base,
        "generated_utc": sheet["generated_utc"],
        "battery": results,
        "passed": passed, "total": total,
    }
    out = REPORTS / "T_SPECS_CIE_TRANCHE1_T2NEAR_CHECK.json"
    out.write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n")
    print(f"record -> {out}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
