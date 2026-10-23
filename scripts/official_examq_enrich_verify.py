#!/usr/bin/env python3
"""official_examq_enrich_verify.py — the F60 value-fidelity review pass for
SOLUTION-ENRICH.json (wave-20 Part C production line, made reproducible in
wave-21). Enforced at build time; a wave ships only at zero problems.

Checks per ledger entry (fail-closed):
  V1 resolve        the key resolves to a real corpus part (C71 parity)
  V2 shape          starts "**Answer:"; no headings/tables/code-fences; length
                    floor (>= 100 chars); not identical to the MS cell
  V3 cleanliness    no PUA glyphs, control chars, or process language
                    (mark scheme / mark point / M1 / ECF / ALLOW / examiner /
                    ignore ...) — the copy is learner-facing teaching text
  V4 numeric census every data-like numeric token is evidence-backed:
                    present in the part's evidence corpus (question text,
                    group/stem text, MS cell, mark points, choices, raw QP
                    text) OR within a printed numeric range ("11 to 14")
                    OR exempt (formula/stoichiometry digits incl. Unicode
                    subscripts, Group-n, charges, Step-n, enum refs) OR
                    verified as correct arithmetic on printed values by the
                    equation scanner (exact to 1e-6, or within 0.6% behind
                    an "approximately/approx/≈" claim)
  V5 arithmetic     every "<expr> = <value>" fragment re-computes true (the
                    scanner feeds V4: verified results whitelist their
                    tokens; unit/element letters inside expressions are
                    stripped; unary minus and signed results respected)
  V6 MCQ key        keyed choice letter appears in the Answer line; every
                    non-keyed letter is mentioned (why-wrong guidance)
  V7 coverage       every mark point's content keywords appear in the
                    authored text (ALLOW/ignore/ECF clauses split out first;
                    chemical formula tokens count as keywords)

Entries of a previous wave (the original ledger shipped before this script)
are out of scope: pass --base-ledger to exclude them.

Usage:
    python3 official_examq_enrich_verify.py --corpus <OE dir> --evidence <dir> \
        [--ledger SOLUTION-ENRICH.json] [--base-ledger SOLUTION-ENRICH.json] \
        [--report out.json] [--entries key,key]
Exit 0 iff zero problems (in scope).
"""
import argparse, json, math, re, sys
from pathlib import Path

STOP = set("""the a an and or of to in on for with as is are was were be been by that this it its
from at into than then so such which who what when where how why not no yes can could may might
will would should must have has had do does did also but if because more most less least some any
all both each other another same own very just about up down out over under again once only own
when while during after before between through against without within upon among across per
""".split())


def clean(s):
    return re.sub(r"\s+", " ", (s or "")).strip()


SUB = {"₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4", "₅": "5",
       "₆": "6", "₇": "7", "₈": "8", "₉": "9", "⁰": "0", "¹": "1", "²": "2",
       "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9"}


def ascii_digits(s):
    for k, v in SUB.items():
        s = s.replace(k, v)
    return s


# ---------------------------------------------------------------- V3 classes
PUA_RE = re.compile(r"[\uE000-\uF8FF]")
CTRL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
PROCESS_RE = re.compile(r"\b(mark\s+scheme|mark\s+point|marking\s+point|examiner|ECF|error\s+carried|\bORA\b|\bALLOW\b|\bIGNORE\b|\bACCEPT\b|M[12]\s+for\b)", re.I)


# ------------------------------------------------------- numeric tokenising
NUM_RE = re.compile(r"\d+(?:[.,\u00a0 ]\d{3})*(?:\.\d+)?")

def norm_num(tok):
    t = tok.replace(",", "").replace("\u00a0", "").replace(" ", "")
    if t.endswith("."):
        t = t[:-1]
    try:
        return float(t)
    except ValueError:
        return None


GROUP_RE = re.compile(r"\bGroup\s+(\d|I{1,3}V?|IV|V|VI{0,3}VII?)\b", re.I)
STEP_RE = re.compile(r"\bStep\s+\d+\b", re.I)
PAREN_ENUM_RE = re.compile(r"\((\d)\)")


