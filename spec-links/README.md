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

## CIE lanes (T-SPECS-CIE-JOIN-1) — ACCEPTED (T-SPECS-CIE-GATE-1)

The 44 `cie-*.json` sidecars join the Cambridge (CIE) SME lanes to the
official codes parsed by T-SPECS-CIE-PARSE-1 (`Official-Specifications/
parsed/<cie-slug>/`, 33 qualifications). Same item shape and schema as the
Edexcel files, plus additive CIE blocks:

- `review_state` — **ACCEPTED by T-SPECS-CIE-GATE-1** (2026-10-19, operator
  directive "review/promotion gate proceed"): promoted from SUGGESTED after
  the join battery + independent re-verification (T1 3547/3547, T2 584/584
  lower-bound, zero defects). Tier policy: `T1_verbatim` authoritative,
  `T2_near` accepted-near non-authoritative hint; unresolved anchors stay
  `pending` (AGENT.md rules 1-3).
- `registry` — the lane's parsed qualification (id, family, point count).
- `anchors` — spcpt anchor counts, universe size/resolved, and the count of
  flashcards discovered-but-uncoded (CIE decks carry no spec links, so
  flashcards contribute honest zeros and are not itemized).

Method: deterministic text join only. SME spec-point `definition` lines are
matched against official point texts (`T1_verbatim` normalized equality or
>=8-token containment; `T2_near` Jaccard >= 0.55 path-restricted / >= 0.75
global), with the SME Cambridge path numbering (section/topic/leaf -> X.Y.Z)
generating candidates where the SME paths mirror the official numbering.
Co-ordinated-science lanes filter by point scope; core/extended maths lanes
prefer their tier. No semantic-similarity coverage is manufactured — lanes
whose SME substrate carries name-only spec-point records (maths, English,
ICT, RS, accounting, economics-25, further maths, double-award biology)
land their anchors in `pending` for a later operator-verdict lane, exactly
as the Edexcel side evolved (T-SPEC-2b/2c).

Built by `scripts/cie_spec_join.py` (deterministic; `--stamp` pins
`generated_utc`), validated by `scripts/cie_join_check.py` (battery J1-J10,
`graph/reports/T_SPECS_CIE_JOIN_1_CHECK.json`).
