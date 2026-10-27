#!/usr/bin/env python3
"""
T-SPECS-CIE-XJOIN-1 — cross-lane join round for the 54 curable dangling ids
(operator directive "① cross-lane join round", 2026-10-19, zai-web, gateway
trace 1a1535a69f8502d1 — fires the T-SPECS-CIE-INDEX-1 record's NEXT lane #1).

For every CIE SME course lane, the lane's spec_point_index.json coverage
block names the dangling EQ-referenced spcpt ids (missing_from_index). The
INDEX-1 record proved 54 of the 322 dangling (lane, id) pairs are curable
cross-lane — the id holds a spec_point record in >=1 SIBLING CIE lane's
index (the H6 mechanism: present-in-sibling-universe) — while 268 are
recordless corpus-wide and stay pending honestly (AGENT.md rule 3).

This engine appends ONE additive top-level block `cross_lane_join` to each
of the 44 index files; schema/generated_utc/.../spec_points/coverage are
byte-stable (the battery's X2 proves byte-additivity vs HEAD). The block:

    {schema, generated_utc, directive, gateway_trace, fires,
     dangling_total,
     resolved{id: {grade, name, definition, notes, subtopic_slugs,
                   via_lanes[, definition_lanes][, norm_equivalent]}},
     ambiguous[{id, reason, via_lanes, variants[]}],
     unresolved_ids[], resolved_count, ambiguous_count, unresolved_count}

Cure policy (deterministic, zero-LLM, nothing invented — rule 3):
  - grade definition : >=1 sibling holds the id WITH a definition. The
    representative record is the lexicographically-first definition-holding
    sibling's spec_points entry VERBATIM. All definition-holding siblings
    must agree verbatim (or under the lineage normalization SPEC — the
    V5a-pinned join/gate/verdict vocabulary) or the id QUARANTINES into
    `ambiguous` (reason definition_conflict, variants recorded per lane).
  - grade name_only  : siblings hold the id but none with a definition;
    representative = lexicographically-first sibling, definition stays ""
    (nothing manufactured). Name disagreement beyond the normalization
    SPEC quarantines (reason name_conflict).
  - recordless ids land in unresolved_ids — no records manufactured.
  - via_lanes lists ALL sibling lanes holding the id (corroboration,
    honest); definition_lanes (definition grade only) is the
    definition-holding subset. norm_equivalent:true marks a cure whose
    sibling records agreed only under the normalization SPEC.

Sourcing: the 44 HEAD index blobs are the canonical substrate (the corpus
is NOT re-streamed — the index is the designed join substrate per the
INDEX-1 record). Sidecar reconciliation stays fail-closed per lane
(universe == anchors.universe_ids). Staging reuses the INDEX-1 write path:
worktree write + `git add --sparse` (the lane dirs sit outside the sparse
cone; the worktree write is the blob-delivery vehicle, the index entry is
the deliverable).

Determinism: FIXED_STAMP, sorted keys/lists everywhere, byte-idempotent
re-runs (the block is recomputed from the same substrate each run).

Battery: scripts/cie_xlane_join_check.py (X1-X10).
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import time
import unicodedata

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from cie_spcpt_index_harvest import (  # noqa: E402
    REPO, git, lanes, stage_index_file,
)

STATS_OUT = REPO / "graph" / "reports" / "T_SPECS_CIE_XJOIN_1_STATS.json"
FIXED_STAMP = "2026-10-23T20:00:00Z"
BLOCK_SCHEMA = "syllabai.sme-cross-lane-join/1.0"
BLOCK_KEY = "cross_lane_join"
DIRECTIVE = "② cross-lane join round (tranche-3 re-harvest vintage; supersedes the ① 2026-10-19 record and the run-003b placeholder re-records)"
TRACE = "1a16a02c49cfc7d9"
FIRES = "T-RULE-T3-SME-COVERAGE-1 run-005 (operator dispatch: class-A/residual-61 disposition processing)"


def norm(s: str) -> str:
    """Normalization SPEC (shared with the join/gate/verdict lineage, NOT its
    code — the T-SPECS-CIE-VERDICT-1 V5a-pinned equivalence): NFKC, lower,
    & -> and, strip punctuation to spaces, collapse whitespace."""
    s = unicodedata.normalize("NFKC", s or "").lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def head_index_bytes(lane: str) -> bytes:
    return subprocess.run(
        ["git", "-C", str(REPO), "show",
         f"HEAD:SME-ExamQuestion/{lane}/spec_point_index.json"],
        capture_output=True, check=True).stdout


def resolve_lane(lane: str, docs: dict[str, dict],
                 holders: dict[str, list[str]]):
    """Compute the lane's cross_lane_join block from the HEAD substrate."""
    d = docs[lane]
    mis = d["coverage"]["missing_from_index"]
    resolved: dict[str, dict] = {}
    ambiguous: list[dict] = []
    unresolved: list[str] = []

    for sid in mis:  # coverage lists are sorted at harvest time
        sibs = sorted(m for m in holders.get(sid, ()) if m != lane)
        if not sibs:
            unresolved.append(sid)  # recordless corpus-wide — stays pending
            continue
        def_lanes = [m for m in sibs
                     if docs[m]["spec_points"][sid]["definition"]]
        if def_lanes:
            reps = {(docs[m]["spec_points"][sid]["name"],
                     docs[m]["spec_points"][sid]["definition"])
                    for m in def_lanes}
            if len(reps) > 1:
                if len({(norm(n), norm(df)) for n, df in reps}) == 1:
                    rep_lane = def_lanes[0]
                    e = docs[rep_lane]["spec_points"][sid]
                    resolved[sid] = {
                        "grade": "definition", "name": e["name"],
                        "definition": e["definition"], "notes": e["notes"],
                        "subtopic_slugs": e["subtopic_slugs"],
                        "via_lanes": sibs, "definition_lanes": def_lanes,
                        "norm_equivalent": True,
                    }
                    continue
                ambiguous.append({
                    "id": sid, "reason": "definition_conflict",
                    "via_lanes": sibs,
                    "variants": [{"lane": m,
                                  "name": docs[m]["spec_points"][sid]["name"],
                                  "definition": docs[m]["spec_points"][sid][
                                      "definition"]}
                                 for m in def_lanes],
                })
                continue
            rep_lane = def_lanes[0]
            e = docs[rep_lane]["spec_points"][sid]
            resolved[sid] = {
                "grade": "definition", "name": e["name"],
                "definition": e["definition"], "notes": e["notes"],
                "subtopic_slugs": e["subtopic_slugs"],
                "via_lanes": sibs, "definition_lanes": def_lanes,
            }
        else:
            names = {docs[m]["spec_points"][sid]["name"] for m in sibs}
            if len(names) > 1 and len({norm(n) for n in names}) > 1:
                ambiguous.append({
                    "id": sid, "reason": "name_conflict", "via_lanes": sibs,
                    "variants": [{"lane": m,
                                  "name": docs[m]["spec_points"][sid]["name"],
                                  "definition": ""}
                                 for m in sibs],
                })
                continue
            rep_lane = sibs[0]
            e = docs[rep_lane]["spec_points"][sid]
            resolved[sid] = {
                "grade": "name_only", "name": e["name"], "definition": "",
                "notes": e["notes"], "subtopic_slugs": e["subtopic_slugs"],
                "via_lanes": sibs,
            }
            if len(names) > 1:
                resolved[sid]["norm_equivalent"] = True

    block = {
        "schema": BLOCK_SCHEMA,
        "generated_utc": FIXED_STAMP,
        "directive": DIRECTIVE,
        "gateway_trace": TRACE,
        "fires": FIRES,
        "dangling_total": len(mis),
        "resolved": {sid: resolved[sid] for sid in sorted(resolved)},
        "ambiguous": sorted(ambiguous, key=lambda a: a["id"]),
        "unresolved_ids": sorted(unresolved),
        "resolved_count": len(resolved),
        "ambiguous_count": len(ambiguous),
        "unresolved_count": len(unresolved),
    }
    return block


