#!/usr/bin/env python3
"""Calibrate the biology fidelity guard: compute garble-normalized char-LCS
for banked OKs and rejects. If rejects cluster at 0.90-0.97 while OKs sit
>=0.97, the guard threshold needs a biology-specific recalibration (the
hvmg-class garbles change characters AND lengths — unmappable generically)."""
import json, re

def normalizeGarble(s):
    s = re.sub(r"\b1s\b", "is", s); s = re.sub(r"\b1n\b", "in", s)
    s = re.sub(r"chapler|chapte r", "chapter", s, flags=re.I)
    s = re.sub(r"\bANO\b", "AND", s)
    s = re.sub(r"kEY POIHl", "KEY POINT", s); s = re.sub(r"\bKEV\b", "KEY", s)
    s = re.sub(r"FOOO", "FOOD", s)
    s = re.sub(r"hvmg|l1vmg", "living", s); s = re.sub(r"thmgs", "things", s)
    s = re.sub(r"\bU1e\b", "The", s); s = re.sub(r"!his", "This", s)
    s = re.sub(r"\bworl<", "work", s); s = re.sub(r"carbOn", "carbon", s)
    s = re.sub(r" -\+ ", " -> ", s); s = re.sub(r"\b-\+", "->", s)
    s = re.sub(r"\bmD\b|\bBD\b|\bDD\b|\bEll\s*>|\b11\s*>|IEl:!l!l>", " ", s)
    # generic icon-junk token rule (JS twin in llm_repair_biology.js)
    def junk(tok):
        if len(tok) < 4 or not re.search(r"\W", tok):
            return False
        residue = re.sub(r"[il1]", "", tok)
        return not re.search(r"\d", residue) and len(residue) <= 2
    return " ".join(t for t in re.sub(r"\s+", " ", s).split(" ") if t and not junk(t))

def lcs_ratio(a, b):
    A = normalizeGarble(a).replace(" ", "")
    B = normalizeGarble(b).replace(" ", "")
    if not A or not B: return 0.0
    prev = [0]*(len(B)+1); cur = [0]*(len(B)+1)
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            cur[j] = prev[j-1]+1 if A[i-1] == B[j-1] else max(prev[j], cur[j-1])
        prev, cur = cur, [0]*(len(B)+1)
    return 2*prev[len(B)]/(len(A)+len(B))

chunks = {}
for line in open("/home/z/my-project/download/rag_biology/edexcel_igcse_biology_chunks_v1.jsonl"):
    c = json.loads(line); chunks[c["id"]] = c["text"]

ok_lcs, rej_lcs = [], []
for line in open("/home/z/my-project/data/biology/llm_repairs_biology.jsonl"):
    r = json.loads(line)
    orig = chunks[r["id"]]
    rep = r.get("text") or r.get("raw") or ""
    v = lcs_ratio(orig, rep)
    (ok_lcs if r["status"] == "ok" else rej_lcs if r["status"] == "rejected" else []).append((v, r["id"]))

ok_lcs.sort(); rej_lcs.sort(reverse=True)
print("OK  LCS: min", round(ok_lcs[0][0], 4), "p10", round(ok_lcs[len(ok_lcs)//10][0], 4),
      "median", round(ok_lcs[len(ok_lcs)//2][0], 4))
print("lowest 5 OK:", [(round(v, 4), i[-20:]) for v, i in ok_lcs[:5]])
print("REJ  LCS (best first):", [(round(v, 4), i[-20:]) for v, i in rej_lcs[:10]])
