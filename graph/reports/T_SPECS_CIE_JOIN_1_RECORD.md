# T-SPECS-CIE-JOIN-1 — CIE join lane record

- Date: 2026-10-19 (Asia/Dhaka; session zai-web `web-64d10b73-…`, gateway trace `1a150ac5cff976a9`)
- Operator directive: *"join lane — map SME spec-point tags to official CIE codes"* — fires NEXT lane #2
  of the T-SPECS-CIE-PARSE-1 record ("the join lane (SME tags -> official CIE codes,
  spec-links/cie-*.json SUGGESTED until the review gate) — operator-gated").
- Base commit: `cddf6af` (T-SPECS-CIE-PARSE-1, on origin/main).
- Lane script: `scripts/cie_spec_join.py` (`cie-spec-join-1.0`), battery `scripts/cie_join_check.py`.

## What was built

44 learner spec-links sidecars `spec-links/cie-*.json` — one per CIE SME course lane — in the EXACT
`syllabai.learner-spec-links/1.0` shape of the 49-file Edexcel precedent
(`scripts/build_learner_spec_links.py`), plus additive CIE blocks
(`board`, `review_state`, `registry`, `anchors`):

- `review_state`: **SUGGESTED / gate pending** per AGENT.md rule 2 (agent-generated mappings are
  suggestions until the review/promotion gate accepts them). Every unresolved anchor stays
  `pending`; nothing was invented (rule 3).
- Items: only content items that carry `spec_point_ids` anchors enter `items` (same contract as
  the Edexcel build): notes (`rn_*`, label = page_title, section/topic = SME path slugs) and
  exam-question parts (`qstnprt_*`, label = `<question ref> / part <order>`).
- Flashcards: the CIE decks (`deck.json`) carry a `spec_links` field but every CIE card holds none,
  so flashcards contribute **honest zeros** and are not itemized; the discovered-but-uncoded count
  is recorded per lane in `anchors.flashcards_discovered_uncoded` (28,718 total).

## Mechanism (deterministic, zero-LLM)

1. **Universe reconstruction.** The CIE corpus has no per-course `spec_point_index.json` (the SME
   spec-point harvest stopped at the SME-native index for the 49 Edexcel-side courses only, and the
   Cambridge scrape lanes stored spec-point records embedded in the notes). Each CIE note JSON
   embeds its spec-point block (`type:"spec_point"`, id `spcpt_*`, `name`, `definition`); the lane
   universe is the union of those blocks, read directly from git blobs (`cat-file --batch`,
   chunked; no worktree materialization, no assets touched).
2. **Candidate generation.** SME Cambridge path numbering mirrors the official syllabus numbering
   (section `1-…`, topic `1-1-…`, leaf `1-1-1-…` → official `X.Y.Z` / `X.Y`): candidates = points
   whose canonical code equals the leaf code, else the subsection prefix class, else the whole
   registry (text-only subjects). `canon_code` strips the `C`/`E` tier letters (0580/0607) and the
   `Biology-`/`Chemistry-`/`Physics-` scope prefixes (0653/0973). Co-ordinated-science lanes
   filter candidates by point scope; core/extended maths lanes prefer their tier.
3. **Text confirmation (tiers frozen).**
   `T1_verbatim` — a normalized SME definition line equals a normalized official point text
   (`&`→`and`, punctuation/quote/dash folding), or containment with ≥8 shared tokens;
   `T2_near` — token Jaccard ≥ 0.55 (path-restricted) / ≥ 0.75 (global), or the
   unique-single-point subsection head whose (column-artifact-stripped) title equals the SME
   spec-point name. Otherwise **pending**. `method`: `cie_definition_text_join` (path-restricted)
   / `cie_text_join` (global). Point pools include `sub_items` content as a second pool where the
   parse recorded it.
4. **Exact candidate pruning** (performance, lossless): token→(point,pool) postings + size floor +
   per-line memoization; `scan_line` is record-independent and cached per `(threshold, line)`, the
   record-dependent name rule rides an exact-equality index. The join runs 44 lanes in ~35 min
   (the earlier unpruned form exceeded 10 min on the 0625/9702 lanes).

## Footprint

- Added: `spec-links/cie-*.json` (44), `scripts/cie_spec_join.py`, `scripts/cie_join_check.py`,
  `graph/reports/T_SPECS_CIE_JOIN_1_RECORD.md`, `graph/reports/T_SPECS_CIE_JOIN_1_CHECK.json`.
