#!/usr/bin/env python3
"""T-C36 K2-C-4 — batch-B04 term-audit probe (authoring aid; the
c35_maths_a_batch03_term_audit_probe.py pattern, fourth-batch instance).

Runs the batch's candidate vocabulary (node titles + aliases + head nouns)
against the WHOLE ratified maths-a surface — the 188 specification-point
wordings, the 6 topic titles and the 39 subtopic codes — case-folded substring,
and prints every match with its store row. Two purposes:

  1. duplicate-mint prevention: a B04 candidate whose term is already carried by
     a DIFFERENT batch's SP wording flags a cross-batch boundary decision (B04
     mints nothing against those rows — the map is recorded, not acted on);
  2. the shared-term map for B05..: this run SUPERSEDES the B03 audit as the
     later batches' boundary-ruling starting point. The B03 map's in-slice
     member (1.6G) is re-classified IN-SLICE here; the audit prints the
     remaining future codes plus any new matches this batch's vocabulary
     surfaces.

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
DECISIONS = HERE / "c36_maths_a_batch04_decisions.yaml"


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
    for term, hits in sorted(matches.items()):
        for code, kind, text in hits:
            tag = "IN-SLICE" if code in slice_sps else "future-batch"
            preview = text[:90]
            print(f"  MATCH {term!r} -> {code} [{kind}] {tag}: {preview}")
    future = sorted({h[0] for hits in matches.values() for h in hits
                     if h[0] not in slice_sps})
    inherited = ["4MA1-1.1H", "4MA1-1.2A", "4MA1-1.6G", "4MA1-2.1D"]
    now_in_slice = sorted(set(inherited) & slice_sps)
    still_future = sorted(set(inherited) - slice_sps)
    print(f"\nB03-inherited boundary codes re-classified by this audit: "
          f"{now_in_slice} now IN-SLICE; {still_future} still future")
    print(f"\nnon-slice SP codes sharing candidate vocabulary "
          f"(the B05.. boundary map, {len(future)} codes): {future}")
    print("no action taken by this probe — the preverify enforces the "
          "in-slice mint discipline; this map supersedes the B03 audit as the "
          "later batches' boundary-ruling starting point")
    return 0


if __name__ == "__main__":
    sys.exit(main())
