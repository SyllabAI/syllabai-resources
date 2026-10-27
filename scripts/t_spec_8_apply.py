#!/usr/bin/env python3
"""T-SPEC-8 — apply the stage-2 re-verdicts (scripts/t_spec_8_verdicts.yaml)
to the lanes affected by the parse repairs / registry corrections:

  maths-a   igcse-maths-a-18-{foundation,higher},
            igcse-maths-a-modular-24-{foundation,higher}-unit-{1,2}
  ial maths ial-maths-20-decision-1
  accounting igcse-accounting-17-financial-statements,
             igcse-accounting-17-introduction-to-bookkeeping-and-accounting

Semantics (fail-closed, per lane):
  - verdict course entry with `codes`  -> the tag must sit in the lane's
    unmapped tail (or already carry the same mapping - idempotent re-run);
    every code must exist in the lane's own registry pool; the tag moves from
    unmapped to mappings (lead code + twin_codes) and the resolution sidecar
    record is updated.
  - verdict course entry with `reason` -> pending tail: the reason is replaced
    with the corrected one (T-SPEC-7's "committed parse dropped it" claim was
    wrong for the maths-a Higher walk); a stage-1 mapping that contradicts the
    pending would be demoted (none exist for these lanes).
  - population closure: after apply, every index id is either mapped or in the
    unmapped tail with a non-empty reason; resolves are consumed exactly once.

Registry pools come from t_spec_7_apply.registry_pool (same construction as
the T-SPEC-7 apply, so lane scoping rules cannot drift).
"""
import json
import sys
import datetime
from collections import Counter
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from t_spec_7_apply import LANES as LANES_7, registry_pool, topic_files  # noqa: E402

# the IAL maths lanes were applied by T-SPEC-6 (unit-scoped full registry);
# T-SPEC-8 re-verdicts only the decision-1 lane
LANES = dict(LANES_7)
LANES["ial-maths-20-decision-1"] = ("ial-maths", "D1")

BASE = Path("/home/z/my-project/download/syllabai-resources")
EQ = BASE / "SME-ExamQuestion"
PARSED = BASE / "Official-Specifications" / "parsed"
REPORTS = BASE / "graph" / "reports"

METHOD_R1 = ("operator-verdict statement join after T-SPEC-8 parse repair "
             "(PMT excluded as source)")
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def lane_pool(qual, mode, lane):
    """Registry pool for one lane. The T-SPEC-6 IAL maths lanes key on the
    D1 unit scope (repaired by T-SPEC-8 to the 15 real unit-content rows);
    everything else reuses the T-SPEC-7 construction."""
    if lane == "ial-maths-20-decision-1":
        pts = json.loads((PARSED / "ial-maths" / "spec_points.json")
                         .read_text(encoding="utf-8"))["spec_points"]
        return {p["official_code"]: p for p in pts if p.get("scope") == "D1"}
    return registry_pool(qual, mode)[0]


