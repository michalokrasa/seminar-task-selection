#!/usr/bin/env python3
"""
run_tests.py — Validate generated solutions using SandboxFusion /run_code (pytest mode).

For each task in selection/{easy,medium,hard}/*/ that has a solution.py, this script:
  1. Looks up the task's parquet path ID from selection.csv.
  2. Extracts tests/test_data.json and tests/test_state.py from the tarball in tasks.parquet.
  3. POSTs to SandboxFusion /run_code with language=pytest, passing:
       - code        = test_state.py  (the authoritative pytest harness)
       - files       = {"/app/solution.py": <solution>, "/tests/test_data.json": <test data>}
  4. Reports pass/fail based on pytest return code and stdout.

The test suite in test_data.json contains 10 real judge test cases per task
(not just the sample examples shown in the problem statement).

Usage:
    python3 run_tests.py [--sandbox http://localhost:8080] [--timeout 60] [--verbose] [--type nl|gherkin]

SandboxFusion must be running (see README § SandboxFusion Setup).
Pyarrow must be installed (pip install pyarrow requests).
"""

import argparse
import base64
import csv
import io
import sys
import tarfile
from pathlib import Path

import requests

HERE = Path(__file__).parent
SELECTION_DIR = HERE / "selected"
PARQUET_PATH = HERE / "task-selection" / "tasks.parquet"
SELECTION_CSV = HERE / "task-selection" / "selection.csv"
DIFFICULTIES = ["easy", "medium", "hard"]
TYPES = ["nl", "gherkin"]


# ---------------------------------------------------------------------------
# Parquet / tarball helpers
# ---------------------------------------------------------------------------

def load_selection_index() -> dict[str, str]:
    """Return {task_slug -> parquet_path_id} from selection.csv."""
    import re

    def slugify(name: str) -> str:
        slug = name.lower()
        slug = re.sub(r"[^\w\s-]", "", slug)
        slug = re.sub(r"[\s_]+", "-", slug)
        return slug.strip("-")

    index: dict[str, str] = {}
    with SELECTION_CSV.open(newline="") as f:
        for row in csv.DictReader(f):
            index[slugify(row["name"])] = row["path"]
    return index


def load_parquet_blobs() -> dict[str, bytes]:
    """Return {path_id -> raw_tar_bytes} for all rows in tasks.parquet."""
    import pyarrow.parquet as pq

    table = pq.read_table(PARQUET_PATH)
    paths = table.column("path").to_pylist()
    binaries = table.column("task_binary").to_pylist()
    result: dict[str, bytes] = {}
    for path, blob in zip(paths, binaries):
        if isinstance(blob, str):
            blob = base64.b64decode(blob)
        result[path] = blob
    return result


def extract_from_tar(blob: bytes, *member_names: str) -> dict[str, bytes]:
    """Extract named members from a gzipped tarball, return {name: content}."""
    buf = io.BytesIO(blob)
    out: dict[str, bytes] = {}
    with tarfile.open(fileobj=buf, mode="r:gz") as tar:
        for name in member_names:
            try:
                f = tar.extractfile(name)
                if f is not None:
                    out[name] = f.read()
            except KeyError:
                pass
    return out


# ---------------------------------------------------------------------------
# SandboxFusion
# ---------------------------------------------------------------------------

def _b64(s: str) -> str:
    return base64.b64encode(s.encode()).decode()


