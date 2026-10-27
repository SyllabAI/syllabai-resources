#!/usr/bin/env python3
"""Task 22 prep (F101): build the OCR source layer for 2019-06 4PH1-1P's image-only QP.

The archive QP PDF (Pearson DAM 4PH1_1P_que_20190523.pdf, 'Microsoft: Print To PDF')
carries NO text layer at all (staged pdftotext output is 32 bytes of form feeds; the
only embedded 'font' is the barcode strip) — every page is a raster scan (144 dpi
class, 32 pages: cover p1, formulae p2, blank p3/p13/p16/p24/p32, questions p4-p31).
The converter fails closed on the empty footer census (Task 15 CRASH-RECEIPT); this
layer is the F41 recovery path, physics twin of chemistry's 2019-06 1C wave.

Layer contract (LEDGER F41 + F101 + AGENTS.md):
- qp-pNN.txt   : agent transcription from the 600-dpi render, cross-checked against
                 the tesseract 5.5.0 draft (psm 6) and, where noted, against the MS
                 text layer (independent same-paper source). Deviations from the raw
                 draft are enumerated per page in the corrections ledger.
- The prepared page texts REPLACE the empty page slots of the staged pdftotext
  -layout extraction (form-feed splice, page order preserved). Pages NOT listed
  here (cover, formulae, blanks) stay empty — print furniture, no question content.
- ocr-pages.json pins sha256 + tool + corrections per page; the converter verifies
  every sha and the source-PDF sha before use (mismatch aborts), splices the
  prepared text into page_norm so figure mentions anchor with page attribution,
  excludes recovered pages from the G1 image-only defect attribution, and emits
  ocr_pages receipts.
Deterministic and idempotent: re-running regenerates the staged qp.txt from the
archive PDF and re-splices.
"""
import hashlib, json, os, subprocess
from pathlib import Path

U = Path(os.environ.get("EXAMQ_UPLOAD_DIR", "/home/z/my-project/upload"))
QP_PDF = U / "official-4PH1-1P-2019-06-qp.pdf"
QP_TXT = U / "official-2019-06-1P-qp.txt"
OCR_DIR = U / "ocr" / "2019-06-1P"
OCR_DIR.mkdir(parents=True, exist_ok=True)

PAGES = {}

PAGES[4] = """\
Answer ALL questions.
1 This question is about waves.
(a) (i) Which of these waves is longitudinal?
(1)
A infrared
B radio
C sound
D ultraviolet
(ii) Draw a straight line linking each electromagnetic wave to its correct hazard.
(2)
Electromagnetic wave Hazard
microwave
infrared
skin burns
blindness
internal heating of body tissue
cell mutation
(b) (i) Which of these is a use for x-rays?
(1)
A checking for broken bones
B cooking food
C detecting forged banknotes
D smoke detectors"""

PAGES[5] = """\
(ii) Which of these is a use for infrared waves?
(1)
A checking for broken bones
B cooking food
C detecting forged banknotes
D sterilising medical instruments
(Total for Question 1 = 5 marks)"""

PAGES[6] = """\
2 This question is about magnetic fields.
(a) Describe an experiment to investigate the magnetic field pattern around a
permanent bar magnet.
You may draw a diagram to help your answer.
(3)"""

PAGES[7] = """\
(b) The diagram shows two bar magnets.
Complete the diagram to show the magnetic field pattern.
(3)
N S
S N
(Total for Question 2 = 6 marks)"""

PAGES[8] = """\
3 This question is about food preservation.
(a) The diagram shows how gamma radiation is used to irradiate fruit stored in a
wooden box.
The radiation kills bacteria on the fruit.
gamma source
wooden box containing fruit
Explain why gamma radiation is used instead of alpha radiation to kill bacteria.
(2)"""

PAGES[9] = """\
(b) The wooden box has this label.
these fruits
have been
irradiated
Explain why fruit irradiated with gamma radiation is safe to eat.
(2)
(Total for Question 3 = 4 marks)"""

