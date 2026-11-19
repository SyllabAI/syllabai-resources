#!/usr/bin/env python3
"""book_structure_9702.py — CIE 9702 Physics Coursebook 2nd ed structure map.

Derived from probes (wf9_probe_books/probe2/probe3/probe4 + raw-span gutter
probes, evidence cache/w-f9/probe-9702.json + probe2-structure.txt +
probe3-display.txt + col-interleaved census):
- 744-page born-digital PDF (Adobe InDesign CS6 -> 3-Heights). Two-column body
  (main + sidebar QUESTION boxes, sides swap per page); openers/EOC pages
  single-column. Column law: per-page gutter vote (wf9_extract_books v3).
- Printed page numbers exist: book = pdf - 12, verified 4 ways
  (ch1 opener pdf13=book1, ch2 pdf26=book14, ch5 pdf81=book69,
  running-header digit 285 on pdf 297).
- 32 chapters + P1 Practical skills at AS level (pdf 251, between ch16 and
  ch17) + P2 Planning, analysis and evaluation (pdf 541) + Appendices 1-3
  (554/555/557) + Glossary (558) + Index (567) + Acknowledgements (576) +
  exam advice (577-587) + Answers to SAQs (588-645) + Answers to EOC questions
  (646-711) + Recommended resources (712-744).
- Chapter openers = LEARNING OUTCOMES pages (32/32 probed).
"""
import re

PDF_PAGES_TOTAL = 744
OFFSET = 12                     # book_page = pdf_page - 12 (pdf >= 13)
FRONT_MATTER_END = 12
P1_START = 251
P2_START = 541
APPENDIX_1_START = 554
APPENDIX_2_START = 555
APPENDIX_3_START = 557
GLOSSARY_START = 558
INDEX_START = 567
ACKS_START = 576
ADVICE_START = 577
EXAM_INTRO_START = 585
ANSWERS_SAQ_START = 588
ANSWERS_EOC_START = 646
RECOMMENDED_START = 712

CHAPTER_OPENERS = [13, 26, 49, 65, 81, 97, 113, 128, 139, 155, 168, 180, 190,
                   204, 222, 234, 270, 283, 297, 321, 339, 357, 371, 384, 398,
                   418, 434, 447, 463, 478, 501, 518]
CHAPTER_TITLES = [
    "Kinematics – describing motion", "Accelerated motion",
    "Dynamics – explaining motion", "Forces – vectors and moments",
    "Work, energy and power", "Momentum", "Matter and materials",
    "Electric fields", "Electric current, potential difference and resistance",
    "Kirchhoff’s laws", "Resistance and resistivity", "Practical circuits",
    "Waves", "Superposition of waves", "Stationary waves", "Radioactivity",
    "Circular motion", "Gravitational fields", "Oscillations",
    "Communications systems", "Thermal physics", "Ideal gases",
    "Coulomb’s law", "Capacitance", "Electronics",
    "Magnetic fields and electromagnetism", "Charged particles",
    "Electromagnetic induction", "Alternating currents", "Quantum physics",
    "Nuclear physics", "Medical imaging",
]
assert len(CHAPTER_OPENERS) == len(CHAPTER_TITLES) == 32

P1_TITLE = "P1 Practical skills at AS level"
P2_TITLE = "P2 Planning, analysis and evaluation"
APPENDIX_TITLES = ["Appendix 1: Physical quantities and units",
                   "Appendix 2: Data, formulae and relationships",
                   "Appendix 3: The Periodic Table"]

FRONT_CHAPTER = {
    "chapter_no": None,
    "chapter_title": "Front matter (cover, contents, introduction, how to use this book)",
}

BOOK_TITLE = "Cambridge International AS and A Level Physics Coursebook (2nd edition)"
AUTHOR = "David Sang, Graham Jones, Gurinder Chadha, Richard Woodside"
ISBN = "9781107697690 (2nd ed family)"


def chapter_ranges():
    """[(start_pdf, end_pdf, {chapter_no, chapter_title})] — tiling, no gaps."""
    ranges = [(1, FRONT_MATTER_END, dict(FRONT_CHAPTER))]
    for k, (op, title) in enumerate(zip(CHAPTER_OPENERS, CHAPTER_TITLES), start=1):
        end = (CHAPTER_OPENERS[k] - 1) if k < 32 else (P2_START - 1)
        if k == 16:
            end = P1_START - 1
        ranges.append((op, end, {"chapter_no": k, "chapter_title": title}))
        if k == 16:
            ranges.append((P1_START, CHAPTER_OPENERS[16] - 1,
                           {"chapter_no": None, "chapter_title": P1_TITLE}))
    ranges.append((P2_START, APPENDIX_1_START - 1,
                   {"chapter_no": None, "chapter_title": P2_TITLE}))
    ranges.append((APPENDIX_1_START, APPENDIX_2_START - 1,
                   {"chapter_no": None, "chapter_title": APPENDIX_TITLES[0]}))
    ranges.append((APPENDIX_2_START, APPENDIX_3_START - 1,
                   {"chapter_no": None, "chapter_title": APPENDIX_TITLES[1]}))
    ranges.append((APPENDIX_3_START, GLOSSARY_START - 1,
                   {"chapter_no": None, "chapter_title": APPENDIX_TITLES[2]}))
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
                   {"chapter_no": None, "chapter_title": "Answers to EOC questions"}))
    ranges.append((RECOMMENDED_START, PDF_PAGES_TOTAL,
                   {"chapter_no": None, "chapter_title": "Recommended resources"}))
    for a, b in zip(ranges, ranges[1:]):
        assert b[0] == a[1] + 1, f"range gap/overlap at {a[:2]} -> {b[:2]}"
    assert ranges[-1][1] == PDF_PAGES_TOTAL
    return ranges


# marker vocabulary (heading-line forms probed; matched per line, in priority order)
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
    "KEY EQUATIONS": "key_points",
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

HEADER_STRIP_Y = 45             # running headers at y ~23-24
FOOTER_STRIP_Y = 753            # page height 781; stray page digits only


def is_running_header(text, size, y):
    return y < HEADER_STRIP_Y and size < 16


if __name__ == "__main__":
    rs = chapter_ranges()
    print(f"{len(rs)} ranges tile 1..{PDF_PAGES_TOTAL}")
    for s, e, m in rs:
        print(f"  pdf {s:>3}-{e:>3}  ch={m['chapter_no']!s:>4}  {m['chapter_title'][:56]}")
