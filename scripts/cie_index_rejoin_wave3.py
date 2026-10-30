#!/usr/bin/env python3
"""
T-SPECS-CIE-REJOIN-3 — index re-join for the EQ/FC wave-growth sidecars
(the JOIN-3 record follow-on #1, the index re-join class; operator directive
"fire that consume lane", 2026-10-30, zai-web, gateway trace 1a18bc6701800065).

Re-fires the wave3 lanes' pending spec-point references against the CANONICAL
per-course spec-point indexes (the T-SPECS-CIE-REJOIN-1/2 machinery, ported —
NOT re-decided):

  J1_definition_text_identity   norm(definition) == norm(official point text),
                                unique in the lane pool
  J2_definition_phrase_identity token-bounded norm(definition) phrase in
                                exactly one official point text
  J3_name_text_identity         norm(name) == norm(official point text),
                                unique — fired ONLY where the verdict lane's
                                name rules did not already evaluate the pair
                                (the ZERO_LANES verdict-exhaustion gate)
  J4_name_phrase_identity       token-bounded norm(name) phrase in exactly one
                                official point text (same scoping as J3)

Definition evidence is assembled corpus-wide (own lane + sibling lanes
holding the same spcpt id + cross_lane_join records) and must agree under the
lineage normalization SPEC or the pair stays pending
(definition_conflict_across_lanes). Pools carry the JOIN-1 lane scoping
(vf.lane_pool — 0654 sciences, 0580/0607 tiers, 9709 components; the wave3
lanes carry no parse-printed scope markers — the JOIN-2 scope table does not
list them, the unscoped doctrine applies). The verdict-exhaustion gate bites
ONLY on cie-igcse-accounting-21 (the one wave3 lane in vf.ZERO_LANES).

Application (the verdict-fill pattern, additive): items' pendings referencing
a resolved (lane, sid) cascade code entries {official_id, official_code,
tier: J*, method: cie_index_rejoin_wave3} (deduped per item by official_id)
and leave the pending list; totals recomputed; the census lands INSIDE the
lane's additive anchors.wave3 block (rejoin3 key) — the of-record
anchors.rejoin / review_state.rejoin blocks of the 44-class lanes are
byte-untouched; review_state.wave3 gains the additive rejoin3 sub-block whose
state is SUGGESTED (AGENT.md rule 2). The wave3 quarantine census of JOIN-3
is enforced: the (item, code) pairs it recorded are re-suppressed at this
cascade (they left no pending refs — enforced structurally; battery RJ-W).

Determinism: fixed stamp, every base read from HEAD (sidecars, manifest,
indexes), sorted iteration, byte-idempotent pre-commit re-runs.
Output: graph/reports/T_SPECS_CIE_WAVE3_REJOIN.json +
scripts/cie_wave3_resolutions.yaml (the REJOIN-3 sheet; consumed by the v2
consume engine's stage B as SHEET3 via "REJOIN-3:gate-3").
"""
from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO = Path("/home/z/my-project/syllabai-resources")
REPORTS = REPO / "graph" / "reports"
SPEC_LINKS = REPO / "spec-links"

STAMP = "2026-10-30T09:30:00Z"
DIRECTIVE = "fire that consume lane"
TRACE = "1a18bc6701800065"
FIRES = "T-SPECS-CIE-JOIN-3 record follow-on #1 (the index re-join class)"
METHOD = "cie_index_rejoin_wave3"
RULES = {
    "J1_definition_text_identity":
        "norm(definition) == norm(official point text), unique in the lane pool",
    "J2_definition_phrase_identity":
        "token-bounded norm(definition) phrase in exactly one official point text",
    "J3_name_text_identity":
        "norm(name) == norm(official point text), unique in the lane pool",
    "J4_name_phrase_identity":
        "token-bounded norm(name) phrase in exactly one official point text",
}
LANES_3 = [
    "cie-a-level-biology-25",
    "cie-a-level-chemistry-25",
    "cie-a-level-physics-25",
    "cie-as-accounting-21",
    "cie-as-biology-25",
    "cie-igcse-accounting-21",
    "cie-igcse-biology-23",
    "cie-igcse-chemistry-23",
    "cie-igcse-physics-23",
]
REJOIN_NOTE = ("index re-join cures applied additively to the wave3 lanes' "
               "pending anchors; pairs with no identity evidence stay pending "
               "honestly (AGENT.md rule 3)")
