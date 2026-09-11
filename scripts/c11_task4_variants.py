#!/usr/bin/env python3
"""
T-C11 — Task-4 supplementary negative-control variants (operator review round).

The frozen suite (scripts/c11_negative_test.py classes 10-11) already machine-
tests the two canonical 4.15 corruptions:
  10  concept attached to 4CH1-4.15 citing the acid-rain note
  11  EXPLAINED_BY built from the premise+consequence notes

This script verifies the REMAINING lure variants the operator tasking names —
the system must still refuse to manufacture 4CH1-4.15 coverage or an
unsupported remediation path merely because:

  V1  the SPECIFICATION WORDING is quoted as the anchor (semantic relatedness
      via the official 4.15 wording itself — an attacker quoting the spec to
      "prove" the attachment),
  V2  sulfur/combustion/SO2/acid-rain concepts exist in OTHER notes (the
      combustion note maps to 4.11-4.13; the acid-rain note to 4.14/4.16 —
      neither is 4.15 coverage),
  V3  a REMEDIATED_BY path is assembled from byte-verifying quotes taken from
      those uncovered notes (quotes are genuine, the coverage is not).

Each variant is injected into a throwaway copy of the graph directory; the
checker groups 10-11 MUST catch each (a miss fails this script). The T-C10
notes crosscheck always reads the REAL notes root, so the copy cannot cheat it.

Usage: python3 scripts/c11_task4_variants.py
"""
from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_check as gc  # noqa: E402

REPO = gc.REPO
GRAPH = gc.GRAPH_DEFAULT

ACID_RAIN_NOTE = ("Chemistry IGCSE Revision Notes/4. Organic Chemistry/b. Crude Oil/"
                  "Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry "
                  "Revision Notes 2017.md")
COMBUSTION_NOTE = ("Chemistry IGCSE Revision Notes/4. Organic Chemistry/b. Crude Oil/"
                   "Definition of combustion - IGCSE Chemistry Revision Notes.md")
ACID_RAIN_QUOTE = ("The sulfur dioxide produced from the combustion of fossil fuels "
                   "dissolves in rainwater")
COMBUSTION_QUOTE = "All these fuels contain carbon, hydrogen and small quantities of sulfur"
# 4.15 official wording (specification_points.yaml): used whole — an attacker
# quoting the spec itself at the attachment
SPEC_415_QUOTE = ("explain how the combustion of some impurities in hydrocarbon fuels "
                  "results in the formation of sulfur dioxide")

PROV = {"tier": "AI_SUGGESTED", "model_version": "GLM (Super Z agent, z.ai)",
        "extraction_pass": "c11-pilot-pass-1",
        "derivation_method": "SINGLE_SOURCE_CAUSAL_TEACHING",
        "derivation_notes": "task-4 variant injection",
        "upstream": "negative control variant", "generated_date": "2026-09-11"}


def clone_graph(tmp: Path) -> Path:
    tmp.mkdir(parents=True, exist_ok=True)
    g = tmp / "graph"
    g.mkdir()
    for f in sorted(GRAPH.glob("*.yaml")):
        shutil.copy2(f, g / f.name)
    return g


def load(g: Path, fn: str):
    return yaml.safe_load((g / fn).read_text(encoding="utf-8"))


def save(g: Path, fn: str, data) -> None:
    (g / fn).write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False,
                                       width=100), encoding="utf-8")


def run_checks(g: Path):
    c09 = gc.load_all(g)
    c11 = gc.load_c11(g)
    chk1 = gc.check_c11_concepts(c11, c09)
    chk2 = gc.check_c11_concept_edges(c11, c09)
    return chk1, chk2


def mut_v1_spec_wording_anchor(g: Path):
    """Lure: quote the OFFICIAL 4.15 wording as the attachment's SPEC anchor."""
    d = load(g, "concepts.yaml")
    d["nodes"].append({
        "code": "4CH1-CON-SO2-FROM-IMPURITIES", "family": "CONCEPT",
        "title": "SO2 formation from fuel impurities (spec-wording lure)",
        "aliases": [],
        "spec_points": [{"code": "4CH1-4.15", "role": "CORE",
                         "evidence": [{"kind": "SPEC",
                                       "file": "graph/specification_points.yaml",
                                       "quote": SPEC_415_QUOTE}]}],
        "provenance": dict(PROV), "confidence": "high",
        "validation_status": "SUGGESTED",
        "version": 1, "created_at": "2026-09-11", "damage_flags": []})
    save(g, "concepts.yaml", d)


