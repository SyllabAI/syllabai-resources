# Corpus Review — 2026-09-10

Review of the first upload batch to `syllabai-resources`, against the corpus
architecture defined in `syllabai/CONTENT_CORPUS_ARCHITECTURE.md` (CMC v1.0,
T-C05). Two urgent repairs were applied during this review (Section 2) — one
of them was time-critical and could not wait.

---

## 1. Inventory (as uploaded, commit `8b9b5c3 ADD`)

| Item | Role | State |
|---|---|---|
| `international-gcse-chemistry-2017-specification.pdf` (1.7 MB) | **A — Official specification (authoritative)** | Source PDF, Issue 3, 4CH1, first teaching 2017-09 |
| `international-gcse-chemistry-2017-specification-2026-09-10_12-18-50.md` (86 KB, 1159 lines) | A — OCR conversion of the above (ocr.z.ai) | Full document captured, incl. Appendices 1–8; 45 HTML tables |
| `Chemistry IGCSE Revision Notes/` (112 md + 244 images, 22 MB) | **D — SME revision notes (supplementary)** | Obsidian Web Clipper dump of Save My Exams 4CH1 notes, 4 sections × 35 subtopics |
| `edexcel-chemistry-igcse-book.pdf` (192 pp, 33.5 MB) | **B — Student Book** | 2-up landscape scan (2 book pages per PDF page) **with an OCR text layer** (moderate quality) |
| `edexcel-international-gcse-9-1-chemistry-student-book-pdf-free.pdf` (383 pp, 54.3 MB) | B — Student Book (same title) | 1-up portrait scan, **image-only, no text layer** — needs full OCR |

Not yet uploaded (per operator): past papers (Role C), SME topic questions /
exam questions (Role E), further processing of the Student Book.

## 2. Repairs applied during this review

### 2.1 TIME-CRITICAL — expired-link image rescue (spec markdown)

The ocr.z.ai output embedded 5 images on **signed UCloud URLs expiring
2026-09-17**. They were downloaded to `assets/` before expiry and the markdown
now references them locally (cover, qualification-structure diagram, two
Pearson marketing diagrams, back cover). The qualification-structure diagram
(1472×926) is the only content-bearing one. Script: `scripts/c05_recover_spec_images.py`.

> Any future ocr.z.ai conversion must be checked for the same expiry issue —
> grep for `Expires=` and localize images the same day.

### 2.2 `{pageTitle}` clipper bug repair (SME notes)

Every note referenced images as `%7BpageTitle%7D/<file>` (a Web Clipper
template variable that was never substituted), while all 244 images were
dumped into one literal `{pageTitle}/` folder at the corpus root. All 245
image references were broken. Fixed by `scripts/c05_repair_clipper_refs.py`
(idempotent — **re-run it after every new clip batch**):

- `{pageTitle}/` → `assets/` (flat, corpus-root level)
- all refs rewritten to correct relative paths (`../../assets/…`)
- 3 percent-encoded filenames on disk decoded (`%E2%80%93` → `–`)
- 1 ref rescued by extension fallback (`.webp` → `.png`)
- 3 genuinely-missing images marked with CMC `<!-- figure-missing: … -->`
  markers (see Section 4)

Result: **244/247 refs resolve**; 3 missing flagged. No prose, tables, or
whitespace semantics were changed (verified by diff audit).

### 2.3 Additive front matter on the specification markdown

CMC v1.0 front matter was prepended (source_type, board, code, issue, ocr
tool/date, `status: raw_ocr`). Nothing else in the file was altered.

## 3. Quality assessment

### 3.1 Specification OCR — structure EXCELLENT, notation DEGRADED

**What survived (the important part):**
- All 4 content sections with complete spec-point tables: §1 Principles
  (1.1–1.60C), §2 Inorganic (2.1–2.5xC), §3 Physical (3.1–3.22C), §4 Organic
  (4.1–4.49C) — including the Issue-3 `C`-suffixed points and 12 `practical:`
  statements
- Appendix 5 command word taxonomy — complete, both tables (Add/Label …
  What/Why/Which). This is the canonical command-word list for the taxonomy
- Appendix 7 Periodic Table (as a large HTML table), Appendix 8 Glossary
- Sub-topic structure (a)–(i) with official wording

**Known damage (do NOT hand-fix now — the ingestion pipeline's lint + human
review own the corrections; hand-fixing risks provenance loss):**