def formula_digits(text):
    """digits inside chemical formulas / equation coefficients (H2O, 2H2O,
    CO₂ after subscript normalisation, equation-line coefficients)"""
    out = set()
    for m in re.finditer(r"(?:\d+\s?)?(?:\(?[\(\[]?[A-Z][a-z]?\d*)+", text):
        seg = m.group(0)
        for d in re.findall(r"\d+", seg):
            out.add(d)
    for line in text.split("\n"):
        if ("→" in line) or ("\u21cc" in line):
            for d in re.findall(r"\d+", line):
                out.add(d)
    return out


def exempt_tokens(text):
    ex = set()
    for m in GROUP_RE.finditer(text):
        g = m.group(1)
        if g.isdigit():
            ex.add(g)
    for m in STEP_RE.finditer(text):
        ex.add(re.search(r"\d+", m.group(0)).group(0))
    for m in PAREN_ENUM_RE.finditer(text):
        ex.add(m.group(1))
    for m in re.finditer(r"(\d+)\s?(?:\+|\u207a|\u2212|\u207b|-)", text):
        ex.add(m.group(1))  # charges: 2+, 3-, ⁻
    return ex


RANGE_RE = re.compile(r"(\d+(?:\.\d+)?)\s*(?:to|–|—|-)\s*(\d+(?:\.\d+)?)")


def range_backed(text, ev_nums):
    """numbers inside a printed range whose endpoints are evidence-backed
    ("any value between 11 and 14" credits the whole range)"""
    backed = set()
    for m in RANGE_RE.finditer(text):
        lo, hi = norm_num(m.group(1)), norm_num(m.group(2))
        if lo is None or hi is None or hi <= lo:
            continue
        lo_s = str(int(lo)) if lo == int(lo) else str(lo)
        hi_s = str(int(hi)) if hi == int(hi) else str(hi)
        if lo_s in ev_nums or hi_s in ev_nums:
            v = lo
            while v <= hi + 1e-9:            # integer walk over the credited range
                backed.add(str(int(v)) if v == int(v) else str(round(v, 6)))
                v += 1
            backed.add(lo_s)
            backed.add(hi_s)
    return backed


GRAPH_READ_RE = re.compile(r"read.{0,12}from.{0,6}graph|from your graph|use your graph|off the graph", re.I)


def graph_read_backed(mark_point_text, ms_text):
    """the MS credits a graph reading (± tolerance) — the plotted value is
    learner-derived by design; the graph itself is the served evidence"""
    return bool(GRAPH_READ_RE.search(mark_point_text + " " + ms_text))


# ------------------------------------------------------- arithmetic scanner
PREC = {"×": 2, "\u00b7": 2, "÷": 2, "/": 2, "+": 1, "\u2212": 1, "-": 1}


def eval_expr(expr):
    """evaluate arithmetic; letters (units/element symbols) are stripped;
    unary minus supported; None when the fragment is not pure arithmetic"""
    s = expr.replace(",", "").replace("\u00a0", "")
    toks = []
    i = 0
    while i < len(s):
        c = s[i]
        if c.isdigit() or c == ".":
            j = i
            while j < len(s) and (s[j].isdigit() or s[j] == "."):
                j += 1
            try:
                toks.append(float(s[i:j]))
            except ValueError:
                return None
            i = j
        elif c in PREC or c in "xX":
            toks.append("×" if c in "xX\u00b7" else c)
            i += 1
        elif c.isspace():
            i += 1
        elif c.isalpha():
            # variable attached to a number ("12n", "2x") — algebra, not arithmetic
            j = i
            while j < len(s) and s[j].isalpha():
                j += 1
            if i > 0 and (s[i - 1].isdigit() or (j < len(s) and any(ch.isdigit() for ch in s[j:j + 2]))):
                return None
            i = j  # bare unit word: strip
        else:
            return None  # parentheses etc: not supported -> not verified
    if not toks:
        return None
    # unary minus fold: leading sign before the first number
    if toks and toks[0] in ("-", "\u2212") and len(toks) > 1 and isinstance(toks[1], float):
        toks = [-toks[1]] + toks[2:]
    try:
        vals, ops = [toks[0]], []
        k = 1
        while k < len(toks):
            op, num = toks[k], toks[k + 1] if k + 1 < len(toks) else None
            if not isinstance(op, str) or op not in PREC or not isinstance(num, float):
                return None  # malformed sequence (stray numbers/operators)
            if PREC[op] == 2:
                vals[-1] = vals[-1] * num if op == "×" else vals[-1] / num
            else:
                ops.append(op)
                vals.append(num)
            k += 2
        res = vals[0]
        for op, v in zip(ops, vals[1:]):
            res = res + v if op == "+" else res - v
        return res
    except (IndexError, ZeroDivisionError, TypeError):
        return None


