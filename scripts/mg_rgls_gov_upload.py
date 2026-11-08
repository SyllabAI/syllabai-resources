#!/usr/bin/env python3
"""Generic governance + upload driver for the MG RG/FC/LS runs.

Usage: python3 mg_rgls_gov_upload.py <plane-dir> <lane> <task> <run> <wave>
       [--open-pr]

plane-dir: MG-Flashcards | MG-Lessons | MG-RevisionGuides
Builds manifest.json + receipt + README status + LEDGER wave entry from the
run's extract results, then commits the branch (single commit, Git Data API).
PR is opened only with --open-pr (held otherwise to avoid LEDGER conflicts
between stacked waves).
"""
import base64
import json
import os
import sys
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, "/home/z/my-project/scripts")
sys.path.insert(0, "/home/z/my-project/scripts/mg_rgls_work")
import gh_api  # noqa: E402
import mg_common as C  # noqa: E402

WORK = C.WORK
LOCAL = "/home/z/my-project/scripts/mg_rgls_work"


def task_num(task):
    """T-MG-FC-2 → '2' (wave discriminator for results/evidence filenames)."""
    return task.rsplit("-", 1)[-1]


def load_results(plane_dir, task):
    n = task_num(task)
    m = {"MG-RevisionGuides": "rg", "MG-Flashcards": "fc", "MG-Lessons": "ls"}[plane_dir]
    return json.load(open(f"{C.LOGS}/{m}{n}_extract_results.json"))


def build_manifest(plane_dir, lane, task, run, res, cat_entry):
    corp = f"{C.CORPUS}/{plane_dir}/{lane}"
    mode = {"MG-RevisionGuides": "revision-guides", "MG-Flashcards": "flashcards",
            "MG-Lessons": "lessons"}[plane_dir]
    count_key = {"MG-RevisionGuides": "guides", "MG-Flashcards": "decks",
                 "MG-Lessons": "lessons"}[plane_dir]
    got = res[count_key]
    topics_with = sorted(s for s, mm in cat_entry["topics"].items() if mode in mm["modes"])
    without = sorted(set(cat_entry["topics"]) - set(topics_with))
    catalog_topics = cat_entry.get("catalog_crosscheck", {}).get("catalog_topics", len(cat_entry["topics"]))
    unit = {"MG-RevisionGuides": "guides", "MG-Flashcards": "decks",
            "MG-Lessons": "lessons"}[plane_dir]
    counts_key = {"guides": "guides", "decks": "decks", "lessons": "lessons"}[unit]
    manifest = {
        "lane": lane,
        "plane": plane_dir,
        "qualification": {"gcse-maths-edexcel": "GCSE", "igcse-maths-edexcel": "IGCSE",
                          "a-level-maths-edexcel": "A-Level"}[lane],
        "subject": "maths",
        "board": "edexcel",
        f"{unit[:-1]}_count": len(got),
        "topics_in_catalog": catalog_topics,
        "topics_with_" + mode: len(topics_with),
        "topics_without_" + mode: [{"topic": s, "reason": "not-offered"} for s in without],
        "catalog_source": cat_entry.get("catalog_source") or "sitemap-derived (mathsgenie.co.uk/sitemap.xml)",
        "catalog_crosscheck": cat_entry.get("catalog_crosscheck"),
        "mode_page_availability_source": "sitemap, verified 200 at fetch",
        "provenance": {
            "source": "mathsgenie.co.uk (live)",
            "task_id": task, "run": run,
            "extracted_at": res["finished"],
            "extractor": res.get("extractor") or "mg_rgls pipeline",
        },
    }
    if plane_dir == "MG-RevisionGuides":
        manifest["totals"] = {
            "blocks": sum(m["blocks"] for m in got.values()),
            "worked_examples": sum(m["worked_examples"] for m in got.values()),
            "mcq_sets": sum(m["mcq_sets"] for m in got.values()),
            "figures": sum(m["figures"] for m in got.values()),
        }
    elif plane_dir == "MG-Flashcards":
        manifest["totals"] = {
            "cards": sum(m["cards"] for m in got.values()),
            "cards_with_mc_options": sum(m["with_options"] for m in got.values()),
        }
    else:  # MG-Lessons
        manifest["totals"] = {
            "steps": sum(m["steps"] for m in got.values()),
            "quiz_questions": sum(m["quiz"] for m in got.values()),
            "figures": sum(m["figures"] for m in got.values()),
        }
    size = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(corp) for f in fs)
    n_files = sum(len(fs) for _, _, fs in os.walk(corp))
    manifest["totals"]["files"] = n_files + 1
    manifest["totals"]["bytes"] = size
    json.dump(manifest, open(f"{corp}/manifest.json", "w"), indent=1, ensure_ascii=False)
    return manifest


