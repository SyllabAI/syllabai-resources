#!/usr/bin/env python3
"""Structural map of Pearson Edexcel International A2 Level Physics Student Book 2
(Miles Hudson, Pearson 2019, ISBN 978-1292244478) — YPH11 lane, corpus prefix yph2.

Derived empirically from: contents page (PDF 3), course structure spread (PDF 4-5),
running headers ("SAMPLE EXAM ANSWERS 213" at PDF 223 -> offset 10), topic-divider
and chapter-opener headers in the parsed corpus, THINKING BIGGER + EXAM PRACTICE
pair census, and "(Total for Question" anchor scan.
PDF page = book page + OFFSET (offset=10; roman front matter i-xi = PDF 1-11;
arabic numbering starts at book 2 = PDF 12 — no printed page 1, same as SB1).

Topic/chapter map (book pages):
  TOPIC 5 FURTHER MECHANICS 2-25:    5A Further Momentum 2, 5B Circular Motion 14
  TOPIC 6 ELECTRIC AND MAGNETIC FIELDS 26-71:
       6A Electric Fields 26, 6B Capacitors 42, 6C Electromagnetic Effects 56
  TOPIC 7 NUCLEAR AND PARTICLE PHYSICS 72-115:
       7A Probing Matter 72, 7B Particle Accelerators and Detectors 84,
       7C The Particle Zoo 100
  TOPIC 8 THERMODYNAMICS 116-131:    8A Heat and Temperature 116
  TOPIC 9 NUCLEAR DECAY 132-149:     9A Radioactivity 132
  TOPIC 10 OSCILLATIONS 150-167:     10A Oscillations 150
  TOPIC 11 ASTROPHYSICS AND COSMOLOGY 168-203:
       11A Gravitational Fields 168, 11B Space 178
  MATHS SKILLS 204-209; PREPARING FOR YOUR EXAMS 210-211;
  SAMPLE EXAM ANSWERS 212-217; COMMAND WORDS 218-219; GLOSSARY 220-223;
  INDEX 224-227. No picture-credits page in this book.
Each of the 13 chapters ends: THINKING BIGGER (2pp, second page often a
SCIENCE COMMUNICATION activity) then EXAM PRACTICE (2pp).

SOURCE INTEGRITY NOTE (2026-10-22, T-PARSE-YPH11-1): the archive copy first
landed at intake (41,870,983 B, sha256 449dc3f3...) was TRUNCATED at 225 pp —
it ended mid-sample-answers (book 215) and lacked the sample-answers tail,
command words, glossary and index (books 216-227). Re-sourced from the
provenance-of-record URL (Googlebot-UA method): original 120,888,486 B,
sha256 28eabe40... (matches lane README exactly), 237 pp complete; this
structure module is built from a fresh 145 dpi derivative of that original:
48,278,974 B, sha256 f8f3fc62...ce82d, OCR parity 1.0000 on contents page.
"""

BOOK_TITLE = "Pearson Edexcel International A2 Level Physics Student Book 2"
BOOK_AUTHOR = "Miles Hudson"
SOURCE_PDF = ("books/pearson-edexcel/international-a-level/physics/yph11/"
              "source/student-book-2.pdf")
SHA256 = "f8f3fc62e55c9ae606b57351f107c22d0c8887f80e9fd565c6a76e176d7ce82d"
PDF_PATH = "/home/z/my-project/data/ial_physics/student-book-2.pdf"
PAGES_DIR = "/home/z/my-project/data/ial_physics/docling_pages_sb2"
OUT_DIR = "/home/z/my-project/download/rag_ial_physics"
N_PAGES = 237
OFFSET = 10  # book_page = pdf_page - OFFSET (no printed book page 1)
ID_PREFIX = "yph2_v1"

UNIT_NAMES = {
    5: "Further Mechanics",
    6: "Electric and Magnetic Fields",
    7: "Nuclear and Particle Physics",
    8: "Thermodynamics",
    9: "Nuclear Decay",
    10: "Oscillations",
    11: "Astrophysics and Cosmology",
}
UNIT_NAME_CAPS = [n.upper() for n in UNIT_NAMES.values()]

# (chapter_no, unit, title, book_page) -- chapter_no sequential 1-13; the
# book's own codes (5A..11B) kept in the title.
CHAPTERS = [
    (1,  5,  "5A Further Momentum", 2),
    (2,  5,  "5B Circular Motion", 14),
    (3,  6,  "6A Electric Fields", 26),
    (4,  6,  "6B Capacitors", 42),
    (5,  6,  "6C Electromagnetic Effects", 56),
    (6,  7,  "7A Probing Matter", 72),
    (7,  7,  "7B Particle Accelerators and Detectors", 84),
    (8,  7,  "7C The Particle Zoo", 100),
    (9,  8,  "8A Heat and Temperature", 116),
    (10, 9,  "9A Radioactivity", 132),
    (11, 10, "10A Oscillations", 150),
    (12, 11, "11A Gravitational Fields", 168),
    (13, 11, "11B Space", 178),
]

