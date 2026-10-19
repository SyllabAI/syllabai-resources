#!/usr/bin/env python3
"""T-SME-FLASH-1 verification gates for the SME-Flashcards corpus.

Gates:
  G1 deck counts vs sitemap-census expectations (per course, warn-only if
     SME added/removed decks since census — recorded, not failed)
  G2 every card has id + non-empty front/back md (except explicit
     empty_front/empty_back flags)
  G3 card types within the observed SME set (4 kinds + unknown flagged)
  G4 fill_in_the_blanks: blank/answer counts equal OR mismatch flag present
     (mismatches are recorded, never guessed)
  G5 equations: blocks carry latex OR math_fallback_alt flag present
  G6 spec_links: only spcpt_ ids; per-course spec-link rate recorded
  G7 asset failures == 0; deck fetch failures == 0
  G8 stable ids unique per deck; fl_/flst_/spcpt_ namespaces respected
Writes verdict + summary to stdout; exit 1 on hard failures.
"""
from __future__ import annotations
import json, re, sys
from collections import Counter
from pathlib import Path

BASE = Path("/home/z/my-project/download/syllabai-resources")
OUT = BASE / "SME-Flashcards"
sys.path.insert(0, str(BASE / "scripts"))
from sme_flashcards_scrape import REGISTRY, MISSING  # noqa: E402

KNOWN_TYPES = {"keyword_definition", "question_and_answer",
               "true_or_false", "fill_in_the_blanks", "unknown"}

def main() -> int:
    hard, warns = [], []
    per_course = {}
    tot = Counter()
    manifests = sorted(p for p in OUT.glob("*/manifest.json") if p.parent != OUT)
    for mf in manifests:
        slug = mf.parent.name
        m = json.loads(mf.read_text(encoding="utf-8"))
        reg = REGISTRY.get(slug) or {}
        decks = m["totals"]["decks"]; cards = m["totals"]["cards"]
        exp = m.get("deck_count_expected")
        if exp and decks != exp:
            warns.append(f"{slug}: decks {decks} != census {exp}")
        if m["totals"]["deck_failures"]:
            hard.append(f"{slug}: {m['totals']['deck_failures']} deck fetch failures")
        if m["totals"]["asset_failures"]:
            hard.append(f"{slug}: {m['totals']['asset_failures']} asset failures")
        stats = {"decks": decks, "cards": cards, "types": m["totals"]["card_types"],
                 "spec": 0, "fitb": 0, "fitb_bad": 0, "eq": 0, "eq_bad": 0,
                 "flags": Counter(), "ids": 0}
        for df in sorted(OUT.glob(f"{slug}/*/*/deck.json")):
            d = json.loads(df.read_text(encoding="utf-8"))
            seen = set()
            for c in d["cards"]:
                stats["ids"] += 1
                if not (c.get("id") or "").startswith("fl_"):
                    hard.append(f"{slug}/{df.parent.name}: bad card id {c.get('id')}")
                if c["id"] in seen:
                    hard.append(f"{slug}/{df.parent.name}: dup id {c['id']}")
                seen.add(c["id"])
                if (c.get("set_id") and not c["set_id"].startswith("flst_")):
                    hard.append(f"{slug}: bad set id {c['set_id']}")
                for s in c.get("spec_links", []):
                    if not s.startswith("spcpt_"):
                        hard.append(f"{slug}: bad spec id {s}")
                if c.get("spec_links"):
                    stats["spec"] += 1
                if c["card_type"] not in KNOWN_TYPES:
                    hard.append(f"{slug}: unknown card_type {c['card_type']}")
                if not c["front_md"].strip() and "empty_front" not in c["flags"]:
                    hard.append(f"{slug}: empty front on {c['id']}")
                if not c["back_md"].strip() and "empty_back" not in c["flags"]:
                    hard.append(f"{slug}: empty back on {c['id']}")
                for f in c["flags"]:
                    stats["flags"][f] += 1
                    if f.startswith(("unknown_block", "unknown_card_type")):
                        hard.append(f"{slug}: {c['id']} {f}")
                if c["card_type"] == "fill_in_the_blanks":
                    stats["fitb"] += 1
                    b = c.get("blanks") or {}
                    if b.get("count", 0) != len(b.get("answers", [])):
                        stats["fitb_bad"] += 1
                        if "blank_answer_mismatch" not in c["flags"] and \
                           "fitb_no_blank_marker" not in c["flags"]:
                            hard.append(f"{slug}: fitb mismatch unflagged {c['id']}")
                inline_math = sum(md.count("$") // 2
                                  for md in (c["front_md"], c["back_md"]))
                stats["eq"] += inline_math
                for blocks in (c["front_blocks"], c["back_blocks"]):
                    for b in blocks:
                        if b.get("type") == "equation":
                            stats["eq"] += 1
                            if not b.get("latex") and "math_fallback_alt" not in c["flags"]:
                                stats["eq_bad"] += 1
                                hard.append(f"{slug}: equation w/o latex {c['id']}")
                        if b.get("type", "").startswith("raw_"):
                            pass  # flagged above
        tot.update({"cards": cards, "decks": decks, "spec": stats["spec"],
                    "fitb": stats["fitb"], "fitb_bad": stats["fitb_bad"],
                    "eq": stats["eq"], "eq_bad": stats["eq_bad"]})
        per_course[slug] = stats
    print("=" * 72)
    print(f"{'course':46} {'decks':>5} {'cards':>6} {'spec%':>6} {'fitb':>5} {'fitb!':>5} {'eq':>4} {'flags':>5}")
    for slug, s in sorted(per_course.items()):
        specp = f"{100 * s['spec'] / s['cards']:.0f}%" if s["cards"] else "-"
        nfl = sum(s["flags"].values())
        print(f"{slug:46} {s['decks']:5} {s['cards']:6} {specp:>6} {s['fitb']:5} {s['fitb_bad']:5} {s['eq']:4} {nfl:5}")
    print("-" * 72)
    cards = tot["cards"]
    print(f"TOTAL decks={tot['decks']} cards={cards} spec_linked={tot['spec']} "
          f"({100 * tot['spec'] / max(cards, 1):.0f}%) fitb={tot['fitb']} "
          f"(mismatch {tot['fitb_bad']}) equations={tot['eq']} (no-latex {tot['eq_bad']})")
    print()
    if warns:
        print(f"WARNINGS ({len(warns)}):")
        for w in warns: print("  ~", w)
    if hard:
        print(f"HARD FAILURES ({len(hard)}):")
        for h in hard[:40]: print("  !", h)
        if len(hard) > 40: print(f"  ... and {len(hard) - 40} more")
        return 1
    print("ALL GATES PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