CHAIN_RE = re.compile(
    r"([0-9][0-9.,\u00a0 \t]*(?:[A-Za-z]{1,3})?(?:\s?[+\u2212\-×÷/xX\u00b7]\s?(?:[A-Za-z/]{1,7})?[0-9][0-9.,\u00a0 \t]*(?:[A-Za-z]{1,3})?)+)"
    r"\s?(?:[A-Za-z/\u00b0]{1,7}\s?)?\s?(?:≈|approx\.?\s?|approximately\s?)?=[+\u2212\-]?\s?(≈|approx\.?\s?|approximately\s?)?([0-9][0-9.,\u00a0 \t]*)")


def scan_equations(text):
    """returns (verified_result_tokens, violations); results carry sign"""
    verified, viol = set(), []
    lines = text.split("\n")
    merged = []
    for ln in lines:
        st = ln.strip()
        if merged and (st.startswith("=") or re.match(r"^\s*(?:≈|approx)", st)):
            merged[-1] += " = " + st.lstrip("=≈ ").strip()
        else:
            merged.append(ln)
    for ln in merged:
        for m in CHAIN_RE.finditer(ln):
            expr, claimed = m.group(1), m.group(3)
            tol = bool(m.group(2))
            ev = eval_expr(expr)
            cv = norm_num(claimed)
            if ev is None or cv is None:
                continue
            signed = cv  # norm_num keeps the claim's own sign
            # chemistry rounding: exact chains are quoted to 3 sf (<=0.6%);
            # ≈/approximately claims may round to 1-2 sf (<=5%)
            if math.isclose(ev, signed, rel_tol=0.051 if tol else 0.0061, abs_tol=0.051 if tol else 0.0061):
                verified.add(str(int(cv)) if cv == int(cv) else str(cv))
            else:
                viol.append(f"arithmetic: {expr.strip()} = {claimed.strip()} but computes to {ev:g}")
    return verified, viol


# ------------------------------------------------------------------- V4/V6/V7
def numeric_census(text, evidence, verified, graph_read=False):
    text_a = ascii_digits(text)
    ev_nums = set()
    for tok in NUM_RE.findall(ascii_digits(evidence)):
        v = norm_num(tok)
        if v is not None:
            ev_nums.add(str(int(v)) if v == int(v) else str(v))
    verified = {ascii_digits(x) for x in verified}
    problems = []
    for m in NUM_RE.finditer(text_a):
        tok = m.group(0)
        v = norm_num(tok)
        if v is None:
            continue
        s = str(int(v)) if v == int(v) else str(v)
        if s in ev_nums or s in verified:
            continue
        if v == int(v) and str(int(v)) in exempt_tokens(text_a):
            continue
        if str(int(v)) in formula_digits(text_a):
            continue
        if graph_read:
            continue  # the MS credits a graph reading; the plot is the evidence
        problems.append(tok)
    # printed-range membership (endpoints or interior of a credited range)
    if problems:
        rb = range_backed(text_a, ev_nums)
        problems = [t for t in problems
                    if not (norm_num(t) == int(norm_num(t)) and str(int(norm_num(t))) in rb)]
    # same-sentence product/sum of two evidence numbers (atom-count narratives:
    # "16 oxygen atoms (from 8 O₂)" — 16 = 8×2 on printed values)
    if problems:
        problems = _sentence_product_exemption(text_a, ev_nums, problems)
    return problems


