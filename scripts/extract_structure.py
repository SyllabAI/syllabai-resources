#!/usr/bin/env python3
"""
extract_structure.py — Pass (1) of IAL/modular unit pass: build structure.json per qualification.

Families:
  ial_science    : units via 16pt body headers 'Unit N: Title'; codes via W-code/01 lines
                   near 'Unit N:' lines in assessment summary; points assigned by page range.
  ial_maths      : units via 16pt 'Unit P1: Pure Mathematics 1' (14 units); codes via ordered
                   W-code/01 table (pages 10..18); points by page range; award combination
                   sentences captured verbatim.
  modular_science: units via 'Unit code 4WXXn/1X' blocks in Qualification-at-a-glance;
                   point assignment via content-summary topic-number prefixes (Part1/Part2).
  maths_modular  : 4 units via 14pt 'Unit N: <Tier> Tier' section headers; codes
                   'Unit N: 4WMnT/01'; points by page range; topic areas captured.
  econ_modular   : 2 units via 16pt 'Unit N: Title' + 'Unit code: 4WECn/01' lines.

All extraction is rule-derived from PDF spans; nothing guessed. Output:
  Official-Specifications/parsed/<qual>/structure.json
"""
import fitz, re, json, os, sys

BASE = "/home/z/my-project/download/syllabai-resources/Official-Specifications"
OUT = os.path.join(BASE, "parsed")

TARGETS = {
    "ial-biology":            ("ial_science",     "International-A-Level-Biology-Spec.pdf", 6),
    "ial-chemistry":          ("ial_science",     "International-A-Level-Chemistry-Spec.pdf", 6),
    "ial-physics":            ("ial_science",     "9781446957783_IAL_Physics_Iss3.pdf", 6),
    "ial-maths":              ("ial_maths",       "international-a-level-maths-spec.pdf", 14),
    "igcse-biology-modular":  ("modular_science", "international-gcse-biology-modular-specification.pdf", 2),
    "igcse-chemistry-modular":("modular_science", "international-gcse-chemistry-modular-specification.pdf", 2),
    "igcse-physics-modular":  ("modular_science", "international-gcse-physics-modular-specification.pdf", 2),
    "igcse-maths-a-modular":  ("maths_modular",   "int-gcse-mathematics-spec-a-modular.pdf", 4),
    "igcse-economics":        ("econ_modular",    "international-gcse-in-economics-modular-specification.pdf", 2),
}

WCODE = re.compile(r"^(W[A-Z]{2}\d{2}|WME\d{2}|WST\d{2})/01$")
MODCODE = re.compile(r"Unit code:?\s*\*?(4W[A-Z]{2}\d/(?:1[A-Z]|\d{2}))", re.I)
SUBJUNIT = re.compile(r"^(Biology|Chemistry|Physics) Unit (\d)$")

def lines_of(doc):
    """Yield (page0, y, size, bold, text) for every span-joined line."""
    for pno in range(len(doc)):
        for blk in doc[pno].get_text("dict")["blocks"]:
            if blk.get("type") != 0:
                continue
            for ln in blk.get("lines", []):
                spans = ln.get("spans", [])
                if not spans:
                    continue
                txt = re.sub(r"\s+", " ", " ".join(sp["text"] for sp in spans)).strip()
                if not txt:
                    continue
                s0 = spans[0]
                bold = any(("Bold" in sp.get("font", "") or "bold" in sp.get("font", "")) for sp in spans)
                yield (pno, round(s0["origin"][1], 1), round(s0["size"], 1), bold, txt)

def sentences_on_page(doc, pno):
    t = doc[pno].get_text()
    return [re.sub(r"\s+", " ", s).strip() for s in re.split(r"(?<=[.:;])\n", t) if s.strip()]

# ---------- unit header detection per family ----------

def find_first_appendix_page(doc):
    """First page carrying an 'Appendix N:' section header — content units end before it."""
    pat = re.compile(r"^Appendix \d+", re.I)
    for (pg, y, sz, bold, txt) in lines_of(doc):
        if pat.match(txt) and (sz >= 14 or bold):
            return pg + 1
    return None

