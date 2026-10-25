#!/usr/bin/env node
// w9-entry-verify.js — WAVE-9 entry discipline (trace 1a174b960e367b61 verbatim "Go wave-9").
// Post-recycle paranoia: recompute the snapshot pin; arbitrate continuity against the REMOTE
// home (fetch head + README-current + MANIFEST-current); verify the local wave-8 set and
// waves 1-7 file counts against MANIFEST v7; verify the three gate libraries resolve.
const fs = require('fs');
const crypto = require('crypto');
const TOKEN = fs.readFileSync('/home/z/my-project/.creds/gh-pat.candidate', 'utf8').trim();
const REPO = 'SyllabAI/syllabai-resources';
const BASE = 'SME-GuidedLessons/';
const H = { Authorization: 'token ' + TOKEN, 'User-Agent': 'w0a-entry-wave9', Accept: 'application/vnd.github.raw+json' };

let fails = 0;
function check(name, ok, detail) {
  console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${detail ? ' — ' + detail : ''}`);
  if (!ok) fails++;
}
async function ghRaw(p) {
  const r = await fetch('https://api.github.com/repos/' + REPO + '/contents/' + p + '?ref=main', { headers: H });
  if (r.status !== 200) throw new Error('raw FAIL ' + r.status + ' ' + p);
  return Buffer.from(await r.arrayBuffer());
}

(async () => {
  // 1. snapshot pin (recompute, zero-DB)
  const SNAP = '/home/z/my-project/.tmp/wave1/corpus-snapshot.json';
  const pin = crypto.createHash('sha256').update(fs.readFileSync(SNAP)).digest('hex');
  check('snapshot pin MATCH (e23e2ab7...487d)', pin === 'e23e2ab79df6b0e957bf12933779e4701b37c88736d87c20b19bac130553487d', pin.slice(0, 16) + '...');

  // 2. remote head of record
  const refR = await fetch('https://api.github.com/repos/' + REPO + '/git/ref/heads/main', { headers: { Authorization: 'token ' + TOKEN, 'User-Agent': 'w0a-entry-wave9' } });
  const ref = await refR.json();
  check('remote main ref reachable', refR.status === 200 && ref.object && ref.object.sha, ref.object ? ref.object.sha.slice(0, 12) + '...' : 'n/a');

  // 3. README-current + MANIFEST-current from remote
  fs.mkdirSync('/home/z/my-project/.tmp/wave9', { recursive: true });
  const readme = await ghRaw(BASE + 'README.md');
  fs.writeFileSync('/home/z/my-project/.tmp/wave9/README-current.md', readme);
  const manBuf = await ghRaw(BASE + 'MANIFEST.json');
  fs.writeFileSync('/home/z/my-project/.tmp/wave9/MANIFEST-current.json', manBuf);
  const mf = JSON.parse(manBuf.toString('utf8'));
  check('MANIFEST v7 of record', mf.manifest_version === 7, 'v' + mf.manifest_version);
  check('MANIFEST status 92 + T3 complete', mf.status && mf.status.notes_authored === 92 && mf.status.topic3_complete === true, JSON.stringify(mf.status && mf.status.notes_authored));
  check('MANIFEST next = wave-9', mf.status && /wave-9 open/.test(mf.status.next_operator_gated || ''), (mf.status && mf.status.next_operator_gated || '').slice(0, 60));
  check('MANIFEST entries 393', Object.keys(mf.files).length === 393, `got ${Object.keys(mf.files).length}`);

  // 4. local wave-8 set verified against MANIFEST v7 sha256 (every entry)
  let ok8 = 0, bad8 = 0;
  for (const [p, meta] of Object.entries(mf.files)) {
    if (!/wave-8\//.test(p)) continue;
    // download entries (wave-8/...) map to download/wave8/; event-log entries map to .tmp/wave8/runs/
    const local = /event-logs\/wave-8\//.test(p)
      ? '/home/z/my-project/.tmp/wave8/runs/' + p.split('/').pop()
      : '/home/z/my-project/download/' + p.replace(/^SME-GuidedLessons\//, '').replace('wave-8', 'wave8');
    if (!fs.existsSync(local)) { bad8++; console.error('  MISSING', local); continue; }
    const sha = crypto.createHash('sha256').update(fs.readFileSync(local)).digest('hex');
    if (sha === meta.sha256) ok8++; else { bad8++; console.error('  SHA MISMATCH', p); }
  }
  check('local wave-8 set matches MANIFEST v7 (43 files: 29 download + 14 logs)', ok8 === 43 && bad8 === 0, `ok ${ok8}, bad ${bad8}`);
  const reports = Object.keys(mf.files).filter(p => /reports\/Wave-8/.test(p));
  check('MANIFEST carries wave-8 report', reports.length === 1, reports.join(','));

  // 5. prior waves file counts intact locally (wave-4 = 23: 11 notes; wave-8 = 29: 14 notes)
  const counts = { wave1: 22, wave2: 25, wave3: 25, wave4: 23, wave5: 25, wave6: 25, wave7: 19, wave8: 29 };
  for (const [w, n] of Object.entries(counts)) {
    const dir = fs.readdirSync(`/home/z/my-project/download/${w}`);
    check(`${w} deliverables intact (${n})`, dir.length === n, `count ${dir.length}`);
  }
  // prior receipt pool = 92
  const prior = new Set();
  for (const w of Object.keys(counts)) {
    for (const f of fs.readdirSync(`/home/z/my-project/download/${w}`).filter(f => f.startsWith('timing-receipt-'))) {
      prior.add(JSON.parse(fs.readFileSync(`/home/z/my-project/download/${w}/${f}`, 'utf8')).noteId);
    }
  }
  check('prior receipt pool 92 unique (waves 1-8)', prior.size === 92, `pool ${prior.size}`);

  // 6. libraries resolve
  for (const lib of ['ajv', 'js-yaml', 'docx']) {
    try { require.resolve('/home/z/node_modules/' + lib); check(`library ${lib} resolves`, true); }
    catch (e) { check(`library ${lib} resolves`, false, e.message.slice(0, 60)); }
  }

  // 7. spec pack present
  check('spec pack present (.tmp/wave5/specification_points.yaml)', fs.existsSync('/home/z/my-project/.tmp/wave5/specification_points.yaml'));
  check('pacing file present', fs.existsSync('/home/z/my-project/download/wave-pacing-open-20261024.json'));
  check('harness patched (save() patch of record)', fs.readFileSync('/home/z/my-project/scripts/wave1-run.js', 'utf8').includes('persist at mutation time'));

  console.log(fails ? `\nENTRY VERIFY FAILS: ${fails}` : '\nENTRY VERIFICATION: ALL PASS');
  process.exit(fails ? 1 : 0);
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
