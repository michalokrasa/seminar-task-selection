#!/usr/bin/env python3
"""
Validate generated solutions in apps_selected/ using SandboxFusion /run_code (pytest mode).

For each task in apps_selected/{competition,interview,introductory}/*/ that has a solution.py,
this script:
  1. Loads input_output.json from the task folder (stdin/stdout pairs).
  2. Generates a pytest harness that runs solution.py as a subprocess for each test case,
     feeding stdin and comparing stdout to the expected output.
  3. POSTs to SandboxFusion /run_code with language=pytest.
  4. Reports pass/fail and writes a test-output.md next to the solution.

Usage:
    python3 scripts/7_run_apps_tests.py [--sandbox http://localhost:8080] [--timeout 60]
                                        [--verbose] [--type nl|gherkin]
                                        [--category competition|interview|introductory|all]
                                        [--task <substring>] [--base-dir <path>]

SandboxFusion must be running (see README § SandboxFusion Setup).
"""

import argparse
import base64
import json
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).parent.parent
APPS_SELECTED_DIR = ROOT / "apps_selected"
CATEGORIES = ["competition", "interview", "introductory"]
TYPES = ["nl", "gherkin"]


# ---------------------------------------------------------------------------
# Pytest harness template
# ---------------------------------------------------------------------------

PYTEST_HARNESS_TEMPLATE = '''\
import json
import subprocess
import sys
import pytest

with open("/tests/input_output.json") as f:
    _data = json.load(f)

_cases = list(enumerate(zip(_data["inputs"], _data["outputs"])))


@pytest.mark.parametrize(
    "i,inp,expected",
    [(i, inp, out) for i, (inp, out) in _cases],
    ids=[f"case{i}" for i in range(len(_cases))],
)
def test_case(i, inp, expected):
    result = subprocess.run(
        [sys.executable, "/app/solution.py"],
        input=inp,
        capture_output=True,
        text=True,
        timeout=10,
    )
    actual = result.stdout.strip()
    exp = expected.strip()
    assert actual == exp, f"input={inp!r}\\nexpected={exp!r}\\ngot={actual!r}"
'''


# ---------------------------------------------------------------------------
# SandboxFusion
# ---------------------------------------------------------------------------

def _b64(s: str) -> str:
    return base64.b64encode(s.encode()).decode()


