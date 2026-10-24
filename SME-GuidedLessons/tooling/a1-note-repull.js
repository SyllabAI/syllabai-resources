#!/usr/bin/env python3
// Node: re-pull the A1 note of record READ-ONLY after the environment rollback.
// Reconstructs note-pin.json + rn-atoms-body.md for the restoration manifest.
// SELECT-only via t0_readonly (.creds/neon-ro-uri); token never echoed.
const fs = require('fs');
const crypto = require('crypto');
const { Client } = require('/home/z/node_modules/pg');

const OUT = '/home/z/my-project/download/A1-Restoration-20261022';

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const uri = fs.readFileSync('/home/z/my-project/.creds/neon-ro-uri', 'utf8').trim();
  const c = new Client({ connectionString: uri });
  await c.connect();

  const note = await c.query(`SELECT * FROM revision_note WHERE note_id = 'rn_kb2VkFMdBTbmG33t'`);
  const n = note.rows[0];
  if (!n) throw new Error('note not found');

  const body = n.body_md;
  const sha256 = crypto.createHash('sha256').update(body).digest('hex');
  fs.writeFileSync(`${OUT}/rn-atoms-body.md`, body);

  // spec joins + downstream question mass (confirm against of-record facts)
  const sps = String(n.spec_point_codes).split(',').map(s => s.trim()).filter(Boolean);
  const sp = await c.query(
    `SELECT code, node_type, title FROM knowledge_nodes WHERE code = ANY($1) ORDER BY code`, [sps]);
  const q = await c.query(`
    SELECT count(DISTINCT q.id) AS q_count
    FROM question_spec_points qsp
    JOIN knowledge_nodes kn ON kn.id = qsp.spec_point_node_id
    JOIN questions q ON q.id = qsp.question_id
    WHERE kn.code = ANY($1)`, [sps]);

  const pin = {
    restoredAt: new Date().toISOString(),
    restorationNote: 'Re-pulled read-only after environment rollback restored the tree to a ~02:13Z snapshot (the original note-pin.json of the 10:26Z pin was lost). This pin re-establishes the corpus pin of record; body sha256 must equal bf99e22d19c633a0ae64484a3ec090fe8c482545d532d21325077596ad13ef63 (the pin of record logged in the timing receipt).',
    noteId: n.note_id,
    title: n.title,
    corpusVersion: n.corpus_version,
    pinnedAt: new Date().toISOString(),
    bodyCharCount: body.length,
    bodySha256: sha256,
    sha256MatchesPinOfRecord: sha256 === 'bf99e22d19c633a0ae64484a3ec090fe8c482545d532d21325077596ad13ef63',
    specPointCodes: sps,
    specPointNodes: sp.rows.map(r => ({ code: r.code, node_type: r.node_type, title: r.title })),
    specJoinStatus: 'HUMAN_VALIDATED (s104 union policy spec map, 2026-09-11) - of record',
    downstreamQuestionCount: Number(q.rows[0].q_count),
    sourceUrl: n.source_url || null,
    rawRowFields: Object.keys(n),
  };
  fs.writeFileSync(`${OUT}/note-pin.json`, JSON.stringify(pin, null, 2));
  console.log(JSON.stringify({
    bodyCharCount: body.length, bodySha256: sha256,
    sha256MatchesPinOfRecord: pin.sha256MatchesPinOfRecord,
    corpusVersion: n.corpus_version, specPointCodes: sps,
    downstreamQuestionCount: pin.downstreamQuestionCount,
    sourceUrl: pin.sourceUrl,
  }, null, 1));
  await c.end();
})().catch(e => { console.error('FAIL:', e.message); process.exit(1); });
