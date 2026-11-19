#!/usr/bin/env python3
"""book_structure_0625.py — Hodder Cambridge IGCSE Physics 3rd ed (Duncan &
Kennett) structure map.

Derived from probes (evidence cache/w-f9/probe-0625.json + probe2-structure.txt
+ probe3-display.txt + raw-span gutter probes):
- 328-page PDFium-re-rendered PDF. Layout: irregular two-band grid — text
  right band (x ~314-570), figures/margin boxes left; openers carry the
  2-column "at a glance" bullet box (bullet glyph renders as 'l'). Column law:
  FIXED gutter x=307, both-bands>=6-spans sanity, crossing spans stay left.
- Printed page numbers: book = pdf - 13, verified 5 ways (Section 1 divider
  pdf14=book1, ch1 opener pdf15=book2 (TOC), ch2 pdf22=book9 (TOC), Answers
  pdf312=book299 (TOC), Index pdf321=book308 (TOC)).
- 5 section dividers (pdf 14/84/118/158/242) + 50 chapters (openers =
  26pt title + 35pt chapter number) + back matter: Revision questions bank
  (258), Cambridge IGCSE exam questions bank (264), Mathematics for physics
  (292), Further experimental investigations (296), Practical test questions
  (298), Alternative to practical test questions (304), Answers (312),
  Index (321), Photo acknowledgements (328).
- Damage class of record (D-2): fi/fl ligature loss in the render
  ('Specifi c', 'classifi cation', ' elds') — census in the parse report;
  deterministic repair NOT applied to body text (v1), polish pending.
"""
import re

PDF_PAGES_TOTAL = 328
OFFSET = 13                     # book_page = pdf_page - 13 (pdf >= 14)
FRONT_MATTER_END = 13
FIXED_GUTTER = 307

SECTION_DIVIDERS = [
    (14, 1, "General physics"),
    (84, 2, "Thermal physics"),
    (118, 3, "Properties of waves"),
    (158, 4, "Electricity and magnetism"),
    (242, 5, "Atomic physics"),
]

CHAPTER_OPENERS = [15, 22, 26, 30, 34, 37, 40, 43, 48, 52, 56, 60, 63, 69, 73,
                   79, 85, 89, 94, 98, 101, 104, 110, 115, 119, 126, 129, 132,
                   135, 139, 142, 148, 153, 159, 163, 170, 175, 180, 187, 190,
                   198, 206, 212, 217, 222, 228, 232, 235, 243, 251]
CHAPTER_TITLES = [
    "Measurements", "Speed, velocity and acceleration", "Graphs of equations",
    "Falling bodies", "Density", "Weight and stretching", "Adding forces",
    "Force and acceleration", "Circular motion", "Moments and levers",
    "Centres of mass", "Momentum", "Energy transfer",
    "Kinetic and potential energy", "Energy sources",
    "Pressure and liquid pressure", "Molecules", "The gas laws",
    "Expansion of solids, liquids and gases", "Thermometers",
    "Specific heat capacity", "Specific latent heat",
    "Conduction and convection", "Radiation", "Mechanical waves",
    "Light rays", "Reflection of light", "Plane mirrors", "Refraction of light",
    "Total internal reflection", "Lenses", "Electromagnetic radiation",
    "Sound waves", "Magnetic fields", "Static electricity", "Electric current",
    "Potential difference", "Resistance", "Capacitors", "Electric power",
    "Electronic systems", "Digital electronics", "Generators", "Transformers",
    "Electromagnets", "Electric motors", "Electric meters", "Electrons",
    "Radioactivity", "Atomic structure",
]
assert len(CHAPTER_OPENERS) == len(CHAPTER_TITLES) == 50

BACK_STARTS = [
    (258, "revision_bank", "Revision questions"),
    (264, "exam_bank", "Cambridge IGCSE exam questions"),
    (292, "mathematics", "Mathematics for physics"),
    (296, "investigations", "Further experimental investigations"),
    (298, "practical_test_bank", "Practical test questions"),
    (304, "alt_practical_bank", "Alternative to practical test questions"),
    (312, "answers", "Answers"),
    (321, "index", "Index"),
    (328, "photo_acknowledgements", "Photo acknowledgements"),
]

