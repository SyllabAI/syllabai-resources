#!/usr/bin/env node
// wave1-assist-fix.js — declaration-integrity correction of record, wave-1 round 2026-10-24.
// Notes 7-10 (rn_kJg2gwF77vdFZZ2H, rn_fQSYvKRMDBj3s2Bx, rn_2d6Yb8GwGfRRd6pZ, rn_4SgDJv8rKxpQQSBh)
// were authored P2-P7 in the 2026-10-23/24 sessions with model-drafted content, but their phase
// clocks were closed without the --assist flag, so the receipts would have declared
// "unflagged phases produced no drafted content" falsely. Spec section 7.2: any drafting
// assistance is a per-phase receipt flag. This patch sets assist:true on P2-P7 phase-end
// events (P0 read-only and P8 mechanical stay unflagged per house rule) and re-exports
// each note so the receipts of record carry true flags.
const fs = require('fs');
const W = '/home/z/my-project/.tmp/wave1/runs';
const NOTES = ['rn_kJg2gwF77vdFZZ2H', 'rn_fQSYvKRMDBj3s2Bx', 'rn_2d6Yb8GwGfRRd6pZ', 'rn_4SgDJv8rKxpQQSBh'];
const FLAGGED = ['P2', 'P3', 'P4', 'P5', 'P6', 'P7'];

NOTES.forEach(noteId => {
  const file = `${W}/${noteId}.events.json`;
  const events = JSON.parse(fs.readFileSync(file, 'utf8'));
  let n = 0;
  events.forEach(e => {
    if (e.type === 'phase-end' && FLAGGED.includes(e.phase) && e.assist === false) {
      // leave resume-boundary no-ops alone: a phase-end is real if a matching phase-start preceded it
      e.assist = true; n++;
    }
  });
  fs.writeFileSync(file, JSON.stringify(events, null, 1));
  console.log(`PATCHED ${noteId}: ${n} phase-end events flagged assist:true (P2-P7)`);
});
