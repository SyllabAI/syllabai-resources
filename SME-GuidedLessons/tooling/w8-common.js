#!/usr/bin/env node
// w8-common.js — shared assembler for wave-8 layer builders. Fills noteRef + specPoints
// from the snapshot of record and the prepared register (zero-DB), applies the standard
// confidence gate, and writes the layer JSON. Per-note content lives in w8-layer-NN.js.
const fs = require('fs');
const SNAP = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json', 'utf8'));
const REG = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave8/wave8-register.json', 'utf8'));

const GATE = {
  ratings: ['low', 'medium', 'high'],
  continueDisabledUntilChoice: true,
  resumeWithoutReRate: true,
  postCheckRecalibration: true,
};

function buildLayer(noteId, content) {
  const row = SNAP.notes.find(n => n.noteId === noteId);
  if (!row) throw new Error('note not in snapshot: ' + noteId);
  const regRow = REG.register.find(r => r.noteId === noteId);
  const specPoints = regRow.specPointCodes.map(code => ({ code, text: REG.specTexts[code] }));
  const layer = {
    format: 'guided-lesson/0.1',
    noteRef: {
      noteId: row.noteId,
      corpusVersion: row.corpusVersion,
      topicTitle: row.topicTitle,
      subtopicTitle: row.subtopicTitle,
      sourceUrl: row.sourceUrl,
    },
    specPoints,
    primer: content.primer,
    lessons: content.lessons.map(L => ({
      title: L.title,
      sourceHeadings: L.sourceHeadings,
      specRefs: L.specRefs,
      opening: L.opening,
      keyPoints: L.keyPoints,
      confidenceGate: GATE,
      depthLayers: L.depthLayers,
      check: L.check,
    })),
    noteAssets: {
      glossary: content.glossary,
      workedExample: content.workedExample === undefined ? null : content.workedExample,
    },
  };
  const out = `/home/z/my-project/.tmp/wave8/layer-${noteId}.json`;
  fs.writeFileSync(out, JSON.stringify(layer, null, 1));
  console.log(`WROTE ${out} (${layer.lessons.length} lessons, ${layer.lessons.reduce((a, l) => a + l.check.length, 0)} checks, we=${layer.noteAssets.workedExample === null ? 'null' : 'port'})`);
  return layer;
}

module.exports = { buildLayer, SNAP, REG };
