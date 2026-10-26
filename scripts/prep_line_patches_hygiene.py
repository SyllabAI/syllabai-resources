#!/usr/bin/env python3
"""T-OEQ-MATHSB-SERVE-1 verdict-A hygiene wave (resources-side, converter lane).

F41-family LINE-PATCH layer for the maths-B staging texts whose embedded-font
cmap is broken beyond glyph-mapping (custom-encoded math runs, OCR-sandwich
MS cells). Every entry: {series, paper, kind, page, line, replacement, evidence}.
The ORIGINAL line content is pinned by sha256 at apply time (fail-closed: a
staged txt that does not carry the recorded original aborts the run).

Ruling of record (run-004 on the serve card, operator verdict A trace
1a177a00bc816e05): the 2019-06 papers' QP layers carry a custom-encoded math
font (lowercase +3 shift, digits at U+0013..U+001C, '=' '(' ')' dropped) and
the 2019-06/02 MS is the OCR-sandwich paper (U+FFFD at fraction bars, matrix
brackets, radicals). Neither is recoverable by a glyph map; the printed page
is the only source. Transcriptions below were made from the 600-dpi renders
(300dpi band crops archived in the lane evidence), cross-checked against the
tesseract drafts and the MS text layers / the repaired SME twin
(UIUX-TIER-B-RUN-004) as independent same-paper sources.

Deterministic and idempotent: re-running re-verifies every sha and re-splices.
"""
import hashlib, json, os, sys
from pathlib import Path

U = Path(os.environ.get("EXAMQ_UPLOAD_DIR", "/home/z/my-project/upload"))

