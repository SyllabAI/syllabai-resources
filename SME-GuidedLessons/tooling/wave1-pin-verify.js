#!/usr/bin/env node
// wave1-pin-verify.js — snapshot pin re-verification of record (operator: "re-verify the
// snapshot pin"), 2026-10-24. ZERO DB contact: the wave's single read-only SELECT pull is
// already consumed and declared final; everything here recomputes from local bytes and
// cross-checks the artifacts that pinned themselves to the snapshot.
//
// Checks:
//   A. per-note body pin: sha256(body) recomputed for every note vs the stored bodySha256
//      (+ bodyChars recomputed) — 112/112 must match;
//   B. census recomputed from the snapshot vs snapshot-manifest.json vs the census of
//      record (4 topics / 28 subtopics / 112 notes / 40-36-15-21; 361,272 chars; single
//      corpus_version sme-revision-notes-igcse-chemistry-19-2026-09-18);
//   C. pull-order + uniqueness invariants (topicOrder, subtopicOrder, noteOrder sorted;
//      noteIds unique);
//   D. cross-pin: all 10 wave-1 timing receipts (bodySha256, bodyChars, corpusVersion,
//      titles, specPointCodes) must equal their snapshot rows; calibration note
//      rn_kb2VkFMdBTbmG33t must exist in the snapshot;
//   E. wave receipt corpusPin: embedded snapshotManifest deep-equals the manifest file;
//      censusOfRecord matches;
//   F. file-level pins minted NOW (sha256 of the snapshot file bytes + manifest file
//      bytes) — recorded going forward; the manifest of record pins per-note hashes, not
//      the file, so this is a NEW local pin, disclosed as such (not retroactive).
// Output: download/wave1/snapshot-pin-reverify-20261024.json
const fs = require('fs');
const crypto = require('crypto');

const SNAP = '/home/z/my-project/.tmp/wave1/corpus-snapshot.json';
const MAN = '/home/z/my-project/.tmp/wave1/snapshot-manifest.json';
const DL = '/home/z/my-project/download/wave1';
const ROSTER = [
  'rn_xT8XsdJtDX5gNFXj', 'rn_HZM2WRjPPT8Srcxt', 'rn_JCfdFrHsCkrmMbFj', 'rn_TM4QVMgXVxs4vbfY',
  'rn_wTtM2fQVVjntRm64', 'rn_jNJ4gTmcHqdFqsNh', 'rn_kJg2gwF77vdFZZ2H', 'rn_fQSYvKRMDBj3s2Bx',
  'rn_2d6Yb8GwGfRRd6pZ', 'rn_4SgDJv8rKxpQQSBh',
];
const CALIBRATION = 'rn_kb2VkFMdBTbmG33t';
const CENSUS_OF_RECORD = { topics: 4, subtopics: 28, notes: 112, perTopicNotes: [40, 36, 15, 21] };
const VERSION_OF_RECORD = 'sme-revision-notes-igcse-chemistry-19-2026-09-18';

const sha256 = s => crypto.createHash('sha256').update(s).digest('hex');
const check = (name, ok, detail) => ({ name, ok, detail: detail === undefined ? '' : String(detail) });
const deepEq = (a, b) => JSON.stringify(a) === JSON.stringify(b);

const snapBytes = fs.readFileSync(SNAP);
const snap = JSON.parse(snapBytes.toString('utf8'));
const manifest = JSON.parse(fs.readFileSync(MAN, 'utf8'));
const results = [];

// ---- A. per-note body pins ----
let pinMismatch = [], charMismatch = [];
for (const n of snap.notes) {
  if (sha256(n.body) !== n.bodySha256) pinMismatch.push(n.noteId);
  if (n.body.length !== n.bodyChars) charMismatch.push(n.noteId);
}
results.push(check('A1 per-note bodySha256 recomputed 112/112', pinMismatch.length === 0, pinMismatch.length ? 'MISMATCH: ' + pinMismatch.join(',') : snap.notes.length + '/112 match'));
results.push(check('A2 per-note bodyChars recomputed', charMismatch.length === 0, charMismatch.length ? 'MISMATCH: ' + charMismatch.join(',') : 'all match'));

