#!/usr/bin/env python3
"""T-C11 session 57 — pre-authoring quote probe for the batch-6 decision
record (scripts/c11_batch6_decisions.yaml): every planned NOTE / MARK_SCHEME
/ SPEC quote must byte-verify under the T-C10 norm() in its cited file, and
every SPEC quote must sit inside its SP's official wording (the
c11_batch5_quote_probe.py pattern, batch-6-scoped).

Run BEFORE authoring so the decision record is written against verified
quotes only (fail-closed; the generator's G03 and the preverify re-check
these independently).
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent

D1 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "d. Reactivity Series/Metals Reacting with Water & Acids  Edexcel "
      "IGCSE Chemistry Revision Notes 2017.md")
D2 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "d. Reactivity Series/Metal displacement - IGCSE Chemistry Revision "
      "Notes.md")
D3 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "d. Reactivity Series/Metals reacting with acids - IGCSE Chemistry "
      "Revision Notes.md")
D4 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "d. Reactivity Series/Rusting of iron - IGCSE Chemistry Revision "
      "Notes.md")
D5 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "d. Reactivity Series/Oxidation and reduction - IGCSE Chemistry "
      "Revision Notes.md")
D6 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "d. Reactivity Series/The reactivity series - IGCSE Chemistry Revision "
      "Notes.md")
E1 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "e. Extraction & Uses of Metals/Where does metal come from - IGCSE "
      "Chemistry Revision Notes.md")
E2 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "e. Extraction & Uses of Metals/Extraction of metals from ores - "
      "IGCSE Chemistry.md")
E3 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "e. Extraction & Uses of Metals/Metals and their uses - IGCSE "
      "Chemistry Revision Notes.md")
E4 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "e. Extraction & Uses of Metals/Alloys - IGCSE Chemistry Revision "
      "Notes.md")
N8 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "c. Gases in the Atmosphere/Thermal decomposition - IGCSE Chemistry "
      "Revision Notes.md")
N6 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "c. Gases in the Atmosphere/Oxygen percentage in air - IGCSE Chemistry "
      "Revision Notes.md")
M1 = "scripts/c11_evidence/REACTIVITY_MS_P2.txt"
SP = "graph/igcse-chemistry/specification_points.yaml"

# (file, quote, kind, sp-or-None)  — SPEC quotes checked against the SP wording
PROBES = [
    # --- 2.15 arranging via water/acid reactions (D1, D3) -------------------
    (D1, "The chemistry of the metals is studied by analysing their reactions with water and acids", "NOTE", "4CH1-2.15"),
    (D1, "Based on these reactions a reactivity series of metals can be produced", "NOTE", "4CH1-2.15"),
    (D1, "The series can be used to place a group of metals in order of reactivity based on the observations of their reactions with water and acids", "NOTE", "4CH1-2.15"),
    (D1, "Only metals above hydrogen in the reactivity series will react with dilute acids", "NOTE", "4CH1-2.15"),
    (D1, "The more reactive the metal then the more vigorous the reaction will be", "NOTE", "4CH1-2.15"),
    (D1, "When acids react with metals they form a salt and hydrogen gas", "NOTE", "4CH1-2.15"),
    (D1, "metal + acid ⟶ salt + hydrogen", "NOTE", "4CH1-2.15"),
    (D3, "To investigate the reactions between dilute hydrochloric and sulfuric acids with the metals magnesium, iron and zinc", "NOTE", "4CH1-2.21"),
    (D3, "The metals can be ranked in reactivity order Mg > Zn > Fe", "NOTE", "4CH1-2.21"),
    (D3, "The three metals react in the same way with both acids", "NOTE", "4CH1-2.21"),
    (D3, "Hydrogen and a metal salt solution is produced", "NOTE", "4CH1-2.21"),
    (D3, "Repeat the experiment with dilute sulfuric acid", "NOTE", "4CH1-2.21"),
    # --- 2.16 displacement (D2) ----------------------------------------------
    (D2, "The reactivity of metals decreases going down the reactivity series.", "NOTE", "4CH1-2.16"),
    (D2, "This means that a more reactive metal will displace a less reactive metal from its compounds", "NOTE", "4CH1-2.16"),
    (D2, "Reacting a metal with a metal oxide (by heating)", "NOTE", "4CH1-2.16"),
    (D2, "Reacting a metal with an aqueous solution of a metal compound", "NOTE", "4CH1-2.16"),
    (D2, "For example it is possible to reduce copper(II) oxide by heating it with zinc.", "NOTE", "4CH1-2.16"),
    (D2, "The reactivity between two metals can be compared using displacement reactions in salt solutions of one of the metals", "NOTE", "4CH1-2.16"),
    (D2, "This is easily seen as the more reactive metal slowly disappears from the solution, displacing the less reactive metal", "NOTE", "4CH1-2.16"),
    (D2, "For example, magnesium is a reactive metal and can displace copper from copper(II)sulfate solution:", "NOTE", "4CH1-2.16"),
    # --- 2.17 the order (D6, D1) ---------------------------------------------
    (D6, "Carbon is an important element and has its own place on the reactivity series", "NOTE", "4CH1-2.17"),
    (D6, "Potassium", "NOTE", "4CH1-2.17"),
    (D6, "Gold", "NOTE", "4CH1-2.17"),
    (D1, "Most reactive", "NOTE", "4CH1-2.17"),
    # --- 2.18 rusting conditions (D4) ----------------------------------------
    (D4, "Oxygen and water must be present for rust to occur", "NOTE", "4CH1-2.18"),
    (D4, "The results show that both air and water must be present for rusting to occur", "NOTE", "4CH1-2.18"),
    (D4, "Boiled water removes any dissolved oxygen and calcium chloride is a drying agent", "NOTE", "4CH1-2.18"),
    (D4, "Rust is a soft solid substance that flakes off the surface of iron easily, exposing fresh iron below which then undergoes rusting", "NOTE", "4CH1-2.18"),
    # --- 2.19 rust prevention (D4) -------------------------------------------
    (D4, "Rust can be prevented by coating iron with barriers that prevent the iron from coming into contact with water and oxygen", "NOTE", "4CH1-2.19"),
    (D4, "Common barrier methods include: paint, oil, grease, and electroplating", "NOTE", "4CH1-2.19"),
    (D4, "Iron can be prevented from rusting using the reactivity series", "NOTE", "4CH1-2.19"),
    (D4, "A more reactive metal can be attached to a less reactive metal", "NOTE", "4CH1-2.19"),
    (D4, "The more reactive metal will oxidise and therefore corrode first, protecting the less reactive metal from corrosion", "NOTE", "4CH1-2.19"),
    (D4, "Zinc is more reactive than iron therefore will lose its electrons more easily than iron and is oxidised more easily", "NOTE", "4CH1-2.19"),
    (D4, "Galvanising is a process where the iron to be protected is coated with a layer of zinc", "NOTE", "4CH1-2.19"),
    (D4, "If the coating is damaged or scratched, the iron is still protected from rusting by sacrificial protection", "NOTE", "4CH1-2.19"),
    # --- 2.20 oxidation/reduction terms (D5) ---------------------------------
    (D5, "Oxidation is any reaction in which a substance gains oxygen", "NOTE", "4CH1-2.20"),
    (D5, "Reduction is a reaction in which a substance loses oxygen", "NOTE", "4CH1-2.20"),
    (D5, "The reactions of metals with oxygen, such as in iron rusting can be classified as oxidation", "NOTE", "4CH1-2.20"),
    (D5, "Oxidation cannot occur without reduction happening simultaneously, hence these are called redox reactions", "NOTE", "4CH1-2.20"),
    (D5, "The copper(II)oxide supplies the oxygen, so it is the oxidising agent", "NOTE", "4CH1-2.20"),
    (D5, "The zinc is the reducing agent because it removes the oxygen", "NOTE", "4CH1-2.20"),
    (D5, "Oxidation is the loss of electrons", "NOTE", "4CH1-2.20"),
    (D5, "Reduction is the gain of electrons", "NOTE", "4CH1-2.20"),
    # --- 2.22C ores (E1) ------------------------------------------------------
    (E1, "Useful metals are often chemically combined with other substances forming ores", "NOTE", "4CH1-2.22C"),
    (E1, "A metal ore is a rock that contains enough of the metal to make it worthwhile extracting", "NOTE", "4CH1-2.22C"),
    (E1, "Unreactive metals do not have to be extracted chemically as they are often found as the uncombined element", "NOTE", "4CH1-2.22C"),
    (E1, "Examples include gold and platinum which can both be mined directly from the Earth’s crust", "NOTE", "4CH1-2.22C"),
    (E1, "In many cases the ore is an oxide of the metal, therefore the extraction of these metals is a reduction process since oxygen is being removed", "NOTE", "4CH1-2.22C"),
    # --- 2.23C/2.24C extraction (E2) -----------------------------------------
    (E2, "The position of the metal on the reactivity series determines the method of extraction", "NOTE", "4CH1-2.23C"),
    (E2, "Higher placed metals (above carbon) have to be extracted using electrolysis as they are too reactive and cannot be reduced by carbon", "NOTE", "4CH1-2.23C"),
    (E2, "Lower placed metals can be extracted by heating with carbon which reduces them", "NOTE", "4CH1-2.23C"),
    (E2, "Instead, aluminium is extracted by electrolysis", "NOTE", "4CH1-2.23C"),
    (E2, "Aluminium is higher in the reactivity series than carbon, so it cannot be extracted by reduction using carbon", "NOTE", "4CH1-2.23C"),
    (E2, "Carbon monoxide reduces the iron(III) oxide in the iron ore to form iron", "NOTE", "4CH1-2.23C"),
    (E2, "Make sure you can explain why aluminium is extracted by electrolysis while iron is extracted by reduction as it is a question that often comes up.", "NOTE", "4CH1-2.23C"),
    (E2, "Iron is extracted in a large container called a blast furnace from its ore, hematite", "NOTE", "4CH1-2.24C"),
    (E2, "A lot of electricity is required for this process of extraction, this is a major expense", "NOTE", "4CH1-2.24C"),
    # --- 2.25C uses (E3) ------------------------------------------------------
    (E3, "The uses of aluminium, copper and steel are summarised in these tables", "NOTE", "4CH1-2.25C"),
    (E3, "High strength-to-weight ratio (low density)", "NOTE", "4CH1-2.25C"),
    (E3, "Very good conductor of electricity and ductile", "NOTE", "4CH1-2.25C"),
    (E3, "Unreactive (does not react with water), non-toxic and malleable", "NOTE", "4CH1-2.25C"),
    (E3, "Very good conductor of heat, unreactive, malleable", "NOTE", "4CH1-2.25C"),
    # --- 2.26C/2.27C alloys (E4) ---------------------------------------------
    (E4, "An alloy is a mixture of two or more metals or metal with a non-metal such as carbon", "NOTE", "4CH1-2.26C"),
    (E4, "Steel is made from iron and carbon", "NOTE", "4CH1-2.26C"),
    (E4, "Brass is a common example of an alloy which contains 70% copper and 30% zinc", "NOTE", "4CH1-2.26C"),
    (E4, "Alloys are harder than pure metals because:", "NOTE", "4CH1-2.27C"),
    (E4, "Alloys contain atoms of different sizes", "NOTE", "4CH1-2.27C"),
    (E4, "This distorts the regular arrangements of atoms", "NOTE", "4CH1-2.27C"),
    (E4, "So it is more difficult for the layers of atoms to slide over each other", "NOTE", "4CH1-2.27C"),
    # --- boundary-edge anchors (batch-5 notes, resolve via their own SPs) -----
    (N8, "Carbonates of metals from the lower half of the reactivity series tend to decompose on heating to produce the metal oxide and carbon dioxide gas:", "NOTE", "4CH1-2.12"),
    (N6, "To determine the percentage of oxygen in air using the oxidation of iron", "NOTE", "4CH1-2.10"),
    (N6, "After 3-4 days note the new position of the water level", "NOTE", "4CH1-2.10"),
    # --- MARK_SCHEME probes (REACTIVITY_MS_P2) --------------------------------
    (M1, "(it/iron is) less reactive (than aluminium)", "MARK_SCHEME", None),
    (M1, "Accept aluminium is more reactive (than iron)", "MARK_SCHEME", None),
    (M1, "Reject references to ions and oxides", "MARK_SCHEME", None),
    (M1, "aluminium replaces iron (from a compound)", "MARK_SCHEME", None),
    (M1, "gain/addition of oxygen", "MARK_SCHEME", None),
    (M1, "loss of (three) electron(s)", "MARK_SCHEME", None),
    (M1, "increase in oxidation number/state", "MARK_SCHEME", None),
    (M1, "burning magnesium / magnesium reacting with air/oxygen", "MARK_SCHEME", None),
    (M1, "Ignore references to water or acid", "MARK_SCHEME", None),
    (M1, "solution of barium chloride", "MARK_SCHEME", None),
    (M1, "white precipitate", "MARK_SCHEME", None),
    # --- SPEC probes (official wording spans) ---------------------------------
    (SP, "understand how metals can be arranged in a reactivity series based on their reactions with:", "SPEC", "4CH1-2.15"),
    (SP, "understand how metals can be arranged in a reactivity series based on their displacement reactions between:", "SPEC", "4CH1-2.16"),
    (SP, "know the order of reactivity of these metals: potassium, sodium, lithium, calcium, magnesium, aluminium, zinc, iron, copper, silver, gold", "SPEC", "4CH1-2.17"),
    (SP, "know the conditions under which iron rusts", "SPEC", "4CH1-2.18"),
    (SP, "understand how the rusting of iron may be prevented by:", "SPEC", "4CH1-2.19"),
    (SP, "understand the terms:", "SPEC", "4CH1-2.20"),
    (SP, "know that most metals are extracted from ores found in the Earth’s crust and that unreactive metals are often found as the uncombined element", "SPEC", "4CH1-2.22C"),
    (SP, "explain how the method of extraction of a metal is related to its position in the reactivity series, illustrated by carbon extraction for iron and electrolysis for aluminium", "SPEC", "4CH1-2.23C"),
    (SP, "be able to comment on a metal extraction process, given appropriate information", "SPEC", "4CH1-2.24C"),
    (SP, "explain the uses of aluminium, copper, iron and steel in terms of their properties", "SPEC", "4CH1-2.25C"),
    (SP, "know that an alloy is a mixture of a metal and one or more elements, usually other metals or carbon", "SPEC", "4CH1-2.26C"),
    (SP, "explain why alloys are harder than pure metals", "SPEC", "4CH1-2.27C"),
    (SP, "describe the formation of carbon dioxide from the thermal decomposition of metal carbonates, including copper(II) carbonate", "SPEC", "4CH1-2.12"),
    (SP, "understand how to determine the percentage by volume of oxygen in air using experiments involving the reactions of metals (e.g. iron) and non-metals (e.g. phosphorus) with air", "SPEC", "4CH1-2.10"),
    (SP, "practical: investigate reactions between dilute hydrochloric and sulfuric acids and metals (e.g. magnesium, zinc and iron)", "SPEC", "4CH1-2.21"),
]

sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402

_TRANS = {ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = s.translate(_TRANS)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def main() -> int:
    import yaml
    spec = yaml.safe_load(
        GP.store("specification_points").read_text(encoding="utf-8"))
    wording = {p["code"]: p["official_wording"]
               for p in spec["specification_points"]}

    fails = 0
    for i, (rel, quote, kind, sp) in enumerate(PROBES, 1):
        file_rel = GP.resolve_rel(rel)
        p = REPO / file_rel
        if not p.exists():
            print(f"FAIL {i:03d} file missing: {file_rel}")
            fails += 1
            continue
        body = norm(p.read_text(encoding="utf-8"))
        if norm(quote) not in body:
            print(f"FAIL {i:03d} [{kind}] quote NOT in {file_rel} :: {quote[:80]!r}")
            fails += 1
            continue
        if kind == "SPEC" and sp:
            if norm(quote) not in norm(wording[sp]):
                print(f"FAIL {i:03d} [SPEC] not inside {sp} wording :: {quote[:60]!r}")
                fails += 1
                continue
        print(f"PASS {i:03d} [{kind}] {quote[:66]!r}")
    print(f"\nquote probe: {len(PROBES) - fails}/{len(PROBES)} green"
          + (" — FAIL-CLOSED" if fails else " — ALL QUOTES VERIFIED"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
