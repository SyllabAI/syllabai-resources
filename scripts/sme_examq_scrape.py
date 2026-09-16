#!/usr/bin/env python3
"""
SME Exam Questions scraper — Save My Exams, Edexcel IGCSE Chemistry (4CH1, syllabus /19/).

Pulls the 28 topic-level "Exam Questions" pages (each fully server-rendered with all
questions inside <script id="__NEXT_DATA__">), converts the TipTap JSON docs
(problem + solution) to Markdown, converts Wiris MathML equations to KaTeX LaTeX,
downloads question images to per-topic assets/, and writes a structured corpus:

  SME-ExamQuestion/
    manifest.json
    README.md
    {section-slug}/{topic-slug}/
      topic.json        structured, atomized questions+parts (machine-readable)
      questions.md      human-readable question paper
      mark-schemes.md   human-readable mark scheme / model answers
      assets/           images (original format: webp/png/gif/jpg)

Operator authorization for SME material: see LICENSE-DATA.md ("Amendment
2026-09-17 — Save My Exams authorization (operator attestation)").

Usage:
  sme_examq_scrape.py [--out DIR] [--only SLUG ...] [--limit N] [--delay S]
                      [--skip-assets] [--offline-landing FILE]
Stdlib only. No secrets required (public pages).
"""
import argparse
import hashlib
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

BASE = "https://www.savemyexams.com"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
LANDING = f"{BASE}/igcse/chemistry/edexcel/19/topic-questions/"
COURSE = {"board": "Edexcel", "level": "IGCSE", "subject": "Chemistry",
          "code": "4CH1", "syllabus_version": "2017", "sme_syllabus_id": "19"}
NOTES_ROOT = "Chemistry IGCSE Revision Notes"
SCHEMA = "syllabai.sme-exam-questions/1.0"

SECTION_LETTERS = "abcdefghijklmnopqrstuvwxyz"


