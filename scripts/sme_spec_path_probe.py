#!/usr/bin/env python3
"""Find the JSON path of courseExamSpecificationPdfLink in __NEXT_DATA__."""
import json
import re
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

URL = "https://www.savemyexams.com/igcse/chemistry/edexcel/19/"

req = urllib.request.Request(URL, headers={"User-Agent": UA})
html = urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")
m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
              html, re.S)
data = json.loads(m.group(1))

hits: list[tuple[str, str]] = []


def walk(node, path):
    if isinstance(node, dict):
        for k, v in node.items():
            if "Specification" in k or "specification" in k:
                s = v if isinstance(v, str) else json.dumps(v)[:200]
                hits.append((".".join(path + [k]), s))
            walk(v, path + [k])
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, path + [f"[{i}]"])


walk(data, [])
for p, v in hits[:40]:
    print(f"{p}\n    = {v[:220]}")
