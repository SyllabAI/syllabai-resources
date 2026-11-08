#!/usr/bin/env python3
"""rsc.py — minimal React Server Components (Next.js flight) payload parser.

MathsGenie is a Next.js app; per-topic resource data lives in the RSC flight
payload embedded in the HTML (`self.__next_f.push([1,"..."])` chunks). This
module reassembles the payload, splits it into rows, and resolves `$id` refs
so extractors can pull the typed envelopes (note / decks / lesson) verbatim.

Row grammar (subset, sufficient for MathsGenie):
  <hexid>:T<hexlen>,<raw text of exactly hexlen chars>   text chunk
  <hexid>:<json until newline>                            data row
"""
import json
import re

PUSH_RE = re.compile(
    r'self\.__next_f\.push\(\s*\[\s*1\s*,\s*"((?:[^"\\]|\\.)*)"\s*\]\s*\)'
)


def flight_payload(html: str) -> str:
    """Join all RSC flight chunks pushed in a page's HTML."""
    chunks = PUSH_RE.findall(html)
    return "".join(json.loads('"' + c + '"') for c in chunks)


def parse_rows(payload: str):
    """Split a flight payload into rows -> {row_id: value}.

    T rows map to raw str; JSON rows map to parsed objects (or the raw str
    if they fail to parse). Malformed tails are ignored.
    """
    table = {}
    i, n = 0, len(payload)
    while i < n:
        j = payload.find(":", i)
        if j == -1:
            break
        rid = payload[i:j]
        k = j + 1
        if rid and not re.fullmatch(r"[0-9a-f]+", rid):
            # unknown id shape — resync to next row boundary
            e = payload.find("\n", k)
            i = e + 1 if e != -1 else n
            continue
        if not rid:
            # hint row (":HL[...]" etc.) — consume payload, store nothing
            m2 = re.match(r"(H[LDEF]|[A-Z])\[", payload[k:k + 3])
            if not m2:
                e = payload.find("\n", k)
                i = e + 1 if e != -1 else n
                continue
        if k < n and payload[k] == "T":
            m = re.match(r"T([0-9a-f]+),", payload[k:])
            if m:
                ln = int(m.group(1), 16)  # UTF-16 code units (JS string length)
                start = k + m.end()
                # walk consuming exactly ln UTF-16 units (astral chars = 2 units)
                pos, units = start, 0
                while pos < n and units < ln:
                    units += 2 if ord(payload[pos]) > 0xFFFF else 1
                    pos += 1
                table[rid] = payload[start:pos]
                # Length-delimited T row: the next row may start immediately
                # (no newline separator). Set i and let the main loop validate.
                i = pos
                continue
        # JSON row: read to next newline
        e = payload.find("\n", k)
        if e == -1:
            e = n
        raw = payload[k:e]
        try:
            table[rid] = json.loads(raw)
        except Exception:
            table[rid] = raw
        i = e + 1
    return table


def _resolve(obj, table, seen, depth=0, memo=None):
    """Recursively resolve "$<id>" / "$L<id>" / "$@<id>" references (memoized)."""
    if depth > 64:
        return obj
    if isinstance(obj, str):
        if len(obj) > 1 and obj[0] == "$":
            body = obj[1:]
            m = re.match(r"(?:L|@|Q|E|F)*([0-9a-f]+)$", body)
            if m and m.group(1) in table and m.group(1) not in seen:
                if m.group(1) in memo:
                    return memo[m.group(1)]
                seen.add(m.group(1))
                out = _resolve(table[m.group(1)], table, seen, depth + 1, memo)
                seen.discard(m.group(1))
                memo[m.group(1)] = out
                return out
            if body in ("undefined", "infinity", "-infinity", "NaN"):
                return None
        return obj
    if isinstance(obj, list):
        return [_resolve(v, table, seen, depth + 1, memo) for v in obj]
    if isinstance(obj, dict):
        return {k: _resolve(v, table, seen, depth + 1, memo) for k, v in obj.items()}
    return obj


def find_dicts(obj, pred, results=None, depth=0, seen_ids=None):
    """Collect every dict in a tree satisfying pred(obj) (cycle-safe)."""
    if results is None:
        results = []
    if seen_ids is None:
        seen_ids = set()
    if depth > 64:
        return results
    if isinstance(obj, dict):
        sig = id(obj)
        if sig in seen_ids:
            return results
        seen_ids.add(sig)
        if pred(obj):
            results.append(obj)
        for v in obj.values():
            find_dicts(v, pred, results, depth + 1, seen_ids)
    elif isinstance(obj, list):
        for v in obj:
            find_dicts(v, pred, results, depth + 1, seen_ids)
    return results


def envelopes(html: str):
    """Parse a topic mode page -> (table, resolved_forest).

    Returns the resolved list of all parsed rows with $refs expanded, ready
    for envelope hunting.
    """
    payload = flight_payload(html)
    table = parse_rows(payload)
    memo = {}
    forest = []
    for rid, val in table.items():
        if isinstance(val, (dict, list)):
            forest.append(_resolve(val, table, {rid}, memo=memo))
    return table, forest


def hunt(forest, keyset):
    """Return dicts containing all keys in keyset, longest-nested last."""
    hits = find_dicts(forest, lambda d: all(k in d for k in keyset))
    # dedupe by identity of contents
    uniq, seen = [], set()
    for h in hits:
        sig = json.dumps(h, sort_keys=True, default=str)[:400]
        if sig not in seen:
            seen.add(sig)
            uniq.append(h)
    return uniq
