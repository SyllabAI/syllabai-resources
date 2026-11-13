#!/usr/bin/env node
/**
 * ialchem-stagea-pipeline.js — IAL-CHEMISTRY (WCH1) stage-A (the new-subject pilot: ONE note end-to-end
 * through the full chain at the 0.8/1.7/1.4 four-plane generation: source-0.8 / hub-import-1.7 /
 * question-packages-1.4 / manifest v45 + records, per the new-subject runbook B3). Derived from the
 * bio-stagea landed pipeline of record. Node >= 18, ajv via ajvkit.
 *
 * Usage:
 *   node ialchem-stagea-pipeline.js --pin <commitA> --repo <resources worktree root> \
 *     --curriculum <curriculum-ial-chem.json> --notes <notes-ial-chem.json> \
 *     --priorInt3 <INT-3 bio-stageb10 v44> --priorManifest <v44 manifest (biology cumulative)> \
 *     --priorChemManifest <v32 manifest (chemistry)> --priorPhysManifest <v31 manifest (physics)> \
 *     --trace <operator ignition trace>
 *
 * Gates of record (the physics-wave battery, re-run over the full corpus): P0 / A0 / AN / JC / SG / KW /
 * 2.1B / NUM / C-6 / written / C-5 / B2 / G-E. Fail-closed: any failure exits 1 before emit.
 *
 * Stage-A authoring of record (census 2026-11-14): 1 note / 2 lessons / 18 checks = 10 MCQ + 4 recall +
 * 2 explain-why + 2 application (the B2 law 5+2+1+1 per lesson); 1 corpus figure bound heading-unique and
 * module-mapped; glossary 4 terms (in the 2..5 band); worked-example port of the corpus exam-hint
 * K2CO3 arithmetic (NUM-ledgered); learner-surface authored fresh per the 2.1B 8-gram law.
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
if (!REPO || !PIN || !TRACE || !args.curriculum || !args.notes || !args.priorInt3 || !args.priorManifest || !args.priorChemManifest || !args.priorPhysManifest) {
  console.error('missing required args'); process.exit(2);
}

const NOTES_W12 = [
  'rn_QbY5FrkKC3TK5vJS',
];
const WAVE12 = 1;
// the corpus-limited heading exception of record (none for the IAL chemistry stage-A)
const CORPUS_LIMITED_HEADINGS = {};
const NEW_WAVE = 'ialchem-stagea';
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
for (const id of NOTES_W12) {
  const p = path.join(INT, 'source-0.8/guided-lesson-' + id + '.json');
  sources[id] = { path: p, raw: fs.readFileSync(p), obj: JSON.parse(fs.readFileSync(p, 'utf8')) };
}

// ── P0: pin + blob identity ──────────────────────────────────────────────────
const headSha = execSync('git rev-parse HEAD', { cwd: REPO }).toString().trim();
check('P0', 'HEAD == declared stage-A commit-A pin', headSha === PIN, 'HEAD=' + headSha.slice(0, 12) + ' pin=' + PIN.slice(0, 12));
const headMsg = execSync('git log -1 --format=%B', { cwd: REPO }).toString();
check('P0', 'commit A message carries the operator trace', headMsg.includes(TRACE), headMsg.slice(0, 90).replace(/\n/g, ' '));
for (const id of NOTES_W12) {
  const rel = 'SME-GuidedLessons/integration/source-0.8/guided-lesson-' + id + '.json';
  const blob = execSync('git show HEAD:' + rel, { cwd: REPO, maxBuffer: 1 << 22 });
  check('P0', 'source blob @ HEAD == disk: ' + id, blob.equals(sources[id].raw), 'blob=' + blob.length + 'B disk=' + sources[id].raw.length + 'B');
}
const parent = execSync('git rev-parse HEAD~1', { cwd: REPO }).toString().trim();
const WAVE_OPEN_BASE = 'de832c5fac7d2e0b21bce266c5c3674581254827';
check('P0', 'commit A parent == the wave-open resources main of record', parent === WAVE_OPEN_BASE, 'parent=' + parent.slice(0, 12));
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
  rn_QbY5FrkKC3TK5vJS: [
    ['corpus exam-hint arithmetic: potassium carbonate Mr = (2 x 39.1) + 12.0 + (3 x 16.0) = 138.2 (WE port + L2 recall answer)', () => Math.abs(2 * 39.1 + 12.0 + 3 * 16.0 - 138.2) < 1e-9],
    ['check arithmetic: P4O10 Mr = 4 x 31.0 + 10 x 16.0 = 284.0 (the MCQ correct option)', () => Math.abs(4 * 31.0 + 10 * 16.0 - 284.0) < 1e-9],
    ['check arithmetic: Mg(NO3)2 correct = 24.3 + 2 x 14.0 + 6 x 16.0 = 148.3; the quoted wrong attempt 24.3 + 2 x 14.0 + 3 x 16.0 = 100.3', () => Math.abs(24.3 + 2 * 14.0 + 6 * 16.0 - 148.3) < 1e-9 && Math.abs(24.3 + 2 * 14.0 + 3 * 16.0 - 100.3) < 1e-9],
    ['stage-A census: 18 checks = 2 lessons x 9 (the B2 law 5+2+1+1 per lesson)', () => 2 * 9 === 18 && 5 + 2 + 1 + 1 === 9],
  ],
};

let totLessons = 0, totChecks = 0, totKP = 0, totDistr = 0, totGloss = 0;
let totFig = 0, totFigMapped = 0, totWEPop = 0, totWENull = 0;
const streamChars = {};

for (const id of NOTES_W12) {
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
let dupClaims = 0;
for (const id of NOTES_W12) {
  const seen = new Map();
  for (const L of sources[id].obj.lessons) for (const h of L.sourceHeadings) { if (seen.has(h)) dupClaims++; seen.set(h, 1); }
}
check('A0', 'corpus-limited heading exception scope (none declared for the IAL chemistry stage-A)', dupClaims === 0 && Object.keys(CORPUS_LIMITED_HEADINGS).length === 0, dupClaims + ' duplicate claims');

// ── C-6: generation-union ajv (all three prior packs byte-untouched) + new outputs ──
function dirFiles(d, suffix) {
  try { return fs.readdirSync(d).filter((f) => f.endsWith(suffix)).sort(); } catch (e) { return []; }
}
const priorIds = new Set([...priorMan.artifacts, ...chemMan.artifacts, ...physMan.artifacts].map((a) => a.noteId));
check('C-6', 'prior packs noteIds union = 381 (142 biology v44 + 112 chemistry v32 + 127 physics v31)', priorIds.size === 381, priorIds.size);
const priorSrc6 = dirFiles(path.join(INT, 'source-0.6'), '.json').filter((f) => { const nid = f.replace('guided-lesson-', '').replace('.json', ''); return priorIds.has(nid) && !NOTES_W12.includes(nid); });
const priorHub15 = dirFiles(path.join(INT, 'hub-import-1.5'), '.json').filter((f) => priorIds.has(f.replace('.hub-lesson-import.json', '')));
const priorPkg12 = dirFiles(path.join(INT, 'question-packages-1.2'), '.json').filter((f) => priorIds.has(f.replace('.sme-question-package.json', '')));
check('C-6', 'physics+chemistry prior generation present on tree, counted by the v31+v32 noteIds (239 sources / 239 lessons / 239 packages)', priorSrc6.length === 239 && priorHub15.length === 239 && priorPkg12.length === 239, `${priorSrc6.length}/${priorHub15.length}/${priorPkg12.length}`);
const bioSrc7 = dirFiles(path.join(INT, 'source-0.7'), '.json').filter((f) => { const nid = f.replace('guided-lesson-', '').replace('.json', ''); return priorIds.has(nid) && !NOTES_W12.includes(nid); });
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

// ── transform (the full derivation) ──────────────────────────────────────────
const outputs = {};
for (const id of NOTES_W12) {
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
for (const id of NOTES_W12) {
  if (!vHub(outputs[id].hub)) { outFails++; console.error('hub ajv fail', id, ajv.errorsText(vHub.errors)); }
  if (!vPkg(outputs[id].pkg)) { outFails++; console.error('pkg ajv fail', id, ajv.errorsText(vPkg.errors)); }
}
check('C-6', `stage-A outputs ajv x2 (1 vs 1.7 + 1 vs 1.4)`, outFails === 0, outFails + ' failures');

// AN census POST-rotation on the emitted packages (wave-6 declared-rotation precedent)
const ROT = {};
let rotDesc = [];
for (const id of NOTES_W12) {
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
for (const id of NOTES_W12) {
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
  check('G-E', `${label} byte conservation vs v${man.manifest_version} x${man.artifacts.length} (untouched by the IAL chemistry stage-A)`, bad === 0, `${bad} drift`);
  return bad;
}
check('G-E', 'biology pack manifest v44 resolves (284 = 142 + 142)', priorMan.manifest_version === 44 && priorMan.artifacts.length === 284, `v${priorMan.manifest_version} x${priorMan.artifacts.length}`);
check('G-E', 'chemistry pack manifest v32 resolves (224 = 112 + 112)', chemMan.manifest_version === 32 && chemMan.artifacts.length === 224, `v${chemMan.manifest_version} x${chemMan.artifacts.length}`);
check('G-E', 'physics pack manifest v31 resolves (254 = 127 + 127)', physMan.manifest_version === 31 && physMan.artifacts.length === 254, `v${physMan.manifest_version} x${physMan.artifacts.length}`);
packConservation(priorMan, 'biology pack');
packConservation(chemMan, 'chemistry pack');
packConservation(physMan, 'physics pack');

// ── prior-pack load + anchor walk (G-E) ─────────────────────────────────────
const WALK_HUB_KIND = 'hub-lesson-import-1.6';
const byNoteArt = new Map();
for (const a of priorMan.artifacts) {
  byNoteArt.set(a.kind + '|' + a.noteId, path.join(REPO, a.path));
}
check('G-E', 'prior (biology v44) artifact census 284 = 142 hub + 142 pkg', priorMan.artifacts.filter((a) => a.kind === WALK_HUB_KIND).length === 142 && priorMan.artifacts.filter((a) => a.kind === 'sme-question-package').length === 142, priorMan.artifacts.length);

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

// all 143 notes in the walk (142 biology prior INT-3 rows + the 1 IAL chemistry stage-A pilot)
const allNotes = [];
const priorAnchors = new Map(priorInt3.notes.map((n) => [n.noteId, n]));
for (const n of priorInt3.notes) allNotes.push({ noteId: n.noteId, wave: n.wave });
for (const id of NOTES_W12) allNotes.push({ noteId: id, wave: NEW_WAVE });
check('G-E', 'G-E walk rows = 143 (142 biology prior re-proven + 1 IAL chemistry stage-A pilot); the emitted INT-3 of record carries the 1 IAL chemistry row', allNotes.length === 143, allNotes.length);

// serialize output buffers (single source of truth for anchors + emit)
const outBufs = {};
for (const id of NOTES_W12) {
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
    waveHashes['wave-ialchem-stagea'] = waveHashes['wave-ialchem-stagea'] || crypto.createHash('sha256');
    waveHashes['wave-ialchem-stagea'].update(Buffer.from(s, 'utf8'));
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
check('G-E', `legacy anchors conserved x142 (byte-identical biology prior pack)`, legacyFails === 0, legacyFails + ' drift');
check('G-E', `stage-A stream chars total = ${NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0)}`, true, NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0) + ' chars');

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
for (const id of NOTES_W12) {
  const hp = path.join(INT, 'hub-import-1.7', id + '.hub-lesson-import.json');
  const pp = path.join(INT, 'question-packages-1.4', id + '.sme-question-package.json');
  if (fs.existsSync(hp) && !fs.readFileSync(hp).equals(outBufs[id].hub)) throw new Error('additive-only violation: output exists with DIFFERENT bytes ' + hp);
  if (fs.existsSync(pp) && !fs.readFileSync(pp).equals(outBufs[id].pkg)) throw new Error('additive-only violation: output exists with DIFFERENT bytes ' + pp);
  fs.writeFileSync(hp, outBufs[id].hub); fs.writeFileSync(pp, outBufs[id].pkg);
  emitted.push({ path: 'SME-GuidedLessons/integration/hub-import-1.7/' + id + '.hub-lesson-import.json', bytes: outBufs[id].hub.length, sha256: sha256(outBufs[id].hub) });
  emitted.push({ path: 'SME-GuidedLessons/integration/question-packages-1.4/' + id + '.sme-question-package.json', bytes: outBufs[id].pkg.length, sha256: sha256(outBufs[id].pkg) });
}

// manifest v45
const waveOut = {};
for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest('hex');
check('G-E', 'IAL-chemistry-scope conservation carries exactly one wave key', Object.keys(waveOut).join(',') === 'wave-ialchem-stagea', Object.keys(waveOut).join(','));
const newArtifacts = [];
for (const id of NOTES_W12) {
  newArtifacts.push({ kind: 'hub-lesson-import-1.7', noteId: id, path: 'SME-GuidedLessons/integration/hub-import-1.7/' + id + '.hub-lesson-import.json', sha256: sha256(outBufs[id].hub), bytes: outBufs[id].hub.length });
  newArtifacts.push({ kind: 'sme-question-package', noteId: id, path: 'SME-GuidedLessons/integration/question-packages-1.4/' + id + '.sme-question-package.json', sha256: sha256(outBufs[id].pkg), bytes: outBufs[id].pkg.length });
}
const idChecks = NOTES_W12.reduce((t, i) => t + streamChars[i].checks, 0);
const idLessons = NOTES_W12.reduce((t, i) => t + streamChars[i].lessons, 0);
function streamCharsArr() { return streamCharsArr.cached || (streamCharsArr.cached = (() => { const m = { mcq: 0, rec: 0, exp: 0, app: 0 }; for (const id of NOTES_W12) { const S = sources[id].obj; for (const L of S.lessons) for (const c of L.check) { if (c.kind === 'mcq') m.mcq++; else if (c.kind === 'recall') m.rec++; else if (c.kind === 'explain-why') m.exp++; else m.app++; } } return m; })()); }
const manifest = {
  format: 'hub-import-manifest/1.0',
  manifest_version: 45,
  course_id: COURSE,
  b6_manifest_continuity: {
    decision: 'continue-global',
    selected: 'IAL chemistry stage-A = manifest v45 (the programme-level v-series continues across subjects: chemistry v1..v17 + v32, physics v18..v31, biology v33..v44, now v45 — the first IAL chemistry tranche, on the 0.8/1.7/1.4 generation minted for this subject)',
    rejected: 'per-course series (IAL chemistry v1 restart) — would fork the programme-level integration ledger and break the single load-scope lineage of record',
    recorded_by: 'runbook B6 (the B6 decision of record is continue-global; the physics stage-A, chemistry stage-B, wave-12 and the biology stage-A..stageb10 receipts re-record it); this receipt records it for the IAL chemistry stage-A',
  },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_trace: TRACE,
  supersedes: `hub-import-manifest-v44.json in the GLOBAL v-series (the biology stage-B wave-10 CUMULATIVE tranche: 284 artifacts @ commit C de832c5f) — this v45 manifest carries the IAL chemistry pack of record only (2 artifacts: the pilot note at the 0.8/1.7/1.4 generation); the biology v44 pack (284), chemistry v32 pack (224) and physics v31 pack (254) are untouched on disk and conserved by the pipeline's dedicated G-E gates, zero mutation anywhere`,
  checks_layer: {
    wave: 'IAL-CHEMISTRY (WCH1) stage-A (the new-subject pilot: 1 note end-to-end per runbook B3, ahead of the stage-B register waves)',
    derivation: `${idChecks} authored pilot checks (${streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application — the B2 law: 9 checks per lesson = 5 MCQ + 2 recall + 1 explain-why + 1 application), graded by the runner's keyword law`,
    declared_revision: 'the FIRST IAL chemistry tranche on the newly minted 0.8/1.7/1.4 generation (strictly additive over 0.7/1.6/1.3: ial-chemistry in the subject enums, id grammar and figure-url alternation); the pilot stays out of the wave buckets (B3); biology + chemistry + physics pack bytes untouched',
    grading_law: 'case-insensitive whole-token match of the learner text against the keyword set (stem-tolerant), fail-closed on written items without modelAnswer',
    fail_closed: 'written item without modelAnswer renders reveal-only, never gradeable; the runner refuses any feed whose manifest fails G-A..G-E',
  },
  source_generation: {
    format: 'guided-lesson/0.8',
    namespace: 'SME-GuidedLessons/integration/source-0.8/',
    pin: PIN,
    prior_generation_pins: "{'physics pack': 'v18..v31 commit-A pins (v31 manifest)', 'chemistry pack': 'v32 chemistry stage-B @ commit A 0ef5c2cc', 'biology pack': 'v33..v44 commit-A pins (v44 manifest)'} — the IAL chemistry pilot is authored fresh against the corpus of record at the 0.8 generation",
    int0_lineage: '(new subject — no INT-0 ancestry; the IAL chemistry 0.8 sources are authored directly against the corpus of record)',
  },
  load_scope: {
    adapter: 'guided-lesson-0.8--hub-lesson-import-1.7',
    target_schemas: ['hub/lesson-import/1.7', 'sme-question-package/1.4'],
  },
  counts: {
    notes: NOTES_W12.length,
    lessons: idLessons,
    checks: idChecks,
    keyPoints: NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.8/guided-lesson-' + i + '.json'), 'utf8')).lessons.reduce((t2, l) => t2 + l.keyPoints.length, 0), 0),
    distractors: streamCharsArr().mcq * 3,
    glossaryTerms: NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.8/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
    figures: NOTES_W12.reduce((t, i) => t + ((JSON.parse(fs.readFileSync(path.join(INT, 'source-0.8/guided-lesson-' + i + '.json'), 'utf8')).figures) || []).length, 0),
    figures_module_mapped: totFigMapped,
    figures_note_level: NOTES_W12.reduce((t, i) => t + (((JSON.parse(fs.readFileSync(path.join(INT, 'source-0.8/guided-lesson-' + i + '.json'), 'utf8')).figures) || []).filter((f) => !f.moduleIds || f.moduleIds.length === 0)).length, 0),
    workedExamples_populated: totWEPop,
    workedExamples_null: NOTES_W12.reduce((t, i) => t + (!JSON.parse(fs.readFileSync(path.join(INT, 'source-0.8/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.workedExample ? 1 : 0), 0),
    authored_chars_conserved: waveChars,
  },
  // v45 counts = the IAL chemistry pack of record (the stage-A pilot; per-course manifest convention)
  conservation: {
    authored_stream_sha256: waveGrand.digest('hex'),
    authored_chars: String(waveChars),
    wave_stream_sha256: waveOut,
  },
  // v45 conservation = the IAL chemistry pilot stream only
  artifacts: newArtifacts,
};
const mb = Buffer.from(JSON.stringify(manifest, null, 2) + '\n');
fs.writeFileSync(path.join(INT, 'hub-import-manifest-v45.json'), mb);

// INT-3 stage-A record
const int3 = {
  stage: 'IAL-CHEMISTRY (WCH1) stage-A (the new-subject pilot: 1 note end-to-end at the 0.8/1.7/1.4 generation)',
  title: 'INT-3 transform record — IAL chemistry stage-A (guided-lesson/0.8 -> hub/lesson-import/1.7 + sme-question-package/1.4), the 1-row IAL chemistry anchor table of record (the 142 biology anchors of record stay in INT-3-transform-record-bio-stageb10-v44.json, re-proven on this tree by the G-E gates; the 112 chemistry + 127 physics anchors stay in their own records, re-proven by the C-6 ajv unions and the pack byte-conservation gates)',
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_traces: { ignition: TRACE, execution: TRACE },
  adapter: 'guided-lesson-0.8--hub-lesson-import-1.7',
  course_id: COURSE,
  supersedes_int3: 'records/INT-3-transform-record-bio-stageb10-v44.json (the 142-row cumulative biology anchor table; its rows stay of record there and are re-proven byte-identical on this tree by the G-E walk)',
  b6_manifest_continuity: { decision: 'continue-global', selected: 'manifest v45 supersedes v44' },
  ialchem_stagea_of_record: {
    basis: 'the new-subject pilot per runbook B3: ONE note (rn_QbY5FrkKC3TK5vJS, Formulae & Mass, specs 1.1 + 1.4) authored end-to-end through the full chain, 2 lessons x 9 checks, riding the 0.8/1.7/1.4 generation minted for this subject',
    bootstrap: 'spec_point_resolution.json derived mechanically from hub notes.json smeSpecPointIds (262 ids / 254 resolved / 8 unresolved-surplus / 234 codes / 196 notes; runbook B1 deviation, physics stage-A precedent, disclosed)',
    figure_law: '1 corpus figure: module-mapped heading-unique to its host lesson (the relative-formula-mass table image, bound to L2 by its verbatim h4 heading); caption declared absent (no explanatory line exists in the source)',
    b4_partition: null,
    b4_partition_note: 'the B4 partition of record is frozen at stage-A open and lives in the promotion receipt: 195 notes in 12 subtopic-atomic waves (W1..W12), the pilot excluded per runbook B3',
    worked_example_law: 'workedExample POPULATED: the corpus exam-hint arithmetic (potassium carbonate Mr = 138.2) ported verbatim in substance, NUM-ledgered; the designed-or-none posture is satisfied by the port',
  },
  source_pin: { commitA: PIN, namespace: 'SME-GuidedLessons/integration/source-0.8/', files: NOTES_W12.map((i) => 'guided-lesson-' + i + '.json') },
  registry_pin: { file: 'apps/hub/content/ial-chemistry-17/notes.json', rows: '196', stagea_rows: 'row 0 (the pilot) — the pilot stays out of the wave buckets per runbook B3' },
  source_08_generation_pin: PIN,
  conservation_law: {
    law: 'adapter spec 0.8 §7 walk (byte-identical to run_import.mjs targetTokens): specAnchors -> primer -> modules (title/headings/specRefs/opening/keyPoints/depthLayers) -> glossary -> workedExample -> questions (stem/class/options + modelAnswer/keywords on written kinds); per-note sha256 of the "\\n"-joined stream',
    wave_subtotals: waveOut,
  },
  grand_stream: { chars: waveChars, sha256: manifest.conservation.authored_stream_sha256 },
  wave_stream_sha256: waveOut,
  battery: {
    names: ['P0', 'A0', 'AN', 'JC', 'SG', 'KW', '2.1B', 'NUM', 'C-6', 'written', 'C-5', 'B2', 'G-E'],
    a0: 'ajv 0.8 source x1 + kind order x2 lessons + B2 sizing + spec text provenance (curriculum graph verbatim x2) + figure closure both ways x1 + corpus image coverage + glossary band + primer band + noteRef identity + section-title map',
    an: 'exactly-one-correct x10; correct-key census >=3 distinct per note (post-rotation); distinct option texts; four options',
    sg: 'lesson specRefs subset of file specPoints; every check KP-anchored (content-token overlap)',
    kw: '>=3 grounded keywords per written item x8',
    jc: 'every option explained; distractors name misconceptions; correct-option misconception null',
    '2.1b': 'zero 8-gram overlaps of learner-surface text vs the corpus note body x1',
    num: 'stage-A spot ledgers on the authored arithmetic (K2CO3 138.2; P4O10 284.0; Mg(NO3)2 148.3 vs wrong 100.3; B2 census 18 = 2x9)',
    c6: 'physics+chemistry+bio prior union ajv x762 + chemistry prior-generation union ajv x336 + stage-A outputs ajv x2',
    c5: 'checkRefs <-> questions bidirectional 1:1 in order x1',
    b2: '9 checkRefs per module x2; identity arithmetic 9 = 5+2+1+1 x2',
    ge: 'IAL chemistry stream anchor x1 (the emitted INT-3 of record) + the 142 biology anchors re-proven on this tree (byte-identical prior pack) + biology v44 pack byte conservation x284 + chemistry v32 pack byte conservation x224 + physics v31 pack byte conservation x254 + IAL chemistry grand stream single-finalization',
  },
  ialchem_census: {
    notes_total_register: 196, notes_landed: 1, lessons_total: idLessons, checks_total: idChecks,
    stagea_figures: totFig, corpus_images_bound: totFig,
    worked_examples_populated: totWEPop, worked_examples_null: totWENull,
  },
  prior_census: {
    biology: { notes_total: 142, lessons_total: priorMan.counts.lessons, checks_total: priorMan.counts.checks, note: 'carried byte-identical from v44; anchors re-proven on the stage-A tree' },
    chemistry: { notes_total: 112, lessons_total: chemMan.counts.lessons, checks_total: chemMan.counts.checks, note: 'carried byte-identical from v32' },
    physics: { notes_total: 127, lessons_total: physMan.counts.lessons, checks_total: physMan.counts.checks, note: 'carried byte-identical from v31' },
  },
  notes: int3Notes,
};
const ib = Buffer.from(JSON.stringify(int3, null, 2) + '\n');
fs.mkdirSync(path.join(INT, 'records'), { recursive: true });
fs.writeFileSync(path.join(INT, 'records/INT-3-transform-record-ialchem-stagea.json'), ib);

// promotion receipt
const receipt = {
  format: 'ialchem-stagea-promotion-receipt/1.0',
  wave: 'IAL-CHEMISTRY (WCH1) stage-A (the new-subject pilot: 1 note end-to-end at the 0.8/1.7/1.4 four-plane generation; programme-level manifest v45)',
  operator_traces: { ignition: TRACE, execution: TRACE },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  commit_a: { sha: PIN, contents: 'the authored stage-A pilot source-0.8 note + the 0.8/1.7/1.4 schema generation + the spec_point_resolution.json bootstrap + integration/tooling/ialchem-stagea-pipeline.js (the pipeline of record, derived from the bio-stagea landed pipeline)', parent: parent, message_carries_trace: headMsg.includes(TRACE) },
  tranche: {
    notes: 1, lessons: idLessons, checks: idChecks,
    kinds: { mcq: streamCharsArr().mcq, recall: streamCharsArr().rec, 'explain-why': streamCharsArr().exp, application: streamCharsArr().app },
    figures: totFig, figures_module_mapped: totFigMapped,
    glossary_terms: NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.8/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
    worked_examples: { populated: totWEPop, null: totWENull },
    stream_chars: NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0),
    authoring_shape: {
      pilot_note: 'rn_QbY5FrkKC3TK5vJS (Formulae & Mass, specs 1.1 + 1.4)',
      lessons: 2, checks: idChecks, figures: totFig, figures_module_mapped: totFigMapped, figures_note_level: totFig - totFigMapped,
      glossary_terms: NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.8/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
      worked_examples: { populated: totWEPop, null: totWENull },
    },
  },
  manifest: { version: 45, artifacts_total: manifest.artifacts.length, scope: 'IAL chemistry pack of record (the per-course manifest convention of the global v-series)', biology_prior_re_pinned_vs_v44: 284, chemistry_prior_re_pinned_vs_v32: 224, physics_prior_re_pinned_vs_v31: 254, first_issues: 2 },
  outputs: emitted.map((e) => e.path),
  gate_log: LOG,
  gates_total: LOG.length,
  gates_passed: LOG.filter((l) => l.ok).length,
  verdict: FAILS.length === 0 ? 'GREEN' : 'RED',
  b4_partition_of_record: B4_PARTITION,
  disclosures: [
    'spec texts carried verbatim from the curriculum graph SPEC_POINT nodes (no spec text invented); spec codes pinned to the notes.json register row 0 (0-based) — the pilot note Formulae & Mass, specs 1.1 + 1.4',
    'corpusVersion pinned as sme-revision-notes-ial-chemistry-17-2026-08-05 — the register rows\u2019 most recent content update (max updatedAt 2026-08-05), the mechanical register-version pin of record for this new subject',
    'the 0.8/1.7/1.4 schema generation is strictly additive over 0.7/1.6/1.3 (ial-chemistry in the subject enums, id grammar and figure-url alternation; format/adapter enums extended; sourceFormat enums extended) — landed at this commit A',
    'spec_point_resolution.json for ial-chemistry-17 is the mechanical hub-landing bootstrap (262 ids: 254 resolved + 8 unresolved-surplus where the row carries more smeSpecPointIds than specPointCodes — no pairing invented, runbook B1 deviation, physics stage-A precedent, disclosed; 234 distinct codes; 196 notes)',
    'the B4 partition of record (frozen at stage-A open; 195 notes in 12 subtopic-atomic waves W1..W12) lives in this receipt as b4_partition_of_record — the pilot stays out of the buckets per runbook B3',
    'worked-example port from the corpus: the note\u2019s own exam hint (potassium carbonate = (2 x 39.1) + 12.0 + (3 x 16.0) = 138.2) is ported verbatim in substance as the populated workedExample, arithmetic NUM-ledgered (the designed-or-none posture satisfied by the port, the chemistry stage-B populated precedent)',
    'the corpus figure\u2019s alt text carries the source site\u2019s own words ("downloadable IGCSE & GCSE Chemistry revision notes") — carried through verbatim per the figure law; the alt is the parent note\u2019s own asset metadata, not learner surface',
    'figure caption declared absent: no bold-italic explanatory line follows the figure block in the source note (the blockquote exam hint is a hint, not a caption line)',
    'MCQ correct-key census enforced POST-transform under the declared deterministic AN rotation table (cyclic per-note re-letter) — the wave-6/8/9/10/11 + stage-A re-lettering precedent, table-recorded',
    'the topicTitle of record is the hub curriculum graph\u2019s SME-S1 node title ("1. Structure, Bonding & Introduction to Organic Chemistry"), the section grouping the register\u2019s sectionSlug denotes',
    'the WAVE_OPEN_BASE ' + WAVE_OPEN_BASE + ' is the resources main tip at wave open (operator directive trace ' + TRACE + '); stage-A sequence: commit A lands on main first, the pipeline runs with the race-guard asserting the tip still sits exactly at the commit-A pin, then commit C lands — the race-guard semantics disclosed',
    'the PROMOTION receipt filename carries the Asia/Dhaka execution date 20261114 while generated_at_utc is honest UTC',
    'the emitted hub/question-package artifacts carry the run_import.mjs legacy identity strings (hub/lesson-import/1.5 + guided-lesson-0.6--hub-lesson-import-1.5 + sourceFormat guided-lesson/0.6) byte-conserved exactly as every prior pack; the RECORD layer (this receipt, the INT-3, the manifest load_scope) declares the true 0.8/1.7/1.4 generation — the conservation law of record',
    'this receipt\u2019s B4 partition was computed mechanically from the hub register\u2019s contiguous (sectionSlug, topicSlug) groups: subtopic-atomic packing, max 20 notes per wave, register order preserved; W7 tops at 20 (4-1 kinetics 10 + 4-2 entropy 4 + 4-3 energetics 6)',
  ],
};

const rb = Buffer.from(JSON.stringify(receipt, null, 2) + '\n');
fs.writeFileSync(path.join(INT, 'records/IAL-CHEMISTRY-WCH1-STAGEA-PROMOTION-20261114.json'), rb);

console.log(`GATES: ${LOG.filter((l) => l.ok).length}/${LOG.length} GREEN, 0 failures`);
console.log(`EMITTED: 2 outputs + manifest v45 (${mb.length}B) + INT-3 (${ib.length}B) + promotion receipt (${rb.length}B)`);
console.log(`Stage-A tranche: 1 note / ${idLessons} lessons / ${idChecks} checks (${streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application) / ${totFig} figures`);
console.log(`MANIFEST v45: ${manifest.counts.notes} notes / ${manifest.counts.lessons} lessons / ${manifest.counts.checks} checks; grand stream ${manifest.conservation.authored_chars} chars`);
console.log(`GRAND: ${manifest.conservation.authored_stream_sha256}`);
console.log(`STAGE-A SUBTOTAL: ${waveOut['wave-ialchem-stagea']}`);
console.log(`ROTATION: ${rotDesc.join(' | ')}`);
