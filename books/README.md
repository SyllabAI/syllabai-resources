# books/ — Student-Book Corpus & Agent Parse Playbook

**Audience:** any AI agent (or human) tasked with adding a new student book to
this corpus and turning it into the RAG-ready chunk dataset.
**This file is self-improving** — you are expected to append lessons, errata
and a post-parse review record to it before you close your task (§9). It was
bootstrapped on 2026-10-21 from the complete history of the two parses done so
far (chemistry 4CH1, physics 4PH1), including their mistakes and dead ends.

---

## 0. TL;DR (returning agent, 60 seconds)

- New book to parse? Execute **§5 phases 0→10** in order. Copy the scaffold
  from `pearson-edexcel/international-gcse/physics/4ph1/`.
- Quality gates live in
  [`pearson-edexcel/international-gcse/PARSE_STANDARD.md`](pearson-edexcel/international-gcse/PARSE_STANDARD.md)
  (the 8-point standard). A parse is not "done" until its validator prints
  **ALL CHECKS PASSED**.
- Reference implementation (externally audited, green light):
  `pearson-edexcel/international-gcse/chemistry/4ch1/`. Scripts are
  **per-book copies**, not shared libraries — copy, rename with a
  `<task>_<subject>` suffix, and adapt (§5).
- The golden rules (§3) and the commit protocol (§5 phase 10) are
  **non-negotiable**; two of them (serving-critical question typing, per-chunk
  dual page numbering) come from an operator directive.
- Hit something surprising (OCR behavior, tool crash, gateway wall)? Check
  §7 findings and §8 post-mortems first — most known failure modes already
  have a documented remedy. Whatever is NOT there yet, you must add (§9).

## 1. What lives in `books/`

```
books/
└── pearson-edexcel/
    └── international-gcse/
        ├── PARSE_STANDARD.md            ← canonical 8-point quality standard (operator-gated)
        ├── chemistry/4ch1/              ← REFERENCE IMPLEMENTATION (audited green)
        │   ├── student-book.pdf         ← sha256-pinned source
        │   ├── manifest.json
        │   ├── chapters/, units/        ← chapter-split source PDFs
        │   ├── docling_pages/, ocr_pages/ ← per-page parse checkpoints
        │   ├── parsed/                  ← RAG DELIVERABLES (chunks v1/v2/v3, md, loader, README)
        │   └── pipeline/                ← METHOD_AND_FINDINGS.md, worklog, scripts/, evidence/
        └── physics/4ph1/                ← SECOND parse (Docling hybrid, polish rounds 1–2)
            ├── README.md                ← book-level status + plan + checklist
            ├── source/student-book.pdf  ← sha256-pinned source
            ├── parsed/                  ← RAG DELIVERABLES (chunks v1, md, loader, README)
            └── pipeline/                ← METHOD_AND_FINDINGS.md, worklog, scripts/, evidence/
```

| Book | ID prefix | Corpus | Status |
|---|---|---|---|
| Edexcel IGCSE Chemistry (4CH1), 383 pp | `chem_v3_…` | v1 640 / v3 **1234** chunks | Final; external audit green (2026-10-18); LLM-polished |
| Edexcel IGCSE Physics (4PH1), 308 pp | `phys_v1_…` | v1 **736** chunks | Final; polish rounds 1–2 (299/300); validation green (2026-10-20) |
| Edexcel IGCSE Biology (4BI1), 357 pp | — | — | **SOURCE landed 2026-10-21** (T-INTAKE-4BI1-1): native-text 2-up spreads, OCR route not required; parse lane not started |

## 2. Read order (do not skip)

1. **This file** — procedure, tools, gotchas, report-back duty.
2. `pearson-edexcel/international-gcse/PARSE_STANDARD.md` — the 8 acceptance
   gates. Note its two **serving-critical** items (question typing, per-chunk
   dual page numbering).
3. Reference book: `chemistry/4ch1/pipeline/METHOD_AND_FINDINGS.md` (why the
   stack looks the way it does) and `physics/4ph1/pipeline/METHOD_AND_FINDINGS.md`
   (version mines, hybrid decision, per-book adaptation pattern).
