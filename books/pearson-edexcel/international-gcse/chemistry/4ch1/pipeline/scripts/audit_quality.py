#!/usr/bin/env python3
"""Audit chunk text quality: quantify OCR corruption classes, rank worst chunks.
Prints statistics only (scores/counts), no book text."""
import json, re
from collections import Counter

PATH = "/home/z/my-project/download/rag_chemistry/edexcel_igcse_chemistry_chunks_v2.jsonl"

# English function-word density: real prose is full of these; garbled text is not
COMMON = {"the", "of", "and", "a", "to", "in", "is", "are", "that", "it",
          "for", "with", "as", "be", "this", "on", "or", "by", "an", "which",
          "from", "at", "when", "has", "was", "you", "can", "not", "they"}

PATTERNS = {
    "state_paren_garble": re.compile(r"[A-Za-z]\s*,\s*\((?:g|l|s|aq)\)"),   # H,(g)
    "zero_for_O":         re.compile(r"(?<![A-Za-z0-9])[A-Z][a-z]?\d*0(?=\d|\b)"),  # H20
    "stray_semicolon_wd": re.compile(r"\b[A-Za-z]+;[A-Za-z]+\b"),
    "lonely_caps_frag":   re.compile(r"(?m)^[A-Z]{1,3}\s*$"),
    "punct_lead_line":    re.compile(r"(?m)^[|}\]>«»\"';:.]{1,4}\s"),
    "qmark_in_number":    re.compile(r"\d\?(?:\s|$)"),
    "digit_comma_digit":  re.compile(r"\b\d+,\d{3}\b"),   # legit thousands; count only
    "broken_apostrophe":  re.compile(r"\b[A-Za-z]+ [A-Z][a-z]+s\b"),
    "double_space":       re.compile(r"  "),
    "eq_arrow_lost":      re.compile(r"\b(should|will)\s+(give|form)\b"),  # weak
}

def common_ratio(text):
    toks = re.findall(r"[a-z]+", text.lower())
    if not toks:
        return 0.0
    return sum(1 for t in toks if t in COMMON) / len(toks)

rows = []
cls_total = Counter()
for line in open(PATH, encoding="utf-8"):
    c = json.loads(line)
    txt = c["text"]
    hits = {}
    for name, pat in PATTERNS.items():
        n = len(pat.findall(txt))
        if n:
            hits[name] = n
            cls_total[name] += n
    cr = common_ratio(txt)
    toks = re.findall(r"[A-Za-z]+", txt)
    short_w = sum(1 for t in toks if len(t) <= 2 and t.lower() not in
                  {"a", "an", "as", "at", "be", "by", "do", "go", "he", "if",
                   "in", "is", "it", "me", "my", "no", "of", "on", "or", "so",
                   "to", "up", "us", "we", "pH"})
    frag_ratio = short_w / max(len(toks), 1)
    score = (1 - cr) * 100 + frag_ratio * 100 + sum(min(v, 20) for v in hits.values())
    rows.append({"id": c["id"], "ctype": c["metadata"]["content_type"],
                 "chap": c["metadata"]["chapter_no"], "score": round(score, 1),
                 "common_ratio": round(cr, 3), "frag_ratio": round(frag_ratio, 3),
                 "hits": hits})

rows.sort(key=lambda r: -r["score"])
print("=== corruption classes across all 640 chunks ===")
for k, v in cls_total.most_common():
    print(f"  {k:22s} {v}")
print("\n=== 20 worst chunks (score | id | type | ch | common_ratio | frag) ===")
for r in rows[:20]:
    print(f"  {r['score']:>6} {r['id']} {r['ctype']:20s} ch{str(r['chap']):>4} "
          f"cr={r['common_ratio']:.2f} fr={r['frag_ratio']:.2f} {r['hits']}")
print(f"\nchunks with score>35: {sum(1 for r in rows if r['score'] > 35)}")
print(f"chunks with score>25: {sum(1 for r in rows if r['score'] > 25)}")
print(f"mean common_ratio: {sum(r['common_ratio'] for r in rows)/len(rows):.3f}")
json.dump(rows, open("/home/z/my-project/data/quality_audit.json", "w"))
print("saved -> data/quality_audit.json")
