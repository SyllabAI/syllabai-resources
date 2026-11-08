#!/usr/bin/env python3
"""T-MG-RG-1 run-001 — bulk-commit the MG-RevisionGuides gcse-maths-edexcel
lane (+ receipt, README status, LEDGER wave 28, scripts, evidence) via the
Git Data API; then open the PR. Single commit, adapted from T-MG-QB-3."""
import base64
import json
import os
import sys
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, "/home/z/my-project/scripts")
sys.path.insert(0, "/home/z/my-project/scripts/mg_rgls_work")
import gh_api  # noqa: E402

WORK = "/home/z/my-project/mg_work"
PLANE = "MG-RevisionGuides"
CORPUS = f"{WORK}/corpus/{PLANE}/gcse-maths-edexcel"
BR = "t-mg-rg-1/run-001"
BASE_BRANCH = "main"
LOCAL = "/home/z/my-project/scripts/mg_rgls_work"

MSG = ("T-MG-RG-1 run-001 — MG-RevisionGuides gcse-maths-edexcel: 132/132 guides "
       "of record (134 catalog topics, 2 not-offered), 1,680 typed blocks "
       "(135 worked examples, 292 mcq-sets), 312 figures, faithful-math markdown "
       "renders; zero PDFs stored (operator decision 2026-11-07); block grammar "
       "amendment (figure, mcq-set) documented in receipt; manifest + receipt + "
       "README status + LEDGER wave 28")

SCRIPT_MAP = {
    f"{LOCAL}/mg_common.py": "scripts/mg_common.py",
    f"{LOCAL}/mg_rgls_catalog.py": "scripts/mg_rgls_catalog.py",
    f"{LOCAL}/mg_rgls_fetch.py": "scripts/mg_rgls_fetch.py",
    f"{LOCAL}/rsc.py": "scripts/rsc.py",
    f"{LOCAL}/envelope.py": "scripts/envelope.py",
    f"{LOCAL}/mg_rg1_extract.py": "scripts/mg_rg1_extract.py",
    f"{LOCAL}/mg_rg1_gov.py": "scripts/mg_rg1_gov.py",
    f"{LOCAL}/mg_rg1_upload.py": "scripts/mg_rg1_upload.py",
    "/home/z/my-project/scripts/gh_api.py": "scripts/gh_api.py",
}
EVIDENCE = {
    "scripts/mg_rg1_run001/rgls_catalog.json": f"{WORK}/logs/rgls_catalog.json",
    "scripts/mg_rg1_run001/rg1_extract_results.json": f"{WORK}/logs/rg1_extract_results.json",
}


def build_file_map():
    files = {}
    for root, _, fns in os.walk(CORPUS):
        for fn in fns:
            lp = os.path.join(root, fn)
            rp = os.path.relpath(lp, CORPUS)
            files[f"{PLANE}/gcse-maths-edexcel/{rp}"] = lp
    files[f"{PLANE}/T-MG-RG-1-run-001-RECEIPT.json"] = f"{WORK}/corpus/{PLANE}/T-MG-RG-1-run-001-RECEIPT.json"
    files[f"{PLANE}/README.md"] = f"{WORK}/RG-README.new.md"
    files["LEDGER.md"] = f"{WORK}/LEDGER.rg1.md"
    for src, dst in SCRIPT_MAP.items():
        if not os.path.exists(src):
            raise SystemExit(f"missing script {src}")
        files[dst] = src
    for rp, lp in EVIDENCE.items():
        files[rp] = lp
    return files


