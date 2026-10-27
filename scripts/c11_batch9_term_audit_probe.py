#!/usr/bin/env python3
"""T-C11 session 62 — batch-9 boundary-ruling AUDIT PROBE (authoring aid).

Runs the exact match the ruling records (S4-a/b/c candidate terms against
the pre-batch-9 merged store = the live 165-node post-batch-8 state: node
codes + titles + aliases + every edge endpoint, case-folded substring) and
prints the matched terms so the ruling's match_dispositions table is
written against the machine truth, not guessed. The standing checker
(c11_batch9_boundary_check.py) re-runs this match as its B-gate.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402

GRAPH = GP.qual_dir()

TERMS = [
    # S4-a introduction vocabulary (4.1-4.6)
    "hydrocarbon", "hydrocarbons", "organic chemistry", "organic molecule",
    "organic molecules", "organic compound", "empirical formula",
    "molecular formula", "general formula", "structural formula",
    "displayed formula", "full displayed", "homologous series",
    "functional group", "isomer", "isomers", "isomerism", "iupac",
    "nomenclature", "naming", "naming organic", "substitution",
    "addition reaction", "combustion", "classify reactions",
    "classification of reactions", "alkane", "alkanes", "alkene", "alkenes",
    "alcohol", "alcohols", "carboxylic", "ester", "esters", "polymer",
    "polymers", "monomer", "carbon atom", "carbon atoms", "hydrogen atom",
    "hydrogen atoms", "chain", "branched", "unbranched", "molecular model",
    # S4-b crude oil vocabulary (4.7-4.18)
    "crude oil", "fractional distillation", "fraction", "fractions",
    "fractionating column", "refinery gas", "gasoline", "kerosene",
    "diesel", "fuel oil", "bitumen", "residue", "petroleum",
    "boiling point", "viscosity", "colour", "trend", "flammable",
    "flammability", "fuel", "fuels", "complete combustion",
    "incomplete combustion", "carbon monoxide", "carbon particulates",
    "soot", "poisonous", "haemoglobin", "hemoglobin", "blood", "oxygen transport",
    "car engine", "car engines", "nitrogen oxide", "nitrogen oxides",
    "nitrogen dioxide", "sulfur dioxide", "sulphur dioxide", "acid rain",
    "impurity", "impurities", "sulfuric acid", "acidic", "ph below",
    "cracking", "catalytic cracking", "thermal cracking", "long-chain",
    "long chain", "shorter-chain", "shorter chain", "supply and demand",
    "vapor", "vapour", "condense", "condensation", "column", "temperature gradient",
    # S4-c alkanes vocabulary (4.19-4.22)
    "saturated", "single bond", "single bonds", "c-c", "c-h",
    "cnh2n+2", "cnh2n+2", "methane", "ethane", "propane", "butane",
    "pentane", "halogen", "halogens", "bromine", "chlorine", "ultraviolet",
    "uv radiation", "uv light", "photochemical", "hydrogen bromide",
    "hydrogen chloride", "substitution reaction", "substituted",
    "free radical", "mixture of products", "limited to substitution",
    # generic surfaces that appear in the S4-a/b/c notes
    "equation", "equations", "molecule", "molecules", "compound",
    "compounds", "mixture", "mixtures", "boiling", "distillation",
    "heating", "catalyst", "oxide", "oxides", "combusts", "burns",
    "burning", "burned", "releases heat", "exothermic", "energy",
    "covalent bond", "covalent bonds", "electron", "electrons", "ion",
    "ions", "separation", "separated", "condenser", "flask",
]


def main() -> int:
    nodes = yaml.safe_load(
        (GRAPH / "concepts.yaml").read_text(encoding="utf-8"))["nodes"]
    edges = yaml.safe_load(
        (GRAPH / "concept_edges.yaml").read_text(encoding="utf-8"))["edges"]
    blob = []
    for x in nodes:
        blob.append(x["code"])
        blob.append(x["title"])
        blob.extend(x.get("aliases", []))
    store_blob = " || ".join(blob).lower()
    endpoints = " ".join(f"{e['source']} {e['target']}"
                         for e in edges).lower()
    matched = [t for t in TERMS if t in store_blob or t in endpoints]
    unmatched = [t for t in TERMS if t not in matched]
    print(f"terms: {len(TERMS)}  matched: {len(matched)}")
    for t in matched:
        hits = []
        for x in nodes:
            hay = " || ".join([x["code"], x["title"]]
                              + list(x.get("aliases", []))).lower()
            if t in hay:
                hits.append(x["code"])
        ep = t in endpoints
        print(f"  MATCH {t!r}: nodes={hits}{' +endpoints' if ep else ''}")
    print(f"\nunmatched ({len(unmatched)}): {unmatched}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
