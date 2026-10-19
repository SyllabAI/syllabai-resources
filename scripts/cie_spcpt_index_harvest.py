#!/usr/bin/env python3
"""
T-SPECS-CIE-INDEX-1 — SME-native spec-point index harvest for the 44 CIE lanes
(operator directive "ignite the SME-native spec-point index harvest lane",
2026-10-19, zai-web, gateway trace 1a153238abda24e1 — fires the
T-SPECS-CIE-VERDICT-1 record's NEXT lane #1).

Builds SME-ExamQuestion/<cie-lane>/spec_point_index.json for every CIE SME
course lane, in the EXACT syllabai.sme-spec-point-index/1.0 shape of the 49
Edexcel precedent files (scripts/sme_spcpt_harvest_all.py):

    {schema, generated_utc, course_slug, notes_base, source_pages,
     fetch_failures, spec_points{id:{name,definition,notes,subtopic_slugs}},
     coverage{question_part_ids_total, covered_by_index, missing_from_index}}

Sourcing (corpus-derived, zero fetching, zero-LLM):
  - spec_points: the notes' embedded spec_point blocks (type spec_point /
    specPoint; id spcpt_*), read straight from git blobs (parallel
    cat-file --batch with multi-pass retry for promisor lock contention;
    no worktree materialization of the corpus). notes = the embedding note's
    rn_* id (note_id field), subtopic_slugs = the note page stem.
    Name-only records keep definition "" — nothing is manufactured
    (AGENT.md rule 3).
  - notes_base: the lane's notes manifest.json notes_base (fail-closed).
  - coverage: the EQ question-part spec_point_ids references vs the index —
    missing_from_index IS the explicit, machine-readable form of the
    corpus's dangling EQ-referenced spcpt ids (previously an implicit
    pending state in the join sidecars).

Determinism: FIXED_STAMP, sorted keys everywhere, byte-idempotent re-runs.
Writes land via `git add --sparse` (the target dirs are outside the sparse
cone; blobs are written to the odb through the worktree file then staged —
the sparse checkout is reapplied by the operator flow, the index is the
deliverable). Sidecar reconciliation is fail-closed: a lane whose index
universe disagrees with its spec-links anchors.universe_ids aborts the run.

Battery: scripts/cie_index_harvest_check.py (H1-H10).
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STATS_OUT = REPO / "graph" / "reports" / "T_SPECS_CIE_INDEX_1_HARVEST.json"
FIXED_STAMP = "2026-10-19T09:00:00Z"
SCHEMA = "syllabai.sme-spec-point-index/1.0"
WORKERS = 6
CHUNK = 64
PASSES = 5


def git(*args: str, binary: bool = False):
    r = subprocess.run(["git", "-C", str(REPO), *args],
                       capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode("utf-8", "replace")


def lanes() -> list[str]:
    out = git("ls-tree", "-r", "--name-only", "HEAD", "spec-links/")
    return sorted(line.rsplit("/", 1)[1][:-5]
                  for line in out.splitlines()
                  if line.startswith("spec-links/cie-") and line.endswith(".json"))


def list_targets(lane: str) -> list[tuple[str, str, str]]:
    targets: list[tuple[str, str, str]] = []
    for tree, kind in ((f"SME-RevisionNotes/{lane}", "note"),
                       (f"SME-ExamQuestion/{lane}", "eq")):
        out = git("ls-tree", "-r", "HEAD", tree)
        for line in out.splitlines():
            meta, path = line.split("\t", 1)
            parts = meta.split()
            oid, otype = parts[2], parts[1]
            if otype != "blob":
                continue
            base = path.rsplit("/", 1)[-1]
            if kind == "note":
                if not path.startswith(f"{tree}/notes/") and base != "manifest.json":
                    continue
                if not base.endswith(".json"):
                    continue
                targets.append((oid, path,
                                "manifest" if base == "manifest.json" else "note"))
            else:
                if base == "topic.json":
                    targets.append((oid, path, "eq"))
    return targets


def read_blobs(requests: list[tuple[str, str, str]]) -> dict[str, bytes]:
    """Parallel cat-file --batch streaming with multi-pass retry.

    Objects reported `missing` (concurrent promisor fetch lock contention)
    are retried in later passes until complete or PASSES exhausted.
    """
    out: dict[str, bytes] = {}

    def work(chunk: list[tuple[str, str, str]]) -> tuple[dict[str, bytes], list[str]]:
        by_oid = {oid: (path, kind) for oid, path, kind in chunk}
        delivered: dict[str, bytes] = {}
        missing: list[str] = []
        proc = subprocess.Popen(
            ["git", "-C", str(REPO), "cat-file", "--batch"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        try:
            req = "".join(oid + "\n" for oid in by_oid).encode()
            proc.stdin.write(req)
            proc.stdin.flush()
            for oid in by_oid:
                header = proc.stdout.readline().decode().strip()
                parts = header.split()
                if len(parts) >= 2 and parts[0] == oid and parts[1] == "missing":
                    missing.append(oid)
                    continue
                if len(parts) < 3 or parts[0] != oid:
                    raise RuntimeError(f"bad batch header for {oid}: {header!r}")
                size = int(parts[2])
                payload = proc.stdout.read(size)
                proc.stdout.read(1)  # trailing LF
                delivered[oid] = payload
        finally:
            proc.stdin.close()
            proc.wait(timeout=30)
        return delivered, missing

    pending = list(requests)
    for pass_no in range(1, PASSES + 1):
        if not pending:
            break
        chunks = [pending[i:i + CHUNK] for i in range(0, len(pending), CHUNK)]
        still: list[str] = []
        with ThreadPoolExecutor(max_workers=WORKERS) as ex:
            for delivered, missing in ex.map(work, chunks):
                out.update(delivered)
                still.extend(missing)
        print(f"  [blobs] pass {pass_no}: {len(pending)} requested, "
              f"{len(pending) - len(still)} delivered, {len(still)} missing")
        keep = set(still)
        pending = [r for r in pending if r[0] in keep]
    if pending:
        raise RuntimeError(f"blobs still missing after {PASSES} passes: "
                           f"{len(pending)} e.g. {pending[0][0]}")
    return out


def walk_blocks(node, hits: list) -> None:
    if isinstance(node, dict):
        t = node.get("type")
        if t in ("spec_point", "specPoint"):
            a = node.get("attrs") or {}
            hits.append({
                "id": node.get("id") or a.get("id"),
                "name": node.get("name") or a.get("name") or "",
                "definition": node.get("definition") or a.get("definition") or "",
            })
        for v in node.values():
            walk_blocks(v, hits)
    elif isinstance(node, list):
        for v in node:
            walk_blocks(v, hits)


def eq_part_ids(doc: dict) -> list[str]:
    ids: list[str] = []
    for q in doc.get("questions", []) or []:
        for part in q.get("parts", []) or []:
            ids.extend(part.get("spec_point_ids", []) or [])
    return ids


def stage_index_file(path: str, content: bytes) -> None:
    """Write to the worktree path and stage it with `git add --sparse`.

    The SME-ExamQuestion lane dirs sit outside the sparse cone; the worktree
    write is the blob-delivery vehicle, the index entry is the deliverable.
    """
    fp = REPO / path
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_bytes(content)
    git("add", "--sparse", "--", path)


def harvest_lane(lane: str, targets: list[tuple[str, str, str]],
                 blobs: dict[str, bytes]) -> tuple[dict, dict, set[str]]:
    spec: dict[str, dict] = {}
    notes_base = None
    n_notes = n_manifests = n_eq = 0
    eq_refs: list[str] = []
    for oid, path, kind in targets:
        payload = blobs[oid]
        doc = json.loads(payload.decode("utf-8"))
        if kind == "manifest":
            n_manifests += 1
            notes_base = doc.get("notes_base")
            continue
        if kind == "note":
            n_notes += 1
            note_id = doc.get("note_id")
            if not note_id:
                raise RuntimeError(f"{lane}: note without note_id: {path}")
            page_slug = path.rsplit("/", 1)[-1][:-5]
            hits: list[dict] = []
            walk_blocks(doc.get("blocks", []), hits)
            for h in hits:
                if not h["id"]:
                    raise RuntimeError(f"{lane}: block without id: {path}")
                e = spec.setdefault(h["id"], {
                    "name": h["name"], "definition": h["definition"],
                    "notes": set(), "subtopic_slugs": set()})
                if not e["definition"] and h["definition"]:
                    e["definition"] = h["definition"]
                e["notes"].add(note_id)
                e["subtopic_slugs"].add(page_slug)
        else:
            n_eq += 1
            eq_refs.extend(eq_part_ids(doc))

    if n_manifests != 1 or not notes_base:
        raise RuntimeError(f"{lane}: expected exactly one notes manifest with "
                           f"notes_base, got {n_manifests} manifests, "
                           f"notes_base={notes_base!r}")

    spec_points = {}
    for sid in sorted(spec):
        e = spec[sid]
        spec_points[sid] = {
            "name": e["name"],
            "definition": e["definition"],
            "notes": sorted(e["notes"]),
            "subtopic_slugs": sorted(e["subtopic_slugs"]),
        }

    uniq_refs = sorted(set(eq_refs))
    missing = [sid for sid in uniq_refs if sid not in spec]
    covered = [sid for sid in uniq_refs if sid in spec]

    doc_out = {
        "schema": SCHEMA,
        "generated_utc": FIXED_STAMP,
        "course_slug": lane,
        "notes_base": notes_base,
        "source_pages": n_notes,
        "fetch_failures": [],
        "spec_points": spec_points,
        "coverage": {
            "question_part_ids_total": len(uniq_refs),
            "covered_by_index": len(covered),
            "missing_from_index": missing,
        },
    }
    content = json.dumps(doc_out, ensure_ascii=False, indent=1).encode("utf-8")

    # fail-closed sidecar reconciliation
    sc = json.loads((REPO / "spec-links" / f"{lane}.json").read_text(encoding="utf-8"))
    side_universe = sc.get("anchors", {}).get("universe_ids")
    if side_universe != len(spec):
        raise RuntimeError(f"{lane}: universe mismatch index={len(spec)} "
                           f"sidecar={side_universe}")

    stats = {
        "lane": lane,
        "notes_files": n_notes,
        "eq_topics": n_eq,
        "universe_ids": len(spec),
        "universe_full_definition": sum(1 for e in spec.values() if e["definition"]),
        "universe_name_only": sum(1 for e in spec.values() if not e["definition"]),
        "question_part_refs_total": len(eq_refs),
        "question_part_ids_unique": len(uniq_refs),
        "covered_by_index": len(covered),
        "missing_from_index": len(missing),
        "notes_base": notes_base,
    }
    return content, stats, set(missing)


def main() -> int:
    t0 = time.time()
    ls = lanes()
    print(f"CIE lanes: {len(ls)}")
    all_targets: dict[str, list[tuple[str, str, str]]] = {}
    for lane in ls:
        all_targets[lane] = list_targets(lane)
    flat = [t for v in all_targets.values() for t in v]
    print(f"total blobs to read: {len(flat)}")
    blobs = read_blobs(flat)

    stats_rows = []
    dangling_by_lane: dict[str, list[str]] = {}
    universes: dict[str, set[str]] = {}
    for lane in ls:
        content, stats, missing = harvest_lane(lane, all_targets[lane], blobs)
        path = f"SME-ExamQuestion/{lane}/spec_point_index.json"
        stage_index_file(path, content)
        stats_rows.append(stats)
        dangling_by_lane[lane] = sorted(missing)
        universes[lane] = set(json.loads(content)["spec_points"].keys())
        print(f"[{lane}] universe {stats['universe_ids']} "
              f"(full-def {stats['universe_full_definition']} / name-only "
              f"{stats['universe_name_only']}) | part ids "
              f"{stats['question_part_ids_unique']} covered "
              f"{stats['covered_by_index']} missing {stats['missing_from_index']}")

    # cross-lane cure analysis over the harvested universes
    all_ids = set().union(*universes.values()) if universes else set()
    cross_curable = cross_uncurable = 0
    for lane, dang in dangling_by_lane.items():
        others = all_ids - universes[lane]
        cross_curable += len(set(dang) & others)
        cross_uncurable += len(set(dang) - others)

    summary = {
        "schema": SCHEMA,
        "generated_utc": FIXED_STAMP,
        "directive": "ignite the SME-native spec-point index harvest lane",
        "gateway_trace": "1a153238abda24e1",
        "fires": "T-SPECS-CIE-VERDICT-1 record NEXT lane #1",
        "lanes": len(ls),
        "universe_ids_total_unique": len(all_ids),
        "universe_ids_sum_per_lane": sum(s["universe_ids"] for s in stats_rows),
        "universe_full_definition": sum(s["universe_full_definition"] for s in stats_rows),
        "universe_name_only": sum(s["universe_name_only"] for s in stats_rows),
        "question_part_refs_total": sum(s["question_part_refs_total"] for s in stats_rows),
        "question_part_ids_unique_sum": sum(s["question_part_ids_unique"] for s in stats_rows),
        "covered_by_index_sum": sum(s["covered_by_index"] for s in stats_rows),
        "missing_from_index_sum": sum(s["missing_from_index"] for s in stats_rows),
        "dangling_cross_lane_curable": cross_curable,
        "dangling_cross_lane_uncurable": cross_uncurable,
        "elapsed_seconds": round(time.time() - t0, 1),
        "lanes_detail": stats_rows,
    }
    STATS_OUT.write_text(json.dumps(summary, ensure_ascii=False, indent=1) + "\n",
                         encoding="utf-8")
    print(f"\nHARVEST SUMMARY: {json.dumps({k: v for k, v in summary.items() if k != 'lanes_detail'}, indent=1)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
