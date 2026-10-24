#!/usr/bin/env node
// wave4-report-postcheck.js — post-generation verification of the Wave-4 report DOCX,
// mirroring the wave-3 post-check profile: structure counts (tables / sections / TOC
// bookmarks), content probes (every h1 + key figures), and cover meta-line checks.
const fs = require('fs');
const { execSync } = require('child_process');
const PATH = '/home/z/my-project/download/Wave-4-Authoring-Wave-Report-20261025.docx';
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
  '1. Executive Summary', '2. Posture and Protocol of Record', '3. Corpus Pin and Register of Record',
  '4. Results of Record', '5. Quality of Record', '6. Measurement Integrity of Record',
  '7. Recalibration Checkpoint', '8. Interpretation and Progress of Record', '9. Artifacts of Record', '10. Next Steps of Record',
  '45 of 112 notes authored (40.2 percent)', 'Topic 1 complete', '39,034', '22 lessons, 110 key points, 54 glossary entries and 110 explained checks',
  'Formulae for Ionic Compounds', 'Electrolysis Experiments', 'Metallic Bonding', 'C60 fullerene',
  '193 to 208 milliseconds', 'e23e2ab7', '28, 56 and 93 author-day bands', '283 seconds per note',
  'nine workedExample-null notes', 'two non-numeric ported examples', '330 named-misconception',
  'Group 1 and Group 7 reactivity notes', 'MANIFEST', 'SME-GuidedLessons',
];
for (const p of probes) check(`probe: "${p.slice(0, 48)}"`, xml.includes(p));
const clean = xml.replace(/<[^>]+>/g, '');
for (const meta of ['11/11 register notes exported clean first-pass', 'trace 1a16fbc3d4b5b749', 'Complete 2026-10-25', 'W  A  V  E  ']) {
  check('cover meta: ' + meta.slice(0, 40), clean.includes(meta));
}
// forbidden: no artificial end markers
check('no artificial end marker', !/End of Report|Document Ends/i.test(clean));

console.log(fails ? `\n${fails} FAILURES` : '\nDOCX POSTCHECK: ALL PASS');
process.exit(fails ? 1 : 0);
