#!/usr/bin/env python3
"""c40 — generate the substrate REPORT + operator REVIEW SHEET from the emitted
maths-a chunk→SP store (the c13_substrate_report.py convention replayed).

Deterministic: same store -> byte-identical reports (no clocks in content).
Sampling (C13 convention): ALL ambiguous rows (the span-marker construction has
none by design) + seeded stratified sample of the anchored rows stratified by
UPSTREAM JOIN ASSURANCE — rows whose join score is <1.0 or absent are sampled at
100% (the low-assurance stratum, chemistry's 'low confidence' analog), rows at
score == 1.0 at ceil(20%). Plus EVERY worklist row as a Part B decision.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import graph_paths as GP
from c40_maths_a_chunk_sp_substrate import (  # noqa: E402
    CORPUS, JOIN, R, norm, span_chunks, load_corpus)

TOOL = "scripts/c40_maths_a_substrate_report.py"


def rank(seed: str, mapping_id: str) -> str:
    return hashlib.sha256(f"{seed}|{mapping_id}".encode()).hexdigest()


def main() -> int:
    store_path = GP.store("spec_chunk_mappings", "igcse-maths-a")
    doc = yaml.safe_load(store_path.read_text(encoding="utf-8"))
    meta, rows = doc["meta"], doc["rows"]

    anchored = [r for r in rows if "chunk" in r and r.get("spec_code")]
    worklist = [r for r in rows if "worklist_reason" in r]
    unres_wl = [r for r in worklist if r.get("spec_code") is None]
    unmapped = [r for r in worklist if r.get("spec_code")]
    ambiguous = [r for r in anchored if r.get("anchor", {}).get("ambiguous_hits", 0) > 1]

    # ---- seeded stratified sample ------------------------------------------
    seed = hashlib.sha256(
        yaml.safe_dump(rows, allow_unicode=True, sort_keys=False).encode()
    ).hexdigest()[:16]

    def stratum(r):
        s = r["provenance"]["upstream"].get("join_score")
        if s is None:
            return "none"
        return "exact" if float(s) >= 1.0 else "partial"

    def take_strat(items):
        by = {}
        for r in items:
            by.setdefault(stratum(r), []).append(r)
        picked = []
        for cls in sorted(by):
            lst = sorted(by[cls], key=lambda r: rank(seed, r["mapping_id"]))
            n = len(lst) if cls in ("none", "partial") else -(-len(lst) * 20 // 100)
            picked += [(cls, r) for r in lst[:n]]
        return picked

    sample_pairs = take_strat([r for r in anchored
                               if r.get("anchor", {}).get("ambiguous_hits", 0) == 0])
    sample = ambiguous + [r for _, r in sample_pairs]
    strata_of = {r["mapping_id"]: cls for cls, r in sample_pairs}
    for r in ambiguous:
        strata_of[r["mapping_id"]] = stratum(r)

    # fresh chunk index for excerpts (re-chunked, not store-copied)
    r_reader = R()
    _, notes = load_corpus(r_reader)
    by_note, _ = span_chunks(notes)
    idx = {(n["manifest"]["path"], c["ordinal"]): c
           for n in notes for c in by_note[n["manifest"]["path"]]}
    title_of = {n["manifest"]["path"]: n["note"].get("title") or ""
                for n in notes}

    # ------------------------------------------------------------ report ------
    tier_counts = {}
    for r_ in anchored:
        tier_counts[r_["provenance"]["upstream"].get("join_tier") or "?"] = \
            tier_counts.get(r_["provenance"]["upstream"].get("join_tier") or "?", 0) + 1
    tier_line = ", ".join(f"{k} {v}" for k, v in sorted(tier_counts.items(),
                                                        key=lambda kv: -kv[1]))

    report = f"""# C40 — maths-a Chunk→SP Mapping Substrate: Construction Report (span-marker construction)