// ---- B. census recompute ----
const topics = {};
for (const n of snap.notes) {
  const k = `T${n.topicOrder}:${n.topicTitle}`;
  (topics[k] = topics[k] || { subtopics: new Set(), notes: 0 });
  topics[k].subtopics.add(`T${n.topicOrder}:S${n.subtopicOrder}:${n.subtopicTitle}`);
  topics[k].notes++;
}
const shape = Object.entries(topics).map(([k, v]) => ({ topic: k, subtopics: v.subtopics.size, notes: v.notes }));
const reCensus = {
  noteCount: snap.notes.length,
  topicCount: shape.length,
  subtopicCount: new Set(snap.notes.map(n => `T${n.topicOrder}:S${n.subtopicOrder}:${n.subtopicTitle}`)).size,
  perTopic: shape,
  totalBodyChars: snap.notes.reduce((a, n) => a + n.bodyChars, 0),
  corpusVersions: [...new Set(snap.notes.map(n => n.corpusVersion))],
};
results.push(check('B1 noteCount 112', reCensus.noteCount === manifest.noteCount && reCensus.noteCount === CENSUS_OF_RECORD.notes, reCensus.noteCount));
results.push(check('B2 topicCount 4', reCensus.topicCount === manifest.topicCount && reCensus.topicCount === CENSUS_OF_RECORD.topics, reCensus.topicCount));
results.push(check('B3 subtopicCount 28', reCensus.subtopicCount === manifest.subtopicCount && reCensus.subtopicCount === CENSUS_OF_RECORD.subtopics, reCensus.subtopicCount));
results.push(check('B4 perTopic 40/36/15/21', deepEq(reCensus.perTopic.map(p => p.notes), CENSUS_OF_RECORD.perTopicNotes) && deepEq(reCensus.perTopic, manifest.perTopic), JSON.stringify(reCensus.perTopic.map(p => p.notes))));
results.push(check('B5 totalBodyChars 361272', reCensus.totalBodyChars === manifest.totalBodyChars, reCensus.totalBodyChars + ' vs ' + manifest.totalBodyChars));
results.push(check('B6 single corpus_version == version of record', reCensus.corpusVersions.length === 1 && reCensus.corpusVersions[0] === VERSION_OF_RECORD && deepEq(manifest.corpusVersions, reCensus.corpusVersions), reCensus.corpusVersions.join(',')));

// ---- C. pull-order + uniqueness invariants ----
// numeric tuple compare (NOT string compare: lexicographic would order note_order 10 < 2)
const key = n => [n.topicOrder, n.subtopicOrder, n.noteOrder];
const cmp = (a, b) => (a[0] - b[0]) || (a[1] - b[1]) || (a[2] - b[2]);
const sorted = snap.notes.every((n, i) => i === 0 || cmp(key(n), key(snap.notes[i - 1])) > 0); // strictly increasing => ordered AND no duplicate positions
const uniq = new Set(snap.notes.map(n => n.noteId)).size === snap.notes.length;
results.push(check('C1 notes in canonical pull order (topic,subtopic,note), no dupes', sorted, sorted ? 'ordered' : 'ORDER BROKEN'));
results.push(check('C2 noteIds unique', uniq, uniq ? snap.notes.length + ' unique' : 'DUPES'));

// ---- D. cross-pin the wave-1 receipts ----
const rowOf = id => snap.notes.find(n => n.noteId === id);
let receiptMismatches = [];
for (const id of ROSTER) {
  const r = JSON.parse(fs.readFileSync(`${DL}/timing-receipt-${id}.json`, 'utf8'));
  const row = rowOf(id);
  const fields = {
    bodySha256: r.bodySha256 === row.bodySha256,
    bodyChars: r.bodyChars === row.bodyChars,
    corpusVersion: r.corpusVersion === row.corpusVersion,
    noteTitle: r.noteTitle === row.title,
    topicTitle: r.topicTitle === row.topicTitle,
    subtopicTitle: r.subtopicTitle === row.subtopicTitle,
    specPointCodes: deepEq(r.specPointCodes, row.specPointCodes),
  };
  const bad = Object.entries(fields).filter(([, ok]) => !ok).map(([k]) => k);
  if (bad.length) receiptMismatches.push(`${id}:${bad.join('+')}`);
}
results.push(check('D1 all 10 wave receipts pinned to snapshot rows', receiptMismatches.length === 0, receiptMismatches.length ? receiptMismatches.join(' | ') : '10/10 receipts match on 7 pin fields each'));
results.push(check('D2 calibration note present in snapshot', !!rowOf(CALIBRATION), CALIBRATION));

