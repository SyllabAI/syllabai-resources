# Validation Record — SME spec-point → 4CH1 code resolution

**Corpus:** `SME-ExamQuestion/` (Save My Exams exam questions, Edexcel IGCSE
Chemistry 4CH1, syllabus 2017)
**Run date:** 2026-09-17
**Pipeline:** `scripts/sme_spcpt_harvest.py` → `scripts/sme_spcpt_resolve.py`
→ `scripts/sme_spcpt_verify.py`
**Adjudications:** `scripts/sme_spcpt_adjudications.yaml`

## 1. Validation status vocabulary (important)

Master Spec §7 reserves `HUMAN_VALIDATED` for human review; AI output may only
emit `SUGGESTED`/`REVIEW_REQUIRED`. For this corpus the **operator explicitly
delegated validation authority to the AI** on 2026-09-17 (IM instruction,
verbatim):

> "let AI self-validate this time. I wont be manually approving"

Scope of the delegation: **the `spcpt_` → 4CH1 spec-code resolution only**.
Accordingly every record produced here is stamped:

- `validation: AI_VALIDATED (operator-delegated 2026-09-17)`
- `HUMAN_VALIDATED` is **never** emitted; records can later be upgraded to it
  if the operator (or a future reviewer) chooses to review, without re-running
  the pipeline.

The SME licensing basis for the underlying corpus is unchanged and documented
in `../LICENSE-DATA.md` (operator attestation, Amendment 2026-09-17).

## 2. How the resolution works (evidence chain)

1. **Harvest** — all 112 SME revision-note pages (the same pages the
   revision-notes corpus was built from) embed TipTap `specPoint` blocks
   containing `id` (e.g. `spcpt_J8pKKwSTHgfFw6tt`), `name`, and a
   `definition` that is SME's near-verbatim rendering of the official Edexcel
   statement wording. Output: `spec_point_index.json` (162 spec points;
   160/160 question-referenced ids covered, 2 index-only extras).
2. **Match** — each SME definition is scored against all 182 official
   wordings in `graph/specification_points.yaml` (token containment/F1 +
   sequence ratio; deterministic, no LLM in the loop) with a subsection boost
   from the slug-anchored note subsections.
3. **Cross-check** — the resolved code is checked against the containing
   notes' `spec_map` codes (the human-reviewed c10/c12 mapping): 161/162
   agree; the single disagreement was adjudicated (see §3).
4. **Apply** — `spec_point_codes` written onto every part of the 28
   `topic.json` files (ordered by the registry's global order).
5. **Verify** — independent gates (`scripts/sme_spcpt_verify.py`): registry
   membership of every emitted code; 0 parts with ids but without codes;
   resolution-table/index size equality; plus a seeded 5-part spot-check.

## 3. AI adjudications (edge cases)

All auto-resolutions were reviewed; the non-trivial cases are recorded with
rationale in `scripts/sme_spcpt_adjudications.yaml`. Summary:

| Case | Outcome |
|---|---|
| `spcpt_HRX72xfw5n8X3QYy` "Formation of Sulfur Dioxide" | Confirmed **4CH1-4.15** — SME definition is *verbatim* the official wording (sim 1.0); the containing notes' `spec_map` omits 4.15 (note-side gap, documented) |
| `spcpt_msKxhyRzxt7pz78K` "Redox reactions" (no SME definition) | Confirmed **4CH1-2.20** via page context (same SME page as the sim-1.0 "Oxidation & Reduction" point; note code 2.20). Not referenced by any question part |
| Duplicate codes 1.10 ×5, 1.36 ×2, 1.58C ×2, 2.20 ×2 | Confirmed legitimate **SME splits** of one official statement into several teaching spec points, each quoting the full statement at similarity ≈ 1.0 |

## 4. Results

- 162 SME spec points resolved to 4CH1 codes (0 unresolved)
- 1,404 parts tagged; parts carrying SME ids with no code: **0**
- Parts without SME ids (and hence no codes): 46 (SME tags some parts to
  question-level only)
- Distinct codes used: 154 of 182; references per section: S1 699, S2 432,
  S3 187, S4 436; C-suffixed (Chemistry-only) codes in use: 39
- Top codes by part references: 4CH1-1.25 (×52, balanced equations),
  4CH1-4.41C (×38), 4CH1-4.3 (×34), 4CH1-1.10 (×31), 4CH1-4.26 (×28),
  4CH1-1.29 (×26) — all plausible for chemistry exam questions

## 5. Limitations (honesty notes)

- The resolution translates **SME's own per-part spec tags** into official
  codes; it does not independently re-tag questions. If SME mis-tags a part,
  this table preserves that error (with faithful provenance).
- The single `spec_map` disagreement (4.15) means the notes corpus has a
  known mapping gap on the sulfur-dioxide statement; fixing the note side is
  a separate, human-gated change (c10 pipeline) and intentionally **not**
  done here.
- Matching is deterministic text similarity, not semantic understanding; the
  adjudication file records why each low-confidence/ambiguous case is still
  correct. A future human review can upgrade any record to
  `HUMAN_VALIDATED` without re-running the pipeline.
