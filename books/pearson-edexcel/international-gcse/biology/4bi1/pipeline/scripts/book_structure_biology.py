#!/usr/bin/env python3
"""Structural map of the Edexcel International GCSE (9-1) Biology Student
Book (Bradfield & Potter; Pearson 2017, ISBN 978-0435185084).

Derived empirically 2026-10-21 (T-PARSE-4BI1-1) from:
- course-structure pages (book iii-v) — chapter titles + book pages + spec codes
- running-header digits (R-top: 93 hits follow book = 2*spread - 9 across
  spreads 72-178; L-top hits follow 2*spread - 10)
- "More questions on ... can be found at the end of Unit N on page M"
  cross-reference lines: exactly 22, one per chapter — anchor each chapter's
  end-of-chapter question section (see QUESTION_RANGES)
- UNIT QUESTIONS headers (sz ~17) + "Total N marks" census (probe_4bi1_derive_structure.py)
- ANSWERS section: "UNIT 1 ANSWERS" header at book 329 (spread 169 R); runs
  to book 348; book 349 = blank back cover (0 text lines, 11 cover images)

Book form: 179 landscape 2-up spreads; book_page(L of spread s) = 2s-10,
book_page(R of spread s) = 2s-9. Book page 1 = spread 5 R; spreads 1-5 L
= cover + roman i-viii (front matter). Three-way confirmed.
"""

BOOK_TITLE = "Edexcel International GCSE (9-1) Biology Student Book"
BOOK_AUTHOR = "Philip Bradfield, Steve Potter"
SOURCE_PDF = "books/pearson-edexcel/international-gcse/biology/4bi1/source/student-book.pdf"
SHA256 = "974ad65d913108b9caa98df9eda1584e546177854bcd5efa6d8642797d093006"
PDF_PATH = "/home/z/my-project/data/biology/student-book.pdf"
PAGES_DIR = "/home/z/my-project/data/biology/text_pages"
OUT_DIR = "/home/z/my-project/download/rag_biology"
N_SPREADS = 179          # PDF pages (2-up spreads)
N_HALVES = 358           # book half-pages incl. front/back matter
N_BOOK_PAGES = 349       # numbered book pages 1..349
ID_PREFIX = "bio_v1"

# ---- spread -> book page helpers (the 2-up law) --------------------------
def book_page_of(spread: int, side: str):
    """book page number for a half-page; None for unnumbered halves."""
    if side == "L":
        bp = 2 * spread - 10
    else:
        bp = 2 * spread - 9
    return bp if bp >= 1 else None

def spread_side_of(book_page: int):
    """(spread, side) for a numbered book page."""
    if book_page % 2 == 0:
        return (book_page + 10) // 2, "L"
    return (book_page + 9) // 2, "R"

# 1-based half index in BOOK PAGE ORDER: s1L=1, s1R=2, ..., s5R(=book 1)=10,
# s6L(=book 2)=11 ... s179R=358
def half_index_of_book_page(bp: int) -> int:
    sp, side = spread_side_of(bp)
    return (sp - 1) * 2 + (1 if side == "L" else 2)

UNIT_NAMES = {
    1: "Organisms and Life Processes",
    2: "Animal Physiology",
    3: "Plant Physiology",
    4: "Ecology and the Environment",
    5: "Variation and Selection",
    6: "Microorganisms and Genetic Modification",
}

# (chapter_no, unit, title, book_page of LEARNING OBJECTIVES opener) --
# course-structure digits, cross-checked against opener scans
CHAPTERS = [
    (1,  1, "Life processes", 3),
    (2,  1, "The variety of living organisms", 25),
    (3,  2, "Breathing and gas exchange", 39),
    (4,  2, "Food and digestion", 52),
    (5,  2, "Blood and circulation", 70),
    (6,  2, "Coordination", 84),
    (7,  2, "Chemical coordination", 98),
    (8,  2, "Homeostasis and excretion", 104),
    (9,  2, "Reproduction in humans", 118),
    (10, 3, "Plants and food", 135),
    (11, 3, "Transport in plants", 152),
    (12, 3, "Chemical coordination in plants", 168),
    (13, 3, "Reproduction in plants", 174),
    (14, 4, "Ecosystems", 187),
    (15, 4, "Human influences on the environment", 204),
    (16, 5, "Chromosomes, genes and DNA", 227),
    (17, 5, "Cell division", 240),
    (18, 5, "Genes and inheritance", 249),
    (19, 5, "Natural selection and evolution", 261),
    (20, 5, "Selective breeding", 268),
    (21, 6, "Using microorganisms", 281),
    (22, 6, "Genetic modification", 289),
]

# Chapter end-of-chapter question sections (book-page ranges, inclusive).
# Start = page carrying the "More questions on ..." cross-reference line
# (or the CHAPTER QUESTIONS header), end = last page before the next
# opener / unit bank / divider. 22/22 chapters anchored.
QUESTION_RANGES = [
    (1,  23, 24), (2,  30, 31), (3,  49, 51), (4,  67, 69), (5,  81, 83),
    (6,  95, 97), (7,  102, 103), (8,  115, 117), (9,  126, 129),
    (10, 148, 151), (11, 164, 167), (12, 172, 173), (13, 179, 181),
    (14, 201, 203), (15, 218, 220), (16, 238, 239), (17, 246, 248),
    (18, 258, 260), (19, 266, 267), (20, 274, 276), (21, 287, 288),
    (22, 299, 300),
]