**Status:** CONSTRUCTED — deterministic, zero-LLM, fail-closed; all rows `SUGGESTED`
(RULE_DERIVED tier); promotion to HUMAN_VALIDATED is the operator review-sheet gate,
never this tool.
**Task:** T-C40 — K2 Lane B (chunk substrate) for igcse-maths-a, the C31 §6
instantiation of the T-C13/C13 pattern; the ninth and final K2 store.
**Upstream (recorded honestly per C31 §4.5):** the T-C32 K2-A notes-join —
202 joins / 1 unresolved, validation tier **AI_VALIDATED (operator-delegated
chain)**. Chemistry's Lane B refined a HUMAN_VALIDATED T-C10 quote store; the
maths-a join carries NO evidence quotes, so the anchoring axis is the corpus's
OWN structure: each note is a sequence of SP spans introduced by the corpus's
`spec_point` blocks (203 markers / 191 notes), the join resolves each marker to
the ratified code, and the row's evidence quote is the chunk's own verbatim
self-slice. Nothing invented; the tier difference is carried on every row.
**Tool:** `{meta['tool']}` — deterministic; two independent constructions
byte-identical (gate G7); corpus read disk-first with the persistent cat-file
fallback (the c32 convention).
**Corpus:** `{CORPUS}` (manifest sha256_16 `{meta['notes_manifest_sha256_16']}`)
**Join artifact:** `{JOIN}`

## Census

| Measure | Value |
|---|---|
| Notes | {meta['notes']} |
| SP spans (spec_point markers) | {meta['spans']} |
| Chunks total (intro / section) | {meta['chunks_total']} ({meta['chunks_intro']} / {meta['chunks_section']}) |
| Anchored rows (resolved spans) | **{meta['rows_anchored']}** |
| Worklist rows — unresolved span | {meta['rows_worklist_anchor_unresolved']} (`spcpt_QWXhzVp2S3VYZdZc` 'Discrete & Continuous Data', the C32 §3 residual — operator adjudication pending) |
| Worklist rows — uncovered SPs | {meta['rows_worklist_unmapped_sps']} |
| SP codes covered | **{meta['sp_codes_covered']} / {meta['registry_size']}** (the C31 §3 notes-coverage bound, exactly) |
| Anchored rows by join tier | {tier_line} |
| Convention | `{meta['convention']}` |

