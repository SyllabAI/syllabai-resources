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
      python3 official_examq_extract.py --spec 4ph1 --series 2023-06 --paper 1P
                                                                       (v0.16.0: spec lanes — every
                                                                        per-spec constant lives in SPECS)
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

# T-OEQ-MATHSB-SERVE-1 hygiene wave (run-001): source-layer text repairs —
# the evidenced per-line law for the broken-symbol-font staging layers
# (lane-scoped; chemistry/physics runs are measured no-ops). See the module
# docstring for the full law + evidence chain. Path-safe sibling import:
# canaries/diffs load this file as a bare module from other CWDs (C87).
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
from official_examq_text_repairs import repair_source_text

SCHEMA = "syllabai.official-paper-questions/0.2"
CONVERTER_VERSION = "0.32.0"  # see Official-ExamQuestion/CHANGELOG.md + LEDGER.md
# v0.21.0 (F85, the QP-side wave): two 4PH1-gated QP parser fixes — (1) the
# repeat-first-label print-defect completion in parse_mcq_block, (2) the
# marks-law structural disqualification in finalize_part. Chemistry/4MB1
# behavior unchanged (both fixes gate on ACTIVE_SPEC_CODE == "4PH1").
# v0.20.0 (run-004 reconciliation v2, trace 1a174f587f822f61): the maths-B lane
# (branch 139ee931, v0.17.0-of-the-maths-line) unions onto the spec-lane
# architecture as SPECS["4mb1"]; chemistry/physics behavior unchanged.

# ---------------------------------------------------------------- spec lanes
# v0.16.0 generalization: the converter serves one spec lane per run (--spec).
# Every per-spec constant lives in SPECS below; the 4ch1 entries are the
# v0.15.0 literals verbatim, so a chemistry run is behavior-identical to
# v0.15.0 (parity receipt: bit-equal topic.json/questions.md/validation-report
# modulo generated_utc/generator on staged 2023-06 1C).
SPECS = {
    "4ch1": dict(
        lane="igcse-chemistry-19",
        spec_code="4CH1",
        # registry expectations per paper variant (LEDGER F34: paper parametrization). Marks
        # totals are footer-verified per series: 1C = 110 (constant across the era), 2C = 70
        # (constant across the era; staging probe 2026-10-21: 16/16 series sum exactly 70).
        # R variants footer-verified from the archive of record 22/22 (F-178 R-VARIANT
        # SCHEDULE, tracker PR #32 receipt: 1CR = 110 x11, 2CR = 70 x11; legacy 4CH0 R
        # papers 2013-2017 are a different spec and stay out of scope).
        paper_totals={"1C": 110, "2C": 70, "1CR": 110, "2CR": 70},
        # printed question counts verified per series (footers vary 6..15 across the
        # 4CH1 era); counts cross-checked against per-question footer marks summing
        # to the paper total
        expect_questions={
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
        },
        # per-series demo seeds (labels only; registry-validated in G6). Other series -> pending-llm.
        seeds={
            # v0.5 demo seeds, audited against the spec registry in v0.7 (LEDGER F31):
            # 4(c)(ii) is an Mr calculation (1.26), 8(c)(ii) a molar-enthalpy
            # calculation (3.4), 10(b) an empirical-formula determination (1.33),
            # 1(b)(i) the noble-gas group (1.24)
            "2020-11": {
                "1(b)(i)": "4CH1-1.24", "4(c)(ii)": "4CH1-1.26",
                "9(c)(ii)": "4CH1-1.28", "10(b)": "4CH1-1.33",
                "8(c)(ii)": "4CH1-3.4", "7": "4CH1-3.15C",   # 7* deliberately incl. registry-gap demo
            },
        },
        seeds_paper="1C",                # demo seeds are 1C artifacts (F31)
        allowed_gaps={"4CH1-3.15C"},     # chemistry-only rates practical; SME notes corpus lacks it
        course_id="igcse-chemistry-19",
        nc_fake_code="4CH1-9.99",
        footer_re=r"\(Total for Question (\d{1,2}) = (\d{1,2}) marks\)",
        default_paper="1C",
        # F39 crop-review keying: 1C keeps the legacy bare '<series>' home, other
        # variants use '<series>:<paper>' (legacy=True reproduces that exactly)
        crop_review_legacy=True,
        # spec-labels wave files: unprefixed ('<series>.json' / '<series>-<paper>.json')
        labels_prefixed=False,
        # v0.17.0: MS text-layer shape. The chemistry MS is a row table (marker
        # + answer content share a printed row) -> parse_ms. 'row' is the default
        # for any lane that does not name a layout.
        ms_layout="row",
        # F108 (v0.28.0): the chemistry MS stream opts into the MS-stream
        # clean_lines behaviors — the F90 geometry-aware bare-digit rule, and
        # the collapsed blank-line preservation the Finding-5 answer-grid
        # parser needs (the 2023-06 1CR 4(a) grid delimits rows with printed
        # blanks). Col-0 bare numerals: census 1 corpus-wide (all 54 chemistry
        # MS layers) — the F75 numeral keep is near-inert here; the maths lane
        # keeps its own flag (F84 markers) unchanged.
        keep_bare_numerals=True,
        # v0.21.0 (F85) lane-override repair: the run-004 union added the
        # SymbolMT digit range (uF030-uF039) to the GLOBAL PUA map for the
        # maths lane's 2020-01 02R decode, silently clobbering chemistry's
        # evidence-backed ZapfDingbatsITCbyBT tick mapping (uF033 -> CHECK MARK,
        # the F48 'Place ticks (✓) in three boxes' entry, v0.19.0 line 262).
        # The battery caught it: a fresh chemistry re-emission served
        # 'Place ticks (3)' (2019-06 1CR 2(a)) where the corpus of record
        # serves the tick. The collision is the union's OWN F068/F06a/F075
        # class — lane-split it the same way: chemistry evidence wins here,
        # maths keeps the digit in its pua_overrides. Corpus census: exactly
        # ONE uF03x occurrence across all 54 chemistry staging txt layers
        # (this line), so the override's blast radius is this glyph alone.
        pua_overrides={"\uf033": "\u2713"},
    ),
    "4ph1": dict(
        lane="igcse-physics-19",
        spec_code="4PH1",
        # 1P/2P totals footer-verified from the archive of record: 2023-06 1P
        # (12 questions, Σ=110) and 2024-06 2P (8 questions, Σ=70). R variants
        # mirrored from the 4CH1 pattern pending their own per-series footer
        # verification during the physics conversion waves.
        paper_totals={"1P": 110, "1PR": 110, "2P": 70, "2PR": 70},
        # only the footer-verified slices carry an expectation; every other
        # series runs with count gate skipped (None) until verified
        expect_questions={
            "1P": {"2023-06": 12, "2019-06": 12},
            "2P": {"2024-06": 8, "2023-06": 8},
        },
        seeds={},                        # no demo seeds for physics
        seeds_paper="1P",
        allowed_gaps=set(),
        course_id="igcse-physics-19",
        nc_fake_code="4PH1-9.99",
        # physics QP text layers split: 1P prints the footer WITHOUT parentheses
        # (2023-06 1P: 12 bare), 2P prints WITH (2024-06 2P: 8 wrapped) — accept both
        footer_re=r"\(?\s*Total for Question (\d{1,2}) = (\d{1,2}) marks\s*\)?",
        default_paper="1P",
        crop_review_legacy=False,
        # physics wave files are spec-namespaced under the shared dirs
        # (spec-labels/4ph1-<series>[-<paper>].json, CROP-REVIEW '4ph1-<series>[:<paper>]')
        labels_prefixed=True,
        # v0.17.0: the physics MS text layer is a CELL-PER-LINE table — every
        # cell lands on its own line at indent 0 (marker rows '1', '(a)', '(i)'
        # bare; marks digits bare; page headers 'Question/number/Answer/Notes/
        # Marks' one token per line). parse_ms's row regexes have nothing to
        # grip and clean_lines strips every bare numeral as page furniture, so
        # the 2024-06 2P probe measured G5 linkage 0%. parse_ms_vertical reads
        # the RAW layer with its own furniture pass and header-anchored state
        # machine (chemistry's parse_ms is untouched — bit-identity by
        # construction).
        ms_layout="vertical",
        # lane-override PUA mappings (run-004 union): these three codepoints
        # carry INDEPENDENT maths-B evidence — moved out of the static map
        # so neither lane's render evidence silently wins globally.
        pua_overrides={
            "\uf068": "\u2191",   # Wingdings3 up-arrow - 2021-06 1P MS p13
            "\uf06a": "",         # TransportMT train pictogram - drop
            "\uf075": "",         # TransportMT aeroplane pictogram - drop
        },
    ),
# --- F73 (the maths-B lane's F64, renumbered at the run-004 union):
# --- igcse-maths-b-16 — the second course on the Official-ExamQuestion
# --- plane (66/66 emission of record at branch tip 139ee931). Registry
# --- payload sourced verbatim from that line's COURSES entry; the CLI
# --- axis migrated --course -> --spec at the union (ONE registry — the
# --- drift-guard canary C87 polices it).
"4mb1": dict(
    lane="igcse-maths-b-16",
    spec_code="4MB1",
    # 4MB1/01 and /02 are 100-mark papers across the era; footer-verified
    # per series by the tranche runs (G1 asserts every series anyway —
    # an unverified total cannot pass G1 silently).
    paper_totals={"01": 100, "02": 100, "01R": 100, "02R": 100},
    # maths-B footers print '(Total for Question N is X marks)' — 'is',
    # not '='; 1-mark questions print the SINGULAR 'is 1 mark)'
    # (2020-01 01 Q1 — the singular-mark footer law, F83).
    footer_re=r"\(Total for Question (\d{1,2}) is (\d{1,2}) marks?\)",
    # No SME spec-point registry exists for maths-B (SME publishes zero
    # maths-B topic questions — T-SME-12). G6 posture: no codes emitted,
    # all parts honest pending-llm, G6 vacuous with a documented gap
    # note. spec_resolution=False selects the no-registry path — the
    # UPLOAD legacy fallback must NEVER serve chemistry's staged
    # registry to a maths run.
    spec_resolution=False,
    expect_questions={"01": {"2026-06": 26, "2024-11": 27, "2025-06": 26, "2023-11": 28, "2025-10": 27, "2024-06": 27, "2023-06": 28, "2022-01": 27, "2021-11": 29, "2021-01": 26, "2020-11": 29, "2020-06": 29, "2022-06": 27, "2023-01": 26, "2019-06": 28, "2018-06": 28, "2020-01": 27, "2021-06": 27, "2019-01": 27}, "02": {"2025-11": 12, "2025-06": 12, "2026-06": 12, "2024-11": 11, "2023-11": 11, "2023-06": 12, "2023-01": 12, "2022-01": 12, "2021-11": 11, "2020-11": 12, "2020-06": 12, "2020-01": 12, "2019-06": 11, "2024-06": 11, "2018-06": 11, "2022-06": 11, "2021-01": 12, "2019-01": 12, "2021-06": 12}, "01R": {"2026-06": 27, "2025-06": 26, "2023-06": 26, "2023-01": 26, "2022-01": 29, "2021-01": 28, "2019-06": 29, "2024-06": 26, "2018-06": 27, "2020-11": 26, "2020-01": 29, "2020-06": 26, "2022-06": 27, "2019-01": 28}, "02R": {"2026-06": 12, "2025-06": 12, "2023-06": 11, "2023-01": 12, "2022-06": 11, "2022-01": 11, "2021-01": 11, "2020-11": 12, "2020-06": 12, "2019-01": 11, "2018-06": 12, "2024-06": 12, "2020-01": 11, "2019-06": 11, "2019-01": 11}},
    seeds={},                        # no demo seeds (no registry to validate against)
    seeds_paper="01",
    allowed_gaps=set(),
    course_id="igcse-maths-b-16",
    # N3 fake-code parity: the branch line's maths runs injected the
    # chemistry fake (4CH1-9.99) — reproduced verbatim so the
    # negative-control evidence of record regenerates identically.
    nc_fake_code="4CH1-9.99",
    default_paper="01",
    crop_review_legacy=False,        # namespaced keying; no maths entries in CROP-REVIEW.json
    labels_prefixed=True,            # namespaced spec-labels paths (no maths files exist)
    # maths MS is a row table (parse_ms + the maths marker regexes);
    # bare-numeral MS rows are markers, not furniture (F84, was F75)
    ms_layout="row",
    keep_bare_numerals=True,
    # lane-override PUA mappings (run-004 union): three codepoints carry
    # INDEPENDENT render evidence on two lanes each — neither may win
    # the global map. Physics evidence lives in SPECS["4ph1"]
    # pua_overrides; maths evidence here.
    pua_overrides={
        "\uf068": "\u03b7",   # eta — 'MP = a + c + \u03b7(-2a - c)' (2023-01 01R p22 render)
        "\uf06a": "\u03c6",   # phi 2nd SymbolMT variant — 'MP = 3b + \u03c6("3a-5b")' (2024-06 01 p24)
        "\uf075": "{",         # Symbol brace-left (6 inst, our-render)
        "\uf0ee": "\u23a9",   # left curly hook BOTTOM 2nd variant (2024-06 02 p14) - maths evidence wins here
        "\uf033": "3",         # SymbolMT digit 3 (2020-01 02R decode) - maths evidence wins here
    },
),
}


def spec_resolution_path(cfg: dict) -> Path:
    # spec-point registry: canonical copy lives in this repo (SME-ExamQuestion/...);
    # staged spc-resolution.json is a legacy fallback for pre-F15 staging areas.
    # EXAMQ_SPEC_RESOLUTION overrides for any lane (F15 exotic staging).
    if os.environ.get("EXAMQ_SPEC_RESOLUTION"):
        return Path(os.environ["EXAMQ_SPEC_RESOLUTION"])
    if cfg.get("spec_resolution") is False:
        return None          # no-registry lane (4mb1): G6 documented gap posture
    _spec_repo = RES_DIR / "SME-ExamQuestion" / cfg["lane"] / "spec_point_resolution.json"
    if _spec_repo.exists():
        return _spec_repo
    return UPLOAD / "spc-resolution.json"


# run_all.sh contract (chemistry corpus driver): the F-178 "paper never
# printed" registry reads the 4CH1 table from this module namespace.
EXPECT_QUESTIONS = SPECS["4ch1"]["expect_questions"]
PAPER_TOTAL = SPECS["4ch1"]["paper_totals"]["1C"]   # runtime global — set per run in main()


