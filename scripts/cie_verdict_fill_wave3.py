#!/usr/bin/env python3
"""
T-SPECS-CIE-VERDICT-3 — operator-verdict fill for the EQ/FC wave-growth
sidecars (the REJOIN-3 record follow-on, the operator-verdict fill class;
operator directive "fire that consume lane", 2026-10-30, zai-web, gateway
trace 1a18bc6701800065).

Fills the wave3 lanes' still-pending anchors with identity-grade verdicts,
mirroring the T-SPECS-CIE-VERDICT-1/2 evolution (cie_verdict_fill_wave2as
ported, NOT re-decided). Every resolve is a deterministic, single-target
identity match whose evidence is verbatim from committed sources; everything
else stays pending with a structured reason (AGENT.md rule 3 — nothing
manufactured). The lane-level review state stays SUGGESTED (additive
review_state.wave3.verdict3 block) — promotion at the chain's stage-#4 gate
(AGENT.md rule 2).

Rules (priority order; tier == rule name; a spec-point id resolves once, by
its strongest rule; on a MULTI hit the id quarantines — no fall-through, the
T-SPEC-2c doctrine):
  V1_name_text_identity / V2_name_phrase_identity /
  V5_topic_scoped_phrase_identity / V3_subsection_head_identity /
  V4_settext_title_identity (literature lanes only)

Pools: vf.lane_pool (JOIN-1 lane scoping — 0654 sciences, 0580/0607 tiers,
9709 components; the wave3 lanes carry no parse-printed scope markers, the
unscoped doctrine applies). Substrate: the lane's note spec_point blocks
(VERDICT-1 pattern), read verbatim from HEAD blobs.

Determinism: fixed stamp, HEAD-pinned reads, sorted iteration,
byte-idempotent pre-commit re-runs; no wall-clock fields in the artifacts.
Output: graph/reports/T_SPECS_CIE_WAVE3_VERDICT.json +
scripts/cie_wave3_verdicts.yaml (the verdict evidence sheet; the stage-#4
gate re-fires every resolution from it verbatim).
"""
from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path("/home/z/my-project/syllabai-resources")
REPORTS = REPO / "graph" / "reports"
SPEC_LINKS = REPO / "spec-links"