def find_units_ial(doc, pat):
    hdr = re.compile(pat)
    out = []
    for (pg, y, sz, bold, txt) in lines_of(doc):
        if sz >= 15 and bold:
            m = hdr.match(txt)
            if m:
                out.append({"page": pg + 1, "label": m.group(1), "title": m.group(2).strip()})
    # keep first occurrence per label (body headers repeat nowhere; TOC is 12pt)
    seen, uniq = set(), []
    for u in out:
        if u["label"] not in seen:
            seen.add(u["label"]); uniq.append(u)
    return uniq

def find_codes_ial_science(doc):
    unit_lines, code_lines = [], []
    for (pg, y, sz, bold, txt) in lines_of(doc):
        if pg > 20:
            continue
        m = re.match(r"^Unit (\d): ", txt)
        if m and sz <= 13:
            unit_lines.append((pg, y, int(m.group(1))))
        if WCODE.match(txt):
            code_lines.append((pg, y, txt.split("/")[0]))
    pairs = {}
    for (cpg, cy, code) in code_lines:
        best, bd = None, 1e9
        for (upg, uy, n) in unit_lines:
            d = abs(upg - cpg) * 1000 + abs(uy - cy)
            if d < bd:
                bd, best = d, n
        if best is not None and bd < 1500:
            pairs[best] = code
    return pairs

def find_codes_ial_maths(doc):
    codes = []
    for (pg, y, sz, bold, txt) in lines_of(doc):
        if 9 <= pg <= 18 and WCODE.match(txt):
            codes.append(txt.split("/")[0])
    return codes

def pair_codes_with_titles(doc, title_pat, max_pg, y_window=60):
    """For each 'Unit code: 4WXXn/..' line, find the unit title line on the same page
    within y_window above (or same baseline). Returns list of unit block dicts sorted by
    (pg, y): the block start IS the canonical at-a-glance header of that unit."""
    tlines, clines = [], []
    for (pg, y, sz, bold, txt) in lines_of(doc):
        if pg >= max_pg:
            continue
        m = title_pat.match(txt)
        if m:
            tlines.append((pg, y, m))
        cm = MODCODE.search(txt)
        if cm:
            clines.append((pg, y, cm.group(1).rstrip("*")))
    units = []
    for (cpg, cy, code) in clines:
        best, bd = None, 1e9
        for (tpg, ty, m) in tlines:
            if tpg != cpg or ty > cy + 2:
                continue
            d = cy - ty
            if d < bd:
                bd, best = d, (tpg, ty, m)
        if best and bd <= y_window:
            m = best[2]
            gd = m.groups()
            if gd[0].isdigit():
                u = {"no": int(gd[0]), "block_pg": cpg, "block_y": best[1], "code": code,
                     "title": gd[1].strip() if len(gd) > 1 else None}
            else:
                # subject-first pattern: (Subject, UnitNo)
                u = {"no": int(gd[1]), "subject": gd[0],
                     "title": f"{gd[0]} Unit {gd[1]}",
                     "block_pg": cpg, "block_y": best[1], "code": code}
            units.append(u)
    # one block per unit no: keep first
    seen, uniq = set(), []
    for u in units:
        if u["no"] not in seen:
            seen.add(u["no"]); uniq.append(u)
    uniq.sort(key=lambda u: (u["block_pg"], u["block_y"]))
    return uniq

def find_modular_science_units(doc):
    return pair_codes_with_titles(doc, SUBJUNIT, max_pg=60)

def find_econ_units(doc):
    pat = re.compile(r"^Unit (\d): (.+)$")
    blocks = pair_codes_with_titles(doc, pat, max_pg=15)
    if not blocks:
        return []
    # attach 16pt body headers as page_start
    out = []
    for (pg, y, sz, bold, txt) in lines_of(doc):
        if sz >= 15 and bold:
            m = pat.match(txt)
            if m:
                out.append((pg, int(m.group(1)), m.group(2).strip()))
    for b in blocks:
        b["page_start"] = next((p + 1 for (p, no, t) in out if no == b["no"]), None)
        b["body_title"] = next((t for (p, no, t) in out if no == b["no"]), None)
    seen, uniq = set(), []
    for b in blocks:
        if b["no"] not in seen:
            seen.add(b["no"]); uniq.append(b)
    return uniq

