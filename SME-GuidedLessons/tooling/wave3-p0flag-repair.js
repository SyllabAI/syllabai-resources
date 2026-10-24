#!/usr/bin/env node
// wave3-p0flag-repair.js — repair of the 2026-10-25 notes-5-6 chain-invocation error.
// ERROR: the first `phase P1` command was passed --assist, so the harness recorded
// assist:true on the P0 phase-end for both notes. The of-record discipline (notes 1-4)
// is P0 unflagged (read-only, no drafted content) with assistedPhases = exactly P1..P7;
// the misflag makes each receipt self-contradictory (its own protocol line says
// "P0 read-only"). LAYERS UNTOUCHED — this is a flow-flag correction, not a content edit.
// REPAIR: set assist:false on the P0 phase-end event of the two affected logs (matching
// the of-record note-3 log shape, which carries assist:false on P0's phase-end), then a
// human fires the harness's own `export` command per note — the idempotent re-export path
// appends export events with reExport:true and regenerates the receipts from the
// corrected logs. The correction is disclosed in worklog.md, not hidden.
const fs = require('fs');
const RUNS = '/home/z/my-project/.tmp/wave3/runs';
const NOTES = ['rn_vXPcH3vS8wv7BFkK', 'rn_pWzTTBv3B4yGFfj3'];

let repaired = 0;
for (const nid of NOTES) {
  const file = `${RUNS}/${nid}.events.json`;
  const events = JSON.parse(fs.readFileSync(file, 'utf8'));
  // sanity: find the P0 phase-end (must be the event right after the P0 phase-start)
  const idx = events.findIndex(e => e.type === 'phase-end' && e.phase === 'P0');
  if (idx === -1) { console.error(`${nid}: no P0 phase-end found - ABORT`); process.exit(1); }
  if (idx !== 1) { console.error(`${nid}: P0 phase-end at unexpected index ${idx} - ABORT`); process.exit(1); }
  const ev = events[idx];
  if (!ev.assist) { console.log(`${nid}: P0 phase-end already unflagged - no-op`); continue; }
  if (events[0].phase !== 'P0' || events[0].type !== 'phase-start') {
    console.error(`${nid}: event 0 is not the P0 phase-start - ABORT`); process.exit(1);
  }
  ev.assist = false;
  fs.writeFileSync(file, JSON.stringify(events, null, 1));
  repaired++;
  console.log(`${nid}: P0 phase-end assist flag corrected true -> false (event ${idx})`);
}
console.log(repaired === 0 ? 'NOTHING REPAIRED' : `REPAIRED ${repaired} log(s); now fire idempotent re-export per note`);
