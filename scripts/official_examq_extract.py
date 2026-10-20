#!/usr/bin/env python3
"""
official_examq_extract.py — ADR-037 prototype converter
========================================================
Converts ONE official past paper (QP+MS) into the serving schema
`syllabai.official-paper-questions/0.1` using VERBATIM extraction
(no generation), then runs fail-closed gates G0–G6 plus negative controls.

The one-sentence rule (ADR-037 §2): the converter extracts; it never authors.
Every character of problem_md / solution_md / choices[].text_md is copied
from the source layer; the only generated fields are labels (command_word,
spec seeds) and links (answer linkage, asset stubs) — and labels are
registry-validated or flagged for human review.

Run:  python3 official_examq_extract.py --series 2020-11   (baseline; also 2019-06, 2020-01, 2021-06, 2022-06, 2024-06)
"""
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import fitz  # PyMuPDF — page-anchored provenance
import yaml

# --- pipeline roots (LEDGER F15: derived from this file's location so the kit
# --- runs from any clean checkout; env vars override for exotic staging) ---
SCRIPTS_DIR = Path(__file__).resolve().parent            # .../syllabai-resources/scripts
RES_DIR     = SCRIPTS_DIR.parent                         # the checkout root
UPLOAD = Path(os.environ.get("EXAMQ_UPLOAD_DIR", "/home/z/my-project/upload"))
OUTROOT = RES_DIR / "Official-ExamQuestion" / "igcse-chemistry-19"   # ALWAYS inside the checkout
# spec-point registry: canonical copy lives in this repo (SME-ExamQuestion/...);
# staged spc-resolution.json is a legacy fallback for pre-F15 staging areas.
_SPEC_REPO = RES_DIR / "SME-ExamQuestion" / "igcse-chemistry-19" / "spec_point_resolution.json"
if os.environ.get("EXAMQ_SPEC_RESOLUTION"):
    SPEC_RESOLUTION = Path(os.environ["EXAMQ_SPEC_RESOLUTION"])
elif _SPEC_REPO.exists():
    SPEC_RESOLUTION = _SPEC_REPO
else:
    SPEC_RESOLUTION = UPLOAD / "spc-resolution.json"

SCHEMA = "syllabai.official-paper-questions/0.1"
CONVERTER_VERSION = "0.4"   # see Official-ExamQuestion/CHANGELOG.md + LEDGER.md
PAPER_TOTAL = 110          # registry expectation for 4CH1/1C — constant across series
# printed question counts verified per series (footers vary 9..15 across the 4CH1 era);
# counts cross-checked against per-question footer marks summing to 110
EXPECT_QUESTIONS = {"2020-11": 10, "2020-01": 10, "2021-06": 10, "2022-06": 10, "2024-06": 10,
                    "2019-06": 15, "2021-01": 11, "2021-11": 11, "2022-01": 11, "2023-01": 12,
                    "2023-06": 10, "2023-11": 10, "2024-11": 11, "2025-06": 10, "2025-11": 10,
                    "2026-06": 9}
# per-series demo seeds (labels only; registry-validated in G6). Other series -> pending-llm.
SEEDS = {
    "2020-11": {
        "1(b)(i)": "4CH1-1.20", "4(c)(ii)": "4CH1-1.25",
        "9(c)(ii)": "4CH1-1.28", "10(b)": "4CH1-1.31",
        "8(c)(ii)": "4CH1-3.9", "7": "4CH1-3.15C",   # 7* deliberately incl. registry-gap demo
    },
}


def paths_for(series: str) -> dict:
    return {
        "qp_pdf": UPLOAD / f"official-4CH1-1C-{series}-qp.pdf",
        "ms_pdf": UPLOAD / f"official-4CH1-1C-{series}-ms.pdf",
        "qp_txt": UPLOAD / f"official-{series}-qp.txt",
        "ms_txt": UPLOAD / f"official-{series}-ms.txt",
        "manifest": UPLOAD / f"manifest-{series}-1C.yaml",
        "out": OUTROOT / series / "4CH1-1C",
    }

# ---------------------------------------------------------------- utilities
def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


DOTRUN_RE = re.compile(r"(?:\s*\.\s*){4,}")   # printed answer lines "= . . . . . g"


def strip_dotrun(s: str) -> str:
    return DOTRUN_RE.sub(" ", s).strip()


def ngrams(text: str, n: int = 5):
    toks = norm(text).split()
    return set(tuple(toks[i:i + n]) for i in range(len(toks) - n + 1))


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------- stage 1: QP cleaning
FURNITURE_SUBS = [
    (re.compile(r"\*P\d{5}[A-Z]\w*\*"), " "),       # page identity marker (P62045A*, P58561A*, ...)
    (re.compile(r"\bTurn over\b"), " "),
    (re.compile(r"DO NOT WRITE IN THIS (?:AREA|MARGIN|SPACE)\s*"), " "),   # often 3x on one line
]
FURNITURE_LINE = [
    re.compile(r"^\s*PMT\s*$"),                     # archive watermark
    re.compile(r"^\s*BLANK PAGE\s*$"),
    re.compile(r"^\s*DO NOT WRITE IN THIS (AREA|MARGIN|SPACE)\s*$"),
    re.compile(r"^\s*\d{1,2}\s*$"),                 # bare page number (1..36)
    re.compile(r"^[\s.]*\.[\s.]*$"),                # dotted answer lines
    re.compile(r"^\s*$"),
]


