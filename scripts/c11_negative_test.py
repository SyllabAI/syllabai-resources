#!/usr/bin/env python3
"""
T-C11 — negative tests for the c11-concepts / c11-concept-edges check groups
in graph_check.py (architecture §15).

Twelve corruption classes are injected into a throwaway copy of the graph
directory (the three c11 YAML files only; the T-C10 notes crosscheck always
reads the REAL notes root, so the copy cannot cheat it). Each class MUST be
caught by the corresponding check group; a miss fails this script.

Classes (§15 table):
  1. evidence quote altered (fabricated evidence)          -> c11.4
  2. node code duplicated                                  -> c11.1
  3. edge endpoint referencing an undeclared code          -> c11.7
  4. self-edge                                             -> c11.8
  5. duplicate (source, relation, target)                  -> c11.8
  6. confidence high on a capped derivation_method         -> c11.9
  7. validation_status forged to HUMAN_VALIDATED           -> c11.10
  8. unknown relation_type                                 -> c11.1
  9. REQUIRES_PREREQUISITE cycle injected                  -> c11.8
 10. concept attached to 4CH1-4.15 citing the acid-rain
     note (manufactured coverage)                          -> c11.5 + c11.6
 11. EXPLAINED_BY built from the premise+consequence notes
     (the 4.15 failure mode: combustion note + acid-rain
     note as two anchors)                                  -> c11.6
 12. misconception node without remediation evidence       -> c11.11

Positive control: the unmodified pilot graph passes groups 10-11 AND the
generator re-run over unchanged decisions is byte-identical (idempotence).

Usage: python3 scripts/c11_negative_test.py
"""
from __future__ import annotations

import shutil
import subprocess
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


TESTS = []


def test(name, expect_substrings, which="edges"):
    TESTS.append((name, expect_substrings, which))


def clone_graph_checked(g: Path):
    chk1, chk2 = run_checks(g)
    return chk1, chk2


# --- mutations ----------------------------------------------------------------
# Each mutation fn receives the cloned graph dir; registered in MUTATE by name.


def mut_01_fabricated_quote(g: Path):
    d = load(g, "concepts.yaml")
    d["nodes"][0]["spec_points"][0]["evidence"][0]["quote"] = (
        "This sentence was invented by an LLM and appears nowhere in the corpus.")
    save(g, "concepts.yaml", d)


def mut_02_duplicate_node(g: Path):
    d = load(g, "concepts.yaml")
    d["nodes"].append(dict(d["nodes"][0]))
    save(g, "concepts.yaml", d)


def mut_03_undeclared_endpoint(g: Path):
    d = load(g, "concept_edges.yaml")
    d["edges"][0]["target"] = "4CH1-CON-DOES-NOT-EXIST"
    save(g, "concept_edges.yaml", d)


def mut_04_self_edge(g: Path):
    d = load(g, "concept_edges.yaml")
    for e in d["edges"]:
        if e["relation"] == "EXPLAINED_BY":
            e["target"] = e["source"]
            break
    save(g, "concept_edges.yaml", d)


def mut_05_duplicate_edge(g: Path):
    d = load(g, "concept_edges.yaml")
    sem = [e for e in d["edges"] if e["relation"] != "PART_OF"]
    d["edges"].append(dict(sem[0]))
    save(g, "concept_edges.yaml", d)


def mut_06_confidence_cap(g: Path):
    d = load(g, "concept_edges.yaml")
    for e in d["edges"]:
        if e["relation"] == "REQUIRES_PREREQUISITE" and e["confidence"] == "medium":
            e["confidence"] = "high"
            save(g, "concept_edges.yaml", d)
            return
    raise SystemExit("no medium-confidence prerequisite edge to corrupt")


def mut_07_forged_promotion(g: Path):
    d = load(g, "concept_edges.yaml")
    e = next(e for e in d["edges"] if e["relation"] == "REQUIRES_PREREQUISITE")
    e["validation_status"] = "HUMAN_VALIDATED"
    save(g, "concept_edges.yaml", d)


def mut_08_unknown_relation(g: Path):
    d = load(g, "concept_edges.yaml")
    e = next(e for e in d["edges"] if e["relation"] == "EXPLAINED_BY")
    e["relation"] = "CAUSES_MAGIC_LEARNING"
    save(g, "concept_edges.yaml", d)


def mut_09_cycle(g: Path):
    d = load(g, "concept_edges.yaml")
    # close a cycle: CON-MOLE is a leaf prerequisite; point it back at
    # CON-REACTING-MASS (which transitively requires CON-MOLE)
    d["edges"].append({
        "source": "4CH1-CON-MOLE", "relation": "REQUIRES_PREREQUISITE",
        "target": "4CH1-CON-REACTING-MASS",
        "evidence": [{"kind": "NOTE",
                      "file": "Chemistry IGCSE Revision Notes/1. Principles of "
                              "Chemistry/e. Chemical Formulae, Equations, "
                              "Calculations/Calculating moles and mass - IGCSE "
                              "Chemistry Revision Notes.md",
                      "quote": "Chemical amounts are measured in moles"}],
        "provenance": {"tier": "AI_SUGGESTED",
                       "model_version": "GLM (Super Z agent, z.ai)",
                       "extraction_pass": "c11-pilot-pass-1",
                       "derivation_method": "USED_WITHOUT_RETEACHING",
                       "derivation_notes": "injected cycle",
                       "upstream": "negative test",
                       "generated_date": "2026-09-11"},
        "confidence": "high", "validation_status": "SUGGESTED",
        "ambiguity_note": None, "version": 1, "created_at": "2026-09-11"})
    save(g, "concept_edges.yaml", d)


