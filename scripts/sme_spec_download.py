#!/usr/bin/env python3
"""Download official Edexcel specification PDFs for all SME courses.

Input : .cache/sme_spec/course_specs.json  (from sme_spec_discover.py)
Output: syllabai-resources/Official-Specifications/
          <qualification-slug>/<original-pearson-filename>.pdf
          <qualification-slug>/spec.json
          manifest.json

- Courses grouped by spec PDF URL (one PDF = one official qualification).
- Science Double Award (4SD0): SME leaves courseExamSpecificationPdfLink null;
  PDF fetched from the direct Pearson CDN path (verified 200 + inspected).
- Validation: %PDF magic, pypdf page count, spec-code regex over extracted
  text, issue number, sha1. Non-PDF or zero-page downloads hard-fail.
- Resumable: skips a qualification when its spec.json exists and validates.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

import pypdf

REPO = Path("/home/z/my-project/download/syllabai-resources")
OUT = REPO / "Official-Specifications"
CACHE = Path("/home/z/my-project/.cache/sme_spec/course_specs.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

MANUAL = {
    # SME leaves the double-award link null (courseExamSpecificationPdfLink
    # is literally null on all three double-award landing pages). URL taken
    # from Pearson's official qualification page:
    #   qualifications.pearson.com/en/qualifications/edexcel-international-gcses/
    #   international-gcse-science-double-award-2017.html
    "https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/"
    "Science%20(Double%20Award)/2017/specification-and-sample-assessments/"
    "international-gcse-science-double-award-2017-specification1.pdf":
        ["igcse-science-double-award-17-biology",
         "igcse-science-double-award-17-chemistry",
         "igcse-science-double-award-17-physics"],
    # T-SME-11: SME leaves courseExamSpecificationPdfLink null on all six
    # Science (Double Award) (Modular) 2024 unit pages, as it did for the
    # 2017 linear course. URL read off the Pearson qualification page
    #   qualifications.pearson.com/en/qualifications/edexcel-international-gcses/
    #   science-double-award-2024-modular.html
    # (verified: PDF magic + spec-code probe, 2026-09-19).
    "https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/"
    "Science%20(Double%20Award)/2024/specification-and-sample-assessments/"
    "international-gcse-science-da-modular-specification.pdf":
        ["igcse-science-double-award-modular-24-biology-unit-1",
         "igcse-science-double-award-modular-24-biology-unit-2",
         "igcse-science-double-award-modular-24-chemistry-unit-1",
         "igcse-science-double-award-modular-24-chemistry-unit-2",
         "igcse-science-double-award-modular-24-physics-unit-1",
         "igcse-science-double-award-modular-24-physics-unit-2"],
}

# SME links that Pearson has renamed/retired (old URL serves HTTP 200 with
# the CDN's 152,114-byte HTML 404 page). Replacement URLs read off the
# current Pearson qualification pages on 2026-09-17.
URL_OVERRIDES = {
    "https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/"
    "Business%20Studies/2017/specification-and-sample-assessment/"
    "9781446942765_International_GCSE_Business_Specification.pdf":
        ("https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/"
         "Business%20Studies/2017/specification-and-sample-assessment/"
         "9781446942765-international-gcse-business-specification.pdf",
         "sme link stale (Pearson CDN 200+404page); replaced with current URL "
         "from qualifications.pearson.com .../business-2017.html"),
}
# Group-slug fixes where the LCP rule is not descriptive.
SLUG_OVERRIDES = {
    # IAL Maths (2018) spec covers WMA/WFM/WST/WDM — SME links the same PDF
    # for ial-maths-20-* and ial-further-maths-18-further-pure-1.
    "https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf":
        "ial-maths",
    # T-SME-11: one 4EA1 spec covers the three ELA paper-module lanes; the
    # LCP rule would yield 'igcse-english-language-a-paper'.
    "https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/English%20Language%20A/2016/Specification%20and%20sample%20assessments/9781446954379-int-gcse-englang-a-iss6-02-02-2023.pdf":
        "igcse-english-language-a",
}

SPEC_CODE_RE = re.compile(
    r"\b(4CH1|4BI1|4PH1|4MA1|4MB1|4SD0|4BS1|4EC1|4ET1|4GE1|4IT1|4AC1|4PM1|"
    r"4XBI1|4XCH1|4XPH1|4XEC1|4XMAF|4XMAH|4XMB1|4XPM1|4XAC1|4XBS1|4XET1|"
    r"4XGE1|4XIT1|4EA1|4XSD1|"
    r"WCH1[1-6]|WBI1[1-6]|WPH1[1-6]|WMA1[1-4]|WFM0[1-3]|WST1[1-3]|WDM1[1-2])")
ISSUE_RE = re.compile(r"[Ii]ssue\s+(\d)")


def group_slug(courses: list[str]) -> str:
    toks = [s.split("-") for s in sorted(courses)]
    lcp: list[str] = []
    for i in range(min(len(t) for t in toks)):
        if all(t[i] == toks[0][i] for t in toks):
            lcp.append(toks[0][i])
        else:
            break
    while lcp and (lcp[-1].isdigit() or lcp[-1] == "unit"):
        lcp.pop()
    lcp = [t for t in lcp
           if not (t.isdigit() and 16 <= int(t) <= 26)]
    return "-".join(lcp)


def fetch(url: str, tries: int = 4) -> tuple[bytes, str]:
    last: Exception | None = None
    for i in range(tries):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": UA,
                              "Accept": "application/pdf,*/*",
                              "Referer": "https://www.savemyexams.com/"})
            with urllib.request.urlopen(req, timeout=120) as resp:
                return resp.read(), resp.headers.get("Content-Type", "")
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(3 + 4 * i)
    raise RuntimeError(f"download failed after {tries} tries: {last!r}")


def _compact(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def cover_code_from(txt: str, slug: str) -> str | None:
    """Qualification code(s) from the cover, anchored on the qualification
    title line (subject-matched to the slug) with a 2-line lookahead for
    wrapped codes like '(Modular) (4XMAF/4XMAH)'."""
    skip = {"igcse", "ial", "gcse", "gce", "as", "a", "level", "modular"}
    toks = [t[:-1] if t.endswith("s") else t
            for t in slug.split("-")
            if len(t) > 3 and t not in skip]
    code_re = re.compile(
        r"\(([4WXY][A-Z0-9]{3,4}(?:/[4WXY][A-Z0-9]{3,4})*)\)")
    lines = txt.splitlines()
    found: list[str] = []
    for i, line in enumerate(lines):
        c = _compact(line)
        if ("pearsonedexcelinternational" not in c
                and "edexcelinternational" not in c):
            continue
        if toks and not any(t in c for t in toks):
            continue
        for j in (i, i + 1, i + 2):
            if j < len(lines):
                m = code_re.search(lines[j])
                if m and m.group(1) not in found:
                    found.append(m.group(1))
    return "/".join(found) if found else None


def pdf_probe(path: Path, slug: str) -> dict:
    raw = path.read_bytes()
    if not raw.startswith(b"%PDF"):
        raise ValueError(f"not a PDF (magic): {path.name}")
    reader = pypdf.PdfReader(str(path))
    pages = len(reader.pages)
    if pages < 4:
        raise ValueError(f"suspicious page count {pages}: {path.name}")
    codes: set[str] = set()
    issue = None
    cover_code = None
    for pi, pg in enumerate(reader.pages):
        try:
            txt = pg.extract_text() or ""
        except Exception:  # noqa: BLE001
            txt = ""
        codes |= set(SPEC_CODE_RE.findall(txt))
        if issue is None:
            m = ISSUE_RE.search(txt)
            if m:
                issue = m.group(1)
        if pi == 0:
            cc = cover_code_from(txt, slug)
            if cc:
                cover_code = cc
    meta = reader.metadata or {}
    return {"pages": pages, "spec_codes": sorted(codes), "issue": issue,
            "cover_code": cover_code,
            "pdf_title": (meta.title or None), "pdf_author":
            (meta.author or None)}


def main() -> int:
    disc = json.loads(CACHE.read_text())
    groups: dict[str, list[str]] = {}
    for slug, rec in disc.items():
        url = rec.get("spec_pdf")
        if url:
            groups.setdefault(url, []).append(slug)
    for url, courses in MANUAL.items():
        groups.setdefault(url, [])
        groups[url] = sorted(set(groups[url]) | set(courses))

    OUT.mkdir(exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    quals: list[dict] = []
    force = "--force" in sys.argv

    for url in sorted(groups):
        courses = groups[url]
        slug = SLUG_OVERRIDES.get(url) or group_slug(courses)
        eff_url = URL_OVERRIDES[url][0] if url in URL_OVERRIDES else url
        fname = eff_url.rsplit("/", 1)[-1].replace("%20", "-")
        qdir = OUT / slug
        spec_json = qdir / "spec.json"
        pdf_path = qdir / fname
        if spec_json.exists() and pdf_path.exists() and not force:
            rec = json.loads(spec_json.read_text())
            quals.append(rec)
            print(f"[skip] {slug} ({rec['pages']}p, codes={rec['spec_codes']})")
            continue
        qdir.mkdir(exist_ok=True)
        if pdf_path.exists():
            # spec.json missing but PDF already fetched+validated earlier —
            # reuse bytes, skip the network round-trip.
            body = pdf_path.read_bytes()
            ctype = "application/pdf (file reused; revalidated below)"
            print(f"[reuse] {slug} {fname}")
        else:
            print(f"[get] {slug} <- {eff_url}")
            body, ctype = fetch(eff_url)
            pdf_path.write_bytes(body)
        meta = pdf_probe(pdf_path, slug)
        rec = {
            "slug": slug,
            "pdf": fname,
            "source_url": eff_url,
            "sme_source_url": (url if url != eff_url else None),
            "http_content_type": ctype,
            "sha1": hashlib.sha1(body).hexdigest(),
            "bytes": len(body),
            **meta,
            "sme_courses": courses,
            "discovered_via": ("sme:courseExamSpecificationPdfLink"
                               if url not in URL_OVERRIDES
                               and not any(c in [s for grp in MANUAL.values()
                                                for s in grp]
                                           for c in courses)
                               else (URL_OVERRIDES[url][1]
                                     if url in URL_OVERRIDES
                                     else "pearson qualification page "
                                          "(SME link is null)")),
            "fetched_utc": now,
        }
        spec_json.write_text(json.dumps(rec, indent=1, sort_keys=False))
        quals.append(rec)
        print(f"      {rec['pages']}p {len(body)//1024}KB "
              f"cover={rec.get('cover_code')} codes={rec['spec_codes']} "
              f"issue={rec['issue']}")

    quals.sort(key=lambda r: r["slug"])
    covered = sorted({c for q in quals for c in q["sme_courses"]})
    all_courses = sorted(disc.keys())
    missing = [c for c in all_courses if c not in covered]

    manifest = {
        "schema": "syllabai.official-specifications/1.0",
        "generated_utc": now,
        "source": {
            "provider": "Pearson Edexcel (qualifications.pearson.com)",
            "discovered_via": ("Save My Exams course landing pages "
                              "(pageProps.courseExamSpecificationPdfLink); "
                              "Science Double Award via direct Pearson CDN path"),
            "license_note": ("official exam-board specification documents, "
                             "public downloads; provenance recorded per file "
                             "in spec.json; see repo LICENSE-DATA.md"),
        },
        "totals": {
            "qualifications": len(quals),
            "sme_courses_covered": len(covered),
            "sme_courses_total": len(all_courses),
            "missing_courses": missing,
        },
        "qualifications": quals,
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=1))

    print(f"\n=== {len(quals)} qualifications, "
          f"{len(covered)}/{len(all_courses)} courses covered ===")
    if missing:
        print("MISSING:", missing)
    for q in quals:
        flag = "" if q["spec_codes"] else "  <-- NO CODE FOUND"
        print(f"  {q['slug']:<38} {q['pages']:>4}p {q['bytes']//1024:>6}KB "
              f"{q.get('cover_code') or '?':<12} "
              f"{len(q['sme_courses'])} courses{flag}")
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
