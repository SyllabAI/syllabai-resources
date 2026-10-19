#!/usr/bin/env python3
"""spec_assembly_guards.py — post-parse assembly guards for spec_parser output.

Added by T-KG-14 (2026-09-24) to close the documented follow-up "spec_parser
itself still emits the old shapes — a future re-parse should adopt the
line-join/lettered guards" (worklog T-KG-13). The functions generalise the
PDF-verified repairs that T-KG-13/T-KG-14 applied to the canonical layer:

  1. join_wrapped_bullets  — the parser kept only the FIRST printed line of
     wrapped bullets (geography SX aims, skills lists, appendix skills: 69
     rows repaired in T-KG-13). This pass re-assembles the continuation
     lines from the page's line geometry (bullet-block model, ported from
     the T-KG-13 repair script) with a verbatim-containment abort guard.

  2. split_lettered_leads  — lettered statements ('b)', 'c)', '4c)') merged
     into the tail of the previous row's text (accounting S1.045 et al.,
     audit finding C). Split them back into separate statement texts.

  3. flag_two_column_interleave — two-column tables whose columns the text
     stream interleaves word-by-word (geography fieldwork/AO/skills tables;
     audit finding B). DETECTION-ONLY: rows are flagged
     'two-column-line-interleave' for manual/spatial rebuild — the same
     convention T-KG-13 used. No text is rewritten by this guard.

Zero-invention discipline: every joined/split string is assembled ONLY from
printed page lines (guard 1 aborts unless the assembly is verbatim-contained
in the source lines); guards 2-3 never invent characters.

Usage (post-parse, before canonicalisation):

    from spec_assembly_guards import apply_guards
    stats = apply_guards(rows, get_page_lines=get_page_lines,
                         families={'heading_bullets'})
"""

import re

FLAG_INTERLEAVE = 'two-column-line-interleave'
FLAG_LETTERED_SPLIT = 'lettered-lead-split'
FLAG_LINE_JOIN = 'line-join-continuation'

# group-label tokens whose repetition around a bullet glyph is the signature
# of a two-column interleave (verified cases: 'Quantitative Quantitative',
# 'Executive function Creativity • Creativity', 'Secondary use (1) A local
# report ...' in the geography tables)
_LABEL_TOKENS = {'primary', 'quantitative', 'qualitative', 'secondary'}

_LEADED_TAIL = re.compile(r'(?:(?<=^)|(?<=[.;!?:"]))\s*([a-z]|\d{1,2}[a-z])\)\s+')
_BULLET_GLYPH = '\u2022'

# families where the wrap-indent bullet-block model applies (guard 1) and
# where lettered-lead merges occur (guard 2)
_JOIN_FAMILIES = {'heading_bullets', 'code_column', 'triplet_table'}
_LETTER_FAMILIES = {'heading_bullets', 'lettered_table'}


def page_lines_from_doc(doc, page):
    """y,x-ordered word lines of a page: [(y, x0, text, words)] — the
    T-KG-13 page_lines convention, on a pymupdf document. words are raw
    pymupdf word tuples (x0, y0, x1, y1, word, block, line)."""
    words = doc[page - 1].get_text('words')
    lines = {}
    for w in words:
        lines.setdefault((w[5], w[6]), []).append(w)
    out = []
    for key in sorted(lines, key=lambda k: (lines[k][0][1], lines[k][0][0])):
        ws = sorted(lines[key], key=lambda w: w[0])
        y, x0 = round(ws[0][1], 1), round(ws[0][0], 1)
        if y > 780:  # skip page footer
            continue
        out.append((y, x0, ' '.join(w[4] for w in ws), ws))
    return out


def _norm(s):
    return re.sub(r'\s+', ' ', str(s or '')).strip().lower()


def _squash(s):
    return re.sub(r'\s+', '', str(s or '')).lower()


# ------------------------------------------------------------------ guard 1

def bullet_blocks(lines, wrap_x=(70, 120)):
    """Group page lines into bullet blocks: [(first_line, [cont_lines])].

    `lines` yields (y, x0, text, words) per physical line (the
    spec_parser.page_spans / T-KG-13 page_lines convention, where words is
    [(x0, x1, y, word), ...]). A block starts at a line whose first word is
    the bullet glyph; continuation lines follow at wrap indent.
    """
    blocks, cur = [], None
    for y, x0, text, words in lines:
        is_bullet = bool(words) and words[0][4] == _BULLET_GLYPH
        if is_bullet:
            if cur:
                blocks.append(cur)
            cur = {'first': text, 'cont': []}
        elif cur is not None and wrap_x[0] < x0 < wrap_x[1]:
            cur['cont'].append(text)
        else:
            if cur:
                blocks.append(cur)
            cur = None
    if cur:
        blocks.append(cur)
    return blocks


def _strip_bullet(text):
    t = text.lstrip()
    return t[1:].strip() if t.startswith(_BULLET_GLYPH) else t


def _stream_in_lines(target, lines):
    """Squashed word-stream containment of target in the given page lines."""
    words = []
    for ln in lines:
        words.extend(re.findall(r'\S+', ln))
    return _squash(target) in _squash(' '.join(words))