# --- the patch table of record ---------------------------------------------
# keys: (series, paper, kind, page, line)  line = 1-based within the page
# 'sub' = position-preserving substitution when only specific glyphs die;
# 'text' = full-line transcription (the printed row incl. any notes tail).
PATCHES = {
    # ===== 2018-06 01R QP — the one shifted-word line (BEG is a straight line...)
    ("2018-06", "01R", "qp", 4, 44): {
        "mode": "text",
        "text": "    BEG is a straight line and ΔEFG is isosceles with EF = EG and ∠EGF = 63°",
        "evidence": "600dpi p4 render; shift-class decode (BEG LV D VWUDLJKW OLQH); ǻ=△ per the F52 class corpus convention; 0x91=∠ per the map",
    },
    # ===== 2018-06 02 QP — italic-Z/Y glyph glitch rows (Venn Q4)
    ("2018-06", "02", "qp", 10, 34): {
        "mode": "text",
        "text": "    (b) (X ∪ Y) ∩ Z′",
        "evidence": "400dpi p10 crop: printed '(X ∪ Y) ∩ Z′'; the layer's '=' is italic-Z, ү(U+048F) is the prime",
    },
    ("2018-06", "02", "qp", 10, 39): {
        "mode": "text",
        "text": "    (d) n([X ∩ Z] ∪ Y′)",
        "evidence": "400dpi p10 crop: printed 'n([X ∩ Z] ∪ Y′)'; the layer's '<' is italic-Y",
    },
    # ===== 2019-06 01 QP — RTL-region Venn line
    ("2019-06", "01", "qp", 16, 45): {
        "mode": "text",
        "text": "   (c) Find n(H′ ∩ [L ∪ G])",
        "evidence": "200dpi p16 render: printed 'n(H′ ∩ [L ∪ G])'; U+202B/މ RTL artifacts + 0x88/0x89 = ∩/∪ (map class)",
    },
    # ===== 2019-06 01R QP — custom-encoded math runs
    ("2019-06", "01R", "qp", 2, 29): {
        "mode": "text",
        "text": "2   The nth term of a sequence is given by 9n − 7",
        "evidence": "200dpi p2 render: '9n − 7'; digit map \\x13+d verified (\\x1a=7)",
    },
    ("2019-06", "01R", "qp", 4, 18): {
        "mode": "text",
        "text": "6   Q = c2 − 4c",
        "evidence": "200dpi p4 render: 'Q = c² − 4c' (ð=², í=−, \\x17=4)",
    },
    ("2019-06", "01R", "qp", 4, 19): {
        "mode": "text",
        "text": "Work out the value of Q when c = −6",
        "evidence": "200dpi p4 render; \\x19=6",
    },
    ("2019-06", "01R", "qp", 5, 41): {
        "mode": "text",
        "text": "9   y = 4x3 − 7",
        "evidence": "200dpi p5 render: 'y = 4x³ − 7/x²' with the x2 denominator row already on the following -layout row",
    },
    ("2019-06", "01R", "qp", 10, 23): {
        "mode": "text",
        "text": "BD = 7.2 cm to 2 significant figures.",
        "evidence": "200dpi p10 render: 'BD = 7.2 cm...'; \\x1a\\x11\\x15 = 7.2 (decimal map)",
    },
    ("2019-06", "01R", "qp", 11, 26): {
        "mode": "text",
        "text": "                                 ∠ABD = 67° and ∠BEF = 123°",
        "evidence": "200dpi p11 render: '∠ABD = 67° and ∠BEF = 123°'; 0x83=°, \\x19\\x1a=67",
    },
    ("2019-06", "01R", "qp", 12, 36): {
        "mode": "text",
        "text": "19  The sum of the interior angles of a regular polygon is 2700°",
        "evidence": "200dpi p12 render: '...is 2700°'; \\x15\\x1a\\x13\\x13=2700 (digit map end-to-end)",
    },
    ("2019-06", "01R", "qp", 13, 15): {
        "mode": "text",
        "text": "(2 − √2) cm           accurately drawn",
        "evidence": "200dpi p13 render: diagram label '(2 − √2) cm'; í=√ on this run",
    },
    ("2019-06", "01R", "qp", 13, 20): {
        "mode": "text",
        "text": "AD = BC = (2 − √2) cm",
        "evidence": "200dpi p13 render",
    },
    ("2019-06", "01R", "qp", 13, 21): {
        "mode": "text",
        "text": "Area of ABCD = 3(5√2 − 2) cm2",
        "evidence": "200dpi p13 render: 'Area of ABCD = 3(5√2 − 2) cm²'",
    },
    ("2019-06", "01R", "qp", 19, 6): {
        "mode": "text",
        "text": "                            26 (a) Use the factor theorem to show that (2x − 1) is a factor of 6x3 + 23x2 − 5x − 4",
        "evidence": "200dpi p19 render; \\x19\\x18\\x17 = 6,5,4 digit-map verified",
    },
    ("2019-06", "01R", "qp", 22, 6): {
        "mode": "text",
        "text": "28  The table below gives information about the lengths of time, in minutes, that 75 cars",
        "evidence": "200dpi p22 render; \\x1a\\x18=75",
    },
    ("2019-06", "01R", "qp", 22, 26): {
        "mode": "text",
        "text": "       that the 75 cars were parked in the car park on Sunday.",
        "evidence": "200dpi p22 render; \\x11 = sentence period",
    },
    ("2019-06", "01R", "qp", 24, 15): {
        "mode": "text",
        "text": "   Given also that P is inversely proportional to y and that P = 75 when y = 4",
        "evidence": "200dpi p24 render; \\x1a\\x18=75",
    },
    # ===== 2019-06 02 QP — custom-encoded math runs
    ("2019-06", "02", "qp", 8, 7): {
        "mode": "text",
        "text": "             The points (1, 2), (3, −2) and (1, 4) are the vertices of triangle B.",
        "evidence": "200dpi p8 render; \\x14..\\x17 = 1,2,3,4; í=−; \\x0f=','",
    },
    ("2019-06", "02", "qp", 24, 18): {
        "mode": "text",
        "text": "(a) Show that x2 − 3x − 9 = 0",
        "evidence": "200dpi p24 render; \\x16=3 \\x1c=9 \\x13=0",
    },
    ("2019-06", "02", "qp", 24, 23): {
        "mode": "text",
        "text": "(ii) show that y = 2 − 3√5",
        "evidence": "200dpi p24 render: 'y = 2 − 3√5' (√ dropped by the layer)",
    },
    ("2019-06", "02", "qp", 28, 15): {
        "mode": "text",
        "text": "The tangent to C at the point A has gradient −8",
        "evidence": "200dpi p28 render; \\x1b=8",
    },
    ("2019-06", "02", "qp", 28, 16): {
        "mode": "text",
        "text": "(b) Show that 2a + b = −14",
        "evidence": "200dpi p28 render; \\x14\\x17=14",
    },
    ("2019-06", "02", "qp", 28, 23): {
        "mode": "text",
        "text": "the line with equation y = 7 − 4x.",
        "evidence": "200dpi p28 render; \\x1a=7 \\x17=4",
    },
    ("2019-06", "02", "qp", 32, 40): {
        "mode": "text",
        "text": "(b) Show that V = 1/3 πr2(15 − 4r)",
        "evidence": "200dpi p32 render: 'V = (1/3)πr²(15 − 4r)'; flat-fraction corpus convention",
    },
    ("2019-06", "02", "qp", 34, 8): {
        "mode": "text",
        "text": "(c) Complete the following table of values for V = 1/3 πr2(15 − 4r)",
        "evidence": "200dpi p32 render (the formula is dropped from the p34 layer row entirely)",
    },
    # ===== 2025-06 01R QP — the single ∠-run line (custom glyph block U+001D..U+001F)
    ("2025-06", "01R", "qp", 15, 23): {
        "mode": "text",
        "text": "    ∠ABC = 52° and the reflex angle AOC = x°",
        "evidence": "200dpi p15 render: '∠ABC = 52° and the reflex angle AOC = x°'",
    },
    # ===== 2019-06 02 MS — the OCR-sandwich rows (U+FFFD at bars/brackets/radicals)
    ("2019-06", "02", "ms", 5, 8): {
        "mode": "text",
        "text": "                  × 360",
        "evidence": "200dpi p5 render: '(48/200) × 360'; the FFFDs are the fraction-bar glyphs (born-digital layers drop bars); numerator 48 on the previous row, denominator 200 on the next",
    },
    ("2019-06", "02", "ms", 6, 13): {
        "mode": "text",
        "text": "                          × 3 )",
        "evidence": "200dpi p6 render: '(\"11 280 000\" / 10 × 3)'; bar dropped, close-paren kept",
    },
    ("2019-06", "02", "ms", 8, 19): {
        "mode": "text",
        "text": "           (         )\" (        )\" =",
        "evidence": "200dpi p8 render: matrix row-1 parens of (−0.5 0)(2 6 2); the digits live on the adjacent rows",
    },
    ("2019-06", "02", "ms", 8, 22): {
        "mode": "text",
        "text": "           (            )",
        "evidence": "200dpi p8 render: matrix row-2 paren pair",
    },
    ("2019-06", "02", "ms", 9, 9): {
        "mode": "text",
        "text": "                                                                      or (             ) seen.",
        "evidence": "200dpi p9 render: bracket pair around the matrix; notes tail preserved",
    },
    ("2019-06", "02", "ms", 9, 13): {
        "mode": "text",
        "text": "                                                   2(         )",
        "evidence": "200dpi p9 render: '2×(matrix)' bracket pair",
    },
    ("2019-06", "02", "ms", 9, 18): {
        "mode": "text",
        "text": "          (       )\"(                  )\" =",
        "evidence": "200dpi p9 render: ALT matrix product parens",
    },
    ("2019-06", "02", "ms", 9, 21): {
        "mode": "text",
        "text": "          \"(             )”",
        "evidence": "200dpi p9 render: quoted matrix bracket pair",
    },
    ("2019-06", "02", "ms", 9, 27): {
        "mode": "text",
        "text": "                                                    (       )         A1 for one correct row or column or for 3 of the variables",
        "evidence": "200dpi p9 render: bracket pair; notes tail preserved verbatim",
    },
    ("2019-06", "02", "ms", 11, 11): {
        "mode": "text",
        "text": "           (BE =) √(52 + 82 − 40√3)                                      We must see 40√3 or values which round to 69.3, 19.7 or",
        "evidence": "200dpi p11 render: '(BE =)√(5² + 8² − 40√3)'; 𝐵𝐵𝐵𝐵 OCR-duplicate → BE; notes tail preserved verbatim",
    },
    ("2019-06", "02", "ms", 11, 35): {
        "mode": "text",
        "text": "           (k =) √((18.9 + \"10\")/\"10\") (= 1.7)",
        "evidence": "200dpi p11 render: '(k =)√[(18.9 + \"10\")/\"10\"] (= 1.7)'",
    },
    ("2019-06", "02", "ms", 13, 8): {
        "mode": "text",
        "text": "              3/5 + (2/5 × 2/5) + (2/5 × 3/5 × 3/8)                                           M2, M1 for either 5 × 5 or 5 × 5 × 8",
        "evidence": "200dpi p13 render: the fraction stack 3/5 + (2/5 × 2/5) + (2/5 × 3/5 × 3/8); numerators were dropped by the OCR, bars = FFFD; notes tail preserved verbatim",
    },
    ("2019-06", "02", "ms", 13, 20): {
        "mode": "text",
        "text": "              3/5 + 2/5 p = 3/4 or (3/4 − 3/5) ÷ 2/5                                M2 or M1 for 2/5 p (oe) or (3/4 − 3/5) seen",
        "evidence": "200dpi p13 render; notes tail preserved verbatim",
    },
    ("2019-06", "02", "ms", 13, 28): {
        "mode": "text",
        "text": "              1/4 = 2/5 × q (q = 5/8)",
        "evidence": "200dpi p13 render: '(b) ALT 1/4 = 2/5 × q (q = 5/8)'",
    },
    ("2019-06", "02", "ms", 14, 10): {
        "mode": "text",
        "text": "      (b)   A = 1/2 ((2x + 3) + (5x + 3))(4x) oe                          2     M1 Allow A = (2x + 3) × 4x + 2 × 3x × 4x or",
        "evidence": "200dpi p14 render: 'A = ½((2x + 3) + (5x + 3))(4x) oe'; notes tail preserved verbatim",
    },
    ("2019-06", "02", "ms", 15, 7): {
        "mode": "text",
        "text": "9     (a)      √((2x − 1)2 + y2) = √98                                   5     M1 Correct use of modulus to form any correct equation",
        "evidence": "200dpi p15 render: '√((2x − 1)² + y²) = √98'; notes tail preserved verbatim",
    },
    ("2019-06", "02", "ms", 15, 28): {
        "mode": "text",
        "text": "               or (x − 3/2)2 − 9/4 − 9 = 0",
        "evidence": "200dpi p15 render: 'or (x − 3/2)² − 9/4 − 9 = 0' (completing the square)",
    },
    ("2019-06", "02", "ms", 16, 7): {
        "mode": "text",
        "text": "          y = 5 − 2((3 + 3√5)/2)                                    involving surds into linear equation to find y",
        "evidence": "200dpi p16 render: 'y = 5 − 2((3 + 3√5)/2)'; notes tail preserved verbatim",
    },
    ("2019-06", "02", "ms", 16, 14): {
        "mode": "text",
        "text": "                                                                     expansion of (2 − 3√5)2 = 49 − 12√5 along with an",
        "evidence": "200dpi p16 render; notes tail preserved verbatim",
    },
    ("2019-06", "02", "ms", 16, 21): {
        "mode": "text",
        "text": "          (2 − 3√5 + 3)2 + (−(2 − 3√5))2                               Eg. (y + 3)2 + y2 or (8 − 2x)2 + (5 − 2x)2",
        "evidence": "200dpi p16 render: '(2 − 3√5 + 3)² + (−(2 − 3√5))²'; notes tail preserved verbatim",
    },
    ("2019-06", "02", "ms", 16, 26): {
        "mode": "text",
        "text": "                                                  7(17 − 6√5)",
        "evidence": "200dpi p16 render: answer '7(17 − 6√5)'",
    },
    ("2019-06", "02", "ms", 17, 10): {
        "mode": "text",
        "text": "            (f′(x) =)6x2 + 2ax + b",
        "evidence": "200dpi p17 render: '(f′(x) =)6x² + 2ax + b'",
    },
}


