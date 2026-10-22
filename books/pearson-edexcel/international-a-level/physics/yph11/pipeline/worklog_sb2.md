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