def join_wrapped_bullets(rows, get_page_lines, exclude_pages=(),
                         exclude_ids=(), stats=None):
    """Re-join wrapped bullet continuations into row texts (guard 1).

    rows: list of spec-point dicts (v1 shape: text + provenance.page, or a
    top-level `page`). get_page_lines(page) -> the page_lines sequence.
    Returns the number of rows repaired. A row is repaired only when its
    text matches a bullet block's first line EXACTLY (normalised) and the
    assembled continuation is verbatim-contained in the block's lines.
    """
    n = 0
    block_cache = {}
    for p in rows:
        pid = p.get('id', '?')
        if pid in exclude_ids:
            continue
        prov = p.get('provenance') or {}
        page = prov.get('page') or p.get('page')
        if not page or page in exclude_pages:
            continue
        text = (p.get('text') or '').strip()
        if not text:
            continue
        if page not in block_cache:
            block_cache[page] = bullet_blocks(get_page_lines(page))
        for b in block_cache[page]:
            first = _strip_bullet(b['first'])
            if _norm(first) != _norm(text):
                continue
            cont = [c for c in (_strip_bullet(c) for c in b['cont']) if c]
            if not cont:
                break
            rebuilt = text + ' ' + ' '.join(cont)
            full_block_lines = [b['first']] + b['cont']
            if not _stream_in_lines(rebuilt, full_block_lines):
                if stats is not None:
                    stats.append({'guard': 'line_join', 'aborted': pid,
                                  'reason': 'assembly not verbatim'})
                break
            if stats is not None:
                stats.append({'guard': 'line_join', 'id': pid, 'page': page,
                              'old': text, 'new': rebuilt})
            p['text'] = rebuilt
            flags = p.setdefault('flags', [])
            if FLAG_LINE_JOIN not in flags:
                flags.append(FLAG_LINE_JOIN)
            n += 1
            break
    return n


# ------------------------------------------------------------------ guard 2

def split_lettered_leads(rows, stats=None):
    """Split merged lettered-statement tails out of row texts (guard 2).

    A row whose text contains mid-text lettered leads ('... prev tail.
    b) Do something ... c) Also ...') is split: the text before the first
    lettered lead stays the row text; each lettered segment becomes its own
    entry in the row's sub_items (the heading_bullets convention: promoted
    list items live as sub_items). Never invents characters — segments are
    verbatim slices of the original text.
    """
    n = 0
    for p in rows:
        text = (p.get('text') or '').strip()
        if not text:
            continue
        matches = list(_LEADED_TAIL.finditer(text))
        if len(matches) < 2:
            continue
        heads = [m.start() for m in matches]
        segs = []
        for i, s in enumerate(heads):
            e = heads[i + 1] if i + 1 < len(heads) else len(text)
            segs.append(text[s:e].strip())
        head_text = text[:heads[0]].strip()
        if not head_text or not segs:
            continue
        if stats is not None:
            stats.append({'guard': 'lettered_split', 'id': p.get('id', '?'),
                          'old': text, 'head': head_text,
                          'segments': [s[:60] for s in segs]})
        p['text'] = head_text
        subs = p.setdefault('sub_items', [])
        subs.extend(segs)
        flags = p.setdefault('flags', [])
        if FLAG_LETTERED_SPLIT not in flags:
            flags.append(FLAG_LETTERED_SPLIT)
        n += 1
    return n


# ------------------------------------------------------------------ guard 3

def flag_two_column_interleave(rows, stats=None):
    """Flag rows whose text shows the two-column interleave signature.

    Detection (conservative, warn-only — no rewriting):
      a) a word repeated adjacently ('Creativity • Creativity',
         'Quantitative Quantitative'), or
      b) >= 2 distinct group-label tokens fused mid-text with a bullet
         glyph present ('Local report on energy Secondary use (1) ...').
    """
    n = 0
    for p in rows:
        text = str(p.get('text') or '')
        if _BULLET_GLYPH not in text:
            continue
        words = re.findall(r'[A-Za-z]+', text)
        dup = any(words[i].lower() == words[i + 1].lower()
                  for i in range(len(words) - 1))
        labels = {w.lower() for w in words if w.lower() in _LABEL_TOKENS}
        fused = len(labels) >= 2
        if not (dup or fused):
            continue
        flags = p.setdefault('flags', [])
        if FLAG_INTERLEAVE not in flags:
            flags.append(FLAG_INTERLEAVE)
            n += 1
            if stats is not None:
                stats.append({'guard': 'interleave_flag', 'id': p.get('id', '?'),
                              'text': text[:80]})
    return n


# ---------------------------------------------------------------- orchestrator

def apply_guards(rows, get_page_lines=None, families=None,
                 join_exclude_pages=(), join_exclude_ids=(), stats=None):
    """Run the assembly guards over parsed rows (post-parse, pre-canonical).

    families: the parse's family name (or set) — guard 1 runs only for the
    bullet/heading families where the wrap model applies, guard 2 only for
    the heading/lettered families where lettered-lead merges occur; guard 3
    (flag-only) runs for all families.
    Returns a stats list (also appended to the caller's list when given).
    """
    out = stats if stats is not None else []
    fam = {families} if isinstance(families, str) else set(families or ())
    if get_page_lines is not None and fam & _JOIN_FAMILIES:
        join_wrapped_bullets(rows, get_page_lines,
                             exclude_pages=join_exclude_pages,
                             exclude_ids=join_exclude_ids, stats=out)
    if fam & _LETTER_FAMILIES:
        split_lettered_leads(rows, stats=out)
    flag_two_column_interleave(rows, stats=out)
    return out
