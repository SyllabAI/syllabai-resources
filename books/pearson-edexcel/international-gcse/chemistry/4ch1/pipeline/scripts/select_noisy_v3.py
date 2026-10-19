#!/usr/bin/env python3
"""Select the noisiest v3 chunks for a light LLM fidelity pass.

Scores residual OCR/parse noise per chunk (v3-specific patterns), writes
data/llm_repair_ids_v3.json (capped, worst first). Prints stats only.
"""
import json, re
from collections import Counter

PATH = "/home/z/my-project/download/rag_chemistry/edexcel_igcse_chemistry_chunks_v3.jsonl"
OUT = "/home/z/my-project/data/llm_repair_ids_v3.json"
CAP = 90  # ~7% of 1234; light pass

COMMON = {"the", "of", "and", "a", "to", "in", "is", "are", "that", "it",
          "for", "with", "as", "be", "this", "on", "or", "by", "an", "which",
          "from", "at", "when", "has", "was", "you", "can", "not", "they"}

PATTERNS = {
    "state_paren_garble": re.compile(r"[A-Za-z]\s*,\s*\((?:g|l|s|aq)\)"),
    "zero_for_O":         re.compile(r"(?<![A-Za-z0-9])[A-Z][a-z]?\d*0(?=\d|\b)"),
    "glued_word":         re.compile(r"\b[a-z]{1,3}[A-Z][a-z]{2,}"),       # dThe, iethis
    "vowelless_token":    re.compile(r"\b[bcdfghj-np-tv-z]{5,}\b"),        # riGw-like
    "arrow_remnant":      re.compile(r"(?<![A-Za-z])arrow(?![A-Za-z])"),
    "latex_remnant":      re.compile(r"\\|\{|\}"),
    "debris_line":        re.compile(r"(?m)^\W{0,3}[a-z]{1,2}\W{0,3}$"),
    "repeated_punct":     re.compile(r"(\W)\1{3,}"),
    "stray_semicolon":    re.compile(r"\b[A-Za-z]+;[A-Za-z]+\b"),
    "odd_caps_run":       re.compile(r"\b[A-Z]{4,}[a-z]{2,}[A-Z]{2,}[a-z]*\b"),
}

def common_ratio(text):
    toks = re.findall(r"[a-z]+", text.lower())
    return sum(1 for t in toks if t in COMMON) / len(toks) if toks else 0.0

def strip_borders(text):
    """Remove markdown table border/separator lines + collapse padding before scoring."""
    text = re.sub(r"(?m)^\s*\|?[\s:|\-]+\|?\s*$", "", text)
    return re.sub(r"[ \t]{2,}", " ", text)

rows = []
for line in open(PATH, encoding="utf-8"):
    c = json.loads(line)
    txt = strip_borders(c["text"])
    hits = {}
    for name, pat in PATTERNS.items():
        n = len(pat.findall(txt))
        if n:
            hits[name] = n
    if c["content_type"] == "table_data":
        # formulas with ASCII digits in table cells = lost subscripts (CH4, C2H6)
        n = len(re.findall(r"\b[A-Z][A-Za-z]?\d[A-Za-z0-9]*\b", txt))
        if n:
            hits["ascii_formula"] = n
    toks = re.findall(r"[A-Za-z]+", txt)
    short_w = sum(1 for t in toks if len(t) <= 2 and t.lower() not in
                  {"a", "an", "as", "at", "be", "by", "do", "go", "he", "if",
                   "in", "is", "it", "me", "my", "no", "of", "on", "or", "so",
                   "to", "up", "us", "we", "ph"})
    frag_ratio = short_w / max(len(toks), 1)
    cr = common_ratio(txt)
    # low common-word density + fragments + explicit noise hits
    score = (1 - cr) * 40 + frag_ratio * 60 + sum(min(v, 15) for v in hits.values())
    # answers/glossary/index are naturally fragment-heavy; damp their base score
    if c["content_type"] in ("answers", "glossary", "index", "front_matter"):
        score -= 18
    if c["content_type"] == "table_data":
        score -= 15  # number/label heavy by nature
    rows.append({"id": c["id"], "ctype": c["content_type"],
                 "chap": c["chapter_no"], "score": round(score, 1), "hits": hits})

rows.sort(key=lambda r: -r["score"])
sel = [r for r in rows if r["score"] > 30][:CAP]

print("=== noise classes across all chunks ===")
tot = Counter()
for r in rows:
    for k, v in r["hits"].items():
        tot[k] += v
for k, v in tot.most_common():
    print(f"  {k:20s} {v}")
print(f"\nselected {len(sel)} chunks (score>30, cap {CAP})")
by_type = Counter(r["ctype"] for r in sel)
print("by type:", dict(by_type))
for r in sel[:15]:
    print(f"  {r['score']:>6} {r['id'][:36]:36s} {r['ctype']:16s} ch{r['chap']} {r['hits']}")
json.dump([r["id"] for r in sel], open(OUT, "w"), indent=1)
print(f"\nsaved -> {OUT}")
