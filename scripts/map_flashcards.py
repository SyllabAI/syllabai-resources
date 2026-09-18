#!/usr/bin/env python3
"""
map_flashcards.py — map SME flashcards to official spec-point codes.

Chain (per course):
  1. SME spec_link inheritance — cards carrying relationships.spec_points
     (spcpt_*) inherit the course's existing spec_point_map.json join
     (tier/score preserved; method 'sme_spec_link_inherited').
  2. Content join fallback — cards with no resolvable links are matched on
     card text against the official pool using map_spec_points machinery:
       - keyword_definition / question_and_answer: back_md text,
         T1 verbatim / T2 near (>=0.93) / T3 section-anchored via deck slug
         numbers (>=0.80) / T4 fuzzy (>=0.85, flagged)
       - true_or_false / fill_in_the_blanks: NEVER text-joined (fronts are
         semantically inverted/blanked) -> recorded unmapped, not guessed
  3. spcpt ids absent from the notes-page harvest are reported
     (spcpt_not_in_harvest) — they stay unresolved until a harvest
     extension exists.

Outputs:
  SME-Flashcards/<course>/flashcard_spec_map.json
  Official-Specifications/parsed/_flashcard_map_report.json

Usage:
  python3 scripts/map_flashcards.py --courses igcse-biology-19
  python3 scripts/map_flashcards.py --all
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys_path = str(Path(__file__).parent)
if sys_path not in __import__("sys").path:
    __import__("sys").path.insert(0, sys_path)
import map_spec_points as msp  # noqa: E402 (QUALS, norm, tokens, joins)

BASE = Path(msp.BASE)
FC = BASE / "SME-Flashcards"
EQ = BASE / "SME-ExamQuestion"
PARSED = BASE / "Official-Specifications" / "parsed"
SCHEMA = "syllabai.sme-flashcard-spec-map/1.0"

TEXT_JOIN_TYPES = {"keyword_definition", "question_and_answer"}
AUTO_RATIO = 0.93      # T2
SECTION_RATIO = 0.80   # T3 (requires deck-slug/section agreement)
FUZZY_RATIO = 0.85     # T4 -> flagged
CONTAINMENT = 0.90     # T3 containment pass: card tokens covered by statement
MIN_CARD_TOKENS = 4    # guard against tiny fronts joining trivially
AMBIGUITY_GAP = 0.02   # runner-up within this -> ambiguous, skip


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def card_query_text(card: dict) -> str:
    md = card.get("back_md") or ""
    # strip cosmetic bold so normalized text matches official statements
    return md.replace("**", "")


def containment_join(course: str, qual_slug: str, card: dict, prep,
                     unit_key, tier_key) -> dict | None:
    """Section-anchored containment join (T-SPEC-1 tuning, 2026-09-18).

    Short card answers that are near-verbatim EXCERPTS of one official
    statement fail full-string SequenceMatcher (ratio penalises length
    mismatch). The validated resolver chain (sme_spcpt_resolve) already
    established token-containment/F1 + section boost as the honest scorer
    for exactly this case. Requirements, all structural — no T4 escape:
      - card answer has >= MIN_CARD_TOKENS content tokens
      - >= CONTAINMENT of those tokens covered by ONE official statement
      - that statement section-agrees with the deck slug (msp.section_agree)
      - runner-up is > AMBIGUITY_GAP behind (else ambiguous -> skip)
    Tier stays T3_section_anchored (weakest tier this evidence supports)."""
    d = msp.norm(card_query_text(card))
    if not d:
        return None
    dtoks = msp.tokens(d)
    if len(dtoks) < MIN_CARD_TOKENS:
        return None
    best, bs, runner = None, 0.0, 0.0
    for i in msp.top_candidates(d, dtoks, prep):
        p, ttoks, _ntext = prep[i]
        if not msp.section_agree(card.get("deck_slug") or "", p):
            continue
        cov = len(dtoks & ttoks) / len(dtoks)
        if cov > bs:
            best, bs, runner = p, cov, bs
        elif cov > runner:
            runner = cov
    if best is None or bs < CONTAINMENT:
        return None
    if runner and bs - runner < AMBIGUITY_GAP:
        return None
    unit = None
    if msp.QUALS[qual_slug]["struct"]:
        unit = msp.QUALS[qual_slug]["struct"]["spec_point_units"].get(best["id"])
    return {
        "official_id": best["id"], "official_code": best["official_code"],
        "tier": "T3_section_anchored", "score": round(bs, 4), "unit": unit,
        "method": "card_text_containment_join",
    }


def content_join(course: str, qual_slug: str, card: dict, prep, exact,
                 unit_key, tier_key) -> dict | None:
    """Regime-A-style join of card text onto official statements."""
    d = msp.norm(card_query_text(card))
    if not d:
        return None
    dtoks = msp.tokens(d)
    best, bs = None, 0.0
    if d in exact:
        best, bs = prep[exact[d]][0], 1.0
    else:
        for i in msp.top_candidates(d, dtoks, prep):
            p, _, ntext = prep[i]
            r = difflib.SequenceMatcher(None, d, ntext).ratio()
            if r > bs:
                bs, best = r, p
        if bs < FUZZY_RATIO:
            return None
    slug = card.get("deck_slug") or ""
    sec_ok = best is not None and msp.section_agree(slug, best)
    if bs >= 0.995:
        tier = "T1_verbatim"
    elif bs >= AUTO_RATIO:
        tier = "T2_near"
    elif sec_ok and bs >= SECTION_RATIO:
        tier = "T3_section_anchored"
    elif bs >= FUZZY_RATIO:
        tier = "T4_fuzzy"
    else:
        return None
    unit = None
    if msp.QUALS[qual_slug]["struct"]:
        unit = msp.QUALS[qual_slug]["struct"]["spec_point_units"].get(best["id"])
    entry = {
        "official_id": best["id"], "official_code": best["official_code"],
        "tier": tier, "score": round(bs, 4), "unit": unit,
        "method": "card_text_join",
    }
    if tier == "T4_fuzzy":
        entry["flag"] = "card text fuzzy join — review"
    return entry


def map_course(course: str) -> dict:
    eq_dir = EQ / course
    map_file = eq_dir / "spec_point_map.json"
    idx_file = eq_dir / "spec_point_index.json"
    qual = None
    mappings, idx_points = {}, {}
    if map_file.exists():
        mj = json.loads(map_file.read_text(encoding="utf-8"))
        qual = mj.get("qual")
        mappings = mj.get("mappings") or {}
    if idx_file.exists():
        ij = json.loads(idx_file.read_text(encoding="utf-8"))
        idx_points = ij.get("spec_points") or {}
    if qual is None:
        # course without a map (shouldn't happen; all 39 have maps)
        reg = json.loads((BASE / "Official-Specifications" / "manifest.json")
                         .read_text(encoding="utf-8"))
        qual = next((q["slug"] for q in reg["qualifications"]
                     if course in (q.get("sme_courses") or [])), None)

    unit_key, tier_key, blocked = msp.course_scope(course, qual)
    prep, exact = [], {}
    if not blocked:
        cands = msp.candidates_for(qual, unit_key, tier_key)
        prep = [(p, msp.tokens(p["text"]), msp.norm(p["text"])) for p in cands]
        for i, (p, _, ntext) in enumerate(prep):
            exact.setdefault(ntext, i)

    cards_out: dict = {}
    totals = Counter()
    totals.setdefault("containment_joined", 0)  # reported even when 0
    unresolved_spcpt: Counter = Counter()

    deck_files = sorted(FC.glob(f"{course}/*/*/deck.json"))
    for df in deck_files:
        deck = json.loads(df.read_text(encoding="utf-8"))
        deck_slug = deck["deck"]["topic_slug"] or ""
        for card in deck["cards"]:
            totals["cards"] += 1
            cid = card["id"]
            codes: list[dict] = []
            unresolved: list[str] = []
            for spcpt in card.get("spec_links", []):
                if spcpt in mappings:
                    m = dict(mappings[spcpt])
                    m["method"] = "sme_spec_link_inherited"
                    m["via_spcpt"] = spcpt
                    codes.append(m)
                    totals["spec_link_inherited"] += 1
                else:
                    unresolved.append(spcpt)
                    unresolved_spcpt["spcpt_not_in_harvest" if spcpt not in idx_points
                                     else "spcpt_unmapped_in_course_map"] += 1
            entry = {}
            if codes:
                totals["cards_with_codes"] += 1
                entry["codes"] = codes
            if blocked:
                if card.get("spec_links"):
                    entry["blocked_reason"] = "parse_gap"
                    totals["cards_blocked"] += 1
                else:
                    totals["cards_unmapped"] += 1
            elif not codes:
                if card["card_type"] in TEXT_JOIN_TYPES and not unresolved:
                    cj = content_join(course, qual, {**card, "deck_slug": deck_slug},
                                      prep, exact, unit_key, tier_key)
                    if cj:
                        entry["codes"] = [cj]
                        if cj.get("flag"):
                            entry["flags"] = [cj["flag"]]
                        totals["content_joined"] += 1
                        totals["cards_with_codes"] += 1
                    else:
                        cj2 = containment_join(course, qual,
                                               {**card, "deck_slug": deck_slug},
                                               prep, unit_key, tier_key)
                        if cj2:
                            entry["codes"] = [cj2]
                            totals["containment_joined"] += 1
                            totals["content_joined"] += 1
                            totals["cards_with_codes"] += 1
                        else:
                            entry["reason"] = "card text below safe join threshold"
                            totals["cards_unmapped"] += 1
                elif card["card_type"] in TEXT_JOIN_TYPES and unresolved:
                    entry["reason"] = "spec links unresolvable; text join skipped to avoid double-anchoring"
                    totals["cards_unmapped"] += 1
                elif card["card_type"] not in TEXT_JOIN_TYPES and not card.get("spec_links"):
                    entry["reason"] = f"no spec links; {card['card_type']} not text-joinable"
                    totals["cards_unmapped"] += 1
                else:
                    entry["reason"] = "no resolvable spec links"
                    totals["cards_unmapped"] += 1
            if unresolved:
                entry["unresolved_spcpt"] = unresolved
            if entry or codes:
                cards_out[cid] = entry

    result = {
        "schema": SCHEMA,
        "generated_utc": now_utc(),
        "course": course,
        "qual": qual,
        "totals": {
            "cards": totals["cards"],
            "cards_with_codes": totals["cards_with_codes"],
            "spec_link_inherited": totals["spec_link_inherited"],
            "content_joined": totals["content_joined"],
            "containment_joined": totals["containment_joined"],
            "cards_unmapped": totals["cards_unmapped"],
            "cards_blocked": totals["cards_blocked"],
        },
        "unresolved_spcpt": dict(unresolved_spcpt),
        "cards": cards_out,
    }
    (FC / course / "flashcard_spec_map.json").write_text(
        json.dumps(result, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"[{course}] cards={totals['cards']} coded={totals['cards_with_codes']} "
          f"(link {totals['spec_link_inherited']} + text {totals['content_joined']} "
          f"[containment {totals['containment_joined']}]) "
          f"unmapped={totals['cards_unmapped']} unresolved={dict(unresolved_spcpt)}",
          flush=True)
    return {"course": course, "qual": qual, **result["totals"],
            "unresolved_spcpt": dict(unresolved_spcpt)}


def main() -> int:
    import sys
    ap = argparse.ArgumentParser()
    ap.add_argument("--courses", default="")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    sys.path.insert(0, str(Path(__file__).parent))
    from sme_flashcards_scrape import REGISTRY, MISSING

    if args.all:
        courses = [c for c in REGISTRY if REGISTRY[c].get("status") != MISSING]
    else:
        courses = [c.strip() for c in args.courses.split(",") if c.strip()]
    reports = []
    for c in courses:
        if not (FC / c).exists():
            print(f"[{c}] no flashcards scraped — skipped")
            continue
        reports.append(map_course(c))
    PARSED.mkdir(parents=True, exist_ok=True)
    (PARSED / "_flashcard_map_report.json").write_text(
        json.dumps({"schema": "syllabai.flashcard-map-report/1.0",
                    "generated_utc": now_utc(), "courses": reports},
                   indent=1, ensure_ascii=False), encoding="utf-8")
    tot = Counter()
    for r in reports:
        for k in ("cards", "cards_with_codes", "spec_link_inherited",
                  "content_joined", "cards_unmapped", "cards_blocked"):
            tot[k] += r[k]
    print("TOTAL", dict(tot))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
