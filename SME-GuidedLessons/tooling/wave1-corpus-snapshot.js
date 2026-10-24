// Wave-1 corpus snapshot: ONE batched read-only pull of the full revision_note corpus.
// Purpose: bring all source note bodies local so the entire instrumented first authoring
// wave (5-10 notes, receipts + declared assistance) runs with ZERO further DB contact —
// per operator note that DB work is ongoing elsewhere (multi-DB re-architecture).
// Lane: t0_readonly, SELECT-only, token never echoed. No writes anywhere.
const fs = require('fs');
const crypto = require('crypto');
const { Client } = require('/home/z/node_modules/pg');

const OUT = '/home/z/my-project/.tmp/wave1';

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const uri = fs.readFileSync('/home/z/my-project/.creds/neon-ro-uri', 'utf8').trim();
  const c = new Client({ connectionString: uri });
  await c.connect();

  const t0 = Date.now();
  const r = await c.query(`
    SELECT note_id, topic_order, topic_title, subtopic_order, subtopic_title,
           note_order, title, body_md, spec_point_codes, corpus_version, source_url,
           octet_length(body_md) AS body_bytes, ingested_at
    FROM revision_note
    ORDER BY topic_order, subtopic_order, note_order`);
  await c.end();
  const elapsedMs = Date.now() - t0;

  const notes = r.rows.map(n => ({
    noteId: n.note_id,
    topicOrder: n.topic_order, topicTitle: n.topic_title,
    subtopicOrder: n.subtopic_order, subtopicTitle: n.subtopic_title,
    noteOrder: n.note_order, title: n.title,
    specPointCodes: n.spec_point_codes ? String(n.spec_point_codes).split(',').map(s => s.trim()).filter(Boolean) : [],
    corpusVersion: n.corpus_version,
    sourceUrl: n.source_url || null,
    bodyChars: n.body_md.length,
    bodySha256: crypto.createHash('sha256').update(n.body_md).digest('hex'),
    body: n.body_md,
  }));

  // Corpus shape of record to verify against (org audit 2026-10-22): 4 topics, 28 subtopics,
  // 112 notes, per-topic counts 40/36/15/21.
  const topics = {};
  for (const n of notes) {
    const k = `T${n.topicOrder}:${n.topicTitle}`;
    (topics[k] = topics[k] || { subtopics: new Set(), notes: 0 });
    topics[k].subtopics.add(`S${n.subtopicOrder}:${n.subtopicTitle}`);
    topics[k].notes++;
  }
  const shape = Object.entries(topics).map(([k, v]) => ({
    topic: k, subtopics: v.subtopics.size, notes: v.notes,
  }));
  const subtopicCount = new Set(notes.map(n => `T${n.topicOrder}:S${n.subtopicOrder}:${n.subtopicTitle}`)).size;

  const manifest = {
    pulledAt: new Date().toISOString(),
    pullElapsedMs: elapsedMs,
    lane: 't0_readonly, SELECT-only, one connection, one query',
    noteCount: notes.length,
    topicCount: shape.length,
    subtopicCount,
    perTopic: shape,
    corpusVersions: [...new Set(notes.map(n => n.corpusVersion))],
    totalBodyChars: notes.reduce((a, n) => a + n.bodyChars, 0),
    verifyAgainstCensusOfRecord: { topics: 4, subtopics: 28, notes: 112, perTopicNotes: [40, 36, 15, 21] },
  };
  fs.writeFileSync(`${OUT}/corpus-snapshot.json`, JSON.stringify({ manifest, notes }, null, 1));
  fs.writeFileSync(`${OUT}/snapshot-manifest.json`, JSON.stringify(manifest, null, 2));
  console.log(JSON.stringify(manifest, null, 1));
})().catch(e => { console.error('FAIL:', e.message); process.exit(1); });
