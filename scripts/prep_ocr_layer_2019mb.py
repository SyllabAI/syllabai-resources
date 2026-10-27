#!/usr/bin/env python3
"""F41 OCR source layer for the 4MB1 2019-01 image-only pages (T-OEQ-MATHSB-1 run-003).

The archive QP PDFs rasterize exactly 3 pages across the two January 2019 papers:
  2019-01 4MB1/01  page 5  (Q8 inequality + Q9 column vectors, both complete)
  2019-01 4MB1/01  page 16 (Q21 stem + table + histogram + part (a); (b) + footer
                            live on page 17, which HAS a text layer)
  2019-01 4MB1/01R page 11 (Q17 similar jugs, complete)

Layer contract (LEDGER F41 + AGENTS.md, mirrored from prep_ocr_layer_2019.py):
- <page text>   : agent transcription from the 600-dpi render, cross-checked
                  against the tesseract 5.5.0 draft (psm 6) and, where noted,
                  against the MS text layer (independent same-paper source):
                  Q9's MS block prints the vector-sum components (-8, 6) that
                  the transcribed OA/OB/AC produce; Q21's MS block prints the
                  60<=l<80 frequency 50 + bar height 10 small squares; Q17's MS
                  prints 1459.5 and the 10^3:3^3 ratio.
- The prepared page texts REPLACE the empty page slots of the staged
  pdftotext -layout extraction (form-feed splice, page order preserved).
- UPLOAD/ocr/<series>-<paper>/ocr-pages.json pins sha256 + tool per page;
  the converter verifies the hashes (fail-closed) and excludes these pages
  from the G1 image-only defect attribution.
Deterministic and idempotent: re-running regenerates the staged qp.txt from
the archive PDF and re-splices.
"""
import hashlib, json, os, subprocess
from pathlib import Path

U = Path(os.environ.get("EXAMQ_UPLOAD_DIR", "/home/z/my-project/upload"))

JOBS = [
    ("2019-01", "01", 5), ("2019-01", "01", 16), ("2019-01", "01R", 11),
]

PAGES = {
    ("2019-01", "01", 5): """\
8 (a) Solve the inequality 5x + 4 < 20 − 3x
(2)
(b) Represent, on the number line below, your solution of the inequality in part (a).
−5 −4 −3 −2 −1 0 1 2 3 4 5 x
(1)
(Total for Question 8 is 3 marks)
9 The points O, A, B and C are such that OA = ( −2 4 ), OB = ( 5 −3 ) and AC = ( −1 −1 )
Find |BC|
|BC| =
(Total for Question 9 is 3 marks)""",
    ("2019-01", "01", 16): """\
21 The lengths of cod caught by fishermen in a small fishing boat last month were measured.
The incomplete table and histogram below give information about the length of each cod caught
last month.
Length (l cm) Number of cod
5 < l ≤ 25 30
25 < l ≤ 40 75
40 < l ≤ 50 100
50 < l ≤ 60 155
60 < l ≤ 80
80 < l ≤ 100 20
Frequency density
0 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
Length (l cm)
(a) Complete the table and the histogram.
(2)""",
    ("2019-01", "01R", 11): """\
17 Diagram NOT accurately drawn
20 cm
6 cm
A B
The diagram shows two similar jugs.
The height of jug A is 20 cm and the height of jug B is 6 cm.
Given that
volume of jug A − volume of jug B = 1459.5 cm3
calculate the volume, in cm3, of jug B.
cm3
(Total for Question 17 is 4 marks)""",
}

# corrections vs the raw tesseract draft (psm 6), enumerated per the F41 contract
CORRECTIONS = {
    ("2019-01", "01", 5): [
        "vector components re-spaced to the printed column layout '( −2 4 )' (tesseract flattens the tall parens)",
        "vector arrows over OA/OB/AC dropped per the corpus extraction-baseline convention (cf. 2026-06 01R Q25)",
    ],
    ("2019-01", "01", 16): [
        "histogram grid noise dropped; axis scale labels transcribed as the printed row",
        "empty 60 < l ≤ 80 frequency cell kept blank (the question asks the candidate to complete it)",
    ],
    ("2019-01", "01R", 11): [
        "jug line-art dropped; printed labels 20 cm / 6 cm / A / B kept",
        "superscript 'cm³' transcribed as 'cm3' per the text-layer convention of the paper's own pdftotext pages",
    ],
}


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def tesseract_draft(pdf: Path, page: int) -> str:
    png = U / f".t-ocr-p{page}.png"
    subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "300",
                    "-png", "-singlefile", str(pdf), str(png.with_suffix(""))], check=True)
    tr = subprocess.run(["tesseract", str(png), "-", "--psm", "6"],
                        capture_output=True, text=True)
    png.unlink(missing_ok=True)
    return tr.stdout


def main():
    from collections import defaultdict
    by_paper = defaultdict(list)
    for job in JOBS:
        by_paper[job[:2]].append(job)

    for (series, paper), jobs in by_paper.items():
        qp_pdf = U / f"official-4MB1-{paper}-{series}-qp.pdf"
        qp_txt = U / f"official-{series}-{paper}-qp.txt"
        ocr_dir = U / "ocr" / f"{series}-{paper}"
        ocr_dir.mkdir(parents=True, exist_ok=True)

        # 1. regenerate the pristine pdftotext layer
        subprocess.run(["pdftotext", "-layout", str(qp_pdf), str(qp_txt)], check=True)

        # 2. tesseract drafts (recorded for the corrections ledger)
        drafts = {p: tesseract_draft(qp_pdf, p) for _, _, p in jobs}

        # 3. splice the prepared pages into the form-feed slots
        chunks = qp_txt.read_text().split("\f")
        manifest = {"source_pdf_sha256": sha256(qp_pdf),
                    "tool": "agent-vision@600dpi+tesseract5.5.0-psm6+MS-crosscheck",
                    "note": ("transcriptions verified against the MS text layer: Q9 vector-sum "
                             "components (-8, 6) and |BC|=10; Q21 60-80 class frequency 50, bar "
                             "height 10 small squares; Q17 1459.5 cm3 and the 10^3:3^3 ratio"),
                    "pages": []}
        for _, _, pno in jobs:
            text = PAGES[(series, paper, pno)]
            (ocr_dir / f"qp-p{pno:02d}.txt").write_text(text)
            assert chunks[pno - 1].strip() == "", f"page {pno} slot not empty"
            chunks[pno - 1] = text
            manifest["pages"].append({"page": pno, "sha256": hashlib.sha256(text.encode()).hexdigest(),
                                      "tesseract_draft_chars": len(drafts[pno])})
        qp_txt.write_text("\f".join(chunks))
        (ocr_dir / "ocr-pages.json").write_text(json.dumps(manifest, indent=1))
        (ocr_dir / "corrections-ledger.json").write_text(json.dumps(
            {f"{s}-{pp} p{p}": CORRECTIONS[(s, pp, p)] for (s, pp, p) in jobs}, indent=1))
        print(f"{series} {paper}: spliced pages {[p for _, _, p in jobs]} "
              f"-> {qp_txt} ({len(chunks)} page chunks)")


if __name__ == "__main__":
    main()