def main() -> int:
    t0 = time.time()
    ls = lanes()
    print(f"CIE lanes: {len(ls)}")

    docs: dict[str, dict] = {}
    for lane in ls:
        docs[lane] = json.loads(head_index_bytes(lane).decode("utf-8"))

    holders: dict[str, list[str]] = {}
    for lane in ls:
        for sid in docs[lane]["spec_points"]:
            holders.setdefault(sid, []).append(lane)

    rows = []
    for lane in ls:
        # fail-closed sidecar reconciliation (the harvest stance, preserved)
        sc = json.loads((REPO / "spec-links" / f"{lane}.json")
                        .read_text(encoding="utf-8"))
        side_universe = sc.get("anchors", {}).get("universe_ids")
        if side_universe != len(docs[lane]["spec_points"]):
            raise RuntimeError(f"{lane}: universe mismatch index="
                               f"{len(docs[lane]['spec_points'])} "
                               f"sidecar={side_universe}")

        block = resolve_lane(lane, docs, holders)
        if (block["resolved_count"] + block["ambiguous_count"]
                + block["unresolved_count"]) != block["dangling_total"]:
            raise RuntimeError(f"{lane}: block arithmetic does not reconcile")

        new_doc = {k: docs[lane][k] for k in docs[lane]}
        new_doc[BLOCK_KEY] = block
        content = json.dumps(new_doc, ensure_ascii=False,
                             indent=1).encode("utf-8")
        path = f"SME-ExamQuestion/{lane}/spec_point_index.json"
        stage_index_file(path, content)

        g = sum(1 for e in block["resolved"].values()
                if e["grade"] == "definition")
        n = block["resolved_count"] - g
        rows.append({
            "lane": lane,
            "dangling_total": block["dangling_total"],
            "resolved_count": block["resolved_count"],
            "resolved_definition_grade": g,
            "resolved_name_only_grade": n,
            "ambiguous_count": block["ambiguous_count"],
            "unresolved_count": block["unresolved_count"],
        })
        print(f"[{lane}] dangling {block['dangling_total']} -> resolved "
              f"{block['resolved_count']} (def {g} / name {n}), ambiguous "
              f"{block['ambiguous_count']}, unresolved "
              f"{block['unresolved_count']}")

    s = {k: sum(r[k] for r in rows) for k in
         ("dangling_total", "resolved_count", "resolved_definition_grade",
          "resolved_name_only_grade", "ambiguous_count", "unresolved_count")}
    summary = {
        "schema": BLOCK_SCHEMA,
        "generated_utc": FIXED_STAMP,
        "directive": DIRECTIVE,
        "gateway_trace": TRACE,
        "fires": FIRES,
        "lanes": len(ls),
        **s,
        "present_in_sibling_pairs": s["resolved_count"] + s["ambiguous_count"],
        "recordless_pairs": s["unresolved_count"],
        "elapsed_seconds": round(time.time() - t0, 1),
        "lanes_detail": rows,
    }
    STATS_OUT.write_text(json.dumps(summary, ensure_ascii=False, indent=1)
                         + "\n", encoding="utf-8")
    print("\nXJOIN SUMMARY:\n"
          + json.dumps({k: v for k, v in summary.items()
                        if k != "lanes_detail"}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
