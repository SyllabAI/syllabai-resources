#!/usr/bin/env python3
"""T-C11 session 53 — authoring aid: probe planned batch-4 evidence quotes
against the T-C10 norm() convention BEFORE writing the decision record
(the same byte-verification the preverify/generator G03 will apply)."""
import re
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

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


# (file, quote) pairs planned for the batch-4 record
E = "Chemistry IGCSE Revision Notes/3. Physical Chemistry"
PROBES = [
    # --- note quotes: Energetics ---
    (f"{E}/a. Energetics/Exothermic and endothermic - IGCSE Chemistry Revision Notes.md",
     "An exothermic reaction releases heat energy into the surroundings"),
    (f"{E}/a. Energetics/Exothermic and endothermic - IGCSE Chemistry Revision Notes.md",
     "An endothermic reaction takes heat energy in from the surroundings"),
    (f"{E}/a. Energetics/Exothermic and endothermic - IGCSE Chemistry Revision Notes.md",
     "Neutralisation reactions:"),
    (f"{E}/a. Energetics/Exothermic and endothermic - IGCSE Chemistry Revision Notes.md",
     "Combustion reactions:"),
    (f"{E}/a. Energetics/Calorimetry - IGCSE Chemistry Revision Notes.md",
     "There are two types of calorimetry experiments you need to know"),
    (f"{E}/a. Energetics/Calorimetry - IGCSE Chemistry Revision Notes.md",
     "The solutions need to be mixed together in an insulated container to prevent heat loss"),
    (f"{E}/a. Energetics/Calorimetry - IGCSE Chemistry Revision Notes.md",
     "We can experimentally determine the relative amounts of energy released by a fuel"),
    (f"{E}/a. Energetics/Calorimetry - IGCSE Chemistry Revision Notes.md",
     "The energy released would be calculated using"),
    (f"{E}/a. Energetics/Calorimetry - IGCSE Chemistry Revision Notes.md",
     "In this experiment the main sources of error are"),
    (f"{E}/a. Energetics/Energetics calculations in chemistry - IGCSE Revision Notes.md",
     "Excess iron powder was added to 100.0 cm"),
    (f"{E}/a. Energetics/Energetics calculations in chemistry - IGCSE Revision Notes.md",
     "in a calorimeter"),
    (f"{E}/a. Energetics/Energetics calculations in chemistry - IGCSE Revision Notes.md",
     "Exothermic reactions have a negative enthalpy change"),
    (f"{E}/a. Energetics/Energetics calculations in chemistry - IGCSE Revision Notes.md",
     "In both cases, the energy released (Q) is calculated first"),
    (f"{E}/a. Energetics/Energetics calculations in chemistry - IGCSE Revision Notes.md",
     "We can compare the amount of energy released per gram and per mole for different fuels"),
    (f"{E}/a. Energetics/Energetics calculations in chemistry - IGCSE Revision Notes.md",
     "The energy released per mole is also known as the molar enthalpy change"),
    (f"{E}/a. Energetics/Energetics calculations in chemistry - IGCSE Revision Notes.md",
     "The units are kJ / mol"),
    (f"{E}/a. Energetics/Energetics calculations in chemistry - IGCSE Revision Notes.md",
     "Convert from J to kJ (divide by 1000)"),
    (f"{E}/a. Energetics/Energetics calculations in chemistry - IGCSE Revision Notes.md",
     "Calculate the enthalpy change in kJ/mol"),
    (f"{E}/a. Energetics/Energy level diagrams - IGCSE Chemistry Revision Notes.md",
     "Energy level diagrams are graphical representations of the relative energies of the reactants and products in chemical reactions"),
    (f"{E}/a. Energetics/Energy level diagrams - IGCSE Chemistry Revision Notes.md",
     "Arrows on the diagrams indicate whether the reaction is exothermic (downwards pointing) or endothermic (upwards pointing)"),
    (f"{E}/a. Energetics/Energy level diagrams - IGCSE Chemistry Revision Notes.md",
     "The difference in height between the energy of reactants and products represents the overall enthalpy change of a reaction"),
    (f"{E}/a. Energetics/What is bond energy - IGCSE Chemistry Revision Notes.md",
     "During a chemical reaction energy must be taken in to break bonds"),
    (f"{E}/a. Energetics/What is bond energy - IGCSE Chemistry Revision Notes.md",
     "During a chemical reaction, energy is released when new bonds are formed"),
    (f"{E}/a. Energetics/What is bond energy - IGCSE Chemistry Revision Notes.md",
     "Because energy is being taken in, bond breaking is an endothermic process"),
    (f"{E}/a. Energetics/What is bond energy - IGCSE Chemistry Revision Notes.md",
     "Each chemical bond has a specific bond energy associated with it"),
    (f"{E}/a. Energetics/What is bond energy - IGCSE Chemistry Revision Notes.md",
     "This is the amount of energy required to break the bond or the amount of energy given out when the bond is formed"),
    (f"{E}/a. Energetics/What is bond energy - IGCSE Chemistry Revision Notes.md",
     "To do this it is necessary to know the bonds present in both the reactants and products"),
    (f"{E}/a. Energetics/What is bond energy - IGCSE Chemistry Revision Notes.md",
     "Don't forget to take into account the balancing numbers when working out how many of each type of bond is being broken/formed"),
    (f"{E}/a. Energetics/What is bond energy - IGCSE Chemistry Revision Notes.md",
     "For bond energy questions, it is helpful to write down a displayed formula equation for the reaction before identifying the type and number of bonds"),
    (f"{E}/a. Energetics/Temperature change practical - IGCSE Revision Notes.md",
     "To perform a calorimetry study of the reaction between HCl and NaOH"),
    (f"{E}/a. Energetics/Temperature change practical - IGCSE Revision Notes.md",
     "The larger the difference in the temperature the more energy is absorbed or released"),
    # --- note quotes: Rates ---
    (f"{E}/b. Rates of Reaction/Rate of reaction - IGCSE Chemistry Revision Notes.md",
     "Reactions take place at different rates depending on the chemicals involved and the conditions"),
    (f"{E}/b. Rates of Reaction/Rate of reaction - IGCSE Chemistry Revision Notes.md",
     "You should be able to describe experiments to investigate the effect of surface area, concentration, temperature and a catalyst on a rate of reaction"),
    (f"{E}/b. Rates of Reaction/Rate of reaction - IGCSE Chemistry Revision Notes.md",
     "With an increase in the concentration of a solution, the rate of reaction will increase"),
    (f"{E}/b. Rates of Reaction/Rate of reaction - IGCSE Chemistry Revision Notes.md",
     "Factors that can affect the rate of a reaction are"),
    (f"{E}/b. Rates of Reaction/Explaining Rates  Edexcel IGCSE Chemistry Revision Notes 2017.md",
     "We can use collision theory to explain why these factors influence the reaction rate"),
    (f"{E}/b. Rates of Reaction/Explaining Rates  Edexcel IGCSE Chemistry Revision Notes 2017.md",
     "Increasing the concentration of a solution increases the rate of reaction"),
    (f"{E}/b. Rates of Reaction/Explaining Rates  Edexcel IGCSE Chemistry Revision Notes 2017.md",
     "Increasing the concentration means that there are more reactant particles in a given volume"),
    (f"{E}/b. Rates of Reaction/Explaining Rates  Edexcel IGCSE Chemistry Revision Notes 2017.md",
     "Increasing the temperature means that the particles have more kinetic energy"),
    (f"{E}/b. Rates of Reaction/Catalysts in Chemistry - IGCSE Chemistry Revision Notes.md",
     "Catalysts are substances which speed up the rate of a reaction without themselves being altered or consumed in the reaction"),
    (f"{E}/b. Rates of Reaction/Catalysts in Chemistry - IGCSE Chemistry Revision Notes.md",
     "They provide an alternative pathway for the reaction to occur"),
    (f"{E}/b. Rates of Reaction/Catalysts in Chemistry - IGCSE Chemistry Revision Notes.md",
     "The alternative pathway has a lower activation energy"),
    (f"{E}/b. Rates of Reaction/Catalysts in Chemistry - IGCSE Chemistry Revision Notes.md",
     "The mass of a catalyst at the beginning and end of a reaction is the same"),
    (f"{E}/b. Rates of Reaction/What is activation energy- IGCSE Revision Notes.md",
     "Reaction profiles are similar to energy level diagrams seen in a previous topic"),
    (f"{E}/b. Rates of Reaction/What is activation energy- IGCSE Revision Notes.md",
     "The initial increase in energy, from the reactants to the peak of the curve, represents the activation energy"),
    (f"{E}/b. Rates of Reaction/What is activation energy- IGCSE Revision Notes.md",
     "Activation energy is the minimum amount of energy that reacting particles must have in order for a reaction to occur"),
    (f"{E}/b. Rates of Reaction/What is activation energy- IGCSE Revision Notes.md",
     "Catalysts provide the reactants with an alternative pathway for the reaction which has a lower activation energy"),
    (f"{E}/b. Rates of Reaction/How surface area affects rate - IGCSE Revision Notes.md",
     "Investigating the effect of different size marble chips on the rate of reaction between calcium carbonate and hydrochloric acid"),
    (f"{E}/b. Rates of Reaction/How surface area affects rate - IGCSE Revision Notes.md",
     "Increasing the surface area of the marble chip, increases the rate of reaction"),
    (f"{E}/b. Rates of Reaction/Investigating catalysts - IGCSE Chemistry Revision Notes.md",
     "To investigate the effect of different solids on the catalytic decomposition of hydrogen peroxide"),
    (f"{E}/b. Rates of Reaction/Investigating catalysts - IGCSE Chemistry Revision Notes.md",
     "Use a delivery tube to connect this flask to a measuring cylinder upside down in water trough"),
    (f"{E}/b. Rates of Reaction/Investigating catalysts - IGCSE Chemistry Revision Notes.md",
     "Repeat experiment with different catalysts and compare results"),
    # --- note quotes: Reversible & Equilibria ---
    (f"{E}/c. Reversible Reactions & Equilibria/Reversible reactions - IGCSE Chemistry Revision Notes.md",
     "In reversible reactions, the product molecules can themselves react with each other or decompose and form the reactant molecules again"),
    (f"{E}/c. Reversible Reactions & Equilibria/Reversible reactions - IGCSE Chemistry Revision Notes.md",
     "When writing chemical equations for reversible reactions, two opposing arrows are used to indicate the forward and reverse reactions occurring at the same time"),
    (f"{E}/c. Reversible Reactions & Equilibria/Reversible reactions - IGCSE Chemistry Revision Notes.md",
     "Heating ammonium chloride produces ammonia and hydrogen chloride gases"),
    (f"{E}/c. Reversible Reactions & Equilibria/Reversible reactions - IGCSE Chemistry Revision Notes.md",
     "Reversible reactions can be seen in some hydrated salts"),
    (f"{E}/c. Reversible Reactions & Equilibria/Reversible reactions - IGCSE Chemistry Revision Notes.md",
     "These are salts that contain water of crystallisation which affects their shape and colour"),
    (f"{E}/c. Reversible Reactions & Equilibria/Reversible reactions - IGCSE Chemistry Revision Notes.md",
     "The hydrated salt can be heated / dehydrated to form anhydrous copper(II) sulfate"),
    (f"{E}/c. Reversible Reactions & Equilibria/Dynamic equilibrium - IGCSE Chemistry Revision Notes.md",
     "A reversible reaction is one which occurs in both directions"),
    (f"{E}/c. Reversible Reactions & Equilibria/Dynamic equilibrium - IGCSE Chemistry Revision Notes.md",
     "When the rate of the forward reaction equals the rate of the reverse reaction, the overall reaction is said to be in a state of equilibrium"),
    (f"{E}/c. Reversible Reactions & Equilibria/Dynamic equilibrium - IGCSE Chemistry Revision Notes.md",
     "It only occurs in a closed system"),
    (f"{E}/c. Reversible Reactions & Equilibria/Dynamic equilibrium - IGCSE Chemistry Revision Notes.md",
     "The concentration of reactants and products remains constant"),
    (f"{E}/c. Reversible Reactions & Equilibria/The position of equilibrium - IGCSE Chemistry Revision Notes.md",
     "The relative amounts of all the reactants and products at equilibrium depend on the conditions of the reaction"),
    (f"{E}/c. Reversible Reactions & Equilibria/The position of equilibrium - IGCSE Chemistry Revision Notes.md",
     "To make this prediction it is necessary to know whether the reaction is exothermic or endothermic"),
    (f"{E}/c. Reversible Reactions & Equilibria/The position of equilibrium - IGCSE Chemistry Revision Notes.md",
     "The equilibrium will shift in the direction of the endothermic reaction"),
    (f"{E}/c. Reversible Reactions & Equilibria/The position of equilibrium - IGCSE Chemistry Revision Notes.md",
     "An increase in pressure will favour the reaction that produces the least number of molecules"),
    (f"{E}/c. Reversible Reactions & Equilibria/The position of equilibrium - IGCSE Chemistry Revision Notes.md",
     "A decrease in pressure will favour the reaction that produces the greatest number of molecules"),
    (f"{E}/c. Reversible Reactions & Equilibria/The position of equilibrium - IGCSE Chemistry Revision Notes.md",
     "The presence of a catalyst does not affect the position of equilibrium but it does increase the rate at which equilibrium is reached"),
    # --- mark-scheme quotes ---
    ("scripts/c11_evidence/RATES_MS_P2.txt",
     "MAX 1 if any reference to particles gaining energy or moving more quickly"),
    ("scripts/c11_evidence/RATES_MS_P2.txt",
     "provides an alternative route"),
    ("scripts/c11_evidence/RRE_MS_P2.txt",
     "moves in the endothermic direction"),
    ("scripts/c11_evidence/RRE_MS_P2.txt",
     "moves in the exothermic direction"),
    ("scripts/c11_evidence/RRE_MS_P2.txt",
     "shifts to the side with fewer (gas) moles/molecules"),
    ("scripts/c11_evidence/ENERGETICS_MS_P2.txt",
     "Award 1 mark for 50 000"),
    ("scripts/c11_evidence/ENERGETICS_MS_P2.txt",
     "Award 2 marks for 50 000 if units changed to J/mol on answer line"),
    ("scripts/c11_evidence/ENERGETICS_MS_P2.txt",
     "Deduct 1 mark for each mistake"),
    ("scripts/c11_evidence/ENERGETICS_MS_P2.txt",
     "not all of the heat energy is transferred to the water"),
    ("scripts/c11_evidence/ENERGETICS_MS_P2.txt",
     "M1 heat (energy) /thermal energy lost (to the atmosphere)"),
]

fails = 0
for rel, quote in PROBES:
    p = REPO / rel
    if not p.exists():
        print(f"MISSING FILE: {rel}")
        fails += 1
        continue
    body = norm(p.read_text(encoding="utf-8"))
    if norm(quote) not in body:
        print(f"QUOTE NOT FOUND in {rel}:\n    {quote}")
        fails += 1
print(f"\nprobe: {len(PROBES)} quotes, {fails} failure(s)")
