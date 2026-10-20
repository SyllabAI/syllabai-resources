#!/usr/bin/env python3
"""Select noisy 4BI1 chunks for LLM fidelity polish (phase 7).

Corruption classes on this TEXT-LAYER source (probe_4bi1_noise.py + chunk
census): broken-CMap display/italic garbles (1s/1n/hvmg/chapler/KEV/ANO/
FOOO/carbOn/worl</!his), arrow garbles (" -+ " for ->), icon glyph junk
(mD / 11> / Ell>), garbled bullets (11 <item>).

Selection per playbook phase 7:
  - FORCE-INCLUDE all question-typed chunks (serving-critical)
  - include every chunk carrying >=1 garble signature
  - include front-matter chunks with stylized-art junk lines
Outputs data/biology/llm_repair_ids_biology.json (array, chunk order).
"""
import json, re, collections

F = "/home/z/my-project/download/rag_biology/edexcel_igcse_biology_chunks_v1.jsonl"
OUT = "/home/z/my-project/data/biology/llm_repair_ids_biology.json"

chunks = [json.loads(l) for l in open(F)]

SIGS = {
    # VERIFIED garble classes only (probe_4bi1_noise.py + chunk census).
    # Broad digit-word heuristics were tried and REJECTED: they false-fire on
    # legitimate words (living, lumen, lungs) and inflated selection 500->671.
    "1s(is)": re.compile(r"\b1s\b"),
    "1n(in)": re.compile(r"\b1n\b"),
    "chapler": re.compile(r"chapler\b|chapte\s+r\b", re.I),
    "ANO(AND)": re.compile(r"\bANO\b"),
    "KEV(KEY)": re.compile(r"KEV\b|kEY\s*POIHl"),
    "FOOO(FOOD)": re.compile(r"FOOO"),
    "hvmg(living)": re.compile(r"hvmg|l1vmg|thmgs"),
    "U1e(The)": re.compile(r"\bU1e\b"),
    "!his(This)": re.compile(r"!his\b|\bworl<\b"),
    "arrow_garble": re.compile(r" -\+ |\b-\+"),
    "icon_junk": re.compile(r"\bmD\b|\bBD\b|\bDD\b|\bEll\s*>|\b11\s*>|IEl:!l!l>"),
    "garbled_bullet": re.compile(r"\b11\s+(Understand|Know|Describe|Explain|Recall|Investigate)"),
    "mixed_case_garble": re.compile(r"\b[a-z]+[A-Z][a-z]+\b"),
}

def score(c):
    s = 0
    hits = []
    for name, rx in SIGS.items():
        n = len(rx.findall(c["text"]))
        if n:
            s += n
            hits.append(name)
    # digit_for_i: '1nvestigate' style (digit inside a lowercase word) with a
    # real-word allowlist filter (life/like/live/limb... are legitimate)
    # digit-starting words ('1nvestigate', '1s', '1n') — English has no
    # digit-initial words except '1st'; the earlier [1l] version false-fired
    # on every l-word and was narrowed to digits only.
    for m in re.findall(r"\b1[a-z]{3,}\b", c["text"]):
        if m.lower() not in REAL_WORDS:
            s += 1
            hits.append(f"digit_for_i:{m}")
    return s, hits

REAL_WORDS = {"1st"}

selected = []
reasons = {}
for c in chunks:
    s, hits = score(c)
    force = c["content_type"] in ("chapter_questions", "unit_questions")
    if force or s > 0:
        selected.append(c["id"])
        reasons[c["id"]] = {"score": s, "hits": hits, "forced": force}

# front matter with stylized-art junk (cover/assessment-overview garble)
for c in chunks:
    if c["content_type"] == "front_matter" and c["id"] not in reasons:
        if re.search(r"[i1l\\]{5,}", c["text"]) or c["text"].count("~") >= 3:
            selected.append(c["id"])
            reasons[c["id"]] = {"score": 1, "hits": ["stylized_art"], "forced": False}

# keep corpus order
order = {c["id"]: i for i, c in enumerate(chunks)}
selected.sort(key=lambda i: order[i])

with open(OUT, "w") as f:
    json.dump(selected, f, indent=1)
types = collections.Counter(c["content_type"] for c in chunks if c["id"] in set(selected))
print(f"selected {len(selected)}/{len(chunks)} chunks -> {OUT}")
print("by type:", dict(types.most_common()))
forced = sum(1 for v in reasons.values() if v["forced"])
garbled_only = len(selected) - forced
print(f"forced question chunks: {forced}   garble/art-selected: {garbled_only}")
