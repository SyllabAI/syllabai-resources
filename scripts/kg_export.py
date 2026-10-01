#!/usr/bin/env python3
"""kg_export.py — resources-side canonicalKG export + golden-sample regression gate.

    graph/igcse-chemistry/{topics.yaml,specification_points.yaml}
        -> canonicalKG JSON (GRAPH_CONTRACT v1.0 payload)

This is the task-B counterpart of the demo repo's exporter: the demo one
serves the visualizer from content/<slug>/curriculum.json, this one proves
the RESOURCES ratified store can regenerate the same canonicalKG that the
v75 OpenHuman build's syncCanonicalKG() produced (the golden sample).

What is corpus-derived here (and therefore exported):
    Subject / Section / SubTopic / SpecificationPoint nodes, hier edges
    (214), assess edges (4 sections x 2 papers, derived from the
    applicability census on every ratified point).

What is NOT corpus-derived (and therefore NOT exported — the corpus
discipline forbids inventing edges; see the task-B reconciliation report):
    the 30 pre + 5 rel point-level edges are v75 hand-curated pedagogy
    with no resources-side source yet. They stay golden-side until the
    operator ratifies a point-edge store. The golden gate pins them as
    EXPECTED_GOLDEN_ONLY so their absence is auditable, not silent.

Papers display metadata (marks / duration / weight) is presentation
metadata from the official Issue 3 assessment table; the parsed corpus
does not capture the assessment-table rows, so it is pinned verbatim in
PAPER_META below (same values the golden sample carries).

Usage:
    python3 scripts/kg_export.py                  # export -> graph/igcse-chemistry/_derived/
    python3 scripts/kg_export.py --out DIR        # custom output dir
    python3 scripts/kg_export.py --check-only     # validate, write nothing
    python3 scripts/kg_export.py --verify-golden  # in-memory export + golden gate (CI step)
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
GRAPH_DIR = REPO / "graph" / "igcse-chemistry"
OUT_DIR = GRAPH_DIR / "_derived"
GOLDEN_FIXTURE = GRAPH_DIR / "_golden" / "canonicalKG.edexcel-chemistry-4ch1.json"
GATE_LEDGER = REPO / "graph" / "reports" / "KG_TASKB_GOLDEN_GATE.json"

CONTRACT_VERSION = "1.0"
NODE_TYPES = {"Subject", "Section", "SubTopic", "SpecificationPoint", "ExamPaper"}
EDGE_TYPES = {"hier", "pre", "rel", "assess"}

# display truth (mirrors the demo repo's courses.json registry entry for 4CH1)
QUALS = {
    "igcse-chemistry": {
        "curriculum_code": "4CH1",
        "subject_label": "Chemistry",
        "board": "Edexcel",
        "level": "International GCSE",
    }
}

# presentation metadata pinned from the official Issue 3 assessment table,
# verbatim as the v75 golden sample renders it (values, not inventions —
# see graph/reports/KG_TASKB_RECONCILIATION_2026-10-01.md section 5)
PAPER_META = {
    "1C": {"id": "paper1", "label": "Paper 1C \u00b7 110 marks",
           "meta": "2 hour \u00b7 61.1%", "marks": 110, "weight": "61.1%"},
    "2C": {"id": "paper2", "label": "Paper 2C \u00b7 70 marks",
           "meta": "1h 15m \u00b7 38.9%", "marks": 70, "weight": "38.9%"},
}


def join_wording(p: dict) -> str:
    """Reconstruct the v75-style inline-bullet statement from the ratified
    store's split fields (official_wording + official_bullets)."""
    w = (p.get("official_wording") or "").strip()
    bullets = p.get("official_bullets") or []
    if not bullets:
        return w
    return w + " " + " ".join(f"\u2022 {b}".strip() for b in bullets)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ExportError(RuntimeError):
    pass


