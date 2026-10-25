#!/usr/bin/env node
// wave6-report-postcheck.js — post-generation verification of the Wave-6 report DOCX,
// mirroring the wave-3/4/5 post-check profile: structure counts (tables / sections / TOC
// bookmarks), content probes (every h1 + key figures), and cover meta-line checks.
const fs = require('fs');
const { execSync } = require('child_process');
const PATH = '/home/z/my-project/download/Wave-6-Authoring-Wave-Report-20261025.docx';
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
  '61.6 percent', 'twenty-seven of thirty-six', 'fifteen of twenty-eight', 'thirty-four thousand three hundred and sixteen',
  'Extracting Metals', 'Acid-Alkali Titrations', 'Oxidation &amp; Reduction', 'Reactivity Series',
  'two hundred four to two hundred thirty-seven milliseconds', 'e23e2ab7',
  'twenty-eight, fifty-six and ninety-three author-day bands', 'two hundred eighty-three seconds per note',
  'eleven designed declarations', 'third arithmetic-verified worked example',
  '360 named-misconception', 'MANIFEST v5', 'SME-GuidedLessons', 'one-command pattern',
];
for (const p of probes) check(`probe: "${p.slice(0, 48)}"`, xml.includes(p));
const clean = xml.replace(/<[^>]+>/g, '');
for (const meta of ['12/12 register notes exported clean first-pass', 'wave-6 next step', 'Complete 2026-10-25', 'W  A  V  E  ']) {
  check('cover meta: ' + meta.slice(0, 40), clean.includes(meta));
}
// forbidden: no artificial end markers
check('no artificial end marker', !/End of Report|Document Ends/i.test(clean));

console.log(fails ? `\n${fails} FAILURES` : '\nDOCX POSTCHECK: ALL PASS');
process.exit(fails ? 1 : 0);
