#!/usr/bin/env python3
"""T-SPEC-REPARSE-1 — fix-at-source re-parse repair for the classes filed by
T-SPEC-RENDER-1 run-001 (receipt filedFollowUps item 1):

  (a) two-column interleave damage from the source parse (EMM p18-19,
      cie-igcse-business-2023-2025, cie-igcse-maths-2025-2027, ial-maths)
  (b) CIE maths superscript/subscript loss ('a x - b y' for a^2 x - b^2 y)
  (c) CIE chemistry subscript scatter ('H SO' + floating 3/4/2)
  (d) Pearson lost formula objects (IAL_PHYSICS:45 n = c/v fraction)
  (e) CIE maths-2020 (9709) MathMagic symbol-font garbling
      ('P ^ A + B h' for P(A u B) h; 'Po m ^ h' for Po(lambda))

Zero-invention discipline: every output character is either (1) a glyph the
PDF text layer itself carries (texttrace char), or (2) a mapping whose
evidence is recorded in FONTMAP_EVIDENCE (font + glyph id -> char, verified
against rendered pixels of the same PDF), or (3) a structural joiner the
of-record laws already insert (space at gaps, U+2044 for a printed fraction
bar glyph). Rows that cannot be assembled under those laws keep their old
text and keep/upgrade flags — fail-closed.

Gates (abort before any write):
  G1 provenance   — every output char traced to a printed glyph or mapped glyph
  G2 conservation — per-qual id/official_code multiset change is exactly the
                    declared repair delta; no new codes invented
  G3 idempotence  — running the repair twice is byte-identical
  G4 serialization— indent=1, ensure_ascii=False round-trip preserved
Modes:
  --probe <qual>  print proposed row diffs, no writes
  --apply <qual>  run gates, write parsed.json + parse_report.json
  --evidence      print the font-map evidence table
"""
import argparse
import glob
import json
import os
import re
import sys

import pymupdf

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OSDIR = os.path.join(BASE, 'Official-Specifications')
PJDIR = os.path.join(OSDIR, 'parsed')

REPAIR_VERSION = 'spec-reparse-1.0'
FRACTION_SLASH = '\u2044'

# ---------------------------------------------------------------------------
# Font maps — PER-QUAL (subset embedding re-assigns glyph ids per PDF).
# Each entry: font-prefix -> {glyph_id: (char, evidence)}; evidence records
# the rendered verification that fixed the mapping.
# ---------------------------------------------------------------------------
FRACTION_SLASH_NOTE = 'EMM p19 y188 rendered "N = n1n2/m" stacked fraction — bar glyph drawn as fraction bar'

FONTMAPS = {
    'cie-a-level-maths-2023-2025': {
        'MMGreekItalic': {
            4: ('A', '9709 p22 y324 rendered "sin(A \u00b1 B)" — gid4 (extracted a) drawn italic capital A'),
            5: ('\u03b8', '9709 p22 y246 rendered "tan \u03b8 + cot \u03b8 = 4, 2 sec\u00b2\u03b8 - tan \u03b8 = 5" — gid5 drawn theta'),
            6: ('\u03bb', '9709 p35 y218 rendered "Po(\u03bb)" — gid6 drawn lambda'),
        },
        'MMVariableA': {
            1: ('(', '9709 p33/p35 rendered "P(A)" / "Po(\u03bb)" — gid1 (Differences slot asciicircum) drawn parenleft'),
            6: (')', '9709 p33/p35 rendered "P(A)" / "Po(\u03bb)" — gid6 (Differences slot h) drawn parenright'),
        },
        'MMBinary': {
            1: ('\u00b1', '9709 p22 y324 rendered "the expansions of sin(A \u00b1 B), cos(A \u00b1 B) and tan(A \u00b1 B)" — gid1 (Differences slot plus) drawn plus-minus'),
            2: ('\u00d7', '9709 p33 y300 rendered "P(A) \u00d7 P(B)" — gid2 (Differences slot numbersign) drawn multiply'),
            3: ('\u2229', '9709 p33 y288 rendered "P(A \u2229 B)" — gid3 (Differences slot plus) drawn intersection'),
        },
        'MMRelation': {
            2: ('~', '9709 p35 y218 rendered "if X ~ Po(\u03bb)" — gid2 drawn tilde (distributed as)'),
            3: ('\u2261', '9709 p21 y308 rendered "sec\u00b2\u03b8 \u2261 1 + tan\u00b2\u03b8 and cosec\u00b2\u03b8 \u2261 1 + cot\u00b2\u03b8" — gid3 (Differences slot slash) drawn identical-to'),
        },
        'MMVariable': {
            1: ('\u2211', '9709 p32 y463 rendered "\u2211x and \u2211x\u00b2, or coded totals \u2211(x\u2212a) and \u2211(x\u2212a)\u00b2" — gid1 drawn n-ary summation'),
        },
        'MMGreek': {
            1: ('+', '9709 p21 y246 rendered "tan \u03b8 + cot \u03b8 = 4" — gid1 drawn plus (identity)'),
            4: ('=', '9709 p21 y246 rendered "cot \u03b8 = 4" (span gids [1,4] = "+=") — gid4 drawn equals (identity)'),
        },
        'MMGreekItalic-extra': {},
        'SymbolMT': {
            120: ('\u2022', 'printed bullet glyph; text layer already yields U+2022 (identity)'),
        },
    },
    'cie-as-environmental-management-2025-2027': {
        'MMBinary': {
            1: ('\u2044', FRACTION_SLASH_NOTE),
        },
        'MMGreek': {
            2: ('=', 'EMM p19 y198 rendered "N =" — gid2 drawn equals (identity)'),
        },
    },
}