| Damage class | Examples | Count |
|---|---|---|
| Lost subscripts (units, formulas) | `mol/dm3`, `24dm3and24000cm3`, `C60` | ~4 sites |
| Lost superscripts (ion charges) | `Ag+，Cu2+，Fe3+`, `CO32-`, `SO42-`, `NH4+`, `NO3-` | 1 spec point (1.38) but 12 ion formulas |
| CJK leak (OCR tool is a Chinese service) | `简单 distillation`, `Groups1，2，3和5，6，7`, `(8-10)和 strongly alkaline` | 3 content sites |
| Full-width punctuation | `，` ×16, `（）` ×6, `：` | ~23 sites |
| LaTeX fragments for math | `$ R_{f} $`, `$ A_{r} $`, `$\rightleftharpoons$`, `$^{2+}$` | ~15 sites |
| Lost spaces | `e.g.magnesium oxide`, `compounds(including`, `Groups1，2` | frequent |
| OCR artifact | `## ```markdown` + empty code block at line 42 | 1 |
| Raw HTML tables | 45 tables (fine for ingestion; not human-pretty) | 45 |

**Verdict:** the spec-point backbone (IDs, wording, ordering, C-points,
practicals, command words) — the part that must be authoritative — is intact.
The damage is exactly the chemistry-notation class the architecture predicted
(CMC §OCR-lint). Next step for this file: none by hand. It enters the pipeline
as `raw_ocr` and gets the 17-check lint + human review.

### 3.2 SME revision notes — clip quality GOOD

- YAML front matter on every note with the **canonical SME source URL** (112
  distinct) — this is the stable external ID and the mapping anchor
- Body: clean Markdown (headings, tables, bold) — no HTML
- Authorship metadata preserved in body (Written by / Reviewed by / Updated)
- Previous/Next navigation links preserved → SME's own topic ordering
- `Examiner Tips and Tricks` sections preserved
- 14 notes contain `Test yourself` links → 11 distinct SME topic-question
  pages (the Role E intake map)
- Notation: same subscript/superscript loss as the spec (`Na+`, `CO32-`,
  `CH4`) — same verdict: pipeline lint + review, not hand-fixing
- Boilerplate present in every note (Download PDF / Guided study / Was this
  helpful / avatars) — the ingest adapter must strip this before embedding;
  it is NOT content
- Sub-script damage concentrated in formula-heavy notes (ionic formulas,
  organic homologous series)

### 3.3 Student Book PDFs — process the 383-page one

Both files are the same Pearson Student Book (Jim Clark / Steve Owen /
Rachel Yu, 2017) in two scan variants. **Use the 383-page 1-up portrait file
for OCR**: per-page images map 1:1 to book pages, which the provenance model
(page-level citation) requires. The 192-page 2-up file has an existing OCR
text layer of moderate quality — useful only as a cross-check reference, not
as the conversion source (its page numbers are ambiguous: 1 PDF page = 2 book
pages, which poisons page-level provenance).

## 4. Genuinely missing images (3)

These failed to download during clipping and are marked
`<!-- figure-missing: … -->` in place. Re-clipping these three notes (or
saving the images manually) closes the gaps:

1. `Formula of ionic compounds` note — the copper(II) chloride swap-and-drop
   diagram (`~5RmSBVa_…`)
2. `Interpreting chromatograms` note — the R_f values identification image
   (empty `.jpeg` name)
3. `Fractional distillation` note — the main fractional-distillation diagram

## 5. Conventions for the remaining processing (from the Pre-Ingestion
Standard — the MUST list only)

1. **Localize ocr.z.ai images the same day** (URLs expire ~7 days) — grep for
   `Expires=`, save to `assets/`, rewrite refs. `scripts/` has the pattern.
2. **One document per conversion, front matter from day one** — even minimal:
   `source_type`, `source_file`, `ocr: {tool, date}`, `status: raw_ocr`.
   Copy the block from the spec md.
3. **Past papers: keep the QP/MS pair identity in the filename** —
   `4CH1_1C_que_20220103.md` + `4CH1_1C_ms_20220103.md` style, matching the
   canonical fixtures already in syllabai-core. Paper code, month, year in the
   name; details in front matter.
4. **Don't hand-fix OCR damage in content** — notation errors get fixed by the
   pipeline's structured lint + review flow, with provenance. Hand-fixing now
   creates silent untracked edits.
5. **Re-run `scripts/c05_repair_clipper_refs.py` after every new SME clip
   batch.**
6. **Keep this repo private** — publisher and SME material is copyrighted;
   ingestion is a fair-use-internal pipeline, not redistribution.

## 6. Structural gaps for the architecture (no action needed now)

- The SME corpus image layout (flat `assets/` at corpus root, refs two levels
  up) deviates from CMC's "assets next to the file" rule — accepted as the
  documented Role-D exception; the SME adapter resolves refs via the flat
  store.
- The 192-page book PDF is redundant once the 383-page one is converted;
  consider archiving it outside the working tree.
- SME notes cover sections 1–4 fully, but the spec also defines assessment
  practicals — no SME note set for Appendix 6 investigations; fine (spec is
  authoritative for practicals).
