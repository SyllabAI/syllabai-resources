#!/usr/bin/env python3
"""Select worst-corrupted chunks from v2 audit for LLM fidelity repair."""
import json

rows = json.load(open("/home/z/my-project/data/quality_audit.json"))
PROSE_TYPES = {"body", "key_point", "learning_objectives", "worked_example",
               "practical", "activity", "did_you_know", "exam_hint", "safety",
               "chapter_questions", "unit_questions", "answers", "glossary"}

selected = []
seen = set()
# 1) any chunk with >= 2 formula-merged garbles
for r in rows:
    if r["ctype"] in PROSE_TYPES and r["hits"].get("state_paren_garble", 0) >= 2:
        if r["id"] not in seen:
            selected.append(r["id"])
            seen.add(r["id"])
# 2) top-scored prose chunks (skip inherently fragmentary answers-heavy ones here)
for r in rows:
    if len(selected) >= 80:
        break
    if r["ctype"] in PROSE_TYPES and r["ctype"] != "answers" and r["score"] > 60:
        if r["id"] not in seen:
            selected.append(r["id"])
            seen.add(r["id"])
# 3) answers chunks with heavy garble (formulas dominate answers)
for r in rows:
    if len(selected) >= 100:
        break
    if r["ctype"] == "answers" and r["hits"].get("state_paren_garble", 0) >= 3:
        if r["id"] not in seen:
            selected.append(r["id"])
            seen.add(r["id"])

selected = selected[:100]
json.dump(selected, open("/home/z/my-project/data/llm_repair_ids.json", "w"))
print(f"selected {len(selected)} chunks for LLM fidelity repair")
by_type = {}
for r in rows:
    if r["id"] in selected:
        by_type[r["ctype"]] = by_type.get(r["ctype"], 0) + 1
print(json.dumps(by_type, indent=1))
