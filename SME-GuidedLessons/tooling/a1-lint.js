#!/usr/bin/env node
// a1-lint.js — house-style lint v0.1, RE-DERIVED from the A1 spec of record Table 5
// (the original source was declared lost 2026-10-22; behaviour re-built from the rule
// table, calibrated against the spec's own section-5 exemplar).
// Usage: node scripts/a1-lint.js <layer.json> --note <noteId> [--snapshot <corpus-snapshot.json>]
// Exit 0 = no hard fails; exit 1 = hard fails present. Warnings are report-only; the
// run harness records any declared overrides in the timing receipt.
const fs = require('fs');

function sentences(t) {
  return String(t).split(/[.!?]+(?:\s|$)/).map(s => s.trim()).filter(Boolean);
}
function words(t) {
  return String(t).toLowerCase().match(/[a-z0-9'-]+/g) || [];
}
function longestSharedRun(text) {
  const w = words(text);
  let best = 0;
  for (let i = 0; i < w.length; i++) {
    let len = 0;
    for (let end = i; end < w.length; end++) {
      const phrase = w.slice(i, end + 1).join(' ');
      if (bodyPhraseIndex.has(phrase)) len = end - i + 1; else break;
    }
    if (len > best) best = len;
    if (len > 0) i += len - 1;
  }
  return best;
}

let bodyPhraseIndex = new Set();

const args = process.argv.slice(2);
const file = args[0];
function opt(name) { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : null; }
const noteId = opt('--note');
const snapshotPath = opt('--snapshot') || '/home/z/my-project/.tmp/wave1/corpus-snapshot.json';
const codesOpt = opt('--codes'); // calibration mode: explicit of-record code set (e.g. single-lesson fixture scope)

const layer = JSON.parse(fs.readFileSync(file, 'utf8'));
const snap = JSON.parse(fs.readFileSync(snapshotPath, 'utf8'));
const noteRow = snap.notes.find(n => n.noteId === noteId);
if (!noteRow) { console.error('note not found in snapshot: ' + noteId); process.exit(2); }

const V = [];
function hard(rule, field, msg) { V.push({ rule, severity: 'hard', field, message: msg }); }
function warn(rule, field, msg) { V.push({ rule, severity: 'warning', field, message: msg }); }

// ── body index for source fidelity ──
const bodyWords = words(noteRow.body);
const bodySet = new Set(bodyWords);
bodyPhraseIndex = new Set();
for (let i = 0; i < bodyWords.length; i++) {
  let p = bodyWords[i];
  bodyPhraseIndex.add(p);
  for (let j = i + 1; j < Math.min(i + 12, bodyWords.length); j++) {
    p += ' ' + bodyWords[j];
    bodyPhraseIndex.add(p);
  }
}

// ── 1. Spec coverage (hard) ──
const ofRecord = new Set(codesOpt ? codesOpt.split(',').map(s => s.trim()).filter(Boolean) : noteRow.specPointCodes);
const declared = new Set(layer.specPoints.map(s => s.code));
const lessonRefs = new Set(layer.lessons.flatMap(l => l.specRefs));
for (const c of ofRecord) if (!lessonRefs.has(c)) hard('spec-coverage', 'lessons[].specRefs', `spec point ${c} of record is not referenced by any lesson`);
for (const c of lessonRefs) if (!ofRecord.has(c)) hard('spec-coverage', 'lessons[].specRefs', `invented spec code ${c} (not in note's spec_point_codes of record)`);
for (const c of lessonRefs) if (!declared.has(c)) hard('spec-coverage', 'specPoints', `referenced code ${c} missing official text in specPoints`);
for (const c of declared) if (!ofRecord.has(c)) hard('spec-coverage', 'specPoints', `declared code ${c} not in note's spec_point_codes of record`);

// ── 2. Check integrity (hard) ──
layer.lessons.forEach((L, li) => {
  (L.check || []).forEach((item, ci) => {
    const f = `lessons[${li}].check[${ci}]`;
    const keys = new Set(item.options.map(o => o.key));
    if (keys.size !== item.options.length) hard('check-integrity', f, 'duplicate option keys');
    const correct = item.options.filter(o => o.correct);
    if (correct.length !== 1) hard('check-integrity', f, `exactly one keyed correct required, found ${correct.length}`);
    item.options.forEach(o => {
      const explSentences = sentences(String(o.explanation).replace(/Catch:.*$/i, ''));
      if (explSentences.length < 1 || explSentences.length > 2) warn('check-integrity', f + `.${o.key}`, `explanation should be 1-2 sentences, found ${explSentences.length}`); // style edge -> warning; absence is hard
      if (!o.explanation || !String(o.explanation).trim()) hard('check-integrity', f + `.${o.key}`, 'every option requires an explanation');
      if (!o.correct && !(o.misconception && String(o.misconception).trim())) hard('check-integrity', f + `.${o.key}`, 'distractor must name the misconception it catches');
      if (o.correct && o.misconception) warn('check-integrity', f + `.${o.key}`, 'correct option should carry null misconception');
    });
  });
});

// ── 3. Arithmetic truth (hard) ──
// Evaluates compound arithmetic with parentheses via shunting-yard; accepts significant-
// figure rounding in the stated result (e.g. 0.250 x 65.38 = 16.3 at 3 s.f.).
function evalArith(expr) {
  const tokens = String(expr).match(/(\d+\.?\d*|\+|\-|−|–|—|×|x|\*|÷|\/|\(|\))/g);
  if (!tokens) return null;
  const prec = { '+': 1, '-': 1, '−': 1, '–': 1, '—': 1, '×': 2, 'x': 2, '*': 2, '÷': 2, '/': 2 };
  const out = [], ops = [];
  let prev = null;
  for (let t of tokens) {
    if (/^\d/.test(t)) { out.push(parseFloat(t)); }
    else if (t === '(') { ops.push(t); }
    else if (t === ')') { while (ops.length && ops[ops.length - 1] !== '(') out.push(applyOp(ops.pop(), out)); if (!ops.length) return null; ops.pop(); }
    else if (prec[t]) {
      if ((t === '-' || t === '−') && (prev === null || prec[prev] || prev === '(')) out.push(0); // unary minus
      while (ops.length && prec[ops[ops.length - 1]] >= prec[t]) out.push(applyOp(ops.pop(), out));
      ops.push(t === '−' ? '-' : t === '–' || t === '—' ? '-' : t);
    } else return null;
    prev = t;
  }
  while (ops.length) { if (ops[ops.length - 1] === '(') return null; out.push(applyOp(ops.pop(), out)); }
  return out.length === 1 ? out[0] : null;
}
function applyOp(op, out) {
  const b = out.pop(), a = out.pop();
  if (a === undefined || b === undefined) throw new Error('malformed expression');
  return op === '+' ? a + b : op === '-' ? a - b : op === '×' || op === 'x' || op === '*' ? a * b : a / b;
}
function sigFigs(nStr) {
  const s = String(nStr).replace(/^[-+]/, '').replace('.', '').replace(/^0+/, '');
  return s.replace(/0+$/, '') === '' ? s.length : s.length; // trailing zeros kept: "16.3"->3, "34"->2
}
function matchesAtSigFigs(got, statedStr, statedFull) {
  const full = (statedFull === undefined) ? parseFloat(statedStr) : statedFull;
  if (full === 0) return Math.abs(got) < 1e-12; // stated zero: sigFigs("0")=0 would trip the sf<1 guard before the old zero-branch could run; exact-zero within float noise is the correct test (tooling fix, wave-1 note 4, documented in worklog)
  const sf = sigFigs(statedStr);
  if (!isFinite(got) || sf < 1) return false;
  const rounded = parseFloat(got.toPrecision(sf));
  const ulp = Math.pow(10, Math.floor(Math.log10(Math.abs(full))) - sf + 1) / 2;
  return Math.abs(rounded - full) <= ulp + 1e-12;
}
function mantissa(x) { if (x === 0) return 0; const e = Math.floor(Math.log10(Math.abs(x))); return Math.abs(x) / Math.pow(10, e); }
const we = layer.noteAssets && layer.noteAssets.workedExample;
const computedResults = [];
if (we) {
  let checked = 0;
  for (const s of we.steps) {
    const clean = String(s).replace(/<sup>|<\/sup>/g, '^');
    const re = /([\d\.\s\+\-\u2212\u2013\u2014\u00d7x*\u00f7\/\(\)]+?)=\s*(-?\d+(?:\.\d+)?)(?:\s*[×x]\s*10\^?\{?(-?\d+)\}?)?/g;
    let m;
    while ((m = re.exec(clean)) !== null) {
      const lhs = m[1].trim();
      if (!/[\+\-\u2212\u2013\u2014\u00d7x*\u00f7\/]/.test(lhs)) continue; // assignment, not arithmetic
      let got = evalArith(lhs);
      if (got === null) { warn('arithmetic-truth', 'noteAssets.workedExample', `could not parse expression "${lhs}" — verify manually`); continue; }
      // exponent tail ("= 7.71 x 10^-3") scales the STATED value, not the computed one
      const statedFull = m[3] ? parseFloat(m[2]) * Math.pow(10, parseInt(m[3], 10)) : parseFloat(m[2]);
      checked++;
      computedResults.push(statedFull);
      if (!matchesAtSigFigs(got, m[2], statedFull)) hard('arithmetic-truth', 'noteAssets.workedExample', `"${lhs}" recomputes to ${got}, stated ${statedFull}`);
    }
  }
  if (checked === 0) warn('arithmetic-truth', 'noteAssets.workedExample', 'no arithmetic expression found to verify (verify manually if the example is non-numeric)');
  // stated values: every number declared anywhere in the steps (assignments like "= 29")
  // plus verified arithmetic results; the final answer may only restate these.
  const statedNumbers = we.steps.map(s => String(s).match(/-?\d+(?:\.\d+)?/g) || []).flat().map(Number).concat(computedResults);
  const faClean = String(we.finalAnswer).replace(/\((?:\d+ )?(?:s\.?f\.?|d\.?p\.?|sig\.?|significant figures?|decimal places?)\)/gi, '');
  const faNums = (faClean.match(/-?\d+(?:\.\d+)?/g) || []).map(Number);
  for (const n of faNums) {
    const ok = statedNumbers.some(s => Math.abs(n - s) < 1e-9 * Math.max(1, Math.abs(s))) ||
      statedNumbers.some(s => s !== 0 && n !== 0 && Math.abs(mantissa(n) - mantissa(s)) < 5e-3); // scale-aware: standard form in the answer
    if (!ok) hard('arithmetic-truth', 'noteAssets.workedExample.finalAnswer', `final answer value ${n} does not trace to any stated step value or verified result`);
  }
} else {
  warn('arithmetic-truth', 'noteAssets.workedExample', 'workedExample is null — declared as none in source note (receipt must carry the declaration)');
}

// ── 4. Key-point economy (warning) ──
layer.lessons.forEach((L, li) => {
  L.keyPoints.forEach((kp, ki) => {
    const f = `lessons[${li}].keyPoints[${ki}]`;
    const nWords = words(kp).length;
    if (nWords > 25) warn('key-point-economy', f, `${nWords} words (max 25)`);
    if (sentences(kp).length > 1) warn('key-point-economy', f, 'more than one sentence');
  });
});

// ── 5. Plain-words register (warning) ──
const glossaryTerms = new Set((layer.noteAssets.glossary || []).map(g => g.term.toLowerCase()));
const jargonMorpheme = /(ation|esis|osis|ometry)\b/;
function scanRegister(text, f) {
  for (const w of new Set(words(text))) {
    if (w.length >= 9 && jargonMorpheme.test(w) && !glossaryTerms.has(w)) {
      warn('plain-words-register', f, `long technical-form word "${w}" not in glossary — define at first use or glossary it`);
    }
  }
}
layer.lessons.forEach((L, li) => {
  scanRegister(L.opening, `lessons[${li}].opening`);
  scanRegister(L.depthLayers.low.restatement + ' ' + L.depthLayers.medium.restatement, `lessons[${li}].depthLayers`);
});
scanRegister(layer.primer.text, 'primer');

// ── 6. Template uniformity (warning) ──
layer.lessons.forEach((L, li) => {
  const lo = L.depthLayers.low, me = L.depthLayers.medium;
  const lenLo = (lo.restatement + ' ' + lo.analogy + ' ' + lo.examPointer).length;
  const lenMe = (me.restatement + ' ' + me.analogy + ' ' + me.examPointer).length;
  const dev = Math.abs(lenLo - lenMe) / Math.max(lenLo, lenMe);
  if (dev > 0.30) warn('template-uniformity', `lessons[${li}].depthLayers`, `layer lengths differ by ${(dev * 100).toFixed(0)}% (max 30%)`);
});

// ── 7. Source fidelity (warning; scope: openings + key points per Table 5) ──
layer.lessons.forEach((L, li) => {
  const texts = [L.opening, ...L.keyPoints];
  texts.forEach((t, ti) => {
    const f = `lessons[${li}].${ti === 0 ? 'opening' : 'keyPoints[' + (ti - 1) + ']'}`;
    const run = longestSharedRun(t);
    if (run > 8) warn('source-fidelity', f, `${run}-word verbatim run from note body (max 8; short definition phrases excepted — override if legitimate)`);
  });
});

// ── 8. Register and units (warning) ──
const allText = JSON.stringify(layer);
if (/!/.test(allText)) warn('register-and-units', 'layer', 'exclamation mark present (house style: none)');
const americanisms = [['\\bcolor\\b', 'colour'], ['\\bcenter\\b', 'centre'], ['\\bliters?\\b', 'litre'], ['\\borganiz', 'organis'], ['\\banalyz', 'analys'], ['\\bioniz', 'ionis']];
for (const [pat, fix] of americanisms) {
  const re = new RegExp(pat, 'i');
  if (re.test(allText)) warn('register-and-units', 'layer', `possible US spelling (${pat.replace(/\\b/g, '')}) — British English required (${fix})`);
}

// ── report ──
const hardFails = V.filter(v => v.severity === 'hard');
const warnings = V.filter(v => v.severity === 'warning');
const report = { file, noteId, hardFails: hardFails.length, warnings: warnings.length, violations: V };
if (process.argv.includes('--json')) console.log(JSON.stringify(report, null, 1));
else {
  console.log(`LINT ${file} (note ${noteId}): hard-fails ${hardFails.length}, warnings ${warnings.length}`);
  for (const v of V) console.log(`  [${v.severity.toUpperCase()}] ${v.rule} @ ${v.field}: ${v.message}`);
}
process.exit(hardFails.length ? 1 : 0);
