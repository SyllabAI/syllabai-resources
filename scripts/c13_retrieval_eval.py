#!/usr/bin/env python3
"""Session 77 — Track 3 (T-C13): the retrieval evaluation harness.

Answers the operator's reframed question — not "can BM25 run?" (settled: it
can) but "why is SpecificationPoint-aware retrieval failing, and what data
construction is necessary before retrieval can be promoted?"

Providers evaluated over the real corpus (112 SME notes -> 732 heading-level
chunks, T-C10 note-level HUMAN_VALIDATED mappings, C10 evidence quotes):

  P1  bm25            — pure lexical ranking over chunks (the baseline).
  P2  sp-note-route   — the ONLY SpecificationPoint-aware path the current
                        data supports: resolve the query to an SP, then
                        return ALL chunks of ALL notes mapped to that SP
                        (note-level inheritance — no chunk-level signal
                        exists, so nothing can be ranked or filtered).
  P3  sp-anchor-route — the data-construction PREVIEW: the same routing but
                        restricted to the quote-anchored chunks derivable
                        from the C10 evidence quotes (what chunk-level
                        mapping construction would give, before any new
                        authoring).

Query families:
  Q1  sp-wording   — the official wording of each of the 182 registry points
                     (the canonical "what the spec demands" query; the gold
                     SP is the query's own identity — used to measure the
                     CONNECT step, with the note-level gold caveat recorded).
  Q2  real-questions — 5 real questions with HUMAN_VALIDATED SP golds: the
                     4 C12 operator-ratified smoke questions + the session-77
                     pilot learner's live tutor question (KG-cited 1.42/1.43).

Honesty notes (recorded in the output):
  * the only gold available is NOTE-granularity (the T-C10 store) plus the
    derived anchors — there is NO chunk-level validated gold; every metric
    below is a diagnostic against that partial gold, not a fair quality
    score. That limitation IS the finding (the operator's confounder).
  * P2/P3 evaluated on Q1 use the gold SP as the route — i.e. they are
    credited with a perfect SP resolver. This is GENEROUS to the SP-aware
    path; its real-world numbers would be strictly worse.
"""
from __future__ import annotations

import json
import math
import os
import re
import sys
from collections import defaultdict

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from c13_retrieval_audit import NOTES_ROOT, SPEC_YAML, parse_note, norm  # noqa: E402
except ImportError:  # the session-77 sandbox layout
    from retrieval_audit import NOTES_ROOT, SPEC_YAML, parse_note, norm  # noqa: E402

