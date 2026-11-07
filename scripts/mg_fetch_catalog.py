#!/usr/bin/env python3
"""Parse old.mathsgenie.co.uk/gcse.html into the MG GCSE Edexcel catalog JSON (v2).

Table columns: # | Videos | Exam Questions (-ws.pdf) | Exam Questions Booklet (.pdf) | Solutions ({slug}ans.pdf)
Grade sections: "Grade 1" .. "Grade 7", "Grade 8/9" (band, codes 8.N).
Empty rows (e.g. 5.13 Midpoint) = question resources not published.
"""
import json, re
from bs4 import BeautifulSoup

SRC = "https://old.mathsgenie.co.uk/gcse.html"
SITE_LANE = "https://mathsgenie.co.uk/gcse/maths/edexcel"
html = open("/home/z/my-project/mg_work/old_gcse.html", encoding="utf-8", errors="replace").read()
soup = BeautifulSoup(html, "html.parser")


def slugify(name):
    s = name.strip().lower().replace("&", "and")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


catalog, cur_band = [], None
for el in soup.find_all(["h2", "table"]):
    if el.name == "h2":
        t = el.get_text()
        m = re.search(r"[Gg]rade\s*(\d+)\s*/\s*(\d+)", t)
        if m:
            cur_band = f"{m.group(1)}-{m.group(2)}"
        else:
            m = re.search(r"[Gg]rade\s*(\d+)", t)
            cur_band = m.group(1) if m else None
        continue
    if el.name == "table" and cur_band:
        for tr in el.find_all("tr"):
            tds = tr.find_all("td")
            if len(tds) < 3:
                continue
            code = tds[0].get_text(strip=True)
            if not re.match(r"^\d+\.\d+$", code):
                continue
            g, n = (int(x) for x in code.split("."))
            a = tds[1].find("a")
            row = {
                "grade_band": cur_band,
                "grade": g,
                "ordinal": n,
                "code": code,
                "name": a.get_text(strip=True) if a else None,
                "video_page": a.get("href", "") if a else None,
                "source_page": SRC,
                "site_slug": f"grade-{cur_band}-{g}-{n}-{slugify(a.get_text(strip=True)) if a else 'unknown'}",
            }
            def link(td):
                x = td.find("a") if td else None
                return x.get("href", "") if x else None
            row["questions_ws_url"] = link(tds[2]) if len(tds) > 2 else None
            row["booklet_url"] = link(tds[3]) if len(tds) > 3 else None
            row["solutions_url"] = link(tds[4]) if len(tds) > 4 else None
            row["exam_questions_published"] = bool(row["questions_ws_url"] or row["booklet_url"])
            catalog.append(row)

out = {
    "source_page": SRC,
    "site_lane": SITE_LANE,
    "scraped_at": "2026-11-07",
    "board": "Edexcel",
    "qualification": "GCSE",
    "subject": "Maths",
    "topic_count": len(catalog),
    "grade_bands": sorted({t["grade_band"] for t in catalog}, key=lambda b: (int(b.split("-")[0]), b)),
    "topics": catalog,
}
with open("/home/z/my-project/mg_work/catalog/gcse_edexcel_catalog.json", "w") as f:
    json.dump(out, f, indent=1)

print(f"topics: {len(catalog)}; bands: {out['grade_bands']}")
n_ws = sum(1 for t in catalog if t["questions_ws_url"])
n_book = sum(1 for t in catalog if t["booklet_url"])
n_sol = sum(1 for t in catalog if t["solutions_url"])
n_none = sum(1 for t in catalog if not t["exam_questions_published"])
print(f"ws: {n_ws}  booklet: {n_book}  solutions: {n_sol}  no-question-resources: {n_none}")
print("no-question-resources:", [t["code"] for t in catalog if not t["exam_questions_published"]])
ws_only = [t["code"] for t in catalog if t["questions_ws_url"] and not t["booklet_url"]]
book_only = [t["code"] for t in catalog if t["booklet_url"] and not t["questions_ws_url"]]
print("ws-only:", ws_only, " booklet-only:", book_only)

# join check against new-site slugs
new_slugs = set(l.strip() for l in open("/home/z/my-project/mg_work/new_site_slugs.txt"))
hits = sum(1 for t in catalog if t["site_slug"] in new_slugs)
miss = [t["site_slug"] for t in catalog if t["site_slug"] not in new_slugs]
print(f"site_slug join: {hits}/{len(catalog)}; misses: {miss}")