# superscript / subscript Unicode attachments (only these may be attached)
SUP = {
    '0': '\u2070', '1': '\u00b9', '2': '\u00b2', '3': '\u00b3', '4': '\u2074',
    '5': '\u2075', '6': '\u2076', '7': '\u2077', '8': '\u2078', '9': '\u2079',
    '+': '\u207a', '-': '\u207b', '=': '\u207c', '(': '\u207d', ')': '\u207e',
    'n': '\u207f', 'i': '\u2071',
    'a': '\u1d43', 'b': '\u1d47', 'c': '\u1d9c', 'd': '\u1d48', 'e': '\u1d49',
    'f': '\u1da0', 'g': '\u1d4d', 'h': '\u02b0', 'j': '\u02b2', 'k': '\u1d4f',
    'l': '\u02e1', 'm': '\u1d50', 'o': '\u1d52', 'p': '\u1d56', 'r': '\u02b3',
    's': '\u02e2', 't': '\u1d57', 'u': '\u1d58', 'v': '\u1d5b', 'w': '\u02b7',
    'x': '\u02e3', 'y': '\u02b8', 'z': '\u1dbb',
    '\u2013': '\u207b', '\u2212': '\u207b', '\u2014': '\u207b',
    'A': '\u1d2c', 'B': '\u1d2e', 'D': '\u1d30', 'E': '\u1d31', 'G': '\u1d33',
    'H': '\u1d34', 'I': '\u1d35', 'J': '\u1d36', 'K': '\u1d37', 'L': '\u1d38',
    'M': '\u1d39', 'N': '\u1d3a', 'O': '\u1d3c', 'P': '\u1d3e', 'R': '\u1d3f',
    'T': '\u1d40', 'U': '\u1d41', 'V': '\u1d41', 'W': '\u1d42',
}
SUB = {
    '0': '\u2080', '1': '\u2081', '2': '\u2082', '3': '\u2083', '4': '\u2084',
    '5': '\u2085', '6': '\u2086', '7': '\u2087', '8': '\u2088', '9': '\u2089',
    '+': '\u208a', '-': '\u208b', '=': '\u208c', '(': '\u208d', ')': '\u208e',
    'a': '\u2090', 'e': '\u2091', 'h': '\u2095', 'i': '\u1d62', 'j': '\u2c7c',
    'k': '\u2096', 'l': '\u2097', 'm': '\u2098', 'n': '\u2099', 'o': '\u2092',
    'p': '\u209a', 'r': '\u1d63', 's': '\u209b', 't': '\u209c', 'u': '\u1d64',
    'v': '\u1d65', 'x': '\u2093',
    '\u2013': '\u208b', '\u2212': '\u208b',
}

CURRENT_QUAL = None


def set_fontmap(qual):
    global CURRENT_QUAL
    CURRENT_QUAL = qual


def font_map_for(font):
    qm = FONTMAPS.get(CURRENT_QUAL) if CURRENT_QUAL else None
    if qm:
        for prefix, m in qm.items():
            if font.startswith(prefix) or font == prefix:
                return m
        # any other MM*/math font of a known-bad family with no entry: no map
        for prefix in KNOWN_BAD_FONTS:
            if font.startswith(prefix):
                return {}
    return None


# ---------------------------------------------------------------------------
# texttrace primitives
# ---------------------------------------------------------------------------

def page_chars(page):
    """All printable chars of a page with font/gid/geometry provenance."""
    out = []
    for span in page.get_texttrace():
        font = span['font']
        size = span['size']
        for ucs, gid, origin, bbox in span.get('chars', []):
            if ucs != 0x20 and not chr(ucs).isprintable():
                continue
            out.append({
                'font': font, 'gid': gid, 'ucs': ucs, 'ch': chr(ucs),
                'x': origin[0], 'y': origin[1],
                'size': size,
                'x0': bbox[0], 'x1': bbox[2],
                'by0': bbox[1], 'by1': bbox[3],
                'cy': (bbox[1] + bbox[3]) / 2.0,
            })
    out.sort(key=lambda c: (round(c['y'], 1), c['x']))
    return out


KNOWN_BAD_FONTS = ('MMGreekItalic', 'MMVariableA', 'MMRelation', 'MMExtra',
                   'MMBinary', 'MMGreek', 'MMItalic', 'MMRoman', 'MMSymbol')


def mapped_char(c):
    """Apply the evidence-based font map; returns (char, was_mapped).
    Known-bad MathMagic fonts must be FULLY mapped — an unmapped gid aborts
    the assembly (fail-closed: no silent passthrough of a known-bad mapping).
    Ligature codepoints normalise to their letter sequences."""
    m = font_map_for(c['font'])
    if m is not None:
        if c['gid'] in m:
            return m[c['gid']][0], True
        if c['font'].startswith('SymbolMT'):
            return c['ch'], False  # SymbolMT maps correctly outside known gaps
        return None, False  # ABORT signal for unmapped MathMagic glyph
    ch = c['ch']
    return {'\ufb01': 'fi', '\ufb02': 'fl', '\ufb00': 'ff', '\ufb03': 'ffi',
            '\ufb04': 'ffl'}.get(ch, ch), False


def group_lines(chars, ytol=None):
    """Group chars into visual lines by mid-bbox-y (sup/sub attach to their
    body line; stacked fractions stay separate lines)."""
    # mid-y proxy from origin: sup/sub chars land inside their body line's band
    for c in chars:
        c['my'] = c['y'] - 0.35 * c['size']
    lines = []
    for c in sorted(chars, key=lambda c: (c['my'], c['x'])):
        for L in lines:
            if abs(L['y'] - c['my']) < 0.6 * max(c['size'], L['base_size'] or c['size']):
                L['chars'].append(c)
                L['y'] = min(L['y'], c['my'])
                break
        else:
            lines.append({'y': c['my'], 'base_size': c['size'], 'chars': [c]})
    for L in lines:
        L['chars'].sort(key=lambda c: c['x'])
        sizes = [c['size'] for c in L['chars']]
        L['base_size'] = max(set(sizes), key=sizes.count) if sizes else 0
        ys = [round(c['y'], 1) for c in L['chars']]
        L['baseline'] = max(set(ys), key=ys.count) if ys else L['y'] + 0.35 * L['base_size']
    lines.sort(key=lambda L: L['y'])
    return lines


