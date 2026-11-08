#!/usr/bin/env python3
"""envelope.py — targeted extraction of MathsGenie resource envelopes.

Instead of fully parsing the RSC flight stream (whose T-row declared lengths
can bleed into the following row on CMS pages with embedded component slots),
we locate the distinctive envelope key ("decks" / "note" / "lessonTitle") in
the payload, balanced-decode that JSON value, and resolve "$<id>" text refs
against a loose T-row table. Robust to row-boundary quirks.
"""
import json
import re

T_ROW_RE = re.compile(r"([0-9a-f]{1,4}):T([0-9a-f]+),")
REF_RE = re.compile(r"^\$(?:L|@|Q|E|F)?([0-9a-f]{1,4})$")
JUNK_TAIL_RE = re.compile(r"[0-9a-f]{1,4}:\[\"\$\",\"\$L[0-9a-f]+\",null,$")


def t_table(payload: str) -> dict:
    """Loose scan for T rows -> {row_id: raw_text} (UTF-16 length aware)."""
    out = {}
    for m in T_ROW_RE.finditer(payload):
        rid, ln = m.group(1), int(m.group(2), 16)
        start = m.end()
        pos, units = start, 0
        n = len(payload)
        while pos < n and units < ln:
            units += 2 if ord(payload[pos]) > 0xFFFF else 1
            pos += 1
        out[rid] = payload[start:pos]
    return out


def balanced_json(s: str, i: int):
    """Decode the JSON value starting at s[i] ('{' '[' '"' digit...).

    Returns (value, end_index) or (None, i) if not decodable.
    """
    if i >= len(s):
        return None, i
    c = s[i]
    if c == '"':
        m = re.match(r'"(?:[^"\\]|\\.)*"', s[i:])
        if not m:
            return None, i
        return json.loads(m.group(0)), i + m.end()
    if c in "{[":
        open_ch, close_ch = c, {"{": "}", "[": "]"}[c]
        depth, j, n = 0, i, len(s)
        in_str = False
        esc = False
        while j < n:
            ch = s[j]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
            else:
                if ch == '"':
                    in_str = True
                elif ch == open_ch:
                    depth += 1
                elif ch == close_ch:
                    depth -= 1
                    if depth == 0:
                        try:
                            return json.loads(s[i:j + 1]), j + 1
                        except Exception:
                            return None, i
            j += 1
    # bare literals
    m = re.match(r"-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?|true|false|null", s[i:])
    if m:
        return json.loads(m.group(0)), i + m.end()
    return None, i


def _clean_t_text(txt: str) -> str:
    """Trim a flight-row fragment that bled into a T text tail."""
    return JUNK_TAIL_RE.sub("", txt)


def _resolve(obj, table):
    if isinstance(obj, str):
        m = REF_RE.match(obj)
        if m:
            rid = m.group(1)
            if rid in table:
                return _clean_t_text(table[rid])
            return None
        return obj
    if isinstance(obj, list):
        return [_resolve(v, table) for v in obj]
    if isinstance(obj, dict):
        return {k: _resolve(v, table) for k, v in obj.items()}
    return obj


def find_key(payload: str, key: str, table: dict, want="last"):
    """Find every '"key":' occurrence, balanced-decode, resolve refs.

    want='last' returns the last (usually the props-of-record) hit.
    """
    hits = []
    needle = f'"{key}":'
    i = payload.find(needle)
    while i != -1:
        vstart = i + len(needle)
        val, end = balanced_json(payload, vstart)
        if val is not None:
            hits.append(_resolve(val, table))
        i = payload.find(needle, i + 1)
    if not hits:
        return None
    if want == "all":
        return hits
    # prefer the first decoded container (dict/list) — other hits can be
    # bare "$ref" strings pointing at the same data
    for h in hits:
        if isinstance(h, (dict, list)):
            return h
    return hits[0]
