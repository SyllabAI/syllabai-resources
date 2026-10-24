#!/usr/bin/env python3
"""
official_examq_extract.py — official-paper converter (ADR-039)
==============================================================
Converts ONE official past paper (QP+MS) into the serving schema
`syllabai.official-paper-questions/0.2` via the deterministic extraction
baseline, then runs fail-disclosed gates G0–G7 incl. G2-D plus negative
controls re-targeted at undisclosed mutation.

The one-sentence rule (ADR-039 §2): the pipeline improves; provenance
discloses. Extraction is the baseline every document is measured against;
any tool may correct, clarify or enrich any serving field provided every
departure from the extraction baseline is machine-disclosed (edit_status,
edits[], value_trace) and graded values corroborate the MS of record or
carry explicit correction evidence. Labels stay registry-validated (G6).

Run:  python3 official_examq_extract.py --series 2020-11                (baseline series, paper 1C)
      python3 official_examq_extract.py --series 2022-06 --paper 2C    (paper variants: 1C default, 2C since v0.8/F34)
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

SCHEMA = "syllabai.official-paper-questions/0.2"
CONVERTER_VERSION = "0.16.0"  # see Official-ExamQuestion/CHANGELOG.md + LEDGER.md

# --- F64: course parametrization (the ADR-037 §5 board-layout generalization
# --- pass, unlocked for igcse-maths-b-16 by operator order trace
# --- 1a16f0dae0405399, 2026-10-25). Chemistry stays the default course and its
# --- behavior is byte-identical: every module-level default below IS the
# --- chemistry config; main() rebinds globals only when --course is given.
COURSE_PREFIX = "4CH1"   # staging/output filename prefix, rebound per course
COURSES = {
    "igcse-chemistry-19": {
        "paper_prefix": "4CH1",
        "paper_totals": {"1C": 110, "2C": 70, "1CR": 110, "2CR": 70},
        "footer_re": r"\(Total for Question (\d{1,2}) = (\d{1,2}) marks\)",
        "spec_resolution": None,   # None = keep the module-level resolution chain
        "expect_questions": None,  # None = keep the module-level EXPECT_QUESTIONS
    },
    "igcse-maths-b-16": {
        "paper_prefix": "4MB1",
        # 4MB1/01 and /02 are 100-mark papers across the era. Footer-verified so
        # far: 2025-11/02 (12 questions summing 100, staged run 2026-10-25). The
        # remaining variants enter EXPECT_QUESTIONS per series as their tranches
        # footer-verify (G1 asserts every series anyway — an unverified total
        # cannot pass G1 silently).
        "paper_totals": {"01": 100, "02": 100, "01R": 100, "02R": 100},
        # maths-B footers print '(Total for Question N is X marks)' — 'is', not '='
        "footer_re": r"\(Total for Question (\d{1,2}) is (\d{1,2}) marks\)",
        # No SME spec-point registry exists for maths-B (SME publishes zero
        # maths-B topic questions — T-SME-12). Tranche-1 G6 posture: no codes
        # emitted, all parts honest pending-llm, G6 vacuous with a documented
        # gap note. A maths-B registry (DB spec tree 4MB1-2017, 215 points) is
        # the spec-tagging wave's prerequisite, filed as open work.
        "spec_resolution": False,
        "expect_questions": {"01": {}, "02": {"2025-11": 12}, "01R": {}, "02R": {}},
    },
}
# registry expectations per paper variant (LEDGER F34: paper parametrization). Marks
# totals are footer-verified per series: 1C = 110 (constant across the era), 2C = 70
# (constant across the era; staging probe 2026-10-21: 16/16 series sum exactly 70).
# R variants footer-verified from the archive of record 22/22 (F-178 R-VARIANT
# SCHEDULE, tracker PR #32 receipt: 1CR = 110 x11, 2CR = 70 x11; legacy 4CH0 R
# papers 2013-2017 are a different spec and stay out of scope).
PAPER_TOTALS = {"1C": 110, "2C": 70, "1CR": 110, "2CR": 70}
PAPER_TOTAL = PAPER_TOTALS["1C"]   # runtime global — set per run in main()
# printed question counts verified per series (footers vary 6..15 across the 4CH1 era);
# counts cross-checked against per-question footer marks summing to the paper total
EXPECT_QUESTIONS = {
    "1C": {"2020-11": 10, "2020-01": 10, "2021-06": 10, "2022-06": 10, "2024-06": 10,
           "2019-06": 15, "2021-01": 11, "2021-11": 11, "2022-01": 11, "2023-01": 12,
           "2023-06": 10, "2023-11": 10, "2024-11": 11, "2025-06": 10, "2025-11": 10,
           "2026-06": 9},
    "2C": {"2019-06": 8, "2020-01": 7, "2020-11": 7, "2021-01": 7, "2021-06": 7,
           "2021-11": 7, "2022-01": 7, "2022-06": 7, "2023-01": 7, "2023-06": 7,
           "2023-11": 7, "2024-06": 7, "2024-11": 7, "2025-06": 6, "2025-11": 6,
           "2026-06": 6},
    # R variants (F-178 schedule, footer-verified 22/22): both tranches convert —
    # 1CR in the v0.12.0 run (resources PR #46), 2CR in the v0.13.0 run.
    "1CR": {"2019-06": 10, "2020-01": 11, "2020-11": 10, "2021-01": 10, "2022-01": 11,
            "2022-06": 11, "2023-01": 10, "2023-06": 11, "2024-06": 12, "2025-06": 11,
            "2026-06": 11},
    "2CR": {"2019-06": 7, "2020-01": 7, "2020-11": 7, "2021-01": 8, "2022-01": 7,
            "2022-06": 7, "2023-01": 8, "2023-06": 7, "2024-06": 7, "2025-06": 7,
            "2026-06": 7},
}
# per-series demo seeds (labels only; registry-validated in G6). Other series -> pending-llm.
SEEDS = {
    # v0.5 demo seeds, audited against the spec registry in v0.7 (LEDGER F31):
    # 4(c)(ii) is an Mr calculation (1.26), 8(c)(ii) a molar-enthalpy
    # calculation (3.4), 10(b) an empirical-formula determination (1.33),
    # 1(b)(i) the noble-gas group (1.24)
    "2020-11": {
        "1(b)(i)": "4CH1-1.24", "4(c)(ii)": "4CH1-1.26",
        "9(c)(ii)": "4CH1-1.28", "10(b)": "4CH1-1.33",
        "8(c)(ii)": "4CH1-3.4", "7": "4CH1-3.15C",   # 7* deliberately incl. registry-gap demo
    },
}


def paths_for(series: str, paper: str = "1C") -> dict:
    # F34: staging names are paper-suffixed. The .txt extraction names were NOT
    # paper-suffixed before v0.8 (a 1C/2C staging collision); fall back to the
    # legacy bare name so pre-0.8 staging areas keep working for 1C.
    # F64: the PDF prefix + output dir are course-scoped (COURSE_PREFIX global,
    # rebound in main() from COURSES[prefix]; chemistry default unchanged).
    qp_txt = UPLOAD / f"official-{series}-{paper}-qp.txt"
    ms_txt = UPLOAD / f"official-{series}-{paper}-ms.txt"
    legacy_qp_txt = UPLOAD / f"official-{series}-qp.txt"
    legacy_ms_txt = UPLOAD / f"official-{series}-ms.txt"
    return {
        "qp_pdf": UPLOAD / f"official-{COURSE_PREFIX}-{paper}-{series}-qp.pdf",
        "ms_pdf": UPLOAD / f"official-{COURSE_PREFIX}-{paper}-{series}-ms.pdf",
        "qp_txt": qp_txt if (qp_txt.exists() or not legacy_qp_txt.exists()) else legacy_qp_txt,
        "ms_txt": ms_txt if (ms_txt.exists() or not legacy_ms_txt.exists()) else legacy_ms_txt,
        "manifest": UPLOAD / f"manifest-{series}-{paper}.yaml",
        # v0.10 (F41): optional OCR source layer for image-only pages
        "ocr_index": UPLOAD / "ocr" / f"{series}-{paper}" / "ocr-pages.json",
        "out": OUTROOT / series / f"{COURSE_PREFIX}-{paper}",
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
# ---------------------------------------------------------------- F48: PUA → Unicode
# The source PDFs embed symbol/dingbat fonts (SymbolMT, Wingdings 1/2/3,
# EuclidExtra, MathType-style CID subsets) whose text layer maps to Unicode
# Private Use Area (U+E000–U+F8FF). Left as-is they leak into served
# problem/stem/solution text as invisible garbage glyphs (corpus census at
# v0.10.1: 18 distinct PUA chars, ~2.4k occurrences). Every mapping below was
# decided from EVIDENCE (PDF font trace + page render, eyeballed), never
# guessed: the char is what the printed page shows at that spot.
PUA_MAP = {
    "\uf022": "\u2192",   # Wingdings3 arrowright — equation arrow (N2 + 3H2 → 2NH3)
    "\uf02d": "\u2212",   # minus — printed CID dash: charge (2Cl−), subtraction (75 − 30)
                          # and bond (C−H) all share this glyph; minus matches the
                          # charge/arithmetic semantics and the corpus house style
                          # ('(ΔH =) − 3600' already uses U+2212)
    "\uf044": "\u0394",   # Symbol Delta — (ΔH =) −3600
    "\uf072": "\u0394",   # Wingdings3 Delta — 'M4 ΔH correctly shown'
    "\uf083": "\u21cc",   # EuclidExtra — equilibrium arrow N2O4(g) ⇌ 2NO2(g)
    "\uf0a2": "",         # Wingdings2 dotted answer-line rule — page furniture, dropped
    "\uf0ad": "\u2191",   # CID subset up-arrow — Energy-axis arrow in the 2022-06 cycle
    "\uf0ae": "\u2192",   # CID long arrowright — equation arrow
    "\uf0b0": "\u00b0",   # Symbol degree — '(°C)'
    "\uf0b4": "\u00d7",   # Symbol multiply — 100 × 4.2 × 49.5
    "\uf0b7": "\u2022",   # Symbol bullet — MS solution list bullets
    "\uf0b8": "\u00f7",   # Symbol divide — 0.0129 ÷ 2
    "\uf0e0": "\u2192",   # Wingdings arrowright — word-equation arrow
    "\uf0e5": "\u03a3",   # CID Sigma — 'M1 Σ bonds broken'
    "\uf097": "\u2022",   # Wingdings2 bullet — QP list bullets
    "\uf09f": "\u2022",   # QP method-list bullet (2021-01 2C 'This is the student's method')
    "\uf0fc": "\u2713",   # Wingdings check — 'Add ticks (✓)'
    "\uf8e7": "\u2500",   # box-drawing light horizontal — the printed continuous bond
                          # rule (H─C──C──C─H); renders as an unbroken line so
                          # double bonds read as one longer rule, like the print
    # Cover-page furniture (wave-14 source-census additions: these live in the
    # raw txt but never reached served strings — the paper-variant tick-box
    # ornaments on the front cover, a filled+hollow shape pair per series;
    # font trace Wingdings2, renders eyeballed). Dropped like F0A2.
    "\uf0ee": "",         # 2023-11/2025-06 covers: eight-point seal + star
    "\uf0c0": "",         # 2023-06/2025-11 covers: pentagons
    "\uf098": "",         # 2022-01/2023-01 covers: circles
    "\uf0bf": "",         # 2022-06 covers: diamonds
    "\uf0c2": "",         # 2024-11 covers: hexagons
    # 1CR tranche additions (2026-10-22, trace 1a162ea420f90a75) — each from a
    # PDF font trace + page render, eyeballed:
    "\uf033": "\u2713",   # ZapfDingbatsITCbyBT check — 'Place ticks (✓) in three boxes'
                          # (2019-06 1CR p4); same semantics as the F0FC Wingdings check
    "\uf8ee": "\u23a1",   # Symbol big-bracket UPPER corner — the drawn repeating-unit
    "\uf8ef": "\u23a2",   #   scaffold (2022-06 1CR p21 chloroethene polymerisation):
    "\uf8f0": "\u23a3",   #   top/extension/bottom pieces, box-drawing family like F8E7.
                          #   The 2022-06 1CR text layer mirrors both columns onto
                          #   these three codepoints (right-corner mirror not then
                          #   distinguishable); the 2CR run (below) evidences and
                          #   maps the true right-column trio.
    # 2CR tranche additions (2026-10-22, trace 1a16373bc7d373fd) — each from a
    # PDF font trace + page render, eyeballed:
    "\uf050": "\u2713",   # Wingdings2 check — 'Add ticks (✓) to the table to show the
                          # concordant results' (2019-06 2CR p16 render; the third
                          # tick glyph of the corpus, after F033 ZapfDingbats + F0FC
                          # Wingdings — same printed semantics, U+2713 everywhere)
    "\uf8f9": "\u23a4",   # Symbol big-bracket UPPER-RIGHT corner — the repeat-unit
    "\uf8fa": "\u23a5",   #   answer scaffold (2023-01 2CR p9 polyester equation):
    "\uf8fb": "\u23a6",   #   top/mid/bottom right pieces mirroring F8EE/F8EF/F8F0;
                          #   text layer pairs them positionally (top row F8EE+F8F9,
                          #   18 extension rows F8EF+F8FA, bottom row F8F0+F8FB),
                          #   font trace MWAWPZ+Symbol, render eyeballed — retires
                          #   the 1CR right-column mirror caveat with direct evidence
    # --- igcse-maths-b-16 tranche-1 additions (2026-10-25, operator order trace
    # --- 1a16f0dae0405399): sourced from the T-MIG-141 glyph-normalization table
    # --- of record (syllabai-parser tools/glyph-normalization/table.v1.json,
    # --- sha256 1fdd4b4a..., 84 entries + 5 sequence rules, each entry carrying
    # --- rendered-PDF evidence in syllabai-parser evidence/T-MIG-141/ — sheets,
    # --- crops-run002b, crops-run004-f0cf). These are corpus-wide Pearson
    # --- SymbolMT/Symbol mappings (the DB patch of record applied them to the
    # --- 13,765-chunk bank, run-005), not chemistry-specific — merging them
    # --- cannot change chemistry outputs (none of these CPs occur in chemistry
    # --- texts). The composed arrow-run sequence rules (SEQ-A1..B5) are NOT
    # --- here: per-char substitution serves the piece glyphs; runs stay a
    # --- disclosed tranche-2 item (none occur in 2025-11/02).
    "\uf05b": "[",         # Symbol bracket-left piece — column-vector/fraction scaffolds
    "\uf05d": "]",         # Symbol bracket-right piece (T-MIG-141: our-render, 51 inst)
    "\uf0e6": "\u239b",   # big paren LEFT-TOP piece (positional law, 1,432 inst)
    "\uf0e7": "\u239c",   # big paren LEFT-EXT piece (positional law, 1,496 inst)
    "\uf0e8": "\u239d",   # big paren LEFT-BOTTOM piece (positional law, 1,436 inst)
    "\uf0e9": "\u23a1",   # big bracket LEFT-TOP piece (positional law, 135 inst)
    "\uf0ea": "\u23a2",   # big bracket LEFT-EXT piece (positional law, 94 inst)
    "\uf0eb": "\u23a3",   # big bracket LEFT-BOTTOM piece (positional law, 135 inst)
    "\uf0f6": "\u239e",   # big paren RIGHT-TOP piece (positional law, 1,432 inst)
    "\uf0f7": "\u239f",   # big paren RIGHT-EXT piece (positional law, 1,498 inst)
    "\uf0f8": "\u23a0",   # big paren RIGHT-BOTTOM piece (positional law, 1,437 inst)
    "\uf0f9": "\u23a4",   # big bracket RIGHT-TOP piece (positional law, 135 inst)
    "\uf0fa": "\u23a5",   # big bracket RIGHT-EXT piece (positional law, 94 inst)
    "\uf0fb": "\u23a6",   # big bracket RIGHT-BOTTOM piece (positional law, 135 inst)
    "\uf026": "\u0307",   # combining dot-above — recurring-decimal notation (95 inst)
    "\uf03c": "<",         # Symbol less-than (99 inst, our-render)
    "\uf03e": ">",         # Symbol greater-than (55 inst, our-render)
    "\uf061": "\u21a6",   # mapsto (20 inst, our-render+context-scaffold)
    "\uf070": "\u03c0",   # Symbol pi (569 inst, our-render)
    "\uf084": "\u2264",   # less-than-or-equal (520 inst; spec-sqrt hypothesis
                          # OVERTURNED by pair evidence with F0B7-family >=)
    "\uf0b1": "\u00b1",   # plus-minus (392 inst, our-render+context-scaffold)
    "\uf0b9": "\u2260",   # not-equal (13 inst, our-render)
    "\uf0de": "\u21d2",   # rightwards double arrow (11 inst, our-render)
    "\uf07b": "{",         # Symbol brace-left (6 inst, our-render)
    "\uf07d": "}",         # Symbol brace-right (6 inst, our-render)
}


# F64 (v0.16.0): spec §3.4 control-char policy — C0 controls that survive into
# served strings (the maths-B QP text layer carries the SymbolMT private-use
# operator class, e.g. 0x16-0x1F between numeric terms) fall back to a single
# space, logged per-instance here and disclosed in the validation report.
# NEVER silent. An operator-class adjudication (which controls are ×/÷ vs
# furniture) is a review-queue item until font-trace + render evidence lands.
CTL_COUNTER = {}

def _ctl_note(cp):
    CTL_COUNTER[cp] = CTL_COUNTER.get(cp, 0) + 1

def normalize_pua(s: str) -> str:
    """F48: map every known PUA char to its real Unicode form; REFUSE unknown
    PUA (fail-closed — a new symbol font must earn an evidenced mapping entry
    above, it must not silently leak into served content).
    F52 (v0.13.1): evidenced non-PUA source-char normalization applied before the
    PUA gate — MyriadPro-It's custom encoding renders the printed italic Delta as
    U+01FB (LATIN SMALL LETTER A WITH RING ABOVE AND ACUTE — bytes C7 BB in the
    UTF-8 source layers; identified by hex census after a visual codepoint guess
    U+01DF proved WRONG and the no-op parity run caught it), so every 'ǻ' in a
    source layer is Δ: 2020-01 1CR p18 renders 'Calculate the molar enthalpy
    change, ΔH, in kJ/mol.' and 2020-01 2CR pp19-20 '...the enthalpy change,
    ΔH.' / 'ΔH = ...' (font trace MPEIOE+MyriadPro-It, Type 1C Custom; renders
    eyeballed). Corpus census: 5 raw-layer hits (C7 BB), ALL immediately before
    'H' (Delta-H semantics), both 2020-01 R slices fixed in this run; the
    mapping runs on both G2 sides (the line-scan + the page-level norm) so
    verbatim overlap is unaffected."""
    s = s.replace("\u01fb", "\u0394")   # F52: italic-Delta artifact -> Δ
    # F64: spec §3.4 control-char fallback (logged, disclosed in the report)
    if any((ord(c) < 0x20 and c not in "\t\n\r\x0c") for c in s):
        s = "".join((_ctl_note(hex(ord(c))) or " ") if (ord(c) < 0x20 and c not in "\t\n\r\x0c") else c
                    for c in s)
    if not any(0xE000 <= ord(c) <= 0xF8FF for c in s):
        return s
    out = []
    for c in s:
        cp = ord(c)
        if 0xE000 <= cp <= 0xF8FF:
            if c not in PUA_MAP:
                raise ValueError(
                    f"unmapped PUA char U+{cp:04X} in {s[:80]!r} — add an evidenced "
                    f"PUA_MAP entry (font trace + page render) before running")
            out.append(PUA_MAP[c])
        else:
            out.append(c)
    return "".join(out)


FURNITURE_SUBS = [
    (re.compile(r"\*P\d{5}[A-Z]\w*\*"), " "),       # page identity marker (P62045A*, P58561A*, ...)
    (re.compile(r"\bTurn over\b"), " "),
    (re.compile(r"DO NOT WRITE IN THIS (?:AREA|MARGIN|SPACE)\s*"), " "),   # often 3x on one line
    # F65 (v0.16.0): maths-B page furniture — the multi-page question continuation
    # header and the printed formula scaffold in the answer space (the quadratic
    # formula box every 4MB1 paper prints; 2025-11 Q5 leak eyeballed). Neither
    # string occurs anywhere in the chemistry corpus (census 2026-10-25: 0 hits
    # in the staged 2020-11 baseline layer), so the parity surface is unchanged.
    (re.compile(r"\bQuestion \d{1,2} continued\b"), " "),
]
FURNITURE_LINE = [
    re.compile(r"^\s*PMT\s*$"),                     # archive watermark
    re.compile(r"^\s*BLANK PAGE\s*$"),
    re.compile(r"^\s*DO NOT WRITE IN THIS (AREA|MARGIN|SPACE)\s*$"),
    re.compile(r"^\s*\d{1,2}\s*$"),                 # bare page number (1..36)
    re.compile(r"^[\s.]*\.[\s.]*$"),                # dotted answer lines
    # F65 (v0.16.0): the printed formula scaffold in the maths answer space —
    # the quadratic-formula box every 4MB1 paper prints. normalize_pua runs
    # BEFORE these patterns (clean_lines), so the SymbolMT control chars are
    # already spaces here; .match() anchors at string start, hence the ^\s*.
    # The box flattens to two lines: 'b b 2 4ac' (the −b ± √(b²−4ac) numerator)
    # and 'Solutions of ax 2 bx c 0 are x' (the caption). The double-b + 4ac
    # token sequence is box-specific — MS working rows substitute numbers and
    # carry at most a single leading 'b'. Census: zero occurrences in chemistry.
    re.compile(r"^\s*Solutions of ax"),
    re.compile(r"^\s*b\s+b\s*2\s*4ac\s*$"),
    re.compile(r"^\s*$"),
    # F42: the MS is one table; every printed page repeats its header, and a
    # marker row near a page break would otherwise swallow the next page's
    # header into its answer block (2019-06 3(d)(ii) inherited
    # 'Question / Answer Notes Marks / number' as its solution)
    re.compile(r"^\s*Question\s*$"),
    re.compile(r"^\s*Answer\s+Notes\s+Marks\s*$"),
    re.compile(r"^\s*number\s*$"),
    re.compile(r"^\s*Marks\s*$"),
]


def clean_lines(raw: str):
    out = []
    for ln in raw.splitlines():
        ln = normalize_pua(ln)   # F48: symbol-font PUA -> real Unicode before any parsing
        for rx, rep in FURNITURE_SUBS:
            ln = rx.sub(rep, ln)
        if any(rx.match(ln) for rx in FURNITURE_LINE):
            continue
        out.append(ln.rstrip())
    # F65 (v0.16.0): the flattened quadratic-formula box — the scaffold prints
    # as a 4-line consecutive run in the layout text layer: 'b' / 'b 2' / '4ac'
    # / '0 are x' (the −b ± √(b²−4ac) numerator pieces + the caption tail,
    # control chars already spaced by normalize_pua). Remove the exact
    # consecutive signature wherever it appears; everything else survives.
    i = 0
    res = []
    while i < len(out):
        if (i + 3 < len(out)
                and out[i].strip() == "b"
                and out[i + 1].strip() == "b 2"
                and out[i + 2].strip() == "4ac"
                and out[i + 3].strip() == "0 are x"):
            i += 4
            continue
        # F65: the box's fraction denominator ('2a') can detach from the
        # numerator pieces by the answer-space page break and surface between
        # the question's '(N)' marks line and its footer. Two-sided anchor:
        # standalone '2a' + previous non-blank line is a marks line + next
        # non-blank line is the question footer — no other '2a' matches.
        if out[i].strip() == "2a":
            prev = next((res[j] for j in range(len(res) - 1, -1, -1) if res[j].strip()), "")
            nxt = next((out[j].strip() for j in range(i + 1, len(out)) if out[j].strip()), "")
            if re.match(r"^\(\d{1,2}\)$", prev.strip()) and FOOTER_RE.search(nxt):
                i += 1
                continue
        res.append(out[i])
        i += 1
    return res


# ---------------------------------------------------------------- stage 2: segmentation
FOOTER_RE = re.compile(r"\(Total for Question (\d{1,2}) = (\d{1,2}) marks\)")
QSTART_RE = re.compile(r"^\s*(\d{1,2})\s+([A-Za-z(].*)$")   # remainder must start alpha/'(' (indent-tolerant)
L1_RE = re.compile(r"^\s*\(([a-h])\s*\)\s*(.*)$")
L2_RE = re.compile(r"^\s*\((i{1,3}|iv|v|vi{1,3})\s*\)\s+(.*)$")   # romans i..viii
L2_INLINE_RE = re.compile(r"^\(([Ii]{1,3}|[Ii][Vv]|[Vv]|[Vv][Ii]{1,3})\s*\)\s+(.*)$")
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
    r"^ {0,20}(?:(\d{1,2})\s+)?(?:\(([a-h])\s*\)\s*)?(?:\(([Ii]{1,3}|[Ii][Vv]|[Vv]|[Vv][Ii]{1,3})\s*\)\s*)?(\S.*)$")
# F42 marker-column gate: marker rows sit in the MS table's marker column
# (indent <= 12 in every observed layout); the answer column starts deeper.
# Without the gate, answer-cell fragments like the unit '(g)' hijack the
# marker state (2019-06: '(g)' after 14(f)(i) re-pointed cur_letter to 'g'
# and 14(f)(ii) became unlinkable).
MS_MARKER_ONLY_RE = re.compile(
    r"^ {0,12}(?:(\d{1,2})\s+)?(?:\(([a-h])\s*\))?\s*(?:\(([Ii]{1,3}|[Ii][Vv]|[Vv]|[Vv][Ii]{1,3})\s*\))?\s*$")
# some series (2019-06) print sub-letters bare without parentheses: "    b      they have..."
# v0.10 (F42): the early 2019-06 MS also prints the letter at END OF LINE when the
# answer cell is a printed image/diagram (9(b) dot-and-cross): '    b' — the
# lookahead must accept end-of-line, else the row never opens its entry.
MS_BARE_LETTER_RE = re.compile(
    r"^ {0,12}(?:(\d{1,2})\s+)?([a-h])(?=\s{2,}|$)\s*(.*)$")
# v0.10 (F42): the early 2019-06 MS prints two-level markers bare —
# 'd   i' (letter + spaces + bare roman, e.g. 3(d)(i), 13(b)(i), 14(f)(i),
# 15(b)(i)), '   ii' (bare roman continuation row, e.g. 3(d)(ii), 10(a)(ii)),
# and glued '10ai' / 'bi' (unspaced qn+letter+roman / letter+roman).
# Same positional family as MS_BARE_LETTER_RE (F7); roman tokens are gated on
# the ascending-sequence invariant so content lines that merely begin with a
# roman-like token can never hijack a marker row.
# v0.12 (F50): DEGRADED two-level markers — the 1CR tranche prints the same
# marker with one or BOTH paren pairs lost in the text layer: '3 c (i)'
# (2019-06: bare letter + ONE space + paren roman — the old 2-space lookahead
# refused it), 'a (ii)' (2019-06 5(a)(ii): the letter repeats on the (ii) row),
# 'b)     i)' (2020-11: half-paren markers), '(e)      i' (2026-06: paren
# letter + bare roman). The branch fires ONLY when at least one paren is
# missing — fully-parenthesized '(a) (i)' rows fall through to MS_ROW_RE and
# keep the exact pre-v0.12 path (2020-01 4(a)(i)-style rows carry the marks
# digit in rest, which that branch keeps as content). The roman token stays
# bracket-bounded by the 2-space lookahead, so 'a viewpoint' can never match.
MS_DEGRADED_MARKER_RE = re.compile(
    r"^ {0,12}(?:(\d{1,2})\s+)?(\()?([a-h])(\))?\s+(\()?(i{1,3}|iv|v|vi{1,3})(\))?(?=\s{2,}|$)\s*(.*)$")
# v0.12 (F50): the glued family also prints letter + PAREN roman unspaced —
# 2019-06 1CR prints 4(b)(iv)'s bare 'b(iv)' marker-only row BETWEEN its M1
# and M2 answer rows ('    b(iv)').
MS_GLUED_MARKER_RE = re.compile(
    r"^ {0,12}(?:(\d{1,2}))?([a-h])(?:(i{1,3}|iv|v|vi{1,3})|\((i{1,3}|iv|v|vi{1,3})\s*\))(?=\s{2,}|$)\s*(.*)$")
# v0.12 (F50): half-paren BARE roman continuation row — 2020-11 1CR 3(b)(ii)
# prints 'ii)    M1 add bromine water' (open paren lost in the text layer).
# Same ascending-sequence gate as the bare form; a strictly separate branch so
# rows without the trailing paren keep the exact pre-v0.12 path.
MS_HALF_ROMAN_RE = re.compile(
    r"^ {0,12}(i{1,3}|iv|v|vi{1,3})\)(?=\s{2,}|$)\s*(.*)$")
# v0.12 (F50): rotated-margin sidebar fragments ('clip / with / graph' printed
# sideways in the scanned MS margin) interleave before the marker column —
# 2022-01 1CR Q8: '    clip    (b)     all points correctly plotted …'. Marker
# evidence must be strong: the row must carry a marks-column digit at the tail
# (a real table row — the wrapped tail fragments carry none) and the letter
# must ADVANCE the current group. Anything else stays content.
MS_SIDEBAR_LETTER_RE = re.compile(
    r"^ {0,6}[a-z]{2,10}\s{2,}\(([a-h])\s*\)\s*(\S.*)$")
MS_BARE_ROMAN_RE = re.compile(
    r"^ {0,12}(i{1,3}|iv|v|vi{1,3})(?=\s{2,}|$)\s*(.*)$")
# F46 (v0.11): parenthesized roman CONTENT row printed DEEP in the marker
# column's answer area (indent 21..30). The 2023-11 1C MS is the observed
# layout ('(ii)   best fit curve…', '(ii)   M1 curve starting…'); every
# previously seen parenthesized roman row sat at indent <= 20, so these rows
# fell through to content and were absorbed into the (i) block. Letter
# markers at this depth stay refused on purpose: answer-cell fragments like
# '(g)' must never re-point the marker state (the F42 lesson).
MS_DEEP_ROMAN_RE = re.compile(
    r"^ {21,30}\(([Ii]{1,3}|[Ii][Vv]|[Vv]|[Vv][Ii]{1,3})\s*\)\s+(\S.*)$")


def parse_ms(ms_lines):
    """Link MS rows positionally: rows carry qnum / letter / roman in any
    combination; absent components inherit from the previous row. Marker-only
    rows (e.g. a bare '(ii)' line) open an entry whose content starts on the
    next line. Returns key -> list of raw lines (per-line structure matters
    for MCQ keying: answer rows vs 'X is incorrect' note rows)."""
    entries = {}
    cur_q, cur_letter = None, None
    cur = None
    last_roman = {}   # F42: (q, letter) -> index into ROMAN of the last marker roman
    TOTAL_RE = re.compile(r"^\s*Total\s+\d+\s*$")

    def _roman_idx(r):
        return ROMAN.index(r.lower()) if r else None

    def _honour_qn(qn_str, has_marker_evidence):
        """F35 (LEDGER): MS content rows can BEGIN with short numerals — Mr
        workings ('12 1 16' inside a 5(a)(i) calculation), coefficient rows,
        isotope masses — and front matter carries numerals too (the 2022-01
        PMT blurb '70 countries, in 100 languages' would hijack the file).
        A leading numeral is a QUESTION-NUMBER marker when EITHER
        (a) the same row carries letter/roman marker evidence ('11 a calculate
            moles…', '5 (a) (i) …') — damaged papers (2019-06 rasterized Q10)
            legitimately skip numbers, so evidence wins over the sequence, OR
        (b) it advances the strictly ascending question sequence: question 1
            bootstraps, then next-question (+1) or a same-question re-print
            (covers numeral-only rows). A numeral-only row that skips
            ('12 1 16 atomic numbers' at cur_q=5) is content, not a marker
            (the 2022-06 2C defect: it hijacked cur_q 5->12 and left
            Q5(b)-(d) unlinkable, G5 79%)."""
        if not qn_str:
            return None
        v = int(qn_str)
        if has_marker_evidence:
            return v
        if cur_q is None:
            return v if v == 1 else None
        if v == cur_q or v == cur_q + 1:
            return v
        return None

    for ln in ms_lines:
        if TOTAL_RE.match(ln):
            continue
        mo = MS_MARKER_ONLY_RE.match(ln)
        m = MS_ROW_RE.match(ln)
        mb = MS_BARE_LETTER_RE.match(ln)
        mdm = MS_DEGRADED_MARKER_RE.match(ln)
        mg = MS_GLUED_MARKER_RE.match(ln)
        mro = MS_BARE_ROMAN_RE.match(ln)
        mhr = MS_HALF_ROMAN_RE.match(ln)
        msl = MS_SIDEBAR_LETTER_RE.match(ln)
        mdr = MS_DEEP_ROMAN_RE.match(ln)
        if mo and any(mo.groups()[:3]):
            qn, letter, roman = mo.group(1), mo.group(2), mo.group(3)
            # v0.9 (F40i): the printed MS sometimes sets the roman in caps —
            # '1 (b) (II)' for the QP's 1(b)(ii) (2025-06 2C) — the lowercase-
            # only row regex treated the row as content and appended the
            # answer to the WRONG part's block. Normalize to lowercase; the
            # QP side (L2_RE) stays lowercase-only.
            roman = roman.lower() if roman else None
            new_q = _honour_qn(qn, bool(letter or roman))
            if new_q is not None:
                cur_q = new_q
            if letter:
                cur_letter = letter
            cur = (cur_q, cur_letter, roman if roman else None)
            if roman and cur_q is not None and cur_letter:
                last_roman[(cur_q, cur_letter)] = _roman_idx(roman)
            entries.setdefault(cur, [])
        elif mdm and not (mdm.group(2) and mdm.group(4) and mdm.group(5) and mdm.group(7)):
            # F42 bare letter + bare roman ('    d   i    Impurities...') and
            # v0.12 (F50) degraded-paren variants — see MS_DEGRADED_MARKER_RE.
            # Fully-parenthesized rows skip this branch (fall through to
            # MS_ROW_RE); a rest that is ONLY a marks-column digit opens a
            # marker-only entry (the digit is layout, not answer content —
            # 3(d)(ii)'s answer cell is a printed image; the digit alone must
            # not become one)
            qn, letter, roman, rest = mdm.group(1), mdm.group(3), mdm.group(6), mdm.group(8)
            roman = roman.lower()
            new_q = _honour_qn(qn, True)
            if new_q is not None:
                cur_q = new_q
            cur_letter = letter
            cur = (cur_q, cur_letter, roman)
            if cur_q is not None:
                last_roman[(cur_q, cur_letter)] = _roman_idx(roman)
            entries.setdefault(cur, [] if re.fullmatch(r"\d{1,2}", rest.strip())
                               else [rest.strip()] if rest.strip() else [])
        elif mg:
            # F42: glued unspaced marker, e.g. '  10ai     M1 ...' or '   bi      (C5H12...'
            # v0.12 (F50): the paren-roman glued form ('    b(iv)') carries the
            # roman in the second alternative group.
            qn, letter, roman, roman_paren, rest = mg.groups()
            roman = (roman or roman_paren).lower()
            new_q = _honour_qn(qn, True) if qn else None
            if new_q is not None:
                cur_q = new_q
            # ascending-sequence gate: the glued letter must not go backwards
            # within the question (content tokens like 'an'/'it' at line start
            # can glue-match; real markers ascend)
            if cur_q is None or (cur_letter and ord(letter) < ord(cur_letter) and qn is None):
                cur = None
            else:
                cur_letter = letter
                cur = (cur_q, cur_letter, roman)
                if cur_q is not None:
                    last_roman[(cur_q, cur_letter)] = _roman_idx(roman)
                entries.setdefault(cur, [rest.strip()] if rest.strip() else [])
        elif msl and cur is not None and cur[0] is not None:
            # v0.12 (F50): rotated-margin sidebar fragment + marker row (see
            # MS_SIDEBAR_LETTER_RE). Fires only on a real table row (marks
            # digit at the tail) whose letter ADVANCES the current group; the
            # wrapped tail fragments (no tail digit) and any backwards letter
            # stay content.
            letter, rest = msl.group(1), msl.group(2)
            if ((cur[1] is None or ord(letter) > ord(cur[1]))
                    and re.search(r"\d{1,2}\s*$", ln)):
                cur_letter = letter
                cur = (cur[0], cur_letter, None)
                entries.setdefault(cur, [rest.strip()] if rest.strip() else [])
            elif cur is not None:
                entries[cur].append(ln)
        elif mb:
            # bare-letter rows must win over MS_ROW_RE (whose groups are all
            # optional and therefore match almost any line)
            qn, letter, rest = mb.groups()
            new_q = _honour_qn(qn, True)   # bare-letter rows carry letter evidence by construction
            if new_q is not None:
                cur_q = new_q
            cur_letter = letter
            roman = None
            r2 = L2_INLINE_RE.match(rest.strip())
            if r2:
                roman, rest = r2.group(1).lower(), r2.group(2)
            cur = (cur_q, cur_letter, roman)
            if roman and cur_q is not None:
                last_roman[(cur_q, cur_letter)] = _roman_idx(roman)
            entries.setdefault(cur, [rest.strip()] if rest.strip() else [])
        elif mro and cur is not None and cur[0] is not None and cur[1] is not None:
            # F42: bare roman continuation row, e.g. '        ii      2' — the
            # letter is inherited. Ascending-sequence gate: the roman must be
            # exactly the next one for this (question, letter); anything else
            # is content, not a marker.
            roman, rest = mro.group(1).lower(), mro.group(2)
            k = (cur[0], cur[1])
            expected = last_roman.get(k, -1) + 1
            if _roman_idx(roman) == expected:
                cur = (cur[0], cur[1], roman)
                last_roman[k] = expected
                entries.setdefault(cur, [] if re.fullmatch(r"\d{1,2}", rest.strip())
                                   else [rest.strip()] if rest.strip() else [])
            elif cur is not None:
                entries[cur].append(ln)
        elif mhr and cur is not None and cur[0] is not None and cur[1] is not None:
            # v0.12 (F50): half-paren bare roman continuation row ('ii)  M1 …',
            # 2020-11 1CR 3(b)(ii)) — same ascending-sequence gate as the bare
            # form above; anything not exactly the next roman stays content.
            roman, rest = mhr.group(1).lower(), mhr.group(2)
            k = (cur[0], cur[1])
            expected = last_roman.get(k, -1) + 1
            if _roman_idx(roman) == expected:
                cur = (cur[0], cur[1], roman)
                last_roman[k] = expected
                entries.setdefault(cur, [] if re.fullmatch(r"\d{1,2}", rest.strip())
                                   else [rest.strip()] if rest.strip() else [])
            elif cur is not None:
                entries[cur].append(ln)
        elif mdr and cur is not None and cur[0] is not None and cur[1] is not None:
            # F46 (v0.11): deep-indent parenthesized roman content row — the
            # 2023-11 1C MS prints '(ii)   best fit curve …' at indent 22,
            # past MS_ROW_RE's {0,20} window, so the row was absorbed as
            # content into the (i) block and 6(c)(ii)/6(d)(ii) stayed honestly
            # unmatched. Same ascending-sequence gate as the bare-roman
            # branch: the roman must be exactly the NEXT one for this
            # (question, letter); anything else stays content.
            roman, rest = mdr.group(1).lower(), mdr.group(2)
            k = (cur[0], cur[1])
            # gate on the CURRENT entry's roman when it carries one (the
            # 2023-11 '(i)' rows arrived via MS_ROW_RE, which never touches
            # last_roman — gating on last_roman alone would expect 'i' again
            # and re-absorb these rows as content)
            expected = (_roman_idx(cur[2]) + 1) if cur[2] else last_roman.get(k, -1) + 1
            if _roman_idx(roman) == expected:
                cur = (cur[0], cur[1], roman)
                last_roman[k] = expected
                entries.setdefault(cur, [] if re.fullmatch(r"\d{1,2}", rest.strip())
                                   else [rest.strip()] if rest.strip() else [])
            elif cur is not None:
                entries[cur].append(ln)
        elif m:
            qn, letter, roman, rest = m.groups()
            # F40i: same lowercase normalization as the marker-only branch —
            # the 2025-06 2C MS prints the marker-only '(II)' row and the
            # MS_ROW_RE branch must fold it too
            roman = roman.lower() if roman else None
            new_q = _honour_qn(qn, bool(letter or roman))
            if any([new_q, letter, roman]):
                if new_q is not None:
                    cur_q = new_q
                if letter:
                    cur_letter = letter
                cur = (cur_q, cur_letter, roman if roman else None)
                entries.setdefault(cur, [rest])
            elif cur is not None:
                entries[cur].append(ln)
        elif cur is not None:
            entries[cur].append(ln)
    return entries


# ---------------------------------------------------------------- v0.5: solution emission
# The reveal + Smart Mark layer: per-part solution_md (verbatim MS answer block)
# and mark_points[] (awardable points whose marks always sum to the part marks).
SOL_TAIL_MARKS_RE = re.compile(r"\s{2,}(\d{1,2})\s*$")   # marks-column digit, far right
TOTAL_ROW_RE = re.compile(r"^Total \d+$")
NOTES_COL_INDENT = 45   # answer-column content sits left of this in every observed table;
                        # the Notes column (ALLOW/ACCEPT/... + its M1/M2 cross-references)
                        # starts at col ~60+ — never confuse its M-rows for points


def build_solution(p, ms_lines, series):
    """v0.5: derive solution_md + mark_points[] from the linked MS entry.

    Verbatim doctrine: solution_md is every content line of the entry block,
    whitespace-normalized, with the marker row's trailing marks-column digit
    removed (it is layout, not answer). Nothing is added or reworded.

    mark_points[]: points are split ONLY on explicit ascending M1..Mn rows
    printed in the answer column (indent < NOTES_COL_INDENT), each worth 1,
    accepted only when n == the part's marks. Every other entry becomes ONE
    point carrying the whole block (marks = part marks). MCQ parts emit a
    single label-style point referencing the keyed choice. Fail-closed: the
    splitter can only under-split, never invent; unlinked parts emit nothing.
    Returns (solution_md, mark_points, ms_marks_digit_or_None)."""
    marks = p["marks"]
    lines = []                      # (raw indent, normalized text)
    ms_marks = None
    for ln in ms_lines:
        raw = ln.rstrip()
        if not raw.strip():
            continue
        tail = SOL_TAIL_MARKS_RE.search(raw)
        if tail and raw[:tail.start()].strip():
            if ms_marks is None:
                ms_marks = int(tail.group(1))
            raw = raw[:tail.start()].rstrip()
        text = re.sub(r"\s{2,}", " ", raw).strip()
        if not text or TOTAL_ROW_RE.match(text):
            continue
        lines.append((len(raw) - len(raw.lstrip()), text))
    if not lines:
        return None, None, None
    solution_md = "\n".join(t for _, t in lines)
    base = f"{series}-{p['part_number'].replace('(', '-').replace(')', '')}"
    pts = None
    if p["question_type"] == "multiple_choice":
        keyed = next((c for c in p.get("choices") or [] if c.get("is_correct")), None)
        if marks is not None:
            pts = [{"id": f"{base}-MP1", "marks": marks,
                    "text_md": (f"Answer {keyed['label']}: {keyed['text_md']}"
                                if keyed else solution_md)}]
    elif marks is not None:
        m_rows = [(k, m) for k, (ind, t) in enumerate(lines)
                  if ind < NOTES_COL_INDENT and (m := re.match(r"^M([1-9])\s+(\S.*)$", t))]
        nums = [int(m.group(1)) for _, m in m_rows]
        if m_rows and nums == list(range(1, len(nums) + 1)) and len(nums) == marks:
            pts = []
            for j, (k, m) in enumerate(m_rows):
                end = m_rows[j + 1][0] if j + 1 < len(m_rows) else len(lines)
                seg = [m.group(2)]
                seg += [t for ind, t in lines[k + 1:end]
                        if ind < NOTES_COL_INDENT and not re.match(r"^M[1-9]\s", t)]
                pts.append({"id": f"{base}-MP{j + 1}", "marks": 1,
                            "text_md": "\n".join(seg)})
        if pts is None:
            pts = [{"id": f"{base}-MP1", "marks": marks, "text_md": solution_md}]
    return solution_md, pts, ms_marks


# ---------------------------------------------------------------- v0.5: figure crop pass
# Turns the page-anchored crop-required stubs into real PNG crops rendered from
# the QP PDF. Detection is deterministic (vector-drawing + raster-image clusters);
# anything not provably a figure stays a stub and keeps its review-queue entry.
CROP_MIN_W, CROP_MIN_H = 40, 25          # figure-sized regions (pt)
CROP_PAD, CROP_DPI = 9.0, 150
FULL_PAGE_FRAC = 0.80                    # page-border frames cover ~100% -> rejected
ANSWER_STRIP_W, ANSWER_STRIP_H = 320, 55  # full-width ruled answer boxes are furniture
FOOTER_BAND = 80                         # pt: page-bottom band (barcode / Turn over) F18


def detect_figure_clusters(page):
    """Figure-sized regions on a QP page: vector-drawing rects (lines, curves,
    fills — apparatus diagrams, graphs, tables) plus embedded raster bboxes,
    union-merged with padding to fixpoint. Page furniture is removed BEFORE
    merging (printed page-border frames, margin decoration strips, full-height
    stripe images, full-page scans) because a frame at 79% page area survives
    any post-hoc area filter, margin stripe images sit close enough to merge
    with it, and a full-height 'DO NOT WRITE' stripe image bridges the border
    rules + answer rules + tables into one page-sized mega-cluster (F18: the
    2019-06 defect that left table pages with zero clusters). Horizontal
    ruling lines are zero-height rects — they ARE table strokes, so only
    truly zero-size artifacts are dropped here; answer-rule stacks that do
    merge are removed by the answer-strip filter. Post-merge filters: footer
    band (F18), figure minimum size, full-width ruled answer strips.
    Deterministic order."""
    pw, ph = page.rect.width, page.rect.height

    def furniture(r):
        if r.width >= 0.45 * pw and r.height >= 0.45 * ph:
            return True                      # page-border frame / full-page scan
        if r.height >= 0.5 * ph and r.width <= 60:
            return True                      # full-height margin stripe image (F18)
        if r.x1 <= 45 or r.x0 >= pw - 45 or r.y1 <= 30 or r.y0 >= ph - 30:
            return True                      # margin decorations / edge stripes
        return False

    seeds = []
    for d in page.get_drawings():
        r = fitz.Rect(d["rect"])
        if max(r.width, r.height) < 3 or furniture(r):
            continue
        seeds.append(r)
    for info in page.get_image_info():
        r = fitz.Rect(info["bbox"])
        if max(r.width, r.height) < 5 or furniture(r):
            continue
        seeds.append(r)
    if not seeds:
        return []
    page_area = abs(page.rect)
    boxes = [fitz.Rect(r.x0 - CROP_PAD, r.y0 - CROP_PAD, r.x1 + CROP_PAD, r.y1 + CROP_PAD)
             for r in seeds]
    merged = []
    for b in sorted(boxes, key=lambda r: (round(r.y0, 1), round(r.x0, 1))):
        hit_i = next((i for i, m in enumerate(merged) if m.intersects(b)), None)
        if hit_i is None:
            merged.append(fitz.Rect(b))
        else:
            merged[hit_i] = merged[hit_i] | b   # NOTE: Rect has no __ior__ — must rebind into the list
    for _ in range(10):                    # absorb merge chains to a fixpoint
        out, changed = [], False
        for b in merged:
            hit_i = next((i for i, m in enumerate(out) if m.intersects(b)), None)
            if hit_i is None:
                out.append(fitz.Rect(b))
            else:
                if not out[hit_i].contains(b):
                    out[hit_i] = out[hit_i] | b
                    changed = True
        merged = out
        if not changed:
            break
    # labelled fragments of one figure sit in a vertical stack (an 'eye' label
    # above the apparatus drawing) — merge pairs with strong x-overlap, a small
    # y-gap and real figure heights; answer-rule stacks (h <= 20) never qualify
    for _ in range(6):
        pairs = []
        for i in range(len(merged)):
            for j in range(i + 1, len(merged)):
                a_, b_ = merged[i], merged[j]
                if a_.height < 40 or b_.height < 40:
                    continue
                xov = min(a_.x1, b_.x1) - max(a_.x0, b_.x0)
                if xov < 0.4 * min(a_.width, b_.width):
                    continue
                gap = max(a_.y0, b_.y0) - min(a_.y1, b_.y1)
                if 0 <= gap <= 24:
                    pairs.append((i, j))
        if not pairs:
            break
        killed = set()
        for i, j in pairs:
            if i in killed or j in killed:
                continue
            merged[i] = merged[i] | merged[j]
            killed.add(j)
        merged = [m for k, m in enumerate(merged) if k not in killed]

    # v0.7 (F27b): paired figures — one figure printed as several drawings
    # side by side at the same height ('an atom of magnesium and an atom of
    # chlorine', the solid/liquid/gas box row). Same-row pairs (y-overlap
    # >= 60%, x-gap <= 90pt) belong together; a mention that picks either
    # half must crop the whole row (the 2024-11 6(b) defect cropped only the
    # chlorine atom of the printed pair).
    for _ in range(4):
        pairs = []
        for i in range(len(merged)):
            for j in range(i + 1, len(merged)):
                a_, b_ = merged[i], merged[j]
                if a_.height < 40 or b_.height < 40:
                    continue
                yov = min(a_.y1, b_.y1) - max(a_.y0, b_.y0)
                if yov < 0.6 * min(a_.height, b_.height):
                    continue
                gap = max(a_.x0, b_.x0) - min(a_.x1, b_.x1)
                if 0 <= gap <= 90 and (a_.width + gap + b_.width) <= 0.85 * pw:
                    pairs.append((i, j))
        if not pairs:
            break
        killed = set()
        for i, j in pairs:
            if i in killed or j in killed:
                continue
            merged[i] = merged[i] | merged[j]
            killed.add(j)
        merged = [m for k, m in enumerate(merged) if k not in killed]

    figs = []
    for m in merged:
        if abs(m) > FULL_PAGE_FRAC * page_area:
            continue
        if m.y0 >= ph - FOOTER_BAND:
            continue                         # footer band: barcode / Turn over / page number (F18)
        if m.width >= ANSWER_STRIP_W and m.height <= ANSWER_STRIP_H:
            continue
        if m.width < CROP_MIN_W or m.height < CROP_MIN_H:
            continue
        figs.append(m)
    return sorted(figs, key=lambda r: (round(r.y0), round(r.x0)))


def figure_anchor_y(page, problem_md, min_words=2):
    """Y position of the part's own text on the page (figures sit below it).
    Tries progressively shorter word prefixes because pdftotext and PyMuPDF
    disagree about spacing/punctuation. min_words raises the shortest prefix
    the search may fall back to — cross-page anchoring must use >= 4 (a
    2-word prefix like 'The student' matches unrelated lines, F25). Returns
    None = unanchorable -> review flag."""
    frag = re.sub(r"\s+", " ", problem_md).strip()
    words = frag.split()
    for n in (8, 6, 4, 3, 2):
        k = min(n, len(words))
        if k < min_words:
            break
        hits = page.search_for(" ".join(words[:k]))
        if hits:
            return hits[0].y0
    return None


REF_PREPS = {"on", "from", "in", "of", "at", "than", "against"}


def noun_anchor_y(page, problem_md, noun):
    """F20/F22/F24: anchor candidates at EVERY figure-noun phrase of the part
    text, each with a direction. 'Complete the table' / 'The diagram shows'
    instruct -> the figure sits BELOW; 'on the diagram' / 'in apparatus X'
    refer -> the figure sits ABOVE. Returns [(y, below?), ...] in document
    order of the phrases. None when the noun is absent from the page text.
    v0.9 (F40f): each occurrence first probes FORWARD context (the noun plus
    the words that FOLLOW it, sentence-bounded) before falling back to the
    legacy pre-noun window — a sentence-INITIAL noun ('The table shows ...')
    has a 1-2-word pre-context whose probe matches later lines of the same
    page, dragging the anchor BELOW the very figure it should sit above
    (the 2022-06 2C 3(c) defect: both anchors landed on the instruction
    line under the printed table)."""
    frag = re.sub(r"\s+", " ", problem_md).strip()
    occ = list(re.finditer(rf"\b{noun}s?\b", frag, re.I))
    if not occ:
        return None
    out = []
    for m in occ:
        ws = frag[:m.end()].split()[-6:]
        # direction: a sentence that OPENS with a prepositional phrase
        # ('On the grid, add ...') refers to a figure printed ABOVE; an
        # instruction sentence ('Plot the results on the grid.', 'Complete
        # the table ...') points at a figure printed BELOW (F24).
        # v0.7 (F26): a noun used as the SOURCE of data — 'from the table',
        # 'from the graph' — refers to a figure printed ABOVE even inside a
        # forward instruction sentence (the 2020-01 9(d)(i) defect where the
        # 'table' of 'Plot the data values from the table' was anchored at
        # the plotting grid below it).
        # v0.9 (F40b): two more source-reference shapes point UP —
        #   '... of the <noun>'  ('Explain the shape of the graph': the graph
        #        is the object being read, 2022-01 2C 6(a)(iii));
        #   'the data in the <noun>' / 'the values in the <noun>' (the noun
        #        is a data source, not a writing surface — 'Use the values
        #        in the table'; 'Complete the table' / 'Plot the results on
        #        the grid' stay BELOW).
        sentence_start = max(frag.rfind(".", 0, m.start()), frag.rfind("!", 0, m.start())) + 1
        head = frag[sentence_start:m.start()].strip()
        below = True
        if head:
            hw = head.split()
            if len(hw) <= 2 and hw[0].lower() in REF_PREPS:
                below = False
            elif hw[-1].lower() == "from" or (
                    len(hw) >= 2 and hw[-2].lower() == "from"
                    and hw[-1].lower() in ("the", "this", "that", "his", "its", "your", "each")):
                below = False
            elif (len(hw) >= 2 and hw[-2].lower() == "of"
                  and hw[-1].lower() in ("the", "this", "that", "his", "its", "each")):
                below = False
            elif (len(hw) >= 3 and hw[-3].lower() in ("data", "values")
                  and hw[-2].lower() in ("in", "on", "from")
                  and hw[-1].lower() in ("the", "this", "that", "his", "its", "each")):
                below = False
            elif (len(hw) >= 3 and hw[-2].lower() in ("on", "in", "at")
                  and hw[-1].lower() in ("the", "this", "that", "his", "its", "each")
                  and re.match(r"^\s*\(?\s*(?:[a-z]+\)\s*)?(?:label|mark|annotate|name)\b", head, re.I)):
                below = False   # 'Label the particles on the diagram' — the
                                # figure being marked sits ABOVE (2025-06 1(a);
                                # 'Plot the results on the grid' stays below —
                                # the verb gates the direction)
        # F40f: forward-context probe first — the noun plus up to 4 words
        # that follow it INSIDE its sentence. A sentence-initial noun gets a
        # specific probe ('table shows the electronic configurations')
        # instead of the ambiguous 1-word pre-context ('the table').
        anchored = False
        sent_end = len(frag)
        for stop in (".", "!", "?"):
            se = frag.find(stop, m.end())
            if se != -1:
                sent_end = min(sent_end, se)
        post = re.sub(r"[^A-Za-z0-9\s]", " ", frag[m.end():sent_end]).split()[:4]
        if post:
            base = re.sub(r"[^A-Za-z0-9\s]", " ", m.group(0)).strip()
            for n in (len(post), 3, 2, 1):
                probe = " ".join([base] + post[:n])
                hits = page.search_for(probe)
                if hits:
                    out.append((hits[0].y1 if below else hits[0].y0, below))
                    anchored = True
                    break
        if not anchored:
            for n in (len(ws), 4, 3):
                if n < 2:
                    break
                hits = page.search_for(" ".join(ws[-n:]))
                if hits:
                    out.append((hits[-1].y1 if below else hits[-1].y0, below))
                    break
    return out or None


PART_MARKER_RE = re.compile(r"^\(?[a-z]+\)?\s+\([ivx]+\)|^\([ivx]+\)|^\([a-z]+\)\s", re.I)
MARK_TAG_RE = re.compile(r"^\(\d+\)$")


def expand_with_labels(page, rect, exclude_frags=()):
    """Union the cluster with nearby text blocks that overlap a fixed +16pt
    ring around it — graph axis labels and chart annotations are TEXT sitting
    just outside the vector strokes, and belong to the figure. Only blocks
    overlapping the ring are absorbed (distant paragraph text is not).
    F22: blocks that sit ENTIRELY outside the pre-expansion rect and carry
    foreign text — the part's own question line, a neighbouring part's marker
    line, a bare mark tag — must never be absorbed: they are layout, not
    labels (the 2025-11 4(c)(i) defect where the crop swallowed '(i) Explain
    the mistake in the student's diagram.'). Axis labels under a graph don't
    match any exclusion and stay inside the crop."""
    ring = fitz.Rect(rect.x0 - 16, rect.y0 - 16, rect.x1 + 16, rect.y1 + 16) & page.rect
    inner = fitz.Rect(rect.x0 + 2, rect.y0 + 2, rect.x1 - 2, rect.y1 - 2)
    contain = fitz.Rect(rect.x0 - 66, rect.y0 - 66, rect.x1 + 66, rect.y1 + 66) & page.rect
    out = fitz.Rect(rect)
    frags = [norm(f)[:40] for f in exclude_frags if f]
    for b in page.get_text("blocks"):
        tb = fitz.Rect(b[:4])
        if tb.is_empty or not ring.intersects(tb):
            continue
        if not contain.contains(tb):
            continue             # a block reaching far beyond the figure is page
                                 # text, not a label (F22: whole-page text blocks)
        if inner.intersects(tb):
            out |= tb
            continue
        txt = norm(b[4] if len(b) > 4 else "")[:80]
        foreign = (MARK_TAG_RE.match(txt) or PART_MARKER_RE.match(txt)
                   or re.search(r"total for (question|paper)", txt)
                   or DOTRUN_RE.search(txt)          # printed answer-line dots
                   or any(f and f in txt for f in frags))
        if not foreign:
            out |= tb
    # v0.7 (F27): callout labels — short unpunctuated text blocks sitting at
    # the side of an apparatus drawing ('sodium thiosulfate solution',
    # 'paper with cross drawn on it', 'Magnesium'). They start near the
    # figure but extend far beyond the +-66pt contain ring, so the F22 ring
    # pass rejects them and the crop clips the label mid-word (the 2020-11
    # 7(b) defect). A side block is absorbed when it is short, unpunctuated,
    # vertically inside the figure span and not foreign layout text.
    for b in page.get_text("blocks"):
        tb = fitz.Rect(b[:4])
        if tb.is_empty or tb.height > 34:
            continue
        if not (rect.y0 - 6 <= (tb.y0 + tb.y1) / 2 <= rect.y1 + 30):
            continue
        side_gap = max(rect.x0 - tb.x1, tb.x0 - rect.x1)
        if side_gap > 130:
            continue
        txt = norm(b[4] if len(b) > 4 else "")[:80]
        if not txt or txt.endswith(".") or len(txt.split()) > 8:
            continue               # prose, never a label
        foreign = (MARK_TAG_RE.match(txt) or PART_MARKER_RE.match(txt)
                   or re.search(r"total for (question|paper)", txt)
                   or DOTRUN_RE.search(txt)
                   or any(f and f in txt for f in frags))
        if not foreign:
            out |= tb
    # v0.7 (F27c): never slice a text block — a short block the final rect
    # cuts through renders as clipped mid-word text (the 2020-11 7(b) top
    # line). Absorb it whole when it is mostly inside and not layout text.
    for b in page.get_text("blocks"):
        tb = fitz.Rect(b[:4])
        if tb.is_empty or tb.height > 30 or out.contains(tb):
            continue
        inter = tb & out
        if inter.is_empty or abs(inter) < 0.4 * abs(tb):
            continue
        txt = norm(b[4] if len(b) > 4 else "")[:80]
        foreign = (MARK_TAG_RE.match(txt) or PART_MARKER_RE.match(txt)
                   or re.search(r"total for (question|paper)", txt)
                   or DOTRUN_RE.search(txt)
                   or any(f and f in txt for f in frags))
        if not foreign:
            out |= tb
    return out


def text_coverage(page, rect):
    """Fraction of the rect's area overlapped by text blocks — high values mean
    the region is mostly text (mis-detected cluster) and the crop needs eyes."""
    tot = 0.0
    for b in page.get_text("blocks"):
        inter = fitz.Rect(b[:4]) & rect
        if not inter.is_empty:
            tot += abs(inter)
    return round(min(1.0, tot / max(abs(rect), 1.0)), 3)


# ---------------------------------------------------- v0.7.1: drawn scaffolds (F32)
# 'Complete/Draw a dot-and-cross diagram' prompts fall to rule 0's honest stub
# because the printed scaffold is usually TEXT-ONLY (bare element letters in a
# blank answer area: 'H C Cl H H', 'N N', 'H O O H'). But some papers print the
# scaffold as a real DRAWING — overlapping electron-shell circles around the
# element letters (2024-11 6(c)(i): an N circle + three H circles). Rule 0 must
# not stub those: a substantial non-furniture vector drawing at/below the part's
# instruction line means the scaffold is drawn and the normal anchoring path
# must crop it. Thin rules (answer lines, separators) and page furniture never
# qualify; a blank answer area yields False, so every verified text-only stub
# stays stubbed.
def drawn_scaffold_below(page, ay, min_dim=20.0):
    if ay is None:
        return False
    pw, ph = page.rect.width, page.rect.height
    for d in page.get_drawings():
        r = fitz.Rect(d["rect"])
        if min(r.width, r.height) < min_dim:
            continue                      # thin rule / dotted answer line
        if r.width >= 0.45 * pw and r.height >= 0.45 * ph:
            continue                      # page-border frame / full-page scan
        if r.height >= 0.5 * ph and r.width <= 60:
            continue                      # full-height margin stripe (F18)
        if r.x1 <= 45 or r.x0 >= pw - 45 or r.y1 <= 30 or r.y0 >= ph - 30:
            continue                      # margin decorations / edge stripes
        if r.y0 >= ay - 10:
            return True
    return False


# ---------------------------------------------------- v0.6: mention semantics (F19)
# A figure noun in the part text is only a figure REFERENCE when at least one
# occurrence is not itself part of a non-figural phrase. "Periodic Table",
# "Draw a dot-and-cross diagram", "Sketch a labelled diagram", "use a diagram",
# "a piece of apparatus" and "set up the apparatus" describe tasks or common
# nouns, never a printed figure. Verbatim problem_md is untouched — this only
# gates asset creation, so spurious crop-required stubs never enter the queue.
MENTION_SUPPRESS_RE = {
    "table": [re.compile(r"periodic\s+table$", re.I)],
    "diagram": [re.compile(r"(?:use|draw|sketch)\s+(?:a\s+)?(?:labelled\s+)?(?:dot(?:-| )and( |-)cross\s+)?diagram$", re.I)],
    "apparatus": [re.compile(r"(?:piece\s+of|set\s+up\s+the)\s+apparatus$", re.I)],
}
MENTION_NOUNS = ("table", "diagram", "grid", "graph", "apparatus", "boxes")


def figure_mentions(problem_md):
    """Nouns of problem_md that refer to a printed figure (F19). A noun is
    suppressed only when EVERY occurrence sits inside a non-figural phrase.
    Scaffold exception: 'Draw a dot-and-cross diagram' with printed element
    tokens after it ('H C Cl H H', 'N N') refers to a real printed scaffold —
    the mention (and its stub) stays.
    v0.9 (F40g): an occurrence immediately followed by 'in your answer'
    describes something the STUDENT provides ('Include suitable apparatus in
    your answer') — never a printed figure."""
    scaffold_re = re.compile(r"(?:\b(?:[HCNOF]|Cl|Br)\b[\s,]*){2,}")
    student_answer_re = re.compile(r"\s+in\s+your\s+answer\b", re.I)
    out = []
    for noun in MENTION_NOUNS:
        occ = list(re.finditer(rf"\b{noun}\b", problem_md, re.I))
        if not occ:
            continue
        ok = False
        for m in occ:
            head = problem_md[:m.end()]
            if any(p.search(head) for p in MENTION_SUPPRESS_RE.get(norm(noun), [])):
                continue
            if (student_answer_re.match(problem_md[m.end():])
                    and not re.search(r"\b(?:the|this|that)\s+$", problem_md[:m.start()], re.I)):
                # F40g: '<noun> in your answer' is student-provided ('include
                # suitable apparatus in your answer') — but a DEFINITE
                # occurrence ('use information from the table in your answer')
                # refers to a printed figure and must survive (the 2022-06 1C
                # 10(c)(ii) regression this guard caused in the first draft).
                continue
            ok = True
            break
        if not ok and noun == "diagram" and any(scaffold_re.search(problem_md[m.end():]) for m in occ):
            ok = True
        if ok:
            out.append(noun)
    return sorted(set(out))


# ---------------------------------------------------- v0.6: figure anaphora (F20)
# Backward references must RESOLVE to an already-rendered figure, never
# re-anchor to whatever drawing happens to sit below the sentence.
BACKREF_RE = re.compile(r"in part \(([a-z])\)", re.I)
NUMBERED_NOUN_RE = re.compile(r"\b(?:grid|table)\s+\d+", re.I)
# forward-introducing verbs: the figure the noun refers to is printed BELOW
# this sentence (the part's own page region) — own-page anchoring is correct.
FORWARD_RE = re.compile(r"^\s*(?:\(?[a-z]+\))?\s*(?:plot|draw|complete|add|label|sketch)\b", re.I)
# an in-text introduction ('The diagram shows ...', 'uses this apparatus')
# means the part itself introduces the figure — own-page anchoring, even
# though the sentence opens with a noun, not a verb (F20: 2019-06 9(b)).
INTRO_RE = re.compile(
    r"\b(?:the\s+|this\s+)?(?:table|diagram|grid|graph|apparatus|boxes)s?\s*\d?\s*"
    r"(?:shows?|gives?|represents?|lists?|displays?|is)\b"
    r"|\buses?\s+this\s+(?:table|diagram|grid|graph|apparatus|boxes)\b", re.I)
# v0.7 (F26): left-context guard for INTRO_RE — 'the syringe in the diagram
# shows' references the stem's figure instead of introducing one
INTRO_CONTEXT_RE = re.compile(
    r"\b(?:in|on|from|of|at|than|against)\s+(?:the|this|that|his|its|each)\s+$", re.I)


def resolve_first(problem_md, noun=None):
    """True when the part must RESOLVE an existing figure before any own-page
    anchoring: an explicit 'in part (x)' back-ref, a numbered figure
    ('grid 1', 'table 2'), or a backward reference ('Use the graph to...')
    with no introduction phrase. Forward-introducing verbs AND in-text
    introductions ('The diagram shows ...') keep the own-page-below anchor.
    v0.7 (F26): an intro noun preceded by a possessive preposition — 'the
    syringe in the diagram shows ...' — is a REFERENCE to a figure the stem
    introduced, not a fresh introduction (the 2022-06 4(b) defect where the
    'diagram' mention anchored at Table 1 below it)."""
    md = problem_md or ""
    if BACKREF_RE.search(md) or NUMBERED_NOUN_RE.search(md):
        return True
    if FORWARD_RE.match(md):
        return False
    if noun:
        for m in INTRO_RE.finditer(md):
            if noun not in m.group(0).lower():
                continue
            if not INTRO_CONTEXT_RE.search(md[:m.start()]):
                return False
    return True


# ---------------------------------------------------------------- main
def main():
    import argparse, copy
    ap = argparse.ArgumentParser(description="ADR-037 official-paper question extractor")
    ap.add_argument("--series", default="2020-11",
                    help="paper series folder, e.g. 2020-11 (baseline), 2019-06, 2020-01, 2021-06, 2022-06, 2024-06")
    ap.add_argument("--paper", default="1C",
                    help="paper variant code (F34): 1C default; 2C since v0.8; 4MB1 01/02/01R/02R since v0.16 (F64)")
    ap.add_argument("--course", default="igcse-chemistry-19", choices=sorted(COURSES),
                    help="course registry entry (F64): igcse-chemistry-19 default; igcse-maths-b-16 since v0.16")
    args = ap.parse_args()
    series = args.series
    paper = args.paper
    course = args.course
    cfg = COURSES[course]
    # F64: fail-closed paper validation against the course registry (argparse
    # cannot do per-course choices on a single --paper argument)
    if paper not in cfg["paper_totals"]:
        ap.error(f"paper {paper!r} is not a registered variant of course {course!r} "
                 f"(registered: {sorted(cfg['paper_totals'])})")
    # F64: rebind the course-scoped globals BEFORE any path/regex use
    global OUTROOT, COURSE_PREFIX, FOOTER_RE, PAPER_TOTAL, SPEC_RESOLUTION
    OUTROOT = RES_DIR / "Official-ExamQuestion" / course
    COURSE_PREFIX = cfg["paper_prefix"]
    FOOTER_RE = re.compile(cfg["footer_re"])
    if cfg["spec_resolution"] is False:
        SPEC_RESOLUTION = None          # no registry for this course (G6 documented gap)
    elif cfg["spec_resolution"] is not None:
        SPEC_RESOLUTION = Path(cfg["spec_resolution"])
    # else: keep the module-level resolution chain (chemistry default)
    P = paths_for(series, paper)
    global QP_PDF, MS_PDF, QP_TXT, MS_TXT, MANIFEST, OUT
    QP_PDF, MS_PDF = P["qp_pdf"], P["ms_pdf"]
    QP_TXT, MS_TXT = P["qp_txt"], P["ms_txt"]
    MANIFEST, OUT = P["manifest"], P["out"]
    PAPER_TOTAL = cfg["paper_totals"][paper]
    eq = cfg["expect_questions"] if cfg["expect_questions"] is not None else EXPECT_QUESTIONS
    expect_q = eq[paper].get(series)

    report = {"schema": "syllabai.official-paper-questions.validation/0.2",
              "generated_utc": now_iso(), "series": series, "paper": paper, "gates": [],
              "negative_controls": [], "review_queue": []}

    # ---- G0 identity -------------------------------------------------------
    manifest = yaml.safe_load(MANIFEST.read_text())
    qp_sha, ms_sha = sha256(QP_PDF), sha256(MS_PDF)
    mat = {m["type"]: m for m in manifest["materials"]}
    sha_ok = (qp_sha == mat["question-paper"]["sha256"] and
              ms_sha == mat["mark-scheme"]["sha256"])
    # F34: the staged manifest must claim the SAME variant we were asked to convert
    # (a 2C run over 1CR bytes would otherwise sail through the sha checks).
    manifest_variant = manifest.get("paper", {}).get("paper_number_variant")
    variant_ok = (manifest_variant == paper)
    identity_ok = sha_ok and variant_ok
    paper_id = manifest["paper_id"]
    report["gates"].append({
        "gate": "G0-identity", "status": "PASS" if identity_ok else "FAIL",
        "summary": f"paper_id={paper_id}; series={manifest['series']['normalized']}; "
                   f"printed={manifest['series'].get('printed', 'n/a (manifest schema v2 omits it)')!r}; sha256 qp/ms match manifest: {sha_ok}; "
                   f"manifest variant {manifest_variant!r} == requested {paper!r}: {variant_ok}",
        "details": {"qp_sha256": qp_sha, "ms_sha256": ms_sha,
                    "registry_paper_id": paper_id}})
    if not identity_ok:
        print("G0 FAIL — aborting (fail-closed)"); json.dump(report, sys.stdout, indent=1); return 1

    # ---- v0.10 (F41): OCR source layer for image-only pages -----------------
    # A rasterized archive page carries no text layer (2019-06: 144-dpi scan,
    # 8 image-only pages). When a prepared OCR page layer exists for such a
    # page (UPLOAD/ocr/<series>-<paper>/qp-pNN.txt + ocr-pages.json manifest),
    # its text IS the page's source layer: the staged qp.txt carries it
    # (form-feed splice, prepared by scripts/prep_ocr_layer_2019.py) and
    # page_norm below splices it so figure mentions anchor with page
    # attribution. Fail-closed: every manifest sha256 must match its staged
    # file or the run aborts; pages listed here are excluded from the G1
    # image-only defect attribution (their content is recovered, not lost).
    ocr_pages = []
    if P["ocr_index"].exists():
        ocr_manifest = json.loads(P["ocr_index"].read_text())
        if ocr_manifest.get("source_pdf_sha256") != sha256(QP_PDF):
            print("OCR layer manifest does not pin this QP PDF — aborting (fail-closed)")
            report["gates"].append({"gate": "G0-identity", "status": "FAIL",
                                    "summary": "ocr layer source_pdf_sha256 mismatch",
                                    "details": {}})
            json.dump(report, sys.stdout, indent=1); return 1
        for e in ocr_manifest["pages"]:
            f = P["ocr_index"].parent / f"qp-p{e['page']:02d}.txt"
            if not f.exists() or sha256(f) != e["sha256"]:
                print(f"OCR layer sha256 mismatch for page {e['page']} — aborting (fail-closed)")
                report["gates"].append({"gate": "G0-identity", "status": "FAIL",
                                        "summary": f"ocr layer sha256 mismatch p{e['page']}",
                                        "details": {}})
                json.dump(report, sys.stdout, indent=1); return 1
            ocr_pages.append(e)
    report["ocr_pages"] = ocr_pages

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
        if not seg["group_order"] and printed_total:
            # F65 (v0.16.0, igcse-maths-b-16 tranche-1): the maths-B QP prints
            # single-part questions with NO (a)/(b) markers — the marks appear
            # as '(N)' after the final stem line (2025-11 Q5 '(6)', Q10 '(7)',
            # Q12 '(6)'). The whole region IS one part carrying the printed
            # total. The MS block union law (linkage loop) links it. Generic
            # layout law, not per-series: chemistry questions carry markers
            # corpus-wide, so this branch is unreachable on the chemistry
            # corpus (parity re-run proved byte-identical structure+marks).
            p = finalize_part(seg["stem_lines"])
            questions_parts.append({
                "part_number": f"{qnum}",
                "group": None, "roman": None,
                "group_stem_md": None, "option_list": None,
                "marks": p["marks"] if p["marks"] is not None else printed_total,
                "question_type": "multiple_choice" if p["choices"] else "structured",
                "problem_md": p["problem_md"], "choices": p["choices"],
                "source_norm": p["source_norm"],
                "implicit_single_part": True,
            })
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
        # lives inside this region (their footer was dropped by the archive PDF).
        # FIRST match, not last (F49): the true question start is the region's
        # earliest "<N> <alpha>" line — lines BEFORE it are page furniture only
        # (bare page numbers etc. are already stripped), while digit-leading
        # SOURCE lines inside the question body (an isotope column '3  Li', an
        # equation '2 NaOH ...') can false-match QSTART_RE and, with cur[-1],
        # truncated 2023-06 1CR Q3 at its isotope label: the whole (a) group
        # (4 marks, incl. three MCQs) vanished and (b)(i)/(ii) landed in the
        # virtual roman group as 3(i)/3(ii).
        pieces = []
        for m in missing:
            ms_ = [i for i, ln in enumerate(region)
                   if QSTART_RE.match(ln) and int(QSTART_RE.match(ln).group(1)) == m]
            if ms_:
                pieces.append((m, ms_[0], None))
        cur = [i for i, ln in enumerate(region)
               if QSTART_RE.match(ln) and int(QSTART_RE.match(ln).group(1)) == qnum]
        pieces.append((qnum, cur[0] if cur else 0, qtotal))
        pieces.sort(key=lambda t: t[1])
        for k, (qn, st, pt) in enumerate(pieces):
            end = pieces[k + 1][1] if k + 1 < len(pieces) else len(region)
            emit_question(qn, pt, region[st:end])
    doc_questions.sort(key=lambda q: q["question_number"])

    # ---- MS linkage + MCQ keys ---------------------------------------------
    ms_entries = parse_ms(clean_lines(MS_TXT.read_text(errors="replace")))
    # ---- v0.8.1 (F37): human-adjudicated MCQ keys, applied pre-emission -----
    # The printed Jan 2020 MS itself misplaces the Q7(a) answer rows: (ii)'s
    # answer block prints under (iii) and a stray (i) rebuttal prints under
    # (ii), so positional linkage cannot key those parts (honest refusal, F6).
    # MCQ-KEYS.json carries the eyeballed key + the corrected verbatim MS rows
    # (evidence: rendered MS page). The override lands BEFORE build_solution so
    # solution_md, mark_points[] and choices[].is_correct all derive from the
    # adjudicated block — never from the mis-linked rows.
    mcq_keys_path = RES_DIR / "Official-ExamQuestion" / "MCQ-KEYS.json"
    mcq_key_overrides = {}
    if mcq_keys_path.exists():
        for e in json.loads(mcq_keys_path.read_text()).get("entries", []):
            # wave-22: paper-scoped keys. The F37 entries predate the 2C/2CR
            # papers and carry no paper field — they stay series-scoped (paper
            # None matches any paper, and 7(a)(i)-(iii) exist only in 1C). New
            # entries SHOULD carry "paper" so same-part MCQs across 1C/2C/1CR/2CR
            # cannot cross-contaminate.
            mcq_key_overrides[(e["series"], e.get("paper"), e["part"])] = e
    mcq_keys_applied = []
    # v0.11 (F47): manual MS-linkage ledger — the same human-adjudication
    # doctrine as MCQ-KEYS.json, for STRUCTURED parts whose printed MS answer
    # is not machine-linkable text. The 2019-06 3(d)(ii) answer cell is a
    # printed image (bordered Property table with ticks): the pipeline
    # refused to fabricate text for it (F42/C52 honest refusal), so the
    # answer of record is the eyeballed verbatim transcription of that image,
    # decided from the rendered MS page — never model guessing. Fail-closed:
    # an override applies ONLY when positional linkage found nothing for the
    # part, and only for non-MCQ parts (MCQ adjudication has its own ledger).
    ms_link_overrides = {}
    ms_link_overrides_path = RES_DIR / "Official-ExamQuestion" / "MS-LINK-OVERRIDES.json"
    if ms_link_overrides_path.exists():
        for e in json.loads(ms_link_overrides_path.read_text()).get("entries", []):
            ms_link_overrides[(e["series"], e["paper"], e["part"])] = e
    ms_link_applied = []
    for q in doc_questions:
        for p in q["parts"]:
            key = (q["question_number"], p["group"], p["roman"])
            lines = ms_entries.get(key, [])
            if not lines and p["group"] is None and p["roman"] is None \
                    and len(q["parts"]) == 1 and p.get("implicit_single_part"):
                # F65: single-part question MS union. The QP prints no sub-part
                # markers, so parse_ms files the answer rows under
                # content-fragment letter keys (a 'b2 − 4ac' fragment keys as
                # 'b', a cosine-rule bracket as 'c', an '(n − 9)(n − 10)' row
                # as 'd' — verified on 2025-11 Q5/Q10/Q12). The question has
                # exactly ONE part, so EVERY parsed block for this question is
                # its answer: concatenate in file order. Fail-closed: only
                # fires for implicit single parts (multi-part questions keep
                # the exact-key laws; a spurious union can never fire there).
                qkeys = [k for k in ms_entries if k[0] == q["question_number"]]
                if qkeys:
                    lines = [ln for k in qkeys for ln in ms_entries[k]]
            if not lines and p["roman"] is not None and p["group"] is None:
                # v0.10 (F42): the QP prints a bare question-level roman
                # (2019-06 11(iii) — the paper itself omits the '(b)' after
                # '(b)(i)/(ii)'), while the MS nests the row under a letter.
                # Fail-closed: use the (q, L, roman) entry only when EXACTLY
                # ONE letter in the question owns that roman.
                cands = [k for k in ms_entries
                         if k[0] == q["question_number"] and k[2] == p["roman"]
                         and k[1] is not None and ms_entries[k]]
                if len(cands) == 1:
                    lines = ms_entries[cands[0]]
            if not lines and p["roman"] is None and p["group"]:
                # v0.9 (F40h): the printed MS sometimes sub-numbers a part the
                # QP leaves undivided — Jan 2021 2C prints '1 (b) (i)' for the
                # QP's 1(b). When this question's letter-group has exactly ONE
                # part (this one), the sub-numbered MS block can only belong
                # to it. Fail-closed: the block's trailing marks digit must
                # equal the part's marks.
                sibs = [pp for pp in q["parts"] if pp["group"] == p["group"]]
                cand = ms_entries.get((q["question_number"], p["group"], "i"), [])
                if len(sibs) == 1 and cand:
                    # the marks digit sits in the right-hand column: a bare
                    # trailing number on a content line (build_solution reads
                    # the same column); the swallowed next-table header rows
                    # carry none, so a match is strong evidence
                    trail_marks = {int(m.group(1)) for ln in cand
                                   for m in [re.search(r"\s(\d{1,2})\s*$", ln)] if m}
                    if p["marks"] in trail_marks:
                        lines = cand
            mk = (mcq_key_overrides.get((series, paper, p["part_number"]))
                  or mcq_key_overrides.get((series, None, p["part_number"])))
            if mk and p["question_type"] == "multiple_choice":
                lines = list(mk["ms_lines"])
                p["answer_key_source"] = "mcq-keys-ledger"
                # wave-22: paper-scoped application marker (the 1C-era reports
                # carry the legacy series-only form; the C31 checker accepts both)
                mcq_keys_applied.append(f"{series}:{paper}/{p['part_number']}")
            mlo = ms_link_overrides.get((series, paper, p["part_number"]))
            if mlo and p["question_type"] != "multiple_choice" and not lines:
                lines = list(mlo["ms_lines"])
                p["answer_key_source"] = "ms-link-overrides-ledger"
                ms_link_applied.append(f"{series}:{paper}/{p['part_number']}")
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
                    # F36: 2C MS entries often open with a sentence —
                    # 'The only correct answer is D as francium is…'. The F12
                    # pattern above misses that word order, and F14's
                    # elimination keying cannot corroborate (no '<L> <text>'
                    # answer rows exist in sentence-style entries), so the key
                    # was refused. Sentence positives are labels-only evidence
                    # and stay subject to the single-distinct-positive rule.
                    pos_sent = re.search(
                        r"(?<![A-Za-z])(?:the\s+)?(?:only\s+)?correct\s+answer\s+is\s+([A-E])\b(?!\s+not\b)", s)
                    chosen = (pos or pos_sent)
                    if chosen and chosen.group(1) in labels:
                        positives.append(chosen.group(1))
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
                # v0.8.1 (F37): the adjudicated key is authoritative and lands
                # LAST — a stale heuristic result can never outrank it, and a
                # key outside the printed labels fails closed to unkeyed (G3).
                if mk is not None:
                    lab = mk["key"] if mk["key"] in labels else None
                if lab:
                    for c in p["choices"]:
                        c["is_correct"] = (c["label"] == lab)
            # v0.5 solution emission (reveal + Smart Mark): verbatim MS block +
            # awardable points; unlinked parts emit nothing (fields stay None)
            p["solution_md"], p["mark_points"], p["_ms_marks"] = build_solution(p, lines, series)

    # ---- page anchoring + assets -------------------------------------------
    pdf = fitz.open(QP_PDF)
    page_norm = [norm(normalize_pua(pg.get_text())) for pg in pdf]   # F48: same mapping both sides
    # v0.10 (F41): OCR-covered pages contribute their prepared text to the
    # page-normalized index, so mentions on recovered pages anchor with real
    # page attribution.
    for e in ocr_pages:
        t = (P["ocr_index"].parent / f"qp-p{e['page']:02d}.txt").read_text()
        if e["page"] - 1 < len(page_norm):
            page_norm[e["page"] - 1] = norm(t)
    # source-defect census: rasterized pages carry no text layer (seen in 2019-06:
    # 8 image-only pages; Q7 lost entirely, Q1/Q11/Q12/Q13/Q15 partly)
    IMG_ONLY_CHARS = 40
    image_only_pages = [i + 1 for i, pg in enumerate(pdf) if len(pg.get_text().strip()) < IMG_ONLY_CHARS]
    ocr_covered = {e["page"] for e in ocr_pages}   # F41: recovered, not lost
    footer_page = {}
    for i, pg in enumerate(pdf):
        t = pg.get_text()
        for m in FOOTER_RE.finditer(t):
            footer_page.setdefault(int(m.group(1)), i + 1)
    # only content pages matter for defect attribution (covers are routinely rasterized);
    # allow up to 3 pages before the first footer (a question's first page precedes its footer)
    first_q_page = min(footer_page.values()) if footer_page else 1
    content_img_pages = [p for p in image_only_pages if p >= max(3, first_q_page - 3)
                         and p not in ocr_covered]
    MENTION_RE = re.compile(r"\b(table|diagram|grid|graph|apparatus|boxes)\b", re.I)
    for q in doc_questions:
        for p in q["parts"]:
            # progressive-length anchoring: a 38-char fragment can collide with
            # an identical sibling wording (2019-06 Q9(b) 'The diagram shows the
            # displayed formula ...' also opens Q8(c) — the collision anchored
            # Q9(b) to page 13 and its figure on page 14 was never found). The
            # shortest fragment that matches EXACTLY ONE page wins (F18b).
            # v0.9 (F40e): PUA furniture glyphs glued to short part text
            # ('Explain the shape of the graph. \uf0a2\uf0a2...') poison every
            # probe — the page text never contains them, so a short part lost
            # its page anchor entirely (2022-01 2C 6(a)(iii)). Strip the PUA
            # range before probing; matching only feeds page attribution, the
            # verbatim problem_md is untouched.
            frag = norm(re.sub(r"[\uf000-\ufbff]+", " ",
                        re.sub(r"^[()a-ziv ]+", "", p["problem_md"])))[:110]
            src_page = None
            for n in (38, 60, 90, 110):
                probe = frag[:n]
                if not probe:
                    break
                pages = [i + 1 for i, t in enumerate(page_norm) if probe in t]
                if len(pages) == 1:
                    src_page = pages[0]
                    break
                if pages and src_page is None:
                    src_page = pages[0]
                if len(probe) < n:        # fragment exhausted (short problem_md)
                    break
            p["source_page"] = src_page
            mentions = figure_mentions(p["problem_md"])       # F19-suppressed
            p["assets"] = [{"id": f"asset_{p['part_number'].replace('(', '_').replace(')', '')}_{k}",
                            "kind": "crop-required", "mention": k,
                            "source": "qp.pdf", "page": p["source_page"], "review": True}
                           for k in mentions]

    # ---- v0.7 figure crop pass ----------------------------------------------
    # Resolution order per mention (fail-closed; anything unresolved stays a
    # crop-required stub in the review queue):
    #   1. explicit back-ref 'on the grid in part (a)'  -> shared ref (F20)
    #   2. numbered figures ('table 1', 'grid 2') anchor on their OWN page
    #      first — the numbered figure prints in the question's region
    #      (F25: 2022-06 4(b) 'table 1' was dragged to the stem apparatus
    #      on the previous page)
    #   3. backward reference ('Use the graph to...', no intro phrase):
    #      3a. stem / group-stem figure intro 'The graph shows ...' -> one
    #          lazy stem crop shared by every referencing part (F21)
    #      3b. sibling part crop for the same figure class -> shared ref (F20)
    #      3c. own-page rescue, both noun-phrase directions, always
    #          review-flagged (F25 reorder: 'the changes listed in the table'
    #          with the table right below on the SAME page must beat the
    #          adjacent-page search that grabbed the printed Periodic Table)
    #      3d. adjacent page anchored on a stem sentence that names the noun
    #          — the 2-word fallback anchor and the single-unclaimed-cluster
    #          rule are GONE (F25: they matched unrelated lines and picked
    #          reference pages)
    #   4. forward introduction ('Plot ... on the grid', 'The diagram shows'):
    #      4a. own-page cluster in the noun phrase's own direction (F26:
    #          'from the table' is a backward reference even inside a
    #          forward instruction sentence)
    #      4b. sibling share   4c. stem figure   4d. adjacent (strong anchor)
    #   5. question-scoped plot fallback: exactly one low-text unclaimed
    #      cluster on the part's page +-1 (F25b: 2022-06 6(c)(i) grid)
    #   6. unresolved -> crop-required stub (honest, review queue)
    ASSETS_DIR = OUT / "assets"
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    # v0.7 (F29): human crop-review verdicts — the durable eyeball record.
    # An 'accepted' verdict clears the review flag on re-runs; anything not
    # in the ledger keeps whatever confidence the converter computed.
    # v0.8.2 (F39): ledger keying follows the documented convention (AGENTS.md,
    # C22) — 1C keeps the legacy bare '<series>' home, other variants use
    # '<series>:<paper>' so verdict homes never collide across papers. The
    # F34 wave documented the convention but the load site kept reading the
    # bare series key, so non-1C verdicts were silently ignored.
    _CROP_REVIEW_PATH = RES_DIR / "Official-ExamQuestion" / "CROP-REVIEW.json"
    crop_reviews = {}
    if _CROP_REVIEW_PATH.exists():
        _review_doc = json.loads(_CROP_REVIEW_PATH.read_text()).get("reviews", {})
        crop_reviews = _review_doc.get(series, {}) if paper == "1C" else _review_doc.get(f"{series}:{paper}", {})
    page_clusters, page_rasters = {}, {}
    claimed = {}                       # page -> {cluster_index: question_number} (F24)
    claimed_asset = {}                 # page -> {cluster_index: owning asset dict} (F28)
    crop_stats = {"crops": 0, "pending": 0, "shared": 0}
    stem_assets = {}                     # (qnum, group, noun) -> asset (F21 lazy)

    FIG_CLASS = {"graph": "plot", "grid": "plot", "table": "table",
                 "diagram": "figure", "apparatus": "figure", "boxes": "figure"}
    CLASS_NOUN_RE = {c: re.compile(rf"\b({'|'.join(sorted(n for n, k in FIG_CLASS.items() if k == c))})s?\b", re.I)
                     for c in set(FIG_CLASS.values())}

    # group stems live on the parts during extraction (q['groups'] is attached
    # to the serialized topic only) — build the per-question view now so the
    # stem-figure / adjacent-page lookups can see them
    for q in doc_questions:
        q["groups"] = {}
        for p in q["parts"]:
            if p.get("group_stem_md"):
                q["groups"].setdefault(p["group"], {})["group_stem_md"] = p["group_stem_md"]

    def clusters_for(pg):
        if pg not in page_clusters:
            page = pdf[pg - 1]
            page_clusters[pg] = detect_figure_clusters(page)
            page_rasters[pg] = [fitz.Rect(i["bbox"]) for i in page.get_image_info()
                                if i["bbox"][2] - i["bbox"][0] >= 5
                                and i["bbox"][3] - i["bbox"][1] >= 5]
        return page_clusters[pg]

    def render_crop(pg, cluster, a, ay):
        page = pdf[pg - 1]
        c = expand_with_labels(page, cluster, exclude_frags=a.get("_src_text") or [])
        clip = fitz.Rect(c.x0 - 3, c.y0 - 3, c.x1 + 3, c.y1 + 3) & page.rect
        pix = page.get_pixmap(clip=clip, dpi=CROP_DPI)
        rel = f"assets/{a['id']}.png"
        pix.save(str(OUT / rel))
        cov = text_coverage(page, c)
        a["kind"] = "crop"
        a["path"] = rel
        a["page"] = pg
        a["render"] = ("raster" if any(rb.contains(c) for rb in page_rasters[pg])
                       else "vector")
        a["text_coverage"] = cov
        a["review"] = bool(ay is None or cov > 0.55)
        v = crop_reviews.get(a["id"])
        if isinstance(v, dict) and v.get("verdict") == "accepted":
            a["review"] = False
            a["review_verdict"] = "accepted"
        crop_stats["crops"] += 1

    def page_of_text(text):
        frag = norm(re.sub(r"\s+", " ", text))[:110]
        probes, seen = [], set()
        for n in (60, 38, 110):
            probe = frag[:n]
            if len(probe) < 20 or probe in seen:
                continue
            seen.add(probe)
            pages = [i + 1 for i, t in enumerate(page_norm) if probe in t]
            if pages:
                return pages[0]
        return None

    def group_letter(p):
        m = re.match(r"\d+\(([a-z])\)", p["part_number"])
        return m.group(1) if m else None

    def stem_figure(q, p, noun, own_group_only=False, same_page=None):
        """F21: crop the figure a question/group stem introduces ('The graph
        shows ...', 'uses this apparatus', 'Grid 2 shows ...'), once per
        (question, group, noun). Returns the asset dict or None.
        v0.7.1 (F33): own_group_only restricts the introducer to the part's
        OWN group stem / the question stem — earlier siblings and other
        groups' stems are NOT introductions (the 2024-11 6(c)(i) defect
        where 6(b)'s sentence hijacked 6(c)(i) before its own-page pick);
        same_page requires the stem sentence to print on the part's page."""
        group = group_letter(p)
        # F33: the cache key carries the search strictness — a None result
        # from the tight 4a-pre search must not poison the wider 3a/4c search
        key = (q["question_number"], group, noun, own_group_only, same_page)
        if key in stem_assets:
            return stem_assets[key]
        cls = FIG_CLASS[noun]
        stems = []
        g = (q.get("groups") or {}).get(group) if group else None
        if g and g.get("group_stem_md"):
            stems.append(g["group_stem_md"])
        if not own_group_only:
            for letter, gg in sorted((q.get("groups") or {}).items()):
                if letter != group and gg.get("group_stem_md"):
                    stems.append(gg["group_stem_md"])
        if q.get("stem_md"):
            stems.append(q["stem_md"])
        if not own_group_only:
            # intro sentences often glue into the first part's problem_md when
            # the group stays inline — earlier siblings are legitimate
            # introductions
            for pp in q["parts"]:
                if pp is p:
                    break
                if pp.get("problem_md"):
                    stems.append(pp["problem_md"])
        a = None
        cnre = CLASS_NOUN_RE[FIG_CLASS[noun]]
        for st in stems:
            sent = next((s for s in re.split(r"(?<=[.!?])\s+", st)
                         if cnre.search(s)), None)
            if not sent:
                continue
            # v0.9 (F40c): stem linearizations glue figure-glyph junk into the
            # intro sentence ('...H O O H The table shows the bond energies...')
            # because the displayed formula carries no punctuation — the glued
            # whole string never matches a page's text order, so the intro was
            # silently lost (the 2022-06 2C 7(d)(i) / 2024-11 2C 5(b)(i) /
            # 2023-01 2C 7(b)(i) defects: the real stem table was never
            # cropped and a neighbour figure got stolen instead). Retry from
            # the noun phrase itself, then with bounded windows.
            probes = [sent]
            m_np = cnre.search(sent)
            if m_np:
                tail = sent[m_np.start():].split()
                probes.append(sent[m_np.start():])
                probes.append(" ".join(tail[:10]))
                probes.append(" ".join(tail[:6]))
            pg, ay, used_sent = None, None, None
            for probe in probes:
                pg_try = page_of_text(probe)
                if pg_try is None:
                    continue
                ay_try = figure_anchor_y(pdf[pg_try - 1], probe)
                if ay_try is None and probe is not probes[0]:
                    # the page hit came from the windowed probe; anchor with
                    # the same window
                    ay_try = figure_anchor_y(pdf[pg_try - 1], probe, min_words=4)
                if ay_try is None:
                    continue
                pg, ay, used_sent = pg_try, ay_try, probe
                break
            if pg is None:
                continue
            sent = used_sent
            if same_page is not None and pg != same_page:
                continue
            page = pdf[pg - 1]
            used = claimed.setdefault(pg, {})
            cand = [(i, c) for i, c in enumerate(clusters_for(pg))
                    if used.get(i) in (None, q["question_number"])]
            pick = None
            if ay is not None:
                below = sorted(((abs(c.y0 - ay), i, c) for i, c in cand
                                if c.y0 >= ay - 36), key=lambda t: (t[0], t[1]))
                pick = below[0] if below else None
            if pick is None:
                continue
            _, i, c = pick
            if used.get(i) == q["question_number"] and claimed_asset.get(pg, {}).get(i):
                # v0.7 (F28): the same question already cropped this cluster —
                # reuse that crop instead of rendering a second file
                stem_assets[key] = claimed_asset[pg][i]
                return claimed_asset[pg][i]
            used[i] = q["question_number"]
            aid = f"asset_{q['question_number']}_{group or 'q'}_{noun}_stem"
            a = {"id": aid, "kind": "crop-required", "mention": noun,
                 "source": "qp.pdf", "page": pg, "review": True,
                 "_src_text": [sent, p.get("problem_md") or ""]}
            render_crop(pg, c, a, ay)
            claimed_asset.setdefault(pg, {})[i] = a
            a["review"] = True          # stem-anchored: verify target choice
            break
        stem_assets[key] = a
        return a

    def sibling_crop(q, p, noun):
        """F20: nearest preceding sibling part owning a REAL crop of the same
        figure class ('graph'/'grid' both resolve to a plotting surface)."""
        cls = FIG_CLASS[noun]
        best = None
        for pp in q["parts"]:
            if pp is p:
                break
            for aa in pp.get("assets") or []:
                if (aa.get("kind") == "crop" and aa.get("mention") in FIG_CLASS
                        and FIG_CLASS[aa["mention"]] == cls and not aa.get("ref_part")):
                    best = aa
        return best

    def adjacent_crop(q, p, a):
        """F23: the figure lives on a neighbouring page (a part continued from
        its group's previous page). Anchor ONLY on a stem sentence that names
        the noun's class, and claim the nearest cluster below it. Always
        review-flagged. v0.9 (F40a): the v0.7 whole-stem fallback (anchor on
        ANY stem text printed on the neighbour page) is GONE — a stem that
        never names the class identifies nothing, and the fallback stole
        unrelated data figures on the neighbour page for draw/resolve
        mentions (2021-11 2C 5(c) reactivity-series box, 7(c) bond table,
        2025-06 2C 2(e) apparatus). Plot-class surfaces (the only legitimate
        continuation targets, 2025-11 3(c)(i)) resolve via the question-
        scoped plot fallback, not this path."""
        group = group_letter(p)
        stems = []
        g = (q.get("groups") or {}).get(group) if group else None
        if g and g.get("group_stem_md"):
            stems.append(g["group_stem_md"])
        if q.get("stem_md"):
            stems.append(q["stem_md"])
        pg = p.get("source_page")
        for pg2 in (pg - 1, pg + 1) if pg else ():
            if not (1 <= pg2 <= len(pdf)) or pg2 in content_img_pages:
                continue
            page = pdf[pg2 - 1]
            ay = None
            cnre2 = CLASS_NOUN_RE[FIG_CLASS[a["mention"]]]
            # v0.9 (F40a-fix): the whole-stem fallback survives ONLY for
            # DEFINITE references ('the diagram shows...', 2022-01 1C 3(b)(ii)
            # — the group stem's diffusion-tube figure the part explicitly
            # refers to) and never for data-source readings ('the data/values
            # in the table', F40b) — those name a specific table the stem
            # path owns. Create/data mentions ('draw a diagram', 'complete
            # the table') stay fallback-free: the four v0.8.1 thefts were
            # all create/data mentions stealing neighbour figures.
            pmd_l = (p.get("problem_md") or "")
            noun_re = re.escape(a["mention"])
            definite = re.search(rf"\b(?:the|this|that|his|its)\s+{noun_re}s?\b", pmd_l, re.I)
            data_source = re.search(
                rf"\b(?:data|values|results)\s+(?:in|on|from|of)\s+(?:the|this|that|his|its)\s+{noun_re}s?\b",
                pmd_l, re.I)
            for st in stems:
                sent = next((s for s in re.split(r"(?<=[.!?])\s+", st)
                             if cnre2.search(s)), None)
                if sent is None:
                    if not (definite and not data_source):
                        # F40a: a stem that never names the noun class does
                        # not anchor the search for indefinite/create/data
                        # mentions — see docstring.
                        continue
                    sent = st
                ay = figure_anchor_y(page, sent, min_words=4)
                if ay is not None:
                    break
            used = claimed.setdefault(pg2, {})
            cand = [(i, c) for i, c in enumerate(clusters_for(pg2))
                    if used.get(i) in (None, q["question_number"])]
            if not cand:
                continue
            if ay is not None:
                below = sorted(((abs(c.y0 - ay), i, c) for i, c in cand
                                if c.y0 >= ay - 36), key=lambda t: (t[0], t[1]))
            else:
                below = []   # v0.7 (F25): never take an un-anchored lone figure
                             # on a neighbour page — that rule grabbed reference
                             # pages like the printed Periodic Table
            if not below:
                continue
            _, i, c = pick = below[0]
            if FIG_CLASS[a["mention"]] == "plot" and text_coverage(page, c) > 0.15:
                # v0.7 (F30): a stem that does not name the noun may anchor on
                # a page whose figure is the wrong class (the 2022-06 6(b)(iii)
                # 'graph' defect: the question stem anchored the apparatus)
                continue
            used[i] = q["question_number"]
            claimed_asset.setdefault(pg2, {})[i] = a
            render_crop(pg2, c, a, ay)
            a["review"] = True
            return True
        return False

    def share_ref(a, target, how):
        a["kind"] = "crop"
        a["path"] = target["path"]
        a["page"] = target.get("page")
        a["render"] = target.get("render")
        a["text_coverage"] = target.get("text_coverage")
        a["shared"] = True
        a["ref_part"] = target.get("_owner") or target.get("id")
        a["review"] = False
        crop_stats["shared"] += 1

    def question_plot_fallback(q, p, a):
        """v0.7 (F25b): 'on the grid' that no own-page, stem, sibling or
        adjacent step could resolve — when the part's page +-1 contains
        EXACTLY ONE low-text cluster unclaimed by other questions, that
        cluster is the referent (the 2022-06 6(c)(i) case: the plotting
        grid prints beside the earlier parts of the same question, none of
        which names it). Same-question claims become shared refs. Always
        review-flagged."""
        pg = p.get("source_page")
        if pg is None:
            return False
        cands = []
        for pg2 in (pg - 1, pg, pg + 1):
            if not (1 <= pg2 <= len(pdf)) or pg2 in content_img_pages:
                continue
            used = claimed.setdefault(pg2, {})
            for i, c in enumerate(clusters_for(pg2)):
                owner_q = used.get(i)
                if owner_q is not None and owner_q != q["question_number"]:
                    continue
                if text_coverage(pdf[pg2 - 1], c) > 0.15:
                    continue          # tables/prose regions are not plot surfaces
                cands.append((pg2, i, c))
        if len(cands) != 1:
            return False              # zero or ambiguous -> honest stub
        pg2, i, c = cands[0]
        if claimed.get(pg2, {}).get(i) == q["question_number"] and claimed_asset.get(pg2, {}).get(i):
            share_ref(a, claimed_asset[pg2][i], "plot-fallback")
            return True
        claimed.setdefault(pg2, {})[i] = q["question_number"]
        claimed_asset.setdefault(pg2, {})[i] = a
        render_crop(pg2, c, a, None)
        a["review"] = True
        return True

    def axis_scaffold_crop(q, p, a):
        """F40d (v0.9): crop a printed DRAWN AXIS scaffold that cluster
        detection misses. An empty energy-profile answer space prints a thin
        vertical line + arrowhead + the 'Energy' label — no vector cluster
        forms, so the resolution chain falls through to the stub. The stub
        would claim 'no croppable figure', but the figure IS printed. Finds
        a substantial vertical drawing below the part's instruction line and
        crops it (labels absorbed by expand_with_labels inside render_crop).
        Fail-closed: anything ambiguous leaves the stub in place."""
        pg = p.get("source_page")
        if pg is None:
            return False
        page = pdf[pg - 1]
        pw, ph = page.rect.width, page.rect.height
        ay = figure_anchor_y(page, p["problem_md"])
        if ay is None:
            return False
        axes = []
        for d in page.get_drawings():
            r = fitz.Rect(d["rect"])
            if r.y0 < ay - 10:
                continue                  # not below the instruction
            if r.x1 <= 45 or r.x0 >= pw - 45 or r.y1 <= 30 or r.y0 >= ph - 30:
                continue                  # margin decorations / furniture
            if r.width >= 0.45 * pw and r.height >= 0.45 * ph:
                continue                  # page frame
            if r.height >= 0.5 * ph and r.width <= 60:
                continue                  # full-height margin stripe (F18)
            vertical_axis = r.width <= 14 and r.height >= 50
            substantial = min(r.width, r.height) >= 20
            if not (vertical_axis or substantial):
                continue                  # thin rule / dotted answer line
            axes.append(r)
        if not axes:
            return False
        # v0.9 (F40d-fix): a stroked line's rect can be zero-width — fitz
        # treats zero-area rects as EMPTY, so the union in expand_with_labels
        # collapses to the absorbed text label and the axis line itself is
        # lost (the 2021-11 7(c) crop that showed only 'Energy'). Give thin
        # rects a minimum stroke before unioning.
        norm_axes = []
        for r in axes:
            rr = fitz.Rect(r)
            if rr.width < 4:
                rr = fitz.Rect(rr.x0 - 2.5, rr.y0, rr.x1 + 2.5, rr.y1)
            if rr.height < 4:
                rr = fitz.Rect(rr.x0, rr.y0 - 2.5, rr.x1, rr.y1 + 2.5)
            norm_axes.append(rr)
        rect = norm_axes[0]
        for r in norm_axes[1:]:
            # keep drawings near the first axis (arrowheads, second axis);
            # distant unrelated drawings would poison the crop
            if (abs(r.x0 - rect.x0) < 200 and abs(r.y0 - rect.y0) < 260):
                rect |= r
        used = claimed.setdefault(pg, {})
        # never steal a cluster-detected figure's region
        for i, c in enumerate(clusters_for(pg)):
            if c.intersects(rect) and used.get(i) not in (None, q["question_number"]):
                return False
        render_crop(pg, rect, a, ay)
        a["review"] = True                # eyeball before the ledger accepts
        return True

    def own_page_pick(q, p, a, force_review, allow_single=True):
        """Own-page resolution shared by forward introductions and the
        backward-rescue path. Anchors at EVERY noun phrase with its direction
        (instructions point DOWN at the figure, references point UP), tries
        them last-first, then part-start, then — forward only — the
        unambiguous single cluster. Clusters claimed by the SAME question may
        be reused (shared=true); clusters claimed by another question are
        never taken (F24: the 2025-06/2021-01 page-mate theft)."""
        noun = a["mention"]
        pg = p.get("source_page")
        if pg is None:
            return False
        page = pdf[pg - 1]
        used = claimed.setdefault(pg, {})
        cand = [(i, c) for i, c in enumerate(clusters_for(pg))
                if used.get(i) in (None, q["question_number"])]
        if not cand:
            return False
        anchors = noun_anchor_y(page, p["problem_md"], noun) or []
        if not anchors:
            # v0.7 (F25): the part-start anchor is only used when the noun
            # phrase itself gives no evidence — a directional noun anchor
            # must never be overridden by a blind below-anchor (the
            # 2020-01 9(d)(i) 'from the table' defect).
            start_ay = figure_anchor_y(page, p["problem_md"])
            if start_ay is not None:
                anchors.append((start_ay, True))
        for ay, below in anchors:
            if below:
                scored = sorted(((min(abs(c.y0 - ay), abs((c.y0 + c.y1) / 2 - ay)), i, c)
                                 for i, c in cand if c.y0 >= ay - 36),
                                key=lambda t: (t[0], t[1]))
            else:
                scored = sorted(((min(abs(c.y1 - ay), abs((c.y0 + c.y1) / 2 - ay)), i, c)
                                 for i, c in cand if c.y1 <= ay + 36),
                                key=lambda t: (t[0], t[1]))
            if scored and FIG_CLASS[noun] == "plot" and \
                    text_coverage(page, scored[0][2]) > 0.30:
                # v0.7 (F25): a text-dense region is a printed data table, not
                # a plotting surface (every verified grid/graph crop has
                # coverage <= 0.05; the 2025-11 3(c)(i) table above the
                # 'On the grid' line must not be taken as the grid)
                scored = []
            if scored:
                _, i, c = scored[0]
                if used.get(i) == q["question_number"] and claimed_asset.get(pg, {}).get(i):
                    # v0.7 (F28): the same question already cropped this
                    # cluster — share the rendered file instead of writing a
                    # byte-identical twin PNG with ref_part:null
                    share_ref(a, claimed_asset[pg][i], "same-claim")
                    return True
                used[i] = q["question_number"]
                claimed_asset.setdefault(pg, {})[i] = a
                p["_owner"] = p["part_number"]
                a["_owner"] = p["part_number"]
                render_crop(pg, c, a, ay if below else None)
                if force_review:
                    a["review"] = True
                return True
        if len(cand) == 1 and not force_review and allow_single:
            # forward introduction on a page with exactly one figure: unambiguous
            i, c = cand[0]
            if used.get(i) == q["question_number"] and claimed_asset.get(pg, {}).get(i):
                share_ref(a, claimed_asset[pg][i], "same-claim")
                return True
            used[i] = q["question_number"]
            claimed_asset.setdefault(pg, {})[i] = a
            p["_owner"] = p["part_number"]
            a["_owner"] = p["part_number"]
            render_crop(pg, c, a, None)
            a["review"] = True          # no anchor evidence -> verify
            return True
        return False

    for q in doc_questions:
        for p in q["parts"]:
            p["_owner"] = None
            pmd = p["problem_md"] or ""
            for a in p.get("assets") or []:
                a["_src_text"] = [pmd]
                noun = a["mention"]
                pg = p.get("source_page")
                # 0. dot-and-cross draw prompts: the printed scaffold is
                # text-only, so no vector region exists — honest stub (F19b).
                # v0.7.1 (F32): a DRAWN scaffold (overlapping electron shells
                # printed as vector circles, 2024-11 6(c)(i)) is a real
                # figure — the normal anchoring path below must crop it, so
                # the stub only applies when no substantial drawing sits at/
                # below the instruction (fail-closed: unanchorable -> stub).
                if (noun == "diagram" and re.search(r"dot.{0,3}and.{0,3}cross", pmd, re.I)
                        and not INTRO_RE.search(pmd)):
                    _page = pdf[pg - 1] if pg is not None else None
                    _ay = figure_anchor_y(_page, pmd) if _page is not None else None
                    if not (_ay is not None and drawn_scaffold_below(_page, _ay)):
                        crop_stats["pending"] += 1
                        continue
                # v0.7: numbered-figure first-look is PER NOUN — 'table 1'
                # pins the table asset to this question's region, but the
                # same part's 'diagram' mention is not numbered (the
                # 2022-06 4(b) defect where the diagram mention was dragged
                # to Table 1 below the instruction)
                numbered = bool(re.search(rf"\b{re.escape(noun)}s?\s+\d+\b", pmd, re.I))
                # 1. explicit 'in part (x)' back-reference
                bm = BACKREF_RE.search(pmd)
                if bm:
                    letter = bm.group(1)
                    tgt = next((pp for pp in q["parts"]
                                if pp["part_number"].startswith(f"{q['question_number']}({letter})")
                                and pp is not p), None)
                    if tgt:
                        resolved = next((aa for aa in (tgt.get("assets") or [])
                                         if aa.get("kind") == "crop"
                                         and FIG_CLASS.get(aa.get("mention")) == FIG_CLASS[noun]), None)
                        if resolved:
                            share_ref(a, resolved, "backref")
                            continue
                backward = resolve_first(pmd, noun) and not BACKREF_RE.search(pmd)
                if numbered:
                    # 2. numbered figures print in the question's own region —
                    # own-page anchoring before any cross-page search (F25)
                    if own_page_pick(q, p, a, force_review=False, allow_single=False):
                        continue
                if backward:
                    # 3a. stem / group-stem figure
                    sa = stem_figure(q, p, noun)
                    if sa:
                        share_ref(a, sa, "stem")
                        continue
                    # 3b. sibling crop
                    sc = sibling_crop(q, p, noun)
                    if sc:
                        share_ref(a, sc, "sibling")
                        continue
                    # 3c. own-page rescue, both directions, always verified
                    if own_page_pick(q, p, a, force_review=True):
                        continue
                    # 3d. adjacent page, strong stem anchor only (F25)
                    if adjacent_crop(q, p, a):
                        continue
                else:
                    # 4a-pre (F33): a group/question stem that NAMES the
                    # noun's class introduces the figure — resolve it BEFORE
                    # any own-page below-pick. The 2024-11 6(a)(i) defect:
                    # 'Complete the table' printed BELOW the table (the
                    # formulae grid the group stem 'The table gives...'
                    # introduces) picked the next part's electron-shell
                    # diagram below the instruction instead; the real table
                    # was never cropped. TWO GATES keep the promotion surgical:
                    #   (1) the part's own text must not introduce the figure
                    #       itself (INTRO_RE — the 2019-06 3(d)(ii) 'The table
                    #       lists...' class: its own sentence anchors the
                    #       correct table below, no stem needed);
                    #   (2) the part's own noun anchors must point DOWN (the
                    #       instruction-below-figure signature — the 2025-06
                    #       1(a) 'Label ... on the diagram' class references
                    #       UP and resolves fine without promotion).
                    # stem_figure fails safe (None) so the below-pick still
                    # runs when no own-group stem names the class on the
                    # part's page.
                    _promote = not INTRO_RE.search(pmd)
                    if _promote and pg is not None:
                        _anchors = noun_anchor_y(pdf[pg - 1], pmd, noun)
                        if _anchors and not any(b for _, b in _anchors):
                            _promote = False
                    sa = stem_figure(q, p, noun, own_group_only=True,
                                     same_page=pg) if _promote else None
                    if sa:
                        share_ref(a, sa, "stem")
                        continue
                    # 4a. forward introduction: own-page cluster in the noun
                    # phrase's own direction
                    if own_page_pick(q, p, a, force_review=False, allow_single=False):
                        continue
                    # 4b. the page's figure was already claimed by a sibling
                    sc = sibling_crop(q, p, noun)
                    if sc:
                        share_ref(a, sc, "sibling")
                        continue
                    # 4c. the group/question stem introduced the figure even
                    # though this part's sentence is an instruction (F25:
                    # 2020-01 9(d)(i) 'the table' = the p24 data table)
                    sa = stem_figure(q, p, noun)
                    if sa:
                        share_ref(a, sa, "stem")
                        continue
                    # 4d. adjacent page, strong anchor only
                    if adjacent_crop(q, p, a):
                        continue
                # 5. question-scoped plot fallback (F25b)
                if FIG_CLASS[noun] == "plot" and question_plot_fallback(q, p, a):
                    continue
                # 5b. drawn-scaffold rescue (F40d, v0.9): a draw/complete
                # instruction whose printed scaffold is TOO THIN for cluster
                # detection — a lone Energy axis with an arrowhead (2021-11
                # 2C 7(c), 2025-06 2C 2(e), 2019-06 2C 5(c), 2025-11 2C 6(a))
                # — must not become a "no croppable figure" stub: the paper
                # DOES print the figure the student completes. Crop the
                # axis's own rect (F32's drawn-scaffold doctrine, extended
                # from dot-and-cross shells to drawn axes).
                if (FORWARD_RE.match(pmd) and FIG_CLASS[noun] == "figure"
                        and pg is not None and axis_scaffold_crop(q, p, a)):
                    continue
                # 6. honest stub
                crop_stats["pending"] += 1
                continue
        # mark owners of real crops for share_ref bookkeeping (stem crops are
        # question-level figures — they keep their own id as the ref target)
        for p in q["parts"]:
            for a in p.get("assets") or []:
                if (a.get("kind") == "crop" and not a.get("ref_part")
                        and not a["id"].endswith("_stem") and not a.get("_owner")):
                    a["_owner"] = p["part_number"]

    # ---- v0.14.0 (wave-20): question-stem figure pass -----------------------
    # The wave-19 exporter restored all 427 question stems to the hub (F53);
    # the FIGURES those stems introduce are this pass: STEM-RESTORE.json's
    # keep-verdict entries may carry stemFigures [{id, page, rect, mention,
    # target}] — the eyeballed crop tranche. Each spec emits a crop-required
    # stub on the target part (the question's first part unless target names
    # one), and the EXISTING F45 manual_crop branch renders it at verdict time
    # (the box is the human decision; the render is deterministic at CROP_DPI).
    # Fail-closed: a malformed spec (page out of range, rect not 4 finite
    # numbers >= 0, colliding asset id) aborts the run.
    _stem_ledger_path = RES_DIR / "Official-ExamQuestion" / "STEM-RESTORE.json"
    _stem_entries = {}
    if _stem_ledger_path.exists():
        _stem_entries = json.loads(_stem_ledger_path.read_text()).get("verdicts", {})
    n_stemfig_stubs = 0
    for q in doc_questions:
        _skey = f"{series}/4CH1-{paper}:Q{q['question_number']}"
        _sentry = _stem_entries.get(_skey) or {}
        for _sf in _sentry.get("stemFigures") or []:
            _aid = _sf.get("id")
            _pg = _sf.get("page")
            _rect = _sf.get("rect")
            if (not isinstance(_aid, str) or not _aid
                    or not isinstance(_pg, int) or not (1 <= _pg <= len(pdf))
                    or not isinstance(_rect, list) or len(_rect) != 4
                    or not all(isinstance(x, (int, float)) and x >= 0 for x in _rect)):
                raise SystemExit(
                    f"wave-20 stemFigure malformed for {_skey}: {_sf!r}")
            _tgt = _sf.get("target")
            _tp = (next((pp for pp in q["parts"] if pp["part_number"] == _tgt),
                        q["parts"][0] if q["parts"] else None))
            if _tp is None:
                continue
            if any(a["id"] == _aid for pp in q["parts"] for a in (pp.get("assets") or [])):
                raise SystemExit(
                    f"wave-20 stemFigure id collision: {_aid} already exists in {_skey}")
            _tp.setdefault("assets", []).append({
                "id": _aid, "kind": "crop-required", "mention": _sf.get("mention") or "figure",
                "source": "qp.pdf", "page": _pg, "review": True, "stem_figure": True,
                "_src_text": [],
            })
            crop_stats["pending"] += 1
            n_stemfig_stubs += 1
    if n_stemfig_stubs:
        report.setdefault("wave20", {})["stem_figure_stubs"] = n_stemfig_stubs

    # ---- v0.7 (F29) / v0.7.1 (F32): crop-review verdicts, applied LAST -----
    # The eyeball ledger overrides every confidence flag — resolution paths
    # set review=True after render_crop runs, so the verdict must land after
    # all of them (the 18-crop wave that still showed review=true otherwise).
    # v0.7.1 verdict vocabulary: 'accepted' clears review on real crops
    # (kind=="crop"); 'stub-accepted' clears review on honest crop-required
    # stubs (the eyeballed "no croppable figure" decision). Any other
    # combination fails closed — C22 flags ledger↔corpus mismatches.
    # v0.10.1 (F45) optional crop pass: a ledger entry may carry
    # manual_crop {page, rect} — the eyeballed crop box (PDF points) for a
    # stub whose printed content the automatic pass cannot reach (text-only
    # scaffolds the F19b doctrine stubs, or figures on rasterized archive
    # pages with no vector anchors). The box is the human decision; the
    # render is deterministic at CROP_DPI on every re-run. Fail-closed: a
    # malformed box aborts the run instead of silently shipping a stub or a
    # wrong crop; the stub's own page must agree with the box's page.
    for q in doc_questions:
        for p in q["parts"]:
            for a in p.get("assets") or []:
                v = crop_reviews.get(a["id"])
                if not isinstance(v, dict):
                    continue
                vd = v.get("verdict")
                mc = v.get("manual_crop")
                if mc is not None:
                    if vd != "accepted" or a.get("kind") != "crop-required":
                        raise SystemExit(
                            f"F45 manual_crop requires verdict=accepted on a crop-required "
                            f"stub: {a['id']} verdict={vd!r} kind={a.get('kind')!r}")
                    mc_pg = mc.get("page")
                    mc_rect = mc.get("rect")
                    if (not isinstance(mc_pg, int) or not (1 <= mc_pg <= len(pdf))
                            or not isinstance(mc_rect, list) or len(mc_rect) != 4
                            or not all(isinstance(x, (int, float)) and x >= 0 for x in mc_rect)):
                        raise SystemExit(
                            f"F45 manual_crop malformed for {a['id']}: {mc!r}")
                    if a.get("page") is not None and int(a["page"]) != mc_pg:
                        raise SystemExit(
                            f"F45 manual_crop page {mc_pg} != stub page {a.get('page')} for {a['id']}")
                    mc_page = pdf[mc_pg - 1]
                    mc_clip = fitz.Rect(*[float(x) for x in mc_rect]) & mc_page.rect
                    if mc_clip.is_empty or mc_clip.width < 20 or mc_clip.height < 20:
                        raise SystemExit(f"F45 manual_crop degenerate rect for {a['id']}: {mc_rect}")
                    clusters_for(mc_pg)          # populate the page raster index
                    mc_rel = f"assets/{a['id']}.png"
                    mc_pix = mc_page.get_pixmap(clip=mc_clip, dpi=CROP_DPI)
                    mc_pix.save(str(OUT / mc_rel))
                    a["kind"] = "crop"
                    a["path"] = mc_rel
                    a["page"] = mc_pg
                    a["render"] = ("raster" if any(rb.contains(mc_clip) for rb in page_rasters[mc_pg])
                                   else "vector")
                    a["text_coverage"] = text_coverage(mc_page, mc_clip)
                    a["manual_crop"] = True
                    if crop_stats["pending"] > 0:
                        crop_stats["pending"] -= 1
                    crop_stats["crops"] += 1
                    vd = "accepted"
                if vd == "accepted" and a.get("kind") == "crop":
                    a["review"] = False
                    a["review_verdict"] = "accepted"
                elif vd == "stub-accepted" and a.get("kind") == "crop-required":
                    a["review"] = False
                    a["review_verdict"] = "stub-accepted"

    # ---- spec tags: v0.5 demo seeds + v0.7 llm spec-tagging waves -----------
    # Labels only (AGENTS.md review taxonomy: 'pending-llm' -> seed via LLM as
    # labels, re-validated by G6). Wave files live in spec-labels/<series>.json
    # as {"parts": {"<part_number>": ["4CH1-x.y", ...]}}; question-level tags
    # are expanded to their parts by the wave authoring script.
    seeds = SEEDS.get(series, {}) if paper == "1C" else {}   # demo seeds are 1C artifacts (F31)
    labels_path = (RES_DIR / "Official-ExamQuestion" / "spec-labels" /
                   (f"{series}.json" if paper == "1C" else f"{series}-{paper}.json"))
    labels, nsp = {}, {}
    if labels_path.exists():
        _labels_doc = json.loads(labels_path.read_text())
        labels = _labels_doc.get("parts", {})
        # v0.8.1 (F38): terminal no-spec-point states — parts the official 4CH1
        # specification itself gives NO numbered point for (verified against the
        # published spec), decided rather than left pending-llm forever.
        nsp = _labels_doc.get("no_spec_point", {})
    # F64: a course without a spec registry (maths-B tranche-1) runs G6 with an
    # empty registry — lawful only while NO codes are emitted (all parts land in
    # pending-llm / no-spec-point states); any emitted code would fail the
    # membership check below, which is exactly the fail-closed posture we want.
    if SPEC_RESOLUTION is not None and Path(SPEC_RESOLUTION).exists():
        reg = json.loads(Path(SPEC_RESOLUTION).read_text())["resolved"]
        registry = set()
        for r in reg:
            if r.get("resolved_code"):
                registry.add(r["resolved_code"])
    else:
        registry = set()   # F64: no-registry course — G6 runs vacuous (0 codes)
    for q in doc_questions:
        for p in q["parts"]:
            codes, tagging = [], None
            seed_code = seeds.get(p["part_number"])
            if seed_code:
                codes, tagging = [seed_code], "seed-demo"
            elif labels.get(p["part_number"]):
                codes, tagging = list(labels[p["part_number"]]), "llm-spec-wave"
            if codes:
                p["spec_point_codes"] = codes
                p["tagging"] = tagging
                bad = [c for c in codes if c not in registry]
                if bad:
                    p["tagging"] = "registry-gap-review"
                    report["review_queue"].append({"part": p["part_number"], "reason": f"spec code {', '.join(bad)} not in registry (gap or invalid) — human decision"})
            else:
                p["spec_point_codes"] = []
                if p["part_number"] in nsp:
                    p["tagging"] = "no-spec-point"
                else:
                    p["tagging"] = "pending-llm"
    # ---- provenance (ADR-039 §4 disclosure contract, schema /0.2) ------------
    # Every part carries explicit provenance. The deterministic extraction is
    # the baseline of record: parts are "extracted" until a disclosed improving
    # pass touches them. edits[] is ABSENT for extracted parts (0.1 corpora
    # load as extracted — the field appears only when there is something to
    # disclose). value_trace records where each graded value came from.
    _ledger_keys = set(mcq_keys_applied)
    for _q in doc_questions:
        for _p in _q["parts"]:
            if _p["question_type"] == "multiple_choice":
                if any(c.get("is_correct") for c in _p["choices"] or []):
                    _kt = ("ledger:MCQ-KEYS"
                           if f"{series}:{paper}/{_p['part_number']}" in _ledger_keys
                           else "ms-positional")
                else:
                    _kt = "unresolved:review-queue"   # honest refusal, still in review
            else:
                _kt = "n/a"
            _p["edit_status"] = "extracted"
            _p["value_trace"] = {"keys": _kt, "marks": "ms-printed",
                                 "numbers": "source-printed"}

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

    # G2-D disclosure (ADR-039 §4) — provenance must match reality. Parts
    # claiming "extracted" must 5-gram-match their source region (the old G2
    # check, demoted from law to a provenance-correctness assertion — it now
    # catches a mislabeled edit_status, not an edit); parts claiming
    # "corrected"/"enriched" must carry a complete edits[] entry per touched
    # field; value_trace must be consistent with the actual emission.
    EDIT_KINDS = {"typo-fix", "clarification", "notation", "enrichment",
                  "structural-repair"}
    g2d_bad, g2_ratios, g2d_disclosed = [], {}, 0
    for q in doc_questions:
        for p in q["parts"]:
            status = p.get("edit_status", "extracted")
            edits = p.get("edits") or []
            if status in ("corrected", "enriched"):
                g2d_disclosed += 1
                if not edits:
                    g2d_bad.append({"part": p["part_number"],
                                    "issue": f"edit_status {status} without edits[]"})
                for e in edits:
                    if not (e.get("field") and e.get("kind") in EDIT_KINDS
                            and e.get("tool") and e.get("evidence_ref")):
                        g2d_bad.append({"part": p["part_number"],
                                        "issue": f"incomplete edits[] entry: {e}"})
            else:
                grams = ngrams(p["problem_md"])
                if not grams:
                    continue
                src_grams = ngrams(p["source_norm"])
                ratio = sum(1 for g in grams if g in src_grams) / len(grams)
                g2_ratios[p["part_number"]] = round(ratio, 4)
                if ratio < 0.95:
                    g2d_bad.append({"part": p["part_number"],
                                    "issue": "claims extracted but 5-gram overlap <0.95 vs source",
                                    "ratio": round(ratio, 4)})
    # value_trace ↔ edits[] coherence: a marks edit must be claimed and a claim
    # must have its edit (ADR-039 §4 G2-D condition 4)
    for q in doc_questions:
        for p in q["parts"]:
            vt = p.get("value_trace") or {}
            touched = {e.get("field") for e in (p.get("edits") or [])}
            if "marks" in touched and not str(vt.get("marks", "")).startswith("corrected:"):
                g2d_bad.append({"part": p["part_number"],
                                "issue": "edits[] touches marks but value_trace.marks does not claim the correction"})
            if str(vt.get("marks", "")).startswith("corrected:") and "marks" not in touched:
                g2d_bad.append({"part": p["part_number"],
                                "issue": "value_trace.marks claims a correction with no edits[] entry"})
    gate("G2-D-disclosure", not g2d_bad,
         f"provenance matches reality for all {len(g2_ratios) + g2d_disclosed} parts "
         f"({g2d_disclosed} disclosed, {len(g2_ratios)} extracted at ≥0.95 5-gram): {not g2d_bad}",
         {"violations": g2d_bad, "min_ratio": min(g2_ratios.values()) if g2_ratios else None})

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
                if figure_mentions(p["problem_md"]) and not p["assets"]]
    n_assets = sum(len(p["assets"]) for q in doc_questions for p in q["parts"])
    n_unanchored = sum(1 for q in doc_questions for p in q["parts"] if p["source_page"] is None)
    gate("G4-figure-resolution", not dangling,
         f"{n_assets} asset records cover every table/diagram/grid/apparatus mention: "
         f"{crop_stats['crops']} cropped to assets/*.png ({CROP_DPI} dpi), "
         f"{crop_stats['pending']} remain crop-required; "
         f"{n_unanchored} parts without page anchor",
         {"dangling": dangling, "pages_unanchored": n_unanchored, "crop_stats": crop_stats})
    for q in doc_questions:
        for p in q["parts"]:
            for a in p.get("assets") or []:
                if a.get("kind") == "crop":
                    if a.get("review"):
                        report["review_queue"].append(
                            {"part": p["part_number"],
                             "reason": f"figure crop emitted — human verify ({a['path']})"})
                else:
                    report["review_queue"].append(
                        {"part": p["part_number"],
                         "reason": f"figure crop required ({a['mention']}, page {a.get('page')})"})

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
    n_nospec = sum(1 for p in parts_all if p["tagging"] == "no-spec-point")
    gate("G6-registry-codes", not g6_bad,
         f"all emitted codes ∈ spec_point_resolution registry ({len(registry)} codes) "
         f"or documented gaps→review; {n_pending} parts pending-llm tagging; "
         f"{n_nospec} parts no-spec-point (terminal, documented per part)",
         {"violations": g6_bad, "allowed_gaps": sorted(ALLOWED_GAPS)})

    # G7 solution emission (v0.5): every linked part carries the verbatim MS
    # block, and every mark_points split sums exactly to the part's marks.
    sol_parts = [p for p in parts_all if p.get("answer_status") == "linked"]
    no_sol = [p["part_number"] for p in sol_parts if not p.get("solution_md")]
    sum_bad = []
    for p in parts_all:
        mp = p.get("mark_points")
        if mp and p.get("marks") is not None and sum(x["marks"] for x in mp) != p["marks"]:
            sum_bad.append({"part": p["part_number"],
                            "points_sum": sum(x["marks"] for x in mp), "marks": p["marks"]})
    ms_seen = sum(1 for p in parts_all
                  if p.get("_ms_marks") is not None and p.get("marks") is not None)
    ms_agree = sum(1 for p in parts_all
                   if p.get("_ms_marks") is not None and p.get("marks") is not None
                   and p["_ms_marks"] == p["marks"])
    ms_disagree = [f"{p['part_number']} (ms={p['_ms_marks']} qp={p['marks']})"
                   for p in parts_all
                   if p.get("_ms_marks") is not None and p.get("marks") is not None
                   and p["_ms_marks"] != p["marks"]]
    gate("G7-solution-emission", not no_sol and not sum_bad,
         f"solution_md on {len(sol_parts) - len(no_sol)}/{len(sol_parts)} linked parts; "
         f"mark_points sum == part marks everywhere: {not sum_bad}; "
         f"MS marks-column digit read for {ms_seen} parts, agrees with QP marks on {ms_agree}",
         {"missing_solution": no_sol, "sum_mismatches": sum_bad,
          "ms_marks_seen": ms_seen, "ms_marks_agree": ms_agree,
          "ms_marks_disagree": ms_disagree})

    # ---- assemble document (before popping internal fields) ------------------
    topic = {
        "schema": SCHEMA, "generated_utc": now_iso(),
        "generator": f"official_examq_extract.py v{CONVERTER_VERSION} (ADR-039) series={series} paper={paper}",
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
                       if k not in ("group_stem_md", "option_list", "group", "roman", "answer_raw", "source_norm", "_ms_marks", "_owner") and v is not None}
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

    # strip private crop-pass bookkeeping ("_" keys) from serialized assets
    for q in topic["questions"]:
        for p in q["parts"]:
            for a in p.get("assets") or []:
                for k in [k for k in a if k.startswith("_")]:
                    a.pop(k, None)

    # strip internal linkage fields from working copy
    for q in doc_questions:
        for p in q["parts"]:
            p.pop("group", None); p.pop("roman", None); p.pop("answer_raw", None)

    # ---- negative controls (ADR-039 §5: target UNDISCLOSED mutation) --------
    nc_results = []
    flat_parts = [p for q in topic["questions"] for p in q["parts"]]
    # N1: bump one mark on the last part of the question with the most parts.
    # Must surface as a value_trace violation: a graded value that moved
    # without an evidenced edits[] entry while still claiming ms-printed.
    if flat_parts:
        nc = copy.deepcopy(topic)
        tgt = max(nc["questions"], key=lambda q: len(q["parts"]))["parts"][-1]
        tgt["marks"] = (tgt["marks"] or 0) + 1
        orig_by_part = {p["part_number"]: p for q in topic["questions"] for p in q["parts"]}
        nc_results.append({"id": "N1-mark-bump", "expected_gate": "G2-D/value-trace",
                           "detected": _value_trace_recheck(nc, orig_by_part)})

    # N2: one-word substitution in a mid-length part (mimics paraphrase drift).
    # Must surface as a missing edits[] entry: text that departed from the
    # extraction baseline without a disclosure.
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
        departed = r < 0.95
        disclosed = (mod.get("edit_status") in ("corrected", "enriched")
                     and any(e.get("field") == "problem_md" and e.get("evidence_ref")
                             for e in (mod.get("edits") or [])))
        g2_nc = departed and not disclosed
    nc_results.append({"id": "N2-paraphrase", "expected_gate": "G2-D/edits[]", "detected": g2_nc,
                       "target": nc2_target})

    # N3: fake spec code injected into the first part (skipped if no parts extracted)
    if flat_parts:
        nc3 = copy.deepcopy(topic)
        next(p for q in nc3["questions"] for p in q["parts"])["spec_point_codes"] = ["4CH1-9.99"]
        g6_nc = any(c not in registry for q in nc3["questions"] for p in q["parts"] for c in p["spec_point_codes"])
        nc_results.append({"id": "N3-fake-spec-code", "expected_gate": "G6", "detected": g6_nc})
    report["negative_controls"] = nc_results
    report["mcq_keys_applied"] = mcq_keys_applied
    report["ms_link_overrides_applied"] = ms_link_applied
    report["spec_tagging"] = {
        "tagged": sum(1 for p in parts_all if p.get("spec_point_codes")),
        "parts": len(parts_all),
        "pending_llm": sum(1 for p in parts_all if p.get("tagging") == "pending-llm"),
        "no_spec_point": sum(1 for p in parts_all if p.get("tagging") == "no-spec-point"),
    }

    # ---- write outputs -------------------------------------------------------
    # F64: spec §3.4 disclosure — the per-instance control-char fallback log
    if CTL_COUNTER:
        report["control_char_fallback"] = {
            "policy": "spec §3.4 single-space fallback, logged per-instance (F64)",
            "instances": dict(sorted(CTL_COUNTER.items())),
        }
        report["review_queue"].append({
            "part": "(corpus)",
            "reason": (f"C0 control chars in the QP text layer ({sum(CTL_COUNTER.values())} instances / "
                       f"{len(CTL_COUNTER)} codepoints) resolved to single space per spec §3.4 — "
                       "probable SymbolMT private-use operators (×/÷ class) between numeric terms; "
                       "font-trace + page-render adjudication owed before these serve as operators")})
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


def _value_trace_recheck(doc, orig_by_part):
    """ADR-039 §5 N1 detector: every graded value must either match the
    extraction-of-record or be disclosed (evidenced edits[] entry AND a
    value_trace claim). Returns True on the first undisclosed movement."""
    for q in doc["questions"]:
        for p in q["parts"]:
            o = orig_by_part.get(p["part_number"])
            if o is None:
                continue
            if p.get("marks") != o.get("marks"):
                edits = p.get("edits") or []
                if not any(e.get("field") == "marks" and e.get("evidence_ref") for e in edits):
                    return True
                if not str((p.get("value_trace") or {}).get("marks", "")).startswith("corrected:"):
                    return True
    return False


def write_questions_md(topic, path):
    out = [f"# {topic['paper_info']['code']} — {topic['source']['series']} (official extraction)",
           "", f"> schema `{topic['schema']}` · paper_id `{topic['paper_id']}` · "
               f"qp sha256 `{topic['source']['qp_sha256'][:16]}…` · extraction is the disclosed baseline (ADR-039)", ""]
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
            for a in p.get("assets") or []:
                if a.get("kind") == "crop" and a.get("path"):
                    cap = f"{a['mention']} — official paper figure (qp.pdf p.{a['page']})"
                    if a.get("shared"):
                        cap += f" — shared with {a.get('ref_part', '?')}"
                    out += [f"![{cap}]({a['path']})", ""]
                else:
                    out += [f"> 🖼 crop required: {a['mention']} (qp.pdf p.{a['page']})", ""]
            if p.get("solution_md"):
                out += ["", "**Mark scheme answer**", ""]
                out += ["> " + ln for ln in p["solution_md"].splitlines()]
                out += [""]
                for pt in p.get("mark_points") or []:
                    out += [f"- **({pt['marks']})** {pt['text_md'].splitlines()[0]}"]
                out += [""]
        out.append("")
    path.write_text("\n".join(out))


if __name__ == "__main__":
    sys.exit(main())
