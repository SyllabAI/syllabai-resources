# 4BI1 parse lane — worklog (T-PARSE-4BI1-1, 2026-10-21)

Times are UTC (workspace clock 2026-10-20T21:xx-23:xx = 2026-10-21 in session tz).

- **21:20** Resumed lane. Repo check: 4BI1 SOURCE present (intake commit
  `607e06b`); PDF at `data/biology/student-book.pdf` (sha256 verified again:
  `974ad65d…93006`). Playbook + PARSE_STANDARD + physics/chemistry references
  read (parse_docling_physics.py / book_structure_physics.py /
  validate_physics.py extracted from git HEAD).
- **21:30** Env: PyMuPDF 1.26.7 / pypdf 6.6.0 / pdfplumber present — no OCR
  stack needed (text-layer lane; intake T-INTAKE-4BI1-1 had re-planned).
- **21:35** probe_4bi1_structure.py: 2-up mapping pinned — R-half top-band
  digits follow `book = 2s−9` (93 hits, spreads 72–178), L-half `2s−10`
  (spreads 7–11). TOC decoded (spread 2R): **6 units** (intake guessed 4 —
  corrected), appendices A/B, glossary 309, index 320. Course structure
  (spreads 3L-3R): 22 chapters with book pages; openers cross-check the
  arithmetic. Front matter roman i–viii = spreads 1R–5L; book 1 = spread 5R.
- **21:50** Marker census: 15/22 LO openers matched; ANSWERS at spreads
  169R–179L (book 329–349); only 3 midline crossers (clean 2-up split).
- **22:00** Noise probes: (1) italic/display font has a broken ToUnicode CMap
  ("hvmg"=living, "chapler", "KEV POINT", "1s", "U1e", " -+ " for →); (2)
  intra-word splits ("Th is") were an ARTIFACT of probe-side span joining —
  natural span concatenation is clean (lesson L-013); (3) icon glyph junk
  ("mD", "11>", "Ell>"); (4) running headers y=13–14, question feature
  headers y≥41 — but question-bank continuation pages carry "UNIT QUESTIONS"
  IN the running header (y=14), so typing must come from page CONTEXT.
- **22:10** Question census: strict "CHAPTER QUESTIONS" on only 6 half-pages;
  **22/22 "More questions …" cross-reference lines** found → QUESTION_RANGES
  for every chapter. Unit banks: 32–37, 130–133, 182–185, 221–225, 277–279,
  301–302. Dividers near-empty (u4 = 0 lines). Back cover 349 blank (0 lines,
  11 images). Answers 329–348 (UNIT N ANSWERS headers).
- **22:20** extract_text_4bi1.py: per-half-page JSONs (natural stream order —
  y-sorting INTERLEAVES sidebars, tested and rejected). 179 spreads in ~40 s.
  First extraction (y-sorted) deleted and re-run.
- **22:30** book_structure_biology.py (22 CHAPTERS, QUESTION_RANGES,
  EXTRA_SECTIONS, 2-up helpers, markers incl. garble-tolerant forms,
  additive types did_you_know + biology_only).
- **22:35** parse_text_biology.py v1: 435 chunks — caught THREE defects in
  self-review: (a) token cleaner ate two-letter words ("composed of" →
  "composed") — corpus-destroying, rewritten surgical (PM-4); (b) char_count
  computed from tuple lengths; (c) HARD_MAX not enforced (152 chunks over
  2400). Fixed all; + opener verb-bullet LO fallback.
- **22:45** Re-run: **871 chunks**. validate_biology.py: **ALL CHECKS PASSED**
  first run (later tightened: polish keys allowed, 2-up law check added).
- **22:50** select_noisy_biology.py: broad heuristics false-fired (671/871 —
  'living/lumen' words); tightened to verified classes → **363 selected**
  (171 forced question chunks + 192 garble-scored), 0 obvious garbles missed.
- **22:55** llm_repair_biology.js (z-ai SDK, physics lineage + biology
  garble classes + garble-map-normalized LCS guard). npm install OK. Round 1:
  quota clear → 29 records in first minutes.
- **23:00** **Guard calibration** (9 rejects, all looking like GOOD repairs):
  rejects score 0.93–0.966 vs OKs ≥ 0.9716 under the map-normalized 0.97 LCS —
  icon junk is CONCATENATED to skill words ("PROBLEMSOLVINGl'!lllllP.lli,,"),
  so token-level junk rules can't reach it. Fix: character-level SYMMETRIC
  normalization (strip symbols, collapse i/l/1 runs) on both strings; replay
  ALL banked records per PM-2 → OK-min 0.9412 → threshold calibrated to
  **0.94** (playbook 0.97 was calibrated on whitespace-only damage).
  Rejects+errors purged with evidence backup (r1a_evidence.jsonl).
- **23:05** **Quota wall** (account-level 429) — intermittent windows:
  banked 91 ok / 9 rejected(pre-calibration) / rest pending. Probed with
  patience per PM-3; wall held ~45 min → **shipped round 1 PARTIAL**
  (resumable runner; JSONL skip-if-done).
- **23:15** Post-merge gates: merge_llm_biology.py — 91 applied,
  2 skill-tag sliver chunks dropped (<40 chars, junk-only), **anchor diff
  0 drift**; validate_biology.py **ALL CHECKS PASSED** (869 chunks);
  audit_polish_biology.py **PASSED** (arrow garble 37→19, icon junk
  120→99, 0 regressions). Audit metric bug fixed en route: `chapte\s*r`
  regex matched the word "chapter" itself (177 false hits — also polluted
  polish selection; corrected to `chapler\b|chapte\s+r\b`).
- **23:20** Docs: METHOD_AND_FINDINGS.md (D-1…D-10), parsed/README.md,
  book README status → PARSED; parse report updated (round 1 partial,
  quota-pending 272); CATALOG + playbook ledgers (L-012…L-015, E-002, R-002)
  prepared; commit T-PARSE-4BI1-1.

## Deliverables

- `parsed/edexcel_igcse_biology_chunks_v1.jsonl` (869 chunks, 1.3 MB)
- `parsed/full_book_textlayer.md`, `parsed/parse_report_v1.json`,
  `parsed/load_rag.py`, `parsed/README.md`
- `pipeline/scripts/` (extract / structure / chunker / validator / select /
  repair / merge / audit / calibrate / probes), `pipeline/METHOD_AND_FINDINGS.md`,
  `pipeline/evidence/` (probe outputs, repair evidence)
- playbook ledgers: L-012…L-015, E-002, R-002 (books/README.md §9)
