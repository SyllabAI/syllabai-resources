#!/usr/bin/env node
// w8-layer-01.js — Exothermic & Endothermic (rn_x5m8QBWxtKvxQ9sx, 3442ch, 4CH1-3.1)
const { buildLayer } = require('./w8-common');

buildLayer('rn_x5m8QBWxtKvxQ9sx', {
  primer: {
    text: 'From Gases in the Atmosphere you already know that burning fuels pours heat into the air. This note sorts chemical reactions into those that give heat out and those that take heat in, and shows how a thermometer tells them apart. It closes with the energy bookkeeping rule that makes every temperature reading meaningful.',
    prerequisiteSubtopic: 'Gases in the Atmosphere',
  },
  lessons: [
    {
      title: 'Spotting exothermic and endothermic changes',
      sourceHeadings: ['Exothermic and endothermic reactions', 'Exothermic reactions'],
      specRefs: ['4CH1-3.1'],
      opening: 'Every reaction either warms or cools its surroundings, and a thermometer reveals which of the two is happening. This lesson builds the two labels chemists use and ties each label to the temperature direction you observe.',
      keyPoints: [
        'Exothermic reactions give heat energy out to the surroundings, raising the temperature of the reaction mixture.',
        'Endothermic reactions take heat in from the surroundings, so the temperature of the reaction mixture falls.',
        'Neutralisation and combustion always give energy out, while displacement reactions can transfer energy either way.',
        'A thermometer measures the heat change, so it reveals whether a reaction is exothermic or endothermic.',
        'Energy is conserved in reactions, so the products end up with less energy than the reactants when heat is released.',
      ],
      depthLayers: {
        low: {
          restatement: 'Some reactions warm things up and some cool them down. A reaction that hands heat to the surroundings is exothermic; one that takes heat from the surroundings is endothermic.',
          analogy: 'A bonfire warms everyone standing near it, while an ice pack soaks up heat from a bruised knee; the fire behaves like the first kind of reaction and the pack like the second.',
          examPointer: 'If asked to identify a reaction type, quote the thermometer direction: temperature up means exothermic, temperature down means endothermic.',
        },
        medium: {
          restatement: 'Exothermic reactions transfer heat to the surroundings, so the reaction mixture and everything around it grow warmer. Endothermic reactions draw heat in from the surroundings, leaving the mixture and its surroundings cooler.',
          analogy: 'A bonfire warms the crowd gathered round it, while a cold pack draws heat out of a sports injury; one hands energy over and the other soaks it up.',
          examPointer: 'Quote the temperature direction from the data, then name the reaction type and justify it by the heat taken in or given out.',
        },
      },
      check: [
        {
          stem: 'A reaction mixture warms from 19 °C to 21 °C as chemicals react. What does this show?',
          misconceptionClass: 'temperature-direction reasoning',
          options: [
            { key: 'A', text: 'The reaction is exothermic because heat was given out to the surroundings', correct: true, explanation: 'A temperature rise means heat left the chemicals and warmed everything around them, which is the signature of an exothermic change.', misconception: null },
            { key: 'B', text: 'The reaction is endothermic because the mixture absorbed heat', correct: false, explanation: 'Endothermic changes take heat in and would cool the mixture; the reading rose instead of falling.', misconception: 'temperature direction reversed' },
            { key: 'C', text: 'The reaction released no energy because the chemicals stayed liquid', correct: false, explanation: 'Physical state does not decide heat flow; the measured temperature rise does.', misconception: 'state-change confusion' },
            { key: 'D', text: 'The thermometer manufactured the extra heat', correct: false, explanation: 'The thermometer records the temperature; the reaction supplies the heat it reports.', misconception: 'apparatus blamed' },
          ],
        },
        {
          stem: 'Which set of reaction types always gives energy out?',
          misconceptionClass: 'classification recall',
          options: [
            { key: 'A', text: 'Neutralisation and combustion', correct: true, explanation: 'Both reaction types always release heat to the surroundings.', misconception: null },
            { key: 'B', text: 'Displacement and combustion', correct: false, explanation: 'Displacement reactions can take energy in or give it out, so they do not always release heat.', misconception: 'displacement assumed always exothermic' },
            { key: 'C', text: 'Displacement and neutralisation', correct: false, explanation: 'Neutralisation does release heat, but displacement can run in either energy direction.', misconception: 'displacement mis-typed' },
            { key: 'D', text: 'Endothermic and combustion', correct: false, explanation: 'Endothermic reactions take heat in, so the pairing cannot be correct.', misconception: 'category inverted' },
          ],
        },
        {
          stem: 'Why does the temperature of the surroundings rise during an exothermic reaction?',
          misconceptionClass: 'energy transfer logic',
          options: [
            { key: 'A', text: 'Heat released by the reaction flows into the surroundings', correct: true, explanation: 'Energy given out by the chemicals has nowhere to go except the surroundings, warming them.', misconception: null },
            { key: 'B', text: 'The surroundings supply the energy for the reaction', correct: false, explanation: 'That describes an endothermic change; exothermic reactions hand energy over instead.', misconception: 'direction inverted' },
            { key: 'C', text: 'The reaction destroys energy so none remains in the chemicals', correct: false, explanation: 'Energy is conserved; it is transferred, never destroyed.', misconception: 'energy destroyed' },
            { key: 'D', text: 'The products store the released heat permanently', correct: false, explanation: 'The heat passes to the surroundings; the products end with less energy than the reactants.', misconception: 'products as heat store' },
          ],
        },
        {
          stem: 'In an endothermic reaction, what happens to the energy of the system?',
          misconceptionClass: 'system-energy bookkeeping',
          options: [
            { key: 'A', text: 'It increases because heat is taken in from the surroundings', correct: true, explanation: 'Energy absorbed from the surroundings raises the heat content of the system.', misconception: null },
            { key: 'B', text: 'It decreases because energy leaves the system', correct: false, explanation: 'An endothermic change pulls energy in; a falling energy content describes exothermic reactions.', misconception: 'exo and endo swapped' },
            { key: 'C', text: 'It stays exactly the same throughout the change', correct: false, explanation: 'Total energy is conserved, but the share held by the system changes when heat crosses the boundary.', misconception: 'conservation misapplied' },
            { key: 'D', text: 'It becomes impossible to measure with school apparatus', correct: false, explanation: 'A thermometer in the mixture tracks the change directly.', misconception: 'measurement despair' },
          ],
        },
        {
          stem: 'The products of a reaction have less energy than the reactants. Which conclusion follows?',
          misconceptionClass: 'energy-level inference',
          options: [
            { key: 'A', text: 'The reaction was exothermic and heat was transferred to the surroundings', correct: true, explanation: 'A lower product energy means energy left the chemicals as heat.', misconception: null },
            { key: 'B', text: 'The reaction was endothermic and heat entered the chemicals', correct: false, explanation: 'Heat entering would leave the products with more energy, not less.', misconception: 'sign inverted' },
            { key: 'C', text: 'Energy was created inside the reaction mixture', correct: false, explanation: 'Energy is never created; the drop matches the heat handed over to the surroundings.', misconception: 'energy created' },
            { key: 'D', text: 'No energy conclusion can be drawn from energy levels', correct: false, explanation: 'The energy difference is exactly the evidence needed to classify the reaction.', misconception: 'inference refused' },
          ],
        },
      ],
    },
    {
      title: 'The energy account behind each reaction type',
      sourceHeadings: ['Endothermic reactions', 'Exothermic & Endothermic'],
      specRefs: ['4CH1-3.1'],
      opening: 'Because energy cannot be created or destroyed, every heating or cooling you measure has to come from somewhere or go somewhere. This lesson follows the energy account that sits behind each reaction type.',
      keyPoints: [
        'The law of conservation of energy says energy cannot be created or destroyed, only transferred.',
        'When energy moves to the surroundings, the products must hold less energy than the reactants by that amount.',
        'Examples of exothermic reactions include neutralisation and combustion, which always give energy out.',
        'The heat content of the system falls in exothermic reactions and rises in endothermic ones.',
        'Temperature changes recorded in a table of results classify each reaction as exothermic or endothermic.',
      ],
      depthLayers: {
        low: {
          restatement: 'Energy keeps a fixed total, so heat that appears or disappears must come from the chemicals or go to them. Warming reactions empty energy into the surroundings; cooling ones pull it in.',
          analogy: 'Picture a bank account: money handed to the street lowers your balance, and money collected raises it, just as heat leaves or fills the chemicals.',
          examPointer: 'Explain reaction types by tracking energy: released means the products end lower, absorbed means they end higher.',
        },
        medium: {
          restatement: 'Energy is conserved in every reaction, so any heat you measure must equal the energy change of the chemicals themselves. Exothermic reactions leave the system holding less energy; endothermic reactions leave it holding more.',
          analogy: 'A bank transfer moves money without creating it; the two balances change by matching amounts, like the chemicals and the surroundings exchanging heat.',
          examPointer: 'Link the thermometer direction to the energy ledger: temperature rise means the system lost energy, temperature fall means it gained.',
        },
      },
      check: [
        {
          stem: 'A student claims energy was destroyed in a reaction that cooled. What is the correct response?',
          misconceptionClass: 'conservation reasoning',
          options: [
            { key: 'A', text: 'Energy was transferred to the surroundings, not destroyed', correct: true, explanation: 'The law of conservation of energy forbids destruction; the heat simply moved out of the mixture.', misconception: null },
            { key: 'B', text: 'Energy was destroyed because the temperature fell', correct: false, explanation: 'A falling temperature signals heat leaving, not energy vanishing.', misconception: 'destruction accepted' },
            { key: 'C', text: 'Energy was created inside the thermometer bulb', correct: false, explanation: 'The thermometer only reports temperature; it does not manufacture energy.', misconception: 'creation claimed' },
            { key: 'D', text: 'The law of conservation of energy does not apply to chemical reactions', correct: false, explanation: 'The law applies to every reaction; energy changes location but persists.', misconception: 'law scope error' },
          ],
        },
        {
          stem: 'Why do the products of an exothermic reaction hold less energy than the reactants?',
          misconceptionClass: 'energy account reasoning',
          options: [
            { key: 'A', text: 'The missing energy was released to the surroundings as heat', correct: true, explanation: 'Conservation requires the energy difference to appear somewhere, and it leaves as heat.', misconception: null },
            { key: 'B', text: 'The products are always colder, so they store less', correct: false, explanation: 'Temperature is a reading, not the energy ledger; the difference is the transferred heat.', misconception: 'temperature equated to energy' },
            { key: 'C', text: 'Some energy was destroyed while bonds rearranged', correct: false, explanation: 'No energy disappears; it is transferred to the surroundings.', misconception: 'destruction claimed' },
            { key: 'D', text: 'The products gained energy from the surroundings', correct: false, explanation: 'Gaining energy would make the products richer in energy, the opposite of the observation.', misconception: 'direction inverted' },
          ],
        },
        {
          stem: 'Which pairing of reaction type and energy direction is correct?',
          misconceptionClass: 'pairing logic',
          options: [
            { key: 'A', text: 'Combustion gives energy out; displacement may give energy out or take it in', correct: true, explanation: 'Combustion always releases heat, while displacement appears in both directions in the list of heat changes.', misconception: null },
            { key: 'B', text: 'Combustion takes energy in; neutralisation gives it out', correct: false, explanation: 'Combustion always gives energy out; only the second half of the pairing is right.', misconception: 'combustion inverted' },
            { key: 'C', text: 'Neutralisation takes energy in; combustion takes it in', correct: false, explanation: 'Both named types give energy out.', misconception: 'both inverted' },
            { key: 'D', text: 'Displacement always takes energy in; combustion gives it out', correct: false, explanation: 'Displacement can run either way, so the word always makes the claim wrong.', misconception: 'displacement fixed' },
          ],
        },
        {
          stem: 'A table shows four experiments; one mixture cools while three warm. What classifies the cooling one?',
          misconceptionClass: 'data interpretation',
          options: [
            { key: 'A', text: 'Endothermic, because its temperature fell as heat was taken in', correct: true, explanation: 'A temperature drop marks heat flowing from the surroundings into the mixture.', misconception: null },
            { key: 'B', text: 'Exothermic, because most reactions are exothermic', correct: false, explanation: 'Classification follows the measured direction, not the frequency of reaction types.', misconception: 'majority voting' },
            { key: 'C', text: 'Impossible to classify without a balanced equation', correct: false, explanation: 'The temperature change alone classifies the reaction.', misconception: 'equation demanded' },
            { key: 'D', text: 'Endothermic, because one chemical in it is a weak acid', correct: false, explanation: 'The classification rests on the observed temperature fall, not on the identity of a single chemical.', misconception: 'chemical stereotyping' },
          ],
        },
        {
          stem: 'Where does the energy transferred in a reaction end up if the mixture warms?',
          misconceptionClass: 'location of transfer',
          options: [
            { key: 'A', text: 'In the surroundings, including the thermometer and the air around the cup', correct: true, explanation: 'The heat spreads to everything touching the mixture, which is what the thermometer detects.', misconception: null },
            { key: 'B', text: 'Nowhere, because the reaction consumed it', correct: false, explanation: 'Energy is conserved; the warming shows it moved to the surroundings.', misconception: 'consumption claimed' },
            { key: 'C', text: 'In the reactants, which store extra energy afterwards', correct: false, explanation: 'The reactants are spent; the products hold less energy than they did.', misconception: 'reactants enriched' },
            { key: 'D', text: 'Only in the products, which stay hot forever', correct: false, explanation: 'The products share their energy with the surroundings as the mixture cools.', misconception: 'products hoard heat' },
          ],
        },
      ],
    },
  ],
  glossary: [
    { term: 'exothermic reaction', definition: 'A reaction that releases heat energy into the surroundings, raising the temperature of the reaction mixture.', firstLesson: 1 },
    { term: 'endothermic reaction', definition: 'A reaction that takes heat energy in from the surroundings, lowering the temperature of the reaction mixture.', firstLesson: 1 },
    { term: 'surroundings', definition: 'Everything outside the chemicals that are reacting, including the air, the container and the thermometer.', firstLesson: 1 },
    { term: 'law of conservation of energy', definition: 'The rule that energy cannot be created or destroyed, only transferred between the system and its surroundings.', firstLesson: 2 },
    { term: 'displacement reaction', definition: 'A reaction in which one element takes the place of another in a compound; it can give energy out or take it in.', firstLesson: 2 },
  ],
  workedExample: null,
});