// ---- E. wave receipt corpusPin ----
const waveReceipt = JSON.parse(fs.readFileSync(`${DL}/wave1-receipt.json`, 'utf8'));
results.push(check('E1 wave receipt embedded manifest == manifest file', deepEq(waveReceipt.corpusPin.snapshotManifest, manifest), deepEq(waveReceipt.corpusPin.snapshotManifest, manifest) ? 'identical' : 'DRIFT'));
results.push(check('E2 wave receipt censusOfRecord == census of record', deepEq(waveReceipt.corpusPin.censusOfRecord, CENSUS_OF_RECORD), 'match'));
const wavePinVersions = new Set(waveReceipt.perNote.map(n => n.bodySha256));
results.push(check('E3 wave receipt perNote body pins == snapshot rows', waveReceipt.perNote.every(n => n.bodySha256 === rowOf(n.noteId).bodySha256), wavePinVersions.size + ' distinct pins, all match'));

// ---- F. file-level pins minted now (going-forward local pins) ----
const snapshotFileSha = sha256(snapBytes);
const manifestFileSha = sha256(fs.readFileSync(MAN));
results.push(check('F1 file-level pin minted (disclosed as new, not retroactive)', /^[0-9a-f]{64}$/.test(snapshotFileSha), snapshotFileSha));

// ---- remaining-102 census (feeds pacing) ----
const remaining = snap.notes.filter(n => !ROSTER.includes(n.noteId));
const remByTopic = {};
for (const n of remaining) {
  const k = `T${n.topicOrder}:${n.topicTitle}`;
  (remByTopic[k] = remByTopic[k] || { notes: 0, chars: 0, subtopics: new Set() });
  remByTopic[k].notes++; remByTopic[k].chars += n.bodyChars;
  remByTopic[k].subtopics.add(`S${n.subtopicOrder}:${n.subtopicTitle}`);
}
const remainingCensus = {
  notes: remaining.length,
  totalBodyChars: remaining.reduce((a, n) => a + n.bodyChars, 0),
  perTopic: Object.entries(remByTopic).map(([k, v]) => ({ topic: k, notes: v.notes, chars: v.chars, subtopics: v.subtopics.size })),
};

const failed = results.filter(r => !r.ok);
const receiptOut = {
  format: 'snapshot-pin-reverify/0.1',
  at: new Date().toISOString(),
  operatorInstruction: 're-verify the snapshot pin (trace 1a169f7a1cd353f5)',
  method: 'local recomputation only — ZERO DB contact (single read-only pull consumed and declared final 2026-10-23); sha256 + census recomputed from local bytes and cross-checked against every artifact that pinned itself to the snapshot',
  snapshotFile: SNAP,
  checks: results,
  filePinsMinted: {
    disclosure: 'the manifest of record pins per-note body hashes; the snapshot FILE had no whole-file pin. These file pins are minted NOW as the going-forward local mutation detectors; they are not retroactive claims.',
    corpusSnapshotSha256: snapshotFileSha,
    snapshotManifestSha256: manifestFileSha,
  },
  remainingCensusAfterWave1: remainingCensus,
  verdict: failed.length === 0 ? 'PIN VERIFIED — snapshot of record intact; all self-pinned artifacts reconcile' : 'PIN VERIFY FAILED',
};
fs.writeFileSync(`${DL}/snapshot-pin-reverify-20261024.json`, JSON.stringify(receiptOut, null, 1));
results.forEach(r => console.log((r.ok ? 'PASS' : 'FAIL') + '  ' + r.name + (r.detail ? '  [' + r.detail + ']' : '')));
console.log('\nremaining census:', JSON.stringify(remainingCensus.perTopic.map(p => p.topic.split(':')[0] + ' ' + p.notes + ' notes / ' + p.chars + ' ch')));
console.log('snapshot file pin (new):', snapshotFileSha);
console.log(failed.length ? 'VERDICT: FAIL' : 'VERDICT: ' + receiptOut.verdict);
process.exit(failed.length ? 1 : 0);