def mut_10_attach_415(g: Path):
    d = load(g, "concepts.yaml")
    d["nodes"].append({
        "code": "4CH1-CON-SO2-FROM-IMPURITIES", "family": "CONCEPT",
        "title": "SO2 formation from fuel impurities (fabricated)",
        "aliases": [],
        "spec_points": [{"code": gc.C11_NEGATIVE_CONTROL, "role": "CORE",
                         "evidence": [{"kind": "NOTE", "file": ACID_RAIN_NOTE,
                                       "quote": ACID_RAIN_QUOTE}]}],
        "provenance": {"tier": "AI_SUGGESTED",
                       "model_version": "GLM (Super Z agent, z.ai)",
                       "extraction_pass": "c11-pilot-pass-1",
                       "derivation_method": "SINGLE_SOURCE_CAUSAL_TEACHING",
                       "derivation_notes": "fabricated 4.15 coverage",
                       "upstream": "negative test",
                       "generated_date": "2026-09-11"},
        "confidence": "high", "validation_status": "SUGGESTED",
        "version": 1, "created_at": "2026-09-11", "damage_flags": []})
    save(g, "concepts.yaml", d)


def mut_11_premise_consequence(g: Path):
    d = load(g, "concept_edges.yaml")
    d["edges"].append({
        "source": "4CH1-CON-CONSERVATION-MASS", "relation": "EXPLAINED_BY",
        "target": "4CH1-CON-EQ-SYMBOL",
        "evidence": [{"kind": "NOTE", "file": COMBUSTION_NOTE,
                      "quote": COMBUSTION_QUOTE},
                     {"kind": "NOTE", "file": ACID_RAIN_NOTE,
                      "quote": ACID_RAIN_QUOTE}],
        "provenance": {"tier": "AI_SUGGESTED",
                       "model_version": "GLM (Super Z agent, z.ai)",
                       "extraction_pass": "c11-pilot-pass-1",
                       "derivation_method": "SINGLE_SOURCE_CAUSAL_TEACHING",
                       "derivation_notes": "premise+consequence aggregation",
                       "upstream": "negative test",
                       "generated_date": "2026-09-11"},
        "confidence": "high", "validation_status": "SUGGESTED",
        "ambiguity_note": None, "version": 1, "created_at": "2026-09-11"})
    save(g, "concept_edges.yaml", d)


def mut_12_no_remediation(g: Path):
    d = load(g, "concepts.yaml")
    n = next(n for n in d["nodes"] if n.get("family") == "MISCONCEPTION")
    del n["remediation_evidence"]
    save(g, "concepts.yaml", d)


MUTATE = {
    "01": (mut_01_fabricated_quote,
           ["c11.4", "quote NOT found"], "concepts"),
    "02": (mut_02_duplicate_node, ["duplicate node code"], "concepts"),
    "03": (mut_03_undeclared_endpoint, ["c11.7", "not in the pilot node universe"],
           "edges"),
    "04": (mut_04_self_edge, ["self-edge"], "edges"),
    "05": (mut_05_duplicate_edge, ["duplicate edge"], "edges"),
    "06": (mut_06_confidence_cap, ["c11.9", "exceeds cap"], "edges"),
    "07": (mut_07_forged_promotion, ["c11.10"], "edges"),
    "08": (mut_08_unknown_relation, ["unknown relation type"], "edges"),
    "09": (mut_09_cycle, ["cycle"], "edges"),
    "10": (mut_10_attach_415, ["c11.5", "NEGATIVE CONTROL"], "concepts"),
    "11": (mut_11_premise_consequence, ["c11.6", "no anchor is admissible"],
           "edges"),
    "12": (mut_12_no_remediation, ["c11.11", "remediation"], "concepts"),
}


def main2():
    tmp = Path(tempfile.mkdtemp(prefix="c11_negtest_"))
    passed = failed = 0
    try:
        # positive control
        g = clone_graph(tmp / "pos")
        chk1, chk2 = run_checks(g)
        if not (chk1.ok and chk2.ok):
            print(f"FAIL  positive control: {chk1.failures[:2]} {chk2.failures[:2]}")
            failed += 1
        else:
            print("PASS  00 positive control (clean pilot graph: groups 10-11 green)")
            passed += 1

        # corruption classes
        for tid, (mut, expects, _which) in sorted(MUTATE.items()):
            g = clone_graph(tmp / f"c{tid}")
            mut(g)
            chk1, chk2 = run_checks(g)
            allf = chk1.failures + chk2.failures
            caught = bool(allf) and all(any(s in f for f in allf) for s in expects)
            if caught:
                print(f"PASS  {tid} {mut.__name__.replace('mut_', '').replace('_', ' ')}")
                passed += 1
            else:
                print(f"FAIL  {tid} {mut.__name__}: expected {expects}, got "
                      f"{allf[:3] if allf else 'NOTHING CAUGHT'}")
                failed += 1

        # generator idempotence as part of the positive control
        before = {f.name: f.read_bytes() for f in GRAPH.glob("*.yaml")
                  if f.name in gc.C11_FILES}
        r = subprocess.run([sys.executable, str(HERE / "c11_concept_pilot.py")],
                           capture_output=True, text=True, cwd=REPO)
        after = {f.name: f.read_bytes() for f in GRAPH.glob("*.yaml")
                 if f.name in gc.C11_FILES}
        if r.returncode == 0 and before == after:
            print("PASS  13 idempotence (generator re-run byte-identical)")
            passed += 1
        else:
            print("FAIL  13 idempotence")
            failed += 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print()
    if failed:
        print(f"c11_negative_test: {failed} FAILURE(S), {passed} passed")
        sys.exit(1)
    print(f"c11_negative_test: ALL PASS — {passed}/{passed + failed} "
          f"(12 corruption classes caught + positive control + idempotence)")


if __name__ == "__main__":
    main2()
