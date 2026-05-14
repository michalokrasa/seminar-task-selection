#!/usr/bin/env python3
"""
generate_solutions.py

Use GPT to generate a Python solution for each problem in selected/,
based on either the Gherkin (.feature) or NL (.md) description.

Usage:
    python generate_solutions.py --format (gherkin|nl) [--problem <path>]

Arguments:
    --format    Required. Which description format to use as the GPT prompt.
                  gherkin  -> <problem>/gherkin/description.feature
                  nl       -> <problem>/nl/description.md
    --problem   Optional. Path to a single problem folder. When omitted,
                all problems under selected/ are processed.

Environment:
    OPENAI_API_KEY  Must be set.
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent / ".env")
except ImportError:
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                k, _, v = line.partition("=")
                os.environ.setdefault(k.strip(), v.strip())

from openai import OpenAI

SELECTED_DIR = Path(__file__).parent / "selected"

SYSTEM_PROMPT = (
    "You are an expert competitive programmer. "
    "Given a problem description, write a complete, correct Python 3 solution. "
    "Output ONLY the raw Python code with no markdown fences, no explanation, "
    "and no commentary — just the code that can be run directly."
)


def find_description(problem_dir: Path, fmt: str) -> Path | None:
    if fmt == "gherkin":
        candidates = [
            problem_dir / "gherkin" / "description.feature",
            problem_dir / "nl" / "description.md",
        ]
    else:
        candidates = [
            problem_dir / "nl" / "description.md",
            problem_dir / "gherkin" / "description.feature",
        ]
    for p in candidates:
        if p.exists():
            return p
    return None


def output_path(problem_dir: Path, description_file: Path) -> Path:
    if description_file.suffix == ".feature":
        return problem_dir / "gherkin" / "solution.py"
    return problem_dir / "nl" / "solution.py"


def strip_fences(code: str) -> str:
    lines = code.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines)


def generate_solution(client: OpenAI, description: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": description},
        ],
        temperature=0,
    )
    return strip_fences(response.choices[0].message.content)


def process_problem(client: OpenAI, problem_dir: Path, fmt: str) -> None:
    desc_file = find_description(problem_dir, fmt)
    if desc_file is None:
        print(f"  [SKIP] No description found in {problem_dir.name}")
        return

    out_file = output_path(problem_dir, desc_file)
    out_file.parent.mkdir(parents=True, exist_ok=True)

    print(f"  [GEN]  {problem_dir.name}  ({desc_file.relative_to(problem_dir)}) -> {out_file.relative_to(problem_dir)}")

    description = desc_file.read_text(encoding="utf-8")
    code = generate_solution(client, description)
    out_file.write_text(code, encoding="utf-8")


def collect_problems(base: Path, difficulty: str = "all") -> list[Path]:
    problems = []
    for diff_dir in sorted(base.iterdir()):
        if not diff_dir.is_dir():
            continue
        if difficulty != "all" and diff_dir.name != difficulty:
            continue
        for problem in sorted(diff_dir.iterdir()):
            if problem.is_dir():
                problems.append(problem)
    return problems


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate GPT solutions for selected problems.")
    parser.add_argument(
        "--format",
        required=True,
        choices=["gherkin", "nl"],
        help="Description format to use as the prompt.",
    )
    parser.add_argument(
        "--problem",
        default=None,
        help="Path to a single problem folder. Omit to process all problems.",
    )
    parser.add_argument(
        "--difficulty",
        default="all",
        choices=["easy", "medium", "hard", "all"],
        help="Limit to one difficulty bucket (default: all).",
    )
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    if args.problem:
        problem_dir = Path(args.problem).resolve()
        if not problem_dir.is_dir():
            print(f"Error: {problem_dir} is not a directory.", file=sys.stderr)
            sys.exit(1)
        problems = [problem_dir]
    else:
        problems = collect_problems(SELECTED_DIR, args.difficulty)

    print(f"Processing {len(problems)} problem(s) with format='{args.format}'...\n")
    for problem_dir in problems:
        process_problem(client, problem_dir, args.format)

    print("\nDone.")


if __name__ == "__main__":
    main()
