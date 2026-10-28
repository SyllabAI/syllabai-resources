#!/usr/bin/env python3
"""
T-SPECS-CIE-VERDICT-2 — operator-verdict fill lane for the 8 wave-2 AS
sidecar lanes (the T-SPECS-CIE-REJOIN-2 record NEXT #1, the operator-verdict
fill class; operator directive "verdict fills -> review gate -> v2 consume",
2026-10-29, zai-web, gateway trace 1a183e66619bd6dd).

Fills the still-pending anchors of the 8 wave-2 AS lanes with identity-grade
operator verdicts, mirroring the T-SPECS-CIE-VERDICT-1 evolution
(scripts/cie_verdict_fill.py, imported helpers, NOT forked normalization).
The lane's verdicts land authoritative by construction (AGENT.md rule 1):
every resolve is a deterministic, single-target identity match whose
evidence is verbatim from committed sources; everything else stays pending
with a structured reason (AGENT.md rule 3 — nothing manufactured). The
lane-level review state stays SUGGESTED — promotion happens at the next
review/promotion gate (AGENT.md rule 2), which the same operator directive
orders as this chain's stage #2.

Rules (priority order; tier == rule name; a spec-point id resolves once, by
its strongest rule; on a MULTI hit the id quarantines — no fall-through, the
T-SPEC-2c doctrine):

  V1_name_text_identity        norm(name) == norm(official point text),
                               unique in the lane pool
  V2_name_phrase_identity      norm(name) (>=3 chars) appears as a
                               token-bounded phrase in exactly one official
                               point text of the lane pool
  V5_topic_scoped_phrase       V2 was ambiguous globally but exactly one hit
                               within the official topic whose title equals
                               the SME note's section|topic title
  V3_subsection_head_identity  norm(name | note topic title) == artifact-
                               stripped norm(subsection title) AND that
                               subsection has exactly one point in the pool
  V4_settext_title_identity    (literature lanes only — pinned 0 for this
                               lane class) note-name segment 0 == the quoted
                               set-text title inside exactly one official
                               point text

Pools carry the JOIN-2 AS scope law (the REJOIN-2 precedent, imported — not
re-decided): 'AS Level'-scoped only (chem-25/phys-25/business-23),
'A Level'-marked excluded (cs-19), unscoped 9709 (maths x4).

Substrate: the SME note spec_point blocks of the lane (the VERDICT-1
substrate), read verbatim from HEAD blobs. Pairs whose sid carries no note
block in the lane (EQ/flashcard-referenced, recordless) are not
V-evaluable and stay pending honestly (dangling_eq_reference class — the
planned SME-native index harvest remains the cure named by VERDICT-1).

Application (the verdict-fill pattern, additive): items' pendings
referencing a resolved sid cascade code entries {official_id,
official_code, tier: V*, method: operator_verdict} (deduped per item by
official_id) and leave the pending list; totals recomputed;
anchors gains an additive `verdict` census block (universe_resolved join
semantics recomputed); review_state gains an additive `verdict` block whose
state is SUGGESTED until the stage-#2 gate. This lane does NOT promote,
does NOT consume, does NOT touch v2.

Determinism: fixed stamp, HEAD-pinned reads (TOCTOU-free), sorted
iteration, byte-idempotent pre-commit re-runs; the stats artifact carries
NO wall-clock fields.
Battery: scripts/cie_verdict_check_wave2as.py (VD1-VD10).
"""
from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path("/home/z/my-project/syllabai-resources")
SL = REPO / "spec-links"
REPORTS = REPO / "graph" / "reports"
sys.path.insert(0, str(REPO / "scripts"))
import cie_verdict_fill as vf  # noqa: E402
import cie_spec_join as base  # noqa: E402
import cie_index_rejoin_wave2as as rj2  # noqa: E402

