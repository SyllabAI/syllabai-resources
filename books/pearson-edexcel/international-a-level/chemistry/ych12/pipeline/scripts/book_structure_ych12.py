"""Structure map for IAL Chemistry SB2 (YCH12 lane) — single source of truth for the chunker.

Derived from the book's own COURSE STRUCTURE pages (PDF 4-7 = roman iv-vii),
cross-checked against rendered openers, the CONTENTS page (PDF 3), and printed
header digits (books/README.md §5 phase 2; YCH11 README page-law section).
Page law: book = pdf - 12 (4-way confirmed: TOC openers, printed '299' on PDF 311,
printed '306'/'305' graph leaves, end leaf '308' on PDF 320); roman = pdf - 0
(PDF 2-13 = ii-xiii, i absent). Book page 1 does not exist in the PDF (print
blank omitted); arabic starts at book 2 = PDF 14. L-021: TOC's INDEX 299 promise
present -> copy COMPLETE.
"""

BOOK_TITLE = "Pearson Edexcel International AS/A Level Chemistry Student Book 2"
BOOK_AUTHOR = "Cliff Curtis, Jason Murgatroyd, David Scott"
SHA256 = "44af34a590914e81bac53b0fbdca92a742ce7c0b43cd6b85166a39be670ee748"
N_PAGES = 320
OFFSET = 12  # book = pdf - 12

# unit_no = topic number (11-20); the IAL unit mapping is Unit 4 = Topics 11-15, Unit 5 = Topics 16-20
UNIT_NAMES = {
    11: "Unit 4: Rates, Equilibria and Further Organic Chemistry",
    12: "Unit 4: Rates, Equilibria and Further Organic Chemistry",
    13: "Unit 4: Rates, Equilibria and Further Organic Chemistry",
    14: "Unit 4: Rates, Equilibria and Further Organic Chemistry",
    15: "Unit 4: Rates, Equilibria and Further Organic Chemistry",
    16: "Unit 5: Transition Metals and Organic Nitrogen Chemistry",
    17: "Unit 5: Transition Metals and Organic Nitrogen Chemistry",
    18: "Unit 5: Transition Metals and Organic Nitrogen Chemistry",
    19: "Unit 5: Transition Metals and Organic Nitrogen Chemistry",
    20: "Unit 5: Transition Metals and Organic Nitrogen Chemistry",
}

TOPIC_TITLES = {
    11: "Topic 11: Kinetics II",
    12: "Topic 12: Entropy and Energetics",
    13: "Topic 13: Chemical Equilibria",
    14: "Topic 14: Acid-Base Equilibria",
    15: "Topic 15: Organic Chemistry: Carbonyls, Carboxylic Acids and Chirality",
    16: "Topic 16: Redox Equilibria",
    17: "Topic 17: Transition Metals and Their Chemistry",
    18: "Topic 18: Organic Chemistry: Arenes",
    19: "Topic 19: Organic Nitrogen Compounds: Amines, Amides, Amino Acids and Proteins",
    20: "Topic 20: Organic Synthesis",
}

# (unit/topic, chapter letter label, title, body_first_book_page, body_last_book_page)
# chapter start = its first section / LEARNING OBJECTIVES page (opener convention,
# verified on renders: 12A LO = PDF 44 = book 32); end = page before next entry.
# Every topic's opener spread (divider 2pp) carries the chapter-list chip, NOT the
# chapter banner — unlike a first reading of PDF 14, 11A genuinely starts at book 4.
CHAPTERS = [
    (11, "11A", "Further Kinetics", 4, 25),
    (12, "12A", "Entropy", 32, 43),
    (12, "12B", "Lattice Energy", 44, 53),
    (13, "13A", "Chemical Equilibria", 60, 73),
    (14, "14A", "Strong and Weak Acids", 80, 90),
    (14, "14B", "Acid-Base Titrations", 91, 101),
    (15, "15A", "Chirality", 108, 113),
    (15, "15B", "Carbonyl Compounds", 114, 121),
    (15, "15C", "Carboxylic Acids", 122, 125),
    (15, "15D", "Carboxylic Acid Derivatives", 126, 133),
    (15, "15E", "Spectroscopy and Chromatography", 134, 153),
    (16, "16A", "Standard Electrode Potential", 160, 171),
    (16, "16B", "Redox in Action", 172, 177),
    (17, "17A", "Principles of Transition Metal Chemistry", 184, 198),
    (17, "17B", "Transition Metal Reactions", 199, 211),
    (17, "17C", "Transition Metals as Catalysts", 212, 215),
    (18, "18A", "Arenes: Benzene", 222, 231),
    (19, "19A", "Amines, Amides, Amino Acids and Proteins", 238, 253),
    (20, "20A", "Organic Structures", 260, 277),
]

# topic dividers share the two pages before the first chapter of the topic
TOPIC_DIVIDERS = {
    11: (2, 3), 12: (30, 31), 13: (58, 59), 14: (78, 79), 15: (106, 107),
    16: (158, 159), 17: (182, 183), 18: (220, 221), 19: (236, 237), 20: (258, 259),
}

