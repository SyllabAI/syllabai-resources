#!/usr/bin/env python3
"""T-SPEC-10 — apply the operator reasoning round to the remaining pendings.

Operator instruction (Nawaf Al Hussain Khondokar, 2026-09-19, IM): the
remaining unresolved tag ids are mapped by direct operator reasoning against
the committed registries and the official specification PDFs — no scripted
matching, no upstream tickets. Four classes of lane-record in
scripts/t_spec_10_verdicts.yaml:

  1. tag-level resolves (codes + tier + official_id) — T-SPEC-8/9 semantics;
  2. tag-level REFINEMENTS (refinement: true + was_code) — correction of an
     existing mapping whose recorded code did not match the tag subject; the
     old code is asserted fail-closed and audited in the report;
  3. tag-level UNRESOLVES (verdict: unresolve + was_code) — an existing
     mapping with no honest target is reverted to the tail with a reason;
  4. pending-reason updates (verdict: pending + pending_reason) — stale or
     wrong pending reasons corrected; refuses to touch resolved entries.

Fail-closed rules mirror T-SPEC-8/9: (official_id, codes[0]) pair-checked
against the qualification registry; twin codes must exist; a resolved tag
must sit in the lane's unmapped tail, be idempotent, or be an explicit
refinement; an unresolve must assert the exact code being reverted;
population closure re-checked per lane. Part codes are re-derived from tag
ids afterwards (2e/9 part-level overrides preserved). PMT excluded as source.
"""
import json
import sys
import copy
import datetime
from collections import Counter
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from t_spec_7_apply import topic_files  # noqa: E402
from t_spec_9_apply import LANES  # noqa: E402

# SDA lanes were coded outside the T-SPEC-7/9 lane registry (T-SPEC-4 round);
# their qual name follows the corpus registry.
LANES = dict(LANES)
LANES["igcse-science-double-award-17-physics"] = \
    ("igcse-science-double-award", None)

BASE = Path("/home/z/my-project/download/syllabai-resources")
EQ = BASE / "SME-ExamQuestion"
PARSED = BASE / "Official-Specifications" / "parsed"
REPORTS = BASE / "graph" / "reports"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

METHOD = ("T-SPEC-10 operator reasoning round "
          "(no upstream; PMT excluded as source)")


def pool_for(qual):
    pts = json.loads((PARSED / qual / "spec_points.json")
                     .read_text())["spec_points"]
    return {p["id"]: p for p in pts}, {p["official_code"]: p for p in pts}