CHAPTER_QUESTIONS_PDF = {
    1: (22, 23), 2: (34, 35), 3: (50, 51), 4: (64, 65), 5: (80, 81),
    6: (92, 93), 7: (108, 109), 8: (124, 125), 9: (140, 141), 10: (158, 159),
    11: (176, 177), 12: (186, 187), 13: (212, 213),
}
THINKING_BIGGER_PDF = {
    1: (20, 21), 2: (32, 33), 3: (48, 49), 4: (62, 63), 5: (78, 79),
    6: (90, 91), 7: (106, 107), 8: (122, 123), 9: (138, 139), 10: (156, 157),
    11: (174, 175), 12: (184, 185), 13: (210, 211),
}

EXTRA_SECTIONS = [
    ("front_matter",  1,  11,  None, "Front matter (cover, contents, course structure, about this book, practical skills, assessment overview)", "front_matter"),
    ("maths_skills",  214, 219, None, "Maths skills (reference)", "skills"),
    ("exam_prep",     220, 221, None, "Preparing for your exams", "skills"),
    ("sample_answers", 222, 227, None, "Sample exam answers with commentary", "sample_answers"),
    ("command_words", 228, 229, None, "Command words", "skills"),
    ("glossary",      230, 233, None, "Glossary", "glossary"),
    ("index",         234, 237, None, "Index", "index"),
]
for _cno, _rng in CHAPTER_QUESTIONS_PDF.items():
    EXTRA_SECTIONS.append((f"q{_cno:02d}", _rng[0], _rng[1], CHAPTERS[_cno - 1][1],
                           f"Chapter {CHAPTERS[_cno - 1][2]} exam practice",
                           "chapter_questions"))
for _cno, _rng in THINKING_BIGGER_PDF.items():
    EXTRA_SECTIONS.append((f"tb{_cno:02d}", _rng[0], _rng[1], CHAPTERS[_cno - 1][1],
                           f"Chapter {CHAPTERS[_cno - 1][2]} thinking bigger",
                           "thinking_bigger"))

MARKERS = {
    "learning_objectives": r"LEARNING[.\s]*OBJECTIVES",
    "maths_skills_chapter": r"MATHS\s*SKILLS\s*FOR\s*(THIS\s*CHAPTER|PHYSICISTS)|MATHSSKILLSFOR",
    "chapter_questions":   r"^EXAM\s*PRACTICE\s*$|^EXAMPRACTICE\s*$",
    "checkpoint":          r"^CHECKPOINT\s*$",
    "exam_hint":           r"^EXAM\s*HINTS?\s*$|^EXAMHINT\s*$|^INTERPRETATION\s*NOTE$|^INTERPRETATIONNOTE$|^THINKING\s*BIGGER\s*TIP$|^THINKINGBIGGERTIP$",
    "worked_example":      r"^WORKED\s*EXAMPLES?\s*\d*\s*$|^WORKEDEXAMPLES?\d*\s*$",
    "learning_tip":        r"^LEARNING\s*TIP\s*$|^LEARNINGTIP\s*$",
    "subject_vocabulary":  r"^SUBJECT\s*VOCABULARY\s*$|^SUBJECTVOCABULARY\s*$",
    "physics_in_detail":   r"^PHYSICS\s*IN\s*DETAIL\s*$|^PHYSICSINDETAIL\s*$",
    "science_communication": r"^SCIENCE\s*COMMUNICATION\s*$|^SCIENCECOMMUNICATION\s*$",
    "did_you_know":        r"^DID\s*YOU\s*KNOW\?*\s*$|^DIDYOUKNOW\?*\s*$",
    "practical":           r"PRACTICAL\s*SKILLS|^PRACTICALSKILLS|^PRACTICAL\b",
    "activity":            r"^ACTIVITY\s*\d*\s*$",
    "safety":              r"^Safety\s+Note:",
}

TYPE_PRIORITY = ["body", "did_you_know", "science_communication", "learning_tip",
                 "subject_vocabulary", "physics_in_detail", "exam_hint",
                 "practical", "worked_example", "activity", "checkpoint",
                 "thinking_bigger", "learning_objectives", "chapter_questions"]

TARGET_MIN, TARGET_MAX, HARD_MAX, MERGE_MIN = 350, 1600, 2400, 250
