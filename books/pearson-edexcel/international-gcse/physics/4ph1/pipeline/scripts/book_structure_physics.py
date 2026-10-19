#!/usr/bin/env python3
"""Structural map of the Edexcel International GCSE (9-1) Physics Student Book
(Arnold, Johnson, Woolley; Pearson 2017).
Derived empirically from: contents pages (PDF 5-7), LEARNING OBJECTIVES chapter
opener scan of the parsed corpus (scripts/scan_physics_markers.py), running
headers, and question-marker pages.
PDF page = book page + OFFSET (offset=10; confirmed: PDF 13 = book 3 ch1 opener,
PDF 144 header prints '134')."""

BOOK_TITLE = "Edexcel International GCSE (9-1) Physics Student Book"
BOOK_AUTHOR = "Brian Arnold, Penny Johnson, Steve Woolley"
SOURCE_PDF = "books/pearson-edexcel/international-gcse/physics/4ph1/source/student-book.pdf"
SHA256 = "9b0783d9fe99790a08255eb1f2ebb6eab5833c03ef8e36dd51b7643ac68a313a"
PDF_PATH = "/home/z/my-project/data/physics/student-book.pdf"
OCR_DIR = "/home/z/my-project/data/physics/ocr_pages"
OUT_DIR = "/home/z/my-project/download/rag_physics"
N_PAGES = 308
OFFSET = 10  # book_page = pdf_page - OFFSET

UNIT_NAMES = {
    1: "Forces and Motion",
    2: "Electricity",
    3: "Waves",
    4: "Energy Resources and Energy Transfer",
    5: "Solids, Liquids and Gases",
    6: "Magnetism and Electromagnetism",
    7: "Radioactivity and Particles",
    8: "Astrophysics",
}
UNIT_NAME_CAPS = [n.upper() for n in UNIT_NAMES.values()]

# (chapter_no, unit, title, book_page) -- contents pages (PDF 5-7), refined by
# LEARNING OBJECTIVES scan: ch8 75 (TOC OCR '15'), ch16 150 (opener PDF 160),
# ch17 158 (opener PDF 168, PHYSICS ONLY), ch22 221 (opener PDF 231).
CHAPTERS = [
    (1,  1, "Movement and position", 3),
    (2,  1, "Forces and shape", 18),
    (3,  1, "Forces and movement", 28),
    (4,  1, "Momentum", 40),
    (5,  1, "The turning effect of forces (physics only)", 48),
    (6,  2, "Mains electricity", 59),
    (7,  2, "Current and voltage in circuits", 67),
    (8,  2, "Electrical resistance", 75),
    (9,  2, "Electric charge (physics only)", 84),
    (10, 3, "Properties of waves", 97),
    (11, 3, "The electromagnetic spectrum", 106),
    (12, 3, "Light waves", 113),
    (13, 3, "Sound", 123),
    (14, 4, "Energy transfers", 133),
    (15, 4, "Thermal energy", 139),
    (16, 4, "Work and power", 150),
    (17, 4, "Energy resources and electricity generation (physics only)", 158),
    (18, 5, "Density and pressure", 173),
    (19, 5, "Solids, liquids and gases", 181),
    (20, 6, "Magnetism and electromagnetism", 197),
    (21, 6, "Electric motors and electromagnetic induction", 206),
    (22, 7, "Atoms and radioactivity", 221),
    (23, 7, "Radiation and half-life", 233),
    (24, 7, "Applications of radioactivity", 241),
    (25, 7, "Fission and fusion", 250),
    (26, 8, "Motion in the universe", 259),
    (27, 8, "Stellar evolution", 265),
    (28, 8, "Cosmology", 271),
]

