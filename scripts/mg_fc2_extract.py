#!/usr/bin/env python3
"""T-MG-FC-2 run-001 extractor — MG-Flashcards igcse-maths-edexcel.

Reads cached flashcards pages, extracts the `decks` envelope (cards with
cardType, front, back, mcqOptions[{text, correct, explanation}]), cleans
display HTML, and writes flat {topic-slug}.json + .md decks per the plane
law (grammar amendment of record: multiple-choice options captured).
"""
import json
import os
import re
import sys

sys.path.insert(0, "/home/z/my-project/scripts/mg_rgls_work")
import envelope as env  # noqa: E402
import mg_common as C  # noqa: E402
import rsc  # noqa: E402

LANE = "igcse-maths-edexcel"
TASK = "T-MG-FC-2"
RUN = "run-001"
EXTRACTOR = f"mg_fc1_extract.py ({TASK} {RUN})"
CORP = f"{C.CORPUS}/MG-Flashcards/{LANE}"

cat = json.load(open(f"{C.LOGS}/rgls_catalog.json"))[LANE]
LANE_DIR = cat["lane_dir"]


def clean(s):
    s = C.strip_inline_html(s)
    if s is None:
        return None
    return re.sub(r"\[ *\]", "[ ___ ]", s)


def extract_topic(slug):
    html = open(C.cache_path(LANE_DIR, slug, "flashcards"),
                encoding="utf-8", errors="ignore").read()
    payload = rsc.flight_payload(html)
    table = env.t_table(payload)
    decks = env.find_key(payload, "decks", table)
    if not decks:
        return None
    if isinstance(decks, dict):
        decks = [decks]
    cards_out = []
    deck_titles = []
    image_urls = []
    for d in decks:
        if not isinstance(d, dict) or "cards" not in d:
            continue
        deck_titles.append(d.get("title"))
        for c in d.get("cards", []):
            front = clean(c.get("front"))
            back = clean(c.get("back"))
            card = {
                "id": c.get("id"),
                "card_type": c.get("cardType"),
                "front": front,
                "back": back,
            }
            mcq = c.get("mcqOptions")
            if mcq:
                card["options"] = [{
                    "text": clean(o.get("text")),
                    "correct": bool(o.get("correct")),
                    "explanation": clean(o.get("explanation")) if o.get("explanation") else None,
                } for o in mcq]
            if c.get("points") is not None:
                card["points"] = c.get("points")
            # image cards? (folder variant trigger)
            for txt in (c.get("front") or "") + (c.get("back") or ""):
                if "<img" in str(txt):
                    card["_has_image"] = True
            cards_out.append(card)
    return {"decks": deck_titles, "cards": cards_out, "images": image_urls}


def render_md(slug, deck):
    out = [f"# {deck['title'] or slug}", ""]
    out += [f"_Lane: `{LANE}` · grade {deck.get('grade') or '—'} · "
            f"{deck['card_count']} cards (source: MathsGenie flashcards)_", ""]
    for i, c in enumerate(deck["cards"], 1):
        out.append(f"## Card {i} — `{c.get('card_type')}`")
        out += ["", f"**Front:** {c.get('front')}", ""]
        out += [f"**Back:** {c.get('back')}", ""]
        if c.get("options"):
            out.append("**Choices:**")
            out.append("")
            for o in c["options"]:
                mark = " ✔" if o.get("correct") else ""
                out.append(f"- {o.get('text')}{mark}")
                if o.get("explanation"):
                    out.append(f"  - _why:_ {o['explanation']}")
            out.append("")
    return "\n".join(out)


def main():
    os.makedirs(CORP, exist_ok=True)
    results = {"lane": LANE, "task": TASK, "run": RUN, "started": C.now_iso(),
               "decks": {}, "gaps": []}
    topics = sorted(s for s, m in cat["topics"].items() if "flashcards" in m["modes"])
    print(f"topics with flashcards: {len(topics)}")
    for idx, slug in enumerate(topics):
        try:
            got = extract_topic(slug)
        except Exception as e:
            results["gaps"].append({"topic": slug, "reason": f"extract-error: {str(e)[:100]}"})
            print(f"  [{idx+1}/{len(topics)}] {slug}: ERROR {str(e)[:60]}")
            continue
        if not got or not got["cards"]:
            results["gaps"].append({"topic": slug, "reason": "no-deck-envelope"})
            print(f"  [{idx+1}/{len(topics)}] {slug}: GAP no-deck")
            continue
        cards = [{k: v for k, v in c.items() if k != "_has_image"} for c in got["cards"]]
        deck = {
            "topic": slug,
            "lane": LANE,
            "grade": C.slug_grade(slug),
            "tier": None,
            "title": got["decks"][0] if got["decks"] else None,
            "cards": cards,
            "card_count": len(cards),
            "source_url": f"https://www.mathsgenie.co.uk/{LANE_DIR}/{slug}/flashcards",
            "source_sha256": C.sha256_str(open(C.cache_path(LANE_DIR, slug, "flashcards"),
                                               encoding="utf-8", errors="ignore").read()),
            "extracted_at": C.now_iso(),
            "extractor": EXTRACTOR,
            "task_id": TASK,
        }
        json.dump(deck, open(os.path.join(CORP, f"{slug}.json"), "w"),
                  indent=1, ensure_ascii=False)
        open(os.path.join(CORP, f"{slug}.md"), "w").write(render_md(slug, deck))
        results["decks"][slug] = {"cards": len(cards),
                                  "with_options": sum(1 for c in cards if c.get("options")),
                                  "card_types": sorted({c.get("card_type") or "?" for c in cards})}
        if (idx + 1) % 25 == 0:
            print(f"  {idx+1}/{len(topics)}", flush=True)
    results["finished"] = C.now_iso()
    json.dump(results, open(f"{C.LOGS}/fc2_extract_results.json", "w"), indent=1)
    tot = sum(m["cards"] for m in results["decks"].values())
    print(f"saved; decks={len(results['decks'])} cards={tot} gaps={len(results['gaps'])}")


if __name__ == "__main__":
    main()
