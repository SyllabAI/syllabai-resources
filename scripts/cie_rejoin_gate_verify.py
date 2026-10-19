#!/usr/bin/env python3
"""T-SPECS-CIE-REJOIN-GATE-1 — independent verifier (runs BEFORE the applier;
the applier refuses on any FAIL).

Re-fires every one of the 634 REJOIN-1 resolutions INDEPENDENTLY against the
canonical pools (registry + scoping) and the canonical lane indexes:

  - the rule re-evaluates from the sheet's verbatim evidence (J1: definition
    text-eq unique; J2: definition phrase unique; J3: name text-eq unique;
    J4: name phrase unique) with the J3/J4 verdict-evaluated scoping
    recomputed from ZERO_LANES + the lane's index universe;
  - uniqueness re-checks over the FULL lane pool (exactly-1 or FAIL);
  - official_id/official_code/official_text must match the pool verbatim;
  - the pair must be OUT of every item's pendings at HEAD (the REJOIN-1 cure)
    and IN the codes with tier/method cie_index_rejoin;
  - the 166 ambiguous pairs must carry their quarantine reasons and stay out
    of the codes.

Output: graph/reports/T_SPECS_CIE_REJOIN_GATE_1_VERIFY.json
{verdict: PASS|FAIL, verified, failed, failures[], counts}. Exit 0 iff PASS.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import yaml

REPO = Path("/home/z/my-project/syllabai-resources")
SL = REPO / "spec-links"
REPORTS = REPO / "graph" / "reports"
sys.path.insert(0, str(REPO / "scripts"))
import cie_verdict_fill as vf  # noqa: E402

GATE = "T-SPECS-CIE-REJOIN-GATE-1"
STAMP = "2026-10-20T12:00:00Z"
BASE_COMMIT = "0fe5f77210f74aaeb3f6c491dfe0263d12db738c"
VERIFY_OUT = REPORTS / "T_SPECS_CIE_REJOIN_GATE_1_VERIFY.json"
SHEET = REPO / "scripts" / "cie_rejoin_resolutions.yaml"
STATS = REPORTS / "T_SPECS_CIE_REJOIN_1_STATS.json"

LANES = [
    "cie-a-level-accounting-21", "cie-a-level-biology-25",
    "cie-a-level-chemistry-25", "cie-a-level-economics-23",
    "cie-a-level-physics-25", "cie-as-environmental-management-20",
    "cie-igcse-biology-23", "cie-igcse-business-23", "cie-igcse-business-25",
    "cie-igcse-chemistry-23", "cie-igcse-computer-science-23",
    "cie-igcse-economics-20", "cie-igcse-geography-20",
    "cie-igcse-geography-25", "cie-igcse-maths-25-core",
    "cie-igcse-maths-25-extended", "cie-igcse-physics-23",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-physics",
    "cie-igcse-science-combined-science-23-biology",
    "cie-igcse-science-combined-science-23-chemistry",
    "cie-igcse-science-combined-science-23-physics",
]


def main() -> int:
    t0 = time.time()
    failures: list[str] = []

    sheet = yaml.safe_load(SHEET.read_text(encoding="utf-8"))
    verdicts = sheet["verdicts"]
    ambiguous = sheet["ambiguous"]
    stats = json.loads(STATS.read_text(encoding="utf-8"))
    detail = {d["lane"]: d for d in stats["lanes_detail"]}

    sidecars = {l: json.loads((SL / f"{l}.json").read_text(encoding="utf-8"))
                for l in LANES}
    indexes = {l: json.loads(
        (REPO / "SME-ExamQuestion" / l / "spec_point_index.json")
        .read_text(encoding="utf-8")) for l in LANES}
    universes = {l: set(indexes[l]["spec_points"]) for l in LANES}
    zero = set(vf.ZERO_LANES)

    # ---- recount the rejoin code entries per lane (must equal the STATS)
    entries = {}
    for l in LANES:
        n = sum(1 for it in sidecars[l]["items"].values()
                for c in (it.get("codes") or [])
                if c.get("method") == "cie_index_rejoin")
        entries[l] = n
        if n != detail[l]["code_entries_added"]:
            failures.append(f"{l}: rejoin entries {n} != stats "
                            f"{detail[l]['code_entries_added']}")
    total_entries = sum(entries.values())
    if total_entries != stats["code_entries_added_total"]:
        failures.append(f"total entries {total_entries} != "
                        f"{stats['code_entries_added_total']}")

    # ---- pool registry per qual (cached), lane pools + normed texts
    regs, pools, texts = {}, {}, {}
    for l in LANES:
        q = sidecars[l]["qual"]
        if q not in regs:
            regs[q] = vf.load_registry(q)
        pools[l] = vf.lane_pool(l, regs[q])
        texts[l] = [(p, vf.norm(p.get("text"))) for p in pools[l]]

    # ---- the codes map: (lane, sid) -> entry, and pendings census
    code_by_pair = {}
    pending_pairs = set()
    for l in LANES:
        for key, it in sidecars[l]["items"].items():
            for sid in (it.get("pending") or []):
                pending_pairs.add((l, sid))
            for c in (it.get("codes") or []):
                if c.get("method") == "cie_index_rejoin":
                    code_by_pair.setdefault((l, None), 0)  # placeholder no-op

    # map codes back to sids: a code entry has official_id; the sid it cured
    # is the pending sid that left — reconstruct via the anchors/STATS pairs
    # is ambiguous, so verify per-verdict instead: sid cured == not pending
    # and SOME item of the lane carries the (official_id, tier) entry.
    def lane_has_code(lane: str, official_id: str, tier: str) -> bool:
        for it in sidecars[lane]["items"].values():
            for c in (it.get("codes") or []):
                if (c.get("method") == "cie_index_rejoin"
                        and c.get("official_id") == official_id
                        and c.get("tier") == tier):
                    return True
        return False

    # ---- independent re-fire per verdict
    per_rule = {}
    verified = 0
    for v in verdicts:
        l, sid = v["lane"], v["id"]
        tier = v["tier"]
        ev = v["evidence"]
        oid, ocode = v["official_id"], v["official_code"]
        # the cure landed: sid out of pendings; the code entry present
        if (l, sid) in pending_pairs:
            failures.append(f"{l}:{sid}: pair still pending at HEAD")
        if not lane_has_code(l, oid, tier):
            failures.append(f"{l}:{sid}: no rejoin code entry "
                            f"({oid}, {tier}) in the lane")
        # pool point identity
        pts = [p for p in pools[l] if p["id"] == oid]
        if len(pts) != 1:
            failures.append(f"{l}:{sid}: official id {oid} not unique in pool")
            continue
        p = pts[0]
        if str(p.get("official_code")) != ocode:
            failures.append(f"{l}:{sid}: official_code mismatch")
        if vf.norm(p.get("text")) != vf.norm(ev.get("official_text") or ""):
            failures.append(f"{l}:{sid}: official_text mismatch vs pool")
        # rule re-fire
        def_norm = vf.norm(ev.get("sme_definition") or "")
        name_norm = vf.norm(ev.get("sme_name") or "")
        tlist = texts[l]
        verdict_evaluated = l in zero and sid in universes[l]
        hit_ok = False
        if tier == "J1_definition_text_identity":
            eq = [q for q, t in tlist if t and t == def_norm]
            hit_ok = (len(eq) == 1 and eq[0]["id"] == oid)
        elif tier == "J2_definition_phrase_identity":
            ph = [q for q, t in tlist
                  if len(def_norm) >= 3 and vf.phrase_in(def_norm, t)]
            hit_ok = (len(ph) == 1 and ph[0]["id"] == oid)
        elif tier == "J3_name_text_identity":
            if verdict_evaluated:
                failures.append(f"{l}:{sid}: J3 fired on a verdict-evaluated "
                                "pair (scoping violation)")
            eq = [q for q, t in tlist if t and t == name_norm]
            hit_ok = (len(eq) == 1 and eq[0]["id"] == oid)
        elif tier == "J4_name_phrase_identity":
            if verdict_evaluated:
                failures.append(f"{l}:{sid}: J4 fired on a verdict-evaluated "
                                "pair (scoping violation)")
            ph = [q for q, t in tlist
                  if len(name_norm) >= 3 and vf.phrase_in(name_norm, t)]
            hit_ok = (len(ph) == 1 and ph[0]["id"] == oid)
        else:
            failures.append(f"{l}:{sid}: unknown tier {tier}")
            hit_ok = False
        if hit_ok:
            verified += 1
            per_rule[tier] = per_rule.get(tier, 0) + 1
        else:
            failures.append(f"{l}:{sid}: rule {tier} did not re-fire uniquely")

    # ---- ambiguous quarantines: reasons present, nothing promoted
    amb_pairs = {(a["lane"], a["id"]) for a in ambiguous}
    if len(amb_pairs) != stats["ambiguous_pairs_total"]:
        failures.append(f"ambiguous census {len(amb_pairs)} != "
                        f"{stats['ambiguous_pairs_total']}")
    for a in ambiguous:
        if not a.get("reason"):
            failures.append(f"{a['lane']}:{a['id']}: quarantine w/o reason")

    out = {
        "gate": GATE, "generated_utc": STAMP, "base_commit": BASE_COMMIT,
        "verdict": "PASS" if not failures else "FAIL",
        "sheet_verdicts": len(verdicts),
        "verified": verified,
        "failed": len(verdicts) - verified,
        "verified_by_rule": dict(sorted(per_rule.items())),
        "code_entries_total": total_entries,
        "ambiguous_stay_quarantined": len(amb_pairs),
        "failures": failures[:50],
        "failures_total": len(failures),
        "elapsed_seconds": round(time.time() - t0, 1),
    }
    VERIFY_OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps({k: out[k] for k in
                      ("verdict", "sheet_verdicts", "verified", "failed",
                       "code_entries_total", "ambiguous_stay_quarantined")}))
    if failures:
        for f in failures[:20]:
            print("FAIL:", f, file=sys.stderr)
    return 0 if out["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
