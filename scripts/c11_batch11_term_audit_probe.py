#!/usr/bin/env python3
"""T-C11 session 66 — batch-11 boundary-ruling AUDIT PROBE (authoring aid).

Runs the exact match the ruling records (S4-g/h candidate terms against
the pre-batch-11 merged store = the live 188-node post-batch-10-verdicts
state @ 15e0ce9: node codes + titles + aliases + every edge endpoint,
case-folded substring) and prints the matched terms so the ruling's
match_dispositions table is written against machine truth, not guessed.
The standing checker (c11_batch11_boundary_check.py) re-runs this match
as its B-gate.
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
    # S4-g esters vocabulary (4.38C-4.43C)
    "ester", "esters", "esterification", "r-coo-r", "-coo-", "coo",
    "ethyl ethanoate", "ethyl", "ethanoate", "butanoate", "pentyl",
    "-yl", "-oate", "sweet-smelling", "smell", "smells", "perfume",
    "perfumes", "flavouring", "flavourings", "food flavourings",
    "volatile", "volatility", "oily", "sulfuric acid", "concentrated",
    "acid catalyst", "ester link", "ester linkage", "hydrolysis",
    "sodium carbonate", "calcium chloride", "water bath", "bunsen",
    "flammable", "fizzing", "reverse reaction", "low boiling",
    "impurities", "purif", "distil", "distilled", "distillation",
    "condensation", "condenser",
    # S4-h polymers vocabulary (4.44-4.50C)
    "polymer", "polymers", "polymerisation", "addition polymer",
    "monomer", "monomers", "repeat unit", "repeat units", "polyethene",
    "polypropene", "poly(chloroethene)", "chloroethene", "pvc", "ptfe",
    "tetrafluoroethene", "polystyrene", "nylon", "resins", "plastic",
    "subscript", "brackets", "extension", "continuation bonds",
    "high pressures", "macromolecule", "long chain", "synthetic",
    "natural", "biological", "landfill", "landfills", "incineration",
    "burned", "burning", "non-biodegradable", "biodegrade",
    "biodegradable", "inert", "unreactive", "toxic", "hydrogen chloride",
    "carbon monoxide", "greenhouse", "climate change", "carbon dioxide",
    "decomposers", "micro-organism", "microorganism", "bacteria",
    "strong c-c", "c-c bonds", "terylene", "dicarboxylic", "diol",
    "diols", "polyester", "polyesters", "biopolyester", "hydrolysis",
    # organic-family + boundary vocabulary (the batch-9/10 owners)
    "functional group", "homologous series", "general formula",
    "structural formula", "displayed formula", "displayed formulae",
    "isomer", "hydrocarbon", "hydrocarbons", "alkene", "alkenes",
    "ethene", "propene", "alkane", "alkanes", "alcohol", "alcohols",
    "ethanol", "carboxylic", "cooh", "oh group", "-oh", "ethanoic acid",
    "oxidation", "combustion", "incomplete combustion", "iupac",
    "naming", "prefix", "addition reaction", "addition reactions",
    "substitution", "catalyst", "catalysts", "c=c", "double bond",
    "double bonds", "single bond", "single bonds", "covalent bond",
    "covalent bonds", "saturated", "unsaturated",
    # generic surfaces that appear in the S4-g/h notes
    "equation", "equations", "molecule", "molecules", "compound",
    "compounds", "oxygen", "water", "acid", "acids", "salt", "salts",
    "energy", "heat", "exothermic", "vinegar", "methanoic", "propanoic",
    "butanoic", "cracking", "fractional distillation",
    "simple distillation", "evaporate", "evaporation",
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
