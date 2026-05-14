"""
Filter and bucket tasks from open-thoughts/CodeContests for Gherkin translation.

Pipeline:
  1. Read data/tasks.parquet (downloaded separately via 1_download.sh).
  2. For each row, decode the gzipped tar in `task_binary` and extract instruction.md.
  3. Parse the "Contest Information" section to obtain Codeforces Rating + Tags.
  4. Keep only Codeforces-sourced rows (Rating > 0).
  5. Apply tag allow/block lists and a math-iness keyword penalty.
  6. Bucket by Rating: easy 800-1100, medium 1300-1600, hard 1800-2200.
  7. Emit data/candidates_{easy,medium,hard}.md plus data/index.csv.

Run:  python3 scripts/2_select_tasks.py
"""

from __future__ import annotations

import base64
import csv
import io
import random
import re
import tarfile
from dataclasses import dataclass, field
from pathlib import Path

import pyarrow.parquet as pq

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
PARQUET_PATH = DATA_DIR / "tasks.parquet"
OUTPUT_DIR = DATA_DIR / "candidates"
INDEX_PATH = DATA_DIR / "index.csv"

# --- Difficulty buckets (Codeforces Rating) ---
BUCKETS = {
    "easy":   (800, 1100),
    "medium": (1300, 1600),
    "hard":   (1800, 2200),
}
PER_BUCKET = 12  # candidates emitted per bucket; user picks final 5 by hand
RANDOM_SEED = 7

# --- Tag filters ---
ALLOWED_TAGS = {
    "implementation",
    "strings",
    "greedy",
    "brute force",
    "sortings",
    "constructive algorithms",
    "two pointers",
    "*special",
    "data structures",
}
# Tags that MUST be present (intersection must be non-empty). Empty set disables.
REQUIRED_TAGS = {"implementation"}
FORBIDDEN_TAGS = {
    "math",
    "number theory",
    "combinatorics",
    "probabilities",
    "geometry",
    "dp",
    "graphs",
    "trees",
    "dsu",
    "graph matchings",
    "flows",
    "bitmasks",
    "fft",
    "matrices",
    "divide and conquer",
    "meet-in-the-middle",
    "ternary search",
    "binary search",
    "shortest paths",
    "dfs and similar",
    "string suffix structures",
    "hashing",
    "games",
    "expression parsing",
}

# --- Math-iness penalty keywords ---
MATH_KEYWORDS = [
    r"\bmod\b", r"\bmodulo\b", r"10\^9\s*\+\s*7", r"998244353",
    r"\bprime\b", r"\bgcd\b", r"\blcm\b", r"factorial",
    r"permutation", r"probability", r"expected value",
    r"binomial", r"fibonacci", r"matrix", r"polynomial",
]
MATH_RE = re.compile("|".join(MATH_KEYWORDS), re.IGNORECASE)
MATH_PENALTY_THRESHOLD = 2  # drop if more than this many math hits


@dataclass
class Task:
    path: str
    name: str = ""
    rating: int = 0
    contest_id: int = 0
    problem_index: str = ""
    tags: list[str] = field(default_factory=list)
    instruction: str = ""
    math_hits: int = 0


# Match: "- **Rating**: 1600", "- **Tags**: dp, math", etc.
META_RE = re.compile(r"-\s*\*\*([^*]+)\*\*:\s*(.+)")
NAME_RE = re.compile(r"^#\s+(.+)", re.MULTILINE)


def parse_instruction(text: str, path: str) -> Task:
    t = Task(path=path, instruction=text)

    # First-line "# foo" header
    m = NAME_RE.search(text)
    if m:
        t.name = m.group(1).strip()

    # Slice the Contest Information block
    ci_start = text.find("## Contest Information")
    if ci_start == -1:
        return t
    ci_end = text.find("\n## ", ci_start + 1)
    block = text[ci_start:ci_end] if ci_end != -1 else text[ci_start:]

    for key, val in META_RE.findall(block):
        key = key.strip().lower()
        val = val.strip()
        if key == "rating":
            try:
                t.rating = int(val)
            except ValueError:
                pass
        elif key == "contest id":
            try:
                t.contest_id = int(val)
            except ValueError:
                pass
        elif key == "problem index":
            t.problem_index = val
        elif key == "tags":
            if val.lower() == "none":
                t.tags = []
            else:
                t.tags = [tg.strip().lower() for tg in val.split(",") if tg.strip()]

    t.math_hits = len(MATH_RE.findall(text))
    return t


def extract_instruction_from_blob(blob: bytes) -> str | None:
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


