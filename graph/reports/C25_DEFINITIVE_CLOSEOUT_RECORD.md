# C25 definitive-lineage closeout record — 2026-09-20

Independent closeout of the definitive-swap directive (operator 2026-09-19: make the
PDF-direct-parse the definitive specification-point source, copy all ratified
enrichments, retire the OCR lineage; follow-up directive: find and fix all parse-damage
classes with the official PDF as cross-check ground truth). Push authorization for
`syllabai-resources` granted 2026-09-20 for this closeout lane.

Context: the swap (T-C23 `a7fdc39c`) and the 1,049-finding PDF-cross-checked repair
(T-C24 `9f9f8fcb`) landed from a parallel lane, followed by T-SME-11
(`9e6b2cd1`, `c2fcd88a`). This lane therefore executed **verification + residual
repair**, not a redo. Everything below is re-verified from remote pins after a full
workspace reset (state rebuilt from `origin/main` @ `c2fcd88a`; PAT re-extracted;
sha256 pins recomputed).

## 1. Verification results (all executed fresh at `c2fcd88a`)

| Check | Result |
|---|---|
| Definitive store lineage | `graph/specification_points.yaml` = PDF-direct (meta `source_documents` = official PDF sha1 `3ad641b7…` + canonical `spec_points.json`, builder canonical-builder-2.0; `definitive_lineage.retired_lineage` documents the OCR md + `c09` generator as retired) |
| Records | 182 spec_points (incl. 52 C-suffixed), 22 records with `official_bullets` (71 bullets total) — matches C23 record |
| Known damage spots | 1.10 CJK artifact GONE; 1.27 `$A_r$` residue GONE; wording verbatim-correct |
| Damage-class sweep | **0 hits** — patterns: CJK, inline `$…$` LaTeX, full-width punctuation, U+FFFD, UTF-8 double-encoding, literal `\uXXXX` escapes, control chars — across **80 derived YAMLs** (20 subjects × topics/spec_points/practicals/relationships), **8 graph stores**, and the canonical `igcse-chemistry/spec_points.json` |
| Canonical ↔ store wording | **182/182 codes, 0 mismatches** (confirms T-C24 "chemistry diff 182/182") |
| SPEC evidence resolution | **92/92** `kind: SPEC` edge quotes resolve against the definitive store (normalized containment, 0 unresolved); concepts/concept_edges re-anchor chain verified: C23 post-pin `ccf89606…` legitimately superseded by T-C24's 2 SPEC quote re-anchors + filename completions → current pins below |
| Damage-flag doctrine | 4.30C `possible-superscript-loss` kept (C23 decision honored); 4.49C colon exception clean; store damage flags otherwise empty |
| OCR lineage retirement | OCR md deleted from `Official-Specifications/parsed/igcse-chemistry/` (content preserved in VCS history at `d4f34e88` and earlier); 12 re-anchored quote originals preserved verbatim in `C23_DEFINITIVE_SWAP_RECORD.md` |

## 2. Residual repairs (this commit)

1. **`graph/specification_points.yaml`** — meta `statement_text_policy` still claimed
   "verbatim from md OCR … never fixed", inherited verbatim from the old store via
   `meta = dict(old_meta)` in the emitter (never overridden). Post-C23 this is false.
   Rewritten to state the actual policy: verbatim from the official PDF
   (canonical PDF-direct parse, whitespace-normalised only; PDF glyph-geometry
   respacing per C24); notation damage preserved and flagged, never fixed.
2. **`scripts/c23_emit_definitive_specpoints.py`** — same override added at emit time so
   any future re-emission carries the correct policy (root-cause fix).
3. **`scripts/c09_spec_graph_extract.py`** — RETIRED banner prepended to the docstring
   (C23 retired the lineage but left the script unmarked; nothing prevented accidental
   re-emission of OCR-lineage stores over the definitive one).

All three are meta/documentation-only: no statement text, no structure, no node state.

## 3. Documented, deliberately not touched

- `graph/{topics,practicals,relationships,assessment_objectives,command_words}.yaml` —
  untouched by C23/C24 (last touched `d4f34e88`), so their "verbatim from md OCR"
  policy lines are **still accurate** for their own text; editing them would be
  falsification. They carry **no damage-class hits**. Open item for a future round:
  PDF-refresh these five sibling stores (their generator `c09` is retired; the refresh
  needs its own emit path — recommended to ride the next T-C24-class emit round).
- The five sibling stores' `generator:` fields still name the retired `c09` script —
  accurate as history, flagged here.

## 4. Pins (sha256)

| File | Pre-edit | Post-edit |
|---|---|---|
| `graph/specification_points.yaml` | `a57e082000e321cf…` | `956d276f6e4354fa…` |
| `scripts/c23_emit_definitive_specpoints.py` | `ce7019f531524c76…` | `135452ddc1f3886c…` |
| `scripts/c09_spec_graph_extract.py` | `524eb71ccd9c7571…` | `cf27444eb2ee57c4…` |
| `graph/concepts.yaml` (reference, untouched) | — | `634a743b65d1612b…` |
| `graph/concept_edges.yaml` (reference, untouched) | — | `ccc674cf3a94b8e4…` |

## 5. Scope guards honored

Node states byte-untouched; no surface changes; 2012-Jan escalations and the data
bridge not approached; D2 sweep was read-only (0 findings → no content edits were
needed beyond the meta repairs above); R1 scope respected (chemistry D1 lane; the D2
sweep covered all subjects read-only and confirmed T-C24's repairs).
