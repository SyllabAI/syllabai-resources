#!/usr/bin/env python3
"""T-C11 session 59 — batch-7 boundary-ruling AUDIT PROBE (authoring aid).

Runs the exact match the ruling records (S2-f/g candidate terms against the
pre-batch-7 merged store = the live 142-node post-batch-6 state: node codes
+ titles + aliases + every edge endpoint, case-folded substring) and prints
the matched terms so the ruling's match_dispositions table is written
against the machine truth, not guessed. The standing checker
(c11_batch7_boundary_check.py) re-runs this match as its B-gate.
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
    # indicators / pH vocabulary (S2-f)
    "indicator", "indicators", "litmus", "phenolphthalein", "methyl orange",
    "universal indicator", "ph scale", "ph value", "ph", "acidic", "alkaline",
    "acidity", "strongly acidic", "weakly acidic", "neutral", "colour change",
    "colour chart", "wide range indicator",
    # acid/alkali theory vocabulary (S2-f)
    "acid", "acids", "alkali", "alkalis", "hydrogen ion", "hydrogen ions",
    "hydroxide ion", "hydroxide ions", "ion", "ions", "aqueous solution",
    "neutralisation", "neutralization", "neutralise", "neutralize",
    "proton", "protons", "proton donor", "proton acceptor", "proton transfer",
    # titration vocabulary (S2-f)
    "titration", "titrations", "burette", "pipette", "endpoint", "end-point",
    "concordant", "meniscus", "volumetric analysis", "white tile",
    # solubility / salt vocabulary (S2-g)
    "solubility", "soluble", "insoluble", "precipitate", "salt", "salts",
    "chloride", "chlorides", "sulfate", "sulfates", "sulphate", "nitrate",
    "nitrates", "carbonate", "carbonates", "hydroxide", "hydroxides",
    "sodium hydroxide", "potassium hydroxide", "ammonia", "ammonium",
    "ammonium hydroxide", "base", "bases", "metal oxide", "metal oxides",
    "metal hydroxide", "metal hydroxides", "copper(II) oxide", "copper(II) sulfate",
    "lead(II) sulfate", "lead(II) nitrate", "potassium sulfate", "barium chloride",
    "barium sulfate", "silver nitrate", "silver chloride", "hydrated",
    "water of crystallisation", "water of crystallization", "anhydrous",
    # salt-prep technique vocabulary (S2-g)
    "crystallisation", "crystallization", "crystals", "filtration", "filter",
    "filtrate", "residue", "evaporation", "evaporate", "saturated solution",
    "saturated", "solution", "solutions", "solvent", "solute", "dilute",
    "concentrated", "concentration", "effervescence", "excess", "washing",
    "double decomposition", "salt preparation", "preparation of salts",
    # cross-slice surfaces that appear in the f/g notes
    "reactivity series", "displacement", "reactivity", "hydrogen", "carbon dioxide",
    "state symbols", "ionic", "ionic compound", "ionic compounds", "covalent",
    "equation", "equations", "word equation", "symbol equation", "mole", "moles",
    "volume", "temperature", "heat", "heating", "exothermic", "endothermic",
    "limewater", "calcium hydroxide", "white precipitate", "distilled water",
    "water bath", "pure", "pure, dry", "acid-alkali", "acid + alkali",
    "metal + acid", "metal carbonate", "titration calculation",
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
