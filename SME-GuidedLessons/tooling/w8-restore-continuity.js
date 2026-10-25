#!/usr/bin/env node
// w8-restore-continuity.js — WAVE-8 entry restoration (post-recycle paranoia discipline).
// The sandbox image lacks wave-6/7 artefacts (worklog records wave-5 as last local close).
// The remote home arbitrates: pull wave-6/ + wave-7/ full sets, event logs, reports,
// README-current, MANIFEST of record; verify every sha256 against MANIFEST entries.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const TOKEN = fs.readFileSync('/home/z/my-project/.creds/gh-pat.candidate', 'utf8').trim();
const REPO = 'SyllabAI/syllabai-resources';
const BASE = 'SME-GuidedLessons/';
const H = { Authorization: 'token ' + TOKEN, 'User-Agent': 'w0a-restore-wave8', Accept: 'application/vnd.github.raw+json' };

async function ghJson(p) {
  const r = await fetch('https://api.github.com/repos/' + REPO + '/contents/' + p + '?ref=main', { headers: H });
  return { status: r.status, body: await r.json() };
}
async function ghRaw(p) {
  const r = await fetch('https://api.github.com/repos/' + REPO + '/contents/' + p + '?ref=main', { headers: H });
  if (r.status !== 200) throw new Error('raw FAIL ' + r.status + ' ' + p);
  return Buffer.from(await r.arrayBuffer());
}

(async () => {
  let ok = 0, fail = 0;
  const pull = async (repoPath, localPath) => {
    const buf = await ghRaw(repoPath);
    fs.mkdirSync(path.dirname(localPath), { recursive: true });
    fs.writeFileSync(localPath, buf);
    return buf;
  };

  // 1. wave-6/ and wave-7/ full sets
  for (const w of ['wave-6', 'wave-7']) {
    const { body } = await ghJson(BASE + w);
    if (!Array.isArray(body)) throw new Error(w + ' listing FAIL');
    for (const f of body) {
      const buf = await pull(BASE + w + '/' + f.name, '/home/z/my-project/download/' + w.replace('-', '') + '/' + f.name);
      const sha = crypto.createHash('sha256').update(buf).digest('hex');
      if (f.sha) { // git blob sha check
        const gitSha = crypto.createHash('sha1').update(Buffer.concat([Buffer.from('blob ' + buf.length + '\0'), buf])).digest('hex');
        if (gitSha === f.sha) ok++; else { fail++; console.error('SHA1 MISMATCH', w + '/' + f.name); }
      } else ok++;
    }
    console.log('RESTORED ' + w + ': ' + body.length + ' files');
  }

  // 2. event logs wave-6/7
  for (const w of ['wave-6', 'wave-7']) {
    const { body } = await ghJson(BASE + 'event-logs/' + w);
    if (!Array.isArray(body)) throw new Error('event-logs/' + w + ' FAIL');
    fs.mkdirSync('/home/z/my-project/.tmp/' + w.replace('-', '') + '/runs', { recursive: true });
    for (const f of body) {
      await pull(BASE + 'event-logs/' + w + '/' + f.name, '/home/z/my-project/.tmp/' + w.replace('-', '') + '/runs/' + f.name);
      ok++;
    }
    console.log('RESTORED event-logs/' + w + ': ' + body.length + ' files');
  }

  // 3. reports Wave-6/7 docx
  const reps = await ghJson(BASE + 'reports');
  for (const f of reps.body.filter(f => /Wave-[67]/.test(f.name))) {
    await pull(BASE + 'reports/' + f.name, '/home/z/my-project/download/' + f.name);
    ok++;
  }

  // 4. README-current + MANIFEST of record
  await pull(BASE + 'README.md', '/home/z/my-project/.tmp/wave8/README-current.md');
  await pull(BASE + 'MANIFEST.json', '/home/z/my-project/.tmp/wave8/MANIFEST-current.json');
  ok += 2;

  // 5. verify against MANIFEST status
  const mf = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave8/MANIFEST-current.json', 'utf8'));
  console.log('MANIFEST status:', JSON.stringify(mf.status && { notes: mf.status.notes_authored, waves: (mf.status.waves_complete || []).length, next: mf.status.next_operator_gated }));
  const files = mf.files || [];
  console.log('MANIFEST entries:', files.length);
  let spot = 0;
  for (const e of files.filter(e => /wave-[67]\//.test(e.path || e.file || ''))) {
    const p = e.path || e.file;
    const local = '/home/z/my-project/download/' + p.replace(/^SME-GuidedLessons\//, '').replace('wave-6', 'wave6').replace('wave-7', 'wave7');
    if (fs.existsSync(local)) {
      const sha = crypto.createHash('sha256').update(fs.readFileSync(local)).digest('hex');
      if (sha === e.sha256) spot++; else { fail++; console.error('MANIFEST SHA MISMATCH', p); }
    } else { fail++; console.error('MISSING locally', p); }
  }
  console.log(`RESTORE DONE: ${ok} pulls, spot-sha ${spot} match, ${fail} failures`);
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
