#!/usr/bin/env python3
"""T-SME-FLASH-1 — recompute fill_in_the_blanks for stored decks.

Uses the alignment-based fitb_from_md (imported from the scraper): the back
restates the front with blanks filled, so answers are EXTRACTED by matching
front-structure against back text — never guessed. Unmatched structure is
flagged (blank_answer_mismatch); fronts without blank markers are flagged
fitb_no_blank_marker (Q-style fitb variant).

Run after: sme_flashcards_scrape.py --courses <all>  (resumable skip then
refreshes course manifests from deck.json), then --registry.
"""
from __future__ import annotations
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from sme_flashcards_scrape import fitb_from_md  # noqa: E402

OUT = Path("/home/z/my-project/download/syllabai-resources/SME-Flashcards")


def main() -> int:
    decks = fitb_cards = rewritten = clean = 0
    flags: Counter = Counter()
    for df in sorted(OUT.glob("*/*/*/deck.json")):
        d = json.loads(df.read_text(encoding="utf-8"))
        changed = False
        for c in d["cards"]:
            if c["card_type"] != "fill_in_the_blanks":
                flags.update(c.get("flags", []))
                continue
            fitb_cards += 1
            ba = fitb_from_md(c["front_md"], c["back_md"])
            new_blanks = {"count": ba["count"], "answers": ba["answers"]}
            new_flags = sorted((set(c.get("flags", []))
                                - {"blank_answer_mismatch",
                                   "fitb_no_blank_marker"})
                               | ({ba["flag"]} if ba["flag"] else set()))
            if c.get("blanks") != new_blanks or c.get("flags") != new_flags:
                changed = True
            c["blanks"] = new_blanks
            c["flags"] = new_flags
            if not ba["flag"]:
                clean += 1
            else:
                flags[ba["flag"]] += 1
            for f in c["flags"]:
                flags["card:" + f] += 1
        if changed:
            rewritten += 1
            df.write_text(json.dumps(d, indent=1, ensure_ascii=False),
                          encoding="utf-8")
        decks += 1
    print(f"decks scanned={decks} fitb cards={fitb_cards} "
          f"decks rewritten={rewritten}")
    print(f"fitb clean (aligned)={clean}/{fitb_cards}")
    print("flag histogram:", dict(flags))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
