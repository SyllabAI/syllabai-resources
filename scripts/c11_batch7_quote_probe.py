#!/usr/bin/env python3
"""T-C11 session 59 — pre-authoring quote probe for the batch-7 decision
record (scripts/c11_batch7_decisions.yaml): every planned NOTE / MARK_SCHEME
/ SPEC quote must byte-verify under the T-C10 norm() in its cited file, and
every SPEC quote must sit inside its SP's official wording (the
c11_batch6_quote_probe.py pattern, batch-7-scoped).

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

F1 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "f. Acids, Alkalis & Titrations/What is an indicator - IGCSE Chemistry "
      "Revision Notes.md")
F2 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "f. Acids, Alkalis & Titrations/Acids, Alkalis & Neutralisation - "
      "IGCSE Revision Notes.md")
F3 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "f. Acids, Alkalis & Titrations/Acid-Alkali Titrations  Edexcel IGCSE "
      "Chemistry Revision Notes 2017.md")
G1 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "g. Acids, Bases & Salt Preparations/Solubility Rules  Edexcel IGCSE "
      "Chemistry Revision Notes 2017.md")
G2 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "g. Acids, Bases & Salt Preparations/What are acids and bases - IGCSE "
      "Chemistry Revision Notes.md")
G3 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "g. Acids, Bases & Salt Preparations/Reactions of acids - IGCSE "
      "Chemistry Revision Notes.md")
G4 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "g. Acids, Bases & Salt Preparations/Bases and alkalis - IGCSE "
      "Chemistry Revision Notes.md")
G5 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "g. Acids, Bases & Salt Preparations/Making soluble salts - IGCSE "
      "Chemistry Revision Notes.md")
G6 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "g. Acids, Bases & Salt Preparations/Preparing copper sulfate - IGCSE "
      "Chemistry Revision Notes.md")
G7 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "g. Acids, Bases & Salt Preparations/Prepare a Soluble Salt II  "
      "Edexcel IGCSE Chemistry Revision Notes 2017.md")
G8 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "g. Acids, Bases & Salt Preparations/Prepare an Insoluble Salt  "
      "Edexcel IGCSE Chemistry Revision Notes 2017.md")
G9 = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
      "g. Acids, Bases & Salt Preparations/Preparing lead sulfate - IGCSE "
      "Chemistry Revision Notes.md")
M1 = "scripts/c11_evidence/ACIDS_ALKALIS_TITRATIONS_MS_P2.txt"
M2 = "scripts/c11_evidence/ACIDS_BASES_SALT_PREP_MS_P2.txt"
SP = "graph/igcse-chemistry/specification_points.yaml"

# (file, quote, kind, sp-or-None)  — SPEC quotes checked against the SP wording
PROBES = [
    # --- 2.28 indicators (F1) ------------------------------------------------
    (F1, "Two colours indicators are used to distinguish between acids and alkalis", "NOTE", "4CH1-2.28"),
    (F1, "Phenolphthalein and methyl orange are synthetic indicators frequently used in acid-alkali titrations", "NOTE", "4CH1-2.28"),
    (F1, "Litmus is not suitable for titrations as the colour change is not sharp and it goes through a purple transition colour in neutral solutions making it difficult to determine an endpoint", "NOTE", "4CH1-2.28"),
    (F1, "Synthetic indicators are used to show the endpoint in titrations as they have a very sharp change of colour when an acid has been neutralised by an alkali and vice-versa", "NOTE", "4CH1-2.28"),
    (SP, "describe the use of litmus, phenolphthalein and methyl orange to distinguish between acidic and alkaline solutions", "SPEC", "4CH1-2.28"),
    # --- 2.29 pH scale (F1) ---------------------------------------------------
    (F1, "The pH scale goes from 0 - 14", "NOTE", "4CH1-2.29"),
    (F1, "All acids have pH values of below 7, all alkalis have pH values of above 7", "NOTE", "4CH1-2.29"),
    (F1, "A solution of pH 7 is described as being neutral", "NOTE", "4CH1-2.29"),
    (F1, "pH 0-3 = strong acid", "NOTE", "4CH1-2.29"),
    (F1, "pH 4-6 = weak acid", "NOTE", "4CH1-2.29"),
    (F1, "pH 8-10 = weak alkali", "NOTE", "4CH1-2.29"),
    (F1, "pH 11-14 = strong alkali", "NOTE", "4CH1-2.29"),
    (SP, "understand how to use the pH scale, from 0-14, can be used to classify solutions as strongly acidic (0-3), weakly acidic (4-6), neutral (7), weakly alkaline (8-10) and strongly alkaline (11-14)", "SPEC", "4CH1-2.29"),
    # --- 2.30 universal indicator (F1) ---------------------------------------
    (F1, "Universal indicator is a wide range indicator and can give only an approximate value for pH", "NOTE", "4CH1-2.30"),
    (F1, "It is made of a mixture of different plant indicators which operate across a broad pH range and is useful for estimating the pH of an unknown solution", "NOTE", "4CH1-2.30"),
    (F1, "A few drops are added to the solution and the colour is matched with a colour chart which indicates the pH which matches with specific colours", "NOTE", "4CH1-2.30"),
    (F1, "A common error is to suggest using universal indicator as a suitable indicator for an acid-base titration", "NOTE", "4CH1-2.30"),
    (SP, "describe the use of universal indicator to measure the approximate pH value of an aqueous solution", "SPEC", "4CH1-2.30"),
    # --- 2.31 acid/alkali ion sources (F2) ------------------------------------
    (F2, "When acids are added to water, they form positively charged hydrogen ions", "NOTE", "4CH1-2.31"),
    (F2, "When alkalis are added to water, they form negative hydroxide ions", "NOTE", "4CH1-2.31"),
    (F2, "The pH scale is a numerical scale which is used to show how acidic or alkaline a solution is", "NOTE", "4CH1-2.31"),
    (F2, "It is a measure of the amount of the hydrogen ions present in solution", "NOTE", "4CH1-2.31"),
    (SP, "know that acids in aqueous solution are a source of hydrogen ions and alkalis in a aqueous solution are a source of hydroxide ions", "SPEC", "4CH1-2.31"),
    # --- 2.32 neutralisation (F2) ----------------------------------------------
    (F2, "A neutralisation reaction occurs when an acid reacts with an alkali", "NOTE", "4CH1-2.32"),
    (F2, "Not all reactions of acids are neutralisations", "NOTE", "4CH1-2.32"),
    (F2, "For example when a metal reacts with an acid, although a salt is produced there is no water formed so it does not fit the definition of neutralisation", "NOTE", "4CH1-2.32"),
    (F2, "Neutralisation is very important in the treatment of soils to raise the pH as some crops cannot tolerate pH levels below 7", "NOTE", "4CH1-2.32"),
    (SP, "know that alkalis can neutralise acids", "SPEC", "4CH1-2.32"),
    # --- 2.33C titration (F3) ---------------------------------------------------
    (F3, "Titrations are a method of analysing the concentration of solutions", "NOTE", "4CH1-2.33C"),
    (F3, "They can determine exactly how much alkali is needed to neutralise a quantity of acid - and vice versa", "NOTE", "4CH1-2.33C"),
    (F3, "Titrations can also be used to prepare salts", "NOTE", "4CH1-2.33C"),
    (F3, "Use the pipette and pipette filler and place exactly 25 cm3 sodium hydroxide solution into the conical flask", "NOTE", "4CH1-2.33C"),
    (F3, "Run a small portion of hydrochloric acid through the burette to remove any air bubbles", "NOTE", "4CH1-2.33C"),
    (F3, "Record the starting point on the burette to the nearest 0.05 cm3", "NOTE", "4CH1-2.33C"),
    (F3, "The purpose of the white tile is to make colour changes more obvious", "NOTE", "4CH1-2.33C"),
    (F3, "Perform a rough titration by taking the burette reading and running in the solution in 1 - 3 cm3 portions", "NOTE", "4CH1-2.33C"),
    (F3, "The end-point wil be indicated by a sharp colour change", "NOTE", "4CH1-2.33C"),
    (F3, "As the rough end-point volume is approached, add the solution from the burette one drop at a time until the indicator just changes colour", "NOTE", "4CH1-2.33C"),
    (F3, "Repeat until you achieve two concordant results (two results that are within 0.1 cm3 of each other) to increase accuracy", "NOTE", "4CH1-2.33C"),
    (SP, "describe how to carry out an acid-alkali titration", "SPEC", "4CH1-2.33C"),
    # --- 2.34 solubility rules (G1) ----------------------------------------------
    (G1, "Ionic compounds are generally soluble in water compared to covalent substances, but there are exceptions", "NOTE", "4CH1-2.34"),
    (G1, "A knowledge of the solubility of ionic compounds helps us to determine the most appropriate method for the preparation of salts", "NOTE", "4CH1-2.34"),
    (G1, "Note that calcium hydroxide is slightly soluble in water", "NOTE", "4CH1-2.34"),
    (G1, "Calcium hydroxide solution is more commonly know as limewater and is used to test for carbon dioxide.", "NOTE", "4CH1-2.34"),
    (SP, "know the general rules for predicting the solubility of ionic compounds in water:", "SPEC", "4CH1-2.34"),
    # --- 2.35 proton transfer (G2) -------------------------------------------------
    (G2, "The earlier definition of an acid and a base can be extended", "NOTE", "4CH1-2.35"),
    (G2, "In terms of proton transfer, we can further define each substance in how they interact with protons", "NOTE", "4CH1-2.35"),
    (SP, "understand acids and bases in terms of proton transfer", "SPEC", "4CH1-2.35"),
    # --- 2.36 donor/acceptor (G2) ---------------------------------------------------
    (G2, "Acids are proton donors as they ionize in solution producing protons", "NOTE", "4CH1-2.36"),
    (G2, "Bases (alkalis) are proton acceptors as they ionize in solution producing OH- ions which can accept protons", "NOTE", "4CH1-2.36"),
    (G2, "These H+ ions make the aqueous solution acidic", "NOTE", "4CH1-2.36"),
    (G2, "OH- ions make the aqueous solution alkaline", "NOTE", "4CH1-2.36"),
    (M2, "H3O+ in place of H+", "MARK_SCHEME", None),
    (SP, "understand that an acid is a proton donor and a base is a proton acceptor", "SPEC", "4CH1-2.36"),
    # --- 2.37 acid reaction families (G3) --------------------------------------------
    (G3, "Only metals above hydrogen in the reactivity series will react with dilute acids", "NOTE", "4CH1-2.37"),
    (G3, "The more reactive the metal then the more vigorous the reaction will be", "NOTE", "4CH1-2.37"),
    (G3, "Metals that are placed high on the reactivity series such as potassium and sodium are very dangerous and react explosively with acids", "NOTE", "4CH1-2.37"),
    (G3, "When acids react with metals they form a salt and hydrogen gas", "NOTE", "4CH1-2.37"),
    (G3, "metal + acid ⟶ salt + hydrogen", "NOTE", "4CH1-2.37"),
    (G3, "When an acid reacts with a base, a neutralisation reaction occurs", "NOTE", "4CH1-2.37"),
    (G3, "In all acid-base neutralisation reactions, a salt and water are produced", "NOTE", "4CH1-2.37"),
    (G3, "The identity of the salt produced depends on the acid used and the positive ions in the base", "NOTE", "4CH1-2.37"),
    (G3, "Hydrochloric acid produces chlorides, sulfuric acid produces sulfate salts and nitric acid produces nitrates", "NOTE", "4CH1-2.37"),
    (G3, "Metal oxides and metal hydroxides act as bases", "NOTE", "4CH1-2.37"),
    (G3, "Acids will react with metal carbonates to form the corresponding metal salt, carbon dioxide and water", "NOTE", "4CH1-2.37"),
    (G3, "due to the presence of effervescence caused by the carbon dioxide gas", "NOTE", "4CH1-2.37"),
    (SP, "describe the reactions of hydrochloric acid, sulfuric acid and nitric acid with metals, bases and metal carbonates (excluding the reactions between nitric acid and metals) to form salts", "SPEC", "4CH1-2.37"),
    # --- 2.38 bases & alkalis (G4) ------------------------------------------------------
    (G4, "Bases are substances which can neutralise an acid, forming a salt and water", "NOTE", "4CH1-2.38"),
    (G4, "A base which is water-soluble is referred to as an alkali", "NOTE", "4CH1-2.38"),
    (G4, "So, all alkalis are bases, but not all bases are alkalis", "NOTE", "4CH1-2.38"),
    (G4, "Alkalis have pH values of above 7", "NOTE", "4CH1-2.38"),
    (G4, "Bases are usually oxides, hydroxides or carbonates of metals", "NOTE", "4CH1-2.38"),
    (G4, "One unusual base is ammonia solution", "NOTE", "4CH1-2.38"),
    (G4, "When ammonia reacts with water it produces hydroxide ions", "NOTE", "4CH1-2.38"),
    (G4, "ammonia is the gas, NH3, ammonium is the ion present in ammonium compounds", "NOTE", "4CH1-2.38"),
    (SP, "know that metal oxides, metal hydroxides and ammonia can act as bases, and that alkalis are bases that are soluble in water", "SPEC", "4CH1-2.38"),
    # --- 2.39 insoluble-reactant route (G5) -----------------------------------------------
    (G5, "A soluble salt can be made from the reaction of an acid with an insoluble base", "NOTE", "4CH1-2.39"),
    (G5, "During the preparation of soluble salts, the insoluble reactant is added in excess to ensure that all of the acid has reacted", "NOTE", "4CH1-2.39"),
    (G5, "If this step is not completed, any unreacted acid would become dangerously concentrated during evaporation and crystallisation", "NOTE", "4CH1-2.39"),
    (G5, "The excess reactant is then removed by filtration to ensure that only the salt and water remain", "NOTE", "4CH1-2.39"),
    (G5, "The water is evaporated by heating until small crystals begin to appear", "NOTE", "4CH1-2.39"),
    (G5, "Allowing the filtered solution to evaporate slowly over a period of days results in the formation of larger crystals", "NOTE", "4CH1-2.39"),
    (G5, "If a carbonate was used as the solid base instead of an oxide or hydroxide, then any carbon dioxide gas produced would have been released into the atmosphere", "NOTE", "4CH1-2.39"),
    (G5, "The acid could also be reacted with a metal to produce the salt, as long as the metal is above hydrogen in the reactivity series and not too reactive so that a dangerous reaction does not take place", "NOTE", "4CH1-2.39"),
    (SP, "describe an experiment to prepare a pure, dry sample of a soluble salt, starting from an insoluble reactant", "SPEC", "4CH1-2.39"),
    # --- 2.40C titration route (G7) ----------------------------------------------------------
    (G7, "It is also possible to prepare a sample of a dry salt starting from an acid and an alkali", "NOTE", "4CH1-2.40C"),
    (G7, "A titration can be used for this", "NOTE", "4CH1-2.40C"),
    (G7, "Use a pipette to measure the alkali into a conical flask and add a few drops of indicator (phenolphthalein or methyl orange)", "NOTE", "4CH1-2.40C"),
    (G7, "Add this same volume of acid into the same volume of alkali without the indicator", "NOTE", "4CH1-2.40C"),
    (G7, "Heat to partially evaporate, leaving a saturated solution", "NOTE", "4CH1-2.40C"),
    (G7, "Leave to crystallise decant excess solution and allow crystals to dry", "NOTE", "4CH1-2.40C"),
    (SP, "describe an experiment to prepare a pure, dry sample of a soluble salt, starting from an acid and alkali", "SPEC", "4CH1-2.40C"),
    # --- 2.41C precipitation route (G8) --------------------------------------------------------
    (G8, "Insoluble salts can be prepared using a precipitation reaction", "NOTE", "4CH1-2.41C"),
    (G8, "The solid salt obtained is the precipitate, thus in order to successfully use this method the solid salt being formed must be insoluble in water", "NOTE", "4CH1-2.41C"),
    (G8, "soluble salt 1 + soluble salt 2 ⟶  insoluble salt + soluble salt 3", "NOTE", "4CH1-2.41C"),
    (G8, "The method involves measuring out a fixed volume of one salt solution and then adding the second salt solution until it is in a slight excess", "NOTE", "4CH1-2.41C"),
    (G8, "This ensures the maximum amount of precipitate will be obtained", "NOTE", "4CH1-2.41C"),
    (G8, "The precipitate is recovered by filtration", "NOTE", "4CH1-2.41C"),
    (G8, "Then it must be washed with distilled water remove reactants that are contaminating the residue (recovered solid)", "NOTE", "4CH1-2.41C"),
    (G8, "This method is a good way to prepare silver and lead(II) salts which are often insoluble; the starting material will usually be the nitrate of silver or lead(II) since all nitrates are soluble", "NOTE", "4CH1-2.41C"),
    (G8, "This reaction is also known as a double decomposition reaction.", "NOTE", "4CH1-2.41C"),
    (SP, "describe an experiment to prepare a pure, dry sample of an insoluble salt, starting from two soluble reactants", "SPEC", "4CH1-2.41C"),
    # --- 2.42 PR-07 copper sulfate (G6) ----------------------------------------------------------
    (G6, "To prepare a pure, dry sample of hydrated copper(II) sulfate crystals", "NOTE", "4CH1-2.42"),
    (G6, "Add the copper(II) oxide slowly to the hot dilute acid and stir until the base is in excess (i.e. until the base stops dissolving and a suspension of the base forms in the acid)", "NOTE", "4CH1-2.42"),
    (G6, "Filter the mixture into an evaporating basin to remove the excess base", "NOTE", "4CH1-2.42"),
    (G6, "Gently heat the solution in a water bath or with an electric heater to evaporate the water and to make the solution saturated", "NOTE", "4CH1-2.42"),
    (G6, "Check the solution is saturated by dipping a cold glass rod into the solution and seeing if crystals form on the end", "NOTE", "4CH1-2.42"),
    (G6, "Leave the filtrate in a warm place to dry and crystallise", "NOTE", "4CH1-2.42"),
    (G6, "The base is added in excess to use up all of the acid, which would become dangerously concentrated during the evaporation and crystallisation stages", "NOTE", "4CH1-2.42"),
    (G6, "Hydrated copper(II) sulfate crystals should be bright blue and regularly shaped", "NOTE", "4CH1-2.42"),
    (SP, "practical: prepare a sample of pure, dry hydrated copper(II) sulfate crystals starting from copper(II) oxide", "SPEC", "4CH1-2.42"),
    # --- 2.43C PR-08 lead sulfate (G9) ---------------------------------------------------------------
    (G9, "To prepare a dry sample of lead(II) sulfate", "NOTE", "4CH1-2.43C"),
    (G9, "The solid salt obtained is the precipitate, thus in order to successfully use this method the solid salt being formed must be insoluble in water, and the reactants must be soluble", "NOTE", "4CH1-2.43C"),
    (G9, "Measure out 25 cm3 of 0.5 mol dm-3 lead(II)nitrate solution and add it to a small beaker", "NOTE", "4CH1-2.43C"),
    (G9, "Measure out 25 cm3 of 0.5 mol dm-3 of potassium sulfate add it to the beaker and mix together using a stirring rod", "NOTE", "4CH1-2.43C"),
    (G9, "Filter to remove precipitate from mixture", "NOTE", "4CH1-2.43C"),
    (G9, "Wash filtrate with distilled water to remove traces of other solutions", "NOTE", "4CH1-2.43C"),
    (G9, "lead(II) nitrate + potassium sulfate → lead(II) sulfate + potassium nitrate", "NOTE", "4CH1-2.43C"),
    (G9, "Pb(NO3)2 (aq) + K2SO4 (aq) → PbSO4 (s) + 2KNO3 (aq)", "NOTE", "4CH1-2.43C"),
    (SP, "practical: prepare a sample of pure, dry lead(II) sulfate", "SPEC", "4CH1-2.43C"),
    # --- misconception 1: endpoint-pH (M1) -------------------------------------------------------------
    (M1, "temperature goes down/stops rising/stays constant", "MARK_SCHEME", None),
    (M1, "Accept measure pH/when pH = 7/when pH is less than 7", "MARK_SCHEME", None),
    (M1, "Reject changing to any pH value > 7", "MARK_SCHEME", None),
    (M1, "Accept use of any indicator (named example or just indicator)", "MARK_SCHEME", None),
    (M1, "stirring/mixing/swirling", "MARK_SCHEME", None),
    # --- misconception 2: precipitate-in-filtrate (M2) ---------------------------------------------------
    (M2, "they would obtain sodium nitrate instead", "MARK_SCHEME", None),
    (M2, "the filtrate does not contain lead(II) sulfate/the insoluble salt", "MARK_SCHEME", None),
    (M2, "the lead(II) sulfate/insoluble salt has already been obtained in step 3", "MARK_SCHEME", None),
    (M2, "they should have used the residue", "MARK_SCHEME", None),
    (M2, "REJECT any reference to heating directly", "MARK_SCHEME", None),
    (M2, "REJECT the use of reagents that would not work, eg magnesium chloride", "MARK_SCHEME", None),
    (M2, "boiling off all the water (will not produce a hydrated salt)", "MARK_SCHEME", None),
    # --- in-slice edge anchors ---------------------------------------------------------------------------
    (F2, "When these substances react together in a neutralisation reaction, the H+ ions react with the OH- ions to produce water", "NOTE", None),
    (F3, "Add a few drops of a suitable indicator to the solution to the conical flask", "NOTE", None),
    (G5, "CuO (s) + H2SO4&nbsp; (aq) ⟶ CuSO4&nbsp; (aq) + H2O (l)", "NOTE", None),
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