def main() -> int:
    doc = yaml.safe_load((BASE / "scripts" / "t_spec_8_verdicts.yaml").read_text())
    idv = doc["id_verdicts"]

    lanes_hit = sorted({lane for v in idv.values()
                        for lane in (v.get("courses") or {})})
    unknown = [l for l in lanes_hit if l not in LANES]
    if unknown:
        raise SystemExit(f"FAIL: unknown lanes in verdicts: {unknown}")

    report = {
        "schema": "syllabai.t-spec-8-apply/1.0",
        "generated_utc": NOW,
        "lanes": lanes_hit,
        "per_lane": {},
        "note": doc["note"],
    }
    errors = []

    for lane in lanes_hit:
        qual, mode = LANES[lane]
        cdir = EQ / lane
        mp_path = cdir / "spec_point_map.json"
        mp = json.loads(mp_path.read_text())
        idx = json.loads((cdir / "spec_point_index.json").read_text())
        res_path = cdir / "spec_point_resolution.json"
        res = json.loads(res_path.read_text())
        by_code = lane_pool(qual, mode, lane)
        mappings = mp.setdefault("mappings", {})
        unmapped = {u["spcpt_id"]: u for u in mp.get("unmapped", [])}
        res_by_id = {r["id"]: r for r in res["resolved"]}

        stats = Counter()
        for sid, v in idv.items():
            crec = (v.get("courses") or {}).get(lane)
            if not crec:
                continue
            if "codes" in crec:
                codes = [str(c) for c in crec["codes"]]
                missing = [c for c in codes if c not in by_code]
                if missing:
                    errors.append(f"{lane}: {sid} codes {missing} not in pool")
                    continue
                lead = by_code[codes[0]]
                existing = mappings.get(sid)
                if sid in unmapped:
                    del unmapped[sid]
                    stats["resolved"] += 1
                elif existing and existing.get("official_code") == codes[0] \
                        and existing.get("official_id") == lead["id"]:
                    stats["idempotent"] += 1
                else:
                    errors.append(
                        f"{lane}: {sid} resolve but tag is mapped elsewhere "
                        f"({(existing or {}).get('official_code')}) and not in "
                        f"unmapped tail")
                    continue
                rec = {
                    "official_id": lead["id"],
                    "official_code": codes[0],
                    "tier": v.get("tier"),
                    "method": METHOD_R1,
                }
                if len(codes) > 1:
                    rec["twin_codes"] = codes[1:]
                mappings[sid] = rec
                r = res_by_id.get(sid)
                if r is None:
                    errors.append(f"{lane}: {sid} missing from resolution sidecar")
                    continue
                r.update({
                    "resolved_code": codes[0],
                    "official_id": lead["id"],
                    "official_wording": lead["text"],
                    "tier": v.get("tier"),
                    "method": METHOD_R1,
                })
                r.pop("reason", None)
            else:
                reason = crec.get("reason") or "no-guess pending (T-SPEC-8)"
                if sid in mappings:
                    # demote any stage-1 mapping contradicted by the pending
                    del mappings[sid]
                    stats["demoted"] += 1
                cur = unmapped.get(sid)
                if cur is None:
                    unmapped[sid] = {"spcpt_id": sid, "reason": reason}
                    stats["pending_new"] += 1
                else:
                    if cur.get("reason") != reason:
                        stats["reason_corrected"] += 1
                    cur["reason"] = reason

        # ---------- population closure ----------
        index_ids = set(idx.get("spec_points", {}))
        mapped = set(mappings)
        tail = set(unmapped)
        if mapped & tail:
            errors.append(f"{lane}: ids both mapped and unmapped: {sorted(mapped & tail)[:3]}")
        missing = index_ids - mapped - tail
        if missing:
            errors.append(f"{lane}: ids in neither map nor tail: {sorted(missing)[:3]}")
        extra = (tail - index_ids) | (mapped - index_ids)
        if extra:
            errors.append(f"{lane}: ids not in index: {sorted(extra)[:3]}")
        for sid, u in unmapped.items():
            if not (u.get("reason") or "").strip():
                errors.append(f"{lane}: {sid} unmapped without reason")

        mp["unmapped"] = [unmapped[k] for k in sorted(unmapped)]
        mp["generated_utc"] = NOW
        res["generated_utc"] = NOW
        res["counts"] = {"ids": len(index_ids), "resolved": len(mapped),
                         "unresolved": len(tail)}
        res["validation"] = (
            "AI_VALIDATED (operator-delegated chain; T-SPEC-8 stage-2 "
            "re-verdicts after parse repair - statement joins quoted verbatim "
            "from the repaired registries; PMT excluded as source); "
            "HUMAN_VALIDATED via operator review")
        mp_path.write_text(json.dumps(mp, indent=1, ensure_ascii=False) + "\n")
        res_path.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")

        # part codes refresh: id-derived union across each part's tag ids
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
                        if p.get("spec_point_codes"):
                            p.pop("spec_point_codes", None)
                            changed = True
                        uncoded += 1
            if changed:
                f.write_text(json.dumps(t, indent=1, ensure_ascii=False) + "\n")

        report["per_lane"][lane] = {
            "stats": dict(stats),
            "resolved_total": len(mapped),
            "unresolved_total": len(tail),
            "parts_coded": coded,
            "parts_uncoded": uncoded,
        }
        print(f"{lane}: {dict(stats)} -> resolved {len(mapped)}, "
              f"tail {len(tail)}")

    if errors:
        for e in errors:
            print("ERROR:", e)
        return 1

    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "T_SPEC_8_APPLY.json").write_text(
        json.dumps(report, indent=1, ensure_ascii=False) + "\n")
    print("report -> graph/reports/T_SPEC_8_APPLY.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
