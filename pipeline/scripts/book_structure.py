#!/usr/bin/env python3
"""Structural map of the Edexcel International GCSE (9-1) Chemistry Student Book.
Derived empirically from: contents pages (PDF 4-6), unit dividers (11/131/215/263),
LEARNING OBJECTIVES chapter starts, running headers, and answers-section groupings.
PDF page = book page + OFFSET (offset=9)."""

BOOK_TITLE = "Edexcel International GCSE (9-1) Chemistry Student Book"
BOOK_AUTHOR = "Jim Clark"
SOURCE_URL = ("https://github.com/SyllabAI/syllabai-resources/blob/main/"
              "edexcel-international-gcse-9-1-chemistry-student-book-pdf-free.pdf")
PDF_PATH = "/home/z/my-project/data/chemistry_book.pdf"
OCR_DIR = "/home/z/my-project/data/ocr_pages"
OUT_DIR = "/home/z/my-project/download/rag_chemistry"
N_PAGES = 383
OFFSET = 9  # book_page = pdf_page - OFFSET

UNIT_NAMES = {
    1: "Principles of Chemistry",
    2: "Inorganic Chemistry",
    3: "Physical Chemistry",
    4: "Organic Chemistry",
}
UNIT_NAME_CAPS = [n.upper() for n in UNIT_NAMES.values()]

# (chapter_no, unit, title, book_page)  -- from the book's own contents pages
CHAPTERS = [
    (1,  1, "States of matter", 3),
    (2,  1, "Elements, compounds and mixtures", 14),
    (3,  1, "Atomic structure", 24),
    (4,  1, "The periodic table", 30),
    (5,  1, "Chemical formulae, equations and calculations - part 1 (chemistry only)", 38),
    (6,  1, "Chemical formulae, equations and calculations - part 2", 64),
    (7,  1, "Ionic bonding", 75),
    (8,  1, "Covalent bonding", 85),
    (9,  1, "Metallic bonding (chemistry only)", 98),
    (10, 1, "Electrolysis (chemistry only)", 101),
    (11, 2, "The alkali metals", 123),
    (12, 2, "The halogens", 130),
    (13, 2, "Gases in the atmosphere", 137),
    (14, 2, "Reactivity series", 145),
    (15, 2, "Extraction and uses of metals (chemistry only)", 160),
    (16, 2, "Acids, alkalis and titrations", 167),
    (17, 2, "Acids, bases and salt preparations", 173),
    (18, 2, "Chemical tests", 190),
    (19, 3, "Energetics", 207),
    (20, 3, "Rates of reaction", 227),
    (21, 3, "Reversible reactions and equilibria", 240),
    (22, 4, "Introduction to organic chemistry", 255),
    (23, 4, "Crude oil", 268),
    (24, 4, "Alkanes", 277),
    (25, 4, "Alkenes", 282),
    (26, 4, "Alcohols (chemistry only)", 287),
    (27, 4, "Carboxylic acids (chemistry only)", 293),
    (28, 4, "Esters (chemistry only)", 297),
    (29, 4, "Synthetic polymers", 302),
]

# Non-chapter sections: (key, pdf_start, pdf_end, unit, label, content_type)
EXTRA_SECTIONS = [
    ("front_matter",  1,  10,  None, "Front matter (contents, about this book, assessment overview)", "front_matter"),
    ("unit1_divider", 11, 11,  1,    "Unit 1 divider and chapter map", "divider"),
    ("unit1_questions", 123, 130, 1, "Unit 1: end-of-unit questions", "unit_questions"),
    ("unit2_divider", 131, 131, 2,   "Unit 2 divider and chapter map", "divider"),
    ("unit2_skills", 211, 214, 2,    "Unit 2: chemistry-only skills pages", "skills"),
    ("unit2_questions", 208, 210, 2, "Unit 2: end-of-unit questions", "unit_questions"),
    ("unit3_divider", 215, 215, 3,   "Unit 3 divider and chapter map", "divider"),
    ("unit3_questions", 257, 262, 3, "Unit 3: end-of-unit questions", "unit_questions"),
    ("unit4_divider", 263, 263, 4,   "Unit 4 divider and chapter map", "divider"),
    ("unit4_questions", 322, 328, 4, "Unit 4: end-of-unit questions", "unit_questions"),
    ("appendices", 329, 336, None,   "Appendices (periodic table, command words, practical guide)", "appendix"),
    ("glossary", 337, 344, None,     "Glossary", "glossary"),
    ("index", 345, 353, None,        "Index", "index"),
    ("answers_u1", 354, 364, 1,      "Answers - Unit 1", "answers"),
    ("answers_u2", 365, 371, 2,      "Answers - Unit 2", "answers"),
    ("answers_u3", 372, 376, 3,      "Answers - Unit 3", "answers"),
    ("answers_u4", 377, 383, 4,      "Answers - Unit 4", "answers"),
]

# Inline feature markers found in OCR text
MARKERS = {
    "learning_objectives": r"LEARNING\s+OBJECTIVES",
    "chapter_questions":   r"CHAPTER\s+QUESTIONS",
    "activity":            r"^ACTIVITY\s*\d*\s*$",
    "practical":           r"PRACTICAL\s+(?:ACTIVITY|INVESTIGATION)",
    "did_you_know":        r"DID\s+YOU\s+KNOW",
    "key_point":           r"^KEY\s+POINTS?\s*$",
    "worked_example":      r"WORKED\s+EXAMPLE",
    "exam_hint":           r"^HINT\s*$",
    "safety":              r"^Safety\s+Note:",
}

# content-type priority when several markers co-occur in one chunk (low -> high)
TYPE_PRIORITY = ["body", "safety", "did_you_know", "exam_hint", "key_point",
                 "worked_example", "activity", "practical", "chapter_questions",
                 "learning_objectives", "unit_questions"]

# Common element symbols for safe chemical-formula rejoining
ELEMENTS = {
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si",
    "P", "S", "Cl", "Ar", "K", "Ca", "Ti", "Cr", "Mn", "Fe", "Co", "Ni", "Cu",
    "Zn", "Br", "Ag", "I", "Ba", "Pb", "Sn", "Hg", "Au", "W", "Pt", "Sr", "Cs",
}

# Chunk packing targets (chars)
TARGET_MIN, TARGET_MAX, HARD_MAX, MERGE_MIN = 350, 1600, 2400, 250
