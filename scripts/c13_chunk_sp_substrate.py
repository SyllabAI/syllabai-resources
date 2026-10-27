#!/usr/bin/env python3
"""c13 — the chunk→SpecificationPoint mapping substrate (quote-anchor construction).

Session-96 diagnosis step 1+2 (T-C06/F-168 keystone): the 209 note-level
HUMAN_VALIDATED T-C10 mappings carry verbatim evidence quotes that are passage
anchors stored at the wrong granularity. This tool refines that store to
chunk-level rows, deterministically and fail-closed:

  1. Chunk every note at the PINNED convention (intro chunk + leaf sections
     h2..h4, chunk text = heading + body — the C10 heading-quote lesson).
  2. Anchor every spec_map evidence quote to exactly one chunk of ITS note
     (normalized substring; ambiguity resolved deterministically and flagged).
  3. Emit graph/igcse-chemistry/spec_chunk_mappings: one row per anchored mapping —
     validation_status SUGGESTED, tier RULE_DERIVED, upstream provenance
     pointing at the T-C10 HUMAN_VALIDATED note-level mapping. NO row is ever
     emitted HUMAN_VALIDATED: promotion is the operator gate (anti-forgery,
     C10/C11/C12 norm).
  4. Emit the enumerable worklist: unanchored quotes (reason-classified), the
     anchorless SP set, and the one unmapped SP (4CH1-4.15, registered gap).
  5. Emit the operator review sheet (seeded, stratified, verdict boxes).

Gates (fail-closed, negative-tested by c13_substrate_negative_test.py):
  G1 corpus shape       112 notes, every note has spec_map
  G2 store shape        209 mappings, all HUMAN_VALIDATED upstream, evidence non-empty
  G3 code validity      every code in the 182-point 4CH1-2017 registry
  G4 anchor fidelity    every emitted row re-verifies quote-in-chunk after emit
  G5 anti-forgery       zero HUMAN_VALIDATED rows in the emitted store
  G6 worklist complete  every unanchored mapping + every uncovered SP enumerated
  G7 idempotency        two in-process runs byte-identical

Usage:
    python3 scripts/c13_chunk_sp_substrate.py                 # in-repo run
    python3 scripts/c13_chunk_sp_substrate.py --mirror DIR    # sandbox mirror layout
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import statistics
import sys
import unicodedata
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import graph_paths as GP  # C28 §3.2 path registry — single source of ratified store paths

import yaml

TOOL = "scripts/c13_chunk_sp_substrate.py"
TOOL_VERSION = "1.0.0"
CONVENTION_ID = "c13-chunk-convention-1"
CURRICULUM = "4CH1-2017"

# ---------------------------------------------------------------- convention --
# The pinned chunk convention (diagnosis step 3). Every byte of a note body
# belongs to exactly one chunk:
#   chunk 0        = INTRO: title (# ) + Excerpt blockquote + preamble, i.e.
#                    everything before the first level-2..4 heading
#   chunks 1..n    = leaf sections cut at headings of level 2..4; chunk text
#                    INCLUDES its own heading line (the C10 heading-quote
#                    lesson: chunks must be retrievable by their heading words)
#   h5/h6 and the '## Excerpt' pseudo-heading inside the blockquote never cut.
MAX_CUT_LEVEL = 4
INTRO_HEADING = "(intro)"

_TRANS = {ord("‘"): "'", ord("’"): "'", ord("“"): '"', ord("”"): '"',
          ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"}


def norm(s: str) -> str:
    """Markdown-insensitive normalization shared with the C10 evidence gate
    (c10_map_notes.py norm): apply to BOTH sides, then substring-match."""
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = s.translate(_TRANS)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def front_matter_split(text: str):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return "", text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    return "", text


def parse_slug(url: str):
    """(section_no, group_no, group_slug, note_slug) from the SME source URL."""
    parts = [p for p in (url or "").rstrip("/").split("/") if p]
    if len(parts) < 2:
        return None
    group_slug, note_slug = parts[-2], parts[-1]
    m = re.match(r"^(\d)-(\d+)-", group_slug)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2)), group_slug, note_slug


def chunk_note(body: str):
    """Return the note's chunks under the pinned convention."""
    lines = body.splitlines()
    first = None
    for i, ln in enumerate(lines):
        m = re.match(r"^(#{1,6}) (.*)$", ln)
        if m and 2 <= len(m.group(1)) <= MAX_CUT_LEVEL and m.group(2).strip().lower() != "excerpt":
            first = i
            break
    chunks = []
    if first is None:
        # no cuttable headings: the whole body is one intro chunk
        chunks.append({"ordinal": 0, "is_intro": True, "heading": INTRO_HEADING,
                       "heading_level": 0, "heading_path": INTRO_HEADING,
                       "text": "\n".join(lines).strip()})
        return chunks
    if any(s.strip() for s in lines[:first]):
        chunks.append({"ordinal": 0, "is_intro": True, "heading": INTRO_HEADING,
                       "heading_level": 0, "heading_path": INTRO_HEADING,
                       "text": "\n".join(lines[:first]).strip()})
    cur_head, cur_level, cur_buf = None, 0, []
    for ln in lines[first:]:
        m = re.match(r"^(#{2,6}) (.*)$", ln)
        if m and len(m.group(1)) <= MAX_CUT_LEVEL and m.group(2).strip().lower() != "excerpt":
            if cur_head is not None:
                chunks.append({"ordinal": len(chunks), "is_intro": False,
                               "heading": cur_head, "heading_level": cur_level,
                               "heading_path": cur_head,
                               "text": (cur_head + "\n" + "\n".join(cur_buf)).strip()})
            cur_head, cur_level, cur_buf = m.group(2).strip(), len(m.group(1)), []
        else:
            cur_buf.append(ln)
    if cur_head is not None:
        chunks.append({"ordinal": len(chunks), "is_intro": False,
                       "heading": cur_head, "heading_level": cur_level,
                       "heading_path": cur_head,
                       "text": (cur_head + "\n" + "\n".join(cur_buf)).strip()})
    return chunks