The anchored surface spans the notes corpus: one row per content section chunk
of every resolved span (median chunk {sorted(r['chunk']['chars'] for r in anchored)[len(anchored)//2]} chars; heading-only chunks kept — the
section heading is itself retrievable content, chemistry-parity behavior).
Coverage is bounded by the notes corpus's 111-code census exactly as C31 §6
forecast; the worklist lanes are recorded, not forced.

## Gates (fail-closed, all green at construction)

| Gate | Asserts |
|---|---|
| G1 corpus shape | 191 notes; 203 spec_point markers; every note's first block is its marker; manifest anchor counts == blocks |
| G2 join shape | 202 resolved + 1 unresolved; note-block anchors == join anchors ∪ THE residual; every join note_path in corpus |
| G3 code validity | every emitted code ∈ the ratified 188-point store (0 foreign) |
| G4 anchor fidelity | every row re-verifies quote-in-chunk + chunk sha256_16 against a fresh re-chunking after emit |
| G5 anti-forgery | zero HUMAN_VALIDATED rows; tier RULE_DERIVED; upstream tier recorded verbatim as AI_VALIDATED (operator-delegated chain) |
| G6 worklist completeness | every uncovered SP + every unresolved-span chunk enumerated with a disposition |
| G7 idempotency | two independent constructions byte-identical |

**Evidence-quote discipline:** the self-slice is deterministic (first ≤240
chars, whitespace-cut) and markdown-safe — the cut walks back over whitespace
boundaries until `norm(quote) ⊆ norm(chunk)` verifies (a raw prefix can land
inside a link/emphasis span where normalization diverges; the quote is only
ever shortened, never rewritten).

## Forward contract

Chunk identity (note_path, ordinal, heading, sha256_16 of chunk text) must
survive T-C06 ingestion — the converter/ChunkingService must reproduce
`{meta['convention']}` or the rows fail closed at join time.
"""
    out_reports = GP.reports_dir("igcse-maths-a")
    out_reports.mkdir(parents=True, exist_ok=True)
    (out_reports / "C40_MATHS_A_CHUNK_SP_SUBSTRATE_REPORT.md").write_text(
        report + "\n", encoding="utf-8")

    # --------------------------------------------------------- review sheet ----
    sheet_rows = []
    for r in sample:
        c = idx[(r["note_path"], r["chunk"]["ordinal"])]
        excerpt = re.sub(r"\s+", " ", c["text"])[:420]
        up = r["provenance"]["upstream"]
        score = up.get("join_score")
        score_s = "n/a" if score is None else str(score)
        sheet_rows.append(f"""### {r['spec_code']} — {r['sp_title']}
- Note: {title_of.get(r['note_path'], '')} (`{r['note_path']}`)
- Chunk: ordinal {r['chunk']['ordinal']} — heading `{r['chunk']['heading']}` — sha256_16 `{r['chunk']['sha256_16']}` — {r['chunk']['chars']} chars
- Evidence quote (verbatim self-slice, markdown-safe): "{r['evidence_quote']}"
- Chunk excerpt: «{excerpt}»
- Upstream: T-C32 join {up['join_row']} — tier {up['join_tier']} — score {score_s} — wording {up.get('wording_check')} — validation tier {up['validation_tier']}
- Rationale: {r['rationale']}
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

""")

    wl_rows = []
    for r in unres_wl + unmapped:
        code_s = r.get("spec_code") or "(anchor unresolved)"
        title_s = r.get("sp_title") or ""
        wl_rows.append(f"""### {code_s} — {title_s}
- Note: `{r.get('note_path', '(no notes coverage)')}`
- Chunk: {('ordinal ' + str(r['chunk']['ordinal']) + ' — heading `' + r['chunk']['heading'] + '`') if 'chunk' in r else '(corpus gap — no chunk exists)'}
- Reason: {r['worklist_reason']}
- Disposition: {r['disposition']}
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [ ] DEFER (record why)

""")

    sheet = f"""# C40 — maths-a Chunk→SP Substrate OPERATOR REVIEW SHEET (the promotion gate)

**Seed:** `{seed}` (sha256 of the emitted rows — deterministic regeneration) ·
**Rows:** {len(sample)} anchored spot-checks + {len(worklist)} worklist decisions.
**Rule:** this sheet is the ONLY path from SUGGESTED to HUMAN_VALIDATED for the
chunk→SP substrate. Per-class rollup: any confirmed-precision < 90% on the sampled
rows → rework that class before promotion.
**Sampling:** all ambiguous rows (the span-marker construction has none by design)
+ seeded stratified anchored sample — low-assurance strata (join score <1.0 or
absent) at 100%, score == 1.0 at ceil(20%) — + every worklist row.
**Anti-forgery reminder:** the tool cannot emit HUMAN_VALIDATED rows (gate G5);
only the verdicts recorded here — applied in a recorded deterministic apply step —
can. The upstream join is AI_VALIDATED (operator-delegated chain); the tier
difference to chemistry's T-C10-backed substrate is intentional and recorded.

## Part A — anchored-row spot-check ({len(sample)} rows)

{"".join(sheet_rows)}
## Part B — worklist decisions ({len(worklist)} rows)

{"".join(wl_rows)}
## Rollup

| Part | Rows | CONFIRM | REJECT | HOLD | Precision |
|---|---|---|---|---|---|
| A (anchored spot-check) | {len(sample)} | | | | |
| A stratum: join score == 1.0 | {sum(1 for r in sample if strata_of.get(r['mapping_id']) == 'exact')} | | | | |
| A stratum: join score < 1.0 | {sum(1 for r in sample if strata_of.get(r['mapping_id']) == 'partial')} | | | | |
| A stratum: join score n/a | {sum(1 for r in sample if strata_of.get(r['mapping_id']) == 'none')} | | | | |
| B (worklist) | {len(worklist)} | | {len(worklist)} decided | | |

Gate: Part A precision >= 90% per class AND every Part B row decided -> the store
may be promoted (rows flip to HUMAN_VALIDATED in a recorded, deterministic apply
step — never hand-edits).
"""
    (out_reports / "C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md").write_text(
        sheet + "\n", encoding="utf-8")

    print(f"C40 substrate report + review sheet written")
    print(f"  seed {seed}: {len(sample)} Part A rows "
          f"(exact {sum(1 for r in sample if strata_of.get(r['mapping_id']) == 'exact')} / "
          f"partial {sum(1 for r in sample if strata_of.get(r['mapping_id']) == 'partial')} / "
          f"none {sum(1 for r in sample if strata_of.get(r['mapping_id']) == 'none')}) "
          f"+ {len(worklist)} Part B rows")
    print(f"  {out_reports / 'C40_MATHS_A_CHUNK_SP_SUBSTRATE_REPORT.md'}")
    print(f"  {out_reports / 'C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
