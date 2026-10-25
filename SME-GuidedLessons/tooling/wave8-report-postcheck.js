#!/usr/bin/env node
// wave8-report-postcheck.js — post-generation verification of the Wave-8 report DOCX,
// mirroring the wave-3/4/5 post-check profile: structure counts (tables / sections / TOC
// bookmarks), content probes (every h1 + key figures), and cover meta-line checks.
const fs = require('fs');
const { execSync } = require('child_process');
const PATH = '/home/z/my-project/download/Wave-8-Authoring-Wave-Report-20261025.docx';
const xml = execSync(`unzip -p ${PATH} word/document.xml`, { maxBuffer: 64 * 1024 * 1024 }).toString('utf8');

let fails = 0;
const check = (name, ok, detail) => { console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${detail ? ' — ' + detail : ''}`); if (!ok) fails++; };

// structure
const tables = (xml.match(/<w:tbl>/g) || []).length;
const sects = (xml.match(/<w:sectPr/g) || []).length;
const bookmarks = (xml.match(/<w:bookmarkStart[^>]*_Toc/g) || []).length;
check('structure: 4 tables (cover wrapper + T1 + T2 + T3)', tables === 4, `count ${tables}`);
check('structure: 3 sections', sects === 3, `count ${sects}`);
check('structure: 10 TOC bookmarks', bookmarks === 10, `count ${bookmarks}`);

// content probes
const probes = [
  '1. Executive Summary', '2. Posture and Protocol', '3. Corpus Pin and Register',
  '4. Results', '5. Quality', '6. Measurement Integrity',
  '7. Recalibration Checkpoint', '8. Interpretation and Progress', '9. Artifacts', '10. Next Steps',
  '82.1 percent', 'fifteen of fifteen', 'twenty of twenty-eight', 'fifty-two thousand five hundred and ninety-five',
  'Measuring Rates', 'The Position of Equilibrium', 'Energetics Calculations', 'Bond Energy',
  'one hundred ninety-four to two hundred fifteen milliseconds', 'e23e2ab7',
  'bands of twenty-eight, fifty-six and ninety-three author-days', 'two hundred eighty-three seconds per note',
  'twelve designed declarations', 'half-rounding boundary', 'official-bullets field',
  '480 named-misconception', 'MANIFEST', 'SME-GuidedLessons', 'one command',
];
for (const p of probes) check(`probe: "${p.slice(0, 48)}"`, xml.includes(p));
const clean = xml.replace(/<[^>]+>/g, '');
for (const meta of ['14/14 register notes exported clean first-pass', 'trace 1a174751135ae18d', 'Complete 2026-10-25', 'W  A  V  E  ']) {
  check('cover meta: ' + meta.slice(0, 40), clean.includes(meta));
}
// forbidden: no artificial end markers
check('no artificial end marker', !/End of Report|Document Ends/i.test(clean));

console.log(fails ? `\n${fails} FAILURES` : '\nDOCX POSTCHECK: ALL PASS');
process.exit(fails ? 1 : 0);
