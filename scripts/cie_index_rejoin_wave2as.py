#!/usr/bin/env python3
"""
T-SPECS-CIE-REJOIN-2 — index re-join lane for the 8 wave-2 AS sidecar lanes
(the T-SPECS-CIE-JOIN-2 record's follow-on #1, the index re-join class;
operator directive "fire the re-join lane", 2026-10-28, zai-web, gateway
trace 1a181f6adcfa4c55).

Re-fires the pending spec-point references of the 8 wave-2 AS lanes built by
T-SPECS-CIE-JOIN-2 against the canonical per-course spec-point indexes,
exactly the T-SPECS-CIE-REJOIN-1 precedent (scripts/cie_index_rejoin.py,
imported helpers, NOT forked normalization):

  - the AS substrate is name-only (definitions null corpus-wide, index
    harvest H4-verified), so the yield class is the name identity rules
    J3/J4 — same honest baseline class the 44 showed pre-gate;
  - definition evidence is still assembled corpus-wide (own lane + the 44
    sibling lanes holding the same spcpt id + cross_lane_join cures) and
    must agree under the lineage normalization SPEC or the pair
    quarantines — nothing is assumed away.

Rules (priority order; tier == rule name; a pair resolves once, by its
strongest rule; on a MULTI hit the pair quarantines — no fall-through, the
T-SPEC-2c doctrine):

  J1_definition_text_identity   norm(definition) == norm(official point
                                text), unique in the lane pool
  J2_definition_phrase_identity token-bounded norm(definition) phrase in
                                exactly one official point text
  J3_name_text_identity         norm(name) == norm(official point text),
                                unique in the lane pool
  J4_name_phrase_identity       token-bounded norm(name) phrase in exactly
                                one official point text

Pools carry the JOIN-2 AS scope law (the parsed registries' own printed
markers, the SME-WAVE2 spine scope_eq basis):

  - cie-as-chemistry-25 / cie-as-physics-25 / cie-as-business-23:
    candidates restricted to 'AS Level'-scoped points;
  - cie-as-computer-science-19: 'A Level'-marked points EXCLUDED,
    scope-less points retained;
  - the 9709 maths lanes: registry carries no scope marks — no filter
    (JOIN-1 semantics for this qualification; the component law is a
    spine-build law, not a sidecar-join law).

None of the 8 lanes was evaluated by any operator verdict lane (no
anchors.verdict block), so the name rules fire on every pending pair — the
REJOIN-1 verdict-exhaustion gate resolves to False for this lane class by
construction.

Application (the verdict-fill pattern, additive): items' pendings
referencing a resolved (lane, sid) cascade code entries {official_id,
official_code, tier: J*, method: cie_index_rejoin_wave2as} (deduped per
item by official_id) and leave the pending list; totals recomputed;
anchors gains an additive `rejoin` census block; review_state gains an
additive `rejoin` block whose state is SUGGESTED — engine-derived
identity-grade joins are suggestions until the next review/promotion gate
(AGENT.md rule 2). This lane does NOT promote, does NOT consume, does NOT
touch v2 — the follow-on chain of record (verdict fills -> review gate ->
v2 consume) stays operator-keyed.

Determinism: fixed stamp, every base read pinned to the base commit
(TOCTOU-free), sorted iteration, byte-idempotent pre-commit re-runs.
Battery: scripts/cie_rejoin_check_wave2as.py (RJ1-RJ10).
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
import cie_spec_join as base  # noqa: E402

LANE_ID = "T-SPECS-CIE-REJOIN-2"
STAMP = "2026-10-28T12:30:00Z"
DIRECTIVE = "fire the re-join lane"
TRACE = "1a181f6adcfa4c55"
FIRES = "T-SPECS-CIE-JOIN-2 record follow-on #1 (the index re-join class)"
PIN = "8460a5f3a03fd7d43ed31e39c27d846f8a747208"
BASE_COMMIT = PIN  # asserted == HEAD at start (fetch-first discipline)
METHOD = "cie_index_rejoin_wave2as"
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
LANES_2 = [
    "cie-as-chemistry-25",
    "cie-as-physics-25",
    "cie-as-business-23",
    "cie-as-computer-science-19",
    "cie-as-maths-20-pure-1",
    "cie-as-maths-20-pure-2",
    "cie-as-maths-20-mechanics",
    "cie-as-maths-20-probability-and-statistics-1",
]
SCOPE_AS_ONLY = {"cie-as-chemistry-25", "cie-as-physics-25", "cie-as-business-23"}
SCOPE_DROP_ALEVEL = {"cie-as-computer-science-19"}
REJOIN_NOTE = ("index re-join cures applied additively to the wave-2 AS "
               "lanes' pending anchors; pairs with no identity evidence "
               "stay pending honestly (AGENT.md rule 3)")
STATS_OUT = REPORTS / "T_SPECS_CIE_REJOIN_2_STATS.json"
SHEET_OUT = REPO / "scripts" / "cie_rejoin_wave2as_resolutions.yaml"


def git(*args: str, binary: bool = False):
    r = subprocess.run(["git", "-C", str(REPO), *args],
                       capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode("utf-8", "replace")


def pin_json(sha: str, path: str):
    return json.loads(git("show", f"{sha}:{path}"))


def scope_law_note(lane: str, full: int, kept: int) -> dict:
    if lane in SCOPE_AS_ONLY:
        return {
            "law": "candidates restricted to the parse's own 'AS Level'-scoped "
                   "points (the SME-WAVE2 spine build scope_eq basis)",
            "registry_points": full,
            "lane_points": kept,
        }
    if lane in SCOPE_DROP_ALEVEL:
        return {
            "law": "parse marks ONLY topics 13-20 'A Level'; topics 1-12 are the "
                   "shared AS & A Level content — 'A Level'-marked points "
                   "excluded, scope-less retained",
            "registry_points": full,
            "lane_points": kept,
        }
    return {
        "law": "registry carries no scope marks — no filter (JOIN-1 semantics "
               "for this qualification; the 9709 component law is a "
               "spine-build law)",
        "registry_points": full,
        "lane_points": kept,
    }


def scoped_pool(lane: str, reg: "base.Registry") -> tuple[list, dict]:
    full = len(reg.points)
    if lane in SCOPE_AS_ONLY:
        reg.points = [p for p in reg.points if p.get("scope") == "AS Level"]
    elif lane in SCOPE_DROP_ALEVEL:
        reg.points = [p for p in reg.points if p.get("scope") != "A Level"]
    reg.by_id = {p["id"]: p for p in reg.points}
    kept = len(reg.points)
    return reg.points, scope_law_note(lane, full, kept)


def context_lanes() -> list[str]:
    out = git("ls-tree", "-r", "--name-only", "HEAD", "spec-links/")
    return sorted(line.rsplit("/", 1)[1][:-5]
                  for line in out.splitlines()
                  if line.startswith("spec-links/cie-")
                  and line.endswith(".json"))


def main() -> int:
    t0 = time.time()
    head = git("rev-parse", "HEAD").strip()
    if head != PIN:
        print(f"FATAL: HEAD {head[:12]} != pin {PIN[:12]} — fetch-first "
              f"re-verify required (parallel-lane discipline)")
        return 1
    sha = head

    lane_to_qual, quals = base.load_manifest()
    unknown = [l for l in LANES_2 if l not in lane_to_qual]
    if unknown:
        print(f"FATAL: lanes not in the spec manifest: {unknown}")
        return 1
    ctx = sorted(context_lanes())
    for l in LANES_2:
        if l not in ctx:
            print(f"FATAL: engine lane {l} has no sidecar at HEAD")
            return 1
    print(f"context lanes (cie-* sidecars): {len(ctx)}; "
          f"engine lanes: {len(LANES_2)}")

    sidecars = {l: pin_json(sha, f"spec-links/{l}.json") for l in LANES_2}

    # per-course indexes: engine lanes (required) + context lanes (evidence)
    indexes: dict[str, dict] = {}
    missing_ctx = []
    for l in ctx:
        try:
            indexes[l] = json.loads(xj.head_index_bytes(l))
        except Exception:
            if l in LANES_2:
                print(f"FATAL: engine lane {l} has no spec_point_index.json")
                return 1
            missing_ctx.append(l)
    universes = {l: set(indexes[l]["spec_points"]) for l in LANES_2}

    # corpus-wide definition holders + the XJOIN cures (context = all lanes)
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

    # official pools per lane (JOIN-2 AS scope law), texts precomputed
    pools: dict[str, list] = {}
    texts: dict[str, list] = {}
    pool_ids: dict[str, dict] = {}
    pool_scope_note: dict[str, dict] = {}
    for l in LANES_2:
        reg = base.Registry(quals[lane_to_qual[l]])
        pts, note = scoped_pool(l, reg)
        pools[l] = pts
        texts[l] = [(p, vf.norm(p.get("text"))) for p in pts]
        pool_ids[l] = {p["id"]: str(p.get("official_code")) for p in pts}
        pool_scope_note[l] = note

    # ---- census: every pending ref, unique (lane, sid) pairs
    refs_total = 0
    pairs: dict[tuple, int] = {}
    for l in LANES_2:
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
        else:
            p = pools[l][[q["id"] for q in pools[l]].index(v["official_id"])]
            if l in SCOPE_AS_ONLY and p.get("scope") != "AS Level":
                errors.append(f"{l}:{sid}:scope law violation")
            if l in SCOPE_DROP_ALEVEL and p.get("scope") == "A Level":
                errors.append(f"{l}:{sid}:scope law violation")
        if v["tier"] not in RULES:
            errors.append(f"{l}:{sid}:tier vocab")
    if verdict_evaluated_pairs:
        errors.append(f"{verdict_evaluated_pairs} verdict-evaluated pairs in "
                      f"an AS lane class (unexpected)")
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
            "scope_law": pool_scope_note[l],
            "note": REJOIN_NOTE,
        }
        rs = d["review_state"]
        rs["rejoin"] = {
            "lane": LANE_ID, "directive": DIRECTIVE, "gateway_trace": TRACE,
            "applied_utc": STAMP, "base_commit": sha,
            "method": METHOD, "tiers": dict(sorted(RULES.items())),
            "state": "SUGGESTED",
            "note": ("engine-derived identity-grade index re-join resolutions "
                     "on the wave-2 AS lanes' pending anchors (JOIN-2 "
                     "follow-on #1); SUGGESTED pending the next "
                     "review/promotion gate per AGENT.md rule 2; the AS scope "
                     "law bounds every pool; nothing manufactured (rule 3)"),
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
            "scope_law": pool_scope_note[l],
        }
        print(f"[{l}] pairs {len(res_l)} refs {resolved_refs} codes {added} "
              f"pending {refs_before} -> {refs_after}")

    # ---- manifest
    manifest = pin_json(sha, "spec-links/manifest.json")
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
    manifest["cie_rejoin_wave2as"] = {
        "lane": LANE_ID, "applied_utc": STAMP, "directive": DIRECTIVE,
        "gateway_trace": TRACE, "base_commit": sha,
        "lanes": len(touched_lanes),
        "resolved_pairs_total": sum(v["resolved_pairs"]
                                    for v in per_lane.values()),
        "code_entries_added_total": sum(v["code_entries_added"]
                                        for v in per_lane.values()),
        "tier_policy": dict(sorted(RULES.items())),
        "scope_law": "JOIN-2 AS scope law bounds every pool: AS Level-only "
                     "(chem-25/phys-25/business-23), A-Level-marked excluded "
                     "(cs-19), unscoped (9709 maths x4)",
        "state": "SUGGESTED",
        "note": ("index re-join on the pending anchors of the 8 wave-2 AS "
                 "lanes (JOIN-2 follow-on #1); engine-derived identity-grade "
                 "text joins under the AS scope law, SUGGESTED until the "
                 "next review/promotion gate (rule 2); no-evidence pairs "
                 "stay pending honestly (rule 3)"),
    }
    (SL / "manifest.json").write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")

    # ---- resolution sheet (T-SPEC-2b shape, per (lane, id))
    sheet = {
        "lane": LANE_ID, "generated_utc": STAMP, "directive": DIRECTIVE,
        "gateway_trace": TRACE, "base_commit": sha,
        "header": (
            "Index re-join on the 8 wave-2 AS lanes' pending spec-point "
            "references (T-SPECS-CIE-JOIN-2 follow-on #1). Deterministic "
            "identity-grade rules J1-J4 fired against the canonical "
            "per-course spec-point indexes (corpus-wide definition context "
            "over all CIE lanes); every resolve carries verbatim evidence "
            "and its evidence source. Pools bounded by the JOIN-2 AS scope "
            "law. Entries are per (lane, id). Multi hits quarantine (no "
            "fall-through); no-evidence pairs stay pending honestly "
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
        "gateway_trace": TRACE, "fires": FIRES, "base_commit": sha,
        "context_lanes": len(ctx),
        "context_lanes_missing_index": sorted(missing_ctx),
        "lanes": len(LANES_2), "touched_lanes": len(touched_lanes),
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
        "verdict_evaluated_pairs": verdict_evaluated_pairs,
        "scope_law": {l: pool_scope_note[l] for l in LANES_2},
        "reconciliation": {
            "pairs": (len(resolves) + len(ambiguous)
                      + sum(census_stays.values())),
            "must_equal": len(pairs),
        },
        # determinism law: NO wall-clock fields in the artifact (byte-idempotent
        # re-runs); elapsed time prints to stdout only
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
    print(f"\nREJOIN-2 SUMMARY: resolves {len(resolves)} "
          f"({sum(1 for v in resolves.values() if v['tier'][0] == 'J')} rules), "
          f"codes {summary['code_entries_added_total']}, "
          f"touched lanes {len(touched_lanes)}, "
          f"ambiguous {len(ambiguous)}, stays {sum(census_stays.values())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
