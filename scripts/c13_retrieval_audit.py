#!/usr/bin/env python3
"""Session 77 — Track 3 (T-C13): corpus + mapping audit.

Quantifies the retrieval-relevant data that actually exists, answering the
operator's question: WHY is SpecificationPoint-aware retrieval failing, and
what does the zero chunk->SpecificationPoint mapping coverage actually mean
in numbers?

Audited facts:
  1. the notes corpus (112 SME notes) and their T-C10 spec_map front-matter
     (note-level mappings, validation statuses, evidence quotes);
  2. the heading-level chunking of every note (the retrieval corpus shape);
  3. whether each mapping's verbatim evidence quote can be LOCATED in a
     specific chunk (the derivable chunk-level anchor — the C10 quotes are
     passage anchors stored at note granularity);
  4. the fan-out structure: SPs per note, notes per SP, chunks per note,
     inherited chunks per SP (what note-level mapping implies at chunk
     granularity — the precision collapse);
  5. SP coverage: which of the 182 registry points have >=1 mapped note
     (HUMAN_VALIDATED vs AI_SUGGESTED), and which have NONE.

Output: scripts/s77/out/retrieval_audit.json + a printed summary.
"""
from __future__ import annotations

import json
import os
import re
import statistics
import sys
from collections import defaultdict

import yaml

NOTES_ROOT = ("/home/z/my-project/work/syllabai-resources/"
              "Chemistry IGCSE Revision Notes")
SPEC_YAML = "/home/z/my-project/work/syllabai-resources/graph/specification_points.yaml"
OUT = os.environ.get("C13_OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "graph", "reports", "C13_RETRIEVAL_AUDIT.json"))

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def parse_note(path):
    """Split a note into front-matter + heading-path chunks."""
    text = open(path, encoding="utf-8").read()
    fm = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            try:
                fm = yaml.safe_load(parts[1]) or {}
                body = parts[2]
            except yaml.YAMLError:
                pass
    chunks = []
    stack = []  # (level, title)
    current_lines = []
    current_path = []

    def flush():
        content = "\n".join(current_lines).strip()
        if content:
            # chunk text includes its own heading title: a chunk must be
            # retrievable by the words in its heading (BM25 reality) — and
            # several C10 evidence quotes ARE heading titles
            chunks.append({"heading_path": " > ".join(current_path),
                           "content": (current_path[-1] + "\n" if current_path else "") + content})

    for line in body.splitlines():
        m = HEADING_RE.match(line)
        if m:
            flush()
            level = len(m.group(1))
            title = m.group(2).strip()
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, title))
            current_path = [t for _, t in stack]
            current_lines = []
        else:
            current_lines.append(line)
    flush()
    return fm, chunks


def norm(s):
    """Normalize for quote location: collapse whitespace AND strip inline
    markdown emphasis/escapes — the C10 evidence quotes are verbatim against
    the SOURCE text, but the notes' markdown wraps phrases in **bold**,
    _italics_, \\[escapes\\] and $LaTeX$, which breaks naive containment
    (the 84-quote lesson: format-insensitive matching is REQUIRED)."""
    s = (s or "").lower()
    s = s.replace("\\[", "[").replace("\\]", "]").replace("\\(", "(").replace("\\)", ")")
    s = re.sub(r"[*_`~$#]+", " ", s)
    s = re.sub(r"https?://\S+", " ", s)      # URLs glued into prose
    s = re.sub(r"\|", " ", s)                 # table cell separators
    s = re.sub(r"[\]\[()]+", " ", s)          # stray link/markup brackets
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def locate_quote(quote, chunks):
    """Find the chunk whose content contains the (normalized) evidence
    quote. Returns (index, exact) — exact=True when the quote matches a
    single chunk verbatim (whitespace-normalized)."""
    q = norm(quote)
    if not q:
        return None, False
    hits = []
    for i, c in enumerate(chunks):
        if q in norm(c["content"]):
            hits.append(i)
    if len(hits) == 1:
        return hits[0], True
    if hits:
        # quote spans multiple chunks (split across a heading) — first hit
        return hits[0], False
    # try a prefix (quotes sometimes truncated with ellipses)
    prefix = q[: min(60, len(q))]
    if prefix:
        for i, c in enumerate(chunks):
            if prefix in norm(c["content"]):
                return i, False
    return None, False


