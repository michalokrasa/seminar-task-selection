#!/usr/bin/env python3
"""
Generate NL and Gherkin descriptions for problems in apps_selected/.

For each problem folder in apps_selected/<category>/<id>/, reads task.md and
uses GPT-4o to write:
  apps_selected/<category>/<id>/nl/description.md
  apps_selected/<category>/<id>/gherkin/description.feature

Usage:
    python scripts/6_generate_apps_descriptions.py [--category <name>] [--problem <path>] [--no-overwrite]

Environment:
    OPENAI_API_KEY  Must be set.
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
except ImportError:
    env_file = Path(__file__).parent.parent / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                k, _, v = line.partition("=")
                os.environ.setdefault(k.strip(), v.strip())

from openai import OpenAI

ROOT = Path(__file__).parent.parent
APPS_SELECTED_DIR = ROOT / "apps_selected"

NL_SYSTEM_PROMPT = """\
You are a technical writer specialising in competitive programming.
Given a problem statement, rewrite it as a concise natural-language description.

Output ONLY valid Markdown following this exact structure (no extra headings,
no preamble, no trailing commentary):

# <Short Title>

## Goal

<One or two sentences stating what to compute or decide.>

## Rules

- <Rule 1>
- <Rule 2>
- ...

## Input / Output

- **Input**: <describe the input format and constraints>
- **Output**: <describe the output format>
"""

GHERKIN_SYSTEM_PROMPT = """\
You are a QA engineer specialising in competitive programming.
Given a problem statement, write a Gherkin feature file that captures the
problem's behaviour.

Requirements:
- Start with a Feature block (name + As/I want/So that lines).
- Include a Rule block that describes the input/output format.
- Include a Background block only if there is shared setup (e.g. a fixed set
  of special values). Omit Background if there is no shared setup.
- Write 3–5 concrete Scenario blocks that cover distinct cases from the
  problem examples or edge cases.
- End with one Scenario Outline block that has an Examples table covering at
  least 4 rows drawn from the problem's sample input/output pairs.

Output ONLY raw Gherkin (no markdown fences, no explanation).
"""


def strip_fences(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines)


def generate(client: OpenAI, system: str, task_text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": task_text},
        ],
        temperature=0,
    )
    return strip_fences(response.choices[0].message.content)


def process_problem(client: OpenAI, problem_dir: Path, no_overwrite: bool) -> None:
    task_file = problem_dir / "task.md"
    if not task_file.exists():
        print(f"  [SKIP] {problem_dir} — task.md not found")
        return

    task_text = task_file.read_text(encoding="utf-8")

    nl_out = problem_dir / "nl" / "description.md"
    gherkin_out = problem_dir / "gherkin" / "description.feature"

    nl_out.parent.mkdir(parents=True, exist_ok=True)
    gherkin_out.parent.mkdir(parents=True, exist_ok=True)

    label = "/".join(problem_dir.parts[-2:])

    if not no_overwrite or not nl_out.exists():
        print(f"  [NL]      {label}")
        nl_text = generate(client, NL_SYSTEM_PROMPT, task_text)
        nl_out.write_text(nl_text + "\n", encoding="utf-8")
    else:
        print(f"  [SKIP-NL] {label} — already exists")

    if not no_overwrite or not gherkin_out.exists():
        print(f"  [GHERKIN] {label}")
        gherkin_text = generate(client, GHERKIN_SYSTEM_PROMPT, task_text)
        gherkin_out.write_text(gherkin_text + "\n", encoding="utf-8")
    else:
        print(f"  [SKIP-GH] {label} — already exists")


def collect_problems(base: Path, category: str = "all") -> list[Path]:
    problems: list[Path] = []
    for cat_dir in sorted(base.iterdir()):
        if not cat_dir.is_dir():
            continue
        if category != "all" and cat_dir.name != category:
            continue
        for problem in sorted(cat_dir.iterdir()):
            if problem.is_dir():
                problems.append(problem)
    return problems


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate NL and Gherkin descriptions for apps_selected problems."
    )
    parser.add_argument(
        "--category",
        default="all",
        help="Limit to one category (e.g. interview, competition, introductory). Default: all.",
    )
    parser.add_argument(
        "--problem",
        default=None,
        help="Path to a single problem folder. Omit to process all problems.",
    )
    parser.add_argument(
        "--no-overwrite",
        action="store_true",
        help="Skip problems that already have description files.",
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
        problems = collect_problems(APPS_SELECTED_DIR, args.category)

    print(f"Processing {len(problems)} problem(s)...\n")
    for problem_dir in problems:
        process_problem(client, problem_dir, args.no_overwrite)

    print("\nDone.")


if __name__ == "__main__":
    main()