def paths_for(series: str, paper: str, cfg: dict) -> dict:
    # F34: staging names are paper-suffixed (and spec-prefixed). The .txt
    # extraction names were NOT paper-suffixed before v0.8 (a 1C/2C staging
    # collision); fall back to the legacy bare name so pre-0.8 staging areas
    # keep working for the default paper.
    qp_txt = UPLOAD / f"official-{series}-{paper}-qp.txt"
    ms_txt = UPLOAD / f"official-{series}-{paper}-ms.txt"
    legacy_qp_txt = UPLOAD / f"official-{series}-qp.txt"
    legacy_ms_txt = UPLOAD / f"official-{series}-ms.txt"
    outroot = RES_DIR / "Official-ExamQuestion" / cfg["lane"]   # ALWAYS inside the checkout
    return {
        "qp_pdf": UPLOAD / f"official-{cfg['spec_code']}-{paper}-{series}-qp.pdf",
        "ms_pdf": UPLOAD / f"official-{cfg['spec_code']}-{paper}-{series}-ms.pdf",
        "qp_txt": qp_txt if (qp_txt.exists() or not legacy_qp_txt.exists()) else legacy_qp_txt,
        "ms_txt": ms_txt if (ms_txt.exists() or not legacy_ms_txt.exists()) else legacy_ms_txt,
        "manifest": UPLOAD / f"manifest-{series}-{paper}.yaml",
        # v0.10 (F41): optional OCR source layer for image-only pages
        "ocr_index": UPLOAD / "ocr" / f"{series}-{paper}" / "ocr-pages.json",
        "out": outroot / series / f"{cfg['spec_code']}-{paper}",
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
    "\uf0c0": "",         # 2023-06/2025-11 covers: pentagons
    "\uf098": "",         # 2022-01/2023-01 covers: circles
    "\uf0bf": "",         # 2022-06 covers: diamonds
    "\uf0c2": "",         # 2024-11 covers: hexagons
    # 1CR tranche additions (2026-10-22, trace 1a162ea420f90a75) — each from a
    # PDF font trace + page render, eyeballed:
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
    # Physics (4PH1) tranche - first full-corpus physics wave (2026-10-26, trace
    # 1a17463dfb7c99c9): corpus PUA census physics-intake/pua-census.json, evidence
    # pass physics-intake/pua-evidence/ (font trace via PyMuPDF rawdict + page
    # render, eyeballed). 5 new codepoints; chemistry-era entries cover the rest.
    "\uf020": " ",        # CIDFont+F12/F9 blank glyph - renders as NOTHING: span
                          # '\uf050\uf020' (2021-11 1P MS p4) prints ONE tick + gap
                          # (tight render pua-evidence/TIGHT_*_p4.png), and
                          # '\uf0b4\uf0203.125' (p13) prints 'x 3.125' - it is the
                          # CID font's space; mapped to U+0020
    "\uf070": "\u03c0",   # pi - CIDFont+F7 2022-01 1P MS p11 'orbital speed =
                          # (2 x pi x 7100) / 5800' and SymbolMT 2023-06 1PR MS p5
                          # 'v = 2pi r/T'; renders eyeballed in both
    # --- igcse-maths-b-16 tranche-1 additions (run-004 union: the lane-collided
# --- CPs F068/F06a/F075 moved to SPECS pua_overrides; F020/F070 shared with
# --- the physics evidence above as single static entries) (2026-10-25, operator order trace
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
    "\uf084": "\u2264",   # less-than-or-equal (520 inst; spec-sqrt hypothesis
                          # OVERTURNED by pair evidence with F0B7-family >=)
    "\uf0b1": "\u00b1",   # plus-minus (392 inst, our-render+context-scaffold)
    "\uf0b9": "\u2260",   # not-equal (13 inst, our-render)
    "\uf0de": "\u21d2",   # rightwards double arrow (11 inst, our-render)
    "\uf07b": "{",         # Symbol brace-left (6 inst, our-render)
    "\uf07d": "}",         # Symbol brace-right (6 inst, our-render)
    # --- tranche-2 completion (2026-10-25): the REMAINING table.v1.json
    # --- entries — the PUA_MAP is now table.v1-complete (every entry carries
    # --- the T-MIG-141 rendered-PDF evidence trail; sha 1fdd4b4a). The
    # --- sequence-first law (run-002b ordering law) is implemented as the
    # --- _PUA_SEQ pre-pass below: composed shaft runs collapse to ONE arrow
    # --- before per-char mapping (SEQ-A: F075 shaft run + optional F072 head;
    # --- SEQ-B: F067 runs). Standalone leftovers then map per-char.
    "\uf028": "(",         # Symbol paren (242 inst)
    "\uf029": ")",         # Symbol paren (242 inst)
    "\uf02b": "+",         # Symbol plus (624 inst)
    "\uf02f": "\u0338",   # combining solidus — cancel stroke (55 inst)
    "\uf03d": "=",         # Symbol equals (819 inst)
    "\uf041": "A",         # Symbol A (1 inst, context-scaffold)
    "\uf053": "\u03a3",   # Symbol Sigma (1 inst)
    "\uf067": "\u2192",   # arrow (singles; runs consumed by _PUA_SEQ first, 41 inst)
    "\uf06c": "\u03bb",   # lambda (160 inst)
    "\uf06d": "\u03bc",   # mu (74 inst)
    "\uf06f": "\u00b0",   # degree (2 inst)
    "\uf071": "\u03b8",   # theta (3 inst)
    "\uf077": "\u03c9",   # omega (2 inst)
    "\uf085": "\u2265",   # greater-or-equal (34 inst)
    "\uf0a3": "\u2264",   # less-or-equal (127 inst)
    "\uf0a5": "\u221e",   # infinity (11 inst)
    "\uf0b3": "\u2265",   # greater-or-equal variant (51 inst)
    "\uf0b5": "\u221d",   # proportional to (13 inst)
    "\uf0b6": "\u21cc",   # equilibrium (1 inst)
    "\uf0bc": "\u2026",   # ellipsis (2 inst)
    "\uf0c6": "\u2205",   # empty set (2 inst)
    "\uf0c7": "\u2229",   # intersection (26 inst)
    "\uf0c8": "\u222a",   # union (3 inst)
    "\uf0cf": "\u2209",   # NOT AN ELEMENT OF — the operator-ruled mapping (run-004, trace 1a169e3fdeaecd11)
    "\uf0d0": "\u2220",   # angle (31 inst)
    "\uf0d7": "\u00b7",   # middle dot (8 inst)
    "\uf0db": "\u25ca",   # lozenge (1 inst)
    "\uf8eb": "\u239b",   # big paren LEFT-TOP, Symbol variant (32 inst)
    "\uf8ec": "\u239c",   # big paren LEFT-EXT, Symbol variant (32 inst)
    "\uf8ed": "\u239d",   # big paren LEFT-BOTTOM, Symbol variant (32 inst)
    "\uf8f6": "\u239e",   # big paren RIGHT-TOP, Symbol variant (32 inst)
    "\uf8f7": "\u239f",   # big paren RIGHT-EXT, Symbol variant (32 inst)
    "\uf8f8": "\u23a0",   # big paren RIGHT-BOTTOM, Symbol variant (32 inst)
    # --- tranche-2 drain additions (2026-10-25, each render-evidenced at
    # --- 150dpi on the staged paper of record, font-trace Symbol layout):
    "\uf021": "\u25b3",   # WHITE UP-POINTING TRIANGLE — 'Prove that \u25b3DAN is congruent
                          # to \u25b3CDM' (2025-10 01 p10 render eyeballed)
    "\uf04a": "\u03d1",   # GREEK THETA SYMBOL (script variant) — 'or tan \u03d1 =' distinct
                          # from F071's upright theta in the SAME MS (2025-06 01 p28:
                          # rows 'tan \u03b8' AND 'tan \u03d1', Notes '[\u03b8=16.35] / [\u03d1=73.649]')
    "\uf066": "\u03c6",   # phi — scalar parameter row 'OR = 3a + \u03c6("3a-3b")' (2026-06 02 p20)
    "\uf079": "\u03c8",   # psi — scalar parameter row 'OR = 3b + \u03c8("3a-3b")' (2026-06 02 p20)
    "\uf062": "\u03b2",   # beta — scalar parameter rows 'OR = 3b + \u03b2("3a-3b")' (2026-06 02 p20
                          # render) + 'OD = 2a + (a+2b) + \u03b2(a+2b)' (2025-10 01) + (2025-06 01)
    "\uf063": "\u03c7",   # chi — Notes 'eg AR = AM \u00b1 \u03c7 NM' (2026-06 02 p21 render eyeballed)
                          # two-variant-one-target precedent F0B3/F085->U+2265; 2024-06 01 p24
                          # render: 'MP = 3b + \u03c6("3a-5b")')
                          # (2024-11 02 QP p20 render: '0 < w \u2264 5' with a single space)
    "\uf0ec": "\u23a7",   # left curly hook TOP — the multi-row system brace '{ tan\u2220FEH=... /
                          # EH=...' (2024-06 02 MS p14 render eyeballed)
    "\uf0ef": "\u23aa",   # curly brace EXTENSION piece (both brace sides, same MS page render)
    "\uf064": "\u03b4",   # delta — 'PD = 1/5(3a-b) + \u03b4/(1-\u03b4)(a+2b)' (2025-10 01 p27 render)
    "\uf0bb": "\u2248",   # almost equal to — 'Allow (90/145)^2 = 324/841 \u2248 0.385'
                          # (2024-06 02R p15 render eyeballed)
    "\uf0ba": "\u2261",   # identical to — 'NB k + 215 + 362 + 181 + 94 + 15 \u2261 k + 867'
                          # (2023-06 01R p20 render eyeballed)
    "\uf065": "\u03b5",   # epsilon — 'CP = a - c + \u03b5(2a + c)' (2023-01 01R p22 render)
    "\uf06b": "\u03ba",   # kappa — 'OR = 2a + \u03ba("2a - 6/5 b")' (2026-06 02 p21 render)
    "\uf07a": "\u03b6",   # zeta — 'CP = \u03b6("21/10 a - 3/10 c")' (2023-01 01R p22 render)
    "\uf0ed": "\u23a9",   # left curly hook BOTTOM — the 2024-06 02 p14 system brace (render)
    "\uf05c": "\u2234",   # therefore - '"6 - 4kt" = 0 \u2234 t = 3/2k' (2021-06 01 p19 render)
    "\uf0a4": "\u211a",   # DOUBLE-STRUCK Q - '<\u211a> is the set of rational numbers'
                          # (2022-06 01 QP p6 Venn render; no conflicting class)
    "\uf0fd": "\u23ab",   # right curly hook TOP - 'eg {2\u03c0r\u00b2 and 2\u03c0(3r)\u00b2}' pair
                          # braces (2024-06 01R p18 render eyeballed)
    "\uf8e6": "|",         # modulus vertical bars - '|AC| = 5' pair around the vector
                          # (2020-11 01R QP p21 render eyeballed)
    "\uf0ee": "\u23a9",   # left curly hook BOTTOM (second variant) - system-brace row 2 left
                          # side '<F0EF><F0EE> cos(12.68...)' (2024-06 02 p14 render)
    "\uf0fe": "\u23ad",   # right curly hook BOTTOM - row 2 right side '<F0EF><F0FE>'
                          # (2024-06 02 p14 render eyeballed)
    "\uf8f1": "\u23a7",   # left curly hook TOP (compact brace class) - the
                          # '{(972/4500)^(1/3)}^2' scaffold (2018-06 01 MS p11 render)
    # F79: the SymbolMT digit embedding - 2020-01 02R MS p16 carries table
    # values wholly in PUA; the decode (F030->0, F02E->'.', F034->4, F037->7,
    # F02C->',') reproduces the printed row '- 0.47, 0.47, 2.53, 2.36' EXACT.
    # Standard Symbol layout 0x30-0x39 = 0-9; F02C comma, F02E period.
    "\uf02c": ",",
    "\uf02e": ".",
    "\uf030": "0", "\uf031": "1", "\uf032": "2", "\uf033": "3", "\uf034": "4",
    "\uf035": "5", "\uf036": "6", "\uf037": "7", "\uf038": "8", "\uf039": "9",
    "\uf8fc": "\u23ab",   # right curly hook TOP (compact brace class) - the same
                          # 2018-06 01 MS p11 scaffold's right side, sibling of F8F1
    "\uf8f4": "\u23aa",   # brace EXTENSION (both sides) - the taller 2018-06 01 p11
                          # scaffold's second expression carries it at both ends
    "\uf8fd": "\u23ac",   # right curly EXTENSION - the taller nested scaffold's right
                          # brace (2018-06 01 MS p11, 'F8EC F8F7 F8FD' context)
    "\uf8f2": "\u23a8",   # left curly EXTENSION - the same scaffold's left brace
                          # ('F8F2 F8EC F8F7 F8FD' context line)
    "\uf8f3": "\u23a9",   # left curly hook BOTTOM - 'F8F4 F8F3 F8ED 4500' (same
                          # scaffold; completes the F8F1-3 left curly trio)
    "\uf8fe": "\u23ad",   # right curly hook BOTTOM - '... F8F8 F8F4 F8FE' (same
                          # scaffold; completes the F8FC/FD/FE right curly trio)
}


# F64 (v0.16.0): spec §3.4 control-char policy — C0 controls that survive into
# served strings (the maths-B QP text layer carries the SymbolMT private-use
# operator class, e.g. 0x16-0x1F between numeric terms) fall back to a single
# space, logged per-instance here and disclosed in the validation report.
# NEVER silent. An operator-class adjudication (which controls are ×/÷ vs
# furniture) is a review-queue item until font-trace + render evidence lands.
CTL_COUNTER = {}

# F66: composed-run collapse laws (sequence-first, run-002b ordering law)
_PUA_SEQ = [
    (re.compile("[\uf075]{2,8}\uf072?"), "\u2192"),
    (re.compile("[\uf067]{2,8}"), "\u2192"),
]

def _ctl_note(cp):
    CTL_COUNTER[cp] = CTL_COUNTER.get(cp, 0) + 1

# run-004 union: per-run lane state, set in main() from the SPECS entry.
# normalize_pua reads these; chemistry/physics runs leave the overrides
# empty and the census off — byte-identity with v0.19.0 preserved.
ACTIVE_PUA_OVERRIDES = {}
ACTIVE_SPEC_CODE = "4ch1"
ACTIVE_FOOTER_RE = None   # per-run lane footer, set in main() (clean_lines anchor)


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
    # F64: spec §3.4 control-char fallback (logged, disclosed in the report).
    # run-004 union: lane-scoped to 4mb1 — the branch census ran on maths-B
    # texts; chemistry carries ZERO C0 controls of record and physics/chemistry
    # must keep v0.19.0 behavior byte-exactly.
    if (ACTIVE_SPEC_CODE == "4MB1"
            and any((ord(c) < 0x20 and c not in "\t\n\r\x0c") for c in s)):
        s = "".join((_ctl_note(hex(ord(c))) or " ") if (ord(c) < 0x20 and c not in "\t\n\r\x0c") else c
                    for c in s)
    if not any(0xE000 <= ord(c) <= 0xF8FF for c in s):
        return s
    # F66 (v0.16.1): sequence-first law (run-002b ordering law) — composed
    # arrow runs collapse to ONE arrow before per-char mapping. SEQ-A: a run
    # of F075 shaft glyphs (2-8, drawn width varies) optionally terminated by
    # the F072 head = one rightwards arrow; SEQ-B: F067 runs. A STANDALONE
    # F072 is Delta (U+0394) and still maps per-char below — the font-split
    # that dissolved the OEQ-Delta conflict.
    for rx, rep in _PUA_SEQ:
        s = rx.sub(rep, s)
    # F66: igcse-maths-b-16 course overrides — the maths-B SymbolMT embeddings
    # re-encode two codepoints the chemistry/4MA1 embeddings use differently
    # (the run-002b font-split class, per-course law with render evidence):
    #   F061: the mapsto class ('f : x \u21a6 ...', 85 census instances, the
    #         standard function-definition notation) keeps U+21A6; every OTHER
    #         maths-B instance is the scalar parameter alpha (2023-01 01R p22
    #         'minus 2\u03b1 = -3 + \u03b2'; 2021-01 01 p18 'sin(\u03b1) = 63.5...' renders).
    #   F067: gamma course-wide (2026-06 02 p21 'OR = b + \u03b7...\u03b3(2a-b)', 2023-01 01R
    #         p22 '1 + 2\u03b3 = \u03b4', 2025-10 01 p27 'PD = \u03b3/(1-\u03b3)(a+2b)' renders);
    #         the DB's arrow evidence for F067 belongs to the 4MA1 run-head
    #         embeddings (SEQ-B family, consumed above). One 2019-06 01R
    #         instance is a tiny unresolved superscript square at 600dpi —
    #         served as \u03b3, disclosed low-confidence in the ledger.
    if ACTIVE_SPEC_CODE == "4MB1":
        s = re.sub(r"(?<=x )[]", "\u21a6", s)
        s = s.replace("", "\u03b3")
        s = s.replace("", "\u03b1")
        # F69: number-set symbols (the Venn-diagram class). The maths-B
        # embeddings encode the double-struck set letters at F0A5/F0A2/F0A4
        # (2022-06 01 QP p6: 'the sets \u2115, \u2124, \u211a and E' + the legend
        # '\u211a is the set of rational numbers'). The DB-corpus evidence for
        # F0A5 (infinity) and F0A2 (the dotted answer-line rule, 5,146 inst)
        # belongs to OTHER embeddings. LINE-SCOPED law anchored on the
        # unambiguous \u211a: a line carrying F0A4 is a set-notation line, so
        # F0A5->\u2115 and F0A2->\u2124 there; elsewhere the older mappings stand.
        if "\uf0a4" in s:
            s = s.replace("\uf0a5", "\u2115").replace("\uf0a2", "\u2124")
            s = s.replace("\uf0a4", "\u211a")
    out = []
    for c in s:
        cp = ord(c)
        if 0xE000 <= cp <= 0xF8FF:
            if c in ACTIVE_PUA_OVERRIDES:
                out.append(ACTIVE_PUA_OVERRIDES[c])
            elif c not in PUA_MAP:
                raise ValueError(
                    f"unmapped PUA char U+{cp:04X} in {s[:80]!r} — add an evidenced "
                    f"PUA_MAP entry (font trace + page render) before running")
            else:
                out.append(PUA_MAP[c])
        else:
            out.append(c)
    return "".join(out)


# ---------------------------------------------------------------- v0.17.0: G0-D cover probes
# The archive's 2026-10-02 corpus-fix wave (F-A2) staged six wrong Pearson-DAM
# artifacts as qp.pdf (four 'rms' mark schemes, two 'pef' examiners' reports:
# 2022-01/2023-01/2023-06 4PH1-1P, 2022-01/2022-06/2023-06 4PH1-2P). Their
# manifest sha256s faithfully describe those bytes, so the sha check cannot see
# the defect — only the document's own cover can. G0-D probes the first two
# pages of each PDF for a foreign cover type. Fail-disclosed: a hit fails G0
# with the defect class in the summary; a clean probe adds NOTHING to the
# receipt, so green lanes' validation-reports stay byte-identical (the Task-12
# no-op standard). Rasterized covers (no text layer, the 2019-06 scans) carry
# no evidence either way and are skipped.
MS_COVER_RE = re.compile(r"Mark\s+Scheme", re.I)
ER_COVER_RE = re.compile(r"Examiners?[\u2019']?\s+Report", re.I)
QP_COVER_RE = re.compile(
    r"Question\s+Paper(?!\s+Log\s+Number)|Paper\s+Reference|Instructions\s+Use|"
    r"Please\s+check\s+the\s+examination\s+details", re.I)
# NB the (?!\s+Log\s+Number) guard: MS covers print the sister document's
# "Question Paper Log Number PxxxxxxA" furniture line (the 1P 2023-06 DAM
# mislabel sailed through the first probe exactly this way). A real QP cover
# never carries that line.


def _cover_text(pdf_path: Path, pages: int = 2) -> str:
    """First-pages text for the G0-D probe; '' when rasterized/unopenable —
    no evidence either way, the probe skips (fail-open ONLY on absent text,
    never on a detected foreign cover)."""
    try:
        doc = fitz.open(pdf_path)
    except Exception:
        return ""
    try:
        return " ".join(doc[i].get_text() for i in range(min(pages, len(doc))))
    except Exception:
        return ""
    finally:
        doc.close()