# ----------------------------------------------------------------------------- http
def http_get(url: str, *, binary: bool = False, retries: int = 3, delay: float = 0.8):
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": UA, "Accept": "*/*",
                "Accept-Language": "en-GB,en;q=0.9"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                return data if binary else data.decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(delay * (attempt + 1))
    raise RuntimeError(f"GET failed after {retries} tries: {url}: {last}")


# ------------------------------------------------------------------- next data parse
def parse_next_data(html: str) -> dict:
    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
                  html, re.S)
    if not m:
        raise RuntimeError("__NEXT_DATA__ not found")
    return json.loads(m.group(1))["props"]["pageProps"]


def topic_urls_from_landing(html: str) -> list:
    urls = sorted(set(re.findall(
        r'href="(/igcse/chemistry/edexcel/19/topic-questions/[a-z0-9-]+/[a-z0-9-]+/exam-questions/)"',
        html)))
    return urls


# ------------------------------------------------------------------- mathml -> latex
_MO_MAP = {
    "\u21cc": r"\rightleftharpoons", "\u2192": r"\rightarrow", "\u2190": r"\leftarrow",
    "\u2194": r"\leftrightarrow", "\u2191": r"\uparrow", "\u2193": r"\downarrow",
    "\u21d2": r"\Rightarrow", "\u21d4": r"\Leftrightarrow", "\u21c4": r"\rightleftarrows",
    "\u0394": r"\Delta", "\u2022": r"\bullet", "\u2248": r"\approx",
    "\u2264": r"\leq", "\u2265": r"\geq", "\u00d7": r"\times", "\u00f7": r"\div",
    "\u2212": "-", "\u2013": "--", "\u2014": "---", "\u221e": r"\infty",
    "\u2211": r"\sum", "\u2206": r"\Delta", "\u2261": r"\equiv", "\u2260": r"\neq",
    "\u221a": r"\sqrt{}", "\u00b1": r"\pm", "\u2032": "'", "\u223f": r"\sim",
    "\u00b0": r"^{\circ}", "\u2736": r"\star", "\u22c5": r"\cdot",
    # A-level maths operators (IAL pages use these; missing entries used to
    # fail the whole equation into spoken-text fallback)
    "*": r"\ast", "\u2218": r"\circ", "\u2208": r"\in", "\u2209": r"\notin",
    "\u2229": r"\cap", "\u222a": r"\cup", "\u2282": r"\subset",
    "\u2286": r"\subseteq", "\u2205": r"\emptyset", "\u221d": r"\propto",
    "\u2026": r"\dots", "\u22ef": r"\cdots", "\u21d0": r"\Leftarrow",
    "\u22ee": r"\vdots", "\u2033": "''", "\u00ac": r"\neg",
    "\u2234": r"\therefore", "\u2235": r"\because", "\u2016": r"\|",
}


def _local(tag):
    return tag.split("}", 1)[-1] if "}" in tag else tag


class MathML2Latex:
    """Small converter for the chemistry MathML subset Wiris emits."""

    def __init__(self):
        self.fail = False

    def convert(self, mathml: str):
        self.fail = False
        try:
            root = ET.fromstring(mathml)
        except ET.ParseError:
            return None
        latex = self._walk(root)
        if self.fail or not latex:
            return None
        latex = latex.strip()
        # Wiris emits one \\mathrm{...} per word with no separator: fix spacing
        latex = re.sub(r"(\\mathrm\{[^}]*\})(?=\\mathrm\{)", r"\1 ", latex)
        return latex

    def _walk(self, el) -> str:
        tag = _local(el.tag)
        if tag in ("math", "semantics", "mrow", "mstyle", "mpadded", "mphantom"):
            inner = "".join(self._walk(c) for c in el)
            return inner if tag != "math" else " ".join(self._walk(c) for c in el)
        if tag == "annotation":
            return ""  # Wiris params/alt encoding alongside the real expression
        if tag in ("mi", "mn"):
            txt = (el.text or "").strip()
            if not txt:
                return ""
            if tag == "mi" and len(txt) > 1:
                return r"\mathrm{" + txt + "}"
            return txt
        if tag == "mo":
            txt = (el.text or "").strip()
            if not txt:
                return ""
            if txt in _MO_MAP:
                return _MO_MAP[txt]
            if all(ch.isalnum() or ch in "+-=()<>,.;:!?'\"/ " for ch in txt):
                return txt
            self.fail = True
            return ""
        if tag == "mtext":
            txt = (el.text or "").strip()
            return r"\text{" + txt + "}" if txt else ""
        if tag == "mspace":
            return r"\,"
        if tag == "mfrac":
            kids = list(el)
            if len(kids) == 2:
                return (r"\frac{" + self._walk(kids[0]) + "}{" +
                        self._walk(kids[1]) + "}")
            self.fail = True
            return ""
        if tag == "msqrt":
            return r"\sqrt{" + "".join(self._walk(c) for c in el) + "}"
        if tag in ("msub", "msup", "msubsup"):
            kids = list(el)
            if tag == "msub" and len(kids) == 2:
                return self._walk(kids[0]) + "_{" + self._walk(kids[1]) + "}"
            if tag == "msup" and len(kids) == 2:
                return self._walk(kids[0]) + "^{" + self._walk(kids[1]) + "}"
            if len(kids) == 3:
                return (self._walk(kids[0]) + "_{" + self._walk(kids[1]) + "}^{"
                        + self._walk(kids[2]) + "}")
            self.fail = True
            return ""
        if tag == "mover" and len(list(el)) == 2:
            base, over = el[0], el[1]
            ot = (over.text or "").strip()
            if ot in ("\u00af", "\u203e"):
                return r"\overline{" + self._walk(base) + "}"
            return (r"\overset{" + self._walk(over) + "}{" + self._walk(base) + "}")
        if tag == "munder" and len(list(el)) == 2:
            base, under = el[0], el[1]
            return (r"\underset{" + self._walk(under) + "}{" + self._walk(base) + "}")
        if tag in ("mtable", "mlabeledtr", "mtr", "mtd", "maction", "merror", "mglyph"):
            self.fail = True
            return ""
        # unknown element
        self.fail = True
        return ""


M2L = MathML2Latex()


# --------------------------------------------------------------------- tip tap -> md
# SME encodes commentary / final-answer / exam-mark semantics as text MARKS
# whose real type lives in mark.attrs.type (outer type is visual styling):
#   attrs.type == 'examMark'    -> creditable marking statement  (render bold)
#   attrs.type == 'commentary'  -> examiner commentary           (blockquote/italic)
#   attrs.type == 'finalAnswer' -> the highlighted final answer  (bold + label)
SEMANTIC_MARKS = {"examMark", "commentary", "finalAnswer"}
VOID_MARKERS = {"commentary": "> **Examiner commentary**", "finalAnswer": "> **Final answer**"}
SKIP_NODES = {"examMark"}


def text_semantic_marks(node) -> set:
    sems = set()
    for m in node.get("marks") or []:
        attrs = m.get("attrs")
        at = attrs.get("type") if isinstance(attrs, dict) else None
        if at in SEMANTIC_MARKS:
            sems.add(at)
    return sems


def clean_text(t: str) -> str:
    t = t.replace("\u00a0", " ").replace("\u200b", "")
    return t


def esc_math_delims(t: str) -> str:
    # avoid $ ambiguity with our inline math
    return t.replace("$", "\\$")


def render_inline(nodes, ctx) -> str:
    out = []
    for n in nodes or []:
        t = n.get("type")
        if t == "text":
            s = clean_text(n.get("text") or "")
            s = esc_math_delims(s)
            sems = text_semantic_marks(n)
            if "examMark" in sems or "finalAnswer" in sems:
                s = f"**{s}**"
            if "commentary" in sems:
                s = f"*{s}*"
            styled = bool(sems)
            for m in n.get("marks") or []:
                mt = m.get("type")
                if styled and mt in ("bold", "emphasis", "italic", "underline"):
                    continue  # semantic wrap supersedes cosmetic styling
                if mt == "bold":
                    s = f"**{s}**"
                elif mt in ("emphasis", "italic"):
                    s = f"*{s}*"
                elif mt == "underline":
                    s = f"<u>{s}</u>"
                elif mt == "subscript":
                    s = f"<sub>{s}</sub>"
                elif mt == "superscript":
                    s = f"<sup>{s}</sup>"
                elif mt == "code":
                    s = f"`{s}`"
                elif mt == "link":
                    href = (m.get("attrs") or {}).get("href") or ""
                    if href:
                        s = f"[{s}]({href})"
                # strike/highlight/... -> keep plain
            out.append(s)
        elif t == "hardBreak":
            out.append("\n")
        elif t == "equation":
            attrs = n.get("attrs") or {}
            mathml = attrs.get("mathml") or ""
            latex = M2L.convert(mathml)
            if latex:
                out.append(f"${latex}$")
                ctx.setdefault("equations", []).append({"latex": latex, "mathml": mathml,
                                                        "alt": attrs.get("alt")})
            else:
                alt = attrs.get("alt") or "equation"
                out.append(f"`{alt}`")
        elif t == "image":  # inline image variant (defensive)
            src, name = ctx.get("asset_fn", lambda *_: (None, None))(n.get("attrs") or {})
            if name:
                out.append(f"![{n.get('attrs', {}).get('alt') or ''}](assets/{name})")
        elif t == "text_" :  # pragma: no cover
            pass
        else:
            # unknown inline node: flatten children defensively
            if isinstance(n.get("content"), list):
                out.append(render_inline(n["content"], ctx))
    return "".join(out)


def render_blocks(nodes, ctx) -> str:
    """Render TipTap block list -> markdown text."""
    chunks = []
    for n in nodes or []:
        t = n.get("type")
        if t == "paragraph":
            content = n.get("content") or []
            texts = [c for c in content if c.get("type") == "text"]
            per_text = [text_semantic_marks(c) for c in texts]
            all_sems = set().union(*per_text) if per_text else set()
            s = render_inline(content, ctx).strip()
            if s:
                if (per_text and all_sems == {"commentary"}
                        and all("commentary" in p for p in per_text)):
                    chunks.append("> " + s + "\n")          # examiner commentary
                elif ("finalAnswer" in all_sems and per_text
                      and all("finalAnswer" in p for p in per_text)):
                    chunks.append("**Final answer:** " + s + "\n")
                else:
                    chunks.append(s + "\n")
        elif t == "heading":
            level = (n.get("attrs") or {}).get("level") or 3
            s = render_inline(n.get("content"), ctx).strip()
            if s:
                chunks.append("#" * min(level, 6) + " " + s + "\n")
        elif t == "bulletList":
            items = n.get("content") or []
            lines = []
            for li in items:
                if li.get("type") != "listItem":
                    continue
                txt = render_list_item(li, ctx, indent="")
                lines.append("- " + txt)
            if lines:
                chunks.append("\n".join(lines) + "\n")
        elif t == "orderedList":
            start = (n.get("attrs") or {}).get("start") or 1
            items = n.get("content") or []
            lines = []
            for i, li in enumerate(items):
                if li.get("type") != "listItem":
                    continue
                txt = render_list_item(li, ctx, indent="")
                lines.append(f"{start + i}. " + txt)
            if lines:
                chunks.append("\n".join(lines) + "\n")
        elif t == "blockquote":
            inner = render_blocks(n.get("content"), ctx).strip()
            if inner:
                quoted = "\n".join("> " + ln for ln in inner.splitlines())
                chunks.append(quoted + "\n")
        elif t == "callout":
            variant = (n.get("attrs") or {}).get("variant") or "note"
            inner = render_blocks(n.get("content"), ctx).strip()
            if inner:
                quoted = "\n".join("> " + ln for ln in inner.splitlines())
                chunks.append(f"> **[{variant}]**\n" + quoted + "\n")
        elif t == "figure":
            attrs = n.get("attrs") or {}
            src, name = ctx["asset_fn"](attrs)
            alt = attrs.get("alt") or ""
            if name:
                chunks.append(f"![{alt}](assets/{name})\n")
            else:
                chunks.append(f"![{alt}]({src}) <!-- asset download failed -->\n")
            if attrs.get("caption"):
                chunks.append(f"*{attrs['caption']}*\n")
        elif t == "table":
            md = render_table(n, ctx)
            if md:
                chunks.append(md + "\n")
        elif t in VOID_MARKERS:
            chunks.append(VOID_MARKERS[t] + "\n")
        elif t in SKIP_NODES:
            pass
        else:
            # unknown block: flatten
            if isinstance(n.get("content"), list) and n.get("content"):
                s = render_blocks(n["content"], ctx).strip()
                if s:
                    chunks.append(s + "\n")
    text = "\n".join(chunks)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def render_list_item(li, ctx, indent="") -> str:
    parts = []
    for c in li.get("content") or []:
        if c.get("type") == "paragraph":
            parts.append(render_inline(c.get("content"), ctx).strip())
        elif c.get("type") in ("bulletList", "orderedList"):
            sub = render_blocks([c], ctx).strip()
            indented = "\n".join("  " + ln for ln in sub.splitlines())
            parts.append("\n" + indented)
        else:
            sub = render_blocks([c], ctx).strip()
            if sub:
                parts.append(sub)
    joined = " ".join(p for p in parts if p and not p.startswith("\n"))
    nested = [p for p in parts if p.startswith("\n")]
    out = joined
    for nn in nested:
        out += "\n" + nn
    return out.strip()


def render_table(tbl, ctx) -> str:
    rows = []
    for tr in tbl.get("content") or []:
        if _local(tr.get("type") or "") != "tableRow":
            continue
        cells = []
        for tc in tr.get("content") or []:
            if _local(tc.get("type") or "") not in ("tableCell", "tableHeader"):
                continue
            cell_md = render_blocks(tc.get("content"), ctx).strip()
            cell_md = cell_md.replace("|", "\\|").replace("\n", "<br>")
            cells.append(cell_md if cell_md else " ")
        rows.append(cells)
    if not rows:
        return ""
    ncols = max(len(r) for r in rows)
    for r in rows:
        r += [" "] * (ncols - len(r))
    lines = ["| " + " | ".join(rows[0]) + " |",
             "|" + "---|" * ncols]
    for r in rows[1:]:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


# ------------------------------------------------------------------------- assets
def normalize_cdn_url(src: str) -> str:
    # strip cloudflare image-resize wrapper, keep original upload
    return re.sub(r"^(https://cdn\.savemyexams\.com)/cdn-cgi/image/[^/]+/",
                  r"\1/", src or "")


class AssetManager:
    def __init__(self, assets_dir: Path, delay: float = 0.3):
        self.dir = assets_dir
        self.delay = delay
        self.map = {}          # url -> filename
        self.failures = []
        self.counter = 0

    def filename_for(self, url: str, alt: str) -> str:
        if url in self.map:
            return self.map[url]
        self.counter += 1
        ext = Path(urllib.parse.urlparse(url).path).suffix.lower() or ".bin"
        if ext not in (".webp", ".png", ".gif", ".jpg", ".jpeg", ".svg"):
            ext = ".bin"
        slug = re.sub(r"[^a-z0-9]+", "-", (alt or "img").lower()).strip("-")[:48]
        slug = slug or "img"
        name = f"{self.counter:03d}-{slug}{ext}"
        self.map[url] = name
        return name

    def fetch_all(self):
        self.dir.mkdir(parents=True, exist_ok=True)
        for url, name in self.map.items():
            target = self.dir / name
            if target.exists() and target.stat().st_size > 0:
                continue
            try:
                data = http_get(url, binary=True, retries=3, delay=self.delay)
                if len(data) < 64:
                    raise RuntimeError(f"suspiciously small ({len(data)} B)")
                if not (data[:4] in (b"RIFF", b"\x89PNG", b"GIF8", b"<svg", b"<?xm")
                        or data[:3] == b"\xff\xd8\xff"):
                    raise RuntimeError("not an image payload")
                target.write_bytes(data)
                time.sleep(self.delay)
            except Exception as e:  # noqa: BLE001
                self.failures.append({"url": url, "name": name, "error": str(e)[:160]})


# ------------------------------------------------------------------ topic processing
def notes_folder_for(section: dict, topic: dict) -> str:
    si = section.get("_order", 0)
    ti = topic.get("_order", 0)
    letter = SECTION_LETTERS[ti] if ti < len(SECTION_LETTERS) else chr(ord('a') + ti)
    return f"{NOTES_ROOT}/{section['attributes']['name']}/{letter}. {topic['attributes']['name']}"


def collect_disk_state(out_root: Path) -> dict:
    """Map topic_slug -> result summary from topic.json files already on disk
    (resume support: completed topics are reused across chunked runs)."""
    state = {}
    if not out_root.is_dir():
        return state
    for tj in sorted(out_root.glob("*/*/topic.json")):
        try:
            t = json.loads(tj.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        slug = t.get("topic", {}).get("slug")
        if not slug:
            continue
        qs = t.get("questions") or []
        n_parts = sum(len(q.get("parts") or []) for q in qs)
        n_assets = len(list((tj.parent / "assets").glob("*"))) if (tj.parent / "assets").is_dir() else 0
        scrape = t.get("scrape") or {}
        state[slug] = {
            "url": t.get("source", {}).get("page_url"),
            "section_slug": t.get("section", {}).get("slug"),
            "section_name": t.get("section", {}).get("name"),
            "topic_slug": slug,
            "topic_name": t.get("topic", {}).get("name"),
            "questions": len(qs), "parts": n_parts,
            "total_marks": sum(q.get("total_marks") or 0 for q in qs),
            "assets": n_assets,
            "asset_failures": scrape.get("asset_failures") or [],
            "missing_questions": scrape.get("questions_missing") or [],
            "equations": sum(len(p.get("equations") or [])
                             for q in qs for p in q.get("parts") or []),
            "files": ["topic.json", "questions.md", "mark-schemes.md"],
            "reused": True,
        }
    return state


def process_topic(url: str, out_root: Path, delay: float, skip_assets: bool) -> dict:
    html = http_get(BASE + url)
    pp = parse_next_data(html)
    sec_by_slug = {s["attributes"]["slug"]: s for s in pp["sections"]}
    topic_by_id = {t["id"]: t for t in pp["topics"]}
    sec_by_id = {s["id"]: s for s in pp["sections"]}

    # page topic from the URL slug (2nd-to-last path segment before /exam-questions/)
    m = re.match(r"/igcse/chemistry/edexcel/19/topic-questions/([a-z0-9-]+)/([a-z0-9-]+)/exam-questions/", url)
    sec_slug, topic_slug = m.group(1), m.group(2)
    topic = next(t for t in pp["topics"] if t["attributes"]["slug"] == topic_slug)
    section = sec_by_id[topic["relationships"]["section"]["data"]["id"]]
    section["_order"] = section["attributes"]["order"]
    topic["_order"] = topic["attributes"]["order"]

    qset = next(s for s in pp["questionSets"]
                if s["relationships"]["topic"]["data"]["id"] == topic["id"])
    set_order_ids = [r["id"] for r in qset["relationships"]["questions"]["data"]]
    q_by_id = {q["id"]: q for q in pp["questions"]}
    missing = [qid for qid in set_order_ids if qid not in q_by_id]

    # subtopics of this topic + revision-note rels
    subtopics = []
    for st in pp["subtopics"]:
        if st["relationships"]["topic"]["data"]["id"] == topic["id"]:
            rn = (st["relationships"].get("revision_note") or {}).get("data") or {}
            subtopics.append({"slug": st["attributes"]["slug"],
                              "name": st["attributes"]["name"],
                              "revision_note_id": rn.get("id")})

    out_dir = out_root / section["attributes"]["slug"] / topic_slug
    assets_dir = out_dir / "assets"

    ctx = {"asset_fn": None, "equations": []}
    assets = AssetManager(assets_dir, delay=delay)

    def asset_fn(fig_attrs):
        src = normalize_cdn_url(fig_attrs.get("src") or "")
        if not src:
            return None, None
        name = assets.filename_for(src, fig_attrs.get("alt"))
        return src, name

    ctx["asset_fn"] = asset_fn

    # render all questions (order = set order)
    questions_out = []
    for qid in set_order_ids:
        q = q_by_id.get(qid)
        if q is None:
            continue
        a = q["attributes"]
        parts_out = []
        for pi, part in enumerate(a.get("parts") or []):
            ctx["equations"] = []
            problem_md = render_blocks(part.get("problem"), ctx)
            solution_md = render_blocks(part.get("solution"), ctx)
            sd = part.get("source_data") or {}
            mc = part.get("marking_context") or {}
            ptype = part.get("question_type") or "structured"
            choices = None
            if ptype == "multiple_choice" and part.get("choices"):
                choices = []
                for ci, ch in enumerate(sorted(part["choices"], key=lambda c: c.get("order", 0))):
                    label = chr(ord("A") + ci)
                    choices.append({"label": label,
                                    "is_correct": bool(ch.get("is_correct")),
                                    "text_md": render_inline(ch.get("content"), ctx).strip()})
            entry = {
                "id": part.get("id"), "order": part.get("order", pi),
                "question_type": ptype,
                "marks": part.get("marks"),
                "command_word": mc.get("command_word"),
                "source_paper": {"date": sd.get("paper_date"),
                                 "number": sd.get("paper_number"),
                                 "question_number": sd.get("question_number"),
                                 "question_part": sd.get("question_part")},
                "spec_point_ids": part.get("spec_point_ids") or [],
                "part_tier": part.get("tier"),
                "problem_md": problem_md,
                "solution_md": solution_md,
            }
            if choices is not None:
                entry["choices"] = choices
            if ctx["equations"]:
                entry["equations"] = ctx["equations"]
            parts_out.append(entry)
        total_marks = sum(p.get("marks") or 0 for p in parts_out)
        questions_out.append({
            "id": qid, "order": a.get("order"),
            "difficulty": a.get("difficulty"), "style": a.get("style"),
            "total_marks": total_marks, "parts": parts_out,
        })

    # download assets
    asset_failures = []
    if not skip_assets:
        assets.fetch_all()
        asset_failures = assets.failures

    # ------- topic.json
    topic_doc = {
        "schema": SCHEMA,
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source": {"provider": "Save My Exams", "page_url": BASE + url,
                   "license": "operator-authorized; see repo LICENSE-DATA.md "
                              "(SME attestation 2026-09-17)"},
        "curriculum": COURSE,
        "section": {"slug": section["attributes"]["slug"],
                    "name": section["attributes"]["name"]},
        "topic": {"id": topic["id"], "slug": topic_slug,
                  "name": topic["attributes"]["name"],
                  "order": topic["attributes"]["order"]},
        "related_revision_notes_folder": notes_folder_for(section, topic),
        "subtopics": subtopics,
        "question_set": {"id": qset["id"],
                         "difficulties": qset["attributes"].get("question_difficulties"),
                         "question_count": len(set_order_ids)},
        "scrape": {"questions_embedded": len(q_by_id and [i for i in set_order_ids if i in q_by_id]),
                   "questions_missing": missing,
                   "asset_failures": asset_failures},
        "questions": questions_out,
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "topic.json").write_text(json.dumps(topic_doc, indent=1, ensure_ascii=False),
                                        encoding="utf-8")

    # ------- questions.md / mark-schemes.md
    def part_label(qn_idx, part):
        sd = part.get("source_paper") or {}
        qn = sd.get("question_number")
        qp = sd.get("question_part")
        if isinstance(qn, int):
            num = str(qn)
        else:
            num = str(qn_idx + 1)
        letter = None
        if qp and re.match(r"^[a-z]$", str(qp), re.I):
            letter = str(qp).lower()
        else:
            letters = [p.get("order", i) for i, p in enumerate([])]
            letter = None
        return num, letter

    qmd = [f"# Exam Questions — {topic['attributes']['name']}",
           f"**{section['attributes']['name']}** · Edexcel IGCSE Chemistry 4CH1",
           f"> Source: [{BASE + url}]({BASE + url}) · {len(questions_out)} questions · "
           f"total {sum(q['total_marks'] for q in questions_out)} marks\n"]
    smd = [f"# Mark Schemes — {topic['attributes']['name']}",
           f"**{section['attributes']['name']}** · Edexcel IGCSE Chemistry 4CH1\n"]

    for qi, q in enumerate(questions_out, 1):
        diff = q.get("difficulty") or "?"
        qmd.append(f"\n## Q{qi} — {diff} — {q['total_marks']} marks")
        smd.append(f"\n## Q{qi} — {diff} — {q['total_marks']} marks")
        for pi, p in enumerate(q["parts"]):
            num, letter = part_label(qi, p)
            label = f"{num}{'(' + letter + ')' if letter else ''}"
            marks = p.get("marks")
            cw = p.get("command_word")
            meta = []
            if marks is not None:
                meta.append(f"{marks} mark" + ("s" if marks != 1 else ""))
            if cw:
                meta.append(f"command: {cw}")
            meta.append(p.get("question_type", "structured"))
            src = p.get("source_paper") or {}
            prov = " · ".join(str(x) for x in (src.get("date"), src.get("number")) if x)
            if prov:
                meta.append(f"from paper {prov}")
            qmd.append(f"\n### {label} — " + " — ".join(meta))
            qmd.append(p["problem_md"] or "*(no question text)*")
            if p.get("choices"):
                for ch in p["choices"]:
                    qmd.append(f"- **{ch['label']}.** {ch['text_md']}")
            smd.append(f"\n### {label} — {marks if marks is not None else '?'} marks")
            if p.get("choices"):
                correct = [c for c in p["choices"] if c["is_correct"]]
                if correct:
                    smd.append("**Correct answer: " +
                               ", ".join(c["label"] for c in correct) + "** — " +
                               " / ".join(c["text_md"] for c in correct) + "\n")
            smd.append(p["solution_md"] or "*(no mark scheme text)*")

    (out_dir / "questions.md").write_text("\n".join(qmd) + "\n", encoding="utf-8")
    (out_dir / "mark-schemes.md").write_text("\n".join(smd) + "\n", encoding="utf-8")

    n_parts = sum(len(q["parts"]) for q in questions_out)
    total_marks = sum(q["total_marks"] for q in questions_out)
    return {
        "url": BASE + url, "section_slug": section["attributes"]["slug"],
        "section_name": section["attributes"]["name"],
        "topic_slug": topic_slug, "topic_name": topic["attributes"]["name"],
        "questions": len(questions_out), "parts": n_parts,
        "total_marks": total_marks,
        "assets": len(assets.map),
        "asset_failures": asset_failures,
        "missing_questions": missing,
        "equations": sum(len(p.get("equations", [])) for q in questions_out
                         for p in q["parts"]),
        "files": ["topic.json", "questions.md", "mark-schemes.md"],
    }