PAGES[10] = """\
4 A car driver sees a hazard on the road ahead.
The graph shows the velocity of the car from when the driver sees the hazard.
Velocity in m/s
15
10
5
1.0 2.0 3.0 4.0
Time in seconds
(a) (i) Use the graph to determine the reaction time of the driver.
(1)
reaction time = .......................................................... s
(ii) Calculate the stopping distance of the car.
(4)
stopping distance = .......................................................... m
(iii) Calculate the acceleration of the car when the car is braking.
(3)
acceleration = .......................................................... m/s2"""

PAGES[11] = """\
(b) The speed of the car affects the thinking distance and the braking distance.
Discuss other factors that affect the thinking distance and the braking distance of
the car.
(4)
(Total for Question 4 = 12 marks)"""

PAGES[12] = """\
5 This question is about stretching a spring.
(a) The graph shows how the extension of a spring varies when a force is applied to the spring.
The line on the graph shows that the spring has been extended past its elastic limit.
The line has a straight section and a curved section.
Extension
0
Force
(i) Draw a cross on the line to show the elastic limit of the spring.
(1)
(ii) Sketch another line to show how the extension will change when the force is
decreased from its maximum value back to 0.
(2)
(b) (i) State which energy store of the spring increases when it is stretched.
Assume the spring does not reach its elastic limit.
(1)
(ii) How is this energy transferred to the spring?
(1)
A electrically
B by heating
C mechanically
D by radiation
(Total for Question 5 = 5 marks)"""

PAGES[14] = """\
6 (a) (i) A student investigates how current varies with voltage for a metal filament lamp.
Draw a diagram of the circuit that a student could use for this investigation.
(4)
(ii) Describe a method the student could use for their investigation.
(4)"""

PAGES[15] = """\
(b) The student extends the investigation by recording additional data for the lamp.
This is her method.
For each voltage
\u25cf switch the current on for 45 seconds
\u25cf record the current and colour of the lamp
\u25cf calculate the power and the energy transferred by the lamp
The table shows the student\u2019s results.
Voltage in V Current Power in W Energy in J Colour of lamp
0.0 0.00 0.0 0.0 off
2.0 0.40 0.8 36 red
4.0 0.90 3.6 orange
6.0 1.60 9.6 430 yellow
8.0 2.80 22.4 1000 white
(i) State the unit for current.
(1)
(ii) Calculate the missing value of energy for the voltage of 4.0 V.
Give your answer to 2 significant figures.
(2)
energy = .......................................................... J
(iii) The colour of a star is related to its surface temperature.
The Sun is yellow.
Use the student\u2019s results to identify a colour for a star that is cooler than the Sun.
(1)
(Total for Question 6 = 12 marks)"""

PAGES[17] = """\
7 This question is about refraction.
(a) State what is meant by the term refraction.
(1)
(b) The diagram shows a ray of light from a torch incident on the surface of a pool of water.
normal
45\u00b0
air
water
The angle of refraction of the ray of light is 33\u00b0
(i) Draw the path of the ray of light in the water.
(2)
(ii) State the formula linking refractive index, angle of incidence and angle of refraction.
(1)
(iii) Show that the refractive index of water is about 1.3
(2)"""

PAGES[18] = """\
(c) The torch is moved below the surface of the water. Light from the torch is
incident on the water surface at an angle greater than the critical angle.
(i) Explain the meaning of the term critical angle.
You may draw a diagram to help your answer.
(2)
(ii) State the formula linking critical angle and refractive index.
(1)
(iii) Calculate the critical angle of water.
Assume the refractive index of water is 1.3
(3)
critical angle = .......................................................... \u00b0"""

PAGES[19] = """\
(iv) A ray of light leaves the torch as shown in the diagram.
Complete the path of the ray of light.
(2)
air
water
55\u00b0
torch
(Total for Question 7 = 14 marks)"""

PAGES[20] = """\
8 Schiaparelli is a spacecraft that was sent to Mars in 2016.
(a) Schiaparelli slowed down as it fell vertically through the atmosphere of Mars.
(i) Draw labelled arrows on the diagram to show the forces acting on Schiaparelli
as it fell.
(3)
spacecraft
(ii) Schiaparelli then opened a parachute to slow down.
Explain how the spacecraft reached a low terminal velocity after opening its parachute.
Use ideas about forces in your answer.
(4)"""