def prepare_readme_and_ledger():
    """Fetch current README + LEDGER from main, patch, stage."""
    cur = base64.b64decode(gh_api.get(f"contents/{PLANE}/README.md?ref=main")["content"]).decode()
    new = cur.replace(
        "**Status:** SCAFFOLD (run-001, organization law of record) — extraction waves follow under `T-MG-RG-*`",
        "**Status:** LIVE (T-MG-RG-1 run-001) — `gcse-maths-edexcel` lane of record (132/132 guides); other waves follow under `T-MG-RG-*`",
    )
    assert new != cur, "README status anchor not found"
    cov = (
        "\n## Coverage of record\n\n"
        "| lane | guides | notes |\n|---|---|---|\n"
        "| `gcse-maths-edexcel` | 132/134 catalog topics (2 not-offered) | "
        "T-MG-RG-1 run-001 — 1,680 blocks (135 worked examples, 292 mcq-sets), "
        "312 figures; grammar amended with `figure` + `mcq-set` blocks |\n"
    )
    if "## Coverage of record" not in new:
        new = new.rstrip("\n") + "\n" + cov
    open(f"{WORK}/RG-README.new.md", "w").write(new)

    led = open(f"{WORK}/LEDGER.cur.md").read()
    entry = """
---

## Wave 28 — MG-RevisionGuides lands: the MathsGenie GCSE Maths (Edexcel) per-topic revision guides (T-MG-RG-1 run-001; branch `t-mg-rg-1/run-001`)

`T-MG-RG-1/run-001` opens the **MG-RevisionGuides plane**: per-topic revision
guides for `gcse-maths-edexcel`, the first lane of record in the learn plane.
Catalog: 134 GCSE Maths (Edexcel) topics (mirror `topics-edexcel.json`,
cross-checked clean against the site sitemap); **132/132 topics that publish a
revision guide extracted, 2 recorded `not-offered`** (never manufactured —
AGENT.md rule 3). Each guide lands as `revision-guide.json` (typed blocks:
heading / paragraph / formula / worked-example / exam-tip, faithful verbatim
math) + script-generated `revision-guide.md` + numbered `assets/` figures with
download provenance; 1,680 blocks total (135 worked examples, 292 embedded
`<mcq-set>` practice sets, 312 figures), ~6.7 MB, zero PDFs (operator decision
2026-11-07). Grammar amendments of record (documented in the receipt): `figure`
and `mcq-set` block kinds. Extraction rides the site's own RSC flight payloads
(parser: `scripts/rsc.py` + `scripts/envelope.py`); mode-page availability from
the site sitemap, every page fetched 200. Receipt:
`MG-RevisionGuides/T-MG-RG-1-run-001-RECEIPT.json`; scripts land as
`scripts/mg_rg1_*.py` (+ shared `mg_common.py`, `rsc.py`, `envelope.py`) with
run evidence under `scripts/mg_rg1_run001/`.
"""
    open(f"{WORK}/LEDGER.rg1.md", "w").write(led.rstrip("\n") + entry)
    print("README + LEDGER staged")


PR_TITLE = ("T-MG-RG-1 run-001: MG-RevisionGuides gcse-maths-edexcel — 132 guides / "
            "1,680 blocks (zero PDFs)")

PR_BODY = """## Scope

`T-MG-RG-1/run-001` opens the **MG-RevisionGuides plane**: per-topic revision guides for `gcse-maths-edexcel` — the learn plane's first lane of record, following the QB lanes (#315/#316/#318) under the same organization law. **Zero PDFs stored** (operator decision 2026-11-07).

## What lands

- **132/132 guides** (every catalog topic that publishes one; 2 of 134 recorded `not-offered`) → `revision-guide.json` (typed blocks, verbatim math) + `revision-guide.md` render + numbered `assets/` figures.
- **1,680 typed blocks**: 135 worked examples · 292 embedded `<mcq-set>` practice sets · 312 figures · ~6.7 MB · **0 PDFs**.
- Grammar amendments of record: `figure` and `mcq-set` block kinds (documented in the receipt).
- Source chain: live `revision-guides` mode pages (RSC flight payload parser `scripts/rsc.py` + `scripts/envelope.py`), sitemap mode availability, mirror catalog cross-check clean.

## Verification

- All 132 JSON parse; all 312 figure refs resolve on disk; 0 extract gaps.
- `manifest.json` carries coverage + provenance; receipt `T-MG-RG-1-run-001-RECEIPT.json`; LEDGER wave 28 appended.
"""