LANE_ID = "T-SPECS-CIE-VERDICT-2"
STAMP = "2026-10-29T12:00:00Z"
DIRECTIVE = "verdict fills -> review gate -> v2 consume"
TRACE = "1a183e66619bd6dd"
FIRES = "T-SPECS-CIE-REJOIN-2 record NEXT #1 (the operator-verdict fill class)"
PIN = "251b46ba0bd9a08d66d57eca44fc8c80cd283289"
BASE_COMMIT = PIN  # asserted == HEAD at start (fetch-first discipline)
METHOD = "operator_verdict"
RULES = {
    "V1_name_text_identity":
        "norm(name) == norm(official point text), unique in the lane pool",
    "V2_name_phrase_identity":
        "token-bounded norm(name) phrase in exactly one official point text",
    "V3_subsection_head_identity":
        "head == artifact-stripped single-point subsection title",
    "V4_settext_title_identity":
        "note-name segment == quoted set-text title, unique (literature "
        "lanes only; pinned 0 for the wave-2 AS class)",
    "V5_topic_scoped_phrase_identity":
        "topic-scoped disambiguation of a phrase ambiguity",
}
LANES_2 = list(rj2.LANES_2)
LANE_PATHS = ({f"spec-links/{l}.json" for l in LANES_2}
              | {"spec-links/manifest.json",
                 "scripts/cie_verdict_fill_wave2as.py",
                 "scripts/cie_verdict_check_wave2as.py",
                 "scripts/cie_verdict_wave2as_verdicts.yaml",
                 "graph/reports/T_SPECS_CIE_VERDICT_2_STATS.json",
                 "graph/reports/T_SPECS_CIE_VERDICT_2_CHECK.json",
                 "graph/reports/T_SPECS_CIE_VERDICT_2_RECORD.md"})
VERDICT_NOTE = ("operator-verdict fills applied additively to the wave-2 AS "
                "lanes' pending anchors (REJOIN-2 NEXT #1); identity-grade "
                "single-target resolves are authoritative by construction "
                "(AGENT.md rule 1); unresolved anchors stay pending with "
                "structured reasons (rule 3); lane promotion happens at the "
                "stage-#2 review/promotion gate (rule 2)")
STATS_OUT = REPORTS / "T_SPECS_CIE_VERDICT_2_STATS.json"
SHEET_OUT = REPO / "scripts" / "cie_verdict_wave2as_verdicts.yaml"


