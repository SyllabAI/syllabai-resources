#!/usr/bin/env python3
"""T-C11 session 57 — batch-6 boundary-ruling AUDIT PROBE (authoring aid).

Runs the exact match the ruling records (S2-d/e candidate terms against the
pre-batch-6 merged store = the live 129-node post-batch-5 state: node codes
+ titles + aliases + every edge endpoint, case-folded substring) and prints
the matched terms so the ruling's match_dispositions table is written
against the machine truth, not guessed. The standing checker
(c11_batch6_boundary_check.py) re-runs this match as its B-gate.
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
    "reactivity series", "order of reactivity", "reactivity trend",
    "displacement", "displacement reaction", "thermite",
    "oxidation", "reduction", "redox", "oxidising agent", "reducing agent",
    "oil rig", "rust", "rusting", "sacrificial protection", "galvanising",
    "galvanizing", "barrier method", "ore", "ores", "extraction",
    "electrolysis", "blast furnace", "cryolite", "bauxite", "haematite",
    "hematite", "alloy", "alloys", "steel", "brass", "stainless",
    "metal oxide", "oxides", "salt", "salts", "hydrogen", "dilute acid",
    "hydrochloric", "sulfuric", "spectator ion", "ionic equation",
    "half equation", "carbon", "gold", "silver", "copper", "iron", "zinc",
    "aluminium", "aluminum", "calcium", "magnesium", "sodium", "potassium",
    "lithium", "exothermic", "endothermic", "corrosion", "corrode",
    "malleable", "ductile", "conductor", "conductivity", "metal", "metals",
    "non-metal", "compound", "mixture", "ion", "ions", "ionic", "electron",
    "electrons", "word equation", "symbol equation", "state symbol",
    "molecule", "molecules", "covalent", "valency", "electrode", "cathode",
    "anode", "uncombined", "reactivity", "oxygen", "water", "acid",
    "acids", "equation", "precipitate", "solution", "solutions",
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
        # show where
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
