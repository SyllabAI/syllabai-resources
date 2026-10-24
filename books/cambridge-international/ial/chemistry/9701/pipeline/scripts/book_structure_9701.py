#!/usr/bin/env python3
"""book_structure_9701.py — Cambridge IAL Chemistry 9701 Coursebook 3rd ed structure map.

Derived from probes (scripts/probe2-5_9701.py, inspect_9701.py):
- 889-page regenerated/re-laid-out PDF (DejaVu/STIX, single column, 9.2pt body).
- NO printed page numbers anywhere (TOC numberless, no edge digits, zero
  'page N' self-refs) -> corpus is PDF-page-anchored (book_pages=None, D-decision).
- 30 chapter openers (LEARNING INTENTIONS pages) + P1 (pdf522) + P2 (pdf870),
  appendices 883-887, acknowledgements 888, imprint 889.
- Chapter end anatomy: SUMMARY -> EXAM-STYLE QUESTIONS -> SELF-EVALUATION.
- Watermark: 3 CJK ad lines at top of pdf 31 and 66 (WeChat CLASS0608) -> strip.
- Sub/superscript geometry: 6.9pt spans, y below/above body baseline 9.2pt.
"""
import re

PDF_PAGES_TOTAL = 889
FRONT_MATTER_END = 14          # pdf 1-14: cover, series, TOC 4-8, how-to-use 11-12, intro 14
P1_START = 522                  # P1 Practical skills 1
CH19_START = 537
P2_START = 870                  # P2 Practical skills 2
APPENDICES_START = 883
ACKNOWLEDGEMENTS_START = 888
WATERMARK_PAGES = {31, 66}

# 30 chapter opener pages (LEARNING INTENTIONS), probed
CHAPTER_OPENERS = [15, 30, 59, 110, 154, 183, 209, 234, 283, 305, 333, 356,
                   375, 389, 421, 455, 472, 495, 537, 565, 611, 645, 685, 719,
                   748, 771, 787, 809, 829, 843]
CHAPTER_TITLES = [
    "Atomic structure", "Electrons in atoms", "Atoms, molecules and stoichiometry",
    "Chemical bonding", "States of matter", "Enthalpy changes", "Redox reactions",
    "Equilibria", "Rates of reaction", "Periodicity", "Group 2", "Group 17",
    "Nitrogen", "Introduction to organic chemistry", "Hydrocarbons",
    "Halogenoalkanes", "Alcohols, esters and carboxylic acids", "Carbonyl compounds",
    "Lattice energy", "Electrochemistry", "Further aspects of equilibria",
    "Reaction kinetics", "Entropy and Gibbs free energy", "Transition elements",
    "Benzene and its compounds", "Carboxylic acids and their derivatives",
    "Organic nitrogen compounds", "Polymerisation", "Organic synthesis",
    "Analytical chemistry",
]
assert len(CHAPTER_OPENERS) == len(CHAPTER_TITLES) == 30
# TOC order sanity: ch19 title follows P1 in the book, opener 537 > P1_START 522
assert CHAPTER_OPENERS[18] == CH19_START

FRONT_CHAPTER = {
    "chapter_no": None,
    "chapter_title": "Front matter (cover, series, contents, how to use this book, introduction)",
}
BACK_CHAPTERS = [
    {"start": P2_START, "end": APPENDICES_START - 1, "chapter_no": None,
     "chapter_title": "P2 Practical skills 2"},
    {"start": APPENDICES_START, "end": ACKNOWLEDGEMENTS_START - 1, "chapter_no": None,
     "chapter_title": "Appendices (Periodic Table, electrode potentials, qualitative analysis)"},
    {"start": ACKNOWLEDGEMENTS_START, "end": PDF_PAGES_TOTAL, "chapter_no": None,
     "chapter_title": "Acknowledgements and imprint"},
]

BOOK_TITLE = "Cambridge International AS & A Level Chemistry Coursebook (3rd edition)"
AUTHOR = "Lawrie Ryan, Roger Norris"


def chapter_ranges():
    """[(start_pdf, end_pdf, {chapter_no, chapter_title})] incl. P1 slot + front/back."""
    ranges = [(1, FRONT_MATTER_END, dict(FRONT_CHAPTER))]
    for k, (op, title) in enumerate(zip(CHAPTER_OPENERS, CHAPTER_TITLES), start=1):
        end = (CHAPTER_OPENERS[k] - 1) if k < 30 else (P2_START - 1)
        # P1 sits between ch18 and ch19: opener[18] is ch19 (537); ch18 ends at 521
        if k == 18:
            end = P1_START - 1
        ranges.append((op, end, {"chapter_no": k, "chapter_title": title}))
        if k == 18:
            ranges.append((P1_START, CH19_START - 1, {"chapter_no": None,
                          "chapter_title": "P1 Practical skills 1"}))
    for r in BACK_CHAPTERS:
        ranges.append((r["start"], r["end"], {"chapter_no": r["chapter_no"],
                      "chapter_title": r["chapter_title"]}))
    # non-overlap + monotonic sanity
    for a, b in zip(ranges, ranges[1:]):
        assert b[0] == a[1] + 1, f"range gap/overlap at {a[:2]} -> {b[:2]}"
    assert ranges[-1][1] == PDF_PAGES_TOTAL
    return ranges


# --- markers (from marker census) ---
MARKER_TYPES = [
    ("LEARNING INTENTIONS", "learning_objectives"),
    ("BEFORE YOU START", "before_you_start"),
    ("WORKED EXAMPLE", "worked_example"),
    ("ACTIVITY", "activity"),
    ("REFLECTION", "reflection"),
    ("KEY POINTS", "key_points"),
    ("EXAM-STYLE QUESTIONS", "chapter_questions"),
    ("SUMMARY", "summary"),
    ("SELF-EVALUATION", "self_evaluation"),
]
# lowercase substring markers (checked after all-caps)
SOFT_MARKERS = [
    ("Study tip", "tip"),
    ("Tip", "tip"),
    ("Link", "cross_link"),
    ("Extension", "extension_work"),
    ("Science in context", "science_in_context"),
]

SECTION_RE = re.compile(r"^(\d{1,2})\.(\d{1,2})\s+[A-Z].+$")
PSECTION_RE = re.compile(r"^[QP]\d\.\d{1,2}\s+.+$")  # P1.1 / P2.3 headings
WATERMARK_PAT = re.compile(r"CLASS0608|请加微信|全网最全")


def is_watermark_line(line: str) -> bool:
    if WATERMARK_PAT.search(line):
        return True
    cjk = sum(1 for c in line if 0x2E80 <= ord(c) <= 0x9FFF)
    return cjk * 2 > len(line.strip()) if line.strip() else False


if __name__ == "__main__":
    rs = chapter_ranges()
    print(f"{len(rs)} ranges:")
    for s, e, m in rs:
        print(f"  pdf {s:>3}-{e:>3}  ch={m['chapter_no']!s:>4}  {m['chapter_title'][:58]}")