def build_projection() -> dict:
    """Derive the canonicalKG projection from the ratified store. Raises
    ExportError on any structural violation (fail-closed, zero invention)."""
    topics = yaml.safe_load((GRAPH_DIR / "topics.yaml").read_text())
    spdoc = yaml.safe_load((GRAPH_DIR / "specification_points.yaml").read_text())

    qual = "igcse-chemistry"
    q = QUALS[qual]
    code = q["curriculum_code"]

    secs = sorted(topics["topics"], key=lambda t: t["ordering"])
    sec_codes = [t["code"] for t in secs]
    expected = [f"{code}-S{i}" for i in range(1, 5)]
    if sec_codes != expected:
        raise ExportError(f"unexpected ratified topic set {sec_codes}; "
                          f"exporter is scoped to the content sections {expected}")
    sec_no = {t["code"]: str(i + 1) for i, t in enumerate(secs)}

    subs_by_parent: dict[str, list[dict]] = {}
    for s in sorted(topics["subtopics"], key=lambda x: (x.get("ordering") or 0)):
        subs_by_parent.setdefault(s["parent"], []).append(s)
    if set(subs_by_parent) - set(sec_codes):
        raise ExportError(f"subtopics attached to unknown topics: "
                          f"{sorted(set(subs_by_parent) - set(sec_codes))}")

    r_sub_id: dict[str, str] = {}
    seen_sub_ids: set[str] = set()
    sub_titles_by_sec: dict[str, list[str]] = {}
    for parent, lst in subs_by_parent.items():
        n = sec_no[parent]
        letters = []
        for s in lst:
            sid = f"{n}{s['letter']}"
            if sid in seen_sub_ids:
                raise ExportError(f"duplicate subtopic id {sid}")
            seen_sub_ids.add(sid)
            r_sub_id[s["code"]] = sid
            letters.append(s["letter"])
            sub_titles_by_sec.setdefault(parent, []).append(s["title"])
        if letters != sorted(letters):
            raise ExportError(f"subtopic letters not strictly ordered in "
                              f"{parent}: {letters}")
    for parent, titles in sub_titles_by_sec.items():
        dupes = {t for t in titles if titles.count(t) > 1}
        if dupes:
            raise ExportError(f"duplicate subtopic titles in {parent}: {dupes}")

    points = spdoc["specification_points"]
    if len(points) != 182:
        raise ExportError(f"expected 182 ratified points, got {len(points)}")

    nodes: list[dict] = []
    nodes.append({"id": "subject", "type": "Subject", "label": q["subject_label"]})
    for t in secs:
        n = sec_no[t["code"]]
        nodes.append({"id": f"sec{n}", "type": "Section", "section": n,
                      "label": t["title"]})
    for parent, lst in subs_by_parent.items():
        n = sec_no[parent]
        for s in lst:
            nodes.append({"id": r_sub_id[s["code"]], "type": "SubTopic",
                          "section": n, "label": s["title"]})

    edges: list[list[str]] = []
    for i in range(1, 5):
        edges.append(["subject", f"sec{i}", "hier"])
    for parent, lst in subs_by_parent.items():
        n = sec_no[parent]
        for s in lst:
            edges.append([f"sec{n}", r_sub_id[s["code"]], "hier"])

    paper_labels: set[str] = set()
    sub_title = {sid: nd["label"] for sid, nd in
                 {r_sub_id[s["code"]]: {"label": s["title"]}
                  for lst in subs_by_parent.values() for s in lst}.items()}
    point_nodes = []
    for p in points:
        sub = r_sub_id.get(p["subsection"])
        if p["subsection"] is None or sub is None:
            raise ExportError(f"point {p['official_code']}: subsection "
                              f"{p['subsection']!r} not resolvable "
                              f"(exactly one subtopic parent required)")
        label = p["official_code"]
        applic = p.get("applicability") or {}
        paper_labels.update(applic.get("papers") or [])
        point_nodes.append({
            "id": "p:" + label, "type": "SpecificationPoint", "pointId": label,
            "label": label, "statement": join_wording(p),
            "section": sec_no[p["section"]],
            "subtopic": sub_title[sub],
        })
    nodes.extend(point_nodes)
    for p in points:
        edges.append([r_sub_id[p["subsection"]], "p:" + p["official_code"], "hier"])

    missing_meta = sorted(paper_labels - set(PAPER_META))
    if missing_meta:
        raise ExportError(f"papers {missing_meta} present in applicability "
                          f"census but missing from PAPER_META — extend the "
                          f"pinned constant with official-source values")
    paper_nodes = []
    for lab in sorted(paper_labels):
        pm = PAPER_META[lab]
        paper_nodes.append({"id": pm["id"], "type": "ExamPaper",
                            "label": pm["label"], "meta": pm["meta"]})
    nodes.extend(paper_nodes)
    for lab in sorted(paper_labels):
        pm = PAPER_META[lab]
        for i in range(1, 5):
            edges.append([f"sec{i}", pm["id"], "assess"])

    # referential integrity + contract check
    ids = {n["id"] for n in nodes}
    if len(ids) != len(nodes):
        raise ExportError("duplicate node ids")
    for e in edges:
        if e[0] not in ids or e[1] not in ids:
            raise ExportError(f"edge endpoint missing: {e}")
        if e[2] not in EDGE_TYPES:
            raise ExportError(f"edge kind not in contract: {e}")
    for n in nodes:
        if n["type"] not in NODE_TYPES:
            raise ExportError(f"node type not in contract: {n['type']}")

    hier = sum(1 for e in edges if e[2] == "hier")
    assess = sum(1 for e in edges if e[2] == "assess")
    meta = {
        "artifact": "canonicalKG",
        "qualification": {
            "board": q["board"], "level": q["level"],
            "subject": q["subject_label"], "code": code,
            "papers": [
                {"id": PAPER_META[lab]["id"], "label": PAPER_META[lab]["label"],
                 "marks": PAPER_META[lab]["marks"], "weight": PAPER_META[lab]["weight"]}
                for lab in sorted(paper_labels)
            ],
        },
        "source": {
            "store": "graph/igcse-chemistry (operator-ratified store)",
            "files": ["topics.yaml", "specification_points.yaml"],
            "note": "corpus-derived export. Papers display metadata pinned "
                    "verbatim from the official Issue 3 assessment table as "
                    "rendered by the v75 golden sample (not yet corpus-captured; "
                    "see the task-B reconciliation report). Point-level pre/rel "
                    "edges are v75-curated and deliberately NOT exported.",
        },
        "emittedBy": "scripts/kg_export.py",
        "generatedAtUtc": dt.datetime.now(dt.timezone.utc)
                          .replace(microsecond=0).isoformat(),
        "goldenRegression": {
            "fixture": "graph/igcse-chemistry/_golden/"
                       "canonicalKG.edexcel-chemistry-4ch1.json",
            "run": "python3 scripts/kg_export.py --verify-golden",
        },
        "contract": {
            "version": CONTRACT_VERSION,
            "nodeTypes": sorted(NODE_TYPES),
            "edgeTypes": sorted(EDGE_TYPES),
        },
        "counts": {
            "nodes": len(nodes), "edges": len(edges),
            "byType": {
                "Subject": sum(1 for n in nodes if n["type"] == "Subject"),
                "Section": sum(1 for n in nodes if n["type"] == "Section"),
                "SubTopic": sum(1 for n in nodes if n["type"] == "SubTopic"),
                "SpecificationPoint": sum(1 for n in nodes
                                          if n["type"] == "SpecificationPoint"),
                "ExamPaper": sum(1 for n in nodes if n["type"] == "ExamPaper"),
            },
            "edgesByType": {"hier": hier, "assess": assess, "pre": 0, "rel": 0},
        },
    }
    return {"meta": meta, "nodes": nodes, "edges": edges}


