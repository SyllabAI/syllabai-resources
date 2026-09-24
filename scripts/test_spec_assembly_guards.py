#!/usr/bin/env python3
"""test_spec_assembly_guards.py — golden tests for the T-KG-14 guards.

Golden pairs come from the REAL repairs: T-KG-13's report.json (SX.002
line-join old/new, S9.139 interleave old) and the audit's raw findings
(accounting lettered-merge S1.045 text shape). Run: python3 this file.
"""
import re
import sys

from spec_assembly_guards import (
    apply_guards, bullet_blocks, flag_two_column_interleave,
    join_wrapped_bullets, split_lettered_leads,
)

FAILS = []


def check(name, cond, detail=''):
    print(('PASS ' if cond else 'FAIL ') + name + (f' {detail}' if detail and not cond else ''))
    if not cond:
        FAILS.append(name)


# ---------------------------------------------------------------- guard 1
# Real case (T-KG-13 report): geography SX.002, page 6 — the parser kept the
# first printed line; the block's continuation lines wrap at x0 ~70-120.
SX002_OLD = 'actively engage in the process of geographical enquiry to develop as effective and'
SX002_NEW = ('actively engage in the process of geographical enquiry to develop as '
             'effective and independent learners, and as critical and reflective '
             'thinkers with enquiring minds')


def fake_page_lines(page):
    # (y, x0, text, words) — words are raw pymupdf word tuples
    # (x0, y0, x1, y1, word, block, line); the glyph check reads index 4
    return [
        (100.0, 70.0, '\u2022 actively engage in the process of geographical '
         'enquiry to develop as effective and',
         [(70.0, 100.0, 74.0, 103.0, '\u2022', 0, 0),
          (78.0, 100.0, 110.0, 103.0, 'actively', 0, 1)]),
        (112.0, 88.0, 'independent learners, and as critical and reflective '
         'thinkers with enquiring minds',
         [(88.0, 112.0, 110.0, 115.0, 'independent', 1, 0)]),
        (130.0, 70.0, '\u2022 develop their knowledge and understanding of '
         'geographical concepts',
         [(70.0, 130.0, 74.0, 133.0, '\u2022', 2, 0),
          (78.0, 130.0, 105.0, 133.0, 'develop', 2, 1)]),
    ]


rows = [{'id': 'IGCSE_GEOGRAPHY:SX.002', 'text': SX002_OLD,
         'provenance': {'page': 6}, 'flags': []}]
stats = []
n = join_wrapped_bullets(rows, fake_page_lines, stats=stats)
check('line_join joins continuation', n == 1 and rows[0]['text'] == SX002_NEW)
check('line_join adds flag', 'line-join-continuation' in rows[0]['flags'])

# invariant path: the repaired text must stay verbatim-contained in the page
# line stream, and the containment helper must reject foreign text (the
# module's tripwire; assembly is by construction contained, so the tripwire
# is defense-in-depth for cache/parse drift).
def bad_page_lines(page):
    lines = fake_page_lines(page)
    return [(y, x0, t.replace('reflective', 'WRONG'), w) for (y, x0, t, w) in lines]


def contained(text, lines):
    stream = G_squash(' '.join(str(t) for (_, _, t, _) in lines))
    return G_squash(text) in stream


def G_squash(s):
    return re.sub(r'\s+', '', s).lower()


rows = [{'id': 'X:1', 'text': SX002_OLD, 'provenance': {'page': 6}, 'flags': []}]
n = join_wrapped_bullets(rows, bad_page_lines)
check('line_join output stays verbatim-contained in page lines',
      n == 1 and contained(rows[0]['text'], bad_page_lines(6)))
check('stream check rejects foreign text',
      not contained(SX002_NEW, bad_page_lines(6)))

# ---------------------------------------------------------------- guard 2
# Real shape (audit raw scan, IGCSE_ACCOUNTING:S1.045): lettered statements
# merged into one text ('... spreadsheets. b) Explain ... c) ...').
merged = ('Prepare the ledger accounts and the trial balance, using computer '
          'spreadsheets. b) Explain the issues regarding the security of data: '
          'c) Understand the role of bookkeeping in an accounting system.')
rows = [{'id': 'IGCSE_ACCOUNTING:S1.045', 'text': merged, 'sub_items': [], 'flags': []}]
stats = []
n = split_lettered_leads(rows, stats=stats)
check('lettered split fires on merged row', n == 1, str(stats))
check('lettered split head text', rows[0]['text'] == (
    'Prepare the ledger accounts and the trial balance, using computer spreadsheets.'))
check('lettered split sub_items carry the lettered tails',
      len(rows[0]['sub_items']) == 2
      and rows[0]['sub_items'][0].startswith('b) Explain the issues')
      and rows[0]['sub_items'][1].startswith('c) Understand the role'))
check('lettered split adds flag', 'lettered-lead-split' in rows[0]['flags'])
check('lettered split is no-op on clean rows',
      split_lettered_leads([{'id': 'X:2', 'text': 'State two uses of a trial balance.',
                             'sub_items': []}]) == 0)

# ---------------------------------------------------------------- guard 3
# Real case (T-KG-13 report): S9.139's pre-repair text showed the interleave
# signature ('Executive function Creativity • Creativity' — dup + labels).
interleaved = 'Executive function Creativity \u2022 Creativity'
clean = 'Investigation of river processes and form through primary and secondary fieldwork evidence'
rows = [{'id': 'GEO:S9.139', 'text': interleaved, 'flags': []},
        {'id': 'GEO:clean', 'text': clean, 'flags': []}]
n = flag_two_column_interleave(rows)
check('interleave flag fires on the real signature',
      n == 1 and rows[0]['flags'] == ['two-column-line-interleave'])
check('interleave flag skips clean rows', all('two-column-line-interleave' not in r['flags']
                                              for r in rows[1:]))

# no-flag rows keep short flag lists (no churn on already-flagged rows)
rows = [{'id': 'GEO:x', 'text': interleaved,
         'flags': ['two-column-line-interleave']}]
check('interleave flag idempotent', flag_two_column_interleave(rows) == 0)

# ---------------------------------------------------------- orchestrator
rows = [{'id': 'IGCSE_GEOGRAPHY:SX.002', 'text': SX002_OLD,
         'provenance': {'page': 6}, 'flags': []}]
stats = apply_guards(rows, get_page_lines=fake_page_lines,
                     families='heading_bullets')
check('apply_guards runs all three',
      rows[0]['text'] == SX002_NEW and len(stats) >= 1
      and any(s['guard'] == 'line_join' for s in stats))
stats = apply_guards(rows, get_page_lines=fake_page_lines, families='maths_table')
check('apply_guards skips join for non-bullet families',
      all(s['guard'] != 'line_join' for s in stats))

# ------------------------------------------------- bullet_blocks geometry
blocks = bullet_blocks(fake_page_lines(6))
check('bullet_blocks groups continuations',
      len(blocks) == 2 and blocks[0]['cont'] and not blocks[1]['cont'])

print()
if FAILS:
    print('FAILURES:', FAILS)
    sys.exit(1)
print('ALL GUARD TESTS PASS')