def clean_lines(raw: str):
    out = []
    for ln in raw.splitlines():
        for rx, rep in FURNITURE_SUBS:
            ln = rx.sub(rep, ln)
        if any(rx.match(ln) for rx in FURNITURE_LINE):
            continue
        out.append(ln.rstrip())
    return out


# ---------------------------------------------------------------- stage 2: segmentation
FOOTER_RE = re.compile(r"\(Total for Question (\d{1,2}) = (\d{1,2}) marks\)")
QSTART_RE = re.compile(r"^\s*(\d{1,2})\s+([A-Za-z(].*)$")   # remainder must start alpha/'(' (indent-tolerant)
L1_RE = re.compile(r"^\s*\(([a-h])\s*\)\s*(.*)$")
L2_RE = re.compile(r"^\s*\((i{1,3}|iv|v|vi{1,3})\s*\)\s+(.*)$")   # romans i..viii
L2_INLINE_RE = re.compile(r"^\((i{1,3}|iv|v|vi{1,3})\s*\)\s+(.*)$")
MARK_RE = re.compile(r"^\s*\((\d{1,2})\)\s*$")
OPT_RE = re.compile(r"^\s*([A-E])\s+(\S.*?)\s*$")
ROMAN = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii"]

COMMAND_WORDS = ["identify", "explain", "state", "describe", "calculate", "draw",
                 "write", "give", "suggest", "name", "complete", "plot", "show",
                 "use", "define", "deduce", "place", "what", "which", "how", "why",
                 "complete the", "add", "order"]


def strip_leading_command(text):
    m = re.match(r"^(identify|explain|state|describe|calculate|draw|write|give|"
                 r"suggest|name|complete|plot|show|use|define|deduce|place)\b",
                 norm(text))
    return m.group(1) if m else None


def parse_mcq_block(lines):
    """Return (choices, consumed_idx_set) for a consecutive A,B,C,... option run."""
    choices, consumed = [], set()
    expect = 0  # index into A,B,C,D,E
    for i, ln in enumerate(lines):
        m = OPT_RE.match(ln)
        if m and ord(m.group(1)) - 65 == expect:
            choices.append({"label": m.group(1), "text_md": m.group(2).strip()})
            consumed.add(i)
            expect += 1
        elif choices:
            break
    return (choices if len(choices) >= 3 else []), consumed


def segment_question(qnum, region_lines):
    """Split a question region into stem + parts (two levels) + option lists."""
    q = {"number": qnum, "stem_lines": [], "groups": {}}
    order = []
    cur_group, cur_part = None, None

    # question-start line
    start_idx = 0
    m = QSTART_RE.match(region_lines[0]) if region_lines else None
    inline_rest = None
    if m and int(m.group(1)) == qnum:
        inline_rest = m.group(2).strip()
        start_idx = 1
    else:
        # line 0 is NOT the question-start (damaged/trimmed region): let the
        # loop classify it — it may itself be a part marker (e.g. a question
        # whose stem page was rasterized, leaving only "(c) ..." fragments)
        start_idx = 0

    # inline "(a) ..." or "(a) (i) ..." on the question-number line
    if inline_rest:
        g = L1_RE.match(inline_rest)
        if g:
            cur_group = g.group(1)
            q["groups"][cur_group] = {"stem_lines": [], "parts": {}, "order": []}
            order.append(cur_group)
            rest = g.group(2).strip()
            r2 = L2_INLINE_RE.match(rest)
            if r2:
                cur_part = r2.group(1)
                q["groups"][cur_group]["parts"][cur_part] = {"lines": [r2.group(2)]}
                q["groups"][cur_group]["order"].append(cur_part)
            elif rest:
                q["groups"][cur_group]["stem_lines"].append(rest)
        else:
            q["stem_lines"].append(inline_rest)

    for ln in region_lines[start_idx:]:
        g = L1_RE.match(ln)
        r = L2_RE.match(ln)
        if g and not r:
            cur_group, cur_part = g.group(1), None
            q["groups"].setdefault(cur_group, {"stem_lines": [], "parts": {}, "order": []})
            if cur_group not in order:
                order.append(cur_group)
            rest = g.group(2).strip()
            r2 = L2_INLINE_RE.match(rest)
            if r2:
                cur_part = r2.group(1)
                q["groups"][cur_group]["parts"][cur_part] = {"lines": [r2.group(2)]}
                q["groups"][cur_group]["order"].append(cur_part)
            elif rest:
                q["groups"][cur_group]["stem_lines"].append(rest)
        elif r:
            if cur_group is None:  # roman without letter — attach to virtual group
                cur_group = "_"
                q["groups"].setdefault(cur_group, {"stem_lines": [], "parts": {}, "order": []})
                order.append(cur_group)
            cur_part = r.group(1)
            q["groups"][cur_group]["parts"][cur_part] = {"lines": [r.group(2)]}
            q["groups"][cur_group]["order"].append(cur_part)
        else:
            if cur_part is not None:
                q["groups"][cur_group]["parts"][cur_part]["lines"].append(ln)
            elif cur_group is not None:
                q["groups"][cur_group]["stem_lines"].append(ln)
            else:
                q["stem_lines"].append(ln)
    q["group_order"] = order
    return q


