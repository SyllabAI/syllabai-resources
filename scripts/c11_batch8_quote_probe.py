#!/usr/bin/env python3
"""T-C11 session 61 — pre-authoring quote probe for the batch-8 decision
record (scripts/c11_batch8_decisions.yaml): every planned NOTE / MARK_SCHEME
/ SPEC quote must byte-verify under the T-C10 norm() in its cited file, and
every SPEC quote must sit inside its SP's official wording (the
c11_batch7_quote_probe.py pattern, batch-8-scoped).

Run BEFORE authoring so the decision record is written against verified
quotes only (fail-closed; the generator's G03 and the preverify re-check
these independently).
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent

H = ("Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
     "h. Chemical Tests/")
F1 = H + "Gas tests - IGCSE Chemistry Revision Notes.md"
F2 = H + "Flame tests - IGCSE Chemistry Revision Notes.md"
F3 = H + "Tests for cations - IGCSE Chemistry Revision Notes.md"
F4 = H + "Tests for Anions  Edexcel IGCSE Chemistry Revision Notes 2017.md"
F5 = H + "Chemical test for water - IGCSE Chemistry Revision Notes.md"
M1 = "scripts/c11_evidence/CHEMICAL_TESTS_MS_P2.txt"
SP = "graph/igcse-chemistry/specification_points.yaml"

# (file, quote, kind, sp-or-None)  — SPEC quotes checked against the SP wording
PROBES = [
    # --- 2.44 gas tests (F1) ------------------------------------------------
    (F1, "Several tests for anions and cations produce gases which then need to be tested", "NOTE", "4CH1-2.44"),
    (F1, "Ammonia is a gas with a characteristic sharp choking smell that turns damp red litmus paper blue", "NOTE", "4CH1-2.44"),
    (F1, "If the gas is carbon dioxide, the limewater turns cloudy white", "NOTE", "4CH1-2.44"),
    (F1, "The test for carbon dioxide involves bubbling the gas through an aqueous solution of limewater (calcium hydroxide)", "NOTE", "4CH1-2.44"),
    (F1, "If chlorine gas is present, damp blue litmus paper will turn red and then be bleached white", "NOTE", "4CH1-2.44"),
    (F1, "It turns red initially as acids are produced when chlorine comes into contact with water", "NOTE", "4CH1-2.44"),
    (F1, "Chlorine should always be handled in a fume cupboard due to its toxicity", "NOTE", "4CH1-2.44"),
    (F1, "The test for hydrogen consists of holding a burning splint at the open end of a test tube of gas", "NOTE", "4CH1-2.44"),
    (F1, "which is the result of the rapid combustion of hydrogen with oxygen to produce water", "NOTE", "4CH1-2.44"),
    (F1, "Be sure not to insert the splint right into the tube, just at the mouth, as the gas needs air to burn", "NOTE", "4CH1-2.44"),
    (F1, "If the gas is oxygen, the splint will relight", "NOTE", "4CH1-2.44"),
    (F1, "If you are testing for ammonia produced from ammonium ions and sodium hydroxide, avoiding touching the sides to prevent traces of sodium hydroxide from also turning the red litmus paper blue", "NOTE", "4CH1-2.44"),
    (SP, "describe tests for these gases:", "SPEC", "4CH1-2.44"),
    # --- 2.45/2.46 flame tests (F2) ------------------------------------------
    (F2, "The flame test is used to identify the positive metal ion (cations) by the colour of the flame they produce", "NOTE", "4CH1-2.45"),
    (F2, "Ions from different metals produce different colours", "NOTE", "4CH1-2.46"),
    (F2, "Dip the loop of an unreactive metal wire such as nichrome or platinum in dilute acid", "NOTE", "4CH1-2.45"),
    (F2, "Hold it in the blue flame of a Bunsen burner until there is no colour change", "NOTE", "4CH1-2.45"),
    (F2, "Dip the loop into the solid sample / solution and place it in the edge of the blue Bunsen flame", "NOTE", "4CH1-2.45"),
    (F2, "It is important to place the wire into acid first to prevent contamination", "NOTE", "4CH1-2.45"),
    (F2, "Not doing this might result in two or more ions being present on the wire meaning the colours will mix", "NOTE", "4CH1-2.45"),
    (F2, "One colour could mask another colour and you will not be able to identify the ion", "NOTE", "4CH1-2.45"),
    (F2, "The colour of the flame is observed and used to identify the metal ion present", "NOTE", "4CH1-2.46"),
    (F2, "The sample needs to be heated strongly, so the Bunsen burner flame should be on a blue flame", "NOTE", "4CH1-2.45"),
    (SP, "describe how to carry out a flame test", "SPEC", "4CH1-2.45"),
    (SP, "know the colours formed in flame tests for these cations:", "SPEC", "4CH1-2.46"),
    # --- 2.47 cation tests (F3) ----------------------------------------------
    (F3, "Metal cations in aqueous solution can be identified by the colour of the precipitate formed when sodium hydroxide (NaOH) is added", "NOTE", "4CH1-2.47"),
    (F3, "A few drops of NaOH is added at first and any colour changes or precipitates formed are noted", "NOTE", "4CH1-2.47"),
    (F3, "A metal hydroxide precipitate typically forms if the hydroxide is insoluble in water", "NOTE", "4CH1-2.47"),
    (F3, "If no precipitate forms, the hydroxide may be soluble or there may not be enough of the metal ion present", "NOTE", "4CH1-2.47"),
    (F3, "Fe2+ (aq) + 2OH– (aq) → Fe(OH)2 (s)", "NOTE", "4CH1-2.47"),
    (F3, "Cu2+ (aq) + 2OH– (aq) → Cu(OH)2 (s)", "NOTE", "4CH1-2.47"),
    (F3, "You need to specifically state light blue for the precipitate colour to be sure of the mark", "NOTE", "4CH1-2.47"),
    (F3, "Add NaOH and warm the mixture", "NOTE", "4CH1-2.47"),
    (F3, "Observation with NaOH: Ammonia gas is released", "NOTE", "4CH1-2.47"),
    (F3, "NH4+ (aq) + OH- (aq) → NH3 (g) + H2O (l)", "NOTE", "4CH1-2.47"),
    (F3, "Test for ammonia gas: Ammonia turns damp red litmus paper blue", "NOTE", "4CH1-2.47"),
    (F3, "Sometimes the cation may be present in very small amounts, so the precipitate might appear only as a slight cloudiness or faint colour change - this can still indicate a positive test result.", "NOTE", "4CH1-2.47"),
    (SP, "describe tests for these cations:", "SPEC", "4CH1-2.47"),
    # --- 2.48 anion tests (F4) -------------------------------------------------
    (F4, "Negatively charged non-metal ions are known as anions", "NOTE", "4CH1-2.48"),
    (F4, "Halide ions are the negative ions / anions formed by the elements in Group 7", "NOTE", "4CH1-2.48"),
    (F4, "Add dilute acid", "NOTE", "4CH1-2.48"),
    (F4, "Bubble the gas released through limewater", "NOTE", "4CH1-2.48"),
    (F4, "Limewater turns cloudy if the carbonate ion is present", "NOTE", "4CH1-2.48"),
    (F4, "If a carbonate compound is present then fizzing / effervescence should be seen as CO2 gas is produced, which forms a white precipitate of calcium carbonate when bubbled through limewater:", "NOTE", "4CH1-2.48"),
    (F4, "The white precipitate turns limewater cloudy", "NOTE", "4CH1-2.48"),
    (F4, "Acidify the sample with nitric acid", "NOTE", "4CH1-2.48"),
    (F4, "A silver halide precipitate forms if a halide ion is present", "NOTE", "4CH1-2.48"),
    (F4, "The precipitate is indicated by the state symbol (s)", "NOTE", "4CH1-2.48"),
    (F4, "The chloride ion forms a white precipitate of silver chloride", "NOTE", "4CH1-2.48"),
    (F4, "The bromide ion forms a cream precipitate of silver bromide", "NOTE", "4CH1-2.48"),
    (F4, "The iodide ions forms a yellow precipitate of silver iodide", "NOTE", "4CH1-2.48"),
    (F4, "Acidify the sample with dilute hydrochloric acid", "NOTE", "4CH1-2.48"),
    (F4, "Add a few drops of barium chloride solution", "NOTE", "4CH1-2.48"),
    (F4, "A white precipitate of barium sulfate is formed, if the sulfate ion is present", "NOTE", "4CH1-2.48"),
    (F4, "Ba2+ (aq) + SO42- (aq) → BaSO4 (s)", "NOTE", "4CH1-2.48"),
    (F4, "The test can also be carried out with barium nitrate solution", "NOTE", "4CH1-2.48"),
    (F4, "Sulfate compounds contain the sulfate ion, SO42-", "NOTE", "4CH1-2.48"),
    (F4, "Carbonate compounds contain the carbonate ion, CO32-", "NOTE", "4CH1-2.48"),
    (SP, "describe tests for these anions:", "SPEC", "4CH1-2.48"),
    # --- 2.49/2.50 water tests (F5) ----------------------------------------------
    (F5, "Water can be identified using a chemical test and/or a physical test", "NOTE", "4CH1-2.49"),
    (F5, "Anhydrous copper(II) sulfate turns from white to blue on the addition of water", "NOTE", "4CH1-2.49"),
    (F5, "CuSO4 (s) + 5H2O (l) → CuSO4.5H2O (s)", "NOTE", "4CH1-2.49"),
    (F5, "Copper sulfate turns a light blue colour in the presence of water", "NOTE", "4CH1-2.49"),
    (SP, "describe a test for the presence of water using anhydrous copper(II) sulfate", "SPEC", "4CH1-2.49"),
    (F5, "A physical test to see if a sample of water is pure is to check its boiling point", "NOTE", "4CH1-2.50"),
    (F5, "A sample of the liquid is placed in a suitable container such as a boiling tube and gently heated", "NOTE", "4CH1-2.50"),
    (F5, "Using a thermometer, you can check if the boiling point is exactly 100 oC", "NOTE", "4CH1-2.50"),
    (F5, "Any impurities present will usually tend to raise the boiling point and depress the melting point of pure substance", "NOTE", "4CH1-2.50"),
    (SP, "describe a physical test to show whether a sample of water is pure", "SPEC", "4CH1-2.50"),
    # --- misconception 1: glowing-splint hydrogen (M1) ----------------------------
    (M1, "Reject reference to glowing splint", "MARK_SCHEME", None),
    (M1, "\u2018Squeaky pop test\u2019 on its own is not sufficient", "MARK_SCHEME", None),
    (M1, "Reference to splint/match with no indication of flame is not enough", "MARK_SCHEME", None),
    (M1, "Ignore flame extinguished", "MARK_SCHEME", None),
    (M1, "hydrogen / H2", "MARK_SCHEME", None),
    (M1, "burns with a pop/squeak", "MARK_SCHEME", None),
    (M1, "use burning/lit splint/flame to see if pop/squeak", "MARK_SCHEME", None),
    # remediation (F1)
    (F1, "It is easy to confuse the tests for hydrogen and oxygen.", "NOTE", None),
    (F1, "Try to remember that a ligHted splint has an H for Hydrogen, while a glOwing splint has an O for Oxygen.", "NOTE", None),
    # --- misconception 2: halide-test acid choice (M1) -----------------------------
    (M1, "Reject hydrochloric acid / HCl", "MARK_SCHEME", None),
    (M1, "Reject other named acids", "MARK_SCHEME", None),
    (M1, "Ignore acid(ified) without a named acid", "MARK_SCHEME", None),
    (M1, "(dilute) nitric acid / HNO3", "MARK_SCHEME", None),
    (M1, "AgCl", "MARK_SCHEME", None),
    # remediation (F4)
    (F4, "The colour of the silver halide precipitate depends on the halide ion:", "NOTE", None),
    # --- in-slice edge anchors --------------------------------------------------------
    (F3, "Test for ammonia gas: Ammonia turns damp red litmus paper blue", "NOTE", None),
    (F4, "Bubble the gas released through limewater", "NOTE", None),
    (F1, "If the gas is carbon dioxide, the limewater turns cloudy white", "NOTE", None),
    (F2, "The flame test is used to identify the positive metal ion (cations) by the colour of the flame they produce", "NOTE", None),
    (F3, "Metal cations in aqueous solution can be identified by the colour of the precipitate formed when sodium hydroxide (NaOH) is added", "NOTE", None),
    (F4, "Sulfate compounds contain the sulfate ion, SO42-", "NOTE", None),
    (F3, "Test for ammonium ion, NH4+", "NOTE", None),
    (F5, "Any impurities present will usually tend to raise the boiling point and depress the melting point of pure substance", "NOTE", None),
]

sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402

_TRANS = {ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = s.translate(_TRANS)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def main() -> int:
    import yaml
    spec = yaml.safe_load(
        GP.store("specification_points").read_text(encoding="utf-8"))
    wording = {p["code"]: p["official_wording"]
               for p in spec["specification_points"]}

    fails = 0
    for i, (rel, quote, kind, sp) in enumerate(PROBES, 1):
        file_rel = GP.resolve_rel(rel)
        p = REPO / file_rel
        if not p.exists():
            print(f"FAIL {i:03d} file missing: {file_rel}")
            fails += 1
            continue
        body = norm(p.read_text(encoding="utf-8"))
        if norm(quote) not in body:
            print(f"FAIL {i:03d} [{kind}] quote NOT in {file_rel} :: {quote[:80]!r}")
            fails += 1
            continue
        if kind == "SPEC" and sp:
            if norm(quote) not in norm(wording[sp]):
                print(f"FAIL {i:03d} [SPEC] not inside {sp} wording :: {quote[:60]!r}")
                fails += 1
                continue
        print(f"PASS {i:03d} [{kind}] {quote[:66]!r}")
    print(f"\nquote probe: {len(PROBES) - fails}/{len(PROBES)} green"
          + (" — FAIL-CLOSED" if fails else " — ALL QUOTES VERIFIED"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