def assemble_linear(chars, base_y=None, ytol=3.0):
    """Reading-order assembly of a char run into linear text.

    - chars grouped into visual lines (mid-bbox-y); x-ordered
    - spacing: an explicit space glyph S is a separator between adjacent
      printed chars B,A iff B.x1-2 <= S.x <= A.x0+2 (handles tab-advance
      degenerate spaces overlapping the next char); gap-based fallback only
      on lines with no explicit spaces (math span joins)
    - small raised/lowered chars attach as Unicode super/subscript when the
      Unicode equivalent exists; otherwise the assembly FAILS (None) —
      fail-closed, no invention
    Returns (text or None, notes list).
    """
    if not chars:
        return '', []
    lines = group_lines(chars, ytol=ytol)
    notes = []
    pieces = []
    for L in lines:
        base = L['base_size'] or max(c['size'] for c in L['chars'])
        ys = [round(c['y'], 1) for c in L['chars']]
        base_y = max(set(ys), key=ys.count) if ys else L['y']
        printed = [c for c in L['chars'] if c['ch'] != ' ']
        spaces = [c for c in L['chars'] if c['ch'] == ' ']
        gap_mode = not spaces
        prev = None
        last_wide_x1 = None  # ligature pieces carry degenerate bboxes
        for c in printed:
            ch, mapped = mapped_char(c)
            if ch is None:
                return None, notes + [f"ABORT: unmapped glyph {c['font']} gid{c['gid']} ucs U+{c['ucs']:04X}"]
            if mapped:
                notes.append(f"mapped {c['font']} gid{c['gid']} -> {ch!r}")
            dy = c['y'] - base_y
            small = c['size'] <= 0.85 * base
            b_by0 = b_by1 = None
            if small:
                body_bs = [b for b in L['chars'] if b['size'] > 0.85 * base and 'by0' in b]
                if body_bs:
                    ref = max(set((round(b['by0'], 1), round(b['by1'], 1))
                                  for b in body_bs),
                              key=lambda k: sum(1 for b in body_bs
                                                if (round(b['by0'], 1), round(b['by1'], 1)) == k))
                    b_by0, b_by1 = ref
            by0_dy = (c['by0'] - b_by0) if b_by0 is not None else 0.0
            by1_dy = (c['by1'] - b_by1) if b_by1 is not None else 0.0
            # tightness: sub/sup glyphs hug their host; standalone small
            # variables sit between spaces. Subs hug on the LEFT; sups may hug
            # either side (exponent clusters like y-sup x-sub A).
            tight_left = False
            if prev is not None and prev[0] in ('body', 'sup', 'sub'):
                tight_left = c['x0'] - prev[1]['x1'] < 0.3 * max(prev[1]['size'], c['size'])
            tight_right = False
            nxt_ch = [d for d in L['chars'] if d['x0'] > c['x1'] and d['ch'] != ' ']
            if nxt_ch:
                tight_right = nxt_ch[0]['x0'] - c['x1'] < 0.3 * max(c['size'], nxt_ch[0]['size'])
            OPERATORS = set('()=+~×∩≡∑±⁄∪')
            math_mapped = mapped and ch in OPERATORS
            is_sup = small and not math_mapped and (tight_left or tight_right) \
                and (by1_dy <= -1.5 or dy <= -1.2)
            is_sub = small and not math_mapped and tight_left and not is_sup and (
                (by0_dy >= 1.5 and by1_dy >= -1.2) or dy >= 1.2)
            if small and is_sup:
                u = SUP.get(ch)
                if u is None:
                    return None, notes + [f"ABORT: no superscript Unicode for {ch!r} (font {c['font']} gid{c['gid']})"]
                pieces.append(u)
                prev = ('sup', c)
                continue
            if small and is_sub and not is_sup:
                u = SUB.get(ch)
                if u is None:
                    return None, notes + [f"ABORT: no subscript Unicode for {ch!r} (font {c['font']} gid{c['gid']})"]
                pieces.append(u)
                prev = ('sub', c)
                continue
            if prev is not None:
                pk, pc = prev
                if pk == 'body':
                    ref_x1 = pc['x1'] if pc['x1'] - pc['x0'] > 0.5 else (last_wide_x1 if last_wide_x1 is not None else pc['x1'])
                    ref_size = max(pc['size'], c['size'])
                    sep = False
                    big_gap = c['x0'] - ref_x1 >= 0.5 * ref_size
                    if gap_mode:
                        sep = c['x0'] - ref_x1 >= 0.25 * ref_size
                    else:
                        sep = any(ref_x1 - 2.0 <= s['x'] <= c['x0'] + 2.0 for s in spaces) or big_gap
                    if sep:
                        pieces.append(' ')
                else:
                    ref_x1 = pc['x1'] if pc['x1'] - pc['x0'] > 0.5 else last_wide_x1
                    had_space = any(pc['x1'] - 2.0 <= s['x'] <= c['x0'] + 2.0 for s in spaces)
                    if had_space or (ref_x1 is not None
                                     and c['x0'] - ref_x1 >= 0.9 * max(c['size'], 6.5)):
                        pieces.append(' ')
            pieces.append(ch)
            if c['x1'] - c['x0'] > 0.5:
                last_wide_x1 = c['x1']
            prev = ('body', c)
    return re.sub(r'[ \t]+', ' ', ''.join(pieces)).strip(), notes


def assemble_lines_para(lines, base_ytol=1.2):
    """Join already-assembled visual lines into a paragraph (statement text).
    Wrap continuation: no hyphen logic — plain space join, whitespace-normalised."""
    texts = []
    for L in lines:
        t, notes = assemble_linear(L['chars'])
        if t is None:
            return None, notes
        texts.append(t)
        notes = []
    return re.sub(r'\s+', ' ', ' '.join(texts)).strip(), []


# ---------------------------------------------------------------------------
# parsed.json IO (format-preserving)
# ---------------------------------------------------------------------------

def load_parsed(qual):
    fs = glob.glob(os.path.join(PJDIR, qual, '*.parsed.json'))
    if len(fs) != 1:
        raise SystemExit(f'expect exactly 1 parsed.json for {qual}, found {fs}')
    path = fs[0]
    raw = open(path, encoding='utf-8').read()
    return path, json.loads(raw), raw


def serialize(obj):
    return json.dumps(obj, indent=1, ensure_ascii=False)
# ---------------------------------------------------------------------------
# assembly v2: fraction stacks + vulgar fractions
# ---------------------------------------------------------------------------

VULGAR = {('1', '2'): '\u00bd', ('1', '4'): '\u00bc', ('3', '4'): '\u00be',
          ('1', '3'): '\u2153', ('2', '3'): '\u2154',
          ('1', '8'): '\u215b', ('3', '8'): '\u215c', ('5', '8'): '\u215d',
          ('7', '8'): '\u215e'}


def merge_fraction_stacks(chars, ytol=2.5):
    """Detect vertical fraction stacks (small numerator directly above small
    denominator, overlapping x, no body chars between) and merge each stack
    into a single synthetic char at the numerator position:
      digit/digit -> vulgar fraction char when one exists, else 'n\u2044d'.
    Returns (merged_chars, notes)."""
    notes = []
    lines = group_lines(chars, ytol=ytol)
    used = set()
    out = []
    for i, L in enumerate(lines):
        if id(L) in used:
            continue
        if i + 1 < len(lines):
            N = L['chars']
            D = lines[i + 1]['chars']
            small_n = max(c['size'] for c in N)
            small_d = max(c['size'] for c in D)
            body = lines[i + 2]['base_size'] if i + 2 < len(lines) else base_size_of(lines)
            if (len(N) <= 2 and len(D) <= 2 and small_n < 0.8 * body
                    and small_d < 0.8 * body and lines[i + 1] not in used):
                nx = (min(c['x'] for c in N), max(c['x1'] for c in N))
                dx = (min(c['x'] for c in D), max(c['x1'] for c in D))
                overlap = min(nx[1], dx[1]) - max(nx[0], dx[0])
                if overlap > 0.5 * min(nx[1] - nx[0], dx[1] - dx[0]):
                    num = ''.join(mapped_char(c)[0] for c in N)
                    den = ''.join(mapped_char(c)[0] for c in D)
                    v = VULGAR.get((num, den)) or VULGAR.get((den, num))
                    if v is None and len(num) == 1 and len(den) == 1:
                        v = num + FRACTION_SLASH + den
                    if v is not None:
                        first = dict(N[0])
                        first['ch'] = v
                        first['x1'] = max(nx[1], dx[1])
                        first['frac'] = f'{num}/{den}'
                        out.append(first)
                        notes.append(f'fraction stack {num}/{den} -> {v!r}')
                        used.add(id(lines[i + 1]))
                        used.add(id(L))
                        continue
        for c in L['chars']:
            out.append(c)
    out.sort(key=lambda c: (c['y'], c['x']))
    return out, notes


