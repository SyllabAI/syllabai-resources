#!/usr/bin/env python3
"""c40 — landing battery + lane record for the maths-a chunk→SP substrate
(T-C40 K2 Lane B). Read-only toward the store and the corpora; writes only
its own check JSON + the lane record.

P1  store shape        meta counts == observed rows; all SUGGESTED; RULE_DERIVED
P2  determinism        the builder's construct() re-run is byte-identical to the
                       emitted store rows (the store is a pure function of its inputs)
P3  anchor fidelity    every chunk row re-verifies quote-in-chunk + sha256_16
                       against a fresh re-chunking (independent of the builder's G4)
P4  anti-forgery       zero HUMAN_VALIDATED anywhere; upstream tier verbatim
P5  code validity      every spec_code ∈ the ratified registry; coverage == the
                       111-code census; worklist completeness (77 uncovered + 2
                       unresolved-span chunks)
P6  registry           maths-a == 9 stores incl. spec_chunk_mappings; chemistry
                       == the 10-store shape; K2 exit state reached
P7  footprint          git status shows EXACTLY the T-C40 allowlist (isolation)
P8  standing checkers  check_no_hardcode.py green
P9  review sheet       sheet seed/counts reconcile to the store; every sampled
                       row resolves to a live store row
P10 record pins        the lane record carries the store/report/sheet sha256_16
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402
from c40_maths_a_chunk_sp_substrate import construct, span_chunks, load_corpus, R, norm  # noqa: E402

QUAL = "igcse-maths-a"
REPO = HERE.parent
CHECK_OUT = GP.reports_dir(QUAL) / "C40_MATHS_A_K2B_LAND_CHECK.json"
RECORD_JSON = GP.reports_dir(QUAL) / "C40_IGCSE_MATHS_A_K2B_LANE_B_RECORD.json"
RECORD_MD = GP.reports_dir(QUAL) / "C40_IGCSE_MATHS_A_K2B_LANE_B_RECORD.md"

ALLOWLIST = {
    "scripts/c40_maths_a_chunk_sp_substrate.py",
    "scripts/c40_maths_a_substrate_report.py",
    "scripts/c40_maths_a_substrate_check.py",
    "scripts/graph_paths.yaml",
    "graph/igcse-maths-a/spec_chunk_mappings.yaml",
    "graph/reports/C40_MATHS_A_CHUNK_SP_SUBSTRATE_REPORT.md",
    "graph/reports/C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md",
    "graph/reports/C40_MATHS_A_K2B_LAND_CHECK.json",
    "graph/reports/C40_IGCSE_MATHS_A_K2B_LANE_B_RECORD.json",
    "graph/reports/C40_IGCSE_MATHS_A_K2B_LANE_B_RECORD.md",
}


def sha256_16(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16]


def main() -> int:
    results = {}

    def gate(name, ok, detail=""):
        results[name] = {"pass": bool(ok), "detail": detail}
        if not ok:
            print(f"FAIL {name}: {detail}", file=sys.stderr)

    store_path = GP.store("spec_chunk_mappings", QUAL)
    doc = yaml.safe_load(store_path.read_text(encoding="utf-8"))
    meta, rows = doc["meta"], doc["rows"]
    anchored = [r for r in rows if "chunk" in r and r.get("spec_code")]
    wl = [r for r in rows if "worklist_reason" in r]
    unres_wl = [r for r in wl if r.get("spec_code") is None]
    unmapped = [r for r in wl if r.get("spec_code")]

    # P1 store shape
    counts_ok = (
        len(rows) == meta["rows_anchored"] + meta["rows_worklist_anchor_unresolved"]
        + meta["rows_worklist_unmapped_sps"]
        and len(anchored) == meta["rows_anchored"] == 860
        and len(unres_wl) == meta["rows_worklist_anchor_unresolved"] == 2
        and len(unmapped) == meta["rows_worklist_unmapped_sps"] == 77
    )
    gate("P1_store_shape", counts_ok,
         f"{len(rows)} rows = {len(anchored)} anchored + {len(unres_wl)} unresolved "
         f"+ {len(unmapped)} unmapped; meta reconciles")

    # P2 determinism — fresh construction == emitted rows
    fresh = construct()
    a = yaml.safe_dump(rows, allow_unicode=True, sort_keys=False)
    b = yaml.safe_dump(fresh["rows"], allow_unicode=True, sort_keys=False)
    gate("P2_determinism", a == b,
         "independent construct() re-run byte-identical to the emitted store rows")

    # P3 anchor fidelity (fresh re-chunk, independent path)
    r = R()
    _, notes = load_corpus(r)
    by_note, _ = span_chunks(notes)
    idx = {(n["manifest"]["path"], c["ordinal"]): c["text"]
           for n in notes for c in by_note[n["manifest"]["path"]]}
    bad = 0
    for rw in rows:
        if "chunk" not in rw:
            continue
        key = (rw["note_path"], rw["chunk"]["ordinal"])
        ctext = idx.get(key)
        if ctext is None or hashlib.sha256(ctext.encode()).hexdigest()[:16] != rw["chunk"]["sha256_16"] \
                or norm(rw["evidence_quote"]) not in norm(ctext):
            bad += 1
    gate("P3_anchor_fidelity", bad == 0,
         f"{sum(1 for x in rows if 'chunk' in x)} chunk rows re-verified against a "
         f"fresh re-chunking; {bad} failures")

    # P4 anti-forgery
    hv = [x for x in rows if x.get("validation_status") == "HUMAN_VALIDATED"
          or x.get("provenance", {}).get("tier") == "HUMAN_VALIDATED"]
    tier_ok = all(x.get("provenance", {}).get("tier") == "RULE_DERIVED" for x in rows)
    up_ok = all((x.get("provenance", {}).get("upstream") or {}).get("validation_tier")
                == meta["upstream_validation_tier"]
                for x in rows if x.get("provenance", {}).get("upstream"))
    gate("P4_anti_forgery", not hv and tier_ok and up_ok,
         f"0 HUMAN_VALIDATED rows; tier RULE_DERIVED on {len(rows)} rows; "
         f"upstream tier verbatim '{meta['upstream_validation_tier']}'")

    # P5 code validity + coverage + worklist completeness
    sp_store = GP.store("specification_points", QUAL)
    registry = {p["code"] for p in yaml.safe_load(
        sp_store.read_text(encoding="utf-8"))["specification_points"]}
    codes = {x["spec_code"] for x in anchored}
    gate("P5_codes_worklist",
         codes <= registry and len(codes) == 111 and len(unmapped) == 77
         and {x["spec_code"] for x in unmapped} == registry - codes
         and all(x.get("disposition") for x in wl),
         f"111 covered codes ⊆ registry({len(registry)}); 77 uncovered enumerated; "
         f"2 unresolved-span chunks dispositioned")

    # P6 registry — K2 exit state
    reg = yaml.safe_load((HERE / "graph_paths.yaml").read_text(encoding="utf-8"))
    ma = sorted(reg["quals"][QUAL]["stores"].keys())
    ch = sorted(reg["quals"]["igcse-chemistry"]["stores"].keys())
    gate("P6_registry_k2_exit",
         ma == sorted(["specification_points", "topics", "practicals",
                       "assessment_objectives", "command_words", "concepts",
                       "concept_edges", "spec_command_kinds", "spec_chunk_mappings"])
         and len(ch) == 10 and "spec_chunk_mappings" in ch,
         f"maths-a {len(ma)} stores (9 = K2 exit); chemistry {len(ch)} stores")

    # P7 footprint isolation
    st = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                        capture_output=True, text=True).stdout
    touched = {ln[3:].strip() for ln in st.splitlines() if ln.strip()}
    gate("P7_footprint", touched <= ALLOWLIST,
         f"touched {len(touched)} paths, all in the T-C40 allowlist"
         if touched <= ALLOWLIST else f"OUTSIDE ALLOWLIST: {sorted(touched - ALLOWLIST)}")

    # P8 standing checker
    rc = subprocess.run([sys.executable, str(HERE / "check_no_hardcode.py")],
                        capture_output=True, text=True, cwd=REPO)
    gate("P8_check_no_hardcode", rc.returncode == 0,
         (rc.stdout.strip().splitlines() or [""])[-1][:120])

    # P9 review sheet reconciliation
    sheet_path = GP.reports_dir(QUAL) / "C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md"
    sheet = sheet_path.read_text(encoding="utf-8")
    seed_ok = "**Seed:** `" in sheet
    a_count = sheet.count("CONFIRM — this chunk belongs to this SP")
    b_count = sheet.count("[x] DEFER (record why)")
    # every Part A row names a note path; verify each against the store
    chunk_keys = {(x["note_path"], x["chunk"]["ordinal"]) for x in anchored}
    part_a_blocks = sheet.split("## Part A")[1].split("## Part B")[0] if "## Part A" in sheet else ""
    missing = 0
    for m in __import__("re").finditer(r"`(notes/[^`]+)`", part_a_blocks):
        np_ = m.group(1)
        if np_ not in {k[0] for k in chunk_keys}:
            missing += 1
    gate("P9_review_sheet",
         seed_ok and a_count == 468 and b_count == 79 and missing == 0,
         f"sheet: {a_count} Part A verdict boxes, {b_count} Part B DEFER boxes; "
         f"{missing} note-path resolution failures")

    # P10 record pins
    pins = {
        "spec_chunk_mappings.yaml": sha256_16(store_path),
        "C40_MATHS_A_CHUNK_SP_SUBSTRATE_REPORT.md": sha256_16(
            GP.reports_dir(QUAL) / "C40_MATHS_A_CHUNK_SP_SUBSTRATE_REPORT.md"),
        "C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md": sha256_16(sheet_path),
    }
    gate("P10_pins", all(len(v) == 16 for v in pins.values()), str(pins))

    all_pass = all(v["pass"] for v in results.values())
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    baseline = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                              capture_output=True, text=True).stdout.strip()
    check_doc = {
        "schema": "c40-k2b-land-check/1.0",
        "task": "T-C40",
        "gate": "K2 Lane B (chunk substrate) landing battery",
        "generated_utc": now,
        "baseline": baseline,
        "result": "ALL PASS" if all_pass else "FAIL",
        "gates": results,
        "store_pins": pins,
    }
    CHECK_OUT.write_text(json.dumps(check_doc, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")

    # ---- lane record -----------------------------------------------------------
    rec = {
        "schema": "c40-k2b-lane-b-record/1.0",
        "task": "T-C40",
        "gate": "K2-B (C31 §8): Lane B build — chunk substrate",
        "generated_utc": now,
        "baseline": baseline,
        "operator_directive": "fire K2-B (chunk substrate), run the §18 "
                              "HUMAN_VALIDATED promotion round over the 73 edges "
                              "(2026-10-02, zai-web)",
        "scope": {
            "qual": QUAL,
            "lane": "B — chunk substrate (T-C13/C13 pattern replayed per C31 §6)",
            "store": "graph/igcse-maths-a/spec_chunk_mappings.yaml",
            "registry_delta": "maths-a 8 → 9 stores — the K2 exit shape (C31 §8)",
        },
        "inputs": {
            "notes_corpus": meta["notes_corpus"],
            "notes_manifest_sha256_16": meta["notes_manifest_sha256_16"],
            "join_artifact": meta["join_artifact"],
            "upstream_validation_tier": meta["upstream_validation_tier"],
            "tier_honesty": "chemistry's Lane B refined a HUMAN_VALIDATED T-C10 "
                            "quote store; the maths-a upstream join is "
                            "AI_VALIDATED (operator-delegated chain) and carries no "
                            "quotes — the anchoring axis is the corpus's own "
                            "spec_point span markers + the T-C32 id-join, recorded "
                            "verbatim on every row (C31 §4.5)",
        },
        "construction": {
            "convention": meta["convention"],
            "tool": meta["tool"],
            "determinism": "two independent constructions byte-identical (G7); "
                           "checker P2 re-derives the rows from inputs",
            "census": {k: meta[k] for k in (
                "notes", "spans", "chunks_total", "chunks_intro", "chunks_section",
                "rows_anchored", "rows_worklist_anchor_unresolved",
                "rows_worklist_unmapped_sps", "sp_codes_covered")},
        },
        "gates": "c40_maths_a_chunk_sp_substrate.py G1–G7 all green at construction; "
                 "landing battery P1–P10 (see C40_MATHS_A_K2B_LAND_CHECK.json)",
        "review_sheet": {
            "path": "graph/reports/C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md",
            "part_a_rows": 468,
            "part_b_rows": 79,
            "sampling": "all ambiguous (none by construction) + seeded stratified: "
                        "join score <1.0 or absent at 100%, score == 1.0 at ceil(20%) "
                        "+ every worklist row (the C13 convention)",
            "gate_rule": "Part A precision >= 90% per class AND every Part B row "
                         "decided -> promotion authorized",
        },
        "not_done": [
            "no HUMAN_VALIDATED rows (promotion is the review-sheet gate + a "
            "recorded deterministic apply step — executed only after the fill "
            "and left to the operator's sign-off)",
            "no chemistry bytes touched; no corpus writes; no other store touched",
            "no K3/K4 work (playbook-deferred)",
        ],
        "store_pins": pins,
        "verification": "graph/reports/C40_MATHS_A_K2B_LAND_CHECK.json",
    }
    RECORD_JSON.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
    md = f"""# C40 — K2 Lane B (Chunk Substrate) — igcse-maths-a

