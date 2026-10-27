#!/usr/bin/env python3
"""T-C11 session 55 — pre-authoring quote probe for the batch-5 decision
record (scripts/c11_batch5_decisions.yaml): every planned NOTE / MARK_SCHEME
/ SPEC quote must byte-verify under the T-C10 norm() in its cited file, and
every SPEC quote must sit inside its SP's official wording (the
c11_batch4_quote_probe.py pattern, batch-5-scoped).

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

N1 = "Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/a. Group 1 (Alkali Metals)/Group 1 reactivity & trends - IGCSE Chemistry Revision Notes.md"
N2 = "Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/a. Group 1 (Alkali Metals)/Group 1 Reactivity & Electronic Configurations  Edexcel IGCSE Chemistry Revision Notes 2017.md"
N3 = "Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/b. Group 7 (Halogens)/Group 7 properties - IGCSE Chemistry Revision Notes.md"
N4 = "Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/b. Group 7 (Halogens)/Group 7 reactivity - IGCSE Chemistry Revision Notes.md"
N5 = "Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/c. Gases in the Atmosphere/Composition of air - IGCSE Chemistry Revision Notes.md"
N6 = "Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/c. Gases in the Atmosphere/Oxygen percentage in air - IGCSE Chemistry Revision Notes.md"
N7 = "Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/c. Gases in the Atmosphere/Combustion  Edexcel IGCSE Chemistry Revision Notes 2017.md"
N8 = "Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/c. Gases in the Atmosphere/Thermal decomposition - IGCSE Chemistry Revision Notes.md"
N9 = "Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/c. Gases in the Atmosphere/Greenhouse effect - IGCSE Chemistry Revision Notes.md"
M1 = "scripts/c11_evidence/GROUP1_MS_P2.txt"
M2 = "scripts/c11_evidence/GROUP7_MS_P2.txt"
M3 = "scripts/c11_evidence/GASES_MS_P2.txt"

# (file, quote, kind, sp-or-None)  — SPEC quotes checked against the SP wording
PROBES = [
    # --- Group 1 (2.1-2.4C) -------------------------------------------------
    (N1, "The Group 1 metals are known as the alkali metals", "NOTE", "4CH1-2.1"),
    (N1, "They form alkaline solutions when they react with water", "NOTE", "4CH1-2.1"),
    (N1, "The reaction of the Group 1 metals with water provides evidence for categorising these elements into the same chemical family", "NOTE", "4CH1-2.1"),
    (N1, "Group 1 metal + water ⟶ metal hydroxide + hydrogen", "NOTE", "4CH1-2.1"),
    (N1, "The differences between the reactions of the group 1 metals with water and oxygen provide evidence of trends within the group", "NOTE", "4CH1-2.2"),
    (N1, "The reactions of the alkali metals with water get more vigorous as you descend the group", "NOTE", "4CH1-2.2"),
    (N1, "The alkali metals react with oxygen in the air forming metal oxides, which is why the alkali metals tarnish when exposed to the air", "NOTE", "4CH1-2.2"),
    (N1, "The metal tarnish more rapidly as you go down the group", "NOTE", "4CH1-2.2"),
    (N1, "Following these trends, we can say that:", "NOTE", "4CH1-2.3"),
    (N1, "Rubidium, caesium and francium will react even more vigorously with air and water than the first three alkali metals", "NOTE", "4CH1-2.3"),
    (N1, "Of the alkali metals, lithium is the least reactive (as it is at the top of Group 1) and francium would be the most reactive (as it’s at the bottom of Group 1)", "NOTE", "4CH1-2.3"),
    (N2, "The reactivity of the Group 1 metals increases as you go down the group", "NOTE", "4CH1-2.4C"),
    (N2, "As you go down Group 1, the number of shells of electrons increases by 1", "NOTE", "4CH1-2.4C"),
    (N2, "This means that the outermost electron gets further away from the nucleus, so there are weaker forces of attraction between the outermost electron and the nucleus", "NOTE", "4CH1-2.4C"),
    (N2, "Less energy is required to overcome the force of attraction as it gets weaker, so the outer electron is lost more easily", "NOTE", "4CH1-2.4C"),
    (N2, "So, the alkali metals get more reactive as you descend the group", "NOTE", "4CH1-2.4C"),
    (M1, "potassium loses its outer/valence electron", "MARK_SCHEME", None),
    (M1, "more easily/readily", "MARK_SCHEME", None),
    (M1, "because it is further from (the attraction of)", "MARK_SCHEME", None),
    (M1, "IGNORE references to more shells / larger atomic radius / more", "MARK_SCHEME", None),
    (M1, "Ignore references to shielding", "MARK_SCHEME", None),
    (M1, "If no reference to nucleus or protons, then neither M3", "MARK_SCHEME", None),
    # --- Group 7 (2.5-2.8C) -------------------------------------------------
    (N3, "The elements in Group 7 are known as the halogens", "NOTE", "4CH1-2.5"),
    (N3, "At room temperature, the halogens exist in different states and colours, with different characteristics", "NOTE", "4CH1-2.5"),
    (N3, "The melting and boiling points of the halogens increase as you go down the group", "NOTE", "4CH1-2.5"),
    (N3, "At room temperature (20 °C), the physical state of the halogens changes as you go down the group", "NOTE", "4CH1-2.5"),
    (N3, "The colours of the halogens also change as you descend the group - they become darker", "NOTE", "4CH1-2.5"),
    (N3, "All halogens have similar reactions as they each have seven electrons in their outermost shell", "NOTE", "4CH1-2.5"),
    (N3, "Chlorine, bromine and iodine react with metals and non-metals to form compounds", "NOTE", "4CH1-2.6"),
    (N3, "The halogens react with some metals to form ionic compounds which are metal halide salts", "NOTE", "4CH1-2.6"),
    (N3, "The halogens decrease in reactivity moving down the group, but they still form halide salts with some metals including iron", "NOTE", "4CH1-2.6"),
    (N3, "the halogens react with hydrogen to form hydrogen halides", "NOTE", "4CH1-2.6"),
    (N3, "A halogen displacement reaction occurs when a more reactive halogen displaces a less reactive halogen from an aqueous solution of its halide", "NOTE", "4CH1-2.7"),
    (N3, "The reactivity of Group 7 elements decreases as you move down the group", "NOTE", "4CH1-2.7"),
    (N3, "The solution becomes orange as bromine is formed or", "NOTE", "4CH1-2.7"),
    (N3, "The solution becomes brown as iodine is formed", "NOTE", "4CH1-2.7"),
    (N3, "Chlorine will displace bromine or iodine from an aqueous solution of the metal halide", "NOTE", "4CH1-2.7"),
    (N3, "Bromine will displace iodine from an aqueous solution of the metal iodide", "NOTE", "4CH1-2.7"),
    (N4, "When halogen atoms gain an electron during reactions, they form -1 ions called halide ions", "NOTE", "4CH1-2.8C"),
    (N4, "We can use electronic configuration to explain the trends in chemical reactivity down Group 7", "NOTE", "4CH1-2.8C"),
    (N4, "Reactivity of Group 7 non-metals decreases as you go down the group", "NOTE", "4CH1-2.8C"),
    (N4, "As you go down Group 7, the number of shells of electrons increases, the same as with all other groups", "NOTE", "4CH1-2.8C"),
    (N4, "This means that the increased distance from the outer shell to the nucleus as you go down a group makes the halogens become less reactive", "NOTE", "4CH1-2.8C"),
    (N4, "As you move down the group, the forces of attraction between the nucleus and the outermost shell decreases", "NOTE", "4CH1-2.8C"),
    (N4, "This makes it harder for the atoms to gain electrons as you descend the group", "NOTE", "4CH1-2.8C"),
    (M2, "a halogen/an element cannot displace itself", "MARK_SCHEME", None),
    (M2, "Reject any references to a halogen", "MARK_SCHEME", None),
    (M2, "a halogen cannot displace a more reactive halogen", "MARK_SCHEME", None),
    (M2, "a halogen cannot react with the (halide) ions of a", "MARK_SCHEME", None),
    # --- Atmosphere (2.9-2.14) ----------------------------------------------
    (N5, "About four-fifths (approximately 80%) nitrogen", "NOTE", "4CH1-2.9"),
    (N5, "about one fifth (approximately 20%) oxygen", "NOTE", "4CH1-2.9"),
    (N5, "small proportions of other gases including carbon dioxide, water vapour and trace quantities of the noble gases", "NOTE", "4CH1-2.9"),
    (N5, "The percentage of oxygen in air can be found by reacting a metal or non-metal with the oxygen in a fixed volume of air", "NOTE", "4CH1-2.10"),
    (N5, "One way to carry this out is to burn a small amount of phosphorus in a bell jar that is sitting in a trough of water", "NOTE", "4CH1-2.10"),
    (N5, "As the phosphorus burns it uses up the oxygen inside the bell jar and the water level rises", "NOTE", "4CH1-2.10"),
    (N5, "Phosphorus is very suitable for this experiment as it burns readily until all the available oxygen is used up", "NOTE", "4CH1-2.10"),
    (N6, "To determine the percentage of oxygen in air using the oxidation of iron", "NOTE", "4CH1-2.10"),
    (N6, "sprinkle some iron filings or push a piece of iron wool into the bottom of the burette", "NOTE", "4CH1-2.10"),
    (N6, "percentage of oxygen =", "NOTE", "4CH1-2.10"),
    (N6, "percentage of oxygen = 19.7%", "NOTE", "4CH1-2.10"),
    (N6, "The oxygen takes up approximately 20% of the air", "NOTE", "4CH1-2.14"),
    (N6, "After 3-4 days note the new position of the water level", "NOTE", "4CH1-2.14"),
    (N7, "Combustion is the scientific word for burning", "NOTE", "4CH1-2.11"),
    (N7, "All combustion reactions involve a chemical change in which oxygen reacts with elements or compounds to produce oxides", "NOTE", "4CH1-2.11"),
    (N7, "Combustion reactions give out heat, so they will always be exothermic reactions", "NOTE", "4CH1-2.11"),
    (N7, "You need to be able to describe the combustion reactions of magnesium, hydrogen and sulfur", "NOTE", "4CH1-2.11"),
    (N7, "Intense white flame", "NOTE", "4CH1-2.11"),
    (N7, "White powder produced (magnesium oxide)", "NOTE", "4CH1-2.11"),
    (N7, "2Mg (s) + O2 (g) → 2MgO (s)", "NOTE", "4CH1-2.11"),
    (N7, "Water is produced", "NOTE", "4CH1-2.11"),
    (N7, "2H2 (g) + O2 (g) → 2H2O (g)", "NOTE", "4CH1-2.11"),
    (N7, "Blue flame", "NOTE", "4CH1-2.11"),
    (N7, "Colourless, poisonous gas produced", "NOTE", "4CH1-2.11"),
    (N7, "S (s) + O2 (g) → SO2 (g)", "NOTE", "4CH1-2.11"),
    (N7, "Combustion reactions can also be classified as oxidation reactions.", "NOTE", "4CH1-2.11"),
    (N8, "Thermal decomposition is the term used to describe reactions where a substance breaks down due to the action of heat", "NOTE", "4CH1-2.12"),
    (N8, "Carbonates of metals from the lower half of the reactivity series tend to decompose on heating to produce the metal oxide and carbon dioxide gas:", "NOTE", "4CH1-2.12"),
    (N8, "metal carbonate → metal oxide + carbon dioxide", "NOTE", "4CH1-2.12"),
    (N8, "The thermal decomposition of copper(II)carbonate occurs readily on heating", "NOTE", "4CH1-2.12"),
    (N8, "Copper(II) carbonate is a green powder and slowly darkens as black copper(II) oxide is produced", "NOTE", "4CH1-2.12"),
    (N8, "CuCO3 (s) → CuO (s)+ CO2 (g)", "NOTE", "4CH1-2.12"),
    (N8, "The carbon dioxide given off can be tested by passing the gas through limewater and looking for it to turn milky", "NOTE", "4CH1-2.12"),
    (N9, "Greenhouse gases maintain the temperatures on Earth high enough to support life", "NOTE", "4CH1-2.13"),
    (N9, "carbon dioxide", "NOTE", "4CH1-2.13"),
    (N9, "Increasing amounts of carbon dioxide in the atmosphere may contribute to climate change", "NOTE", "4CH1-2.13"),
    (N9, "Much of the radiation is trapped inside the Earth’s atmosphere by greenhouse gases which can absorb and store the energy", "NOTE", "4CH1-2.13"),
    (N9, "Combustion of wood and fossil fuels", "NOTE", "4CH1-2.13"),
    (M3, "REJECT all other colours", "MARK_SCHEME", None),
    (M3, "black", "MARK_SCHEME", None),
    (M3, "IGNORE brown", "MARK_SCHEME", None),
    (M3, "white precipitate forms / liquid goes milky/cloudy", "MARK_SCHEME", None),
    # --- SPEC probes (official wording spans) --------------------------------
    ("graph/igcse-chemistry/specification_points.yaml", "the similarities in the reactions of these elements with water provide evidence for their recognition as a family of elements", "SPEC", "4CH1-2.1"),
    ("graph/igcse-chemistry/specification_points.yaml", "the differences between the reactions of these elements with air and water provide evidence for the trend in reactivity in Group 1", "SPEC", "4CH1-2.2"),
    ("graph/igcse-chemistry/specification_points.yaml", "use knowledge of trends in Group 1 to predict the properties of other alkali metals", "SPEC", "4CH1-2.3"),
    ("graph/igcse-chemistry/specification_points.yaml", "explain the trend in reactivity in Group 1 in terms of electronic configurations", "SPEC", "4CH1-2.4C"),
    ("graph/igcse-chemistry/specification_points.yaml", "know the colours, physical states (at room temperature) and trends in physical properties of these elements", "SPEC", "4CH1-2.5"),
    ("graph/igcse-chemistry/specification_points.yaml", "use knowledge of trends in Group 7 to predict the properties of other halogens", "SPEC", "4CH1-2.6"),
    ("graph/igcse-chemistry/specification_points.yaml", "displacement reactions involving halogens and halides provide evidence for the trend in reactivity in Group 7", "SPEC", "4CH1-2.7"),
    ("graph/igcse-chemistry/specification_points.yaml", "explain the trend in reactivity in Group 7 in terms of electronic configurations", "SPEC", "4CH1-2.8C"),
    ("graph/igcse-chemistry/specification_points.yaml", "know the approximate percentages by volume of the four most abundant gases in dry air", "SPEC", "4CH1-2.9"),
    ("graph/igcse-chemistry/specification_points.yaml", "understand how to determine the percentage by volume of oxygen in air using experiments involving the reactions of metals (e.g. iron) and non-metals (e.g. phosphorus) with air", "SPEC", "4CH1-2.10"),
    ("graph/igcse-chemistry/specification_points.yaml", "describe the combustion of elements in oxygen, including magnesium, hydrogen and sulfur", "SPEC", "4CH1-2.11"),
    ("graph/igcse-chemistry/specification_points.yaml", "describe the formation of carbon dioxide from the thermal decomposition of metal carbonates, including copper(II) carbonate", "SPEC", "4CH1-2.12"),
    ("graph/igcse-chemistry/specification_points.yaml", "know that carbon dioxide is a greenhouse gas and that increasing amounts in the atmosphere may contribute to climate change", "SPEC", "4CH1-2.13"),
    ("graph/igcse-chemistry/specification_points.yaml", "practical: determine the approximate percentage by volume of oxygen in air using a metal or a non-metal", "SPEC", "4CH1-2.14"),
]

sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402

_SPEC_SP = {}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = s.translate({ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"})
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def main() -> int:
    import yaml
    spec = yaml.safe_load(GP.store("specification_points").read_text(encoding="utf-8"))
    wording = {p["code"]: p["official_wording"] for p in spec["specification_points"]}

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
