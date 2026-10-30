#!/usr/bin/env python3
"""F119 zero-network unit battery — the printed-part-label serving wave.

Verifies the LAW and the SERVED DATA of record without emitting:
  1. printed_part_label(): the derivation law — question number stripped,
     1-3 parenthesized [a-z0-9]{1,5} groups, fail-closed (bare numbers,
     uppercase, 4-level, glued fragments all refuse to None).
  2. g_e6_label_law(): the identity law — questionPart == the id slug's path
     re-wrapped, null IFF path-less; both drift directions raise; census
     accumulates per-path-level counts.
  3. The staged exports of record (the F119 v2 sync bytes) carry the law:
     every official part in the staged official-papers.json satisfies
     g_e6_label_law, and the labelled/null census matches the F119 receipt
     (4ph1: 2,239 labelled / 15 null; 4ch1: 2,607 labelled / 0 null).
  4. The exporter source carries the emission site (questionPart wired to
     printed_part_label) — a regression that unwires the field fails here.

Zero network, zero emission; reads the staged outputs when present
(set EXAMQ_F119_STAGE_ROOT to the run's staging root, default <repo>/../f119-stage).
"""
import json
import os
import re
import sys
from pathlib import Path

RES = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RES / "scripts"))
import official_examq_export_hub as E

fails = []


def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {name}{(' — ' + detail) if detail else ''}")
    if not ok:
        fails.append(name)


def raises(fn):
    try:
        fn()
        return False
    except E.ExportGateError:
        return True


# ── 1. printed_part_label derivation law ─────────────────────────────────────
P = E.printed_part_label
check("1(a)(i) -> (a)(i)", P("1(a)(i)") == "(a)(i)")
check("2(b) -> (b)", P("2(b)") == "(b)")
check("10(c)(ii) -> (c)(ii)", P("10(c)(ii)") == "(c)(ii)")
check("3(a) -> (a)", P("3(a)") == "(a)")
check("bare '7' -> None (whole-question slice)", P("7") is None)
check("bare '24' -> None", P("24") is None)
check("None-safe", P(None) is None)
check("empty-safe", P("") is None)
check("glued fragment '1(b ii)' refuses", P("1(b ii)") is None)
check("uppercase '1(A)' refuses", P("1(A)") is None)
check("4-group '1(a)(i)(x)(ii)' refuses (grammar ≤ 3 levels)", P("1(a)(i)(x)(ii)") is None)
check("3-group '1(a)(i)(x)' accepts (grammar boundary)", P("1(a)(i)(x)") == "(a)(i)(x)")
check("digits-in-group '2(a1)' accepts", P("2(a1)") == "(a1)")
check("no leading number 'a(i)' refuses (identity is qnum-prefixed)", P("a(i)") is None)

# ── 2. g_e6_label_law identity law ──────────────────────────────────────────
def part(pid, label):
    return {"id": pid, "sourcePaper": {"questionPart": label}}

census = {}
E.g_e6_label_law([part("offp_2019-06_1p_1-a-i", "(a)(i)"),
                  part("offp_2019-06_1p_7", None)], census)
check("law holds on matching parts", census == {2: 1, 0: 1}, str(census))
check("vanished label raises", raises(lambda: E.g_e6_label_law(
    [part("offp_2019-06_1p_1-a-i", None)])))
check("invented label raises", raises(lambda: E.g_e6_label_law(
    [part("offp_2019-06_1p_1-a-i", "(a)(ii)")])))
check("path-less + label raises", raises(lambda: E.g_e6_label_law(
    [part("offp_2019-06_1p_7", "(a)")])))
check("off-grammar id raises", raises(lambda: E.g_e6_label_law(
    [part("offp_2019-06_1p", None)])))
check("4-segment path raises", raises(lambda: E.g_e6_label_law(
    [part("offp_2019-06_1p_1-a-i-x-ii", "(a)(i)(x)(ii)")])))
check("3-segment path accepts", not raises(lambda: E.g_e6_label_law(
    [part("offp_2019-06_1p_1-a-i-x", "(a)(i)(x)")])))

# ── 3. the emission site is wired ────────────────────────────────────────────
src = (RES / "scripts" / "official_examq_export_hub.py").read_text(encoding="utf-8")
check("sourcePaper.questionPart wired to printed_part_label",
      '"questionPart": printed_part_label(p["part_number"])' in src)
check("G-E6 gate present in run_gates", "g_e6_label_law(q[\"parts\"]" in src)
import official_examq_verify_export as V
check("verify harness delta classes learned sourcePaper (F119)",
      "sourcePaper" in V.DISCLOSED_DELTA_CLASSES)

# ── 4. the staged exports of record carry the law (when staged) ─────────────
# Local receipt re-verification: SKIP (not FAIL) when no F119 staging exists —
# the CI tree has no staged exports; the law + wiring checks above are the CI
# value of this battery.
_env = os.environ.get("EXAMQ_F119_STAGE_ROOT")
_default_local = Path("/home/z/my-project/hubsync/final")
if _env:
    stage_root = Path(_env)
elif _default_local.exists():
    stage_root = _default_local
else:
    stage_root = None
COURSE_DIRS = {"igcse-physics-19": "phys", "igcse-chemistry-19": "chem",
               "igcse-maths-b-16": "mb"}
if stage_root is None:
    print("SKIP  staged-export checks (no F119 stage — local receipt only)")
EXPECT = {
    "igcse-physics-19": (2239, 15),
    "igcse-chemistry-19": (2607, 0),
    "igcse-maths-b-16": (1723, 720),
}
for course, (n_lab, n_null) in EXPECT.items():
    if stage_root is None:
        continue
    f = stage_root / COURSE_DIRS[course] / "content" / course / "official-papers.json"
    if not f.exists():
        check(f"{course}: staged export present (EXAMQ_F119 stage)", False,
              f"missing {f} — run the F119 exports first")
        continue
    doc = json.load(open(f, encoding="utf-8"))
    c = {}
    bad = 0
    n_lab_seen = n_null_seen = 0
    try:
        for s in doc:
            for q in s["questions"]:
                E.g_e6_label_law(q["parts"], c)
    except E.ExportGateError:
        bad += 1
    for s in doc:
        for q in s["questions"]:
            for p in q["parts"]:
                if p["sourcePaper"]["questionPart"] is None:
                    n_null_seen += 1
                else:
                    n_lab_seen += 1
    check(f"{course}: every official part satisfies the G-E6 law", bad == 0)
    check(f"{course}: labelled/null census == F119 receipt",
          (n_lab_seen, n_null_seen) == (n_lab, n_null),
          f"seen {n_lab_seen}/{n_null_seen} vs expected {n_lab}/{n_null}")

print()
if fails:
    print(f"F119 UNIT BATTERY: {len(fails)} FAIL")
    sys.exit(1)
print("F119 UNIT BATTERY: all checks PASS")