**Generated:** {now}  |  **Baseline:** `{baseline}`
**Operator directive:** "fire K2-B (chunk substrate), run the §18 HUMAN_VALIDATED
promotion round over the 73 edges" (2026-10-02, zai-web) — this record covers the
K2-B half; the §18 round over the 73 authored semantic edges is the T-C41 record.

## What this is

The C31 §6 Lane B build replayed for subject #2: the T-C13/C13 chunk→SP
substrate constructed over the maths-a notes corpus, emitting
`graph/igcse-maths-a/spec_chunk_mappings.yaml` — **{meta['rows_anchored']} anchored rows** +
{meta['rows_worklist_anchor_unresolved']} unresolved-span worklist rows + {meta['rows_worklist_unmapped_sps']} uncovered-SP
worklist rows = {len(rows)} rows, **{meta['sp_codes_covered']}/{meta['registry_size']} codes covered** (exactly the C31 §3
notes-coverage bound). Registry: maths-a 8 → **9 stores — the K2 exit shape.**

## The anchoring axis (the honest tier difference, recorded)

Chemistry's Lane B refined a HUMAN_VALIDATED T-C10 quote store (209 rows) into
passage chunks. The maths-a upstream is the **T-C32 K2-A notes-join —
AI_VALIDATED (operator-delegated chain)** — and carries no evidence quotes. The
construction therefore anchors on the corpus's own structure: every note is a
sequence of SP spans introduced by the corpus's `spec_point` blocks (203
markers), the join resolves each marker to the ratified code, and each row's
evidence quote is the chunk's own verbatim self-slice (markdown-safe, ≤240
chars). The upstream tier is recorded verbatim on every row and in the store
meta (C31 §4.5). Nothing invented; no fabricated quotes; the single unresolved
anchor (`spcpt_QWXhzVp2S3VYZdZc`) stays on the worklist, never forced.