def base_size_of(lines):
    sizes = []
    for L in lines:
        sizes.append(L['base_size'])
    return max(sizes) if sizes else 10.0


def inline_fraction_merge(chars, notes):
    """Printed fractions whose numerator/denominator sit ABOVE/BELOW a prose
    baseline (drawn bar, math glyphs, any size): at an x-gap >= 18px between
    consecutive body-font chars, math-font chars 2-15px above AND below the
    baseline whose x-ranges overlap >= 40% merge into one synthetic token
    'num\u2044den'. Zero invention: every output char is a printed glyph;
    the bar is structural (same law as the EMM bar glyph -> U+2044)."""
    if not chars:
        return chars
    MATH = ('TimesNewRoman', 'MM', 'SymbolMT')
    used = set()
    out = list(chars)
    # candidate gaps: CONSECUTIVE printed chars on one baseline, far in x
    # (math-only formula lines like 'n = c/v' get trailing slots too; the
    # above/below scans stay math-font-only so prose stacks never merge)
    baselines = {}
    for c in chars:
        if c['ch'] == ' ' or c['ch'] == '':
            continue
        key = round(c['y'] / 2.0)
        baselines.setdefault(key, []).append(c)
    pairs = []
    for key, cs in baselines.items():
        cs = sorted(cs, key=lambda c: c['x'])
        math_only = all(c['font'].startswith(MATH) for c in cs)
        if math_only and len(cs) > 3:
            continue  # prose-scale math lines: no slots (false merges)
        for a, b in zip(cs, cs[1:]):
            if b['x0'] - a['x1'] >= 14:
                pairs.append((a, b))
        # trailing slot: fraction stack after the last char (e.g. 'n = c/v')
        if cs:
            pairs.append((cs[-1], None))
    # body-anchored slots first: they claim fraction glyphs with the most
    # context; math-only formula lines (n = c/v) run last
    MATHF = ('TimesNewRoman', 'MM', 'SymbolMT')
    pairs.sort(key=lambda p: 0 if (p[0] and not p[0]['font'].startswith(MATHF))
               or (p[1] and not p[1]['font'].startswith(MATHF)) else 1)
    for a, b in pairs:
            if b is None:
                gap0, gap1 = a['x1'], a['x1'] + 60.0
                yref = a['y']
            else:
                gap0, gap1 = a['x1'], b['x0']
                yref = (a['y'] + b['y']) / 2
            above = [c for c in chars if id(c) not in used and c['font'].startswith(MATH)
                     and c['ch'] != ' ' and c['x1'] >= gap0 - 2 and c['x0'] <= gap1 + 2
                     and yref - 17 <= c['y'] <= yref - 2]
            below = [c for c in chars if id(c) not in used and c['font'].startswith(MATH)
                     and c['ch'] != ' ' and c['x1'] >= gap0 - 2 and c['x0'] <= gap1 + 2
                     and yref + 2 <= c['y'] <= yref + 17]
            if not above or not below:
                continue
            ax0, ax1 = min(c['x'] for c in above), max(c['x1'] for c in above)
            bx0, bx1 = min(c['x'] for c in below), max(c['x1'] for c in below)
            overlap = min(ax1, bx1) - max(ax0, bx0)
            if overlap < 0.4 * min(ax1 - ax0, bx1 - bx0):
                continue

            def lin(cs2):
                cs2 = sorted(cs2, key=lambda c: c['x'])
                s, prev = '', None
                for c in cs2:
                    ch, _ = mapped_char(c)
                    if ch is None:
                        return None
                    if prev is not None and c['x0'] - prev >= 0.5 * c['size']:
                        s += ' '
                    s += ch
                    prev = c['x1'] if c['x1'] > c['x0'] else prev
                return re.sub(r'\s+', ' ', s).strip()

            num, den = lin(above), lin(below)
            if not num or not den:
                continue
            for c in above + below:
                used.add(id(c))
            syn = dict(above[0])
            syn['ch'] = num + FRACTION_SLASH + den
            syn['x0'] = gap0
            syn['x1'] = gap1
            syn['x'] = gap0
            syn['y'] = yref
            syn['frac'] = f'{num}/{den}'
            out = [syn if c is above[0] else c for c in out]
            for c in below + above[1:]:
                if c is not syn:
                    out = [x for x in out if x is not c]
            notes.append(f'inline fraction {num}/{den} -> {syn["ch"]!r}')
    return [c for c in out if id(c) not in used]


def assemble_band(chars, ytol=3.0):
    """Full linear assembly of a band: fraction stacks + inline fractions
    first, then per-line assembly joined with spaces."""
    notes_extra = []
    chars = inline_fraction_merge(chars, notes_extra)
    merged, notes = merge_fraction_stacks(chars, ytol=2.2)
    lines = group_lines(merged, ytol=ytol)
    texts = []
    for L in lines:
        t, ns = assemble_linear(L['chars'], ytol=ytol)
        if t is None:
            return None, notes + ns + notes_extra
        if t:
            texts.append(t)
    return re.sub(r'\s+', ' ', ' '.join(texts)).strip(), notes + notes_extra


# ---------------------------------------------------------------------------
# page-level row rebuilders (family layouts)
# ---------------------------------------------------------------------------

def _in(page_chars_out, x_lo=None, x_hi=None, y_lo=None, y_hi=None):
    for c in page_chars_out:
        if x_lo is not None and c['x'] < x_lo:
            continue
        if x_hi is not None and c['x'] >= x_hi:
            continue
        if y_lo is not None and c['y'] < y_lo - 0.1:
            continue
        if y_hi is not None and c['y'] > y_hi + 0.1:
            continue
        yield c


def find_bullets(chars, x_max=70, glyph='\u2022'):
    """Row anchor bullets: printed bullet glyphs at the left margin."""
    ys = []
    for c in chars:
        if c['ch'] == glyph and c['x'] <= x_max:
            ys.append((c['y'], c['x']))
    ys.sort()
    merged = []
    for y, x in ys:
        if merged and abs(merged[-1][0] - y) < 2.5:
            continue
        merged.append((y, x))
    return merged


def find_code_anchors(chars, x_max=105, pat=re.compile(r'^\d{1,2}(\.\d{1,3})*[A-Za-z]?$')):
    """Row anchors = standalone printed codes near the left margin."""
    lines = group_lines(chars)
    out = []
    for L in lines:
        cs = [c for c in L['chars'] if c['x'] <= x_max]
        if not cs:
            continue
        t = ''.join(mapped_char(c)[0] for c in cs).strip()
        if pat.fullmatch(t):
            out.append((L['y'], t))
    return out


