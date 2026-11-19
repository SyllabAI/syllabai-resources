#!/usr/bin/env python3
"""book_structure_9700.py — CIE 9700 Biology Coursebook 4th ed structure map.

Derived from probes (evidence cache/w-f9/probe-9700.json + probe2-structure.txt
+ probe3-display.txt):
- 696-page born-digital PDF (Adobe InDesign CC -> 3-Heights). Two-column body
  (equal columns, gutter ~19pt); openers/EOC pages single-column. Column law:
  per-page gutter vote (wf9_extract_books v3).
- Printed page numbers: book = pdf - 10, verified 4 ways (ch1 pdf11=book1,
  ch2 pdf37=book27, ch5 pdf103=book93 (TOC), running-header digit 490 on
  pdf 500).
- 19 chapters + P1 Practical skills for AS (pdf 256, between ch11 and ch12) +
  P2 Planning, analysis and evaluation (pdf 500) + Appendices 1-2 (522/523) +
  Glossary (524) + Index (536) + Acknowledgements (544) + exam advice
  (547-566) + Answers to SAQs (567-609) + Answers to EOCQs (610-673) +
  Recommended resources (674-696).
- Chapter openers = LEARNING OUTCOMES pages (19/19 probed). Note: the 4th ed
  numbers the practical-skills chapters in running headers as "Chapter P1/P2".
"""
import re

PDF_PAGES_TOTAL = 696
OFFSET = 10                     # book_page = pdf_page - 10 (pdf >= 11)
FRONT_MATTER_END = 10
P1_START = 256
P2_START = 500
APPENDIX_1_START = 522
APPENDIX_2_START = 523
GLOSSARY_START = 524
INDEX_START = 536
ACKS_START = 544
ADVICE_START = 547
EXAM_INTRO_START = 562
ANSWERS_SAQ_START = 567
ANSWERS_EOC_START = 610
RECOMMENDED_START = 674

CHAPTER_OPENERS = [11, 37, 63, 82, 103, 120, 136, 167, 195, 208, 232, 277,
                   296, 309, 339, 374, 407, 433, 472]
CHAPTER_TITLES = [
    "Cell structure", "Biological molecules", "Enzymes",
    "Cell membranes and transport", "The mitotic cell cycle",
    "Nucleic acids and protein synthesis", "Transport in plants",
    "Transport in mammals", "Gas exchange and smoking", "Infectious diseases",
    "Immunity", "Energy and respiration", "Photosynthesis", "Homeostasis",
    "Coordination", "Inherited change", "Selection and evolution",
    "Biodiversity, classification and conservation", "Genetic technology",
]
assert len(CHAPTER_OPENERS) == len(CHAPTER_TITLES) == 19

P1_TITLE = "P1 Practical skills for AS"
P2_TITLE = "P2 Planning, analysis and evaluation"
APPENDIX_TITLES = ["Appendix 1: Amino acid R groups",
                   "Appendix 2: DNA and RNA triplet codes"]

FRONT_CHAPTER = {
    "chapter_no": None,
    "chapter_title": "Front matter (cover, contents, how to use this book, introduction)",
}

BOOK_TITLE = "Cambridge International AS and A Level Biology Coursebook (4th edition)"
AUTHOR = "Mary Jones, Richard Fosbery, Jennifer Gregory, Dennis Taylor"
ISBN = "9781107636828 (4th ed family)"


