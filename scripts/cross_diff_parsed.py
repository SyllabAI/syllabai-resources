#!/usr/bin/env python3
"""ADR-037 cross-diff: converter topic.json vs the repo's own parsed/questions.json layer.

Independent parse agreement — the strongest correctness evidence available:
two different parsers over the same PDF must agree on every part mark.

Usage: python3 cross_diff_parsed.py [--paper P] [series ...]   (default: all series that have a parsed layer)
Expects: $EXAMQ_UPLOAD_DIR (default /home/z/my-project/upload)/parsed-{S}-questions.json
         and <checkout>/Official-ExamQuestion/igcse-chemistry-19/{S}/4CH1-{paper}/topic.json
F34: --paper selects the variant (default 1C). The repo parsed/ layer exists for
1C dirs only today, so 2C runs SKIP honestly (no independent parse to diff against).
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
_args = [a for a in sys.argv[1:] if not a.startswith("--") and not a in ("1C", "2C")]
PAPER = "2C" if ("--paper" in sys.argv and sys.argv.index("--paper") + 1 < len(sys.argv)
                 and sys.argv[sys.argv.index("--paper") + 1] == "2C") else "1C"
series = _args or HAVE_PARSED

out = {"schema": "syllabai.official-paper-questions.cross-diff/0.1", "paper": PAPER, "series": []}
for S in series:
    pf = UPLOAD / f"parsed-{S}-questions.json"
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