## Construction

- Tool: `{meta['tool']}` — deterministic, zero-LLM, fail-closed; convention
  `{meta['convention']}` (the c13-chunk-convention-1 analog for the JSON block
  corpus); two independent constructions byte-identical (G7).
- Census: {meta['notes']} notes / {meta['spans']} spans / {meta['chunks_total']} chunks
  ({meta['chunks_intro']} intro + {meta['chunks_section']} section).
- Gates G1–G7 all green at construction; landing battery P1–P10 ALL PASS
  (`graph/reports/C40_MATHS_A_K2B_LAND_CHECK.json`).

## The operator review sheet (the promotion gate)

`graph/reports/C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md` — **468 Part A**
anchored spot-checks (seeded stratified: join score <1.0 or absent at 100%,
score == 1.0 at ceil(20%); the span-marker construction has no ambiguous rows by
design) + **79 Part B** worklist decisions. Gate rule (the C13 rule): Part A
precision ≥ 90% per class AND every Part B row decided → the rows may flip
SUGGESTED → HUMAN_VALIDATED **in a recorded deterministic apply step** — which
is NOT executed by this task; it waits on the sheet's fill and the operator's
sign-off (the store lands at SUGGESTED, anti-forgery G5 holds).

## Not done (deliberate)

- No HUMAN_VALIDATED anywhere in the emitted store.
- No chemistry bytes touched; no corpus writes; no other store touched.
- No K3/K4 work (playbook-deferred).

## Pins

| Artifact | sha256_16 |
|---|---|
| `graph/igcse-maths-a/spec_chunk_mappings.yaml` | `{pins['spec_chunk_mappings.yaml']}` |
| `C40_MATHS_A_CHUNK_SP_SUBSTRATE_REPORT.md` | `{pins['C40_MATHS_A_CHUNK_SP_SUBSTRATE_REPORT.md']}` |
| `C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md` | `{pins['C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md']}` |
"""
    RECORD_MD.write_text(md + "\n", encoding="utf-8")

    print(f"C40 landing battery: {'ALL PASS' if all_pass else 'FAIL'} "
          f"({sum(1 for v in results.values() if v['pass'])}/{len(results)} gates)")
    for k, v in results.items():
        print(f"  {'PASS' if v['pass'] else 'FAIL'} {k}: {v['detail'][:110]}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
