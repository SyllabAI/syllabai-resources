#!/usr/bin/env python3
"""C28 stage-4: ratified-store serving-plane emitter (D2 option (a) execution).

Emits, per commissioned qual (P3 — a qual appears here only when its ratified
K2 stores exist), into the existing serving surface
Official-Specifications/parsed/_derived/graph/<qual>/:

  concepts.yaml         ratified-store projection (verbatim nodes rows)
  concept_edges.yaml    ratified-store projection (verbatim edges rows)
  explorer_blob.json    per-qual explorer feed, schema explorer-blob/1.0
                        (C28 spec section 4 contract: header with sources +
                        sha256_16 pins; GRAPH_CONTRACT 1.0 content mapping)

Every artifact carries the section-5 provenance header {source path,
source sha256_16, emitted_at, emitter}. Content is verbatim from the ratified
stores — the projection adds nothing of its own (P1/P6). Store paths resolve
exclusively through the C28 path registry (scripts/graph_paths.py).

Drift protection: sweep gate S8 verifies G1 (recorded source sha == live
source sha) and G2 (re-emission is idempotent; `emitted_at` is the sole
volatile field, by documented normalization). Hand-edits to any emitted
artifact fail the battery.

Zero-LLM, deterministic. Emitter id: scripts/c28_emit_explorer_blob.py@1.0.0
"""
import argparse
import datetime
import hashlib
import json
import os
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import graph_paths as GP

EMITTER_ID = "scripts/c28_emit_explorer_blob.py@1.0.0"
DERIVED_ROOT = os.path.join(GP.REPO, "Official-Specifications/parsed/_derived/graph")

PROJECTION_SCHEMA = "ratified-store-projection/1.0"
BLOB_SCHEMA = "explorer-blob/1.0"
GRAPH_CONTRACT = "1.0"

# Ratified stores projected as sibling YAMLs (only for quals whose ratified
# program has earned them — P3). Presence of the ratified concepts store marks
# a qual as K2-commissioned.
PROJECTION_STORES = ("concepts", "concept_edges")

# Ratified stores consumed by the explorer blob, in registry order.
BLOB_SOURCES = ("specification_points", "topics", "assessment_objectives",
                "relationships", "concepts", "concept_edges")

# store -> (source list key inside the store, blob content key)
CONTENT_MAP = (
    ("topics", "topics", "topics"),
    ("topics", "subtopics", "subtopics"),
    ("specification_points", "specification_points", "specification_points"),
    ("relationships", "edges", "relationships"),
    ("assessment_objectives", "assessment_objectives", "assessment_objectives"),
    ("assessment_objectives", "papers", "papers"),
    ("concepts", "nodes", "concepts"),
    ("concept_edges", "edges", "concept_edges"),
)

PROJECTION_NOTE = (
    "Emitter-owned serving projection (C28 spec sections 3.3/5). Rows verbatim "
    "from the ratified store at the pinned sha; never hand-edit - the S8 drift "
    "gate (G1 source freshness + G2 re-emit idempotency) fails on drift. "
    "Authority: the ratified store."
)


def _sha16(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()[:16]


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).replace(
        microsecond=0).isoformat().replace("+00:00", "Z")


def _dump_yaml(path: str, obj) -> None:
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(obj, f, sort_keys=False, allow_unicode=True, width=100)


def _dump_json(path: str, obj) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, ensure_ascii=False)
        f.write("\n")


def _load_store(name: str, qual: str):
    return yaml.safe_load(open(GP.store(name, qual), encoding="utf-8"))


def _dist(rows, key: str):
    d = {}
    for r in rows:
        k = str(r.get(key, "?"))
        d[k] = d.get(k, 0) + 1
    return dict(sorted(d.items()))


def commissioned_quals() -> list:
    """Registry quals whose ratified plane has earned the K2 concept stores (P3)."""
    out = []
    for q in GP._reg()["quals"]:
        try:
            if GP.store("concepts", q).exists() and GP.store("concept_edges", q).exists():
                out.append(q)
        except KeyError:
            continue
    return sorted(out)


def emit(qual: str = None, outdir: str = None) -> dict:
    """Emit the serving-plane artifacts for one qual. Returns a manifest."""
    qual = qual or GP.default_qual()
    outdir = outdir or os.path.join(DERIVED_ROOT, qual)
    os.makedirs(outdir, exist_ok=True)
    now = _now()
    artifacts = {}

    # ---- ratified-store projections (concepts / concept_edges) ----
    for store in PROJECTION_STORES:
        src_rel = GP.store_rel(store, qual)
        src_path = GP.store(store, qual)
        data = _load_store(store, qual)
        proj = {
            "meta": {
                "schema": PROJECTION_SCHEMA,
                "projection_of": src_rel,
                "source_sha256_16": _sha16(src_path),
                "emitter": EMITTER_ID,
                "emitted_at": now,
                "note": PROJECTION_NOTE,
            }
        }
        for k, v in data.items():
            if k != "meta":
                proj[k] = v
        fname = f"{store}.yaml"
        fpath = os.path.join(outdir, fname)
        _dump_yaml(fpath, proj)
        artifacts[fname] = _sha16(fpath)

    # ---- explorer blob (section-4 contract) ----
    sources = [{"path": GP.store_rel(s, qual),
                "sha256_16": _sha16(GP.store(s, qual))} for s in BLOB_SOURCES]
    loaded = {s: _load_store(s, qual) for s in BLOB_SOURCES}
    content = {}
    for store, src_key, blob_key in CONTENT_MAP:
        content[blob_key] = loaded[store][src_key]
    cedges = content["concept_edges"]
    counts = {}
    for blob_key, rows in content.items():
        counts[blob_key] = len(rows)
    counts["concept_edge_validation_status"] = _dist(cedges, "validation_status")
    counts["concepts_by_family"] = _dist(content["concepts"], "family")
    blob = {
        "schema_version": BLOB_SCHEMA,
        "qual": qual,
        "graph_contract": GRAPH_CONTRACT,
        "sources": sources,
        "emitted_at": now,
        "emitter": EMITTER_ID,
        "counts": counts,
        "content": content,
    }
    fpath = os.path.join(outdir, "explorer_blob.json")
    _dump_json(fpath, blob)
    artifacts["explorer_blob.json"] = _sha16(fpath)

    return {"qual": qual, "outdir": outdir, "emitter": EMITTER_ID,
            "emitted_at": now, "artifacts": artifacts, "sources": sources}


def main() -> int:
    ap = argparse.ArgumentParser(description="C28 stage-4 serving-plane emitter")
    ap.add_argument("--qual", default=GP.default_qual())
    ap.add_argument("--outdir", default=None)
    args = ap.parse_args()
    m = emit(args.qual, args.outdir)
    print(f"emitted for {m['qual']} -> {m['outdir']}")
    for fname, sha in sorted(m["artifacts"].items()):
        print(f"  {fname}  sha256_16={sha}")
    for s in m["sources"]:
        print(f"  source {s['path']}  {s['sha256_16']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