def export(out_dir: Path | None, check_only: bool) -> Path | None:
    doc = build_projection()
    print(f"export: {doc['meta']['counts']['nodes']} nodes / "
          f"{doc['meta']['counts']['edges']} edges "
          f"(hier {doc['meta']['counts']['edgesByType']['hier']}, "
          f"assess {doc['meta']['counts']['edgesByType']['assess']})")
    if check_only:
        print("check-only: validated, wrote nothing")
        return None
    out_dir = out_dir or OUT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "canonicalKG.edexcel-chemistry-4ch1.json"
    out.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {out.relative_to(REPO)} ({out.stat().st_size} B)")
    return out


def verify_golden() -> int:
    """Golden-sample regression gate. Compares the in-memory projection
    against the vendored golden fixture using the pinned acceptance ledger
    (graph/reports/KG_TASKB_GOLDEN_GATE.json). Fails closed: anything not
    explained by the ledger is a hard failure."""
    doc = build_projection()
    if not GOLDEN_FIXTURE.exists():
        print(f"GATE RED: golden fixture missing: {GOLDEN_FIXTURE}")
        return 1
    if not GATE_LEDGER.exists():
        print(f"GATE RED: acceptance ledger missing: {GATE_LEDGER}")
        return 1
    golden = json.loads(GOLDEN_FIXTURE.read_text())
    ledger = json.loads(GATE_LEDGER.read_text())

    failures: list[str] = []

    fixture_sha = sha256_file(GOLDEN_FIXTURE)
    if fixture_sha != ledger["golden_fixture"]["sha256"]:
        failures.append("golden fixture sha256 drifted from the pinned ledger")

    g_nodes = {n["id"]: n for n in golden["nodes"]}
    r_nodes = {n["id"]: n for n in doc["nodes"]}
    only_g = sorted(set(g_nodes) - set(r_nodes))
    only_r = sorted(set(r_nodes) - set(g_nodes))
    if only_r:
        failures.append(f"resources-only nodes (unexpected): {only_r}")
    exp_nodes = ledger["expected"]["nodes"]
    if sorted(only_g) != sorted(exp_nodes["golden_only_ids"]):
        failures.append(f"golden-only nodes {only_g} != pinned "
                        f"{exp_nodes['golden_only_ids']}")

    variants = ledger["accepted_text_variants"]
    seen_variant_keys = set()
    for nid in sorted(set(g_nodes) & set(r_nodes)):
        gn, rn = g_nodes[nid], r_nodes[nid]
        for f in ("type", "label", "section", "subtopic", "pointId", "statement"):
            gv, rv = gn.get(f), rn.get(f)
            if gv == rv:
                continue
            key = f"{nid}:{f}"
            av = variants.get(key)
            if av is None:
                failures.append(f"unaccepted field diff {key}: "
                                f"golden={gv!r} resources={rv!r}")
            elif av["golden"] != gv or av["resources"] != rv:
                failures.append(f"accepted variant {key} drifted from its "
                                f"pinned pair")
            else:
                seen_variant_keys.add(key)
    stale = sorted(set(variants) - seen_variant_keys)
    if stale:
        failures.append(f"pinned variants no longer differ (stale ledger): {stale}")

    g_edges = {(e[0], e[1], e[2]) for e in golden["edges"]}
    r_edges = {(e[0], e[1], e[2]) for e in doc["edges"]}
    e_only_g = sorted(g_edges - r_edges)
    e_only_r = sorted(r_edges - g_edges)
    if e_only_r:
        failures.append(f"resources-only edges (unexpected): {e_only_r}")
    exp_edges = ledger["expected"]["edges"]
    if sorted(map(list, e_only_g)) != sorted(exp_edges["golden_only_exact"]):
        failures.append("golden-only edges differ from the pinned curated set "
                        f"(got {len(e_only_g)}, pinned "
                        f"{len(exp_edges['golden_only_exact'])})")

    exp_stmt = ledger["expected"]["statements"]
    r_points = {n["pointId"]: n for n in doc["nodes"]
                if n["type"] == "SpecificationPoint"}
    g_points = {n["pointId"]: n for n in golden["nodes"]
                if n["type"] == "SpecificationPoint"}
    exact = sum(1 for pid in g_points
                if g_points[pid].get("statement") == r_points.get(pid, {}).get("statement"))
    if exact != exp_stmt["exact"]:
        failures.append(f"exact statement count {exact} != pinned "
                        f"{exp_stmt['exact']}")

    if failures:
        print("GOLDEN GATE RED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("GOLDEN GATE GREEN — resources projection reproduces the golden "
          f"canonicalKG within the pinned ledger "
          f"({len(r_nodes)} nodes / {len(r_edges)} edges; "
          f"{exact}/{len(g_points)} statements exact, "
          f"{len(seen_variant_keys)} accepted text variants, "
          f"{len(e_only_g)} golden-only curated edges pinned)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", type=Path, default=None,
                    help="output directory (default graph/igcse-chemistry/_derived)")
    ap.add_argument("--check-only", action="store_true",
                    help="validate the projection, write nothing")
    ap.add_argument("--verify-golden", action="store_true",
                    help="run the golden-sample regression gate and exit")
    args = ap.parse_args()
    if args.verify_golden:
        return verify_golden()
    export(args.out, args.check_only)
    return 0


if __name__ == "__main__":
    sys.exit(main())