def mut_v2_semantically_related_notes(g: Path):
    """Lure: attach to 4.15 citing the combustion note (4.11-4.13 coverage) —
    'combustion exists' / 'sulfur exists in fuels'."""
    d = load(g, "concepts.yaml")
    d["nodes"].append({
        "code": "4CH1-CON-FUEL-IMPURITY-COMBUSTION", "family": "CONCEPT",
        "title": "Combustion of fuel impurities (topical-similarity lure)",
        "aliases": [],
        "spec_points": [{"code": "4CH1-4.15", "role": "CORE",
                         "evidence": [{"kind": "NOTE", "file": COMBUSTION_NOTE,
                                       "quote": COMBUSTION_QUOTE}]}],
        "provenance": dict(PROV), "confidence": "high",
        "validation_status": "SUGGESTED",
        "version": 1, "created_at": "2026-09-11", "damage_flags": []})
    save(g, "concepts.yaml", d)


def mut_v3_remediation_from_uncovered_notes(g: Path):
    """Lure: a REMEDIATED_BY path assembled from genuine quotes of UNCOVERED
    notes (acid-rain note as misconception evidence, combustion note as the
    'remediation') pointed at an in-slice concept. Quotes byte-verify; the
    coverage does not exist."""
    d = load(g, "concepts.yaml")
    d["nodes"].append({
        "code": "4CH1-MIS-ACID-RAIN-CAUSE", "family": "MISCONCEPTION",
        "pattern_class": "ERRONEOUS_BELIEF", "title": "SO2/acid-rain (remediation lure)",
        "aliases": [],
        "evidence": [{"kind": "NOTE", "file": ACID_RAIN_NOTE,
                      "quote": ACID_RAIN_QUOTE}],
        "remediation_evidence": [{"kind": "NOTE", "file": COMBUSTION_NOTE,
                                  "quote": COMBUSTION_QUOTE}],
        "provenance": dict(PROV), "confidence": "high",
        "validation_status": "SUGGESTED",
        "version": 1, "created_at": "2026-09-11", "damage_flags": []})
    save(g, "concepts.yaml", d)
    e = load(g, "concept_edges.yaml")
    e["edges"].append({
        "source": "4CH1-MIS-ACID-RAIN-CAUSE", "relation": "REMEDIATED_BY",
        "target": "4CH1-CON-EQ-SYMBOL",
        "evidence": [{"kind": "NOTE", "file": ACID_RAIN_NOTE,
                      "quote": ACID_RAIN_QUOTE}],
        "provenance": dict(PROV), "confidence": "high",
        "validation_status": "SUGGESTED", "ambiguity_note": None,
        "version": 1, "created_at": "2026-09-11"})
    save(g, "concept_edges.yaml", e)


VARIANTS = {
    "V1": (mut_v1_spec_wording_anchor,
           ["c11.5", "NEGATIVE CONTROL"],
           "4.15 attachment via official spec wording as SPEC anchor"),
    "V2": (mut_v2_semantically_related_notes,
           ["c11.5", "NEGATIVE CONTROL"],
           "4.15 attachment via semantically-related combustion note (4.11-4.13)"),
    "V3": (mut_v3_remediation_from_uncovered_notes,
           ["c11.6", "no anchor is admissible"],
           "REMEDIATED_BY path from uncovered notes (byte-true quotes)"),
}


def main2():
    tmp = Path(tempfile.mkdtemp(prefix="c11_task4_"))
    passed = failed = 0
    try:
        for tid, (mut, expects, label) in sorted(VARIANTS.items()):
            g = clone_graph(tmp / tid.lower())
            mut(g)
            chk1, chk2 = run_checks(g)
            allf = chk1.failures + chk2.failures
            caught = bool(allf) and all(any(s in f for f in allf) for s in expects)
            if caught:
                print(f"PASS  {tid} {label}")
                passed += 1
            else:
                print(f"FAIL  {tid} {label}: expected {expects}, got "
                      f"{allf[:3] if allf else 'NOTHING CAUGHT'}")
                failed += 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print()
    if failed:
        print(f"c11_task4_variants: {failed} FAILURE(S), {passed} passed")
        sys.exit(1)
    print(f"c11_task4_variants: ALL PASS — {passed}/{passed + failed} "
          f"(4.15 spec-wording / topical-similarity / uncovered-remediation "
          f"lures all machine-rejected)")


if __name__ == "__main__":
    main2()