def run_pytest(sandbox_url: str, test_state: str, solution: str,
               test_data_json: str, timeout: int) -> dict:
    """
    POST /run_code with language=pytest.

    Files injected into the sandbox:
      /app/solution.py        — generated solution
      /tests/test_data.json   — judge test cases from the parquet

    The `code` field is test_state.py which pytest discovers and runs.
    A pytest.ini is also injected to enable -s (no output capture).
    """
    pytest_ini = "[pytest]\nlog_cli = true\naddopts = -s -p no:nameko\n"

    payload = {
        "code": test_state,
        "language": "pytest",
        "files": {
            "/app/solution.py": _b64(solution),
            "/tests/test_data.json": _b64(test_data_json),
            "pytest.ini": _b64(pytest_ini),
        },
        "run_timeout": timeout,
    }
    resp = requests.post(
        f"{sandbox_url}/run_code",
        json=payload,
        timeout=timeout + 30,
    )
    resp.raise_for_status()
    return resp.json()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Run generated solutions via SandboxFusion.")
    parser.add_argument("--sandbox", default="http://localhost:8080", help="SandboxFusion base URL")
    parser.add_argument("--timeout", type=int, default=60,
                        help="Per-task pytest run timeout in seconds (default: 60)")
    parser.add_argument("--verbose", action="store_true",
                        help="Print full pytest stdout on failure")
    parser.add_argument(
        "--difficulty", choices=DIFFICULTIES + ["all"], default="all",
        help="Only test tasks of this difficulty",
    )
    parser.add_argument(
        "--task", default=None,
        help="Only test tasks whose folder name contains this substring",
    )
    parser.add_argument(
        "--type", choices=TYPES, default="nl",
        help="Description type subfolder to look for solution.py in (default: nl)",
    )
    args = parser.parse_args()

    if not PARQUET_PATH.exists():
        print(f"ERROR: {PARQUET_PATH} not found. Run task-selection/download.sh first.")
        sys.exit(1)

    print("Loading selection index and parquet …")
    slug_to_path = load_selection_index()
    parquet_blobs = load_parquet_blobs()
    print(f"  {len(parquet_blobs)} tasks in parquet, {len(slug_to_path)} in selection.csv\n")

    difficulties = DIFFICULTIES if args.difficulty == "all" else [args.difficulty]

    tasks: list[tuple[str, str, Path]] = []
    for diff in difficulties:
        diff_dir = SELECTION_DIR / diff
        if not diff_dir.exists():
            continue
        for task_dir in sorted(diff_dir.iterdir()):
            if not task_dir.is_dir():
                continue
            if args.task and args.task not in task_dir.name:
                continue
            tasks.append((diff, task_dir.name, task_dir))

    if not tasks:
        print("No tasks matched the given filters.")
        sys.exit(0)

    passed_tasks = 0
    failed_tasks: list[str] = []

    def write_output(task_dir: Path, type_: str, lines: list[str]) -> None:
        out_path = task_dir / type_ / "test-output.md"
        out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    for diff, name, task_dir in tasks:
        solution_path = task_dir / args.type / "solution.py"
        label = f"{diff}/{name}"

        if not solution_path.exists():
            print(f"[SKIP] {label} — solution.py not found")
            write_output(task_dir, args.type, [f"# {label}", "", "**Status:** SKIP", "", "solution.py not found"])
            continue

        path_id = slug_to_path.get(name)
        if path_id is None:
            print(f"[SKIP] {label} — not found in selection.csv")
            write_output(task_dir, args.type, [f"# {label}", "", "**Status:** SKIP", "", "not found in selection.csv"])
            continue

        blob = parquet_blobs.get(path_id)
        if blob is None:
            print(f"[SKIP] {label} — path {path_id} not found in parquet")
            write_output(task_dir, args.type, [f"# {label}", "", "**Status:** SKIP", "", f"path {path_id} not found in parquet"])
            continue

        extracted = extract_from_tar(blob, "tests/test_data.json", "tests/test_state.py")
        if "tests/test_data.json" not in extracted or "tests/test_state.py" not in extracted:
            print(f"[SKIP] {label} — test files missing from tarball")
            write_output(task_dir, args.type, [f"# {label}", "", "**Status:** SKIP", "", "test files missing from tarball"])
            continue

        test_data_json = extracted["tests/test_data.json"].decode("utf-8")
        test_state = extracted["tests/test_state.py"].decode("utf-8")
        solution = solution_path.read_text(encoding="utf-8")

        try:
            result = run_pytest(args.sandbox, test_state, solution, test_data_json, args.timeout)
        except requests.exceptions.ConnectionError:
            print(f"  [ERROR] Cannot connect to SandboxFusion at {args.sandbox}")
            print("          Start the sandbox first — see README § SandboxFusion Setup")
            sys.exit(1)
        except requests.exceptions.Timeout:
            print(f"[FAIL] {label} — sandbox request timed out")
            failed_tasks.append(label)
            write_output(task_dir, args.type, [f"# {label}", "", "**Status:** FAIL", "", "sandbox request timed out"])
            continue
        except Exception as exc:  # noqa: BLE001
            print(f"[ERROR] {label} — {exc}")
            failed_tasks.append(label)
            write_output(task_dir, args.type, [f"# {label}", "", "**Status:** ERROR", "", str(exc)])
            continue

        status = result.get("status", "")
        run_result = result.get("run_result") or {}
        return_code = run_result.get("return_code", -1)
        stdout = run_result.get("stdout", "")
        stderr = run_result.get("stderr", "")

        if status != "Success":
            print(f"[FAIL] {label} — sandbox error (status={status})")
            if args.verbose:
                if stdout:
                    print(f"       stdout: {stdout.strip()}")
                if stderr:
                    print(f"       stderr: {stderr.strip()}")
            failed_tasks.append(label)
            out_lines = [f"# {label}", "", "**Status:** FAIL", "", f"sandbox error (status={status})"]
            if result.get("message"):
                out_lines += ["", "## message", "", result["message"]]
            if stdout:
                out_lines += ["", "## stdout", "", "```", stdout.strip(), "```"]
            if stderr:
                out_lines += ["", "## stderr", "", "```", stderr.strip(), "```"]
            out_lines += ["", "## raw response", "", "```json", __import__('json').dumps(result, indent=2), "```"]
            write_output(task_dir, args.type, out_lines)
            continue

        if return_code == 0:
            passed_tasks += 1
            print(f"[PASS] {label}")
            if args.verbose:
                print(stdout.strip())
            out_lines = [f"# {label}", "", "**Status:** PASS", ""]
            if stdout:
                out_lines += ["## stdout", "", "```", stdout.strip(), "```"]
            write_output(task_dir, args.type, out_lines)
        else:
            print(f"[FAIL] {label} — pytest exit code {return_code}")
            failed_tasks.append(label)
            if args.verbose:
                print(stdout.strip())
            out_lines = [f"# {label}", "", f"**Status:** FAIL (exit code {return_code})", ""]
            if stdout:
                out_lines += ["## stdout", "", "```", stdout.strip(), "```"]
            if stderr:
                out_lines += ["", "## stderr", "", "```", stderr.strip(), "```"]
            write_output(task_dir, args.type, out_lines)

    total = passed_tasks + len(failed_tasks)
    print()
    print("=" * 60)
    print(f"Tasks : {passed_tasks}/{total} passed")
    if failed_tasks:
        print("Failed:")
        for t in failed_tasks:
            print(f"  - {t}")
        sys.exit(1)
    else:
        print("All tasks passed.")


if __name__ == "__main__":
    main()