# ------------------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="/home/z/my-project/download/syllabai-resources/SME-ExamQuestion")
    ap.add_argument("--only", nargs="*", default=None,
                    help="topic slugs to include (default: all 28)")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--delay", type=float, default=0.8)
    ap.add_argument("--skip-assets", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="re-scrape topics even if topic.json exists on disk")
    ap.add_argument("--manifest-only", action="store_true",
                    help="(re)build manifest.json + README.md from disk state and exit")
    ap.add_argument("--offline-landing", default=None,
                    help="use a saved landing.html instead of fetching")
    args = ap.parse_args()

    out_root = Path(args.out)
    disk_state = collect_disk_state(out_root)
    if args.manifest_only:
        print(f"{len(disk_state)} topics on disk; writing manifest only")
        write_global(out_root, list(disk_state.values()), failures=[])
        return
    if args.offline_landing:
        landing_html = Path(args.offline_landing).read_text(encoding="utf-8")
    else:
        landing_html = http_get(LANDING)
    urls = topic_urls_from_landing(landing_html)
    if args.only:
        urls = [u for u in urls if any(o in u for o in args.only)]
    if args.limit:
        urls = urls[:args.limit]
    print(f"{len(urls)} topic pages in scope")

    results = []
    t0 = time.time()
    for i, u in enumerate(urls, 1):
        slug = u.rstrip("/").split("/")[-2]
        if slug in disk_state and not args.force:
            results.append(disk_state[slug])
            print(f"[{i}/{len(urls)}] {slug}: reused from disk "
                  f"(q={disk_state[slug]['questions']}, assets={disk_state[slug]['assets']})")
            continue
        try:
            r = process_topic(u, out_root, delay=args.delay, skip_assets=args.skip_assets)
            results.append(r)
            print(f"[{i}/{len(urls)}] {r['section_slug']}/{r['topic_slug']}: "
                  f"q={r['questions']} parts={r['parts']} marks={r['total_marks']} "
                  f"assets={r['assets']} eq={r['equations']} "
                  f"missing_q={len(r['missing_questions'])} "
                  f"asset_fail={len(r['asset_failures'])}")
        except Exception as e:  # noqa: BLE001
            print(f"[{i}/{len(urls)}] !! FAIL {slug}: {e}")
            results.append({"topic_slug": slug, "url": BASE + u, "error": str(e)[:200]})

    ok = [r for r in results if "error" not in r]
    totals = {
        "topics_ok": len(ok), "topics_failed": len(results) - len(ok),
        "questions": sum(r["questions"] for r in ok),
        "parts": sum(r["parts"] for r in ok),
        "marks": sum(r["total_marks"] for r in ok),
        "assets": sum(r["assets"] for r in ok),
        "asset_failures": sum(len(r["asset_failures"]) for r in ok),
        "missing_questions": sum(len(r["missing_questions"]) for r in ok),
        "equations": sum(r["equations"] for r in ok),
        "secs": round(time.time() - t0, 1),
    }

    write_global(out_root, ok, failures=[r for r in results if "error" in r])
    print(json.dumps(totals, indent=2))
    if totals["topics_failed"]:
        sys.exit(1)


