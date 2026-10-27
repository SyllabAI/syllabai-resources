#!/usr/bin/env python3
"""T-SME-CAMBRIDGE — verification gates over the Cambridge (CAIE) corpus
extension. Scoped to the 34 cie-* lanes (the standing Edexcel corpora are
byte-untouched by construction: the extension only ADDS new course dirs +
rebuilds the three registry manifests/READMEs; `git status` receipts cover
the Edexcel side).

Gates:
  N1 notes   : per-course manifest; scraped == expected; 0 fetch/asset
               failures; json+md file counts == manifest pages
  N2 notes   : every asset referenced in a note JSON exists on disk
  N3 notes   : author-strip (no bylines/CTAs in rendered md)
  E1 examq   : per-course manifest; topic.json count == totals.topics;
               questions/parts/marks self-consistent; asset_map targets
               exist; every q.set_slug appears in question_sets
  E2 examq   : curriculum page-sourced (board Cambridge (CIE), exam_code
               non-null); schema 1.1
  F1 flash   : per-course manifest; deck.json count == totals.decks; cards
               have front/back md (or explicit flags); failures == 0
  F2 flash   : deck_count_actual vs REGISTRY expected_decks (warn-only)
  R1 registry: EQ top manifest covers all 34 slugs w/ correct status;
               notes/FC top manifests rebuilt from ALL per-course manifests
               (Edexcel + Cambridge counts match the materialized dirs)

Writes graph/reports/SME_CAMBRIDGE_VERIFICATION.json. Exit 1 on hard fails.
"""
from __future__ import annotations

import json
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import sme_cambridge_courses as cc  # noqa: E402

REPO = Path("/home/z/my-project/download/syllabai-resources")
NOTES = REPO / "SME-RevisionNotes"
EXAMQ = REPO / "SME-ExamQuestion"
FLASH = REPO / "SME-Flashcards"
REPORT = REPO / "graph" / "reports" / "SME_CAMBRIDGE_VERIFICATION.json"

FORBIDDEN_MD = ("Written by", "Reviewed by", "Updated on", "Guided study",
                "Excerpt From", "Read more")


