# Learner spec-links (UI serving bundle)

One JSON per SME course: every learner-facing content item (revision note,
exam question part, flashcard) joined to official Edexcel specification
codes, with provenance preserved. This is the data contract the learner UI
renders for "spec links" — canonical truth only (no learner state).

## Files

- `spec-links/<course>.json` — schema `syllabai.learner-spec-links/1.0`
- `spec-links/manifest.json` — per-course totals
- Built by `scripts/build_learner_spec_links.py --all` (idempotent, offline)

## Item shape

```json
"rn_xBYWN9JGPSnmJVY7": {
  "kind": "note",                    // note | question_part | flashcard
  "label": "Selective Breeding in Animals",
  "section": "5-use-of-biological-resources",
  "topic": "selective-breeding",
  "codes": [
    {"official_id": "IGCSE_BIOLOGY:5.7B",
     "official_code": "5.7B",
     "tier": "T1_verbatim",
     "method": "definition_text_join"}
  ],
  "pending": ["spcpt_..."]           // anchored upstream, join still unresolved
}
```

## Provenance tiers (never guessed)

- `T1_verbatim` / `T2_near` / `T3_section_anchored` / `T4_fuzzy` (T4 always
  carries a review flag upstream) — from `spec_point_map.json`
- `S1_name_match` / `S2_name_ambiguous` (S2 flagged) — name-only regimes
- flashcard codes additionally via `sme_spec_link_inherited` (SME's own
  card→spcpt anchor through our verified map) or `card_text_join`
  (alignment-checked fill-in-the-blanks / definition text)
- `pending` lists SME `spcpt_*` anchors whose official join is still
  unresolved — render as "pending link", never silently dropped

## Update chain

`spec_point_map.json` (map_spec_points.py) → `flashcard_spec_map.json`
(map_flashcards.py) → `spec-links/` (build_learner_spec_links.py).
When any upstream layer changes, re-run the downstream builders; the
manifest records coverage so regressions are visible.