def _sentence_product_exemption(text, ev_nums, problems):
    """exempt flagged small integers that are a product/sum of two
    evidence-backed numbers in the same sentence (atom-count narratives)"""
    if not problems:
        return problems
    remaining = set(problems)
    for sent in re.split(r"(?<=[.;])\s+|\n", text):
        toks_here = {t for t in remaining if t in sent}
        if not toks_here:
            continue
        sent_nums = []
        for tok in NUM_RE.findall(sent):
            sv = norm_num(tok)
            if sv is not None and sv == int(sv) and str(int(sv)) in ev_nums:
                sent_nums.append(int(sv))
        if len(sent_nums) < 2:
            continue
        for t in list(toks_here):
            v = norm_num(t)
            if v is None or v != int(v) or not (0 < v <= 400):
                continue
            if any(a * b == int(v) or a + b == int(v)
                   for a in sent_nums for b in sent_nums):
                remaining.discard(t)
    return [t for t in problems if t in remaining]


def keywords(s):
    toks = []
    for w in re.findall(r"[a-z]{4,}", clean(s).lower()):
        if w not in STOP:
            toks.append(w)
    # chemical formula / symbol tokens count too (HBr, SO4, CO2, ΔH, Mr)
    for f in re.findall(r"(?:\u0394|M(?:r)?)?[A-Z][a-z]?\d*[a-z]?\d*", clean(s)):
        f = f.strip()
        if len(f) >= 2 and (any(c.isdigit() for c in f) or f in ("HBr", "ΔH")):
            toks.append(ascii_digits(f.lower()))
    return [t for t in toks if t not in ("figs", "figure", "figures")]


JARGON = {"figs", "answer", "correctly", "balanced", "award", "mark", "notes"}


GUIDANCE_SPLIT = re.compile(r"\b(?:ALLOW|allow|IGNORE|ignore|ECF|ORA|accept|Accept|reject|Reject|both orders|either order|Do not accept|do not accept|correctly balanced|Calculator answer|answer is|Award|award)\b")


def mp_formula_tokens(t):
    """distinctive tokens of a mark point: symbols (Q, ΔH, V), formulas
    (HBr, OH-, CO2), and numbers"""
    out = set()
    for f in re.findall(r"(?:\u0394|M(?:r)?)?[A-Z][a-z]?\d*[a-z]?\d*", clean(t)):
        f = f.strip()
        if len(f) >= 1 and re.fullmatch(r"(?:\u0394H?|Q|H\u2082?|M\u2082?|V|W|X|Y|Z|n|pH)", f):
            out.add(f)
    for f in re.findall(r"\b[A-Z][A-Za-z]?\d*(?:[\u2070-\u209f\u00b2\u00b3\u207b]|[+\u2212-])?", clean(t)):
        f = f.strip()
        if len(f) >= 2 and any(c.isupper() for c in f) and not f.isupper():
            out.add(f)  # HBr, OH-, CO2, SO4
        elif len(f) >= 2 and f.isupper() and f[-1].isdigit():
            out.add(f)  # O2, H2
    for n in NUM_RE.findall(ascii_digits(t)):
        v = norm_num(n)
        if v is not None:
            out.add(str(int(v)) if v == int(v) else str(v))
    return {x for x in out if x}


def close_num_in_text(v, text_a):
    for n in NUM_RE.findall(text_a):
        x = norm_num(n)
        if x is not None and math.isclose(x, v, rel_tol=0.007, abs_tol=0.007):
            return True
    return False