def finalize_part(lines):
    """Extract marks, MCQ choices, clean problem text from a part's raw lines."""
    lines = [l for l in lines if l.strip()]
    marks = None
    kept = []
    for ln in lines:
        mm = MARK_RE.match(ln)
        if mm and marks is None:
            marks = int(mm.group(1))
        else:
            kept.append(ln)
    source_norm = norm(" ".join(kept))   # verbatim ground truth BEFORE choice strip
    if marks is None:  # fallback: trailing "(n)"
        for ln in reversed(kept):
            tm = re.search(r"\((\d{1,2})\)\s*$", ln)
            if tm and not ln.strip().startswith(("A ", "B ", "C ", "D ")):
                marks = int(tm.group(1))
                kept[kept.index(ln)] = re.sub(r"\((\d{1,2})\)\s*$", "", ln).rstrip()
                break

    choices, consumed = parse_mcq_block(kept)
    if choices:
        kept = [ln for i, ln in enumerate(kept) if i not in consumed]
    source_norm = norm(strip_dotrun(" ".join(kept)))   # final ground truth (marks + options removed)

    text = strip_dotrun(re.sub(r"\s{2,}", " ", " ".join(kept))).strip()
    return {"marks": marks, "choices": choices, "problem_md": text, "source_norm": source_norm}


# ---------------------------------------------------------------- stage 3: MS linkage
MS_ROW_RE = re.compile(
    r"^ {0,20}(?:(\d{1,2})\s+)?(?:\(([a-h])\s*\)\s*)?(?:\((i{1,3}|iv|v|vi{1,3})\s*\)\s*)?(\S.*)$")
MS_MARKER_ONLY_RE = re.compile(
    r"^\s*(?:(\d{1,2})\s+)?(?:\(([a-h])\s*\))?\s*(?:\((i{1,3}|iv|v|vi{1,3})\s*\))?\s*$")
# some series (2019-06) print sub-letters bare without parentheses: "    b      they have..."
MS_BARE_LETTER_RE = re.compile(
    r"^ {0,20}(?:(\d{1,2})\s+)?([a-h])(?=\s{2,})\s*(.*)$")


def parse_ms(ms_lines):
    """Link MS rows positionally: rows carry qnum / letter / roman in any
    combination; absent components inherit from the previous row. Marker-only
    rows (e.g. a bare '(ii)' line) open an entry whose content starts on the
    next line. Returns key -> list of raw lines (per-line structure matters
    for MCQ keying: answer rows vs 'X is incorrect' note rows)."""
    entries = {}
    cur_q, cur_letter = None, None
    cur = None
    TOTAL_RE = re.compile(r"^\s*Total\s+\d+\s*$")
    for ln in ms_lines:
        if TOTAL_RE.match(ln):
            continue
        mo = MS_MARKER_ONLY_RE.match(ln)
        m = MS_ROW_RE.match(ln)
        mb = MS_BARE_LETTER_RE.match(ln)
        if mo and any(mo.groups()[:3]):
            qn, letter, roman = mo.group(1), mo.group(2), mo.group(3)
            if qn:
                cur_q = int(qn)
            if letter:
                cur_letter = letter
            cur = (cur_q, cur_letter, roman if roman else None)
            entries.setdefault(cur, [])
        elif mb:
            # bare-letter rows must win over MS_ROW_RE (whose groups are all
            # optional and therefore match almost any line)
            qn, letter, rest = mb.groups()
            if qn:
                cur_q = int(qn)
            cur_letter = letter
            roman = None
            r2 = L2_INLINE_RE.match(rest.strip())
            if r2:
                roman, rest = r2.group(1), r2.group(2)
            cur = (cur_q, cur_letter, roman)
            entries.setdefault(cur, [rest.strip()] if rest.strip() else [])
        elif m:
            qn, letter, roman, rest = m.groups()
            if any([qn, letter, roman]):
                if qn:
                    cur_q = int(qn)
                if letter:
                    cur_letter = letter
                cur = (cur_q, cur_letter, roman if roman else None)
                entries.setdefault(cur, [rest])
            elif cur is not None:
                entries[cur].append(ln)
        elif cur is not None:
            entries[cur].append(ln)
    return entries