PAGES[21] = """\
(b) The parachute was disconnected when Schiaparelli was at a height of 2.0 m from
the surface of Mars and travelling at a speed of 0.45 m/s.
Calculate the speed of the spacecraft just before it hits the surface of Mars.
[acceleration of free-fall on Mars = 3.4 m/s2]
(4)
speed = .......................................................... m/s
(c) Suggest why Mars has a lower gravitational field strength than Earth.
(1)
(Total for Question 8 = 12 marks)"""

PAGES[22] = """\
9 (a) The diagram shows a nuclear reactor.
control rod
moderator
fuel rod
shielding
reactor vessel
coolant out
coolant in
Each part of the nuclear reactor has a function and is made of a suitable material
for its function.
Complete the table by giving the missing information.
(5)
Part Function Suitable material
control rod boron
moderator graphite
shielding prevents irradiation of workers
fuel rod"""

PAGES[23] = """\
(b) Heavy water is a compound of oxygen and an isotope of hydrogen called deuterium.
Deuterium is formed by the fusion of protons.
(i) State the meaning of the term isotope.
(2)
(ii) Explain the difference between nuclear fission and nuclear fusion.
(2)
(iii) State a location where nuclear fusion takes place.
(1)
(iv) Explain why fusion cannot take place at low temperature or low pressure.
(2)
(Total for Question 9 = 12 marks)"""

PAGES[25] = """\
10 This question is about voltage and current.
(a) The diagram shows two resistors connected to a battery.
9.2V
12 mA
240\u03a9
R
Calculate the voltage across resistor R.
(4)
voltage = .......................................................... V"""

PAGES[26] = """\
(b) The diagram shows the parts of an ammeter.
The pointer is connected to the coil so they can move together.
scale
pointer
return spring
permanent magnet
B
C
N
S
A
D
coil
+
\u2212
(i) Explain what happens when there is a current in the coil.
(3)
(ii) Draw an arrow on the diagram to show the force acting on side CD of the coil
when there is a current in the coil.
(1)"""

PAGES[27] = """\
(iii) Explain how the ammeter could be changed so that it could measure smaller currents.
(3)
(Total for Question 10 = 11 marks)"""

PAGES[28] = """\
11 The diagram shows a manometer, a device used for measuring differences in pressure.
trapped gas
liquid
difference in the levels of the liquid
(a) One side of the manometer has some trapped gas. The other side is left open to
the atmosphere.
The difference in pressure can be calculated using this formula.
[difference in pressure = height \u00d7 density \u00d7 10]
The density of the liquid is 1.3 \u00d7 104 kg/m3.
The difference in the levels of the liquid is 3.8 cm.
Calculate the difference in pressure between the atmosphere and the trapped gas.
(3)
difference in pressure = .......................................................... Pa"""

PAGES[29] = """\
(b) The temperature and pressure of the trapped gas increase when it is warmed.
(i) Explain, in terms of particles, why the pressure of the trapped gas increases.
(3)
(ii) The pressure of the trapped gas in the manometer is 9.95 \u00d7 104 Pa and the
temperature is 16 \u00b0C.
Calculate the new pressure of the trapped gas if the temperature increases to 32 \u00b0C.
[assume volume of the trapped gas remains constant]
(4)
new pressure = .......................................................... Pa
(Total for Question 11 = 10 marks)"""

PAGES[30] = """\
12 (a) The diagram shows a ball of dough, of mass 580 g, held at a height of 92 cm above
the floor.
dough
92 cm
Calculate the increase in gravitational potential energy (GPE) stored in the ball of
dough when it is above the floor.
(3)
GPE = .......................................................... J"""

PAGES[31] = """\
(b) The ball of dough hits the floor and does not rebound.
Describe the energy transfers taking place from when the dough is dropped to
after it has hit the floor.
You should refer to energy stores as well as transfers between energy stores at
these stages.
\u25cf before the dough is dropped
\u25cf just before the dough hits the floor
\u25cf after the dough has hit the floor
(4)
(Total for Question 12 = 7 marks)
TOTAL FOR PAPER = 110 MARKS"""

