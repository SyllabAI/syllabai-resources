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

Official codes come exclusively from the course's spec_point_map.json plus
the operator-verdict overlays (T-SPEC-2b sidecar records whose method is the
operator-verdict lane fill only ids the map itself left unmapped; T-SPEC-2c
part-level verdict codes recorded on the parts themselves; provenance tiers
preserved; nothing invented here). Content items keep
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


def verdict_overlay(eq_dir: Path, mappings: dict) -> dict:
    """T-SPEC-2b: operator-verdict lane resolutions from the resolution sidecar.
    Fills ONLY ids the stage-1 map itself left unmapped (map lane wins)."""
    res_file = eq_dir / "spec_point_resolution.json"
    if not res_file.exists():
        return {}
    res = json.loads(res_file.read_text(encoding="utf-8"))
    overlay = {}
    for rec in res.get("resolved") or []:
        method = rec.get("method") or ""
        if not method.startswith("operator-verdict"):
            continue
        sid = rec["id"]
        if sid in mappings or not rec.get("resolved_code"):
            continue
        overlay[sid] = {
            "official_id": rec.get("official_id"),
            "official_code": rec["resolved_code"],
            "tier": rec.get("tier"),
            "method": method,
        }
    return overlay


def merge_part_codes(codes, part, mappings):
    """T-SPEC-2c/2e: part-level operator-verdict codes live directly on the
    topic.json part (spec_point_codes). They are authoritative (validated
    against the course registry by the fail-closed apply lanes and by verify
    G1) and are merged here so learner links match the corpus. Id-level
    resolutions (map lane / overlay) win on duplicate official_code."""
    have = {c["official_code"] for c in codes}
    prefix = None
    for m in mappings.values():
        oid = m.get("official_id") or ""
        if ":" in oid:
            prefix = oid.rsplit(":", 1)[0]
            break
    extra = []
    for c in part.get("spec_point_codes") or []:
        if c in have:
            continue
        have.add(c)
        extra.append({"official_id": f"{prefix}:{c}" if prefix else c,
                      "official_code": c,
                      "tier": "operator-verdict-part",
                      "method": "operator-verdict part lane (T-SPEC-2c/2e; "
                                "PMT excluded as source per operator "
                                "instruction 2026-09-18)"})
    if not extra:
        return codes
    return sorted(codes + extra, key=lambda c: c["official_id"])


def course_bundle(course: str) -> dict:
    eq_dir = EQ / course
    map_file = eq_dir / "spec_point_map.json"
    mappings = {}
    qual = None
    if map_file.exists():
        mj = json.loads(map_file.read_text(encoding="utf-8"))
        qual = mj.get("qual")
        mappings = mj.get("mappings") or {}
    mappings.update(verdict_overlay(eq_dir, mappings))

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
                codes = merge_part_codes(codes, p, mappings)
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
    mpath = OUT / "manifest.json"
    # merge into an existing manifest so single-course runs don't clobber
    # the other courses' entries (latent defect fixed 2026-09-18, T-SPEC-1)
    if mpath.exists():
        manifest = json.loads(mpath.read_text(encoding="utf-8"))
        manifest["generated_utc"] = now_utc()
    else:
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
    (mpath).write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"TOTAL items={tot['items']} coded={tot['items_with_codes']} | "
          f"notes {tot['notes_coded']}/{tot['notes']}, "
          f"parts {tot['question_parts_coded']}/{tot['question_parts']}, "
          f"cards {tot['flashcards_coded']}/{tot['flashcards']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