# Non-chapter sections: (key, book_page_start, book_page_end, unit, label,
# content_type). book ranges; front matter / back cover are half-page ranges
# expressed via FRONT_MATTER_HALVES / BACK_COVER_HALVES below.
EXTRA_SECTIONS = [
    ("skills",          1,   1,   None, "Experimental skills (intro)", "skills"),
    ("unit1_divider",   2,   2,   1,    "Unit 1 divider and chapter map", "divider"),
    ("unit1_questions", 32,  37,  1,    "Unit 1: end-of-unit questions", "unit_questions"),
    ("unit2_divider",   38,  38,  2,    "Unit 2 divider and chapter map", "divider"),
    ("unit2_questions", 130, 133, 2,    "Unit 2: end-of-unit questions", "unit_questions"),
    ("unit3_divider",   134, 134, 3,    "Unit 3 divider and chapter map", "divider"),
    ("unit3_questions", 182, 185, 3,    "Unit 3: end-of-unit questions", "unit_questions"),
    ("unit4_divider",   186, 186, 4,    "Unit 4 divider and chapter map", "divider"),
    ("unit4_questions", 221, 225, 4,    "Unit 4: end-of-unit questions", "unit_questions"),
    ("unit5_divider",   226, 226, 5,    "Unit 5 divider and chapter map", "divider"),
    ("unit5_questions", 277, 279, 5,    "Unit 5: end-of-unit questions", "unit_questions"),
    ("unit6_divider",   280, 280, 6,    "Unit 6 divider and chapter map", "divider"),
    ("unit6_questions", 301, 302, 6,    "Unit 6: end-of-unit questions", "unit_questions"),
    ("appendices",      303, 308, None, "Appendices A-B (experimental skills, command words)", "appendix"),
    ("glossary",        309, 319, None, "Glossary", "glossary"),
    ("index",           320, 328, None, "Index", "index"),
    ("answers",         329, 348, None, "Answers (by unit and chapter)", "answers"),
]

# half indices (1..358): front matter = spreads 1-5 L halves (cover, i-viii);
# back cover = spread 179 R (blank, pixel-verified: 0 text lines, 11 images)
FRONT_MATTER_SPREADS = (1, 5)   # inclusive spread range, L halves only
BACK_COVER_HALVES = (179, "R")

# chapter ranges in book pages, with question ranges split out
def chapter_page_ranges():
    """[(ch_no, unit, title, bp_start, bp_end)] — body ranges only
    (question ranges and dividers/banks excluded downstream)."""
    out = []
    for i, (cno, unit, title, start) in enumerate(CHAPTERS):
        nxt = CHAPTERS[i + 1][3] if i + 1 < len(CHAPTERS) else N_BOOK_PAGES + 1
        out.append((cno, unit, title, start, nxt - 1))
    return out

# Inline feature markers found in the text layer (CMap-garble aware:
# "KEV POINT", "kEY POIHl", "W ANING OBJECTIVES", "BIOL OGY ONL Y")
MARKERS = {
    "learning_objectives": r"O\s*B\s*J\s*E\s*C\s*T\s*I\s*V\s*E\s*S\s*$",
    "chapter_questions":   r"C\s*H\s*A\s*P\s*T\s*E\s*R\s+Q\s*U\s*E\s*S\s*T\s*I\s*O\s*N\s*S",
    "unit_questions":      r"U\s*N\s*I\s*T\s+Q\s*U\s*E\s*S\s*T\s*I\s*O\s*N\s*S",
    "activity":            r"^A\s*C\s*T\s*I\s*V\s*I\s*T\s*Y\s*\d*\s*$",
    "practical":           r"P\s*R\s*A\s*C\s*T\s*I\s*C\s*A\s*L\b|^PRACTICAL\b",
    "extension_work":      r"^E\s*X\s*T\s*E\s*N\s*S\s*I\s*O\s*N\s+W\s*O\s*R\s*K\s*$",
    "key_point":           r"^K\s*E\s*[VY]\s*P\s*[OI]\s*I\s*N\s*T\s*l?\s*$|^kEY POIHl$",
    "did_you_know":        r"^D\s*I\s*D\s+Y\s*O\s*U\s+K\s*N\s*O\s*W\s*\??\s*$",
    "exam_hint":           r"^H\s*I\s*N\s*T\s*s?\s*$",
    "biology_only":        r"^B\s*I\s*O\s*L\s*O\s*G\s*Y\s+O\s*N\s*L\s*Y\s*$",
    "safety":              r"^Safety\s+Note:",
}

# content-type priority when several markers co-occur (low -> high);
# question/answers context types are absolute (see chunker guard)
TYPE_PRIORITY = ["body", "biology_only", "safety", "exam_hint", "key_point",
                 "did_you_know", "worked_example", "activity", "practical",
                 "extension_work", "chapter_questions",
                 "learning_objectives", "unit_questions"]

# Chunk packing targets (chars) — proven packing from 4CH1/4PH1
TARGET_MIN, TARGET_MAX, HARD_MAX, MERGE_MIN = 350, 1600, 2400, 250