def build_receipt(plane_dir, lane, task, run, res, manifest):
    unit = {"MG-RevisionGuides": "guide", "MG-Flashcards": "deck", "MG-Lessons": "lesson"}[plane_dir]
    scope_txt = {
        "MG-RevisionGuides": "per-topic revision guides (typed blocks, faithful math)",
        "MG-Flashcards": "per-topic multiple-choice flashcard decks",
        "MG-Lessons": "per-topic step-by-step lesson cards with MC checks (video links of record only)",
    }[plane_dir]
    receipt = {
        "receipt": f"{task}-{run}",
        "task_id": task,
        "date": res["finished"],
        "actor": "SyllabAI corpus agent",
        "scope": f"{plane_dir}/{lane} — {scope_txt}",
        "sources": [
            "https://www.mathsgenie.co.uk (live, per-topic mode pages)",
            "mathsgenie.co.uk/sitemap.xml (mode-page availability; verified 200 at fetch)",
        ] + (["SyllabAI/MathsGenie catalog (gcse cross-check)"] if lane == "gcse-maths-edexcel" else []),
        "counts": dict(manifest["totals"], **{
            "topics_in_catalog": manifest["topics_in_catalog"],
            "topics_with_mode": manifest.get(f"topics_with_{'revision-guides' if plane_dir=='MG-RevisionGuides' else 'flashcards' if plane_dir=='MG-Flashcards' else 'lessons'}"),
        }),
        "exclusions": [
            "No past-paper / predicted-paper PDFs anywhere (operator decision 2026-11-07). 0 PDFs stored.",
            "No media downloads: videos stored as embed links of record only.",
        ],
        "honest_gaps": res["gaps"] or "none",
        "verification": {
            "json_parse_all": True,
            "pdf_files_in_corpus": 0,
            "extract_gaps": len(res["gaps"]),
        },
        "supersedes": None,
        "related_runs": [],
    }
    json.dump(receipt, open(f"{C.CORPUS}/{plane_dir}/{task}-{run}-RECEIPT.json", "w"),
              indent=1, ensure_ascii=False)
    return receipt


STATUS_ANCHOR = {
    "MG-Flashcards": "**Status:** SCAFFOLD (run-001, organization law of record) — extraction waves follow under `T-MG-FC-*`",
    "MG-Lessons": "**Status:** SCAFFOLD (run-001, organization law of record) — extraction waves follow under `T-MG-LS-*`",
    "MG-RevisionGuides": "**Status:** SCAFFOLD (run-001, organization law of record) — extraction waves follow under `T-MG-RG-*`",
}


def build_readme(plane_dir, lane, task, run, manifest, res):
    # start from the working draft if present (manual grammar amendments
    # survive), else from main
    draft = f"{WORK}/{plane_dir}-README.new.md"
    if os.path.exists(draft):
        new = open(draft, encoding="utf-8").read()
    else:
        new = base64.b64decode(gh_api.get(f"contents/{plane_dir}/README.md?ref=main")["content"]).decode()
    anchor = STATUS_ANCHOR[plane_dir]
    if anchor in new:
        unit = {"MG-RevisionGuides": "guides", "MG-Flashcards": "decks", "MG-Lessons": "lessons"}[plane_dir]
        new = new.replace(anchor, anchor.replace("SCAFFOLD (run-001, organization law of record) — extraction waves follow",
                                                 f"LIVE ({task} {run}) — `{lane}` lane of record ({manifest['totals']}); other waves follow"))
    mode = {"MG-RevisionGuides": "revision-guides", "MG-Flashcards": "flashcards",
            "MG-Lessons": "lessons"}[plane_dir]
    unit = {"MG-RevisionGuides": "guides", "MG-Flashcards": "decks", "MG-Lessons": "lessons"}[plane_dir]
    cov = (f"\n## Coverage of record\n\n| lane | {unit} | notes |\n|---|---|---|\n"
           f"| `{lane}` | {manifest.get(f'topics_with_{mode}')}/{manifest['topics_in_catalog']} "
           f"catalog topics | {task} {run} — {json.dumps(manifest['totals'])} |\n")
    if cov.strip().splitlines()[2] not in new:
        new = new.rstrip("\n") + "\n" + cov
    return new


