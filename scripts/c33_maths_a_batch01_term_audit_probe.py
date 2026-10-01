#!/usr/bin/env python3
"""T-C33 K2-C-1 — batch-B01 term-audit probe (authoring aid; the
c11_batch11_term_audit_probe.py pattern adapted to a first-batch state).

Runs the batch's candidate vocabulary (node titles + aliases + the edge-bearing
terms) against the WHOLE ratified maths-a surface — the 188 specification-point
wordings, the 6 topic titles and the 39 subtopic codes — case-folded substring,
and prints every match with its store row. Two purposes:

  1. duplicate-mint prevention: a B01 candidate whose term is already carried by
     a DIFFERENT batch's SP wording flags a future cross-batch boundary decision
     (B01 mints nothing against those rows — the map is recorded, not acted on);
  2. the shared-term map: later batches (B02..B16) inherit this audit instead of
     re-deriving it, so cross-batch boundary rulings start from machine truth.

Exit 0 always (the probe informs; the preverify enforces), except on hard
errors (missing stores / unparsable record).
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QUAL = "igcse-maths-a"
DECISIONS = HERE / "c33_maths_a_batch01_decisions.yaml"

# candidate terms: node titles are decomposed into their head nouns + the
# aliases are audited whole; the list is the batch's mint vocabulary
TERM_SOURCES = ("titles", "aliases", "demanded_substance_heads")


def main() -> int:
    doc = yaml.safe_load(DECISIONS.read_text(encoding="utf-8"))
    store = yaml.safe_load(
        (REPO / f"graph/{QUAL}/specification_points.yaml").read_text("utf-8"))
    topics = yaml.safe_load(
        (REPO / f"graph/{QUAL}/topics.yaml").read_text("utf-8"))

    rows = store["specification_points"]
    slice_sps = set(doc["meta"]["scope"]["spec_points"])

    terms: list[str] = []
    for x in doc["nodes"]:
        terms.append(x["title"])
        terms.extend(x.get("aliases") or [])
    # head-noun decomposition of titles (before the parenthesis / dash)
    heads = []
    for x in doc["nodes"]:
        t = x["title"].split("(")[0].split(" — ")[0].strip()
        heads.append(t)
    terms.extend(heads)

    surface = []
    for r in rows:
        surface.append((r["code"], "SP", r["official_wording"]))
    for t in topics["topics"]:
        surface.append((t["code"], "TOPIC", t["title"]))
    for s in topics["subtopics"]:
        surface.append((s["code"], "SUBTOPIC",
                        s.get("title_md") or s.get("title") or ""))

    matches: dict[str, list[tuple[str, str, str]]] = {}
    for term in terms:
        tl = term.lower().strip()
        if len(tl) < 4:
            continue
        hits = [(code, kind, text) for code, kind, text in surface
                if tl in text.lower()]
        if hits:
            matches[term] = hits

    print(f"candidate terms audited: {len(terms)} "
          f"({len(doc['nodes'])} nodes x (title + aliases + head))")
    print(f"terms with ratified-surface matches: {len(matches)}")
    in_slice_leak = []
    for term, hits in sorted(matches.items()):
        for code, kind, text in hits:
            tag = "IN-SLICE" if code in slice_sps else "future-batch"
            preview = text[:90]
            print(f"  MATCH {term!r} -> {code} [{kind}] {tag}: {preview}")
            if tag == "IN-SLICE" and kind == "SP":
                in_slice_leak.append((term, code))
    future = sorted({h[0] for hits in matches.values() for h in hits
                     if h[0] not in slice_sps})
    print(f"\nnon-slice SP codes sharing candidate vocabulary "
          f"(the B02.. boundary map, {len(future)} codes): {future}")
    print("no action taken by this probe — the preverify enforces the "
          "in-slice mint discipline; this map is the later batches' "
          "boundary-ruling starting point")
    return 0


if __name__ == "__main__":
    sys.exit(main())
