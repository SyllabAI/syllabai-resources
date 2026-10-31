# Coverage report — igcse-biology-19 video map (draft P2)

| | |
| --- | --- |
| Task | T-VIDEOMAP-P2 |
| Course | `igcse-biology-19` (4BI1, Edexcel International GCSE Biology) |
| Source | Cognito shelf `b2-gcse-iedexcel` — guest-visible set only |
| Spine of record | `apps/hub/spines/igcse-biology-19.json` — 176 SPEC_POINTs, sha `9902a87a443e…` |
| Generated | 2026-10-31T11:54:43.321Z |

## Coverage

| Metric | Value |
| --- | --- |
| Spec points (spine) | 176 |
| Spec points with ≥1 drafted video | 137 (78%) |
| Spec points with no video (honest) | 39 |
| Videos (distinct ids) | 73 |
| Videos with ≥1 drafted mapping | 72 |
| Videos unmapped | 1 (1.4) |
| Mapping rows | 105 (73 high / 30 medium / 2 low) |
| Guest-gated lessons (D1) | 34 |

## Method

1. Deterministic lexical evidence (`align-deterministic.mjs`) — refs deliberately ignored:
   Cognito's chapter numbering ≠ 4BI1 spec numbering (amendment A6; 25/109 ref coincidences,
   several misleading, e.g. Cognito `3.1 Photosynthesis` vs spec `3.1` meiosis).
2. LLM draft pass (`align-curation.json`) over title + description + keyPoints vs spine statements;
   every row carries a one-line evidence string; refs resolved to videos via the P1 inventory.
3. Gates: referential integrity, id shape, dup ids, draft law, census recompute — all enforced
   in `align-build-draft.mjs` (this file's numbers are generated, not hand-written).

## Coverage by topic

| Topic | Mapped / total |
| --- | --- |
| Structure and functions in living organisms | 82 / 95 |
| Reproduction and inheritance | 29 / 39 |
| Use of biological resources | 7 / 20 |
| Ecology and the environment | 15 / 18 |
| The nature and variety of living organisms | 4 / 4 |

## Unmapped spec points by topic

- **Structure and functions in living organisms** (13): `2.7`, `2.8`, `2.22`, `2.33B`, `2.39`, `2.45B`, `2.49`, `2.55B`, `2.58B`, `2.70`, `2.79B`, `2.89`, `2.95B`
- **Reproduction and inheritance** (10): `3.4`, `3.5`, `3.6`, `3.7`, `3.8`, `3.11`, `3.12`, `3.21B`, `3.26`, `3.27`
- **Ecology and the environment** (3): `4.4B`, `4.11B`, `4.17`
- **Use of biological resources** (13): `5.1`, `5.2`, `5.3`, `5.4`, `5.5`, `5.6`, `5.7`, `5.8`, `5.9B`, `5.17B`, `5.18B`, `5.19B`, `5.20B`

## Notes

- `1.4 Magnification & Units` has no spine statement (skills content) — recorded unmapped.
- The 34 guest-gated lessons (full list in review-file.md) are excluded by the draft law, not forgotten (D1).
- `b2-gcse-iedexcel` also carries modular/double-award relevance for future lanes; this draft binds the triple lane only.
