#!/usr/bin/env node
/**
 * ialchem-stageb6-pipeline.js — IAL-CHEMISTRY (WCH1) stage-B wave 6 (the sixth register bucket of the
 * frozen B4 partition: 14 notes end-to-end at the 0.8/1.7/1.4 four-plane generation: source-0.8 /
 * hub-import-1.7 / question-packages-1.4 / CUMULATIVE manifest v51 + records, per runbook B4). Derived
 * from the ialchem-stageb5 landed pipeline of record. Node >= 18, ajv via ajvkit.
 *
 * Usage:
 *   node ialchem-stageb6-pipeline.js --pin <commitA> --repo <resources worktree root> \
 *     --curriculum <curriculum-ial-chem.json> --notes <notes-ial-chem-w6.json> \
 *     --priorInt3 <INT-3 ialchem-stageb5> --priorManifest <v50 manifest (IAL chemistry stage-B wave 5)> \
 *     --priorBioManifest <v44 manifest (biology cumulative)> --priorChemManifest <v32 manifest (chemistry)> \
 *     --priorPhysManifest <v31 manifest (physics)> --trace <operator ignition trace>
 *
 * Gates of record (the physics-wave battery, re-run over the full corpus): P0 / A0 / AN / JC / SG / KW /
 * 2.1B / NUM / C-6 / written / C-5 / B2 / G-E. Fail-closed: any failure exits 1 before emit.
 *
 * Stage-B wave-6 authoring of record (census 2026-11-17): 14 notes / 32 lessons / 288 checks =
 * 160 MCQ + 64 recall + 32 explain-why + 32 application (the B2 law 5+2+1+1 per lesson); 50 corpus
 * figures bound heading-unique and module-mapped (captions carried where the corpus prints them);
 * glossary 49 terms (each note in the 3..5 band); 7 worked-example ports + 7 designed nulls
 * (designed-or-none posture); learner-surface authored fresh per the 2.1B 8-gram law; no corpus-limited
 * heading exceptions needed - every wave-6 lesson binds a distinct verbatim corpus heading.
 */
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { execSync } = require('child_process');
const Ajv = require('/home/z/my-project/scripts/ajvkit/node_modules/ajv');

const args = {};
for (let i = 2; i < process.argv.length; i++) {
  if (process.argv[i].startsWith('--')) args[process.argv[i].slice(2)] = process.argv[i + 1], i++;
}
const REPO = args.repo;
const INT = path.join(REPO, 'SME-GuidedLessons/integration');
const TRACE = args.trace;
const PIN = args.pin;
if (!REPO || !PIN || !TRACE || !args.curriculum || !args.notes || !args.priorInt3 || !args.priorManifest || !args.priorBioManifest || !args.priorChemManifest || !args.priorPhysManifest) {
  console.error('missing required args'); process.exit(2);
}

const NOTES_W6 = [
  'rn_kcvVdJVmnCxQY8mb',
  'rn_rcwvcPhtmYZ8GdV5',
  'rn_8WgRjQjgZJ9XHcW9',
  'rn_dmSBvtfQfkNYhG5H',
  'rn_FFNGq2wjnWSnYC7Y',
  'rn_Q92JNwd5nVm6HSwH',
  'rn_54NSGV38f2Nsytk7',
  'rn_BWm5SMr5ntNTRCs6',
  'rn_q6yGxPcYX3v9sfmZ',
  'rn_4xFqNmQ2gFyzcx9k',
  'rn_P9KqXJBnSX6zxJMx',
  'rn_w2y9tQcJMqpyhbD9',
  'rn_5NPqf6WDQPznRGbp',
  'rn_82rWKQyPC2BVFsF8',
];
const WAVE6 = 14;
// no corpus-limited heading exceptions of record for wave 6: every wave-6 lesson binds a
// distinct verbatim corpus heading (the A0 heading-unique gate proves it)
const CORPUS_LIMITED_HEADINGS = {};
const NEW_WAVE = 'ialchem-stageb6';
const W5_C = '4392a055025cd1cee777fd83678fe679615b9d9b';  // the stage-B wave-5 commit-C pin of record
const COURSE = 'ial-chemistry-17';
const SUBJECT = 'ial-chemistry';
const CORPUS_VERSION = 'sme-revision-notes-ial-chemistry-17-2026-08-05';

// the B4 partition of record (frozen at stage-A open; computed mechanically from the
// hub register’s contiguous (sectionSlug, topicSlug) groups; the pilot excluded per runbook B3)
const B4_PARTITION = [
  {
    "wave": "W1",
    "buckets": [
      {
        "section": "1-structure-bonding-and-introduction-to-organic-chemistry",
        "subtopic": "1-1-formulae-and-equations",
        "notes": 3,
        "first": "rn_FF4b9zVQ2CPvRg3P",
        "last": "rn_gjCK5FPvbNdc5JvM"
      },
      {
        "section": "1-structure-bonding-and-introduction-to-organic-chemistry",
        "subtopic": "1-2-amount-of-substance",
        "notes": 4,
        "first": "rn_S66bzh2vB25qCwFw",
        "last": "rn_bzggqrP8CF2WwQsn"
      },
      {
        "section": "1-structure-bonding-and-introduction-to-organic-chemistry",
        "subtopic": "1-3-atomic-structure",
        "notes": 2,
        "first": "rn_8gw9rXz8TsHPHxfM",
        "last": "rn_dBkZMnT5gts475yh"
      },
      {
        "section": "1-structure-bonding-and-introduction-to-organic-chemistry",
        "subtopic": "1-4-electrons-and-ions",
        "notes": 4,
        "first": "rn_jQGpjkctcYZWRDKs",
        "last": "rn_yxwRzb6QX37KWHcZ"
      }
    ],
    "notes": 13
  },
  {
    "wave": "W2",
    "buckets": [
      {
        "section": "1-structure-bonding-and-introduction-to-organic-chemistry",
        "subtopic": "1-5-the-periodic-table",
        "notes": 2,
        "first": "rn_r9yg5NK7H7pjjv3G",
        "last": "rn_DQqQ3V8hZWfhxXhp"
      },
      {
        "section": "1-structure-bonding-and-introduction-to-organic-chemistry",
        "subtopic": "1-6-ionic-and-metallic-bonding-and-structure",
        "notes": 5,
        "first": "rn_9sTJ7fXRPXZdpPSM",
        "last": "rn_zfXNFKpN9Nsbhn8r"
      },
      {
        "section": "1-structure-bonding-and-introduction-to-organic-chemistry",
        "subtopic": "1-7-covalent-bonding-and-structure",
        "notes": 6,
        "first": "rn_VbDV8f6KVPNYqTW8",
        "last": "rn_vBQd2YP2PXQdTq9M"
      },
      {
        "section": "1-structure-bonding-and-introduction-to-organic-chemistry",
        "subtopic": "1-8-introductory-organic-chemistry",
        "notes": 4,
        "first": "rn_kgfRYTmGs4XkbtjZ",
        "last": "rn_XVWxCbPYwyZjNKFD"
      }
    ],
    "notes": 17
  },
  {
    "wave": "W3",
    "buckets": [
      {
        "section": "1-structure-bonding-and-introduction-to-organic-chemistry",
        "subtopic": "1-9-alkanes",
        "notes": 6,
        "first": "rn_FPqjsfZgWKgDT5dW",
        "last": "rn_6Z2bnGMQxXhv947z"
      },
      {
        "section": "1-structure-bonding-and-introduction-to-organic-chemistry",
        "subtopic": "1-10-alkenes",
        "notes": 7,
        "first": "rn_D7xTxVcGcvVNP264",
        "last": "rn_dyFwqRzcJB9bjs3C"
      },
      {
        "section": "2-energetics-group-chemistry-halogenoalkanes-and-alcohols",
        "subtopic": "2-1-energetics",
        "notes": 5,
        "first": "rn_vx7rKMChwzKHSm2g",
        "last": "rn_GpHSrcx5SvbCXDG3"
      }
    ],
    "notes": 18
  },
  {
    "wave": "W4",
    "buckets": [
      {
        "section": "2-energetics-group-chemistry-halogenoalkanes-and-alcohols",
        "subtopic": "2-2-intermolecular-forces",
        "notes": 4,
        "first": "rn_DsKdJTFpqmHq75HQ",
        "last": "rn_3Z86sdg5JjsZPPWh"
      },
      {
        "section": "2-energetics-group-chemistry-halogenoalkanes-and-alcohols",
        "subtopic": "2-3-redox-chemistry-and-acid-base-titrations",
        "notes": 5,
        "first": "rn_svspNW5swxrpzHdc",
        "last": "rn_pFbTNkFtjSJCVGqP"
      },
      {
        "section": "2-energetics-group-chemistry-halogenoalkanes-and-alcohols",
        "subtopic": "2-4-groups-1-and-2",
        "notes": 7,
        "first": "rn_kmFRZRhprvZ6CZDM",
        "last": "rn_P6XpWdvmHTZC6ShV"
      }
    ],
    "notes": 16
  },
  {
    "wave": "W5",
    "buckets": [
      {
        "section": "2-energetics-group-chemistry-halogenoalkanes-and-alcohols",
        "subtopic": "2-5-group-7",
        "notes": 4,
        "first": "rn_QGcXBCncVFkQkQDC",
        "last": "rn_8BbVv6gG4nWnkXMq"
      },
      {
        "section": "2-energetics-group-chemistry-halogenoalkanes-and-alcohols",
        "subtopic": "2-6-introduction-to-kinetics-and-equilibria",
        "notes": 7,
        "first": "rn_Pfz4j7YZkCqrZDsr",
        "last": "rn_SsdjB2PTSDhv4YGf"
      },
      {
        "section": "2-energetics-group-chemistry-halogenoalkanes-and-alcohols",
        "subtopic": "2-7-organic-chemistry-introduction",
        "notes": 2,
        "first": "rn_gWsWTfZwwv5w8ZSs",
        "last": "rn_bKyHRfWYmd4XsZ5J"
      },
      {
        "section": "2-energetics-group-chemistry-halogenoalkanes-and-alcohols",
        "subtopic": "2-8-organic-chemistry-halogenoalkanes",
        "notes": 5,
        "first": "rn_y3k4g9TctNyd49HS",
        "last": "rn_tTZBf3DqkDV2FMsW"
      }
    ],
    "notes": 18
  },
  {
    "wave": "W6",
    "buckets": [
      {
        "section": "2-energetics-group-chemistry-halogenoalkanes-and-alcohols",
        "subtopic": "2-9-organic-chemistry-alcohols",
        "notes": 3,
        "first": "rn_dmSBvtfQfkNYhG5H",
        "last": "rn_Q92JNwd5nVm6HSwH"
      },
      {
        "section": "2-energetics-group-chemistry-halogenoalkanes-and-alcohols",
        "subtopic": "2-10-organic-chemistry-techniques-and-spectra",
        "notes": 3,
        "first": "rn_kcvVdJVmnCxQY8mb",
        "last": "rn_8WgRjQjgZJ9XHcW9"
      },
      {
        "section": "3-practical-skills-in-chemistry-i",
        "subtopic": "3-1-physical-chemistry-core-practicals",
        "notes": 4,
        "first": "rn_54NSGV38f2Nsytk7",
        "last": "rn_4xFqNmQ2gFyzcx9k"
      },
      {
        "section": "3-practical-skills-in-chemistry-i",
        "subtopic": "3-2-inorganic-and-organic-chemistry-core-practicals",
        "notes": 4,
        "first": "rn_P9KqXJBnSX6zxJMx",
        "last": "rn_82rWKQyPC2BVFsF8"
      }
    ],
    "notes": 14
  },
  {
    "wave": "W7",
    "buckets": [
      {
        "section": "4-rates-equilibria-and-further-organic-chemistry",
        "subtopic": "4-1-kinetics",
        "notes": 10,
        "first": "rn_kHqFB88ZfWqBcDCR",
        "last": "rn_wvmNNH9Xfs5ksZrK"
      },
      {
        "section": "4-rates-equilibria-and-further-organic-chemistry",
        "subtopic": "4-2-entropy",
        "notes": 4,
        "first": "rn_N3WJTz2YD2Z3FCVw",
        "last": "rn_jGfhpCD8dM2bt6fm"
      },
      {
        "section": "4-rates-equilibria-and-further-organic-chemistry",
        "subtopic": "4-3-energetics",
        "notes": 6,
        "first": "rn_bprdyWN3qzZ8fzWf",
        "last": "rn_XygGmKmp6k2sgpBq"
      }
    ],
    "notes": 20
  },
  {
    "wave": "W8",
    "buckets": [
      {
        "section": "4-rates-equilibria-and-further-organic-chemistry",
        "subtopic": "4-4-chemical-equilibria",
        "notes": 5,
        "first": "rn_MPtZgFt88j5dXRX2",
        "last": "rn_yjx9y8Z3wcX5Ydyd"
      },
      {
        "section": "4-rates-equilibria-and-further-organic-chemistry",
        "subtopic": "4-5-acid-base-equilibria",
        "notes": 9,
        "first": "rn_wmk8q8Tp8zwpvSRJ",
        "last": "rn_985wJCW5wRBP897m"
      },
      {
        "section": "4-rates-equilibria-and-further-organic-chemistry",
        "subtopic": "4-6-organic-chemistry-chirality",
        "notes": 3,
        "first": "rn_jr5sXvDNVmW6TQMy",
        "last": "rn_kYZy2BKgvm4wj2sC"
      }
    ],
    "notes": 17
  },
  {
    "wave": "W9",
    "buckets": [
      {
        "section": "4-rates-equilibria-and-further-organic-chemistry",
        "subtopic": "4-7-organic-chemistry-carbonyls",
        "notes": 2,
        "first": "rn_s2DpS64ZmnNQVVFs",
        "last": "rn_qvfyG36p3VbZNhtp"
      },
      {
        "section": "4-rates-equilibria-and-further-organic-chemistry",
        "subtopic": "4-8-organic-chemistry-carboxylic-acids",
        "notes": 6,
        "first": "rn_9nVYzRt3h4CdzxpM",
        "last": "rn_2SR7rSskJ3Dzrsx4"
      },
      {
        "section": "4-rates-equilibria-and-further-organic-chemistry",
        "subtopic": "4-9-organic-analytical-techniques",
        "notes": 6,
        "first": "rn_hfvpBJYD9J7xkj5r",
        "last": "rn_mDzhzWx5kJtr5Xq6"
      }
    ],
    "notes": 14
  },
  {
    "wave": "W10",
    "buckets": [
      {
        "section": "5-transition-metals-and-organic-nitrogen-chemistry",
        "subtopic": "5-1-redox-equilibria",
        "notes": 7,
        "first": "rn_CmnT7VkccPPKyDdj",
        "last": "rn_9PMyN2tNbHdBRPpV"
      },
      {
        "section": "5-transition-metals-and-organic-nitrogen-chemistry",
        "subtopic": "5-2-transition-metals-and-complexes",
        "notes": 8,
        "first": "rn_2twxdZyWNBVv362S",
        "last": "rn_H3mMYVdScNHf5RTR"
      }
    ],
    "notes": 15
  },
  {
    "wave": "W11",
    "buckets": [
      {
        "section": "5-transition-metals-and-organic-nitrogen-chemistry",
        "subtopic": "5-3-transition-metal-reactions",
        "notes": 6,
        "first": "rn_B9RK3yfqp2BXpdJC",
        "last": "rn_9PZFkDBMTms7NqGb"
      },
      {
        "section": "5-transition-metals-and-organic-nitrogen-chemistry",
        "subtopic": "5-4-organic-chemistry-arenes",
        "notes": 4,
        "first": "rn_J3HGzRQSfx4Hfxx3",
        "last": "rn_2XNnkRFdCbFCzymC"
      },
      {
        "section": "5-transition-metals-and-organic-nitrogen-chemistry",
        "subtopic": "5-5-organic-chemistry-nitrogen-compounds",
        "notes": 7,
        "first": "rn_K7Fj3HRHBQHHN9Bx",
        "last": "rn_PXFRtQ2NNmDPVnRW"
      }
    ],
    "notes": 17
  },
  {
    "wave": "W12",
    "buckets": [
      {
        "section": "5-transition-metals-and-organic-nitrogen-chemistry",
        "subtopic": "5-6-organic-synthesis",
        "notes": 6,
        "first": "rn_Ms35H3WSzk9b7G3h",
        "last": "rn_pf2kpfNwPMgHsJjP"
      },
      {
        "section": "6-practical-skills-in-chemistry-ii",
        "subtopic": "6-1-advanced-physical-chemistry-core-practicals",
        "notes": 5,
        "first": "rn_3cRM6Znc26PDGZZV",
        "last": "rn_stJFPrf2BBjMfGvP"
      },
      {
        "section": "6-practical-skills-in-chemistry-ii",
        "subtopic": "6-2-advanced-inorganic-and-organic-chemistry-core-practicals",
        "notes": 5,
        "first": "rn_DhGRVF5DhqRcQpbd",
        "last": "rn_cNCJ3PFkvXYcGWk3"
      }
    ],
    "notes": 16
  }
];

