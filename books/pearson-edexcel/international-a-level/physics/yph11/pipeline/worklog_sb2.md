# YPH11 SB2 delta lane — worklog (T-PARSE-YPH11-1, 2026-10-22, second session)

Operator directive "Retry YPH11 polish" (same task ID as the SB1 lane;
L-008 parallel-lane protocol — origin had moved: SB1 was pushed by the first
session + 4BI1 polish completed by a third; this session delivers the SB2
delta on top, blob-compared before push).

- State check: no SB2 parse artifacts anywhere; lane sources materialized
  from git (SB1 sha256 aa1aed60…15d0 verified vs lane README).
- Environment restore (PM-5, mirrors SB1 lane's L-018): CPU-only torch
  2.14.1 + torchvision 0.29.1+cpu realign, transformers pinned 4.51.3
  (4.57 removed RTDetrImageProcessor), docling 2.33.0 + rapidocr-onnxruntime;
  z-ai SDK reinstalled; model caches re-downloaded.
- Phase 1: SB1 225pp image-only verified → OCR route.
- Phase 2 (SB1): TOC decode (PDF 4); offset hypothesis pdf−11.
- Phase 4 (SB1 grind): 225/225 pages, 0 errors, 76 formula-OFF retries;
  11 s/page body, 60–325 s on dense index pages.
- Phase 2 (SB1): census — 11 EXAM PRACTICE pairs / THINKING BIGGER pairs,
  offset confirmed 3 ways (header digits 60→49, 120→109, 200→189).
- Phase 3-6 (SB1): structure module + chunker (7 additive IAL types);
  validator ALL CHECKS PASSED (875 chunks).
- SB2 SOURCE INTEGRITY FIX: intake archive copy TRUNCATED (225pp vs its own
  TOC promising index at book 224) → original re-sourced via documented
  taleem360 Googlebot-UA route, byte-verified vs original-of-record
  (28eabe40…8f, 237pp) → fresh 145dpi derivative (f8f3fc62…ce82d,
  48,278,974 B; -dPassThroughJPEGImages=false required — L-022), OCR parity
  1.0000; lane source replaced in the delta commit (E-004).
- Phase 2-6 (SB2): 237/237 pages OCR'd; structure probed independently
  (offset −10, no printed page 1, 7 topics / 13 chapters, 13 EXAM PRACTICE
  pairs); chunker + validator ALL CHECKS PASSED (826 chunks); corpus rebuilt
  under the SB1 lane's published two-book ID law (yph2_v1_) after the L-008
  discovery; pristine snapshot staged.
- Phase 7: glue census 90%; 794/826 selected (67 questions forced); runner
  staged; 429 wall (since 2026-10-20) blocked all calls — 0/794, resumable.
- Phase 8-9: additive lane docs (this file set), playbook ledgers renumbered
  to L-021/L-022 + E-004 + R-005 (SB1 lane took L-018…L-020 + E-003 + R-004),
  CATALOG row 3 / §3.4 / §4.2 / change log.
- Phase 10: temp-index delta commit on fresh origin/main.

## Phase 7 completion (2026-10-30, sessions of 10-25 → 10-30)

- Five quota openings of the account-level 429 wall banked the full
  selection, PM-3 probe/resume throughout, crash-safe JSONL append per
  chunk: 2026-10-25 22:17–22:52Z +94 · 2026-10-26 evening +261 · 2026-10-27
  evening +254 · two sealed probe-only cycles +0 · 2026-10-30 07:45–08:50Z
  +185 (last window finished the final 19, `remaining todo: 0`).
- Final: **794/794 terminal = 774 applied (all with text changes) + 20
  guard-rejected** (original text preserved; same guard class as SB1 —
  LCS ≥ 0.97 whitespace-stripped, length 0.6–1.7×, Unicode-unit
  non-decrease, pipe discipline, line-strict retry).
- Merge (`merge_llm_ial_physics_sb2.py`): anchor diff vs pristine **0
  drift**; char_count recomputed; `full_book_sb2_docling.md` +
  `parse_report_sb2_v1.json` regenerated.
- Audit (`audit_polish_ial_physics_sb2.py`): on repaired chunks space-run
  4610→15, camel-glue 450→13, caps-glue 326→94, 0 Unicode-unit regressions.
  The 7 chunks retaining 18+-char lowercase runs verified against
  `text_original`: all carry the runs verbatim in the OCR source (URLs,
  acknowledgements, one unrecoverably mangled Latin-quote passage) — 0 true
  regressions.
- Validator (`validate_ial_physics_sb2.py`): **ALL CHECKS PASSED** (826
  chunks, 13/13 chapters, 7/7 units, 26/26 question pages, 0 order breaks).
- Chain scripts of record replaced: the 2026-10-25 commit had shipped the
  pre-fix phantom-path versions (`download/rag_ial_physics/` +
  `data/ial_physics/` paths; MD_OUT pointing at the 4PH1 lane's
  `full_book_docling.md` — clobber hazard) and omitted the wrapper entirely
  (`books/README.md` E-006); this commit lands the tested flat-path scripts
  that produced the R1 merge.
- Phase 10: delta commit on fresh origin/main (L-008 protocol — workspace
  reset had corrupted the stale local checkout; hard-reset to 8dd16e99,
  clean tree verified, CATALOG rebased on upstream row state).
