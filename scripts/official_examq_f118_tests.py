#!/usr/bin/env python3
"""F118 zero-network unit battery — the F95 ALLOW-lead guard (the answer-cell class).

Verifies the LAW and its DATA of record without emitting:
  1. The guard law in the converter source of record: the ALLOW arm is split
     out of the fragment regex and refuses to fire on M-marker ROW structure
     (`\\nM<digit>` — the answer cell's own content skeleton); version 0.33.0.
  2. The law is alive on the of-record bytes: 2025-11 1C 5(c)'s exact MP1
     (the full six-M-row transcription, sha-verified MS p8 eyeball) is NOT a
     fragment — the F95 junk flag exits; the part's of-record serving is
     already complete (solution_md == the MP copy), so no corpus byte moves.
  3. The guard is arm-scoped: every standing classification keeps its flag —
     the ALLOW-lead margin notes without M-rows (2021-01 1C 3(d), 2021-06 1C
     10(c)(i), the F113-served 2019-06 2C 2(a)), the IGNORE/REJECT arms
     (6(d)(ii), 8(c)(ii), 7(c)(ii)), the disclosed class-4 `scores`-arm
     members whose texts DO carry M-rows (2020-01 1CR 8(a), 2022-01 1C 6(a)),
     the founding fragment shapes ('If M1 and M2 not fully', 'max 1 mark',
     'dep on M1', inline 'ALLOW M1×2.5'), the bare marks-digit leak, and the
     F108 answer-grid exemption.
  4. Corpus-wide census with the live code: exactly 18 fragment-shape hits;
     the delta vs the pre-F118 law is exactly {2025-11 1C 5(c)} (19 -> 18,
     the A/B of record); the F113-served parts and the disclosed residual
     keep their flags.
  5. F97-site blast radius: zero parts corpus-wide have an empty solution_md
     with refused MPs — no emission changes, learner bytes untouched.

Zero network, zero emission; corpus read-only.
"""
import json, re, sys
from pathlib import Path

RES = Path(__file__).resolve().parent.parent
CORP = RES / "Official-ExamQuestion" / "igcse-chemistry-19"
sys.path.insert(0, str(RES / "scripts"))
import official_examq_extract as X

fails = []


def check(name, ok, note=""):
    print(("PASS  " if ok else "FAIL  ") + name + (f" — {note}" if note else ""))
    if not ok:
        fails.append(name)


# ---- 1. the guard law in the source of record --------------------------------
src = (RES / "scripts" / "official_examq_extract.py").read_text()
check("F118 guard: ALLOW arm split out of the fragment regex",
      re.search(r"allow_frag = re\.compile\(r\"\^ALLOW\\b\.\*\$\", re\.I \| re\.S\)", src) is not None)
check("F118 guard: M-row guard present",
      re.search(r"mrow = re\.compile\(r\"\\nM\\d\+\\b\"\)", src) is not None)
check("F118 guard: the guarded continue is in the loop",
      "if allow_frag.match(t) and not mrow.search(t):" in src)
check("F118 guard: the bare ALLOW arm is gone from the shared regex",
      re.search(r'r"\|ALLOW\\b\.\|', src) is None and "dep\\s+on\\s+M\\d.*\"\n        r\"|ALLOW\\b.*" not in src)
m = re.search(r'CONVERTER_VERSION = "(\d+)\.(\d+)\.(\d+)"', src)
ver = tuple(int(x) for x in m.groups()) if m else (0, 0, 0)
check("F118 version floor 0.33.0", ver >= (0, 33, 0), f"v{ver[0]}.{ver[1]}.{ver[2]}")


def part_of(series, paper, pn):
    t = json.loads((CORP / series / f"4CH1-{paper}" / "topic.json").read_text())
    return [pp for q in t["questions"] for pp in q["parts"] if pp["part_number"] == pn][0]