# corrections ledger: every deviation class where the prepared text deviates from
# the raw tesseract draft, with the evidence that authorises it.
CORRECTIONS = {
    4: [
        {"find": "option rows arrive as '<box-glyph> A infrared' / '= [|] C\u20ac\u00a2 sound'",
         "replace": "A infrared / C sound",
         "reason": "MCQ answer-box glyphs and misread letters normalised to '<L> <text>' "
                   "(answer boxes are print furniture; option text matches the render)",
         "evidence": "eyeball: ocrwave/pages600/p-04.png; MS (a)(i) rebuttals name "
                     "A/B/D as transverse waves, key C (sound waves)"},
        {"find": "right-margin column noise ('Lox ax Oo aS SPs ...') + 'DO NOT WRITE IN THIS AREA'",
         "replace": "dropped",
         "reason": "margin/border print furniture, never question content",
         "evidence": "eyeball: p-04 render margins"},
        {"find": "matching boxes land as interleaved fragments",
         "replace": "'Electromagnetic wave Hazard' + microwave/infrared + skin burns/"
                    "blindness/internal heating of body tissue/cell mutation as printed",
         "reason": "linking-question boxes transcribed in column order; box positions "
                   "are spatial furniture",
         "evidence": "eyeball: p-04 render; MS (a)(ii) 'one mark for each correct line'"},
    ],
    5: [
        {"find": "(b)(ii) option row D draft-garbled",
         "replace": "D sterilising medical instruments",
         "reason": "option text from the render",
         "evidence": "eyeball: pages200/p-05.png; MS (b)(ii) 'D is incorrect because gamma "
                     "has this use' (gamma sterilises)"},
    ],
    6: [
        {"find": "dotted answer-line runs dominate the draft (page reduced to noise)",
         "replace": "dropped (bare dotted rules are furniture)",
         "reason": "the (3)-mark part carries named answer space only",
         "evidence": "eyeball: pages200/p-06.png"},
    ],
    7: [
        {"find": "magnet pole labels draft-lost",
         "replace": "N S / S N",
         "reason": "box labels transcribed in printed order (left box N-S, right box S-N)",
         "evidence": "eyeball: pages200/p-07.png"},
    ],
    8: [
        {"find": "figure labels absent from draft",
         "replace": "gamma source / wooden box containing fruit",
         "reason": "diagram label text is printed content; pdftotext would carry it",
         "evidence": "eyeball: pages200/p-08.png"},
    ],
    9: [
        {"find": "label box text draft-lost",
         "replace": "these fruits / have been / irradiated",
         "reason": "printed label text, three lines as printed",
         "evidence": "eyeball: pages200/p-09.png"},
    ],
    10: [
        {"find": "graph axis labels/values draft-mangled",
         "replace": "Velocity in m/s / 15 / 10 / 5 / 1.0 2.0 3.0 4.0 / Time in seconds",
         "reason": "axis furniture transcribed compactly from the render",
         "evidence": "eyeball: pages200/p-10.png; MS (a)(i) '1.0 (s)' + (a)(ii) 4-mark "
                     "stopping-distance rows corroborate the 15 m/s plateau and 4.0 s stop"},
        {"find": "answer-unit lines draft-lost",
         "replace": "reaction time = ... s / stopping distance = ... m / acceleration = ... m/s2",
         "reason": "named answer lines carry the printed unit; superscript 2 flattened "
                   "to m/s2 (corpus convention)",
         "evidence": "eyeball: p-10 render"},
    ],
    12: [
        {"find": "option rows arrive as '<box-glyph> A electrically' etc.",
         "replace": "A electrically / B by heating / C mechanically / D by radiation",
         "reason": "MCQ box glyphs normalised; option text matches the render "
                   "(MS (b)(ii) keys C mechanically)",
         "evidence": "eyeball: pages200/p-12.png"},
    ],
    15: [
        {"find": "bullet glyphs draft-mangled",
         "replace": "\u25cf switch the current on for 45 seconds / \u25cf record the current "
                    "and colour of the lamp / \u25cf calculate the power and the energy "
                    "transferred by the lamp",
         "reason": "bullet rows transcribed from the render",
         "evidence": "eyeball: pages200/p-15.png"},
        {"find": "results-table grid dropped by draft",
         "replace": "header + rows 0.0/0.00/0.0/0.0/off, 2.0/0.40/0.8/36/red, "
                    "4.0/0.90/3.6/(blank)/orange, 6.0/1.60/9.6/430/yellow, 8.0/2.80/22.4/1000/white",
         "reason": "table values transcribed from the render (the 4.0 V energy cell is "
                   "the printed blank the question asks to calculate)",
         "evidence": "eyeball: p-15 render; MS (b)(ii) '36 \u00d7 2' + 'P = IV' rows "
                     "corroborate the 36/0.8/2.0 and 430/9.6/6.0 pairings"},
    ],
    17: [
        {"find": "figure labels draft-lost",
         "replace": "normal / 45\u00b0 / air / water",
         "reason": "diagram labels + angle text as printed",
         "evidence": "eyeball: pages200/p-17.png; MS (b) rows name 45\u00b0 incidence"},
    ],
    18: [
        {"find": "answer-unit line draft-lost",
         "replace": "critical angle = ... \u00b0",
         "reason": "named answer line with the printed degree unit",
         "evidence": "eyeball: pages200/p-18.png; MS (c)(iii) '(c =) 50 (\u00b0)'"},
    ],
    19: [
        {"find": "figure labels draft-lost",
         "replace": "air / water / 55\u00b0 / torch",
         "reason": "diagram labels + angle text as printed",
         "evidence": "eyeball: pages200/p-19.png; MS (c)(iv) '55\u00b0 > c' row"},
    ],
    20: [
        {"find": "figure label draft-lost",
         "replace": "spacecraft",
         "reason": "diagram label as printed",
         "evidence": "eyeball: pages200/p-20.png"},
    ],
    21: [
        {"find": "[acceleration of free-fall on Mars = 3.4 m/s?] superscript draft-lost",
         "replace": "[acceleration of free-fall on Mars = 3.4 m/s2]",
         "reason": "superscript 2 flattened to m/s2 (corpus convention)",
         "evidence": "eyeball: pages200/p-21.png; MS (b) 'v2 = u2 + 2as' row with 3.4"},
    ],
    22: [
        {"find": "reactor figure labels draft-lost",
         "replace": "control rod / moderator / fuel rod / shielding / reactor vessel / "
                    "coolant out / coolant in",
         "reason": "diagram label text as printed",
         "evidence": "eyeball: pages200/p-22.png"},
        {"find": "table grid dropped by draft",
         "replace": "Part/Function/Suitable material header + control rod/boron, "
                    "moderator/graphite, shielding/prevents irradiation of workers, fuel rod",
         "reason": "table values transcribed from the render (blank cells are the "
                   "missing information the question asks for)",
         "evidence": "eyeball: p-22 render; MS 9(a) '1 mark for each correct answer in "
                     "the table' rows corroborate"},
    ],
    25: [
        {"find": "circuit labels draft-lost",
         "replace": "9.2V / 12 mA / 240\u03a9 / R",
         "reason": "circuit value labels as printed",
         "evidence": "eyeball: pages200/p-25.png; MS (a) 'use of V = IR' rows with "
                     "0.012 A corroborate 12 mA/240\u03a9/9.2V"},
    ],
    26: [
        {"find": "ammeter figure labels draft-lost/mangled",
         "replace": "scale / pointer / return spring / permanent magnet / B / C / N / S / "
                    "A / D / coil / + / \u2212",
         "reason": "diagram label text as printed (A-D coil corners, N-S poles, "
                   "terminals + and \u2212)",
         "evidence": "eyeball: pages200/p-26.png"},
    ],
    28: [
        {"find": "'1.3 \u00d7 10? kg/m?' draft garbled; '\u00d7' dropped",
         "replace": "1.3 \u00d7 104 kg/m3  /  [difference in pressure = height \u00d7 density \u00d7 10]",
         "reason": "superscript 4 flattened (104), \u00d7 transcribed as printed; MS text "
                   "layer prints '0.038  1.3  104  10' (same flattening, \u00d7 lost there)",
         "evidence": "eyeball: pages200/p-28.png; ms.txt line 648"},
        {"find": "figure labels draft-lost",
         "replace": "trapped gas / liquid / difference in the levels of the liquid",
         "reason": "diagram label text as printed",
         "evidence": "eyeball: p-28 render"},
    ],
    29: [
        {"find": "'9.95 \u00d7 10? Pa' draft garbled",
         "replace": "9.95 \u00d7 104 Pa",
         "reason": "superscript flattening; MS line 678 prints '9.95  104 / 289 = p2'",
         "evidence": "eyeball: pages200/p-29.png; ms.txt line 678"},
    ],
    30: [
        {"find": "figure labels draft-lost",
         "replace": "dough / 92 cm",
         "reason": "diagram labels as printed; MS 12(a) 'substitution into GPE = mass g height'",
         "evidence": "eyeball: pages200/p-30.png"},
    ],
    31: [
        {"find": "bullet glyphs draft-mangled; TOTAL FOR PAPER row draft-lost",
         "replace": "\u25cf rows as printed + 'TOTAL FOR PAPER = 110 MARKS'",
         "reason": "bullet rows and the paper-total banner transcribed from the render",
         "evidence": "eyeball: pages200/p-31.png"},
    ],
}


