#!/usr/bin/env python3
"""MS-grid strip-law tests — the F88 reconciliation's remaining half (v0.30.1).

Zero-network, zero-staging unit battery for the two laws that own the MS-grid
furniture universe (LEDGER F88/F108/F111):

  1. FURNITURE_SUBS — the raw-layer footer consumption. v0.30.1 completes the
     F87 abbreviated-footer sub with its printed ' marks' tail: the staging
     line 'Total for Q3 = 8 marks' (2020-11 1C MS L229) previously left the
     tail behind, which reached the assembled solution text of 3(c)(ii) as a
     lone 'marks' line mid-text — the F111 census's ONE fresh-vs-record
     furniture disagreement ("the F88 reconciliation's remaining half").
  2. strip_ms_grid_furniture / MS_TOTAL_LINE_RE — the assembled-text strip.
     The F88 wrap-ambiguous keep class (bare answer/mark/marks/Number lines —
     wrapped guidance fragments) must stay KEPT mid-text; the trailing pop and
     the fail-closed refusal must behave exactly as the F108 port defined.

The battery pins BOTH directions of the reconciliation: the leak class closes
at source, and the 12 standing keep instances' law is untouched.

Run: python3 scripts/official_examq_strip_law_tests.py   (exit 0 = all hold)
"""
import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONVERTER = HERE / "official_examq_extract.py"

spec = importlib.util.spec_from_file_location("oeq_extract_law", CONVERTER)
mod = importlib.util.module_from_spec(spec)
sys.modules["oeq_extract_law"] = mod
spec.loader.exec_module(mod)


def raw_layer(line: str) -> str:
    """Replicates the clean_lines per-line transform for the chemistry lane:
    normalize_pua -> FURNITURE_SUBS (+ the F89 exponent restore after each
    sub, chemistry-gated). This is the layer the v0.30.1 fix lives in."""
    ln = mod.normalize_pua(line)
    for rx, rep in mod.FURNITURE_SUBS:
        ln = rx.sub(rep, ln)
        ln = mod.restore_flat_exponents(ln)  # ACTIVE lane is 4ch1 in these tests
    return ln


fails = []
checks = 0


def check(name, cond, detail=""):
    global checks
    checks += 1
    if cond:
        print(f"  ok  {name}")
    else:
        fails.append(name)
        print(f"  FAIL {name} {detail}")


print("leg 1 — the abbreviated footer is consumed WITH its marks tail (the leak closed at source)")
for footer, qn in [("Total for Q1 = 7 marks", "Q1"),
                   ("Total for Q2 = 6 marks", "Q2"),
                   ("Total for Q3 = 8 marks", "Q3"),
                   ("Total for Q10 = 13 marks", "Q10")]:
    staged = " " * 60 + footer            # deep-right layout line, as staged
    out = raw_layer(staged)
    check(f"{qn} footer fully consumed (2020-11 1C staging)", out.strip() == "", repr(out.strip()))

out = raw_layer(" " * 40 + "Total for Q3 = 8")
check("marks-less abbreviated form still consumed (F87 original)", out.strip() == "", repr(out.strip()))
out = raw_layer(" " * 30 + "Total for question = 15 marks")
check("F93 third word order still consumed", out.strip() == "", repr(out.strip()))

print("leg 2 — the F88 wrap-ambiguous keep class is UNTOUCHED (the 12 standing keeps)")
keeps = [
    ("2019-06 1C 9(a)", "or numerators and\ndenominators reversed 0\nmarks\nAlternative method"),
    ("2019-06 1CR 9(c)", "must include M3 and M6 for full\nmarks\n(graphite is soft because)"),
    ("2021-11 2C 2(c)(ii)", "307.5-312.5 with no\nworking scores 2\nmarks\nALLOW M1×2.5"),
    ("2023-11 2C 7(d)(i)", "ALLOW −241 (kJ) (for 1\nmole of water) for all 3\nmarks\nsign required to score"),
    ("2026-06 1CR 6(a)(iii)", "correct answer scores 2\nmarks\nM1 (28 ÷ 80) × 100"),
]
for label, text in keeps:
    lines = text.splitlines()
    after = [raw_layer(ln) for ln in lines]
    # no sub may consume or rewrite a bare wrapped-guidance 'marks' line
    bare = [ln for ln in lines if ln.strip() == "marks"]
    check(f"{label}: bare 'marks' line not a sub target", bool(bare) and all(raw_layer(b).strip() == "marks" for b in bare))
    # and the assembled-text strip must KEEP it mid-text (fail-closed <2-token law)
    stripped = mod.strip_ms_grid_furniture(text)
    check(f"{label}: mid-text 'marks' kept by strip law", any(ln.strip() == "marks" for ln in stripped.splitlines()),
          repr(stripped))