def write_global(out_root: Path, ok: list, failures: list):
    """manifest.json + README.md from the union of run + disk results."""
    if not ok:
        return
    disk = collect_disk_state(out_root)
    merged = {r["topic_slug"]: r for r in ok}
    merged.update({k: v for k, v in disk.items() if k not in merged})
    topics = sorted(merged.values(), key=lambda r: (r["section_slug"], r["topic_slug"]))
    totals = {
        "topics": len(topics),
        "questions": sum(r["questions"] for r in topics),
        "parts": sum(r["parts"] for r in topics),
        "marks": sum(r["total_marks"] for r in topics),
        "assets": sum(r["assets"] for r in topics),
        "asset_failures": sum(len(r["asset_failures"]) for r in topics),
        "missing_questions": sum(len(r["missing_questions"]) for r in topics),
        "equations": sum(r["equations"] for r in topics),
    }
    manifest = {
        "schema": SCHEMA,
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source": {"provider": "Save My Exams", "landing_url": LANDING,
                   "license": "operator-authorized; see repo LICENSE-DATA.md "
                              "(SME attestation 2026-09-17)"},
        "course": COURSE,
        "totals": totals,
        "topics": topics,
        "failures": failures,
    }
    out_root.mkdir(parents=True, exist_ok=True)
    (out_root / "manifest.json").write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    write_readme(out_root, totals)
    return totals


