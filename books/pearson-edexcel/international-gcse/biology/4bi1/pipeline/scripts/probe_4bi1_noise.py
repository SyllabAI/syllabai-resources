#!/usr/bin/env python3
"""Phase-2 noise & question census for the 4BI1 text layer.

Known noise classes from probe_4bi1_structure.py:
  A. broken-CMap display/italic font garbles ("hvmg"=living, "1s"=is,
     "chapler"=chapter, "KEV POINT"=KEY POINT, "ANO"=AND, "FOOO"=FOOD)
  B. intra-word extra spaces from Word conversion ("Th is", "t he", "l ooks")
  C. icon/skill-tag glyph junk ("mD", "ll!!lll'll'f.!I", "Ell>")
  D. decorative rules as dash runs

This script quantifies each class per italic-flagged vs regular spans and
runs a TOLERANT question-page scan (intra-word splits/garbles defeat the
strict "CHAPTER QUESTIONS" regex used in the first probe).
"""
import fitz, re, json, collections

PDF = "/home/z/my-project/data/biology/student-book.pdf"
OUT = "/home/z/my-project/data/biology/probe_out/noise_census.json"
doc = fitz.open(PDF)
mid = doc[0].rect.width / 2

GARBLE_SIGS = {
    "1s(is)": re.compile(r"\b1s\b"),
    "1n(in)": re.compile(r"\b1n\b"),
    "m(in)":  re.compile(r"(?<![A-Za-z])m(?![A-Za-z])"),
    "th e(the)": re.compile(r"\bth e\b"),
    "t he(the)": re.compile(r"\bt he\b"),
    "chapler(chapter)": re.compile(r"chapler|chapte r", re.I),
    "ANO(AND)": re.compile(r"\bANO\b"),
    "KEV(KEY)": re.compile(r"KEV\b"),
    "hvmg(living)": re.compile(r"hvmg|l1vmg"),
}
INTRA_SPLIT = re.compile(r"(?<=\b[A-Za-z]) (?=[a-z]{1,2}\b)")  # "Th is", "t he"
ICON_JUNK = re.compile(r"\b(mD|Ell>|\)\s*D)\b")
DASH_RUN = re.compile(r"^[-_=~.\u2014\u2013]{6,}$")

italic_chars = regular_chars = 0
italic_garbles = regular_garbles = 0
intra_splits = 0
icon_junk_hits = 0
dash_blocks = 0
garbled_halves = set()
tol_q = {
    "chapter_questions": re.compile(r"C\s*H\s*A\s*P\s*T\s*E\s*R\s+Q\s*U\s*E\s*S\s*T\s*I\s*O\s*N\s*S"),
    "unit_questions": re.compile(r"U\s*N\s*I\s*T\s+Q\s*U\s*E\s*S\s*T\s*I\s*O\s*N\s*S"),
    "total_marks": re.compile(r"Total\s*\d+\s*marks?"),
}
tol_hits = collections.defaultdict(list)

for p in range(len(doc)):
    d = doc[p].get_text("dict")
    halves = {"L": [], "R": []}
    for b in d["blocks"]:
        if b.get("type") != 0:
            continue
        x0, y0, x1, y1 = b["bbox"]
        side = "L" if (x0 + x1) / 2 < mid else "R"
        # header/footer band lines are stripped downstream; census them separately
        in_band = y0 < 42 or y0 > doc[p].rect.height - 45
        for ln in b.get("lines", []):
            line_txt = ""
            ln_italic = False
            for sp in ln.get("spans", []):
                t = sp["text"]
                line_txt += t
                italic = bool(sp["flags"] & 2)
                n = len(t)
                if italic:
                    italic_chars += n
                else:
                    regular_chars += n
                g = sum(len(rx.findall(t)) for rx in GARBLE_SIGS.values())
                if italic:
                    italic_garbles += g
                else:
                    regular_garbles += g
                if g:
                    garbled_halves.add((p + 1, side))
                if italic:
                    ln_italic = True
            if in_band:
                continue
            intra_splits += len(INTRA_SPLIT.findall(line_txt))
            icon_junk_hits += len(ICON_JUNK.findall(line_txt))
            if DASH_RUN.match(line_txt.strip()):
                dash_blocks += 1
            halves[side].append(line_txt)
    for side in ("L", "R"):
        txt = "\n".join(halves[side])
        for key, rx in tol_q.items():
            if rx.search(txt):
                tol_hits[key].append((p + 1, side))

res = {
    "char_census": {
        "italic_chars": italic_chars, "regular_chars": regular_chars,
        "italic_garble_sigs": italic_garbles, "regular_garble_sigs": regular_garbles,
        "italic_garble_per_1k": round(italic_garbles * 1000 / max(1, italic_chars), 2),
        "regular_garble_per_1k": round(regular_garbles * 1000 / max(1, regular_chars), 2),
        "halves_with_garble": len(garbled_halves),
        "halves_total": len(doc) * 2,
    },
    "intra_word_split_hits": intra_splits,
    "icon_junk_hits": icon_junk_hits,
    "dash_rule_blocks": dash_blocks,
    "tolerant_question_hits": {k: v for k, v in tol_hits.items()},
}
json.dump(res, open(OUT, "w"), indent=1)
print(json.dumps(res, indent=1)[:3000])