def git(*args: str, binary: bool = False):
    r = subprocess.run(["git", "-C", str(REPO), *args],
                       capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode("utf-8", "replace")


def pin_json(sha: str, path: str):
    return json.loads(git("show", f"{sha}:{path}"))


def norm_sub(title: str) -> str:
    """Artifact-stripped normalization for subsection-title head matches
    (the VERDICT-1 V3 semantics, shared shape)."""
    return vf.norm(vf.ARTIFACT.sub(" ", title or ""))


def main() -> int:
    head = git("rev-parse", "HEAD").strip()
    if head != PIN:
        print(f"FATAL: HEAD {head[:12]} != pin {PIN[:12]} — fetch-first "
              f"re-verify required (parallel-lane discipline)")
        return 1
    sha = head
    dirty = [line[3:].strip().strip('"')
             for line in git("status", "--porcelain").splitlines() if line.strip()]
    foreign = [p for p in dirty if p not in LANE_PATHS]
    if foreign:
        print(f"FATAL: foreign dirty paths before any write "
              f"({foreign[:8]}) — TOCTOU guard")
        return 1

    lane_to_qual, quals = base.load_manifest()
    unknown = [l for l in LANES_2 if l not in lane_to_qual]
    if unknown:
        print(f"FATAL: lanes not in the spec manifest: {unknown}")
        return 1
    print(f"engine lanes: {len(LANES_2)} (HEAD == pin, tree clean)")

    sidecars = {l: pin_json(sha, f"spec-links/{l}.json") for l in LANES_2}

    # official pools per lane (JOIN-2 AS scope law via the REJOIN-2 engine)
    pools: dict[str, list] = {}
    texts: dict[str, list] = {}
    pool_ids: dict[str, dict] = {}
    pool_scope_note: dict[str, dict] = {}
    reg_ids: dict[str, str] = {}
    sub_pts: dict[str, dict] = {}
    top_titles: dict[str, dict] = {}
    for l in LANES_2:
        reg = base.Registry(quals[lane_to_qual[l]])
        reg_ids[l] = reg.reg_id
        pts, note = rj2.scoped_pool(l, reg)
        pools[l] = pts
        texts[l] = [(p, vf.norm(p.get("text"))) for p in pts]
        pool_ids[l] = {p["id"]: str(p.get("official_code")) for p in pts}
        pool_scope_note[l] = note
        sp: dict[str, list] = {}
        for p in pts:
            st = norm_sub((p.get("subsection") or {}).get("title") or "")
            sp.setdefault(st, []).append(p)
        sub_pts[l] = sp
        tt: dict[str, list] = {}
        for p in pts:
            t = p.get("topic") or {}
            tnorm = vf.norm(t.get("title") if isinstance(t, dict) else "")
            tt.setdefault(tnorm, []).append(p)
        top_titles[l] = tt

    # ---- census: every pending ref, unique (lane, sid) pairs
    refs_total = 0
    pairs: dict[tuple, int] = {}
    for l in LANES_2:
        for key, it in sidecars[l]["items"].items():
            for sid in (it.get("pending") or []):
                refs_total += 1
                pairs[(l, sid)] = pairs.get((l, sid), 0) + 1
    print(f"pending refs {refs_total} -> unique pairs {len(pairs)}")

    # ---- substrate: the lane's note spec_point blocks (VERDICT-1 pattern)
    files = base.ls_tree()
    blobs_cache: dict = {}
    blocks: dict[str, dict[str, tuple]] = {}
    conflicts: dict[str, set] = {}
    universes: dict[str, set] = {}
    for l in LANES_2:
        bl = vf.lane_blocks(l, files, blobs_cache)
        m: dict[str, tuple] = {}
        conflict: set = set()
        for sid, name, ttopic, nsec in bl:
            if sid in m and m[sid] != (name, ttopic, nsec):
                conflict.add(sid)
                continue
            m.setdefault(sid, (name, ttopic, nsec))
        blocks[l] = m
        conflicts[l] = conflict
        universes[l] = set(m)
        if conflict:
            print(f"  [{l}] note-name conflicts (kept pending): "
                  f"{len(conflict)}")

    # ---- evaluate the V-rule chain per pair
    resolves: dict[tuple, dict] = {}
    ambiguous: dict[tuple, dict] = {}
    stays: Counter = Counter()
    for (l, sid) in sorted(pairs):
        blk = blocks[l].get(sid)
        if blk is None:
            stays["dangling_eq_reference"] += 1
            continue
        name, ttopic, nsec = blk
        if sid in conflicts[l]:
            ambiguous[(l, sid)] = {"lane": l,
                                   "reason": "note_name_conflict_across_blocks"}
            continue
        nn = vf.norm(name)
        if not nn:
            stays["no_unique_identity"] += 1
            continue
        tlist = texts[l]
        # --- V1: name == point text (unique)
        eq = [p for p, t in tlist if t and t == nn]
        if len(eq) == 1:
            resolves[(l, sid)] = _resolve(l, sid, "V1_name_text_identity",
                                          eq[0], name, ttopic, nsec)
            continue
        if len(eq) > 1:
            ambiguous[(l, sid)] = {
                "lane": l, "reason": "name_eq_multi_text",
                "matched_codes": sorted(str(p.get("official_code"))
                                        for p in eq)}
            continue
        # --- V2: name phrase-unique in point text
        ph = [p for p, t in tlist
              if len(nn) >= 3 and vf.phrase_in(nn, t)]
        if len(ph) == 1:
            resolves[(l, sid)] = _resolve(l, sid, "V2_name_phrase_identity",
                                          ph[0], name, ttopic, nsec)
            continue
        if len(ph) > 1:
            # --- V5: topic-scoped disambiguation of the phrase ambiguity
            scoped = []
            cand = None
            for c in (nsec, ttopic):
                nc = vf.norm(c)
                if nc and nc in top_titles[l]:
                    scoped = [p for p in top_titles[l][nc]
                              if vf.phrase_in(nn, vf.norm(p.get("text")))]
                    if len(scoped) == 1:
                        cand = c
                        break
                    scoped = []
            if len(scoped) == 1:
                resolves[(l, sid)] = _resolve(
                    l, sid, "V5_topic_scoped_phrase_identity", scoped[0],
                    name, ttopic, nsec, topic_title=cand)
                continue
            ambiguous[(l, sid)] = {
                "lane": l, "reason": "name_phrase_multi_text",
                "matched_codes": sorted(str(p.get("official_code"))
                                        for p in ph)}
            continue
        # --- V3: head identity against a single-point subsection
        fired = False
        for cand, src in ((name, "spcpt_name"), (ttopic, "note_topic_title")):
            nc = norm_sub(cand)
            if nc and nc in sub_pts[l]:
                if len(sub_pts[l][nc]) == 1:
                    op = sub_pts[l][nc][0]
                    resolves[(l, sid)] = _resolve(
                        l, sid, "V3_subsection_head_identity", op,
                        name, ttopic, nsec, head=cand, head_source=src)
                else:
                    ambiguous[(l, sid)] = {
                        "lane": l, "reason": "finer_than_official_subsection",
                        "head": cand, "head_source": src,
                        "matched_codes": sorted(
                            str(p.get("official_code"))
                            for p in sub_pts[l][nc])}
                fired = True
                break
        if fired:
            continue
        # --- V4: set-text title identity (literature lanes only)
        if "literature" in reg_ids[l]:
            seg = vf.norm(name.split(":")[0]) if name else ""
            if seg:
                qh = [p for p, _t in tlist
                      if vf.quoted_title(p.get("text"))
                      and vf.quoted_title(p.get("text")) == seg]
                if len(qh) == 1:
                    resolves[(l, sid)] = _resolve(
                        l, sid, "V4_settext_title_identity", qh[0],
                        name, ttopic, nsec)
                    continue
                if len(qh) > 1:
                    ambiguous[(l, sid)] = {
                        "lane": l, "reason": "name_phrase_multi_text",
                        "matched_codes": sorted(
                            str(p.get("official_code")) for p in qh)}
                    continue
        stays["no_unique_identity"] += 1

    print(f"resolves {len(resolves)}  ambiguous {len(ambiguous)}  "
          f"stays {dict(stays)}")

    # ---- fail-closed validation before any write
    errors = []
    touched_lanes = sorted({l for (l, _s) in resolves})
    for (l, sid), v in sorted(resolves.items()):
        if (l, sid) not in pairs:
            errors.append(f"{l}:{sid}:resolved pair was not pending")
        if sid not in universes[l]:
            errors.append(f"{l}:{sid}:resolved sid outside the note universe")
        ids = pool_ids[l]
        if v["official_id"] not in ids:
            errors.append(f"{l}:{sid}:dangling official id {v['official_id']}")
        elif ids[v["official_id"]] != v["official_code"]:
            errors.append(f"{l}:{sid}:code mismatch")
        else:
            p = next(p for p in pools[l] if p["id"] == v["official_id"])
            if l in rj2.SCOPE_AS_ONLY and p.get("scope") != "AS Level":
                errors.append(f"{l}:{sid}:scope law violation")
            if l in rj2.SCOPE_DROP_ALEVEL and p.get("scope") == "A Level":
                errors.append(f"{l}:{sid}:scope law violation")
        if v["tier"] not in RULES:
            errors.append(f"{l}:{sid}:tier vocab")
    v4 = sum(1 for v in resolves.values()
             if v["tier"] == "V4_settext_title_identity")
    if v4:
        errors.append(f"{v4} V4 resolves in an AS lane class (unexpected)")
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
        refs_before = refs_after = 0
        resolved_refs = 0
        for key in sorted(items):
            it = items[key]
            pend = it.get("pending") or []
            if not pend:
                continue
            refs_before += len(pend)
            keep, new_codes = [], []
            seen_oids = {c.get("official_id")
                         for c in (it.get("codes") or [])}
            for sid in pend:
                if sid in code_by_sid:
                    resolved_refs += 1
                    oid, ocode, tier = code_by_sid[sid]
                    if oid not in seen_oids:
                        seen_oids.add(oid)
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
        pend_universe = {sid for it in items.values()
                         for sid in (it.get("pending") or [])
                         if sid in universes[l]}
        a = d["anchors"]
        a["universe_resolved"] = (int(a["universe_ids"])
                                  - len(pend_universe))
        a["pending_refs"] = refs_after
        dangling_l = sum(1 for (ll, _s) in pairs
                         if ll == l and _s not in universes[l])
        a["verdict"] = {
            "lane": LANE_ID, "applied_utc": STAMP,
            "resolved_ids": len(res_l),
            "resolved_refs": resolved_refs,
            "by_tier": {k: sum(1 for v in res_l.values() if v["tier"] == k)
                        for k in sorted(RULES)},
            "pending_ids": len(pend_universe),
            "pending_reasons": dict(sorted(
                Counter(_stay_reason(stays, ambiguous, res_l, l,
                                     universes[l], pairs)).items())),
            "dangling_eq_refs_pending": dangling_l,
            "scope_law": pool_scope_note[l],
            "note": VERDICT_NOTE,
        }
        rs = d["review_state"]
        rs["verdict"] = {
            "lane": LANE_ID, "directive": DIRECTIVE, "gateway_trace": TRACE,
            "applied_utc": STAMP, "base_commit": sha,
            "method": METHOD, "tiers": dict(sorted(RULES.items())),
            "state": "SUGGESTED",
            "note": ("identity-grade operator-verdict fills on the wave-2 AS "
                     "lanes' pending anchors (REJOIN-2 NEXT #1); "
                     "authoritative by construction per AGENT.md rule 1; "
                     "lane promotion happens at the stage-#2 "
                     "review/promotion gate (rule 2); nothing manufactured "
                     "(rule 3)"),
        }
        (SL / f"{l}.json").write_text(
            json.dumps(d, indent=1, ensure_ascii=False) + "\n")
        per_lane[l] = {
            "resolved_ids": len(res_l),
            "resolved_refs": resolved_refs,
            "code_entries_added": added,
            "by_tier": a["verdict"]["by_tier"],
            "pending_reasons": a["verdict"]["pending_reasons"],
            "ambiguous_pairs": len(amb_l),
            "pending_refs_before": refs_before,
            "pending_refs_after": refs_after,
            "items_with_codes": t["items_with_codes"],
            "scope_law": pool_scope_note[l],
        }
        print(f"[{l}] ids {len(res_l)} refs {resolved_refs} codes {added} "
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
        row["verdict"] = {
            "lane": LANE_ID,
            "resolved_ids": per_lane[l]["resolved_ids"],
            "resolved_refs": per_lane[l]["resolved_refs"],
            "by_tier": per_lane[l]["by_tier"],
            "pending_reasons": per_lane[l]["pending_reasons"],
        }
    manifest["cie_verdict_wave2as"] = {
        "lane": LANE_ID, "applied_utc": STAMP, "directive": DIRECTIVE,
        "gateway_trace": TRACE, "base_commit": sha,
        "lanes": len(touched_lanes),
        "resolved_ids_total": sum(v["resolved_ids"]
                                  for v in per_lane.values()),
        "resolved_refs_total": sum(v["resolved_refs"]
                                   for v in per_lane.values()),
        "code_entries_added_total": sum(v["code_entries_added"]
                                        for v in per_lane.values()),
        "tier_policy": dict(sorted(RULES.items())),
        "scope_law": "JOIN-2 AS scope law bounds every pool (REJOIN-2 "
                     "precedent, imported): AS Level-only (chem-25/phys-25/"
                     "business-23), A-Level-marked excluded (cs-19), "
                     "unscoped (9709 maths x4)",
        "state": "SUGGESTED",
        "note": ("operator-verdict fills on the still-pending anchors of the "
                 "8 wave-2 AS lanes (REJOIN-2 NEXT #1); authoritative by "
                 "construction (AGENT.md rule 1); SUGGESTED until the "
                 "stage-#2 review/promotion gate (rule 2); no-evidence pairs "
                 "stay pending honestly (rule 3)"),
    }
    (SL / "manifest.json").write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")

    # ---- verdict sheet (decision record, T-SPEC-2b shape; per (lane, id))
    sheet = {
        "lane": LANE_ID, "generated_utc": STAMP, "directive": DIRECTIVE,
        "gateway_trace": TRACE, "base_commit": sha,
        "header": (
            "Operator-verdict fills on the 8 wave-2 AS lanes' still-pending "
            "anchors (T-SPECS-CIE-REJOIN-2 NEXT #1). Identity-grade "
            "deterministic verdicts rendered by cie_verdict_fill_wave2as.py "
            "under the JOIN-2 AS scope law and re-validated fail-closed by "
            "cie_verdict_check_wave2as.py (VD3 re-derives every resolve from "
            "HEAD blobs with an independent implementation). Entries are per "
            "(lane, id). Multi hits quarantine (no fall-through); pairs with "
            "no identity evidence stay pending honestly (AGENT.md rule 3). "
            "Resolutions are SUGGESTED until the stage-#2 review/promotion "
            "gate (rule 2)."),
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

    # ---- stats (determinism law: NO wall-clock fields)
    stays_tax = {
        "dangling_eq_reference": stays["dangling_eq_reference"],
        "no_unique_identity": stays["no_unique_identity"],
    }
    amb_by_reason = dict(sorted(Counter(
        a["reason"] for a in ambiguous.values()).items()))
    by_tier = dict(sorted(Counter(
        v["tier"] for v in resolves.values()).items()))
    summary = {
        "lane": LANE_ID, "generated_utc": STAMP, "directive": DIRECTIVE,
        "gateway_trace": TRACE, "fires": FIRES, "base_commit": sha,
        "lanes": len(LANES_2), "touched_lanes": len(touched_lanes),
        "pending_refs_total": refs_total,
        "unique_pairs_total": len(pairs),
        "resolved_ids_total": len(resolves),
        "resolved_refs_total": sum(v["resolved_refs"]
                                   for v in per_lane.values()),
        "code_entries_added_total": sum(v["code_entries_added"]
                                        for v in per_lane.values()),
        "ambiguous_pairs_total": len(ambiguous),
        "ambiguous_by_reason": amb_by_reason,
        "resolves_by_tier": by_tier,
        "stays": stays_tax,
        "note_universe_sizes": {l: len(universes[l]) for l in LANES_2},
        "scope_law": {l: pool_scope_note[l] for l in LANES_2},
        "reconciliation": {
            "pairs": (len(resolves) + len(ambiguous)
                      + sum(stays_tax.values())),
            "must_equal": len(pairs),
        },
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
    print(f"\nVERDICT-2 SUMMARY: resolves {len(resolves)}, "
          f"codes {summary['code_entries_added_total']}, "
          f"touched lanes {len(touched_lanes)}, "
          f"ambiguous {len(ambiguous)}, stays {sum(stays_tax.values())}")
    return 0


def _resolve(l, sid, tier, op, name, ttopic, nsec, **extra) -> dict:
    ev = {
        "sme_name": name,
        "note_topic_title": ttopic,
        "note_section": nsec,
        "evidence_source": "own",
        "corroborating_sources": [],
        "official_text": op.get("text"),
        "rule": RULES[tier],
    }
    ev.update(extra)
    return {"lane": l, "verdict": "resolve", "tier": tier,
            "official_id": op["id"],
            "official_code": str(op.get("official_code")),
            "evidence": ev}


def _stay_reason(stays, ambiguous, res_l, l, universe, pairs) -> list:
    """Per-lane stay taxonomy for the verdict block (deterministic order)."""
    out = []
    for (ll, sid) in sorted(pairs):
        if ll != l or sid in res_l:
            continue
        a = ambiguous.get((ll, sid))
        if a:
            out.append(a["reason"])
        elif sid not in universe:
            out.append("dangling_eq_reference")
        else:
            out.append("no_unique_identity")
    return out


if __name__ == "__main__":
    sys.exit(main())
