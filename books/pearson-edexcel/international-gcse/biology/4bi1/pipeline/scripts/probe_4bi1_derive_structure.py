#!/usr/bin/env python3
"""Derive the 4BI1 structure map (question banks, dividers, answers) from the
extracted half-pages, cross-checked against course-structure arithmetic.

Outputs a proposed EXTRA_SECTIONS + per-chapter question ranges for review
before baking into book_structure_biology.py.
"""
import json, re, glob, collections

PAGES = "/home/z/my-project/data/biology/text_pages"

UNIT_NAMES = {
    1: "Organisms and Life Processes", 2: "Animal Physiology",
    3: "Plant Physiology", 4: "Ecology and the Environment",
    5: "Variation and Selection", 6: "Microorganisms and Genetic Modification",
}
# book page of unit start (= first chapter opener) and chapter starts
CHAPTERS = [
    (1, 1, "Life processes", 3), (2, 1, "The variety of living organisms", 25),
    (3, 2, "Breathing and gas exchange", 39), (4, 2, "Food and digestion", 52),
    (5, 2, "Blood and circulation", 70), (6, 2, "Coordination", 84),
    (7, 2, "Chemical coordination", 98), (8, 2, "Homeostasis and excretion", 104),
    (9, 2, "Reproduction in humans", 118),
    (10, 3, "Plants and food", 135), (11, 3, "Transport in plants", 152),
    (12, 3, "Chemical coordination in plants", 168), (13, 3, "Reproduction in plants", 174),
    (14, 4, "Ecosystems", 187), (15, 4, "Human influences on the environment", 204),
    (16, 5, "Chromosomes, genes and DNA", 227), (17, 5, "Cell division", 240),
    (18, 5, "Genes and inheritance", 249), (19, 5, "Natural selection and evolution", 261),
    (20, 5, "Selective breeding", 268),
    (21, 6, "Using microorganisms", 281), (22, 6, "Genetic modification", 289),
]
UNIT_START = {u: min(b for _, uu, _, b in CHAPTERS if uu == u) for u in UNIT_NAMES}
UNIT_START[1] = 2  # unit 1 divider at book 2 (ch1 opener 3)

CH_RX = re.compile(r"C\s*H\s*A\s*P\s*T\s*E\s*R\s+Q\s*U\s*E\s*S\s*T\s*I\s*O\s*N\s*S", re.I)
UN_RX = re.compile(r"U\s*N\s*I\s*T\s+Q\s*U\s*E\s*S\s*T\s*I\s*O\s*N\s*S", re.I)
TOTAL = re.compile(r"Total\s*(\d+)\s*marks?", re.I)
SKILL = re.compile(r"CRITICAL\s*THINKING|ANALYSIS|REASONING|INTERPRETATION|"
                   r"DECISION\s*MAKING|EXECUTIVE|PROBLEM\s*SOLVING|MATHEMATICS|"
                   r"PRAC\w*ICAL\s*SKILLS?", re.I)
UNANS = re.compile(r"UNIT\s*\d*\s*ANSWERS", re.I)
CHANS = re.compile(r"CHAPTER\s*\d+", re.I)
LO_RX = re.compile(r"OBJECTIVES\b")

halves = []  # (spread, side, book_page, feats)
for fp in sorted(glob.glob(f"{PAGES}/page_*.json")):
    d = json.load(open(fp))
    p = d["pdf_page"]
    for side in ("L", "R"):
        body = d["body_lines"][side]
        band = d["header_lines"][side]
        txt_body = "\n".join(r[3] for r in body)
        txt_band = "\n".join(r[3] for r in band)
        halves.append({
            "sp": p, "side": side, "bp": d["book_pages"][side],
            "ch_q_body": bool(CH_RX.search(txt_body)),
            "ch_q_band": bool(CH_RX.search(txt_band)),
            "un_q_body": bool(UN_RX.search(txt_body)),
            "un_q_band": bool(UN_RX.search(txt_band)),
            "n_total": sum(int(m) for m in TOTAL.findall(txt_body)),
            "skill": len(SKILL.findall(txt_body)),
            "unit_answers": bool(UNANS.search(txt_body)),
            "chapter_answers": bool(CHANS.search(txt_body)) and d["book_pages"][side] >= 320,
            "lo": bool(LO_RX.search(txt_body)),
            "n_lines": len(body),
            "first": body[0][3][:60] if body else "",
        })

def bp_key(h):
    return (h["sp"], h["side"])

print("=== UNIT QUESTION bank candidates (header or high marks) ===")
for h in halves:
    if h["un_q_body"] or h["un_q_band"] or h["n_total"] >= 4:
        tag = "HDR" if (h["un_q_body"] or h["un_q_band"]) else "   "
        print(f"  {tag} book {h['bp']:>3} (s{h['sp']}{h['side']}) total={h['n_total']:>3} skill={h['skill']:>2}  {h['first'][:48]!r}")

print("\n=== CHAPTER QUESTION candidates (strict/tolerant header) ===")
for h in halves:
    if h["ch_q_body"] or h["ch_q_band"]:
        where = "body" if h["ch_q_body"] else "band"
        print(f"  book {h['bp']:>3} (s{h['sp']}{h['side']}) {where} total={h['n_total']:>3} skill={h['skill']:>2}  {h['first'][:48]!r}")

print("\n=== marks-bearing half-pages by book-page (question-density timeline) ===")
cur_ch = None
for h in halves:
    bp = h["bp"]
    ch_here = [c for c in CHAPTERS if c[3] == bp]
    u_here = [u for u, b in UNIT_START.items() if b == bp and u > 1]
    marks = h["n_total"] + h["skill"]
    label = ""
    if ch_here:
        label = f"<<< ch{ch_here[0][0]} opener"
    if u_here:
        label += " <<< unit divider/start"
    if marks or label or h["unit_answers"]:
        print(f"  book {bp:>3} s{h['sp']}{h['side']}  marks={h['n_total']:>3} skill={h['skill']:>2} "
              f"{'UNANS' if h['unit_answers'] else '     '} {label} {h['first'][:40]!r}")

print("\n=== answers section headers ===")
for h in halves:
    if h["unit_answers"]:
        print(f"  book {h['bp']:>3} (s{h['sp']}{h['side']})  {h['first'][:50]!r}")
