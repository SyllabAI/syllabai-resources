#!/usr/bin/env python3
"""
T-SPECS-CIE-REJOIN-1 — index re-join lane (the T-SPECS-CIE-XJOIN-1 record's
NEXT lane #1; operator directive "Re-join against the index", 2026-10-19,
zai-web, gateway trace 1a15370131f93699).

Re-fires the pending spec-point references of all 44 CIE SME course lanes
against the CANONICAL per-course spec-point indexes (now cross-lane-aware)
instead of the blob-restricted evidence the original join and the verdict
lane were limited to:

  - the join lane's T1 text confirmation was gated on path-numbering
    candidates, so definition-text identities outside the candidate set
    never fired;
  - the verdict lane's V1-V5 rules were NAME-only (the honest-zero lanes
    are name-only substrates) and never used definitions;
  - the indexes now carry, corpus-wide, every id's name/definition (H4
    deep-equal to the blobs) plus the cross_lane_join cures for 54 of the
    322 dangling EQ-referenced ids.

Rules (priority order; tier == rule name, the verdict-lane pattern; a pair
resolves once, by its strongest rule; on a MULTI hit the pair quarantines —
no fall-through to weaker rules, the T-SPEC-2c doctrine):

  J1_definition_text_identity   norm(definition) == norm(official point
                                text), unique in the lane pool
  J2_definition_phrase_identity token-bounded norm(definition) phrase in
                                exactly one official point text
  J3_name_text_identity         norm(name) == norm(official point text),
                                unique — fired ONLY where the verdict lane's
                                name rules did not already evaluate the pair
                                (coded lanes + non-universe pairs)
  J4_name_phrase_identity       token-bounded norm(name) phrase in exactly
                                one official point text (same scoping as J3)

Definition evidence is assembled corpus-wide (own lane + sibling lanes
holding the same spcpt id + cross_lane_join records) and must agree under
the lineage normalization SPEC or the pair stays pending
(definition_conflict_across_lanes). Pools mirror the join/verdict scoping
(0654 scope filter, 0580/0607 tier preference, 9709 component topics).

Application (the verdict-fill pattern, additive): items' pendings referencing
a resolved (lane, sid) cascade code entries {official_id, official_code,
tier: J*, method: cie_index_rejoin} (deduped per item by official_id) and
leave the pending list; totals recomputed; anchors gains an additive
`rejoin` census block; review_state gains an additive `rejoin` block whose
state is SUGGESTED — engine-derived identity-grade joins are suggestions
until the next review/promotion gate (AGENT.md rule 2); the gate's ACCEPTED
payload and the verdict lane's authoritative entries are preserved. The 268
record-less (lane, sid) pairs stay pending honestly (rule 3).

Determinism: fixed stamp, every base read from HEAD (sidecars, manifest,
indexes), sorted iteration, byte-idempotent pre-commit re-runs.
Battery: scripts/cie_rejoin_check.py (RJ1-RJ10).
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

import yaml

REPO = Path("/home/z/my-project/syllabai-resources")
SL = REPO / "spec-links"
REPORTS = REPO / "graph" / "reports"
sys.path.insert(0, str(REPO / "scripts"))
import cie_verdict_fill as vf  # noqa: E402
import cie_xlane_join as xj  # noqa: E402

LANE_ID = "T-SPECS-CIE-REJOIN-1"
STAMP = "2026-10-19T11:00:00Z"
DIRECTIVE = "Re-join against the index"
TRACE = "1a15370131f93699"
FIRES = "T-SPECS-CIE-XJOIN-1 record NEXT lane #1"
BASE_COMMIT = "c9fc6dfb"
METHOD = "cie_index_rejoin"
RULES = {
    "J1_definition_text_identity":
        "norm(definition) == norm(official point text), unique in the lane pool",
    "J2_definition_phrase_identity":
        "token-bounded norm(definition) phrase in exactly one official point text",
    "J3_name_text_identity":
        "norm(name) == norm(official point text), unique in the lane pool "
        "(fired only where the verdict lane's name rules did not already "
        "evaluate the pair)",
    "J4_name_phrase_identity":
        "token-bounded norm(name) phrase in exactly one official point text "
        "(same scoping as J3)",
}
STATS_OUT = REPORTS / "T_SPECS_CIE_REJOIN_1_STATS.json"
SHEET_OUT = REPO / "scripts" / "cie_rejoin_resolutions.yaml"


def git(*args: str, binary: bool = False):
    r = subprocess.run(["git", "-C", str(REPO), *args],
                       capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode("utf-8", "replace")


def head_json(path: str):
    return json.loads(git("show", f"HEAD:{path}"))


def main() -> int:
    t0 = time.time()
    lanes = sorted(engine_lanes())
    print(f"CIE lanes: {len(lanes)}")

    sidecars = {l: head_json(f"spec-links/{l}.json") for l in lanes}
    indexes = {l: json.loads(xj.head_index_bytes(l)) for l in lanes}
    universes = {l: set(indexes[l]["spec_points"]) for l in lanes}

    # corpus-wide definition holders + the XJOIN cures
    def_holders: dict[str, list[str]] = {}
    for l in lanes:
        for sid, e in indexes[l]["spec_points"].items():
            if e["definition"]:
                def_holders.setdefault(sid, []).append(l)
    xjoin_resolved = {}
    for l in lanes:
        for sid, e in (indexes[l].get(xj.BLOCK_KEY, {})
                       .get("resolved", {}) or {}).items():
            xjoin_resolved[(l, sid)] = e

    # official pools per lane (join/verdict scoping), texts precomputed
    regs: dict[str, dict] = {}
    pools, texts = {}, {}
    for l in lanes:
        qual = sidecars[l]["qual"]
        if qual not in regs:
            regs[qual] = vf.load_registry(qual)
        pools[l] = vf.lane_pool(l, regs[qual])
        texts[l] = [(p, vf.norm(p.get("text"))) for p in pools[l]]
    pool_ids = {l: {p["id"]: str(p.get("official_code")) for p in pools[l]}
                for l in lanes}

    # ---- census: every pending ref, unique (lane, sid) pairs
    refs_total = 0
    pairs: dict[tuple, int] = {}
    for l in lanes:
        for key, it in sidecars[l]["items"].items():
            for sid in (it.get("pending") or []):
                refs_total += 1
                pairs[(l, sid)] = pairs.get((l, sid), 0) + 1
    print(f"pending refs {refs_total} -> unique pairs {len(pairs)}")

    zero = set(vf.ZERO_LANES)

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
            # representative: own > cross_lane_join > first sibling
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
    for (l, sid) in sorted(pairs):
        ev = assemble(l, sid)
        tlist = texts[l]
        verdict_evaluated = l in zero and sid in universes[l]
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
          f"stays {dict(stays)}")

    # ---- fail-closed validation before any write
    errors = []
    touched_lanes = sorted({l for (l, _s) in resolves})
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

    # ---- apply to the touched sidecars (verdict-fill pattern)
    per_lane = {}
    for l in touched_lanes:
        d = sidecars[l]
        items = d["items"]
        code_by_sid = {sid: (v["official_id"], v["official_code"], v["tier"])
                       for (ll, sid), v in resolves.items() if ll == l}
        added = 0
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
        # universe_resolved carries TWO lineage semantics: the verdict fill
        # redefined it as universe_ids - pending-universe-sids on the 25
        # zero lanes, while the 19 coded lanes keep the JOIN's original
        # text-resolved count. Recompute ONLY where the verdict semantics
        # live (anchors.verdict present); coded lanes keep their join value.
        if "verdict" in a:
            pend_universe = {sid for it in items.values()
                             for sid in (it.get("pending") or [])
                             if sid in universes[l]}
            a["universe_resolved"] = int(a["universe_ids"]) - len(pend_universe)
        a["pending_refs"] = refs_after
        a["rejoin"] = {
            "lane": LANE_ID, "applied_utc": STAMP,
            "resolved_pairs": len(res_l),
            "resolved_refs": resolved_refs,
            "by_rule": {k: sum(1 for v in res_l.values() if v["tier"] == k)
                        for k in sorted(RULES)},
            "ambiguous_pairs": len(amb_l),
            "pending_refs": refs_after,
            "note": ("index re-join cures applied additively; the 268 "
                     "record-less (lane, id) pairs stay pending honestly "
                     "(AGENT.md rule 3)"),
        }
        rs = d["review_state"]
        rs["rejoin"] = {
            "lane": LANE_ID, "directive": DIRECTIVE, "gateway_trace": TRACE,
            "applied_utc": STAMP, "base_commit": BASE_COMMIT,
            "method": METHOD, "tiers": dict(sorted(RULES.items())),
            "state": "SUGGESTED",
            "note": ("engine-derived identity-grade index re-join resolutions "
                     "on the pending anchors; SUGGESTED pending the next "
                     "review/promotion gate per AGENT.md rule 2; the gate's "
                     "ACCEPTED payload and the verdict lane's authoritative "
                     "entries are preserved"),
        }
        (SL / f"{l}.json").write_text(
            json.dumps(d, indent=1, ensure_ascii=False) + "\n")
        per_lane[l] = {
            "resolved_pairs": len(res_l),
            "resolved_refs": resolved_refs,
            "code_entries_added": added,
            "by_rule": a["rejoin"]["by_rule"],
            "ambiguous_pairs": len(amb_l),
            "pending_refs_before": refs_before,
            "pending_refs_after": refs_after,
            "items_with_codes": t["items_with_codes"],
        }
        print(f"[{l}] pairs {len(res_l)} refs {resolved_refs} codes {added} "
              f"pending {refs_before} -> {refs_after}")

    # ---- manifest
    manifest = head_json("spec-links/manifest.json")
    for l in touched_lanes:
        row = manifest["courses"].get(l)
        if not row:
            continue
        d = sidecars[l]
        t = d["totals"]
        row["items"] = t["items"]
        row["items_with_codes"] = t["items_with_codes"]
        row["by_kind"] = t["by_kind"]
        row["coded_by_kind"] = t["coded_by_kind"]
        row["pending_refs"] = d["anchors"]["pending_refs"]
        row["rejoin"] = {
            "lane": LANE_ID,
            "resolved_pairs": per_lane[l]["resolved_pairs"],
            "resolved_refs": per_lane[l]["resolved_refs"],
            "by_rule": per_lane[l]["by_rule"],
        }
    manifest["cie_rejoin"] = {
        "lane": LANE_ID, "applied_utc": STAMP, "directive": DIRECTIVE,
        "gateway_trace": TRACE, "base_commit": BASE_COMMIT,
        "lanes": len(touched_lanes),
        "resolved_pairs_total": sum(v["resolved_pairs"]
                                    for v in per_lane.values()),
        "code_entries_added_total": sum(v["code_entries_added"]
                                        for v in per_lane.values()),
        "tier_policy": dict(sorted(RULES.items())),
        "state": "SUGGESTED",
        "note": ("index re-join on the pending anchors of the 44 CIE lanes "
                 "(XJOIN-1 NEXT #1); engine-derived identity-grade text "
                 "joins, SUGGESTED until the next review/promotion gate "
                 "(rule 2); record-less pairs stay pending honestly "
                 "(rule 3)"),
    }
    (SL / "manifest.json").write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")

    # ---- resolution sheet (T-SPEC-2b shape, per (lane, id))
    sheet = {
        "lane": LANE_ID, "generated_utc": STAMP, "directive": DIRECTIVE,
        "gateway_trace": TRACE, "base_commit": BASE_COMMIT,
        "header": (
            "Index re-join on the 44 CIE lanes' pending spec-point references "
            "(T-SPECS-CIE-XJOIN-1 NEXT #1). Deterministic identity-grade rules "
            "J1-J4 fired against the canonical per-course indexes "
            "(cross-lane-aware); every resolve carries verbatim evidence and "
            "its evidence source. Entries are per (lane, id): SME reuses "
            "spcpt ids across course trees. Multi hits quarantine (no "
            "fall-through); the 268 record-less pairs stay pending honestly "
            "(AGENT.md rule 3). Resolutions are SUGGESTED until the next "
            "review/promotion gate (rule 2)."),
        "verdicts": [],
        "ambiguous": [],
    }
    for (l, sid), v in sorted(resolves.items()):
        sheet["verdicts"].append({"id": sid, **v})
    for (l, sid), a in sorted(ambiguous.items()):
        sheet["ambiguous"].append({"id": sid, **a})
    sheet["verdicts"].sort(key=lambda e: (e["lane"], e["id"]))
    sheet["ambiguous"].sort(key=lambda e: (e["lane"], e["id"]))
    SHEET_OUT.write_text(
        yaml.safe_dump(sheet, sort_keys=False, allow_unicode=True, width=100))

    # ---- stats
    census_stays = {
        "no_new_evidence_verdict_evaluated":
            stays["no_new_evidence_verdict_evaluated"],
        "no_identity_evidence": stays["no_identity_evidence"],
        "recordless_no_corpus_record":
            stays["recordless_no_corpus_record"],
    }
    amb_by_reason = dict(sorted(Counter(
        a["reason"] for a in ambiguous.values()).items()))
    by_rule = dict(sorted(Counter(
        v["tier"] for v in resolves.values()).items()))
    summary = {
        "lane": LANE_ID, "generated_utc": STAMP, "directive": DIRECTIVE,
        "gateway_trace": TRACE, "fires": FIRES, "base_commit": BASE_COMMIT,
        "lanes": len(lanes), "touched_lanes": len(touched_lanes),
        "pending_refs_total": refs_total,
        "unique_pairs_total": len(pairs),
        "resolved_pairs_total": len(resolves),
        "resolved_refs_total": sum(v["resolved_refs"]
                                   for v in per_lane.values()),
        "code_entries_added_total": sum(v["code_entries_added"]
                                        for v in per_lane.values()),
        "ambiguous_pairs_total": len(ambiguous),
        "ambiguous_by_reason": amb_by_reason,
        "resolves_by_rule": by_rule,
        "stays": census_stays,
        "reconciliation": {
            "pairs": (len(resolves) + len(ambiguous)
                      + sum(census_stays.values())),
            "must_equal": len(pairs),
            "recordless_pin": 268,
        },
        "elapsed_seconds": round(time.time() - t0, 1),
        "lanes_detail": [dict(lane=l, **per_lane[l]) for l in touched_lanes],
    }
    assert summary["reconciliation"]["pairs"] == \
        summary["reconciliation"]["must_equal"]
    STATS_OUT.write_text(json.dumps(summary, ensure_ascii=False, indent=1)
                         + "\n")

    # ---- stage everything the lane touched
    for l in touched_lanes:
        git("add", "--", f"spec-links/{l}.json")
    git("add", "--", "spec-links/manifest.json")
    git("add", "--", str(SHEET_OUT.relative_to(REPO)))
    git("add", "--", str(STATS_OUT.relative_to(REPO)))
    print(f"\nREJOIN SUMMARY: resolves {len(resolves)} "
          f"({sum(1 for v in resolves.values() if v['tier'][0] == 'J')} rules), "
          f"codes {summary['code_entries_added_total']}, "
          f"touched lanes {len(touched_lanes)}, "
          f"ambiguous {len(ambiguous)}, stays {sum(census_stays.values())}")
    return 0


def engine_lanes() -> list[str]:
    out = git("ls-tree", "-r", "--name-only", "HEAD", "spec-links/")
    return sorted(line.rsplit("/", 1)[1][:-5]
                  for line in out.splitlines()
                  if line.startswith("spec-links/cie-")
                  and line.endswith(".json"))


if __name__ == "__main__":
    sys.exit(main())
