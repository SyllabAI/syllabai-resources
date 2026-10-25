---
id: u3:c19:s10
title: "Worked example: the combustion calculation"
bookPage: 212
chunkRefs: [chem_v3_u3_c19_pdf221_0847, chem_v3_u3_c19_pdf221_0848, chem_v3_u3_c19_pdf222_0850, chem_v3_u3_c19_pdf222_0851]
specRefs: ["3.3", "3.4"]
blocks: []
glossary: [molar-enthalpy-change, enthalpy-change-of-combustion]
---

Combustion is exothermic, so the temperature of the water goes up; as the
ethanol burns, the total mass of burner plus ethanol goes down. Here is a
complete data set and the full route from it to a molar enthalpy change of
combustion — the calculation the examiner asks you to reproduce with fresh
numbers.

| Measurement | Value |
|---|---|
| Volume of water / cm³ | 100 |
| Mass of burner + ethanol before / g | 137.36 |
| Mass of burner + ethanol after / g | 136.58 |
| Original temperature of water / °C | 21.5 |
| Final temperature of water / °C | 62.8 |

:::worked-example
**Find the molar enthalpy change of combustion of ethanol from the data
above.**

*Step 1 — temperature change.* ∆T = 62.8 − 21.5 = **41.3 °C**.

*Step 2 — mass of water.* 100 cm³ of water has mass **100 g** (density of
water ≈ 1 g/cm³ at room temperature).

*Step 3 — heat gained by the water.* c = 4.18 J/g/°C (it is the water that
is being heated):

Q = mc∆T = 100 × 4.18 × 41.3 = 17 260 J

Divide by 1000 to convert to kJ: Q = **17.26 kJ**. This is the heat released
by the ethanol burned in this experiment.

*Step 4 — moles of ethanol burned.* Mass burned = 137.36 − 136.58 = **0.78 g**.
Ethanol, C₂H₅OH, has relative molecular mass (2 × 12) + (5 × 1) + 16 + 1 =
**46**:

n = mass ÷ Mr = 0.78 ÷ 46 = **0.01696 mol**

*Step 5 — molar enthalpy change.* The [[molar-enthalpy-change]] is the heat
energy change divided by the number of moles burned:

∆H = Q ÷ n = −17.26 ÷ 0.01696 = −1017.7 ≈ **−1020 kJ/mol** (3 s.f.)

Written on the equation:

CH₃CH₂OH + 3O₂ → 2CO₂ + 3H₂O   ∆H = −1020 kJ/mol

The negative sign shows heat is released — the combustion is exothermic, as
the rising temperature already told you.
:::

:::key-point
The [[enthalpy-change-of-combustion]] is defined for **one mole** of
substance burned — that is why Step 4 exists. Quoting −17.26 kJ as a final
answer confuses the heat released *in the experiment* with the per-mole
quantity the question asked for.
:::

:::exam-hint
Two technique rules decide whether the arithmetic marks survive to the end.
First, significant figures: quote the final answer to 3 significant figures,
carry more figures through the calculator, and round only at the end — the
least precise piece of experimental data fixes how many figures your answer
can honestly carry. Second, the sign: add it at the ∆H stage and sanity-check
it against the temperature change. Temperature went **up** → exothermic →
∆H **negative**. Temperature down → endothermic → ∆H positive. A
sign-and-trend mismatch means a step has gone wrong.
:::

:::misconception
"Rounding at every step keeps the working tidy." Rounding early compounds:
0.01696 mol rounded to 0.02 mol turns −1017.7 kJ/mol into −863 kJ/mol — off
by more than 150 kJ and outside the mark scheme's tolerance. Keep the
calculator's full display until the final line, then round once.
:::

:::quick-check
Question-bank join: spec 3.3 + 3.4 combustion-calculation items. Redo the
five steps with the burner masses 200.00 g and 199.30 g, the same 100 cm³ of
water warming from 20.0 °C to 54.0 °C, and butan-1-ol (Mr = 74). Check: your
Q = 14 212 J, your n = 0.00946 mol, and your answer near −1500 kJ/mol with
a minus sign.
:::
