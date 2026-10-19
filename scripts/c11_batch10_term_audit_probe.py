#!/usr/bin/env python3
"""T-C11 session 64 — batch-10 boundary-ruling AUDIT PROBE (authoring aid).

Runs the exact match the ruling records (S4-d/e/f candidate terms against
the pre-batch-10 merged store = the live 180-node post-batch-9-verdicts
state @ 9dc0e47: node codes + titles + aliases + every edge endpoint,
case-folded substring) and prints the matched terms so the ruling's
match_dispositions table is written against machine truth, not guessed.
The standing checker (c11_batch10_boundary_check.py) re-runs this match
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
    # S4-d alkenes vocabulary (4.23-4.28)
    "alkene", "alkenes", "c=c", "double bond", "double bonds",
    "unsaturated", "dibromoalkane", "dibromoalkanes", "bromine water",
    "bromine", "addition", "addition reaction", "addition reactions",
    "decolouris", "decoloris", "orange", "ethene", "propene", "butene",
    "but-1-ene", "but-2-ene", "distinguish", "saturated", "cnh2n",
    # S4-e alcohols vocabulary (4.29C-4.33C)
    "alcohol", "alcohols", "hydroxyl", "oh group", "-oh", "ethanol",
    "methanol", "propanol", "butanol", "fermentation", "glucose",
    "anaerobic", "yeast", "optimum temperature", "oxidation", "oxidised",
    "oxidise", "manufacture", "hydration", "steam", "phosphoric",
    "catalyst", "methylated", "biofuel", "carbon neutral", "zymase",
    "acidified potassium", "manganate", "dichromate", "crystals",
    "ethanoic acid", "alcoholic drinks", "solvent",
    # S4-f carboxylic acids vocabulary (4.34C-4.37C)
    "carboxylic", "cooh", "methanoic", "propanoic", "butanoic",
    "vinegar", "weak acid", "weak acids", "partially ionised",
    "partially ionized", "metal carbonate", "metal carbonates",
    "carbonate", "hydrogen carbonate", "salt", "salts", "effervescence",
    # manufacture/separation + process vocabulary (the S4-e notes)
    "fractional distillation", "distillation", "fractionating column",
    "by-product", "feedstock", "dibromoethane", "condenser", "reflux",
    "boiling point", "carbon monoxide", "poisonous", "toxic",
    "complete combustion", "incomplete combustion", "spirit burner",
    # organic-family boundary vocabulary (the batch-9 owners)
    "homologous series", "functional group", "general formula",
    "structural formula", "displayed formula", "isomer", "isomers",
    "hydrocarbon", "hydrocarbons", "combustion", "burns", "burning",
    "complete combustion", "incomplete combustion", "cracking",
    "iupac", "substitution", "organic reaction", "reaction classes",
    "alkane", "alkanes",
    # generic surfaces that appear in the S4-d/e/f notes
    "equation", "equations", "molecule", "molecules", "compound",
    "compounds", "covalent bond", "covalent bonds", "ion", "ions",
    "exothermic", "energy", "acid", "acids", "alkali", "alkalis",
    "enzyme", "enzymes", "bacteria", "respiration", "air", "oxygen",
    "water", "carbon dioxide", "ester", "esters", "polymer", "polymers",
    "monomer", "condensation", "naming", "prefix", "an-", "propyl",
    "ethyl", "methyl",
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
