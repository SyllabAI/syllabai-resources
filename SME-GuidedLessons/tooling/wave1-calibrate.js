#!/usr/bin/env node
// wave1-calibrate.js — calibration of the re-derived toolchain against the A1 spec's own
// section-5 exemplar. Builds a single-lesson layer (The Structure of the Atom, spec 4CH1-1.15)
// from the verbatim spec text, validates it against guided-lesson/0.1 (ajv draft-07), then
// runs the re-derived lint in --codes calibration scope. Expected: schema PASS, 0 hard-fails,
// 0 warnings — spec-conformant content must lint clean; any firing rule is a miscalibrated
// heuristic to fix, not a content problem.
// This fixture is a calibration artifact, NOT the lost A1 layer JSON of record.
const fs = require('fs');
const path = require('path');
const Ajv = require('/home/z/node_modules/ajv');
const { execFileSync } = require('child_process');

const W = '/home/z/my-project/.tmp/wave1';
const snap = JSON.parse(fs.readFileSync(path.join(W, 'corpus-snapshot.json'), 'utf8'));
const specTexts = JSON.parse(fs.readFileSync(path.join(W, 'spec-point-texts.json'), 'utf8'));
const row = snap.notes.find(n => n.noteId === 'rn_kb2VkFMdBTbmG33t');
const spText = code => specTexts.nodes.find(n => n.code === code).title;

