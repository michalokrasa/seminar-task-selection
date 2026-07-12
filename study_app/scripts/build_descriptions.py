#!/usr/bin/env python3
"""Embed selected task descriptions into the frontend build.

Reads the original task.md problem statement from
../apps_selected_approved/<bucket>/<slug>/task.md and writes
study_app/src/data/descriptions.json so the Vite app can import them.

The task description shown to participants is the same regardless of
modality (nl vs. gherkin) — the modality only affects what *style* of
prompt the participant is asked to write.

Run this before `npm run build` or `npm run dev`.
"""

import json
from pathlib import Path

SELECTED_DIR = Path(__file__).resolve().parents[2] / "apps_selected_approved"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "src" / "data"


def read_file(path):
    if path.exists():
        return path.read_text(encoding="utf-8")
    return None


def trim_task_md(text):
    """Drop the leading '# CF .../.' title header, the
    '## Problem Description' header, and the trailing
    '## Contest Information' section (and everything after it)."""
    if text is None:
        return None

    lines = text.split("\n")

    # Drop the first line if it's the top-level title header.
    if lines and lines[0].startswith("# "):
        lines = lines[1:]

    # Drop the "## Contest Information" section onward.
    trimmed = []
    for line in lines:
        if line.startswith("## Contest Information"):
            break
        trimmed.append(line)

    return "\n".join(trimmed).strip()


def build():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    descriptions = {}

    for bucket in ("introductory", "interview", "competition"):
        bucket_dir = SELECTED_DIR / bucket
        if not bucket_dir.exists():
            continue
        for slug_dir in bucket_dir.iterdir():
            if not slug_dir.is_dir():
                continue
            slug = slug_dir.name
            task_md = read_file(slug_dir / "task.md")
            descriptions[slug] = trim_task_md(task_md)

    out_path = OUTPUT_DIR / "descriptions.json"
    out_path.write_text(json.dumps(descriptions, indent=2), encoding="utf-8")
    print(f"Wrote {len(descriptions)} task descriptions to {out_path}")


if __name__ == "__main__":
    build()