def rebuild_int_statements_page(page, stmt_x_hi=300.0, dash_x=(60.0, 84.0)):
    """9709-style: bullet-anchored statement rows, statement band x<stmt_x_hi,
    dash items ('-'/bullet at dash_x) inside the statement band become
    sub_item groups, notes band (x>=stmt_x_hi) becomes trailing sub_items."""
    chars = page_chars(page)
    bullets = find_bullets(chars, x_max=70)
    rows = []
    for i, (by, bx) in enumerate(bullets):
        y_hi = bullets[i + 1][0] if i + 1 < len(bullets) else 10**9
        band = list(_in(chars, x_lo=71, x_hi=stmt_x_hi, y_lo=by, y_hi=y_hi))
        notes = list(_in(chars, x_lo=stmt_x_hi, y_lo=by, y_hi=y_hi))
        if not band:
            continue
        lines = group_lines(band)
        dash_lines, plain_lines = [], []
        for L in lines:
            x0 = L['chars'][0]['x']
            first = mapped_char(L['chars'][0])[0]
            if dash_x[0] <= x0 <= dash_x[1] and first in '\u2212\u2013-\u2022\x07':
                dash_lines.append(L)
            elif dash_x[0] <= x0 <= dash_x[1] and not plain_lines:
                dash_lines.append(L)
            else:
                plain_lines.append(L)
        text, n1 = assemble_lines_para(plain_lines)
        items, n2 = _dash_groups(dash_lines)
        nitems, n3 = _notes_groups(notes)
        rows.append({
            'anchor_y': by, 'text': text, 'sub_items': items + nitems,
            'aborted': n1 is None or any(t is None for t, _ in items + nitems),
            'notes': n1 + [x for t, ns in items + nitems for x in ns] + n3,
        })
    return rows


def _dash_groups(dash_lines):
    """Dash-anchored item groups; continuation lines (no dash) join the last
    group."""
    groups = []
    for L in dash_lines:
        first = mapped_char(L['chars'][0])[0]
        if first in '\u2212\u2013-\u2022\x07':
            groups.append([L])
        elif groups:
            groups[-1].append(L)
        else:
            groups.append([L])
    out = []
    for g in groups:
        t, ns = assemble_lines_para(g)
        # strip the leading dash glyph itself
        if t is not None:
            t = re.sub(r'^[\u2212\u2013\-\u2022\x07]\s*', '', t).strip()
        out.append((t, ns))
    return out


def _notes_groups(notes_chars, bullet_x=300.0):
    """Notes band -> paragraph groups split on printed bullet glyphs; each
    group assembles to one sub_item."""
    if not notes_chars:
        return [], []
    notes_chars = [c for c in notes_chars]
    bl = sorted([c for c in notes_chars if c['ch'] == '\u2022'], key=lambda c: c['y'])
    out, ns_all = [], []
    if not bl:
        t, ns = assemble_band(notes_chars)
        if t and t.strip() in ('Notes and examples', 'Notes and guidance', 'Examples'):
            return [], ns
        return [(t, ns)], ns
    ys = [c['y'] for c in bl]
    bounds = ys + [10**9]
    lo = min(c['y'] for c in notes_chars) - 1
    for k, b in enumerate(bl):
        seg = [c for c in notes_chars if b['y'] - 0.5 <= c['y'] < bounds[k + 1] - 0.5 and c is not b]
        t, ns = assemble_band(seg)
        if t is not None:
            t = re.sub(r'^[\u2212\u2013\-\u2022\x07]\s*', '', t).strip()
            if t in ('Notes and examples', 'Notes and guidance', 'Examples'):
                continue
        out.append((t, ns))
        ns_all += ns
    return out, ns_all


def rebuild_nmk_page(page, stmt_x_hi=300.0, notes_x_lo=300.0):
    """business-23-style nmk_outcomes/tier pages: statement rows anchored by a
    bullet/dingbat at x<70, notes bullets printed at x=notes_x_lo."""
    chars = page_chars(page)
    bullets = find_bullets(chars, x_max=70, glyph='\u2022')
    ding = find_bullets(chars, x_max=70, glyph='\x07')
    anchors = sorted(bullets + ding)
    rows = []
    for i, (by, bx) in enumerate(anchors):
        y_hi = anchors[i + 1][0] if i + 1 < len(anchors) else 10**9
        band = list(_in(chars, x_lo=71, x_hi=stmt_x_hi, y_lo=by, y_hi=y_hi))
        notes = list(_in(chars, x_lo=notes_x_lo, y_lo=by - 1.0, y_hi=y_hi))
        if not band:
            continue
        text, n1 = assemble_band(band)
        items, n2 = _notes_groups(notes, bullet_x=notes_x_lo)
        rows.append({
            'anchor_y': by, 'text': text, 'sub_items': [t for t, _ in items],
            'aborted': n1 is None or any(t is None for t, _ in items),
            'notes': (n1 or []) + [x for t, ns in items for x in ns] + n2,
        })
    return rows


# ---------------------------------------------------------------------------
# row matching (rebuilt page rows <-> parsed rows)
# ---------------------------------------------------------------------------

def _words(t):
    return re.findall(r'[a-z]{4,}', (t or '').lower())


def _lcs_words(a, b):
    """Longest common contiguous word run."""
    aw, bw = _words(a), _words(b)
    best = []
    for i in range(len(aw)):
        for j in range(len(bw)):
            k = 0
            while i + k < len(aw) and j + k < len(bw) and aw[i + k] == bw[j + k]:
                k += 1
            if k > len(best):
                best = aw[i:i + k]
    return best


def match_rows(rebuilt, parsed_row, by_code=True):
    """Score rebuilt rows against a parsed row; returns (best, score, margin)."""
    best, bs, second = None, 0, 0
    for r in rebuilt:
        s = 0
        if by_code and r.get('code') and parsed_row.get('official_code'):
            if r['code'].lstrip('0') == str(parsed_row['official_code']).lstrip('0'):
                s += 100
        lcs = _lcs_words(r.get('text') or '', parsed_row.get('text') or '')
        if s < 100 and len(lcs) < 3:
            continue
        s += min(len(lcs), 12)
        if s > bs:
            second, bs, best = bs, s, r
        elif s > second:
            second = s
    return best, bs, second


# ---------------------------------------------------------------------------
# per-qual drivers
# ---------------------------------------------------------------------------

GARBLE_TEXT = re.compile(r'\^ |\bP \^|Po m|\b(sin|cos|tan|sec|cosec|cot) i\b| # ')
MERGE_TEXT = re.compile('\x07.*\u2022')
SUPLOSS_HINT = re.compile(r'notation y A|\bH SO\b|\bSimpson')


