#!/usr/bin/env python3
"""T-C11 session 64 — batch-10 boundary-ruling FINALIZER.

Renders scripts/c11_batch10_boundary_ruling.yaml from machine truth:
  * the full 146-term candidate list (imported from the audit probe)
  * the exact 73-term match set re-computed against the live pre-batch-10
    store (180 nodes / 425 edges @ 9dc0e47)
  * a PER-TERM disposition table (71 entries; the batch-8/9 one-entry-per-
    match contract) with the disposition class + rationale
  * the curated non_mint_list (the plausible-collision set) asserted live
  * the ELEVEN sanctioned boundary targets with owner verification
Run c11_batch10_term_audit_probe.py first if the store moved; this
finalizer refuses to write if the match count differs from 73.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402

GRAPH = GP.qual_dir()
OUT = HERE / "c11_batch10_boundary_ruling.yaml"

# disposition classes (the batch-8/9 vocabulary + the adjacency class)
BOUNDARY = "BOUNDARY_EDGE_SANCTIONED"
NEAR_MISS = "NO_COLLISION_DIFFERENT_DOMAIN"
REAGENT = "REAGENT_APPLIED_AS_GIVEN"
NOISE = "SUBSTRING_NOISE"
ADJACENT = "NO_EDGE_ADJACENT_OWNER"

# per-term disposition map (term -> (class, rationale)); every matched
# term MUST appear here — the finalizer fails closed otherwise.
DISPOSITIONS = {
    # --- the ELEVEN sanctioned boundary targets -----------------------
    "homologous series": (BOUNDARY, "TARGET-1 (the batch-9 CON-HOMOLOGOUS-"
        "SERIES owner): the notes name the alkene ('the first four members "
        "of the alkene homologous series') and alcohol ('the first four "
        "alcohols in the homologous series') series-membership surfaces as "
        "given; the owner is never re-defined by the S4-d/e/f notes"),
    "functional group": (BOUNDARY, "TARGET-1: the batch-9 owner teaches "
        "the functional-group term inside the homologous-series surface "
        "('Three important terms...'); the alkenes (-C=C-), alcohols (-OH) "
        "and carboxylic acids (-COOH) notes APPLY the term to name their "
        "own groups; no re-definition"),
    "general formula": (BOUNDARY, "TARGET-2 (the batch-9 CON-ORGANIC-"
        "FORMULAE owner): 4.24's CnH2n and 4.34C's CnH2n+1COOH apply the "
        "owner's general-formula representation surface; the owner taught "
        "the formula types, never the alkenes/acids values themselves"),
    "structural formula": (BOUNDARY, "TARGET-2: 4.26/4.30C/4.35C drawing "
        "demands run the owner's structural/displayed toolkit on the new "
        "families; the toolkit is applied, not re-taught"),
    "displayed formula": (BOUNDARY, "TARGET-2: as above — the 4.26/4.30C "
        "displayed-formulae tables apply the owner's surface"),
    "hydrocarbon": (BOUNDARY, "TARGET-3 (the batch-9 CON-HYDROCARBON "
        "owner): 4.25's classification ('alkenes are unsaturated "
        "hydrocarbons') and Q5(c)'s 'not a hydrocarbon because it contains "
        "oxygen' apply the owner's H/C-only definition as given"),
    "hydrocarbons": (BOUNDARY, "SAME AS 'hydrocarbon' (TARGET-3)"),
    "alkane": (BOUNDARY, "TARGET-4 (the batch-9 CON-ALKANES owner): the "
        "4.28 distinguishing test is DEFINED against the alkane surface "
        "('All alkanes are saturated and alkenes are unsaturated'; "
        "'alkanes do not have double carbon bonds so the bromine remains "
        "in solution'); the owner is the contrast class, never re-taught"),
    "alkanes": (BOUNDARY, "SAME AS 'alkane' (TARGET-4)"),
    "saturated": (BOUNDARY, "TARGET-4 via the saturated-contrast surface "
        "('All alkanes are saturated' — the CON-ALKANES hit); the CON-"
        "SATURATED-SOLUTION co-hit is a different domain (dissolution "
        "science — NO_COLLISION_DIFFERENT_DOMAIN); the MIS-KEROSENE "
        "co-hit rides its title"),
    "addition": (BOUNDARY, "TARGET-5 (the batch-9 CON-ORGANIC-REACTION-"
        "CLASSES owner): 4.27's 'alkenes undergo addition reactions' runs "
        "the owner's addition class (taught at 4.6) on the new family; the "
        "class owner is applied, not re-taught"),
    "addition reaction": (BOUNDARY, "SAME AS 'addition' (TARGET-5)"),
    "iupac": (BOUNDARY, "TARGET-6 (the batch-9 CON-IUPAC-NAMING owner): "
        "the alcohols note's naming sentence ('the same system is used as "
        "for alkanes and alkenes, with the final e replaced with ol') and "
        "the carboxylic-acids note's 'alkan + oic acid' pattern apply the "
        "owner's naming system; stems/prefixes are never re-taught"),
    "naming": (BOUNDARY, "TARGET-6 via the same naming-system surface (the "
        "MIS-GLOWING-SPLINT-HYDROGEN co-hit is SUBSTRING_NOISE — an "
        "unrelated reject-column sentence)"),
    "combustion": (BOUNDARY, "TARGET-7 (the batch-5 CON-COMBUSTION-O2 "
        "owner): 4.31C's combustion route ('Alcohols undergo combustion to "
        "form carbon dioxide and water'; the MS 'needs more oxygen' "
        "surface) presupposes the owner's combustion-oxygen chemistry; "
        "never re-taught by the S4-e note"),
    "burning": (BOUNDARY, "TARGET-7 via 'Combustion (burning in air)' (the "
        "MIS-GLOWING-SPLINT-HYDROGEN co-hit is SUBSTRING_NOISE)"),
    "oxidation": (BOUNDARY, "TARGET-8 (the batch-6 CON-OX-RED-AGENTS "
        "owner): 4.31C's third route ('Treatment with an oxidising agent'; "
        "'The oxidising agent is represented by [O]') applies the owner's "
        "oxidising-agent surface; the REDOX-ELECTRONS co-hit stays "
        "un-sanctioned (one boundary edge into the redox family — "
        "BOUNDARY-TARGETS-ONCE)"),
    "oxidised": (BOUNDARY, "SAME AS 'oxidation' (TARGET-8)"),
    "oxidise": (BOUNDARY, "SAME AS 'oxidation' (TARGET-8)"),
    "cracking": (BOUNDARY, "TARGET-9 (the batch-9 CON-CRACKING owner): "
        "'Ethene is a by-product of the cracking of hydrocarbons' — the "
        "hydration feedstock sentence applies the owner as given (the "
        "session-62 ruling future-note 1 routed this surface to batch 10)"),
    "fractional distillation": (BOUNDARY, "TARGET-10 (the batch-1 "
        "CON-FRACTIONAL-DISTILLATION owner): BOTH ethanol routes end "
        "'separated by fractional distillation' — the note applies the "
        "batch-1 technique as given (the CRUDE-OIL-FRACTIONS co-hit is the "
        "batch-9 node that itself boundary-points at the owner; the "
        "SIMPLE-DISTILLATION co-hit is a different technique — "
        "NO_COLLISION)"),
    "distillation": (BOUNDARY, "TARGET-10 via the same separation surface "
        "(the SIMPLE-DISTILLATION co-hit is a different technique — "
        "NO_COLLISION_DIFFERENT_DOMAIN)"),
    "metal carbonate": (BOUNDARY, "TARGET-11 (the batch-7 CON-ACID-"
        "REACTIONS owner): 4.36C's 'carbonates to form a salt, water and "
        "carbon dioxide gas' runs the owner's metal-carbonate reaction set "
        "on the carboxylic-acid family (the CO2-FROM-CARBONATES co-hit is "
        "the batch-2 CO2-test owner — a second boundary edge there would "
        "double-target: BOUNDARY-TARGETS-ONCE, held)"),
    "metal carbonates": (BOUNDARY, "SAME AS 'metal carbonate' (TARGET-11)"),
    "carbonate": (BOUNDARY, "TARGET-11 via the same reaction surface (the "
        "ANION-TESTS and CO2-FROM-CARBONATES co-hits are distinct owners — "
        "no additional boundary edges, BOUNDARY-TARGETS-ONCE)"),
    "acid": (BOUNDARY, "TARGET-11 via 'The carboxylic acids behave like "
        "other acids' — the owner's reaction set is the applied surface "
        "(the other acid-family co-hits are generic vocabulary — NOISE; "
        "the acid-rain owner is unrelated)"),
    "acids": (BOUNDARY, "SAME AS 'acid' (TARGET-11)"),
    # --- real adjacencies the ruling deliberately does NOT sanction ----
    "isomer": (ADJACENT, "the batch-9 CON-ISOMERS owner exists and 4.26's "
        "'up to four carbon atoms' touches the but-1-ene/but-2-ene "
        "position-isomer surface, but the notes never teach isomerism for "
        "alkenes (the table names four alkenes without the isomer "
        "framing) — HELD (B10-H-05, AVAILABLE-BUT-SURFACE-MINIMAL); no "
        "boundary edge"),
    "isomers": (ADJACENT, "SAME AS 'isomer' (B10-H-05)"),
    "double bond": (ADJACENT, "the batch-9 MIS-KEROSENE-DOUBLE-BONDS "
        "misconception owns the kerosene/double-bonds surface; the S4-d "
        "notes teach the REAL C=C chemistry that the misconception denies "
        "— no edge to a misconception record (its REMEDIATED_BY already "
        "targets the batch-9 CON-CRUDE-OIL-FRACTIONS owner); the owner "
        "stays untouched"),
    "double bonds": (ADJACENT, "SAME AS 'double bond'"),
    "unsaturated": (ADJACENT, "the MIS-KEROSENE-DOUBLE-BONDS co-hit rides "
        "its title; the real unsaturated surface is minted IN-BATCH "
        "(CON-ALKENES, 4.25); no owner collision"),
    "hydration": (ADJACENT, "the batch-5 CON-REVERSIBLE-EXAMPLES owner "
        "teaches the hydration-of-ethene equilibrium framing; the 4.32C "
        "note teaches hydration as a manufacture ROUTE with an "
        "unreacted-ethene separation surface, not as an equilibrium — "
        "HELD (B10-H-06, EXPLANATION-DEEPER-THAN-DEMAND); no boundary edge"),
    "catalyst": (ADJACENT, "the CON-CATALYST owner exists (the audit "
        "co-hits EQ-POSITION/RATE-FACTORS/MIS-CATALYST-PARTICLE-ENERGY are "
        "the rates family); the phosphoric-acid catalyst in 4.32C is a "
        "CONDITION applied as given — HELD (B10-H-04, MECHANISM-APPLIED-AS-"
        "GIVEN, the B9-H-04 rule); no boundary edge"),
    "oxidation family note": (NOISE, "never matched — documentation guard "
        "row (kept out of the table by the finalizer)"),
    "complete combustion": (ADJACENT, "the batch-9 CON-FUELS-COMBUSTION "
        "owner owns the complete/incomplete products surface; the 4.31C "
        "combustion route ('carbon dioxide and water') is routed via "
        "TARGET-7 (CON-COMBUSTION-O2) — ONE edge into the combustion "
        "family family-tree (BOUNDARY-TARGETS-ONCE); the fuels-family "
        "link is HELD (B10-H-07, SAME-FAMILY-ADJACENCY)"),
    "incomplete combustion": (ADJACENT, "SAME AS 'complete combustion' "
        "(B10-H-07)"),
    "carbon monoxide": (ADJACENT, "the batch-9 CON-CO-POISONING owner owns "
        "the CO surface; the pinned MS Q4(d)ii documents the "
        "ethanol-incomplete-combustion CO question, but the NOTE teaches "
        "only clean burning ('carbon dioxide and water') — an "
        "assessment-documented surface the notes do not carry: HELD "
        "(B10-H-08, ENRICHMENT-NOT-LOAD-BEARING); no boundary edge"),
    "poisonous": (ADJACENT, "SAME AS 'carbon monoxide' (B10-H-08)"),
    "substitution": (ADJACENT, "the batch-9 CON-ALKANE-HALOGEN-SUBSTITUTION "
        "owner owns the alkane substitution surface; 4.27's bromine "
        "chemistry is ADDITION (in-slice), and the pinned MS 'bromine in "
        "presence of uv' near-miss rule documents the contrast — no edge "
        "(the test note carries the distinction itself)"),
    "organic reaction": (BOUNDARY, "TARGET-5 via the same class-owner "
        "surface ('Alkenes undergo addition reactions' runs the batch-9 "
        "CON-ORGANIC-REACTION-CLASSES owner's addition class)"),
    "fractionating column": (BOUNDARY, "TARGET-10 via the fractional-"
        "distillation technique vocabulary (the CON-FRACTIONAL-"
        "DISTILLATION owner's own apparatus term applied as given; the "
        "CRUDE-OIL-FRACTIONS co-hit is the batch-9 node that itself "
        "boundary-points at the owner)"),
    # --- reagents applied as given -------------------------------------
    "bromine": (REAGENT, "the batch-2 G7-DISPLACEMENT owner teaches halogen "
        "displacement chemistry; 4.27/4.28 use bromine as the reagent "
        "whose ADDITION chemistry is in-slice (the same disposition the "
        "session-62 ruling made for 4.22's substitution chemistry); no "
        "boundary edge (the reagent-applied class would double-count a "
        "reagent mention)"),
    "oxygen": (REAGENT, "generic reagent vocabulary (the COMBUSTION-O2 "
        "owner surface routes via TARGET-7; the GAS-TESTS/AIR-COMPOSITION "
        "co-hits are unrelated)"),
    "water": (REAGENT, "generic solvent/product vocabulary across the "
        "notes; the water-family owners (CUSO4 test, purity) are "
        "unrelated to S4-d/e/f demands"),
    "salt": (NOISE, "generic product vocabulary; the carboxylate -anoate "
        "salt naming is minted IN-BATCH (CON-CARBOXYLIC-ACID-REACTIONS, "
        "4.36C); the salt-preparation owners are a different demand"),
    "salts": (NOISE, "SAME AS 'salt'"),
    "carbon dioxide": (REAGENT, "product/reagent vocabulary (the "
        "CO2-FROM-CARBONATES co-hit routes via TARGET-11's reaction set; "
        "the GREENHOUSE/GAS-TESTS co-hits are unrelated)"),
    "air": (REAGENT, "generic vocabulary (the AIR-COMPOSITION owner is "
        "unrelated; 'absence of air' in fermentation is a condition "
        "taught in-batch)"),
    # --- substring noise ------------------------------------------------
    "cnh2n": (NOISE, "substring of the ALKANES owner's CnH2n+2 general "
        "formula alias; the alkenes CnH2n surface is minted IN-BATCH "
        "(4.24)"),
    "orange": (NOISE, "the FLAME-TEST flame-colour and INDICATORS "
        "methyl-orange hits are different domains; 4.28's 'orange' is the "
        "bromine-water colour minted IN-BATCH"),
    "distinguish": (NOISE, "the INDICATORS hit is generic vocabulary; "
        "4.28's distinguishing test is minted IN-BATCH"),
    "ethyl": (NOISE, "substring noise (the INDICATORS hit is an indicator "
        "name; the ethyl group is minted IN-BATCH via 4.30C/4.35C naming)"),
    "methyl": (NOISE, "substring noise (methyl orange the indicator; the "
        "methyl group is minted IN-BATCH)"),
    "crystals": (NOISE, "the MIS-CRYSTALLISATION-DRYNESS hit is unrelated "
        "(crystallisation practical vocabulary; no S4-d/e/f SP teaches "
        "crystals)"),
    "solvent": (NEAR_MISS, "the SOLUBILITY/SOLUTION owners teach dissolution "
        "science; 4.30C's 'alcohols... dissolve in water to form neutral "
        "solutions' is a property mention, not a solubility-science demand "
        "— coincidental vocabulary, no boundary edge"),
    "boiling point": (NOISE, "the five co-hit owners teach bp as a "
        "separation/property principle; the ethanol/ethene/water bp values "
        "in the 4.32C note ride TARGET-10's fractional-distillation "
        "surface — no separate edge"),
    "condensation": (NOISE, "the STATE-CHANGES owner is the physical "
        "process; the S4-d/e/f notes' condenser mentions ride the "
        "reflux/separation context — no collision with polymerisation "
        "condensation (batch 11's surface, not yet minted)"),
    "equation": (NOISE, "generic equation vocabulary (the eq-family owners "
        "teach symbol-equation construction; the S4-d/e/f equations are "
        "in-batch content)"),
    "equations": (NOISE, "SAME AS 'equation'"),
    "molecule": (NOISE, "generic vocabulary (the MOLECULE/SIMPLE-MOLECULAR "
        "owners teach the particle model; S4-d/e/f uses the word "
        "generically)"),
    "molecules": (NOISE, "SAME AS 'molecule'"),
    "compound": (NOISE, "generic vocabulary (the COMPOUND owner teaches the "
        "definition; S4-d/e/f uses the word generically)"),
    "compounds": (NOISE, "SAME AS 'compound'"),
    "covalent bond": (NOISE, "the COVALENT-BOND owner teaches bonding "
        "theory; the S4-d C=C bond-breaking surface is taught in-batch as "
        "organic reactivity, not bonding theory"),
    "covalent bonds": (NOISE, "SAME AS 'covalent bond'"),
    "ion": (NOISE, "generic ion vocabulary (the ionic-family owners are "
        "unrelated to S4-d/e/f demands; 4.36C's salt formation is taught "
        "in-batch via the TARGET-11 reaction set)"),
    "ions": (NOISE, "SAME AS 'ion'"),
    "exothermic": (NEAR_MISS, "the EXO-ENDO owner teaches the energy "
        "classification; the S4-d/e/f notes never classify their reactions "
        "as exo/endothermic (the ethanol-as-fuel energy mention is "
        "use-mention — HELD context, B10-H-09); no boundary edge"),
    "energy": (NOISE, "generic energy vocabulary (the energetics-family "
        "owners are unrelated to the S4-d/e/f demands)"),
    "alkali": (NOISE, "the alkali-family owners are unrelated (the MS "
        "'acid or an alkali' KMnO4 accept-line is an alternative-test "
        "footnote, not taught chemistry)"),
    "alkalis": (NOISE, "SAME AS 'alkali'"),
}

# the ELEVEN sanctioned boundary targets
SANCTIONED_TARGETS = [
    {"id": "TARGET-1", "for_sps": ["4CH1-4.23", "4CH1-4.26", "4CH1-4.29C",
                                   "4CH1-4.30C"],
     "owner": "batch 9", "target": "4CH1-CON-HOMOLOGOUS-SERIES",
     "surface": "the S4-d/e/f notes name their families as homologous-"
        "series members and apply the functional-group term to the -C=C-, "
        "-OH and -COOH groups — the batch-9 owner's own vocabulary applied "
        "as given; never re-defined"},
    {"id": "TARGET-2", "for_sps": ["4CH1-4.24", "4CH1-4.26", "4CH1-4.30C",
                                   "4CH1-4.35C"],
     "owner": "batch 9", "target": "4CH1-CON-ORGANIC-FORMULAE",
     "surface": "the general/structural/displayed formulae demands of "
        "4.24/4.26/4.30C/4.35C run the batch-9 representation toolkit on "
        "the new families; the toolkit is applied, never re-taught"},
    {"id": "TARGET-3", "for_sps": ["4CH1-4.25"],
     "owner": "batch 9", "target": "4CH1-CON-HYDROCARBON",
     "surface": "4.25 classifies alkenes as unsaturated HYDROCARBONS — the "
        "batch-9 H/C-only definition owner applied as given"},
    {"id": "TARGET-4", "for_sps": ["4CH1-4.28"],
     "owner": "batch 9", "target": "4CH1-CON-ALKANES",
     "surface": "the 4.28 bromine-water test is defined against the alkane "
        "contrast ('All alkanes are saturated'; 'alkanes do not have "
        "double carbon bonds'); the batch-9 owner is the contrast class"},
    {"id": "TARGET-5", "for_sps": ["4CH1-4.27"],
     "owner": "batch 9", "target": "4CH1-CON-ORGANIC-REACTION-CLASSES",
     "surface": "4.27's 'alkenes undergo addition reactions' runs the "
        "batch-9 class owner (which taught substitution/addition/combustion "
        "at 4.6) on the new family"},
    {"id": "TARGET-6", "for_sps": ["4CH1-4.30C"],
     "owner": "batch 9", "target": "4CH1-CON-IUPAC-NAMING",
     "surface": "the alcohols note applies the naming system ('the same "
        "system is used as for alkanes and alkenes, with the final e "
        "replaced with ol' — the position-convention Examiner Tip rides "
        "here); stems and prefixes never re-taught"},
    {"id": "TARGET-7", "for_sps": ["4CH1-4.31C"],
     "owner": "batch 5", "target": "4CH1-CON-COMBUSTION-O2",
     "surface": "4.31C's combustion route ('Alcohols undergo combustion to "
        "form carbon dioxide and water'; the MS 'needs more oxygen' "
        "surface) presupposes the batch-5 combustion-oxygen owner"},
    {"id": "TARGET-8", "for_sps": ["4CH1-4.31C"],
     "owner": "batch 6", "target": "4CH1-CON-OX-RED-AGENTS",
     "surface": "4.31C's third oxidation route ('Treatment with an "
        "oxidising agent'; '[O]') applies the batch-6 oxidising/reducing-"
        "agent owner as given; REDOX-ELECTRONS stays un-sanctioned "
        "(BOUNDARY-TARGETS-ONCE)"},
    {"id": "TARGET-9", "for_sps": ["4CH1-4.32C"],
     "owner": "batch 9", "target": "4CH1-CON-CRACKING",
     "surface": "'Ethene is a by-product of the cracking of hydrocarbons' — "
        "the hydration feedstock sentence applies the batch-9 cracking "
        "owner (the session-62 future-note 1 routed this surface to "
        "batch 10)"},
    {"id": "TARGET-10", "for_sps": ["4CH1-4.32C", "4CH1-4.33C"],
     "owner": "batch 1", "target": "4CH1-CON-FRACTIONAL-DISTILLATION",
     "surface": "BOTH ethanol routes end 'separated by fractional "
        "distillation' — the batch-1 technique owner applied as given "
        "(the same owner batch 9 sanctioned for the 4.8 industrial row; "
        "BOUNDARY-TARGETS-ONCE respected — one edge per route surface "
        "into the owner)"},
    {"id": "TARGET-11", "for_sps": ["4CH1-4.36C"],
     "owner": "batch 7", "target": "4CH1-CON-ACID-REACTIONS",
     "surface": "'The carboxylic acids behave like other acids' — 4.36C's "
        "metal and metal-carbonate reactions run the batch-7 owner's "
        "reaction set on the new family (the CO2-FROM-CARBONATES owner "
        "stays un-sanctioned: BOUNDARY-TARGETS-ONCE)"},
]

NON_MINT_LIST = [
    "4CH1-CON-ACID-ALKALI-IONS", "4CH1-CON-ACID-RAIN-CAUSES",
    "4CH1-CON-ACID-REACTIONS",
    "4CH1-CON-ANION-TESTS", "4CH1-CON-AIR-COMPOSITION",
    "4CH1-CON-ALKANE-HALOGEN-SUBSTITUTION", "4CH1-CON-ALKANES",
    "4CH1-CON-CALORIMETRY", "4CH1-CON-CATALYST",
    "4CH1-CON-CO2-FROM-CARBONATES", "4CH1-CON-CO2-GREENHOUSE",
    "4CH1-CON-CO-POISONING", "4CH1-CON-COMBUSTION-O2",
    "4CH1-CON-COMPOUND", "4CH1-CON-COVALENT-BOND", "4CH1-CON-CRACKING",
    "4CH1-CON-CRUDE-OIL", "4CH1-CON-CRUDE-OIL-FRACTIONS",
    "4CH1-CON-EQ-POSITION", "4CH1-CON-EQ-SYMBOL", "4CH1-CON-EQ-WORD",
    "4CH1-CON-FRACTIONAL-DISTILLATION", "4CH1-CON-FUELS-COMBUSTION",
    "4CH1-CON-G7-DISPLACEMENT", "4CH1-CON-GAS-TESTS",
    "4CH1-CON-HOMOLOGOUS-SERIES", "4CH1-CON-HYDROCARBON",
    "4CH1-CON-INDICATORS", "4CH1-CON-IUPAC-NAMING", "4CH1-CON-ISOMERS",
    "4CH1-CON-FLAME-TEST", "4CH1-CON-MOLECULE",
    "4CH1-CON-OX-RED-AGENTS", "4CH1-CON-PH-SCALE",
    "4CH1-CON-ORGANIC-REACTION-CLASSES", "4CH1-CON-ORGANIC-FORMULAE",
    "4CH1-CON-RATE-FACTORS", "4CH1-CON-REDOX-ELECTRONS",
    "4CH1-CON-REVERSIBLE-EXAMPLES", "4CH1-CON-SATURATED-SOLUTION",
    "4CH1-CON-SIMPLE-DISTILLATION", "4CH1-CON-SOLUBILITY",
    "4CH1-CON-SOLUTION", "4CH1-CON-STATE-CHANGES",
    "4CH1-MIS-CATALYST-PARTICLE-ENERGY",
    "4CH1-MIS-CRYSTALLISATION-DRYNESS",
    "4CH1-MIS-GLOWING-SPLINT-HYDROGEN",
    "4CH1-MIS-KEROSENE-DOUBLE-BONDS",
]

FUTURE_NOTES = [
    "4.38C-4.43C (S4-g esters) ride the functional-group vocabulary the "
    "batch-10 -OH/-COOH nodes establish and the ethanoic-acid surface "
    "batch 10's oxidation/acid nodes teach — batch 11 owns the ester "
    "surfaces (the session-62 future-note 2 routing continues)",
    "4.44-4.50C (S4-h polymers) ride 4.27's addition chemistry (the pinned "
    "Alkenes MS Q2(c) polymer-drawing Reject row 'Any double-bonded "
    "product scores 0/2' is BATCH-11's mint evidence — the polymer "
    "families are out of batch-10 scope) and the Crude Oil MS "
    "condensation-polymerisation/disposal surfaces",
    "the 4.15 negative control sits in S4-b and is untouched by batch 10 "
    "(no batch-10 SP is 4.15-adjacent; the graph_check D12 control "
    "continues to verify zero attachments)",
    "the batch-9 CON-ALKANES owner's UV-substitution surface connects to "
    "the pinned Alkenes MS Q2(a)(ii) near-miss rule ('bromine in presence "
    "of uv... observation mark can be awarded') — the substitution-vs-"
    "addition contrast is carried by the batch-9 owner and batch-10's "
    "TARGET-5/TARGET-4 boundary edges; no batch-10 node re-teaches it",
    "the ethanol incomplete-combustion/CO surface (pinned Alkenes MS "
    "Q4(d)ii into the batch-9 CON-CO-POISONING owner) is HELD as "
    "B10-H-08 — if a later batch's notes teach the ethanol-CO surface "
    "explicitly, the boundary edge can be sanctioned then (the held "
    "record cites this note)",
]

NON_GOALS = ["no ontology redesign", "no re-opening of settled batches",
             "no re-scoping of the section plan",
             "no promotion authority (SUGGESTED until the operator's §18 "
             "command)", "no direct writes to graph/*.yaml"]


def main() -> int:
    probe = HERE / "c11_batch10_term_audit_probe.py"
    sys.path.insert(0, str(HERE))
    # re-run the probe's match against the live store (machine truth)
    import importlib.util
    spec = importlib.util.spec_from_file_location("b10probe", probe)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    nodes = yaml.safe_load(
        (GRAPH / "concepts.yaml").read_text(encoding="utf-8"))["nodes"]
    edges = yaml.safe_load(
        (GRAPH / "concept_edges.yaml").read_text(encoding="utf-8"))["edges"]
    # reconstruct the PRE-batch-10 store: subtract the batch-10 record's
    # own nodes and any edge touching them (the standing checker's B-gate
    # method) so the finalizer reproduces the ruling's match set at any
    # post-authoring state
    b10 = yaml.safe_load(
        (HERE / "c11_batch10_decisions.yaml").read_text(encoding="utf-8"))
    b10_codes = {x["code"] for x in b10["nodes"]}
    nodes = [x for x in nodes if x["code"] not in b10_codes]
    edges = [e for e in edges
             if e["source"] not in b10_codes and e["target"] not in b10_codes]
    blob = []
    for x in nodes:
        blob.append(x["code"])
        blob.append(x["title"])
        blob.extend(x.get("aliases", []))
    store_blob = " || ".join(blob).lower()
    endpoints = " ".join(f"{e['source']} {e['target']}"
                         for e in edges).lower()
    matched = [t for t in mod.TERMS if t in store_blob or t in endpoints]
    print(f"live match count: {len(matched)} (expected 73)")
    if len(matched) != 73:
        print("FAIL-CLOSED: the match count differs from the authored "
              "ruling (73) — the store moved; re-characterize before "
              "rendering")
        return 1
    missing = [t for t in matched if t not in DISPOSITIONS
               or t == "oxidation family note"]
    missing = [t for t in matched if t not in DISPOSITIONS]
    extra = [t for t in DISPOSITIONS if t not in matched
             and t != "oxidation family note"]
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
            "session": 64,
            "recorded_date": "2026-09-25",
            "commissioned_by": "operator directive 'commission batch 10' "
                "(2026-09-25, session 64) under the session-46 §16 "
                "authorization; the S4 slice plan (batches 9-11) is "
                "recorded in the session-62 commissioning record",
            "scope": "conflict-prevention ruling for the "
                "S4-a/b/c(complete, settled) -> S4-d/e/f(batch 10: d "
                "Alkenes 4.23-4.28 + e Alcohols 4.29C-4.33C + f Carboxylic "
                "acids 4.34C-4.37C, 15 authorable SPs) boundary only; "
                "supersedes nothing; extends the session-55/57/59/61/62 "
                "ruling pattern to the S4-d/e/f slice",
            "applies_to_batch": 10,
            "scope_sp_note": "the audit covers the 15 authorable SPs; "
                "4CH1-4.15 (S4-b) is the standing negative control and "
                "stays CARVED OUT of all batch scopes (no node/edge may "
                "attach or cite it); no batch-10 SP is practical-typed "
                "(the 4CH1-4.43C practical belongs to batch 11's slice)",
        },
        "conflict_audit": {
            "result": "NO UNHANDLED CONFLICTS — every one of the 73 matches "
                "is dispositioned below; the ELEVEN sanctioned boundary "
                "targets are existing owners reached via boundary edges "
                "only; the non-mint discipline holds",
            "method": "S4-d/e/f candidate term vocabulary (146 terms: "
                "alkene vocabulary, alcohol vocabulary, carboxylic-acid "
                "vocabulary, manufacture/separation process vocabulary, "
                "the named reagents and conditions, generic chemistry "
                "vocabulary and equation scaffolding) matched against the "
                "whole merged pre-batch-10 store at 9dc0e47 (node codes + "
                "titles + aliases + every edge endpoint, case-folded "
                "substring; the probe is persisted as "
                "scripts/c11_batch10_term_audit_probe.py). 73 terms "
                "match; EVERY match is dispositioned below — sanctioned "
                "boundary edge, no-edge-adjacent-owner (held or routed "
                "elsewhere), near-miss distinct-demand (no edge, mint "
                "in-batch), reagent-applied-as-given (no edge), or "
                "sub-string noise (no owner surface).",
            "s4_def_candidate_terms": mod.TERMS,
        },
        "match_dispositions": dispositions,
        "mint_ruling": {
            "rule": "the batch-10 extraction mints only the in-slice "
                "family nodes the notes teach (7 CONCEPT + 1 "
                "MISCONCEPTION); every existing owner the audit touched "
                "stays untouched except through the ELEVEN sanctioned "
                "boundary edges; the negative control 4CH1-4.15 gains NO "
                "attachment and NO citation",
            "mints": "7 CONCEPT (ALKENES 4.23-4.26 one-family; "
                "BROMINE-WATER-TEST 4.27-4.28; ALCOHOLS 4.29C-4.30C; "
                "ETHANOL-OXIDATION 4.31C; ETHANOL-MANUFACTURE 4.32C-4.33C; "
                "CARBOXYLIC-ACIDS 4.34C+4.35C+4.37C; CARBOXYLIC-ACID-"
                "REACTIONS 4.36C) + 1 MISCONCEPTION (MIS-PROPANOL-POSITION "
                "from the pinned Alkenes MS Q4(b)(ii) Reject column "
                "'Reject propan-1-ol / 1-propanol' — the "
                "MIS-HALIDE-TEST-HCL/B8-M-02 and MIS-KEROSENE-DOUBLE-BONDS/"
                "B9-M-01 precedent); the identity questions B10-ID-01..05 "
                "ride the one-family rulings",
        },
        "boundary_edge_ruling": {
            "rule": "the FN-B1-2/FN-B2-2 cross-batch discipline at the "
                "S4-d/e/f boundary: boundary EDGES are sanctioned ONLY "
                "into the exact-owner nodes below, ONLY for the surfaces "
                "named, and each target takes AT MOST the edges its "
                "surface rows carry (BOUNDARY-TARGETS-ONCE: no second "
                "edge into the same owner family where a held record "
                "routes the remainder)",
            "sanctioned_targets": SANCTIONED_TARGETS,
            "max_boundary_edges": 11,
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