# ---- 2. the law is alive on the of-record bytes -------------------------------
p5c = part_of("2025-11", "1C", "5(c)")
mps5c = p5c["mark_points"]
t5c = mps5c[0]["text_md"]
check("5(c) of record: single 2-mark MP, the full six-M-row transcription",
      len(mps5c) == 1 and p5c["marks"] == 2 and t5c.startswith("Allow any two from:")
      and len(re.findall(r"\nM\d+\b", t5c)) == 6, f"{len(mps5c)} MP / {p5c['marks']} marks")
check("5(c) M-rows M1..M6 all present", all(f"\nM{i}" in t5c for i in range(1, 7)))
check("F118 LAW: 5(c) is NOT a margin-note fragment (the junk flag exits)",
      X._mp_only_fragments(mps5c, p5c["marks"]) is False)
check("5(c) of-record serving already complete (solution_md == the MP copy)",
      (p5c.get("solution_md") or "").strip() == t5c,
      "no corpus byte moves — the F95 flag was report-side only")

# ---- 3. the guard is arm-scoped: every standing classification keeps ----------
check("3(d) 'ALLOW multiples and…' (no M-rows) still a fragment",
      X._mp_only_fragments(part_of("2021-01", "1C", "3(d)")["mark_points"], 1) is True)
check("10(c)(i) 'ALLOW any\\nPb(NO3)2…' (no M-rows) still a fragment",
      X._mp_only_fragments(part_of("2021-06", "1C", "10(c)(i)")["mark_points"], 1) is True)
check("F113-served 2(a) 'ALLOW black…' still a fragment (its answer IS the drawing)",
      X._mp_only_fragments(part_of("2019-06", "2C", "2(a)")["mark_points"], 2) is True)
check("F113-served 6(d)(ii) 'IGNORE bond angles…' still a fragment",
      X._mp_only_fragments(part_of("2019-06", "2C", "6(d)(ii)")["mark_points"], 2) is True)
check("8(c)(ii) 'IGNORE greenhouse…' still a fragment",
      X._mp_only_fragments(part_of("2021-01", "1CR", "8(c)(ii)")["mark_points"], 1) is True)
check("F113-served 7(c)(ii) 'REJECT -OH…' still a fragment",
      X._mp_only_fragments(part_of("2023-06", "2CR", "7(c)(ii)")["mark_points"], 3) is True)
p8a = part_of("2020-01", "1CR", "8(a)")
check("class-4 8(a) (scores arm, text HAS M-rows) still a fragment — the disclosed residual keeps",
      X._mp_only_fragments(p8a["mark_points"], p8a["marks"]) is True,
      "the guard is ALLOW-scoped; F113 receipt class 4 membership unchanged")
p6a = part_of("2022-01", "1C", "6(a)")
check("class-4 6(a) 'Any three from:\\nM1…' (scores arm) still a fragment",
      X._mp_only_fragments(p6a["mark_points"], p6a["marks"]) is True)
HIST = [  # the standing fragment shapes, each with its law-exact expectation
    ({"text_md": "If M1"}, True),            # the If-M arm (marks-dependency fragment)
    ({"text_md": "max 1 mark"}, True),        # the max-mark arm
    ({"text_md": "dep on M1 and M2"}, True),  # the dep arm (carries its own wildcard)
    ({"text_md": "ALLOW M1×2.5"}, True),      # inline M-ref, no M-row — the ALLOW arm
    ({"text_md": "ALLOW ORA"}, True),
    ({"text_md": "2"}, True),                  # bare marks-digit leak (marks=2)
    # the If-M arm has NO trailing wildcard (law semantics, unchanged by F118):
    # a multi-line If-M text with content after the marker is NOT a fragment
    ({"text_md": "If M1 and M2 not fully\nachieved max 1 mark"}, False),
]
check("standing fragment shapes fire; non-fragment shapes re-emit (law-exact)",
      all(X._mp_only_fragments([h], 2) is exp for h, exp in HIST))
check("the F95-founding 2-MP shape ('If M1' + 'max 1 mark' as separate MPs) still flags",
      X._mp_only_fragments([{"text_md": "If M1"}, {"text_md": "max 1 mark"}], 2) is True)
check("inline-M ALLOW text without M-rows still a fragment ('ALLOW M1×2.5')",
      X._mp_only_fragments([{"text_md": "ALLOW M1×2.5"}], 2) is True)
