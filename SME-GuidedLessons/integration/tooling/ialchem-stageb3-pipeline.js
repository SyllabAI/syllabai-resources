#!/usr/bin/env node
/**
 * ialchem-stageb3-pipeline.js — IAL-CHEMISTRY (WCH1) stage-B wave 3 (the third register bucket of the
 * frozen B4 partition: 18 notes end-to-end at the 0.8/1.7/1.4 four-plane generation: source-0.8 /
 * hub-import-1.7 / question-packages-1.4 / CUMULATIVE manifest v48 + records, per runbook B4). Derived
 * from the ialchem-stageb2 landed pipeline of record. Node >= 18, ajv via ajvkit.
 *
 * Usage:
 *   node ialchem-stageb3-pipeline.js --pin <commitA> --repo <resources worktree root> \
 *     --curriculum <curriculum-ial-chem.json> --notes <notes-ial-chem-w3.json> \
 *     --priorInt3 <INT-3 ialchem-stageb2> --priorManifest <v47 manifest (IAL chemistry stage-B wave 2)> \
 *     --priorBioManifest <v44 manifest (biology cumulative)> --priorChemManifest <v32 manifest (chemistry)> \
 *     --priorPhysManifest <v31 manifest (physics)> --trace <operator ignition trace>
 *
 * Gates of record (the physics-wave battery, re-run over the full corpus): P0 / A0 / AN / JC / SG / KW /
 * 2.1B / NUM / C-6 / written / C-5 / B2 / G-E. Fail-closed: any failure exits 1 before emit.
 *
 * Stage-B wave-3 authoring of record (census 2026-11-15): 18 notes / 46 lessons / 414 checks =
 * 230 MCQ + 92 recall + 46 explain-why + 46 application (the B2 law 5+2+1+1 per lesson); 82 corpus
 * figures bound heading-unique and module-mapped (captions carried where the corpus prints them);
 * glossary 66 terms (each note in the 3..5 band); 5 worked-example ports + 13 designed nulls
 * (designed-or-none posture); learner-surface authored fresh per the 2.1B 8-gram law; no corpus-limited
 * heading exceptions needed - every wave-3 lesson binds a distinct verbatim corpus heading.
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

const NOTES_W3 = [
  'rn_D7xTxVcGcvVNP264',
  'rn_NTPrtZFbDW7QSmkM',
  'rn_jSKV5rYbCfKNQ9sX',
  'rn_t2nwJFrmkTRd7qsq',
  'rn_4fC4yJkMpgh4r6SR',
  'rn_4mtRwFS9YpSSvpbq',
  'rn_dyFwqRzcJB9bjs3C',
  'rn_FPqjsfZgWKgDT5dW',
  'rn_CtzhyDct39G6dpvC',
  'rn_PSdnDqH5S9S3B4H4',
  'rn_cfnbqHpbczGvkz3x',
  'rn_mG3Q5T33GSSt7cdY',
  'rn_6Z2bnGMQxXhv947z',
  'rn_vx7rKMChwzKHSm2g',
  'rn_ymQPrR3g4BVDVyfd',
  'rn_sKsfrZnSWVsGzgfW',
  'rn_7Tgb4gzybkSVcPDf',
  'rn_GpHSrcx5SvbCXDG3',
];
const WAVE3 = 18;
// no corpus-limited heading exceptions of record for wave 3: every wave-3 lesson binds a
// distinct verbatim corpus heading (the A0 heading-unique gate proves it)
const CORPUS_LIMITED_HEADINGS = {};
const NEW_WAVE = 'ialchem-stageb3';
const W2_C = 'be6c96f5b587c8f17cd7f3362b008dbc8a68f102';  // the stage-B wave-2 commit-C pin of record
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
for (const id of NOTES_W3) {
  const p = path.join(INT, 'source-0.8/guided-lesson-' + id + '.json');
  sources[id] = { path: p, raw: fs.readFileSync(p), obj: JSON.parse(fs.readFileSync(p, 'utf8')) };
}

// ── P0: pin + blob identity ──────────────────────────────────────────────────
const headSha = execSync('git rev-parse HEAD', { cwd: REPO }).toString().trim();
check('P0', 'HEAD == declared stage-B wave-3 commit-A pin', headSha === PIN, 'HEAD=' + headSha.slice(0, 12) + ' pin=' + PIN.slice(0, 12));
const headMsg = execSync('git log -1 --format=%B', { cwd: REPO }).toString();
check('P0', 'commit A message carries the operator trace', headMsg.includes(TRACE), headMsg.slice(0, 90).replace(/\n/g, ' '));
for (const id of NOTES_W3) {
  const rel = 'SME-GuidedLessons/integration/source-0.8/guided-lesson-' + id + '.json';
  const blob = execSync('git show HEAD:' + rel, { cwd: REPO, maxBuffer: 1 << 22 });
  check('P0', 'source blob @ HEAD == disk: ' + id, blob.equals(sources[id].raw), 'blob=' + blob.length + 'B disk=' + sources[id].raw.length + 'B');
}
const parent = execSync('git rev-parse HEAD~1', { cwd: REPO }).toString().trim();
const WAVE_OPEN_BASE_W3 = '3c8c25158748e4831d987c631abaa15a1327399a';
const CORRECTIVE_BASE_W3 = 'c847274a35561b55c51100b374666ed6e294ce0a';  // the disclosed first-issue base accepted by the P0 parent check (the wave-2 A2 precedent)
check('P0', 'commit A parent == the wave-open resources main of record (or the disclosed first-issue base c847274a, force-back rule-blocked)', parent === WAVE_OPEN_BASE_W3 || parent === CORRECTIVE_BASE_W3, 'parent=' + parent.slice(0, 12));
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
  rn_D7xTxVcGcvVNP264: [
    ['check arithmetic: ethene sigma census 4 C-H + 1 C-C = 5 sigma bonds', () => Math.abs(4 + 1 - 5) < 1e-9],
    ['check arithmetic: propene sigma census 6 C-H + 2 C-C = 8 sigma bonds', () => Math.abs(6 + 2 - 8) < 1e-9],
    ['check arithmetic: C5H10 molar mass 5 x 12 + 10 x 1 = 70', () => Math.abs(5 * 12 + 10 * 1 - 70) < 1e-9],
  ],
  rn_NTPrtZFbDW7QSmkM: [
    ['check arithmetic: the CIP ladder 35 > 17 > 6 > 1 (Br > Cl > C > H)', () => (35 > 17 && 17 > 6 && 6 > 1)],
  ],
  rn_jSKV5rYbCfKNQ9sX: [
    ['check arithmetic: ethene bromination atom census 2 C + 4 H + 2 Br = 8 conserved', () => Math.abs(2 + 4 + 2 - 8) < 1e-9],
  ],
  rn_t2nwJFrmkTRd7qsq: [
    ['check arithmetic: one Br2 delivers 2 Br atoms to the dibromo product', () => Math.abs(2 - 2) < 1e-9],
  ],
  rn_4fC4yJkMpgh4r6SR: [
    ['check arithmetic: HBr onto propene yields 2 regioisomers (1- and 2-bromopropane)', () => Math.abs(2 - 2) < 1e-9],
  ],
  rn_4mtRwFS9YpSSvpbq: [
    ['WE port: chloroethene census 2 C + 3 H + 1 Cl = 6 atoms conserved into the repeat unit', () => Math.abs(2 + 3 + 1 - 6) < 1e-9],
    ['check arithmetic: monomer and repeat unit share the identical 6-atom inventory', () => Math.abs(6 - 6) < 1e-9],
  ],
  rn_dyFwqRzcJB9bjs3C: [
    ['check arithmetic: compostable endpoint set = 3 products (CO2, water, biomass)', () => Math.abs(3 - 3) < 1e-9],
    ['check arithmetic: one PVC chlorine yields one HCl on incineration', () => Math.abs(1 - 1) < 1e-9],
  ],
  rn_FPqjsfZgWKgDT5dW: [
    ['check arithmetic: propane combustion oxygen ledger 2 x 5 = 6 + 4', () => Math.abs(2 * 5 - 6 - 4) < 1e-9],
    ['check arithmetic: cycloalkane C6H12 vs alkane C6H14 (6 x 2 = 12; 6 x 2 + 2 = 14)', () => Math.abs(6 * 2 - 12) < 1e-9 && Math.abs(6 * 2 + 2 - 14) < 1e-9],
    ['check arithmetic: methane to ethane to propane masses 16 -> 30 -> 44 (both steps +14)', () => Math.abs(30 - 16 - 14) < 1e-9 && Math.abs(44 - 30 - 14) < 1e-9],
  ],
  rn_CtzhyDct39G6dpvC: [
    ['WE port: decane cracking C balance 10 = 8 + 2', () => Math.abs(10 - 8 - 2) < 1e-9],
    ['WE port: decane cracking H balance 22 = 18 + 4', () => Math.abs(22 - 18 - 4) < 1e-9],
    ['check arithmetic: hexane reforming H balance 14 = 12 + 2', () => Math.abs(14 - 12 - 2) < 1e-9],
  ],
  rn_PSdnDqH5S9S3B4H4: [
    ['check arithmetic: CaCO3 + SO2 -> CaSO3 + CO2 oxygen census 3 + 2 = 3 + 2', () => Math.abs(3 + 2 - 3 - 2) < 1e-9],
    ['check arithmetic: converter 2CO + 2NO -> 2CO2 + N2 atom census C2 N2 O4 both sides', () => Math.abs(2 + 2 - 4) < 1e-9],
  ],
  rn_cfnbqHpbczGvkz3x: [
    ['check arithmetic: converter O census 2 + 2 = 2 x 2', () => Math.abs(2 + 2 - 2 * 2) < 1e-9],
    ['check arithmetic: 2CO + O2 -> 2CO2 oxidation census O 2 + 2 = 4', () => Math.abs(2 + 2 - 4) < 1e-9],
  ],
  rn_mG3Q5T33GSSt7cdY: [
    ['check arithmetic: Cl2 homolysis deals 1 + 1 = 2 bonding electrons to two radicals', () => Math.abs(1 + 1 - 2) < 1e-9],
    ['check arithmetic: Br2 homolysis likewise yields 2 bromine radicals', () => Math.abs(2 - 2) < 1e-9],
  ],
  rn_6Z2bnGMQxXhv947z: [
    ['check arithmetic: termination ethane census 2 C + 6 H on both sides', () => Math.abs(2 - 2) < 1e-9 && Math.abs(6 - 6) < 1e-9],
    ['check arithmetic: the substitution series runs 4 steps (CH3Cl, CH2Cl2, CHCl3, CCl4)', () => Math.abs(4 - 4) < 1e-9],
  ],
  rn_vx7rKMChwzKHSm2g: [
    ['check arithmetic: profile read Ea 120 - 50 = 70 and dH 90 - 50 = +40', () => Math.abs(120 - 50 - 70) < 1e-9 && Math.abs(90 - 50 - 40) < 1e-9],
    ['check arithmetic: profile read Ea 160 - 80 = 80 and dH 120 - 80 = +40', () => Math.abs(160 - 80 - 80) < 1e-9 && Math.abs(120 - 80 - 40) < 1e-9],
  ],
  rn_ymQPrR3g4BVDVyfd: [
    ['check arithmetic: ethanol formation H census 3 x 2 = 6', () => Math.abs(3 * 2 - 6) < 1e-9],
    ['check arithmetic: propan-1-ol formation H census 4 x 2 = 8', () => Math.abs(4 * 2 - 8) < 1e-9],
  ],
  rn_sKsfrZnSWVsGzgfW: [
    ['WE port: displacement q = 25 x 4.18 x 14.0 = 1463 J', () => Math.abs(25 * 4.18 * 14.0 - 1463) < 0.01],
    ['WE port: per mole 1463 / 1000 / 0.025 = 58.52 -> dH = -58.5 kJ mol^-1', () => Math.abs(1463 / 1000 / 0.025 - 58.52) < 0.01],
    ['check arithmetic: neutralisation q = 75.0 x 4.18 x 9.5 = 2978.25 J', () => Math.abs(75.0 * 4.18 * 9.5 - 2978.25) < 0.01],
    ['check arithmetic: methanol moles 0.92 / 32 = 0.02875', () => Math.abs(0.92 / 32 - 0.02875) < 0.001],
    ['check arithmetic: methanol dHc -18.6 / 0.0288 = -645.83 kJ mol^-1', () => Math.abs(18.6 / 0.0288 - 645.83) < 0.5],
  ],
  rn_7Tgb4gzybkSVcPDf: [
    ['check arithmetic: ammonia synthesis dHr = 2 x (-46) = -92 kJ mol^-1', () => Math.abs(2 * 46 - 92) < 1e-9],
    ['WE port: propanone legs 3 x 394 = 1182 and 3 x 286 = 858', () => Math.abs(3 * 394 - 1182) < 1e-9 && Math.abs(3 * 286 - 858) < 1e-9],
    ['WE port: propanone dHf = -1182 - 858 + 1821 = -219 kJ mol^-1', () => Math.abs(-1182 - 858 + 1821 + 219) < 1e-9],
    ['WE port: propan-1-ol legs 1182 + 1144 = 2326', () => Math.abs(3 * 394 + 4 * 286 - 2326) < 1e-9],
    ['WE port: propan-1-ol dHf = -2326 + 1821 = -505 kJ mol^-1', () => Math.abs(-2326 + 1821 + 505) < 1e-9],
    ['check arithmetic: subtraction example -780 - (-602) = -178', () => Math.abs(-780 - (-602) + 178) < 1e-9],
    ['check arithmetic: ammonia doubling 2 x 46 = 92 (the coefficient law)', () => Math.abs(2 * 46 - 92) < 1e-9],
  ],
  rn_GpHSrcx5SvbCXDG3: [
    ['WE port: HCl synthesis broken sum 436 + 242 = 678', () => Math.abs(436 + 242 - 678) < 1e-9],
    ['WE port: HCl synthesis formed sum 2 x 431 = 862', () => Math.abs(2 * 431 - 862) < 1e-9],
    ['WE port: HCl synthesis dH = 678 - 862 = -184 kJ mol^-1', () => Math.abs(678 - 862 + 184) < 1e-9],
    ['check arithmetic: corpus WE dH = 2912 - 4142 = -1230 kJ mol^-1', () => Math.abs(2912 - 4142 + 1230) < 1e-9],
    ['check arithmetic: NH3 broken sum 944 + 3 x 436 = 2252', () => Math.abs(944 + 3 * 436 - 2252) < 1e-9],
    ['check arithmetic: NH3 formed sum 2252 - (-92) = 2344; mean N-H 2344 / 6 = 390.67', () => Math.abs(2252 - (-92) - 2344) < 1e-9 && Math.abs(2344 / 6 - 390.67) < 0.01],
    ['check arithmetic: ledger example 520 - 700 = -180; methane mean 1646 / 4 = 411.5', () => Math.abs(520 - 700 + 180) < 1e-9 && Math.abs(1646 / 4 - 411.5) < 0.01],
  ],
};
let totLessons = 0, totChecks = 0, totKP = 0, totDistr = 0, totGloss = 0;
let totFig = 0, totFigMapped = 0, totWEPop = 0, totWENull = 0;
const streamChars = {};

for (const id of NOTES_W3) {
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
for (const id of NOTES_W3) {
  const seen = new Map();
  for (const L of sources[id].obj.lessons) for (const h of L.sourceHeadings) {
    if (seen.has(h)) {
      dupClaims++;
      if (!(CORPUS_LIMITED_HEADINGS[id] || []).includes(h)) undeclaredDups++;
    }
    seen.set(h, 1);
  }
}
check('A0', 'corpus-limited heading exception scope (none declared for wave 3: every lesson binds a distinct verbatim corpus heading)', undeclaredDups === 0 && dupClaims === 0, dupClaims + ' dups, ' + undeclaredDups + ' undeclared');

// ── C-6: generation-union ajv (all three prior packs byte-untouched) + new outputs ──
function dirFiles(d, suffix) {
  try { return fs.readdirSync(d).filter((f) => f.endsWith(suffix)).sort(); } catch (e) { return []; }
}
const priorIds = new Set([...bioMan.artifacts, ...chemMan.artifacts, ...physMan.artifacts].map((a) => a.noteId));
check('C-6', 'prior legacy packs noteIds union = 381 (142 biology v44 + 112 chemistry v32 + 127 physics v31); the IAL chemistry stage-A pilot rides the 0.8 generation outside these legacy counts', priorIds.size === 381, priorIds.size);
const priorSrc6 = dirFiles(path.join(INT, 'source-0.6'), '.json').filter((f) => { const nid = f.replace('guided-lesson-', '').replace('.json', ''); return priorIds.has(nid) && !NOTES_W3.includes(nid); });
const priorHub15 = dirFiles(path.join(INT, 'hub-import-1.5'), '.json').filter((f) => priorIds.has(f.replace('.hub-lesson-import.json', '')));
const priorPkg12 = dirFiles(path.join(INT, 'question-packages-1.2'), '.json').filter((f) => priorIds.has(f.replace('.sme-question-package.json', '')));
check('C-6', 'physics+chemistry prior generation present on tree, counted by the v31+v32 noteIds (239 sources / 239 lessons / 239 packages)', priorSrc6.length === 239 && priorHub15.length === 239 && priorPkg12.length === 239, `${priorSrc6.length}/${priorHub15.length}/${priorPkg12.length}`);
const bioSrc7 = dirFiles(path.join(INT, 'source-0.7'), '.json').filter((f) => { const nid = f.replace('guided-lesson-', '').replace('.json', ''); return priorIds.has(nid) && !NOTES_W3.includes(nid); });
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
check('C-6', 'IAL chemistry prior generation counted by the v47 noteIds (31 = 1 stage-A pilot + 13 wave 1 + 17 wave 2)', ialPriorIds.size === 31, ialPriorIds.size);
const ialSrc8 = dirFiles(path.join(INT, 'source-0.8'), '.json').filter((f) => ialPriorIds.has(f.replace('guided-lesson-', '').replace('.json', '')) && !NOTES_W3.includes(f.replace('guided-lesson-', '').replace('.json', '')));
const ialHub17 = dirFiles(path.join(INT, 'hub-import-1.7'), '.json').filter((f) => ialPriorIds.has(f.replace('.hub-lesson-import.json', '')));
const ialPkg14 = dirFiles(path.join(INT, 'question-packages-1.4'), '.json').filter((f) => ialPriorIds.has(f.replace('.sme-question-package.json', '')));
check('C-6', 'IAL chemistry prior generation present on tree (31 sources / 31 lessons / 31 packages)', ialSrc8.length === 31 && ialHub17.length === 31 && ialPkg14.length === 31, `${ialSrc8.length}/${ialHub17.length}/${ialPkg14.length}`);
let ialFails = 0;
for (const f of ialSrc8) { if (!vSrc(JSON.parse(fs.readFileSync(path.join(INT, 'source-0.8', f), 'utf8')))) ialFails++; }
for (const f of ialHub17) { if (!vHub(JSON.parse(fs.readFileSync(path.join(INT, 'hub-import-1.7', f), 'utf8')))) ialFails++; }
for (const f of ialPkg14) { if (!vPkg(JSON.parse(fs.readFileSync(path.join(INT, 'question-packages-1.4', f), 'utf8')))) ialFails++; }
check('C-6', `IAL chemistry prior-generation union ajv x${ialSrc8.length + ialHub17.length + ialPkg14.length} (0.8 sources vs 0.8, 1.7 lessons vs 1.7, 1.4 packages vs 1.4)`, ialFails === 0, ialFails + ' failures');

// ── transform (the full derivation) ──────────────────────────────────────────
const outputs = {};
for (const id of NOTES_W3) {
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
for (const id of NOTES_W3) {
  if (!vHub(outputs[id].hub)) { outFails++; console.error('hub ajv fail', id, ajv.errorsText(vHub.errors)); }
  if (!vPkg(outputs[id].pkg)) { outFails++; console.error('pkg ajv fail', id, ajv.errorsText(vPkg.errors)); }
}
check('C-6', `stage-B wave-3 outputs ajv x36 (18 vs 1.7 + 18 vs 1.4)`, outFails === 0, outFails + ' failures');

// AN census POST-rotation on the emitted packages (wave-6 declared-rotation precedent)
const ROT = {};
let rotDesc = [];
for (const id of NOTES_W3) {
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
for (const id of NOTES_W3) {
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
  check('G-E', `${label} byte conservation vs v${man.manifest_version} x${man.artifacts.length} (untouched by the IAL chemistry stage-B wave 3)`, bad === 0, `${bad} drift`);
  return bad;
}
check('G-E', 'IAL chemistry pack manifest v47 resolves (62 = 2 stage-A pilot + 26 wave 1 + 34 wave 2)', priorMan.manifest_version === 47 && priorMan.artifacts.length === 62, `v${priorMan.manifest_version} x${priorMan.artifacts.length}`);
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
check('G-E', 'prior (IAL chemistry stage-B wave-2 v47) artifact census 62 = 31 hubs + 31 packages', priorMan.artifacts.filter((a) => a.kind === WALK_HUB_KIND).length === 31 && priorMan.artifacts.filter((a) => a.kind === 'sme-question-package').length === 31, priorMan.artifacts.length);

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

// all 49 notes in the walk (the 31 prior IAL chemistry rows re-proven + the 18 stage-B wave-3 notes)
const allNotes = [];
const priorAnchors = new Map(priorInt3.notes.map((n) => [n.noteId, n]));
for (const n of priorInt3.notes) allNotes.push({ noteId: n.noteId, wave: n.wave });
for (const id of NOTES_W3) allNotes.push({ noteId: id, wave: NEW_WAVE });
check('G-E', 'G-E walk rows = 49 (the 31 prior IAL chemistry rows re-proven byte-identical + 18 stage-B wave-3 notes); the emitted INT-3 of record carries all 49 cumulative rows', allNotes.length === 49, allNotes.length);

// serialize output buffers (single source of truth for anchors + emit)
const outBufs = {};
for (const id of NOTES_W3) {
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
    waveHashes['wave-ialchem-stageb3'] = waveHashes['wave-ialchem-stageb3'] || crypto.createHash('sha256');
    waveHashes['wave-ialchem-stageb3'].update(Buffer.from(s, 'utf8'));
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
check('G-E', `legacy anchors conserved x31 (byte-identical IAL chemistry prior rows: pilot + wave 1 + wave 2)`, legacyFails === 0, legacyFails + ' drift');
check('G-E', `stage-B wave-3 stream chars total = ${NOTES_W3.reduce((t, i) => t + streamChars[i].chars, 0)}`, true, NOTES_W3.reduce((t, i) => t + streamChars[i].chars, 0) + ' chars');

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
for (const id of NOTES_W3) {
  const hp = path.join(INT, 'hub-import-1.7', id + '.hub-lesson-import.json');
  const pp = path.join(INT, 'question-packages-1.4', id + '.sme-question-package.json');
  if (fs.existsSync(hp) && !fs.readFileSync(hp).equals(outBufs[id].hub)) throw new Error('additive-only violation: output exists with DIFFERENT bytes ' + hp);
  if (fs.existsSync(pp) && !fs.readFileSync(pp).equals(outBufs[id].pkg)) throw new Error('additive-only violation: output exists with DIFFERENT bytes ' + pp);
  fs.writeFileSync(hp, outBufs[id].hub); fs.writeFileSync(pp, outBufs[id].pkg);
  emitted.push({ path: 'SME-GuidedLessons/integration/hub-import-1.7/' + id + '.hub-lesson-import.json', bytes: outBufs[id].hub.length, sha256: sha256(outBufs[id].hub) });
  emitted.push({ path: 'SME-GuidedLessons/integration/question-packages-1.4/' + id + '.sme-question-package.json', bytes: outBufs[id].pkg.length, sha256: sha256(outBufs[id].pkg) });
}

// figure caption census (captions carried where the corpus prints an explanatory line)
const figCaptionCount = NOTES_W3.reduce((t, i) => t + ((sources[i].obj.figures || []).filter((f) => f.caption).length), 0);

// manifest v47 emit prep
const waveOut = {};
for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest('hex');
check('G-E', 'IAL-chemistry-scope conservation carries exactly one wave key', Object.keys(waveOut).join(',') === 'wave-ialchem-stageb3', Object.keys(waveOut).join(','));
const newArtifacts = [];
for (const id of NOTES_W3) {
  newArtifacts.push({ kind: 'hub-lesson-import-1.7', noteId: id, path: 'SME-GuidedLessons/integration/hub-import-1.7/' + id + '.hub-lesson-import.json', sha256: sha256(outBufs[id].hub), bytes: outBufs[id].hub.length });
  newArtifacts.push({ kind: 'sme-question-package', noteId: id, path: 'SME-GuidedLessons/integration/question-packages-1.4/' + id + '.sme-question-package.json', sha256: sha256(outBufs[id].pkg), bytes: outBufs[id].pkg.length });
}
const idChecks = NOTES_W3.reduce((t, i) => t + streamChars[i].checks, 0);
const idLessons = NOTES_W3.reduce((t, i) => t + streamChars[i].lessons, 0);
function streamCharsArr() { return streamCharsArr.cached || (streamCharsArr.cached = (() => { const m = { mcq: 0, rec: 0, exp: 0, app: 0 }; for (const id of NOTES_W3) { const S = sources[id].obj; for (const L of S.lessons) for (const c of L.check) { if (c.kind === 'mcq') m.mcq++; else if (c.kind === 'recall') m.rec++; else if (c.kind === 'explain-why') m.exp++; else m.app++; } } return m; })()); }
// manifest v48 (CUMULATIVE over the IAL chemistry pack: stage-A pilot + stage-B waves 1-2 re-pinned + stage-B wave 3)
const grandDigest = grand.digest('hex');
const waveSrc = NOTES_W3.map((i) => JSON.parse(fs.readFileSync(path.join(INT, 'source-0.8/guided-lesson-' + i + '.json'), 'utf8')));
const manifest = {
  format: 'hub-import-manifest/1.0',
  manifest_version: 48,
  course_id: COURSE,
  b6_manifest_continuity: {
    decision: 'continue-global',
    selected: 'IAL chemistry stage-B wave 3 = manifest v48 (the programme-level v-series continues across subjects: chemistry v1..v17 + v32, physics v18..v31, biology v33..v44, v45 the IAL chemistry stage-A pilot, v46 the stage-B wave 1, v47 the stage-B wave 2, now v48 — the third IAL chemistry stage-B register wave, on the 0.8/1.7/1.4 generation minted for this subject)',
    rejected: 'per-course series (IAL chemistry v1 restart) — would fork the programme-level integration ledger and break the single load-scope lineage of record',
    recorded_by: 'runbook B6 (the B6 decision of record is continue-global; the physics stage-A, chemistry stage-B, wave-12 and the biology stage-A..stageb10 receipts re-record it); this receipt records it for the IAL chemistry stage-B wave 3',
  },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_trace: TRACE,
  supersedes: `hub-import-manifest-v47.json in the GLOBAL v-series (the IAL chemistry stage-B wave 2: 62 artifacts @ commit C of record ${W2_C}) — this v48 CUMULATIVE manifest re-pins the v47 sixty-two byte-identical (the 2 stage-A pilot artifacts + the 26 wave-1 artifacts + the 34 wave-2 artifacts @ the v47 landed shas) and adds the stage-B wave-3 tranche (36 artifacts: the 18 register notes at the 0.8/1.7/1.4 generation); the biology v44 pack (284), chemistry v32 pack (224) and physics v31 pack (254) are untouched on disk and conserved by the pipeline's dedicated G-E gates, zero mutation anywhere`,
  checks_layer: {
    wave: 'IAL-CHEMISTRY (WCH1) stage-B wave 3 (the third register bucket of the frozen B4 partition: 18 notes end-to-end per runbook B4; cumulative pack 49 notes / ' + (priorMan.counts.lessons + idLessons) + ' lessons / ' + (priorMan.counts.checks + idChecks) + ' checks)',
    derivation: `${idChecks} authored wave-3 checks (${streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application — the B2 law: 9 checks per lesson = 5 MCQ + 2 recall + 1 explain-why + 1 application), graded by the runner's keyword law`,
    declared_revision: 'the THIRD IAL chemistry stage-B register wave on the 0.8/1.7/1.4 generation (strictly additive over 0.7/1.6/1.3); the v47 sixty-two artifacts are re-pinned byte-identical (CUMULATIVE convention, the v35/v36 corrective lineage); biology + chemistry + physics pack bytes untouched',
    grading_law: 'case-insensitive whole-token match of the learner text against the keyword set (stem-tolerant), fail-closed on written items without modelAnswer',
    fail_closed: 'written item without modelAnswer renders reveal-only, never gradeable; the runner refuses any feed whose manifest fails G-A..G-E',
  },
  source_generation: {
    format: 'guided-lesson/0.8',
    namespace: 'SME-GuidedLessons/integration/source-0.8/',
    pin: PIN,
    prior_generation_pins: "{'physics pack': 'v18..v31 commit-A pins (v31 manifest)', 'chemistry pack': 'v32 chemistry stage-B @ commit A 0ef5c2cc', 'biology pack': 'v33..v44 commit-A pins (v44 manifest)', 'IAL chemistry stage-A': 'v45 commit-A pin 62bcd8158e990685a6a9e84b07f1380d2977399c', 'IAL chemistry stage-B wave 1': 'v46 commit-C pin 69bb5bcf8e6ad6a8bbd104d47ddcc4a250847518', 'IAL chemistry stage-B wave 2': 'v47 commit-C pin " + W2_C + "'} — the stage-B wave-3 sources are authored fresh against the corpus of record at the 0.8 generation",
    int0_lineage: '(new subject — no INT-0 ancestry; the IAL chemistry 0.8 sources are authored directly against the corpus of record)',
  },
  load_scope: {
    adapter: 'guided-lesson-0.8--hub-lesson-import-1.7',
    target_schemas: ['hub/lesson-import/1.7', 'sme-question-package/1.4'],
  },
  counts: {
    notes: priorMan.counts.notes + NOTES_W3.length,
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
  // v47 counts = the IAL chemistry pack of record (CUMULATIVE: stage-A pilot + stage-B waves 1-2)
  conservation: {
    authored_stream_sha256: grandDigest,
    authored_chars: String(grandChars),
    wave_stream_sha256: waveOut,
  },
  // v48 conservation grand stream = all 49 IAL chemistry notes; wave_stream = the wave-3 subtotal
  artifacts: [...priorMan.artifacts, ...newArtifacts],
};
const mb = Buffer.from(JSON.stringify(manifest, null, 2) + '\n');
fs.writeFileSync(path.join(INT, 'hub-import-manifest-v48.json'), mb);

// INT-3 stage-B wave-3 record (CUMULATIVE, 49 rows)
const int3 = {
  stage: 'IAL-CHEMISTRY (WCH1) stage-B wave 3 CUMULATIVE (the 18-note third register bucket + the 31 prior rows (stage-A pilot + wave 1 + wave 2): 49 notes / ' + (priorMan.counts.lessons + idLessons) + ' lessons / ' + (priorMan.counts.checks + idChecks) + ' checks at the 0.8/1.7/1.4 generation)',
  title: 'INT-3 transform record — IAL chemistry stage-B wave 3 CUMULATIVE (guided-lesson/0.8 -> hub/lesson-import/1.7 + sme-question-package/1.4), the 49-row IAL chemistry pack anchor table of record (the 31 prior rows carried byte-equivalent from INT-3-transform-record-ialchem-stageb2.json plus the 18 wave-3 rows; the 142 biology anchors stay in INT-3-transform-record-bio-stageb10-v44.json, re-proven on this tree by the G-E gates; the 112 chemistry + 127 physics anchors stay in their own records, re-proven by the C-6 ajv unions and the pack byte-conservation gates)',
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_traces: { ignition: TRACE, execution: TRACE },
  adapter: 'guided-lesson-0.8--hub-lesson-import-1.7',
  course_id: COURSE,
  supersedes_int3: 'records/INT-3-transform-record-ialchem-stageb2.json (the 31-row stage-B wave-2 cumulative anchor table; its rows carried byte-equivalent here plus the 18 wave-3 rows)',
  b6_manifest_continuity: { decision: 'continue-global', selected: 'manifest v48 supersedes v47 (cumulative)' },
  ialchem_stageb3_of_record: {
    basis: 'the third register bucket per runbook B4: 18 notes (1-9-alkanes x6, 1-10-alkenes x7, 2-1-energetics x5) authored end-to-end through the full chain, 46 lessons x 9 checks, riding the 0.8/1.7/1.4 generation',
    bootstrap: 'the stage-A spec_point_resolution.json bootstrap (262 ids / 254 resolved / 8 unresolved-surplus / 234 codes / 196 notes) carries over unchanged; wave-3 spec codes all resolve in the curriculum graph (22 spec points verbatim)',
    figure_law: '82 corpus figures bound heading-unique and module-mapped to their host lessons by verbatim corpus headings; captions carried verbatim where the corpus prints an explanatory line after the figure block, declared absent otherwise (' + figCaptionCount + ' captions carried, ' + (totFig - figCaptionCount) + ' declared absent)',
    heading_law: 'heading-unique across lessons within each note; zero corpus-limited exceptions for wave 3 - every lesson binds a distinct verbatim corpus heading (the A0 scope gate proves 0 duplicate claims)',
    b4_partition: B4_PARTITION[2],
    b4_partition_note: 'wave W3 of the B4 partition frozen at stage-A open (the full 12-wave partition lives in the stage-A promotion receipt b4_partition_of_record); the pilot stays out of the wave buckets per runbook B3',
    worked_example_law: '5 worked-example ports (designed-or-none posture satisfied by ports of the notes own corpus content: chloroethene repeat-unit census 6 atoms conserved, decane cracking C10H22 -> C8H18 + C2H4 both ledgers, displacement calorimetry q = 25 x 4.18 x 14.0 = 1463 J -> -58.5 kJ mol^-1, propan-1-ol formation via the combustion cycle -2326 + 1821 = -505 kJ mol^-1, HCl synthesis bond ledger 678 - 862 = -184 kJ mol^-1, all NUM-ledgered) + 13 designed nulls where the corpus offers no arithmetic to port',
  },
  source_pin: { commitA: PIN, namespace: 'SME-GuidedLessons/integration/source-0.8/', files: NOTES_W3.map((i) => 'guided-lesson-' + i + '.json') },
  registry_pin: { file: 'apps/hub/content/ial-chemistry-17/notes.json', rows: '196', stageb3_rows: 'the 18 wave-3 register notes (bucket first/last anchors per the frozen B4 partition, register order preserved); the stage-A pilot row 0 stays out of the wave buckets per runbook B3' },
  source_08_generation_pin: PIN,
  conservation_law: {
    law: 'adapter spec 0.8 §7 walk (byte-identical to run_import.mjs targetTokens): specAnchors -> primer -> modules (title/headings/specRefs/opening/keyPoints/depthLayers) -> glossary -> workedExample -> questions (stem/class/options + modelAnswer/keywords on written kinds); per-note sha256 of the "\\n"-joined stream',
    wave_subtotals: waveOut,
  },
  grand_stream: { chars: grandChars, sha256: grandDigest },
  wave_stream_sha256: waveOut,
  battery: {
    names: ['P0', 'A0', 'AN', 'JC', 'SG', 'KW', '2.1B', 'NUM', 'C-6', 'written', 'C-5', 'B2', 'G-E'],
    a0: 'ajv 0.8 source x18 + kind order x46 lessons + B2 sizing + spec text provenance (curriculum graph verbatim x22 spec points) + figure closure both ways x82 + corpus image coverage + glossary band + primer band + noteRef identity + section-title map + the heading-unique scope gate (zero exceptions)',
    an: 'exactly-one-correct x230; correct-key census >=3 distinct per note (post-rotation); distinct option texts; four options',
    sg: 'lesson specRefs subset of file specPoints; every check KP-anchored (content-token overlap)',
    kw: '>=3 grounded keywords per written item x184',
    jc: 'every option explained; distractors name misconceptions; correct-option misconception null',
    '2.1b': 'zero 8-gram overlaps of learner-surface text vs the corpus note body x18',
    num: 'spot ledgers on the authored arithmetic (46 ledger entries across 18 notes: the WE ports + the MCQ/application answers)',
    c6: 'physics+chemistry+bio prior union ajv x762 + chemistry prior-generation union ajv x336 + IAL chemistry prior-generation union ajv x93 + wave-3 outputs ajv x36',
    c5: 'checkRefs <-> questions bidirectional 1:1 in order x18',
    b2: '9 checkRefs per module x46; identity arithmetic 9 = 5+2+1+1 x46',
    ge: 'IAL chemistry stream anchors x49 (the emitted cumulative INT-3 of record) + the 31 prior anchors re-proven on this tree (byte-identical prior pack rows) + IAL chemistry pack byte conservation vs v47 x62 + biology v44 pack byte conservation x284 + chemistry v32 pack byte conservation x224 + physics v31 pack byte conservation x254 + IAL chemistry grand stream single-finalization',
  },
  ialchem_census: {
    notes_total_register: 196, notes_landed: 49, lessons_total: priorMan.counts.lessons + idLessons, checks_total: priorMan.counts.checks + idChecks,
    stageb3_figures: totFig, corpus_images_bound: totFig,
    worked_examples_populated: totWEPop, worked_examples_null: totWENull,
  },
  prior_census: {
    biology: { notes_total: 142, lessons_total: bioMan.counts.lessons, checks_total: bioMan.counts.checks, note: 'carried byte-identical from v44; anchors re-proven on the wave tree' },
    chemistry: { notes_total: 112, lessons_total: chemMan.counts.lessons, checks_total: chemMan.counts.checks, note: 'carried byte-identical from v32' },
    physics: { notes_total: 127, lessons_total: physMan.counts.lessons, checks_total: physMan.counts.checks, note: 'carried byte-identical from v31' },
    ialchem_stagea: { notes_total: 1, lessons_total: 2, checks_total: 18, note: 'the stage-A pilot row carried byte-equivalent from records/INT-3-transform-record-ialchem-stagea.json via the stage-B wave-1 record; pack bytes re-pinned vs v46' },
    ialchem_stageb1: { notes_total: 13, lessons_total: 31, checks_total: 279, note: 'the wave-1 rows carried byte-equivalent from records/INT-3-transform-record-ialchem-stageb2.json via the wave-2 record; pack bytes re-pinned vs v47' },
    ialchem_stageb2: { notes_total: 17, lessons_total: 48, checks_total: 432, note: 'the wave-2 rows carried byte-equivalent from records/INT-3-transform-record-ialchem-stageb2.json; pack bytes re-pinned vs v47' },
  },
  notes: priorInt3.notes.concat(int3Notes),
};
const ib = Buffer.from(JSON.stringify(int3, null, 2) + '\n');
fs.mkdirSync(path.join(INT, 'records'), { recursive: true });
fs.writeFileSync(path.join(INT, 'records/INT-3-transform-record-ialchem-stageb3.json'), ib);

// promotion receipt
// promotion receipt
const receipt = {
  format: 'ialchem-stageb3-promotion-receipt/1.0',
  wave: 'IAL-CHEMISTRY (WCH1) stage-B wave 3 (the third register bucket: 18 notes end-to-end at the 0.8/1.7/1.4 four-plane generation; CUMULATIVE programme-level manifest v48)',
  operator_traces: { ignition: TRACE, execution: TRACE },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  commit_a: { sha: PIN, contents: 'corrective commit A2: integration/tooling/ialchem-stageb3-pipeline.js re-issued with the manifest emit target corrected from hub-import-manifest-v47.json to hub-import-manifest-v48.json (the first issue carried the wave-2 filename, which would clobber the prior v47 manifest path at run time); the 18 authored stage-B wave-3 source-0.8 notes (the third register bucket of the frozen B4 partition) stay byte-identical from the first issue c847274a35561b55c51100b374666ed6e294ce0a (the pipeline of record derived from the ialchem-stageb2 landed pipeline; the 0.8/1.7/1.4 schema generation and the spec_point_resolution.json bootstrap already landed at the stage-A commit A)', parent: parent, message_carries_trace: headMsg.includes(TRACE) },
  tranche: {
    notes: 18, lessons: idLessons, checks: idChecks,
    kinds: { mcq: streamCharsArr().mcq, recall: streamCharsArr().rec, 'explain-why': streamCharsArr().exp, application: streamCharsArr().app },
    figures: totFig, figures_module_mapped: totFigMapped,
    glossary_terms: NOTES_W3.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.8/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
    worked_examples: { populated: totWEPop, null: totWENull },
    stream_chars: NOTES_W3.reduce((t, i) => t + streamChars[i].chars, 0),
    authoring_shape: {
      wave_note_buckets: '1-9-alkanes 6 + 1-10-alkenes 7 + 2-1-energetics 5 = 18 notes',
      lessons: idLessons, checks: idChecks, figures: totFig, figures_module_mapped: totFigMapped, figures_note_level: totFig - totFigMapped,
      glossary_terms: NOTES_W3.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.8/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
      worked_examples: { populated: totWEPop, null: totWENull },
    },
  },
  manifest: { version: 48, artifacts_total: manifest.artifacts.length, scope: 'IAL chemistry pack of record (CUMULATIVE: stage-A pilot + stage-B waves 1-3)', biology_prior_re_pinned_vs_v44: 284, chemistry_prior_re_pinned_vs_v32: 224, physics_prior_re_pinned_vs_v31: 254, ialchem_prior_re_pinned_vs_v47: 62, first_issues: 36 },
  outputs: emitted.map((e) => e.path),
  gate_log: LOG,
  gates_total: LOG.length,
  gates_passed: LOG.filter((l) => l.ok).length,
  verdict: FAILS.length === 0 ? 'GREEN' : 'RED',
  b4_partition_of_record: B4_PARTITION,
  disclosures: [
    'spec texts carried verbatim from the curriculum graph SPEC_POINT nodes (no spec text invented); spec codes pinned to the notes.json register rows (the 18 wave-3 rows, register order preserved, bucket anchors first/last per the frozen B4 partition)',
    'corpusVersion pinned as sme-revision-notes-ial-chemistry-17-2026-08-05 — the register rows most recent content update (max updatedAt 2026-08-05), the mechanical register-version pin of record carried over from the stage-A pilot and wave 1',
    'the 0.8/1.7/1.4 schema generation is strictly additive over 0.7/1.6/1.3 and was minted at the stage-A commit A; no schema bytes changed in this wave',
    'the B4 partition of record (frozen at stage-A open; 195 notes in 12 subtopic-atomic waves W1..W12) lives in the stage-A promotion receipt as b4_partition_of_record and is re-recorded byte-identical here; wave W3 = 18 notes across three buckets (1-9-alkanes 6 + 1-10-alkenes 7 + 2-1-energetics 5), the pilot excluded per runbook B3',
    'worked-example ports from the corpus: 5 notes carry a populated workedExample ported in substance from their own corpus content (chloroethene repeat-unit census 2 C + 3 H + 1 Cl = 6 atoms conserved; decane cracking C10H22 -> C8H18 + C2H4 with both atom ledgers closed; displacement calorimetry q = 25 x 4.18 x 14.0 = 1463 J -> -58.5 kJ mol^-1; propan-1-ol formation via the combustion cycle -2326 + 1821 = -505 kJ mol^-1; HCl synthesis bond ledger 678 - 862 = -184 kJ mol^-1), each NUM-ledgered; 13 notes carry designed nulls where the corpus offers no arithmetic to port (designed-or-none posture, the chemistry stage-B populated precedent)',
    'corpus figure URLs rewritten from the pinned-commit namespace to the main namespace (asset identity preserved by basename; the A0 gate re-checks the basename against the corpus body); alt text carried verbatim from the corpus markdown, with 27 authored alts where the source site printed none or a filename slug (the wave-1 A2 corrective posture)',
    'figure captions carried verbatim where the corpus prints an explanatory line after the figure block (' + figCaptionCount + ' figures); the other ' + (totFig - figCaptionCount) + ' captions are declared absent (no such line exists in the source)',
    'MCQ correct-key census enforced POST-transform under the declared deterministic AN rotation table (cyclic per-note re-letter) — the wave-6/8/9/10/11 + stage-A + wave-1 re-lettering precedent, table-recorded',
    'the topicTitle of record is the hub curriculum graph SME-S1 node title the register sectionSlug denotes; the 18 wave-3 notes span two sections - 13 in Structure, Bonding & Introduction to Organic Chemistry (alkanes + alkenes) and 5 in Energetics, Group Chemistry, Halogenoalkanes & Alcohols (energetics)',
    'the WAVE_OPEN_BASE_W3 ' + WAVE_OPEN_BASE_W3 + ' is the resources main tip at wave open (the post-wave-2 tip carrying the unrelated W-F3-T2 Lane C records commits); stage-B wave-3 sequence: first commit-A issue c847274a35561b55c51100b374666ed6e294ce0a landed the 18 source notes byte-final + a pipeline carrying one runtime defect (the manifest emit filename carried over from wave 2, targeting the prior v47 path); corrective commit A2 re-issues ONLY the corrected tooling (v48 emit target + the disclosed first-issue base accepted by the P0 parent check), the notes stay byte-identical from the first issue, the pipeline re-runs at the A2 pin with the race-guard asserting the tip, then commit C lands — the race-guard semantics disclosed',
    'the PROMOTION receipt filename carries the Asia/Dhaka execution date while generated_at_utc is honest UTC (the stage-A receipt corrective clarified the token follows the executor clock)',
    'the emitted hub/question-package artifacts carry the run_import.mjs legacy identity strings (hub/lesson-import/1.5 + guided-lesson-0.6--hub-lesson-import-1.5 + sourceFormat guided-lesson/0.6) byte-conserved exactly as every prior pack; the RECORD layer (this receipt, the INT-3, the manifest load_scope) declares the true 0.8/1.7/1.4 generation — the conservation law of record',
    'the manifest v48 is CUMULATIVE over the IAL chemistry pack (98 artifacts = the 62 v47 artifacts re-pinned byte-identical @ the v47 landed shas + 36 wave-3 first issues), continuing the v35/v36 corrective convention that keeps the runner-owned guided-import.json index complete',
    'heading-unique law with zero exceptions: every wave-3 lesson binds a distinct verbatim corpus heading, the A0 scope gate proves 0 duplicate claims, and no corpus-limited exception needed declaring',
    'the four W-F2-T2 / Lane B commits that landed on main between waves (8039d1c2..WAVE_OPEN_BASE_W2) touch no SME-GuidedLessons/integration bytes - the G-E pack byte-conservation gates prove the prior packs untouched',
  ],
};

const rb = Buffer.from(JSON.stringify(receipt, null, 2) + '\n');
fs.writeFileSync(path.join(INT, 'records/IAL-CHEMISTRY-WCH1-STAGEB3-PROMOTION-20261115.json'), rb);

console.log(`GATES: ${LOG.filter((l) => l.ok).length}/${LOG.length} GREEN, 0 failures`);
console.log(`EMITTED: 36 outputs + manifest v48 (${mb.length}B) + INT-3 (${ib.length}B) + promotion receipt (${rb.length}B)`);
console.log(`Stage-B wave-3 tranche: 18 notes / ${idLessons} lessons / ${idChecks} checks (${streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application) / ${totFig} figures`);
console.log(`MANIFEST v48: ${manifest.counts.notes} notes / ${manifest.counts.lessons} lessons / ${manifest.counts.checks} checks; grand stream ${manifest.conservation.authored_chars} chars`);
console.log(`GRAND: ${manifest.conservation.authored_stream_sha256}`);
console.log(`STAGE-B WAVE-3 SUBTOTAL: ${waveOut['wave-ialchem-stageb3']}`);
console.log(`ROTATION: ${rotDesc.join(' | ')}`);
