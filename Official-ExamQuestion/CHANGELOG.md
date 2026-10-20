# CHANGELOG — official_examq_extract.py (ADR-037 converter)

Semantics: outputs embed `generator: official_examq_extract.py v<version>`, so any
topic.json traces to exactly this behaviour. Every version bump must follow the
AGENTS.md improvement loop: ledger entry (F#) + canary + full-corpus re-run.

## 0.3 — 2026-10 · full-corpus batch wave (16/16 series of 4CH1/1C)

New findings fixed (LEDGER.md F11–F14):
- F11: MS continuation-row indent tolerance `{0,10}` → `{0,20}` (2023-06 G5 76% → 100%).
- F12: MCQ positive-statement keying — '<L> is (the) correct answer' is authoritative;
  note filter extended to 2021+ phrasing 'is not the correct answer'.
- F13: manifest schema-v2 tolerance — 2026-06 gap-fill manifests omit
  `series.printed`/`series.source`; G0 annotates instead of crashing.
- F14: elimination keying for rebuttal-style MS ('A is incorrect…' for every wrong
  option, '<L> (answer)' cells, glued 'B4' cells) — key the sole un-rebutted option
  only when corroborated by exactly one answer row.
- Question-count registry extended to all 16 series (9..12 verified against footers
  summing to 110; 2026-06 genuinely prints 9 questions).

Result: 14/16 series all-gates PASS · 169 questions · 930 parts · 1754/1760 marks ·
all MCQs keyed everywhere except the two honest 2020-01 refusals · negative controls
3/3 everywhere · independent-parse cross-diff 161/161 marks agree (2024-06, 2025-06,
2026-06 vs repo parsed/ layer).

## 0.2 — 2026-10 · multi-series generalization wave (6 series)

Findings F1–F10 (LEDGER.md): QSTART indent tolerance, image-only page census with
defect attribution + G1 REVIEW path, footer-gap census, per-series question-count
registry, MS note-phrasing unification, ambiguity-guard answer keying (2020-01 Q7a),
bare-letter MS rows, phrase-level DO-NOT-WRITE handling, damaged-region start
classification, glued marks-digit stripping.
Result: pipeline proven to generalize beyond the baseline; 2019-06 archive damage
honestly attributed; 2024-06 cross-diff 55/55 marks vs repo parsed layer.

## 0.1 — 2026-10 · prototype (2020-11 baseline)

Converter + gates G0–G6 + negative controls N1–N3; verbatim 5-gram gate; positional
MS linkage; MCQ keying from MS answer text; page-anchored asset stubs; spec seeds
validated against the SME spec-point resolution registry.
Result: 10 questions, 64 parts, 110/110 marks, G0–G6 PASS, 6/6 MCQ keyed, NC 3/3.
