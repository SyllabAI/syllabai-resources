#!/usr/bin/env python3
"""Select YPH11 SB1 chunks for LLM fidelity polish round 1.

Scan damage class (Skia/ActiveLearn ~155dpi print replica -> RapidOCR):
dropped spaces between words, scan-wide (L-005 glue-run census: 79% of chunks
carry 18+ char lowercase runs; 90% carry 12+ runs).

Policy:
- force-include ALL chapter_questions chunks (serving-critical, golden rule 1)
- include every chunk with measurable glue damage (longest lowercase run >= 12)
- table_data and glossary/index glue is included too (guards protect structure;
  4PH1 precedent: index table chunk was the only holdout, evidence kept)
Outputs data/ial_physics/llm_repair_ids_sb2.json (ordered: questions first).
"""
import json, re, collections

F = "/home/z/my-project/download/rag_ial_physics/edexcel_ial_physics_yph11_sb2_chunks_v1.jsonl"
OUT = "/home/z/my-project/data/ial_physics/llm_repair_ids_sb2.json"
chunks = [json.loads(l) for l in open(F)]

def glue_metrics(text):
    runs = re.findall(r"[a-z]{12,}", text)
    longest = max((len(r) for r in runs), default=0)
    return longest, len(runs)

selected, stats = [], []
for c in chunks:
    longest, nruns = glue_metrics(c["text"])
    damaged = longest >= 12
    forced = c["content_type"] == "chapter_questions"
    if forced or damaged:
        selected.append((c["id"], forced, longest, c["content_type"]))
    stats.append((c["content_type"], longest))

forced_n = sum(1 for _, f, _, _ in selected if f)
scored_n = len(selected) - forced_n
tc = collections.Counter(t for t, l in stats if l >= 12)
print(f"selected {len(selected)}/{len(chunks)} (forced question chunks: {forced_n}, glue-scored: {scored_n})")
print("damaged by type:", dict(tc.most_common(12)))

# order: forced question chunks first, then by damage severity desc
selected.sort(key=lambda t: (not t[1], -t[2]))
ids = [i for i, _, _, _ in selected]
json.dump(ids, open(OUT, "w"), indent=0)
print(f"-> {OUT} ({len(ids)} ids)")