def chapter_ranges():
    ranges = [(1, FRONT_MATTER_END, dict(FRONT_CHAPTER))]
    for k, (op, title) in enumerate(zip(CHAPTER_OPENERS, CHAPTER_TITLES), start=1):
        end = (CHAPTER_OPENERS[k] - 1) if k < 19 else (P2_START - 1)
        if k == 11:
            end = P1_START - 1
        ranges.append((op, end, {"chapter_no": k, "chapter_title": title}))
        if k == 11:
            ranges.append((P1_START, CHAPTER_OPENERS[11] - 1,
                           {"chapter_no": None, "chapter_title": P1_TITLE}))
    ranges.append((P2_START, APPENDIX_1_START - 1,
                   {"chapter_no": None, "chapter_title": P2_TITLE}))
    ranges.append((APPENDIX_1_START, APPENDIX_2_START - 1,
                   {"chapter_no": None, "chapter_title": APPENDIX_TITLES[0]}))
    ranges.append((APPENDIX_2_START, GLOSSARY_START - 1,
                   {"chapter_no": None, "chapter_title": APPENDIX_TITLES[1]}))
    ranges.append((GLOSSARY_START, INDEX_START - 1,
                   {"chapter_no": None, "chapter_title": "Glossary"}))
    ranges.append((INDEX_START, ACKS_START - 1,
                   {"chapter_no": None, "chapter_title": "Index"}))
    ranges.append((ACKS_START, ADVICE_START - 1,
                   {"chapter_no": None, "chapter_title": "Acknowledgements"}))
    ranges.append((ADVICE_START, EXAM_INTRO_START - 1,
                   {"chapter_no": None,
                    "chapter_title": "Advice on how to revise for and approach examinations"}))
    ranges.append((EXAM_INTRO_START, ANSWERS_SAQ_START - 1,
                   {"chapter_no": None,
                    "chapter_title": "Introduction to the examination and changes to the syllabus"}))
    ranges.append((ANSWERS_SAQ_START, ANSWERS_EOC_START - 1,
                   {"chapter_no": None, "chapter_title": "Answers to SAQs"}))
    ranges.append((ANSWERS_EOC_START, RECOMMENDED_START - 1,
                   {"chapter_no": None, "chapter_title": "Answers to EOCQs"}))
    ranges.append((RECOMMENDED_START, PDF_PAGES_TOTAL,
                   {"chapter_no": None, "chapter_title": "Recommended resources"}))
    for a, b in zip(ranges, ranges[1:]):
        assert b[0] == a[1] + 1, f"range gap/overlap at {a[:2]} -> {b[:2]}"
    assert ranges[-1][1] == PDF_PAGES_TOTAL
    return ranges


ALLCAPS_MARKERS = {
    "LEARNING OUTCOMES": "learning_outcomes",
    "BEFORE YOU START": "before_you_start",
    "WORKED EXAMPLE": "worked_example",
    "WORKED EXAMPLES": "worked_example",
    "ACTIVITY": "activity",
    "ACTIVITIES": "activity",
    "REFLECTION": "reflection",
    "KEY POINTS": "key_points",
    "KEY POINT": "key_points",
    "END-OF-CHAPTER QUESTIONS": "chapter_questions",
    "SUMMARY": "summary",
    "CHAPTER SUMMARY": "summary",
    "SELF-EVALUATION CHECKLIST": "self_evaluation",
    "SCIENCE IN CONTEXT": "science_in_context",
    "EXTENSION": "extension_work",
    "LINK": "cross_link",
    "QUESTION": "questions",
    "QUESTIONS": "questions",
}
SOFT_MARKERS = [
    ("End-of-chapter questions", "chapter_questions"),
    ("Worked example", "worked_example"),
    ("Self-assessment questions", "questions"),
    ("Study tip", "tip"),
    ("Science in context", "science_in_context"),
    ("Practical skills", "practical"),
]

HEADER_STRIP_Y = 45
FOOTER_STRIP_Y = 753


def is_running_header(text, size, y):
    return y < HEADER_STRIP_Y and size < 16


if __name__ == "__main__":
    rs = chapter_ranges()
    print(f"{len(rs)} ranges tile 1..{PDF_PAGES_TOTAL}")
    for s, e, m in rs:
        print(f"  pdf {s:>3}-{e:>3}  ch={m['chapter_no']!s:>4}  {m['chapter_title'][:56]}")