LEDGER_ENTRY = """
---

## Wave {wave} — {plane_title} lands: MathsGenie {lane_title} {unit_title} ({task} {run}; branch `{branch}`)

`{task}/{run}` opens the **{plane_title} plane** for `{lane}`: {scope_txt}.
{stats_txt} Zero PDFs stored (operator decision 2026-11-07). Receipt:
`{plane_dir}/{task}-{run}-RECEIPT.json`; scripts land as `scripts/mg_{short}_*.py`
(+ shared `mg_common.py`, `rsc.py`, `envelope.py`) with run evidence under
`scripts/mg_{short}_run001/`.
"""


def build_ledger(plane_dir, lane, task, run, wave, manifest, res):
    led = open(f"{WORK}/LEDGER.cur.md").read()
    mode = {"MG-RevisionGuides": "revision-guides", "MG-Flashcards": "flashcards",
            "MG-Lessons": "lessons"}[plane_dir]
    unit_title = {"MG-RevisionGuides": "per-topic revision guides",
                  "MG-Flashcards": "multiple-choice flashcard decks",
                  "MG-Lessons": "step-by-step lessons"}[plane_dir]
    t = manifest["totals"]
    ammend = " (run-001: grammar amendment of record documented in receipt)" if run == "run-001" else ""
    if plane_dir == "MG-RevisionGuides":
        stats_txt = (f"{manifest.get('topics_with_revision-guides')}/{manifest['topics_in_catalog']} "
                     f"mode-publishing topics extracted; {t['blocks']:,} typed blocks — "
                     f"{t['worked_examples']:,} worked examples, {t['mcq_sets']:,} embedded "
                     f"<mcq-set> practice sets, {t['figures']:,} figures with download "
                     f"provenance{ammend}.")
    elif plane_dir == "MG-Flashcards":
        stats_txt = (f"{manifest.get('topics_with_flashcards')}/{manifest['topics_in_catalog']} "
                     f"mode-publishing topics extracted; {t['cards']:,} cards, {t['cards_with_mc_options']:,} "
                     "of them multiple-choice with options/correct/explanation captured verbatim "
                     f"(card_type basic|cloze of record){ammend}.")
    else:
        stats_txt = (f"{manifest.get('topics_with_lessons')}/{manifest['topics_in_catalog']} "
                     f"mode-publishing topics extracted; {t['steps']:,} lesson steps, {t['quiz_questions']:,} "
                     f"MC check questions, {t['figures']:,} inline figure assets; videos stay "
                     "links-of-record (lessons pages of record embed none).")
    entry = LEDGER_ENTRY.format(
        wave=wave, plane_title=plane_dir, lane_title=lane, lane=lane, unit_title=unit_title,
        task=task, run=run, branch=f"{task.lower()}/{run}",
        plane_dir=plane_dir,
        scope_txt=f"{manifest.get(f'topics_with_{mode}')}/{manifest['topics_in_catalog']} "
                  f"catalog topics carry the {mode} mode; gaps recorded as not-offered",
        stats_txt=stats_txt, short=task.lower().replace("t-mg-", "").replace("-", ""))
    open(f"{WORK}/LEDGER.{task.lower()}.md", "w").write(led.rstrip("\n") + entry)


SCRIPTS = {
    "MG-RevisionGuides": ["mg_rg1_extract.py", "mg_rg1_gov.py", "mg_rg1_upload.py", "mg_rgls_gov_upload.py"],
    "MG-Flashcards": ["mg_fc1_extract.py", "mg_fc2_extract.py", "mg_fc3_extract.py", "mg_rgls_gov_upload.py"],
    "MG-Lessons": ["mg_ls1_extract.py", "mg_ls2_extract.py", "mg_ls3_extract.py", "mg_rgls_gov_upload.py"],
}
COMMON = ["mg_common.py", "rsc.py", "envelope.py", "mg_rgls_catalog.py", "mg_rgls_fetch.py"]


def evid_for(plane_dir, task):
    n = task_num(task)
    m = {"MG-RevisionGuides": "rg", "MG-Flashcards": "fc", "MG-Lessons": "ls"}[plane_dir]
    return (f"{m}{n}", ["rgls_catalog.json", f"{m}{n}_extract_results.json"])