def content_prefixes_for_unit(doc, unit, next_unit):
    """Collect 'N.' topic numbers listed under the unit's Content summary."""
    start_pg, start_y = unit["block_pg"], unit["block_y"]
    if next_unit:
        end_pg, end_y = next_unit["block_pg"], next_unit["block_y"]
    else:
        end_pg, end_y = start_pg + 3, 0
    nums = []
    for (pg, y, sz, bold, txt) in lines_of(doc):
        if start_pg <= pg <= end_pg:
            if pg == start_pg and y < start_y - 2:
                continue
            if next_unit and pg == end_pg and y >= end_y:
                continue
            if pg > start_pg + 3:
                continue
            m = re.match(r"^(\d+)\.\s+[A-Z]", txt)
            if m and "Unit code" not in txt:
                nums.append(int(m.group(1)))
    # only keep the contiguous numbered topic list (>= 2 entries)
    return sorted(set(nums)) if len(set(nums)) >= 2 else []

def find_maths_modular_units(doc):
    hdr = re.compile(r"^Unit (\d): (Foundation|Higher) Tier$")
    # group lines per page for TOC rejection (TOC entries are followed by a bare page number)
    per_page = {}
    for (pg, y, sz, bold, txt) in lines_of(doc):
        per_page.setdefault(pg, []).append((y, sz, bold, txt))
    out = []
    for pg in sorted(per_page):
        rows = sorted(per_page[pg], key=lambda r: r[0])
        for i, (y, sz, bold, txt) in enumerate(rows):
            if sz >= 13.5 and bold and pg > 13:
                m = hdr.match(txt)
                if not m:
                    continue
                # reject TOC form: next line on same page within 25pt is a bare page number
                if i + 1 < len(rows) and rows[i + 1][0] - y <= 25 and re.match(r"^\d+$", rows[i + 1][3]):
                    continue
                out.append({"page": pg + 1, "no": int(m.group(1)), "tier": m.group(2), "_ord": (pg, y)})
    # keep LAST occurrence per (no, tier) = body section header; enforce order U1F<U1H<U2F<U2H
    last = {}
    for u in out:
        last[(u["no"], u["tier"])] = u
    uniq = sorted(last.values(), key=lambda u: u["_ord"])
    for u in uniq:
        del u["_ord"]
    return uniq

def find_maths_modular_codes(doc):
    pairs = {}
    for (pg, y, sz, bold, txt) in lines_of(doc):
        m = re.match(r"^Unit (\d): (4WM[12][FH])/01$", txt)
        if m and pg <= 14:
            pairs.setdefault(int(m.group(1)), []).append(m.group(2))
    return pairs  # no -> [F, H] codes

def capture_award_sentences(doc, family):
    notes = []
    pats = [
        re.compile(r"mandatory units", re.I),
        re.compile(r"cashed? in", re.I),
        re.compile(r"\ball six units\b", re.I),
        re.compile(r"\b(P1, P2, P3 and P4)\b", re.I),
        re.compile(r"\b(P[1-4]|FP[1-3]|[MS][1-3]|D1)\s*(,| and | or | with )\s*(P[1-4]|FP[1-3]|[MS][1-3]|D1)\b"),
    ]
    seen = set()
    scan_pages = range(3, min(24, len(doc)))
    for pno in scan_pages:
        flat = re.sub(r"\s+", " ", doc[pno].get_text())
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", flat):
            s = s.strip()
            if not (30 < len(s) < 400):
                continue
            for p in pats:
                if p.search(s):
                    key = s[:120]
                    if key not in seen:
                        seen.add(key)
                        notes.append({"text": s, "page": pno + 1})
                    break
    # line-level scan: award rules often live in tables without sentence punctuation
    for (pg, y, sz, bold, txt) in lines_of(doc):
        if pg >= 24 or len(txt) > 130:
            continue
        if pats[2].search(txt) or pats[3].search(txt) or pats[4].search(txt):
            key = txt[:120]
            if key not in seen:
                seen.add(key)
                notes.append({"text": txt, "page": pg + 1, "form": "table_line"})
    return notes[:14]

