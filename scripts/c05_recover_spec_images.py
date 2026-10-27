#!/usr/bin/env python3
"""T-C05: recover the 5 expiring OCR-service images from the 4CH1 spec markdown.

The ocr.z.ai output embeds images on signed UCloud URLs that expire
(Expires=1789643336 -> 2026-09-17). Download them into local assets/ and
rewrite the markdown to reference the local files. Additive only: no content
changes. Also prepends CMC v1.0 front matter (status: raw_ocr).
"""
import re
import urllib.request
import ssl
import sys

REPO = "/home/z/my-project/work/syllabai-resources"
MD = REPO + "/international-gcse-chemistry-2017-specification-2026-09-10_12-18-50.md"

# figure id -> (descriptive filename, alt text) ; located by their line context
FIGURES = {
    1:    ("fig-cover.png", "Front cover of the Pearson Edexcel International GCSE in Chemistry (4CH1) specification, Issue 3"),
    176:  ("fig-qualification-structure.png", "Diagram of the qualification structure: relationship of Papers 1C/2C to the International GCSE in Chemistry award and the Science (Single/Double Award) pathway"),
    788:  ("fig-wcqc-framework.png", "Pearson World Class Qualification design principles framework diagram"),
    872:  ("fig-transferable-skills.png", "Transferable skills framework diagram (cognitive, intrapersonal, interpersonal skills)"),
    1160: ("fig-back-cover.png", "Back cover artwork of the specification document"),
}

FRONT_MATTER = """---
source_type: specification
board: Pearson Edexcel
qualification: International GCSE (9-1)
subject: Chemistry
subject_code: 4CH1
doc_title: "International GCSE in Chemistry (4CH1) specification"
issue: 3
first_teaching: 2017-09
first_examination: 2019-06
source_file: international-gcse-chemistry-2017-specification.pdf
source_pages: 1-53
ocr:
  tool: ocr.z.ai
  date: 2026-09-10
  operator: human
status: raw_ocr
notes: >
  Single-file full-document OCR of the Issue 3 specification. Spec-point tables
  captured as raw HTML tables; chemistry notation partially degraded (see
  CORPUS_REVIEW_2026-09-10.md). Not yet reviewed or validated; do not ingest
  as-is. Images recovered from expiring signed URLs to local assets/.
---
"""

def main():
    with open(MD, encoding="utf-8") as f:
        lines = f.read().split("\n")

    changed = 0
    downloaded = 0
    for lineno, (fname, alt) in FIGURES.items():
        idx = lineno - 1
        line = lines[idx]
        m = re.search(r"<img src='([^']+)'", line)
        if not m:
            print(f"SKIP line {lineno}: no img tag found")
            continue
        url = m.group(1)
        dest = f"{REPO}/assets/{fname}"
        try:
            ctx = ssl.create_default_context()
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60, context=ctx) as r, open(dest, "wb") as out:
                out.write(r.read())
            downloaded += 1
            print(f"OK   {fname} ({lineno})")
        except Exception as e:
            print(f"FAIL {fname} (line {lineno}): {e}")
            continue
        new_img = f"<img src='assets/{fname}' alt='{alt}'/>"
        lines[idx] = re.sub(r"<img src='[^']+'[^>]*/>", new_img, line, count=1)
        changed += 1

    text = "\n".join(lines)
    if not text.startswith("---"):
        text = FRONT_MATTER + text
        print("front matter prepended")

    with open(MD, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"downloaded={downloaded} refs_rewritten={changed}")

if __name__ == "__main__":
    sys.exit(main())
