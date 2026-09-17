#!/usr/bin/env python3
"""
build_learner_spec_links.py — learner-UI spec-links bundle (all 39 courses).

Unifies every SME content item's anchor to official Edexcel spec codes into
one per-course serving artifact the learner UI renders directly:

  items: {content_id:
    {kind: "note" | "question_part" | "flashcard",
     label, section, topic,
     codes:   [{official_id, official_code, tier, method, unit?}],
     pending: [spcpt_id...]   # anchored but upstream join still unresolved
    }}

Sources per course:
  notes      SME-RevisionNotes/<c>/notes/**/*.json  (note_id, spec_point_ids)
  questions  SME-ExamQuestion/<c>/*/*/topic.json    (part id, spec_point_ids)
  flashcards SME-Flashcards/<c>/flashcard_spec_map.json (card -> codes)

Official codes come exclusively from the course's spec_point_map.json
(provenance tiers preserved; nothing invented here). Content items keep
their SME ids so the UI can deep-link.

Output: spec-links/<course>.json + spec-links/manifest.json + README.md
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

BASE = Path("/home/z/my-project/download/syllabai-resources")
NOTES = BASE / "SME-RevisionNotes"
EQ = BASE / "SME-ExamQuestion"
FC = BASE / "SME-Flashcards"
OUT = BASE / "spec-links"
SCHEMA = "syllabai.learner-spec-links/1.0"

ALL_COURSES = sorted(p.name for p in EQ.iterdir()
                     if p.is_dir() and not p.name.startswith("."))


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def resolve(spcpt_ids, mappings):
    codes, pending = [], []
    for s in spcpt_ids or []:
        m = mappings.get(s)
        if m:
            codes.append({"official_id": m["official_id"],
                          "official_code": m["official_code"],
                          "tier": m["tier"],
                          "method": m.get("method")})
        else:
            pending.append(s)
    # de-dup by official_id, keep best tier order
    seen, uniq = set(), []
    for c in sorted(codes, key=lambda c: c["official_id"]):
        if c["official_id"] in seen:
            continue
        seen.add(c["official_id"])
        uniq.append(c)
    return uniq, pending


def course_bundle(course: str) -> dict:
    eq_dir = EQ / course
    map_file = eq_dir / "spec_point_map.json"
    mappings = {}
    qual = None
    if map_file.exists():
        mj = json.loads(map_file.read_text(encoding="utf-8"))
        qual = mj.get("qual")
        mappings = mj.get("mappings") or {}

    items: dict = {}
    stats = Counter()

    # ---- revision notes
    for nf in sorted((NOTES / course).glob("notes/**/*.json")) if (NOTES / course).exists() else []:
        n = json.loads(nf.read_text(encoding="utf-8"))
        spids = n.get("spec_point_ids") or []
        if not spids:
            continue
        codes, pending = resolve(spids, mappings)
        path = n.get("path") or {}
        items[n["note_id"]] = {
            "kind": "note",
            "label": n.get("page_title") or n.get("title"),
            "section": path.get("section"),
            "topic": path.get("topic"),
            "codes": codes,
            "pending": pending,
        }
        stats["notes"] += 1
        stats["notes_coded"] += 1 if codes else 0

    # ---- exam question parts
    for tf in sorted(eq_dir.glob("*/*/topic.json")):
        t = json.loads(tf.read_text(encoding="utf-8"))
        topic = (t.get("topic") or {}).get("slug")
        section = (t.get("section") or {}).get("slug") if isinstance(t.get("section"), dict) else t.get("section")
        for q in t.get("questions") or []:
            for p in q.get("parts") or []:
                spids = p.get("spec_point_ids") or []
                if not spids:
                    continue
                codes, pending = resolve(spids, mappings)
                items[p["id"]] = {
                    "kind": "question_part",
                    "label": f"{(q.get('reference') or q.get('id') or 'question')} / part {p.get('order')}",
                    "section": section,
                    "topic": topic,
                    "codes": codes,
                    "pending": pending,
                }
                stats["question_parts"] += 1
                stats["question_parts_coded"] += 1 if codes else 0

    # ---- flashcards (codes precomputed by map_flashcards.py)
    fm = FC / course / "flashcard_spec_map.json"
    if fm.exists():
        fj = json.loads(fm.read_text(encoding="utf-8"))
        for deck_file in sorted(FC.glob(f"{course}/*/*/deck.json")):
            deck = json.loads(deck_file.read_text(encoding="utf-8"))
            meta = deck["deck"]
            for card in deck["cards"]:
                spids = card.get("spec_links") or []
                entry = fj.get("cards", {}).get(card["id"]) or {}
                codes = entry.get("codes") or []
                if not spids and not codes:
                    continue  # flashcards only appear when anchored somehow
                pending = list(entry.get("unresolved_spcpt") or [])
                # cards without links may still be content-joined
                if not spids and codes:
                    pending = []
                items[card["id"]] = {
                    "kind": "flashcard",
                    "label": (card.get("front_md") or "").replace("**", "")[:90],
                    "section": meta.get("section_slug"),
                    "topic": meta.get("topic_slug"),
                    "codes": codes,
                    "pending": pending,
                }
                stats["flashcards"] += 1
                stats["flashcards_coded"] += 1 if codes else 0

    bundle = {
        "schema": SCHEMA,
        "generated_utc": now_utc(),
        "course": course,
        "qual": qual,
        "totals": {
            "items": len(items),
            "items_with_codes": sum(1 for v in items.values() if v["codes"]),
            "by_kind": {k: stats[k] for k in ("notes", "question_parts", "flashcards")},
            "coded_by_kind": {k: stats[k + "_coded"] for k in ("notes", "question_parts", "flashcards")},
        },
        "items": items,
    }
    return bundle


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--courses", default="")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    courses = ALL_COURSES if args.all else \
        [c.strip() for c in args.courses.split(",") if c.strip()]
    manifest = {"schema": "syllabai.learner-spec-links-manifest/1.0",
                "generated_utc": now_utc(), "courses": {}}
    tot = Counter()
    for c in courses:
        b = course_bundle(c)
        (OUT / f"{c}.json").write_text(
            json.dumps(b, indent=1, ensure_ascii=False), encoding="utf-8")
        manifest["courses"][c] = {"qual": b["qual"], **b["totals"]}
        for k in ("items", "items_with_codes"):
            tot[k] += b["totals"][k]
        for k in ("notes", "question_parts", "flashcards"):
            tot[k] += b["totals"]["by_kind"][k]
            tot[k + "_coded"] += b["totals"]["coded_by_kind"][k]
        t = b["totals"]
        print(f"[{c}] items={t['items']} coded={t['items_with_codes']} "
              f"(notes {t['coded_by_kind']['notes']}/{t['by_kind']['notes']}, "
              f"parts {t['coded_by_kind']['question_parts']}/{t['by_kind']['question_parts']}, "
              f"cards {t['coded_by_kind']['flashcards']}/{t['by_kind']['flashcards']})",
              flush=True)
    (OUT / "manifest.json").write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"TOTAL items={tot['items']} coded={tot['items_with_codes']} | "
          f"notes {tot['notes_coded']}/{tot['notes']}, "
          f"parts {tot['question_parts_coded']}/{tot['question_parts']}, "
          f"cards {tot['flashcards_coded']}/{tot['flashcards']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
