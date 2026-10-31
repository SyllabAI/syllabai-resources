#!/usr/bin/env python3
"""ZNotes revision-notes fetcher for SyllabAI/syllabai-resources.

Task: T-ZNOTES-1 — captures ZNotes (znotes.org) web revision notes for the
CAIE + Edexcel boards via the public api.znotes.org content API, and stores
them in the SME-RevisionNotes folder conventions:

    ZNotes/<course_slug>/notes/<module>/<nn-chapter>/<nn-card>.md + .json
    ZNotes/<course_slug>/assets/<cardid12>-<name>.<ext>
    ZNotes/<course_slug>/manifest.json
    ZNotes/manifest.json                     (global, built with --manifest)

Upstream chain (all slugs/ids/codes come from the upstream API, never invented):
    /v1/boards -> /v1/subjects -> /v1/modules?subject= (moduleType=note)
    -> /v1/chapters?module= -> /v1/cards?chapter=   (markdown + LaTeX + S3 images)

stdlib only; resumable (images skipped when present); time-budget friendly.

Usage:
    python3 zn_fetch.py --index                  # refresh courses_index.json
    python3 zn_fetch.py --course <course_slug>
    python3 zn_fetch.py --board caie --level igcse
    python3 zn_fetch.py --all
    python3 zn_fetch.py --manifest               # rebuild global manifest
Options:
    --time-budget S   stop starting new courses after S seconds (default 480)
    --root DIR        repo root (default: parent of this script's ../..)
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
API = "https://api.znotes.org"
BOARDS = ("caie", "edexcel")
TASK_ID = "T-ZNOTES-1"
BASE_COMMIT = "992bf84bb440025df2f5ec789cd1a1300bf3f1df"
TEXT_WORKERS = 5
IMG_WORKERS = 8
API_TIMEOUT = 90
IMG_TIMEOUT = 60
POLITENESS = 0.04

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

_md_img = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
_html_img = re.compile(r"<img[^>]+src=[\"']([^\"']+)[\"']", re.I)
_ext_re = re.compile(r"\.([A-Za-z0-9]{2,5})$")
_slug_bad = re.compile(r"[^a-z0-9]+")


def now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def slugify(text, maxlen=64):
    s = _slug_bad.sub("-", (text or "").lower()).strip("-")
    return s[:maxlen].rstrip("-") or "untitled"


def api_get(path, retries=3):
    delay = 1.0
    for attempt in range(retries):
        try:
            req = urllib.request.Request(API + path, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=API_TIMEOUT) as r:
                return json.load(r)
        except Exception as e:
            if attempt == retries - 1:
                raise RuntimeError(f"API GET {path}: {e}") from e
            time.sleep(delay)
            delay *= 2


def sniff_ext(url, data):
    m = _ext_re.search(urllib.parse.urlparse(url).path.lower())
    if m:
        return m.group(1)
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return "png"
    if data[:3] == b"\xff\xd8\xff":
        return "jpg"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return "gif"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    if data[:5] == b"<?xml" or data[:4] == b"<svg":
        return "svg"
    return "png"


class CourseScraper:
    def __init__(self, course, root):
        self.c = course
        self.root = root
        self.course_dir = os.path.join(root, "ZNotes", course["course_slug"])
        self.assets_dir = os.path.join(self.course_dir, "assets")
        self.notes_dir = os.path.join(self.course_dir, "notes")
        self.asset_map = {}      # orig url -> local filename
        self.failures = {"cards": [], "images": []}
        self.counts = {"modules": 0, "chapters": 0, "cards": 0, "images": 0,
                       "image_failures": 0, "fetch_failures": 0,
                       "markdown_chars": 0, "assets_bytes": 0}
        self.tree = {}
        self.modules_meta = []
        self._used_names = set()

    # ---------- assets ----------
    def _asset_name(self, url, data, card_id):
        base = os.path.basename(urllib.parse.urlparse(url).path)
        base = urllib.parse.unquote(base)
        stem, ext = os.path.splitext(base)
        ext = ext.lstrip(".").lower()
        if ext not in ("png", "jpg", "jpeg", "gif", "webp", "svg", "avif"):
            ext = sniff_ext(url, data)
        stem = _slug_bad.sub("-", stem.lower()).strip("-")[:48]
        prefix = (card_id or hashlib.sha1(url.encode()).hexdigest())[:12]
        name = f"{prefix}-{stem or 'image'}.{ext}"
        n = 1
        while name in self._used_names and self.asset_map.get(url) != name:
            n += 1
            name = f"{prefix}-{stem or 'image'}-{n}.{ext}"
        self._used_names.add(name)
        return name

    def collect_image_jobs(self, card_id, md):
        jobs = []
        seen = set()
        for m in _md_img.finditer(md):
            url = m.group(2)
            if url.startswith("data:") or url in seen:
                continue
            seen.add(url)
            jobs.append(url)
        for m in _html_img.finditer(md):
            url = m.group(1)
            if url.startswith("data:") or url in seen:
                continue
            seen.add(url)
            jobs.append(url)
        return jobs

    def fetch_images(self, jobs):
        todo = [u for u in jobs if u not in self.asset_map]
        os.makedirs(self.assets_dir, exist_ok=True)

        def one(url):
            last = (None, "error")
            for hdrs in ({"User-Agent": UA},
                         {"User-Agent": UA, "Referer": "https://znotes.org/"}):
                try:
                    req = urllib.request.Request(url, headers=hdrs)
                    with urllib.request.urlopen(req, timeout=IMG_TIMEOUT) as r:
                        data = r.read()
                    if not data:
                        last = (None, None, "empty")
                        continue
                    head = data[:64].lstrip()
                    if head[:9].upper().startswith(b"<!DOCTYPE") or \
                            head[:5].upper().startswith(b"<HTML"):
                        # some hosts serve an HTML block page with HTTP 200
                        last = (None, "html body served for image url", "error")
                        continue
                    return url, data, None, "ok"
                except Exception as e:
                    last = (None, str(e), "error")
            return (url,) + last

        with ThreadPoolExecutor(IMG_WORKERS) as ex:
            for url, data, err, status in ex.map(one, todo):
                if status != "ok":
                    self.failures["images"].append({"url": url, "error": err or status})
                    self.counts["image_failures"] += 1
                    continue
                name = self._asset_name(url, data, hashlib.sha1(url.encode()).hexdigest()[:12])
                dest = os.path.join(self.assets_dir, name)
                with open(dest, "wb") as f:
                    f.write(data)
                self.asset_map[url] = name
                self.counts["images"] += 1
                self.counts["assets_bytes"] += len(data)

    def localize(self, md):
        def sub_md(m):
            alt, url = m.group(1), m.group(2)
            name = self.asset_map.get(url)
            if not name:
                return m.group(0)
            return f"![{alt}](../../../assets/{name})"

        def sub_html(m):
            url = m.group(1)
            name = self.asset_map.get(url)
            if not name:
                return m.group(0)
            return m.group(0).replace(url, f"../../../assets/{name}")

        md = _md_img.sub(sub_md, md)
        md = _html_img.sub(sub_html, md)
        return md

    # ---------- course ----------
    def run(self):
        os.makedirs(self.notes_dir, exist_ok=True)
        sid = self.c["znotes_id"]
        mods_raw = api_get(f"/v1/modules?subject={sid}") or []
        if not isinstance(mods_raw, list):
            raise RuntimeError(f"modules not a list: {type(mods_raw).__name__}")
        mods = [m for m in mods_raw
                if isinstance(m, dict) and m.get("moduleType") == "note"
                and not m.get("archived") and not m.get("deleted")]
        self.counts["modules"] = len(mods)
        self.modules_meta = [{
            "id": m["_id"], "name": m.get("name"), "slug": m.get("slug"),
            "wip": bool(m.get("wip")), "metadata": m.get("metadata") or {},
            "pdf_version": m.get("pdfVersion"),
        } for m in mods]

        img_jobs_all = {}
        card_records = []
        for m in mods:
            ms = m.get("slug") or slugify(m.get("name"))
            chs_raw = api_get(f"/v1/chapters?module={m['_id']}") or []
            if not isinstance(chs_raw, list):
                self.failures["cards"].append(
                    {"module_id": m["_id"], "module": m.get("name"),
                     "error": f"chapters not a list: {type(chs_raw).__name__}"})
                continue
            chs = [c for c in chs_raw
                   if isinstance(c, dict) and not c.get("deleted") and not c.get("archived")]
            chs.sort(key=lambda c: (c.get("sortKey") if c.get("sortKey") is not None else 999))
            self.counts["chapters"] += len(chs)
            mod_tree = {}
            for ci, ch in enumerate(chs, 1):
                cs = ch.get("slug") or slugify(ch.get("name"))
                ch_dir = os.path.join(self.notes_dir, ms, f"{ci:02d}-{cs}")
                try:
                    raw_cards = api_get(f"/v1/cards?chapter={ch['_id']}")
                    if isinstance(raw_cards, dict):
                        # upstream's "empty chapter" response, e.g.
                        # {"message": "No cards found for this chapter"}
                        raw_cards = []
                    if not isinstance(raw_cards, list):
                        raise RuntimeError(f"cards not a list: {type(raw_cards).__name__}")
                except Exception as e:
                    self.failures["cards"].append(
                        {"chapter_id": ch.get("_id"), "chapter": ch.get("name"),
                         "error": str(e)})
                    mod_tree[ch.get("name") or cs] = []
                    continue
                cards = [c for c in raw_cards if isinstance(c, dict) and not c.get("deleted")]
                seen_ids = set()
                cards = [c for c in cards if not (c["_id"] in seen_ids or seen_ids.add(c["_id"]))]
                cards.sort(key=lambda c: (c.get("sortKey") if c.get("sortKey") is not None else 999))
                leaves = []
                used_leaf = set()
                for ki, card in enumerate(cards, 1):
                    md = card.get("content")
                    if not md or not md.strip():
                        continue
                    self.counts["cards"] += 1
                    title = card.get("title") or "Untitled"
                    base_leaf = f"{ki:02d}-{slugify(title)}"
                    leaf, n = base_leaf, 1
                    while leaf in used_leaf:
                        n += 1
                        leaf = f"{base_leaf}-{n}"
                    used_leaf.add(leaf)
                    img_jobs_all.setdefault(card["_id"], (md, leaf, ch_dir))
                    card_records.append({
                        "card": card, "leaf": leaf, "ch_dir": ch_dir,
                        "module": m, "chapter": ch,
                    })
                    leaves.append(title)
                mod_tree[ch.get("name") or cs] = leaves
            self.tree[m.get("name") or ms] = mod_tree

        # download every referenced image
        all_jobs = []
        for card_id, (md, _, _) in img_jobs_all.items():
            all_jobs.extend(self.collect_image_jobs(card_id, md))
        self.fetch_images(sorted(set(all_jobs)))

        # write leaves
        for rec in card_records:
            self.write_leaf(rec)
        self.counts["fetch_failures"] = len(self.failures["cards"])
        self.write_manifest()
        return self.counts

    def write_leaf(self, rec):
        card, leaf, ch_dir = rec["card"], rec["leaf"], rec["ch_dir"]
        module, chapter = rec["module"], rec["chapter"]
        os.makedirs(ch_dir, exist_ok=True)
        md = card.get("content") or ""
        self.counts["markdown_chars"] += len(md)
        local = self.localize(md)
        images = []
        for m in _md_img.finditer(md):
            url = m.group(2)
            images.append({"orig_url": url, "file": self.asset_map.get(url),
                           "alt": m.group(1)})
        stem = leaf
        note = {
            "schema": "syllabai.znotes-revision-note/1.0",
            "generated_utc": now_utc(),
            "task": TASK_ID,
            "note_id": card["_id"],
            "course_slug": self.c["course_slug"],
            "url": f"https://znotes.org/{self.c['board']}/{self.c['level']}/"
                   f"{self.c['slug']}/{module.get('slug')}/{chapter.get('slug')}/",
            "title": card.get("title"),
            "path": {
                "module": module.get("slug"),
                "chapter": chapter.get("slug"),
                "leaf": stem,
            },
            "titles": {
                "board": self.c["board"].upper(), "level": self.c["level_name"],
                "subject": self.c["subject"], "code": self.c["code"],
                "module": module.get("name"), "chapter": chapter.get("name"),
                "leaf": card.get("title"),
            },
            "author": card.get("author"),
            "created_at": card.get("createdAt"),
            "updated_at": card.get("updatedAt"),
            "sort_key": card.get("sortKey"),
            "chapter_outcomes": chapter.get("outcomes") or [],
            "module_metadata": module.get("metadata") or {},
            "has_translations": {"arabic": bool(card.get("content_arabic")),
                                 "chinese": bool(card.get("content_chinese"))},
            "images": images,
            "stats": {"markdown_chars": len(md), "images": len(images),
                      "math_spans": md.count("$")},
            "license_note": "Upstream content (c) ZNotes (znotes.org); "
                            "captured for internal study-platform use; see ZNotes/README.md",
        }
        with open(os.path.join(ch_dir, stem + ".json"), "w", encoding="utf-8") as f:
            json.dump(note, f, indent=1, ensure_ascii=False)
        with open(os.path.join(ch_dir, stem + ".md"), "w", encoding="utf-8") as f:
            f.write(local)

    def write_manifest(self):
        man = {
            "schema": "syllabai.znotes-revision-notes-course/1.0",
            "generated_utc": now_utc(),
            "task": TASK_ID,
            "base_commit": BASE_COMMIT,
            "course_slug": self.c["course_slug"],
            "board": self.c["board"], "level": self.c["level"],
            "level_name": self.c["level_name"],
            "subject": self.c["subject"], "code": self.c["code"],
            "znotes_subject_id": self.c["znotes_id"],
            "notes_base": f"https://znotes.org/{self.c['board']}/{self.c['level']}/{self.c['slug']}/",
            "syllabus_link": self.c.get("syllabusLink"),
            "updated_to": self.c.get("updatedTo"),
            "wip": self.c.get("wip", False),
            "counts": self.counts,
            "modules": self.modules_meta,
            "failures": self.failures if (self.failures["cards"] or self.failures["images"]) else {},
            "tree": self.tree,
        }
        with open(os.path.join(self.course_dir, "manifest.json"), "w", encoding="utf-8") as f:
            json.dump(man, f, indent=1, ensure_ascii=False)


# ---------- index / driver ----------

def build_index(root):
    boards = api_get("/v1/boards")
    subjects = api_get("/v1/subjects")
    lvl = {}
    for b in boards:
        for lv in b.get("levels", []):
            lvl[lv["_id"]] = {"board": b["slug"], "level": lv["slug"],
                              "level_name": lv["name"]}
    dedup = {}
    for s in subjects:
        meta = lvl.get(s.get("level"))
        if not meta or meta["board"] not in BOARDS:
            continue
        if s.get("deleted") or s.get("archived"):
            continue
        key = (meta["board"], meta["level"], s["slug"])
        prev = dedup.get(key)
        if prev is None or (prev[0].get("wip") and not s.get("wip")) or (
                str(s.get("updatedAt", "")) > str(prev[0].get("updatedAt", ""))):
            dedup[key] = (s, meta)
    courses = []
    for (board, level, slug), (s, meta) in sorted(dedup.items()):
        courses.append({
            "board": board, "level": level, "level_name": meta["level_name"],
            "subject": s["name"], "code": s.get("code"), "slug": slug,
            "course_slug": f"{board}-{level}-{slug}", "znotes_id": s["_id"],
            "wip": bool(s.get("wip")), "updatedTo": s.get("updatedTo"),
            "syllabusLink": s.get("syllabusLink"),
            "subject_updated_at": s.get("updatedAt"),
        })
    idx_dir = os.path.join(root, "ZNotes", "scripts")
    os.makedirs(idx_dir, exist_ok=True)
    out = {"schema": "syllabai.znotes-courses-index/1.0",
           "generated_utc": now_utc(), "task": TASK_ID, "courses": courses}
    with open(os.path.join(idx_dir, "courses_index.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(f"index: {len(courses)} courses -> ZNotes/scripts/courses_index.json")
    return courses


def course_done(course_dir):
    man_path = os.path.join(course_dir, "manifest.json")
    if not os.path.exists(man_path):
        return False
    try:
        man = json.load(open(man_path, encoding="utf-8"))
    except Exception:
        return False
    cnt = man.get("counts", {})
    # image_failures are documented dead third-party hotlinks; tolerate them,
    # but a card/structural fetch failure means the course must be re-run.
    return cnt.get("fetch_failures", 1) == 0 and man.get("schema", "").endswith("/1.0")


def build_global_manifest(root):
    zn = os.path.join(root, "ZNotes")
    courses = {}
    tot = {"modules": 0, "chapters": 0, "cards": 0, "images": 0,
           "image_failures": 0, "fetch_failures": 0, "markdown_chars": 0,
           "assets_bytes": 0}
    for slug in sorted(os.listdir(zn)):
        p = os.path.join(zn, slug, "manifest.json")
        if not os.path.isfile(p):
            continue
        man = json.load(open(p, encoding="utf-8"))
        cnt = man["counts"]
        courses[slug] = {"course_slug": slug, "notes_base": man["notes_base"],
                         "subject": man.get("subject"), "code": man.get("code"),
                         "board": man.get("board"), "level": man.get("level"),
                         "wip": man.get("wip", False), "counts": cnt}
        for k in tot:
            tot[k] += cnt.get(k, 0)
    out = {
        "schema": "syllabai.znotes-revision-notes/1.0",
        "generated_utc": now_utc(),
        "task": TASK_ID,
        "source": {"site": "https://znotes.org", "api": "https://api.znotes.org",
                   "boards": ["caie", "edexcel"]},
        "totals": tot,
        "scraped_courses": len(courses),
        "courses": courses,
    }
    with open(os.path.join(zn, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(f"global manifest: {len(courses)} courses, {tot['cards']} cards, "
          f"{tot['images']} assets, {tot['assets_bytes']/1e6:.0f} MB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", action="store_true")
    ap.add_argument("--course")
    ap.add_argument("--board")
    ap.add_argument("--level")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--manifest", action="store_true")
    ap.add_argument("--time-budget", type=int, default=480)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--root", default=DEFAULT_ROOT)
    a = ap.parse_args()
    t0 = time.time()

    if a.index:
        build_index(a.root)
        return
    if a.manifest:
        build_global_manifest(a.root)
        return

    idx = os.path.join(a.root, "ZNotes", "scripts", "courses_index.json")
    if not os.path.exists(idx):
        courses = build_index(a.root)
    else:
        courses = json.load(open(idx, encoding="utf-8"))["courses"]
    if a.course:
        sel = [c for c in courses if c["course_slug"] == a.course]
        if not sel:
            sys.exit(f"unknown course {a.course}")
    else:
        sel = [c for c in courses
               if (not a.board or c["board"] == a.board)
               and (not a.level or c["level"] == a.level)]
        if not (a.board or a.level or a.all):
            sys.exit("pick --course / --board [--level] / --all")

    done = skipped = scraped = 0
    for c in sel:
        cdir = os.path.join(a.root, "ZNotes", c["course_slug"])
        if not a.force and course_done(cdir):
            done += 1
            continue
        if time.time() - t0 > a.time_budget:
            skipped += 1
            continue
        print(f"== scraping {c['course_slug']} ({c['subject']} {c['code'] or ''})", flush=True)
        try:
            cnt = CourseScraper(c, a.root).run()
            scraped += 1
            print(f"   done: {cnt['chapters']} chapters, {cnt['cards']} cards, "
                  f"{cnt['images']} assets, {cnt['image_failures']} img_fail, "
                  f"{cnt['assets_bytes']/1e6:.1f} MB, "
                  f"elapsed {time.time()-t0:.0f}s", flush=True)
        except Exception as e:
            print(f"   !! FAILED: {e}", flush=True)
    print(f"summary: scraped={scraped} already_done={done} deferred={skipped} "
          f"of {len(sel)} courses, wall {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
