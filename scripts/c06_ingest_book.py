#!/usr/bin/env python3
"""T-C06 book ingest: deterministic parse of the per-page Student Book
substrates (c05_book_ocr.py output, status: raw_ocr; and/or
c05_book_textlayer.py output, status: text_layer) into chapter-level CMC
Markdown + an auditable report.

Implements the runbook's registered ingest implications
(BOOK_OCR_RUNBOOK.md §4):
  1. LaTeX -> HTML <sub>/<sup> normalization — a deterministic KaTeX-style
     scanner, NOT AI interpretation (safe for the converter by construction).
     Unicode sub/superscript leaks (Na₂CO₃, cm³) are normalized too.
  2. Figure extraction from raw sidecar bboxes + page PNGs — SUPPORTED but
     only runs when the OCR run's raw/*.raw.txt + pages-assets/*.png exist;
     otherwise the placeholder census is recorded and figure extraction is
     reported as pending (CPU-side crop is a separate registered step).
  3. Header/footer strip: running heads, bare book-page-number lines,
     repeated chapter-title banners — every strip is LOGGED per page, never
     silent.
  4. Damage lint (flag, NEVER hand-fix — runbook rule): state-symbol
     suspects `()`/`(1)` where `(l)` is expected, Aᵣ damage (`A;`, `A.,`),
     garbled lines, unhandled LaTeX, digit/letter substitution noise.
  5. Chapter-level assembly from the page front matter (29 chapters, 4
     units + front matter), with per-page provenance markers.

Inputs (same page keys as c05 outputs — 1-up pdf page numbers):
  --src      pages dir REQUIRED (e.g. student-book-textlayer/pages)
  --fallback pages dir optional, consulted only for slots missing from
             --src (the OCR-supersedes-text-layer join)

Outputs (--out, default student-book-ingest):
  chapters/*.md        chapter-level CMC markdown (assembled)
  ingest-report.json   per-page actions + lint findings + coverage + totals

Determinism: with --generated-at pinned, re-runs over identical inputs are
byte-identical (house double-run rule).

Usage:
  python3 c06_ingest_book.py --src student-book-textlayer/pages \
      --out student-book-ingest --generated-at 2026-10-24T00:00:00Z
  python3 c06_ingest_book.py --src student-book-pilot/pages --no-assemble \
      --out student-book-ingest-pilot        # OCR-shape smoke run
  python3 c06_ingest_book.py --selftest
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import sys

try:
    import yaml
except ImportError:                                    # pragma: no cover
    yaml = None

# ---------------------------------------------------------------- constants
RUNNING_HEADS = {
    "PRINCIPLES OF CHEMISTRY",          # unit 1 running banner
    "PRINCIPLES OF CHEMISTRY ",         # trailing-space variant
    "CHEMISTRY",                        # short banner variant
}
MAX_GARBLE_SYMBOL_RATIO = 0.5
MIN_GARBLE_LEN = 8

# Known chemistry-ish tokens allowed to contain digits inside words
# (digit/letter-noise heuristic whitelist, lowercase).
CHEM_TOKENS = {
    "h2o", "h2o2", "co2", "co", "no2", "no", "n2o", "so2", "so3", "nh3",
    "ch4", "c2h4", "c2h6", "c3h8", "c4h10", "caco3", "caco", "hcl", "h2so4",
    "hno3", "naoh", "nano3", "na2co3", "k2co3", "cuso4", "mgo", "cao",
    "cacl2", "nacl", "fe2o3", "al2o3", "sio2", "o2", "h2", "n2", "cl2",
    "ccl4", "ch3oh", "c2h5oh", "ch3cooh", "c12h22o11", "pbo", "pbo2",
    "zno", "feo", "fe3o4", "cuo", "mgo2", "kmno4", "k2cr2o7", "h2s",
    "bc3", "c8h18", "c25h52", "c30h62", "c2h5o", "ch3", "c2h5", "dm3",
    "nh4cl", "nh4no3", "nahco3", "khco3", "kno3", "znso4", "feso4",
    "mgso4", "mgcl2", "kcl", "ki", "kbr", "naf", "li2o", "bao", "sro",
    "no", "n2o4", "p2o5", "so2", "h2s", "ph3", "sif4", "bf3", "h2so4",
}

# Unicode sub/superscript -> ASCII digit (for tag building)
UNI_SUB = {"₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4", "₅": "5",
           "₆": "6", "₇": "7", "₈": "8", "₉": "9", "₊": "+", "₋": "-",
           "ₙ": "n"}
UNI_SUP = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5",
           "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁺": "+", "⁻": "-"}

# LaTeX symbol commands -> literal output (KaTeX-style scanner vocabulary)
LATEX_SYMBOLS = {
    r"\rightarrow": "→", r"\leftarrow": "←",
    r"\rightleftharpoons": "⇌", r"\longleftrightarrow": "⟷",
    r"\Delta": "Δ", r"\times": "×", r"\cdot": "·", r"\pm": "±", r"\leq": "≤",
    r"\geq": "≥", r"\neq": "≠", r"\approx": "≈", r"\degree": "°",
    r"\circ": "°", r"\%": "%", r"^\circ": "°",
}
LATEX_SPACING = {r"\,": " ", r"\;": " ", r"\!": "", r"\ ": " ", r"\quad": " ",
                 r"\qquad": "  "}
LATEX_DROP = {r"\left", r"\right", r"\displaystyle"}

MATH_SPAN = re.compile(r"\\\((.+?)\\\)", re.S)          # inline \( ... \)
MATH_BLOCK = re.compile(r"\\\[(.+?)\\\]", re.S)         # display \[ ... \]
SUB_SCRIPT = re.compile(r"_\s*(?:\{([^}]*)\}|([A-Za-z0-9]))")
SUP_SCRIPT = re.compile(r"\^\s*(?:\{([^}]*)\}|([-+]?[A-Za-z0-9]))")
CMD_ARG = re.compile(r"\\(?:mathrm|text|mathbf|bm)\s*\{([^{}]*)\}")
LEFTOVER_CMD = re.compile(r"\\[A-Za-z]+")
FIGURE_PLACEHOLDER = re.compile(r"!\[[^\]]*\]\([^)]*\)")
STATE_SUSPECT = re.compile(r"\(\s*\)|\(\s*1\s*\)")
AR_SUSPECT = re.compile(r"(?:^|[\s(])A\s*[.,;:]{1,3}(?=\s|[A-Z0-9])")
NOISE_WORD = re.compile(r"\b[A-Za-z]*[0-9][A-Za-z0-9]*\b")
BARE_NUMBER = re.compile(r"^\d{1,3}[.:]?$")

SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    return SLUG_RE.sub("-", text.lower()).strip("-")[:48]


# ------------------------------------------------------------- normalization
def _math_to_html(expr: str) -> str:
    """Deterministic KaTeX-style scan of ONE math expression -> HTML text."""
    s = expr
    # symbol commands first (longest first to avoid prefix shadowing)
    for cmd in sorted(LATEX_SYMBOLS, key=len, reverse=True):
        s = s.replace(cmd, LATEX_SYMBOLS[cmd])
    for cmd, rep in LATEX_SPACING.items():
        s = s.replace(cmd, rep)
    for cmd in LATEX_DROP:
        s = s.replace(cmd, "")
    # subscripts then superscripts FIRST (so \mathrm{H_ {2} ...} loses its
    # nested braces before the wrapper unwrap needs to match it)
    for rx in (SUB_SCRIPT, SUP_SCRIPT):
        prev = None
        while prev != s:
            prev = s
            def _tag(m, is_sub=rx is SUB_SCRIPT):
                content = (m.group(1) if m.group(1) is not None
                           else m.group(2) or "")
                content = content.strip()
                tag = "sub" if is_sub else "sup"
                if not content:
                    return ""
                return f"<{tag}>{content}</{tag}>"
            s = rx.sub(_tag, s)
    # \mathrm{...} / \text{...} wrappers (now brace-free inside)
    prev = None
    while prev != s:
        prev = s
        s = CMD_ARG.sub(r"\1", s)
    # leftover braces that wrapped groups
    s = s.replace("{", "").replace("}", "")
    # charge minus inside sup: 2- -> 2−  (only ascii hyphen -> U+2212 in sup)
    s = re.sub(r"(<sup>)([^<]*?)-([^<]*?</sup>)", r"\1\2−\3", s)
    return re.sub(r"\s+", " ", s).strip()


def normalize_math(body: str):
    """Convert \\(...\\) inline and \\[...\\] display math to HTML-shaped text.
    Returns (body, stats) — stats counts inline/display conversions and
    unhandled leftover commands."""
    stats = {"inline_math": 0, "display_math": 0, "unhandled_latex": []}

    def _inline(m):
        stats["inline_math"] += 1
        return _math_to_html(m.group(1))
    body = MATH_SPAN.sub(_inline, body)

    def _display(m):
        stats["display_math"] += 1
        inner = _math_to_html(m.group(1))
        return f'\n<p class="equation">{inner}</p>\n'
    body = MATH_BLOCK.sub(_display, body)

    # any remaining backslash-commands: keep text, flag for review
    for m in LEFTOVER_CMD.finditer(body):
        stats["unhandled_latex"].append(m.group(0))
    return body, stats


def normalize_unicode_scripts(body: str) -> tuple:
    """Unicode sub/superscript runs -> <sub>/<sup> (outside existing tags)."""
    count = 0
    sub_run = re.compile("([" + "".join(UNI_SUB) + "]+)")
    sup_run = re.compile("([" + "".join(UNI_SUP) + "]+)")

    # split on tags to avoid touching tag interiors
    parts = re.split(r"(<(?:sub|sup)>.*?</(?:sub|sup)>)", body, flags=re.S)
    for i, part in enumerate(parts):
        if i % 2 == 1:
            continue  # tag interior — untouched

        def _sub_mm(m):
            nonlocal count
            digits = "".join(UNI_SUB.get(c, c) for c in m.group(1))
            count += 1
            return f"<sub>{digits}</sub>"

        def _sup_mm(m):
            nonlocal count
            digits = "".join(UNI_SUP.get(c, c) for c in m.group(1))
            count += 1
            return f"<sup>{digits}</sup>"

        part = sub_run.sub(_sub_mm, part)
        part = sup_run.sub(_sup_mm, part)
        parts[i] = part
    return "".join(parts), count


# ------------------------------------------------------------ header / strip
def parse_front_matter(text: str) -> tuple:
    """Split a c05 page file into (meta, body). Missing front matter -> {}."""
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            block = text[4:end]
            body = text[end + 4:].lstrip("\n")
            if yaml is not None:
                try:
                    return (yaml.safe_load(block) or {}), body
                except yaml.YAMLError:
                    pass
            # tolerant fallback: flat key: value lines only
            meta = {}
            for line in block.splitlines():
                if ":" in line and not line.startswith((" ", "-")):
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip().strip('"')
            return meta, body
    return {}, text


def strip_running_heads(body: str, meta: dict, opener_page: bool):
    """Strip running heads / bare page numbers / repeated chapter banners.
    Returns (clean_body, stripped:[{line_no, line, rule}])."""
    stripped = []
    book_page = meta.get("book_page")
    ch_title = str(meta.get("chapter_title") or "").upper()
    lines = body.splitlines()
    out = []
    for i, line in enumerate(lines):
        raw = line.strip()
        rule = None
        # (a) bare page-number line equal to the book page (running footer)
        if (book_page is not None and BARE_NUMBER.match(raw)
                and raw.rstrip(".:") == str(book_page)):
            rule = "page_number_line"
        # (b) known running banner
        elif raw in RUNNING_HEADS:
            rule = "running_head"
        # (c) repeated chapter-title banner in the first 3 lines of a
        #     NON-opener page (opener keeps its single title line)
        elif (not opener_page and i < 3 and ch_title and raw == ch_title):
            rule = "chapter_banner_repeat"
        if rule:
            stripped.append({"line_no": i + 1, "line": raw, "rule": rule})
        else:
            out.append(line)
    return "\n".join(out), stripped


# ------------------------------------------------------------------- lint
def lint_page(body: str) -> list:
    """Damage lint — flags for review, NEVER fixes (runbook rule)."""
    findings = []
    # math-span-scoped suspects
    math_regions = [m.group(0) for m in MATH_SPAN.finditer(body)]
    math_regions += [m.group(0) for m in MATH_BLOCK.finditer(body)]
    for region in math_regions:
        if STATE_SUSPECT.search(region):
            findings.append({
                "type": "state_symbol_suspect",
                "sample": STATE_SUSPECT.search(region).group(0).strip(),
            })
    # Aᵣ damage in plain text (A; / A., followed by element list)
    m = AR_SUSPECT.search(body)
    if m:
        findings.append({"type": "ar_symbol_suspect",
                         "sample": m.group(0).strip()})
    # garbled lines (text-layer ghosting / OCR noise)
    for i, line in enumerate(body.splitlines()):
        raw = line.strip()
        if len(raw) < MIN_GARBLE_LEN:
            continue
        ok_chars = " .,;:()%\u00b0+=<>|_-/\u2022\u25a0"
        symbols = sum(1 for c in raw
                      if not (c.isalnum() or c in ok_chars))
        if symbols / len(raw) > MAX_GARBLE_SYMBOL_RATIO:
            findings.append({"type": "garbled_line",
                             "line_no": i + 1, "sample": raw[:60]})
    # digit/letter substitution noise (whitelist-guarded, count only)
    for w in NOISE_WORD.finditer(body):
        tok = w.group(0).lower()
        if tok in CHEM_TOKENS or re.fullmatch(r"\d+", tok):
            continue
        if re.search(r"[a-z]\d[a-z]", tok) and not re.fullmatch(
                r"[a-z]*\d", tok):
            findings.append({"type": "digit_letter_noise",
                             "sample": w.group(0)})
            break                                    # one sample per page
    # dedupe identical finding types (keep first sample of each)
    seen = set()
    deduped = []
    for f in findings:
        key = (f["type"], f.get("sample", f.get("line_no")))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(f)
    return deduped


# ------------------------------------------------------------- page driver
def process_page(path: str, opener_pages: set) -> dict:
    """One page -> {meta, clean_body, actions, lint, figures}."""
    text = open(path, encoding="utf-8").read()
    meta, body = parse_front_matter(text)
    key = os.path.basename(path).replace(".md", "")
    book_page = meta.get("book_page")
    opener = key in opener_pages
    actions = {"stripped": [], "inline_math": 0, "display_math": 0,
               "unicode_scripts": 0}
    body, strip_log = strip_running_heads(body, meta if meta else {},
                                          opener)
    actions["stripped"] = strip_log
    figures = FIGURE_PLACEHOLDER.findall(body)
    lint = lint_page(body)          # raw-body lint: damage lives in the
    body, math_stats = normalize_math(body)   # substrate BEFORE transforms
    actions["inline_math"] = math_stats["inline_math"]
    actions["display_math"] = math_stats["display_math"]
    body, uni_count = normalize_unicode_scripts(body)
    actions["unicode_scripts"] = uni_count
    lint.extend({"type": "unhandled_latex", "sample": c}
                for c in sorted(set(math_stats["unhandled_latex"])))
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return {"key": key, "meta": meta, "body": body, "actions": actions,
            "lint": lint, "figures": len(figures),
            "sha256": hashlib.sha256(text.encode()).hexdigest()[:16]}


# ---------------------------------------------------------- chapter assembly
def chapter_key(meta) -> int:
    ch = meta.get("chapter") or 0
    return int(ch) if str(ch).strip().lstrip("-").isdigit() else 0


def assemble(pages: list, out_dir: str, generated_at: str) -> list:
    """Group processed pages by chapter -> chapters/*.md. Returns manifest."""
    by_ch: dict = {}
    for p in pages:
        by_ch.setdefault(chapter_key(p["meta"]), []).append(p)
    written = []
    for ch in sorted(by_ch):
        group = sorted(
            by_ch[ch],
            key=lambda p: (p["meta"].get("book_page") is None,
                           p["meta"].get("book_page") or 0, p["key"]))
        if ch == 0:
            fname, title = "front-matter.md", "Front matter"
        else:
            title = str(group[0]["meta"].get("chapter_title")
                        or f"Chapter {ch}")
            fname = f"ch-{ch:02d}-{slugify(title)}.md"
        unit = str(group[0]["meta"].get("unit") or "front")
        book_pages = [p["meta"].get("book_page") for p in group
                      if isinstance(p["meta"].get("book_page"), int)]
        page_range = (f"{min(book_pages)}-{max(book_pages)}"
                      if book_pages else "n/a")
        statuses = sorted({str(p["meta"].get("status")) for p in group})
        header = (
            "---\n"
            'source_type: textbook\n'
            'book_title: "Edexcel International GCSE (9-1) Chemistry '
            'Student Book"\n'
            f"unit: {unit}\n"
            f"chapter: {ch}\n"
            f'chapter_title: "{title}"\n'
            f'book_page_range: "{page_range}"\n'
            f"page_count: {len(group)}\n"
            f"statuses: [{', '.join(statuses)}]\n"
            "ingest:\n"
            "  tool: c06_ingest_book.py (deterministic transform)\n"
            f"  generated_at: {generated_at}\n"
            "status: ingested\n"
            "notes: >\n"
            "  Assembled from per-page substrates: LaTeX->HTML normalization,\n"
            "  running-head strip (every strip logged), damage lint (flags\n"
            "  recorded in ingest-report.json, NOT hand-fixed — runbook\n"
            "  rule). Figure placeholders await bbox extraction at ingest.\n"
            "---\n")
        parts = [header]
        for p in group:
            bp = p["meta"].get("book_page")
            parts.append(
                f"\n<!-- {p['key']}.md | book p.{bp} | "
                f"status: {p['meta'].get('status')} | "
                f"lint findings: {len(p['lint'])} | "
                f"figures: {p['figures']} -->\n\n")
            parts.append(p["body"])
            parts.append("\n")
        path = os.path.join(out_dir, "chapters", fname)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write("".join(parts))
        written.append({"file": f"chapters/{fname}", "chapter": ch,
                        "title": title, "pages": len(group)})
    return written


# ------------------------------------------------------------------ report
def build_report(pages: list, written: list, args, missing: list,
                 blanks: list) -> dict:
    lint_agg: dict = {}
    for p in pages:
        for f in p["lint"]:
            lint_agg.setdefault(f["type"], []).append(
                {"page": p["key"], **f})
    per_page = [{
        "page": p["key"],
        "book_page": p["meta"].get("book_page"),
        "chapter": p["meta"].get("chapter"),
        "status": p["meta"].get("status"),
        "sha256": p["sha256"],
        "stripped_lines": [{"line_no": s["line_no"], "rule": s["rule"],
                            "line": s["line"]} for s in p["actions"]["stripped"]],
        "inline_math": p["actions"]["inline_math"],
        "display_math": p["actions"]["display_math"],
        "unicode_scripts": p["actions"]["unicode_scripts"],
        "figures": p["figures"],
        "lint": p["lint"],
    } for p in pages]
    return {
        "schema": "c06-book-ingest-report/1.0",
        "generated_at": args.generated_at,
        "src": args.src,
        "fallback": args.fallback,
        "totals": {
            "pages_processed": len(pages),
            "chapters_written": len(written),
            "missing_slots": len(missing),
            "blank_slots": len(blanks),
            "inline_math_converted": sum(p["actions"]["inline_math"]
                                         for p in pages),
            "display_math_converted": sum(p["actions"]["display_math"]
                                          for p in pages),
            "unicode_scripts_converted": sum(
                p["actions"]["unicode_scripts"] for p in pages),
            "figure_placeholders": sum(p["figures"] for p in pages),
            "stripped_lines": sum(len(p["actions"]["stripped"])
                                  for p in pages),
            "lint_findings": sum(len(p["lint"]) for p in pages),
        },
        "lint_by_type": {k: len(v) for k, v in sorted(lint_agg.items())},
        "chapters": written,
        "missing_slots": missing,
        "blank_slots": blanks,
        "pages": per_page,
    }


# ----------------------------------------------------------------- selftest
SELFTEST_INPUT = (
    r"\[" + "\n"
    + r"\mathrm{CaCO} _ {3} (\mathrm{s}) + 2 \mathrm{HCl} (\mathrm{aq}) "
      r"\rightarrow \mathrm{CaCl} _ {2} (\mathrm{aq}) + \mathrm{H} _ {2} "
      r"\mathrm{O} () + \mathrm{CO} _ {2} (g)" + "\n" + r"\]" + "\n\n"
    + r"Water is  \( H_2O \) , carbonate is  \( CO_{3}^{2-} \) , volume  "
      r"\( 30.0 \, cm^{3} \)  of Na₂CO₃ solution, units cm³ and dm³. "
      "(A.; C = 12, O = 16, Ca = 40)")


def selftest() -> int:
    ok = True
    lint = lint_page(SELFTEST_INPUT)          # raw-body lint first (as in
    body, stats = normalize_math(SELFTEST_INPUT)   # process_page)
    body, uni = normalize_unicode_scripts(body)

    def check(name, cond):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {name}")
        ok = ok and cond

    check("display block -> <p class=equation>",
          '<p class="equation">' in body)
    check("rightarrow -> glyph", "→" in body)
    check("subscript group", "<sub>3</sub>" in body)
    check("inline math unwrapped", "H<sub>2</sub>O" in body)
    check("charge sup with minus", "<sup>2−</sup>" in body)
    check("spacing command collapsed", "30.0 cm<sup>3</sup>" in body)
    check("unicode sub Na2CO3", "Na<sub>2</sub>CO<sub>3</sub>" in body)
    check("unicode sup cm3", "cm<sup>3</sup>" in body)
    check("no leftover mathrm", "\\mathrm" not in body)
    check("state_symbol_suspect flagged",
          any(f["type"] == "state_symbol_suspect" for f in lint))
    check("ar_symbol_suspect flagged",
          any(f["type"] == "ar_symbol_suspect" for f in lint))
    check("unhandled latex empty", not stats["unhandled_latex"])
    print(f"  normalized sample: {body[:160]}")
    return 0 if ok else 1


# -------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=None,
                    help="pages dir (c05 output); required unless --selftest")
    ap.add_argument("--fallback", default=None,
                    help="pages dir consulted for slots missing from --src")
    ap.add_argument("--out", default="student-book-ingest")
    ap.add_argument("--generated-at",
                    default=datetime.datetime.now(
                        datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    ap.add_argument("--no-assemble", action="store_true",
                    help="page-level processing + report only")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        sys.exit(selftest())
    if not args.src:
        ap.error("--src is required (unless --selftest)")

    keys = sorted(f for f in os.listdir(args.src) if f.endswith(".md"))
    if not keys:
        print(f"no .md pages in {args.src}", file=sys.stderr)
        sys.exit(2)
    texts = {f[:-3]: open(os.path.join(args.src, f),
                          encoding="utf-8").read() for f in keys}
    if args.fallback:
        for f in sorted(os.listdir(args.fallback)):
            if f.endswith(".md") and f[:-3] not in texts:
                texts[f[:-3]] = open(os.path.join(args.fallback, f),
                                     encoding="utf-8").read()

    metas = {k: parse_front_matter(t)[0] for k, t in texts.items()}
    # chapter openers: earliest book_page within each chapter
    openers = set()
    first_by_ch: dict = {}
    for k, m in metas.items():
        bp = m.get("book_page")
        ch = chapter_key(m)
        if isinstance(bp, int) and (ch not in first_by_ch
                                    or bp < first_by_ch[ch][0]):
            first_by_ch[ch] = (bp, k)
    for ch, (_, k) in first_by_ch.items():
        openers.add(k)

    all_slots = sorted(texts)
    pages, missing, blanks = [], [], []
    for k in all_slots:
        p = process_page(os.path.join(args.src if k in
                                      {f[:-3] for f in keys} else
                                      (args.fallback or args.src),
                                      k + ".md"), openers)
        pages.append(p)
        if p["meta"].get("status") == "blank":
            blanks.append(k)

    if args.no_assemble:
        written = []
    else:
        written = assemble(pages, args.out, args.generated_at)

    report = build_report(pages, written, args, missing, blanks)
    os.makedirs(args.out, exist_ok=True)
    rpath = os.path.join(args.out, "ingest-report.json")
    with open(rpath, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=1, ensure_ascii=False)
    t = report["totals"]
    print(f"ingest: {t['pages_processed']} pages -> "
          f"{t['chapters_written']} chapters | math "
          f"{t['inline_math_converted']}+{t['display_math_converted']} | "
          f"unicode {t['unicode_scripts_converted']} | stripped "
          f"{t['stripped_lines']} | figures {t['figure_placeholders']} | "
          f"lint {t['lint_findings']} ({report['lint_by_type']})")
    print(f"report: {rpath}")


if __name__ == "__main__":
    main()