# Non-chapter sections: (key, pdf_start, pdf_end, unit, label, content_type)
# Question ranges from UNIT QUESTIONS marker scan; back matter from TOC +
# GLOSSARY (PDF 295) / INDEX (PDF 299) hits. No answers section in this book.
EXTRA_SECTIONS = [
    ("front_matter",  1,  10,  None, "Front matter (contents, about this book, assessment overview)", "front_matter"),
    ("skills",        11, 11,  None, "Experimental skills (book p1)", "skills"),
    ("unit1_divider", 12, 12,  1,    "Unit 1 divider and chapter map", "divider"),
    ("unit1_questions", 65, 67, 1,  "Unit 1: end-of-unit questions", "unit_questions"),
    ("unit2_divider", 68, 68,  2,   "Unit 2 divider and chapter map", "divider"),
    ("unit2_questions", 103, 105, 2, "Unit 2: end-of-unit questions", "unit_questions"),
    ("unit3_divider", 106, 106, 3,  "Unit 3 divider and chapter map", "divider"),
    ("unit3_questions", 140, 141, 3, "Unit 3: end-of-unit questions", "unit_questions"),
    ("unit4_divider", 142, 142, 4,  "Unit 4 divider and chapter map", "divider"),
    ("unit4_questions", 178, 181, 4, "Unit 4: end-of-unit questions", "unit_questions"),
    ("unit5_divider", 182, 182, 5,  "Unit 5 divider and chapter map", "divider"),
    ("unit5_questions", 203, 205, 5, "Unit 5: end-of-unit questions", "unit_questions"),
    ("unit6_divider", 206, 206, 6,  "Unit 6 divider and chapter map", "divider"),
    ("unit6_questions", 227, 229, 6, "Unit 6: end-of-unit questions", "unit_questions"),
    ("unit7_divider", 230, 230, 7,  "Unit 7 divider and chapter map", "divider"),
    ("unit7_questions", 265, 267, 7, "Unit 7: end-of-unit questions", "unit_questions"),
    ("unit8_divider", 268, 268, 8,  "Unit 8 divider and chapter map", "divider"),
    ("unit8_questions", 285, 286, 8, "Unit 8: end-of-unit questions", "unit_questions"),
    ("appendices",    287, 294, None, "Appendices A-E (periodic table, formulae, quantities, skills, command words)", "appendix"),
    ("glossary",      295, 298, None, "Glossary", "glossary"),
    ("index",         299, 308, None, "Index", "index"),
]

# Inline feature markers found in the parsed corpus (merged-OCR form aware:
# Docling v1 headings often lose spaces, e.g. LEARNING.OBJECTIVES, KEYPOINT,
# ACTIVITY1, EXTENSIONWORK)
MARKERS = {
    "learning_objectives": r"LEARNING[.\s]*OBJECTIVES",
    "chapter_questions":   r"CHAPTER\s*QUESTIONS",
    "unit_questions":      r"UNIT\s*QUESTIONS",
    "activity":            r"^ACTIVITY\s*\d*\s*$",
    "practical":           r"PRACTICAL\s*[:\d]|^PRACTICAL\b",
    "extension_work":      r"^EXTENSION\s*WORK$",
    "key_point":           r"^KEY\s*POINTS?\s*$",
    "example":             r"^EXAMPLES?\s*\d*\s*$",
    "reminder":            r"^REMINDER\s*$",
    "exam_hint":           r"^HINT\s*$",
    "physics_only_box":    r"^PHYSICS\s*ONLY$|^END\s*OF\s*PHYSICS\s*ONLY$",
    "units_box":           r"^UNITS$",
    "safety":              r"^Safety\s+Note:",
}

# content-type priority when several markers co-occur in one chunk (low -> high)
TYPE_PRIORITY = ["body", "safety", "exam_hint", "key_point", "worked_example",
                 "activity", "practical", "chapter_questions",
                 "learning_objectives", "unit_questions"]

# Chunk packing targets (chars)
TARGET_MIN, TARGET_MAX, HARD_MAX, MERGE_MIN = 350, 1600, 2400, 250
