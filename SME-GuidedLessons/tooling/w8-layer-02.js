#!/usr/bin/env node
// w8-layer-02.js — Calorimetry (rn_w25KHshCMNQWwftj, 4590ch, 4CH1-3.2)
const { buildLayer } = require('./w8-common');

buildLayer('rn_w25KHshCMNQWwftj', {
  primer: {
    text: 'From Exothermic & Endothermic you already know that reactions hand heat to their surroundings or take it from them. This note shows how simple calorimetry turns that heat into numbers you can compare, first for reactions mixed in solution and then for burning fuels. It ends with the errors that spoil the measurement and how to shut them down.',
    prerequisiteSubtopic: 'Energetics',
  },
  lessons: [
    {
      title: 'Calorimetry for reactions in solution',
      sourceHeadings: ['Reactions in solution', 'A simple calorimeter'],
      specRefs: ['4CH1-3.2'],
      opening: 'Mixing two solutions and watching the thermometer is the simplest energy measurement in chemistry. This lesson shows the insulated set-up that keeps the heat in and the working assumptions that let the numbers be trusted.',
      keyPoints: [
        'The energy produced by a reaction in solution is found by measuring the temperature change when the solutions are mixed.',
        'The solutions are mixed in an insulated container to prevent heat loss to the surroundings.',
        'Solution calorimetry suits neutralisation reactions, dissolving solids in water and displacement reactions.',
        'A simple calorimeter can be a polystyrene cup, a vacuum flask or a metal can.',
        'Assumptions include a specific heat capacity of 4.18 J/g/°C, a density of 1 g/cm3 and negligible heat losses.',
      ],
      depthLayers: {
        low: {
          restatement: 'To compare energies from solutions, mix them in a cup that keeps heat in and record how much the temperature climbs. The cup, flask or can that holds the mixture is the calorimeter.',
          analogy: 'It is like weighing soup in a vacuum flask so none of the heat leaks out before you measure how warm it got.',
          examPointer: 'Name the insulated container, the thermometer and the stirred mixture when describing this experiment.',
        },
        medium: {
          restatement: 'The temperature change of a mixed solution measures the energy produced, provided the vessel is insulated so heat stays inside. The working assumes the solution behaves like pure water, with a specific heat capacity of 4.18 J/g/°C and a density of 1 g/cm3.',
          analogy: 'A polystyrene cup is the budget version of a laboratory flask: cheap, light and surprisingly good at trapping heat where you want it.',
          examPointer: 'List the assumptions when asked: water-like specific heat capacity and density, container ignored, complete reaction, negligible losses.',
        },
      },
      check: [
        {
          stem: 'Why are the solutions mixed in an insulated container?',
          misconceptionClass: 'experimental design',
          options: [
            { key: 'A', text: 'To prevent heat loss so the temperature change reflects the reaction alone', correct: true, explanation: 'Insulation keeps the released heat inside the vessel, so the thermometer sees the full change.', misconception: null },
            { key: 'B', text: 'To speed up the reaction between the two solutions', correct: false, explanation: 'Insulation changes where the heat goes, not how fast the chemicals react.', misconception: 'rate confused with heat' },
            { key: 'C', text: 'To keep the solutions at a constant temperature', correct: false, explanation: 'The temperature is meant to change; insulation only stops that change leaking away.', misconception: 'constant conditions assumed' },
            { key: 'D', text: 'To stop the solutions mixing too quickly', correct: false, explanation: 'Mixing is required and is helped by stirring, not prevented.', misconception: 'mixing resisted' },
          ],
        },
        {
          stem: 'Which set of reactions can be studied by solution calorimetry of this kind?',
          misconceptionClass: 'method scope',
          options: [
            { key: 'A', text: 'Neutralisation, dissolving and displacement', correct: true, explanation: 'All three happen in solution and release or absorb a measurable amount of heat.', misconception: null },
            { key: 'B', text: 'Combustion, dissolving and neutralisation', correct: false, explanation: 'Combustion needs a burning fuel and a different arrangement with a spirit burner.', misconception: 'combustion misfiled' },
            { key: 'C', text: 'Combustion, displacement and rusting', correct: false, explanation: 'Combustion uses the copper-can method, and rusting is far too slow to measure this way.', misconception: 'scope over-extended' },
            { key: 'D', text: 'Electrolysis, dissolving and neutralisation', correct: false, explanation: 'Electrolysis needs a power supply and is not one of the solution-mixing examples.', misconception: 'electrolysis intruded' },
          ],
        },
        {
          stem: 'In the method, why is an excess of the second reagent added?',
          misconceptionClass: 'procedure reasoning',
          options: [
            { key: 'A', text: 'So that all of the first reagent reacts and the temperature rise reaches its maximum', correct: true, explanation: 'Excess second reagent drives the reaction to completion, giving the largest measurable temperature change.', misconception: null },
            { key: 'B', text: 'To make the solution less dense so it is easier to stir', correct: false, explanation: 'Density is assumed equal to water; stirring is for even mixing, not density control.', misconception: 'density confused' },
            { key: 'C', text: 'To keep the temperature constant during the reaction', correct: false, explanation: 'The temperature is supposed to rise; excess reagent maximises that rise.', misconception: 'constant temperature goal' },
            { key: 'D', text: 'To prevent heat escaping through the cup walls', correct: false, explanation: 'Insulation and a lid slow heat escape; excess reagent has a different job.', misconception: 'insulation conflated' },
          ],
        },
        {
          stem: 'Which assumption lets the calculation treat the solution as if it were pure water?',
          misconceptionClass: 'assumption recall',
          options: [
            { key: 'A', text: 'The solution has the same specific heat capacity and density as water', correct: true, explanation: 'Taking 4.18 J/g/°C and 1 g/cm3 lets the mass heated be read straight from the volume.', misconception: null },
            { key: 'B', text: 'The solution boils at exactly 100 °C', correct: false, explanation: 'Boiling point is not part of the assumption set for these calculations.', misconception: 'irrelevant property' },
            { key: 'C', text: 'The solution is colourless so the thermometer can be read', correct: false, explanation: 'Colour does not enter the calculation at all.', misconception: 'observation confused with calculation' },
            { key: 'D', text: 'The reaction is endothermic in every case', correct: false, explanation: 'The method covers exothermic and endothermic changes alike.', misconception: 'direction assumed' },
          ],
        },
        {
          stem: 'A polystyrene cup, a vacuum flask and a metal can are all acceptable because they all…',
          misconceptionClass: 'apparatus function',
          options: [
            { key: 'A', text: 'act as the calorimeter holding the reacting mixture', correct: true, explanation: 'Each vessel can serve as the insulated container whose contents are measured.', misconception: null },
            { key: 'B', text: 'measure the temperature directly', correct: false, explanation: 'The thermometer measures temperature; the vessel just holds the mixture.', misconception: 'apparatus roles swapped' },
            { key: 'C', text: 'burn the fuel cleanly', correct: false, explanation: 'Burning belongs to the combustion experiment with a spirit burner, not to solution mixing.', misconception: 'methods merged' },
            { key: 'D', text: 'stop the reaction from completing', correct: false, explanation: 'The assumption list says the reaction is complete; the vessel does not hinder it.', misconception: 'purpose inverted' },
          ],
        },
      ],
    },
    {
      title: 'Burning fuels and the errors that follow',
      sourceHeadings: ['Enthalpy of combustion experiments', 'Sources of error'],
      specRefs: ['4CH1-3.2'],
      opening: 'Burning a fuel under a known mass of water turns the flame into a heater you can score. This lesson walks the copper-can experiment step by step, then faces the two errors that always lurk in it.',
      keyPoints: [
        'Combustion calorimetry uses the heat released by a burning fuel to raise the heat content of water.',
        'A fixed volume of water is heated in a copper can while a spirit burner with the fuel is weighed before and after.',
        'The flame is extinguished once the water has risen by about 20 °C and the final temperature is recorded.',
        'The main sources of error are heat losses and incomplete combustion of the fuel.',
        'A lid over the calorimeter and shielding from draughts reduce the heat lost to the surroundings.',
      ],
      depthLayers: {
        low: {
          restatement: 'Burn a weighed burner under a can of water, then weigh it again; the mass lost is the fuel burned and the thermometer shows the warmth gained. Heat escapes and fuel burns poorly, and both spoil the answer.',
          analogy: 'It is like boiling a kettle in a draughty doorway: some heat never reaches the water, exactly as some flame heat never reaches the can.',
          examPointer: 'Name heat losses and incomplete combustion as the errors, with a lid and shielding as the fixes.',
        },
        medium: {
          restatement: 'The burning fuel transfers heat to water in a copper can, and weighing the spirit burner before and after shows how much fuel was consumed. Heat lost to the surroundings and heat absorbed by the calorimeter are the main errors, reduced by a lid and by shielding the flame from draughts.',
          analogy: 'A windbreak behind a camp stove keeps the flame working on the pan instead of the breeze, just as shielding keeps the flame heating the can.',
          examPointer: 'Describe the full sequence, including the 20 °C target rise and the re-weighing, and finish with the two named errors.',
        },
      },
      check: [
        {
          stem: 'Why is the spirit burner weighed before and after the experiment?',
          misconceptionClass: 'procedure purpose',
          options: [
            { key: 'A', text: 'To find the mass of fuel burned during the temperature rise', correct: true, explanation: 'The mass lost by the burner is the fuel consumed, which pairs the energy change with the amount of fuel.', misconception: null },
            { key: 'B', text: 'To check the balance is working correctly', correct: false, explanation: 'The balance is assumed fine; the two weighings measure fuel used.', misconception: 'calibration confusion' },
            { key: 'C', text: 'To measure the temperature of the flame', correct: false, explanation: 'A balance cannot read temperature; the thermometer does that.', misconception: 'apparatus roles swapped' },
            { key: 'D', text: 'To confirm the wick stayed dry throughout', correct: false, explanation: 'Wick condition is not the target measurement; fuel mass is.', misconception: 'irrelevant detail' },
          ],
        },
        {
          stem: 'Why is the flame extinguished after the temperature has risen by roughly 20 °C?',
          misconceptionClass: 'procedure reasoning',
          options: [
            { key: 'A', text: 'To give a measurable rise while keeping heat losses and fuel use under control', correct: true, explanation: 'A rise of about 20 °C is large enough to read accurately yet short enough to limit uncontrolled losses.', misconception: null },
            { key: 'B', text: 'Because water cannot be heated by more than 20 °C', correct: false, explanation: 'Water can heat further; the value is a working choice, not a physical limit.', misconception: 'false physical limit' },
            { key: 'C', text: 'Because the spirit burner stops working above that temperature', correct: false, explanation: 'The burner could keep burning; the stop is deliberate.', misconception: 'apparatus limit invented' },
            { key: 'D', text: 'To make sure the fuel is all used up', correct: false, explanation: 'The burner must still hold fuel for the final weighing to show the mass burned.', misconception: 'completion misread' },
          ],
        },
        {
          stem: 'Which pair names the main sources of error in the combustion experiment?',
          misconceptionClass: 'error identification',
          options: [
            { key: 'A', text: 'Heat losses and incomplete combustion', correct: true, explanation: 'Heat escapes to the surroundings and some fuel burns incompletely, both shrinking the measured effect.', misconception: null },
            { key: 'B', text: 'Heat gains and complete combustion', correct: false, explanation: 'Complete combustion is the ideal, not an error; gains are not the named problem.', misconception: 'error inverted' },
            { key: 'C', text: 'Thermometer drift and balance drift', correct: false, explanation: 'Instrument drift is not one of the two named errors for this experiment.', misconception: 'wrong error family' },
            { key: 'D', text: 'Water evaporating and the can rusting', correct: false, explanation: 'Neither evaporation nor rust is the named error pair.', misconception: 'invented errors' },
          ],
        },
        {
          stem: 'How does a lid reduce the error in the measured energy change?',
          misconceptionClass: 'error mitigation',
          options: [
            { key: 'A', text: 'It prevents heat escaping from the water surface into the air', correct: true, explanation: 'A lid sits over the calorimeter so rising warm water loses less heat to the air above.', misconception: null },
            { key: 'B', text: 'It raises the flame temperature of the burner', correct: false, explanation: 'The lid does not touch the flame; it caps the can.', misconception: 'flame interaction invented' },
            { key: 'C', text: 'It stops the water from evaporating completely', correct: false, explanation: 'Evaporation control is incidental; the named purpose is heat loss.', misconception: 'secondary effect chosen' },
            { key: 'D', text: 'It makes the combustion reaction complete', correct: false, explanation: 'Completeness of burning depends on oxygen supply at the wick, not on the lid over the water.', misconception: 'fix over-credited' },
          ],
        },
        {
          stem: 'Not all the heat from the burning fuel reaches the water. Where does the rest go?',
          misconceptionClass: 'energy accounting',
          options: [
            { key: 'A', text: 'Some is lost to the surroundings and some is absorbed by the calorimeter', correct: true, explanation: 'Those two sinks are the named destinations for the missing heat.', misconception: null },
            { key: 'B', text: 'It is destroyed inside the flame', correct: false, explanation: 'Energy is conserved; it spreads to other places instead of vanishing.', misconception: 'energy destroyed' },
            { key: 'C', text: 'It turns the fuel into a denser liquid', correct: false, explanation: 'Density changes of the fuel are not part of the heat account.', misconception: 'invented sink' },
            { key: 'D', text: 'It stays in the wick forever', correct: false, explanation: 'The wick is not a named heat sink in this experiment.', misconception: 'invented sink' },
          ],
        },
      ],
    },
  ],
  glossary: [
    { term: 'calorimeter', definition: 'An insulated container, such as a polystyrene cup, vacuum flask or metal can, used to measure heat changes in a reaction.', firstLesson: 1 },
    { term: 'neutralisation', definition: 'The reaction between an acid and an alkali that always gives energy out to the surroundings.', firstLesson: 1 },
    { term: 'specific heat capacity', definition: 'The energy needed to raise the temperature of 1 g of a substance by 1 °C; for water it is 4.18 J/g/°C.', firstLesson: 1 },
    { term: 'spirit burner', definition: 'A small burner holding a liquid fuel, weighed before and after burning to find the mass of fuel consumed.', firstLesson: 2 },
    { term: 'incomplete combustion', definition: 'Burning that does not convert all of the fuel into the usual products, wasting some of the available energy.', firstLesson: 2 },
  ],
  workedExample: null,
});
