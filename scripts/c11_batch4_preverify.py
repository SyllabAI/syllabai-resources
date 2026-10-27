#!/usr/bin/env python3
"""T-C11 session 53 — pre-write verification of the batch-4 decision record
(scripts/c11_batch4_decisions.yaml): every evidence/remediation quote must
byte-verify under the T-C10 norm() in its cited file, every SPEC quote must
sit inside its SP's official wording, and every NOTE anchor file must
HUMAN_VALIDATED-map (T-C10) to a spec point. Mirrors the generator's
G03/c11.4/G07 checks so authoring is fail-closed BEFORE the registry grows.
(The scripts/c11_batch2_preverify.py pattern, batch-4-scoped.)

Session-51 note: this is a PRE-write tool. After the batch-4 record enters
the registry and the graph is generated, the "edge re-uses an existing
identity" failures it reports against the LIVE store are the batch's OWN
edges (self-match) — expected post-generation, not a defect. The
authoring-time run over the pre-registry state was 144/144 green.
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
DEC = HERE / "c11_batch4_decisions.yaml"

_TRANS = {ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = s.translate(_TRANS)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def main() -> int:
    dec = yaml.safe_load(DEC.read_text(encoding="utf-8"))
    spec = yaml.safe_load(
        (REPO / "graph" / "specification_points.yaml").read_text(
            encoding="utf-8"))
    sps = {p["code"]: p for p in spec["specification_points"]}

    # T-C10 HUMAN_VALIDATED mapping index (as the generator's TC10)
    tc10: dict[str, set] = {}
    notes_root = REPO / "Chemistry IGCSE Revision Notes"
    for f in notes_root.rglob("*.md"):
        text = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError:
            continue
        sm = (fm or {}).get("spec_map") or {}
        for sp in sm.get("spec_points", []):
            prov = sp.get("provenance") or {}
            if prov.get("validation_status") == "HUMAN_VALIDATED":
                tc10.setdefault(str(f.relative_to(REPO)), set()).add(sp["code"])

    fails = []
    n_checks = 0

    def check_anchor(anchor, where, require_scoped_note=True):
        nonlocal n_checks
        n_checks += 1
        kind = anchor.get("kind")
        rel = anchor.get("file")
        quote = anchor.get("quote")
        p = REPO / rel
        if not p.exists():
            fails.append(f"{where}: file missing {rel}")
            return
        body = norm(p.read_text(encoding="utf-8"))
        if norm(quote) not in body:
            fails.append(f"{where}: quote NOT in {rel} :: {quote[:70]!r}")
            return
        if kind == "SPEC":
            hit = any(norm(quote) in norm(sps[sp]["official_wording"])
                      for sp in dec["meta"]["scope"]["spec_points"]
                      if sp in sps)
            if not hit:
                fails.append(f"{where}: SPEC quote not inside any scoped SP "
                             f"wording :: {quote[:60]!r}")
        elif kind == "NOTE" and require_scoped_note:
            mapped = tc10.get(rel, set())
            if not (mapped & set(dec["meta"]["scope"]["spec_points"])):
                fails.append(f"{where}: NOTE {rel} does not HUMAN_VALIDATED-"
                             f"map to a scoped SP (mapped: {sorted(mapped)})")

    # NOTE anchors on EDGES may instead map to a cross-boundary endpoint's
    # attached SPs (the generator's G07 rule: source-attached OR source-
    # practical's SP OR target-attached)
    live_nodes = yaml.safe_load(
        (REPO / "graph" / "concepts.yaml").read_text(encoding="utf-8"))
    live_by_code = {n["code"]: n for n in live_nodes["nodes"]}
    own_codes = {n["code"] for n in dec["nodes"]}
    practicals = yaml.safe_load(
        (REPO / "graph" / "practicals.yaml").read_text(encoding="utf-8"))
    pr_by_code = {p["code"]: p for p in practicals["practicals"]}

    def attached(end):
        if end in own_codes:
            n = next(x for x in dec["nodes"] if x["code"] == end)
            if n.get("spec_points"):
                return {a["code"] for a in n["spec_points"]}
        if end in live_by_code:
            n = live_by_code[end]
            if n.get("spec_points"):
                return {a["code"] for a in n["spec_points"]}
        if end in pr_by_code:
            return {pr_by_code[end]["spec_point"]}
        return set()

    for e in dec["edges"]:
        admissible = attached(e["source"]) | attached(e["target"])
        for a in e.get("evidence") or []:
            if a.get("kind") == "NOTE":
                mapped = tc10.get(a.get("file", ""), set())
                if not (mapped & admissible):
                    fails.append(
                        f"edge {e['source']} {e['relation']} {e['target']}: "
                        f"NOTE does not map to any endpoint-attached SP "
                        f"(mapped: {sorted(mapped)})")

    for n in dec["nodes"]:
        for att in n.get("spec_points") or []:
            for a in att.get("evidence") or []:
                check_anchor(a, f"node {n['code']} @ {att['code']}")
        for a in n.get("evidence") or []:
            # misconception node evidence: byte-verification only (G11 has no
            # mapping requirement at node level)
            check_anchor(a, f"node {n['code']} (misconception evidence)",
                         require_scoped_note=False)
        for a in n.get("remediation_evidence") or []:
            check_anchor(a, f"node {n['code']} (remediation)",
                         require_scoped_note=False)

    for e in dec["edges"]:
        for a in e.get("evidence") or []:
            # NOTE-mapping admissibility for edges is enforced by the
            # endpoint-attached-SP block above (G07 rule); here: byte-verify
            check_anchor(a, f"edge {e['source']} {e['relation']} {e['target']}",
                         require_scoped_note=False)

    # cross-boundary edge endpoint existence check: endpoints must be in
    # (the live universe) ∪ (this record's own nodes)
    existing = live_nodes
    codes = {n["code"] for n in existing["nodes"]}
    for e in dec["edges"]:
        for end in (e["source"], e["target"]):
            if end not in codes and end not in own_codes \
                    and not end.startswith("4CH1-PR-"):
                fails.append(f"edge endpoint {end} not in the live universe "
                             f"nor this record")

    # duplicate-identity check against the live authored edges
    edges_doc = yaml.safe_load(
        (REPO / "graph" / "concept_edges.yaml").read_text(encoding="utf-8"))
    live = {(e["source"], e["relation"], e["target"])
            for e in edges_doc["edges"]}
    for e in dec["edges"]:
        k = (e["source"], e["relation"], e["target"])
        if k in live:
            fails.append(f"edge re-uses an existing identity: {k}")
        if e["source"] == e["target"]:
            fails.append(f"self-edge: {k}")

    # scoped-attachment check (G05 shape)
    scope = set(dec["meta"]["scope"]["spec_points"])
    for n in dec["nodes"]:
        for att in n.get("spec_points") or []:
            if att["code"] not in scope:
                fails.append(f"node {n['code']} attaches out-of-scope "
                             f"{att['code']}")
            if "4.15" in att["code"]:
                fails.append(f"negative-control attach on {n['code']}")

    print(f"pre-verification: {n_checks} quote anchors checked")
    if fails:
        print(f"FAIL-CLOSED: {len(fails)} problem(s):")
        for f_ in fails:
            print("  -", f_)
        return 1
    print("ALL QUOTES + ANCHORS + BOUNDARY ENDPOINTS VERIFIED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
