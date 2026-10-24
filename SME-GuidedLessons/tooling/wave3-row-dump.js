#!/usr/bin/env node
// wave3-row-dump.js — round data pull (per-round IDs edited in place; latest: W3 notes 11-12, operator trace 1a16f545d13c4ae1).
// 1. Pacing file wavePlan wave-3 rows 11-12 (register cross-check, side A).
// 2. Snapshot rows for the same IDs matched BOTH ways: noteId, title, subtopicTitle,
//    bodyChars, bodySha256 (recomputed from the pinned body), specPointCodes (side B).
// 3. Bodies printed in full for authoring (zero DB - pinned snapshot only).
// 4. Spec texts for 1.37 / 1.38 resolved from the repo content pack (read-only).
const fs = require('fs');
const crypto = require('crypto');

const IDS = ['rn_mbcBZkygY4YpG2bf', 'rn_8Nv33F4dD3kkZnY6'];
const snap = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json', 'utf8'));
const pacing = JSON.parse(fs.readFileSync('/home/z/my-project/download/wave-pacing-open-20261024.json', 'utf8'));

const wave3 = pacing.wavePlan.find(w => w.wave === 3);
console.log('=== pacing file wavePlan wave-3 rows 11-12 (side A) ===');
for (const i of [10, 11]) {
  const r = wave3.register[i];
  console.log(JSON.stringify(r));
}

console.log('\n=== snapshot rows matched BOTH ways (side B) ===');
for (const id of IDS) {
  const row = snap.notes.find(n => n.noteId === id);
  if (!row) { console.log('MISSING IN SNAPSHOT: ' + id); process.exit(1); }
  const sha = crypto.createHash('sha256').update(row.body, 'utf8').digest('hex');
  const meta = { noteId: row.noteId, title: row.title, topicTitle: row.topicTitle, subtopicTitle: row.subtopicTitle, corpusVersion: row.corpusVersion, bodyChars: row.bodyChars, bodySha256: row.bodySha256, shaRecomputed: sha.slice(0, 12), shaMatch: sha === row.bodySha256, specPointCodes: row.specPointCodes, sourceUrl: row.sourceUrl };
  console.log(JSON.stringify(meta));
  console.log('--- body (' + row.body.length + ' ch) ---');
  console.log(row.body);
  console.log('--- end body ---\n');
}

console.log('=== spec texts from content pack (read-only) ===');
const cur = JSON.parse(fs.readFileSync('/home/z/my-project/syllabai-v2/apps/hub/content/igcse-chemistry-19/curriculum.json', 'utf8'));
for (const code of ['4CH1-1.37', '4CH1-1.38']) {
  const n = cur.nodes.find(x => x.code === code);
  console.log(code + ': ' + (n ? JSON.stringify({ title: n.title, description: n.description, parents: n.parents }) : 'NOT FOUND'));
}