def write_readme(out_root: Path, totals: dict):
    txt = f"""# SME Exam Questions — Edexcel IGCSE Chemistry (4CH1)

Scraped corpus of **Save My Exams** exam questions (topic questions) for
Edexcel IGCSE Chemistry, syllabus 2017 (4CH1). Every question carries its
mark scheme / model answer, per-part marks, command word, original paper
provenance, and SME spec-point references. Topics mirror the revision-notes
corpus in `../{NOTES_ROOT}/` (section/subtopic tree is the same).

**Provenance & authorization:** scraped from savemyexams.com under the
operator's documented SME authorization — see `../LICENSE-DATA.md`
("Amendment 2026-09-17 — Save My Exams authorization (operator attestation)").
Questions are attributed to their original Edexcel papers where SME records
that provenance (per-part `source_paper`).

## Layout

    SME-ExamQuestion/
      manifest.json                     course-level index + totals
      <section-slug>/<topic-slug>/
        topic.json    structured corpus: questions -> parts -> problem/solution
        questions.md  human-readable question paper (images inline)
        mark-schemes.md  human-readable mark scheme / model answers
        assets/       question images (original CDN format: webp/png/gif)

## topic.json schema (syllabai.sme-exam-questions/1.0)

- `questions[]`: `id`, `difficulty` (easy/medium/hard), `style`, `total_marks`
- `questions[].parts[]`:
  - `marks`, `command_word`, `question_type` (`structured` | `multiple_choice`)
  - `source_paper`: `{{date, number, question_number, question_part}}` (provenance)
  - `spec_point_ids`: SME spec-point ids (raw; resolution to 4CH1 codes is downstream)
  - `problem_md` / `solution_md`: Markdown render of the TipTap docs
  - `choices[]` (MCQ): `label`, `is_correct`, `text_md`
  - `equations[]`: KaTeX `latex` + raw Wiris `mathml` (lossless re-processing)
- `subtopics[]`: SME subtopic slugs + `revision_note_id` (maps to the notes corpus)

## Rendering conventions

- Equations are KaTeX (`$...$`); raw MathML kept in `equations[]`.
- Chemical formulas use `<sub>`/`<sup>` HTML tags.
- Examiner commentary renders as blockquotes (`> ...`) in `mark-schemes.md`.
- The highlighted final answer renders as `**Final answer:** ...`.
- Bold lines in `mark-schemes.md` are SME's creditable marking statements
  (their `examMark` text-mark); authoritative per-part marks live in
  `part.marks`.
- Images reference `assets/…` relatively.

## Totals

- topics: {totals['topics']} · questions: {totals['questions']} · parts: {totals['parts']}
- marks: {totals['marks']} · assets: {totals['assets']} · equations (KaTeX): {totals['equations']}

## Regeneration

    scripts/sme_examq_scrape.py --out SME-ExamQuestion

(public pages only; no credentials needed; idempotent per topic)
"""
    (out_root / "README.md").write_text(txt, encoding="utf-8")


if __name__ == "__main__":
    main()
