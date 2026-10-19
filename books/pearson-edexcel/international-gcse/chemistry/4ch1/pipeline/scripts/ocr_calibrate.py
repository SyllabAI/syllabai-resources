#!/usr/bin/env python3
"""Calibrate OCR: try a few pages at different render scales, report time + word confidence."""
import time, re, json
import pypdfium2 as pdfium
import pytesseract
from PIL import Image

PDF = "/home/z/my-project/data/chemistry_book.pdf"

# representative pages: front matter, body text, dense body, exam-style page
TEST_PAGES = [21, 51, 101, 201]   # 0-based
SCALES = [3.0, 4.0]

def word_conf_ratio(text: str):
    """Fraction of tokens that look like real words (letters, common chem tokens)."""
    tokens = re.findall(r"[A-Za-z][A-Za-z\-']*", text)
    if not tokens:
        return 0.0, 0
    good = [t for t in tokens if len(t) >= 2]
    return (len(good) / len(tokens), len(tokens))

pdf = pdfium.PdfDocument(PDF)
results = []
for scale in SCALES:
    for p in TEST_PAGES:
        t0 = time.time()
        bitmap = pdf[p].render(scale=scale)
        img = bitmap.to_pil().convert("L")
        render_s = time.time() - t0
        t1 = time.time()
        txt = pytesseract.image_to_string(img, lang="eng", config="--oem 1 --psm 3")
        ocr_s = time.time() - t1
        ratio, ntok = word_conf_ratio(txt)
        results.append({
            "page": p + 1, "scale": scale,
            "px": list(img.size),
            "render_s": round(render_s, 2), "ocr_s": round(ocr_s, 2),
            "chars": len(txt), "tokens": ntok, "word_ratio": round(ratio, 3),
        })
        print(json.dumps(results[-1]), flush=True)

best = [r for r in results if r["scale"] == 4.0]
print("\nAVG ocr_s @4.0:", round(sum(r["ocr_s"] for r in best) / len(best), 2))
print("AVG word_ratio @4.0:", round(sum(r["word_ratio"] for r in best) / len(best), 3))
