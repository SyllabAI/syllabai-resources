# books/cambridge-international/ial/chemistry/9701 — parsed

## Corpus

- `cie_a_level_chemistry_9701_chunks_v1.jsonl` — **1083 chunks** (`c9701_v1_u0_c{n}_pdf{p}_{i}`),
  13-key grammar (same schema as 4BI1/YPH11 v1), 10 content types
  (body 668, chapter_questions 86, reflection 70, before_you_start 64,
  worked_example 58, self_evaluation 38, summary 35, learning_objectives 36,
  activity 27, science_in_context 1).
- `cie_a_level_chemistry_9701_chunks_v1.pristine` — byte-identical snapshot
  (merge-diff + anchor law reference).
- `full_book_textlayer.md` — rendered book (1.43 MB).
- `parse_report_v1.json` — provenance, decisions D-1…D-6, census.

## Book facts

- Cambridge International AS & A Level Chemistry Coursebook **3rd edition**,
  Lawrie Ryan & Roger Norris (CIE 9701, exams from 2022).
- Source: **regenerated/accessibility re-layout** (DejaVu/STIX, single column,
  9.2pt body, 889 pdf pages). NOT a print replica.
- **No printed page numbers anywhere** → chunks carry `pdf_pages` only,
  `book_pages: null` (parse_report D-1). Validator asserts range coherence
  against the 35-range chapter map instead of a page-offset law.
- Structure: 30 chapters (openers = LEARNING INTENTIONS pages, pdf 15…843) +
  P1 Practical skills 1 (pdf 522–536, sits between ch18 and ch19) + P2
  Practical skills 2 (pdf 870–882) + Appendices (883–887) + Acknowledgements
  (888–889). Chapter end anatomy: SUMMARY → EXAM-STYLE QUESTIONS →
  SELF-EVALUATION.
- Disclosed intake defect handled: WeChat ad watermark on pdf 31 + 66 —
  stripped at line level; validator gates zero CJK / CLASS0608.

## Quality notes

- **Text-layer lane, no OCR.** Native extraction with span-pool assembly:
  sub/superscripts rebuilt from span geometry into Unicode — 553/1083 chunks
  carry Unicode subscripts, ~500 superscripts (`H₂O`, `mol⁻¹`, `Ni²⁺`,
  stacked isotopes `⁵²₂₄Cr²⁺` in correct nucleon/proton order).
- 22 residual <80-char fragments (2%) — header slivers (`WORKED EXAMPLE 18 …`)
  and paragraph tails; candidates for the LLM polish merge pass.
- Margin features (Study tip / Link / Extension) are **not present as text**
  in this render (D-2) — not a parser miss.

## LLM fidelity polish (NOT STARTED — quota-walled period)

Census pending (text-layer source, expected light selection vs OCR lanes).
Protocol identical to the 4PH1/4BI1/YPH11 lanes:

```bash
cd pipeline/scripts && python3 select_noisy_9701.py       # -> data/llm_repair_ids_9701.json
node llm_repair_9701.js                                    # resumable JSONL
python3 merge_llm_9701.py && python3 audit_polish_9701.py && python3 validate_9701.py
```

Guards (fleet-standard): length drift 0.6–1.7×, refusals, Unicode
sub/superscript non-decrease, per-line pipe counts on tables, wording fidelity
via whitespace-stripped char-LCS ≥ 0.97. Pristine snapshot is the anchor
diff target (expected 0 drift on id/unit/chapter/type/pdf_pages/section).