out = raw_layer("working scores 2")
check("guidance fragment line passes through unchanged", out == "working scores 2", repr(out))

print("leg 3 — MS_TOTAL_LINE_RE recognizes the printed footer verbatim (consistency leg)")
check("abbreviated + marks fullmatch", bool(mod.MS_TOTAL_LINE_RE.fullmatch("Total for Q3 = 8 marks")))
check("abbreviated without marks fullmatch (unchanged)", bool(mod.MS_TOTAL_LINE_RE.fullmatch("Total for Q3 = 8")))
check("spelled form fullmatch (unchanged)", bool(mod.MS_TOTAL_LINE_RE.fullmatch("Total for Question 3 = 8 marks")))
check("bare Total fullmatch (unchanged)", bool(mod.MS_TOTAL_LINE_RE.fullmatch("Total")))
check("F110 digit-bearing guidance line is NOT Total-family",
      not mod.MS_TOTAL_LINE_RE.fullmatch("ALLOW 297 X 9.75/65 =44.55/44.6 for 2 marks"))
mid = "M1 copper(II) oxide/CuO\nTotal for Q3 = 8 marks\nM2 because it loses oxygen"
stripped = mod.strip_ms_grid_furniture(mid)
check("mid-text footer-verbatim line stripped by the assembled-text law",
      "Total for Q3 = 8 marks" not in stripped.splitlines() and "M1 copper(II) oxide/CuO" in stripped.splitlines())

print("leg 4 — the trailing pop and the fail-closed refusal behave exactly as the F108 port")
check("trailing lone marks popped (the Q1/Q2/Q10 tail path)",
      mod.strip_ms_grid_furniture("IGNORE references to\nelectrons\nmarks") == "IGNORE references to\nelectrons")
check("trailing Total-footer popped", mod.strip_ms_grid_furniture("answer text\nTotal for Question 3 = 8 marks")
      == "answer text")
only_furniture = "Question Answer Notes Marks\nTotal\nmarks"
check("fail-closed refusal: all-furniture text returned intact",
      mod.strip_ms_grid_furniture(only_furniture) == only_furniture)
check("empty text untouched", mod.strip_ms_grid_furniture("") == "")

print("leg 5 — the 2020-11 1C 3(c)(ii) reconciliation, end to end at the law level")
# The of-record solution_md (serve-clean form) and the pre-fix fresh form
# (fresh carried the leaked tail between 'electrons' and '- -'). The raw layer
# must now produce the of-record form from the staged footer universe.
of_record_tail = "IGNORE references to\nelectrons\n- -"
leaky_tail = "IGNORE references to\nelectrons\nmarks\n- -"
check("strip law refuses to create the of-record form from the leaky text (the fix is UPSTREAM, not a strip patch)",
      mod.strip_ms_grid_furniture(leaky_tail) == "IGNORE references to\nelectrons\nmarks\n- -")
check("raw layer consumes the staged footer line whole (no 'marks' can reach assembly)",
      raw_layer(" " * 75 + "Total for Q3 = 8 marks").strip() == "")

print()
if fails:
    print(f"STRIP-LAW TESTS: {len(fails)}/{checks} FAILED: {fails}")
    sys.exit(1)
print(f"STRIP-LAW TESTS: all {checks} checks green")