STATS_OUT = REPORTS / "T_SPECS_CIE_WAVE3_REJOIN.json"
SHEET_OUT = REPO / "scripts" / "cie_wave3_resolutions.yaml"

sys.path.insert(0, str(REPO / "scripts"))
import cie_verdict_fill as vf  # noqa: E402
import cie_xlane_join as xj  # noqa: E402
import cie_spec_join as base  # noqa: E402


def git(*args: str, binary: bool = False):
    r = subprocess.run(["git", "-C", str(REPO), *args],
                       capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode("utf-8", "replace")


def pin_json(sha: str, path: str):
    return json.loads(git("show", f"{sha}:{path}"))


def context_lanes() -> list[str]:
    out = git("ls-tree", "-r", "--name-only", "HEAD", "spec-links/")
    return sorted(line.rsplit("/", 1)[1][:-5]
                  for line in out.splitlines()
                  if line.startswith("spec-links/cie-")
                  and line.endswith(".json"))


def main() -> int:
    sha = git("rev-parse", "HEAD").strip()
    print(f"HEAD pin {sha[:12]}; stamp {STAMP}")

    lane_to_qual, quals = base.load_manifest()
    unknown = [l for l in LANES_3 if l not in lane_to_qual]
    if unknown:
        print(f"FATAL: lanes not in the spec manifest: {unknown}")
        return 1
    ctx = sorted(context_lanes())
    for l in LANES_3:
        if l not in ctx:
            print(f"FATAL: engine lane {l} has no sidecar at HEAD")
            return 1
    print(f"context lanes (cie-* sidecars): {len(ctx)}; engine lanes: {len(LANES_3)}")

    sidecars = {l: pin_json(sha, f"spec-links/{l}.json") for l in LANES_3}

    indexes: dict[str, dict] = {}
    for l in ctx:
        try:
            indexes[l] = json.loads(xj.head_index_bytes(l))
        except Exception:
            if l in LANES_3:
                print(f"FATAL: engine lane {l} has no spec_point_index.json")
                return 1
    universes = {l: set(indexes[l]["spec_points"]) for l in LANES_3 if l in indexes}

    def_holders: dict[str, list[str]] = {}
    for l in ctx:
        if l not in indexes:
            continue
        for sid, e in indexes[l]["spec_points"].items():
            if e["definition"]:
                def_holders.setdefault(sid, []).append(l)
    xjoin_resolved = {}
    for l in ctx:
        if l not in indexes:
            continue
        for sid, e in (indexes[l].get(xj.BLOCK_KEY, {})
                       .get("resolved", {}) or {}).items():
            xjoin_resolved[(l, sid)] = e

    pools: dict[str, list] = {}
    texts: dict[str, list] = {}
    pool_ids: dict[str, dict] = {}
    regs: dict[str, dict] = {}
    for l in LANES_3:
        qual = sidecars[l]["qual"]
        if qual not in regs:
            regs[qual] = vf.load_registry(qual)
        pools[l] = vf.lane_pool(l, regs[qual])
        texts[l] = [(p, vf.norm(p.get("text"))) for p in pools[l]]
        pool_ids[l] = {p["id"]: str(p.get("official_code")) for p in pools[l]}

    refs_total = 0
    pairs: dict[tuple, int] = {}
    for l in LANES_3:
        for key, it in sidecars[l]["items"].items():
            for sid in (it.get("pending") or []):
                refs_total += 1
                pairs[(l, sid)] = pairs.get((l, sid), 0) + 1
    print(f"pending refs {refs_total} -> unique pairs {len(pairs)}")

    def assemble(lane: str, sid: str) -> dict:
        own = indexes[lane]["spec_points"].get(sid)
        defs: dict[str, tuple[str, str]] = {}
        if own and own["definition"]:
            defs.setdefault(vf.norm(own["definition"]),
                            (own["definition"], "own"))
        for m in sorted(def_holders.get(sid, ())):
            if m == lane:
                continue
            d = indexes[m]["spec_points"][sid]["definition"]
            defs.setdefault(vf.norm(d), (d, f"sibling:{m}"))
        xe = xjoin_resolved.get((lane, sid))
        if xe and xe["grade"] == "definition":
            defs.setdefault(vf.norm(xe["definition"]),
                            (xe["definition"], "cross_lane_join"))
        if own:
            name, name_source = own["name"], "own"
        elif xe:
            name, name_source = xe["name"], "cross_lane_join"
        else:
            name, name_source = "", ""
        if len(defs) > 1:
            return {"conflict": True, "name": name,
                    "name_source": name_source,
                    "variants": sorted({t for t, _ in defs.values()})}
        if defs:
            pref = [d for d in defs.values() if d[1] == "own"] or \
                   [d for d in defs.values() if d[1] == "cross_lane_join"] or \
                   sorted(defs.values(), key=lambda v: v[1])
            dtext, dsource = pref[0]
            corr = sorted({s for _, s in defs.values()} - {dsource})
        else:
            dtext, dsource, corr = "", "", []
        return {"conflict": False, "name": name, "name_source": name_source,
                "def_text": dtext, "def_norm": vf.norm(dtext),
                "def_source": dsource, "corroborating": corr}

    resolves: dict[tuple, dict] = {}
    ambiguous: dict[tuple, dict] = {}
    stays: Counter = Counter()
    verdict_evaluated_pairs = 0
    for (l, sid) in sorted(pairs):
        ev = assemble(l, sid)
        tlist = texts[l]
        verdict_evaluated = l in vf.ZERO_LANES and sid in universes[l]
        if verdict_evaluated:
            verdict_evaluated_pairs += 1
        if ev["conflict"]:
            ambiguous[(l, sid)] = {
                "lane": l, "reason": "definition_conflict_across_lanes",
                "variants": ev["variants"]}
            continue
        hit = None
        if ev["def_norm"]:
            eq = [p for p, t in tlist if t and t == ev["def_norm"]]
            if len(eq) == 1:
                hit = ("J1_definition_text_identity", eq[0])
            elif len(eq) > 1:
                ambiguous[(l, sid)] = {
                    "lane": l, "reason": "definition_eq_multi_text",
                    "matched_codes": sorted(str(p.get("official_code"))
                                            for p in eq)}
                continue
            else:
                ph = [p for p, t in tlist
                      if len(ev["def_norm"]) >= 3
                      and vf.phrase_in(ev["def_norm"], t)]
                if len(ph) == 1:
                    hit = ("J2_definition_phrase_identity", ph[0])
                elif len(ph) > 1:
                    ambiguous[(l, sid)] = {
                        "lane": l, "reason": "definition_phrase_multi_text",
                        "matched_codes": sorted(str(p.get("official_code"))
                                                for p in ph)}
                    continue
        if hit is None and not verdict_evaluated and ev["name"]:
            nn = vf.norm(ev["name"])
            eq = [p for p, t in tlist if t and t == nn]
            if len(eq) == 1:
                hit = ("J3_name_text_identity", eq[0])
            elif len(eq) > 1:
                ambiguous[(l, sid)] = {
                    "lane": l, "reason": "name_eq_multi_text",
                    "matched_codes": sorted(str(p.get("official_code"))
                                            for p in eq)}
                continue
            else:
                ph = [p for p, t in tlist
                      if len(nn) >= 3 and vf.phrase_in(nn, t)]
                if len(ph) == 1:
                    hit = ("J4_name_phrase_identity", ph[0])
                elif len(ph) > 1:
                    ambiguous[(l, sid)] = {
                        "lane": l, "reason": "name_phrase_multi_text",
                        "matched_codes": sorted(str(p.get("official_code"))
                                                for p in ph)}
                    continue
        if hit is not None:
            rule, op = hit
            resolves[(l, sid)] = {
                "lane": l, "verdict": "resolve", "tier": rule,
                "official_id": op["id"],
                "official_code": str(op.get("official_code")),
                "evidence": {
                    "sme_name": ev["name"],
                    "sme_definition": ev["def_text"],
                    "evidence_source": (ev["def_source"] if rule.startswith(
                        ("J1", "J2")) else ev["name_source"]),
                    "corroborating_sources": ev["corroborating"],
                    "official_text": op.get("text"),
                    "rule": RULES[rule],
                },
            }
        else:
            if verdict_evaluated:
                stays["no_new_evidence_verdict_evaluated"] += 1
            elif not ev["name"] and not ev["def_text"]:
                stays["recordless_no_corpus_record"] += 1
            else:
                stays["no_identity_evidence"] += 1

    print(f"resolves {len(resolves)}  ambiguous {len(ambiguous)}  "
          f"stays {dict(stays)}  verdict_evaluated {verdict_evaluated_pairs}")

    # ---- fail-closed validation before any write
    errors = []
    for (l, sid), v in sorted(resolves.items()):
        if (l, sid) not in pairs:
            errors.append(f"{l}:{sid}:resolved pair was not pending")
        if sid not in universes[l] and (l, sid) not in xjoin_resolved:
            errors.append(f"{l}:{sid}:no corpus record for the id")
        ids = pool_ids[l]
        if v["official_id"] not in ids:
            errors.append(f"{l}:{sid}:dangling official id {v['official_id']}")
        elif ids[v["official_id"]] != v["official_code"]:
            errors.append(f"{l}:{sid}:code mismatch")
        if v["tier"] not in RULES:
            errors.append(f"{l}:{sid}:tier vocab")
    if errors:
        for e in errors:
            print("FAIL-CLOSED:", e)
        return 1

    # ---- apply to the touched sidecars (verdict-fill pattern, additive blocks)
    touched_lanes = sorted({l for (l, _s) in resolves})
    per_lane = {}
    for l in touched_lanes:
        d = sidecars[l]
        items = d["items"]
        code_by_sid = {sid: (v["official_id"], v["official_code"], v["tier"])
                       for (ll, sid), v in resolves.items() if ll == l}
        refs_before = refs_after = 0
        resolved_refs = 0
        for key in sorted(items):
            it = items[key]
            pend = it.get("pending") or []
            if not pend:
                continue
            refs_before += len(pend)
            keep, new_codes = [], []
            for sid in pend:
                if sid in code_by_sid:
                    resolved_refs += 1
                    oid, ocode, tier = code_by_sid[sid]
                    if not any(c.get("official_id") == oid
                               for c in (it.get("codes") or [])):
                        new_codes.append({"official_id": oid,
                                          "official_code": ocode,
                                          "tier": tier, "method": METHOD})
                else:
                    keep.append(sid)
            if new_codes:
                it["codes"] = (it.get("codes") or []) + new_codes
            it["pending"] = keep
            refs_after += len(keep)
        added = sum(1 for it in items.values()
                    for c in (it.get("codes") or [])
                    if c.get("method") == METHOD)
        t = d["totals"]
        by = {"notes": 0, "question_parts": 0, "flashcards": 0}
        coded = {"notes": 0, "question_parts": 0, "flashcards": 0}
        for it in items.values():
            by[it["kind"] + "s"] += 1
            coded[it["kind"] + "s"] += 1 if it["codes"] else 0
        t["by_kind"] = by
        t["coded_by_kind"] = coded
        t["items_with_codes"] = sum(coded.values())
        amb_l = [a for (ll, _s), a in ambiguous.items() if ll == l]
        res_l = {sid: v for (ll, sid), v in resolves.items() if ll == l}
        a = d["anchors"]
        a["pending_refs"] = refs_after
        w3 = a.get("wave3") or {}
        w3["rejoin3"] = {
            "lane": "T-SPECS-CIE-REJOIN-3", "applied_utc": STAMP,
            "resolved_pairs": len(res_l),
            "resolved_refs": resolved_refs,
            "code_entries_added": added,
            "by_rule": {k: sum(1 for v in res_l.values() if v["tier"] == k)
                        for k in sorted(RULES)},
            "ambiguous_pairs": len(amb_l),
            "pending_refs_after": refs_after,
            "note": REJOIN_NOTE,
        }
        a["wave3"] = w3
        rs = d["review_state"]
        w3rs = rs.get("wave3") or {}
        w3rs["rejoin3"] = {
            "state": "SUGGESTED", "lane": "T-SPECS-CIE-REJOIN-3",
            "directive": DIRECTIVE, "gateway_trace": TRACE,
            "applied_utc": STAMP,
        }
        rs["wave3"] = w3rs
        (SPEC_LINKS / f"{l}.json").write_text(
            json.dumps(d, indent=1, ensure_ascii=False) + "\n",
            encoding="utf-8")
        per_lane[l] = {"resolved_pairs": len(res_l),
                       "resolved_refs": resolved_refs,
                       "code_entries_added": added,
                       "ambiguous": len(amb_l),
                       "pending_refs_after": refs_after}
        print(f"[{l}] resolves={len(res_l)} refs_cured={resolved_refs} "
              f"codes+{added} pending {refs_before}->{refs_after}", flush=True)

    manifest_path = SPEC_LINKS / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    pre_blocks = json.dumps({k: v for k, v in manifest.items()
                             if k not in ("courses", "generated_utc")},
                            sort_keys=True)
    if touched_lanes:
        manifest["generated_utc"] = STAMP
        manifest["cie_wave3_rejoin"] = {
        "lane": "T-SPECS-CIE-REJOIN-3",
        "review_state": "SUGGESTED",
        "lanes": len(touched_lanes),
        "resolved_pairs": len(resolves),
        "operator_directive": f"{DIRECTIVE} (gateway trace {TRACE})",
        "fires": FIRES,
    }
        manifest_path.write_text(
            json.dumps(manifest, indent=1, ensure_ascii=False) + "\n",
            encoding="utf-8")
    drifted = [k for k, v in json.loads(pre_blocks).items()
               if manifest.get(k) != v]
    if drifted:
        print("FATAL: pre-existing manifest blocks drifted:", drifted)
        return 1

    if not touched_lanes:
        print("no-op re-run: sidecars, manifest and sheet byte-identical")
        STATS_OUT.write_text(json.dumps({
            "lane": "T-SPECS-CIE-REJOIN-3", "stamp": STAMP, "pin": sha,
            "lanes": {}, "totals": {"pending_refs_before": refs_total,
                                    "unique_pairs": len(pairs),
                                    "resolved_pairs": 0,
                                    "ambiguous_pairs": 0,
                                    "stays": dict(stays),
                                    "verdict_evaluated_pairs":
                                        verdict_evaluated_pairs},
        }, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        return 0

    sheet = {"schema": "syllabai.cie-rejoin-resolutions/1.0",
             "lane": "T-SPECS-CIE-REJOIN-3",
             "stamp": STAMP,
             "directive": DIRECTIVE, "gateway_trace": TRACE,
             "verdicts": [resolves[k] for k in sorted(resolves)],
             "ambiguous": [dict(a, lane=l, id=sid)
                           for (l, sid), a in sorted(ambiguous.items())]}
    SHEET_OUT.write_text(yaml.safe_dump(sheet, sort_keys=False,
                                        allow_unicode=True),
                         encoding="utf-8")

    STATS_OUT.write_text(json.dumps({
        "lane": "T-SPECS-CIE-REJOIN-3", "stamp": STAMP, "pin": sha,
        "lanes": per_lane,
        "totals": {"pending_refs_before": refs_total,
                   "unique_pairs": len(pairs),
                   "resolved_pairs": len(resolves),
                   "ambiguous_pairs": len(ambiguous),
                   "stays": dict(stays),
                   "verdict_evaluated_pairs": verdict_evaluated_pairs},
    }, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"sheet {SHEET_OUT.name}: {len(resolves)} resolve rows, "
          f"{len(ambiguous)} ambiguous")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