check("a bare token that is NOT the part's marks still re-emits (2021-06 1C 2(b)(ii) '25' law)",
      X._mp_only_fragments([{"text_md": "25"}], 1) is False)
check("F108 answer-grid exemption unchanged ('| ' table text)",
      X._mp_only_fragments([{"text_md": "| Answer | Notes |\n| M1 x | scores 0 |"}], 2) is False)
check("empty MP text still flags",
      X._mp_only_fragments([{"text_md": ""}], 2) is True)
check("M-row guard needs a LINE-START M-marker (inline 'see M1' never releases)",
      X._mp_only_fragments([{"text_md": "ALLOW guidance see M1 and M2 for the marks"}], 2) is True)

# ---- 4. corpus-wide census with the live code (the A/B of record) --------------
hits = []
slices = sorted(p for p in CORP.iterdir() if p.is_dir() and len(p.name) == 7 and p.name[4] == "-")
for sl in slices:
    for pd in sorted(sl.iterdir()):
        if not (pd / "topic.json").exists():
            continue
        t = json.loads((pd / "topic.json").read_text())
        for q in t["questions"]:
            parts = list(q.get("parts") or [])
            groups = q.get("groups")
            if isinstance(groups, dict):
                for g in groups.values():
                    if isinstance(g, dict) and isinstance(g.get("parts"), list):
                        parts += g["parts"]
            for pp in parts:
                mp = pp.get("mark_points") or []
                if not mp or not (pp.get("marks") or 0) > 0:
                    continue
                if X._mp_only_fragments(mp, pp.get("marks")):
                    hits.append(f"{sl.name}/{pd.name}:{pp['part_number']}")
check("census: exactly 18 fragment-shape hits corpus-wide (19 -> 18, the A/B of record)",
      len(hits) == 18, f"got {len(hits)}")
check("census: the sole exit is 2025-11/4CH1-1C:5(c)",
      "2025-11/4CH1-1C:5(c)" not in hits)
served_keeps = ("2019-06/4CH1-2C:2(a)" in hits and "2019-06/4CH1-2C:6(d)(ii)" in hits
                and "2022-01/4CH1-2C:7(a)(i)" in hits and "2023-01/4CH1-2C:6(a)(i)" in hits
                and "2023-06/4CH1-2CR:7(c)(ii)" in hits and "2024-11/4CH1-2C:7(a)(ii)" in hits)
check("census: the F113-served drawing answers keep their flags",
      served_keeps, "6 of the 7 served keys remain flagged (2026-06 2C 5(a) exited at its own serving)")
class4_keeps = ("2020-01/4CH1-1CR:8(a)" in hits and "2022-01/4CH1-1C:6(a)" in hits
                and "2024-06/4CH1-2CR:7(b)(i)" in hits and "2026-06/4CH1-1C:8(b)(i)" in hits)
check("census: the disclosed class-4 residual keeps its flags", class4_keeps)

# ---- 5. F97-site blast radius ---------------------------------------------------
flips = []
for sl in slices:
    for pd in sorted(sl.iterdir()):
        if not (pd / "topic.json").exists():
            continue
        t = json.loads((pd / "topic.json").read_text())
        for q in t["questions"]:
            for pp in (q.get("parts") or []):
                mp = pp.get("mark_points") or []
                if (not (pp.get("solution_md") or "").strip() and (pp.get("marks") or 0) > 0
                        and mp and all((m.get("text_md") or "").strip() for m in mp)):
                    flips.append(f"{sl.name}/{pd.name}:{pp['part_number']}")
check("F97 site: zero empty-solution parts corpus-wide (no emission can change)",
      not flips, "; ".join(flips[:4]))

check("16 series / 54 slices scanned", len(slices) == 16
      and sum(1 for sl in slices for d in sl.iterdir() if (d / "topic.json").exists()) == 54,
      f"{len(slices)} series")

print()
if fails:
    print(f"F118 UNIT BATTERY: {len(fails)} FAIL")
    sys.exit(1)
print("F118 UNIT BATTERY: all checks PASS")