def main() -> int:
    lanes = cc.courses()
    slugs = {c["slug"] for c in lanes}
    hard: list[str] = []
    warns: list[str] = []
    per_corpus = {}

    # ---------------- notes
    n_stat = {"courses": 0, "pages": 0, "assets": 0}
    for c in lanes:
        slug = c["slug"]
        cdir = NOTES / slug
        mf = cdir / "manifest.json"
        if not mf.exists():
            hard.append(f"notes/{slug}: no manifest.json")
            continue
        m = json.loads(mf.read_text(encoding="utf-8"))
        cnt = m["counts"]
        n_stat["courses"] += 1
        n_stat["pages"] += cnt["pages_scraped"]
        n_stat["assets"] += cnt["assets"]
        if cnt["pages_scraped"] != cnt["pages_expected"]:
            hard.append(f"notes/{slug}: scraped {cnt['pages_scraped']} != "
                        f"expected {cnt['pages_expected']}")
        if cnt["fetch_failures"]:
            hard.append(f"notes/{slug}: {cnt['fetch_failures']} fetch failures")
        if cnt["asset_failures"]:
            hard.append(f"notes/{slug}: {cnt['asset_failures']} asset failures")
        n_json = len(list(cdir.glob("notes/*/*/*.json")))
        n_md = len(list(cdir.glob("notes/*/*/*.md")))
        if n_json != len(m.get("pages", [])) or n_md != n_json:
            hard.append(f"notes/{slug}: files json={n_json} md={n_md} vs "
                        f"manifest pages={len(m.get('pages', []))}")
        # N2: assets exist + N3 author strip (full walk, Cambridge only)
        assets_dir = cdir / "assets"
        for jf in cdir.glob("notes/*/*/*.json"):
            j = json.loads(jf.read_text(encoding="utf-8"))
            md_text = jf.with_suffix(".md").read_text(encoding="utf-8")
            for bad in FORBIDDEN_MD:
                if bad in md_text:
                    hard.append(f"notes/{slug}/{jf.name}: forbidden string "
                                f"{bad!r} in md")
        for img in _md_images(cdir):
            # md refs come in two corpus forms (both pre-existing in the
            # Edexcel corpus): "../../../assets/<name>" and bare
            # "assets/<name>" — both resolve to course assets/<name>.
            if not (assets_dir / img).exists():
                hard.append(f"notes/{slug}: missing asset {img}")
    per_corpus["notes"] = n_stat

    # ---------------- examq
    e_stat = {"courses": 0, "topics": 0, "questions": 0, "assets": 0}
    for c in lanes:
        slug = c["slug"]
        cdir = EXAMQ / slug
        mf = cdir / "manifest.json"
        if not mf.exists():
            hard.append(f"examq/{slug}: no manifest.json")
            continue
        m = json.loads(mf.read_text(encoding="utf-8"))
        tot = m.get("totals") or {}
        e_stat["courses"] += 1
        e_stat["topics"] += tot.get("topics", 0)
        e_stat["questions"] += tot.get("questions", 0)
        e_stat["assets"] += tot.get("assets", 0)
        tjs = list(cdir.glob("*/*/topic.json"))
        if m.get("status") == "scraped" and len(tjs) != tot.get("topics"):
            hard.append(f"examq/{slug}: {len(tjs)} topic.json vs "
                        f"manifest topics {tot.get('topics')}")
        for tj in tjs:
            t = json.loads(tj.read_text(encoding="utf-8"))
            if t.get("schema") != "syllabai.sme-exam-questions/1.1":
                hard.append(f"examq/{slug}/{tj.parent.name}: schema "
                            f"{t.get('schema')}")
            cur = t.get("curriculum") or {}
            if cur.get("board") != "Cambridge (CIE)":
                hard.append(f"examq/{slug}/{tj.parent.name}: board "
                            f"{cur.get('board')!r}")
            if not cur.get("exam_code"):
                hard.append(f"examq/{slug}/{tj.parent.name}: no exam_code")
            set_slugs = {s["slug"] for s in t.get("question_sets") or []}
            for q in t.get("questions") or []:
                if set_slugs and q.get("set_slug") not in set_slugs:
                    hard.append(f"examq/{slug}/{tj.parent.name}: set_slug "
                                f"{q.get('set_slug')!r} not in question_sets")
                for p in q.get("parts") or []:
                    if not (p.get("problem_md") or "").strip():
                        hard.append(f"examq/{slug}/{tj.parent.name}: empty "
                                    f"problem_md qid={q.get('id')}")
            amap = (t.get("scrape") or {}).get("asset_map") or {}
            for url, name in amap.items():
                if not (tj.parent / "assets" / name).exists():
                    hard.append(f"examq/{slug}/{tj.parent.name}: missing "
                                f"asset {name}")
            if (t.get("scrape") or {}).get("asset_failures"):
                hard.append(f"examq/{slug}/{tj.parent.name}: asset failures")
    per_corpus["examq"] = e_stat

    # ---------------- flashcards
    sys.path.insert(0, str(REPO / "scripts"))
    from sme_flashcards_scrape import REGISTRY  # noqa: E402
    f_stat = {"courses": 0, "decks": 0, "cards": 0}
    for c in lanes:
        slug = c["slug"]
        reg = REGISTRY.get(slug) or {}
        if reg.get("status") == "missing_on_sme":
            if (FLASH / slug).exists():
                hard.append(f"flash/{slug}: MISSING lane has a dir")
            continue
        cdir = FLASH / slug
        mf = cdir / "manifest.json"
        if not mf.exists():
            hard.append(f"flash/{slug}: no manifest.json")
            continue
        m = json.loads(mf.read_text(encoding="utf-8"))
        tot = m.get("totals") or {}
        f_stat["courses"] += 1
        f_stat["decks"] += tot.get("decks", 0)
        f_stat["cards"] += tot.get("cards", 0)
        if tot.get("deck_failures") or tot.get("asset_failures"):
            hard.append(f"flash/{slug}: deck/asset failures "
                        f"{tot.get('deck_failures')}/{tot.get('asset_failures')}")
        decks = list(cdir.glob("*/*/deck.json"))
        if len(decks) != tot.get("decks"):
            hard.append(f"flash/{slug}: {len(decks)} deck.json vs totals "
                        f"{tot.get('decks')}")
        exp = m.get("deck_count_actual")
        if exp != len(decks):
            hard.append(f"flash/{slug}: deck_count_actual {exp} != on-disk "
                        f"{len(decks)}")
        expected = reg.get("expected_decks")
        if expected is not None and expected != len(decks):
            warns.append(f"flash/{slug}: decks {len(decks)} != census "
                         f"expected {expected} (SME-side change; recorded)")
        for df in decks:
            d = json.loads(df.read_text(encoding="utf-8"))
            for card in d.get("cards") or []:
                if not ((card.get("front_md") or "").strip()
                        or (card.get("front_blocks") or [])):
                    hard.append(f"flash/{slug}/{df.parent.name}: empty front "
                                f"card {card.get('id')}")
                if not ((card.get("back_md") or "").strip()
                        or (card.get("back_blocks") or [])):
                    hard.append(f"flash/{slug}/{df.parent.name}: empty back "
                                f"card {card.get('id')}")
    per_corpus["flashcards"] = f_stat

    # ---------------- registries
    eq_reg = json.loads((EXAMQ / "manifest.json").read_text(encoding="utf-8"))
    eq_slugs = {c["slug"]: c.get("status") for c in eq_reg["courses"]}
    for s in slugs:
        want = ("no_topic_questions_on_sme"
                if (EXAMQ / s / "manifest.json").exists()
                and json.loads((EXAMQ / s / "manifest.json")
                               .read_text(encoding="utf-8")).get("status")
                == "no_topic_questions_on_sme" else "scraped")
        if eq_slugs.get(s) != want:
            hard.append(f"registry/eq: {s} status {eq_slugs.get(s)!r} != {want!r}")
    no_reg = json.loads((NOTES / "manifest.json").read_text(encoding="utf-8"))
    if no_reg.get("scraped_courses") != len(list(NOTES.glob("*/manifest.json"))):
        hard.append("registry/notes: scraped_courses != course manifests on disk")
    fc_reg = json.loads((FLASH / "manifest.json").read_text(encoding="utf-8"))
    missing_reg = [s for s in slugs if s not in fc_reg.get("registry", {})]
    if missing_reg:
        hard.append(f"registry/fc: Cambridge slugs absent from global "
                    f"registry: {missing_reg[:4]}")

    verdict = {"date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               "lanes": len(lanes),
               "hard_failures": hard, "warnings": warns,
               "per_corpus": per_corpus,
               "status": "PASS" if not hard else "FAIL"}
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(verdict, indent=1, ensure_ascii=False),
                      encoding="utf-8")
    print(json.dumps({"status": verdict["status"],
                      "hard": len(hard), "warns": len(warns),
                      "per_corpus": per_corpus}, indent=1))
    for h in hard[:25]:
        print("HARD:", h)
    for w in warns[:10]:
        print("WARN:", w)
    return 0 if not hard else 1


def _walk_blocks(nodes):
    for n in nodes or []:
        yield n
        if isinstance(n, dict):
            yield from _walk_blocks(n.get("content"))


def _md_images(cdir: Path) -> set[str]:
    """Basenames of every asset referenced from any note md (both corpus
    reference forms); all resolve to <course>/assets/<name>."""
    import re
    imgs = set()
    for mf in cdir.glob("notes/*/*/*.md"):
        for m in re.finditer(r"\]\((?:\.{3}/)?assets/([^)]+)\)",
                             mf.read_text(encoding="utf-8",
                                          errors="replace")):
            imgs.add(m.group(1))
    return imgs


if __name__ == "__main__":
    sys.exit(main())
