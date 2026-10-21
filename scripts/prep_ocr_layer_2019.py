#!/usr/bin/env python3
"""Wave 12 prep (F41): build the OCR source layer for 2019-06 1C's rasterized QP pages.

The archive QP PDF has 8 image-only pages (144 dpi scan); pages 1-2 are covers,
pages 4/12/16/18/20/26 carry question content that pdftotext cannot see
(Q7 lost entirely; Q1/Q11/Q12/Q13 heads; Q15 head).

Layer contract (documented in LEDGER F41 + AGENTS.md):
- <page text>   : agent transcription from the 600-dpi render, cross-checked
                  against the tesseract 5.5.0 draft (psm 6) and, where noted,
                  against the MS text layer (independent same-paper source).
                  Deviations from the raw OCR draft are enumerated per page in
                  the corrections ledger below.
- The prepared page texts REPLACE the empty page slots of the staged
  pdftotext -layout extraction (form-feed splice, page order preserved).
- UPLOAD/ocr/2019-06-1C/ocr-pages.json pins sha256 + tool + corrections per
  page; the converter verifies the hashes (fail-closed) and emits receipts.
Deterministic and idempotent: re-running regenerates the staged qp.txt from
the archive PDF and re-splices.
"""
import hashlib, json, os, subprocess
from pathlib import Path

# F15 convention (mirrors the converter): staging derives from EXAMQ_UPLOAD_DIR,
# outputs derive from this checkout; evidence renders are session-local.
U = Path(os.environ.get("EXAMQ_UPLOAD_DIR", "/home/z/my-project/upload"))
QP_PDF = U / "official-4CH1-1C-2019-06-qp.pdf"
QP_TXT = U / "official-2019-06-1C-qp.txt"
OCR_DIR = U / "ocr" / "2019-06-1C"
OCR_DIR.mkdir(parents=True, exist_ok=True)

PAGES = {
    4: """\
Answer ALL questions.
1 Potassium permanganate is a purple solid that is soluble in water.
A crystal of potassium permanganate is placed in a beaker containing water.
potassium permanganate crystal
start
after a short time
purple liquid
(a) After a short time, the crystal becomes smaller and the liquid at the bottom of the
beaker becomes purple.
Which statement explains this observation?
(1)
A the crystal condenses in the water
B the crystal dissolves in the water
C the crystal evaporates in the water
D the crystal melts in the water
(b) The beaker is left until there is no further change in the appearance of the liquid.
(i) Which statement describes the final appearance of the liquid?
(1)
A all of the liquid is purple
B none of the liquid is purple
C only the bottom half of the liquid is purple
D only the top half of the liquid is purple
(ii) Which process causes this change in appearance?
(1)
A condensation
B crystallisation
C diffusion
D evaporation""",
    12: """\
7 Diamond, graphite and silicon dioxide all have giant covalent structures.
The diagram shows the structures of these three substances.
key
silicon
oxygen
diamond
graphite
silicon dioxide
(a) Explain why silicon dioxide has a high melting point.
(2)
(b) Explain why graphite conducts electricity.
(2)
(c) State why diamond is hard but graphite is soft.
(2)
(Total for Question 7 = 6 marks)""",
    16: """\
11 The gas burned in a Bunsen burner is methane.
The equation for the complete combustion of methane is
CH4(g) + 2O2(g) \u2192 CO2(g) + 2H2O(g)
(a) Calculate the mass of oxygen required to react with 32 g of methane.
[Mr of methane = 16]
(2)
mass of oxygen = ......................................................... g
(b) The diagram shows methane burning in air. It also shows how the two gases formed
are collected and tested.
methane burning
U-tube
ice and water
limewater
to pump
(i) Explain why water collects in the U-tube.
(2)
(ii) Describe how anhydrous copper(II) sulfate is used to test for water.
(2)""",
    18: """\
12 A student uses this apparatus to investigate the temperature change that occurs
when ammonium nitrate is dissolved in water.
polystyrene cup
She uses this method.
\u25cf put 100 cm3 of water into the polystyrene cup and measure the initial temperature
of the water
\u25cf add 8.00 g of ammonium nitrate and stir
\u25cf record the lowest temperature reached by the solution
The table shows her results.
Initial temperature of water in \u00b0C   20.0
Lowest temperature of solution in \u00b0C   14.2
(a) Use the results of the experiment to explain what type of reaction is taking place
when ammonium nitrate is added to water.
(2)""",
    20: """\
13 A student uses this apparatus to investigate the rate of reaction between magnesium
and an excess of dilute hydrochloric acid.
gas syringe
magnesium ribbon
dilute hydrochloric acid
She uses this method.
\u25cf use a graduated beaker to pour 50 cm3 of dilute hydrochloric acid of
concentration 2.00 mol/dm3 into the conical flask
\u25cf add a piece of magnesium ribbon of mass 0.086 g to the acid and put the
bung into the neck of the flask
\u25cf measure the total volume of gas collected every ten seconds until the
reaction stops
The table shows the student's results.
Time in s   Volume of hydrogen in cm3
0   0
10   29
20   52
30   67
40   76
50   81
60   84
70   84
80   84""",
    26: """\
15 Hydrated ammonium iron(III) sulfate is a violet solid that has the formula
(NH4)2SO4.Fe2(SO4)3.xH2O
The table shows some tests done on three separate samples of the solid.
Test   Observation
Dissolve the solid in water and add acidified barium chloride solution.
Dissolve the solid in water and add sodium hydroxide solution.
Add sodium hydroxide solution to the solid and warm the mixture.
Test the gas given off with moist universal indicator paper.
(a) Complete the table to show the observation made in each test.
(3)
(b) A student needs to find the value of x in the formula (NH4)2SO4.Fe2(SO4)3.xH2O
He uses this apparatus.
hydrated ammonium iron(III) sulfate
heat
ice
water
The hydrated solid decomposes when heated gently.
The equation for the reaction is
(NH4)2SO4.Fe2(SO4)3.xH2O \u2192 (NH4)2SO4.Fe2(SO4)3   +   xH2O""",
}

