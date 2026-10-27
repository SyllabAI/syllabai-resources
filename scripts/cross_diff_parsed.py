#!/usr/bin/env python3
"""ADR-037 cross-diff: converter topic.json vs the repo's own parsed/questions.json layer.

Independent parse agreement — the strongest correctness evidence available:
two different parsers over the same PDF must agree on every part mark.

Usage: python3 cross_diff_parsed.py [--paper P] [series ...]   (default: all series that have a parsed layer)
Expects: $EXAMQ_UPLOAD_DIR (default /home/z/my-project/upload)/parsed-{S}-questions.json for 1C
         and parsed-{paper}-{S}-questions.json for the other variants,
         plus <checkout>/Official-ExamQuestion/igcse-chemistry-19/{S}/4CH1-{paper}/topic.json
F34: --paper selects the variant (default 1C). Wave-26: the repo parsed/ layer now
also covers all 16 2C sittings (pastpapers PR #3: 12 new + 2 regenerated verified,
alongside the pre-existing 2024-06/2026-06), so --paper 2C runs end-to-end.
Wave-27: --paper 2CR runs end-to-end too (pastpapers PR: 9 new + 1 regenerated
verified, alongside the pre-existing 2026-06 — 2024-06 regenerated false→true
with byte-equal marks); non-1C parsed files are namespaced
parsed-{paper}-{S}-questions.json to keep the variants from clobbering each
other in the shared upload dir.
Writes:  <checkout>/Official-ExamQuestion/CROSS-DIFF.json  (always inside the checkout; F15)
"""
import json
import os
import sys
from pathlib import Path

UPLOAD = Path(os.environ.get("EXAMQ_UPLOAD_DIR", "/home/z/my-project/upload"))
BASE = Path(__file__).resolve().parent.parent / "Official-ExamQuestion"
IGCSE = BASE / "igcse-chemistry-19"

HAVE_PARSED = ["2024-06", "2025-06", "2026-06"]
HAVE_PARSED_2C = ["2019-06", "2020-01", "2020-11", "2021-01", "2021-06", "2021-11",
                  "2022-01", "2022-06", "2023-01", "2023-06", "2023-11", "2024-06",
                  "2024-11", "2025-06", "2025-11", "2026-06"]
HAVE_PARSED_2CR = ["2019-06", "2020-01", "2020-11", "2021-01", "2022-01", "2022-06",
                   "2023-01", "2023-06", "2024-06", "2025-06", "2026-06"]
PAPERS = {"1C": HAVE_PARSED, "2C": HAVE_PARSED_2C, "2CR": HAVE_PARSED_2CR}
_args = [a for a in sys.argv[1:] if not a.startswith("--") and not a in PAPERS]
_idx = sys.argv.index("--paper") + 1 if "--paper" in sys.argv else None
PAPER = sys.argv[_idx] if (_idx and _idx < len(sys.argv) and sys.argv[_idx] in PAPERS) else "1C"
series = _args or PAPERS[PAPER]

out = {"schema": "syllabai.official-paper-questions.cross-diff/0.1", "paper": PAPER, "series": []}
for S in series:
    stem = f"parsed-{S}" if PAPER == "1C" else f"parsed-{PAPER}-{S}"
    pf = UPLOAD / f"{stem}-questions.json"
    tf = IGCSE / S / f"4CH1-{PAPER}" / "topic.json"
    if not pf.exists() or not tf.exists():
        print(f"{S}: SKIP (missing {'parsed' if not pf.exists() else 'topic.json'})")
        continue
    parsed = json.loads(pf.read_text())
    ours = json.loads(tf.read_text())

    def pmap(doc):
        m = {}
        for q in doc["questions"]:
            for p in q.get("parts", []):
                lab, sub = p.get("label"), p.get("sub")
                pn = f"{q['number']}({lab})" + (f"({sub})" if sub else "")
                m[pn] = p["marks"]
        return m

    pm, om = pmap(parsed), {}
    for q in ours["questions"]:
        for p in q["parts"]:
            om[p["part_number"]] = p["marks"]

    common = sorted(set(pm) & set(om))
    mism = [(k, om[k], pm[k]) for k in common if om[k] != pm[k]]
    only_ours = sorted(set(om) - set(pm))
    only_parsed = sorted(set(pm) - set(om))
    qm = {q["number"]: q["marks"] for q in parsed["questions"]}
    qo = {q["question_number"]: q["total_marks"] for q in ours["questions"]}
    qmism = [(n, qo.get(n), qm[n]) for n in sorted(set(qo) & set(qm)) if qo.get(n) != qm[n]]

    rec = {"series": S, "paper": PAPER,
           "comparable_parts": len(common), "part_mismatches": mism,
           "only_in_ours": only_ours, "only_in_parsed": only_parsed,
           "question_mismatches": qmism,
           "match_rate": f"{len(common) - len(mism)}/{len(common)}"}
    out["series"].append(rec)
    print(f"{S}: parts {len(common)-len(mism)}/{len(common)} agree, {len(mism)} mismatches"
          f" | only-ours {len(only_ours)} only-parsed {len(only_parsed)} | Q-level mismatches {len(qmism)}")

(BASE / "CROSS-DIFF.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
print("written:", BASE / "CROSS-DIFF.json")