# ---------------------------------------------------------------- main
def main():
    import argparse, copy
    ap = argparse.ArgumentParser(description="ADR-037 official-paper question extractor")
    ap.add_argument("--series", default="2020-11",
                    help="paper series folder, e.g. 2020-11 (baseline), 2019-06, 2020-01, 2021-06, 2022-06, 2024-06")
    args = ap.parse_args()
    series = args.series
    P = paths_for(series)
    global QP_PDF, MS_PDF, QP_TXT, MS_TXT, MANIFEST, OUT
    QP_PDF, MS_PDF = P["qp_pdf"], P["ms_pdf"]
    QP_TXT, MS_TXT = P["qp_txt"], P["ms_txt"]
    MANIFEST, OUT = P["manifest"], P["out"]
    expect_q = EXPECT_QUESTIONS.get(series)

    report = {"schema": "syllabai.official-paper-questions.validation/0.1",
              "generated_utc": now_iso(), "series": series, "gates": [],
              "negative_controls": [], "review_queue": []}

    # ---- G0 identity -------------------------------------------------------
    manifest = yaml.safe_load(MANIFEST.read_text())
    qp_sha, ms_sha = sha256(QP_PDF), sha256(MS_PDF)
    mat = {m["type"]: m for m in manifest["materials"]}
    sha_ok = (qp_sha == mat["question-paper"]["sha256"] and
              ms_sha == mat["mark-scheme"]["sha256"])
    paper_id = manifest["paper_id"]
    report["gates"].append({
        "gate": "G0-identity", "status": "PASS" if sha_ok else "FAIL",
        "summary": f"paper_id={paper_id}; series={manifest['series']['normalized']}; "
                   f"printed={manifest['series'].get('printed', 'n/a (manifest schema v2 omits it)')!r}; sha256 qp/ms match manifest: {sha_ok}",
        "details": {"qp_sha256": qp_sha, "ms_sha256": ms_sha,
                    "registry_paper_id": paper_id}})
    if not sha_ok:
        print("G0 FAIL — aborting (fail-closed)"); json.dump(report, sys.stdout, indent=1); return 1

    qp_lines = clean_lines(QP_TXT.read_text(errors="replace"))
    footers = [(i, int(m.group(1)), int(m.group(2)))
               for i, ln in enumerate(qp_lines) if (m := FOOTER_RE.search(ln))]

    # ---- extraction --------------------------------------------------------
    # footer census: printed totals must exist for 1..N; a missing footer (seen in
    # 2019-06 Q7 — absent from the PDF text layer itself) splits the following
    # region into a footer-less question (marks inferred from parts -> REVIEW)
    footer_qnums = {q for _, q, _ in footers}
    max_q = max(footer_qnums)
    missing = [n for n in range(1, max_q + 1) if n not in footer_qnums]

    def emit_question(qnum, printed_total, region):
        seg = segment_question(qnum, [l for l in region if l.strip()])
        stem_md = re.sub(r"\s{2,}", " ", " ".join(seg["stem_lines"])).strip()
        questions_parts = []
        for gletter in seg["group_order"]:
            grp = seg["groups"][gletter]
            grp_stem = strip_dotrun(re.sub(r"\s{2,}", " ", " ".join(grp["stem_lines"])).strip())
            grp_choices, consumed = parse_mcq_block(
                [l for l in grp["stem_lines"]]) if not grp["parts"] else ([], set())
            option_list = [c["text_md"] for c in grp_choices] or None
            if not grp["order"]:
                # letter-group with no roman sub-parts: the group IS a part (e.g. 2(a), 7(d))
                p = finalize_part(grp["stem_lines"])
                questions_parts.append({
                    "part_number": f"{qnum}({gletter})",
                    "group": gletter, "roman": None,
                    "group_stem_md": None, "option_list": None,
                    "marks": p["marks"],
                    "question_type": "multiple_choice" if p["choices"] else "structured",
                    "problem_md": p["problem_md"], "choices": p["choices"],
                    "source_norm": p["source_norm"],
                })
                continue
            for roman in grp["order"]:
                p = finalize_part(grp["parts"][roman]["lines"])
                part_number = f"{qnum}({gletter})({roman})" if gletter != "_" else f"{qnum}({roman})"
                questions_parts.append({
                    "part_number": part_number,
                    "group": gletter, "roman": roman,
                    "group_stem_md": grp_stem or None, "option_list": option_list,
                    "marks": p["marks"], "question_type": "multiple_choice" if p["choices"] else "structured",
                    "problem_md": p["problem_md"], "choices": p["choices"],
                    "source_norm": p["source_norm"],
                })
        doc_questions.append({"question_number": qnum, "printed_total": printed_total,
                              "stem_md": stem_md, "parts": questions_parts,
                              "region_norm": norm(" ".join(region))})

    doc_questions = []
    prev = 0
    for fi, (idx, qnum, qtotal) in enumerate(footers):
        region = qp_lines[prev + 1 if fi else 0:idx]
        prev = idx
        # start lines for this question and for any missing questions whose body
        # lives inside this region (their footer was dropped by the archive PDF)
        pieces = []
        for m in missing:
            ms_ = [i for i, ln in enumerate(region)
                   if QSTART_RE.match(ln) and int(QSTART_RE.match(ln).group(1)) == m]
            if ms_:
                pieces.append((m, ms_[-1], None))
        cur = [i for i, ln in enumerate(region)
               if QSTART_RE.match(ln) and int(QSTART_RE.match(ln).group(1)) == qnum]
        pieces.append((qnum, cur[-1] if cur else 0, qtotal))
        pieces.sort(key=lambda t: t[1])
        for k, (qn, st, pt) in enumerate(pieces):
            end = pieces[k + 1][1] if k + 1 < len(pieces) else len(region)
            emit_question(qn, pt, region[st:end])
    doc_questions.sort(key=lambda q: q["question_number"])

    # ---- MS linkage + MCQ keys ---------------------------------------------
    ms_entries = parse_ms(clean_lines(MS_TXT.read_text(errors="replace")))
    for q in doc_questions:
        for p in q["parts"]:
            key = (q["question_number"], p["group"], p["roman"])
            lines = ms_entries.get(key, [])
            raw = re.sub(r"\s{2,}", " ", " ".join(lines)).strip()
            p["answer_status"] = "linked" if raw else "unmatched"
            p["answer_raw"] = raw
            if p["question_type"] == "multiple_choice" and raw:
                labels = {c["label"] for c in p["choices"]}
                # candidate answer rows: "<Letter> <text>" lines that are NOT
                # "X is incorrect ..." note rows (Edexcel MS layout drifts its
                # marker column one row early in some series, so notes leak in;
                # key only when the entry shows exactly ONE distinct candidate)
                ans, positives, rebut, ansrow = [], [], {}, {}
                for ln in lines:
                    s = re.sub(r"^\s*\d{1,2}\s+(?=[A-E]\b)", "", ln)   # glued marks digit
                    m = re.match(r"^\s*([A-E])\s+\S", s)
                    g = re.match(r"^\s*([A-E])(?=[0-9(])", s)   # glued answer cell: 'B4', 'D(NH4+)'
                    pos = re.search(r"(?<![A-Za-z])([A-E])\s+is\s+(?:the\s+)?correct\b", s)
                    if pos and pos.group(1) in labels:
                        positives.append(pos.group(1))
                    hit = m or g
                    if hit and hit.group(1) in labels:
                        # rebuttal row: an option letter followed by negative text
                        # ('A is incorrect ...', 'B is not the formula ...',
                        #  'C the charges are incorrect', 'B is X incorrect ...')
                        if re.search(r"\bis\s+not\b|\bare\s+not\b|\b(?:is|are)\s+(?:\w+\s+)?incorrect\b", s):
                            rebut[hit.group(1)] = rebut.get(hit.group(1), 0) + 1
                        else:
                            ans.append(hit.group(1))
                            ansrow[hit.group(1)] = ansrow.get(hit.group(1), 0) + 1
                    elif s.strip() in labels:
                        ans.append(s.strip())
                        ansrow[s.strip()] = ansrow.get(s.strip(), 0) + 1
                # a printed '<L> is the correct answer ...' statement is
                # authoritative: key it even if stray note-drift letters leaked in
                lab = (positives[0] if len(set(positives)) == 1 else
                       (ans[0] if len(set(ans)) == 1 else None))
                # elimination keying (F14): entries whose MS prints an explicit
                # rebuttal for every option except the correct one — key the sole
                # un-rebutted option ONLY when corroborated by exactly one answer
                # row; anything else stays unkeyed for human review
                if lab is None:
                    clean = [L for L in sorted(labels) if L not in rebut]
                    if len(clean) == 1 and clean[0] in ansrow and len(ansrow) == 1:
                        lab = clean[0]
                if lab is None and not re.search(r"\bis\s+(?:not\s+(?:the\s+)?)?correct\b|\bis\s+incorrect\b", raw):
                    # letters fallback ONLY on note-free entries (a greedy note-strip
                    # can swallow an adjacent answer row and yield a wrong key)
                    letters = set(re.findall(r"(?<![A-Za-z])([A-D])(?![A-Za-z])", raw))
                    if len(letters) == 1:
                        lab = letters.pop()
                if lab:
                    for c in p["choices"]:
                        c["is_correct"] = (c["label"] == lab)

    # ---- page anchoring + assets -------------------------------------------
    pdf = fitz.open(QP_PDF)
    page_norm = [norm(pg.get_text()) for pg in pdf]
    # source-defect census: rasterized pages carry no text layer (seen in 2019-06:
    # 8 image-only pages; Q7 lost entirely, Q1/Q11/Q12/Q13/Q15 partly)
    IMG_ONLY_CHARS = 40
    image_only_pages = [i + 1 for i, pg in enumerate(pdf) if len(pg.get_text().strip()) < IMG_ONLY_CHARS]
    footer_page = {}
    for i, pg in enumerate(pdf):
        t = pg.get_text()
        for m in FOOTER_RE.finditer(t):
            footer_page.setdefault(int(m.group(1)), i + 1)
    # only content pages matter for defect attribution (covers are routinely rasterized);
    # allow up to 3 pages before the first footer (a question's first page precedes its footer)
    first_q_page = min(footer_page.values()) if footer_page else 1
    content_img_pages = [p for p in image_only_pages if p >= max(3, first_q_page - 3)]
    MENTION_RE = re.compile(r"\b(table|diagram|grid|graph|apparatus|boxes)\b", re.I)
    for q in doc_questions:
        for p in q["parts"]:
            anchor = norm(re.sub(r"^[()a-ziv ]+", "", p["problem_md"]))[:38]
            p["source_page"] = next((i + 1 for i, t in enumerate(page_norm) if anchor in t), None)
            mentions = sorted(set(m.group(1).lower() for m in MENTION_RE.finditer(p["problem_md"])))
            p["assets"] = [{"id": f"asset_{p['part_number'].replace('(', '_').replace(')', '')}_{k}",
                            "kind": "crop-required", "mention": k,
                            "source": "qp.pdf", "page": p["source_page"], "review": True}
                           for k in mentions]

    # ---- spec seeds (labels only; registry-validated) -----------------------
    seeds = SEEDS.get(series, {})
    reg = json.loads(SPEC_RESOLUTION.read_text())["resolved"]
    registry = set()
    for r in reg:
        if r.get("resolved_code"):
            registry.add(r["resolved_code"])
    for q in doc_questions:
        for p in q["parts"]:
            code = seeds.get(p["part_number"])
            if code:
                p["spec_point_codes"] = [code]
                p["tagging"] = "seed-demo"
                if code not in registry:
                    p["tagging"] = "registry-gap-review"
                    report["review_queue"].append({"part": p["part_number"], "reason": f"spec code {code} not in registry (gap or invalid) — human decision"})
            else:
                p["spec_point_codes"] = []
                p["tagging"] = "pending-llm"
    # ---- gates ---------------------------------------------------------------
    def gate(name, ok, summary, details=None):
        report["gates"].append({"gate": name, "status": "PASS" if ok else "FAIL",
                                "summary": summary, "details": details or {}})
        return ok

    # G1 structure: marks invariant (fail-closed; source defects -> REVIEW, parser bugs -> FAIL)
    # attribution: a mismatch/missing question is a SOURCE defect when an image-only
    # page (no text layer) sits inside or immediately before the question's pages.
    footer_gaps = []
    defective = set()
    emitted_qnums = {q["question_number"] for q in doc_questions}
    for m in missing:
        if m in emitted_qnums:
            continue                      # split succeeded; inferred total handled below
        prev_p = max((footer_page[q] for q in footer_page if q < m), default=0)
        next_p = min((footer_page[q] for q in footer_page if q > m), default=10**6)
        lost_pages = [p for p in content_img_pages if prev_p < p < next_p]
        footer_gaps.append({"question": m,
                            "reason": (f"footer absent in source PDF; question not extractable — "
                                       f"image-only page(s) {lost_pages} in archive PDF (content lost at scan)"
                                       if lost_pages else
                                       "footer absent in source PDF and no start line found — needs human split"),
                            "attributed": bool(lost_pages)})
        if lost_pages:
            defective.add(m)

    g1_bad = []
    inferred_totals = {}
    for q in doc_questions:
        ssum = sum(p["marks"] or 0 for p in q["parts"])
        if q["printed_total"] is None:
            inferred_totals[q["question_number"]] = ssum
        elif ssum != q["printed_total"]:
            g1_bad.append({"question": q["question_number"], "parts_sum": ssum, "printed": q["printed_total"]})
    # attribute mismatches to image-only pages within [min_part_page-2, max_part_page]
    for mrec in g1_bad:
        q = next(x for x in doc_questions if x["question_number"] == mrec["question"])
        pages = [p["source_page"] for p in q["parts"] if p.get("source_page")]
        if pages:
            lost = [p for p in content_img_pages if min(pages) - 2 <= p <= max(pages)]
        else:   # no anchored parts (heavily damaged question) — use neighbour footer window
            prev_p = max((footer_page[qq] for qq in footer_page if qq < mrec["question"]), default=0)
            next_p = min((footer_page[qq] for qq in footer_page if qq > mrec["question"]), default=10**6)
            lost = [p for p in content_img_pages if prev_p <= p <= next_p]
        if lost:
            mrec["attributed_to_image_only_pages"] = lost
            defective.add(mrec["question"])
    unattributed_bad = [m for m in g1_bad if "attributed_to_image_only_pages" not in m]
    total = sum(q["printed_total"] if q["printed_total"] is not None
                else inferred_totals[q["question_number"]] for q in doc_questions)
    count_ok = (expect_q is None) or (len(doc_questions) == expect_q)
    for g in footer_gaps:
        report["review_queue"].append({"part": f"Q{g['question']}", "reason": g["reason"]})
    g1_ok = not g1_bad and not footer_gaps and total == PAPER_TOTAL and count_ok
    g1_review = (not g1_ok) and not unattributed_bad and all(g["attributed"] for g in footer_gaps)
    report["gates"].append({
        "gate": "G1-structure", "status": "PASS" if g1_ok else ("REVIEW" if g1_review else "FAIL"),
        "summary": (f"{len(doc_questions)} questions; Σ question totals={total}/{PAPER_TOTAL}; "
                    f"parts-sum == printed total for all questions: {not g1_bad}"
                    if not footer_gaps and not inferred_totals else
                    f"{len(doc_questions)} questions extracted; Σ known totals={total}/{PAPER_TOTAL}; "
                    f"source defects: missing Q{sorted(defective)} (image-only pages "
                    f"{content_img_pages} in archive PDF) — lost content needs human/OCR re-ingest"),
        "details": {"mismatches": g1_bad, "unattributed": unattributed_bad,
                    "inferred_totals": inferred_totals, "footer_gaps": footer_gaps,
                    "image_only_pages": content_img_pages, "count_expected": expect_q}})
    if defective or content_img_pages:
        report["source_defects"] = {"image_only_pages": content_img_pages,
                                    "affected_questions": sorted(defective)}

    # G2 verbatim — emitted text vs the source lines it claims to be copied from
    g2_bad, g2_ratios = [], {}
    for q in doc_questions:
        for p in q["parts"]:
            grams = ngrams(p["problem_md"])
            if not grams:
                continue
            src_grams = ngrams(p["source_norm"])
            ratio = sum(1 for g in grams if g in src_grams) / len(grams)
            g2_ratios[p["part_number"]] = round(ratio, 4)
            if ratio < 0.95:
                g2_bad.append({"part": p["part_number"], "ratio": round(ratio, 4)})
    gate("G2-verbatim", not g2_bad,
         f"5-gram overlap vs source region ≥0.95 for all {len(g2_ratios)} parts: {not g2_bad}",
         {"violations": g2_bad, "min_ratio": min(g2_ratios.values()) if g2_ratios else None})

    # G3 MCQ integrity
    mcq = [p for q in doc_questions for p in q["parts"] if p["question_type"] == "multiple_choice"]
    g3_issues = []
    for p in mcq:
        labels = [c["label"] for c in p["choices"]]
        if labels != ["A", "B", "C", "D"]:
            g3_issues.append({"part": p["part_number"], "issue": f"labels={labels}"})
        if not any(c.get("is_correct") for c in p["choices"]):
            g3_issues.append({"part": p["part_number"], "issue": "no keyed correct choice"})
            report["review_queue"].append({"part": p["part_number"], "reason": "MCQ key unresolved from MS"})
    gate("G3-mcq-integrity", not g3_issues,
         f"{len(mcq)} MCQ parts; all have printed A–D and MS-keyed answer: {not g3_issues}",
         {"issues": g3_issues})

    # G4 figure resolution
    dangling = [{"part": p["part_number"]} for q in doc_questions for p in q["parts"]
                if MENTION_RE.search(p["problem_md"]) and not p["assets"]]
    n_assets = sum(len(p["assets"]) for q in doc_questions for p in q["parts"])
    n_unanchored = sum(1 for q in doc_questions for p in q["parts"] if p["source_page"] is None)
    gate("G4-figure-resolution", not dangling,
         f"{n_assets} asset records (crop-required) cover every table/diagram/grid/apparatus mention; "
         f"{n_unanchored} parts without page anchor",
         {"dangling": dangling, "pages_unanchored": n_unanchored})
    report["review_queue"].extend(
        [{"part": p["part_number"], "reason": f"figure crop required ({', '.join(a['mention'] for a in p['assets'])}, page {p['source_page']})"}
         for q in doc_questions for p in q["parts"] if p["assets"]])

    # G5 answer linkage
    parts_all = [p for q in doc_questions for p in q["parts"]]
    linked = sum(1 for p in parts_all if p["answer_status"] == "linked")
    cov = linked / len(parts_all)
    status = "PASS" if cov >= 0.8 else ("REVIEW" if cov >= 0.5 else "FAIL")
    unmatched = [p["part_number"] for p in parts_all if p["answer_status"] != "linked"]
    report["gates"].append({"gate": "G5-answer-linkage", "status": status,
                            "summary": f"MS linkage {linked}/{len(parts_all)} ({cov:.0%})",
                            "details": {"unmatched": unmatched}})
    report["review_queue"].extend([{"part": pn, "reason": "answer not auto-linked to MS"} for pn in unmatched])

    # G6 registry codes — documented registry gaps go to REVIEW; unknown codes FAIL
    ALLOWED_GAPS = {"4CH1-3.15C"}   # chemistry-only rates practical; SME notes corpus lacks it
    g6_bad = []
    for q in doc_questions:
        for p in q["parts"]:
            for c in p["spec_point_codes"]:
                if c not in registry and c not in ALLOWED_GAPS:
                    g6_bad.append({"part": p["part_number"], "code": c})
    n_pending = sum(1 for p in parts_all if p["tagging"] == "pending-llm")
    gate("G6-registry-codes", not g6_bad,
         f"all emitted codes ∈ spec_point_resolution registry ({len(registry)} codes) "
         f"or documented gaps→review; {n_pending} parts pending-llm tagging",
         {"violations": g6_bad, "allowed_gaps": sorted(ALLOWED_GAPS)})

    # ---- assemble document (before popping internal fields) ------------------
    topic = {
        "schema": SCHEMA, "generated_utc": now_iso(),
        "generator": f"official_examq_extract.py v{CONVERTER_VERSION} (ADR-037) series={series}",
        "paper_id": paper_id,
        "source": {"qp_sha256": qp_sha, "ms_sha256": ms_sha,
                   "series": manifest["series"]["normalized"],
                   "printed": manifest["series"].get("printed"),
                   "archive": [m["source"]["archive"] for m in manifest["materials"]]},
        "paper_info": {"code": manifest["paper"]["official_reference"],
                       "session": manifest["series"]["normalized"],
                       "total_marks": total,
                       "course_id": "igcse-chemistry-19"},
        "questions": [{
            "id": f"{manifest['paper']['official_reference'].replace('/', '-')}-{q['question_number']:02d}",
            "question_number": q["question_number"],
            "total_marks": q["printed_total"] if q["printed_total"] is not None else inferred_totals[q["question_number"]],
            "total_marks_source": "printed-footer" if q["printed_total"] is not None else "inferred-parts-footer-missing",
            "stem_md": q["stem_md"],
            "parts": [{k: v for k, v in p.items()
                       if k not in ("group_stem_md", "option_list", "group", "roman", "answer_raw", "source_norm") and v is not None}
                      for p in q["parts"]],
        } for q in doc_questions],
    }
    # attach group stems/option lists that carry content
    for q, dq in zip(topic["questions"], doc_questions):
        extras = {}
        for p in dq["parts"]:
            if p.get("group_stem_md") and p["group_stem_md"] not in extras:
                extras[p["group"]] = {"group_stem_md": p["group_stem_md"]}
            if p.get("option_list"):
                extras.setdefault(p["group"], {})["option_list"] = p["option_list"]
        q["groups"] = {g: v for g, v in extras.items() if v}

    # strip internal linkage fields from working copy
    for q in doc_questions:
        for p in q["parts"]:
            p.pop("group", None); p.pop("roman", None); p.pop("answer_raw", None)

    # ---- negative controls ---------------------------------------------------
    nc_results = []
    flat_parts = [p for q in topic["questions"] for p in q["parts"]]
    # N1: bump one mark on the last part of the question with the most parts
    if flat_parts:
        nc = copy.deepcopy(topic)
        tgt = max(nc["questions"], key=lambda q: len(q["parts"]))["parts"][-1]
        tgt["marks"] = (tgt["marks"] or 0) + 1
        g1_nc = _g1_recheck(nc, PAPER_TOTAL)
        nc_results.append({"id": "N1-mark-bump", "expected_gate": "G1", "detected": g1_nc})

    # N2: one-word substitution in a mid-length part (mimics paraphrase drift)
    nc2 = copy.deepcopy(topic)
    cands = [(qn, p) for qn, q in enumerate(nc2["questions"]) for p in q["parts"]
             if p.get("problem_md") and 15 <= len(p["problem_md"].split()) <= 90]
    nc2_target = None
    if cands:
        _, p_t = max(cands, key=lambda t: len(t[1]["problem_md"].split()))
        toks = p_t["problem_md"].split()
        i = next((j for j in range(len(toks) // 3, len(toks))
                  if len(toks[j]) > 3 and toks[j].isalpha()), None)
        if i is not None:
            toks[i] = "qxqqx"
            p_t["problem_md"] = " ".join(toks)
            nc2_target = p_t["part_number"]
    g2_nc = False
    if nc2_target:
        src = next(p for q in topic["questions"] for p in q["parts"] if p["part_number"] == nc2_target)
        mod = next(p for q in nc2["questions"] for p in q["parts"] if p["part_number"] == nc2_target)
        grams = ngrams(mod["problem_md"])
        r = sum(1 for g in grams if g in ngrams(src["problem_md"])) / len(grams) if grams else 1.0
        g2_nc = r < 0.95
    nc_results.append({"id": "N2-paraphrase", "expected_gate": "G2", "detected": g2_nc,
                       "target": nc2_target})

    # N3: fake spec code injected into the first part (skipped if no parts extracted)
    if flat_parts:
        nc3 = copy.deepcopy(topic)
        next(p for q in nc3["questions"] for p in q["parts"])["spec_point_codes"] = ["4CH1-9.99"]
        g6_nc = any(c not in registry for q in nc3["questions"] for p in q["parts"] for c in p["spec_point_codes"])
        nc_results.append({"id": "N3-fake-spec-code", "expected_gate": "G6", "detected": g6_nc})
    report["negative_controls"] = nc_results

    # ---- write outputs -------------------------------------------------------
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "topic.json").write_text(json.dumps(topic, indent=1, ensure_ascii=False))
    (OUT / "validation-report.json").write_text(json.dumps(report, indent=1, ensure_ascii=False))
    write_questions_md(topic, OUT / "questions.md")

    print(f"paper: {paper_id}  (series arg: {series})")
    for g in report["gates"]:
        print(f"  {g['gate']:22} {g['status']:6} {g['summary']}")
    for nc in nc_results:
        print(f"  NC {nc['id']:18} {'DETECTED' if nc['detected'] else 'MISSED'} (expected {nc['expected_gate']})")
    print(f"  review queue: {len(report['review_queue'])} items")
    print(f"  outputs -> {OUT}")
    return 0