FRONT_CHAPTER = {
    "chapter_no": None,
    "chapter_title": "Front matter (cover, contents, preface, physics and technology, scientific enquiry)",
}

BOOK_TITLE = "Cambridge IGCSE Physics (3rd edition, Hodder)"
AUTHOR = "Tom Duncan, Heather Kennett"
ISBN = "9781444176421 (Hodder 3rd ed)"


def unit_for_page(p):
    cur_no, cur_name = None, None
    for s, no, name in SECTION_DIVIDERS:
        if p >= s:
            cur_no, cur_name = no, name
    return cur_no, cur_name


def chapter_ranges():
    ranges = [(1, FRONT_MATTER_END, dict(FRONT_CHAPTER))]
    # build: divider pages as 1-page ranges, chapters fill the gaps
    events = sorted(
        [(op, "ch", i + 1, t) for i, (op, t) in
         enumerate(zip(CHAPTER_OPENERS, CHAPTER_TITLES))] +
        [(s, "div", no, name) for s, no, name in SECTION_DIVIDERS] +
        [(st, "back", None, title) for st, _k, title in BACK_STARTS],
        key=lambda ev: ev[0])
    for i, (s, kind, no, title) in enumerate(events):
        e = (events[i + 1][0] - 1) if i + 1 < len(events) else PDF_PAGES_TOTAL
        if kind == "ch":
            meta = {"chapter_no": no, "chapter_title": title}
            uno, uname = unit_for_page(s)
            meta["unit_no"], meta["unit_name"] = uno, uname
        else:
            meta = {"chapter_no": None, "chapter_title": title}
        ranges.append((s, e, meta))
    for a, b in zip(ranges, ranges[1:]):
        assert b[0] == a[1] + 1, f"range gap/overlap at {a[:2]} -> {b[:2]}"
    assert ranges[-1][1] == PDF_PAGES_TOTAL
    return ranges


# content-type for each back-matter range key
BACK_TYPES = {
    "revision_bank": "revision_bank",
    "exam_bank": "exam_bank",
    "mathematics": "mathematics",
    "investigations": "investigations",
    "practical_test_bank": "practical_test_bank",
    "alt_practical_bank": "alt_practical_bank",
    "answers": "answers",
    "index": "index",
    "photo_acknowledgements": "acknowledgements",
}

# marker vocabulary (line forms probed)
ALLCAPS_MARKERS = {
    "WORKED EXAMPLE": "worked_example",
    "WORKED EXAMPLES": "worked_example",
    "REVISION QUESTIONS": "revision_questions",
    "CHECKLIST": "checklist",
    "PRACTICAL": "practical",
    "ACTIVITY": "activity",
}
SOFT_MARKERS = [
    ("Worked example", "worked_example"),
    ("Revision questions", "revision_questions"),
    ("Checklist", "checklist"),
    ("Practical work:", "practical"),
    ("Practical", "practical"),
]

# 0625 display headings: '●● ' bullet lines (>=18pt) are the sub-section law
BULLET_HEAD = re.compile(r"^●●\s*")
OPENER_BULLET = re.compile(r"^(?:●(?!●)|l)[\s\t]+")  # box bullets: single U+25CF or symbol-font l
HEADER_STRIP_Y = 62                          # running headers at y ~53.8 (small caps)
FOOTER_STRIP_Y = 770                         # page height 798


def is_running_header(text, size, y):
    return y < HEADER_STRIP_Y and size < 16


if __name__ == "__main__":
    rs = chapter_ranges()
    print(f"{len(rs)} ranges tile 1..{PDF_PAGES_TOTAL}")
    for s, e, m in rs:
        print(f"  pdf {s:>3}-{e:>3} ch={m['chapter_no']!s:>4} u={m.get('unit_no')!s:>4} {m['chapter_title'][:52]}")