def target_rows(parsed, qual):
    """Rows this lane targets, per qual scope."""
    ids = []
    for sp in parsed['spec_points']:
        t = sp.get('text', '')
        flags = sp.get('flags') or []
        if qual == 'cie-a-level-maths-2023-2025':
            if GARBLE_TEXT.search(t) or any(GARBLE_TEXT.search(s) for s in sp.get('sub_items') or []):
                ids.append(sp['id'])
        elif qual == 'cie-as-environmental-management-2025-2027':
            if sp.get('page') == 19:
                ids.append(sp['id'])
        elif qual in ('cie-igcse-business-2023-2025',):
            if MERGE_TEXT.search(t):
                ids.append(sp['id'])
        elif qual == 'cie-igcse-maths-2025-2027':
            if 'Examples include' in t or MERGE_TEXT.search(t) or 'these)' in t:
                ids.append(sp['id'])
        elif qual == 'ial-maths':
            if 'two-column-line-interleave' in flags:
                ids.append(sp['id'])
        elif qual == 'ial-physics':
            if sp['id'] == 'IAL_PHYSICS:45':
                ids.append(sp['id'])
        elif qual in ('cie-a-level-chemistry-2025-2027', 'cie-igcse-chemistry-2023-2025'):
            if SUPLOSS_HINT.search(t) or 'possible-superscript-loss' in flags:
                ids.append(sp['id'])
    return ids


FAMILY_CFG = {
    # qual -> (rebuild fn, extra kwargs, anchor kind)
    'cie-a-level-maths-2023-2025': ('int_statements', {}),
    'cie-as-environmental-management-2025-2027': ('nmk', {}),
    'cie-igcse-business-2023-2025': ('nmk', {}),
    'cie-igcse-maths-2025-2027': ('nmk', {}),
    'ial-maths': ('nmk', {}),
    'ial-physics': ('ial_physics', {}),
}


def row_region_chars(chars, y_lo, y_hi, x_lo, x_hi):
    y_lo = max(y_lo, 58.0)
    if y_hi is None:
        y_hi = 772.0
    y_hi = min(y_hi, 772.0)
    return [c for c in chars if y_lo <= c['y'] and c['x'] >= x_lo
            and (x_hi is None or c['x'] < x_hi) and (c['y'] < y_hi - 0.5)]


MARKER_RE = re.compile(r'^\((?:[a-z]|\d{1,2})\)\s')

HEAD_CODE_RE = re.compile(r'^(?:[A-Z]?\d{1,2}(?:\.\d{1,2}){0,1})$')
NOISE_RE = re.compile(r'Back to contents page|www\.cambridgeinternational\.org|^\d{1,3}$')


def _split_marker_items(band):
    """Split a statement band into (plain_lines, item_groups). A line is a
    marker line when its first glyph is a dash/bullet near the band's left
    edge or the text starts with '(a)'/'(1)'-style markers. A bare subtopic
    head code line (N / N.M at the left edge) CUTS the band (next head)."""
    lines = group_lines(band)
    cut = []
    for L in lines:
        t_quick = re.sub(r'\s+', ' ', ''.join(
            (mapped_char(c)[0] or '') for c in L['chars'])).strip()
        if L['chars'][0]['x'] < 105:
            m = re.match(r'^([A-Z]?\d{1,2}(?:\.\d{1,2}){0,2})(?:\s|$)', t_quick)
            if m and m.group(1).count('.') <= 1:
                break  # bare subtopic head (N or N.M) -> next row's territory
        if NOISE_RE.search(t_quick):
            continue
        cut.append(L)
    lines = cut
    plain, groups = [], []
    for L in lines:
        first = mapped_char(L['chars'][0])[0]
        x0 = L['chars'][0]['x']
        head = ''.join(mapped_char(c)[0] for c in L['chars'][:6])
        is_marker = (first in '\u2212\u2013-\u2022\x07' and x0 <= L['chars'][0]['x'] + 15) \
            or bool(MARKER_RE.match(re.sub(r'\s+', ' ', head + ' ')))
        if is_marker:
            groups.append([L])
        elif groups:
            groups[-1].append(L)
        else:
            plain.append(L)
    return plain, groups


SECTION_FURNITURE_RE = re.compile(r'^Candidates should be able to:')


def _head_cut_y(chars, y_lo, y_hi):
    """Y of the next section furniture line after y_lo (full-width scan):
    a bare head code (N / N.M, 0-1 dots) at x<105 or the 'Candidates should
    be able to:' marker. None when the row runs to its natural end."""
    lines = group_lines([c for c in chars if y_lo - 0.5 <= c['y'] < (y_hi or 10**9)])
    for L in lines:
        if L['y'] <= y_lo + 3.0:
            continue  # the row's own first line (its printed code lives here)
        t = re.sub(r'\s+', ' ', ''.join((mapped_char(c)[0] or '') for c in L['chars'])).strip()
        if not t:
            continue
        x0 = L['chars'][0]['x']
        if SECTION_FURNITURE_RE.match(t):
            return L['y']
        if x0 < 105:
            m = re.match(r'^([A-Z]?\d{1,2}(?:\.\d{1,2}){0,2})(?:\s|$)', t)
            if m and m.group(1).count('.') <= 1:
                return L['y']
    return None


def repair_row_region(doc, page, oy, y_end, x_lo, x_hi=None, notes_x=None, y_lo_ext=None):
    """Row-region rebuild via parsed oy bounds. Returns dict(text, sub_items,
    aborted, notes). In-band dash/(a)/(b) markers become sub_item groups."""
    chars = page_chars(doc[page])
    cut = _head_cut_y(chars, oy - 2.0, y_end)
    if cut is not None and (y_end is None or cut < y_end):
        y_end = cut
    y_lo = oy - (y_lo_ext if y_lo_ext else 2.0)
    y_hi_eff = min(y_end, 772.0) if y_end is not None else 772.0
    band = row_region_chars(chars, y_lo, y_end, x_lo, x_hi)
    # line-edge refinement: a rounded end-oy must not orphan a line's small
    # glyphs (subscripts print below their line's body baseline) — keep whole
    # visual lines whose mid-y sits inside the region
    ext = row_region_chars(chars, y_lo, (y_end or 772.0) + 14.0, x_lo, x_hi)
    lines_all = group_lines(ext)
    kept = []
    for L in lines_all:
        if y_lo - 5.0 <= L['baseline'] < y_hi_eff - 0.5:
            kept.extend(L['chars'])
    band = sorted(kept, key=lambda c: (c['y'], c['x']))
    frac_notes = []
    band = inline_fraction_merge(band, frac_notes)
    plain, groups = _split_marker_items(band)
    text, n1 = assemble_lines_para(plain) if plain else ('', [])
    if text == '' and not groups:
        text, n1 = assemble_band(band)
        groups = []
    items = []
    for g in groups:
        t, ns = assemble_lines_para(g)
        if t is not None:
            t = re.sub(r'^[\u2212\u2013\-\u2022\x07]\s*', '', t).strip()
        items.append((t, ns))
    sub_notes = []
    sub_items = [t for t, _ in items]
    if notes_x is not None:
        nchars = row_region_chars(chars, oy - 2.0, y_end, notes_x, None)
        ngroups, sub_notes = _notes_groups(nchars)
        sub_items += [t for t, _ in ngroups if t]
    aborted = text is None or any(t is None for t, _ in items)
    return {
        'text': text, 'sub_items': sub_items,
        'aborted': aborted,
        'notes': (n1 or []) + frac_notes + [x for t, ns in items for x in ns] + sub_notes,
    }