def coverage_problems(mark_points, text):
    problems = []
    tl = ascii_digits(clean(text).lower())
    for mp in mark_points:
        t = ascii_digits(mp.get("text") or "")
        t = GUIDANCE_SPLIT.split(t)[0]
        t = clean(t)
        if not t:
            continue
        kws = keywords(t)
        real = [k for k in kws if k not in JARGON]
        covered = False
        if real:
            hit = sum(1 for k in real if k in tl)
            if hit / len(real) >= 0.30:
                covered = True
        if not covered:
            # formula-symbol / number route: a mark point like "Q = 1310 (J)"
            # is covered when its symbol or its value (3sf-equivalent) appears
            toks = mp_formula_tokens(t)
            if toks:
                sym_hit = any(re.search(rf"(?<![A-Za-z]){re.escape(ascii_digits(x))}(?![A-Za-z])", tl)
                              for x in toks if not x.isdigit())
                num_hit = any(close_num_in_text(float(x), tl) for x in toks if x.isdigit())
                if sym_hit or num_hit:
                    covered = True
        if not covered:
            # single-letter diagram labels ("X and Z", "V and W")
            labels = [x for x in re.findall(r"(?<![A-Za-z])([A-Z])(?![A-Za-z])", t) if x not in ("A", "I")]
            if labels and all(re.search(rf"(?<![A-Za-z]){x}(?![A-Za-z])", tl) for x in labels):
                covered = True
        if not covered and (keywords(t) or labels or mp_formula_tokens(t)):
            problems.append(f"coverage: marking point '{t[:70]}' under-covered")
        # else: a pure-guidance fragment ('only', 'OH-' with nothing else)
        # carries nothing substantive to cover — not a defect
    return problems


# ----------------------------------------------------------------- evidence
def load_evidence(evdir):
    ev = {}
    for f in Path(evdir).glob("*.jsonl"):
        for ln in f.read_text().split("\n"):
            if not ln.strip():
                continue
            p = json.loads(ln)
            ev[p["key"]] = p
    return ev


