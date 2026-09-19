#!/usr/bin/env python3
"""
T-SME-FLASH-1 — SME flashcards corpus scraper (Edexcel courses; 34 of 39 have decks).

For each course: fetch the flashcards landing page, decode the deck index from
__NEXT_DATA__ (pageProps.sections + pageProps.topics where
has_published_flashcard_sets), then fetch each deck page and parse
pageProps.flashcards — TipTap documents on front/back.

Card anatomy preserved for faithful rendering:
- id (fl_*), set id (flst_*), attributes.type kept first-class:
  keyword_definition | question_and_answer | true_or_false | fill_in_the_blanks
- front/back -> typed blocks (reuses sme_notes_scrape.to_blocks) + md render
  (bold/italic/underline/sub/sup preserved; bulletList preserved; textAlign
  center is cosmetic and dropped)
- Wiris equation nodes: flashcards carry attrs.src = data-URI SVG whose HTML
  comment embeds the MathML — extracted into attrs.mathml so the shared
  MathML2Latex (sme_examq_scrape) works unchanged; latex + raw mathml + alt
  all recorded (lossless re-processing)
- fill_in_the_blanks: blank = whitespace-only run with underline mark on the
  front; back repeats the sentence with the answer bolded. We record
  blanks/answers counts + answers text and flag mismatches (never guessed)
- relationships.spec_points -> SME spcpt_* anchors recorded verbatim
  (population varies by course; join to the spcpt_ harvest happens later)
- images -> per-deck assets/ via sme_notes_scrape.fetch_assets (hash names)

Output:
  SME-Flashcards/
    manifest.json            global (registry incl. 5 courses with no SME decks)
    README.md
    {course_slug}/manifest.json
    {course_slug}/{section-slug}/{deck-slug}/deck.json + cards.md + assets/

Resumable: existing deck.json skipped unless --force. No raw-HTML caching
(pages parsed in memory; disk budget is small). Cambridge/CAIE extension =
new REGISTRY entries; scrapers are registry-driven.

Usage:
  python3 scripts/sme_flashcards_scrape.py --courses igcse-biology-19 [--limit 3]
  python3 scripts/sme_flashcards_scrape.py --all --workers 4
  python3 scripts/sme_flashcards_scrape.py --registry   # rebuild global manifest+README
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import re
import sys
import time
import urllib.parse
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import sme_examq_scrape as eq  # noqa: E402 (http_get, parse_next_data, M2L)
import sme_notes_scrape as notes  # noqa: E402 (to_blocks, blocks_to_md, assets)

BASE = Path("/home/z/my-project/download/syllabai-resources")
OUT = BASE / "SME-Flashcards"
SCHEMA = "syllabai.sme-flashcard-deck/1.0"

# --------------------------------------------------------------------- registry
# SME flashcard path per course slug (after https://www.savemyexams.com/).
# expected_decks = sitemap census 2026-09-17 (deck URLs minus landing page).
# 5 of the 39 courses have no flashcards on SME — recorded, never synthesized.
MISSING = "missing_on_sme"
MISSING_REASON = "no flashcard decks on SME (sitemap census 2026-09-17)"

REGISTRY: dict[str, dict] = {
    # IAL
    "ial-biology-18":                {"path": "international-a-level/biology/edexcel/18", "expected_decks": 28},
    "ial-chemistry-17":              {"path": "international-a-level/chemistry/edexcel/17", "expected_decks": 39},
    "ial-physics-19":                {"path": "international-a-level/physics/edexcel/19", "expected_decks": 37},
    "ial-maths-20-pure-1":           {"path": "international-a-level/maths/edexcel/20/pure-1", "expected_decks": 13},
    "ial-maths-20-pure-2":           {"path": "international-a-level/maths/edexcel/20/pure-2", "expected_decks": 12},
    "ial-maths-20-pure-3":           {"path": "international-a-level/maths/edexcel/20/pure-3", "expected_decks": 12},
    "ial-maths-20-pure-4":           {"path": "international-a-level/maths/edexcel/20/pure-4", "expected_decks": 12},
    "ial-maths-20-mechanics-1":      {"path": "international-a-level/maths/edexcel/20/mechanics-1", "expected_decks": 10},
    "ial-maths-20-mechanics-2":      {"path": "international-a-level/maths/edexcel/20/mechanics-2", "expected_decks": 8},
    "ial-maths-20-statistics-1":     {"path": "international-a-level/maths/edexcel/20/statistics-1", "expected_decks": 7},
    "ial-maths-20-statistics-2":     {"path": "international-a-level/maths/edexcel/20/statistics-2", "expected_decks": 7},
    "ial-maths-20-decision-1":       {"path": "international-a-level/maths/edexcel/20/decision-1", "expected_decks": 9},
    # IGCSE sciences (linear + modular + double award)
    "igcse-biology-19":              {"path": "igcse/biology/edexcel/19", "expected_decks": 21},
    "igcse-chemistry-19":            {"path": "igcse/chemistry/edexcel/19", "expected_decks": 28},
    "igcse-physics-19":              {"path": "igcse/physics/edexcel/19", "expected_decks": 24},
    "igcse-biology-modular-24-unit-1":    {"path": "igcse/biology/edexcel/modular/24/unit-1", "expected_decks": 8},
    "igcse-biology-modular-24-unit-2":    {"path": "igcse/biology/edexcel/modular/24/unit-2", "expected_decks": 13},
    "igcse-chemistry-modular-24-unit-1":  {"path": "igcse/chemistry/edexcel/modular/24/unit-1", "expected_decks": 14},
    "igcse-chemistry-modular-24-unit-2":  {"path": "igcse/chemistry/edexcel/modular/24/unit-2", "expected_decks": 14},
    "igcse-physics-modular-24-unit-1":    {"path": "igcse/physics/edexcel/modular/24/unit-1", "expected_decks": 12},
    "igcse-physics-modular-24-unit-2":    {"path": "igcse/physics/edexcel/modular/24/unit-2", "expected_decks": 12},
    "igcse-science-double-award-17-biology":   {"path": "igcse/science/edexcel/double-award/17/biology", "expected_decks": 20},
    "igcse-science-double-award-17-chemistry": {"path": "igcse/science/edexcel/double-award/17/chemistry", "expected_decks": 22},
    "igcse-science-double-award-17-physics":   {"path": "igcse/science/edexcel/double-award/17/physics", "expected_decks": 18},
    # IGCSE humanities / others
    "igcse-business-19":             {"path": "igcse/business/edexcel/19", "expected_decks": 25},
    "igcse-economics-17":            {"path": "igcse/economics/edexcel/17", "expected_decks": 16},
    "igcse-geography-19":            {"path": "igcse/geography/edexcel/19", "expected_decks": 38},
    "igcse-ict-17":                  {"path": "igcse/ict/edexcel/17", "expected_decks": 21},
    "igcse-english-literature-16":   {"path": "igcse/english-literature/edexcel/16", "expected_decks": 15},
    # IGCSE maths
    "igcse-maths-a-18-foundation":   {"path": "igcse/maths/edexcel/a/18/foundation", "expected_decks": 27},
    "igcse-maths-a-18-higher":       {"path": "igcse/maths/edexcel/a/18/higher", "expected_decks": 58},
    "igcse-maths-a-modular-24-higher-unit-1": {"path": "igcse/maths/edexcel/a-modular/24/higher-unit-1", "expected_decks": 32},
    "igcse-maths-a-modular-24-higher-unit-2": {"path": "igcse/maths/edexcel/a-modular/24/higher-unit-2", "expected_decks": 27},
    "igcse-further-maths-19":        {"path": "igcse/further-maths/edexcel/19", "expected_decks": 19},
    # honest gaps
    "ial-further-maths-18-further-pure-1": {"status": MISSING, "reason": MISSING_REASON},
    "igcse-accounting-17-financial-statements": {"status": MISSING, "reason": MISSING_REASON},
    "igcse-accounting-17-introduction-to-bookkeeping-and-accounting": {"status": MISSING, "reason": MISSING_REASON},
    "igcse-maths-a-modular-24-foundation-unit-1": {"status": MISSING, "reason": MISSING_REASON},
    "igcse-maths-a-modular-24-foundation-unit-2": {"status": MISSING, "reason": MISSING_REASON},
    # T-SME-11 (2026-09-19): the 10 missing Edexcel courses
    "igcse-english-language-a-16-paper-1-non-fiction-texts-and-transactional-writing":
        {"path": "igcse/english-language/edexcel/a/16/paper-1-non-fiction-texts-and-transactional-writing", "expected_decks": 3},
    "igcse-english-language-a-16-paper-2-poetry-and-prose-texts-and-imaginative-writing":
        {"path": "igcse/english-language/edexcel/a/16/paper-2-poetry-and-prose-texts-and-imaginative-writing", "expected_decks": 3},
    "igcse-maths-b-16":              {"path": "igcse/maths/edexcel/b/16", "expected_decks": 62},
    "igcse-english-language-a-16-paper-3-coursework": {"status": MISSING, "reason": MISSING_REASON},
    "igcse-science-double-award-modular-24-biology-unit-1": {"status": MISSING, "reason": MISSING_REASON},
    "igcse-science-double-award-modular-24-biology-unit-2": {"status": MISSING, "reason": MISSING_REASON},
    "igcse-science-double-award-modular-24-chemistry-unit-1": {"status": MISSING, "reason": MISSING_REASON},
    "igcse-science-double-award-modular-24-chemistry-unit-2": {"status": MISSING, "reason": MISSING_REASON},
    "igcse-science-double-award-modular-24-physics-unit-1": {"status": MISSING, "reason": MISSING_REASON},
    "igcse-science-double-award-modular-24-physics-unit-2": {"status": MISSING, "reason": MISSING_REASON},
}


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ------------------------------------------------------------------ discovery
def deck_index(sme_path: str) -> list[dict]:
    """Decode deck list from the course flashcards landing page."""
    base = f"https://www.savemyexams.com/{sme_path}/"
    pp = eq.parse_next_data(eq.http_get(f"{base}flashcards/"))
    secs = {s["id"]: (s.get("attributes") or {})
            for s in pp.get("sections") or []}
    decks = []
    for t in pp.get("topics") or []:
        a = t.get("attributes") or {}
        if not a.get("has_published_flashcard_sets"):
            continue
        sec = secs.get(((t.get("relationships") or {}).get("section", {})
                        .get("data", {}) or {}).get("id"), {})
        decks.append({
            "url": f"{base}flashcards/{sec.get('slug')}/{a.get('slug')}/",
            "section_slug": sec.get("slug") or "ungrouped",
            "section_name": sec.get("name"),
            "topic_slug": a.get("slug"),
            "title": a.get("name"),
            "order": a.get("order"),
        })
    decks.sort(key=lambda d: (d["section_slug"] or "", d["topic_slug"] or ""))
    return decks


# ------------------------------------------------------------------ card parse
def mathml_from_attrs(attrs: dict) -> str | None:
    m = attrs.get("mathml")
    if m:
        return m
    src = attrs.get("src") or ""
    if src.startswith("data:"):
        try:
            dec = urllib.parse.unquote(src.split(",", 1)[1])
            mm = re.search(r"<!--MathML:\s*(<math.*?</math>)\s*-->", dec, re.S)
            if mm:
                return mm.group(1)
        except Exception:  # noqa: BLE001
            return None
    return None


def normalize_equations(nodes) -> None:
    """Copy MathML out of Wiris data-URI src into attrs.mathml (in place)."""
    for n in nodes or []:
        if not isinstance(n, dict):
            continue
        if n.get("type") == "equation":
            a = n.setdefault("attrs", {})
            mm = mathml_from_attrs(a)
            if mm:
                a["mathml"] = mm
        normalize_equations(n.get("content"))


WS_BLANKS = "\u2001\u2003\u2009 \t\u00a0"

_BLANK_RE = re.compile(
    f"(?:<u>[{WS_BLANKS}]*</u>)"                     # econ: <u> em-quad run
    "|(?:\\*\\*[.\\uff3f_\\u00b7\\u2026\\s]{4,}\\*\\*)"  # physics: bold dots
    "|(?<![\\w$])(?:[\\uff3f_]{2,}|\\.{4,})(?![\\w$])")  # SDA: bare filler

_MARKUP_RE = re.compile(r"</?u>|</?sub>|</?sup>|</?em>|</?strong>|\*\*|`")


def fitb_from_md(front_md: str, back_md: str) -> dict:
    """fill_in_the_blanks via front/back alignment.

    The back restates the front sentence with each blank replaced by its
    answer, so we turn the front into a regex (blank -> lazy capture) and
    match it against the back. Returns {'count', 'answers', 'flag'} where
    flag is None | 'fitb_no_blank_marker' | 'blank_answer_mismatch'.
    Never guesses: unmatched structure is flagged, not forced.
    """
    n = [0]

    def _sub(_m):
        n[0] += 1
        return f"\x00{n[0]}\x00"

    front_md = front_md.strip()
    back_md = back_md.strip()
    pat_src = _BLANK_RE.sub(_sub, front_md)
    if n[0] == 0:
        return {"count": 0, "answers": [],
                "flag": "fitb_no_blank_marker"}
    # cosmetic bold varies between front/back (emphasis vs plain) — strip it
    # on both sides AFTER blank sentinels are in place (keeps dot-blanks)
    pat_src = pat_src.replace("**", "")
    back_norm = back_md.replace("**", "")
    segs = re.split("\x00(?:\\d+)\x00", pat_src)
    if len(segs) != n[0] + 1:
        return {"count": n[0], "answers": [],
                "flag": "blank_answer_mismatch"}
    regex = "(.*?)".join(re.escape(s) for s in segs)
    # SME front/back pairs differ in spacing around blanks ('60 °C' vs
    # '60°C', ' %' vs '%') — whitespace-flexible matching, never content
    # guessing (hard failures still flagged)
    regex = regex.replace("\\ ", r"\s*")
    m = re.fullmatch(regex, back_norm, re.S)
    if not m:
        # Template variant (eng-lit/ICT): '**Fill in the gap:** "quote"'
        # front vs '**Answer:** "quote"' back, citation lines dropped.
        # Deterministic normalization: strip known preambles + standalone
        # italic citation lines, then retry; else align quoted spans.
        pre = re.compile(r"^(?:Fill in the (?:gap|blank)|Answer):?\s*",
                         re.M)
        cite = re.compile(r"^\*[^*\n]+\*\s*$", re.M)
        f2 = cite.sub("", pre.sub("", pat_src.replace("**", "")))
        b2 = cite.sub("", pre.sub("", back_norm))
        m = re.fullmatch("(.*?)".join(re.escape(s) for s in
                                      re.split("\x00(?:\\d+)\x00", f2))
                         .replace("\\ ", r"\s*"), b2, re.S)
    if not m:
        fq = re.findall(r'"([^"]*)"', pat_src.replace("**", ""))
        bq = re.findall(r'"([^"]*)"', back_norm)
        if fq and len(fq) == len(bq) and any("\x00" in q for q in fq):
            ok = True
            answers = []
            for qf, qb in zip(fq, bq):
                if "\x00" not in qf:
                    continue
                parts = re.split("\x00(?:\\d+)\x00", qf)
                if len(parts) != qf.count("\x00") // 2 + 1:
                    ok = False
                    break
                mm = re.fullmatch("(.*?)".join(re.escape(p) for p in parts)
                                  .replace("\\ ", r"\s*"), qb, re.S)
                if not mm:
                    ok = False
                    break
                answers += [_MARKUP_RE.sub("", g).strip()
                            for g in mm.groups()]
            if ok and answers and all(answers):
                return {"count": len(answers), "answers": answers,
                        "flag": None}
        return {"count": n[0], "answers": [],
                "flag": "blank_answer_mismatch"}
    answers = [_MARKUP_RE.sub("", g).strip() for g in m.groups()]
    if any(not a for a in answers) or len(answers) != n[0]:
        return {"count": n[0], "answers": [a for a in answers if a],
                "flag": "blank_answer_mismatch"}
    return {"count": n[0], "answers": answers, "flag": None}


def side_blocks(tiptap: list, ctx: dict) -> list:
    return notes.to_blocks(tiptap, ctx)


def card_record(card: dict, asset_urls: set) -> dict:
    a = card.get("attributes") or {}
    rel = card.get("relationships") or {}
    spec_links = [sp.get("id") for sp in
                  (rel.get("spec_points", {}).get("data") or [])
                  if sp.get("id")]
    flags: list[str] = []

    def asset_fn(attrs: dict):
        url = notes.fig_url(attrs or {})
        if not url:
            return None, None
        name = notes.asset_name_for(url)
        asset_urls.add(url)
        return url, name

    ctx = {"asset_fn": asset_fn, "equations": []}
    front = a.get("front") or []
    back = a.get("back") or []
    normalize_equations(front)
    normalize_equations(back)
    fb = side_blocks(front, ctx)
    bb = side_blocks(back, ctx)
    if not fb:
        flags.append("empty_front")
    if not bb:
        flags.append("empty_back")
    for blocks in (fb, bb):
        for b in blocks:
            if b.get("type", "").startswith("raw_"):
                flags.append("unknown_block:" + b["type"])
            if b.get("type") == "equation" and not b.get("latex"):
                flags.append("math_fallback_alt")

    ctype = a.get("type") or "unknown"
    if ctype == "unknown":
        flags.append("unknown_card_type")
    rec = {
        "id": card.get("id"),
        "card_type": ctype,
        "order": a.get("order"),
        "set_id": (rel.get("flashcard_set", {}).get("data", {}) or {}).get("id"),
        "front_blocks": fb,
        "back_blocks": bb,
        "front_md": notes.blocks_to_md(fb, asset_prefix=""),
        "back_md": notes.blocks_to_md(bb, asset_prefix=""),
        "spec_links": spec_links,
        "flags": sorted(set(flags)),
    }
    if ctype == "fill_in_the_blanks":
        ba = fitb_from_md(rec["front_md"], rec["back_md"])
        rec["blanks"] = {"count": ba["count"], "answers": ba["answers"]}
        if ba["flag"]:
            rec["flags"] = sorted(set(rec["flags"]) | {ba["flag"]})
    return rec


def cards_md(deck: dict) -> str:
    out = [f"# {deck['title'] or deck['topic_slug']}\n",
           f"Course: {deck['course_slug']} · Section: "
           f"{deck['section_name'] or deck['section_slug']}\n",
           f"Source: {deck['url']}\n"]
    for i, c in enumerate(deck["cards"], 1):
        out.append(f"\n## Card {i} — {c['card_type']} (`{c['id']}`)\n")
        out.append("**FRONT**\n\n" + (c["front_md"] or "*(empty)*") + "\n")
        out.append("**BACK**\n\n" + (c["back_md"] or "*(empty)*") + "\n")
        if c.get("blanks"):
            out.append(f"*Blanks: {c['blanks']['count']} — "
                       f"answers: {c['blanks']['answers']}*\n")
        if c["spec_links"]:
            out.append("Spec links: " + " ".join(f"`{s}`"
                                                 for s in c["spec_links"]) + "\n")
        if c["flags"]:
            out.append("Flags: " + ", ".join(c["flags"]) + "\n")
    return "\n".join(out) + "\n"


# ------------------------------------------------------------------ scraping
def scrape_deck(course_slug: str, meta: dict, delay: float,
                force: bool) -> dict:
    deck_dir = (OUT / course_slug / (meta["section_slug"] or "ungrouped")
                / (meta["topic_slug"] or "deck"))
    deck_file = deck_dir / "deck.json"
    if deck_file.exists() and not force:
        try:
            old = json.loads(deck_file.read_text(encoding="utf-8"))
            return {"slug": meta["topic_slug"], "cards": len(old.get("cards", [])),
                    "flags": sum(len(c.get("flags", []))
                                 for c in old.get("cards", [])),
                    "types": old.get("card_types") or {},
                    "spec_linked": old.get("spec_link_cards", 0),
                    "assets": 0, "asset_failures": 0,
                    "skipped": True, "url": meta["url"], "error": None}
        except Exception:  # noqa: BLE001
            pass
    time.sleep(delay)
    try:
        pp = eq.parse_next_data(eq.http_get(meta["url"]))
    except Exception as e:  # noqa: BLE001
        return {"slug": meta["topic_slug"], "cards": 0, "flags": 0,
                "skipped": False, "url": meta["url"],
                "error": str(e)[:200]}
    raw_cards = pp.get("flashcards") or []
    bc = (pp.get("breadcrumbs") or {}).get("titles") or {}
    asset_urls: set = set()
    cards, failures = [], []
    for rc in raw_cards:
        try:
            cards.append(card_record(rc, asset_urls))
        except Exception as e:  # noqa: BLE001
            failures.append({"card_id": rc.get("id"), "error": str(e)[:200]})
    deck = {
        "schema": SCHEMA,
        "generated_utc": now_utc(),
        "course_slug": course_slug,
        "deck": {
            "url": meta["url"],
            "section_slug": meta["section_slug"],
            "section_name": meta["section_name"],
            "topic_slug": meta["topic_slug"],
            "title": meta["title"] or bc.get("topic"),
            "order": meta["order"],
        },
        "card_count": len(cards),
        "card_types": dict(Counter(c["card_type"] for c in cards)),
        "spec_link_cards": sum(1 for c in cards if c["spec_links"]),
        "asset_failures": [],
        "card_failures": failures,
        "cards": cards,
    }
    deck_dir.mkdir(parents=True, exist_ok=True)
    if asset_urls:
        plan, fails = notes.fetch_assets(sorted(asset_urls),
                                         deck_dir / "assets", workers=4)
        deck["asset_failures"] = fails
        for c in deck["cards"]:
            pass  # block file names already deterministic per url
    deck_file.write_text(json.dumps(deck, indent=1, ensure_ascii=False),
                         encoding="utf-8")
    (deck_dir / "cards.md").write_text(
        cards_md({**meta, "course_slug": course_slug, "cards": cards}),
        encoding="utf-8")
    return {"slug": meta["topic_slug"], "cards": len(cards),
            "flags": sum(len(c["flags"]) for c in cards),
            "spec_linked": deck["spec_link_cards"],
            "types": deck["card_types"],
            "assets": len(asset_urls),
            "asset_failures": len(fails) if asset_urls else 0,
            "skipped": False, "url": meta["url"],
            "error": None}


def scrape_course(slug: str, workers: int, delay: float,
                  limit: int, force: bool) -> dict:
    reg = REGISTRY[slug]
    course_dir = OUT / slug
    course_dir.mkdir(parents=True, exist_ok=True)
    decks = deck_index(reg["path"])
    if limit:
        decks = decks[:limit]
    results, failures = [], []
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(scrape_deck, slug, d, delay, force) for d in decks]
        for i, f in enumerate(cf.as_completed(futs), 1):
            r = f.result()
            results.append(r)
            if r["error"]:
                failures.append({"deck": r["slug"], "url": r["url"],
                                 "error": r["error"]})
            print(f"  [{slug}] {i}/{len(decks)} {r['slug']}: "
                  f"{'ERR ' + (r['error'] or '')[:60] if r['error'] else str(r['cards']) + ' cards'}",
                  flush=True)
    types: Counter = Counter()
    for r in results:
        types.update(r.get("types") or {})
    manifest = {
        "schema": "syllabai.sme-flashcards-course/1.0",
        "generated_utc": now_utc(),
        "course_slug": slug,
        "sme_path": reg["path"],
        "base_url": f"https://www.savemyexams.com/{reg['path']}/flashcards/",
        "deck_count_expected": reg.get("expected_decks"),
        "deck_count_actual": len(decks),
        "totals": {
            "decks": len(results),
            "cards": sum(r["cards"] for r in results),
            "card_types": dict(types),
            "flags": sum(r["flags"] for r in results),
            "assets": sum(r.get("assets", 0) for r in results),
            "asset_failures": sum(r.get("asset_failures", 0)
                                  for r in results),
            "deck_failures": len(failures),
        },
        "decks": sorted(results, key=lambda r: r["slug"]),
        "failures": failures,
    }
    (course_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"[{slug}] decks={len(results)} cards={manifest['totals']['cards']} "
          f"types={dict(types)} failures={len(failures)}", flush=True)
    return {"slug": slug, **manifest["totals"],
            "expected": reg.get("expected_decks")}


# ------------------------------------------------------------------ outputs
def write_global(course_summaries: list[dict]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    totals = {
        "courses_active": len([s for s in course_summaries]),
        "decks": sum(s["decks"] for s in course_summaries),
        "cards": sum(s["cards"] for s in course_summaries),
        "flags": sum(s["flags"] for s in course_summaries),
        "deck_failures": sum(s["deck_failures"] for s in course_summaries),
    }
    man = {
        "schema": "syllabai.sme-flashcards/1.0",
        "generated_utc": now_utc(),
        "source": {
            "provider": "Save My Exams",
            "registry": "scripts/sme_flashcards_scrape.py REGISTRY",
            "license": "operator-authorized; see LICENSE-DATA.md "
                       "(SME attestation)",
        },
        "totals": totals,
        "registry": REGISTRY,
        "courses": {s["slug"]: s for s in course_summaries},
    }
    (OUT / "manifest.json").write_text(
        json.dumps(man, indent=1, ensure_ascii=False), encoding="utf-8")


def write_readme() -> None:
    lines = [
        "# SME Flashcards corpus (Edexcel)",
        "",
        "Scraped from Save My Exams flashcards decks via "
        "`scripts/sme_flashcards_scrape.py` (registry-driven; see that file "
        "for the course registry incl. courses with no SME decks).",
        "",
        "- Layout: `{course}/{section}/{deck}/deck.json` (schema "
        "`syllabai.sme-flashcard-deck/1.0`) + `cards.md` + `assets/`",
        "- Card types kept first-class: keyword_definition, "
        "question_and_answer, true_or_false, fill_in_the_blanks",
        "- front/back typed TipTap blocks (+ md render); bold/italic/"
        "underline/sub/sup preserved",
        "- Math: Wiris MathML -> KaTeX latex (raw mathml + alt retained)",
        "- fill_in_the_blanks: blanks counted, answers extracted; "
        "blank_answer_mismatch flagged (never guessed)",
        "- `spec_links`: SME spcpt_* anchors as printed (join to "
        "spec_point_index harvest happens at mapping stage)",
        "- Operator authorization: LICENSE-DATA.md (SME attestation)",
        "",
        "Global manifest: `manifest.json` (registry + per-course totals).",
        "",
    ]
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("--courses", default="",
                    help="comma-separated course slugs")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--limit", type=int, default=0,
                    help="max decks per course (smoke test)")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--delay", type=float, default=0.5)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--registry", action="store_true",
                    help="rebuild global manifest+README from disk only")
    args = ap.parse_args()

    if args.registry:
        summaries = []
        for mf in sorted(OUT.glob("*/manifest.json")):
            if mf.parent == OUT:
                continue
            m = json.loads(mf.read_text(encoding="utf-8"))
            summaries.append({"slug": m["course_slug"], **m["totals"],
                              "expected": m.get("deck_count_expected")})
        write_global(summaries)
        write_readme()
        print(f"registry rebuilt: {len(summaries)} courses")
        return 0

    if args.all:
        slugs = [s for s, r in REGISTRY.items() if r.get("status") != MISSING]
    else:
        slugs = [s.strip() for s in args.courses.split(",") if s.strip()]
    bad = [s for s in slugs if s not in REGISTRY]
    if bad:
        print("unknown courses:", bad)
        return 2
    skipped_missing = [s for s in slugs
                       if REGISTRY[s].get("status") == MISSING]
    for s in skipped_missing:
        print(f"[{s}] {MISSING}: {REGISTRY[s]['reason']}")
    slugs = [s for s in slugs if s not in skipped_missing]

    summaries = []
    for slug in slugs:
        print(f"== {slug}", flush=True)
        summaries.append(scrape_course(slug, args.workers, args.delay,
                                       args.limit, args.force))
    write_global(summaries)
    write_readme()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