OUT = os.environ.get("C13_OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "graph", "reports", "C13_RETRIEVAL_EVAL.json"))

# ---- Q2 real questions with HUMAN_VALIDATED golds --------------------------
REAL_QUERIES = [
    {"id": "c12-fractional-distillation",
     "text": ("Describe how the industrial process of fractional distillation "
              "separates crude oil into fractions, and state that crude oil "
              "is a mixture of hydrocarbons."),
     "gold_primary": "4CH1-4.8", "gold_secondary": ["4CH1-4.7"],
     "gold_source": "C12 operator ratification 2026-09-15"},
    {"id": "c12-ionic-conduction",
     "text": ("Explain why an ionic compound does not conduct electricity when "
              "solid, but does conduct electricity when molten and in aqueous "
              "solution, referring to its giant ionic lattice and high melting "
              "and boiling points."),
     "gold_primary": "4CH1-1.56C", "gold_secondary": ["4CH1-1.43"],
     "gold_source": "C12 operator ratification 2026-09-15"},
    {"id": "c12-acid-rain",
     "text": ("Explain how sulfur dioxide and oxides of nitrogen contribute "
              "to acid rain, including how nitrogen oxide forms in a car "
              "engine."),
     "gold_primary": "4CH1-4.16", "gold_secondary": ["4CH1-4.14"],
     "gold_source": "C12 operator ratification 2026-09-15 (amended)"},
    {"id": "c12-fuels-sulfur",
     "text": ("Some fuels contain sulfur impurities. State the consequence of "
              "burning sulfur-containing fuels and name the acidic gas "
              "produced."),
     "gold_primary": "4CH1-4.16", "gold_secondary": ["4CH1-4.15"],
     "gold_source": "C12 operator ratification 2026-09-15"},
    {"id": "pilot-tutor-ask",
     "text": ("My teacher said sodium chloride is a giant lattice of ions, but "
              "I thought it was made of separate NaCl molecules, one sodium "
              "ion bonded to one chloride ion. Why is sodium chloride a "
              "lattice and not molecules?"),
     "gold_primary": "4CH1-1.42", "gold_secondary": ["4CH1-1.43"],
     "gold_source": "session-77 pilot live tutor citations (KG-side)"},
]

TOKEN_RE = re.compile(r"[a-z0-9]+")


def tokens(s):
    return [t for t in TOKEN_RE.findall((s or "").lower()) if len(t) > 1]


# ---- BM25 ---------------------------------------------------------------
class BM25:
    def __init__(self, docs, k1=1.5, b=0.75):
        self.k1, self.b = k1, b
        self.docs = [tokens(d) for d in docs]
        self.N = len(self.docs)
        self.avgdl = sum(len(d) for d in self.docs) / max(1, self.N)
        self.tf = [defaultdict(int) for _ in self.docs]
        for i, doc in enumerate(self.docs):
            for t in doc:
                self.tf[i][t] += 1
        df = defaultdict(int)
        for doc in self.docs:
            for t in set(doc):
                df[t] += 1
        self.idf = {t: math.log(1 + (self.N - n + 0.5) / (n + 0.5))
                    for t, n in df.items()}

    def search(self, query, k=10):
        q = tokens(query)
        scores = []
        for i in range(self.N):
            s = 0.0
            for t in q:
                if t not in self.idf:
                    continue
                f = self.tf[i].get(t, 0)
                if not f:
                    continue
                dl = len(self.docs[i])
                s += self.idf[t] * f * (self.k1 + 1) / (
                    f + self.k1 * (1 - self.b + self.b * dl / self.avgdl))
            scores.append((s, i))
        scores.sort(key=lambda x: (-x[0], x[1]))
        return [(i, s) for s, i in scores[:k] if s > 0]


def main() -> int:
    # ---- corpus ---------------------------------------------------------
    registry = yaml.safe_load(open(SPEC_YAML))["specification_points"]
    chunks = []          # {note, chunk_idx, heading, content}
    note_points = {}     # note path -> [sp codes]  (HV note-level)
    sp_notes = defaultdict(set)
    sp_anchors = defaultdict(set)   # sp -> {(note, chunk_idx)}
    for dirpath, _, files in os.walk(NOTES_ROOT):
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            fm, cs = parse_note(path)
            rel = os.path.relpath(path, NOTES_ROOT)
            for ci, c in enumerate(cs):
                chunks.append({"note": rel, "chunk_idx": ci,
                               "heading": c["heading_path"],
                               "content": c["content"]})
            pts = []
            for sp in (fm.get("spec_map") or {}).get("spec_points") or []:
                code = sp.get("code")
                pts.append(code)
                sp_notes[code].add(rel)
                ev = (sp.get("provenance") or {}).get("evidence") or ""
                if ev.strip():
                    # anchor location (audit logic)
                    q = norm(ev)
                    hits = [i for i, c in enumerate(cs)
                            if q and q in norm(c["content"])]
                    if len(hits) == 1:
                        sp_anchors[code].add((rel, hits[0]))
                    elif hits:
                        sp_anchors[code].add((rel, hits[0]))
                    else:
                        prefix = q[: min(60, len(q))]
                        if prefix:
                            for i, c in enumerate(cs):
                                if prefix in norm(c["content"]):
                                    sp_anchors[code].add((rel, i))
                                    break
            note_points[rel] = pts

    chunk_note = [c["note"] for c in chunks]
    bm25 = BM25([c["content"] for c in chunks])
    bm25_sp = BM25([p["official_wording"] for p in registry])  # SP resolver

    results = {
        "corpus": {"chunks": len(chunks),
                   "notes": len(note_points),
                   "sps_with_notes": len(sp_notes),
                   "sps_with_anchors": len(sp_anchors)},
        "honesty": {
            "gold_granularity": ("note-level T-C10 mappings + derived anchors; "
                                 "NO chunk-level validated gold exists"),
            "generous_routing": ("P2/P3 on Q1 are credited with a perfect SP "
                                 "resolver (the query's own SP); real "
                                 "performance is strictly worse"),
        },
        "q1_sp_wording": {},
        "q2_real_questions": [],
    }

    # ---- Q1: SP-wording queries ------------------------------------------
    # For each SP: does BM25 top-k contain (a) a chunk from a note mapped to
    # this SP (note-gold), (b) a derived anchor chunk? And what do the
    # SP-routes return?
    k = 5
    bm25_note_hit = bm25_anchor_hit = 0
    sp_route_covered = sp_route_chunks = []
    anchor_route_covered = anchor_route_sizes = []
    sps_evaluated = 0
    per_sp_rows = []
    for p in registry:
        sp = p["code"]
        query = p["official_wording"]
        gold_notes = sp_notes.get(sp, set())
        gold_anchors = sp_anchors.get(sp, set())
        if not gold_notes:
            continue
        sps_evaluated += 1
        hits = bm25.search(query, k)
        hit_chunks = [i for i, _ in hits]
        note_hit = any(chunk_note[i] in gold_notes for i in hit_chunks)
        anchor_hit = any((chunk_note[i], chunks[i]["chunk_idx"]) in gold_anchors
                         for i in hit_chunks)
        bm25_note_hit += note_hit
        bm25_anchor_hit += anchor_hit
        # P2: note-inheritance route (perfect resolver assumed)
        p2 = [i for i, c in enumerate(chunks) if c["note"] in gold_notes]
        # P3: anchor route
        p3 = [i for i, c in enumerate(chunks)
              if (c["note"], c["chunk_idx"]) in gold_anchors]
        sp_route_chunks.append(len(p2))
        anchor_route_sizes.append(len(p3))
        per_sp_rows.append({
            "sp": sp, "bm25_note_hit": note_hit,
            "bm25_anchor_hit": anchor_hit,
            "p2_size": len(p2), "p3_size": len(p3),
        })

    n = max(1, sps_evaluated)
    results["q1_sp_wording"] = {
        "sps_evaluated": sps_evaluated,
        "k": k,
        "bm25_top5_note_gold_hit_rate": round(bm25_note_hit / n, 4),
        "bm25_top5_anchor_hit_rate": round(bm25_anchor_hit / n, 4),
        "sp_note_route": {
            "coverage": 1.0,
            "mean_chunks_returned": round(sum(sp_route_chunks) / n, 2),
            "max": max(sp_route_chunks),
            "ranking_signal": "NONE (no chunk->SP data to rank or filter with)",
        },
        "sp_anchor_route": {
            "coverage": round(sum(1 for x in anchor_route_sizes if x > 0) / n, 4),
            "mean_chunks_returned": round(sum(anchor_route_sizes) / n, 2),
            "max": max(anchor_route_sizes),
        },
        "precision_ceiling_of_note_inheritance": round(
            (sum(anchor_route_sizes) / n) / (sum(sp_route_chunks) / n), 4),
        "per_sp": per_sp_rows,
    }

    # ---- Q2: real questions ----------------------------------------------
    for rq in REAL_QUERIES:
        gold_sps = set([rq["gold_primary"]] + rq["gold_secondary"])
        gold_notes = set().union(*(sp_notes.get(s, set()) for s in gold_sps))
        gold_anchors = set().union(*(sp_anchors.get(s, set()) for s in gold_sps))
        hits = bm25.search(rq["text"], 10)
        top5 = [i for i, _ in hits[:5]]
        top10 = [i for i, _ in hits]
        row = {
            "id": rq["id"],
            "gold": sorted(gold_sps),
            "gold_source": rq["gold_source"],
            "bm25_top5": [{"note": chunks[i]["note"].split("/")[-1][:60],
                           "heading": chunks[i]["heading"][:80]} for i in top5],
            "bm25_top5_note_gold_hit":
                any(chunk_note[i] in gold_notes for i in top5),
            "bm25_top10_note_gold_hit":
                any(chunk_note[i] in gold_notes for i in top10),
            "bm25_top5_anchor_hit":
                any((chunk_note[i], chunks[i]["chunk_idx"]) in gold_anchors
                    for i in top5),
        }
        # the SP resolver as it would really run: BM25 over SP wordings
        sp_hits = bm25_sp.search(rq["text"], 5)
        resolved = [registry[i]["code"] for i, _ in sp_hits]
        row["sp_resolver_top5"] = resolved
        row["sp_resolver_gold_in_top5"] = bool(gold_sps & set(resolved))
        # P2 under the REAL resolver
        p2_notes = set().union(*(sp_notes.get(s, set()) for s in resolved))
        p2_chunks = [i for i, c in enumerate(chunks) if c["note"] in p2_notes]
        row["sp_note_route_real_resolver"] = {
            "resolved_sps": resolved,
            "chunks_returned": len(p2_chunks),
            "note_gold_hit": any(chunk_note[i] in gold_notes for i in p2_chunks[:5])
            if p2_chunks else False,
        }
        results["q2_real_questions"].append(row)

    with open(OUT, "w") as f:
        json.dump(results, f, indent=1, sort_keys=True)

    q1 = results["q1_sp_wording"]
    print(f"corpus: {len(chunks)} chunks / {len(note_points)} notes / "
          f"{len(sp_notes)} SPs with notes / {len(sp_anchors)} with anchors")
    print(f"Q1 ({q1['sps_evaluated']} SPs, top-{q1['k']}):")
    print(f"  BM25 note-gold hit rate:      {q1['bm25_top5_note_gold_hit_rate']}")
    print(f"  BM25 anchor hit rate:         {q1['bm25_top5_anchor_hit_rate']}")
    print(f"  SP note-route size (mean/max): "
          f"{q1['sp_note_route']['mean_chunks_returned']}/"
          f"{q1['sp_note_route']['max']}")
    print(f"  SP anchor-route size (mean):  "
          f"{q1['sp_anchor_route']['mean_chunks_returned']} "
          f"(coverage {q1['sp_anchor_route']['coverage']})")
    print(f"  precision ceiling of note-inheritance: "
          f"{q1['precision_ceiling_of_note_inheritance']}")
    print("Q2 (real questions):")
    for r in results["q2_real_questions"]:
        print(f"  {r['id']}: bm25 top5 note-hit={r['bm25_top5_note_gold_hit']} "
              f"anchor-hit={r['bm25_top5_anchor_hit']} | resolver top5="
              f"{r['sp_resolver_top5']} gold-in-top5={r['sp_resolver_gold_in_top5']}"
              f" | P2 real-resolver chunks={r['sp_note_route_real_resolver']['chunks_returned']}")
    print(f"written {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
