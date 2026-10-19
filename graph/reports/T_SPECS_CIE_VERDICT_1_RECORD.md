# T-SPECS-CIE-VERDICT-1 — operator-verdict fill lane record

- Date: 2026-10-19 (Asia/Dhaka; session zai-web `web-64d10b73-…`, gateway trace `1a15123a0964b44d`)
- Operator directive: *"operator-verdict fill lane"* — fires NEXT lane #1 of the
  T-SPECS-CIE-GATE-1 record ("the operator-verdict fill lane for the honest-zero lanes
  (maths/English/ICT/RS/accounting/…) — the Edexcel T-SPEC-2b/2c evolution; its verdicts
  land authoritative by construction").
- Base commit: `fea58c8a` (T-SPECS-CIE-GATE-1, on origin/main).
- Lane script: `scripts/cie_verdict_fill.py` (deterministic engine, fixed stamp, byte-idempotent),
  verdict sheet `scripts/cie_verdict_fill_verdicts.yaml`, battery `scripts/cie_verdict_check.py`.

## What was built

Identity-grade operator verdicts applied to the **25 honest-zero CIE lanes** (the lanes whose
post-gate `items_with_codes == 0` because the SME substrate carries name-only, non-numeric-path
spec-point records the join's text confirmation could not fire on):

- **613 spec-point ids resolved** across the 25 lanes (sheet: 613 resolve entries + 965
  ambiguous-hold entries), cascading **2,923 learner code entries** into the sidecars
  (`tier: V*`, `method: operator_verdict`).
- **4,386 ids stay `pending` with structured reasons** recorded per lane in
  `anchors.verdict.pending_reasons`: `no_unique_identity` 3,421 ·
  `finer_than_official_subsection` 786 · `name_phrase_multi_text` 179 ·
  `dangling_eq_reference` 0 (the corpus's dangling EQ refs live in the coded lanes, not here).
- The gate's **ACCEPTED review states and provenance are preserved**; `review_state.verdict`
  and `anchors.verdict` blocks are additive. Unresolved anchors stay pending (AGENT.md rule 3
  continues post-fill).

## Verdict rules (deterministic, zero-LLM, single-target identity only)

| tier | rule | resolves |
|------|------|---------:|
| `V1_name_text_identity` | norm(name) == norm(official point text), unique in pool | 110 |
| `V2_name_phrase_identity` | token-bounded norm(name) phrase in exactly one official point text | 475 |
| `V3_subsection_head_identity` | head (name or note topic title) == artifact-stripped subsection title AND the subsection holds exactly one point in the pool | 25 |
| `V4_settext_title_identity` | note-name leading segment == quoted set-text title, unique (0475 literature) | 3 |
| `V5_topic_scoped_phrase_identity` | V2 ambiguous globally, exactly one hit inside the official topic whose title == the SME section/topic title | 0 |

Every resolve carries verbatim evidence in the sheet (`sme_name`, `official_text`, rule detail;
V3 adds `head`/`head_source`). Any rule hitting >1 official point → the id is NOT resolved and
lands in the sheet's ambiguous list with its N matched codes (quarantine, rule 7). Pools mirror
the join lane's scoping: Biology/Chemistry/Physics scope filter (0654), Core/Extended tier filter
(0580/0607), and per-component official topics for the five 9709 maths lanes.

Doctrine guards: an id is **never collapsed onto several statements** (the Edexcel T-SPEC-2c
precedent) — that is the `finer_than_official_subsection` reason (786 ids, mostly env-mgmt and
business, where SME topic == official subsection title but the subsection holds >1 point); no
semantic-similarity coverage is manufactured (rule 3); SME reuses `spcpt_*` ids across course
trees, so verdicts are evaluated and recorded **per (lane, id)**.

## Per-lane outcomes (resolved ids / code entries / items_with_codes after fill)

| lane | resolved | codes | items_with_codes |
|------|---------:|------:|-----------------:|
| cie-a-level-business-23 | 29 | 134 | 108/831 |
| cie-a-level-computer-science-19 | 49 | 373 | 344/1380 |
| cie-a-level-economics-23 | 78 | 78 | 55/159 |
| cie-a-level-maths-20-mechanics | 6 | 184 | 173/565 |
| cie-a-level-maths-20-probability-and-statistics-1 | 2 | 34 | 32/633 |
| cie-a-level-maths-20-probability-and-statistics-2 | 2 | 77 | 77/580 |
| cie-a-level-maths-20-pure-1 | 6 | 105 | 104/1280 |
| cie-a-level-maths-20-pure-3 | 3 | 51 | 51/1400 |
| cie-as-english-general-paper-21 | 1 | 1 | 1/22 |
| cie-igcse-accounting-21 | 35 | 123 | 105/316 |
| cie-igcse-accounting-25 | 34 | 34 | 26/105 |
| cie-igcse-economics-25 | 0 | 0 | 0/48 |
| cie-igcse-english-language-20 | 39 | 39 | 25/68 |
| cie-igcse-english-language-25 | 0 | 0 | 0/174 |
| cie-igcse-english-literature-21 | 3 | 4 | 2/255 |
| cie-igcse-environmental-management-25 | 46 | 68 | 53/154 |
| cie-igcse-further-maths-additional-maths-25 | 3 | 18 | 18/496 |
| cie-igcse-history-18 | 24 | 69 | 55/407 |
| cie-igcse-ict-21 | 51 | 241 | 223/468 |
| cie-igcse-maths-25-core | 20 | 240 | 231/1504 |
| cie-igcse-maths-25-extended | 32 | 353 | 351/1739 |
| cie-igcse-maths-international-maths-23-core | 23 | 235 | 223/1244 |
| cie-igcse-maths-international-maths-23-extended | 26 | 236 | 235/1639 |
| cie-igcse-religious-studies-23 | 79 | 154 | 98/238 |
| cie-igcse-science-co-ordinated-sciences-double-award-23-biology | 22 | 72 | 67/339 |

(Totals cross-checked by V6/V7; per-lane `items_with_codes` recomputed post-apply.)

## Battery

`scripts/cie_verdict_check.py` **V1–V10: 12/12 PASS** (incl. the V5a SPEC self-test)
(`graph/reports/T_SPECS_CIE_VERDICT_1_CHECK.json`):

| id | check |
|----|-------|
| V1 | 25 verdict lanes well-formed (ACCEPTED + gate intact + additive verdict blocks) |
| V2 | verdict bijection: sheet (lane,id) == by_tier sums == independently recomputed resolved set (pre-pending minus post-pending) |
| V3 | zero dangling verdict targets (official_id AND official_code in the lane registry) |
| V4 | verdict + join vocabularies both conform (V*+operator_verdict; T*+cie_* unchanged) |
| V5a | normalization SPEC equivalence self-test (5 unicode-punctuation probes) |
| V5 | INDEPENDENT re-derivation of all 613 resolves from source blobs (fresh implementation) |
| V6 | cascade integrity + fresh universe recount (blobs re-read; totals/pending_refs/universe_resolved recomputed) |
| V7 | manifest verdict rows + pre-existing rows value-identical + cie_verdict block |
| V8a | 19 non-verdict CIE lanes + all Edexcel spec-links byte-identical vs HEAD |
| V8b | join payload preserved verbatim (codes/order); pending delta == verdict removals exactly |
| V9 | footprint guard (git status within declared set) |
| V10 | fixed-stamp re-evaluation of 2 sample lanes == sheet |

Determinism: the engine re-run with the fixed stamp is byte-identical across **all** artifacts
(25 sidecars, manifest, sheet, FILL.json — verified by sha256 across consecutive runs).

## Defects caught and fixed en route (recorded honestly)

1. **Sheet keying defect** (caught by count reconciliation): the sheet was initially keyed by
   `spcpt_*` id alone; SME reuses ids across course trees, so 53 per-lane verdict entries were
   being overwritten (35 ids shared across lanes). Sheet rebuilt as per-(lane, id) entries.
2. **Bookkeeping stability** (caught by the idempotency diff): `code_entries_added` was counted
   at apply time, so a re-run recorded 0. Changed to a post-apply census of
   `method == operator_verdict` entries — stable across runs.
3. **Battery SPEC divergence** (caught by V5's initial 4/613 failures — history ×2, RS ×2): the
   battery's fresh normalizer preserved apostrophes/typographic quotes ("'Hundred Days'",
   "Shi'ah") while the lineage SPEC strips all punctuation. The 4 flags were ALL verifier SPEC
   gaps, not engine defects; the battery now shares the lineage SPEC semantics and pins the
   equivalence with a 5-probe self-test (V5a), the gate's own pattern.

## Footprint

- Modified: `spec-links/cie-*.json` (25 verdict lanes: codes + pending + totals + additive
  blocks), `spec-links/manifest.json` (25 rows + `cie_verdict` block), `spec-links/README.md`
  (verdict lane section).
- Added: `scripts/cie_verdict_fill.py`, `scripts/cie_verdict_fill_verdicts.yaml`,
  `scripts/cie_verdict_check.py`, `graph/reports/T_SPECS_CIE_VERDICT_1_RECORD.md`,
  `graph/reports/T_SPECS_CIE_VERDICT_1_FILL.json`, `T_SPECS_CIE_VERDICT_1_CHECK.json`.
- Byte-untouched: the 19 coded CIE lanes, all 49 Edexcel spec-links files, SME trees,
  Official-Specifications/**, graph/** beyond the three verdict records.

## NEXT (operator-gated, NOT fired by this directive)

1. **SME-native spec-point index harvest for the CIE lanes** (`spec_point_index.json`) —
   resolves the EQ-referenced dangling spcpt ids and gives the name-only substrates a real
   index to join against (the designed cure for most of the 4,386 structured pendings).
2. **Learner-UI consumption** — verdict entries render with their operator-verdict
   authoritative semantics alongside the gate's T1/T2 tier policy.
3. R41-shaped validation re-gate — explicit instruction only; standing Render console disable
   lever; **PAT rotation still CRITICAL-OVERDUE** (fingerprint `a8ccee736aa8c75b`, 13 recorded
   plaintext transits).