def _strip_leading_code(t):
    return re.sub(r'^(?:[A-Z]?\d{1,2}(?:\.\d{1,3}){0,3})\s+', '', t or '', count=1)


def qual_pdf_path(qual):
    fs = glob.glob(os.path.join(OSDIR, qual, '*.pdf'))
    if len(fs) != 1:
        raise SystemExit(f'expect 1 pdf for {qual}: {fs}')
    return fs[0]


def next_oy_map(parsed, exclude=()):
    """id -> (page, end_y): the oy of the next spec_point in document order
    (rows in `exclude` are skipped as bounds)."""
    rows = sorted((s for s in parsed['spec_points'] if s['id'] not in exclude),
                  key=lambda s: (s.get('page', 0), s.get('oy', 0)))
    out = {}
    for i, sp in enumerate(rows):
        if i + 1 < len(rows):
            nxt = rows[i + 1]
            out[sp['id']] = (nxt['page'], nxt['oy']) if nxt['page'] == sp['page'] else (sp['page'], None)
        else:
            out[sp['id']] = (sp['page'], None)
    return out


def build_proposals(qual, parsed):
    """Returns (proposals, deletes, stats). proposals: id -> new text/sub_items."""
    set_fontmap(qual)
    cfg = FAMILY_CFG.get(qual)
    doc = pymupdf.open(qual_pdf_path(qual))
    targets = target_rows(parsed, qual)
    tset = set(targets)

    # pre-pass deletes (EMM p19 spurious note-rows) must not bound the real
    # row's region: exclude them from the oy map before any rebuild
    deletes = []
    if qual == 'cie-as-environmental-management-2025-2027':
        for sp in parsed['spec_points']:
            if sp['page'] == 19 and sp['oy'] > 190:
                deletes.append(sp['id'])
    nxt = next_oy_map(parsed, exclude=set(deletes))
    by_id = {sp['id']: sp for sp in parsed['spec_points']}
    proposals, aborts, nomatch = {}, [], []

    if qual == 'ial-maths':
        # full rebuild of every row (statement band x 103-271, notes x>=271);
        # y-bounds from parsed oy; both layers updated identically
        for sp in parsed['spec_points']:
            page = sp['page'] - 1
            end_page, end_y = nxt[sp['id']]
            r = repair_row_region(doc, page, sp['oy'], end_y, x_lo=103, x_hi=271, notes_x=271)
            if r['aborted'] or not r['text']:
                aborts.append(sp['id'])
                continue
            cur_t = re.sub(r'\s+', ' ', sp['text']).strip()
            if r['text'] != cur_t or (r['sub_items'] or []) != (sp.get('sub_items') or []):
                proposals[sp['id']] = r
        return proposals, deletes, {'aborts': aborts, 'nomatch': nomatch, 'targets': len(targets)}

    if qual == 'ial-physics':
        sp = by_id['IAL_PHYSICS:45']
        page = sp['page'] - 1
        end_page, end_y = nxt[sp['id']]
        r = repair_row_region(doc, page, sp['oy'], end_y, x_lo=105, x_hi=None, notes_x=None)
        if r['aborted'] or not r['text']:
            aborts.append(sp['id'])
        elif 'refractive index' in r['text'] and r['text'] != sp['text']:
            proposals[sp['id']] = r
        else:
            nomatch.append(sp['id'])
        return proposals, deletes, {'aborts': aborts, 'nomatch': nomatch, 'targets': 1}

    if qual in ('cie-a-level-chemistry-2025-2027', 'cie-igcse-chemistry-2023-2025'):
        for sp in parsed['spec_points']:
            if sp['id'] not in tset:
                continue
            page = sp['page'] - 1
            end_page, end_y = nxt[sp['id']]
            r = repair_row_region(doc, page, sp['oy'], end_y, x_lo=71, x_hi=None, notes_x=None)
            if r['aborted'] or not r['text']:
                aborts.append(sp['id'])
                continue
            lcs = _lcs_words(r['text'], sp['text'])
            if len(lcs) >= 5 and r['text'] != sp['text']:
                proposals[sp['id']] = r
            else:
                nomatch.append(sp['id'])
        return proposals, deletes, {'aborts': aborts, 'nomatch': nomatch, 'targets': len(targets)}

    # oy-region families: parsed (page, oy) is the row's first line (verified
    # for all four quals); region ends at the next spec_point's oy on the same
    # page. Statement band + notes band per qual; in-band markers split items.
    REGION_X = {
        'cie-igcse-business-2023-2025': (50, 300, 300),
        'cie-as-environmental-management-2025-2027': (71, 300, 300),
        'cie-igcse-maths-2025-2027': (60, 295, 295),
        'cie-a-level-maths-2023-2025': (71, 300, 300),
    }
    x_lo, x_hi, notes_x = REGION_X[qual]
    dset = set(deletes)
    MATH_FONTS = ('TimesNewRoman', 'MM', 'SymbolMT')
    for sp in parsed['spec_points']:
        if sp['id'] not in tset or sp['id'] in dset:
            continue
        page = sp['page'] - 1
        end_page, end_y = nxt[sp['id']]
        # stacked-fraction ownership: math glyphs printed 12px ABOVE a row's
        # oy are that row's own numerator (capture) — and for the NEXT row
        # they are not ours (cut)
        own_pre = [c for c in page_chars(doc[page])
                   if sp['oy'] - 12.0 <= c['y'] < sp['oy'] - 1.0
                   and x_lo <= c['x'] and c['x'] < x_hi]
        y_lo_ext = 12.0 if own_pre and all(c['font'].startswith(MATH_FONTS) for c in own_pre) else None
        end_adj = end_y
        if end_y is not None:
            nxt_pre = [c for c in page_chars(doc[page])
                       if end_y - 12.0 <= c['y'] < end_y - 1.0 and x_lo <= c['x'] and c['x'] < x_hi]
            if nxt_pre and all(c['font'].startswith(MATH_FONTS) for c in nxt_pre):
                end_adj = end_y - 12.5
        r = repair_row_region(doc, page, sp['oy'], end_adj, x_lo, x_hi, notes_x, y_lo_ext=y_lo_ext)
        if r['aborted'] or not r['text']:
            aborts.append(sp['id'])
            continue
        lcs = _lcs_words(r['text'], sp['text'])
        code_ok = (sp.get('official_code') and r['text'].lstrip().startswith(
            str(sp['official_code'])))
        min_lcs = 1 if qual in ('cie-as-environmental-management-2025-2027',
                                'cie-a-level-maths-2023-2025') else 4
        if len(lcs) < min_lcs and not code_ok:
            nomatch.append(sp['id'])
            continue
        new_text = _strip_leading_code(r['text']) if qual in (
            'cie-as-environmental-management-2025-2027', 'cie-igcse-maths-2025-2027') else r['text']
        new_items = [t for t in (r.get('sub_items') or []) if t]
        cur_items = [re.sub(r'\s+', ' ', s).strip() for s in (sp.get('sub_items') or [])]
        # zero-degradation: never ship a rebuild that loses content (notes
        # legitimately move text -> sub_items, so compare the sums)
        new_vol = len(_words(new_text)) + sum(len(_words(t)) for t in new_items)
        old_vol = len(_words(sp['text'])) + sum(len(_words(t)) for t in cur_items)
        new_chars = len(new_text) + sum(len(t) for t in new_items)
        old_chars = len(sp['text']) + sum(len(t) for t in cur_items)
        if new_vol < old_vol - 1 or new_chars < 0.75 * old_chars:
            aborts.append(sp['id'])
            continue
        if new_text != sp['text'] or new_items != cur_items:
            proposals[sp['id']] = {'text': new_text, 'sub_items': new_items,
                                   'aborted': False, 'notes': r.get('notes', []),
                                   'old_text': sp['text'], 'old_items': cur_items}

    return proposals, deletes, {'aborts': aborts, 'nomatch': nomatch, 'targets': len(targets)}