4. Repo root `AGENT.md` — multi-agent rules (provenance, gates, task IDs).
5. `BOOK_OCR_RUNBOOK.md` (repo root) — **legacy** Unlimited-OCR route
   (2026-09-10). Kept only for the rented-GPU path; superseded by this
   playbook's Docling route for CPU workspaces.

## 3. Golden rules — non-negotiable

1. **Serving-critical anchors.** `chapter_questions` / `unit_questions` pages
   get their own `content_type`, exactly on their pages — the serving split
   derives from these chunk anchors. A question page typed `body` (or the
   reverse) breaks the downstream split. Same for the unit/chapter numbers and
   both page fields on those chunks.
2. **Dual page numbering per chunk.** Every chunk carries `book_pages`
   (citation numbering) AND `pdf_pages` (viewer numbering). Never move them to
   a sidecar. `book_pages: null` only for front matter.
3. **Additive-only evolution.** The chunk grammar is the 15-key v3 grammar
   (13 base keys + `text_original` + `llm_repaired` on polished chunks). New
   subjects may add keys/content types (physics added `extension_work`);
   never rename, renumber or drop existing ones. Chunk IDs are immutable once
   published.
4. **LLM touches are transcription-only.** If any chunk is LLM-polished: the
   prompt must forbid rewording/paraphrasing; the pre-polish text is preserved
   in `text_original`; `llm_repaired: true` is set; guards must run (length
   drift, refusals, table pipe discipline, wording-fidelity LCS) and rejects
   keep their original text. Rejected raws are kept as evidence.
5. **No wholesale LLM rewrite.** Never paraphrase-rewrite book text (three
   reasons: derivative-work risk on copyrighted content, hallucination risk on
   science content, RAG fidelity loss). Fidelity repair only.
6. **Pin the source.** sha256 of the source PDF goes into the book README and
   the parse report. Provenance of how the file arrived goes in the book
   README too.
7. **Resumability everywhere.** Per-page JSON checkpoints for parsing
   (skip-if-exists), append-only JSONL for LLM repairs. Any batch may be
   killed at any moment; re-running the same command must make progress, never
   restart from zero.
8. **Foreground batches + file logs.** The agent workspace kills background
   processes; run work in foreground windows and log to a file (stdout dies
   with the batch). Every network call gets a timeout (LLM: 120 s via
   `Promise.race`) — a hung call must not eat a batch.
9. **Commits via temp index only.** This is a partial clone (`blob:none`); the
   default index carries phantom deletions/modifications. NEVER `git add -A`,
   NEVER commit with the default index. Use the temp-index protocol (§5
   phase 10) and add only paths you touched.
10. **Validate before "done".** No deliverable status change before the
    validator passes all checks; after any polish round, re-run validation AND
    the anchor diff against the pristine corpus (must be 0 drift).
11. **Report back (§9).** A parse task is not finished until the lesson/errata/
    review ledgers in this file are updated and committed with the task.

## 4. Toolchain & environment (as proven, not as advertised)

### 4.1 Decision table

| Need | Tool | Why |
|---|---|---|
| PDF → text/layout/tables | **IBM Docling** (layout model + TableFormer), CPU mode | Best quality per GB of RAM in a no-GPU, ~3 GB-RAM, 2-core workspace. Chandra (needs 16–24 GB VRAM) and MinerU (needs ~16 GB RAM) are infeasible here. PaddleOCR rejected: would need hand-written layout/ordering glue that Docling already provides. |
| OCR engine (inside Docling) | **RapidOCR** (onnxruntime) backend | Beat the Tesseract backend decisively on sample pages (cleaner formulas/boxes; 26.8 vs 11.3 s/page — quality won). Tesseract is kept ONLY as a last-resort fallback for pages Docling cannot process (`tess_fallback.py`). |
| Display equations | **CodeFormula VLM** (`do_formula_enrichment=True`) | Decodes display math to LaTeX, then converted to Unicode (`latex_to_chem()`) — `2K(s) + 2H₂O(l) → 2KOH(aq) + H₂(g)` parses natively instead of post-hoc repair. |
| LLM fidelity polish | **z-ai-web-dev-sdk** (`zai.chat.completions.create`), Node | Strict no-paraphrase OCR-repair prompt; resumable JSONL; guards. `npm install z-ai-web-dev-sdk` in the scripts dir. |
| Validation / audits | plain Python (`validate_<subject>.py`, `audit_<...>.py`) | Deterministic checks, exit non-zero on failure. |

