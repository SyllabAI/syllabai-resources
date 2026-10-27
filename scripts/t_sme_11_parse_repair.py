#!/usr/bin/env python3
"""T-SME-11 parse repair: igcse-science-double-award-modular.

The code_column family (correct for this PDF's content pages) misfires on one
preamble line: the marketing boilerplate "With over 3.4 million students
studying our academic and vocational qualifications worldwide ..." in the
'Why choose Pearson Edexcel...' section (PDF page 10, before any content
section) is parsed as statement 3.4 with text "million learners studying ...".

The genuine 4.x statement numbering starts in the Biology content section
(page 17+); page-10 rows are preamble by construction. Repair: drop parsed
points on preamble pages (page < 15) whose text continues a sentence fragment
("million learners ..."), i.e. the exact false-positive class — verified
against the full parsed set (1 row affected).
"""
from __future__ import annotations

import glob
import json
from datetime import datetime, timezone
from pathlib import Path

QUAL = "igcse-science-double-award-modular"
PARSED = Path("/home/z/my-project/download/syllabai-resources/Official-Specifications/parsed")

DROP_RULE = ("drop preamble false-positive: official_code 3.4 with text "
             "starting 'million learners' (marketing boilerplate 'over 3.4 "
             "million students studying ...' on PDF page 10, before the "
             "content sections; genuine N.M statements start page 17)")


def main() -> int:
    changed = 0
    for f in glob.glob(str(PARSED / QUAL / "*.parsed.json")):
        doc = json.loads(Path(f).read_text())
        before = len(doc["spec_points"])
        doc["spec_points"] = [
            p for p in doc["spec_points"]
            if not (p.get("page", 99) < 15
                    and (p.get("text") or "").startswith("million learners"))
        ]
        dropped = before - len(doc["spec_points"])
        if dropped:
            doc.setdefault("repairs", []).append(
                {"rule": DROP_RULE, "dropped": dropped,
                 "applied_utc": datetime.now(timezone.utc)
                 .strftime("%Y-%m-%dT%H:%M:%SZ")})
            Path(f).write_text(json.dumps(doc, indent=1, ensure_ascii=False))
            changed += 1
            print(f"{f}: dropped {dropped} preamble false-positive(s)")
        else:
            print(f"{f}: nothing to drop (already repaired?)")
    return 0 if changed <= 1 else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