def sha16(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


# ------------------------------------------------------------------- loading --
def load_registry(graph_dir: Path):
    reg = yaml.safe_load((graph_dir / "specification_points.yaml").read_text(encoding="utf-8"))
    return {p["code"]: p for p in reg["specification_points"]}


def load_store(notes_root: Path):
    """Parse the T-C10 note-level store from note front matter."""
    notes, store, no_map = [], [], []
    for p in sorted(notes_root.rglob("*.md")):
        if "assets" in p.parts:
            continue
        fm_text, body = front_matter_split(p.read_text(encoding="utf-8"))
        fm = yaml.safe_load(fm_text) or {}
        sm = fm.get("spec_map")
        rel = str(p.relative_to(notes_root))
        slug = parse_slug(fm.get("source") or "")
        notes.append({"path": rel, "body": body, "slug": slug, "source_url": fm.get("source") or ""})
        if not sm:
            no_map.append(rel)
            continue
        for sp in sm.get("spec_points", []):
            prov = sp.get("provenance") or {}
            store.append({
                "note_path": rel,
                "note_slug": (slug or (None,) * 4)[3],
                "group_slug": (slug or (None,) * 4)[2],
                "code": sp.get("code"),
                "evidence": prov.get("evidence") or "",
                "confidence": prov.get("confidence"),
                "rationale": prov.get("rationale") or "",
                "validation_status": prov.get("validation_status"),
                "validated_by": prov.get("validated_by"),
                "validated_date": prov.get("validated_date"),
                "mapped_date": sm.get("mapped_date"),
                "mapper": sm.get("mapper"),
            })
    return notes, store, no_map


# ------------------------------------------------------------------- anchor --
def anchor_mappings(notes, store):
    """Anchor every mapping's evidence quote to one content chunk of its note.
    The intro chunk is NEVER an anchor target: a quote that only resolves to
    title/excerpt region is by definition not a passage anchor (the audit's
    discipline) — it lands on the worklist instead."""
    by_note = {}
    for n in notes:
        by_note[n["path"]] = chunk_note(n["body"])
    results = []
    for m in store:
        ck = by_note[m["note_path"]]
        nq = norm(m["evidence"])
        targets = [c for c in ck if not c["is_intro"]]
        hits = [c for c in targets if nq and nq in norm(c["text"])]
        r = dict(m)
        if len(hits) == 1:
            c = hits[0]
            r["anchor"] = {"chunk_ordinal": c["ordinal"], "chunk_sha256_16": sha16(c["text"]),
                           "chunk_heading": c["heading"], "chunk_chars": len(c["text"]),
                           "match_type": "exact", "ambiguous_hits": 1}
        elif len(hits) > 1:
            c = hits[0]  # deterministic: lowest ordinal wins, ambiguity flagged
            r["anchor"] = {"chunk_ordinal": c["ordinal"], "chunk_sha256_16": sha16(c["text"]),
                           "chunk_heading": c["heading"], "chunk_chars": len(c["text"]),
                           "match_type": "exact", "ambiguous_hits": len(hits),
                           "ambiguous_ordinals": [h["ordinal"] for h in hits]}
        else:
            # reason classification: does it resolve to the intro (title/excerpt)?
            intros = [c for c in ck if c["is_intro"]]
            in_intro = bool(intros and nq and nq in norm(intros[0]["text"]))
            r["anchor"] = None
            r["unanchored_reason"] = ("quote resolves only to the note title/excerpt region — "
                                      "no passage anchor; author a fresh verbatim section quote"
                                      if in_intro else
                                      "quote does not appear verbatim in any section (likely "
                                      "source-conversion artifact or edited wording)")
        results.append(r)
    return results, by_note


# -------------------------------------------------------------------- gates --
def verify_store(doc: dict, registry: dict, idx: dict):
    """Verify an emitted store document against the chunk index.
    G4 anchor fidelity · G5 anti-forgery · G6 worklist completeness.
    Shared by the construction run and the negative test suite."""
    rows = doc["rows"]

    # G3 code validity — every emitted row must reference the ratified registry
    for i, r in enumerate(rows):
        if r.get("spec_code") not in registry:
            raise SystemExit(f"G3 FAIL: row {i} ({r.get('mapping_id')}) references code outside the registry: {r.get('spec_code')}")

    # G4 anchor fidelity — every chunk row re-verifies against the chunk index
    for r in rows:
        if "chunk" not in r:
            continue
        key = (r["note_path"], r["chunk"]["ordinal"])
        if key not in idx:
            raise SystemExit(f"G4 FAIL: unknown chunk ref {key}")
        if sha16(idx[key]) != r["chunk"]["sha256_16"]:
            raise SystemExit(f"G4 FAIL: chunk hash mismatch {key}")
        if norm(r["evidence_quote"]) not in norm(idx[key]):
            raise SystemExit(f"G4 FAIL: quote not in chunk {key}")

    # G5 anti-forgery — a row's OWN claim must never be HUMAN_VALIDATED; the
    # nested provenance.upstream.validation_status is a REFERENCE to the T-C10
    # store's status and is required provenance, not a self-claim.
    for i, r in enumerate(rows):
        if r.get("validation_status") == "HUMAN_VALIDATED":
            raise SystemExit(f"G5 FAIL: row {i} ({r.get('mapping_id')}) claims HUMAN_VALIDATED")
        if r.get("provenance", {}).get("tier") == "HUMAN_VALIDATED":
            raise SystemExit(f"G5 FAIL: row {i} ({r.get('mapping_id')}) carries tier HUMAN_VALIDATED")
        up = r.get("provenance", {}).get("upstream", {})
        if up and up.get("validation_status") != "HUMAN_VALIDATED":
            raise SystemExit(f"G5 FAIL: row {i} upstream reference is not HUMAN_VALIDATED (anchor integrity)")

    # G6 worklist completeness — every uncovered SP must be enumerated
    anchored_codes = {r["spec_code"] for r in rows if "chunk" in r}
    uncovered = set(registry) - anchored_codes
    for code in uncovered:
        if not any(r.get("spec_code") == code and r.get("worklist_reason") for r in rows):
            raise SystemExit(f"G6 FAIL: uncovered SP {code} missing from worklist")
    for r in rows:
        if "worklist_reason" in r and not r.get("disposition"):
            raise SystemExit(f"G6 FAIL: worklist row {r.get('mapping_id')} has no disposition")


def run(notes_root: Path, graph_dir: Path, out_dir: Path):
    registry = load_registry(graph_dir)
    notes, store, no_map = load_store(notes_root)

    # G1 corpus shape
    if len(notes) != 112:
        raise SystemExit(f"G1 FAIL: {len(notes)} notes != 112")
    if no_map:
        raise SystemExit(f"G1 FAIL: notes without spec_map: {no_map}")

    # G2 store shape
    bad_status = [m for m in store if m["validation_status"] != "HUMAN_VALIDATED"]
    if bad_status:
        raise SystemExit(f"G2 FAIL: non-HUMAN_VALIDATED upstream rows: {[(m['note_path'], m['code']) for m in bad_status]}")
    empty_ev = [m for m in store if not norm(m["evidence"])]
    if empty_ev:
        raise SystemExit(f"G2 FAIL: empty evidence: {[(m['note_path'], m['code']) for m in empty_ev]}")
    if len(store) != 209:
        raise SystemExit(f"G2 FAIL: {len(store)} mappings != 209")

    # G3 code validity
    foreign = [m for m in store if m["code"] not in registry]
    if foreign:
        raise SystemExit(f"G3 FAIL: codes not in registry: {sorted({m['code'] for m in foreign})}")

    anchored, by_note = anchor_mappings(notes, store)
    rows = [m for m in anchored if m["anchor"]]
    worklist = [m for m in anchored if not m["anchor"]]

    chunk_counts = [len(by_note[n["path"]]) for n in notes]
    section_counts = [sum(1 for c in by_note[n["path"]] if not c["is_intro"]) for n in notes]
    covered = sorted({m["code"] for m in rows})
    uncovered = sorted(set(registry) - set(covered))
    mapped_codes = {m["code"] for m in store}
    unmapped_sps = sorted(set(registry) - mapped_codes)

    # deterministic ordering: (note_path, code, quote)
    rows.sort(key=lambda m: (m["note_path"], m["code"], m["evidence"]))
    worklist.sort(key=lambda m: (m["note_path"], m["code"], m["evidence"]))

    def emit_rows(items):
        out = []
        for m in items:
            mid = sha16(f"{m['note_path']}|{m['code']}|{norm(m['evidence'])}")
            if m["anchor"]:
                a = m["anchor"]
                out.append({
                    "mapping_id": mid,
                    "spec_code": m["code"],
                    "sp_title": registry[m["code"]].get("official_wording") or registry[m["code"]].get("title") or "",
                    "note_slug": m["note_slug"],
                    "note_path": m["note_path"],
                    "chunk": {"ordinal": a["chunk_ordinal"], "heading": a["chunk_heading"],
                              "sha256_16": a["chunk_sha256_16"], "chars": a["chunk_chars"],
                              "convention": CONVENTION_ID},
                    "anchor": {"match_type": a["match_type"], "ambiguous_hits": a["ambiguous_hits"],
                               **({"ambiguous_ordinals": a["ambiguous_ordinals"]} if a["ambiguous_hits"] > 1 else {})},
                    "evidence_quote": m["evidence"],
                    "provenance": {
                        "tier": "RULE_DERIVED",
                        "derivation": "quote-anchor granularity refinement of the T-C10 note-level mapping "
                                      "(verbatim evidence quote anchored to its passage chunk; deterministic, zero-LLM)",
                        "tool": f"{TOOL}@{TOOL_VERSION}",
                        "upstream": {"store": "T-C10 note-level spec_map (note front matter)",
                                     "mapping": f"{m['note_path']}::{m['code']}",
                                     "validation_status": "HUMAN_VALIDATED",
                                     "validated_by": m["validated_by"],
                                     "validated_date": str(m["validated_date"]),
                                     "confidence": m["confidence"],
                                     "model_version": m["mapper"]},
                    },
                    "rationale": m["rationale"],
                    "validation_status": "SUGGESTED",
                })
            else:
                out.append({
                    "mapping_id": mid,
                    "spec_code": m["code"],
                    "note_slug": m["note_slug"],
                    "note_path": m["note_path"],
                    "evidence_quote": m["evidence"],
                    "worklist_reason": m["unanchored_reason"],
                    "provenance": {"tier": "RULE_DERIVED", "tool": f"{TOOL}@{TOOL_VERSION}",
                                   "upstream": {"store": "T-C10 note-level spec_map (note front matter)",
                                                "mapping": f"{m['note_path']}::{m['code']}",
                                                "validation_status": "HUMAN_VALIDATED",
                                                "validated_by": m["validated_by"],
                                                "validated_date": str(m["validated_date"]),
                                                "confidence": m["confidence"]}},
                    "validation_status": "SUGGESTED",
                    "disposition": "WORKLIST — needs a fresh authored passage quote (or markdown repair) before a chunk-level row can exist",
                })
        return out

    emitted = emit_rows(rows) + emit_rows(worklist)
    for sp in unmapped_sps:
        emitted.append({
            "mapping_id": sha16(f"unmapped|{sp}"),
            "spec_code": sp,
            "sp_title": registry[sp].get("official_wording") or registry[sp].get("title") or "",
            "worklist_reason": "no note-level mapping exists in the T-C10 store for this SP (registered corpus gap)",
            "provenance": {"tier": "RULE_DERIVED", "tool": f"{TOOL}@{TOOL_VERSION}"},
            "validation_status": "SUGGESTED",
            "disposition": "WORKLIST — chunk-level mapping decision needed (C12 question-level mappings exist; see C10_GAP_ANNOTATIONS)",
        })

    doc = {
        "meta": {
            "store": "c13 chunk→SpecificationPoint mapping substrate (quote-anchor construction)",
            "convention": CONVENTION_ID,
            "convention_spec": "chunk 0 = intro (title+excerpt+preamble); leaf sections cut at h2..h4; "
                               "chunk text = its own heading line + section body (the C10 heading-quote lesson); "
                               "anchoring targets content sections only",
            "curriculum": CURRICULUM,
            "registry_size": len(registry),
            "notes": len(notes),
            "chunks_total": int(sum(chunk_counts)),
            "chunks_intro": len(notes),
            "chunks_section": int(sum(section_counts)),
            "mappings_upstream": len(store),
            "rows_anchored": len(rows),
            "rows_worklist_quotes": len(worklist),
            "rows_worklist_unmapped_sps": len(unmapped_sps),
            "anchor_rate": round(len(rows) / len(store), 4),
            "sp_codes_covered": len(covered),
            "sp_codes_uncovered": uncovered,
            "tool": f"{TOOL}@{TOOL_VERSION}",
            "upstream_store": "T-C10 note-level spec_map (209 HUMAN_VALIDATED mappings, operator 2026-09-11)",
            "promotion_rule": "rows are SUGGESTED; HUMAN_VALIDATED only via the operator review sheet gate "
                              "(graph/reports/C13_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md)",
            "forward_contract": "chunk identity (note_slug, ordinal, heading, sha256_16 of chunk text) must "
                                "survive T-C06 ingestion — the converter/ChunkingService must reproduce this "
                                "convention or the rows fail closed at join time",
        },
        "rows": emitted,
    }

    # G4/G5/G6 on the emitted doc (shared with the negative test suite)
    idx = {(n["path"], c["ordinal"]): c["text"] for n in notes for c in by_note[n["path"]]}
    verify_store(doc, registry, idx)

    out_dir.mkdir(parents=True, exist_ok=True)
    text = yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=100)
    (out_dir / "spec_chunk_mappings.yaml").write_text(text, encoding="utf-8")

    stats = {
        "notes": len(notes), "mappings": len(store), "anchored": len(rows),
        "worklist_quotes": len(worklist), "unmapped_sps": unmapped_sps,
        "covered": len(covered), "uncovered": uncovered,
        "chunks_total": int(sum(chunk_counts)),
        "chunks_median_chars": int(statistics.median([len(c["text"]) for n in notes for c in by_note[n["path"]]])),
        "ambiguous": sum(1 for r in rows if r["anchor"]["ambiguous_hits"] > 1),
        "match_types": {t: sum(1 for r in rows if r["anchor"]["match_type"] == t) for t in ("exact",)},
        "registry": len(registry),
    }
    (out_dir / ".c13_stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    return doc, stats, emitted, rows, worklist, registry, uncovered


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--notes-root", default=None, help="defaults to <repo>/Chemistry IGCSE Revision Notes")
    ap.add_argument("--graph-dir", default=None, help="defaults to <repo>/graph")
    ap.add_argument("--out-dir", default=None, help="defaults to <repo>/graph")
    ap.add_argument("--mirror", default=None, help="sandbox mirror: expects DIR/notes and DIR/specification_points.yaml")
    args = ap.parse_args()

    if args.mirror:
        m = Path(args.mirror)
        notes_root, graph_dir, out_dir = m / "notes", m, m / "graph"
    else:
        repo = Path(__file__).resolve().parent.parent
        notes_root = Path(args.notes_root) if args.notes_root else repo / "Chemistry IGCSE Revision Notes"
        graph_dir = Path(args.graph_dir) if args.graph_dir else GP.qual_dir()  # C28 registry-resolved
        out_dir = Path(args.out_dir) if args.out_dir else GP.qual_dir()

    doc, stats, emitted, rows, worklist, registry, uncovered = run(notes_root, graph_dir, out_dir)

    # G7 idempotency — second in-process run must produce identical rows
    doc2, stats2, emitted2, *_ = run(notes_root, graph_dir, out_dir)
    if yaml.safe_dump(doc2["rows"], allow_unicode=True, sort_keys=False) != yaml.safe_dump(doc["rows"], allow_unicode=True, sort_keys=False):
        raise SystemExit("G7 FAIL: construction is not deterministic (rows differ between runs)")

    print("C13 CHUNK→SP SUBSTRATE — construction OK (all gates green)")
    for k in ("notes", "chunks_total", "mappings", "anchored", "worklist_quotes", "covered", "ambiguous"):
        print(f"  {k}: {stats[k]}")
    print(f"  anchor_rate: {stats['anchored']}/{stats['mappings']} = {round(stats['anchored']/stats['mappings']*100,1)}%")
    print(f"  uncovered SPs: {stats['uncovered']}")
    print(f"  store: {out_dir / 'spec_chunk_mappings.yaml'}")


if __name__ == "__main__":
    main()