def main() -> int:
    vdoc = yaml.safe_load((BASE / "scripts" / "t_spec_10_verdicts.yaml")
                          .read_text())
    idv = vdoc["id_verdicts"]

    lanes_hit = sorted({lane for v in idv.values() for lane in v})
    unknown = [l for l in lanes_hit if l not in LANES]
    if unknown:
        raise SystemExit(f"FAIL: unknown lanes: {unknown}")

    errors = []
    report = {"schema": "syllabai.t-spec-10-apply/1.0", "generated_utc": NOW,
              "note": vdoc["note"], "per_lane": {}}

    # ---------- pass 1: tag-level records ----------
    for lane in lanes_hit:
        qual, _mode = LANES[lane]
        cdir = EQ / lane
        mp_path = cdir / "spec_point_map.json"
        mp = json.loads(mp_path.read_text())
        mp_orig = copy.deepcopy(mp)
        idx = json.loads((cdir / "spec_point_index.json").read_text())
        res_path = cdir / "spec_point_resolution.json"
        res = json.loads(res_path.read_text())
        res_orig = copy.deepcopy(res)
        by_id, by_code = pool_for(qual)
        mappings = mp.setdefault("mappings", {})
        unmapped = {u["spcpt_id"]: u for u in mp.get("unmapped", [])}
        res_by_id = {r["id"]: r for r in res["resolved"]}
        stats = Counter()
        audit = []

        for sid, v in idv.items():
            crec = v.get(lane)
            if not crec:
                continue

            # --- class 3: unresolve (revert a wrong mapping to the tail) ---
            if crec.get("verdict") == "unresolve":
                cur = mappings.get(sid)
                if cur is None:
                    # idempotent re-run: the unresolve already took effect
                    rprev = res_by_id.get(sid)
                    if rprev is not None and \
                            rprev.get("resolved_code") == crec.get("was_code"):
                        errors.append(
                            f"{lane}: {sid} unresolve but sidecar still "
                            f"resolves {crec.get('was_code')}")
                        continue
                    reason = crec.get("reason") or ""
                    if rprev is not None and reason \
                            and rprev.get("reason") != reason:
                        rprev["reason"] = reason
                        stats["reason_updated"] += 1
                    else:
                        stats["idempotent"] += 1
                    continue
                if cur.get("official_code") != crec.get("was_code"):
                    errors.append(
                        f"{lane}: {sid} unresolve was_code "
                        f"{crec.get('was_code')} != mapped "
                        f"{cur.get('official_code')}")
                    continue
                r = res_by_id.get(sid)
                if r is None or r.get("resolved_code") != crec["was_code"]:
                    errors.append(f"{lane}: {sid} unresolve sidecar mismatch")
                    continue
                reason = crec.get("reason") or ""
                if not reason:
                    errors.append(f"{lane}: {sid} unresolve without reason")
                    continue
                audit.append({"id": sid, "action": "unresolve",
                              "was_code": crec["was_code"]})
                del mappings[sid]
                unmapped[sid] = {"spcpt_id": sid,
                                 "name": r.get("sme_name") or "",
                                 "reason": reason}
                r.pop("resolved_code", None)
                r.pop("official_id", None)
                r.pop("official_wording", None)
                r.pop("tier", None)
                r.pop("method", None)
                r["reason"] = reason
                stats["unresolved"] += 1
                continue

            # --- class 4: pending-reason update ---
            if crec.get("verdict") == "pending":
                r = res_by_id.get(sid)
                if r is None:
                    errors.append(f"{lane}: {sid} missing from sidecar")
                    continue
                if r.get("resolved_code"):
                    errors.append(
                        f"{lane}: {sid} pending-reason update refused "
                        f"(entry is resolved)")
                    continue
                reason = crec.get("pending_reason") or ""
                if not reason:
                    errors.append(f"{lane}: {sid} empty pending_reason")
                    continue
                r["reason"] = reason
                stats["reason_updated"] += 1
                continue

            # --- classes 1/2: resolve or refine ---
            if "codes" not in crec:
                errors.append(f"{lane}: {sid} record without codes or verdict")
                continue
            codes = [str(c) for c in crec["codes"]]
            lead = by_id.get(crec.get("official_id"))
            expected = None
            if lead is not None:
                expected = lead.get("official_code") or \
                    lead["id"].rsplit(":", 1)[-1]
            if lead is None or expected != codes[0]:
                errors.append(f"{lane}: {sid} official_id/code pair mismatch "
                              f"({crec.get('official_id')} vs {codes[0]})")
                continue
            for c in codes[1:]:
                if c not in by_code:
                    errors.append(f"{lane}: {sid} twin code {c} not in registry")

            if sid in unmapped:
                del unmapped[sid]
                stats["resolved"] += 1
            elif sid in mappings and mappings[sid].get("official_code") \
                    == codes[0] and mappings[sid].get("official_id") \
                    == lead["id"]:
                if mappings[sid].get("tier") != crec["tier"]:
                    audit.append({"id": sid, "action": "record_updated",
                                  "was_tier": mappings[sid].get("tier"),
                                  "now_tier": crec["tier"]})
                    stats["record_updated"] += 1
                else:
                    stats["idempotent"] += 1
            elif sid in mappings:
                # a DIFFERENT existing code: only an explicit refinement
                if not crec.get("refinement"):
                    errors.append(f"{lane}: {sid} mapped elsewhere "
                                  f"({mappings[sid].get('official_code')})")
                    continue
                if mappings[sid].get("official_code") != crec.get("was_code"):
                    errors.append(
                        f"{lane}: {sid} refinement was_code "
                        f"{crec.get('was_code')} != mapped "
                        f"{mappings[sid].get('official_code')}")
                    continue
                audit.append({"id": sid, "action": "refinement",
                              "was_code": crec["was_code"],
                              "now_code": codes[0]})
                stats["refined"] += 1
            else:
                stats["resolved_from_neither"] += 1

            mappings[sid] = {"official_id": lead["id"],
                             "official_code": codes[0],
                             "tier": crec["tier"], "method": METHOD}
            if crec.get("cross_unit"):
                mappings[sid]["cross_unit"] = True
            r = res_by_id.get(sid)
            if r is None:
                errors.append(f"{lane}: {sid} missing from sidecar")
                continue
            r.update({"resolved_code": codes[0], "official_id": lead["id"],
                      "official_wording": lead["text"],
                      "tier": crec["tier"], "method": METHOD})
            if crec.get("cross_unit"):
                r["cross_unit"] = True
            r.pop("reason", None)

        # population closure
        index_ids = set(idx.get("spec_points", {}))
        mapped, tail = set(mappings), set(unmapped)
        if mapped & tail:
            errors.append(f"{lane}: both mapped+unmapped: "
                          f"{sorted(mapped & tail)[:3]}")
        extra = (tail - index_ids) | (mapped - index_ids)
        if extra:
            errors.append(f"{lane}: not in index: {sorted(extra)[:3]}")
        res_missing = [i for i in index_ids if i not in res_by_id]
        if res_missing:
            errors.append(f"{lane}: index ids missing from sidecar: "
                          f"{res_missing[:3]}")

        mp["unmapped"] = [unmapped[k] for k in sorted(unmapped)]
        mp["generated_utc"] = NOW
        res["generated_utc"] = NOW
        res["counts"] = {"ids": len(index_ids), "resolved": len(mapped),
                         "unresolved": len(tail)}
        res["validation"] = (
            "AI_VALIDATED (operator-delegated chain; T-SPEC-10 operator "
            "reasoning round per operator instruction 2026-09-19 - mappings "
            "reasoned directly against the committed registries and the "
            "official Pearson PDFs, no scripted matching, no upstream "
            "tickets, PMT excluded as source); HUMAN_VALIDATED via operator "
            "review")

        def _content(d):
            return {k: v for k, v in d.items() if k != "generated_utc"}

        unchanged = (_content(mp) == _content(mp_orig)
                     and _content(res) == _content(res_orig))
        if not unchanged:
            mp_path.write_text(json.dumps(mp, indent=1, ensure_ascii=False)
                               + "\n")
            res_path.write_text(json.dumps(res, indent=1, ensure_ascii=False)
                                + "\n")
        report["per_lane"][lane] = {"stats": dict(stats),
                                    "audit": audit,
                                    "resolved_total": len(mapped),
                                    "unresolved_total": len(tail)}
        print(f"{lane}: {dict(stats)} "
              + ("(unchanged) " if unchanged else "")
              + f"-> resolved {len(mapped)}, tail {len(tail)}")

    if errors:
        for e in errors:
            print("ERROR:", e)
        return 1

    # ---------- pass 2: part-code refresh (id-derived union) ----------
    refresh = {}
    for lane in lanes_hit:
        qual, _mode = LANES[lane]
        cdir = EQ / lane
        mp = json.loads((cdir / "spec_point_map.json").read_text())
        refresh[lane] = mp.get("mappings", {})
    for lane, mappings in refresh.items():
        cdir = EQ / lane
        coded = uncoded = 0
        for f in topic_files(cdir):
            t = json.loads(f.read_text())
            changed = False
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    sids = p.get("spec_point_ids") or []
                    if not sids:
                        continue
                    codes, seen = [], set()
                    for s in sids:
                        m = mappings.get(s)
                        if m and m["official_code"] not in seen:
                            codes.append(m["official_code"])
                            seen.add(m["official_code"])
                    if codes:
                        if p.get("spec_point_codes") != codes:
                            changed = True
                        p["spec_point_codes"] = codes
                        coded += 1
                    else:
                        # preserve part-level override codes (2e/9 pattern)
                        if p.get("spec_point_codes"):
                            coded += 1
                        else:
                            uncoded += 1
            if changed:
                f.write_text(json.dumps(t, indent=1, ensure_ascii=False)
                             + "\n")
        report["per_lane"][lane]["parts_coded"] = coded
        report["per_lane"][lane]["parts_uncoded"] = uncoded

    # ---------- manifest counts refresh ----------
    for lane in lanes_hit:
        cdir = EQ / lane
        coded = uncoded = 0
        for f in topic_files(cdir):
            t = json.loads(f.read_text())
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    if p.get("spec_point_ids"):
                        if p.get("spec_point_codes"):
                            coded += 1
                        else:
                            uncoded += 1
        mpath = cdir / "manifest.json"
        if mpath.exists():
            man = json.loads(mpath.read_text())
            man_orig = copy.deepcopy(man)
            man.setdefault("spec_point_resolution", {}).setdefault(
                "counts", {}).update({
                    "parts_with_codes": coded,
                    "parts_left_uncoded_no_guess_tail": uncoded,
                    "parts_total": coded + uncoded})
            # sorted: set->list was order-nondeterministic across runs
            man["spec_point_resolution"]["pipeline"] = sorted(set(
                man["spec_point_resolution"].get("pipeline", []) +
                ["scripts/t_spec_10_apply.py"]))
            man["spec_point_resolution"]["updated_utc"] = NOW

            def _mcontent(d):
                m = copy.deepcopy(d)
                m.get("spec_point_resolution", {}).pop("updated_utc", None)
                return m

            if _mcontent(man) != _mcontent(man_orig):
                mpath.write_text(json.dumps(man, indent=1,
                                            ensure_ascii=False) + "\n")

    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "T_SPEC_10_APPLY.json").write_text(
        json.dumps(report, indent=1, ensure_ascii=False) + "\n")
    print("report -> graph/reports/T_SPEC_10_APPLY.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
