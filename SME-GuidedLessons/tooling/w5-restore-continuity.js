#!/usr/bin/env node
// Post-recycle continuity restoration from SME-GuidedLessons/ @ cc5f0e8d (wave-4 of record).
// contents-API only (LEDGER F16); every restored blob sha256-verified against MANIFEST v3.
// Token never printed.
const fs = require('fs');
const crypto = require('crypto');
const path = require('path');
const TOKEN = fs.readFileSync('/home/z/my-project/.creds/gh-pat.candidate', 'utf8').trim();
const REPO = 'SyllabAI/syllabai-resources';
const BASE = 'SME-GuidedLessons/';
const H = { Authorization: 'token ' + TOKEN, 'User-Agent': 'w0a-restore', Accept: 'application/vnd.github+json' };

async function ghJson(url) { const r = await fetch('https://api.github.com' + url, { headers: H }); return { status: r.status, body: await r.json().catch(() => null) }; }
async function listDir(dir) {
  const r = await ghJson('/repos/' + REPO + '/contents/' + BASE + dir);
  if (r.status !== 200) throw new Error(dir + ' list FAIL ' + r.status);
  return r.body.filter(x => x.type === 'file').map(x => x.name);
}

(async () => {
  const mf = await ghJson('/repos/' + REPO + '/contents/' + BASE + 'MANIFEST.json');
  if (mf.status !== 200) throw new Error('MANIFEST FAIL ' + mf.status);
  const man = JSON.parse(Buffer.from(mf.body.content, 'base64').toString('utf8'));
  const shaByPath = new Map();
  const filesField = man.files || {};
  if (Array.isArray(filesField)) for (const e of filesField) shaByPath.set(e.path, e.sha256 || e.sha);
  else for (const [p, v] of Object.entries(filesField)) shaByPath.set(p, typeof v === 'string' ? v : (v.sha256 || v.sha));
  console.log('MANIFEST v' + man.manifest_version + ' entries with sha:', shaByPath.size, '| sample:', JSON.stringify((Array.isArray(filesField) ? filesField[0] : Object.entries(filesField)[0])));

  const jobs = [
    ['wave-3/wave3-receipt.json', '/home/z/my-project/download/wave3/wave3-receipt.json'],
    ['reports/Wave-3-Authoring-Wave-Report-20261025.docx', '/home/z/my-project/download/Wave-3-Authoring-Wave-Report-20261025.docx'],
    ['reports/Wave-4-Authoring-Wave-Report-20261025.docx', '/home/z/my-project/download/Wave-4-Authoring-Wave-Report-20261025.docx'],
  ];
  for (const f of await listDir('wave-4')) jobs.push(['wave-4/' + f, '/home/z/my-project/download/wave4/' + f]);
  for (const f of await listDir('event-logs/wave-4')) jobs.push(['event-logs/wave-4/' + f, '/home/z/my-project/.tmp/wave4/runs/' + f]);
  for (const f of ['wave3-wave-receipt.js', 'wave3-report.js', 'wave3-report-content-1.js', 'wave3-report-content-2.js',
    'wave4-round-verify.js', 'wave4-wave-receipt.js', 'wave4-report.js', 'wave4-report-content-1.js',
    'wave4-report-content-2.js', 'wave4-report-postcheck.js']) jobs.push(['tooling/' + f, '/home/z/my-project/scripts/' + f]);

  let ok = 0; const bad = [];
  for (const [rp, lp] of jobs) {
    const r = await ghJson('/repos/' + REPO + '/contents/' + BASE + rp);
    if (r.status !== 200) { bad.push(rp + ' FETCH ' + r.status); continue; }
    const buf = Buffer.from(r.body.content, 'base64');
    fs.mkdirSync(path.dirname(lp), { recursive: true });
    fs.writeFileSync(lp, buf);
    const expect = shaByPath.get(rp) || shaByPath.get(BASE + rp);
    const got = crypto.createHash('sha256').update(buf).digest('hex');
    const v = expect ? (expect === got ? 'SHA-MATCH' : 'SHA-MISMATCH!') : 'NO-MANIFEST-ENTRY';
    if (v === 'SHA-MISMATCH!') bad.push(rp + ' SHA');
    else { ok++; console.log('restored', rp, '->', lp.replace('/home/z/my-project/', ''), buf.length + 'B', v); }
  }
  console.log('RESTORED OK: ' + ok + '/' + jobs.length + (bad.length ? ' | BAD: ' + bad.join('; ') : ' | zero bad'));
})().catch(e => { console.error('RESTORE CRASH ' + e.message); process.exit(1); });
