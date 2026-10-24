// Wave-1 spec-point official texts: ONE micro-pull (t0_readonly, SELECT-only) of the
// knowledge_nodes titles for every spec code referenced by the wave roster + the A1 note.
// Completes the local source pack so authoring needs zero DB contact. Token never echoed.
const fs = require('fs');
const { Client } = require('/home/z/node_modules/pg');

(async () => {
  const snap = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json', 'utf8'));
  const roster = ['rn_kb2VkFMdBTbmG33t',
    'rn_xT8XsdJtDX5gNFXj', 'rn_JCfdFrHsCkrmMbFj', 'rn_HZM2WRjPPT8Srcxt', 'rn_TM4QVMgXVxs4vbfY',
    'rn_wTtM2fQVVjntRm64', 'rn_jNJ4gTmcHqdFqsNh', 'rn_kJg2gwF77vdFZZ2H', 'rn_fQSYvKRMDBj3s2Bx',
    'rn_2d6Yb8GwGfRRd6pZ', 'rn_4SgDJv8rKxpQQSBh'];
  const codes = [...new Set(snap.notes.filter(n => roster.includes(n.noteId)).flatMap(n => n.specPointCodes))].sort();
  console.error('codes(' + codes.length + '):', codes.join(' '));

  const uri = fs.readFileSync('/home/z/my-project/.creds/neon-ro-uri', 'utf8').trim();
  const c = new Client({ connectionString: uri });
  await c.connect();
  const r = await c.query(`SELECT code, node_type, title FROM knowledge_nodes WHERE code = ANY($1) ORDER BY code`, [codes]);
  await c.end();

  const out = { pulledAt: new Date().toISOString(), lane: 't0_readonly, SELECT-only, one query', roster, codes, nodes: r.rows };
  fs.writeFileSync('/home/z/my-project/.tmp/wave1/spec-point-texts.json', JSON.stringify(out, null, 1));
  console.log(JSON.stringify({ requested: codes.length, returned: r.rows.length, missing: codes.filter(c => !r.rows.find(x => x.code === c)) }, null, 1));
})().catch(e => { console.error('FAIL:', e.message); process.exit(1); });