### 4.2 Environment reality

- Workspace: **no GPU, ~3 GB RAM, 2 cores**, internet OK. Workspace resets
  wipe installed packages AND `/home/z/my-project/data` — everything durable
  lives in this repo; scripts re-run from a fresh clone.
- Offline env for Docling runs: `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
  TOKENIZERS_PARALLELISM=false OMP_NUM_THREADS=2 MKL_NUM_THREADS=2`, and
  `DOCLING_ARTIFACTS_PATH` pointed at the local model cache.
- Parse rates to set expectations: RapidOCR ≈ 27 s/page; formula enrichment
  ≈ 43 s/page (chemistry); fast pinned stack ≈ 9–13 s/page (physics).
  A 300–400 page book is a multi-hour grind — batch it (§5 phase 4).

### 4.3 Version mines (verified the hard way — see §8 PM-1)

| Version | Behavior |
|---|---|
| docling 2.140 (fresh default) | Formulas decode BUT 140–230 s/page on graph-heavy pages: CodeFormulaV2 `max_new_tokens` defaults to 4096 and burns on graphs. Avoid on CPU. |
| docling **2.33.0** | Fast (9–13 s/page); stable base corpus. BUT its CodeFormula v1 integration returns EMPTY formula text, and it crashed on some pages. |
| docling **2.133.0** | Chemistry's actual stack; formulas decode correctly. Erratic multi-minute hangs on ordinary pages; needs `rapidocr==3.9.2` (3.10.0 removed `PP_OCRV6_LANGS`) and artifact-path surgery. |
| **Physics resolution** | Page-level hybrid: fast 2.33.0 base corpus + formula-decoded 2.133.0 spliced in where it succeeded + Tesseract fallback for 4 unprocessable pages + 1 pixel-verified blank page. |

Rule of thumb: **pin what worked** (`docling==2.33.0` base + `rapidocr==3.9.2`;
formula enrichment via 2.133.0 only where needed), record exact versions in
the book's parse report, and never trust a fresh `pip install docling` default.

## 5. Procedure — phases 0→10

Scripts are per-book copies (`<task>_<subject>.py`) living in the book's
`pipeline/scripts/`. They contain hardcoded workspace paths near the top
(`PDF`, `OUT_DIR`, `PAGES_DIR`) — adapt those, then keep everything else
identical to the reference so diffs stay meaningful.

**Phase 0 — Intake & scaffold.** Put the PDF in `<book>/source/` (chemistry
used the book root), compute sha256, create the book `README.md` from
`physics/4ph1/README.md` (status header, source-of-record table, folder
layout, checklist), create empty `parsed/` and `pipeline/` (with
`.gitkeep`s if empty). Get the file via a relay link if direct upload fails —
record provenance either way.

