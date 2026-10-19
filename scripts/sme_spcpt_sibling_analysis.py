#!/usr/bin/env python3
"""T-SME-EQ-2 batch-2 gap analysis: for every course index, check the
missing part-id coverage against SIBLING course indexes (same subject
family — cross-unit / cross-tier SME tagging). Read-only report."""
from __future__ import annotations

import json
from pathlib import Path

CORPUS = Path("/home/z/my-project/download/syllabai-resources/SME-ExamQuestion")

FAMILIES = {
    "ial-maths": ["ial-maths-20-pure-1", "ial-maths-20-pure-2",
                  "ial-maths-20-pure-3", "ial-maths-20-pure-4",
                  "ial-maths-20-statistics-1", "ial-maths-20-statistics-2",
                  "ial-maths-20-mechanics-1", "ial-maths-20-mechanics-2",
                  "ial-maths-20-decision-1"],
    "accounting": ["igcse-accounting-17-financial-statements",
                   "igcse-accounting-17-introduction-to-bookkeeping-and-accounting"],
    "biology": ["igcse-biology-19", "igcse-biology-modular-24-unit-1",
                "igcse-biology-modular-24-unit-2"],
    "chemistry": ["igcse-chemistry-19", "igcse-chemistry-modular-24-unit-1",
                  "igcse-chemistry-modular-24-unit-2"],
    "physics": ["igcse-physics-19", "igcse-physics-modular-24-unit-1",
                "igcse-physics-modular-24-unit-2"],
    "maths-a": ["igcse-maths-a-18-foundation", "igcse-maths-a-18-higher",
                "igcse-maths-a-modular-24-foundation-unit-1",
                "igcse-maths-a-modular-24-foundation-unit-2",
                "igcse-maths-a-modular-24-higher-unit-1",
                "igcse-maths-a-modular-24-higher-unit-2"],
    "science-double-award": ["igcse-science-double-award-17-biology",
                             "igcse-science-double-award-17-chemistry",
                             "igcse-science-double-award-17-physics"],
    "english-lit": ["igcse-english-literature-16"],
}
COURSE_FAMILY = {c: f for f, cs in FAMILIES.items() for c in cs}

idx = {}
for c in COURSE_FAMILY:
    f = CORPUS / c / "spec_point_index.json"
    if f.exists():
        idx[c] = json.loads(f.read_text(encoding="utf-8"))

total_missing = 0
total_resolved = 0
for c, doc in sorted(idx.items()):
    miss = doc["coverage"]["missing_from_index"]
    if not miss:
        continue
    total_missing += len(miss)
    fam = COURSE_FAMILY[c]
    sib = {s: set(idx[s]["spec_points"]) for s in FAMILIES[fam] if s != c}
    resolved = {}
    for sid in miss:
        hits = [s for s, ids in sib.items() if sid in ids]
        if hits:
            resolved[sid] = hits
    total_resolved += len(resolved)
    pct = 100 * len(miss and (doc["coverage"]["covered_by_index"] * [0]) or 0)
    print(f"[{c}] missing {len(miss)} | resolved in siblings: "
          f"{len(resolved)} | still nowhere: {len(miss) - len(resolved)}")
    for sid, hits in sorted(resolved.items())[:6]:
        print(f"    {sid} -> {'; '.join(hits)}")
    if len(miss) - len(resolved):
        rest = [s for s in miss if s not in resolved]
        print(f"    NOWHERE sample: {rest[:5]}")

print(f"\nTOTAL missing {total_missing}, sibling-resolved {total_resolved}, "
      f"genuinely-unpublished {total_missing - total_resolved}")