# corrections ledger: every span where the prepared text deviates from the raw
# tesseract draft, with the evidence that authorises it.
CORRECTIONS = {
    4: [
        {"find": "———— [] B_ the crystal dissolves", "replace": "B the crystal dissolves",
         "reason": "MCQ option rows normalised to '<L> <text>' (answer-box glyphs are "
                   "print furniture; option text itself matches the draft byte-for-byte)",
         "evidence": "eyeball: ocr-2019-06/pages/p04-04.png"},
        {"find": "(1 A the crystal condenses", "replace": "A the crystal condenses",
         "reason": "same option-row normalisation",
         "evidence": "eyeball: ocr-2019-06/pages/p04-04.png"},
    ],
    12: [
        {"find": "(<) State why", "replace": "(c) State why",
         "reason": "part marker '(c)' misread as '(<)'; bw6 variant reads it correctly",
         "evidence": "eyeball: ocr-2019-06/pages/p12-12.png + hi2/p12-bw6.txt"},
    ],
    16: [
        {"find": "CH,(g) + 20g) > CO,(g) + 2H,O(g)", "replace": "CH4(g) + 2O2(g) \u2192 CO2(g) + 2H2O(g)",
         "reason": "subscript digits below the 144 dpi OCR floor + arrow glyph; "
                   "transcribed from the render",
         "evidence": "eyeball: ocr-2019-06/eq_crop.png (600 dpi); corroborated by the MS "
                     "text layer 'M1 n[CH4] = 32 \u00f7 16' / 'mass of O2 = 128 (g)'"},
        {"find": "[M, of methane = 16]", "replace": "[Mr of methane = 16]",
         "reason": "subscript r in M_r; corpus convention 'Mr' (cf. 15(iii) '[Mr of ... = 532]')",
         "evidence": "eyeball: p16 render; MS text layer uses M_r subscripts as 'Mr'"},
        {"find": "copper(I!)", "replace": "copper(II)",
         "reason": "roman-numeral misread; 400 dpi draft reads copper(II) correctly",
         "evidence": "hi2/p16-bw6.txt line 21"},
    ],
    18: [
        {"find": "Initial temperature of water in \u00b0C   20.0",
         "replace": "Initial temperature of water in \u00b0C   20.0",
         "reason": "table VALUES 20.0/14.2 absent from every OCR variant (dark header "
                   "row inverted); transcribed from the render",
         "evidence": "eyeball: p18 render; corroborated by MS 'M1 14.2 \u2013 20.0 = (-)5.8'"},
        {"find": "100cm'", "replace": "100 cm3",
         "reason": "superscript 3 below OCR floor; corpus convention 'cm3' with space "
                   "(cf. 13(e) '50 cm3')",
         "evidence": "eyeball: p18 render; corpus convention probe"},
    ],
    20: [
        {"find": "50cm\u2019 of dilute hydrochloric acid", "replace": "50 cm3 of dilute hydrochloric acid",
         "reason": "superscript 3; corpus convention",
         "evidence": "eyeball: p20 render; 13(e) prints '50 cm3'"},
        {"find": "2.00 mol/dm\u2019", "replace": "2.00 mol/dm3",
         "reason": "superscript 3; corpus convention",
         "evidence": "eyeball: p20 render"},
        {"find": "(table rows 0/0, 10/29, 20/52, 30/67, 40/76, 50/81, 60/84, 70/84, 80/84)",
         "replace": "transcribed",
         "reason": "results-table grid values dropped by every OCR variant; transcribed "
                   "from the render; cross-checked: MS 13(b)(ii) 'levelling off at 84 cm3' "
                   "and 13(e) repeat-conditions agree with the plateau",
         "evidence": "eyeball: p20 render"},
    ],
    26: [
        {"find": "(NH,),SO,.Fe,(SO,)3.xH,O", "replace": "(NH4)2SO4.Fe2(SO4)3.xH2O",
         "reason": "subscript digits below OCR floor (3 occurrences); corpus convention "
                   "plain digits (cf. existing 15(iii) '[Mr of (NH4)2SO4.Fe2(SO4)3 = 532]')",
         "evidence": "eyeball: p26 render; existing text-page convention for the same formula"},
        {"find": "ironiIll)", "replace": "iron(III)",
         "reason": "roman numeral misread",
         "evidence": "eyeball: p26 render"},
    ],
}