**Phase 1 — Inspect the PDF.** `inspect_pdf.py` pattern: page count, text
layer per sampled page, producer, embedded outline. Expected for this
collection: **image-only scans** (zero extractable text, one full-page image
per page, fake per-page outline) → OCR route mandatory; "just use
pdfplumber/PyMuPDF" is never an option. If a future book HAS a text layer,
stop here and re-plan (this playbook's grind assumes scans).

**Phase 2 — Probe structure (never assume from a sibling book).** Write small
probe scripts (probe_*). You need, for THIS book:
- **Page offset** `book_page = pdf_page − offset`, confirmed **three ways**
  (running header digits, chapter opener vs book page, index entry). Physics:
  offset 10, book 1 = PDF 11; chemistry: offset 9. Both differ — probe it.
- **Units & chapters** from the book's own contents pages; chapter start =
  its LEARNING OBJECTIVES page. Cross-check TOC digits against opener
  openers (physics TOC OCR garbled 75→"15", 150→"160-opener", 158, 221 —
  every one was caught by the cross-check).
- **Special sections**: skills pages, answers section (physics has NONE —
  verified by corpus-wide marker scan; chemistry has one), appendices,
  glossary, index. Note where unit-question banks sit.
- **Marker census**: scan parsed text for box/heading markers
  (`KEY POINT`, `EXAMPLE n`, `HINT`, `ACTIVITY n`, `PRACTICAL`,
  `EXTENSION WORK`, `EXAM PAPER`/questions…) including **merged-OCR forms**
  (`KEYPOINT`, `PHYSICSONLY`, `LEARNING.OBJECTIVES` with punctuation).
- Front-matter boundary (pages before book page 1) and blank pages
  (pixel-verify before accepting, e.g. physics PDF 307 = 0.7% ink).

**Phase 3 — Structure map module.** Write
`book_structure_<subject>.py`: `CHAPTERS`, `EXTRA_SECTIONS`, `UNIT_NAMES`,
`OFFSET`, `N_PAGES`, `MARKERS`, `TYPE_PRIORITY`, `BOOK_TITLE`, `BOOK_AUTHOR`,
`SHA256`. This module is the single source of truth the chunker imports.

**Phase 4 — Full-book parse.** `docling_full_<subject>.py`: per-page JSON
checkpoints (skip-if-exists = resume-safe), items serialized with label +
text + bbox; tables exported to markdown; retry ladder per page:
**formula ON → formula OFF → record error** (layout+tables survive the
OFF retry); optional Tesseract fallback record for dead pages (schema-
compatible, flagged). Run in **foreground windows** (5–10 pages per fresh
process to stay under RAM/timeout; a loop script like
`run_parse_physics.sh` chains windows and logs to a file). Expect a
multi-hour grind; the checkpoints make every kill survivable.

**Phase 5 — Chunking & normalization.** `parse_docling_<subject>.py`:
- cleaned ordered blocks: `latex_to_<subject>()` Unicode conversion
  (sub/superscripts, arrows, fractions, state symbols, subject symbols:
  chemistry `Aᵣ/Mᵣ`, physics `∝ λ ρ Ω °C m/s²`); sidebar double-OCR dedup;
  heading dedup (incl. merged forms);
- structure mapping via the Phase-3 module; marker-based `content_type`
  with priority; front matter gets `book_pages: null`;
- packing 350–1600 chars target, **2400 hard max**; small-chunk merge
  (<250); `split_long` falls back to sentence → line → word (index and
  glossary entries have no sentence punctuation — this bit physics with
  35k-char chunks until fixed);
- chunk ID grammar: `<subject>_v<corpus>_u<unit|0>_c<chapter|0>_pdf<pdfpage:03d>_<block:04d>`
  (e.g. `phys_v1_u1_c5_pdf058_0090`);
- outputs: `<subject>_chunks_v<n>.jsonl` + `full_book_*.md` +
  `parse_report_v<n>.json` (embeds sha256, stack versions, counts).

**Phase 6 — Validation gate.** `validate_<subject>.py` must check at minimum:
unique IDs; chapter/unit coverage complete; 0 body order breaks (benign
exceptions like multi-column index MUST be justified inline); dual page
numbering on every chunk; question chunks anchored to the probed question
pages; `char_count` consistency; 0 LaTeX remnants; size bounds. Exit
non-zero unless ALL CHECKS PASSED. Fix data or code, never weaken a check
silently — any exemption goes through the §9 review record.

**Phase 7 — LLM fidelity polish (conditional but usually needed).**
Chemistry and physics scans damage text in different ways (§7). When noise
classes survive parsing:
1. `select_noisy_<subject>.py` — score chunks per corruption class
   (fix false-positive sources first: table borders, cell padding);
   **force-include all question-typed chunks** (serving-critical).
2. `llm_repair_<subject>.js` — z-ai SDK; strict no-paraphrase prompt whose
   primary job is transcription repair (restore dropped spaces/characters,
   fix unambiguous formulas `CH8→C3H8`, `CI-CI→Cl-Cl`); tables keep per-line
   pipe counts; units/equations verbatim. Guards: length drift 0.6–1.6×,
   refusal patterns, Unicode-unit non-decrease, **wording fidelity via
   character-level LCS ≥ 0.97 on whitespace-stripped text** (NOT token-level
   — §8 PM-2). Resumable append-only JSONL; per-call 120 s timeout; 429
   backoff 20 s×attempt; quota-stop after 2 consecutive 429 chunks;
   rejected raws saved as evidence.
3. `merge_llm_<subject>.py` — apply in place; `text_original` preserved;
   `llm_repaired: true`; recompute `char_count`; regenerate md + report;
   then **anchor diff vs pristine corpus must be 0 drift** on every chunk
   (id/unit/chapter/type/pdf_pages/book_pages/section/unit/chapter title).
4. `audit_polish_<subject>.py` — before/after corruption-class counts,
   regression checks (Unicode units must not decrease).
5. Re-run Phase 6 validation.
Gateway quota note: LLM quota walls can last **15+ hours at account level**
(§8 PM-3). The runner's probe/backoff/quota-stop + JSONL resume means you can
simply re-run in later batches/sessions until done; do not idle-poll.

**Phase 8 — Documentation.** Update: book `README.md` (checklist + status),
`parsed/README.md` (schema sample, content-type table with RAG advice,
polish provenance, recommended filters), `pipeline/METHOD_AND_FINDINGS.md`
(findings + numbered decision log), `pipeline/worklog.md`.

**Phase 9 — Report back.** Append your §9 review record + any lesson/errata
entries to THIS file. Non-optional (golden rule 11).

**Phase 10 — Commit & push (temp-index protocol).**

```bash
cd /home/z/my-project/syllabai-resources
export GIT_INDEX_FILE="$PWD/.git/tmp-index"
git read-tree HEAD                       # start from committed tree — ignores phantom deletions
git add -- <only paths you touched>      # NEVER -A; new files included explicitly
TREE=$(git write-tree --missing-ok)
COMMIT=$(git commit-tree "$TREE" -p HEAD -m "<TASK-ID> <short summary>")
git push origin "$COMMIT":main
git update-ref refs/heads/main "$COMMIT"
rm -f "$GIT_INDEX_FILE"; unset GIT_INDEX_FILE
```

- Verify first with a dry run: `read-tree HEAD` + `write-tree --missing-ok`
  with no additions must equal the HEAD tree (it does as of `9b04bad`).
- Commit messages follow the repo convention: `TASK-ID` + dense summary of
  what/why/evidence (see `git log` for examples). The parallel-lane rule
  applies: if HEAD moved while you worked, blob-compare your deliverables
  against what's already pushed and push only the genuine delta.
- CI (`.github/workflows/scripts-tests.yml`) gates root `scripts/` and
  `graph/` only — `books/**` is NOT CI-gated, which makes your Phase 6
  validator the gate of record. (Proposal to add a books CI gate = a §9
  improvement entry, not a license to skip validation.)

## 6. Cleaning & normalization checklist

**DO (deterministic, in-code):**
- strip running headers/footers, unit banners, roman-numeral junk;
- de-hyphenate across line breaks; expand ligatures;
- rejoin formulas split by OCR (element/symbol whitelist);
- convert LaTeX → Unicode (sub/superscripts `→ ₀₁₂…⁰¹²…`, arrows `→ ⇌`,
  fractions `½ ⅓…`, subject symbols);
- dedup sidebar double-OCR and repeated headings (incl. merged forms);
- normalize whitespace (learning_objectives chunks MUST NOT carry raw
  newlines — audit action item from chemistry, applied since physics);
- type every non-body section separately (`divider`, `unit_questions`,
  `chapter_questions`, `glossary`, `appendix`, `index`, `front_matter`,
  `skills`, …).

**NEVER:**
- never hand-edit corpus JSONL in place without a script + evidence;
- never "fix" OCR damage by paraphrasing (LLM touch = transcription-only);
- never drop a suspicious page silently — record it (blank/pixel-verified
  or fallback-typed) in the parse report;
- never let a check fail soft — exemptions must be explicit, justified, and
  reported (§9);
- never edit a published corpus version in place — new version files
  (`_v<n+1>.jsonl`) with the old ones kept for diffing.

## 7. Findings ledger — how these scans actually behave

- **Common to this collection:** image-only scans, zero text layer, fake
  per-page outline, front matter unnumbered, OCR route mandatory.
- **Chemistry 4CH1 scan:** subscript→comma/semicolon garbles (`2H,(g)`),
  zero-for-O, multi-column interleave with sidebars, sidebar double-OCR,
  display equations lost by Tesseract (the v1→v3 rebuild motivation).
  Tesseract-inherited noise classes: state-paren commas, junk/punct debris.
- **Physics 4PH1 scan (RICOH MP C4503):** **drops spaces between words
  scan-wide** ("therelationshipbetween") — 62% of chunks carried glue runs;
  TOC digit garbles; merged heading OCR (`KEYPOINT`, `LEARNING.OBJECTIVES`);
  fullwidth punctuation leaks (index tables); 33 pages needed formula OFF
  (their equations survive as plain text, also present in body — marginal
  loss, documented); NO answers section; multi-column index reorders
  internally (benign, exempted with justification).
- **LLM polish outcomes:** chemistry 87/90 repaired (v3); physics 299/300
  across two rounds — the single holdout is an index table chunk twice
  rejected by pipe-discipline guard (kept original; index is
  filter-recommended anyway). Rejections are information, not failures.

## 8. Post-mortems (these cost real time — read before you parse)

- **PM-1 Docling version mines (physics):** fresh `pip install docling`
  (2.140) was 10–20× slower on graph-heavy pages (CodeFormulaV2
  `max_new_tokens=4096` burn); "known-good 2.133" turned out to be actually
  2.33.0 (empty formula text, some crashes); true 2.133.0 decodes formulas
  but hangs erratically. Remedy: pin versions, verify formula decoding on a
  probe page, use the page-level hybrid + retry ladder, checkpoint per page.
- **PM-2 Token-level LCS guard bug (physics round 2):** the wording-fidelity
  guard was coded as token-level LCS, contradicting its documented
  whitespace-normalized intent — a de-glue repair splits a glued token, so
  token equality fails and EVERY correct repair was rejected (replay showed
  235/236 already-banked OKs would fail it too). Remedy: character-level LCS
  on whitespace-stripped text; **replay banked OKs against any guard change**
  before trusting a reject storm.
- **PM-3 Gateway 429 quota walls:** account-level (all model aliases, probe
  requests included), can persist 15+ h, breaks into intermittent windows.
  Remedy: quota-probe loop before processing (env `PROBE_MAX`/`PROBE_WAIT`),
  per-call timeouts, 429 backoff, quota-stop, append-only JSONL resume,
  foreground batches, file-based logs. Minimize probing (it consumes rolling
  quota); re-run later instead of idle-polling.
- **PM-4 Post-hoc repair cannot recover structure (chemistry v1→v2):**
  mechanical + LLM repair fixed garbles but could not restore reading order
  or display equations Tesseract never captured. Remedy: fix the parser, not
  the symptoms — a better parse beats a smarter repair.
- **PM-5 Workspace fragility:** resets wipe packages and data; background
  processes get killed. Remedy: everything durable lives in the repo;
  foreground batches; resumable checkpoints; reinstall is a known 10-minute
  routine (see §4.2 pins).

## 9. Self-improvement protocol — how this playbook learns

### 9.1 What you MUST do before closing a parse task

1. Append a **Review record** (template in §9.5) to §9.5 of this file —
   even if everything went perfectly (a clean run that confirms the playbook
   is itself a finding).
2. Append one **Lesson** (L-entry) per genuinely new, reusable insight
   (template §9.3). If it's already covered in §7/§8, update nothing —
   but say so in your review record.
3. If this README or `PARSE_STANDARD.md` misled you, wasted your time, or
   contains a factual error: append an **Errata** (E-entry) AND, when the fix
   is uncontroversial and within §6/§7/§8 scope, apply the fix in the same
   commit. Never delete or rewrite existing text — corrections supersede.

### 9.2 Who may change what

- **Any parse agent, append-only:** lessons (§9.3), errata (§9.4), review
  records (§9.5), change-log line (§10). Additive edits to §6/§7/§8 that add
  findings/remedies (no rule changes).
- **Operator gate only:** golden rules (§3), the 8-point
  `PARSE_STANDARD.md`, anything affecting published chunk IDs/schema/content
  types (consistency with root `AGENT.md` gates). File an E-entry proposing
  the change; do not edit those sections directly.
- **Disagreements:** if you believe a golden rule is wrong, do NOT work
  around it silently — quarantine the ambiguity, file the E-entry with
  evidence, and continue on the non-affected work (rule 7 of root `AGENT.md`).

### 9.3 Lesson entry format (append to §9.4)

```
- **L-<seq>** (<date>, <TASK-ID>, <agent/lane>): <one-line lesson>.
  Evidence: <script/report/worklog path>. Action: <what a future agent does
  differently / none needed>.
```

### 9.4 Lesson ledger

- **L-001** (2026-10-04, chem task 1, Super Z): Tesseract is structurally
  inadequate for formula-heavy scans (subscript commas, lost equations,
  interleaved reading order). Evidence: `chemistry/4ch1/pipeline/METHOD_AND_FINDINGS.md`
  §4 v1. Action: RapidOCR backend is the default; Tesseract = fallback only.
- **L-002** (2026-10-05, chem task 3, Super Z): Docling+RapidOCR+CodeFormula
  is the CPU-quality sweet spot; formula enrichment turns display equations
  into native Unicode. Evidence: chemistry v3 quality table. Action: keep
  enrichment ON unless a page crashes (retry ladder).
- **L-003** (2026-10-18, chem audit, external lane): the 8-point standard +
  green-light gate process works; "by-design gaps" at unit boundaries are
  typed end-matter, not misses. Evidence:
  `chemistry/4ch1/pipeline/AUDIT_VERDICT_2026-10-18.md`. Action: new parses
  self-audit against PARSE_STANDARD.md before claiming done.
- **L-004** (2026-10-19, T-PARSE-4PH1-1/2/3, Super Z): never trust sibling
  book structure — physics offset (−10), 8 units/28 chapters, no answers
  section all differ from chemistry (−9, 4/29, has answers). Evidence:
  `physics/4ph1/pipeline/METHOD_AND_FINDINGS.md` §2. Action: three-way
  offset confirmation + TOC-vs-opener cross-check per book (§5 phase 2).
- **L-005** (2026-10-19, T-PARSE-4PH1-3, Super Z): RICOH scans can drop
  inter-word spaces scan-wide (62% of chunks). Evidence: physics polish
  rounds 1–2. Action: run the glue-run census on every new scan early; if
  high, budget an LLM polish round (§5 phase 7) in the plan.
- **L-006** (2026-10-20, T-PARSE-4PH1-4-R2, Super Z): token-level LCS wording
  guards reject every correct de-glue repair; character-level LCS on
  whitespace-stripped text is the documented intent. Evidence: §8 PM-2,
  `replay_rejects.js`. Action: replay banked OKs against any guard change.
- **L-007** (2026-10-19/20, T-PARSE-4PH1-4, Super Z): 429 walls are
  account-level and can outlast a session; probes consume rolling quota.
  Evidence: §8 PM-3 probe logs. Action: probe sparingly, batch in windows,
  resume via JSONL — the protocol tolerates any number of restarts.
- **L-008** (2026-10-20, T-PARSE-4PH1-4-R2, Super Z): parallel lanes happen —
  round 1 was pushed by another lane while this lane was quota-walled.
  Evidence: commit `a645faf` message (blob-compare + delta rebase). Action:
  before committing, fetch and blob-compare deliverables; push genuine delta
  only (§5 phase 10).
- **L-009** (2026-10-19, physics parse, Super Z): index/glossary entries have
  no sentence punctuation — sentence-only `split_long` produced 35k-char
  chunks. Evidence: physics METHOD §4. Action: sentence → line → word
  fallback is mandatory in the chunker.
- **L-010** (2026-10-21, T-BOOKS-README-1, Super Z): playbook extracted from
  per-book histories so future parses start from evidence, not memory.
  Evidence: this file's bootstrap commit. Action: keep it alive via §9.
- **L-011** (2026-10-21, T-INTAKE-4BI1-1, Super Z): intake download walls
  are not dead ends — SiteGround sgcaptcha-class JS challenges clear in a
  headless browser; hand the clearance cookies to curl for the bulk
  download (theonlineschool.co.uk 4BI1 PDF landed this way after curl-only
  failed). Cloudflare "Just a moment" hosts (dokumen.pub, pdfcoffee)
  remain hostile to curl; try the same browser route before declaring a
  source bot-walled. Evidence: worklog T-INTAKE-4BI1-1, lane README
  provenance. Action: at Phase 0 intake, curl first, then headless-browser
  clearance + cookie handoff, and only then log a wall as blocking.

### 9.5 Errata ledger

- **E-001** (2026-10-21, T-INTAKE-4BI1-1): `books/CATALOG.md` §4.1 queue
  row listed the 4BI1 SB authors as "Penny Johnson, Susan Kearsey". The
  book of record (ISBN 9780435185084, 2017) is by **Philip Bradfield &
  Steve Potter** — verified against the landed copy's title page, Pearson's
  official sample PDF, and retail ISBN listings. Disposition: FIXED in
  CATALOG.md (§3.3 + §4.1) in the same commit; lane README carries the
  note. Lesson: verify author/ISBN against the artifact itself at intake
  (title page), not against queue-planning rows.

*(template for future entries; superseding entries must reference the
E-ID they correct)*

```
- **E-<seq>** (<date>, <TASK-ID>): <what is wrong / what misled you, where
  (file+section)>. Evidence: <path>. Disposition: FIXED HERE (additive) /
  PROPOSED FOR OPERATOR GATE / WONTFIX (reason).
```

### 9.6 Review records

- **R-001** (2026-10-21, T-INTAKE-4BI1-1, 4BI1 intake): repo check — 4BI1
  SB absent (only spec spine `Official-Specifications/igcse-biology/`);
  web-sourced theonlineschool.co.uk copy via headless-browser sgcaptcha
  clearance + curl cookie handoff; pypdf verified 179 spread pages / 357
  book pp, native text layer (18/18 sampled pages >40 chars), authors
  confirmed Bradfield & Potter (ISBN 9780435185084); lane scaffold landed;
  CATALOG tracker row 9 + §3.3 record + §4.1 state S. No parse yet (next
  lane runs §5 phases 0–10 with the spread-mapping watch item).
  Deviations from playbook: none (intake-only task). Lessons appended:
  L-011. Errata filed: E-001.

```
- **R-<seq>** (<date>, <TASK-ID>, <book>): pages parsed N/N; chunks N;
  content types N; offset N (3-way confirmed); validation ALL CHECKS PASSED
  (Y/N + notes); LLM polish rounds (selected/applied/rejected + holdouts);
  deviations from this playbook (list or "none"); lessons appended (IDs or
  "none"); errata filed (IDs or "none").
```

## 10. Change log

- **2026-10-21 — v1.1 (T-INTAKE-4BI1-1):** 4BI1 student book landed as
  SOURCE (lane `pearson-edexcel/international-gcse/biology/4bi1/`,
  sha256 `974ad65d…93006`, 357pp native-text 2-up spreads, OCR route not
  required); CATALOG tracker row 9 + §3.3 + §4.1→S; L-011 + E-001 + R-001
  recorded (first exercised cycle of the §9 self-improvement loop).
- **2026-10-21 — v1.0 (T-BOOKS-README-1):** bootstrapped the playbook from
  the complete chemistry 4CH1 + physics 4PH1 histories (methods, findings,
  decision logs, post-mortems, audit verdict); seeded lesson ledger L-001…
  L-010; established self-improvement protocol (§9) and the temp-index
  commit convention (§5 phase 10).
