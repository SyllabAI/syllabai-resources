#!/usr/bin/env node
// w10-layer-02.js — Manufacture of Ethanol (rn_ncFJkGhXFsKrkNkH, 2959ch, 4CH1-4.32C + 4.33C)
const { buildLayer } = require('./w10-common');

buildLayer('rn_ncFJkGhXFsKrkNkH', {
  primer: {
    text: "From the previous note you already know the two-carbon alcohol and its eagerness to meet oxygen. This note steps back to ask where industrial ethanol comes from: an oil-derived alkene joined with steam in one route, and living yeast digesting sugar in the other.",
    prerequisiteSubtopic: "Alcohols",
  },
  lessons: [
    {
      title: "Hydration of ethene",
      sourceHeadings: ["Hydration of ethene"],
      specRefs: ["4CH1-4.32C"],
      opening: "Industry builds ethanol from ethene, the short alkene that cracking hands over in bulk. This lesson states the three conditions that switch the reaction on and follows the exit mixture through the condenser, where everything is sorted by boiling point.",
      keyPoints: [
        "The ethene feedstock comes from the cracking of hydrocarbons.",
        "Steam adds across the ethene double bond using a concentrated phosphoric acid catalyst.",
        "The conditions are a temperature of about 300 degrees Celsius and a pressure of 60 to 70 atmospheres.",
        "Unreacted ethene leaves first because it boils at minus 103 degrees, far below the liquids.",
        "The ethanol and water are then separated by fractional distillation.",
      ],
      depthLayers: {
        low: {
          restatement: "Ethene from cracking reacts with steam to make ethanol. Concentrated phosphoric acid catalyses the change at about 300 degrees and 60 to 70 atmospheres, and the leaving mixture is sorted by boiling point.",
          analogy: "The carbon double bond is like an open zip; a water molecule zips straight into the gap, with the acid catalyst acting as the fingers that start the pull.",
          examPointer: "Learn the three conditions as a set; examiners ask for the catalyst, the temperature and the pressure together.",
        },
        medium: {
          restatement: "Hydration adds steam across the ethene double bond using a concentrated phosphoric acid catalyst, a temperature near 300 degrees Celsius and a pressure of 60 to 70 atmospheres. Unreacted ethene, ethanol and water leave the chamber and are separated first by boiling point, then by fractional distillation.",
          analogy: "Picture a sorting office: parcels arrive mixed, the gas exits through the top vent first because it boils coldest, and the two liquids travel on to a second, slower line.",
          examPointer: "Quote the boiling points if asked why ethene separates first: minus 103 against 78 and 100 degrees.",
        },
      },
      check: [
        {
          stem: "Which catalyst does the industrial hydration of ethene use?",
          misconceptionClass: "catalyst recall",
          options: [
            { key: "A", text: "Concentrated phosphoric acid", correct: true, explanation: "Phosphoric acid is the named catalyst for adding steam across the double bond.", misconception: null },
            { key: "B", text: "Concentrated sulfuric acid", correct: false, explanation: "Sulfuric acid appears in other organic reactions; the hydration catalyst is phosphoric.", misconception: "acid swap" },
            { key: "C", text: "Iron filings", correct: false, explanation: "Iron catalyses other industrial processes and plays no part here.", misconception: "metal catalyst guess" },
            { key: "D", text: "Enzymes from yeast", correct: false, explanation: "Enzymes belong to the fermentation route, not to the ethene route.", misconception: "routes crossed" },
          ],
        },
        {
          stem: "Which temperature and pressure does the hydration of ethene need?",
          misconceptionClass: "condition recall",
          options: [
            { key: "A", text: "About 300 degrees Celsius and 60 to 70 atmospheres", correct: true, explanation: "Both figures are stated conditions of the industrial process.", misconception: null },
            { key: "B", text: "About 30 degrees Celsius and normal pressure", correct: false, explanation: "Those are roughly the fermentation conditions applied to the wrong route.", misconception: "route conditions swapped" },
            { key: "C", text: "About 300 degrees Celsius at normal pressure", correct: false, explanation: "The high temperature is right but the pressure must also be raised to 60 to 70 atmospheres.", misconception: "half conditions remembered" },
            { key: "D", text: "Room temperature with a pressure of 60 to 70 atmospheres", correct: false, explanation: "The pressure is right but the reaction also needs the raised temperature.", misconception: "half conditions remembered" },
          ],
        },
        {
          stem: "Where does the ethene for this process come from?",
          misconceptionClass: "feedstock origin",
          options: [
            { key: "A", text: "The cracking of hydrocarbons", correct: true, explanation: "Cracking hands over ethene as a valuable by-product in bulk.", misconception: null },
            { key: "B", text: "The fermentation of glucose", correct: false, explanation: "Fermentation makes ethanol directly and never supplies ethene.", misconception: "product misattributed" },
            { key: "C", text: "Burning ethanol in air", correct: false, explanation: "Burning destroys ethanol into carbon dioxide and water.", misconception: "reverse logic" },
            { key: "D", text: "Distilling sea water", correct: false, explanation: "Water supplies steam for the reaction but no carbon skeleton at all.", misconception: "reactant confused with feedstock" },
          ],
        },
        {
          stem: "When the reaction is complete, how is unreacted ethene removed from the chamber contents?",
          misconceptionClass: "separation logic",
          options: [
            { key: "A", text: "It boils off first because its boiling point is far lower than those of ethanol and water", correct: true, explanation: "At minus 103 degrees the gas leaves long before either liquid vaporises.", misconception: null },
            { key: "B", text: "It is filtered out through paper", correct: false, explanation: "Filtration separates solids from liquids, not gases from liquids.", misconception: "wrong technique" },
            { key: "C", text: "It is neutralised with sodium carbonate solution", correct: false, explanation: "Neutralisation removes acids, and ethene is not an acid.", misconception: "technique mismatch" },
            { key: "D", text: "It is frozen solid at the bottom of the chamber", correct: false, explanation: "Ethene is the coldest-boiling component and leaves as gas, not as a solid.", misconception: "phase invented" },
          ],
        },
        {
          stem: "Which method finally separates the ethanol and water?",
          misconceptionClass: "technique recall",
          options: [
            { key: "A", text: "Fractional distillation", correct: true, explanation: "The two liquids boil at 78 and 100 degrees, so distillation divides them.", misconception: null },
            { key: "B", text: "Filtration", correct: false, explanation: "Both substances are dissolved liquids, so nothing can be caught on a filter.", misconception: "wrong technique" },
            { key: "C", text: "Adding calcium chloride solution", correct: false, explanation: "Calcium chloride removes ethanol as an impurity in a different practical, not here.", misconception: "practical crossed" },
            { key: "D", text: "Decanting", correct: false, explanation: "Ethanol and water mix completely, so no layer forms to pour off.", misconception: "immiscibility assumed" },
          ],
        },
      ],
    },
    {
      title: "Fermentation",
      sourceHeadings: ["Fermentation"],
      specRefs: ["4CH1-4.32C", "4CH1-4.33C"],
      opening: "The second route lets yeast do the work: enzymes inside the cells split glucose into ethanol and carbon dioxide. The recipe is strict about air and gentle with warmth, and this lesson explains exactly why both conditions matter.",
      keyPoints: [
        "Yeast enzymes break dissolved sugar or starch down into ethanol and carbon dioxide.",
        "The equation is written C6H12O6 giving 2CO2 plus 2C2H5OH.",
        "The mixture is kept between 25 and 35 degrees, with 30 degrees as the optimum.",
        "Air is excluded because the yeast must respire without oxygen to make ethanol.",
        "Yeast dies once the alcohol reaches about 15 percent, so the route runs in batches.",
      ],
      depthLayers: {
        low: {
          restatement: "Yeast turns glucose into ethanol and carbon dioxide with no air present, at about 30 degrees. Colder runs too slowly, hotter harms the enzymes, and strong alcohol kills the yeast so the vessel restarts in batches.",
          analogy: "Yeast is a tiny workforce with a strict climate: too cold and they labour slowly, too hot and they quit, and at 15 percent alcohol they drown in their own product.",
          examPointer: "Give the two reasons separately: no air because the process is anaerobic, and about 30 degrees to keep the enzymes working.",
        },
        medium: {
          restatement: "Enzymes in yeast split glucose without oxygen into ethanol and carbon dioxide, written as C6H12O6 giving two carbon dioxides plus two ethanols. Air is shut out so the yeast respires anaerobically, about 30 degrees keeps the enzymes active without harming them, and alcohol near 15 percent kills the yeast to end the batch.",
          analogy: "A brewery vat is a sealed greenhouse for workers who cannot stand a draught: keep the windows shut, hold a mild warmth, and harvest before their own product poisons them.",
          examPointer: "State the optimum as about 30 degrees and explain both tails: too slow below, enzymes damaged above.",
        },
      },
      check: [
        {
          stem: "Why must air be kept out of a fermentation vessel?",
          misconceptionClass: "anaerobic reasoning",
          options: [
            { key: "A", text: "The yeast must respire without oxygen for ethanol to be the product", correct: true, explanation: "Anaerobic respiration of glucose is what delivers ethanol; oxygen would redirect the chemistry.", misconception: null },
            { key: "B", text: "Oxygen would poison the yeast instantly", correct: false, explanation: "Yeast survives oxygen fine; the issue is which products respiration then makes.", misconception: "overstated toxicity" },
            { key: "C", text: "Air would dilute the glucose solution", correct: false, explanation: "Gases bubbling through do not dilute a solution appreciably.", misconception: "dilution excuse" },
            { key: "D", text: "Oxygen would evaporate the ethanol as it formed", correct: false, explanation: "Evaporation depends on temperature, not on the presence of air.", misconception: "wrong mechanism" },
          ],
        },
        {
          stem: "Why is about 30 degrees Celsius the optimum fermentation temperature?",
          misconceptionClass: "optimum temperature reasoning",
          options: [
            { key: "A", text: "Below it the reaction is too slow and above it the enzymes stop working", correct: true, explanation: "Rates fall when cold, and excess heat changes the enzyme shapes that do the catalysing.", misconception: null },
            { key: "B", text: "Yeast only survives at exactly 30 degrees", correct: false, explanation: "The yeast tolerates the 25 to 35 degree band; 30 is simply the best compromise.", misconception: "narrow survival band" },
            { key: "C", text: "Ethanol boils at 30 degrees so higher temperatures lose the product", correct: false, explanation: "Ethanol boils at 78 degrees, well above the fermentation range.", misconception: "boiling point misremembered" },
            { key: "D", text: "Sugar dissolves fastest at exactly 30 degrees", correct: false, explanation: "Dissolving is not the bottleneck; enzyme activity is.", misconception: "dissolution blamed" },
          ],
        },
        {
          stem: "Which equation matches fermentation?",
          misconceptionClass: "equation recall",
          options: [
            { key: "A", text: "C6H12O6 gives 2CO2 plus 2C2H5OH", correct: true, explanation: "One glucose molecule yields two carbon dioxides and two ethanols.", misconception: null },
            { key: "B", text: "C2H5OH + O2 gives CH3COOH + H2O", correct: false, explanation: "That is the oxidation of ethanol, the chemistry of a different note entirely.", misconception: "routes crossed" },
            { key: "C", text: "C6H12O6 + 6O2 gives 6CO2 + 6H2O", correct: false, explanation: "That is aerobic respiration, which releases energy and makes no ethanol.", misconception: "aerobic route chosen" },
            { key: "D", text: "CO2 + H2O gives C6H12O6 + O2", correct: false, explanation: "That is photosynthesis, the reverse direction of carbon fixation.", misconception: "biology crossed" },
          ],
        },
        {
          stem: "Why is fermentation described as a batch process?",
          misconceptionClass: "batch reasoning",
          options: [
            { key: "A", text: "Alcohol near 15 percent kills the yeast, so the vessel must be emptied and restarted", correct: true, explanation: "Each batch ends when the yeast is killed by its own product, and a fresh charge begins.", misconception: null },
            { key: "B", text: "The ethanol is collected one drop at a time", correct: false, explanation: "Collection method is irrelevant; the stopping-and-restarting is what makes it a batch.", misconception: "collection confused" },
            { key: "C", text: "The reaction only runs during daylight hours", correct: false, explanation: "Light plays no part in fermentation chemistry.", misconception: "invented constraint" },
            { key: "D", text: "Each batch requires a different kind of sugar", correct: false, explanation: "The sugar source can stay the same; the yeast dying off forces the restart.", misconception: "wrong cause" },
          ],
        },
        {
          stem: "How is the ethanol and water mixture from fermentation separated?",
          misconceptionClass: "technique recall",
          options: [
            { key: "A", text: "Fractional distillation", correct: true, explanation: "The boiling-point gap between ethanol and water is exploited in the usual way.", misconception: null },
            { key: "B", text: "Filtration through paper", correct: false, explanation: "Nothing solid remains once the yeast has done its work.", misconception: "wrong technique" },
            { key: "C", text: "Adding sodium carbonate until fizzing stops", correct: false, explanation: "That step removes acidic impurities in the ester practical, not ethanol from water.", misconception: "practical crossed" },
            { key: "D", text: "Letting the water evaporate into the air", correct: false, explanation: "Ethanol evaporates faster than water, so waiting loses the product first.", misconception: "volatility reversed" },
          ],
        },
      ],
    },
  ],
  glossary: [
    { term: "hydration", definition: "Adding water across a double bond; ethene plus steam yields ethanol under the industrial conditions.", firstLesson: 1 },
    { term: "fermentation", definition: "The breakdown of glucose by yeast enzymes without oxygen, yielding ethanol and carbon dioxide.", firstLesson: 2 },
    { term: "distillation", definition: "Separating liquids by boiling point and recondensing the vapours; both route mixtures end this way.", firstLesson: 1 },
    { term: "enzyme", definition: "A biological catalyst in yeast that speeds the breakdown of glucose at mild temperatures.", firstLesson: 2 },
    { term: "respiration", definition: "The release of energy from glucose in living cells; yeast carries it out without oxygen here so ethanol forms.", firstLesson: 2 },
    { term: "batch process", definition: "A production method that stops and restarts; fermentation ends when alcohol near 15 percent kills the yeast.", firstLesson: 2 },
  ],
  workedExample: null,
});
