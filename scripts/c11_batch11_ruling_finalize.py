#!/usr/bin/env python3
"""T-C11 session 66 — batch-11 boundary-ruling FINALIZER.

Renders scripts/c11_batch11_boundary_ruling.yaml from machine truth:
  * the full 171-term candidate list (imported from the audit probe)
  * the exact 72-term match set re-computed against the live pre-batch-11
    store (188 nodes / 459 edges @ 15e0ce9)
  * a PER-TERM disposition table (72 entries; the batch-8/9/10
    one-entry-per-match contract) with the disposition class + rationale
  * the curated non_mint_list (the plausible-collision set) asserted live
  * the TWELVE sanctioned boundary targets with owner verification
Run c11_batch11_term_audit_probe.py first if the store moved; this
finalizer refuses to write if the match count differs from 72.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402

GRAPH = GP.qual_dir()
OUT = HERE / "c11_batch11_boundary_ruling.yaml"

# disposition classes (the batch-8/9/10 vocabulary + the adjacency class)
BOUNDARY = "BOUNDARY_EDGE_SANCTIONED"
NEAR_MISS = "NO_COLLISION_DIFFERENT_DOMAIN"
REAGENT = "REAGENT_APPLIED_AS_GIVEN"
NOISE = "SUBSTRING_NOISE"
ADJACENT = "NO_EDGE_ADJACENT_OWNER"

# per-term disposition map (term -> (class, rationale)); every matched
# term MUST appear here — the finalizer fails closed otherwise.
DISPOSITIONS = {
    # --- the TWELVE sanctioned boundary targets -----------------------
    "alcohol": (BOUNDARY, "TARGET-1/TARGET-12 (the batch-10 CON-ALCOHOLS "
        "owner): the esterification reactant surface ('Alcohols and "
        "carboxylic acids react to make esters') and the diol monomer "
        "surface (an alcohol with an -OH group at either end) — two "
        "distinct surfaces, the batch-5 x2 precedent"),
    "alcohols": (BOUNDARY, "TARGET-1 (the batch-10 CON-ALCOHOLS owner): "
        "the esterification reactant vocabulary applied as given"),
    "ethanol": (BOUNDARY, "TARGET-1 (the batch-10 CON-ALCOHOLS owner): the "
        "ethanol reactant in the formation equation (the "
        "ETHANOL-MANUFACTURE/ETHANOL-OXIDATION hits are the batch-10 "
        "owners; no batch-11 surface routes there)"),
    "-oh": (BOUNDARY, "TARGET-1/TARGET-12 (the batch-10 CON-ALCOHOLS "
        "owner): the -OH functional-group vocabulary applied as given "
        "(the diol's -OH at either end rides the terylene surface)"),
    "carboxylic": (BOUNDARY, "TARGET-2/TARGET-11 (the batch-10 "
        "CON-CARBOXYLIC-ACIDS owner): the ethanoic-acid esterification "
        "reactant and the dicarboxylic-acid monomer surfaces — two "
        "distinct surfaces, the batch-5 x2 precedent"),
    "cooh": (BOUNDARY, "TARGET-2/TARGET-11 (the batch-10 "
        "CON-CARBOXYLIC-ACIDS owner): the -COOH reactant/monomer "
        "vocabulary applied as given"),
    "ethanoic acid": (BOUNDARY, "TARGET-2 (the batch-10 "
        "CON-CARBOXYLIC-ACIDS owner): the formation-equation reactant "
        "surface applied as given (the session-64 future-note 1 routing)"),
    "ethanoate": (BOUNDARY, "TARGET-2 (the batch-10 CON-CARBOXYLIC-ACIDS "
        "owner): the -oate name part is the carboxylate naming the "
        "batch-10 acids owner establishes (the CARBOXYLIC-ACID-REACTIONS "
        "-anoate hit rides the same surface — no separate edge, "
        "BOUNDARY-TARGETS-ONCE)"),
    "coo": (BOUNDARY, "TARGET-2 + the in-slice ester-link row (the "
        "batch-10 CON-CARBOXYLIC-ACIDS owner hit): the -COO- ester-link "
        "vocabulary rides the esterification-reactant edge and the "
        "CONDENSATION -> ESTERS link row"),
    "general formula": (BOUNDARY, "TARGET-3 (the batch-9 "
        "CON-ORGANIC-FORMULAE owner): the 4.40C/4.41C formulae demands run "
        "the batch-9 representation toolkit on the new family"),
    "structural formula": (BOUNDARY, "TARGET-3 (the batch-9 "
        "CON-ORGANIC-FORMULAE owner): the structural-formulae demand "
        "applied as given"),
    "displayed formula": (BOUNDARY, "TARGET-3 (the batch-9 "
        "CON-ORGANIC-FORMULAE owner): the displayed-formulae demand "
        "applied as given"),
    "displayed formulae": (BOUNDARY, "TARGET-3 (the batch-9 "
        "CON-ORGANIC-FORMULAE owner): the displayed-formulae demand "
        "applied as given"),
    "iupac": (BOUNDARY, "TARGET-4 (the batch-9 CON-IUPAC-NAMING owner): the "
        "4.41C naming demand CONSTRUCTS ester names from reactant stems "
        "(pent-yl + butan-oate) — the stem vocabulary applied as given"),
    "naming": (BOUNDARY, "TARGET-4 (the batch-9 CON-IUPAC-NAMING owner): "
        "the ester naming surface (the MIS-PROPANOL-POSITION hit rides "
        "the batch-10 record's own remediation note)"),
    "ethyl": (BOUNDARY, "TARGET-4 (the batch-9 CON-IUPAC-NAMING owner): the "
        "ethyl- stem in ethyl ethanoate is the batch-9 stem vocabulary "
        "applied (the INDICATORS hit is methyl-orange substring noise)"),
    "distil": (BOUNDARY, "TARGET-5 (the batch-1 CON-SIMPLE-DISTILLATION "
        "owner): the practical's distil-off-early collection step applied "
        "as given"),
    "distillation": (BOUNDARY, "TARGET-5 (the batch-1 "
        "CON-SIMPLE-DISTILLATION owner): the collection step IS the "
        "technique applied"),
    "simple distillation": (BOUNDARY, "TARGET-5 (the batch-1 "
        "CON-SIMPLE-DISTILLATION owner): the PR-12 edge's exact owner"),
    "acid": (BOUNDARY, "TARGET-2/TARGET-6 (the batch-10 "
        "CON-CARBOXYLIC-ACIDS and batch-7 CON-ACID-REACTIONS owners): the "
        "esterification acids and the practical's acidic-impurities "
        "removal surfaces"),
    "acids": (BOUNDARY, "TARGET-2/TARGET-11 (the batch-10 owners): the "
        "esterification + dicarboxylic-acid surfaces applied as given"),
    "alkene": (BOUNDARY, "TARGET-7 (the batch-10 CON-ALKENES owner): the "
        "C=C monomer requirement ('only occurs in monomers that contain "
        "C=C bonds') — the session-64 future-note 2 routing"),
    "alkenes": (BOUNDARY, "TARGET-7 (the batch-10 CON-ALKENES owner): "
        "'Many polymers can be made by the addition of alkene monomers'"),
    "ethene": (BOUNDARY, "TARGET-7 (the batch-10 CON-ALKENES owner): the "
        "polyethene monomer surface applied as given"),
    "c=c": (BOUNDARY, "TARGET-7 (the batch-10 CON-ALKENES owner): the C=C "
        "opening chemistry the polymerisation rides"),
    "double bond": (BOUNDARY, "TARGET-7 (the batch-10 CON-ALKENES owner): "
        "the C=C-bond-opening surface (the MIS-KEROSENE-DOUBLE-BONDS hit "
        "is the batch-9 misconception — no batch-11 surface)"),
    "double bonds": (BOUNDARY, "TARGET-7 (the batch-10 CON-ALKENES owner): "
        "same C=C-opening surface"),
    "addition reaction": (BOUNDARY, "TARGET-8 (the batch-9 "
        "CON-ORGANIC-REACTION-CLASSES owner): addition polymerisation IS "
        "the 4.6 addition class (a distinct surface from batch-10's "
        "TARGET-5 bromination row — the batch-5 x2 precedent)"),
    "greenhouse": (BOUNDARY, "TARGET-9 (the batch-5 CON-CO2-GREENHOUSE "
        "owner): the incineration surface ('a greenhouse gas that "
        "contributes to climate change') applied as given"),
    "climate change": (BOUNDARY, "TARGET-9 (the batch-5 "
        "CON-CO2-GREENHOUSE owner): the climate-change link applied as "
        "given"),
    "carbon dioxide": (BOUNDARY, "TARGET-9 (the batch-5 "
        "CON-CO2-GREENHOUSE owner): the incineration CO2 surface (the "
        "GAS-TESTS/CO2-FROM-CARBONATES hits are adjacent owners — the "
        "practical's carbonate fizzing rides TARGET-6)"),
    "carbon monoxide": (BOUNDARY, "TARGET-10 (the batch-9 "
        "CON-CO-POISONING owner): the incomplete-combustion CO surface "
        "restates the owner's blood-oxygen surface as given (POLYMER-CO, "
        "not the held ethanol-CO B10-H-08)"),
    # --- adjacent owners, no edge (held or routed elsewhere) ----------
    "functional group": (ADJACENT, "the batch-9 CON-HOMOLOGOUS-SERIES "
        "owner's vocabulary applied IN-SLICE (the ester R-COO-R group and "
        "the monomers' two-functional-groups surface are taught by the "
        "batch's own nodes); no notes row names the ester/polymer "
        "families as series members, so no HOMOLOGOUS-SERIES edge "
        "(contrast the batch-10 TARGET-1 rows)"),
    "homologous series": (ADJACENT, "the batch-9 owner; no batch-11 notes "
        "row names the ester/polymer families as series members"),
    "isomer": (ADJACENT, "the batch-9 CON-ISOMERS owner; no isomerism "
        "surface in the batch-11 notes"),
    "hydrocarbon": (ADJACENT, "the batch-9 CON-HYDROCARBON owner; esters "
        "contain oxygen and the notes never classify the families as "
        "hydrocarbons"),
    "hydrocarbons": (ADJACENT, "the batch-9 CON-HYDROCARBON owner; same "
        "no-surface"),
    "alkane": (ADJACENT, "the batch-9 CON-ALKANES owner; no batch-11 "
        "surface runs the saturated-alkane contrast (the batch-10 "
        "TARGET-4 surface)"),
    "alkanes": (ADJACENT, "the batch-9 CON-ALKANES owner; same no-surface"),
    "oxidation": (ADJACENT, "no batch-11 oxidation surface (the "
        "esterification is not oxidation; the OX-RED-AGENTS/"
        "REDOX-ELECTRONS owners untouched)"),
    "combustion": (ADJACENT, "the incineration surface routes via "
        "TARGET-9/TARGET-10; the batch-5 CON-COMBUSTION-O2 owner (elements "
        "in oxygen) is a different domain"),
    "incomplete combustion": (ADJACENT, "routes via TARGET-10 (the "
        "CO-POISONING edge); CON-FUELS-COMBUSTION held as B11-H-09"),
    "substitution": (ADJACENT, "the batch-9 class owner's substitution "
        "surface; no batch-11 row"),
    "catalyst": (ADJACENT, "the batch-4 owner reached only as a NAMED "
        "CONDITION (the sulfuric-acid catalyst B11-H-01, the "
        "high-pressure/catalyst conditions B11-H-03) — held, the "
        "B10-H-01/B9-H-04 rule"),
    "catalysts": (ADJACENT, "same named-condition surface as 'catalyst'"),
    "covalent bond": (ADJACENT, "the batch-3 owner; the note's 'connected "
        "via covalent bonds' is vocabulary-as-given (held B11-H-05; the "
        "C=C manipulation routes via TARGET-7)"),
    "covalent bonds": (ADJACENT, "same vocabulary-as-given surface (held "
        "B11-H-05)"),
    "saturated": (ADJACENT, "the batch-9/10 saturated-hydrocarbon owners + "
        "the batch-2 CON-SATURATED-SOLUTION owner (a different domain); "
        "no batch-11 notes usage"),
    "unsaturated": (ADJACENT, "the batch-10 CON-ALKENES owner; no batch-11 "
        "notes usage"),
    "vinegar": (ADJACENT, "the batch-10 CON-CARBOXYLIC-ACIDS owner's "
        "surface; no batch-11 row"),
    "cracking": (ADJACENT, "the batch-9 owner; ethene appears as the "
        "polyethene monomer, not via cracking; no batch-11 surface"),
    "fractional distillation": (ADJACENT, "the batch-1 owner; the "
        "practical is a single-distillate collection with no column — the "
        "owner stays single-targeted (the batch-9 4.8 row + batch-10 "
        "TARGET-10)"),
    "evaporation": (ADJACENT, "the batch-2 CON-EVAPORATION-BOILING owner; "
        "the practical's 'first to evaporate' mention rides TARGET-5; no "
        "separate edge"),
    "salt": (ADJACENT, "the S1 salt-preparation owners are a different "
        "domain; the practical's carbonate step rides TARGET-6"),
    "salts": (ADJACENT, "same as 'salt'"),
    "oxygen": (ADJACENT, "the blood-oxygen surface rides TARGET-10; the "
        "store's oxygen owners are adjacent (no batch-11 mint)"),
    "water": (ADJACENT, "the condensation water-by-product surface is "
        "taught IN-SLICE by the batch's own node; the store's water "
        "owners are different domains"),
    "energy": (ADJACENT, "the heat-energy release mention routes via "
        "TARGET-9; the energy owners untouched"),
    "heat": (ADJACENT, "same as 'energy' — the incineration heat surface "
        "is not load-bearing on any energy owner"),
    "exothermic": (ADJACENT, "the batch-4 energy owners; no batch-11 "
        "usage"),
    "reverse reaction": (ADJACENT, "the batch-4 CON-REVERSIBLE owner; the "
        "practical's reverse-reaction sentence HELD as B11-H-10, the "
        "condensation hydrolysis surface HELD as B11-H-08"),
    "condensation": (ADJACENT, "the store's CON-STATE-CHANGES owner is the "
        "gas-to-liquid state change (a different domain); the batch-11 "
        "condensation-polymerisation surface is minted in-slice; the "
        "practical's 'by condensation' collection step rides TARGET-5"),
    "macromolecule": (ADJACENT, "the batch-3 CON-GIANT-COVALENT owner uses "
        "'macromolecule' for giant lattices — a different structure "
        "class; the polymer long-chain surface is taught in-slice"),
    "burning": (ADJACENT, "the combustion-family owners; the disposal "
        "incineration surface routes via TARGET-9/TARGET-10 (B11-H-09)"),
    # --- different-domain collisions ---------------------------------
    "inert": (NEAR_MISS, "the inert-electrode (ELECTROLYSIS) and noble-gas "
        "(NOBLE-GAS-INERTNESS) senses differ from the chemically-inert "
        "polymer sense — which is taught in-slice by the disposal node"),
    "subscript": (NEAR_MISS, "the MIS-EQ-SUBSCRIPT equation-balancing "
        "sense differs from the repeat-unit subscript n (taught in-slice)"),
    # --- substring noise ----------------------------------------------
    "equation": (NOISE, "the equation owners exist; the esterification "
        "equation is the batch's own teaching surface"),
    "equations": (NOISE, "same substring surface"),
    "molecule": (NOISE, "generic vocabulary; the molecule owner's surface "
        "is not load-bearing in the batch-11 notes"),
    "molecules": (NOISE, "generic vocabulary"),
    "compound": (NOISE, "generic vocabulary"),
    "compounds": (NOISE, "generic vocabulary"),
}

SANCTIONED_TARGETS = [
    {"id": "TARGET-1", "for_sps": ["4CH1-4.38C", "4CH1-4.39C", "4CH1-4.42C"],
     "owner": "batch 10", "target": "4CH1-CON-ALCOHOLS",
     "surface": "the esterification reactant surface ('Alcohols and "
                "carboxylic acids react to make esters'; the ethanol "
                "reactant in the formation equation; the -yl name part is "
                "the alcohol chain) — the batch-10 owner applied as given; "
                "the session-64 future-note 1 routing"},
    {"id": "TARGET-2", "for_sps": ["4CH1-4.38C", "4CH1-4.39C", "4CH1-4.40C",
                                   "4CH1-4.41C"],
     "owner": "batch 10", "target": "4CH1-CON-CARBOXYLIC-ACIDS",
     "surface": "the ethanoic-acid reactant surface (the formation "
                "equation's CH3COOH; the -oate name part is the acid "
                "chain) — the batch-10 owner applied as given"},
    {"id": "TARGET-3", "for_sps": ["4CH1-4.40C", "4CH1-4.41C"],
     "owner": "batch 9", "target": "4CH1-CON-ORGANIC-FORMULAE",
     "surface": "the structural/displayed-formulae demands of 4.40C/4.41C "
                "run the batch-9 representation toolkit on the new family; "
                "the toolkit is applied, never re-taught (the batch's ONE "
                "formulae-toolkit edge — the polymer candidates are held "
                "as B11-H-04/B11-H-07)"},
    {"id": "TARGET-4", "for_sps": ["4CH1-4.41C"],
     "owner": "batch 9", "target": "4CH1-CON-IUPAC-NAMING",
     "surface": "the 4.41C naming demand CONSTRUCTS ester names from the "
                "reactant names (pent-yl + butan-oate) — the batch-9 stem "
                "vocabulary applied as given; stems never re-taught"},
    {"id": "TARGET-5", "for_sps": ["4CH1-4.43C"],
     "owner": "batch 1", "target": "4CH1-CON-SIMPLE-DISTILLATION",
     "surface": "the 4.43C practical's distil-off-early collection step IS "
                "the batch-1 simple-distillation technique applied (single "
                "volatile product, condensation collection; no column — "
                "CON-FRACTIONAL-DISTILLATION stays un-sanctioned)"},
    {"id": "TARGET-6", "for_sps": ["4CH1-4.43C"],
     "owner": "batch 7", "target": "4CH1-CON-ACID-REACTIONS",
     "surface": "the 4.43C purification step (sodium carbonate until the "
                "mixture stops fizzing, no more carbon dioxide) runs the "
                "batch-7 acid+carbonate reaction set as given "
                "(CON-CO2-FROM-CARBONATES stays un-sanctioned: "
                "BOUNDARY-TARGETS-ONCE)"},
    {"id": "TARGET-7", "for_sps": ["4CH1-4.44", "4CH1-4.45", "4CH1-4.46"],
     "owner": "batch 10", "target": "4CH1-CON-ALKENES",
     "surface": "the C=C monomer requirement ('only occurs in monomers "
                "that contain C=C bonds'; 'Many polymers can be made by "
                "the addition of alkene monomers'; the ethene/propene "
                "examples) — the batch-10 owner applied as given; the "
                "session-64 future-note 2 routing"},
    {"id": "TARGET-8", "for_sps": ["4CH1-4.44"],
     "owner": "batch 9", "target": "4CH1-CON-ORGANIC-REACTION-CLASSES",
     "surface": "addition polymerisation IS the 4.6 addition class ('This "
                "process is called addition polymerisation'; the "
                "condensation note's no-atoms-lost contrast) — a distinct "
                "surface from batch-10's TARGET-5 bromination row (the "
                "batch-5 x2 precedent)"},
    {"id": "TARGET-9", "for_sps": ["4CH1-4.47"],
     "owner": "batch 5", "target": "4CH1-CON-CO2-GREENHOUSE",
     "surface": "the incineration surface ('carbon dioxide which is a "
                "greenhouse gas that contributes to climate change') "
                "applies the batch-5 owner as given"},
    {"id": "TARGET-10", "for_sps": ["4CH1-4.47"],
     "owner": "batch 9", "target": "4CH1-CON-CO-POISONING",
     "surface": "the incomplete-combustion CO surface ('a toxic gas that "
                "reduces the capacity of the blood to carry oxygen') "
                "restates the batch-9 owner's surface as given; POLYMER-CO, "
                "not the held ethanol-CO record B10-H-08 (which stays "
                "held — no batch-11 note teaches the ethanol-CO surface)"},
    {"id": "TARGET-11", "for_sps": ["4CH1-4.48C", "4CH1-4.49C"],
     "owner": "batch 10", "target": "4CH1-CON-CARBOXYLIC-ACIDS",
     "surface": "the dicarboxylic-acid monomer surface (a carboxylic with "
                "a -COOH group at either end) — the second edge into this "
                "owner, the batch-5 x2 precedent (distinct surface from "
                "TARGET-2's esterification-reactant row)"},
    {"id": "TARGET-12", "for_sps": ["4CH1-4.48C", "4CH1-4.49C"],
     "owner": "batch 10", "target": "4CH1-CON-ALCOHOLS",
     "surface": "the diol monomer surface (an alcohol with an -OH group at "
                "either end) — the second edge into this owner, the "
                "batch-5 x2 precedent (distinct surface from TARGET-1's "
                "esterification-reactant row)"},
]

NON_MINT_LIST = [
    "4CH1-CON-ACID-ALKALI-IONS", "4CH1-CON-ACID-REACTIONS",
    "4CH1-CON-ALCOHOLS",
    "4CH1-CON-ALKANE-HALOGEN-SUBSTITUTION", "4CH1-CON-ALKANES",
    "4CH1-CON-ALKENES", "4CH1-CON-BROMINE-WATER-TEST",
    "4CH1-CON-CALORIMETRY", "4CH1-CON-CARBOXYLIC-ACID-REACTIONS",
    "4CH1-CON-CARBOXYLIC-ACIDS", "4CH1-CON-CATALYST",
    "4CH1-CON-CO2-FROM-CARBONATES", "4CH1-CON-CO2-GREENHOUSE",
    "4CH1-CON-CO-POISONING", "4CH1-CON-COMBUSTION-O2",
    "4CH1-CON-COMPOUND", "4CH1-CON-COVALENT-BOND", "4CH1-CON-CRACKING",
    "4CH1-CON-CRUDE-OIL-FRACTIONS", "4CH1-CON-EQ-SYMBOL",
    "4CH1-CON-ETHANOL-MANUFACTURE", "4CH1-CON-ETHANOL-OXIDATION",
    "4CH1-CON-EVAPORATION-BOILING", "4CH1-CON-EXO-ENDO",
    "4CH1-CON-FRACTIONAL-DISTILLATION", "4CH1-CON-FUELS-COMBUSTION",
    "4CH1-CON-GAS-TESTS", "4CH1-CON-GIANT-COVALENT",
    "4CH1-CON-HOMOLOGOUS-SERIES", "4CH1-CON-HYDROCARBON",
    "4CH1-CON-INDICATORS", "4CH1-CON-IUPAC-NAMING", "4CH1-CON-ISOMERS",
    "4CH1-CON-MOLECULE", "4CH1-CON-NEUTRALISATION",
    "4CH1-CON-NOBLE-GAS-INERTNESS", "4CH1-CON-ORGANIC-FORMULAE",
    "4CH1-CON-ORGANIC-REACTION-CLASSES", "4CH1-CON-OX-RED-AGENTS",
    "4CH1-CON-REDOX-ELECTRONS", "4CH1-CON-REVERSIBLE",
    "4CH1-CON-SATURATED-SOLUTION", "4CH1-CON-SIMPLE-DISTILLATION",
    "4CH1-CON-SIMPLE-MOLECULAR", "4CH1-CON-STATE-CHANGES",
    "4CH1-MIS-CATALYST-PARTICLE-ENERGY",
    "4CH1-MIS-COVALENT-BONDS-BROKEN", "4CH1-MIS-EQ-SUBSCRIPT",
    "4CH1-MIS-KEROSENE-DOUBLE-BONDS", "4CH1-MIS-PROPANOL-POSITION",
]

FUTURE_NOTES = [
    "batch 11 COMPLETES S4 (and the §16 S1-S4 authoring program): 49 of the "
    "50 S4 SPs carry candidate-level coverage after this batch; the 4CH1-4.15 "
    "negative control is the only uncovered SP in the whole 182-SP "
    "specification (181/182 covered at candidate level)",
    "the polymer-formulae toolkit rows are HELD (B11-H-04/B11-H-07, "
    "BOUNDARY-TARGETS-ONCE) with the batch's ONE formulae-toolkit edge "
    "carried by ESTERS TARGET-3 — if the operator splits the esters node, "
    "the held records name the re-open path",
    "the ethanol-CO held record B10-H-08 STAYS HELD — batch 11's CO surface "
    "is polymer incineration (sanctioned TARGET-10 into the batch-9 "
    "CON-CO-POISONING owner), not the ethanol-CO surface its re-open path "
    "requires; no batch-11 note teaches ethanol-CO",
    "the pinned Alkenes MS Q2(c) polymer-drawing Reject row ('Any "
    "double-bonded product scores 0/2' — dual-pinned as Synthetic Polymers "
    "MS Q4(c)) minted the batch's ONE misconception (MIS-POLYMER-DOUBLE-"
    "BOND, B11-ID-04) exactly as the session-64 ruling pre-routed",
    "the PART_OF lane stays outside §18 (the 12 batch-11 derived rows "
    "SUGGESTED pending their own lane, the T-C19 pattern); the next S4 "
    "session after the verdict gate is the batch-11 verdict encode + §18 "
    "apply session, which closes the section program",
]

NON_GOALS = ["no ontology redesign", "no re-opening of settled batches",
             "no re-scoping of the section plan",
             "no promotion authority (SUGGESTED until the operator's §18 "
             "command)", "no direct writes to graph/*.yaml"]


def main() -> int:
    probe = HERE / "c11_batch11_term_audit_probe.py"
    sys.path.insert(0, str(HERE))
    # re-run the probe's match against the live store (machine truth)
    import importlib.util
    spec = importlib.util.spec_from_file_location("b11probe", probe)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    nodes = yaml.safe_load(
        (GRAPH / "concepts.yaml").read_text(encoding="utf-8"))["nodes"]
    edges = yaml.safe_load(
        (GRAPH / "concept_edges.yaml").read_text(encoding="utf-8"))["edges"]
    # reconstruct the PRE-batch-11 store: subtract the batch-11 record's
    # own nodes and any edge touching them (the standing checker's B-gate
    # method) so the finalizer reproduces the ruling's match set at any
    # post-authoring state
    b11 = yaml.safe_load(
        (HERE / "c11_batch11_decisions.yaml").read_text(encoding="utf-8"))
    b11_codes = {x["code"] for x in b11["nodes"]}
    nodes = [x for x in nodes if x["code"] not in b11_codes]
    edges = [e for e in edges
             if e["source"] not in b11_codes and e["target"] not in b11_codes]
    blob = []
    for x in nodes:
        blob.append(x["code"])
        blob.append(x["title"])
        blob.extend(x.get("aliases", []))
    store_blob = " || ".join(blob).lower()
    endpoints = " ".join(f"{e['source']} {e['target']}"
                         for e in edges).lower()
    matched = [t for t in mod.TERMS if t in store_blob or t in endpoints]
    print(f"live match count: {len(matched)} (expected 72)")
    if len(matched) != 72:
        print("FAIL-CLOSED: the match count differs from the authored "
              "ruling (72) — the store moved; re-characterize before "
              "rendering")
        return 1
    missing = [t for t in matched if t not in DISPOSITIONS]
    extra = [t for t in DISPOSITIONS if t not in matched]
    if missing or extra:
        print(f"FAIL-CLOSED: disposition table mismatch — "
              f"missing={missing} extra={extra}")
        return 1
    live_codes = {x["code"] for x in nodes}
    for t in SANCTIONED_TARGETS:
        if t["target"] not in live_codes:
            print(f"FAIL-CLOSED: sanctioned target {t['target']} is not a "
                  f"live node")
            return 1
    for c in NON_MINT_LIST:
        if c not in live_codes:
            print(f"FAIL-CLOSED: non-mint code {c} is not a live node")
            return 1
    # sanctioned targets must NOT be re-mintable: they sit in the
    # non_mint_list too (the batch-9 convention — non-mint = not minted
    # IN-batch; sanctioned targets are reached via edges only)
    dispositions = [{"term": t, "disposition": DISPOSITIONS[t][0],
                     "rationale": DISPOSITIONS[t][1]}
                    for t in matched]
    doc = {
        "meta": {
            "task": "T-C11",
            "stage": "s16-cross-slice-boundary-ruling",
            "session": 66,
            "recorded_date": "2026-09-25",
            "commissioned_by": "operator directive 'commission batch 11' "
                "(2026-09-25, session 66) under the session-46 §16 "
                "authorization; the S4 slice plan (batches 9-11) is "
                "recorded in the session-62 commissioning record",
            "scope": "conflict-prevention ruling for the "
                "S4-a/b/c/d/e/f(complete, settled) -> S4-g/h(batch 11: g "
                "Esters 4.38C-4.43C incl. the 4.43C practical + h "
                "Synthetic polymers 4.44-4.50C, 13 authorable SPs) "
                "boundary only; supersedes nothing; extends the "
                "session-55/57/59/61/62/64 ruling pattern to the S4-g/h "
                "slice",
            "applies_to_batch": 11,
            "scope_sp_note": "the audit covers the 13 authorable SPs; "
                "4CH1-4.15 (S4-b) is the standing negative control and "
                "stays CARVED OUT of all batch scopes (no node/edge may "
                "attach or cite it); the 4CH1-4.43C practical-typed SP is "
                "carried by the scoped T-C10 practical 4CH1-PR-12 (the "
                "batch-3 1.60C/PR-04 precedent)",
        },
        "conflict_audit": {
            "result": "NO UNHANDLED CONFLICTS — every one of the 72 matches "
                "is dispositioned below; the TWELVE sanctioned boundary "
                "targets are existing owners reached via boundary edges "
                "only; the non-mint discipline holds",
            "method": "S4-g/h candidate term vocabulary (171 terms: ester "
                "vocabulary, polymer vocabulary, the named reagents and "
                "practical apparatus, the organic-family boundary "
                "vocabulary, generic chemistry vocabulary and equation "
                "scaffolding) matched against the whole merged "
                "pre-batch-11 store at 15e0ce9 (node codes + titles + "
                "aliases + every edge endpoint, case-folded substring; the "
                "probe is persisted as "
                "scripts/c11_batch11_term_audit_probe.py). 72 terms "
                "match; EVERY match is dispositioned below — sanctioned "
                "boundary edge, no-edge-adjacent-owner (held or routed "
                "elsewhere), near-miss different-demand (no edge, mint "
                "in-batch), reagent-applied-as-given (no edge), or "
                "sub-string noise (no owner surface).",
            "s4_def_candidate_terms": mod.TERMS,
        },
        "match_dispositions": dispositions,
        "mint_ruling": {
            "rule": "the batch-11 extraction mints only the in-slice "
                "family nodes the notes teach (4 CONCEPT + 1 "
                "MISCONCEPTION); every existing owner the audit touched "
                "stays untouched except through the TWELVE sanctioned "
                "boundary edges; the negative control 4CH1-4.15 gains NO "
                "attachment and NO citation",
            "mints": "4 CONCEPT (ESTERS 4.38C-4.42C one-family; "
                "ADDITION-POLYMERS 4.44-4.46 one-family; POLYMER-DISPOSAL "
                "4.47; CONDENSATION-POLYMERS 4.48C-4.50C one-family with "
                "the biopolyesters fold) + 1 MISCONCEPTION "
                "(MIS-POLYMER-DOUBLE-BOND from the pinned Alkenes MS "
                "Q2(c)/Synthetic Polymers MS Q4(c) Reject column 'Any "
                "double-bonded product scores 0/2' — the "
                "MIS-PROPANOL-POSITION/B10-M-01 and "
                "MIS-KEROSENE-DOUBLE-BONDS/B9-M-01 precedent); the 4.43C "
                "practical rides the scoped 4CH1-PR-12 (the batch-3 "
                "1.60C/PR-04 precedent); the identity questions "
                "B11-ID-01..04 ride the one-family rulings and the mint",
        },
        "boundary_edge_ruling": {
            "rule": "the FN-B1-2/FN-B2-2 cross-batch discipline at the "
                "S4-g/h boundary: boundary EDGES are sanctioned ONLY into "
                "the exact-owner nodes below, ONLY for the surfaces named, "
                "and each target takes AT MOST the edges its surface rows "
                "carry (BOUNDARY-TARGETS-ONCE: no second edge into the "
                "same owner family where a held record routes the "
                "remainder; the two double-targeted owners carry the "
                "batch-5 x2 precedent)",
            "sanctioned_targets": SANCTIONED_TARGETS,
            "max_boundary_edges": 12,
            "non_mint_list": NON_MINT_LIST,
        },
        "future_boundary_notes": FUTURE_NOTES,
        "non_goals": NON_GOALS,
    }
    OUT.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True,
                                  width=100), encoding="utf-8")
    print(f"wrote {OUT}")
    print(f"sanctioned targets: {len(SANCTIONED_TARGETS)}  "
          f"non-mint: {len(NON_MINT_LIST)}  dispositions: "
          f"{len(dispositions)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