# ---------- main per-qual ----------

def process(qual, family, pdf, expected):
    doc = fitz.open(os.path.join(BASE, qual, pdf))
    sha1 = json.load(open(os.path.join(BASE, qual, "spec.json")))["sha1"]
    sp = json.load(open(os.path.join(OUT, qual, "spec_points.json")))
    points = sp["spec_points"]
    gaps = []

    units, assign, prefix_map = [], {}, {}

    if family in ("ial_science", "ial_maths"):
        pat = r"^Unit (\d): (.+)$" if family == "ial_science" else r"^Unit ([A-Z]+\d+): (.+)$"
        units = find_units_ial(doc, pat)
        units.sort(key=lambda u: u["page"])
        cap = find_first_appendix_page(doc)
        for i, u in enumerate(units):
            u["page_end"] = units[i + 1]["page"] - 1 if i + 1 < len(units) else (cap - 1 if cap else len(doc))
        if cap:
            print(f"    content capped before appendix page {cap}")
        if family == "ial_science":
            cmap = find_codes_ial_science(doc)
            for u in units:
                u["code"] = cmap.get(int(u["label"]))
        else:
            codes = find_codes_ial_maths(doc)
            for u, c in zip(units, codes):
                u["code"] = c
        for p in points:
            pg = p["provenance"]["page"]
            host = next((u for u in units if u["page"] <= pg <= u["page_end"]), None)
            if host:
                assign[p["id"]] = host["label"]
            elif cap and pg >= cap:
                gaps.append({"id": p["id"], "reason": f"page {pg} in appendix/notation region (parse defect: non-spec content captured as points)"})
            else:
                gaps.append({"id": p["id"], "reason": f"page {pg} outside unit ranges"})

    elif family == "modular_science":
        units = find_modular_science_units(doc)
        for u in units:
            u["page_start"] = u["block_pg"] + 1
        claimed = set()
        overlaps_dropped = []
        for i, u in enumerate(units):
            nxt = units[i + 1] if i + 1 < len(units) else None
            u["content_topic_prefixes"] = content_prefixes_for_unit(doc, u, nxt)
            clean = []
            for n in u["content_topic_prefixes"]:
                if n in claimed:
                    overlaps_dropped.append({"unit": u["no"], "prefix": n})
                else:
                    claimed.add(n); clean.append(n)
            u["content_topic_prefixes"] = clean
            for n in clean:
                prefix_map[n] = u["no"]
        for p in points:
            code = p.get("official_code")
            if code is None:
                gaps.append({"id": p["id"], "reason": "no official_code"}); continue
            top = str(code).split(".")[0]
            if not top.isdigit():
                gaps.append({"id": p["id"], "reason": f"non-numeric prefix {top}"}); continue
            n = int(top)
            if n in prefix_map:
                assign[p["id"]] = f"Unit {prefix_map[n]}"
            else:
                gaps.append({"id": p["id"], "reason": f"prefix {n} not in any unit content list"})

    elif family == "maths_modular":
        units = find_maths_modular_units(doc)
        units.sort(key=lambda u: u["page"])
        for i, u in enumerate(units):
            u["page_start"] = u["page"]
            u["page_end"] = units[i + 1]["page"] - 1 if i + 1 < len(units) else len(doc)
        cmap = find_maths_modular_codes(doc)
        for u in units:
            cl = cmap.get(u["no"], [])
            u["code"] = cl[0] if u["tier"] == "Foundation" else (cl[1] if len(cl) > 1 else None)
        content_pages = [p["provenance"]["page"] for p in points
                         if units[0]["page_start"] <= p["provenance"]["page"] <= units[-1]["page_end"]]
        parse_gap_note = None
        if not content_pages:
            parse_gap_note = (
                "PARSE GAP: no captured spec points fall inside the unit content page ranges "
                f"({units[0]['page_start']}..{units[-1]['page_end']}). The real unit content (coded rows "
                "like '1.8 Degree of accuracy' with A/B/C statements) was not captured by the original "
                "parse; captured points come from non-content sections (aims, calculators, progression). "
                "Requires parser repair (T-PARSE-FIX) before per-point mapping for this qualification.")
            gaps.append({"id": "*structure_parse_gap*", "reason": parse_gap_note})
        for p in points:
            pg = p["provenance"]["page"]
            host = next((u for u in units if u["page_start"] <= pg <= u["page_end"]), None)
            if host:
                assign[p["id"]] = f"Unit {host['no']} {host['tier']}"
            else:
                gaps.append({"id": p["id"], "reason": f"page {pg} outside unit ranges"})

    elif family == "econ_modular":
        units = find_econ_units(doc)
        units.sort(key=lambda u: u["page_start"] or 0)
        for i, u in enumerate(units):
            u["page_end"] = (units[i + 1]["page_start"] - 1 if i + 1 < len(units) and units[i + 1]["page_start"]
                             else len(doc))
        for p in points:
            pg = p["provenance"]["page"]
            host = next((u for u in units if u.get("page_start") and u["page_start"] <= pg <= u["page_end"]), None)
            if host:
                assign[p["id"]] = f"Unit {host['no']}"
            else:
                gaps.append({"id": p["id"], "reason": f"page {pg} outside unit ranges"})

    award = capture_award_sentences(doc, family)
    doc.close()

    n_units_ok = len(units) == expected
    per_unit = {}
    for pid, lab in assign.items():
        per_unit[lab] = per_unit.get(lab, 0) + 1
    front_gaps = [g for g in gaps if "outside unit ranges" in g["reason"]]
    overlaps_dropped = locals().get("overlaps_dropped", [])
    struct = {
        "schema": "syllabai.spec-structure/1.0",
        "id": qual,
        "family": family,
        "source": {"pdf": pdf, "pdf_sha1": sha1},
        "units": [
            {k: v for k, v in u.items() if k not in ("block_pg", "block_y", "code_pg", "page_end", "page")}
            | {"page_start": u.get("page") or u.get("block_pg")}
            for u in units
        ],
        "spec_point_units": assign,
        "points_per_unit": per_unit,
        "award_sentences": award,
        "validation": {
            "units_found": len(units),
            "units_expected": expected,
            "units_ok": n_units_ok,
            "points_assigned": len(assign),
            "points_total": len(points),
            "gaps": gaps[:40],
            "gap_count": len(gaps),
            "front_matter_gap_ids": [g["id"] for g in front_gaps],
            "prefix_overlaps_dropped": overlaps_dropped,
        },
    }
    with open(os.path.join(OUT, qual, "structure.json"), "w") as f:
        json.dump(struct, f, indent=1, ensure_ascii=False)

    print(f"[{qual}] family={family} units={len(units)}/{expected} "
          f"assigned={len(assign)}/{len(points)} gaps={len(gaps)} award_notes={len(award)}")
    print("    per_unit:", per_unit)
    for u in units:
        print("   ", u.get("label") or f"Unit {u.get('no')}", "|", u.get("code"), "|",
              (u.get("title") or u.get("tier") or "")[:60], "| pg", u.get("page_start") or u.get("block_pg"),
              ("| prefixes " + str(u.get("content_topic_prefixes"))) if u.get("content_topic_prefixes") else "")
    if gaps:
        print("    GAP SAMPLE:", gaps[:3])
    hard = [g for g in gaps
            if "outside unit ranges" not in g["reason"]
            and "appendix/notation region" not in g["reason"]
            and g.get("id") != "*structure_parse_gap*"]
    return n_units_ok and len(hard) == 0

def main():
    ok_all = True
    for qual, (family, pdf, expected) in TARGETS.items():
        ok_all &= process(qual, family, pdf, expected)
    print("\nALL_OK" if ok_all else "\nSOME_GATES_FAILED (see gap samples above)")

if __name__ == "__main__":
    main()