# per-topic THINKING BIGGER (2pp) and EXAM PRACTICE banks (2pp) — TB first pages
# mined from content banners (pdf 38/66/86/114/166/190/228/244/266/290), matching
# the course-structure promises (74/102/178/254/278 ...)
THINKING_BIGGER = {11: (26, 27), 12: (54, 55), 13: (74, 75), 14: (102, 103), 15: (154, 155),
                   16: (178, 179), 17: (216, 217), 18: (232, 233), 19: (254, 255), 20: (278, 279)}
EXAM_PRACTICE = {11: (28, 29), 12: (56, 57), 13: (76, 77), 14: (104, 105), 15: (156, 157),
                 16: (180, 181), 17: (218, 219), 18: (234, 235), 19: (256, 257), 20: (280, 281)}

# back matter in book pages (arabic), per the course structure page (roman vii)
EXTRA_SECTIONS = [
    ("maths_skills", 282, 285, "Maths skills"),
    ("preparing_for_exams", 286, 292, "Preparing for your exams"),
    ("command_words", 293, 294, "Command words"),
    ("glossary", 295, 297, "Glossary"),
    ("periodic_table", 298, 298, "Periodic table"),
    ("index", 299, 304, "Index"),
    ("graph_paper", 305, 308, "Graph paper"),
]

# front matter roman pages PDF 2-13 (book_pages: null)
FRONT_MATTER_PDF = (2, 13)

# marker families (Curtis/Murgatroyd/Scott book), same census as YCH11 (L-013 discipline)
MARKERS = {
    "learning_objectives": r"LEARNING\s*\.?\s*OBJECTIVES|LEARNINGOBJECTIVES",
    "exam_hint": r"EXAM\s*HINT",
    "learning_tip": r"LEARNING\s*TIP",
    "checkpoint": r"CHECKPOINT",
    "subject_vocabulary": r"SUBJECT\s*VOCABULARY",
    "did_you_know": r"DID\s*YOU\s*KNOW",
    "thinking_bigger": r"THINKING\s*BIGGER",
    "exam_practice": r"EXAM\s*PRACTICE",
    "maths_skills": r"MATHS\s*SKILLS\s*FOR\s*THIS\s*TOPIC|MATHS\s*SKILLS",
    "spec_reference": r"SPEC\s*REFERENCE",
    "core_practical": r"CORE\s*PRACTICAL",
    "activity": r"^\s*ACTIVITY\b|\bACTIVITY\s*\d",
    "worked_example": r"WORKED\s*EXAMPLE",
    "key_point": r"KEY\s*POINT",
}

# content-type priority when a page/item matches several (higher wins)
TYPE_PRIORITY = [
    "topic_divider", "chapter_opener", "front_matter",
    "unit_questions", "chapter_questions",
    "thinking_bigger", "exam_practice",
    "learning_objectives", "subject_vocabulary", "checkpoint",
    "maths_skills", "preparing_for_exams", "command_words",
    "glossary", "periodic_table", "index", "graph_paper",
    "skills", "body",
]


def chapter_for(book_page: int):
    """(unit, chapter_label, title) for a book page inside a chapter body, else None."""
    for unit, label, title, b, e in CHAPTERS:
        if b <= book_page <= e:
            return unit, label, title
    return None


def topic_for(book_page: int):
    """Topic number for any arabic book page 2..308."""
    for unit, label, title, b, e in CHAPTERS:
        if b <= book_page <= e:
            return unit
    for t, (b, e) in TOPIC_DIVIDERS.items():
        if b <= book_page <= e:
            return t
    for t, (b, e) in THINKING_BIGGER.items():
        if b <= book_page <= e:
            return t
    for t, (b, e) in EXAM_PRACTICE.items():
        if b <= book_page <= e:
            return t
    if book_page >= 282:
        return 20
    return None


def boundary_coherence():
    """Assert the arabic map tiles 2..308 with no gaps/overlaps (validator-grade)."""
    claims = []  # (first, last, kind, label)
    for t, (b, e) in TOPIC_DIVIDERS.items():
        claims.append((b, e, "divider", f"topic {t}"))
    for unit, label, title, b, e in CHAPTERS:
        claims.append((b, e, "chapter", label))
    for t, (b, e) in THINKING_BIGGER.items():
        claims.append((b, e, "tb", f"topic {t}"))
    for t, (b, e) in EXAM_PRACTICE.items():
        claims.append((b, e, "ep", f"topic {t}"))
    for kind, b, e, title in EXTRA_SECTIONS:
        claims.append((b, e, kind, title))
    claims.sort()
    problems = []
    prev_end = 1  # arabic starts at book 2 (book 1 does not exist)
    for b, e, kind, label in claims:
        if b != prev_end + 1:
            problems.append(f"gap/overlap before {kind} {label}: expect {prev_end + 1}, got {b}")
        if e < b:
            problems.append(f"inverted range {kind} {label}")
        prev_end = e
    if prev_end != 308:
        problems.append(f"map ends at {prev_end}, expected 308")
    return problems


if __name__ == "__main__":
    probs = boundary_coherence()
    print("boundary_coherence:", "OK (tiles 2..308 exactly)" if not probs else probs)