const fixture = {
  format: 'guided-lesson/0.1',
  noteRef: {
    noteId: row.noteId,
    corpusVersion: row.corpusVersion,
    topicTitle: row.topicTitle,
    subtopicTitle: row.subtopicTitle,
    sourceUrl: row.sourceUrl,
  },
  specPoints: [{ code: '4CH1-1.15', text: spText('4CH1-1.15') }],
  primer: {
    text: 'Before starting this lesson you should already know that all substances are made of particles, that an element contains only one kind of atom, and that a compound joins atoms of different elements together. You met these ideas in Elements, Compounds & Mixtures, along with the difference between mixtures and compounds. If any of those terms feel shaky, revisit that subtopic first, because this lesson builds directly on it.',
    prerequisiteSubtopic: 'Elements, Compounds & Mixtures',
  },
  lessons: [{
    title: 'The Structure of the Atom',
    sourceHeadings: ['The Structure of the Atom', 'Atomic structure'],
    specRefs: ['4CH1-1.15'],
    opening: 'Every substance around you is built from atoms, and atoms are themselves built from even smaller parts. This lesson covers what those parts are, where each one sits, and why almost all of an atom\u2019s mass is packed into its centre. By the end you should be able to state the relative masses and charges of the three sub-atomic particles without your notes.',
    keyPoints: [
      'An atom contains three kinds of sub-atomic particle: protons, neutrons and electrons.',
      'Protons and neutrons sit in the nucleus at the centre of the atom, and the nucleus is positively charged.',
      'Electrons move very fast around the nucleus in orbital paths called shells.',
      'A proton and a neutron each have relative mass 1, while an electron\u2019s mass of about 1/1840 is treated as negligible.',
      'Because the electron\u2019s mass is negligible, effectively all of an atom\u2019s mass is contained in its nucleus.',
    ],
    confidenceGate: {
      ratings: ['low', 'medium', 'high'],
      continueDisabledUntilChoice: true,
      resumeWithoutReRate: true,
      postCheckRecalibration: true,
    },
    depthLayers: {
      low: {
        restatement: 'An atom has a tiny heavy centre and a light outer region.',
        analogy: 'Think of a stadium: the nucleus is a handful of coins on the centre spot, and the electrons are dust specks racing around the stands. The coins carry nearly all the weight; the dust barely registers.',
        examPointer: 'In an exam, say that the mass of an electron is negligible or very small. You are not expected to recall 1/1840, and the note\u2019s exam hint says exactly this.',
      },
      medium: {
        restatement: 'An atom consists of a nucleus surrounded by electrons in shells. The nucleus holds protons, with relative mass 1 and charge +1, and neutrons, with relative mass 1 and charge 0; electrons carry charge -1 and occupy the shells, with relative mass about 1/1840.',
        analogy: 'The word relative matters: these values are comparisons between particles, not measurements in grams or coulombs, because sub-atomic particles are far too small for conventional units.',
        examPointer: 'Since proton and neutron masses dominate, the mass of the atom is concentrated in the nucleus, which is also why the nucleus\u2019s positive charge is what defines the element.',
      },
    },
    check: [{
      stem: 'Most of the mass of an atom is located in...',
      misconceptionClass: 'mass spread evenly across particles',
      options: [
        { key: 'A', text: 'the shells, where the electrons move', correct: false, explanation: 'The shells hold only electrons, whose mass of about 1/1840 is negligible, so the shells contain almost none of the atom\u2019s mass.', misconception: 'electron mass treated as significant' },
        { key: 'B', text: 'the nucleus, which holds protons and neutrons', correct: true, explanation: 'Protons and neutrons each have relative mass 1 and both sit in the nucleus, while the electron\u2019s mass is negligible, so effectively all the mass is at the centre.', misconception: null },
        { key: 'C', text: 'shared evenly between protons, neutrons and electrons', correct: false, explanation: 'Electrons are about 2000 times lighter than protons and neutrons, so the mass is not shared evenly.', misconception: 'the phrase relative mass read as equal mass' },
        { key: 'D', text: 'the electron orbits considered as a whole', correct: false, explanation: 'Shells are paths electrons move along, not a store of mass; there is no separate orbit material.', misconception: 'orbits imagined as physical structures' },
      ],
    }],
  }],
  noteAssets: {
    glossary: [
      { term: 'nucleus', definition: 'The positively charged centre of an atom where the protons and neutrons are located.', firstLesson: 1 },
      { term: 'shell', definition: 'An orbital path around the nucleus in which electrons move.', firstLesson: 1 },
      { term: 'relative mass', definition: 'A particle\u2019s mass expressed as a comparison with other particles rather than in absolute units.', firstLesson: 1 },
      { term: 'negligible', definition: 'So small it can be ignored; the conventional way to describe the electron\u2019s mass.', firstLesson: 1 },
    ],
    workedExample: {
      prompt: 'Determine the number of protons, electrons and neutrons in an atom of element X with atomic number 29 and mass number 63.',
      steps: [
        'The number of protons of element X is the same as the atomic number, so the number of protons = 29.',
        'The number of protons is always equal to the number of electrons, so the number of electrons = 29.',
        'The number of neutrons is the mass number minus the atomic number: 63 - 29 = 34.',
      ],
      finalAnswer: 'Element X has 29 protons, 29 electrons and 34 neutrons.',
    },
  },
};

const OUT = path.join(W, 'calibration-fixture.json');
fs.writeFileSync(OUT, JSON.stringify(fixture, null, 1));

// 1. schema validation (ajv draft-07)
const schema = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/guided-lesson.0.1.schema.json', 'utf8'));
const ajv = new Ajv({ allErrors: true, strict: false });
const validate = ajv.compile(schema);
const ok = validate(fixture);
console.log('SCHEMA:', ok ? 'PASS' : 'FAIL');
if (!ok) console.log(JSON.stringify(validate.errors, null, 1));

// 2. lint in calibration scope
console.log('---');
try {
  const out = execFileSync('node', ['/home/z/my-project/scripts/a1-lint.js', OUT,
    '--note', 'rn_kb2VkFMdBTbmG33t', '--codes', '4CH1-1.15'], { encoding: 'utf8' });
  console.log(out);
  console.log('CALIBRATION: lint exit 0');
} catch (e) {
  console.log(e.stdout);
  console.log('CALIBRATION: lint exit ' + e.status);
}