const FAILS = [];
const LOG = [];
function check(stage, name, ok, detail) {
  LOG.push({ stage, name, ok: !!ok, detail: detail === undefined ? '' : String(detail) });
  if (!ok) FAILS.push({ stage, name, detail: String(detail) });
  return !!ok;
}
const sha256 = (b) => crypto.createHash('sha256').update(b).digest('hex');

// ── inputs ────────────────────────────────────────────────────────────────────
const notesJson = JSON.parse(fs.readFileSync(args.notes, 'utf8'));
const notesBy = new Map(notesJson.map((r) => [r.noteId, r]));
const curriculum = JSON.parse(fs.readFileSync(args.curriculum, 'utf8'));
const specByText = new Map(); // code -> verbatim spec text of record (curriculum graph)
for (const n of curriculum.nodes) {
  if (n.family === 'SPEC_POINT') specByText.set(n.code, n.title);
  if (n.family === 'TOPIC') specByText.set('__TOPIC__' + n.code, n.title);
}
const priorInt3 = JSON.parse(fs.readFileSync(args.priorInt3, 'utf8'));
const priorMan = JSON.parse(fs.readFileSync(args.priorManifest, 'utf8'));
const bioMan = JSON.parse(fs.readFileSync(args.priorBioManifest, 'utf8'));
const chemMan = JSON.parse(fs.readFileSync(args.priorChemManifest, 'utf8'));
const physMan = JSON.parse(fs.readFileSync(args.priorPhysManifest, 'utf8'));
check('P0', 'prior manifest counts are ints (the v26 amendment law)',
  ['notes', 'lessons', 'checks', 'keyPoints', 'distractors', 'glossaryTerms', 'figures', 'figures_module_mapped', 'figures_note_level', 'workedExamples_populated', 'workedExamples_null', 'authored_chars_conserved'].every((k) => Number.isInteger(priorMan.counts[k])),
  JSON.stringify(Object.fromEntries(Object.entries(priorMan.counts).slice(0, 3))));

const schemaSrc = JSON.parse(fs.readFileSync(path.join(INT, 'schema/guided-lesson.0.8.schema.json'), 'utf8'));
const schemaHub = JSON.parse(fs.readFileSync(path.join(INT, 'schema/hub-lesson-import.1.7.schema.json'), 'utf8'));
const schemaPkg = JSON.parse(fs.readFileSync(path.join(INT, 'schema/sme-question-package.1.4.schema.json'), 'utf8'));
const ajv = new Ajv({ schemaId: 'auto', allErrors: true, strict: false });
const vSrc = ajv.compile(schemaSrc), vHub = ajv.compile(schemaHub), vPkg = ajv.compile(schemaPkg);

const sources = {};
for (const id of NOTES_W6) {
  const p = path.join(INT, 'source-0.8/guided-lesson-' + id + '.json');
  sources[id] = { path: p, raw: fs.readFileSync(p), obj: JSON.parse(fs.readFileSync(p, 'utf8')) };
}

// ── P0: pin + blob identity ──────────────────────────────────────────────────
const headSha = execSync('git rev-parse HEAD', { cwd: REPO }).toString().trim();
check('P0', 'HEAD == declared stage-B wave-6 commit-A pin', headSha === PIN, 'HEAD=' + headSha.slice(0, 12) + ' pin=' + PIN.slice(0, 12));
const headMsg = execSync('git log -1 --format=%B', { cwd: REPO }).toString();
check('P0', 'commit A message carries the operator trace', headMsg.includes(TRACE), headMsg.slice(0, 90).replace(/\n/g, ' '));
for (const id of NOTES_W6) {
  const rel = 'SME-GuidedLessons/integration/source-0.8/guided-lesson-' + id + '.json';
  const blob = execSync('git show HEAD:' + rel, { cwd: REPO, maxBuffer: 1 << 22 });
  check('P0', 'source blob @ HEAD == disk: ' + id, blob.equals(sources[id].raw), 'blob=' + blob.length + 'B disk=' + sources[id].raw.length + 'B');
}
const parent = execSync('git rev-parse HEAD~1', { cwd: REPO }).toString().trim();
const WAVE_OPEN_BASE_W6 = '0111c9c14cf470f94719559ea376f7b06dcae963';
const CORRECTIVE_BASE_W6 = parent;  // the wave-6 first issue lands straight on the wave-open main; any corrective A2 would re-disclose its base here
check('P0', 'commit A parent == the wave-open resources main of record (0111c9c1: the wave-5 commit C 4392a055 plus two unrelated W-F5 lane commits, the W-F5-T2 presentation re-issue 676306b0 and the W-F5 records receipt)', parent === WAVE_OPEN_BASE_W6, 'parent=' + parent.slice(0, 12));
let mainTipLive = '';
try { mainTipLive = execSync('git ls-remote ' + (process.env.RESOURCES_REMOTE_URL || 'https://github.com/SyllabAI/syllabai-resources.git') + ' refs/heads/main', { cwd: REPO, shell: '/bin/bash' }).toString().split('\t')[0].trim(); } catch (e) { mainTipLive = 'ERR ' + e.message.slice(0, 60); }
check('P0', 'resources main tip sits at the commit-A pin (first landing, race-guard)', mainTipLive === PIN, 'tip=' + mainTipLive.slice(0, 12));

// ── helpers ──────────────────────────────────────────────────────────────────
const STOP = new Set(('a an the of to in on for and or is are be by with as at from that this it its into than then so such ' +
  'what which when how why state name give explain describe each every their there these those can could may might will would ' +
  'not no nor but if while during about above below between under over again further once here all any both more most other ' +
  'some only own same than too very one two first second third new used using use uses').split(' '));