def is_acceptable(t: Task) -> tuple[bool, str]:
    if t.rating <= 0:
        return False, "no_rating"
    if not t.tags:
        return False, "no_tags"
    tagset = set(t.tags)
    if tagset & FORBIDDEN_TAGS:
        return False, f"forbidden_tag:{','.join(sorted(tagset & FORBIDDEN_TAGS))}"
    if not (tagset & ALLOWED_TAGS):
        return False, "no_allowed_tag"
    if REQUIRED_TAGS and not (tagset & REQUIRED_TAGS):
        return False, "missing_required_tag"
    if t.math_hits > MATH_PENALTY_THRESHOLD:
        return False, f"math_hits={t.math_hits}"
    if "<image>" in t.instruction.lower():
        return False, "has_image_placeholder"
    # Heuristic: not too long, not too short
    if len(t.instruction) < 400:
        return False, "instruction_too_short"
    if len(t.instruction) > 6000:
        return False, "instruction_too_long"
    return True, "ok"


def bucket_of(rating: int) -> str | None:
    for name, (lo, hi) in BUCKETS.items():
        if lo <= rating <= hi:
            return name
    return None


def load_tasks() -> list[Task]:
    if not PARQUET_PATH.exists():
        raise SystemExit(f"Missing {PARQUET_PATH}. Run bash scripts/1_download.sh first.")

    print(f"Reading {PARQUET_PATH} ...")
    table = pq.read_table(PARQUET_PATH)
    n = table.num_rows
    print(f"  {n} rows; columns = {table.column_names}")

    paths = table.column("path").to_pylist()
    binaries = table.column("task_binary").to_pylist()

    tasks: list[Task] = []
    for i, (path, blob) in enumerate(zip(paths, binaries)):
        if i % 500 == 0:
            print(f"  parsing {i}/{n}")
        if isinstance(blob, str):
            blob = base64.b64decode(blob)
        text = extract_instruction_from_blob(blob)
        if text is None:
            continue
        tasks.append(parse_instruction(text, path))
    print(f"  parsed {len(tasks)} instructions")
    return tasks


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    tasks = load_tasks()

    # Bucket and filter
    buckets: dict[str, list[Task]] = {k: [] for k in BUCKETS}
    rejected_counts: dict[str, int] = {}
    accepted = 0
    for t in tasks:
        b = bucket_of(t.rating)
        if b is None:
            rejected_counts["wrong_bucket"] = rejected_counts.get("wrong_bucket", 0) + 1
            continue
        ok, reason = is_acceptable(t)
        if not ok:
            rejected_counts[reason] = rejected_counts.get(reason, 0) + 1
            continue
        buckets[b].append(t)
        accepted += 1

    print(f"\nAccepted {accepted} tasks across buckets:")
    for k, v in buckets.items():
        print(f"  {k:<7} {len(v):>5}  (rating {BUCKETS[k][0]}–{BUCKETS[k][1]})")
    print("\nRejection reasons (top 10):")
    for reason, count in sorted(rejected_counts.items(), key=lambda x: -x[1])[:10]:
        print(f"  {count:>5}  {reason}")

    # Random sample per bucket
    rng = random.Random(RANDOM_SEED)
    selected: dict[str, list[Task]] = {}
    for k, lst in buckets.items():
        rng.shuffle(lst)
        # Sort by lowest math_hits first within the shuffled list
        lst.sort(key=lambda t: t.math_hits)
        selected[k] = lst[:PER_BUCKET]

    # Emit per-bucket markdown files
    for k, picks in selected.items():
        out = OUTPUT_DIR / f"candidates_{k}.md"
        with out.open("w") as f:
            lo, hi = BUCKETS[k]
            f.write(f"# {k.capitalize()} candidates (rating {lo}–{hi})\n\n")
            f.write(f"{len(picks)} tasks. Pick 5 by hand.\n\n---\n\n")
            for t in picks:
                f.write(f"## {t.path} — {t.name}\n\n")
                f.write(f"- **Rating**: {t.rating}\n")
                f.write(f"- **Contest**: {t.contest_id}{t.problem_index}\n")
                f.write(f"- **Tags**: {', '.join(t.tags)}\n")
                f.write(f"- **Math-keyword hits**: {t.math_hits}\n")
                f.write(f"- **Length**: {len(t.instruction)} chars\n\n")
                f.write("<details><summary>Full instruction</summary>\n\n")
                f.write(t.instruction)
                f.write("\n\n</details>\n\n---\n\n")
        print(f"Wrote {out}")

    # Emit index.csv
    with INDEX_PATH.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["bucket", "path", "name", "rating", "tags", "math_hits", "length"])
        for k, picks in selected.items():
            for t in picks:
                w.writerow([k, t.path, t.name, t.rating,
                            ";".join(t.tags), t.math_hits, len(t.instruction)])
    print(f"Wrote {INDEX_PATH}")


if __name__ == "__main__":
    main()