# F89 (v0.21.1): restore flattened standard-form exponents ("× 1023" -> "× 10²³").
# pdftotext drops superscript sizing; the QP/MS of record prints 10²³. Validity
# rule keeps the legit multipliers × 100 / × 1000 (exponent 0 / 00) and refuses
# out-of-range tails like "× 1050" that are plain numbers, not exponents.
_SUP = str.maketrans("0123456789-−", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁻")
def restore_flat_exponents(s: str) -> str:
    def _r(m):
        sign, d = m.group(1), m.group(2)
        if not (sign or (d[0] != "0" and (len(d) == 1 or 20 <= int(d) <= 29))):
            return m.group(0)
        return "× 10" + (sign or "").translate(_SUP) + d.translate(_SUP)
    return re.sub(r"×\s?10(-|−)?(\d{1,3})\b", _r, s)


FURNITURE_SUBS = [
    (re.compile(r"\*P\d{5}[A-Z]\w*\*"), " "),       # page identity marker (P62045A*, P58561A*, ...)
    (re.compile(r"\bTurn over\b"), " "),
    (re.compile(r"DO NOT WRITE IN THIS (?:AREA|MARGIN|SPACE)\s*"), " "),   # often 3x on one line
    # v0.18.0 (F70): BEL U+0007 — the pdftotext artifact behind numbered method
    # steps ("Step 1 \x07add 25 cm3"). Removed EXACTLY like the exporter's
    # _bulletize control-char strip (drop, no space inserted), so the served
    # stems are byte-identical before/after this fix; the strip runs here AND on
    # the page_norm index (below) so part->page anchoring probes stay consistent.
    (re.compile("\x07"), ""),
    (re.compile("\x08"), ""),   # F88: backspace artifact (2024-06 2C group stem "+\x08–")
    # F74 (v0.16.0): maths-B page furniture — the multi-page question continuation
    # header and the printed formula scaffold in the answer space (the quadratic
    # formula box every 4MB1 paper prints; 2025-11 Q5 leak eyeballed). Neither
    # string occurs anywhere in the chemistry corpus (census 2026-10-25: 0 hits
    # in the staged 2020-11 baseline layer), so the parity surface is unchanged.
    (re.compile(r"\bQuestion \d{1,2} continued\b"), " "),
    # F87 (v0.21.1): the multi-page QP footer — "QUESTION 11 CONTINUES ON NEXT /
    # BACK PAGE" in 5 print shapes (caps / mixed case / no number / slash form /
    # trailing period). Census 2026-10-26 (hygiene-v2): 9 chemistry instances
    # corpus-wide, all in problem_md; the v0.18.0 battery never enumerated the
    # QP footer universe (F87 lesson, AGENTS.md standing rule 3).
    (re.compile(r"\bQUESTION\s*\d{0,2}\s*CONTINUES\s+ON\s+(?:THE\s+)?(?:NEXT|BACK)(?:\s*/\s*(?:NEXT|BACK))?\s+PAGE\.?", re.I), " "),
    # F87 (v0.21.1): the abbreviated question-total footer ("Total for Q1 = 5") —
    # the v0.18.0 battery only matched the spelled-out "Question" word order.
    # v0.30.1 (F88 reconciliation's remaining half, the F111 furniture-residue
    # class): the printed footer line ends '... = 8 marks' — the incomplete
    # match consumed 'Total for Q3 = 8' and left the ' marks' tail, which the
    # raw layer carried into the assembled solution text as a lone 'marks'
    # line (2020-11 1C 3(c)(ii): the F111 census's ONE fresh-vs-record
    # disagreement). The tail belongs to the footer verbatim; the sibling F93
    # sub already consumes its own marks suffix. The F88 wrap-ambiguous keep
    # class (bare answer/mark/marks/Number lines) is NOT touched by this —
    # those lines are wrapped guidance fragments, never footer tails.
    (re.compile(r"\bTotal\s+for\s+Q\d{1,2}\s*=\s*\d{1,3}(?:\s+marks)?\b"), " "),
    # F93 (v0.23.0): the third word order of the same footer — "Total for question
    # = 15 marks" (number AFTER the equals, "question" spelled out). Found by the
    # Task 19 deep-audit re-run reconciliation (2022-01 1C Q9 leak into
    # solution_md tail); the F87 pair covers only the Q<digits> and
    # "Question <digits> =" orders. Census: 1 staged instance (2022-01 1C MS).
    (re.compile(r"\bTotal\s+for\s+question\s*=\s*\d{1,3}\s*marks\b", re.I), " "),
    # F92 (v0.23.0): the tick-glyph mojibake — the printed tick (the F48/F033
    # mapping family) surfaces in the QP text layer as Latin-1 'ü' inside the
    # instruction "Add/Place ticks (ü) in/to the table". Scoped to the exact
    # instruction phrase: a bare 'ü' sub would also rewrite PRINTED table-cell
    # ticks (2025-11 2C 1(a) carries one in the printed grid, where the glyph is
    # question content, not mojibake). Census: 3 instruction instances corpus-wide
    # (2025-06 2C 5(c)(i), 2025-11 2C 1(a), 2026-06 2C 2(d)(i)) + 1 printed-cell
    # instance deliberately left verbatim.
    (re.compile(r"(?<=\bticks\s\()ü(?=\))"), "✓"),
]
FURNITURE_LINE = [
    re.compile(r"^\s*PMT\s*$"),                     # archive watermark
    re.compile(r"^\s*BLANK PAGE\s*$"),
    re.compile(r"^\s*DO NOT WRITE IN THIS (AREA|MARGIN|SPACE)\s*$"),
    re.compile(r"^\s*\d{1,2}\s*$"),                 # bare page number (1..36) — see the F90
    # geometry rule below: inside the MS stream (keep_bare_numerals=True) a bare
    # digit at an ANSWER/NOTES-cell column is preserved (F108 leg 1), so this
    # pattern effectively strips page numbers, question-column numerals and
    # marks-column digits only.
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


# F108 leg 0: marker-row pattern for the marks-digit adjacency guard —
# an MS line opening with a part marker ('5 (c)', '(b) (i)', '2 (a) (i)').
MS_MARKER_ROW_FOR_DIGIT = re.compile(r"^\s{0,8}\d{0,2}\s*\([a-z]{1,2}\)\s*\S")


def _ms_header_columns(raw_lines):
    """F108 leg 0 (F90 support): per-line MS table geometry.

    Walks the raw MS text and, for every line index, records the x-columns of
    the most recent printed table header (the 'Answer   Notes   Marks' band
    every MS page repeats — F42). The printed header x-positions are the only
    reliable discriminator between a bare digit that is PAGE/MARKS furniture
    and one that is ANSWER-CELL content (the F90 class): a standalone digit
    whose column sits left of the Marks column and right of the Question
    column is inside the answer/notes cell region.

    Returns {line_index: (x_answer, x_marks)} for lines that sit under a known
    header (entries absent = no header seen yet -> fail-closed stripping)."""
    header_rx = re.compile(r"^(?P<lead>\s*)(?P<ans>Answer)\s{2,}(?P<mid>.+?)?\s{2,}(?P<marks>Marks)\s*$")
    cols: dict = {}
    cur = None
    for i, ln in enumerate(raw_lines):
        m = header_rx.match(ln.rstrip("\n"))
        if m:
            x_ans = m.start("ans")
            x_marks = m.start("marks")
            cur = (x_ans, x_marks)
        elif re.match(r"^\s*Question\s*$", ln) or re.match(r"^\s*number\s*$", ln):
            pass  # the trio's other rows; geometry unchanged
        cols[i] = cur
    return cols


def clean_lines(raw: str, keep_bare_numerals: bool = False):
    """F75: keep_bare_numerals preserves COLUMN-0 bare numeral lines ('6' —
    the MS question numeral whose Working cell wrapped to the next line,
    2021-06 1MS). INDENTED bare numerals (page footers, col 17+) strip in both
    streams; a col-0 numeral in the QP is a top-of-page continuation marker
    and keeps stripping there — the flag is passed by the MS parse only.

    F108 leg 0 (v0.28.0, closes the F90 queued converter pass): inside the MS
    stream the bare `^\\d{1,2}$` FURNITURE_LINE strip becomes GEOMETRY-AWARE.
    The printed MS header band's x-columns split each page into the Question
    region (left of Answer), the Answer/Notes cell region, and the Marks
    column. A bare 1-2 digit line is page/marks furniture (stripped, unchanged
    behavior) EXCEPT when its column sits inside the Answer/Notes cell region
    of the page's most recent header — there it is an MS ANSWER VALUE the
    printed table carries (the F90 class: 2021-06 1C 2(b)(ii) '25' family),
    and it is preserved so the extraction matches the printed MS. The Marks
    margin is 12 columns (measured: printed marks digits sit 8-12 columns
    left of the header 'Marks' x — 2020-01-1C 7(b)(i) '2' @ col 88 vs header
    98; content divisors sit deep inside the answer cell — the ÷3/÷7/÷2
    fraction denominators at cols 27-32, 2021-01-1C 11(b)(i) 'except 1' at
    col 79). Lines with no header above them strip unchanged (fail-closed)."""
    raw_line_list = raw.splitlines()
    header_cols = _ms_header_columns(raw_line_list) if keep_bare_numerals else {}
    out = []
    for idx, ln0 in enumerate(raw_line_list):
        ln = normalize_pua(ln0)   # F48: symbol-font PUA -> real Unicode before any parsing
        for rx, rep in FURNITURE_SUBS:
            ln = rx.sub(rep, ln)
            # v0.32.0 (F117): case-robust lane gate. main() sets
            # ACTIVE_SPEC_CODE = cfg["spec_code"] == "4CH1" (line ~2671), so the
            # v0.21.1 lowercase check `== "4ch1"` NEVER fired in any real
            # conversion — the F89 restore law was dead code in every run since
            # the spec_code value became uppercase. Fresh emissions re-flattened
            # every restored superscript (the F111 class-2 exponent universe:
            # 23 parts / 51 fields; C95 red on every fresh tree, F86/F116).
            # Diagnosed 2026-10-29: instrumented run showed ACTIVE_SPEC_CODE
            # == '4CH1' inside main(); blast-radius census: the of-record
            # carries 414 sup chars and ZERO flat law-fireable instances, so
            # re-activation reproduces the of-record exactly and cannot mint
            # new deltas. The lane gate stays (physics C74 pin of record
            # carries flat forms — 4PH1 decides its own tranche; maths-B has
            # its own conventions).
            if (ACTIVE_SPEC_CODE or "").lower() == "4ch1":
                ln = restore_flat_exponents(ln)  # F89 (v0.21.1) — chemistry-gated; other lanes pending their own census (physics C74 pin of record carries flat forms)
        # F108 leg 2: the MS stream keeps (collapsed) blank lines — the printed
        # grid's blank row separators are layout information the Finding-5 box
        # parser needs (the 2023-06 1CR 4(a) grid delimits rows with blanks);
        # downstream consumers already skip empties (build_solution drops them).
        # MUST run before the FURNITURE_LINE check, which drops `^\s*$` lines.
        if keep_bare_numerals and not ln.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        if any(rx.match(ln) for rx in FURNITURE_LINE):
            if (keep_bare_numerals and ln and ln == ln.strip()
                    and re.fullmatch(r"\d{1,2}", ln.strip())):
                # F75: col-0 MS question numerals survive unchanged (the
                # Working-cell-wrap law), ...
                pass
            elif (keep_bare_numerals
                  and re.fullmatch(r"\s*\d{1,2}", ln)
                  and not (out and MS_MARKER_ROW_FOR_DIGIT.match(out[-1]))
                  and (lambda c: c is not None and c[0] - 8 <= len(ln) - len(ln.lstrip())
                       and len(ln) - len(ln.lstrip()) < c[1] - 12)(header_cols.get(idx))):
                # F108 leg 0 (F90): an indented bare digit inside the printed
                # Answer/Notes cell region is MS answer content — preserve it.
                # EXCEPT when it directly follows a marker row: pdftotext splits
                # the marker's printed marks digit onto its own line there
                # (2020-11 1C 5(c): '(c) Explanation including' + '2') — layout,
                # not answer content.
                pass
            else:
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
            if re.match(r"^\(\d{1,2}\)$", prev.strip()) and ACTIVE_FOOTER_RE.search(nxt):
                i += 1
                continue
        res.append(out[i])
        i += 1
    return res


# ---------------------------------------------------------------- stage 2: segmentation
# v0.16.0: the per-lane footer law lives in SPECS[<spec>]["footer_re"]; the
# module constant below is kept only as the chemistry-of-record reference.
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
        elif (m and len(choices) == 3 and expect == 3
              and m.group(1) == choices[0]["label"]
              and ACTIVE_SPEC_CODE == "4PH1"):
            # v0.21.0 (F85): the QP print-defect class — the FINAL row of a
            # 4-option run repeats the FIRST label. 2020-01 1PR 1(b) prints
            # 'A S' where the run is A/B/C/D-S; the MS of record keys the
            # block AND its rebuttal row names 'D is incorrect as arrow S',
            # corroborating the intended label. The canonical printed run is
            # A–D, so a repeat of choices[0]'s label at expect==3 completes
            # the run in exactly one way: relabel to the next expected letter
            # and disclose (value_trace.choices, LEDGER F85, C90). The row
            # previously leaked into problem_md and the run served short
            # (labels A–C). Corpus census (the F85 wave, 53 slices): exactly
            # 1 instance. The '_relabel' marker rides the choice record only
            # as far as the provenance block, which pops it into
            # value_trace.choices — it never serializes.
            choices.append({"label": chr(65 + expect), "text_md": m.group(2).strip(),
                            "_relabel": m.group(1)})
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
    # v0.21.0 (F85): the structural choice-bearing class — a printed option
    # run on a part carrying >=2 marks is NOT a single-select MCQ. Corpus law
    # (the F85 wave census, 53 slices, 138 option-run parts): every true 4PH1
    # MCQ prints exactly 1 mark; the marks>=2 exceptions are exactly the
    # mis-typed structural shapes — 2023-06 2PR 7(a) place-ticks-in-the-table
    # (2 marks), 2022-06 2PR 1(a) draw-matching-lines (4), 2026-06 1PR 1(a)
    # name-the-object answer lines (4). Serving them as MCQs produced a FALSE
    # key (7(a)'s compound tick rule 'C and D ticked...' keyed C 500 Hz) and
    # dot-run answer lines served as choice texts. The rows stay in the
    # problem text verbatim; the part types structured and links its MS block
    # through the ordinary G5 lane. 4PH1-gated: chemistry/4MB1 outputs are
    # bit-identical by construction (parity receipt, C-pin battery).
    if (choices and ACTIVE_SPEC_CODE == "4PH1"
            and marks is not None and marks > 1):
        choices, consumed = [], set()
    if choices:
        kept = [ln for i, ln in enumerate(kept) if i not in consumed]
    source_norm = norm(strip_dotrun(" ".join(kept)))   # final ground truth (marks + options removed)

    text = strip_dotrun(re.sub(r"\s{2,}", " ", " ".join(kept))).strip()
    glue = glue_candidates(kept) if marks is None else []
    return {"marks": marks, "choices": choices, "problem_md": text, "source_norm": source_norm,
            "_kept": kept, "_glue_cands": glue}


# --- F73a (maths-B): text-glued QP marks markers -----------------------------
# The QP prints each part's marks as a right-column '(N)'. In the archive text
# layer of the first-sitting-era papers the marker is GLUED into the problem
# text at phrase seams — mid-line ('diagram (3)for the sets', 'on(1)the number
# line', '(5) (4x + 3)(2x - 1) < ...') or at the START of a wrapped line
# ('(1) be excluded from any domain', '(3)h-1 in the form', '(5)a + sqrt(b)')
# — so MARK_RE (a bare '(N)' line) and the trailing-'(N)$' fallback cannot see
# it. Candidate rule (evidence-derived, 2019-06 02R corpus): a bare-digit paren
# group 1..12 is a candidate iff (a) it is NOT a function application — the
# preceding character is not a letter (gf(4), h(3) are content) — or (b) it is
# letter-preceded AND followed immediately by a lowercase letter (the direct
# glue 'on(1)the'). Candidates are only COLLECTED here; the fill decision is
# the question-level footer sum law (F73a post-pass below), fail-closed.
GLUE_MARK_RE = re.compile(r"\((\d{1,2})\)")


def glue_candidates(kept):
    cands = []
    for li, ln in enumerate(kept):
        for m in GLUE_MARK_RE.finditer(ln):
            n = int(m.group(1))
            if not (1 <= n <= 12):
                continue
            prev_ch = ln[m.start() - 1] if m.start() else ""
            next_ch = ln[m.end()] if m.end() < len(ln) else ""
            if prev_ch.isalpha():
                if next_ch.islower():          # direct glue: 'on(1)the'
                    cands.append({"value": n, "line": li, "start": m.start(), "end": m.end()})
                continue                        # letter-preceded otherwise: gf(4) class
            if (not prev_ch or not prev_ch.isalpha()) and not next_ch.isdigit():
                cands.append({"value": n, "line": li, "start": m.start(), "end": m.end()})
    return cands


def _f73_unique_assignment(target, cands_per_part):
    """Exact-cover: per unresolved part choose one candidate value (or None)
    so the values sum to `target`. Returns the UNIQUE value tuple, else None
    (0 or >=2 assignments = fail-closed to the patch path / review)."""
    sols = []

    def dfs(i, rest, acc):
        if len(sols) > 1:
            return
        if i == len(cands_per_part):
            if rest == 0:
                sols.append(tuple(acc))
            return
        for v in [None] + sorted(set(c["value"] for c in cands_per_part[i])):
            if v is None or v <= rest:
                dfs(i + 1, rest - (v or 0), acc + [v])

    dfs(0, target, [])
    return sols[0] if len(sols) == 1 else None


# ---------------------------------------------------------------- stage 3: MS linkage
MS_ROW_RE = re.compile(
    r"^ {0,20}(?:(\d{1,2})\s+)?(?:\(([a-h])\s*\)\s*)?(?:\(([Ii]{1,3}|[Ii][Vv]|[Vv]|[Vv][Ii]{1,3})\s*\)\s*)?(\S.*)$")
# F42 marker-column gate: marker rows sit in the MS table's marker column
# (indent <= 12 in every observed layout); the answer column starts deeper.
# Without the gate, answer-cell fragments like the unit '(g)' hijack the
# marker state (2019-06: '(g)' after 14(f)(i) re-pointed cur_letter to 'g'
# and 14(f)(ii) became unlinkable).
MS_QNUM_ONLY_RE = re.compile(r"^ {0,20}(\d{1,2})\s*$")
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
# F68 (v0.16.1): the glued QUESTION-NUMBER + paren-letter marker - the
# 2022-01..2023-06 maths-B MS layouts print '6(a)   AB = 5b - 4a ...' (digit
# and paren-letter glued; MS_ROW_RE requires whitespace after the digit so it
# never matched, and MS_GLUED_MARKER_RE expects a bare letter). Optional
# roman sub-part, parened or bare.
MS_QPAREN_GLUED_RE = re.compile(
    r"^ {0,12}(\d{1,2})\(([a-h])\)(?:(i{1,3}|iv|v|vi{1,3})|\((i{1,3}|iv|v|vi{1,3})\s*\))?(?=\s{2,}|$)\s*(.*)$")
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
    for MCQ keying: answer rows vs 'X is incorrect' note rows).

    F75: a NUMERAL-ONLY row ('6' alone — the Working cell wrapped to the next
    line in the 2021-06 1MS table) is a question marker when it advances the
    strict sequence (cur_q + 1). Only column-0 bare numerals reach this law —
    clean_lines keeps them for the MS stream exclusively; INDENTED bare
    numerals (page footers, lone answer-column fragments) strip as furniture,
    so no answer-fragment hijack class exists."""
    entries = {}
    cur_q, cur_letter = None, None
    cur = None
    last_roman = {}   # F42: (q, letter) -> index into ROMAN of the last marker roman
    TOTAL_RE = re.compile(r"^\s*Total\s+\d+\s*$")
    # v0.18.0 (F69): the MS prints page-bottom furniture at the end of every
    # question block — the question-total footer (two printed word orders:
    # '(Total for Question 7 = 6)' and 'Total marks for Question 7 = 10'), the
    # paper-total line ('Total for Paper = 70 marks'), and the closing Pearson
    # copyright block ('Pearson Education Limited. Registered company number
    # 872828' + 'with its registered office at 80 Strand, ...'). parse_ms
    # treated all of it as content of the last open entry, so the furniture
    # leaked into the corpus's final-question answer blocks (first census pass:
    # 53 question-total lines; the full census: +60 total lines in the second
    # word order / paper-total shapes, +96 Pearson copyright lines, + the bare
    # 'Total = N' fragment shape the 2025-06 2CR layout prints — 42+ mark
    # points served that furniture before this fix, G8 audit §4 #1 class).
    # The text layer truncates/case-drifts the lines, so the skips accept every
    # observed shape (case-insensitive; the marks digit accepts 1-3 digits for
    # the paper total) and NOTHING else. The vertical lane already skips its
    # own strict form (MS_V_TOTAL_RE) — chemistry's row lane is the leak. Two
    # footer-only blocks exist corpus-wide — 2021-01 2CR 7(d) (the printed MS
    # answer cell is an IMAGE) and 2025-06 2CR 7(c)(ii) (the parser had linked
    # the footer block while the printed answer 'ethyl ethanoate' sits in the
    # continuation row the row-parser mis-attributed) — both dispositioned
    # through the F47 MS-LINK-OVERRIDES ledger with eyeballed verbatim
    # transcriptions, pinned by canaries C80/C81/C82.
    MS_FOOTER_LINE_RE = re.compile(
        r"^\s*\(?\s*Total\s+(?:marks\s+)?for\s+(?:Question\s+\d{1,2}|Paper)\s*=\s*\d{1,3}\)?\s*(?:marks?)?\s*\)?\s*$"
        r"|^\s*\(?\s*Total\s*=\s*\d{0,3}\)?\s*(?:marks?)?\s*\)?\s*$",
        re.I)
    PEARSON_COPYRIGHT_RE = re.compile(
        r"^\s*Pearson\s+(?:Education\s+Limited|Edexcel)\b", re.I)
    PEARSON_OFFICE_RE = re.compile(
        r"^\s*with\s+its\s+registered\s+office\b", re.I)

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

    skip_office_next = False
    prev_line = ""
    for ln in ms_lines:
        prev_line = ln
        if TOTAL_RE.match(ln) or MS_FOOTER_LINE_RE.match(ln):
            continue
        if PEARSON_COPYRIGHT_RE.match(ln):
            skip_office_next = True      # the copyright block's office line follows
            continue
        if skip_office_next and PEARSON_OFFICE_RE.match(ln):
            skip_office_next = False
            continue
        skip_office_next = False
        mq = MS_QNUM_ONLY_RE.match(ln)
        if mq:
            # F75: the numeral reached parse_ms ONLY because clean_lines kept
            # it (col-0 bare numeral, MS stream) — indented bare numerals (page
            # footers, answer-column fragments) never survive furniture, so
            # the ascending law alone is the guard here.
            v = _honour_qn(mq.group(1), False)
            if v is not None and cur_q is not None and v == cur_q + 1:
                cur_q = v
                cur_letter = None
                cur = (cur_q, None, None)
                entries.setdefault(cur, [])
                continue
        mo = MS_MARKER_ONLY_RE.match(ln)
        m = MS_ROW_RE.match(ln)
        mb = MS_BARE_LETTER_RE.match(ln)
        mdm = MS_DEGRADED_MARKER_RE.match(ln)
        mg = MS_GLUED_MARKER_RE.match(ln)
        mqp = MS_QPAREN_GLUED_RE.match(ln)
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
        elif mqp:
            # F68: glued '<qnum>(<letter>)' marker - the same state machine as
            # the mg branch: marker evidence wins, the ascending-sequence gate
            # in _honour_qn applies, and the roman sub-part is optional.
            qn, letter, roman, roman_paren, rest = mqp.groups()
            roman = (roman or roman_paren).lower() if (roman or roman_paren) else None
            new_q = _honour_qn(qn, True)
            if new_q is not None:
                cur_q = new_q
            cur_letter = letter
            key = (cur_q, letter, roman)
            entries.setdefault(key, [])
            if rest.strip():
                entries[key].append(rest)
            cur = key
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
    # F108: trim leading/trailing blank lines from every entry (interior blanks
    # survive — the Finding-5 grid parser needs them). The MS-LINK-OVERRIDES
    # law keys on `not lines` (the image-cell 2019-06 3(d)(ii) case): an entry
    # whose only lines are stripped blanks must stay FALSY so the override
    # still applies.
    for k in entries:
        es = entries[k]
        while es and not es[0].strip():
            es.pop(0)
        while es and not es[-1].strip():
            es.pop()
    return entries


# ---------------------------------------------------------------- stage 3b: MS linkage (vertical lane)
# v0.17.0 (4ph1): the physics MS text layer is a CELL-PER-LINE table — pdftotext
# and PyMuPDF both render every table cell on its own line at indent 0, so the
# row-shaped chemistry parser (parse_ms) has nothing to grip: '1' and '(a)'
# arrive as bare lines, marks digits are indistinguishable from question
# numbers by shape alone, and clean_lines strips every bare numeral as page
# furniture before parse_ms even runs (2024-06 2P: G5 linkage 0%).
# parse_ms_vertical takes the RAW layer (clean_lines is bypassed for this lane)
# and runs a header-anchored state machine. Separate function — chemistry's
# parse_ms is untouched, bit-identity by construction:
#   page-header run  ('Question' ['number'] 'Answer' 'Notes' 'Marks', one
#     token per line) ARMS the parser: the next bare-numeral line is the
#     question-number marker, accepted under the same strictly-ascending law
#     as parse_ms's _honour_qn (bootstrap at 1, then cur_q or cur_q+1 — a
#     continuation page's first marks digit can never hijack the sequence);
#   a bare numeral elsewhere is the MARKS digit of the currently open entry —
#     layout, not answer: stored in the ms_marks map (first-wins), never
#     appended to content, never printed in solution_md;
#   '(a)' alone opens a letter entry; '(i)' alone opens a roman entry under
#     the same ascending-sequence invariant as the chemistry parser;
#   'Total for Question N = X marks' is the question footer (skipped);
#   everything else is content of the open entry (furniture pass drops PMT /
#     blank / cover matter, which has no open entry and cannot leak).
MS_HEADER_TOKENS = {"question", "number", "question number", "answer", "notes", "marks"}
MS_V_TOTAL_RE = re.compile(r"^Total for Question \d{1,2} = \d{1,2} marks$", re.I)
MS_V_BARE_NUM_RE = re.compile(r"^(\d{1,2})$")
# v0.18.0: inner-space tolerance '(\s*a\s*)' — the corpus census found 4 rows
# where the letter cell carries stray padding ('(a )' shapes via pdftotext).
MS_V_PAREN_LETTER_RE = re.compile(r"^\(\s*([a-h])\s*\)$")
MS_V_PAREN_ROMAN_RE = re.compile(r"^\((i{1,3}|iv|v|vi{1,3})\)$", re.I)
# v0.17.0 (1P 2024-06 probe): the same layout family occasionally GLUES the
# question number and the letter marker onto one row — '3 (a)' (observed once,
# Q3 of the 1P 2024-06 MS; the 2P sample kept '3' / '(a)' separate). Marker
# evidence (letter on the row) follows parse_ms._honour_qn gate (a): it wins
# over the sequence, so a legitimately skipped question number can never
# derail the file. The letter+roman sibling ('(b) (i)') is added for the same
# positional family before any future series run needs it.
MS_V_GLUED_QN_LETTER_RE = re.compile(r"^(\d{1,2})\s+\(([a-h])\)\s*(.*)$")
MS_V_GLUED_LETTER_ROMAN_RE = re.compile(r"^\(([a-h])\)\s*\((i{1,3}|iv|v|vi{1,3})\)\s*(.*)$", re.I)
# v0.17.0 (1P 2024-06 probe): roman marker GLUED to its answer content on one
# row — '(iii) substitution into P = E/t;' (7(b)(iii); the sibling parts kept
# '(iii)' bare). Same ascending-sequence gate as the bare form: a content line
# that merely opens with a roman-shaped token can never hijack a marker.
MS_V_GLUED_ROMAN_CONTENT_RE = re.compile(r"^\((i{1,3}|iv|v|vi{1,3})\)\s+(\S.*)$", re.I)
# v0.18.0 (MS-table parser wave, 53-slice corpus census receipted in
# physics-intake/ms-forensics/): three further marker-row families the
# vertical layer carries that v0.17.4 lost — each proven by census counts
# over all 53 landed 4PH1 slices before a line of this was written:
#   triple rows '4 (a)   (i)   A (friction);  [marks]' — qn+letter+roman+
#     content on ONE row (175 rows). v0.17.4's qn+letter rule fired first and
#     swallowed the roman marker into the entry's content, so roman parts
#     never existed and their MCQ answer cells came out polluted.
#   letter+content rows '(b)   galaxy;   allow named galaxy  [marks]' — the
#     letter marker with its answer/notes text glued to it (842 rows).
#     v0.17.4 matched nothing and appended the WHOLE row to the previous
#     entry's content, losing the letter entry entirely — the single largest
#     linkage-loss class (2024-06 2P missed 1(b)/2(b)/3(b)/5(b)/7(b) exactly
#     this way).
#   qn+content rows '8   any six from:   [marks]' — the question number
#     glued straight to answer content with NO letter cell (2024-06 1P Q8;
#     v0.17.4 appended the row to the previous question's last entry and the
#     whole question vanished). Acceptance is DELIBERATELY strict — ALL of:
#     the ascending-question law, a trailing marks-column digit (2+ spaces
#     then 1-2 digits, line-end), and column-0 placement in the RAW line —
#     because numeric answer lines share the stripped shape ('39 000 = 0.45
#     × c × 49', '2 marks max.'): 181 of 198 corpus rows in this family are
#     plain content, and 0 of the indented ones carry the tail signature.
# Continuation semantics for every glued opener (incl. the v0.17.0 qn+letter
# form): when the entry key already exists (multi-page continuations re-print
# the marker row), the row's own content APPENDS to the existing block —
# v0.17.4's setdefault silently dropped a re-printed marker row's content.
# parse_ms_vertical is 4ph1-only (ms_layout='vertical'); chemistry's
# parse_ms never sees any of this — bit-identity by construction.
MS_V_GLUED_QN_LETTER_ROMAN_RE = re.compile(
    r"^(\d{1,2})\s+\(([a-h])\)\s+\((i{1,3}|iv|v|vi{1,3})\)\s*(.*)$", re.I)
MS_V_GLUED_LETTER_CONTENT_RE = re.compile(r"^\(([a-h])\)\s*(\S.*)$", re.I)
MS_V_GLUED_QN_CONTENT_RE = re.compile(r"^\s{0,3}(\d{1,2})\s+(\S.*)$")  # v0.18.0: up to 3 leading spaces (marker-column tolerance, 2023-01 2P prints tables 1-2 deep)
MS_V_QN_CONTENT_TAIL_MARKS_RE = re.compile(r"\s{2,}(\d{1,2})\s*$")
MS_V_GLUED_LETTER_ROMAN_NOPAREN_RE = re.compile(
    r"^([a-h])\)\s*\((i{1,3}|iv|v|vi{1,3})\)\s*(.*)$", re.I)
# v0.18.0: the MCQ row-rebuttal lexicon, hoisted from the keying site so the
# lane split is explicit. _MS_ROW_REBUTTAL_RE carried the v0.17.4 inline text
# BYTE-EXACT (including the concatenated-branch quirk '\b\b' that made its
# final '(is|are) ... incorrect' branch unreachable) until the F86-queued
# repair executed in v0.29.1 (F110): the missing alternation '|' is restored
# so 'X is incorrect ...' rows rebut again in the row lane. The served
# chemistry corpus keyed its MCQs from a pre-quirk staging era; every fresh
# re-emission on current staging de-keyed exactly the parts whose rebuttals
# lack an 'is not' lexeme (F86 forensics; 2021-06 1C 5(b)(i)/6(b)(ii) are the
# first regeneration bites — F110). The vertical variant is the sane
# alternation and adds the 'does not'/'do not' elimination family the physics
# tables print (2025-11 2P 2(b): 'A does not affect gravitational field
# strength').
_MS_ROW_REBUTTAL_RE = re.compile(
    r"\bis\s+not\b|\bare\s+not\b|\bcannot\s+be\b"
    r"|\b(?:is|are)\s+(?:\w+\s+)?incorrect\b")
_MS_V_REBUTTAL_RE = re.compile(
    r"\bis\s+not\b|\bare\s+not\b|\bcannot\s+be\b|\bdoes\s+not\b|\bdo\s+not\b"
    r"|\b(?:is|are)\s+(?:\w+\s+)?incorrect\b")

# F86 re-receipt (v0.29.2): a linkage block whose every line is a bare 1-2
# digit marks fragment (optionally behind an abbreviated 'Total ... =' footer
# prefix) is marks furniture, not machine-linkable answer text. The F90
# geometry-aware bare-numeral keep (F108 leg 0) resurrects exactly these
# blocks for the printed-image answer cells (2023-06 2CR 7(c)(i): the '1';
# 2025-06 2CR 7(c)(ii): '1' + the Total footer's orphan '15'), which defeated
# the `not lines` override precondition and let fresh emissions serve the
# fabricated digits the F47/F107 eyeballed transcriptions had removed.
# The MS-LINK-OVERRIDES ledger is the human adjudication of record for its
# seven parts and outranks an all-fragments machine block. Blast radius: the
# 7 ledger entries only — legitimate F90 restorations never enter this path
# (they are not ledger parts).
_MS_MARKS_FRAGMENT_RE = re.compile(r"^(?:Total\b[^=]*=\s*)?\d{1,2}$")


def _all_marks_fragments(lines):
    ls = [l.strip() for l in lines if l and l.strip()]
    return bool(ls) and all(_MS_MARKS_FRAGMENT_RE.match(l) for l in ls)


def parse_ms_vertical(ms_lines):
    """Vertical (cell-per-line) MS layout -> (entries, ms_marks).

    Same key space as parse_ms: (qnum, letter, roman) -> list of raw content
    lines. ms_marks: (qnum, letter, roman) -> the marks-column digit read for
    that entry (first-wins; None when the layout withheld it — the G7
    corroboration is skipped, never guessed)."""
    entries = {}
    ms_marks = {}
    cur_q, cur_letter = None, None
    cur = None
    last_roman = {}          # (q, letter) -> ROMAN index of the last marker roman
    armed = False            # set by a page-header run; consumed by the next bare numeral
    header_run = []
    for ln in ms_lines:
        # F67 (v0.17.4): the F48 PUA gate applies to EVERY raw-layer reader that
        # feeds serving content - the vertical lane bypassed clean_lines by design
        # and skipped normalize_pua with it, leaking mapped PUA chars (U+F020,
        # U+F050, U+F0B4, U+F0B7, U+F044, U+F070, U+F068) into 4ph1
        # solution_md/mark_points. The normalized line REBINDS ln (indentation
        # preserved - build_solution's NOTES_COL_INDENT column logic reads it), so
        # the stored entries are clean at all three append sites. normalize_pua is
        # fail-closed: an unmapped codepoint still aborts the run (C74 pins the
        # absence law corpus-wide).
        ln = normalize_pua(ln)
        s = ln.strip()
        if not s:
            continue
        low = s.lower()
        if low == "pmt" or re.fullmatch(r"BLANK PAGE", s, re.I):
            continue
        if low in MS_HEADER_TOKENS:
            header_run.append(low)
            if low == "marks" and any(t.startswith("question") for t in header_run):
                armed = True
                header_run = []
            continue
        header_run = []      # any non-header line breaks the run (armed persists)
        if MS_V_TOTAL_RE.match(s):
            continue
        mnum = MS_V_BARE_NUM_RE.match(s)
        if mnum:
            v = int(mnum.group(1))
            if armed:
                armed = False
                # same law as parse_ms._honour_qn gate (b): bootstrap at 1,
                # then strictly ascending / same-question re-print
                ok = (cur_q is None and v == 1) or (cur_q is not None and v in (cur_q, cur_q + 1))
                if ok:
                    cur_q = v
                    cur_letter = None
                    cur = (cur_q, None, None)
                    entries.setdefault(cur, [])
                    continue
            if cur is not None:
                ms_marks.setdefault(cur, v)   # marks digit: first-wins, never content
            continue
        # v0.18.0: letter-only rows carry a marker-column indent gate (<=3
        # spaces in the raw line). The corpus census: real letter cells sit at
        # indent 0-2; the ONLY deeper letter-shaped rows are notes-column
        # WRAPS of a bare paren token — 2020-01 2P prints 'allow ... for
        # (a)' wrapped so the continuation line is exactly '(a)' at indent
        # 65, which reset cur_letter and derailed the next roman gate
        # (3(b)(ii) never opened). Same gate for roman-only rows (poison
        # wraps at indent 57-70, real markers at 0-2).
        mlet = MS_V_PAREN_LETTER_RE.fullmatch(s)
        if mlet and (len(ln) - len(ln.lstrip())) <= 3:
            cur_letter = mlet.group(1)
            cur = (cur_q, cur_letter, None)
            entries.setdefault(cur, [])
            continue
        # v0.18.0: triple row (qn+letter+roman+content) MUST be tested before
        # the qn+letter rule — that rule would otherwise accept the row with
        # '(i) content' swallowed into the entry's first content line.
        # Marker evidence (the full qn+letter+roman tuple printed on the row)
        # wins over the running sequence, exactly as for the qn+letter form;
        # the roman itself stays under the ascending-sequence law.
        mqlr = MS_V_GLUED_QN_LETTER_ROMAN_RE.match(s)
        if mqlr:
            armed = False
            new_q = int(mqlr.group(1))
            new_letter = mqlr.group(2)
            roman = mqlr.group(3).lower()
            k = (new_q, new_letter)
            expected = last_roman.get(k, -1) + 1
            rest = (mqlr.group(4) or "").strip()
            if ROMAN.index(roman) == expected:
                cur_q, cur_letter = new_q, new_letter
                cur = (cur_q, cur_letter, roman)
                last_roman[k] = expected
                if cur in entries and rest:
                    entries[cur].append(rest)   # continuation re-print
                else:
                    entries.setdefault(cur, [rest] if rest else [])
            elif cur is not None:
                entries[cur].append(ln.rstrip())
            continue
        mg = MS_V_GLUED_QN_LETTER_RE.match(s)
        if mg:
            armed = False   # the row carries its own question number
            cur_q = int(mg.group(1))
            cur_letter = mg.group(2)
            rest = (mg.group(3) or "").strip()
            cur = (cur_q, cur_letter, None)
            if cur in entries:
                if rest:
                    entries[cur].append(rest)   # v0.18.0: continuation re-print
            else:
                entries[cur] = [rest] if rest else []
            continue
        mgr = MS_V_GLUED_LETTER_ROMAN_RE.match(s)
        if mgr:
            cur_letter = mgr.group(1)
            roman = mgr.group(2).lower()
            k = (cur_q, cur_letter)
            expected = last_roman.get(k, -1) + 1
            rest = (mgr.group(3) or "").strip()
            lead = len(ln) - len(ln.lstrip())
            if cur_q is not None and ROMAN.index(roman) == expected:
                cur = (cur_q, cur_letter, roman)
                last_roman[k] = expected
                entries.setdefault(cur, [rest] if rest else [])
            elif cur_q is not None and lead <= 3 and ROMAN.index(roman) == expected - 1 and cur in entries:
                # v0.18.0: continuation re-print of the marker row on a new
                # page (same roman again, marker column) — append, never lose
                cur = (cur_q, cur_letter, roman)
                if rest:
                    entries[cur].append(rest)
            elif cur_q is not None and lead <= 3 and not any(kk[0] == cur_q and kk[1] == cur_letter for kk in entries):
                # v0.18.0 orphan-roman re-anchor: the letter+roman row is the
                # FIRST row of its letter family yet carries a roman past (i)
                # — the (i) row's letter cell was lost upstream (2026-06 2P
                # prints Q4(c)(ii) with no preceding (c) marker because
                # pdftotext merged the (c) cell into the (ii) row). A marker
                # column row (indent <=3) for a fresh letter family can only
                # be a marker: re-anchor the roman sequence at it. Cross-
                # reference content ('use (c)(ii) from...') sits at answer-
                # column indent >=9 and can never fire this.
                cur = (cur_q, cur_letter, roman)
                last_roman[k] = ROMAN.index(roman)
                entries[cur] = [rest] if rest else []
            elif cur is not None:
                entries[cur].append(ln.rstrip())
            continue
        # v0.18.0: paren-less letter cell — 'b)   (i)   (Np/Ns) = (Vp/Vs);'
        # (2019-06 2P Q2(b): pdftotext dropped the opening paren of the letter
        # cell; exactly 1 row corpus-wide). Sibling of the paren-tolerant form
        # above, same gates.
        mgrp = MS_V_GLUED_LETTER_ROMAN_NOPAREN_RE.match(s)
        if mgrp and cur_q is not None:
            cur_letter = mgrp.group(1)
            roman = mgrp.group(2).lower()
            k = (cur_q, cur_letter)
            expected = last_roman.get(k, -1) + 1
            rest = (mgrp.group(3) or "").strip()
            if ROMAN.index(roman) == expected:
                cur = (cur_q, cur_letter, roman)
                last_roman[k] = expected
                entries[cur] = [rest] if rest else []
            elif cur is not None:
                entries[cur].append(ln.rstrip())
            continue
        # v0.18.0: letter marker with its content glued to the row. Tested
        # AFTER the letter+roman rule (which it would otherwise shadow for
        # '(b) (i) any two from:' rows — the roman IS content shaped '(i ...'
        # there). Opens the letter entry with the row's own text as its first
        # content line; a re-printed letter row appends (continuation).
        mlc = MS_V_GLUED_LETTER_CONTENT_RE.match(s)
        if mlc and cur_q is not None:
            cur_letter = mlc.group(1)
            rest = mlc.group(2).strip()
            cur = (cur_q, cur_letter, None)
            if cur in entries:
                entries[cur].append(rest)
            else:
                entries[cur] = [rest]
            continue
        # v0.18.0: question number glued straight to content (no letter cell).
        # Strict triple gate before acceptance — ascending question law AND a
        # trailing marks-column digit AND column-0 placement in the raw line
        # (numeric answer lines like '39 000 = 0.45 × c × 49' share the
        # stripped shape; none of them is column-0 with a tail digit).
        mqc = MS_V_GLUED_QN_CONTENT_RE.match(ln)
        if mqc:
            v = int(mqc.group(1))
            ok_seq = (cur_q is None and v == 1) or (cur_q is not None and v in (cur_q, cur_q + 1))
            if ok_seq and MS_V_QN_CONTENT_TAIL_MARKS_RE.search(ln) and (len(ln) - len(ln.lstrip())) <= 3:
                # v0.18.0: indent <=3 (raw line) replaces the original strict
                # column-0 — 2023-01 2P prints its tables 1-2 spaces deep and
                # Q1's whole-question row ('1   electrons;   5') sat at
                # indent 1. Corpus census of this shape at indent <=3 with a
                # tail digit: 15/15 rows are real question rows.
                armed = False
                cur_q = v
                cur_letter = None
                rest = mqc.group(2).strip()
                cur = (cur_q, None, None)
                if cur in entries:
                    if rest:
                        entries[cur].append(rest)   # continuation re-print
                else:
                    entries[cur] = [rest] if rest else []
                continue
        mrom = MS_V_PAREN_ROMAN_RE.fullmatch(s)
        mromc = None if mrom else MS_V_GLUED_ROMAN_CONTENT_RE.match(s)
        if mrom or mromc:
            roman = (mrom or mromc).group(1).lower()
            rest = "" if mrom else mromc.group(2).strip()
            k = (cur_q, cur_letter)
            expected = last_roman.get(k, -1) + 1
            if cur_q is not None and cur_letter and ROMAN.index(roman) == expected:
                cur = (cur_q, cur_letter, roman)
                last_roman[k] = expected
                entries.setdefault(cur, [rest] if rest else [])
            elif cur is not None:
                entries[cur].append(ln.rstrip())
            continue
        if cur is not None:
            entries[cur].append(ln.rstrip())
    return entries, ms_marks


# ---------------------------------------------------------------- v0.5: solution emission
# The reveal + Smart Mark layer: per-part solution_md (verbatim MS answer block)
# and mark_points[] (awardable points whose marks always sum to the part marks).
SOL_TAIL_MARKS_RE = re.compile(r"\s{2,}(\d{1,2})\s*$")   # marks-column digit, far right
TOTAL_ROW_RE = re.compile(r"^Total \d+$")
NOTES_COL_INDENT = 45   # answer-column content sits left of this in every observed table;
                        # the Notes column (ALLOW/ACCEPT/... + its M1/M2 cross-references)
                        # starts at col ~60+ — never confuse its M-rows for points


def _mp_only_fragments(mark_points, part_marks=None):
    """F97 helper: True when EVERY mark_point text is a margin-note fragment or a
    bare marks digit — the shapes the MS parser captures when the printed answer
    is a drawing. Re-emitting those as a solution body would fabricate an answer,
    so the F97 bare-answer fallback refuses to fire (fail-visible via the G7
    mp_answer_gap census instead). A bare digit equal to the part's own marks is
    the marks-column digit leak (2023-06 2CR 7(c)(i): answer cell is a printed
    drawing, the parser captured the marks digit); any other bare token is a real
    printed answer (2021-06 1C 2(b)(ii): '25') and must re-emit."""
    frag = re.compile(
        r"^(?:If\s+M\d\b|max\s*\d+\s*mark\b|.*\bscores\s+(?:0|both)\b.*|dep\s+on\s+M\d.*"
        r"|ALLOW\b.*|REJECT\b.*|IGNORE\b.*|ECF\b.*|OWTTE\b.*|_+)$",
        re.I | re.S)
    # F108: a reconstructed MS answer-grid table (the Finding-5 parser) is the
    # opposite of a margin-note fragment — the part's full printed answer grid.
    # Its text may BEGIN with 'ALLOW ' (the grid's printed note row), which the
    # fragment shapes would otherwise swallow whole (re.S).
    if any((mp.get("text_md") or "").lstrip().startswith("| ")
           or "\n| " in (mp.get("text_md") or "") for mp in mark_points):
        return False
    for mp in mark_points:
        t = (mp.get("text_md") or "").strip()
        if not t:
            return True
        if t.isdigit() and part_marks is not None and int(t) == part_marks:
            return True
        if frag.match(t):
            continue
        return False
    return True


# ------------------------------------------------------- v0.28.0: the MS-grid parser tranche
# Three legs, one subsystem (the MS answer grid), landed together because they
# share the failure surface (LEDGER F108):
#   leg 0 — the F90 MS-side-aware bare-number rule (geometry-aware FURNITURE_LINE
#           strip, implemented in clean_lines above);
#   leg 1 — the F88-queued converter-side MS-grid furniture strip: the exporter's
#           serve-time strip semantics (F-W15-2) ported byte-verbatim to the
#           source, so a full re-run reproduces the serve-clean corpus of record
#           instead of re-introducing grid furniture that the exporter then has
#           to remove again (the reproducibility-debt class of AUDIT-2026-10-27
#           Finding 8c);
#   leg 2 — the Finding-5 MS answer-grid (box) parser: "match description"
#           questions whose MS answer grid linearizes into scrambled text
#           (2021-06 1C 1(a), 2023-06 1CR 4(a)); the F68 vertical-parser
#           lineage adapted to the chemistry row-layout lane. The grid's two
#           columns are reconstructed from the pdftotext -layout x-geometry and
#           re-emitted as a readable two-column table (verbatim tokens, rows
#           reassembled — Mode A presentation repair, disclosed per part).

# Byte-verbatim port of the exporter's F-W15-2 word-set (official_examq_export_hub.py).
MS_FURNITURE_WORDS = {"question", "number", "answer", "notes", "marks",
                      "additional", "guidance", "total", "for"}


def _ms_furniture_line(line):
    toks = [t for t in re.split(r"[^A-Za-z]+", line) if t]
    return bool(toks) and all(t.lower().lstrip("0123456789") in MS_FURNITURE_WORDS for t in toks)


# The F88 mid-text classes (the two UNAMBIGUOUS ones only — bare answer/mark
# lines are wrap-ambiguous, "1 mark" splits across lines, and stay mid-text):
#   (a) bare Total-family rows ("Total", "Total 7", "Total for Question 3 = 7 marks");
#   (b) MS-table header rows ("Question Answer Notes Marks", "Answer Additional
#       guidance Marks") — >=2 furniture tokens.
MS_TOTAL_LINE_RE = re.compile(
    r"^Total(?:\s+\d+)?$"
    r"|^Total\s+for\s+Question\s+\d+\s*=\s*\d+\s*marks$"
    # v0.30.1 (F88 reconciliation): the abbreviated form recognizes the marks
    # suffix too, matching the printed footer verbatim ('Total for Q3 = 8
    # marks') — consistency with the spelled-form alternative above; with the
    # v0.30.1 FURNITURE_SUBS completion such lines are consumed at the raw
    # layer and never reach this strip (A/B-proven zero live firing).
    r"|^Total\s+for\s+Q\.?\s?\d+\s*=\s*\d+(?:\s+marks)?$",
    re.I)
MS_HEADER_ROW_MIN_TOKENS = 2


def strip_ms_grid_furniture(text):
    """F108 leg 1 (closes the F88 caveat 'the MS-table parser may anchor on
    header lines'): the converter-side MS-grid furniture strip.

    The strip runs on the ASSEMBLED solution/mark-point text — after the grid
    rows have been consumed for linkage, keying and M-splitting — never on the
    raw grid lines the parser anchors on. Semantics are the exporter's
    strip_furniture ported verbatim (trailing furniture lines, up to 4, from
    the end only) plus the F88 mid-text classes (bare Total-family lines and
    header rows). A strip that would empty a whole text is refused
    (fail-closed): the text stays and the class stays visible to the battery."""
    if not text:
        return text
    lines = text.rstrip().splitlines()
    mid = []
    for ln in lines:
        s = ln.strip()
        toks = [t for t in re.split(r"[^A-Za-z]+", s) if t]
        if s and (MS_TOTAL_LINE_RE.fullmatch(s)
                  or (_ms_furniture_line(s) and len(toks) >= MS_HEADER_ROW_MIN_TOKENS
                      # v0.29.1 (F110): a line carrying digits is never a header
                      # row — the printed header bands have none. Digit-bearing
                      # all-furniture-token lines are the F88 wrap-ambiguous
                      # guidance class ('ALLOW 297 X 9.75/65 =44.55/44.6 for 2
                      # marks' / 'for 2 marks'), kept verbatim; eyeballed on the
                      # sha-verified 2023-11 1C + 2025-06 2C MS pages of record.
                      and not any(ch.isdigit() for ch in s))):
            continue
        mid.append(ln)
    n = 0
    while mid and n < 4:
        last = mid[-1].strip()
        if (_ms_furniture_line(last)
                or re.fullmatch(r"Total\s+\d+", last)
                or re.fullmatch(r"Total\s+for\s+Question\s+\d+\s*=\s*\d+\s*marks", last)):
            mid.pop()
            n += 1
            continue
        break
    if not "\n".join(mid).strip():
        return text                      # refuse to empty a text (fail-closed)
    return "\n".join(mid).rstrip()


MS_GRID_HEADER_RE = re.compile(r"^(?P<pad>\s*)Information(?P<gap>\s{2,})(?P<right>\S.*)$")
MS_GRID_MARKER_RE = re.compile(r"^\s{0,12}\d{0,2}\s*\([a-z]{1,2}\)")
MS_GRID_MAX_ROWS = 14
MS_GRID_RIGHT_TOL = 10


def restore_ms_answer_grids(ms_lines):
    """F108 leg 2 (the Finding-5 MS-box parser tranche). Reconstructs the
    printed 'match description' answer grid from the entry's layout-geometry
    lines and re-emits it as a two-column table; verbatim tokens, rows
    reassembled — no authoring, no paraphrase (Mode A + G2-D disclosure).

    Returns (lines, meta): meta is None when no transform fired, else a dict
    {"rows": n, "right_header": str} the caller turns into the part's
    edits[] disclosure entry (structural-repair, evidence LEDGER F108).

    Geometry (from the staged 2021-06 1C and 2023-06 1CR grids):
      - a header line  'Information<2+ spaces><right header>'  fixes the right
        column x (R = start of the right header text);
      - a body line carrying text BOTH left of R-TOL and at/after R-TOL is a
        two-column row line (new row; right cell = the trailing text);
      - text only left of R-TOL continues the current row's description;
      - text only at/after R-TOL continues the current row's answer (the
        2023-06 grid wraps 'carbon'/'monoxide' on interleaved right-only
        lines);
      - a blank line closes the current row (the 2023-06 grid separates rows
        with blanks; the 2021-06 grid starts each row with a two-column line —
        both delimiters coexist).

    Fail-closed: the transform fires only when the header parses, at least two
    rows reconstruct, and EVERY reconstructed row has non-empty description
    and answer cells; otherwise the entry lines are returned unchanged and
    the part keeps its (disclosed-defective) verbatim block."""
    lines = list(ms_lines)
    h = None
    hm = None
    for i, ln in enumerate(lines):
        m = MS_GRID_HEADER_RE.match(ln)
        if m:
            h, hm = i, m
            break
    if h is None:
        return lines, None
    right_x = hm.start("right")
    rows = []           # [left_parts, right_parts]
    cur = None

    def close():
        nonlocal cur
        if cur is not None:
            rows.append(cur)
            cur = None

    for ln in lines[h + 1:]:
        s = ln.rstrip()
        st = s.strip()
        if not st:
            close()
            continue
        if MS_GRID_MARKER_RE.match(s) or st in ("Question", "number", "PMT") \
                or st.startswith("Total") or st.startswith("PMT"):
            break
        content_start = len(s) - len(s.lstrip())
        zone = right_x - MS_GRID_RIGHT_TOL
        left = right = None
        if content_start >= zone:
            right = st                       # right-only line (2023-06 'carbon')
        else:
            # split at the LAST internal 2+ space run whose text lands in the
            # right zone — the printed column boundary is whitespace, never a
            # mid-word cut (the fixed-offset cut broke 'product of' / 'the')
            gstart = None
            for m in re.finditer(r"\s{2,}\S", s):
                if m.end() - 1 >= zone and s[:m.start()].strip():
                    gstart = m.start()
            if gstart is not None:
                left = s[:gstart].strip()
                right = s[gstart:].strip()
            else:
                left = st                    # left-only continuation line
        if left is not None and right is not None:
            close()
            cur = [[left], [right]]
        elif left:
            if cur is None:
                cur = [[left], []]
            else:
                cur[0].append(left)
        elif right:
            if cur is None:
                cur = [[], [right]]
            else:
                cur[1].append(right)
    close()
    rows = [r for r in rows if r[0] or r[1]]
    if len(rows) < 2 or len(rows) > MS_GRID_MAX_ROWS \
            or any(not r[0] or not r[1] for r in rows):
        return lines, None               # fail-closed: keep the verbatim block
    right_header = " ".join(hm.group("right").split())
    out = lines[:h]
    out.append(f"| Information | {right_header} |")
    out.append("| --- | --- |")
    for lft, rgt in rows:
        lcell = " ".join(" ".join(lft).split())
        rcell = " ".join(" ".join(rgt).split())
        out.append(f"| {lcell} | {rcell} |")
    return out, {"rows": len(rows), "right_header": right_header}


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
    # F108 leg 2: reconstruct printed match-description answer grids (Finding 5)
    # BEFORE normalization — the transform needs the layout x-geometry that the
    # per-line whitespace collapse below would destroy. A fired transform is a
    # structural repair: it discloses through edits[] (G2-D) with the finding
    # id as evidence, exactly like the F97 fallback.
    ms_lines, grid_meta = restore_ms_answer_grids(list(ms_lines))
    if grid_meta:
        p.setdefault("edits", []).append({
            "field": "solution_md", "kind": "structural-repair",
            "tool": f"official_examq_extract.py v{CONVERTER_VERSION} (F108 MS answer-grid parser)",
            "evidence_ref": (f"LEDGER F108 (AUDIT-2026-10-27 Finding 5); printed MS answer grid "
                             f"reconstructed from the layout x-geometry — {grid_meta['rows']} rows, "
                             f"right column '{grid_meta['right_header']}'; verbatim tokens, rows reassembled"),
        })
        p["edit_status"] = "corrected"
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
    # F108 leg 1 (closes the F88 caveat): the converter-side MS-grid furniture
    # strip — the serve-clean form IS the corpus form of record (F88 wave), so
    # the extraction emits it directly and the exporter's serve-time strip
    # becomes a redundant second line of defense instead of the only one.
    solution_md = strip_ms_grid_furniture(solution_md)
    for mp in pts or []:
        stripped = strip_ms_grid_furniture(mp.get("text_md") or "")
        if stripped.strip():
            mp["text_md"] = stripped      # never empty an MP (fail-closed)
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
    ap.add_argument("--spec", default="4ch1", choices=sorted(SPECS),
                    help="spec lane (v0.16.0): 4ch1 default (chemistry, the v0.15.0 "
                         "behavior); 4ph1 = Edexcel IGCSE Physics")
    ap.add_argument("--series", default="2020-11",
                    help="paper series folder, e.g. 2020-11 (baseline), 2019-06, 2020-01, 2021-06, 2022-06, 2024-06")
    ap.add_argument("--paper", default=None,
                    help="paper variant code (F34); defaults to the spec's default paper")
    args = ap.parse_args()
    cfg = SPECS[args.spec]
    series = args.series
    paper = args.paper if args.paper is not None else cfg["default_paper"]
    if paper not in cfg["paper_totals"]:
        ap.error(f"paper {paper!r} is not a registry variant of spec {args.spec!r} "
                 f"(choices: {', '.join(sorted(cfg['paper_totals']))})")
    P = paths_for(series, paper, cfg)
    global QP_PDF, MS_PDF, QP_TXT, MS_TXT, MANIFEST, OUT, PAPER_TOTAL
    global ACTIVE_PUA_OVERRIDES, ACTIVE_SPEC_CODE, ACTIVE_FOOTER_RE
    ACTIVE_PUA_OVERRIDES = cfg.get("pua_overrides", {})
    ACTIVE_SPEC_CODE = cfg["spec_code"]
    ACTIVE_FOOTER_RE = re.compile(cfg["footer_re"])
    QP_PDF, MS_PDF = P["qp_pdf"], P["ms_pdf"]
    QP_TXT, MS_TXT = P["qp_txt"], P["ms_txt"]
    MANIFEST, OUT = P["manifest"], P["out"]
    PAPER_TOTAL = cfg["paper_totals"][paper]
    SPEC_RESOLUTION = spec_resolution_path(cfg)
    footer_re = re.compile(cfg["footer_re"])
    expect_q = cfg["expect_questions"].get(paper, {}).get(series)

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
    # ---- v0.17.0 (G0-D): document-type identity probe -----------------------
    # See the MS_COVER_RE block above: a manifest can attestation-grade the
    # wrong bytes (F-A2 mislabels are sha-consistent); the cover cannot lie.
    # Invisible-on-pass: the G0 summary string is extended ONLY on a hit, so
    # clean slices' validation-reports stay byte-identical.
    qp_cover = _cover_text(QP_PDF)
    ms_cover = _cover_text(MS_PDF)
    doc_type_issue = None
    if qp_cover and not QP_COVER_RE.search(qp_cover):
        if MS_COVER_RE.search(qp_cover):
            doc_type_issue = "qp.pdf prints a mark-scheme cover (archive mislabel: F-A2 wrong-DAM-artifact class)"
        elif ER_COVER_RE.search(qp_cover):
            doc_type_issue = "qp.pdf prints an examiners-report cover (archive mislabel: F-A2 wrong-DAM-artifact class)"
    if doc_type_issue is None and ms_cover and not MS_COVER_RE.search(ms_cover):
        doc_type_issue = "ms.pdf cover does not print a mark-scheme marker (archive mislabel suspected)"
    identity_ok = sha_ok and variant_ok and doc_type_issue is None
    paper_id = manifest["paper_id"]
    report["gates"].append({
        "gate": "G0-identity", "status": "PASS" if identity_ok else "FAIL",
        "summary": f"paper_id={paper_id}; series={manifest['series']['normalized']}; "
                   f"printed={manifest['series'].get('printed', 'n/a (manifest schema v2 omits it)')!r}; sha256 qp/ms match manifest: {sha_ok}; "
                   f"manifest variant {manifest_variant!r} == requested {paper!r}: {variant_ok}"
                   + (f"; G0-D: {doc_type_issue}" if doc_type_issue else ""),
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

    # run-001 hygiene wave: the repaired text IS the extraction of record —
    # G2-D provenance, source_norm and the emission all move together.
    QP_TEXT_SRC, qp_repair_receipt = repair_source_text(
        QP_TXT.read_text(errors="replace"), QP_TXT, cfg["lane"])
    MS_TEXT_SRC, ms_repair_receipt = repair_source_text(
        MS_TXT.read_text(errors="replace"), MS_TXT, cfg["lane"])
    if qp_repair_receipt["applied"] or qp_repair_receipt["fffc_stripped"] \
            or ms_repair_receipt["applied"] or ms_repair_receipt["fffc_stripped"]:
        report["text_repairs"] = {"qp": qp_repair_receipt, "ms": ms_repair_receipt}

    qp_lines = clean_lines(QP_TEXT_SRC)
    footers = [(i, int(m.group(1)), int(m.group(2)))
               for i, ln in enumerate(qp_lines) if (m := footer_re.search(ln))]

    # ---- extraction --------------------------------------------------------
    # footer census: printed totals must exist for 1..N; a missing footer (seen in
    # 2019-06 Q7 — absent from the PDF text layer itself) splits the following
    # region into a footer-less question (marks inferred from parts -> REVIEW)
    footer_qnums = {q for _, q, _ in footers}
    # F101 (v0.25.0): an EMPTY footer census means the QP text layer carries no
    # question footers at all — the image-only archive-scan class (2019-06 4PH1-1P
    # Task 15 CRASH-RECEIPT: this branch previously crashed with a bare ValueError
    # from max()). Fail closed with an honest, machine-readable G1 attribution
    # instead of a traceback: the run still aborts (never serve from a census-less
    # extraction), but the receipt now names the defect class and the OCR-layer
    # remedy. Chemistry/4MB1/normal physics runs never reach this branch (their
    # footers always exist), so no served corpus changes.
    if not footer_qnums:
        report["gates"].append({
            "gate": "G1-structure", "status": "FAIL",
            "summary": "empty footer census: 0 'Total for Question' rows in the QP text "
                       "layer — image-only archive scan without an OCR source layer "
                       "(stage UPLOAD/ocr/<series>-<paper>/qp-pNN.txt + ocr-pages.json "
                       "per LEDGER F41/F101); previous behaviour: bare ValueError crash "
                       "(Task 15 CRASH-RECEIPT)",
            "details": {"qp_txt_bytes": len(QP_TEXT_SRC)}})
        print("G1 FAIL — empty footer census (fail-closed attribution, F101)")
        json.dump(report, sys.stdout, indent=1)
        return 1
    max_q = max(footer_qnums)
    missing = [n for n in range(1, max_q + 1) if n not in footer_qnums]

    def emit_question(qnum, printed_total, region):
        seg = segment_question(qnum, [l for l in region if l.strip()])
        stem_md = re.sub(r"\s{2,}", " ", " ".join(seg["stem_lines"])).strip()
        questions_parts = []
        if (cfg["spec_code"] == "4MB1"  # run-004 union: lane-guarded (physics sole parts keep the v0.19.0 path)
                and not seg["group_order"] and printed_total):
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
                "_kept": p.get("_kept"), "_glue_cands": p.get("_glue_cands"),
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
                "_kept": p.get("_kept"), "_glue_cands": p.get("_glue_cands"),
                })
                continue
            # F72 (maths-B): romans without printed marks inside a marks-carrying
            # letter group are continuation list items (2021-06 02 Q7: '(b)
            # Calculate the interest she receives in one year. (2)' then
            # '(i) change his dollars into euros...' '(ii) ... straight into
            # pounds.' with no marks of their own) - the WHOLE group finalizes
            # as one part from its raw lines, so the extraction baseline (and
            # G2-D's 5-gram check) stays byte-faithful.
            if cfg["spec_code"] == "4MB1" and grp["order"]:
                roman_probes = [finalize_part(grp["parts"][r]["lines"]) for r in grp["order"]]
                letter_probe = finalize_part(grp["stem_lines"])
                if (letter_probe["marks"] is not None
                        and all(rp["marks"] is None for rp in roman_probes)):
                    whole = finalize_part(grp["stem_lines"]
                                          + [l for r in grp["order"] for l in grp["parts"][r]["lines"]])
                    questions_parts.append({
                        "part_number": f"{qnum}({gletter})",
                        "group": gletter, "roman": None,
                        "group_stem_md": grp_stem or None, "option_list": option_list,
                        "marks": whole["marks"],
                        "question_type": "multiple_choice" if whole["choices"] else "structured",
                        "problem_md": whole["problem_md"], "choices": whole["choices"],
                        "source_norm": whole["source_norm"],
                        "_kept": whole.get("_kept"), "_glue_cands": whole.get("_glue_cands"),
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
                "_kept": p.get("_kept"), "_glue_cands": p.get("_glue_cands"),
                })
        if not questions_parts and seg["stem_lines"]:
            # v0.17.0: whole-question part — the question printed no letter or
            # roman parts, so its stem IS the single part (physics 1P 2024-06
            # Q8: one 6-mark explanation question, marks printed in the footer
            # only). Inert on chemistry: every chemistry question carries
            # letter parts (and any marks-less sole part would always have
            # failed G1 — none ever did).
            p = finalize_part(seg["stem_lines"])
            questions_parts.append({
                "part_number": f"{qnum}",
                "group": None, "roman": None,
                "group_stem_md": None, "option_list": None,
                "marks": p["marks"],
                "question_type": "multiple_choice" if p["choices"] else "structured",
                "problem_md": p["problem_md"], "choices": p["choices"],
                "source_norm": p["source_norm"],
            })
        # F80 (maths-B): romans whose parts ALL lack printed marks are (lane-scoped to 4mb1 at the run-004 union — chemistry and physics parts carry marks corpus-wide)
        # instruction list items, not markable parts (2020-11 01R Q20:
        # construction steps '(i) closer to DA...' with no per-part marks
        # printed). Collapse to one implicit part carrying the printed total;
        # the single-part MS union law then links it.
        if (cfg["spec_code"] == "4MB1" and printed_total and questions_parts
                and len(questions_parts) > 1
                and all(p["marks"] is None for p in questions_parts)):
            p = finalize_part([l for l in region if l.strip()][1:])
            questions_parts = [{
                "part_number": f"{qnum}",
                "group": None, "roman": None,
                "group_stem_md": None, "option_list": None,
                "marks": p["marks"] if p["marks"] is not None else printed_total,
                "question_type": "multiple_choice" if p["choices"] else "structured",
                "problem_md": p["problem_md"], "choices": p["choices"],
                "source_norm": p["source_norm"],
                "_kept": p.get("_kept"), "_glue_cands": p.get("_glue_cands"),
                "implicit_single_part": True,
            }]
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
        # F67: a missing question's content lives ONLY in the first region after
        # it — the handler whose footer question number is the next one above m.
        # In EARLIER regions a QSTART@m match is always a digit-leading source
        # line (the F49 class — e.g. 2023-01 02 Q10's right-aligned '(3)' marks
        # tuple after a probability '11'), and firing there emitted Q11 twice
        # (a 5-mark fragment + the true 13-mark question; sum 113/100).
        prev_qnum = footers[fi - 1][1] if fi else 0
        for m in missing:
            if not (prev_qnum < m < qnum):
                continue
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

    # ---- v0.17.0: sole-part marks inference (fail-disclosed) -----------------
    # Some questions print their marks ONLY in the question footer (the sidebar
    # marks box never reaches the text layer — physics 1P 2024-06 Q8). When a
    # question has exactly ONE part and that part parsed no marks digit, the
    # footer total IS the part's marks by arithmetic necessity (the G1 law
    # itself: parts_sum == printed total). Provably inert on chemistry: a
    # marks-less sole part means parts_sum 0 != printed > 0, i.e. G1 FAIL — no
    # chemistry slice ever tripped it. Disclosed in value_trace.marks and in
    # G1 details; never silent.
    sole_part_inferred = []
    for q in doc_questions:
        if (q["printed_total"] is not None and len(q["parts"]) == 1
                and q["parts"][0]["marks"] is None):
            q["parts"][0]["marks"] = q["printed_total"]
            q["parts"][0]["marks_inferred"] = "inferred:sole-part-printed-footer"
            sole_part_inferred.append(q["parts"][0]["part_number"])

    # ---- F82a/F82b (maths-B): QP marks recovery, fail-closed ------------------
    # F82a: text-glued markers resolved by the question-level footer sum law
    # (unique exact-cover assignment; marker stripped from _kept so problem_md
    # and source_norm move together — G2-D 5-gram provenance stays at 1.0).
    # F82b: markers that are vector-drawn in the QP (absent from the text
    # layer entirely) recover from the sha-pinned UPLOAD/ocr/<series>-<paper>/
    # marks-patch.json (600dpi render transcription, tesseract draft, MS
    # Mark-column cross-check); the converter verifies crop hashes + the sum
    # law and hard-fails on any discrepancy (F41 contract).
    # Both fills are FULLY DISCLOSED (edits[] + edit_status corrected +
    # value_trace.marks corrected:*, applied in the provenance block below).
    if cfg["spec_code"] == "4MB1":
        f73_review = []
        _dbg = bool(os.environ.get("EXAMQ_DEBUG_F82"))
        for q in doc_questions:
            total = q["printed_total"]
            unresolved = [p for p in q["parts"] if p.get("marks") is None]
            if total is None or not unresolved:
                continue
            known = sum(p["marks"] for p in q["parts"] if p["marks"] is not None)
            cands = [p.get("_glue_cands") or [] for p in unresolved]
            if _dbg:
                print(f"[F82] Q{q['question_number']} total={total} known={known} "
                      f"unresolved={[p['part_number'] for p in unresolved]} "
                      f"cands={[[c['value'] for c in cl] for cl in cands]}", file=sys.stderr)
            if any(cands):
                target = total - known
                if target > 0:
                    assign = _f73_unique_assignment(target, cands)
                    if assign is not None:
                        for p, v in zip(unresolved, assign):
                            if v is None:
                                continue
                            rec = next(c for c in p["_glue_cands"] if c["value"] == v)
                            kept2 = list(p["_kept"])
                            ln2 = kept2[rec["line"]]
                            kept2[rec["line"]] = (ln2[:rec["start"]] + ln2[rec["end"]:]).rstrip()
                            p["marks"] = v
                            p["_marks_fill"] = "f73a"
                            p["problem_md"] = strip_dotrun(re.sub(r"\s{2,}", " ", " ".join(kept2))).strip()
                            p["source_norm"] = norm(strip_dotrun(" ".join(kept2)))
                            ctx = ln2[max(0, rec["start"] - 24):rec["start"]].strip()  # run-004: branch-commit defect fixed (139ee931 lost "[m" — the file parsed only via accidental bracket rebalance and cannot be the script that produced the corpus of record)
                            p.setdefault("edits", []).append({
                                "field": "marks", "kind": "structural-repair",
                                "tool": "official_examq_extract.py F82a",
                                "evidence_ref": (f"qp text-glued marker ({v}) after '{ctx}' — "
                                                 f"Q{q['question_number']} footer sum "
                                                 f"{known}+{v}={total}")})
                        continue
            # F82b: sha-pinned render/MS patch for text-layer-orphan markers
            patch_path = UPLOAD / "ocr" / f"{series}-{paper}" / "marks-patch.json"
            if not unresolved or not patch_path.exists():
                continue
            patch = json.loads(patch_path.read_text())
            if patch.get("schema") != "syllabai.examq-marks-patch/0.1":
                sys.exit(f"F82b fail-closed: {patch_path} schema mismatch")
            if patch.get("paper_id") != paper_id:
                sys.exit(f"F82b fail-closed: {patch_path} paper_id mismatch")
            by_part = {e["part_number"]: e for e in patch.get("entries", [])}
            for p in unresolved:
                e = by_part.get(p["part_number"])
                if not e:
                    continue
                crop = UPLOAD / "ocr" / f"{series}-{paper}" / "crops" / \
                    f"{p['part_number'].replace('(', '').replace(')', '')}.png"
                if not crop.exists():
                    sys.exit(f"F82b fail-closed: missing crop {crop}")
                sha = hashlib.sha256(crop.read_bytes()).hexdigest()
                if sha != e["evidence"]["crop_sha256"]:
                    sys.exit(f"F82b fail-closed: crop sha mismatch for {p['part_number']}")
                if e["evidence"]["ms_crosscheck"]["mark_column_digit"] != e["marks"]:
                    sys.exit(f"F82b fail-closed: MS cross-check mismatch for {p['part_number']}")
                p["marks"] = int(e["marks"])
                p["_marks_fill"] = "f73b"
                p.setdefault("edits", []).append({
                    "field": "marks", "kind": "structural-repair",
                    "tool": "official_examq_extract.py F82b",
                    "evidence_ref": (f"vector-drawn qp marker, 600dpi render crop {sha[:12]} "
                                     f"(tesseract draft '{e['evidence']['tesseract_draft']}'), "
                                     f"MS Mark column = {e['marks']}")})
            # sum law over EVERY touched question (F82a and F82b fills together)
            for qq in doc_questions:
                if not any(p.get("_marks_fill") for p in qq["parts"]):
                    continue
                if qq["printed_total"] is None:
                    continue
                ssum = sum(p["marks"] or 0 for p in qq["parts"])
                if ssum != qq["printed_total"]:
                    sys.exit(f"F82 fail-closed: Q{qq['question_number']} marks sum {ssum} "
                             f"!= printed total {qq['printed_total']} after fills")
        # honesty: every part the laws could NOT resolve is disclosed with the reason
        for q in doc_questions:
            for p in q["parts"]:
                if p.get("marks") is None and p.get("_glue_cands") is not None:
                    n = len(p.get("_glue_cands") or [])
                    reason = ("no glue candidate in text layer (vector-drawn or absent marker; "
                              "F82b patch path)" if n == 0 else
                              f"{n} glue candidate(s) but footer sum law not uniquely satisfiable")
                    report["review_queue"].append({"part": p["part_number"], "reason": f"F82: {reason}"})


    # ---- MS linkage + MCQ keys ---------------------------------------------
    # v0.17.0: the vertical lane parses the RAW layer (clean_lines would strip
    # the bare-numeral markers this layout runs on); chemistry keeps the exact
    # pre-v0.17 path.
    if cfg.get("ms_layout") == "vertical":
        ms_entries, ms_marks_by_key = parse_ms_vertical(MS_TEXT_SRC.splitlines())
    else:
        ms_entries = parse_ms(clean_lines(MS_TEXT_SRC,
                                          keep_bare_numerals=cfg.get("keep_bare_numerals", False)))
        ms_marks_by_key = {}
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
            # v0.16.0: entries also carry an implicit spec (default 4ch1 — every
            # pre-v0.16 entry is chemistry); the paper-None fallback below only
            # applies within the SAME spec so chemistry's legacy series-scoped
            # keys can never key a physics part.
            e.setdefault("spec", "4ch1")
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
    # v0.19.0: vertical-lane keying refinements. The 4ph1 MS table answers in
    # shapes the chemistry row-layout never prints; every refinement below is
    # gated on ms_layout='vertical' so the chemistry lane's keying code path
    # is untouched bit-for-bit (the Task 12/14/15 bit-identity law).
    _ms_vertical = cfg.get("ms_layout") == "vertical"
    for q in doc_questions:
        for p in q["parts"]:
            key = (q["question_number"], p["group"], p["roman"])
            eff_key = key   # v0.17.0: tracks the entry whose block the linkage actually used
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
                    eff_key = cands[0]
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
                        eff_key = (q["question_number"], p["group"], "i")
            _mk_exact = mcq_key_overrides.get((series, paper, p["part_number"]))
            _mk_legacy = (mcq_key_overrides.get((series, None, p["part_number"]))
                          if _mk_exact is None
                          and mcq_key_overrides.get((series, None, p["part_number"]), {}).get("spec") == args.spec
                          else None)
            mk = _mk_exact or _mk_legacy
            if mk and p["question_type"] == "multiple_choice":
                lines = list(mk["ms_lines"])
                p["answer_key_source"] = "mcq-keys-ledger"
                # wave-22: paper-scoped application marker (the 1C-era reports
                # carry the legacy series-only form; the C31 checker accepts both)
                mcq_keys_applied.append(f"{series}:{paper}/{p['part_number']}")
            mlo = ms_link_overrides.get((series, paper, p["part_number"]))
            if mlo and p["question_type"] != "multiple_choice" and (
                    not lines or _all_marks_fragments(lines)):
                # v0.29.2 (F86 re-receipt): an all-marks-fragments block (the
                # F90 bare-numeral keep resurrecting the marks digits / Total
                # footer fragments for image-answer cells) no longer defeats
                # the ledger precondition — see _MS_MARKS_FRAGMENT_RE above.
                lines = list(mlo["ms_lines"])
                p["answer_key_source"] = "ms-link-overrides-ledger"
                ms_link_applied.append(f"{series}:{paper}/{p['part_number']}")
                # v0.31.0 (F116, F111 class 5): the entry may carry
                # transcription_of_record — the exact rendering of record
                # (ledger == corpus == fresh). Carried on the part for the
                # post-build_solution verbatim application below.
                _tor = mlo.get("transcription_of_record")
                if _tor is not None:
                    if not isinstance(_tor, str) or not _tor.strip():
                        raise SystemExit(
                            f"F47 transcription_of_record must be a non-empty string "
                            f"({series}/{paper}/{p['part_number']})")
                    p["_f47_transcription"] = _tor
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
                        #  'C the charges are incorrect', 'B is X incorrect ...';
                        #  v0.17.1: the physics 2023-06 2P MS prints the
                        #  elimination family 'X cannot be the answer as ...' /
                        #  'X cannot be correct as ...' — without it the
                        #  elimination rows counted as ANSWER rows and drowned
                        #  the real 'D - thermometer;' key (G3 unkeyed))
                        # v0.18.0 (vertical lane only): (a) the negative
                        # lexeme is searched AFTER stripping ALL parenthesized
                        # spans — answer rows quote choice text that can
                        # CONTAIN negatives ('B (absorbing material is not a
                        # continuous variable);' — 2020-01 1P 9(e)(ii)), while
                        # rebuttal rows carry their negative OUTSIDE any
                        # parens ('A (P) is incorrect as...' — 2025-11 1P
                        # 9(b): the parenthesized alias must not mask the
                        # negative, and a naive first-paren split regressed
                        # exactly that row on the first battery); (b) the
                        # lexicon gains 'does not'/'do not' — 2025-11 2P 2(b)
                        # prints its eliminations as 'A does not affect
                        # gravitational field strength'.
                        _neg_text = (re.sub(r"\([^()]*\)", " ", s)
                                     if _ms_vertical else s)
                        _neg_re = (_MS_V_REBUTTAL_RE if _ms_vertical
                                   else _MS_ROW_REBUTTAL_RE)
                        if _neg_re.search(_neg_text):
                            rebut[hit.group(1)] = rebut.get(hit.group(1), 0) + 1
                        else:
                            ans.append(hit.group(1))
                            ansrow[hit.group(1)] = ansrow.get(hit.group(1), 0) + 1
                    elif (re.sub(r"[;.:]+$", "", s.strip()) if _ms_vertical
                          else s.strip()) in labels:
                        # v0.18.0 (vertical lane): bare-key rows 'B;' — the
                        # answer letter printed ALONE with its semicolon
                        # terminator (2022-01 1P/2P print five keys this way;
                        # the row-layout lane never does). Trailing ';', '.',
                        # ':' stripped before the label check; the single-
                        # distinct-candidate law still governs.
                        _bk = re.sub(r"[;.:]+$", "", s.strip())
                        ans.append(_bk)
                        ansrow[_bk] = ansrow.get(_bk, 0) + 1

                # a printed '<L> is the correct answer ...' statement is
                # authoritative: key it even if stray note-drift letters leaked in
                lab = (positives[0] if len(set(positives)) == 1 else
                       (ans[0] if len(set(ans)) == 1 else None))
                # elimination keying (F14): entries whose MS prints an explicit
                # rebuttal for every option except the correct one — key the sole
                # un-rebutted option ONLY when corroborated by exactly one answer
                # row; anything else stays unkeyed for human review
                # v0.18.0 (vertical lane only): pure-elimination entries — the
                # MS prints NO answer row at all and rebuts exactly every
                # option but one (2025-11 2P 2(b): 'A/B/D does not affect...'=
                # the sole survivor C is the key by explicit elimination of
                # the complete option set). Deterministic when the rebuttal
                # set covers all-but-one PRINTED labels and no answer row
                # exists; anything sparser stays unkeyed.
                if lab is None:
                    clean = [L for L in sorted(labels) if L not in rebut]
                    if len(clean) == 1 and clean[0] in ansrow and len(ansrow) == 1:
                        lab = clean[0]
                    elif (_ms_vertical and len(clean) == 1 and not ans
                          and len(rebut) == len(labels) - 1):
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
            # F97 (v0.23.0): the bare-answer row fallback — some printed MS rows
            # carry ONLY the answer token (no notes cell), which the row parser
            # routes to a single mark_point while solution_md stays empty. The
            # part then serves an empty solution box next to a populated mark
            # point (Task 19 deep-audit census: 2021-06 1C 2(b)(ii) '25',
            # 2021-11 2C 1(d) '73'). The fallback re-emits the SAME verbatim
            # token as the solution body — no authoring, no paraphrase — and
            # discloses the re-emission through edits[] (G2-D). Refuses to fire
            # when the MS text is only a margin-note fragment or a bare marks
            # digit (the 2023-06 2CR 7(c)(i) class: the real answer is a printed
            # drawing; re-emitting the marks digit would fabricate an answer).
            if not (p["solution_md"] or "").strip() and (p.get("marks") or 0) > 0 \
                    and p["mark_points"] and all((mp.get("text_md") or "").strip() for mp in p["mark_points"]) \
                    and not _mp_only_fragments(p["mark_points"], p.get("marks")):
                _fb = "\n".join(mp["text_md"].strip() for mp in p["mark_points"])
                p["solution_md"] = _fb
                p.setdefault("edits", []).append({
                    "field": "solution_md", "kind": "structural-repair",
                    "tool": f"official_examq_extract.py v{CONVERTER_VERSION} (F97 bare-answer fallback)",
                    "evidence_ref": "Task 19 deep-audit da-sweep (empty-solution census); verbatim re-emission of the part's own mark_points text",
                })
                p["edit_status"] = "corrected"
            # v0.31.0 (F116, F111 class 5): the F47 ledger's
            # transcription_of_record is the rendering of record for
            # MS-image-answer parts (ledger == corpus == fresh). Emitted
            # VERBATIM — whitespace-immune: the 2D letter arrangement IS the
            # drawing; the standard prose whitespace law destroys it (the
            # v0.30.1-and-before fresh emissions collapsed it — the F111
            # class-5 delta). Exactly one mark_point is lawful (the drawing
            # scores a single mark); the solution's provenance is the ledger.
            _tor = p.pop("_f47_transcription", None)
            if _tor is not None:
                if len(p["mark_points"]) != 1:
                    raise SystemExit(
                        f"F47 transcription_of_record requires exactly 1 mark_point "
                        f"({series}/{paper} {p['part_number']}: got {len(p['mark_points'])})")
                p["solution_md"] = _tor
                p["mark_points"][0]["text_md"] = _tor
                p["edit_status"] = "corrected"
                p.setdefault("edits", []).append({
                    "field": "solution_md+mark_points[0].text_md",
                    "kind": "structural-repair",
                    "tool": (f"official_examq_extract.py v{CONVERTER_VERSION} "
                             f"(F47 ledger application — replay of the F107 "
                             f"adjudication of record)"),
                    "evidence_ref": (f"MS-LINK-OVERRIDES.json {series}/{paper}/"
                                     f"{p['part_number']}: the F47 ledger entry is the "
                                     f"adjudication of record — the printed MS answer cell "
                                     f"is a hand-annotated photograph; the eyeball evidence "
                                     f"chain and transcription_of_record live in the entry."),
                })
                p["_f47_value_trace"] = (f"ms-image-eyeball-transcription "
                                         f"(F47 ledger {series}/{paper}/{p['part_number']})")
            if cfg.get("ms_layout") == "vertical":
                # v0.17.0: the vertical layout carries the marks digit on its own
                # line — build_solution's tail-scan cannot see it; the vertical
                # parser's per-entry marks map is the corroboration source
                # (None when the layout withheld it — G7 skips, never guesses).
                p["_ms_marks"] = ms_marks_by_key.get(eff_key)

    # ---- page anchoring + assets -------------------------------------------
    pdf = fitz.open(QP_PDF)
    # F48: same mapping both sides. v0.18.0 (F70): the BEL strip mirrors
    # clean_lines so the fixed problem_md probes keep matching the page index
    # exactly as the BEL-bearing probes did (same pages anchor, same results).
    # F92 mirror law: the ü→✓ tick sub transforms problem_md, so the anchoring
    # probes must see the SAME transform on the page side or the subbed parts
    # lose their page anchor (found live: 2025-06 2C 5(c)(i) and 2025-11 2C 1(a)
    # both dropped to source_page None + crop-required downgrade before this
    # mirror). Same pattern as the F70 BEL-strip mirror.
    _tick_sub = re.compile(r"(?<=\bticks\s\()ü(?=\))")
    page_norm = [norm(_tick_sub.sub("✓", normalize_pua(pg.get_text())).replace("\x07", "")) for pg in pdf]
    # v0.10 (F41): OCR-covered pages contribute their prepared text to the
    # page-normalized index, so mentions on recovered pages anchor with real
    # page attribution.
    for e in ocr_pages:
        t = (P["ocr_index"].parent / f"qp-p{e['page']:02d}.txt").read_text()
        if e["page"] - 1 < len(page_norm):
            page_norm[e["page"] - 1] = norm(t.replace("\x07", ""))   # F70 parity
    # source-defect census: rasterized pages carry no text layer (seen in 2019-06:
    # 8 image-only pages; Q7 lost entirely, Q1/Q11/Q12/Q13/Q15 partly)
    IMG_ONLY_CHARS = 40
    image_only_pages = [i + 1 for i, pg in enumerate(pdf) if len(pg.get_text().strip()) < IMG_ONLY_CHARS]
    ocr_covered = {e["page"] for e in ocr_pages}   # F41: recovered, not lost
    footer_page = {}
    for i, pg in enumerate(pdf):
        t = pg.get_text()
        for m in footer_re.finditer(t):
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

    # ---- v0.16 (F64): MCQ choice script restoration -------------------------
    # The plain-text option lines flatten print scripts: the 2026-06 1(a)
    # options printed as NH4(sub) with a raised + and its distractor with a
    # RAISED 4 both arrive as "NH4+" — a duplicate-choice ambiguity (the
    # first G8 audit, igcse-chemistry-19, 2026-10-25). The printed page
    # carries the truth in span geometry: a small RAISED span is a
    # superscript, a small LOWERED span a subscript, and a floating charge
    # span ("+" / "−") is picked up geometrically even at full size.
    # Rebuild every short (formula-length scope guard — options only, never
    # prose) choice from its row's spans; FAIL CLOSED when the rebuilt text
    # does not normalize back to the extracted text (scripts stripped, dashes
    # normalized, whitespace dropped) — a geometry mis-read aborts the slice
    # instead of shipping a wrong formula. Rows are matched by label + flat
    # text equality against the extracted line, and the first match at/below
    # the part's own problem text wins — the same-label-rows-on-one-page
    # hazard (two questions listing option A on one page) can no longer
    # cross-contaminate a rebuild.
    _F64_SUP = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵",
                "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "+": "⁺", "-": "⁻",
                "−": "⁻", "–": "⁻", "(": "⁽", ")": "⁾", "n": "ⁿ", "m": "ᵐ",
                "=": "⁼"}
    _F64_SUB = {"0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅",
                "6": "₆", "7": "₇", "8": "₈", "9": "₉", "+": "₊", "-": "₋",
                "−": "₋", "–": "₋", "(": "₍", ")": "₎", "=": "₌"}
    _F64_UNSTYLE = {}
    for _c6, _p6 in list(_F64_SUP.items()) + list(_F64_SUB.items()):
        _F64_UNSTYLE[_p6] = "-" if _c6 in ("-", "−", "–") else _c6
    _F64_SCRIPT_MAX = 32          # formula-length scope guard
    _F64_STYLE_CHARS = frozenset(_F64_SUP.values()) | frozenset(_F64_SUB.values())
    _F64_LABEL_RE = re.compile(r"^\s*\(?\s*([A-E])\s*[).:]?\s*")

    def _f64_unstyle(s):
        return "".join(_F64_UNSTYLE.get(ch, ch) for ch in s)

    def _f64_key(s):
        return re.sub(r"\s+", "", _f64_unstyle(
            str(s).replace("−", "-").replace("–", "-")).lower())

    def _f64_rows(page):
        # Visual rows, not dict lines: raised/lowered script spans often land
        # in their OWN dict line (floating above the option row they belong
        # to), so lines under-group. Group instead around the option LABEL
        # anchors by baseline proximity (raised ≈ base − 5.4, lowered ≈
        # base + 1.8 in the observed 4CH1 layouts; option rows sit 24 pt
        # apart, so the −9/+6 window cannot reach a neighbouring row).
        spans = []
        for blk in page.get_text("dict")["blocks"]:
            if blk.get("type") != 0:
                continue
            for ln in blk.get("lines") or []:
                for sp in (ln.get("spans") or []):
                    if sp.get("text", "").strip():
                        spans.append(sp)
        anchors = [sp for sp in spans
                   if _F64_LABEL_RE.match(sp["text"]) and sp["bbox"][0] < 140]
        rows = []
        for a in anchors:
            cand = [sp for sp in spans
                    if sp is not a and sp["bbox"][0] >= a["bbox"][0] - 2
                    and -9.0 <= sp["origin"][1] - a["origin"][1] <= 6.0]
            cand.sort(key=lambda s: (round(s["bbox"][0], 1), s["origin"][1]))
            rows.append([a] + cand)
        return rows

    def _f64_rebuild(spans, label):
        lm = _F64_LABEL_RE.match(spans[0]["text"])
        if lm is None or lm.group(1) != label:
            return None
        texts = [spans[0]["text"][lm.end():]]
        texts += [sp["text"] for sp in spans[1:]]
        if not "".join(texts).strip():
            return None
        dom = max(sp["size"] for sp in spans)
        bases = sorted(sp["origin"][1] for sp in spans if sp["size"] >= 0.9 * dom)
        base = bases[len(bases) // 2]
        out, prev = [], None
        for sp, t in zip(spans, texts):
            if prev is not None and t:
                gap = sp["bbox"][0] - prev["bbox"][2]
                if (gap > 0.3 * dom and not out[-1].endswith(" ")
                        and not t.startswith(" ")):
                    out.append(" ")
            small = sp["size"] < 0.82 * dom
            raised = bool(t) and sp["bbox"][3] <= base - 0.5
            lowered = bool(t) and sp["origin"][1] >= base + 0.5
            charge = re.fullmatch(r"[+−-]+", t.strip() or "?") is not None
            if (small or charge) and raised:
                out.append("".join(_F64_SUP.get(c, c) for c in t))
            elif (small or charge) and lowered:
                out.append("".join(_F64_SUB.get(c, c) for c in t))
            else:
                out.append(t)
            if t:
                prev = sp
        return "".join(out).strip()

    n_f64 = 0
    for _q in doc_questions:
        for _p in _q["parts"]:
            if not _p.get("choices"):
                continue
            _pg = _p.get("source_page")
            if not isinstance(_pg, int) or not (1 <= _pg <= len(pdf)):
                continue
            _page = pdf[_pg - 1]
            _rows = _f64_rows(_page)
            # anchor y of the part's own problem text (same-label disambiguation)
            _probe = _f64_key(_p.get("problem_md") or "")[:60]
            _py = 0.0
            if _probe:
                for blk in _page.get_text("dict")["blocks"]:
                    for ln in blk.get("lines") or []:
                        _t = "".join(sp.get("text", "") for sp in (ln.get("spans") or []))
                        if _probe in _f64_key(_t):
                            _py = ln["bbox"][3]
                            break
            for _c in _p["choices"]:
                _md = (_c.get("text_md") or "").strip()
                if not _md or len(_md) > _F64_SCRIPT_MAX:
                    continue
                _want = _f64_key(_md)
                _cands = []
                for _spans in _rows:
                    if not re.match(rf"^\(?\s*{_c['label']}\s*[).:]?\s*",
                                    _spans[0]["text"]):
                        continue
                    _rb = _f64_rebuild(_spans, _c["label"])
                    if _rb is not None and _f64_key(_rb) == _want:
                        _cands.append((_spans[0]["bbox"][1], _rb))
                if not _cands:
                    continue
                _below = [c for c in _cands if c[0] >= _py - 1.0]
                _y, _rb = (_below or _cands)[0]
                if os.environ.get("EXAMQ_F64_DEBUG"):
                    print(f"F64DBG p={_p['part_number']} {_c['label']} md={_md!r} "
                          f"cands={[(round(y,1), r) for y, r in _cands]!r} py={_py:.1f}",
                          file=sys.stderr)
                if _rb != _md and any(ch in _F64_STYLE_CHARS for ch in _rb):
                    # restore only real script restorations — a script-free
                    # rebuild (pure spacing/kerning artefacts) keeps the
                    # extracted text verbatim
                    _c["text_md"] = _rb
                    n_f64 += 1
    if n_f64:
        report.setdefault("wave24", {})["choice_script_restored"] = n_f64

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
        if cfg["crop_review_legacy"]:
            # F39 chemistry convention: 1C keeps the legacy bare '<series>' home,
            # other variants use '<series>:<paper>'.
            crop_reviews = _review_doc.get(series, {}) if paper == "1C" else _review_doc.get(f"{series}:{paper}", {})
        else:
            # v0.16.0 non-chemistry lanes are spec-namespaced so verdict homes
            # never collide across lanes: '4ph1-<series>:<paper>'.
            crop_reviews = _review_doc.get(f"{cfg['spec_code'].lower()}-{series}:{paper}", {})
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

    # ---- v0.30.0 (F113): MS answer-figure ledger ---------------------------
    # The F95 census's MS-answer-is-a-drawing class: parts whose printed MS
    # answer cell is a figure/table/hand-drawn photo the text layer cannot
    # carry (the F95 ledger filed this as the open MS-side crop wave; until
    # this converter version every crop rendered QP-side only). The eyeballed
    # boxes live in MS-ANSWER-FIGURES.json — one flat verdict per part keyed
    # '<series>/4CH1-<paper>:<part_number>' with the MS page (1-based); the
    # F45 manual_crop verdict pass below renders the stub FROM THE MS PDF.
    # The ledger is the eyeball record of provenance (same rhythm as
    # STEM-RESTORE stemFigures -> CROP-REVIEW verdicts). Fail-closed: a
    # malformed entry, an unconsumed ledger key (typo'd part number), or an
    # id collision aborts the run instead of silently shipping a stub.
    _ms_fig_path = RES_DIR / "Official-ExamQuestion" / "MS-ANSWER-FIGURES.json"
    _ms_fig_entries = {}
    if _ms_fig_path.exists():
        _ms_fig_entries = json.loads(_ms_fig_path.read_text()).get("verdicts", {})
    _ms_pdf_doc = [None]
    _ms_page_rasters = {}

    def _ms_doc():
        if _ms_pdf_doc[0] is None:
            if not MS_PDF.exists():
                raise SystemExit(
                    "F113: MS-ANSWER-FIGURES entries present but the MS PDF is missing")
            _ms_pdf_doc[0] = fitz.open(MS_PDF)
        return _ms_pdf_doc[0]

    def _ms_rasters(pg):
        if pg not in _ms_page_rasters:
            mp = _ms_doc()[pg - 1]
            _ms_page_rasters[pg] = [fitz.Rect(i["bbox"]) for i in mp.get_image_info()
                                    if i["bbox"][2] - i["bbox"][0] >= 5
                                    and i["bbox"][3] - i["bbox"][1] >= 5]
        return _ms_page_rasters[pg]

    _ms_fig_consumed = set()
    n_msfig_stubs = 0
    if _ms_fig_entries:
        for q in doc_questions:
            for p in q["parts"]:
                _e = _ms_fig_entries.get(f"{series}/4CH1-{paper}:{p['part_number']}")
                if not isinstance(_e, dict):
                    continue
                _aid, _pg = _e.get("id"), _e.get("page")
                if (not isinstance(_aid, str) or not _aid
                        or not isinstance(_pg, int) or not (1 <= _pg <= len(_ms_doc()))
                        or not isinstance(_e.get("mention") if _e.get("mention") is not None else "", str)):
                    raise SystemExit(
                        f"F113 ms-answer-figure malformed for "
                        f"{series}/4CH1-{paper}:{p['part_number']}: {_e!r}")
                if any(a["id"] == _aid for pp in doc_questions for a in (pp.get("assets") or [])):
                    raise SystemExit(f"F113 ms-answer-figure id collision: {_aid}")
                p.setdefault("assets", []).append({
                    "id": _aid, "kind": "crop-required",
                    "mention": _e.get("mention") or "ms answer figure",
                    "source": "ms.pdf", "page": _pg, "review": True,
                    "ms_answer_figure": True, "_src_text": [],
                })
                _ms_fig_consumed.add(f"{series}/4CH1-{paper}:{p['part_number']}")
                crop_stats["pending"] += 1
                n_msfig_stubs += 1
        # unconsumed-key guard is SLICE-SCOPED: the ledger is corpus-wide
        # (every slice's run reads the same file), so only keys owned by THIS
        # series/paper may be left unconsumed — another slice's entries are
        # that slice's run's business.
        _owned_prefix = f"{series}/4CH1-{paper}:"
        _unconsumed = sorted(k for k in set(_ms_fig_entries) - _ms_fig_consumed
                             if k.startswith(_owned_prefix))
        if _unconsumed:
            raise SystemExit(
                f"F113 ms-answer-figure ledger keys not consumed by any part: {_unconsumed}")
    if n_msfig_stubs:
        report.setdefault("f113", {})["ms_answer_figure_stubs"] = n_msfig_stubs

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
    # v0.24.0 (F99, the crop-eyeball wave): two new verdicts from the physics
    # eyeball tranche, both fail-closed and both data-driven (chemistry has no
    # such entries, so bit-identity holds by construction):
    #   'rejected' (kind==crop only) — the emitted crop is the WRONG region
    #   (a stem figure, a photograph, or a false mention anchor). The crop is
    #   withdrawn: the asset demotes to an honest crop-required stub, the
    #   stale PNG is removed, and review clears with review_verdict
    #   'rejected' (the eyeballed "this mention has no croppable figure"
    #   decision, recorded with its own history marker).
    #   'recrop' (kind==crop only) — the emitted crop targeted the wrong
    #   region/page or the wrong bounds; the SAME asset id re-renders at the
    #   eyeballed box. review clears with review_verdict 'recrop'.
    # F45 page moves: an entry whose box page differs from the asset's own
    # page must carry page_move: true (explicit disclosure — a silent typo
    # can never move a crop to another page); the asset's page then follows
    # the box's page and the move is visible on the emitted record.
    for q in doc_questions:
        for p in q["parts"]:
            for a in p.get("assets") or []:
                v = crop_reviews.get(a["id"])
                if not isinstance(v, dict):
                    continue
                vd = v.get("verdict")
                if vd == "rejected":
                    if a.get("kind") != "crop":
                        raise SystemExit(
                            f"F99 rejected requires kind==crop: {a['id']} kind={a.get('kind')!r}")
                    _stale = OUT / (a.get("path") or "")
                    if a.get("path") and _stale.exists():
                        _stale.unlink()
                    for k in ("path", "render", "text_coverage", "manual_crop"):
                        a.pop(k, None)
                    a["kind"] = "crop-required"
                    a["review"] = False
                    a["review_verdict"] = "rejected"
                    crop_stats["crops"] -= 1
                    crop_stats["pending"] += 1
                    crop_stats["withdrawn"] = crop_stats.get("withdrawn", 0) + 1
                    continue
                if vd == "recrop":
                    if a.get("kind") != "crop":
                        raise SystemExit(
                            f"F99 recrop requires kind==crop: {a['id']} kind={a.get('kind')!r}")
                    mc = v.get("manual_crop")
                    if not isinstance(mc, dict):
                        raise SystemExit(f"F99 recrop requires manual_crop: {a['id']}")
                    mc_pg, mc_rect = mc.get("page"), mc.get("rect")
                    if (not isinstance(mc_pg, int) or not (1 <= mc_pg <= len(pdf))
                            or not isinstance(mc_rect, list) or len(mc_rect) != 4
                            or not all(isinstance(x, (int, float)) and x >= 0 for x in mc_rect)):
                        raise SystemExit(f"F99 recrop malformed for {a['id']}: {mc!r}")
                    if a.get("page") is not None and int(a["page"]) != mc_pg \
                            and not v.get("page_move"):
                        raise SystemExit(
                            f"F99 recrop page {mc_pg} != asset page {a.get('page')} for "
                            f"{a['id']} without page_move disclosure")
                    # F113: an ms.pdf-sourced asset re-renders from the MS PDF
                    # (page numbers are MS pages; the raster index is the MS
                    # page's) — the QP path is unchanged for QP assets.
                    if a.get("source") == "ms.pdf":
                        _rc_doc, _rc_rasters = _ms_doc(), _ms_rasters(mc_pg)
                    else:
                        _rc_doc, _rc_rasters = pdf, (
                            (clusters_for(mc_pg), page_rasters[mc_pg])[1])
                    if not (1 <= mc_pg <= len(_rc_doc)):
                        raise SystemExit(
                            f"F99 recrop page {mc_pg} out of range for {a['id']} "
                            f"(source={a.get('source') or 'qp.pdf'})")
                    _rc_page = _rc_doc[mc_pg - 1]
                    _rc_clip = fitz.Rect(*[float(x) for x in mc_rect]) & _rc_page.rect
                    if _rc_clip.is_empty or _rc_clip.width < 20 or _rc_clip.height < 20:
                        raise SystemExit(f"F99 recrop degenerate rect for {a['id']}: {mc_rect}")
                    _rc_rel = f"assets/{a['id']}.png"
                    _rc_pix = _rc_page.get_pixmap(clip=_rc_clip, dpi=CROP_DPI)
                    _rc_pix.save(str(OUT / _rc_rel))
                    a["path"] = _rc_rel
                    a["page"] = mc_pg
                    a["render"] = ("raster" if any(rb.contains(_rc_clip) for rb in _rc_rasters)
                                   else "vector")
                    a["text_coverage"] = text_coverage(_rc_page, _rc_clip)
                    a["manual_crop"] = True
                    a["review"] = False
                    a["review_verdict"] = "recrop"
                    continue
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
                    if a.get("page") is not None and int(a["page"]) != mc_pg \
                            and not v.get("page_move"):
                        raise SystemExit(
                            f"F45 manual_crop page {mc_pg} != stub page {a.get('page')} for "
                            f"{a['id']} without page_move disclosure")
                    # F113: an ms.pdf-sourced stub renders from the MS PDF
                    # (the stub's page is an MS page; validation above already
                    # pinned it against the QP — re-validate against the MS
                    # doc so the two page spaces can never be confused).
                    if a.get("source") == "ms.pdf":
                        mc_doc, mc_rasters = _ms_doc(), _ms_rasters(mc_pg)
                    else:
                        mc_doc, mc_rasters = pdf, (
                            (clusters_for(mc_pg), page_rasters[mc_pg])[1])
                    if not (1 <= mc_pg <= len(mc_doc)):
                        raise SystemExit(
                            f"F45 manual_crop page {mc_pg} out of range for {a['id']} "
                            f"(source={a.get('source') or 'qp.pdf'})")
                    mc_page = mc_doc[mc_pg - 1]
                    mc_clip = fitz.Rect(*[float(x) for x in mc_rect]) & mc_page.rect
                    if mc_clip.is_empty or mc_clip.width < 20 or mc_clip.height < 20:
                        raise SystemExit(f"F45 manual_crop degenerate rect for {a['id']}: {mc_rect}")
                    mc_rel = f"assets/{a['id']}.png"
                    mc_pix = mc_page.get_pixmap(clip=mc_clip, dpi=CROP_DPI)
                    mc_pix.save(str(OUT / mc_rel))
                    a["kind"] = "crop"
                    a["path"] = mc_rel
                    a["page"] = mc_pg
                    a["render"] = ("raster" if any(rb.contains(mc_clip) for rb in mc_rasters)
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

    # ---- v0.31.0 (F116, F111 class 7): F94 shared-asset curation replay -----
    # STEM-RESTORE stemFigure entries may carry share_with [{part, asset}]:
    # the sibling parts that answer from the same printed figure carry the
    # of-record shared-ref asset entries VERBATIM (the F94 curation of
    # record; the F111 census class-7 delta — the v0.30.1-and-before fresh
    # emissions lost the sibling refs entirely, dropping the figure from the
    # siblings' learner surface and the questions.md shared-with captions).
    # Applied AFTER the verdict pass so the owner crop is fully resolved
    # (path/render/text_coverage final). Fail-closed:
    #   - the owner asset must exist resolved (kind=="crop" with a path),
    #   - ref_part must resolve to the owner (asset id, or a part number
    #     carrying the owner's path),
    #   - the target part must exist in the same question,
    #   - an existing different asset with the same id aborts (id collision);
    #     an identical entry is an idempotent no-op,
    #   - slice-scoped consumption: every share_with item owned by this
    #     series/paper must be consumed (the F113 unconsumed-key law).
    _share_consumed = 0
    for q in doc_questions:
        _skey = f"{series}/4CH1-{paper}:Q{q['question_number']}"
        _sentry = _stem_entries.get(_skey) or {}
        for _sf in _sentry.get("stemFigures") or []:
            _sw = _sf.get("share_with") or []
            if not _sw:
                continue
            _owner = next((a for pp in q["parts"] for a in (pp.get("assets") or [])
                           if a.get("id") == _sf.get("id")), None)
            if _owner is None or _owner.get("kind") != "crop" or not _owner.get("path"):
                raise SystemExit(
                    f"F94 share_with owner not resolved for {_skey} {_sf.get('id')}: "
                    f"kind={(_owner or {}).get('kind')!r} path={(_owner or {}).get('path')!r}")
            for _item in _sw:
                _tgt_pn = _item.get("part")
                _asset = _item.get("asset")
                if (not isinstance(_tgt_pn, str) or not isinstance(_asset, dict)
                        or not isinstance(_asset.get("id"), str)):
                    raise SystemExit(f"F94 share_with malformed for {_skey}: {_item!r}")
                _tp = next((pp for pp in q["parts"] if pp["part_number"] == _tgt_pn), None)
                if _tp is None:
                    raise SystemExit(f"F94 share_with target part missing: {_skey} -> {_tgt_pn}")
                _ref = _asset.get("ref_part")
                _ref_ok = (_ref == _sf.get("id")
                           or any(pp["part_number"] == _ref
                                  for pp in q["parts"]
                                  for a in (pp.get("assets") or [])
                                  if a.get("path") == _owner.get("path")))
                if not _ref_ok:
                    raise SystemExit(
                        f"F94 share_with ref_part {_ref!r} does not resolve to the owner "
                        f"{_sf.get('id')} for {_skey} -> {_tgt_pn}")
                _cur = next((a for a in (_tp.get("assets") or [])
                             if a.get("id") == _asset["id"]), None)
                if _cur is not None:
                    if _cur == _asset:
                        _share_consumed += 1
                        continue
                    raise SystemExit(
                        f"F94 share_with id collision: {_asset['id']} already on {_tgt_pn} "
                        f"with different content ({_skey})")
                _tp.setdefault("assets", []).append(_asset)
                _share_consumed += 1
    _share_owned = 0
    for _k, _v in _stem_entries.items():
        if not _k.startswith(f"{series}/4CH1-{paper}:"):
            continue
        for _sf in (_v or {}).get("stemFigures") or []:
            _share_owned += len(_sf.get("share_with") or [])
    if _share_owned and _share_consumed < _share_owned:
        raise SystemExit(
            f"F94 share_with items not consumed: {_share_consumed}/{_share_owned} "
            f"for {series}/4CH1-{paper}")
    if _share_consumed:
        report.setdefault("f94", {})["shared_asset_refs"] = _share_consumed

    # ---- spec tags: v0.5 demo seeds + v0.7 llm spec-tagging waves -----------
    # Labels only (AGENTS.md review taxonomy: 'pending-llm' -> seed via LLM as
    # labels, re-validated by G6). Wave files live in spec-labels/<series>.json
    # as {"parts": {"<part_number>": ["4CH1-x.y", ...]}}; question-level tags
    # are expanded to their parts by the wave authoring script.
    seeds = (cfg["seeds"].get(series, {})
             if paper == cfg["seeds_paper"] else {})   # demo seeds are default-paper artifacts (F31)
    _labels_stem = (f"{series}" if paper == cfg["default_paper"] else f"{series}-{paper}")
    if cfg["labels_prefixed"]:
        _labels_stem = f"{cfg['spec_code'].lower()}-{_labels_stem}"
    labels_path = (RES_DIR / "Official-ExamQuestion" / "spec-labels" /
                   f"{_labels_stem}.json")
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
            _p["edit_status"] = ("corrected"
                                 if (_p.get("_marks_fill") or _p.get("edit_status") == "corrected")
                                 else "extracted")
            _p["value_trace"] = {"keys": _kt,
                                 "marks": ({"f73a": "corrected:qp-glued-marker-sum-law",
                                            "f73b": "corrected:render-ms-marks-patch"}[_p["_marks_fill"]]
                                           if _p.get("_marks_fill")
                                           else (_p.pop("marks_inferred", None) or "ms-printed")),
                                 "numbers": "source-printed"}
            # v0.31.0 (F116, F111 class 5): the F47 ledger-applied transcription
            # records its provenance — the value comes from the ledger entry of
            # record (accurate for the surgical application AND the replay).
            _f47vt = _p.pop("_f47_value_trace", None)
            if _f47vt:
                _p["value_trace"]["solution"] = _f47vt
            # v0.21.0 (F85): pop the repeat-label print-defect markers into the
            # part's value_trace — disclosed on the record, never serialized on
            # the choice rows.
            _rel = [c["_relabel"] for c in (_p.get("choices") or []) if "_relabel" in c]
            for _c in _p.get("choices") or []:
                _c.pop("_relabel", None)
            if _rel:
                _p["value_trace"]["choices"] = (
                    f"normalized:qp-print-defect-repeat-label "
                    f"({len(_rel)} option row(s) printed '{_rel[0]}' where the "
                    f"A–D run required the next letter; completed per the "
                    f"canonical printed run — MS of record corroborates; F85)")

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
    _g1_details = {"mismatches": g1_bad, "unattributed": unattributed_bad,
                   "inferred_totals": inferred_totals, "footer_gaps": footer_gaps,
                   "image_only_pages": content_img_pages, "count_expected": expect_q}
    if sole_part_inferred:
        _g1_details["sole_part_marks_inferred"] = sole_part_inferred   # v0.17.0 disclosure
    report["gates"].append({
        "gate": "G1-structure", "status": "PASS" if g1_ok else ("REVIEW" if g1_review else "FAIL"),
        "summary": (f"{len(doc_questions)} questions; Σ question totals={total}/{PAPER_TOTAL}; "
                    f"parts-sum == printed total for all questions: {not g1_bad}"
                    if not footer_gaps and not inferred_totals else
                    f"{len(doc_questions)} questions extracted; Σ known totals={total}/{PAPER_TOTAL}; "
                    f"source defects: missing Q{sorted(defective)} (image-only pages "
                    f"{content_img_pages} in archive PDF) — lost content needs human/OCR re-ingest"),
        "details": _g1_details})
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
    # F94 (v0.23.0) — the drawing-option MCQ-candidate census: 'Which structure /
    # diagram / drawing ...?' problems that name a bare A-D option run but carry
    # NO choices[] (the options are printed drawings the text layer linearizes).
    # The v0.22.0 gate reported '0 MCQ parts' for 2026-06 2C while Q1(b) is one —
    # a vacuous pass this census makes visible. Report-only (these parts are
    # honestly structured; the option drawings are a crop-wave item).
    _which_re = re.compile(r"\bwhich\s+(?:structure|diagram|drawing|row|particle|equation)\b", re.I)
    _opt_run_re = re.compile(r"(?:^|\s)A\s{1,3}[BCD]\s{1,3}(?:C|B|D)?\b")
    mcq_candidates = [p["part_number"] for q in doc_questions for p in q["parts"]
                      if p["question_type"] != "multiple_choice"
                      and (_which_re.search(p["problem_md"]) or _opt_run_re.search(p["problem_md"]))]
    for pn in mcq_candidates:
        report["review_queue"].append({"part": pn,
                                       "reason": "drawing-option MCQ candidate (options linearized in problem_md, no choices[])"})
    gate("G3-mcq-integrity", not g3_issues,
         f"{len(mcq)} MCQ parts; all have printed A–D and MS-keyed answer: {not g3_issues}; "
         f"{len(mcq_candidates)} drawing-option MCQ candidates (census, F94)",
         {"issues": g3_issues, "drawing_option_mcq_candidates": mcq_candidates})

    # G4 figure resolution
    dangling = [{"part": p["part_number"]} for q in doc_questions for p in q["parts"]
                if figure_mentions(p["problem_md"]) and not p["assets"]]
    # F96 (v0.23.0) — the drawing-linearization census: problem text carrying the
    # linearized remains of a printed drawing (≥4 single-letter atom tokens in a
    # run / bond-fragment letter triples) with NO figure asset. The v0.22.0 gate
    # counted only table/diagram/grid/apparatus MENTION nouns, so 2026-06 2C
    # Q1(b)/(c)(ii)/(c)(iii) passed G4 while serving 'H H H H H H A C C C B C C C
    # ...' garbage. Report-only + review-queue entries; the content fix is a
    # crop+strip wave per part (the 2C tranche ships with this release).
    _atom_run_re = re.compile(r"(?:\b[CHONSPKl-]\b[ ,]*){4,}")
    _bond_frag_re = re.compile(r"\b[CON]\s+[CON]\s+[CON]\b")
    drawing_gaps = []
    for q in doc_questions:
        for p in q["parts"]:
            if p.get("assets"):
                continue
            pm = p["problem_md"]
            if _atom_run_re.search(pm) or _bond_frag_re.search(pm):
                drawing_gaps.append({"part": p["part_number"],
                                     "probe": (_atom_run_re.search(pm) or _bond_frag_re.search(pm)).group(0)[:40]})
                report["review_queue"].append({"part": p["part_number"],
                                               "reason": "drawing-linearization in problem_md without figure asset (F96)"})
    n_assets = sum(len(p["assets"]) for q in doc_questions for p in q["parts"])
    n_unanchored = sum(1 for q in doc_questions for p in q["parts"] if p["source_page"] is None)
    gate("G4-figure-resolution", not dangling,
         f"{n_assets} asset records cover every table/diagram/grid/apparatus mention: "
         f"{crop_stats['crops']} cropped to assets/*.png ({CROP_DPI} dpi), "
         f"{crop_stats['pending']} remain crop-required; "
         f"{n_unanchored} parts without page anchor; "
         f"{len(drawing_gaps)} drawing-linearization gaps (census, F96)"
         + (f"; {crop_stats['withdrawn']} wrong-region crops withdrawn by eyeball verdict"
            if crop_stats.get("withdrawn") else ""),
         {"dangling": dangling, "pages_unanchored": n_unanchored, "crop_stats": crop_stats,
          "drawing_gaps": drawing_gaps})
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
    g6_bad = []
    for q in doc_questions:
        for p in q["parts"]:
            for c in p["spec_point_codes"]:
                if c not in registry and c not in cfg["allowed_gaps"]:
                    g6_bad.append({"part": p["part_number"], "code": c})
    n_pending = sum(1 for p in parts_all if p["tagging"] == "pending-llm")
    n_nospec = sum(1 for p in parts_all if p["tagging"] == "no-spec-point")
    gate("G6-registry-codes", not g6_bad,
         f"all emitted codes ∈ spec_point_resolution registry ({len(registry)} codes) "
         f"or documented gaps→review; {n_pending} parts pending-llm tagging; "
         f"{n_nospec} parts no-spec-point (terminal, documented per part)",
         {"violations": g6_bad, "allowed_gaps": sorted(cfg["allowed_gaps"])})

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
    # F95 (v0.23.0) — the mark-point answer-gap census: parts whose EVERY
    # mark_point text is a margin-note fragment or a marks-digit leak — the
    # MS-answer-is-a-drawing class the sum law cannot see (G7 passed 2026-06
    # 2C 5(a) while its served MPs were 'If M1 and M2 not fully' / 'max 1
    # mark': two fragments of one margin note, the two printed formulae
    # absent). Report-only + review-queue entries; the fix is an MS-side crop
    # (converter MS-crop support = the filed follow-up wave).
    mp_gap = []
    for p in parts_all:
        mp = p.get("mark_points") or []
        if not mp or not (p.get("marks") or 0) > 0:
            continue
        if _mp_only_fragments(mp, p.get("marks")):
            mp_gap.append({"part": p["part_number"],
                           "mp_texts": [ (m.get("text_md") or "")[:40] for m in mp ]})
            report["review_queue"].append({"part": p["part_number"],
                                           "reason": "mark-point answer gap: MPs are margin-note fragments / marks digit (MS answer is a printed drawing)"})
    gate("G7-solution-emission", not no_sol and not sum_bad,
         f"solution_md on {len(sol_parts) - len(no_sol)}/{len(sol_parts)} linked parts; "
         f"mark_points sum == part marks everywhere: {not sum_bad}; "
         f"MS marks-column digit read for {ms_seen} parts, agrees with QP marks on {ms_agree}; "
         f"{len(mp_gap)} mark-point answer gaps (census, F95; the printed-drawing subclass serves via the F113 MS-answer-figure crops)",
         {"missing_solution": no_sol, "sum_mismatches": sum_bad,
          "ms_marks_seen": ms_seen, "ms_marks_agree": ms_agree,
          "ms_marks_disagree": ms_disagree, "mp_answer_gap": mp_gap})

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
                       "course_id": cfg["course_id"]},
        "questions": [{
            "id": f"{manifest['paper']['official_reference'].replace('/', '-')}-{q['question_number']:02d}",
            "question_number": q["question_number"],
            "total_marks": q["printed_total"] if q["printed_total"] is not None else inferred_totals[q["question_number"]],
            "total_marks_source": "printed-footer" if q["printed_total"] is not None else "inferred-parts-footer-missing",
            "stem_md": q["stem_md"],
            "parts": [{k: v for k, v in p.items()
                       if k not in ("group_stem_md", "option_list", "group", "roman", "answer_raw", "source_norm", "_ms_marks", "_owner", "_kept", "_glue_cands", "_marks_fill")
                       and (v is not None or k in ("marks",))}
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
        # v0.16.0: `.get` — a part may legitimately carry marks=None (dropped key
        # in serialization); chemistry never hit this, a physics 1P part does.
        # None -> 1 is still an undisclosed graded-value movement: the detector
        # sees the marks delta and refuses it (detected=True), exactly the N1 law.
        tgt["marks"] = (tgt.get("marks") or 0) + 1
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
        next(p for q in nc3["questions"] for p in q["parts"])["spec_point_codes"] = [cfg["nc_fake_code"]]
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
            marks = f"[{p['marks']}]" if p.get("marks") is not None else "[?]"
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