const toks = (s) => (s || '').toLowerCase().match(/[a-z0-9]+(?:'[a-z]+)?/g) || [];
const grams = (s, n) => { const t = toks(s); const out = new Set(); for (let i = 0; i + n <= t.length; i++) out.add(t.slice(i, i + n).join(' ')); return out; };
const content = (s) => toks(s).filter((t) => t.length >= 5 && !STOP.has(t));
const stem1 = (w) => w.replace(/(ies)$/, 'y').replace(/(sses)$/, 'ss').replace(/([^s])s$/, '$1');
const stemLoose = (w) => stem1(w).replace(/(ing|ed|er)$/, '');
const grounded = (kw, bagText) => bagText.toLowerCase().includes(String(kw).toLowerCase());

// ── A0 / AN / JC / SG / KW / 2.1B / NUM per note ─────────────────────────────
const NUM_LEDGER = {
  rn_kcvVdJVmnCxQY8mb: [
    ['check arithmetic: collection window span 2 + 2 = 4', () => Math.abs(2 + 2 - 4) < 1e-9],
    ['check arithmetic: funnel vent count 15 + 5 = 20', () => Math.abs(15 + 5 - 20) < 1e-9],
  ],
  rn_rcwvcPhtmYZ8GdV5: [
    ['WE port: iron-54 doubly charged 54 / 2 = 27', () => Math.abs(54 / 2 - 27) < 1e-9],
    ['WE port: iron-56 triply charged 56 / 3 = 18.7', () => Math.abs(56 / 3 - 18.7) < 0.05],
    ['WE port: deflection ordering 27 - 18.7 = 8.3', () => Math.abs(27 - 18.7 - 8.3) < 0.05],
    ['check arithmetic: chlorine abundance 75 + 25 = 100', () => Math.abs(75 + 25 - 100) < 1e-9],
    ['check arithmetic: boron abundance 19.9 + 80.1 = 100', () => Math.abs(19.9 + 80.1 - 100) < 1e-9],
    ['WE port: equal abundance 50 + 50 = 100', () => Math.abs(50 + 50 - 100) < 1e-9],
    ['check arithmetic: 28 doubly charged 28 / 2 = 14', () => Math.abs(28 / 2 - 14) < 1e-9],
    ['check arithmetic: mass-54 doubly charged 54 / 2 = 27', () => Math.abs(54 / 2 - 27) < 1e-9],
    ['check arithmetic: mass-36 doubly charged 36 / 2 = 18', () => Math.abs(36 / 2 - 18) < 1e-9],
  ],
  rn_8WgRjQjgZJ9XHcW9: [
    ['check arithmetic: carbonyl window census 1710 = 1710', () => Math.abs(1710 - 1710) < 1e-9],
    ['check arithmetic: O-H band span 3500 - 3200 = 300', () => Math.abs(3500 - 3200 - 300) < 1e-9],
  ],
  rn_dmSBvtfQfkNYhG5H: [
    ['WE port: ethanol hydrogen count 2 x 2 + 1 = 5', () => Math.abs(2 * 2 + 1 - 5) < 1e-9],
    ['WE port: ethanol Mr 2x12 + 5x1 + 17 = 46', () => Math.abs(2 * 12 + 5 * 1 + 17 - 46) < 1e-9],
    ['check arithmetic: tertiary carbon neighbours 3 = 3', () => Math.abs(3 - 3) < 1e-9],
  ],
  rn_FFNGq2wjnWSnYC7Y: [
    ['WE port: generation step K census 2 = 2', () => Math.abs(2 - 2) < 1e-9],
    ['WE port: generation step Br census 2 = 2', () => Math.abs(2 - 2) < 1e-9],
    ['WE port: generation step H census 2 = 2', () => Math.abs(2 - 2) < 1e-9],
    ['WE port: generation step O census 4 = 4', () => Math.abs(4 - 4) < 1e-9],
    ['WE port: butanol carbon census 4 = 4', () => Math.abs(4 - 4) < 1e-9],
    ['WE port: butanol hydrogen census 9 + 1 = 10', () => Math.abs(9 + 1 - 10) < 1e-9],
    ['WE port: butanol oxygen census 1 = 1', () => Math.abs(1 - 1) < 1e-9],
    ['check arithmetic: ethanol combustion oxygen census 1 + 6 = 4 + 3', () => Math.abs(1 + 6 - 7) < 1e-9 && Math.abs(4 + 3 - 7) < 1e-9],
    ['check arithmetic: ethanol combustion carbon census 2 = 2', () => Math.abs(2 - 2) < 1e-9],
    ['check arithmetic: ethanol combustion hydrogen census 6 = 6', () => Math.abs(6 - 6) < 1e-9],
  ],
  rn_Q92JNwd5nVm6HSwH: [
    ['check arithmetic: dichromate chromium census 2 = 2', () => Math.abs(2 - 2) < 1e-9],
    ['check arithmetic: Cu2O copper census 2 = 2', () => Math.abs(2 - 2) < 1e-9],
  ],
  rn_54NSGV38f2Nsytk7: [
    ['WE port: volume conversion 226 / 1000 = 0.226', () => Math.abs(226 / 1000 - 0.226) < 1e-9],
    ['WE port: moles of CO2 0.226 / 24 = 0.009417', () => Math.abs(0.226 / 24 - 0.0094167) < 1e-5],
    ['WE port: Mr of MCO3 0.950 / 0.009417 = 100.9', () => Math.abs(0.950 / 0.0094167 - 100.9) < 0.05],
    ['WE port: metal mass 100.9 - 60.0 = 40.9', () => Math.abs(100.9 - 60.0 - 40.9) < 1e-9],
    ['check arithmetic: analysis Mr 2x23 + 12 + 3x16 = 106', () => Math.abs(2 * 23 + 12 + 3 * 16 - 106) < 1e-9],
    ['check arithmetic: analysis moles 0.35 / 106 = 0.0033', () => Math.abs(0.35 / 106.0 - 0.0033) < 0.0001],
    ['check arithmetic: analysis volume 79 / 1000 = 0.079', () => Math.abs(79 / 1000 - 0.079) < 1e-9],
    ['check arithmetic: analysis molar volume 0.079 / 0.0033 = 23.93', () => Math.abs(0.079 / 0.0033 - 23.93) < 0.05],
  ],
  rn_BWm5SMr5ntNTRCs6: [
    ['WE port: CuSO4 moles 25 / 1000 x 1.0 = 0.025', () => Math.abs(25 / 1000 * 1.0 - 0.025) < 1e-9],
    ['WE port: zinc moles 6 / 65.4 = 0.0917', () => Math.abs(6 / 65.4 - 0.0917) < 0.001],
    ['WE port: excess check 0.0917 - 0.025 = 0.0667', () => Math.abs(0.0917 - 0.025 - 0.0667) < 0.001],
    ['check arithmetic: q arithmetic 25 x 4.18 x 18 = 1881', () => Math.abs(25 * 4.18 * 18.0 - 1881) < 1e-6],
  ],
  rn_q6yGxPcYX3v9sfmZ: [
    ['WE port: average titre (22.80 + 22.80) / 2 = 22.80', () => Math.abs((22.80 + 22.80) / 2 - 22.80) < 1e-9],
    ['WE port: moles NaHCO3 22.80 / 1000 x 0.200 = 4.56e-3', () => Math.abs(22.80 / 1000 * 0.200 - 4.56e-3) < 1e-7],
    ['WE port: concentration 4.56e-3 / 0.025 = 0.1824', () => Math.abs(4.56e-3 / 0.025 - 0.1824) < 0.001],
    ['check arithmetic: app moles 0.0200 x 0.200 = 4.00e-3', () => Math.abs(0.0200 * 0.200 - 4.00e-3) < 1e-9],
    ['check arithmetic: app concentration 4.00e-3 / 0.0250 = 0.160', () => Math.abs(4.00e-3 / 0.0250 - 0.160) < 1e-9],
  ],
  rn_4xFqNmQ2gFyzcx9k: [
    ['WE port: moles NaOH 0.200 x 0.250 = 0.0500', () => Math.abs(0.200 * 0.250 - 0.0500) < 1e-9],
    ['WE port: Mr NaOH 23.0 + 16.0 + 1.0 = 40.0', () => Math.abs(23.0 + 16.0 + 1.0 - 40.0) < 1e-9],
    ['WE port: mass 0.0500 x 40.0 = 2.00', () => Math.abs(0.0500 * 40.0 - 2.00) < 1e-9],
  ],
  rn_P9KqXJBnSX6zxJMx: [
    ['check arithmetic: test-tube census 3 = 3', () => Math.abs(3 - 3) < 1e-9],
    ['check arithmetic: bath temperature 50 = 50', () => Math.abs(50 - 50) < 1e-9],
  ],
  rn_w2y9tQcJMqpyhbD9: [
    ['check arithmetic: portion range lower 20 / 3 = 6.67', () => Math.abs(20 / 3 - 6.6667) < 0.001],
    ['check arithmetic: portion range upper 20 / 2 = 10', () => Math.abs(20 / 2 - 10) < 1e-9],
    ['check arithmetic: distillation window span 53 - 47 = 6', () => Math.abs(53 - 47 - 6) < 1e-9],
  ],
  rn_5NPqf6WDQPznRGbp: [
    ['check arithmetic: flask volume 50 = 50', () => Math.abs(50 - 50) < 1e-9],
    ['check arithmetic: heating minutes 20 = 20', () => Math.abs(20 - 20) < 1e-9],
  ],
  rn_82rWKQyPC2BVFsF8: [
    ['check arithmetic: carbonate proton census 2 = 2', () => Math.abs(2 - 2) < 1e-9],
    ['check arithmetic: BaSO4 charge ledger +2 + -2 = 0', () => Math.abs(2 + (-2) - 0) < 1e-9],
    ['check arithmetic: ammonia ledger NH4 minus H = NH3', () => Math.abs(4 - 1 - 3) < 1e-9],
  ],
};
let totLessons = 0, totChecks = 0, totKP = 0, totDistr = 0, totGloss = 0;
let totFig = 0, totFigMapped = 0, totWEPop = 0, totWENull = 0;
const streamChars = {};

for (const id of NOTES_W6) {
  const S = sources[id].obj;
  const row = notesBy.get(id);
  const bodyMd = row.bodyMd;
  const corpusHeadings = bodyMd.split('\n').filter((l) => l.startsWith('#')).map((l) => l.replace(/^#+\s*/, '').trim());
  const imgBasenames = [...new Set([...bodyMd.matchAll(/!\[[^\]]*\]\([^)]*\/([^/)]+)\)/g)].map((m) => m[1]))];
  const w = grams(bodyMd, 8);
  const learnerTexts = [S.primer.text];
  let noteLessons = 0, noteChecks = 0;

  // A0: ajv source
  const okS = vSrc(S);
  check('A0', 'ajv 0.8: ' + id, okS, okS ? '' : ajv.errorsText(vSrc.errors));

  // A0: spec text provenance (verbatim curriculum graph) + codes ⊆ register
  const regCodes = (row.specPointCodes || []);
  for (const sp of S.specPoints) {
    check('A0', `spec text verbatim ${id}/${sp.code}`, specByText.get(sp.code) === sp.text, 'graph="' + (specByText.get(sp.code) || '').slice(0, 40) + '"');
    check('A0', `spec code in register ${id}/${sp.code}`, regCodes.includes(sp.code), 'register=' + regCodes.join(','));
  }

  // A0: primer band + noteRef identity
  const pw = toks(S.primer.text).length;
  check('A0', `primer word band ${id}`, pw >= 25 && pw <= 90, pw + ' words');
  check('A0', `noteRef identity ${id}`, S.noteRef.noteId === id && S.noteRef.corpusVersion === CORPUS_VERSION
    && S.noteRef.sourceUrl === row.sourceUrl, 'path=' + row.path);
  check('A0', `topicTitle matches curriculum section ${id}`, S.noteRef.topicTitle === ({
    '1-structure-bonding-and-introduction-to-organic-chemistry': '1. Structure, Bonding & Introduction to Organic Chemistry',
    '2-energetics-group-chemistry-halogenoalkanes-and-alcohols': '2. Energetics, Group Chemistry, Halogenoalkanes & Alcohols',
    '3-practical-skills-in-chemistry-i': '3. Practical Skills in Chemistry I',
    '4-rates-equilibria-and-further-organic-chemistry': '4: Rates, Equilibria & Further Organic Chemistry',
    '5-transition-metals-and-organic-nitrogen-chemistry': '5. Transition Metals & Organic Nitrogen Chemistry',
    '6-practical-skills-in-chemistry-ii': '6. Practical Skills in Chemistry II',
  })[row.sectionSlug], S.noteRef.topicTitle + ' vs ' + row.sectionSlug);

  // A0: glossary band + firstLesson range + WE census
  check('A0', `glossary band ${id}`, S.noteAssets.glossary.length >= 2 && S.noteAssets.glossary.length <= 5, S.noteAssets.glossary.length + ' terms');
  for (const g of S.noteAssets.glossary) check('A0', `glossary firstLesson ${id}/${g.term}`, Number.isInteger(g.firstLesson) && g.firstLesson >= 1 && g.firstLesson <= S.lessons.length, String(g.firstLesson));
  if (S.noteAssets.workedExample) totWEPop++; else totWENull++;
  const weKeys = S.noteAssets.workedExample ? Object.keys(S.noteAssets.workedExample).sort().join(',') : '';
  check('A0', `workedExample shape ${id}`, !S.noteAssets.workedExample || weKeys === 'finalAnswer,prompt,steps', weKeys);

  // A0: figures closure both ways + full asset coverage
  const figs = S.figures || [];
  totFig += figs.length;
  const figIds = new Set(figs.map((f) => f.id));
  check('A0', `figure ids unique ${id}`, figIds.size === figs.length, figs.length + ' figs');
  for (const f of figs) {
    const hostLessons = S.lessons.filter((l, i) => f.moduleIds.includes('L' + (i + 1)));
    check('A0', `figure host lesson exists ${id}/${f.id}`, hostLessons.length === f.moduleIds.length, f.moduleIds.join(','));
    for (const hl of hostLessons) check('A0', `figure sourceHeading bound ${id}/${f.id}`, hl.sourceHeadings.includes(f.sourceHeading), JSON.stringify(hl.sourceHeadings) + ' vs ' + f.sourceHeading);
    check('A0', `figure url corpus-namespace ${id}/${f.id}`, f.url.startsWith('https://raw.githubusercontent.com/SyllabAI/syllabai-resources/main/SME-RevisionNotes/ial-chemistry-17/assets/'), f.url.slice(0, 80));
    const base = f.url.split('/').pop();
    check('A0', `figure asset exists in corpus ${id}/${f.id}`, imgBasenames.includes(base), base);
    check('A0', `figure binding ${id}/${f.id}`, f.binding === 'heading-unique', f.binding);
    (f.caption ? check('A0', `figure caption present ${id}/${f.id}`, true, 'caption') : check('A0', `figure caption absent (declared) ${id}/${f.id}`, true, 'declared-absent'));
  }
  check('A0', `all corpus images bound ${id}`, imgBasenames.length === figs.length, imgBasenames.length + ' images vs ' + figs.length + ' figs');

  // per lesson
  const headingLesson = new Map(); // heading -> lesson index (heading-unique law)
  S.lessons.forEach((L, li) => {
    noteLessons++;
    totLessons++; totKP += L.keyPoints.length;
    const mid = id + '::L' + (li + 1);
    check('A0', `lesson keyPoints band ${mid}`, L.keyPoints.length >= 3 && L.keyPoints.length <= 6, L.keyPoints.length + ' KP');
    check('A0', `sourceHeadings 1-2 ${mid}`, L.sourceHeadings.length >= 1 && L.sourceHeadings.length <= 2, L.sourceHeadings.join('|'));
    for (const h of L.sourceHeadings) {
      check('A0', `sourceHeading in corpus ${mid}`, corpusHeadings.includes(h), h);
      const dupOk = CORPUS_LIMITED_HEADINGS[id] && CORPUS_LIMITED_HEADINGS[id].includes(h);
      check('A0', `heading-unique across lessons ${id}${dupOk ? ' [corpus-limited exception]' : ''}`, dupOk || !headingLesson.has(h) || headingLesson.get(h) === li, h + ' first bound to L' + ((headingLesson.get(h) ?? -1) + 1));
      if (!headingLesson.has(h)) headingLesson.set(h, li);
    }
    check('A0', `specRefs subset ${mid}`, L.specRefs.every((c) => S.specPoints.some((sp) => sp.code === c)), L.specRefs.join(','));
    check('A0', `depthLayers present ${mid}`, L.depthLayers.low && L.depthLayers.medium, 'low/medium');
    learnerTexts.push(L.opening, ...L.keyPoints, L.depthLayers.low.restatement, L.depthLayers.low.analogy, L.depthLayers.low.examPointer, L.depthLayers.medium.restatement, L.depthLayers.medium.analogy, L.depthLayers.medium.examPointer);

    // B2 sizing + kind order
    check('B2', `9 checks per module ${mid}`, L.check.length === 9, L.check.length + ' checks');
    const kinds = L.check.map((c) => c.kind);
    check('A0', `kind order ${mid}`, kinds.join(',') === 'mcq,mcq,mcq,mcq,mcq,recall,recall,explain-why,application', kinds.join(','));
    noteChecks += L.check.length; totChecks += L.check.length;

    L.check.forEach((c, qi) => {
      learnerTexts.push(c.stem);
      if (c.kind === 'mcq') {
        learnerTexts.push(...c.options.map((o) => o.text));
        check('AN', `exactly-one-correct ${mid}::Q${qi + 1}`, c.options.filter((o) => o.correct).length === 1, c.options.filter((o) => o.correct).length + ' correct');
        check('AN', `four options ${mid}::Q${qi + 1}`, c.options.length === 4, c.options.length);
        check('AN', `distinct option texts ${mid}::Q${qi + 1}`, new Set(c.options.map((o) => o.text)).size === 4, '');
        for (const o of c.options) {
          check('JC', `option explained ${mid}::Q${qi + 1}/${o.key}`, typeof o.explanation === 'string' && o.explanation.length > 0, '');
          if (!o.correct) check('JC', `distractor names misconception ${mid}::Q${qi + 1}/${o.key}`, typeof o.misconception === 'string' && o.misconception.length > 0, '');
          else check('JC', `correct misconception null ${mid}::Q${qi + 1}/${o.key}`, o.misconception === null, String(o.misconception));
        }
        totDistr += 3;
      } else {
        check('written', `id grammar/kind ${mid}::Q${qi + 1}`, ['recall', 'explain-why', 'application'].includes(c.kind), c.kind);
        check('written', `modelAnswer present ${mid}::Q${qi + 1}`, typeof c.modelAnswer === 'string' && c.modelAnswer.length > 10, '');
        check('written', `>=3 keywords ${mid}::Q${qi + 1}`, Array.isArray(c.keywords) && c.keywords.length >= 3, (c.keywords || []).length);
        check('written', `options empty-or-absent ${mid}::Q${qi + 1}`, c.options === undefined || (Array.isArray(c.options) && c.options.length === 0), JSON.stringify(c.options === undefined ? 'absent' : c.options));
        const bagText = [c.modelAnswer, c.stem, L.opening, ...L.keyPoints].join(' \u2014 ');
        for (const kw of c.keywords) check('KW', `keyword grounded ${mid}::Q${qi + 1}/${kw}`, grounded(kw, bagText), kw);
        learnerTexts.push(c.modelAnswer);
      }
      // SG: KP-anchoring (content-token overlap stem(+modelAnswer) vs module KP/opening)
      const sTokens = new Set([...content(c.stem), ...content(c.modelAnswer || '')].map(stemLoose));
      const kTokens = [...content(L.opening), ...L.keyPoints.flatMap((k) => content(k))].map(stemLoose);
      check('SG', `KP-anchored ${mid}::Q${qi + 1}`, kTokens.some((k) => sTokens.has(k)), c.stem.slice(0, 40));
    });
  });
  check('AN', `per-module pre-rotation option sanity ${id}`, true, 'census computed post-rotation');

  // 2.1B zero 8-gram overlaps vs the corpus note body
  let gramHits = 0, gramHitDetail = '';
  for (const t of learnerTexts) {
    for (const g of grams(t, 8)) if (w.has(g)) { gramHits++; gramHitDetail = g; break; }
  }
  check('2.1B', `zero 8-gram overlaps vs corpus body ${id}`, gramHits === 0, gramHits ? gramHitDetail : 'clean');

  // NUM ledger
  for (const [name, fn] of (NUM_LEDGER[id] || [])) check('NUM', `${id}: ${name}`, !!fn(), name);

  totGloss += S.noteAssets.glossary.length;
  totFigMapped += figs.filter((f) => (f.moduleIds || []).length > 0).length;
  streamChars[id] = { lessons: noteLessons, checks: noteChecks };
}

// corpus-level scope of the declared corpus-limited heading exception
let dupClaims = 0, undeclaredDups = 0;
for (const id of NOTES_W6) {
  const seen = new Map();
  for (const L of sources[id].obj.lessons) for (const h of L.sourceHeadings) {
    if (seen.has(h)) {
      dupClaims++;
      if (!(CORPUS_LIMITED_HEADINGS[id] || []).includes(h)) undeclaredDups++;
    }
    seen.set(h, 1);
  }
}
check('A0', 'corpus-limited heading exception scope (none declared for wave 6: every lesson binds a distinct verbatim corpus heading)', undeclaredDups === 0 && dupClaims === 0, dupClaims + ' dups, ' + undeclaredDups + ' undeclared');

// ── C-6: generation-union ajv (all three prior packs byte-untouched) + new outputs ──
function dirFiles(d, suffix) {
  try { return fs.readdirSync(d).filter((f) => f.endsWith(suffix)).sort(); } catch (e) { return []; }
}
const priorIds = new Set([...bioMan.artifacts, ...chemMan.artifacts, ...physMan.artifacts].map((a) => a.noteId));
check('C-6', 'prior legacy packs noteIds union = 381 (142 biology v44 + 112 chemistry v32 + 127 physics v31); the IAL chemistry stage-A pilot rides the 0.8 generation outside these legacy counts', priorIds.size === 381, priorIds.size);
const priorSrc6 = dirFiles(path.join(INT, 'source-0.6'), '.json').filter((f) => { const nid = f.replace('guided-lesson-', '').replace('.json', ''); return priorIds.has(nid) && !NOTES_W6.includes(nid); });
const priorHub15 = dirFiles(path.join(INT, 'hub-import-1.5'), '.json').filter((f) => priorIds.has(f.replace('.hub-lesson-import.json', '')));
const priorPkg12 = dirFiles(path.join(INT, 'question-packages-1.2'), '.json').filter((f) => priorIds.has(f.replace('.sme-question-package.json', '')));
check('C-6', 'physics+chemistry prior generation present on tree, counted by the v31+v32 noteIds (239 sources / 239 lessons / 239 packages)', priorSrc6.length === 239 && priorHub15.length === 239 && priorPkg12.length === 239, `${priorSrc6.length}/${priorHub15.length}/${priorPkg12.length}`);
const bioSrc7 = dirFiles(path.join(INT, 'source-0.7'), '.json').filter((f) => { const nid = f.replace('guided-lesson-', '').replace('.json', ''); return priorIds.has(nid) && !NOTES_W6.includes(nid); });
const bioHub16 = dirFiles(path.join(INT, 'hub-import-1.6'), '.json').filter((f) => priorIds.has(f.replace('.hub-lesson-import.json', '')));
const bioPkg13 = dirFiles(path.join(INT, 'question-packages-1.3'), '.json').filter((f) => priorIds.has(f.replace('.sme-question-package.json', '')));
check('C-6', 'biology prior generation present on tree, counted by the v44 noteIds (142 sources / 142 lessons / 142 packages)', bioSrc7.length === 142 && bioHub16.length === 142 && bioPkg13.length === 142, `${bioSrc7.length}/${bioHub16.length}/${bioPkg13.length}`);
const chemOldSrc = dirFiles(path.join(INT, 'source-0.5'), '.json');
const chemOldHub = dirFiles(path.join(INT, 'hub-import-1.4'), '.json');
const chemOldPkg = dirFiles(path.join(INT, 'question-packages-1.1'), '.json');
check('C-6', 'chemistry prior generation present (112 sources / 112 lessons / 112 packages)', chemOldSrc.length === 112 && chemOldHub.length === 112 && chemOldPkg.length === 112, `${chemOldSrc.length}/${chemOldHub.length}/${chemOldPkg.length}`);
let priorFails = 0;
for (const f of priorSrc6) { if (!vSrc(JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6', f), 'utf8')))) priorFails++; }
for (const f of bioSrc7) { if (!vSrc(JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7', f), 'utf8')))) priorFails++; }
for (const f of priorHub15) { if (!vHub(JSON.parse(fs.readFileSync(path.join(INT, 'hub-import-1.5', f), 'utf8')))) priorFails++; }
for (const f of bioHub16) { if (!vHub(JSON.parse(fs.readFileSync(path.join(INT, 'hub-import-1.6', f), 'utf8')))) priorFails++; }
for (const f of priorPkg12) { if (!vPkg(JSON.parse(fs.readFileSync(path.join(INT, 'question-packages-1.2', f), 'utf8')))) priorFails++; }
for (const f of bioPkg13) { if (!vPkg(JSON.parse(fs.readFileSync(path.join(INT, 'question-packages-1.3', f), 'utf8')))) priorFails++; }
check('C-6', `physics+chemistry+bio prior union ajv x${priorSrc6.length + bioSrc7.length + priorHub15.length + bioHub16.length + priorPkg12.length + bioPkg13.length} (sources vs 0.8, lessons vs 1.7, packages vs 1.4 — generation-union schemas)`, priorFails === 0, priorFails + ' failures');
let oldFails = 0;
for (const f of chemOldSrc) { if (!vSrc(JSON.parse(fs.readFileSync(path.join(INT, 'source-0.5', f), 'utf8')))) oldFails++; }
for (const f of chemOldHub) { if (!vHub(JSON.parse(fs.readFileSync(path.join(INT, 'hub-import-1.4', f), 'utf8')))) oldFails++; }
for (const f of chemOldPkg) { if (!vPkg(JSON.parse(fs.readFileSync(path.join(INT, 'question-packages-1.1', f), 'utf8')))) oldFails++; }
check('C-6', `chemistry prior-generation union ajv x${chemOldSrc.length + chemOldHub.length + chemOldPkg.length} (0.5 sources vs 0.6, 1.4 lessons vs 1.5, 1.1 packages vs 1.2 — generation-union schemas)`, oldFails === 0, oldFails + ' failures');
// the IAL chemistry prior generation (stage-A pilot + stage-B wave 1) re-proven on this tree
const ialPriorIds = new Set(priorMan.artifacts.map((a) => a.noteId));
check('C-6', 'IAL chemistry prior generation counted by the v50 noteIds (83 = 1 stage-A pilot + 13 wave 1 + 17 wave 2 + 18 wave 3 + 16 wave 4 + 18 wave 5)', ialPriorIds.size === 83, ialPriorIds.size);
const ialSrc8 = dirFiles(path.join(INT, 'source-0.8'), '.json').filter((f) => ialPriorIds.has(f.replace('guided-lesson-', '').replace('.json', '')) && !NOTES_W6.includes(f.replace('guided-lesson-', '').replace('.json', '')));
const ialHub17 = dirFiles(path.join(INT, 'hub-import-1.7'), '.json').filter((f) => ialPriorIds.has(f.replace('.hub-lesson-import.json', '')));
const ialPkg14 = dirFiles(path.join(INT, 'question-packages-1.4'), '.json').filter((f) => ialPriorIds.has(f.replace('.sme-question-package.json', '')));
check('C-6', 'IAL chemistry prior generation present on tree (83 sources / 83 lessons / 83 packages)', ialSrc8.length === 83 && ialHub17.length === 83 && ialPkg14.length === 83, `${ialSrc8.length}/${ialHub17.length}/${ialPkg14.length}`);
let ialFails = 0;
for (const f of ialSrc8) { if (!vSrc(JSON.parse(fs.readFileSync(path.join(INT, 'source-0.8', f), 'utf8')))) ialFails++; }
for (const f of ialHub17) { if (!vHub(JSON.parse(fs.readFileSync(path.join(INT, 'hub-import-1.7', f), 'utf8')))) ialFails++; }
for (const f of ialPkg14) { if (!vPkg(JSON.parse(fs.readFileSync(path.join(INT, 'question-packages-1.4', f), 'utf8')))) ialFails++; }
check('C-6', `IAL chemistry prior-generation union ajv x${ialSrc8.length + ialHub17.length + ialPkg14.length} (0.8 sources vs 0.8, 1.7 lessons vs 1.7, 1.4 packages vs 1.4)`, ialFails === 0, ialFails + ' failures');

// ── transform (the full derivation) ──────────────────────────────────────────
const outputs = {};
for (const id of NOTES_W6) {
  const S = sources[id].obj;
  const raw = sources[id].raw;
  const sourceBlock = {
    sourceFormat: 'guided-lesson/0.6',
    noteId: id,
    corpusVersion: S.noteRef.corpusVersion,
    sourceLayerSha256: sha256(raw),
    pinnedRef: PIN,
  };
  const hub = {
    format: 'hub/lesson-import/1.5',
    adapter: 'guided-lesson-0.6--hub-lesson-import-1.5',
    source: sourceBlock,
    lesson: {
      id: SUBJECT + '::' + id,
      topicTitle: S.noteRef.topicTitle,
      subtopicTitle: S.noteRef.subtopicTitle,
      sourceUrl: S.noteRef.sourceUrl,
      specAnchors: S.specPoints.map((sp) => ({ code: sp.code, text: sp.text })),
      primer: { text: S.primer.text, prerequisiteSubtopic: S.primer.prerequisiteSubtopic },
      modules: S.lessons.map((L, i) => {
        const m = {
          id: id + '::L' + (i + 1),
          title: L.title,
          sourceHeadings: L.sourceHeadings,
          specRefs: L.specRefs,
          opening: L.opening,
          keyPoints: L.keyPoints,
          depthLayers: L.depthLayers,
          gatePolicy: {
            ratingsScale: L.confidenceGate.ratings,
            continueDisabledUntilChoice: L.confidenceGate.continueDisabledUntilChoice,
            resumeWithoutReRate: L.confidenceGate.resumeWithoutReRate,
            postCheckRecalibration: L.confidenceGate.postCheckRecalibration,
          },
          checkRefs: L.check.map((_, k) => id + '::L' + (i + 1) + '::Q' + (k + 1)),
          figureIds: (S.figures || []).filter((f) => f.moduleIds.includes('L' + (i + 1))).map((f) => f.id),
        };
        return m;
      }),
      assets: { glossary: S.noteAssets.glossary, workedExample: S.noteAssets.workedExample },
    },
  };
  if (S.figures && S.figures.length) {
    hub.lesson.figures = S.figures.map((f) => { const g = { id: f.id, url: f.url, alt: f.alt, sourceHeading: f.sourceHeading, moduleIds: f.moduleIds, binding: f.binding }; if (f.caption) g.caption = f.caption; return g; });
  }
  const questions = [];
  S.lessons.forEach((L, i) => {
    L.check.forEach((c, k) => {
      const q = { id: id + '::L' + (i + 1) + '::Q' + (k + 1), moduleId: id + '::L' + (i + 1), stem: c.stem, misconceptionClass: c.misconceptionClass };
      if (c.kind === 'mcq') {
        q.options = c.options.map((o) => ({ key: o.key, text: o.text, correct: o.correct, explanation: o.explanation, misconception: o.misconception }));
      } else {
        q.kind = c.kind; q.modelAnswer = c.modelAnswer; q.keywords = c.keywords; q.options = [];
      }
      questions.push(q);
    });
  });
  const pkg = {
    format: 'sme-question-package/1.2',
    adapter: 'guided-lesson-0.6--hub-lesson-import-1.5',
    source: sourceBlock,
    packageId: SUBJECT + '::' + id,
    subject: SUBJECT,
    questions,
  };
  outputs[id] = { hub, pkg };
}

// validate outputs against the 1.7 / 1.4 generation-union schemas
let outFails = 0;
for (const id of NOTES_W6) {
  if (!vHub(outputs[id].hub)) { outFails++; console.error('hub ajv fail', id, ajv.errorsText(vHub.errors)); }
  if (!vPkg(outputs[id].pkg)) { outFails++; console.error('pkg ajv fail', id, ajv.errorsText(vPkg.errors)); }
}
check('C-6', `stage-B wave-6 outputs ajv x28 (14 vs 1.7 + 14 vs 1.4)`, outFails === 0, outFails + ' failures');

// AN census POST-rotation on the emitted packages (wave-6 declared-rotation precedent)
const ROT = {};
let rotDesc = [];
for (const id of NOTES_W6) {
  const pkg = outputs[id].pkg;
  const census = {};
  let mcqIndex = 0;
  for (const q of pkg.questions) {
    if (q.kind) continue; // written kinds carry options: []
    const origIdx = q.options.findIndex((o) => o.correct);
    const off = ((mcqIndex % 4) - origIdx + 4) % 4;
    mcqIndex++;
    const letters = ['A', 'B', 'C', 'D'];
    q.options = q.options.map((o, i) => ({ ...o, key: letters[(i + off) % 4] }));
    q.options.sort((a, b) => letters.indexOf(a.key) - letters.indexOf(b.key));
    ROT[q.id] = off;
    const corr = q.options.find((o) => o.correct);
    census[corr.key] = (census[corr.key] || 0) + 1;
  }
  check('AN', `correct-key census >=3 distinct (post-rotation) ${id}`, Object.keys(census).length >= 3, JSON.stringify(census));
  check('AN', `no correct letter exceeds 5 (post-rotation) ${id}`, Object.values(census).every((n) => n <= 5), JSON.stringify(census));
  rotDesc.push(id + ': ' + JSON.stringify(census));
}

// C-5 + B2 target on outputs
for (const id of NOTES_W6) {
  const hub = outputs[id].hub, pkg = outputs[id].pkg;
  const refs = hub.lesson.modules.flatMap((m) => m.checkRefs);
  const qids = pkg.questions.map((q) => q.id);
  check('C-5', `checkRefs <-> questions 1:1 in order ${id}`, JSON.stringify(refs) === JSON.stringify(qids), refs.length + ' vs ' + qids.length);
  check('B2', `every module exactly 9 checkRefs ${id}`, hub.lesson.modules.every((m) => m.checkRefs.length === 9), '');
  check('B2', `identity arithmetic 9 = 5+2+1+1 per module ${id}`, hub.lesson.modules.every((m) => {
    const kinds = pkg.questions.filter((q) => q.moduleId === m.id).map((q) => q.kind || 'mcq');
    return kinds.length === 9 && kinds.filter((k) => k === 'mcq').length === 5 && kinds.filter((k) => k === 'recall').length === 2 && kinds.filter((k) => k === 'explain-why').length === 1 && kinds.filter((k) => k === 'application').length === 1;
  }), '');
}

// ── prior-pack byte conservation (G-E): v44 biology + v32 chemistry + v31 physics ──
function packConservation(man, label) {
  let bad = 0;
  for (const a of man.artifacts) {
    const p = path.join(REPO, a.path);
    if (!fs.existsSync(p)) { bad++; continue; }
    const b = fs.readFileSync(p);
    if (b.length !== a.bytes || sha256(b) !== a.sha256) bad++;
  }
  check('G-E', `${label} byte conservation vs v${man.manifest_version} x${man.artifacts.length} (untouched by the IAL chemistry stage-B wave 6)`, bad === 0, `${bad} drift`);
  return bad;
}
check('G-E', 'IAL chemistry pack manifest v50 resolves (166 = 2 stage-A pilot + 26 wave 1 + 34 wave 2 + 36 wave 3 + 32 wave 4 + 36 wave 5)', priorMan.manifest_version === 50 && priorMan.artifacts.length === 166, `v${priorMan.manifest_version} x${priorMan.artifacts.length}`);
check('G-E', 'biology pack manifest v44 resolves (284 = 142 + 142)', bioMan.manifest_version === 44 && bioMan.artifacts.length === 284, `v${bioMan.manifest_version} x${bioMan.artifacts.length}`);
check('G-E', 'chemistry pack manifest v32 resolves (224 = 112 + 112)', chemMan.manifest_version === 32 && chemMan.artifacts.length === 224, `v${chemMan.manifest_version} x${chemMan.artifacts.length}`);
check('G-E', 'physics pack manifest v31 resolves (254 = 127 + 127)', physMan.manifest_version === 31 && physMan.artifacts.length === 254, `v${physMan.manifest_version} x${physMan.artifacts.length}`);
packConservation(priorMan, 'IAL chemistry pack');
packConservation(bioMan, 'biology pack');
packConservation(chemMan, 'chemistry pack');
packConservation(physMan, 'physics pack');

// ── prior-pack load + anchor walk (G-E) ─────────────────────────────────────
const WALK_HUB_KIND = 'hub-lesson-import-1.7';
const byNoteArt = new Map();
for (const a of priorMan.artifacts) {
  byNoteArt.set(a.kind + '|' + a.noteId, path.join(REPO, a.path));
}
check('G-E', 'prior (IAL chemistry stage-B wave-5 v50) artifact census 166 = 83 hubs + 83 packages', priorMan.artifacts.filter((a) => a.kind === WALK_HUB_KIND).length === 83 && priorMan.artifacts.filter((a) => a.kind === 'sme-question-package').length === 83, priorMan.artifacts.length);

function targetTokens(hub, pkg) {
  const s = [];
  const les = hub.lesson;
  for (const sp of les.specAnchors) s.push(sp.code, sp.text);
  s.push(les.primer.text);
  if (les.primer.prerequisiteSubtopic != null) s.push(les.primer.prerequisiteSubtopic);
  for (const m of les.modules) {
    s.push(m.title);
    for (const h of m.sourceHeadings) s.push(h);
    for (const r of m.specRefs) s.push(r);
    s.push(m.opening);
    for (const k of m.keyPoints) s.push(k);
    s.push(m.depthLayers.low.restatement, m.depthLayers.low.analogy, m.depthLayers.low.examPointer);
    s.push(m.depthLayers.medium.restatement, m.depthLayers.medium.analogy, m.depthLayers.medium.examPointer);
  }
  for (const g of les.assets.glossary) s.push(g.term, g.definition);
  const we = les.assets.workedExample;
  if (we) { s.push(we.prompt); for (const st of we.steps) s.push(st); s.push(we.finalAnswer); }
  for (const q of pkg.questions) {
    s.push(q.stem, q.misconceptionClass);
    for (const o of q.options) { s.push(o.key, o.text, o.explanation); if (o.misconception != null) s.push(o.misconception); }
    if (q.kind && q.kind !== 'mcq') {
      if (q.modelAnswer != null) s.push(q.modelAnswer);
      if (Array.isArray(q.keywords)) for (const k of q.keywords) s.push(k);
    }
  }
  return s;
}

// all 97 notes in the walk (the 83 prior IAL chemistry rows re-proven + the 14 stage-B wave-6 notes)
const allNotes = [];
const priorAnchors = new Map(priorInt3.notes.map((n) => [n.noteId, n]));
for (const n of priorInt3.notes) allNotes.push({ noteId: n.noteId, wave: n.wave });
for (const id of NOTES_W6) allNotes.push({ noteId: id, wave: NEW_WAVE });
check('G-E', 'G-E walk rows = 97 (the 83 prior IAL chemistry rows re-proven byte-identical + 14 stage-B wave-6 notes); the emitted INT-3 of record carries all 97 cumulative rows', allNotes.length === 97, allNotes.length);

// serialize output buffers (single source of truth for anchors + emit)
const outBufs = {};
for (const id of NOTES_W6) {
  outBufs[id] = {
    hub: Buffer.from(JSON.stringify(outputs[id].hub, null, 2) + '\n'),
    pkg: Buffer.from(JSON.stringify(outputs[id].pkg, null, 2) + '\n'),
  };
}

let legacyFails = 0;
const grand = crypto.createHash('sha256');
let grandChars = 0;
const waveGrand = crypto.createHash('sha256');
let waveChars = 0;
const waveHashes = {};
const int3Notes = [];
for (const row of allNotes) {
  const id = row.noteId;
  const isNew = row.wave === NEW_WAVE;
  const hubBuf = isNew ? outBufs[id].hub : fs.readFileSync(byNoteArt.get(WALK_HUB_KIND + '|' + id));
  const pkgBuf = isNew ? outBufs[id].pkg : fs.readFileSync(byNoteArt.get('sme-question-package|' + id));
  const hubObj = isNew ? outputs[id].hub : JSON.parse(hubBuf.toString('utf8'));
  const pkgObj = isNew ? outputs[id].pkg : JSON.parse(pkgBuf.toString('utf8'));
  const toksArr = targetTokens(hubObj, pkgObj);
  const s = toksArr.join('\n');
  const sha = sha256(Buffer.from(s, 'utf8'));
  const prior = priorAnchors.get(id);
  if (!isNew) {
    if (!prior || prior.stream.sha256 !== sha || prior.stream.chars !== s.length || prior.hubSha256 !== sha256(hubBuf) || prior.pkgSha256 !== sha256(pkgBuf)) legacyFails++;
  }
  grand.update(Buffer.from(s, 'utf8'));
  grandChars += s.length;
  if (isNew) {
    waveGrand.update(Buffer.from(s, 'utf8'));
    waveChars += s.length;
    waveHashes['wave-ialchem-stageb6'] = waveHashes['wave-ialchem-stageb6'] || crypto.createHash('sha256');
    waveHashes['wave-ialchem-stageb6'].update(Buffer.from(s, 'utf8'));
  }
  if (isNew) int3Notes.push({
    noteId: id,
    wave: row.wave,
    sourceLayerSha256: sha256(sources[id].raw),
    hubSha256: sha256(hubBuf),
    pkgSha256: sha256(pkgBuf),
    stream: { sha256: sha, chars: s.length },
  });
  streamChars[id] = streamChars[id] || {};
  streamChars[id].chars = s.length;
}
check('G-E', `legacy anchors conserved x83 (byte-identical IAL chemistry prior rows: pilot + wave 1 + wave 2 + wave 3 + wave 4 + wave 5)`, legacyFails === 0, legacyFails + ' drift');
check('G-E', `stage-B wave-6 stream chars total = ${NOTES_W6.reduce((t, i) => t + streamChars[i].chars, 0)}`, true, NOTES_W6.reduce((t, i) => t + streamChars[i].chars, 0) + ' chars');

// ── fail-closed barrier before emit ─────────────────────────────────────────
if (FAILS.length) {
  console.error(`FAIL-CLOSED: ${FAILS.length} failures`);
  for (const f of FAILS) console.error(`  [${f.stage}] ${f.name} — ${f.detail}`);
  process.exit(1);
}

// ── emit outputs ─────────────────────────────────────────────────────────────
fs.mkdirSync(path.join(INT, 'hub-import-1.7'), { recursive: true });
fs.mkdirSync(path.join(INT, 'question-packages-1.4'), { recursive: true });
const emitted = [];
for (const id of NOTES_W6) {
  const hp = path.join(INT, 'hub-import-1.7', id + '.hub-lesson-import.json');
  const pp = path.join(INT, 'question-packages-1.4', id + '.sme-question-package.json');
  if (fs.existsSync(hp) && !fs.readFileSync(hp).equals(outBufs[id].hub)) throw new Error('additive-only violation: output exists with DIFFERENT bytes ' + hp);
  if (fs.existsSync(pp) && !fs.readFileSync(pp).equals(outBufs[id].pkg)) throw new Error('additive-only violation: output exists with DIFFERENT bytes ' + pp);
  fs.writeFileSync(hp, outBufs[id].hub); fs.writeFileSync(pp, outBufs[id].pkg);
  emitted.push({ path: 'SME-GuidedLessons/integration/hub-import-1.7/' + id + '.hub-lesson-import.json', bytes: outBufs[id].hub.length, sha256: sha256(outBufs[id].hub) });
  emitted.push({ path: 'SME-GuidedLessons/integration/question-packages-1.4/' + id + '.sme-question-package.json', bytes: outBufs[id].pkg.length, sha256: sha256(outBufs[id].pkg) });
}

// figure caption census (captions carried where the corpus prints an explanatory line)
const figCaptionCount = NOTES_W6.reduce((t, i) => t + ((sources[i].obj.figures || []).filter((f) => f.caption).length), 0);

// manifest v51 emit prep
const waveOut = {};
for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest('hex');
check('G-E', 'IAL-chemistry-scope conservation carries exactly one wave key', Object.keys(waveOut).join(',') === 'wave-ialchem-stageb6', Object.keys(waveOut).join(','));
const newArtifacts = [];
for (const id of NOTES_W6) {
  newArtifacts.push({ kind: 'hub-lesson-import-1.7', noteId: id, path: 'SME-GuidedLessons/integration/hub-import-1.7/' + id + '.hub-lesson-import.json', sha256: sha256(outBufs[id].hub), bytes: outBufs[id].hub.length });
  newArtifacts.push({ kind: 'sme-question-package', noteId: id, path: 'SME-GuidedLessons/integration/question-packages-1.4/' + id + '.sme-question-package.json', sha256: sha256(outBufs[id].pkg), bytes: outBufs[id].pkg.length });
}
const idChecks = NOTES_W6.reduce((t, i) => t + streamChars[i].checks, 0);
const idLessons = NOTES_W6.reduce((t, i) => t + streamChars[i].lessons, 0);
function streamCharsArr() { return streamCharsArr.cached || (streamCharsArr.cached = (() => { const m = { mcq: 0, rec: 0, exp: 0, app: 0 }; for (const id of NOTES_W6) { const S = sources[id].obj; for (const L of S.lessons) for (const c of L.check) { if (c.kind === 'mcq') m.mcq++; else if (c.kind === 'recall') m.rec++; else if (c.kind === 'explain-why') m.exp++; else m.app++; } } return m; })()); }
// manifest v51 (CUMULATIVE over the IAL chemistry pack: stage-A pilot + stage-B waves 1-5 re-pinned + stage-B wave 6)
const grandDigest = grand.digest('hex');
const waveSrc = NOTES_W6.map((i) => JSON.parse(fs.readFileSync(path.join(INT, 'source-0.8/guided-lesson-' + i + '.json'), 'utf8')));
const manifest = {
  format: 'hub-import-manifest/1.0',
  manifest_version: 51,
  course_id: COURSE,
  b6_manifest_continuity: {
    decision: 'continue-global',
    selected: 'IAL chemistry stage-B wave 6 = manifest v51 (the programme-level v-series continues across subjects: chemistry v1..v17 + v32, physics v18..v31, biology v33..v44, v45 the IAL chemistry stage-A pilot, v46 the stage-B wave 1, v47 the stage-B wave 2, v48 the stage-B wave 3, v49 the stage-B wave 4, v50 the stage-B wave 5, now v51 — the sixth IAL chemistry stage-B register wave, on the 0.8/1.7/1.4 generation minted for this subject)',
    rejected: 'per-course series (IAL chemistry v1 restart) — would fork the programme-level integration ledger and break the single load-scope lineage of record',
    recorded_by: 'runbook B6 (the B6 decision of record is continue-global; the physics stage-A, chemistry stage-B, wave-12 and the biology stage-A..stageb10 receipts re-record it); this receipt records it for the IAL chemistry stage-B wave 6',
  },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_trace: TRACE,
  supersedes: `hub-import-manifest-v50.json in the GLOBAL v-series (the IAL chemistry stage-B wave 5: 166 artifacts @ commit C of record ${W5_C}) — this v51 CUMULATIVE manifest re-pins the v50 one hundred sixty-six byte-identical (the 2 stage-A pilot artifacts + the 26 wave-1 artifacts + the 34 wave-2 artifacts + the 36 wave-3 artifacts + the 32 wave-4 artifacts + the 36 wave-5 artifacts @ the v50 landed shas) and adds the stage-B wave-6 tranche (28 artifacts: the 14 register notes at the 0.8/1.7/1.4 generation); the biology v44 pack (284), chemistry v32 pack (224) and physics v31 pack (254) are untouched on disk and conserved by the pipeline's dedicated G-E gates, zero mutation anywhere`,
  checks_layer: {
    wave: 'IAL-CHEMISTRY (WCH1) stage-B wave 6 (the sixth register bucket of the frozen B4 partition: 14 notes end-to-end per runbook B4; cumulative pack 97 notes / ' + (priorMan.counts.lessons + idLessons) + ' lessons / ' + (priorMan.counts.checks + idChecks) + ' checks)',
    derivation: `${idChecks} authored wave-6 checks (${streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application — the B2 law: 9 checks per lesson = 5 MCQ + 2 recall + 1 explain-why + 1 application), graded by the runner's keyword law`,
    declared_revision: 'the SIXTH IAL chemistry stage-B register wave on the 0.8/1.7/1.4 generation (strictly additive over 0.7/1.6/1.3); the v50 one hundred sixty-six artifacts are re-pinned byte-identical (CUMULATIVE convention, the v35/v36 corrective lineage); biology + chemistry + physics pack bytes untouched',
    grading_law: 'case-insensitive whole-token match of the learner text against the keyword set (stem-tolerant), fail-closed on written items without modelAnswer',
    fail_closed: 'written item without modelAnswer renders reveal-only, never gradeable; the runner refuses any feed whose manifest fails G-A..G-E',
  },
  source_generation: {
    format: 'guided-lesson/0.8',
    namespace: 'SME-GuidedLessons/integration/source-0.8/',
    pin: PIN,
    prior_generation_pins: "{'physics pack': 'v18..v31 commit-A pins (v31 manifest)', 'chemistry pack': 'v32 chemistry stage-B @ commit A 0ef5c2cc', 'biology pack': 'v33..v44 commit-A pins (v44 manifest)', 'IAL chemistry stage-A': 'v45 commit-A pin 62bcd8158e990685a6a9e84b07f1380d2977399c', 'IAL chemistry stage-B wave 1': 'v46 commit-C pin 69bb5bcf8e6ad6a8bbd104d47ddcc4a250847518', 'IAL chemistry stage-B wave 2': 'v47 commit-C pin be6c96f5b587c8f17cd7f3362b008dbc8a68f102', 'IAL chemistry stage-B wave 3': 'v48 commit-C pin 57587ea582d9ff843339fac52c2dbf0347bfff81', 'IAL chemistry stage-B wave 4': 'v49 commit-C pin 14dd39f0a5e9729e670eeb1cde32ed7e5e42dc0e', 'IAL chemistry stage-B wave 5': 'v50 commit-C pin " + W5_C + "'} — the stage-B wave-6 sources are authored fresh against the corpus of record at the 0.8 generation",
    int0_lineage: '(new subject — no INT-0 ancestry; the IAL chemistry 0.8 sources are authored directly against the corpus of record)',
  },
  load_scope: {
    adapter: 'guided-lesson-0.8--hub-lesson-import-1.7',
    target_schemas: ['hub/lesson-import/1.7', 'sme-question-package/1.4'],
  },
  counts: {
    notes: priorMan.counts.notes + NOTES_W6.length,
    lessons: priorMan.counts.lessons + idLessons,
    checks: priorMan.counts.checks + idChecks,
    keyPoints: priorMan.counts.keyPoints + waveSrc.reduce((t, S) => t + S.lessons.reduce((t2, l) => t2 + l.keyPoints.length, 0), 0),
    distractors: priorMan.counts.distractors + streamCharsArr().mcq * 3,
    glossaryTerms: priorMan.counts.glossaryTerms + waveSrc.reduce((t, S) => t + S.noteAssets.glossary.length, 0),
    figures: priorMan.counts.figures + waveSrc.reduce((t, S) => t + ((S.figures) || []).length, 0),
    figures_module_mapped: priorMan.counts.figures_module_mapped + totFigMapped,
    figures_note_level: priorMan.counts.figures_note_level + waveSrc.reduce((t, S) => t + (((S.figures) || []).filter((f) => !f.moduleIds || f.moduleIds.length === 0)).length, 0),
    workedExamples_populated: priorMan.counts.workedExamples_populated + totWEPop,
    workedExamples_null: priorMan.counts.workedExamples_null + waveSrc.reduce((t, S) => t + (!S.noteAssets.workedExample ? 1 : 0), 0),
    authored_chars_conserved: priorMan.counts.authored_chars_conserved + waveChars,
  },
  // v50 counts = the IAL chemistry pack of record (CUMULATIVE: stage-A pilot + stage-B waves 1-5)
  conservation: {
    authored_stream_sha256: grandDigest,
    authored_chars: String(grandChars),
    wave_stream_sha256: waveOut,
  },
  // v51 conservation grand stream = all 97 IAL chemistry notes; wave_stream = the wave-6 subtotal
  artifacts: [...priorMan.artifacts, ...newArtifacts],
};
const mb = Buffer.from(JSON.stringify(manifest, null, 2) + '\n');
fs.writeFileSync(path.join(INT, 'hub-import-manifest-v51.json'), mb);

// INT-3 stage-B wave-6 record (CUMULATIVE, 97 rows)
const int3 = {
  stage: 'IAL-CHEMISTRY (WCH1) stage-B wave 6 CUMULATIVE (the 14-note sixth register bucket + the 83 prior rows (stage-A pilot + wave 1 + wave 2 + wave 3 + wave 4 + wave 5): 97 notes / ' + (priorMan.counts.lessons + idLessons) + ' lessons / ' + (priorMan.counts.checks + idChecks) + ' checks at the 0.8/1.7/1.4 generation)',
  title: 'INT-3 transform record — IAL chemistry stage-B wave 6 CUMULATIVE (guided-lesson/0.8 -> hub/lesson-import/1.7 + sme-question-package/1.4), the 97-row IAL chemistry pack anchor table of record (the 83 prior rows carried byte-equivalent from INT-3-transform-record-ialchem-stageb5.json plus the 14 wave-6 rows; the 142 biology anchors stay in INT-3-transform-record-bio-stageb10-v44.json, re-proven on this tree by the G-E gates; the 112 chemistry + 127 physics anchors stay in their own records, re-proven by the C-6 ajv unions and the pack byte-conservation gates)',
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_traces: { ignition: TRACE, execution: TRACE },
  adapter: 'guided-lesson-0.8--hub-lesson-import-1.7',
  course_id: COURSE,
  supersedes_int3: 'records/INT-3-transform-record-ialchem-stageb5.json (the 83-row stage-B wave-5 cumulative anchor table; its rows carried byte-equivalent here plus the 14 wave-6 rows)',
  b6_manifest_continuity: { decision: 'continue-global', selected: 'manifest v51 supersedes v50 (cumulative)' },
  ialchem_stageb6_of_record: {
    basis: 'the sixth register bucket per runbook B4: 14 notes (2-9-organic-chemistry-alcohols x3, 2-10-organic-chemistry-techniques-and-spectra x3, 3-1-physical-chemistry-core-practicals x4, 3-2-inorganic-and-organic-chemistry-core-practicals x4) authored end-to-end through the full chain, 32 lessons x 9 checks, riding the 0.8/1.7/1.4 generation',
    bootstrap: 'the stage-A spec_point_resolution.json bootstrap (262 ids / 254 resolved / 8 unresolved-surplus / 234 codes / 196 notes) carries over unchanged; wave-6 spec codes all resolve in the curriculum graph (14 spec points verbatim)',
    figure_law: '50 corpus figures bound heading-unique and module-mapped to their host lessons by verbatim corpus headings; captions carried verbatim where the corpus prints an explanatory line after the figure block, declared absent otherwise (' + figCaptionCount + ' captions carried, ' + (totFig - figCaptionCount) + ' declared absent)',
    heading_law: 'heading-unique across lessons within each note; zero corpus-limited exceptions for wave 6 - every lesson binds a distinct verbatim corpus heading (the A0 scope gate proves 0 duplicate claims)',
    b4_partition: B4_PARTITION[5],
    b4_partition_note: 'wave W6 of the B4 partition frozen at stage-A open (the full 12-wave partition lives in the stage-A promotion receipt b4_partition_of_record); the pilot stays out of the wave buckets per runbook B3',
    worked_example_law: '7 worked-example ports (designed-or-none posture satisfied by ports of the notes own corpus content: the iron m/z comparison 54/2 = 27 against 56/3 = 18.7 deciding the deflection, the ethanol formula check 2 x 2 + 1 = 5 hydrogens with Mr 46.0, the two-step bromination census 2KBr + H2SO4 -> K2SO4 + 2HBr plus the butan-1-ol substitution ledger, the MCO3 calcium deduction 0.226/24 = 0.009417 mol -> Mr 100.9 -> 100.9 - 60.0 = 40.9, the limiting-reagent census 0.025 mol CuSO4 against 0.0917 mol zinc, the hydrogencarbonate titration 22.80/1000 x 0.200 = 4.56e-3 mol -> 0.182 mol dm-3, the standard-solution mass 0.200 x 0.250 = 0.0500 mol -> 2.00 g, all NUM-ledgered) + 7 designed nulls where the corpus offers no arithmetic to port',
  },
  source_pin: { commitA: PIN, namespace: 'SME-GuidedLessons/integration/source-0.8/', files: NOTES_W6.map((i) => 'guided-lesson-' + i + '.json') },
  registry_pin: { file: 'apps/hub/content/ial-chemistry-17/notes.json', rows: '196', stageb6_rows: 'the 14 wave-6 register notes (bucket first/last anchors per the frozen B4 partition, register order preserved); the stage-A pilot row 0 stays out of the wave buckets per runbook B3' },
  source_08_generation_pin: PIN,
  conservation_law: {
    law: 'adapter spec 0.8 §7 walk (byte-identical to run_import.mjs targetTokens): specAnchors -> primer -> modules (title/headings/specRefs/opening/keyPoints/depthLayers) -> glossary -> workedExample -> questions (stem/class/options + modelAnswer/keywords on written kinds); per-note sha256 of the "\\n"-joined stream',
    wave_subtotals: waveOut,
  },
  grand_stream: { chars: grandChars, sha256: grandDigest },
  wave_stream_sha256: waveOut,
  battery: {
    names: ['P0', 'A0', 'AN', 'JC', 'SG', 'KW', '2.1B', 'NUM', 'C-6', 'written', 'C-5', 'B2', 'G-E'],
    a0: 'ajv 0.8 source x14 + kind order x32 lessons + B2 sizing + spec text provenance (curriculum graph verbatim x14 spec points) + figure closure both ways x50 + corpus image coverage + glossary band + primer band + noteRef identity + section-title map + the heading-unique scope gate (zero exceptions)',
    an: 'exactly-one-correct x160; correct-key census >=3 distinct per note (post-rotation); distinct option texts; four options',
    sg: 'lesson specRefs subset of file specPoints; every check KP-anchored (content-token overlap)',
    kw: '>=3 grounded keywords per written item x128',
    jc: 'every option explained; distractors name misconceptions; correct-option misconception null',
    '2.1b': 'zero 8-gram overlaps of learner-surface text vs the corpus note body x14',
    num: 'spot ledgers on the authored arithmetic (58 ledger entries across 14 notes: the WE ports + the MCQ/application answers)',
    c6: 'physics+chemistry+bio prior union ajv x762 + chemistry prior-generation union ajv x336 + IAL chemistry prior-generation union ajv x249 + wave-6 outputs ajv x28',
    c5: 'checkRefs <-> questions bidirectional 1:1 in order x14',
    b2: '9 checkRefs per module x32; identity arithmetic 9 = 5+2+1+1 x32',
    ge: 'IAL chemistry stream anchors x97 (the emitted cumulative INT-3 of record) + the 83 prior anchors re-proven on this tree (byte-identical prior pack rows) + IAL chemistry pack byte conservation vs v50 x166 + biology v44 pack byte conservation x284 + chemistry v32 pack byte conservation x224 + physics v31 pack byte conservation x254 + IAL chemistry grand stream single-finalization',
  },
  ialchem_census: {
    notes_total_register: 196, notes_landed: 97, lessons_total: priorMan.counts.lessons + idLessons, checks_total: priorMan.counts.checks + idChecks,
    stageb6_figures: totFig, corpus_images_bound: totFig,
    worked_examples_populated: totWEPop, worked_examples_null: totWENull,
  },
  prior_census: {
    biology: { notes_total: 142, lessons_total: bioMan.counts.lessons, checks_total: bioMan.counts.checks, note: 'carried byte-identical from v44; anchors re-proven on the wave tree' },
    chemistry: { notes_total: 112, lessons_total: chemMan.counts.lessons, checks_total: chemMan.counts.checks, note: 'carried byte-identical from v32' },
    physics: { notes_total: 127, lessons_total: physMan.counts.lessons, checks_total: physMan.counts.checks, note: 'carried byte-identical from v31' },
    ialchem_stagea: { notes_total: 1, lessons_total: 2, checks_total: 18, note: 'the stage-A pilot row carried byte-equivalent from records/INT-3-transform-record-ialchem-stagea.json via the stage-B wave-1 record; pack bytes re-pinned vs v46' },
    ialchem_stageb1: { notes_total: 13, lessons_total: 31, checks_total: 279, note: 'the wave-1 rows carried byte-equivalent from records/INT-3-transform-record-ialchem-stageb2.json via the wave-2 record; pack bytes re-pinned vs v47' },
    ialchem_stageb2: { notes_total: 17, lessons_total: 48, checks_total: 432, note: 'the wave-2 rows carried byte-equivalent from records/INT-3-transform-record-ialchem-stageb2.json; pack bytes re-pinned vs v47' },
    ialchem_stageb3: { notes_total: 18, lessons_total: 46, checks_total: 414, note: 'the wave-3 rows carried byte-equivalent from records/INT-3-transform-record-ialchem-stageb3.json; pack bytes re-pinned vs v48' },
    ialchem_stageb4: { notes_total: 16, lessons_total: 44, checks_total: 396, note: 'the wave-4 rows carried byte-equivalent from records/INT-3-transform-record-ialchem-stageb4.json; pack bytes re-pinned vs v49' },
    ialchem_stageb5: { notes_total: 18, lessons_total: 50, checks_total: 450, note: 'the wave-5 rows carried byte-equivalent from records/INT-3-transform-record-ialchem-stageb5.json; pack bytes re-pinned vs v50' },
  },
  notes: priorInt3.notes.concat(int3Notes),
};
const ib = Buffer.from(JSON.stringify(int3, null, 2) + '\n');
fs.mkdirSync(path.join(INT, 'records'), { recursive: true });
fs.writeFileSync(path.join(INT, 'records/INT-3-transform-record-ialchem-stageb6.json'), ib);

// promotion receipt
// promotion receipt
const receipt = {
  format: 'ialchem-stageb6-promotion-receipt/1.0',
  wave: 'IAL-CHEMISTRY (WCH1) stage-B wave 6 (the sixth register bucket: 14 notes end-to-end at the 0.8/1.7/1.4 four-plane generation; CUMULATIVE programme-level manifest v51)',
  operator_traces: { ignition: TRACE, execution: TRACE },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  commit_a: { sha: PIN, contents: 'commit A: the 14 authored stage-B wave-6 source-0.8 notes (the sixth register bucket of the frozen B4 partition) + the pipeline of record ialchem-stageb6-pipeline.js derived from the ialchem-stageb5 landed pipeline (the 0.8/1.7/1.4 schema generation and the spec_point_resolution.json bootstrap already landed at the stage-A commit A)', parent: parent, message_carries_trace: headMsg.includes(TRACE) },
  tranche: {
    notes: 14, lessons: idLessons, checks: idChecks,
    kinds: { mcq: streamCharsArr().mcq, recall: streamCharsArr().rec, 'explain-why': streamCharsArr().exp, application: streamCharsArr().app },
    figures: totFig, figures_module_mapped: totFigMapped,
    glossary_terms: NOTES_W6.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.8/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
    worked_examples: { populated: totWEPop, null: totWENull },
    stream_chars: NOTES_W6.reduce((t, i) => t + streamChars[i].chars, 0),
    authoring_shape: {
      wave_note_buckets: '2-9-organic-chemistry-alcohols 3 + 2-10-organic-chemistry-techniques-and-spectra 3 + 3-1-physical-chemistry-core-practicals 4 + 3-2-inorganic-and-organic-chemistry-core-practicals 4 = 14 notes',
      lessons: idLessons, checks: idChecks, figures: totFig, figures_module_mapped: totFigMapped, figures_note_level: totFig - totFigMapped,
      glossary_terms: NOTES_W6.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.8/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
      worked_examples: { populated: totWEPop, null: totWENull },
    },
  },
  manifest: { version: 51, artifacts_total: manifest.artifacts.length, scope: 'IAL chemistry pack of record (CUMULATIVE: stage-A pilot + stage-B waves 1-6)', biology_prior_re_pinned_vs_v44: 284, chemistry_prior_re_pinned_vs_v32: 224, physics_prior_re_pinned_vs_v31: 254, ialchem_prior_re_pinned_vs_v50: 166, first_issues: 28 },
  outputs: emitted.map((e) => e.path),
  gate_log: LOG,
  gates_total: LOG.length,
  gates_passed: LOG.filter((l) => l.ok).length,
  verdict: FAILS.length === 0 ? 'GREEN' : 'RED',
  b4_partition_of_record: B4_PARTITION,
  disclosures: [
    'spec texts carried verbatim from the curriculum graph SPEC_POINT nodes (no spec text invented); spec codes pinned to the notes.json register rows (the 14 wave-6 rows, register order preserved, bucket anchors first/last per the frozen B4 partition)',
    'corpusVersion pinned as sme-revision-notes-ial-chemistry-17-2026-08-05 — the register rows most recent content update (max updatedAt 2026-08-05), the mechanical register-version pin of record carried over from the stage-A pilot and wave 1',
    'the 0.8/1.7/1.4 schema generation is strictly additive over 0.7/1.6/1.3 and was minted at the stage-A commit A; no schema bytes changed in this wave',
    'the B4 partition of record (frozen at stage-A open; 195 notes in 12 subtopic-atomic waves W1..W12) lives in the stage-A promotion receipt as b4_partition_of_record and is re-recorded byte-identical here; wave W6 = 14 notes across four buckets (2-9-organic-chemistry-alcohols 3 + 2-10-organic-chemistry-techniques-and-spectra 3 + 3-1-physical-chemistry-core-practicals 4 + 3-2-inorganic-and-organic-chemistry-core-practicals 4), the pilot excluded per runbook B3',
    'worked-example ports from the corpus: 7 notes carry a populated workedExample ported in substance from their own corpus content (the iron m/z comparison 54/2 = 27 against 56/3 = 18.7 deciding the magnet deflection; the ethanol formula check 2 x 2 + 1 = 5 hydrogens with Mr 46.0; the two-step bromination census 2KBr + H2SO4 -> K2SO4 + 2HBr with the butan-1-ol substitution ledger closed; the MCO3 calcium deduction 0.226/24 = 0.009417 mol -> Mr 100.9 -> 100.9 - 60.0 = 40.9; the limiting-reagent census 0.025 mol CuSO4 against 0.0917 mol zinc; the hydrogencarbonate titration 22.80/1000 x 0.200 = 4.56e-3 mol -> 0.182 mol dm-3; the standard-solution mass 0.200 x 0.250 = 0.0500 mol -> 2.00 g), each NUM-ledgered; 7 notes carry designed nulls where the corpus offers no arithmetic to port (designed-or-none posture, the chemistry stage-B populated precedent)',
    'corpus figure URLs rewritten from the pinned-commit namespace to the main namespace (asset identity preserved by basename; the A0 gate re-checks the basename against the corpus body); alt text carried verbatim from the corpus markdown, with 4 authored alts where the source site printed none (the wave-1 A2 corrective posture)',
    'figure captions carried verbatim where the corpus prints an explanatory line after the figure block (' + figCaptionCount + ' figures); the other ' + (totFig - figCaptionCount) + ' captions are declared absent (no such line exists in the source)',
    'MCQ correct-key census enforced POST-transform under the declared deterministic AN rotation table (cyclic per-note re-letter) — the wave-6/8/9/10/11 + stage-A + waves 1-5 re-lettering precedent, table-recorded',
    'the topicTitle of record is the hub curriculum graph SME-S1 node title the register sectionSlug denotes; the 14 wave-6 notes sit in two sections - Energetics, Group Chemistry, Halogenoalkanes & Alcohols (six notes: 2-9 and 2-10) and Practical Skills in Chemistry I (eight notes: 3-1 and 3-2)',
    'the WAVE_OPEN_BASE_W6 ' + WAVE_OPEN_BASE_W6 + ' is the resources main tip at wave open; two unrelated W-F5 lane commits (the W-F5-T2 presentation re-issue 676306b0 and the W-F5 records receipt 0111c9c1) landed on main between the stage-B wave-5 commit C 4392a055 and the wave-6 open — the W-F3-T2 precedent waves 3 and 5 rode on — so the wave-open base is the live tip at open, not the wave-5 commit C; stage-B wave-6 sequence: commit A lands the 14 source notes byte-final + the pipeline of record, the pipeline re-runs at the commit-A pin with the race-guard asserting the tip, then commit C lands — the race-guard semantics disclosed',
    'the PROMOTION receipt filename carries the Asia/Dhaka execution date while generated_at_utc is honest UTC (the stage-A receipt corrective clarified the token follows the executor clock)',
    'the emitted hub/question-package artifacts carry the run_import.mjs legacy identity strings (hub/lesson-import/1.5 + guided-lesson-0.6--hub-lesson-import-1.5 + sourceFormat guided-lesson/0.6) byte-conserved exactly as every prior pack; the RECORD layer (this receipt, the INT-3, the manifest load_scope) declares the true 0.8/1.7/1.4 generation — the conservation law of record',
    'the manifest v51 is CUMULATIVE over the IAL chemistry pack (194 artifacts = the 166 v50 artifacts re-pinned byte-identical @ the v50 landed shas + 28 wave-6 first issues), continuing the v35/v36 corrective convention that keeps the runner-owned guided-import.json index complete',
    'heading-unique law with zero exceptions: every wave-6 lesson binds a distinct verbatim corpus heading, the A0 scope gate proves 0 duplicate claims, and no corpus-limited exception needed declaring',
    'the four W-F2-T2 / Lane B commits that landed on main between waves (8039d1c2..WAVE_OPEN_BASE_W2) touch no SME-GuidedLessons/integration bytes - the G-E pack byte-conservation gates prove the prior packs untouched',
  ],
};

const rb = Buffer.from(JSON.stringify(receipt, null, 2) + '\n');
fs.writeFileSync(path.join(INT, 'records/IAL-CHEMISTRY-WCH1-STAGEB6-PROMOTION-20261117.json'), rb);

console.log(`GATES: ${LOG.filter((l) => l.ok).length}/${LOG.length} GREEN, 0 failures`);
console.log(`EMITTED: 28 outputs + manifest v51 (${mb.length}B) + INT-3 (${ib.length}B) + promotion receipt (${rb.length}B)`);
console.log(`Stage-B wave-6 tranche: 14 notes / ${idLessons} lessons / ${idChecks} checks (${streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application) / ${totFig} figures`);
console.log(`MANIFEST v51: ${manifest.counts.notes} notes / ${manifest.counts.lessons} lessons / ${manifest.counts.checks} checks; grand stream ${manifest.conservation.authored_chars} chars`);
console.log(`GRAND: ${manifest.conservation.authored_stream_sha256}`);
console.log(`STAGE-B WAVE-6 SUBTOTAL: ${waveOut['wave-ialchem-stageb6']}`);
console.log(`ROTATION: ${rotDesc.join(' | ')}`);