def _g1_recheck(doc, paper_total):
    """Negative-control recheck: any per-question parts/total mismatch or paper-total drift."""
    per_q = any(sum(p["marks"] or 0 for p in q["parts"]) != q["total_marks"] for q in doc["questions"])
    return per_q or sum(q["total_marks"] for q in doc["questions"]) != paper_total


def write_questions_md(topic, path):
    out = [f"# {topic['paper_info']['code']} — {topic['source']['series']} (official extraction)",
           "", f"> schema `{topic['schema']}` · paper_id `{topic['paper_id']}` · "
               f"qp sha256 `{topic['source']['qp_sha256'][:16]}…` · extracted verbatim, never regenerated (ADR-037)", ""]
    for q in topic["questions"]:
        out.append(f"## Question {q['question_number']} ({q['total_marks']} marks)")
        if q["stem_md"]:
            out += ["", q["stem_md"], ""]
        for g, gv in (q.get("groups") or {}).items():
            if gv.get("group_stem_md"):
                out += [f"**({g})** {gv['group_stem_md']}", ""]
            if gv.get("option_list"):
                out += [f"- {lab}" for lab in gv["option_list"]] + [""]
        for p in q["parts"]:
            marks = f"[{p['marks']}]" if p["marks"] is not None else "[?]"
            out.append(f"### {p['part_number']} {marks}")
            out += ["", p["problem_md"], ""]
            if p.get("choices"):
                out += [f"- **({c['label']})** {c['text_md']}" + ("  ✔" if c.get("is_correct") else "")
                        for c in p["choices"]] + [""]
            if p.get("assets"):
                out += [f"> 🖼 asset required: {a['mention']} (qp.pdf p.{a['page']})" for a in p["assets"]] + [""]
        out.append("")
    path.write_text("\n".join(out))


if __name__ == "__main__":
    sys.exit(main())
