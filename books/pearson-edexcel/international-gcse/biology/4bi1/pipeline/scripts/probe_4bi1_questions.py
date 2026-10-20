#!/usr/bin/env python3
"""Focused probe: question-page census + exact y-geometry of feature headers
vs running headers (band-strip safety for the serving-critical question
typing). No band exclusion in this scan."""
import fitz, re, json, collections

PDF = "/home/z/my-project/data/biology/student-book.pdf"
doc = fitz.open(PDF)
mid = doc[0].rect.width / 2
H = doc[0].rect.height

strict_ch = re.compile(r"CHAPTER\s+QUESTIONS")
strict_un = re.compile(r"UNIT\s+QUESTIONS")
total_marks = re.compile(r"Total\s*\d+\s*marks?")
marks_paren = re.compile(r"\((\d)\)")

rows = []
q_header_y = []
run_header_y = []
for p in range(len(doc)):
    d = doc[p].get_text("dict")
    halves = {"L": [], "R": []}
    for b in d["blocks"]:
        if b.get("type") != 0:
            continue
        x0, y0, x1, y1 = b["bbox"]
        side = "L" if (x0 + x1) / 2 < mid else "R"
        lines = []
        for ln in b.get("lines", []):
            t = "".join(s["text"] for s in ln.get("spans", []))
            lines.append((ln["bbox"][1], t))
            if "QUESTIONS" in t.upper() and len(t.strip()) < 40:
                q_header_y.append((p + 1, side, round(y0), t.strip()[:40]))
            if re.match(r"^\d{1,3}\s+[A-Z]{4,}", t.strip()) and y0 < 40:
                run_header_y.append((p + 1, side, round(y0), t.strip()[:40]))
        halves[side].append((y0, y1, "\n".join(t for _, t in lines)))
    for side in ("L", "R"):
        txt = "\n".join(t for _, _, t in halves[side])
        rows.append({
            "spread": p + 1, "side": side,
            "chapter_q": bool(strict_ch.search(txt)),
            "unit_q": bool(strict_un.search(txt)),
            "n_total_marks": len(total_marks.findall(txt)),
            "n_mark_parens": len(marks_paren.findall(txt)),
        })

# classify candidate question pages: >=2 "Total marks" OR (questions marker + >=1 marks)
qp = [r for r in rows if r["n_total_marks"] >= 2 or
      ((r["chapter_q"] or r["unit_q"]) and r["n_total_marks"] >= 1)]
print(f"candidate question half-pages: {len(qp)}")
for r in qp:
    flag = "CH" if r["chapter_q"] else ("UN" if r["unit_q"] else "??")
    print(f"  s{r['spread']:>3}{r['side']}  {flag}  total_marks={r['n_total_marks']}  parens={r['n_mark_parens']}")

print(f"\nquestion-feature header y values (n={len(q_header_y)}): "
      f"min={min((y for _,_,y,_ in q_header_y), default=None)} "
      f"max={max((y for _,_,y,_ in q_header_y), default=None)}")
for r in q_header_y[:12]:
    print("   ", r)
print(f"\nrunning-header y values (n={len(run_header_y)}): "
      f"min={min((y for _,_,y,_ in run_header_y), default=None)} "
      f"max={max((y for _,_,y,_ in run_header_y), default=None)}")

json.dump({"rows": rows, "q_header_y": q_header_y, "run_header_y": run_header_y},
          open("/home/z/my-project/data/biology/probe_out/question_census.json", "w"), indent=1)
