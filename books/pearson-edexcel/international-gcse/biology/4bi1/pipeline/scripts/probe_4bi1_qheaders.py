#!/usr/bin/env python3
"""Dump header-zone (30<=y<80) lines + marks density for every half-page that
shows any question signal, to find how chapter question sections are labelled
across all 22 chapters (strict header found on only 6)."""
import fitz, re, json

PDF = "/home/z/my-project/data/biology/student-book.pdf"
doc = fitz.open(PDF)
mid = doc[0].rect.width / 2
total_marks = re.compile(r"Total\s*\d+\s*marks?")
any_q = re.compile(r"Q\s*U\s*E\s*S\s*T\s*I\s*O\s*N", re.I)

out = []
for p in range(len(doc)):
    d = doc[p].get_text("dict")
    halves = {"L": [], "R": []}
    hdr = {"L": [], "R": []}
    for b in d["blocks"]:
        if b.get("type") != 0:
            continue
        x0, y0, x1, y1 = b["bbox"]
        side = "L" if (x0 + x1) / 2 < mid else "R"
        for ln in b.get("lines", []):
            t = "".join(s["text"] for s in ln.get("spans", [])).strip()
            if not t:
                continue
            y = ln["bbox"][1]
            halves[side].append(t)
            if 30 <= y < 80 and len(t) < 50:
                hdr[side].append((round(y), t))
    for side in ("L", "R"):
        txt = "\n".join(halves[side])
        nm = len(total_marks.findall(txt))
        if nm >= 1 or any(hdr[side]):
            out.append({"spread": p + 1, "side": side, "total_marks": nm,
                        "hdr_zone": hdr[side]})

for r in out:
    print(f"s{r['spread']:>3}{r['side']} marks={r['total_marks']}  hdr={r['hdr_zone'][:3]}")
json.dump(out, open("/home/z/my-project/data/biology/probe_out/question_headers.json", "w"), indent=1)
print(f"\n{len(out)} half-pages with question signals")
