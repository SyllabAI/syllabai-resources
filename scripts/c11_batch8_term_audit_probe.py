#!/usr/bin/env python3
"""T-C11 session 61 — batch-8 boundary-ruling AUDIT PROBE (authoring aid).

Runs the exact match the ruling records (S2-h candidate terms against the
pre-batch-8 merged store = the live 157-node post-batch-7 state: node codes
+ titles + aliases + every edge endpoint, case-folded substring) and prints
the matched terms so the ruling's match_dispositions table is written
against the machine truth, not guessed. The standing checker
(c11_batch8_boundary_check.py) re-runs this match as its B-gate.
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
    # gas-test vocabulary (2.44)
    "gas test", "gas tests", "test for gases", "tests for gases", "hydrogen",
    "oxygen", "carbon dioxide", "ammonia", "chlorine", "squeaky pop", "pop",
    "burning splint", "lit splint", "lighted splint", "glowing splint",
    "splint", "relight", "limewater", "cloudy", "cloudy white", "milky",
    "bleach", "bleached", "bleaches", "damp red litmus", "damp blue litmus",
    "red litmus paper", "blue litmus paper", "litmus paper", "damp",
    "fume cupboard", "toxic", "choking smell", "test tube", "mouth of the test tube",
    # flame-test vocabulary (2.45/2.46)
    "flame test", "flame tests", "wire loop", "nichrome", "platinum",
    "dilute acid", "bunsen", "blue flame", "non-luminous", "contamination",
    "contaminating", "cation", "cations", "metal ion", "metal ions",
    "lithium", "sodium", "potassium", "calcium", "copper", "lilac",
    "orange-red", "blue-green", "crimson", "brick red",
    # cation-test vocabulary (2.47)
    "sodium hydroxide", "naoh", "precipitate", "precipitates", "pale green",
    "orange / brown", "orange/brown", "brown precipitate", "blue precipitate",
    "ammonium ion", "ammonium ions", "nh4", "warm", "ionic equation",
    "ammonia gas", "gas evolved", "gas released", "cloudiness", "faint",
    # anion-test vocabulary (2.48)
    "anion", "anions", "halide", "halides", "halide ion", "halide ions",
    "carbonate ion", "carbonate ions", "carbonate", "carbonates",
    "silver nitrate", "acidify", "acidified", "nitric acid",
    "silver halide", "chloride", "bromide", "iodide", "white precipitate",
    "cream precipitate", "yellow precipitate", "barium chloride",
    "sulfate ion", "sulfate ions", "sulfate", "sulfates", "sulphate",
    "barium sulfate", "barium nitrate", "dilute hydrochloric acid",
    "hydrochloric acid", "effervescence", "group 7", "state symbol",
    "silver chloride", "silver bromide", "silver iodide", "barium",
    # water-test vocabulary (2.49/2.50)
    "anhydrous", "anhydrous copper(ii) sulfate", "copper(ii) sulfate",
    "copper sulfate", "white to blue", "hydrated", "water of crystallisation",
    "boiling point", "pure", "purity", "impurities", "impure", "thermometer",
    "100", "physical test", "chemical test", "boiling tube", "condensation",
    "melting point",
    # cross-slice surfaces that appear in the h notes
    "equation", "equations", "aqueous", "solution", "displacement",
    "reactivity series", "filtration", "precipitation", "state symbols",
    "ionic", "ion", "ions", "positive ion", "negative ion", "negatively charged",
    "positively charged", "metal hydroxide", "insoluble", "soluble",
    "acid", "acids", "alkali", "litmus", "indicator", "indicator colours",
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