def main():
    raw = subprocess.run(["pdftotext", "-layout", str(QP_PDF), "-"],
                         check=True, capture_output=True, text=True).stdout
    chunks = raw.split("\f")
    if len(chunks) == 33 and chunks[-1].strip() == "":
        chunks = chunks[:-1]          # trailing form feed
    assert len(chunks) == 32, f"expected 32 page chunks, got {len(chunks)}"
    assert all(len(c.strip()) == 0 for c in chunks), \
        "archive QP is supposed to be image-only — an unexpected text layer appeared"
    index = []
    for pno, text in sorted(PAGES.items()):
        h = hashlib.sha256(text.encode()).hexdigest()
        (OCR_DIR / f"qp-p{pno:02d}.txt").write_text(text)
        index.append({
            "page": pno, "sha256": h,
            "chars": len(text), "lines": len(text.splitlines()),
            "tool": "tesseract 5.5.0 --psm 6 (600-dpi gray draft) + agent transcription",
            "render": "pdftoppm -r 600 -gray (evidence: physics-intake/ocrwave/pages600/) "
                      "+ 200-dpi reading set (pages200/)",
            "corrections": len(CORRECTIONS.get(pno, [])),
        })
    (OCR_DIR / "ocr-pages.json").write_text(json.dumps(
        {"schema": "syllabai.ocr-page-layer/0.1",
         "note": "OCR source layer for the image-only 2019-06 4PH1-1P QP scan (LEDGER "
                 "F101; physics twin of the F41 chemistry wave). Prepared page texts are "
                 "transcriptions from the 600-dpi render cross-checked against the "
                 "tesseract 5.5.0 draft and, where stated, the MS text layer. The "
                 "converter verifies sha256 and emits receipts; pages listed here are "
                 "excluded from the G1 image-only defect attribution. Cover (p1), "
                 "formulae (p2) and the printed BLANK pages (p3/p13/p16/p24/p32) stay "
                 "empty — print furniture, no question content.",
         "paper_identity": "P58372A (cover + per-page barcode strips); 'Total mark for "
                            "this paper is 110' on the cover; printed footers sum "
                            "5+6+4+12+5+12+14+12+12+11+10+7 = 110",
         "source_pdf_sha256": hashlib.sha256(QP_PDF.read_bytes()).hexdigest(),
         "pages": index}, indent=1))
    (OCR_DIR / "corrections-ledger.json").write_text(
        json.dumps(CORRECTIONS, indent=1, ensure_ascii=False))

    for pno, text in sorted(PAGES.items()):
        chunks[pno - 1] = text
    QP_TXT.write_text("\f".join(chunks))

    print(f"staged {QP_TXT.name}: {QP_TXT.stat().st_size}B, "
          f"{len(chunks)} page chunks, {len(PAGES)} pages spliced")
    for e in index:
        print(f"  p{e['page']:02d}: {e['lines']:3d} lines  sha={e['sha256'][:10]}  "
              f"corrections={e['corrections']}")


if __name__ == "__main__":
    main()
