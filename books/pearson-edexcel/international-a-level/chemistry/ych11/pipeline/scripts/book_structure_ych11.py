"""Structure map for IAL Chemistry SB1 (YCH11 lane) — single source of truth for the chunker.

Derived from the book's own COURSE STRUCTURE pages (PDF 5-8 = roman iv-vii),
cross-checked against rendered openers and printed header digits
(books/README.md §5 phase 2; YCH11 README page-law section).
Page law: book = pdf - 13 (3-way confirmed); roman front matter = pdf - 1 (PDF 2-14 = i-xiii).
Book page 1 does not exist in the PDF (print blank omitted); arabic starts at book 2 = PDF 15.
"""

BOOK_TITLE = "Pearson Edexcel International AS/A Level Chemistry Student Book 1"
BOOK_AUTHOR = "Cliff Curtis, Jason Murgatroyd, David Scott"
SHA256 = "3d5348894f011e3fb8351f6c8badd691e1bbb2ea54d64eb306524dd0b20372eb"
N_PAGES = 329
OFFSET = 13  # book = pdf - 13

# unit_no = topic number (1-10); the IAL unit mapping is Unit 1 = Topics 1-5, Unit 2 = Topics 6-10
UNIT_NAMES = {
    1: "Unit 1: Structure, Bonding and Introduction to Organic Chemistry",
    2: "Unit 1: Structure, Bonding and Introduction to Organic Chemistry",
    3: "Unit 1: Structure, Bonding and Introduction to Organic Chemistry",
    4: "Unit 1: Structure, Bonding and Introduction to Organic Chemistry",
    5: "Unit 1: Structure, Bonding and Introduction to Organic Chemistry",
    6: "Unit 2: Energetics, Group Chemistry, Halogenoalkanes and Alcohols",
    7: "Unit 2: Energetics, Group Chemistry, Halogenoalkanes and Alcohols",
    8: "Unit 2: Energetics, Group Chemistry, Halogenoalkanes and Alcohols",
    9: "Unit 2: Energetics, Group Chemistry, Halogenoalkanes and Alcohols",
    10: "Unit 2: Energetics, Group Chemistry, Halogenoalkanes and Alcohols",
}

TOPIC_TITLES = {
    1: "Topic 1: Formulae, Equations and Amount of Substance",
    2: "Topic 2: Atomic Structure and the Periodic Table",
    3: "Topic 3: Bonding and Structure",
    4: "Topic 4: Introductory Organic Chemistry and Alkanes",
    5: "Topic 5: Alkenes",
    6: "Topic 6: Energetics",
    7: "Topic 7: Intermolecular Forces",
    8: "Topic 8: Redox Chemistry and Groups 1, 2 and 7",
    9: "Topic 9: Introduction to Kinetics and Equilibria",
    10: "Topic 10: Organic Chemistry: Halogenoalkanes, Alcohols and Spectra",
}

# (unit/topic, chapter letter label, title, body_first_book_page, body_last_book_page)
# chapter start = its LEARNING OBJECTIVES page (opener convention); end = page before next entry
CHAPTERS = [
    (1, "1A", "Atoms, elements and molecules", 4, 5),
    (1, "1B", "Equations and reaction types", 6, 15),
    (1, "1C", "Energy", 16, 25),
    (1, "1D", "Empirical and molecular formulae", 26, 29),
    (1, "1E", "Calculations with solutions and gases", 30, 35),
    (2, "2A", "Atomic structure", 42, 55),
    (2, "2B", "The periodic table", 56, 59),
    (3, "3A", "Ionic bonding", 66, 71),
    (3, "3B", "Covalent bonding", 72, 81),
    (3, "3C", "Shapes of molecules", 82, 85),
    (3, "3D", "Metallic bonding", 86, 87),
    (3, "3E", "Solid lattices", 88, 93),
    (4, "4A", "Introduction to organic chemistry", 100, 115),
    (4, "4B", "Alkanes", 116, 123),
    (5, "5A", "Alkenes", 130, 139),
    (5, "5B", "Addition polymers", 140, 143),
    (6, "6A", "Introducing enthalpy and enthalpy change", 150, 151),
    (6, "6B", "Enthalpy level diagrams", 152, 153),
    (6, "6C", "Standard enthalpy change of combustion", 154, 155),
    (6, "6D", "Standard enthalpy change of neutralisation", 156, 157),
    (6, "6E", "Standard enthalpy change of formation and Hess's law", 158, 159),
    (6, "6F", "Bond enthalpy and mean bond enthalpy", 160, 160),
    (6, "6G", "Using mean bond enthalpies", 161, 163),
    (7, "7A", "Intermolecular interactions", 170, 173),
    (7, "7B", "Intermolecular interactions and physical properties", 174, 179),
    (8, "8A", "Redox chemistry", 186, 195),
    (8, "8B", "The elements of Groups 1 and 2", 196, 207),
    (8, "8C", "Inorganic chemistry of Group 7", 208, 217),
    (8, "8D", "Quantitative chemistry", 218, 229),
    (9, "9A", "Kinetics", 236, 245),
    (9, "9B", "Equilibria", 246, 253),
    (10, "10A", "General principles in organic chemistry", 262, 263),
    (10, "10B", "Halogenoalkanes", 264, 269),
    (10, "10C", "Alcohols", 270, 277),
    (10, "10D", "Mass spectra and IR", 278, 285),
]

# topic dividers share the two pages before the first chapter of the topic
TOPIC_DIVIDERS = {
    1: (2, 3), 2: (40, 41), 3: (64, 65), 4: (98, 99), 5: (128, 129),
    6: (148, 149), 7: (168, 169), 8: (184, 185), 9: (234, 235), 10: (260, 261),
}

# per-topic THINKING BIGGER (2pp) and EXAM PRACTICE banks (2pp, T9's is 4pp)
THINKING_BIGGER = {1: (36, 37), 2: (60, 61), 3: (94, 95), 4: (124, 125), 5: (144, 145),
                   6: (164, 165), 7: (180, 181), 8: (230, 231), 9: (254, 255), 10: (286, 287)}
EXAM_PRACTICE = {1: (38, 39), 2: (62, 63), 3: (96, 97), 4: (126, 127), 5: (146, 147),
                 6: (166, 167), 7: (182, 183), 8: (232, 233), 9: (256, 259), 10: (288, 289)}

# back matter in book pages (arabic), per the course structure page (roman vii)
EXTRA_SECTIONS = [
    ("maths_skills", 290, 295, "Maths skills"),
    ("preparing_for_exams", 296, 301, "Preparing for your exams"),
    ("command_words", 302, 303, "Command words"),
    ("glossary", 304, 307, "Glossary"),
    ("periodic_table", 308, 308, "Periodic table"),
    ("index", 309, 315, "Index"),
    ("graph_paper", 316, 316, "Graph paper"),
]

# front matter roman pages PDF 2-14 (book_pages: null)
FRONT_MATTER_PDF = (2, 14)

# marker families (Curtis/Murgatroyd/Scott book), production census refined.
# regexes run on UPPERCASED item text; merged OCR forms included (L-013 discipline: census from production items).
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
    """Topic number for any arabic book page 2..316."""
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
    if book_page >= 290:
        return 10
    return None


def boundary_coherence():
    """Assert the arabic map tiles 2..316 with no gaps/overlaps (validator-grade)."""
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
    if prev_end != 316:
        problems.append(f"map ends at {prev_end}, expected 316")
    return problems
