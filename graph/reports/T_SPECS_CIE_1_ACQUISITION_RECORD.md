# T-SPECS-CIE-1 — Official CIE specification acquisition record (2026-10-18)

**Directive:** operator message (gateway trace 1a14f6c452f19ce5, 2026-10-18, zai-web) — "fire CIE specs".

**Result:** ALL 44 `cie-*` SME course lanes now anchor to an official Cambridge International syllabus document. 33 unique official PDFs registered under `Official-Specifications/<cie-...>-<edition-window>/` with full provenance (`spec.json`, Edexcel entry shape + `board`/`edition_window`), the manifest extended in place, and the C1-C7 check battery ALL PASS (`T_SPECS_CIE_1_CHECK.json`).

## Method

1. `scripts/cie_spec_discover.py` — probed all 44 CIE course landing pages (cache `/home/z/my-project/.cache/sme_spec/cie_course_specs.json`): 41 lanes expose `courseExamSpecificationPdfLink` → 30 unique PDFs; 3 lanes null.
2. Manual resolution of the 3 null cards + 1 stale card from the official Cambridge qualification pages (newest-published-edition convention): 4 more PDFs → 33 unique documents (the null accounting/English-language/environmental-management `-25` lanes and the 404'd 8021 2022-2024 edition).
3. `scripts/cie_spec_download.py` — download + validate (`%PDF` magic, pypdf pages, SHA-1, cover-code detection from the cover text with years excluded from code candidates), register `<slug>/spec.json`, extend `manifest.json` in place (Edexcel 23 entries pinned byte-stable via the pre-change sha256 snapshot `scripts/cie_spec_edexcel_snapshot.json`).

## Verification (C1-C7, ALL PASS)

- C1 pdf integrity (sha1/magic/bytes/pages) 33/33 — C2 manifest<->spec.json two-way 33/33 — C3 lane coverage 44/44, each lane EXACTLY one qualification — C4 Edexcel byte-stability 23/23 vs snapshot — C5 cover codes + edition windows 33/33 — C6 totals 56 quals (23 Edexcel + 33 CIE), 93/93 SME courses covered, zero missing — C7 footprint guard: changes confined to `Official-Specifications/**`, `scripts/cie_spec_*`, `graph/reports/T_SPECS_CIE_1_*`, `LICENSE-DATA.md`.

## Observations

- The 2027-2029 redeveloped IGCSE Business syllabus is renumbered **0264**; Co-ordinated Sciences (Double Award) 2025-2027 is **0973** (9-1 line). SME lane year tags are course tags, not syllabus codes.
- One lane per unique edition (not per subject): business and economics register both their 2023-2025 and 2027-2029 editions; geography's two lanes share the single 2025-2026 edition.

## Next lanes (operator-gated, NOT fired by this directive)

1. **CIE parse lane** — deterministic PDF-text parse of the 33 syllabuses into `parsed/<cie-*>` registries (the SCHEMA v1.0 shape; a CIE outcome-numbering family may need a schema extension).
2. **Join lane** — SME spec-point tags → official CIE codes, emitting `spec-links/cie-*.json` sidecars (SUGGESTED state until the review gate accepts them, per `AGENT.md`).