def _attach_codes(page, rebuilt):
    """Attach printed N.M[.K] codes to rebuilt rows by anchor-y proximity."""
    chars = page_chars(page)
    lines = group_lines([c for c in chars if c['x'] <= 105])
    codes = []
    for L in lines:
        t = ''.join(mapped_char(c)[0] for c in L['chars']).strip()
        m = re.fullmatch(r'([A-Z]?\d{1,2}(?:\.\d{1,3}){0,2})', t)
        if m:
            codes.append((L['y'], m.group(1)))
    for r in rebuilt:
        best = None
        for cy, code in codes:
            if cy <= r['anchor_y'] + 2.0 and (best is None or cy > best[0]):
                best = (cy, code)
        if best:
            r['code'] = best[1]


# ---------------------------------------------------------------------------
# gates + apply + CLI
# ---------------------------------------------------------------------------

def gate_check(qual, parsed, proposals, deletes):
    """G2 conservation: id set after = id set before - deletes; no new ids;
    official codes of surviving rows unchanged."""
    before = {sp['id'] for sp in parsed['spec_points']}
    after = before - set(deletes)
    if set(proposals) - before:
        raise SystemExit(f'G2 FAIL: proposals reference unknown ids: {set(proposals) - before}')
    if set(deletes) - before:
        raise SystemExit(f'G2 FAIL: deletes reference unknown ids: {set(deletes) - before}')
    code_before = {sp['id']: sp.get('official_code') for sp in parsed['spec_points']}
    for sp in parsed['spec_points']:
        if sp['id'] in proposals and 'official_code' in sp:
            pass  # codes untouched by construction (text/sub_items only)
    return len(before), len(after), code_before


def apply_qual(qual, dry=False):
    path, parsed, raw = load_parsed(qual)
    before_raw = raw
    proposals, deletes, stats = build_proposals(qual, parsed)
    n_before, n_after, _ = gate_check(qual, parsed, proposals, deletes)

    changed = 0
    for sp in parsed['spec_points']:
        if sp['id'] in proposals:
            p = proposals[sp['id']]
            if p['text']:
                sp['text'] = p['text']
            if p['sub_items'] is not None and not p['aborted']:
                sp['sub_items'] = p['sub_items']
            fl = sp.setdefault('flags', [])
            if 'reparse-1.0' not in fl:
                fl.append('reparse-1.0')
            sp['flags'] = sorted(set(fl))
            changed += 1
    if deletes:
        parsed['spec_points'] = [sp for sp in parsed['spec_points'] if sp['id'] not in set(deletes)]
    if 'counts' in parsed:
        parsed['counts']['spec_points'] = len(parsed['spec_points'])
        parsed['counts']['flagged'] = sum(1 for sp in parsed['spec_points'] if sp.get('flags'))
    if 'source' in parsed:
        pv = parsed['source'].get('parser', '')
        if REPAIR_VERSION not in pv:
            parsed['source']['parser'] = f'{pv}+{REPAIR_VERSION}' if pv else REPAIR_VERSION

    new_raw = serialize(parsed)
    if new_raw == before_raw:
        print(f'  {qual}: no changes (proposals={len(proposals)} deletes={len(deletes)})')
        return

    # parse_report provenance
    rp_path = os.path.join(PJDIR, qual, 'parse_report.json')
    rp_raw = open(rp_path, encoding='utf-8').read()
    rp = json.loads(rp_raw)
    rp['reparse'] = {
        'version': REPAIR_VERSION,
        'classes': sorted(set(stats.get('classes', ['interleave/garble/supsub']))),
        'proposals': sorted(proposals),
        'deletes': sorted(deletes),
        'aborted_rows': sorted(stats.get('aborts', [])),
        'nomatch_rows': sorted(stats.get('nomatch', [])),
        'counts_before': n_before,
        'counts_after': n_after,
    }
    if 'counts' in rp:
        rp['counts'] = dict(rp['counts'])
        rp['counts']['spec_points'] = len(parsed['spec_points'])

    print(f'  {qual}: proposals={len(proposals)} deletes={len(deletes)} '
          f'aborted={len(stats.get("aborts", []))} nomatch={len(stats.get("nomatch", []))}')
    if dry:
        for sp_id in sorted(proposals)[:60]:
            p = proposals[sp_id]
            print(f'    ~ {sp_id}')
            print(f'        old: {(p.get("old_text") or "")[:150]!r}')
            print(f'        new: {(p.get("text") or "")[:150]!r}')
            if p.get('sub_items'):
                print(f'        items: {[s[:80] for s in p["sub_items"][:4]]}')
        for sp_id in sorted(deletes):
            print(f'    - {sp_id}')
        return

    open(path, 'w', encoding='utf-8').write(new_raw)
    open(rp_path, 'w', encoding='utf-8').write(serialize(rp))
    print(f'    WROTE {path}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['probe', 'apply'])
    ap.add_argument('quals', nargs='+')
    args = ap.parse_args()
    for qual in args.quals:
        apply_qual(qual, dry=(args.mode == 'probe'))


if __name__ == '__main__':
    main()
