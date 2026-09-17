#!/usr/bin/env python3
"""Corpus-wide nowhere-check: for every course index's missing ids, is the
id present in ANY other harvested index in the whole corpus? Emits the
definitive sibling-resolution report and writes it to
.cache/sme_spcpt_sibling_report.json for the registry refresh."""
from __future__ import annotations

import json
import time
from pathlib import Path

CORPUS = Path("/home/z/my-project/download/syllabai-resources/SME-ExamQuestion")
OUT = Path("/home/z/my-project/.cache/sme_spcpt_sibling_report.json")

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

all_ids = {c: set(d["spec_points"]) for c, d in idx.items()}
report = {"generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
          "courses": {}}
tot_miss = tot_fam = tot_any = tot_none = 0
for c in sorted(idx):
    miss = idx[c]["coverage"]["missing_from_index"]
    fam = COURSE_FAMILY[c]
    fam_hits, any_hits, none = {}, {}, []
    for sid in miss:
        in_fam = [s for s in FAMILIES[fam] if s != c and sid in all_ids.get(s, ())]
        in_any = [s for s in idx if s != c and sid in all_ids[s]]
        if in_fam:
            fam_hits[sid] = in_fam
        if in_any:
            any_hits[sid] = in_any
        else:
            none.append(sid)
    tot_miss += len(miss)
    tot_fam += len(fam_hits)
    tot_any += len(any_hits)
    tot_none += len(none)
    report["courses"][c] = {
        "missing": len(miss),
        "sibling_resolved_same_family": {k: v for k, v in fam_hits.items()},
        "resolved_outside_family": {k: v for k, v in any_hits.items()
                                    if k not in fam_hits},
        "nowhere_corpus_wide": none,
    }
    print(f"{c:55s} miss={len(miss):3d} fam={len(fam_hits):3d} "
          f"any+={len(any_hits) - len(fam_hits):2d} nowhere={len(none):3d}")

report["totals"] = {"missing": tot_miss, "family_resolved": tot_fam,
                    "outside_family_resolved": tot_any - tot_fam,
                    "nowhere_corpus_wide": tot_none}
OUT.write_text(json.dumps(report, indent=1), encoding="utf-8")
print(f"\nTOTALS missing={tot_miss} family={tot_fam} "
      f"outside+={tot_any - tot_fam} nowhere={tot_none}")
print(f"saved {OUT}")