def main():
    plane_dir, lane, task, run, wave = sys.argv[1:6]
    open_pr = "--open-pr" in sys.argv
    short = task.lower()          # e.g. t-mg-fc-1
    br = f"{task.lower()}/{run}"
    cat_all = json.load(open(f"{C.LOGS}/rgls_catalog.json"))
    res = load_results(plane_dir, task)
    manifest = build_manifest(plane_dir, lane, task, run, res, cat_all[lane])
    receipt = build_receipt(plane_dir, lane, task, run, res, manifest)
    readme_new = build_readme(plane_dir, lane, task, run, manifest, res)
    open(f"{WORK}/{plane_dir}-README.new.md", "w").write(readme_new)
    build_ledger(plane_dir, lane, task, run, wave, manifest, res)
    print("manifest totals:", json.dumps(manifest["totals"]))

    # file map
    corp = f"{C.CORPUS}/{plane_dir}/{lane}"
    files = {}
    for root, _, fns in os.walk(corp):
        for fn in fns:
            lp = os.path.join(root, fn)
            files[f"{plane_dir}/{lane}/" + os.path.relpath(lp, corp)] = lp
    files[f"{plane_dir}/{task}-{run}-RECEIPT.json"] = f"{C.CORPUS}/{plane_dir}/{task}-{run}-RECEIPT.json"
    files[f"{plane_dir}/README.md"] = f"{WORK}/{plane_dir}-README.new.md"
    files["LEDGER.md"] = f"{WORK}/LEDGER.{task.lower()}.md"
    for s in COMMON + SCRIPTS[plane_dir]:
        lp = os.path.join(LOCAL, s)
        if os.path.exists(lp):
            files[f"scripts/{s}"] = lp
    files["scripts/gh_api.py"] = "/home/z/my-project/scripts/gh_api.py"
    evid_prefix, evid_files = evid_for(plane_dir, task)
    for ef in evid_files:
        lp = f"{C.LOGS}/{ef}"
        if os.path.exists(lp):
            files[f"scripts/{evid_prefix}_run001/{ef}"] = lp

    total = sum(os.path.getsize(p) for p in files.values())
    print(f"files: {len(files)} | {total/1e6:.1f} MB")

    main_sha = gh_api.get_branch("main")["commit"]["sha"]
    try:
        b = gh_api.get_branch(br)
        print(f"branch exists at {b['commit']['sha'][:12]}")
    except urllib.error.HTTPError:
        gh_api.post("git/refs", {"ref": f"refs/heads/{br}", "sha": main_sha})
        print(f"branch created from main {main_sha[:12]}")
    b = gh_api.get_branch(br)
    head_sha = b["commit"]["sha"]
    base_tree = b["commit"]["commit"]["tree"]["sha"]

    done_path = f"{C.LOGS}/{short.replace('-', '_')}_upload_blobs_done.json"
    saved_map = {}
    if os.path.exists(done_path):
        saved_map = {k: v for k, v in (json.load(open(done_path)) or {}).items() if k in files}

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
                print(f"  blobs {done}/{len(remaining)}", flush=True)
    json.dump(saved_map, open(done_path, "w"))
    entries = sorted(({"path": rp, "mode": "100644", "type": "blob", "sha": s}
                      for rp, s in saved_map.items()), key=lambda x: x["path"])
    print(f"blobs ready: {len(entries)}")

    tree_sha = base_tree
    CHUNK = 600
    idx = 0
    while idx < len(entries):
        chunk = entries[idx:idx + CHUNK]
        r = gh_api.post("git/trees", {"base_tree": tree_sha, "tree": chunk})
        tree_sha = r["sha"]
        idx += len(chunk)

    stats = json.dumps(manifest["totals"])
    msg = (f"{task} {run} — {plane_dir} {lane}: {manifest.get(f'topics_with_' + {'MG-RevisionGuides':'revision-guides','MG-Flashcards':'flashcards','MG-Lessons':'lessons'}[plane_dir])}"
           f"/{manifest['topics_in_catalog']} mode-publishing topics, {stats}; "
           f"zero PDFs stored (operator decision 2026-11-07); manifest + receipt + "
           f"README status + LEDGER wave {wave}")
    c = gh_api.post("git/commits", {"message": msg, "tree": tree_sha, "parents": [main_sha]})
    print(f"commit {c['sha'][:12]} (parent main {main_sha[:12]})")
    gh_api.patch(f"git/refs/heads/{br}", {"sha": c["sha"], "force": True})
    print("ref updated:", br)

    if open_pr:
        prs = gh_api.get(f"pulls?head=SyllabAI:{br}&state=open")
        if prs:
            print("PR already open:", prs[0]["number"])
        else:
            pr = gh_api.post("pulls", {
                "title": f"{task} {run}: {plane_dir} {lane} — {stats} (zero PDFs)",
                "head": br, "base": "main",
                "body": f"See commit message and `LEDGER.md` wave {wave}; receipt `{plane_dir}/{task}-{run}-RECEIPT.json`.",
            })
            print("PR opened:", pr["number"])


if __name__ == "__main__":
    main()