- Modified (additive only): `spec-links/manifest.json` (44 CIE rows appended; all pre-existing
  rows value-identical vs HEAD — J7b), `spec-links/README.md` (CIE section appended).
- Byte-untouched: all 49 Edexcel spec-links files (J8, sha256 vs HEAD), both SME trees,
  Official-Specifications/**, graph/** (records added only), everything else.

## Results

- Anchored items: **28,913** (notes 4,453 / question parts 24,460); **coded 3,373**;
  pending anchor refs 36,823; universe 8,651 spcpt ids, 755 text-resolved.
- By registry family (coded/items): int_statements 2,338/14,811 · tier_columns 815/3,746 ·
  nmk_outcomes 220/3,066 · ce_codes 0/6,126 · heading_bullets 0/926 · lettered_items 0/238.
- Top lanes: a-level-biology-25 1722/1773 · igcse-geography-20 340/689 · igcse-physics-23 267/794 ·
  co-ordinated-double-award-23-chemistry 255/463 · igcse-computer-science-23 212/434 ·
  igcse-biology-23 120/726.
- **Honest zeros** where the SME substrate carries name-only, non-numeric-path spec-point records
  (definitions absent): all 8 maths lanes (0580/0606/9709 — `ce_codes`/`heading_bullets` families),
  English language/literature, history, ICT, religious studies, accounting, economics-25,
  environmental management, further maths, double-award biology. These stay `pending` for a later
  operator-verdict lane, exactly as the Edexcel side evolved (T-SPEC-2b/2c).
- Known corpus limitation (recorded, not a defect): CIE EQ `topic.json` parts reference
  `spcpt_*` ids that are dangling in the corpus itself (no embedded definition anywhere); they
  remain pending until the SME-native spec-point index is harvested for the CIE lanes.

## Checks

Battery `scripts/cie_join_check.py` **J1–J10: 12/12 PASS** at the round commit
(`graph/reports/T_SPECS_CIE_JOIN_1_CHECK.json`):

| id | check |
|----|-------|
| J1 | 44 well-formed SUGGESTED sidecars (schema/course/board/review_state) |
| J2/J2b | lane↔manifest bijection 44/44; sidecar qual == manifest mapping |
| J3 | zero dangling official ids (id AND code verified in the lane's parsed registry) |
| J4 | official_id prefix == registry internal QUAL prefix |
| J5 | tier/method vocabulary frozen ({T1_verbatim,T2_near} / {cie_definition_text_join,cie_text_join}) |
| J6 | universe conservation (note-block recount == anchors.universe_ids) + pending well-formedness |
| J7/J7b | sidecar totals cross-foot; manifest rows == sidecar totals; pre-existing manifest rows value-identical vs HEAD |
| J8 | Edexcel spec-links files byte-identical vs HEAD (sha256) |
| J9 | footprint guard (git status ⊆ declared paths) |
| J10 | fixed-stamp rerun byte-identical (3 sample lanes) |

Battery fixes made during the run (recorded honestly): J4's prefix derivation corrected (the
registry `id` field is the slug; the internal prefix comes from the points themselves), J6's
pending-integrity claim corrected to the corpus reality (dangling EQ-referenced spcpt ids are an
honest pending state), J9's porcelain regex fixed, J7's kind pluralization fixed.

## Scope guards

The C42 store + all R-records, the corpus, SME-RevisionNotes/**, SME-ExamQuestion/**,
SME-Flashcards/**, Official-Specifications/** (parse tree unchanged), graph/ (records added only),
all Edexcel spec-links files — byte-untouched.

## NEXT (operator-gated, NOT fired by this directive)

1. **Review/promotion gate** — accept or reject the SUGGESTED sidecars (AGENT.md rule 2); on
   acceptance the learner UI may consume them.
2. **Operator-verdict fill lane** for the honest-zero lanes (maths/English/ICT/RS/accounting/…),
   mirroring the Edexcel T-SPEC-2b/2c evolution.
3. **SME-native spec-point index harvest for the CIE lanes** (`spec_point_index.json`), to resolve
   the dangling EQ-referenced spcpt ids.
4. R41-shaped validation re-gate — explicit instruction only; standing Render console disable lever.