def main():
    prepare_readme_and_ledger()
    files = build_file_map()
    total = sum(os.path.getsize(p) for p in files.values())
    print(f"files: {len(files)} | {total/1e6:.1f} MB")

    main_sha = gh_api.get_branch(BASE_BRANCH)["commit"]["sha"]
    try:
        br = gh_api.get_branch(BR)
        print(f"branch exists at {br['commit']['sha'][:12]}")
    except urllib.error.HTTPError:
        gh_api.post("git/refs", {"ref": f"refs/heads/{BR}", "sha": main_sha})
        br = gh_api.get_branch(BR)
        print(f"branch created from main {main_sha[:12]}")
    head_sha = br["commit"]["sha"]
    base_tree = br["commit"]["commit"]["tree"]["sha"]

    entries_path = f"{WORK}/logs/rg1_upload_entries.json"
    done_path = f"{WORK}/logs/rg1_upload_blobs_done.json"
    saved_map = {}
    if os.path.exists(done_path):
        saved_map = json.load(open(done_path)) or {}
        saved_map = {k: v for k, v in saved_map.items() if k in files}
    print(f"checkpoint: {len(saved_map)} blobs already created")

    def make_blob(rp, lp):
        sha = saved_map.get(rp)
        if sha:
            return {"path": rp, "mode": "100644", "type": "blob", "sha": sha}
        data = open(lp, "rb").read()
        r = gh_api.post("git/blobs", {"content": base64.b64encode(data).decode(), "encoding": "base64"})
        return {"path": rp, "mode": "100644", "type": "blob", "sha": r["sha"]}

    remaining = {rp: lp for rp, lp in sorted(files.items()) if rp not in saved_map}
    print(f"blobs to create: {len(remaining)}")
    done = 0
    with ThreadPoolExecutor(max_workers=12) as ex:
        futs = {ex.submit(make_blob, rp, lp): rp for rp, lp in remaining.items()}
        for fu in as_completed(futs):
            e = fu.result()
            saved_map[e["path"]] = e["sha"]
            done += 1
            if done % 200 == 0:
                json.dump(saved_map, open(done_path, "w"))
                print(f"  blobs {done}/{len(remaining)} (checkpointed)", flush=True)
    json.dump(saved_map, open(done_path, "w"))
    entries = sorted(({"path": rp, "mode": "100644", "type": "blob", "sha": s}
                      for rp, s in saved_map.items()), key=lambda x: x["path"])
    print(f"blobs ready: {len(entries)}")
    json.dump(entries, open(entries_path, "w"))

    tree_sha = base_tree
    CHUNK = 600
    idx = 0
    while idx < len(entries):
        chunk = entries[idx:idx + CHUNK]
        r = gh_api.post("git/trees", {"base_tree": tree_sha, "tree": chunk})
        tree_sha = r["sha"]
        idx += len(chunk)
        print(f"  tree chunk -> {tree_sha[:12]}")

    c = gh_api.post("git/commits", {"message": MSG, "tree": tree_sha, "parents": [head_sha]})
    print(f"commit {c['sha'][:12]}")
    gh_api.patch(f"git/refs/heads/{BR}", {"sha": c["sha"], "force": False})
    print("ref updated")

    # PR (idempotent-ish: check for existing open PR for this head)
    prs = gh_api.get(f"pulls?head=SyllabAI:{BR}&state=open")
    if prs:
        print("PR already open:", prs[0]["number"])
        return
    pr = gh_api.post("pulls", {"title": PR_TITLE, "head": BR, "base": BASE_BRANCH,
                               "body": PR_BODY})
    print("PR opened:", pr["number"])


if __name__ == "__main__":
    main()