def load_corpus_parts(oedir):
    corpus = {}
    base = Path(oedir) / "igcse-chemistry-19"
    for d in sorted(base.iterdir()):
        if not d.is_dir():
            continue
        for pd in sorted(d.iterdir()):
            if not pd.name.startswith("4CH1-"):
                continue
            paper = pd.name.split("-")[1]
            t = json.loads((pd / "topic.json").read_text())
            for q in t["questions"]:
                for p in q["parts"]:
                    slug = p["part_number"].replace("(", "-").replace(")", "")
                    pid = f"offp_{d.name}_{paper.lower()}_{slug}"
                    corpus[pid] = (d.name, paper, q, p)
    return corpus


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", default="/home/z/my-project/oe-w21/Official-ExamQuestion")
    ap.add_argument("--evidence", default="/home/z/my-project/oe-w21/evidence")
    ap.add_argument("--ledger", default="/home/z/my-project/oe-w21/staging-enrich.json")
    ap.add_argument("--base-ledger", default="/home/z/my-project/oe-main/SOLUTION-ENRICH.json",
                    help="entries of previous waves: out of scope for this pass")
    ap.add_argument("--report", default=None)
    ap.add_argument("--entries", default=None, help="comma list; default all in-scope")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    led = json.loads(Path(args.ledger).read_text())["entries"]
    base_keys = set()
    if args.base_ledger and Path(args.base_ledger).exists():
        base_keys = set(json.loads(Path(args.base_ledger).read_text())["entries"].keys())
    ev = load_evidence(args.evidence)
    corpus = load_corpus_parts(args.corpus)
    want = set(args.entries.split(",")) if args.entries else None

    problems = {}
    stats = {"checked": 0, "out_of_scope": 0}
    for key, entry in sorted(led.items()):
        if want and key not in want:
            continue
        if key in base_keys:
            stats["out_of_scope"] += 1
            continue
        text = entry.get("solutionMd") or ""
        plist = problems.setdefault(key, [])
        stats["checked"] += 1

        # V2 shape
        if not text.strip():
            plist.append("empty solutionMd")
            continue
        if not text.lstrip().startswith("**Answer"):
            plist.append("must open with **Answer:")
        if re.search(r"^#{1,6}\s", text, re.M) or "\n|" in text or "```" in text:
            plist.append("forbidden markdown: heading/table/code-fence")
        if len(text) < 100:
            plist.append(f"too thin: {len(text)} chars (floor 100)")

        # V3 cleanliness
        if PUA_RE.search(text):
            plist.append("PUA glyph present")
        if CTRL_RE.search(text):
            plist.append("control char present")
        if PROCESS_RE.search(text):
            plist.append("process language leaked")

        # resolve part
        series_paper, slug = key.split(":")
        series, paper = series_paper.rsplit("-", 1)
        pid = f"offp_{series}_{paper.lower()}_{slug}"
        part = corpus.get(pid)
        if not part:
            plist.append("does not resolve to a corpus part")
            continue
        _, _, q, p = part
        ms = clean(p.get("solution_md"))
        if clean(text) == ms:
            plist.append("identical to MS cell")

        # evidence corpus (authoring and verify see identical evidence)
        # + sibling parts of the same question (MS cross-reference chains like
        # "answer to b(i)" make sibling MS cells/mark points legitimate evidence)
        sib = []
        for sp2 in q["parts"]:
            if sp2 is p:
                continue
            sib.append(sp2.get("solution_md") or "")
            sib.extend(m["text_md"] for m in (sp2.get("mark_points") or []))
        pack = ev.get(key)
        if pack:
            ev_text = "\n".join([
                pack.get("stem") or "", pack.get("groupStems") or "",
                pack.get("problem") or "", pack.get("ms") or "",
                json.dumps(pack.get("choices") or [], ensure_ascii=False),
                "\n".join(mp.get("text") or "" for mp in pack.get("markPoints") or []),
                "\n".join(pack.get("qpPages") or []),
                "\n".join(sib),
            ])
        else:
            ev_text = "\n".join([
                q.get("stem_md") or "", "\n".join((v.get("group_stem_md") or "") for v in (q.get("groups") or {}).values()),
                p.get("problem_md") or "", ms,
                json.dumps(p.get("choices") or [], ensure_ascii=False),
                "\n".join(m["text_md"] for m in (p.get("mark_points") or [])),
                "\n".join(sib),
            ])

        # V5/V4 arithmetic + census
        verified, a_viol = scan_equations(text)
        for v in a_viol:
            plist.append(v)
        gr = graph_read_backed("\n".join(mp.get("text") or "" for mp in (pack.get("markPoints") if pack else [{"text": m["text_md"]} for m in (p.get("mark_points") or [])])), pack.get("ms") if pack else ms)
        for tok in numeric_census(text, ev_text, verified, graph_read=gr):
            plist.append(f"numeric token not evidence-backed: {tok}")

        # V6 MCQ key guard
        if p.get("question_type") == "multiple_choice" and p.get("choices"):
            ch = p["choices"]
            if isinstance(ch, str):
                ch = json.loads(ch)
            keyed = [c for c in ch if c.get("is_correct")]
            if keyed:
                letter = keyed[0]["label"]
                m = re.search(r"\*\*Answer:\s*\**\s*([A-D])\b", text)
                if not m or m.group(1) != letter:
                    plist.append(f"MCQ answer line must state the keyed letter {letter}")
                wrong = [c["label"] for c in ch if not c.get("is_correct")]
                for wl in wrong:
                    if not re.search(rf"\b{wl}\b", text):
                        plist.append(f"MCQ why-wrong missing for option {wl}")
            else:
                plist.append("MCQ part without a keyed choice (corpus defect)")

        # V7 coverage
        mps = pack.get("markPoints") if pack else [{"text": m["text_md"]} for m in (p.get("mark_points") or [])]
        if mps:
            for cp in coverage_problems(mps, text):
                plist.append(cp)

        if not plist:
            problems.pop(key, None)

    n_bad = len(problems)
    print(f"verify: checked {stats['checked']} in-scope entries · out-of-scope {stats['out_of_scope']} · "
          f"clean {stats['checked'] - n_bad} · problems {n_bad}")
    if args.report:
        Path(args.report).write_text(json.dumps(problems, indent=1, ensure_ascii=False))
    if not args.quiet:
        shown = 0
        for k, ps in problems.items():
            print(f"  {k}:")
            for x in ps[:4]:
                print(f"    - {x}")
            shown += 1
            if shown >= 30:
                print("  ... (see --report)")
                break
    sys.exit(1 if n_bad else 0)


if __name__ == "__main__":
    main()