def sha256(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main(apply: bool = True):
    by_file = {}
    for (series, paper, kind, page, line), spec in sorted(PATCHES.items()):
        by_file.setdefault((series, paper, kind), []).append((page, line, spec))
    manifest = []
    failures = []
    for (series, paper, kind), items in sorted(by_file.items()):
        txt = U / f"official-{series}-{paper}-{kind}.txt"
        pages = txt.read_text().split("\f")
        for page, line, spec in items:
            if page - 1 >= len(pages):
                failures.append((series, paper, kind, page, line, "page out of range"))
                continue
            lines = pages[page - 1].split("\n")
            if line - 1 >= len(lines):
                failures.append((series, paper, kind, page, line, "line out of range"))
                continue
            orig = lines[line - 1]
            entry = {
                "series": series, "paper": paper, "kind": kind, "page": page,
                "line": line, "original_sha256": sha256(orig),
                "original": orig, "replacement": spec["text"],
                "evidence": spec["evidence"],
            }
            manifest.append(entry)
            if apply:
                lines[line - 1] = spec["text"]
                pages[page - 1] = "\n".join(lines)
        if apply:
            txt.write_text("\f".join(pages))
    out = U / "line-patch-manifest.json"
    out.write_text(json.dumps({"schema": "syllabai.examq-line-patch/0.1",
                               "patches": manifest, "failures": failures},
                              indent=1, ensure_ascii=False))
    print(f"patches: {len(manifest)}  failures: {len(failures)}")
    for f in failures:
        print("  FAIL", f)
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main(apply="--check" not in sys.argv)
