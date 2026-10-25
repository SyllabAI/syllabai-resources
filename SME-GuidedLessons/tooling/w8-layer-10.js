#!/usr/bin/env node
// w8-layer-10.js — Activation Energy (rn_y85XYRv5QfgZFQxv, 2521ch, 4CH1-3.14C)
const { buildLayer } = require('./w8-common');

buildLayer('rn_y85XYRv5QfgZFQxv', {
  primer: {
    text: 'From Catalysts you already know that helpers open lower-energy routes through a reaction. This note draws those routes as reaction profiles, adding the peak that particles must clear before any product forms. Reading that peak, and the arrow for the overall change, is the skill this note builds.',
    prerequisiteSubtopic: 'Rates of Reaction',
  },
  lessons: [
    {
      title: 'Reading reaction profiles',
      sourceHeadings: ['Reaction profiles'],
      specRefs: ['4CH1-3.14C'],
      opening: 'A reaction profile is the energy level diagram grown a curve: it follows the energy as bonds strain, peak and settle. This lesson names the two features examiners want labelled, the enthalpy arrow and the energy hurdle.',
      keyPoints: [
        'Reaction profiles show the relative energies of reactants and products and how energy changes as the reaction progresses.',
        'The height difference between reactants and products represents the overall enthalpy change.',
        'For an exothermic reaction the enthalpy value is negative and the arrow points downwards.',
        'For an endothermic reaction the enthalpy value is positive and the arrow points upwards.',
        'The climb from reactants up to the peak of the curve marks the energy needed to start reacting.',
      ],
      depthLayers: {
        low: {
          restatement: 'The profile line starts at the reactants, climbs over a hump and settles at the products. The hump is the energy hurdle for starting, and the height drop or climb from start to finish gives the overall change.',
          analogy: 'It is like a cross-country run: the race starts and finishes at set heights, but the hardest hill in between decides who can even complete the course.',
          examPointer: 'Label both the enthalpy change arrow and the activation energy rise when drawing a profile.',
        },
        medium: {
          restatement: 'A reaction profile traces energy from reactants over a peak to products, with the reactant-to-product gap giving the overall enthalpy change and the reactant-to-peak rise giving the energy hurdle for starting. Downward overall arrows carry negative values for exothermic reactions and upward arrows positive ones for endothermic.',
          analogy: 'A theme-park ride climbs its biggest lift hill before any drops; the lift height is the activation energy and the net height change is the enthalpy change.',
          examPointer: 'Mark Ea from reactants to peak and ΔH from reactants to products, with the sign matching the direction.',
        },
      },
      check: [
        {
          stem: 'What extra feature does a reaction profile show that a simple energy level diagram does not?',
          misconceptionClass: 'diagram comparison',
          options: [
            { key: 'A', text: 'How the energy changes during the course of the reaction', correct: true, explanation: 'The curve between the levels is the added information a profile carries.', misconception: null },
            { key: 'B', text: 'The temperature of the reaction mixture', correct: false, explanation: 'Temperature never appears on energy diagrams.', misconception: 'invented feature' },
            { key: 'C', text: 'The concentration of the reactants', correct: false, explanation: 'Concentration belongs to rate experiments, not profiles.', misconception: 'topic intrusion' },
            { key: 'D', text: 'The time taken for the reaction', correct: false, explanation: 'Profiles show energy against progress, not time.', misconception: 'axis confusion' },
          ],
        },
        {
          stem: 'What does the rise from reactants to the peak of the curve represent?',
          misconceptionClass: 'feature identification',
          options: [
            { key: 'A', text: 'The activation energy required to start the reaction', correct: true, explanation: 'That initial climb is the minimum energy particles need to react.', misconception: null },
            { key: 'B', text: 'The overall enthalpy change', correct: false, explanation: 'The enthalpy change is reactants to products, not to the peak.', misconception: 'features swapped' },
            { key: 'C', text: 'The energy released by the products', correct: false, explanation: 'Release happens on the way down, not on the initial climb.', misconception: 'direction confused' },
            { key: 'D', text: 'The activation energy of the reverse reaction only', correct: false, explanation: 'The forward barrier is the one drawn from the reactant level.', misconception: 'direction misassigned' },
          ],
        },
        {
          stem: 'On an exothermic profile, which way does the enthalpy arrow point and what sign carries?',
          misconceptionClass: 'sign and direction',
          options: [
            { key: 'A', text: 'Downwards with a negative value', correct: true, explanation: 'Products sit lower, so the overall arrow descends and ΔH is negative.', misconception: null },
            { key: 'B', text: 'Upwards with a positive value', correct: false, explanation: 'That is the endothermic profile.', misconception: 'type swapped' },
            { key: 'C', text: 'Downwards with a positive value', correct: false, explanation: 'A downward arrow with a positive sign contradicts itself.', misconception: 'sign mismatched' },
            { key: 'D', text: 'Upwards with a negative value', correct: false, explanation: 'Neither half matches exothermic behaviour.', misconception: 'both wrong' },
          ],
        },
        {
          stem: 'Two reactions share the same enthalpy change but reaction X has a higher peak. What follows?',
          misconceptionClass: 'profile comparison',
          options: [
            { key: 'A', text: 'X needs more energy to get going, so more heat is needed to start it', correct: true, explanation: 'A taller barrier means a harder start even when the overall change matches.', misconception: null },
            { key: 'B', text: 'X releases more energy overall', correct: false, explanation: 'The overall change is stated to be the same.', misconception: 'conflation' },
            { key: 'C', text: 'X must be endothermic and the other exothermic', correct: false, explanation: 'Equal enthalpy changes mean both point the same way.', misconception: 'type invented' },
            { key: 'D', text: 'X has no activation energy', correct: false, explanation: 'Every reaction has some barrier; X\'s is simply taller.', misconception: 'absurd claim' },
          ],
        },
        {
          stem: 'What is the definition of activation energy?',
          misconceptionClass: 'definition recall',
          options: [
            { key: 'A', text: 'The minimum energy that reacting particles must have for a reaction to occur', correct: true, explanation: 'That threshold is exactly what the profile peak measures.', misconception: null },
            { key: 'B', text: 'The total energy stored in all the bonds of the reactants', correct: false, explanation: 'Stored energy is not the threshold concept.', misconception: 'concept swapped' },
            { key: 'C', text: 'The energy released when products form', correct: false, explanation: 'Release belongs to the product side of the profile.', misconception: 'direction inverted' },
            { key: 'D', text: 'The energy needed to raise the temperature by one degree', correct: false, explanation: 'That is specific heat capacity.', misconception: 'term confused' },
          ],
        },
      ],
    },
    {
      title: 'Catalysts drawn onto the profile',
      sourceHeadings: ['Catalysts and reaction profiles'],
      specRefs: ['4CH1-3.14C'],
      opening: 'A catalyst redraws the profile with a second, lower hump while the start and finish stay put. This lesson sketches that overlay and explains why the lower hump means a faster reaction.',
      keyPoints: [
        'Catalysts provide the reactants with an alternative pathway of lower activation energy.',
        'A lower peak means a greater proportion of molecules have sufficient energy for an effective collision.',
        'The catalysed reaction finishes faster than the same reaction without the catalyst.',
        'The reactant and product levels on the profile are unchanged by adding a catalyst.',
        'Reactions with low activation energy occur readily because little energy is needed to begin.',
      ],
      depthLayers: {
        low: {
          restatement: 'Draw the same start and finish, then add a smaller hump labelled as the catalysed route. More particles can clear the smaller hump, so the catalysed reaction runs faster even though the overall change is identical.',
          analogy: 'Two paths over the same hill: the tunnel route needs far less climbing, so more hikers finish per hour.',
          examPointer: 'Show both humps on one diagram and label the lower one as the catalysed pathway.',
        },
        medium: {
          restatement: 'The catalysed profile keeps the original reactant and product levels but offers a lower peak, so a greater proportion of molecules can achieve an effective collision. The catalysed reaction therefore completes faster while the overall enthalpy change stays exactly as before.',
          analogy: 'Adding a chairlift does not move the mountain top, but far more skiers reach it each hour; the mountain is the reaction, the lift is the catalyst.',
          examPointer: 'State that the peak drops, not the levels, and link the drop to a greater proportion of effective collisions.',
        },
      },
      check: [
        {
          stem: 'How does a catalyst appear on a reaction profile?',
          misconceptionClass: 'profile reading',
          options: [
            { key: 'A', text: 'As a second curve with a lower peak between the same reactant and product levels', correct: true, explanation: 'The alternative pathway is drawn lower while the endpoints stay fixed.', misconception: null },
            { key: 'B', text: 'As a deeper valley below the reactant level', correct: false, explanation: 'The route still climbs to a peak; it is just a smaller one.', misconception: 'shape misread' },
            { key: 'C', text: 'As a new product level lower than before', correct: false, explanation: 'Product levels are unchanged by catalysis.', misconception: 'levels shifted' },
            { key: 'D', text: 'As a vertical line at the start', correct: false, explanation: 'Catalysts change the pathway shape, not the axes.', misconception: 'absurd shape' },
          ],
        },
        {
          stem: 'Why does lowering the peak increase the rate?',
          misconceptionClass: 'mechanism link',
          options: [
            { key: 'A', text: 'A greater proportion of molecules now have sufficient energy for an effective collision', correct: true, explanation: 'The smaller hurdle converts average collisions into successful ones.', misconception: null },
            { key: 'B', text: 'Because the molecules themselves become more energetic', correct: false, explanation: 'Molecule energies are unchanged; the requirement drops.', misconception: 'energy myth' },
            { key: 'C', text: 'Because the products are more stable', correct: false, explanation: 'Product stability is identical with or without the catalyst.', misconception: 'stability myth' },
            { key: 'D', text: 'Because the reactant level falls', correct: false, explanation: 'The reactant level never moves.', misconception: 'level myth' },
          ],
        },
        {
          stem: 'What happens to the overall enthalpy change when a catalyst is added?',
          misconceptionClass: 'invariance reasoning',
          options: [
            { key: 'A', text: 'It is unchanged, because the start and finish levels are the same', correct: true, explanation: 'Catalysts alter the route, never the endpoints.', misconception: null },
            { key: 'B', text: 'It becomes more negative', correct: false, explanation: 'The drop between levels is fixed.', misconception: 'sign drift' },
            { key: 'C', text: 'It becomes positive', correct: false, explanation: 'The direction of the overall change is untouched.', misconception: 'sign flip' },
            { key: 'D', text: 'It halves, because the barrier fell', correct: false, explanation: 'Barrier and overall change are different quantities.', misconception: 'conflation' },
          ],
        },
        {
          stem: 'A reaction occurs readily at room temperature. What does its profile look like?',
          misconceptionClass: 'profile inference',
          options: [
            { key: 'A', text: 'It has a low activation peak, so little energy is needed to begin', correct: true, explanation: 'Ready reactions correspond to small barriers.', misconception: null },
            { key: 'B', text: 'It has no peak at all', correct: false, explanation: 'Every reaction has some barrier to clear.', misconception: 'zero-barrier myth' },
            { key: 'C', text: 'It has a very high peak', correct: false, explanation: 'A high peak would make the reaction reluctant, not ready.', misconception: 'inversion' },
            { key: 'D', text: 'Its product level sits above its reactant level', correct: false, explanation: 'Readiness says nothing about the sign of the change.', misconception: 'type conflated' },
          ],
        },
        {
          stem: 'The activation energy for a particular reaction is described as what kind of quantity?',
          misconceptionClass: 'property reasoning',
          options: [
            { key: 'A', text: 'A fixed value for that reaction, unchanged by how fast the reaction is run', correct: true, explanation: 'The barrier is a property of the reaction and its pathway.', misconception: null },
            { key: 'B', text: 'A value that grows as the reaction proceeds', correct: false, explanation: 'The barrier is set by the pathway, not by progress.', misconception: 'growth myth' },
            { key: 'C', text: 'A value that depends on the amount of product formed', correct: false, explanation: 'Yield does not set the barrier.', misconception: 'yield conflated' },
            { key: 'D', text: 'A value that changes with the colour of the mixture', correct: false, explanation: 'Colour has no bearing on the barrier.', misconception: 'absurd link' },
          ],
        },
      ],
    },
  ],
  glossary: [
    { term: 'reaction profile', definition: 'A diagram showing how energy changes as a reaction progresses, including the activation peak.', firstLesson: 1 },
    { term: 'activation energy', definition: 'The minimum energy that reacting particles must have for a reaction to occur.', firstLesson: 1 },
    { term: 'overall enthalpy change', definition: 'The energy difference between reactants and products, drawn as the arrow between the levels.', firstLesson: 1 },
    { term: 'effective collision', definition: 'A collision with enough energy to form products, made more likely by a lower peak.', firstLesson: 2 },
    { term: 'catalysed pathway', definition: 'The lower-energy route through a reaction provided by a catalyst.', firstLesson: 2 },
  ],
  workedExample: null,
});
