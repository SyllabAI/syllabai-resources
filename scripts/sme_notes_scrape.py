#!/usr/bin/env python3
"""
T-SME-NOTES-3 — SME revision-notes corpus scraper (all 39 Edexcel courses).

For each course: fetch leaf revision-note pages (discovered by
scripts/sme_notes_discover.py), parse the TipTap document embedded in
__NEXT_DATA__ (pageProps.revisionNote.attributes.content), and write per-note
JSON (authoritative typed blocks) + Markdown render.

Key properties:
- author/reviewer bylines are NEVER part of note content; recorded once in
  the per-course manifest as ids+names (no avatars, no biographies)
- callouts become typed blocks via attrs.variant (exam-tip -> Exam Hint,
  worked-example -> Worked Example, case-study -> Case Study)
- "Guided study" is a client-side CTA widget, NOT content: dropped from
  blocks, recorded as guided_study.lesson_ids metadata
- Wiris MathML equations -> KaTeX latex (reuses sme_examq_scrape.MathML2Latex)
  with raw mathml retained for lossless re-processing
- figures -> per-course assets/<sha12>-<slug>.<ext> (deterministic, deduped
  by content hash), markdown src rewritten relative
- resumable: raw parsed pages cached at .cache/sme_notes/<course>/<leaf>.json

Usage:
  python3 scripts/sme_notes_scrape.py --courses igcse-chemistry-19
  python3 scripts/sme_notes_scrape.py --all --workers 8
  python3 scripts/sme_notes_scrape.py --registry   # rebuild manifests+README
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import re
import sys
import time
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import sme_examq_scrape as eq  # noqa: E402 (M2L, render_inline, render_table, ...)

BASE = Path("/home/z/my-project/download/syllabai-resources")
OUT = BASE / "SME-RevisionNotes"
CACHE = Path("/home/z/my-project/.cache/sme_notes")
DISCOVER = Path("/home/z/my-project/.cache/sme_notes_urls.json")
SCHEMA = "syllabai.sme-revision-note/1.0"

VARIANT_LABELS = {
    "exam-tip": "Exam Hint",
    "worked-example": "Worked Example",
    "case-study": "Case Study",
}


def leaf_urls(course: str) -> tuple[str, list[str]]:
    disc = json.loads(DISCOVER.read_text(encoding="utf-8"))
    base = disc["courses"][course]["notes_base"]
    urls = set()
    for u in disc["notes_urls"]:
        if not u.startswith(base):
            continue
        u = u.rstrip("/")
        rest = u[len(base):].strip("/").split("/") if u[len(base):] else []
        if len(rest) >= 2:  # section/topic/leaf (or deeper)
            urls.add(u)
    return base, sorted(urls)


def author_meta(a: dict | None) -> dict | None:
    """id+name+role only. No images, no biographies."""
    if not a:
        return None
    at = a.get("attributes") or {}
    return {"id": a.get("id"), "name": at.get("name"),
            "role": at.get("subject_name")}


def parse_page(url: str, html: str) -> dict:
    pp = eq.parse_next_data(html)  # returns pageProps directly
    rn = pp["revisionNote"]
    attrs = rn.get("attributes") or {}
    rels = rn.get("relationships") or {}
    bc = pp.get("breadcrumbs") or {}
    slugs, titles = bc.get("slugs") or {}, bc.get("titles") or {}
    lessons = [(l or {}).get("id") for l in
               (rels.get("revision_note_lessons") or {}).get("data") or []]
    # canonical path from the URL itself (unique per page; breadcrumb slugs
    # can collide when SME reuses a leaf slug under two topics)
    disc_base = url.split("/revision-notes/")[0]
    segs = url.rstrip("/").split("/revision-notes/", 1)[-1].split("/")
    segs = [s for s in segs if s]
    return {
        "url": url,
        "segs": segs,
        "rn_id": rn.get("id"),
        "content": attrs.get("content") or [],
        "updated_at": attrs.get("updated_at"),
        "created_at": attrs.get("created_at"),
        "is_ai_assisted": attrs.get("is_ai_assisted"),
        "authors": [author_meta(pp.get("author"))],
        "reviewers": [author_meta(pp.get("reviewer"))],
        "guided_study_lesson_ids": [x for x in lessons if x],
        "pdf_url": pp.get("pdfUrl"),
        "page_title": pp.get("title"),
        "title": titles.get("subtopic") or pp.get("title"),
        "slugs": {"section": slugs.get("section"),
                  "topic": slugs.get("topic"),
                  "subtopic": slugs.get("subtopic")},
        "titles": {"section": titles.get("section"),
                   "topic": titles.get("topic"),
                   "subtopic": titles.get("subtopic")},
    }


# --------------------------------------------------------------- blocks (JSON)
def make_ctx(asset_name_fn) -> dict:
    """ctx dict compatible with sme_examq_scrape renderers."""
    return {"asset_fn": asset_name_fn, "equations": []}


def fig_url(attrs: dict) -> str:
    return eq.normalize_cdn_url(attrs.get("src") or "")


def collect_asset_urls(content: list) -> set:
    urls = set()

    def walk(nodes):
        for n in nodes or []:
            if not isinstance(n, dict):
                continue
            if n.get("type") == "figure":
                u = fig_url(n.get("attrs") or {})
                if u:
                    urls.add(u)
            if isinstance(n.get("content"), list):
                walk(n["content"])
            # inline image nodes (defensive)
            if n.get("type") == "image" and isinstance(n.get("attrs"), dict):
                u = fig_url(n["attrs"])
                if u:
                    urls.add(u)
    walk(content)
    return urls


def asset_name_for(url: str) -> str:
    ext = Path(urllib.parse.urlparse(url).path).suffix.lower() or ".bin"
    if ext not in (".webp", ".png", ".gif", ".jpg", ".jpeg", ".svg", ".avif"):
        ext = ".bin"
    base = Path(urllib.parse.urlparse(url).path).stem
    slug = re.sub(r"[^a-z0-9]+", "-", (base or "img").lower()).strip("-")[:48]
    h = hashlib.sha1(url.encode()).hexdigest()[:12]
    return f"{h}-{slug or 'img'}{ext}"


def to_blocks(nodes: list, ctx: RenderCtx) -> list:
    """TipTap blocks -> typed JSON blocks (specPoint wrappers flattened)."""
    blocks = []
    for n in nodes or []:
        if not isinstance(n, dict):
            continue
        t = n.get("type")
        if t == "specPoint":
            a = n.get("attrs") or {}
            video = a.get("video") or {}
            blocks.append({"type": "spec_point", "id": a.get("id"),
                           "name": a.get("name"),
                           "definition": a.get("definition"),
                           **({"video_id": video["id"]}
                              if video.get("id") else {})})
            blocks.extend(to_blocks(n.get("content") or [], ctx))
        elif t == "heading":
            blocks.append({"type": "heading",
                           "level": (n.get("attrs") or {}).get("level") or 2,
                           "text": eq.render_inline(n.get("content"),
                                                    ctx).strip()})
        elif t == "paragraph":
            md = eq.render_inline(n.get("content"), ctx).strip()
            if md:
                blocks.append({"type": "paragraph", "md": md})
        elif t in ("bulletList", "orderedList"):
            md = eq.render_blocks([n], ctx).strip()
            if md:
                blocks.append({"type": "bullets" if t == "bulletList"
                               else "ordered", "md": md})
        elif t == "callout":
            variant = (n.get("attrs") or {}).get("variant") or "note"
            md = eq.render_blocks(n.get("content"), ctx).strip()
            if md:
                blocks.append({"type": "callout", "variant": variant,
                               "label": VARIANT_LABELS.get(variant, variant),
                               "md": md})
        elif t == "figure":
            attrs = n.get("attrs") or {}
            src, name = ctx["asset_fn"](attrs)
            blk = {"type": "figure", "orig_src": src, "file": None,
                   "alt": attrs.get("alt"), "caption": attrs.get("caption")}
            if name:
                blk["file"] = f"assets/{name}"
            blocks.append(blk)
        elif t == "equation":
            attrs = n.get("attrs") or {}
            mathml = attrs.get("mathml") or ""
            latex = eq.M2L.convert(mathml)
            blocks.append({"type": "equation", "latex": latex,
                           "mathml": mathml,
                           "alt": attrs.get("alt")})
        elif t == "table":
            md = eq.render_table(n, ctx)
            if md:
                blocks.append({"type": "table", "md": md})
        elif t == "hardBreak":
            continue
        else:
            # unknown block: flatten defensively
            if isinstance(n.get("content"), list) and n["content"]:
                inner = to_blocks(n["content"], ctx)
                if inner:
                    blocks.append({"type": f"raw_{t}", "blocks": inner})
    return blocks


def blocks_to_md(blocks: list, asset_prefix: str = "../../../",
                 depth: int = 0) -> str:
    chunks = []
    for b in blocks:
        t = b.get("type")
        if t == "spec_point":
            head = b.get("name") or "Spec point"
            chunks.append(f"## {head}\n")
            card = []
            if b.get("id"):
                card.append(f"`{b['id']}`")
            if b.get("definition"):
                card.append(b["definition"])
            if card:
                chunks.append("> **Spec point** — " + " · ".join(card) + "\n")
        elif t == "heading":
            lvl = min(b.get("level") or 2, 6) + depth
            chunks.append("#" * lvl + " " + (b.get("text") or "") + "\n")
        elif t == "paragraph":
            chunks.append(b["md"] + "\n")
        elif t in ("bullets", "ordered"):
            chunks.append(b["md"] + "\n")
        elif t == "callout":
            quoted = "\n".join("> " + ln for ln in b["md"].splitlines())
            chunks.append(f"> **{b.get('label') or b.get('variant')}**\n"
                          + quoted + "\n")
        elif t == "figure":
            alt = b.get("alt") or ""
            if b.get("file"):
                chunks.append(f"![{alt}]({asset_prefix}{b['file']})\n")
            else:
                chunks.append(f"![{alt}]({b.get('orig_src')}) "
                              f"<!-- asset download failed -->\n")
            if b.get("caption"):
                chunks.append(f"*{b['caption']}*\n")
        elif t == "equation":
            if b.get("latex"):
                chunks.append(f"$$ {b['latex']} $$\n")
            elif b.get("alt"):
                chunks.append(f"`{b['alt']}`\n")
        elif t == "table":
            chunks.append(b["md"] + "\n")
        elif t == "raw_block":
            chunks.append(blocks_to_md(b.get("blocks", []), asset_prefix,
                                       depth + 1) + "\n")
    text = "\n".join(chunks)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


# ------------------------------------------------------------------ fetching
def fetch_page(course: str, url: str, force: bool) -> dict:
    slug = url.rstrip("/").split("/")[-1]
    cdir = CACHE / course
    cpath = cdir / (hashlib.sha1(url.encode()).hexdigest()[:10] + "-"
                    + slug + ".json")
    if cpath.exists() and not force:
        return json.loads(cpath.read_text(encoding="utf-8"))
    html = eq.http_get(url)
    out = parse_page(url, html)
    cdir.mkdir(parents=True, exist_ok=True)
    cpath.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    return out


def fetch_assets(urls: list[str], assets_dir: Path, workers: int = 4,
                 delay: float = 0.1) -> tuple[dict, list]:
    """url -> {file, ok, error}; deterministic sha1 names."""
    assets_dir.mkdir(parents=True, exist_ok=True)
    plan = {}
    for u in sorted(urls):
        name = asset_name_for(u)
        target = assets_dir / name
        if target.exists() and target.stat().st_size > 0:
            plan[u] = {"file": f"assets/{name}", "ok": True, "error": None}
    todo = [u for u in sorted(urls) if u not in plan]

    def grab(u: str):
        name = asset_name_for(u)
        target = assets_dir / name
        try:
            data = eq.http_get(u, binary=True, retries=3, delay=delay)
            if len(data) < 64:
                raise RuntimeError(f"suspiciously small ({len(data)} B)")
            is_avif = data[4:8] == b"ftyp"
            if not (is_avif
                    or data[:4] in (b"RIFF", b"\x89PNG", b"GIF8", b"<svg",
                                    b"<?xm")
                    or data[:3] == b"\xff\xd8\xff"):
                raise RuntimeError("not an image payload")
            target.write_bytes(data)
            time.sleep(delay)
            return u, {"file": f"assets/{name}", "ok": True, "error": None}
        except Exception as e:  # noqa: BLE001
            return u, {"file": f"assets/{name}", "ok": False,
                       "error": str(e)[:160]}

    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        for u, res in ex.map(grab, todo):
            plan[u] = res
    return plan, [{"url": u, "error": r["error"]} for u, r in plan.items()
                  if not r["ok"]]


# ------------------------------------------------------------------ pipeline
def render_note(rec: dict, course: str, asset_results: dict,
                spec_codes: dict | None) -> dict:
    def asset_fn(attrs: dict):
        src = eq.normalize_cdn_url(attrs.get("src") or "")
        r = asset_results.get(src)
        return src, (Path(r["file"]).name if r and r["ok"] else None)

    ctx = make_ctx(asset_fn)
    blocks = to_blocks(rec["content"], ctx)
    segs = rec.get("segs") or [rec["slugs"]["section"],
                               rec["slugs"]["topic"],
                               rec["slugs"]["subtopic"]]
    asset_prefix = "../" * len(segs)
    spec_ids = [b["id"] for b in blocks if b.get("type") == "spec_point"
                and b.get("id")]
    codes = sorted({spec_codes[sid] for sid in spec_ids
                    if spec_codes and sid in spec_codes})
    md = blocks_to_md(blocks, asset_prefix)
    return {
        "schema": SCHEMA,
        "note_id": rec["rn_id"],
        "course_slug": course,
        "url": rec["url"],
        "title": rec.get("title"),
        "page_title": rec.get("page_title"),
        "path": {"segs": segs,
                 "section": segs[0], "topic": segs[1] if len(segs) > 1 else "",
                 "leaf": segs[-1]},
        "titles": rec.get("titles") or {},
        "updated_at": rec.get("updated_at"),
        "is_ai_assisted": rec.get("is_ai_assisted"),
        "authors": [a for a in rec.get("authors") or [] if a],
        "reviewers": [a for a in rec.get("reviewers") or [] if a],
        "guided_study": {"lesson_ids": rec.get("guided_study_lesson_ids") or []},
        "pdf_url": rec.get("pdf_url"),
        "spec_point_ids": spec_ids,
        "spec_point_codes": codes,
        "equations": ctx["equations"],
        "stats": {"blocks": len(blocks),
                  "figures": sum(1 for b in blocks if b["type"] == "figure"),
                  "worked_examples": sum(
                      1 for b in blocks if b["type"] == "callout"
                      and b.get("variant") == "worked-example"),
                  "exam_hints": sum(1 for b in blocks if b["type"] == "callout"
                                    and b.get("variant") == "exam-tip"),
                  "case_studies": sum(1 for b in blocks
                                      if b["type"] == "callout"
                                      and b.get("variant") == "case-study"),
                  "equations": len(ctx["equations"])},
        "blocks": blocks,
        "_md": md,
    }


def write_note(course_dir: Path, rec: dict, note: dict) -> str:
    segs = note["path"]["segs"]
    rel = Path("notes").joinpath(*segs[:-1])
    rel = rel / (segs[-1] + ".json")
    target = course_dir / rel
    target.parent.mkdir(parents=True, exist_ok=True)

    fm = [f'note_id: "{note["note_id"]}"',
          f'title: {json.dumps(note["title"] or "", ensure_ascii=False)}',
          f'source: {note["url"]}',
          f'path: {"/".join(segs)}',
          f'updated_at: "{note.get("updated_at") or ""}"',
          'spec_point_ids: '
          f'{json.dumps(note["spec_point_ids"])}',
          'spec_point_codes: '
          f'{json.dumps(note["spec_point_codes"])}',
          f'guided_study: {json.dumps(bool(note["guided_study"]["lesson_ids"]))}']
    md_text = ("---\n" + "\n".join(fm) + "\n---\n\n"
               + f"# {note['title'] or note['path']['leaf']}\n\n" + note["_md"])
    target.write_text(json.dumps(
        {k: v for k, v in note.items() if k != "_md"},
        ensure_ascii=False, indent=1), encoding="utf-8")
    target.with_suffix(".md").write_text(md_text, encoding="utf-8")
    return str(rel)


def scrape_course(course: str, workers: int, force: bool) -> int:
    base, urls = leaf_urls(course)
    print(f"[{course}] notes_base {base}")
    print(f"[{course}] leaf pages: {len(urls)}")
    records, failures = [], []
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(fetch_page, course, u, force): u for u in urls}
        done = 0
        for fut in cf.as_completed(futs):
            u = futs[fut]
            try:
                records.append(fut.result())
            except Exception as exc:  # noqa: BLE001
                failures.append({"url": u, "error": str(exc)[:200]})
            done += 1
            if done % 25 == 0 or done == len(urls):
                print(f"[{course}]   fetched {done}/{len(urls)} "
                      f"(failures: {len(failures)})")

    asset_urls = set()
    for r in records:
        asset_urls |= collect_asset_urls(r["content"])
    asset_results, asset_failures = fetch_assets(
        sorted(asset_urls), OUT / course / "assets")
    print(f"[{course}] assets: {len(asset_urls)} "
          f"(failures: {len(asset_failures)})")

    course_dir = OUT / course
    pages, md_chars = [], 0
    for r in sorted(records, key=lambda x: x.get("segs") or []):
        note = render_note(r, course, asset_results, None)
        rel = write_note(course_dir, r, note)
        md_chars += len(note["_md"])
        pages.append({"path": rel,
                      "rn_id": note["note_id"],
                      "title": note["title"],
                      "spec_point_ids": len(note["spec_point_ids"]),
                      "stats": note["stats"]})

    guided = sum(1 for r in records if r.get("guided_study_lesson_ids"))
    authors = {}
    for r in records:
        for a in (r.get("authors") or []) + (r.get("reviewers") or []):
            if a and a.get("id"):
                authors[a["id"]] = a
    tree: dict = {}
    for r in records:
        tree.setdefault(r["titles"]["section"] or r["slugs"]["section"] or "?",
                        {}).setdefault(
            r["titles"]["topic"] or r["slugs"]["topic"] or "?", []).append(
            r["titles"]["subtopic"] or r["slugs"]["subtopic"])
    for sec in tree:
        for top in tree[sec]:
            tree[sec][top] = sorted(tree[sec][top])

    manifest = {
        "schema": "syllabai.sme-revision-notes-course/1.0",
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "course_slug": course,
        "notes_base": base,
        "counts": {"pages_expected": len(urls),
                   "pages_scraped": len(records),
                   "fetch_failures": len(failures),
                   "assets": len(asset_urls),
                   "asset_failures": len(asset_failures),
                   "spec_point_links": sum(p["spec_point_ids"]
                                           for p in pages),
                   "guided_study_pages": guided,
                   "markdown_chars": md_chars},
        "authors": sorted(authors.values(),
                          key=lambda a: a.get("id") or ""),
        "tree": tree,
        "fetch_failures": failures,
        "asset_failures": asset_failures,
        "pages": pages,
    }
    (course_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    s = manifest["counts"]
    print(f"[{course}] DONE pages {s['pages_scraped']}/{s['pages_expected']} "
          f"fail {s['fetch_failures']} | assets {s['assets']} "
          f"(fail {s['asset_failures']}) | spec links "
          f"{s['spec_point_links']} | guided {s['guided_study_pages']}")
    return 0


def write_registry() -> int:
    """Top-level manifest.json + README.md from per-course manifests."""
    OUT.mkdir(parents=True, exist_ok=True)
    courses = {}
    for mf in sorted(OUT.glob("*/manifest.json")):
        m = json.loads(mf.read_text(encoding="utf-8"))
        c = m["course_slug"]
        # merge counts across re-runs (sum into one entry)
        if c in courses:
            for k, v in m["counts"].items():
                courses[c]["counts"][k] = courses[c]["counts"].get(k, 0) + v
        else:
            courses[c] = {"course_slug": c, "notes_base": m["notes_base"],
                          "counts": dict(m["counts"])}
    tot = {k: sum(c["counts"].get(k, 0) for c in courses.values())
           for k in ("pages_expected", "pages_scraped", "fetch_failures",
                     "assets", "asset_failures", "spec_point_links",
                     "guided_study_pages", "markdown_chars")}
    doc = {"schema": "syllabai.sme-revision-notes/1.0",
           "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                          time.gmtime()),
           "totals": tot, "scraped_courses": len(courses), "courses": courses}
    (OUT / "manifest.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

    lines = ["# SME Revision Notes (Edexcel IGCSE + IAL)",
             "",
             f"Scraped from Save My Exams revision-notes trees for the same "
             f"39 courses as `../SME-ExamQuestion/`. "
             f"{tot['pages_scraped']}/{tot['pages_expected']} leaf pages, "
             f"{tot['assets']} assets, {tot['spec_point_links']} spec-point "
             f"links.",
             "",
             "Per note: `<leaf>.json` (authoritative typed blocks; Wiris "
             "MathML kept verbatim) + `<leaf>.md` (render). Callout variants "
             "map to typed blocks (`exam-tip` -> Exam Hint, `worked-example` "
             "-> Worked Example, `case-study` -> Case Study).",
             "",
             "- Author/reviewer bylines are metadata-only (ids+names in "
             "course `manifest.json`; no avatars or biographies anywhere in "
             "content).",
             "- \"Guided study\" is a client-side SME widget, not note "
             "content; recorded as `guided_study.lesson_ids`.",
             "- Chemistry additionally carries official 4CH1 "
             "`spec_point_codes` (AI_VALIDATED, operator-delegated) and the "
             "operator-validated legacy `spec_map` joined by URL — see "
             "`scripts/sme_notes_chem_join.py`.",
             "- License: operator-authorized; see `../LICENSE-DATA.md`.",
             "",
             "| course | pages | assets | spec links |",
             "|---|---|---|---|"]
    for c in sorted(courses):
        s = courses[c]["counts"]
        lines.append(f"| {c} | {s['pages_scraped']}/{s['pages_expected']} | "
                     f"{s['assets']} | {s['spec_point_links']} |")
    (OUT / "README.md").write_text("\n".join(lines) + "\n",
                                   encoding="utf-8")
    print(f"registry: {len(courses)} courses, {tot['pages_scraped']} pages")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--courses", help="comma-separated course slugs")
    g.add_argument("--all", action="store_true", help="all courses in cache")
    g.add_argument("--registry", action="store_true",
                   help="rebuild top-level manifest.json + README.md and exit")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    if args.registry:
        return write_registry()

    if args.all:
        disc = json.loads(DISCOVER.read_text(encoding="utf-8"))
        courses = sorted(disc["courses"])
    else:
        courses = [c.strip() for c in args.courses.split(",") if c.strip()]

    rc = 0
    for course in courses:
        try:
            scrape_course(course, args.workers, args.force)
        except Exception as exc:  # noqa: BLE001
            print(f"[{course}] FAILED: {exc}", file=sys.stderr)
            rc = 2
    write_registry()
    return rc


if __name__ == "__main__":
    sys.exit(main())
