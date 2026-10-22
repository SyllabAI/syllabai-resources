#!/usr/bin/env python3
"""Structural map of Pearson Edexcel International AS Level Physics Student Book 1
(Miles Hudson, Pearson 2018, YPH11 course book 1 of 2).
Derived empirically from: contents page (PDF 4), course structure (PDF 5-6),
visual opener probes, running headers, and the production-stack OCR probe
(pages 15-17). See pipeline/worklog.md T-PARSE-YPH11-1.

PAGE LAW (offset=11; confirmed 5 ways — roman front matter = pdf-1 with
iii=PDF4/v=PDF6/xi=PDF12; TOC cross-checks STANDARD UNITS b4=PDF15,
ESTIMATION b6=PDF17, 1 MOMENTUM b48=PDF59; INDEX header prints '211' on PDF 222):
  arabic body/back:  book_page = pdf_page - 11   (book 2..214 = PDF 13..225)
  front matter:      roman numerals  = pdf_page - 1 (book_pages stays null)
Book page 1 does NOT exist in the PDF (print-blank omitted by the
ActiveLearn/Chromium print-replica rendering).

TOP LEVEL = 4 TOPICS (this is an IAL book: Unit 1 exams Topics 1-2, Unit 2
exams Topics 3-4, per the book's own ASSESSMENT OVERVIEW tables, book 200).
The book's own word for the A/B/C/D subdivisions is CHAPTER (banner
'CHAPTER 3A BASIC WAVES') -> unit = topic, chapter = section, numbered 1-11.
Each chapter ends with a 2-page EXAM PRACTICE bank (serving-critical
chapter_questions anchors)."""

BOOK_TITLE = "Pearson Edexcel International AS Level Physics Student Book 1"
BOOK_AUTHOR = "Miles Hudson"
SOURCE_PDF = "books/pearson-edexcel/international-a-level/physics/yph11/source/student-book-1.pdf"
SHA256 = "aa1aed604d627fda8a46cf67bd562234b2934abe9d26690e1bf38c27f9c015d0"
PDF_PATH = "/home/z/my-project/data/yph11_sb1.pdf"
OCR_DIR = "/home/z/my-project/data/yph11_sb1/docling_pages"
OUT_DIR = "/home/z/my-project/download/rag_yph11"
N_PAGES = 225
OFFSET = 11  # book_page = pdf_page - OFFSET (arabic region; front matter null)

# ID grammar: yph1_v1_u<unit|0>_c<chapter|0>_pdf<pdfpage:03d>_<block:04d>
# (subject token 'yph1' = YPH11 Student Book 1; SB2 will use 'yph2' so the
# two corpora of the two-book course stay globally disjoint)

TOPIC_NAMES = {
    1: "Mechanics",
    2: "Materials",
    3: "Waves and Particle Nature of Light",
    4: "Electric Circuits",
}

# (chapter_no, unit, title, book_page) — course structure (PDF 5-6), opener
# book pages cross-checked: 1A b8=PDF19, 1 MOMENTUM b48=PDF59, TOPIC 3+3A
# b88=PDF99 (divider shares the first-chapter opener page in this book)
CHAPTERS = [
    (1,  1, "Motion",                        8),
    (2,  1, "Energy",                       34),
    (3,  1, "Momentum",                     46),
    (4,  2, "Fluids",                       58),
    (5,  2, "Solid material properties",    74),
    (6,  3, "Basic waves",                  88),
    (7,  3, "The behaviour of waves",      100),
    (8,  3, "More wave properties of light",118),
    (9,  3, "Quantum physics",             130),
    (10, 4, "Electrical quantities",       148),
    (11, 4, "Complete electrical circuits", 172),
]

# Non-chapter sections: (key, pdf_start, pdf_end, unit, label, content_type)
# EXAM PRACTICE = last 2 book pages of each chapter (TOC digits; e.g. 1A EP
# b32-33=PDF43-44; 4B EP b192-193=PDF203-204) -> chapter_questions.
# Back matter from TOC (MATHS SKILLS 194, PREPARING 200, SAMPLE EXAM ANSWERS
# 202, COMMAND WORDS 205, GLOSSARY 207, INDEX 211) + observed ACKNOWLEDGEMENTS
# b214 (unlisted in TOC — same pattern as 4BI1's unlisted ANSWERS section).
EXTRA_SECTIONS = [
    ("front_matter",  1,  12,  None, "Cover, copyright, contents, course structure, about this book, practical skills, assessment overview (roman i-xi)", "front_matter"),
    ("waap",          13, 18,  None, "Working as a Physicist: standard units + estimation (book 2-7)", "skills"),
    ("ep_1a",         43, 44,  1,    "1A Exam practice", "chapter_questions"),
    ("ep_1b",         55, 56,  1,    "1B Exam practice", "chapter_questions"),
    ("ep_1c",         67, 68,  1,    "1C Exam practice", "chapter_questions"),
    ("ep_2a",         83, 84,  2,    "2A Exam practice", "chapter_questions"),
    ("ep_2b",         97, 98,  2,    "2B Exam practice", "chapter_questions"),
    ("ep_3a",         109, 110, 3,   "3A Exam practice", "chapter_questions"),
    ("ep_3b",         127, 128, 3,   "3B Exam practice", "chapter_questions"),
    ("ep_3c",         139, 140, 3,   "3C Exam practice", "chapter_questions"),
    ("ep_3d",         157, 158, 3,   "3D Exam practice", "chapter_questions"),
    ("ep_4a",         181, 182, 4,   "4A Exam practice", "chapter_questions"),
    ("ep_4b",         203, 204, 4,   "4B Exam practice", "chapter_questions"),
    ("maths_skills",  205, 210, None, "Maths skills reference (book 194-199)", "skills"),
    ("exam_guidance", 211, 217, None, "Preparing for your exams + sample exam answers + command words (book 200-206)", "appendix"),
    ("glossary",      218, 221, None, "Glossary (book 207-210)", "glossary"),
    ("index",         222, 224, None, "Index (book 211-213, 4-column)", "index"),
    ("acknowledgements", 225, 225, None, "Acknowledgements / picture credits (book 214, unlisted in TOC)", "appendix"),
]

# Inline feature markers (merged-OCR form aware — Docling v1 headings often
# lose spaces: LEARNINGOBJECTIVES, THINKINGBIGGER). Census scan refines after
# the full parse.
MARKERS = {
    "learning_objectives": r"LEARNING[.\s]*OBJECTIVES",
    "worked_example":      r"WORKED\s*EXAMPLE",
    "exam_hint":           r"EXAM\s*HINT",
    "thinking_bigger":     r"THINKING\s*BIGGER",
    "exam_practice":       r"EXAM\s*PRACTICE",
    "maths_skills":        r"MATHS\s*SKILLS",
    "spec_reference":      r"SPECIFICATION\s*REFERENCE",
    "key_point":           r"^KEY\s*POINTS?\s*$",
    "did_you_know":        r"DID\s*YOU\s*KNOW",
    "core_practical":      r"CORE\s*PRACTICAL",
}

# content-type priority when several markers co-occur in one chunk (low -> high)
TYPE_PRIORITY = ["body", "maths_skills", "exam_hint", "worked_example",
                 "thinking_bigger", "learning_objectives", "chapter_questions"]

# Chunk packing targets (chars) — playbook §5 phase 5
TARGET_MIN, TARGET_MAX, HARD_MAX, MERGE_MIN = 350, 1600, 2400, 250