def main():
    # 1. regenerate the pristine pdftotext layer and splice the prepared pages
    raw = subprocess.run(["pdftotext", "-layout", str(QP_PDF), "-"],
                         check=True, capture_output=True, text=True).stdout
    chunks = raw.split("\f")
    assert len(chunks) >= 28, f"expected 28 page chunks, got {len(chunks)}"
    index = []
    for pno, text in sorted(PAGES.items()):
        h = hashlib.sha256(text.encode()).hexdigest()
        (OCR_DIR / f"qp-p{pno:02d}.txt").write_text(text)
        index.append({
            "page": pno, "sha256": h,
            "chars": len(text), "lines": len(text.splitlines()),
            "tool": "tesseract 5.5.0 --psm 6 (600-dpi bw draft) + agent transcription",
            "render": "pdftoppm -r 600 -gray; evidence renders in ocr-2019-06/pages + hi2",
            "corrections": len(CORRECTIONS.get(pno, [])),
        })
    (OCR_DIR / "ocr-pages.json").write_text(json.dumps(
        {"schema": "syllabai.ocr-page-layer/0.1",
         "note": "OCR source layer for image-only QP pages (LEDGER F41). Prepared page "
                 "texts are transcriptions from the 600-dpi render cross-checked against "
                 "the tesseract draft and, where stated, the MS text layer. The converter "
                 "verifies sha256 and emits receipts; pages listed here are excluded from "
                 "the G1 image-only defect attribution.",
         "source_pdf_sha256": hashlib.sha256(QP_PDF.read_bytes()).hexdigest(),
         "pages": index}, indent=1))
    (OCR_DIR / "corrections-ledger.json").write_text(json.dumps(CORRECTIONS, indent=1, ensure_ascii=False))

    for pno, text in sorted(PAGES.items()):
        chunks[pno - 1] = text
    QP_TXT.write_text("\f".join(chunks))

    print(f"staged {QP_TXT.name}: {QP_TXT.stat().st_size}B, "
          f"{len(chunks)} page chunks, pages {sorted(PAGES)} spliced")
    for e in index:
        print(f"  p{e['page']:02d}: {e['lines']:2d} lines  sha={e['sha256'][:10]}  "
              f"corrections={e['corrections']}")


if __name__ == "__main__":
    main()
