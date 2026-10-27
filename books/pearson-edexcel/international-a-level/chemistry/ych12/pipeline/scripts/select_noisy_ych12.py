#!/usr/bin/env python3
"""Select noisy YCH12 SB2 v1 chunks for the LLM fidelity polish.
Damage class = scan-wide dropped spaces (Chromium/Skia print-replica ->
RapidOCR), same dominant class as 4PH1 (63% of chunks carry glue runs).
Writes data/llm_repair_ids_ych12.json (worst first)."""
import json, re, os
from collections import Counter

PATH = os.environ.get("YCH12_CORPUS", "/home/z/my-project/data/ych12_sb2/out/edexcel_ial_chemistry_ych12_sb2_chunks_v1.jsonl")
OUT = os.environ.get("YCH12_IDS_OUT", "/home/z/my-project/data/ych12_sb2/llm_repair_ids_ych12.json")
CAP = 800  # 1571-chunk book, scan-wide glue; resumable runner tolerates quota gaps

COMMON = {"the", "of", "and", "a", "to", "in", "is", "are", "that", "it",
          "for", "with", "as", "be", "this", "on", "or", "by", "an", "which",
          "from", "at", "when", "has", "was", "you", "can", "not", "they"}

# legit long all-caps tokens in this book (sidebar labels, merged OCR heading
# forms, topic names) — census 2026-10-22
CAPS_OK = {"INTERPRETATION", "ELECTROMAGNETISM", "ELECTROMAGNETIC", "ACCELERATION",
           "INVESTIGATION", "INTERNATIONAL", "GRAVITATIONAL", "CHARACTERISTIC",
           "CHARACTERISTICS", "PROPORTIONALITY", "UNDERSTANDING", "MEASUREMENTS",
           "TEMPERATURES", "OSCILLOSCOPE", "OSCILLOSCOPES", "OBSERVATIONS",
           "LEARNINGOBJECTIVES", "WORKEDEXAMPLE", "EXAMPRACTICE", "THINKINGBIGGER",
           "SUBJECTVOCABULARY", "PRACTICALSKILLS", "MATHSSKILLSFORTHISCHAPTER",
           "MATHSSKILLS", "PHYSICSINDETAIL", "ADAPTIVELEARNING", "PROBLEMSOLVING",
           "CRITICALTHINKING", "SCIENCECOMMUNICATION", "INTERPRETATIONNOTE",
           "ARGUMENTATION", "ASSESSMENTOBJECTIVE", "SPECIFICATIONREFERENCE",
           "ELECTRICALQUANTITIES", "COMPLETEELECTRICALCIRCUITS", "COMMUNICATION",
           "DISPLACEMENT", "RESISTIVITY", "RESISTANCE", "QUANTISATION",
           "LEARNINGTIP", "DIDYOUKNOW", "CHECKPOINT", "MATHSSKILLSFORTHISTOPIC",
           "CHEMISTRYINDETAIL", "ADDITIONALREADING", "SPECREFERENCE", "EXAMHINT",
           "REACTANTS", "PRODUCTS", "OXIDATION", "REDUCTION", "ELECTRONS",
           "CONCENTRATION", "TEMPERATURE", "AQUEOUS", "PRECIPITATE"}

PATTERNS = {
    "space_run":     re.compile(r"\b[a-z]{18,}\b"),
    "caps_glue":     re.compile(r"\b[A-Z]{12,}\b"),
    "camel_glue":    re.compile(r"\b[a-z]{3,}[A-Z][a-z]{2,}\b"),
    "glued_word":         re.compile(r"\b[a-z]{1,3}[A-Z][a-z]{2,}"),
    "vowelless_token":    re.compile(r"\b[bcdfghj-np-tv-z]{5,}\b"),
    "latex_remnant":      re.compile(r"\\|\{|\}"),
    "debris_line":        re.compile(r"(?m)^\W{0,3}[a-z]{1,2}\W{0,3}$"),
    "repeated_punct":     re.compile(r"(\W)\1{3,}"),
    "stray_semicolon":    re.compile(r"\b[A-Za-z]+;[A-Za-z]+\b"),
    "odd_caps_run":       re.compile(r"\b[A-Z]{4,}[a-z]{2,}[A-Z]{2,}[a-z]*\b"),
}
WEIGHT = {"space_run": 3.0, "caps_glue": 1.0, "camel_glue": 2.0,
          "latex_remnant": 4.0, "repeated_punct": 2.0}
BOOST_TYPES = {"chapter_questions": 10.0}
DAMP_TYPES = {"glossary": 18.0, "front_matter": 12.0, "appendix": 12.0,
              "table_data": 15.0, "divider": 6.0}

def common_ratio(text):
    toks = re.findall(r"[a-z]+", text.lower())
    return sum(1 for t in toks if t in COMMON) / len(toks) if toks else 0.0

def strip_borders(text):
    text = re.sub(r"(?m)^\s*\|?[\s:|\-]+\|?\s*$", "", text)
    return re.sub(r"[ \t]{2,}", " ", text)

rows = []
for line in open(PATH, encoding="utf-8"):
    c = json.loads(line)
    txt = strip_borders(c["text"])
    hits = {}
    for name, pat in PATTERNS.items():
        n = len(pat.findall(txt))
        if name == "caps_glue":
            n = len([m for m in pat.findall(txt) if m not in CAPS_OK])
        if n:
            hits[name] = n
    toks = re.findall(r"[A-Za-z]+", txt)
    short_w = sum(1 for t in toks if len(t) <= 2 and t.lower() not in
                  {"a", "an", "as", "at", "be", "by", "do", "go", "he", "if",
                   "in", "is", "it", "me", "my", "no", "of", "on", "or", "so",
                   "to", "up", "us", "we", "ph"})
    frag_ratio = short_w / max(len(toks), 1)
    cr = common_ratio(txt)
    score = (1 - cr) * 40 + frag_ratio * 30 + \
            sum(min(v * WEIGHT.get(k, 1.0), 30) for k, v in hits.items())
    score += BOOST_TYPES.get(c["content_type"], 0.0)
    score -= DAMP_TYPES.get(c["content_type"], 0.0)
    rows.append({"id": c["id"], "ctype": c["content_type"],
                 "chap": c["chapter_no"], "score": round(score, 1), "hits": hits})

rows.sort(key=lambda r: -r["score"])
sel = [r for r in rows if r["score"] > 25][:CAP]
sel_ids = {r["id"] for r in sel}
for r in rows:
    if r["ctype"] in BOOST_TYPES and r["id"] not in sel_ids and \
       (r["hits"].get("space_run", 0) or r["hits"].get("camel_glue", 0)):
        sel.append(r)

print("=== noise classes across all chunks ===")
tot = Counter()
for r in rows:
    for k, v in r["hits"].items():
        tot[k] += v
for k, v in tot.most_common():
    print(f"  {k:18s} {v}")
print(f"\nselected {len(sel)} chunks")
by_type = Counter(r["ctype"] for r in sel)
print("by type:", dict(by_type))
qsel = [r for r in sel if r["ctype"] in BOOST_TYPES]
print("question-typed selected:", len(qsel), "(serving-critical, force-included with glue)")
json.dump([r["id"] for r in sel], open(OUT, "w"), indent=1)
print(f"\nsaved -> {OUT}")
