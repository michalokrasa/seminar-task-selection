"""
Extract final selected tasks from data/tasks.parquet into selected/.

For each row in data/selection.csv, extracts instruction.md from the task_binary
and writes it to:
  selected/<bucket>/<slug>/task.md

Run:  python3 scripts/3_extract_selected.py
"""

from __future__ import annotations

import base64
import csv
import io
import re
import tarfile
from pathlib import Path

import pyarrow.parquet as pq

ROOT = Path(__file__).parent.parent
PARQUET_PATH = ROOT / "data" / "tasks.parquet"
SELECTION_CSV = ROOT / "data" / "selection.csv"
OUTPUT_DIR = ROOT / "selected"


def extract_instruction(blob: bytes) -> str | None:
    buf = io.BytesIO(blob)
    try:
        with tarfile.open(fileobj=buf, mode="r:gz") as tar:
            for m in tar.getmembers():
                if m.name == "instruction.md" and m.isfile():
                    f = tar.extractfile(m)
                    if f is not None:
                        return f.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  tar error: {e}")
    return None


def slugify(name: str) -> str:
    """Convert a task name like '1173_A. Nauuo and Votes' to a filesystem-safe slug."""
    slug = name.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = slug.strip("-")
    return slug


def load_selection() -> list[dict]:
    with SELECTION_CSV.open(newline="") as f:
        return list(csv.DictReader(f))


def main() -> None:
    rows = load_selection()
    wanted: dict[str, dict] = {r["path"]: r for r in rows}
    print(f"Loaded {len(wanted)} tasks from {SELECTION_CSV}")

    if not PARQUET_PATH.exists():
        raise SystemExit(f"Missing {PARQUET_PATH}. Run bash scripts/1_download.sh first.")

    print(f"Reading {PARQUET_PATH} ...")
    table = pq.read_table(PARQUET_PATH)
    paths = table.column("path").to_pylist()
    binaries = table.column("task_binary").to_pylist()
    print(f"  {table.num_rows} rows total")

    found = 0
    for path, blob in zip(paths, binaries):
        if path not in wanted:
            continue

        row = wanted[path]
        bucket = row["bucket"]
        name = row["name"]
        slug = slugify(name)

        if isinstance(blob, str):
            blob = base64.b64decode(blob)

        instruction = extract_instruction(blob)
        if instruction is None:
            print(f"  WARNING: could not extract instruction for {path}")
            continue

        out_dir = OUTPUT_DIR / bucket / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / "task.md"
        out_file.write_text(instruction, encoding="utf-8")
        print(f"  [{bucket}] {slug}  →  {out_file.relative_to(ROOT)}")
        found += 1

    print(f"\nDone. Extracted {found}/{len(wanted)} tasks to {OUTPUT_DIR}/")
    if found < len(wanted):
        missing = set(wanted) - {p for p, _ in zip(paths, binaries) if p in wanted}
        for m in missing:
            print(f"  NOT FOUND in parquet: {m}")


if __name__ == "__main__":
    main()
