// Content module 1 of 2 for the Wave-1 report of record (sections 1-5).
// Element grammar: {t:"h1"|"h2"|"p", x:"..."} and {t:"table", caption, header[], rows[][], widths[]}.
module.exports = [
  { t: "h1", x: "1. Executive Summary" },
  { t: "p", x: "Wave-1, the instrumented first authoring wave of the guided-learning programme, is complete of record: all ten roster notes were authored end to end through the restored A1 toolchain, exported against the guided-lesson/0.1 schema, linted, and filed with per-phase timing receipts. Every note passed the schema validation with zero lint hard-fail violations, and the only warnings present are the seven designed declarations of record (six notes whose source carries no worked example, declared via the workedExample null warning, plus one non-numeric worked example declared via the arithmetic-verification warning). The wave ran under the operator OPEN posture decided 2026-10-23, build it fully, which retains the measurement discipline of the instrumented wave while dissolving its gate function." },
  { t: "p", x: "The output volume of record is 24 lessons, 116 key points and 120 explained checks across the ten notes, with every one of the 360 check distractors naming the specific misconception it is designed to catch. The focused authoring time of record is 2,830 seconds, 0.79 hours in total, a mean of 0.08 hours per note or 0.033 hours per lesson. These figures measure the model-drafted, declared-assisted pipeline under the OPEN posture; they are not unassisted human rates, and the corpus-wide arithmetic of record remains the exposure bands of 28, 56 and 93 author-days rather than any extrapolation of the wave mean. The phase shape of the wave concentrates in load-and-read (P0, 31.2 percent) and check authoring (P7, 26.3 percent), which matches the expectation in the A1 specification that checking is where tooling or team shape helps later waves." },
  { t: "p", x: "This round also closed an integrity finding against the lane's own work: notes seven through ten initially carried receipts whose assistance flags understated the model-drafted phases, and the run harness was found not to persist its event log on the export success path, which inflated phase P8 when receipts were recomputed. Both defects were corrected of record, the receipts were restored to reconcile with the console totals at each note's successful export, and the harness defect is filed for patching before any future timed wave. Section 6 documents the full integrity trail." },

  { t: "h1", x: "2. Posture and Protocol of Record" },
  { t: "p", x: "The posture of record is OPEN, recorded on the operator's explicit instruction \u201copen (build it fully)\u201d (trace 1a1683ec43a016a9) and captured in the brief of record A5-Posture-Decision-Brief-Open-20261023.docx, which supersedes the same-day METERED provisional entry. Under OPEN, the programme commits to authoring the full guided study and guided practice corpus (112 notes of record, structured one-to-one against the SME analysis), the first instrumented wave is retained as a measurement discipline rather than a gate, the approximately two-hours-per-note open-flip threshold is dissolved, and learner-side metering design is deferred. The not-build boundary remains closed." },
  { t: "p", x: "The measurement discipline retained from the A1 specification, section 7, is: per-phase clocks P0 through P8 with the total of the phase clocks as the authoring time of record; explicit logged pauses with reason codes; a corpus pinned to the local snapshot taken at first read, with any mid-run corpus change voiding the run; and declared assistance per phase, so the measured number is always interpretable as pure-human or declared-assisted and never silently hybrid. Two adaptations of record apply under OPEN and are disclosed in every receipt: drafting assistance is the norm rather than the exception (each receipt declares exactly which phases drafted content), and the wave is a ten-note roster rather than the single-note timed run of the original A1 protocol, because the posture decision converted the wave from a gate-feeding measurement into the first production increment." },
  { t: "p", x: "Standing lane constraints were honoured throughout: no workflow dispatch, no secret writes, no waiter or scheduler processes, Vercel lanes GET-only, zero database writes, and the single database contact of the entire wave was one read-only SELECT snapshot pull at wave open. Tokens were never echoed; fingerprints only appear where provenance required them." },

  { t: "h1", x: "3. Corpus Pin and Roster of Record" },
  { t: "p", x: "The corpus of record was pinned once, at wave open, by a single SELECT over the revision_note table of the read-only production replica, producing .tmp/wave1/corpus-snapshot.json with all 112 notes (361,272 characters) at the single corpus version sme-revision-notes-igcse-chemistry-19-2026-09-18. The snapshot manifest verifies the census of record (4 topics, 28 subtopics, 112 notes; per-topic note counts 40, 36, 15 and 21) and the three-way SHA-256 consistency of every note body from database to snapshot to manifest. No further database contact occurred for the rest of the wave; all authoring ran against the local pin, and every receipt carries the pin's corpus version and body hash." },
  { t: "p", x: "The ten-note roster of record was fixed against the format minimums to maximise information about format overfit, the risk named in the A1 specification, section 9: it spans more than eight note genres (definitional, procedural calculation, equation construction, multi-spec-point worked notes, classification, family trends, parallel test structures, practical methods, concepts with a worked system example, and drawing skills) and both size extremes of the authored band. The A1 seed note (Atoms: Definitions and Structure, rn_kb2VkFMdBTbmG33t) is retained as the calibration reference layer of record and is deliberately excluded from the timed roster. Table 1 lists the roster." },
  {
    t: "table",
    caption: "Table 1: Wave-1 roster of record (order of authoring)",
    widths: [6, 30, 26, 22, 16],
    header: ["#", "Note (title of record)", "Genre coverage", "Spec points", "Body chars"],
    rows: [
      ["1", "Solutions", "Definitional, single lesson", "1.4", "920"],
      ["2", "Moles, Mass & RFM", "Procedural calculation", "1.27, 1.28", "3,937"],
      ["3", "Writing Half-Equations", "Procedural, equations", "1.59C", "4,130"],
      ["4", "Word & Chemical Equations", "Worked equations, largest body", "1.25", "9,662"],
      ["5", "Classify Metals & Non-Metals", "Classification comparison", "1.20, 1.21", "2,160"],
      ["6", "Group 1 (Alkali Metals)", "Family trends, 3 spec points", "2.1, 2.2, 2.3", "6,191"],
      ["7", "Tests for Anions", "Parallel test structure", "2.48", "4,788"],
      ["8", "Practical: Prepare Copper(II)Sulfate", "Practical method", "2.39, 2.42", "1,983"],
      ["9", "Dynamic Equilibrium", "Concepts + system example", "3.19C, 3.20C", "2,792"],
      ["10", "Addition Polymers", "Drawing skill, 3 spec points", "4.44, 4.45, 4.46", "4,051"],
    ],
  },

  { t: "h1", x: "4. Results of Record" },
  { t: "p", x: "Table 2 carries the per-note figures of record after the integrity corrections of section 6. The focused total is the sum of the nine phase clocks; the wall-clock span additionally shows rework and turn-boundary time, which is why it exceeds the focused total on the notes that crossed session boundaries. Five logged pauses of record exist across the wave, every one a turn-boundary pause resumed in the following session, and no pause was silent." },
  {
    t: "table",
    caption: "Table 2: Per-note results of record (post integrity pass, 2026-10-24)",
    widths: [24, 8, 8, 12, 12, 10, 10, 16],
    header: ["Note", "Lessons", "Checks", "Focused s", "h/note", "Wall s", "Pauses", "Assisted phases"],
    rows: [
      ["Solutions", "1", "5", "214", "0.06", "214", "0", "P1-P7"],
      ["Moles, Mass & RFM", "2", "10", "217", "0.06", "2,152", "2", "P1-P7"],
      ["Writing Half-Equations", "3", "15", "471", "0.13", "471", "0", "P1-P7"],
      ["Word & Chemical Equations", "3", "15", "336", "0.09", "8,440", "1", "P1-P7"],
      ["Classify Metals & Non-Metals", "2", "10", "165", "0.05", "8,562", "1", "P1-P5, P7"],
      ["Group 1 (Alkali Metals)", "3", "15", "351", "0.10", "351", "0", "P1-P7"],
      ["Tests for Anions", "3", "15", "262", "0.07", "871", "1", "P1-P7"],
      ["Practical: Prepare Copper(II)Sulfate", "2", "10", "315", "0.09", "939", "0", "P1-P7"],
      ["Dynamic Equilibrium", "2", "10", "215", "0.06", "215", "0", "P2-P7"],
      ["Addition Polymers", "3", "15", "284", "0.08", "284", "0", "P2-P7"],
    ],
  },
  { t: "p", x: "The aggregate of record: 10 notes, 24 lessons, 116 key points, 120 checks; focused 2,830 seconds = 0.79 hours; mean 283 seconds = 0.08 hours per note and 0.033 hours per lesson. The phase share of the focused total is: P0 load-and-read 31.2 percent, P1 split 4.5 percent, P2 key points 7.7 percent, P3 openings 5.1 percent, P4 depth layers 9.3 percent, P5 primer and glossary 5.7 percent, P6 worked example 4.0 percent, P7 checks 26.3 percent, P8 lint and export 6.1 percent. Under the A1 specification's reading rule, the concentration in P7 (and secondarily P4) is the signal that authoring tooling for checks and layering is where later waves gain most; the large P0 share reflects model read-and-pin time over full note bodies, which is disclosed rather than buried, and which shrinks per note as the corpus pin is reused." },
  { t: "p", x: "The notes with the largest wall-clock spans (Classify Metals and Non-Metals at 8,562 seconds; Word and Chemical Equations at 8,440 seconds) crossed turn boundaries mid-authoring; their focused totals are unaffected because paused and boundary time is excluded from the phase clocks, which is precisely the separation the receipt format is designed to preserve." },

  { t: "h1", x: "5. Quality of Record" },
  { t: "p", x: "All ten layer files validate against the guided-lesson/0.1 JSON Schema (draft-07, additionalProperties false throughout, so unknown fields fail closed). All ten pass the house-style lint with zero hard-fail violations: spec-point coverage is exact (every code of record referenced, no invented codes, every referenced code carrying its official text), every check item keys exactly one correct option, every option carries an explanation, and every one of the 480 distractors names the misconception it catches. The arithmetic-verification rule evaluated the one numeric worked example of the wave (note 6's ported rubidium prediction) and its two quoted reference values trace to the steps." },
  { t: "p", x: "The complete warning inventory of the wave is seven entries, all designed declarations: six instances of the workedExample-null warning, each declaring that the source note carries no worked example (notes 1, 2, 5, 7, 8 and 10), and one instance of the no-arithmetic-expression warning, which is the declaration of record that note 6's worked example is non-numeric apart from its two quoted reference values. No style warning, no register warning, no source-fidelity warning and no template-uniformity warning survived to export on any note; the handful raised during authoring (a ten-word verbatim run, a glossary over the eight-item cap, a thirty-percent layer-length imbalance) were fixed before the clean export of record, and the export blocked once on the glossary cap before the merge that resolved it." },
  { t: "p", x: "Content discipline held across genres: source fidelity runs stayed within the eight-word limit after the one flagged key point was rephrased; the plain-words register scan is clean with all long technical-form words either glossary-backed or rephrased; British spelling and the no-exclamation house rule are respected throughout; and every primer cites its prerequisite by the exact subtopic title of record, snapshot-verified (Atomic Structure, Ionic Bonding, Acids Alkalis and Titrations, Rates of Reaction, Alkenes)." },
];