def main() -> int:
    registry = yaml.safe_load(open(SPEC_YAML))["specification_points"]
    reg_codes = {p["code"] for p in registry}

    notes = []
    for dirpath, _, files in os.walk(NOTES_ROOT):
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            fm, chunks = parse_note(path)
            sm = fm.get("spec_map") or {}
            points = []
            for sp in (sm.get("spec_points") or []):
                points.append({
                    "code": sp.get("code"),
                    "validation": (sp.get("provenance") or {}).get(
                        "validation_status"),
                    "evidence": (sp.get("provenance") or {}).get("evidence"),
                    "confidence": (sp.get("provenance") or {}).get("confidence"),
                })
            notes.append({
                "path": os.path.relpath(path, NOTES_ROOT),
                "subsection": sm.get("subsection"),
                "points": points,
                "chunks": chunks,
            })
    by_path = {n["path"]: n for n in notes}

    # ---- aggregate facts -------------------------------------------------
    total_notes = len(notes)
    total_chunks = sum(len(n["chunks"]) for n in notes)
    mappings = [(n, p) for n in notes for p in n["points"]]
    hv = [(n, p) for n, p in mappings if p["validation"] == "HUMAN_VALIDATED"]
    other = [(n, p) for n, p in mappings if p["validation"] != "HUMAN_VALIDATED"]

    sps_per_note = defaultdict(set)
    notes_per_sp = defaultdict(set)
    for n, p in mappings:
        sps_per_note[n["path"]].add(p["code"])
        notes_per_sp[p["code"]].add(n["path"])

    # chunk-level: what the CURRENT data implies
    quote_anchor = {"exact": 0, "fuzzy": 0, "missing": 0, "empty_quote": 0}
    anchored_pairs = 0
    hv_anchored = 0
    derived = defaultdict(set)   # sp -> {(note_path, chunk_index)}
    for n, p in mappings:
        if not (p.get("evidence") or "").strip():
            quote_anchor["empty_quote"] += 1
            continue
        idx, exact = locate_quote(p["evidence"], n["chunks"])
        if idx is None:
            quote_anchor["missing"] += 1
        else:
            if exact:
                quote_anchor["exact"] += 1
            else:
                quote_anchor["fuzzy"] += 1
            anchored_pairs += 1
            derived[p["code"]].add((n["path"], idx))
            if p["validation"] == "HUMAN_VALIDATED":
                hv_anchored += 1

    # inherited chunk fan-out: SP -> all chunks of all mapped notes
    inherited_chunks_per_sp = {
        sp: sum(len(by_path[pth]["chunks"]) for pth in paths)
        for sp, paths in notes_per_sp.items()
    }

    # coverage vs the registry (HUMAN_VALIDATED-only view)
    hv_sps = {p["code"] for n in notes for p in n["points"]
              if p["validation"] == "HUMAN_VALIDATED"}
    covered_any = set(notes_per_sp.keys())
    chunk_direct = 0  # no chunk->SP store exists anywhere

    report = {
        "corpus": {
            "notes": total_notes,
            "chunks_heading_level": total_chunks,
            "avg_chunks_per_note": round(total_chunks / total_notes, 2),
            "chunk_chars_p50": None,
        },
        "mappings": {
            "note_level_total": len(mappings),
            "human_validated": len(hv),
            "not_validated": len(other),
            "distinct_sps_mapped_any_status": len(covered_any),
            "distinct_sps_hv": len(hv_sps),
            "registry_sps": len(reg_codes),
            "sps_with_no_note_mapping": sorted(reg_codes - covered_any),
            "sps_per_note_p50": None,
            "notes_per_sp_distribution": None,
        },
        "chunk_level": {
            "direct_chunk_to_sp_rows_in_any_store": chunk_direct,
            "direct_coverage_fraction": 0.0,
            "evidence_quote_anchors": quote_anchor,
            "derived_anchor_pairs": anchored_pairs,
            "derived_hv_pairs": hv_anchored,
            "derived_sps_covered": len(derived),
        },
        "fanout": {"inherited_chunks_per_sp": {}},
        "per_sp": [],
    }

    spn = sorted(len(v) for v in sps_per_note.values())
    report["mappings"]["sps_per_note_p50"] = spn[len(spn)//2] if spn else 0
    nps = sorted(len(v) for v in notes_per_sp.values())
    dist = defaultdict(int)
    for v in nps:
        dist[v] += 1
    report["mappings"]["notes_per_sp_distribution"] = dict(sorted(dist.items()))
    inh = sorted(inherited_chunks_per_sp.values())
    report["fanout"]["inherited_chunks_per_sp"] = {
        "mean": round(sum(inh)/len(inh), 2) if inh else 0,
        "p50": inh[len(inh)//2] if inh else 0,
        "max": inh[-1] if inh else 0,
    }
    chars = sorted(len(c["content"]) for n in notes for c in n["chunks"])
    report["corpus"]["chunk_chars_p50"] = chars[len(chars)//2] if chars else 0

    for p in registry:
        sp = p["code"]
        detail = {
            "code": sp,
            "wording": (p.get("official_wording") or "")[:120],
            "hv": sp in hv_sps,
            "notes_mapped": len(notes_per_sp.get(sp, ())),
            "inherited_chunks": inherited_chunks_per_sp.get(sp, 0),
            "derived_anchor_chunks": len(derived.get(sp, ())),
        }
        report["per_sp"].append(detail)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(report, f, indent=1, sort_keys=True)

    print(f"notes: {total_notes}, chunks: {total_chunks}")
    print(f"note-level mappings: {len(mappings)} "
          f"(HUMAN_VALIDATED {len(hv)}, other {len(other)})")
    print(f"distinct SPs mapped: {len(covered_any)}/{len(reg_codes)} "
          f"(HV {len(hv_sps)}); unmapped: {len(reg_codes - covered_any)}")
    print(f"evidence-quote anchors: {quote_anchor}")
    print(f"derived chunk-level pairs: {anchored_pairs} (HV {hv_anchored}) "
          f"over {len(derived)} SPs")
    print(f"inherited chunks/SP: {report['fanout']['inherited_chunks_per_sp']}")
    print(f"DIRECT chunk->SP rows in any store: {chunk_direct}")
    print(f"written {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
