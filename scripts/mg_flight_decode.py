#!/usr/bin/env python3
"""Decode Next.js RSC flight payload from a saved HTML file into one stream text."""
import json, re, sys

def decode_stream(html_path):
    html = open(html_path, encoding="utf-8", errors="replace").read()
    # chunks look like: self.__next_f.push([1,"...."]); possibly multiple string literals
    out = []
    for m in re.finditer(r"self\.__next_f\.push\(\s*\[\s*1\s*,\s*((?:\"(?:[^\"\\]|\\.)*\"\s*,?\s*)+)\]\s*\)", html):
        lits = re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(1))
        for lit in lits:
            try:
                out.append(json.loads('"' + lit + '"'))
            except Exception:
                pass
    return "".join(out)

if __name__ == "__main__":
    stream = decode_stream(sys.argv[1])
    open(sys.argv[2], "w", encoding="utf-8").write(stream)
    print(f"stream chars: {len(stream)}")