def run_pytest(sandbox_url: str, solution: str, input_output_json: str, timeout: int) -> dict:
    pytest_ini = "[pytest]\nlog_cli = true\naddopts = -s -p no:nameko\n"

    payload = {
        "code": PYTEST_HARNESS_TEMPLATE,
        "language": "pytest",
        "files": {
            "/app/solution.py": _b64(solution),
            "/tests/input_output.json": _b64(input_output_json),
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

def collect_tasks(base_dir: Path, category: str, task_filter: str | None) -> list[tuple[str, str, Path]]:
    tasks = []
    cats = CATEGORIES if category == "all" else [category]
    for cat in cats:
        cat_dir = base_dir / cat
        if not cat_dir.exists():
            continue
        for task_dir in sorted(cat_dir.iterdir()):
            if not task_dir.is_dir():
                continue
            if task_filter and task_filter not in task_dir.name:
                continue
            tasks.append((cat, task_dir.name, task_dir))
    return tasks


def write_output(task_dir: Path, type_: str, lines: list[str]) -> None:
    out_path = task_dir / type_ / "test-output.md"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run apps_selected solutions via SandboxFusion.")
    parser.add_argument("--sandbox", default="http://localhost:8080", help="SandboxFusion base URL")
    parser.add_argument("--timeout", type=int, default=60,
                        help="Per-task pytest run timeout in seconds (default: 60)")
    parser.add_argument("--verbose", action="store_true",
                        help="Print full pytest stdout on failure")
    parser.add_argument(
        "--category", choices=CATEGORIES + ["all"], default="all",
        help="Only test tasks in this category (default: all)",
    )
    parser.add_argument(
        "--task", default=None,
        help="Only test tasks whose folder name contains this substring",
    )
    parser.add_argument(
        "--type", choices=TYPES, default="nl",
        help="Description type subfolder to look for solution.py in (default: nl)",
    )
    parser.add_argument(
        "--base-dir", default=None,
        help="Root directory containing category subdirectories. Defaults to apps_selected/.",
    )
    args = parser.parse_args()

    base_dir = Path(args.base_dir).resolve() if args.base_dir else APPS_SELECTED_DIR

    tasks = collect_tasks(base_dir, args.category, args.task)
    if not tasks:
        print("No tasks matched the given filters.")
        sys.exit(0)

    passed_tasks = 0
    failed_tasks: list[str] = []

    for cat, name, task_dir in tasks:
        solution_path = task_dir / args.type / "solution.py"
        io_path = task_dir / "input_output.json"
        label = f"{cat}/{name}"

        if not solution_path.exists():
            print(f"[SKIP] {label} — solution.py not found")
            write_output(task_dir, args.type, [f"# {label}", "", "**Status:** SKIP", "", "solution.py not found"])
            continue

        if not io_path.exists():
            print(f"[SKIP] {label} — input_output.json not found")
            write_output(task_dir, args.type, [f"# {label}", "", "**Status:** SKIP", "", "input_output.json not found"])
            continue

        solution = solution_path.read_text(encoding="utf-8")
        input_output_json = io_path.read_text(encoding="utf-8")

        n_cases = len(json.loads(input_output_json).get("inputs", []))
        print(f"[RUN]  {label} ({n_cases} cases) …", end=" ", flush=True)

        try:
            result = run_pytest(args.sandbox, solution, input_output_json, args.timeout)
        except requests.exceptions.ConnectionError:
            print(f"\n  [ERROR] Cannot connect to SandboxFusion at {args.sandbox}")
            print("          Start the sandbox first — see README § SandboxFusion Setup")
            sys.exit(1)
        except requests.exceptions.Timeout:
            print("TIMEOUT")
            failed_tasks.append(label)
            write_output(task_dir, args.type, [f"# {label}", "", "**Status:** FAIL", "", "sandbox request timed out"])
            continue
        except Exception as exc:  # noqa: BLE001
            print(f"ERROR: {exc}")
            failed_tasks.append(label)
            write_output(task_dir, args.type, [f"# {label}", "", "**Status:** ERROR", "", str(exc)])
            continue

        status = result.get("status", "")
        run_result = result.get("run_result") or {}
        return_code = run_result.get("return_code", -1)
        stdout = run_result.get("stdout", "")
        stderr = run_result.get("stderr", "")

        if status not in ("Success", "Failed"):
            print(f"FAIL (sandbox status={status})")
            if args.verbose and stdout:
                print(f"       stdout: {stdout.strip()}")
            failed_tasks.append(label)
            out_lines = [f"# {label}", "", "**Status:** FAIL", "", f"sandbox error (status={status})"]
            if result.get("message"):
                out_lines += ["", "## message", "", result["message"]]
            if stdout:
                out_lines += ["", "## stdout", "", "```", stdout.strip(), "```"]
            if stderr:
                out_lines += ["", "## stderr", "", "```", stderr.strip(), "```"]
            write_output(task_dir, args.type, out_lines)
            continue

        if return_code == 0:
            passed_tasks += 1
            print("PASS")
            if args.verbose and stdout:
                print(stdout.strip())
            out_lines = [f"# {label}", "", "**Status:** PASS", ""]
            if stdout:
                out_lines += ["## stdout", "", "```", stdout.strip(), "```"]
            write_output(task_dir, args.type, out_lines)
        else:
            print(f"FAIL (exit code {return_code})")
            if args.verbose and stdout:
                print(stdout.strip())
            failed_tasks.append(label)
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