STAMP = "2026-10-30T10:00:00Z"
DIRECTIVE = "fire that consume lane"
TRACE = "1a18bc6701800065"
FIRES = "T-SPECS-CIE-REJOIN-3 record follow-on (the operator-verdict fill class)"
METHOD = "cie_verdict_fill_wave3"
LANE_ID = "T-SPECS-CIE-VERDICT-3"
RULES = {
    "V1_name_text_identity":
        "norm(name) == norm(official point text), unique in the lane pool",
    "V2_name_phrase_identity":
        "norm(name) (>=3 chars) appears as a token-bounded phrase in exactly "
        "one official point text of the lane pool",
    "V3_subsection_head_identity":
        "norm(name | note topic title) == artifact-stripped norm(subsection "
        "title) AND that subsection has exactly one point in the pool",
    "V4_settext_title_identity":
        "(literature lanes only) note-name segment 0 == the quoted set-text "
        "title inside exactly one official point text",
    "V5_topic_scoped_phrase_identity":
        "V2 was ambiguous globally but exactly one hit within the official "
        "topic whose title equals the SME note's section|topic title",
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
STATS_OUT = REPORTS / "T_SPECS_CIE_WAVE3_VERDICT.json"
SHEET_OUT = REPO / "scripts" / "cie_wave3_verdicts.yaml"

sys.path.insert(0, str(REPO / "scripts"))
import cie_verdict_fill as vf  # noqa: E402
import cie_spec_join as base  # noqa: E402
from cie_verdict_fill_wave2as import norm_sub, _resolve  # noqa: E402


def git(*args: str, binary: bool = False):
    r = subprocess.run(["git", "-C", str(REPO), *args],
                       capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode("utf-8", "replace")


def pin_json(sha: str, path: str):
    return json.loads(git("show", f"{sha}:{path}"))


def main() -> int:
    sha = git("rev-parse", "HEAD").strip()
    dirty = [line[3:].strip().strip('"')
             for line in git("status", "--porcelain").splitlines() if line.strip()]
    if dirty:
        print(f"FATAL: dirty tree before any write ({dirty[:8]}) — TOCTOU guard")
        return 1

    lane_to_qual, quals = base.load_manifest()
    unknown = [l for l in LANES_3 if l not in lane_to_qual]
    if unknown:
        print(f"FATAL: lanes not in the spec manifest: {unknown}")
        return 1
    sidecars = {l: pin_json(sha, f"spec-links/{l}.json") for l in LANES_3}

    pools: dict[str, list] = {}
    texts: dict[str, list] = {}
    pool_ids: dict[str, dict] = {}
    reg_ids: dict[str, str] = {}
    sub_pts: dict[str, dict] = {}
    top_titles: dict[str, dict] = {}
    regs: dict[str, dict] = {}
    for l in LANES_3:
        reg = base.Registry(quals[lane_to_qual[l]])
        reg_ids[l] = reg.reg_id
        qual = sidecars[l]["qual"]
        if qual not in regs:
            regs[qual] = vf.load_registry(qual)
        pts = vf.lane_pool(l, regs[qual])
        pools[l] = pts
        texts[l] = [(p, vf.norm(p.get("text"))) for p in pts]
        pool_ids[l] = {p["id"]: str(p.get("official_code")) for p in pts}
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

    refs_total = 0
    pairs: dict[tuple, int] = {}
    for l in LANES_3:
        for key, it in sidecars[l]["items"].items():
            for sid in (it.get("pending") or []):
                refs_total += 1
                pairs[(l, sid)] = pairs.get((l, sid), 0) + 1
    print(f"pending refs {refs_total} -> unique pairs {len(pairs)}")

    files = base.ls_tree()
    blobs_cache: dict = {}
    blocks: dict[str, dict[str, tuple]] = {}
    conflicts: dict[str, set] = {}
    universes: dict[str, set] = {}
    for l in LANES_3:
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
        ph = [p for p, t in tlist
              if len(nn) >= 3 and vf.phrase_in(nn, t)]
        if len(ph) == 1:
            resolves[(l, sid)] = _resolve(l, sid, "V2_name_phrase_identity",
                                          ph[0], name, ttopic, nsec)
            continue
        if len(ph) > 1:
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
                        "matched_codes": sorted(str(p.get("official_code"))
                                                for p in qh)}
                    continue
        stays["no_unique_identity"] += 1

    print(f"resolves {len(resolves)}  ambiguous {len(ambiguous)}  "
          f"stays {dict(stays)}")

    errors = []
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
        if v["tier"] not in RULES:
            errors.append(f"{l}:{sid}:tier vocab")
    if errors:
        for e in errors:
            print("FAIL-CLOSED:", e)
        return 1

    touched_lanes = sorted({l for (l, _s) in resolves})
    if not touched_lanes:
        print("no-op re-run: sidecars, manifest, sheet and stats "
              "byte-identical")
        return 0

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
        a = d["anchors"]
        a["pending_refs"] = refs_after
        w3 = a.get("wave3") or {}
        w3["verdict3"] = {
            "lane": LANE_ID, "applied_utc": STAMP,
            "resolved_pairs": len(res_l),
            "resolved_refs": resolved_refs,
            "code_entries_added": added,
            "by_rule": {k: sum(1 for v in res_l.values() if v["tier"] == k)
                        for k in sorted(RULES)},
            "ambiguous_pairs": len(amb_l),
            "pending_refs_after": refs_after,
        }
        a["wave3"] = w3
        rs = d["review_state"]
        w3rs = rs.get("wave3") or {}
        w3rs["verdict3"] = {
            "state": "SUGGESTED", "lane": LANE_ID,
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
    manifest["generated_utc"] = STAMP
    manifest["cie_wave3_verdict"] = {
        "lane": LANE_ID,
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

    sheet = {"schema": "syllabai.cie-verdict-resolutions/1.0",
             "lane": LANE_ID, "stamp": STAMP,
             "directive": DIRECTIVE, "gateway_trace": TRACE,
             "verdicts": [resolves[k] for k in sorted(resolves)],
             "ambiguous": [dict(a, lane=l, id=sid)
                           for (l, sid), a in sorted(ambiguous.items())]}
    SHEET_OUT.write_text(yaml.safe_dump(sheet, sort_keys=False,
                                        allow_unicode=True),
                         encoding="utf-8")

    STATS_OUT.write_text(json.dumps({
        "lane": LANE_ID, "stamp": STAMP, "pin": sha,
        "lanes": per_lane,
        "totals": {"pending_refs_before": refs_total,
                   "unique_pairs": len(pairs),
                   "resolved_pairs": len(resolves),
                   "ambiguous_pairs": len(ambiguous),
                   "stays": dict(stays)},
    }, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"sheet {SHEET_OUT.name}: {len(resolves)} resolve rows, "
          f"{len(ambiguous)} ambiguous")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
