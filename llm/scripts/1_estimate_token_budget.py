"""
Estimate token budget for code generation based on NL vs Gherkin task
descriptions (inputs) and their reference solutions (outputs).

For every task under `processing/apps_selected_approved/<level>/<task_id>/`
this script looks at both variants:
    nl/description.md      + nl/solution.py
    gherkin/description.feature + gherkin/solution.py

and counts characters (and an estimated token count) for the input
(description) and output (solution) of each variant.

Usage:
    .venv/bin/python processing/scripts/1_estimate_token_budget.py

Outputs (written to processing/token_budget/):
    breakdown.csv   - one row per task/variant with char & token counts
    summary.json    - aggregated stats (totals, mean, median, min, max) per
                       variant and per difficulty level

Token estimate:
    Uses `tiktoken` (cl100k_base encoding) if installed, otherwise falls
    back to a simple heuristic of chars / 4.
"""

import csv
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = ROOT / "processing" / "apps_selected_approved"
OUT_DIR = ROOT / "processing" / "token_budget"

VARIANTS = {
    "nl": {"input": "description.md", "output": "solution.py"},
    "gherkin": {"input": "description.feature", "output": "solution.py"},
}

try:
    import tiktoken

    _ENC = tiktoken.get_encoding("cl100k_base")

    def count_tokens(text: str) -> int:
        return len(_ENC.encode(text))

    TOKEN_METHOD = "tiktoken(cl100k_base)"
except ImportError:
    def count_tokens(text: str) -> int:
        # crude fallback heuristic: ~4 chars per token
        return max(1, round(len(text) / 4))

    TOKEN_METHOD = "heuristic(chars/4)"


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def collect_rows():
    rows = []
    for level_dir in sorted(DATA_DIR.iterdir()):
        if not level_dir.is_dir():
            continue
        level = level_dir.name
        for task_dir in sorted(level_dir.iterdir()):
            if not task_dir.is_dir():
                continue
            task_id = task_dir.name
            for variant, files in VARIANTS.items():
                variant_dir = task_dir / variant
                if not variant_dir.exists():
                    continue
                input_path = variant_dir / files["input"]
                output_path = variant_dir / files["output"]

                input_text = read_text(input_path)
                output_text = read_text(output_path)

                input_chars = len(input_text)
                output_chars = len(output_text)
                input_tokens = count_tokens(input_text)
                output_tokens = count_tokens(output_text)

                rows.append(
                    {
                        "level": level,
                        "task_id": task_id,
                        "variant": variant,
                        "input_file": str(input_path.relative_to(ROOT)),
                        "output_file": str(output_path.relative_to(ROOT)),
                        "input_chars": input_chars,
                        "output_chars": output_chars,
                        "total_chars": input_chars + output_chars,
                        "input_tokens": input_tokens,
                        "output_tokens": output_tokens,
                        "total_tokens": input_tokens + output_tokens,
                    }
                )
    return rows


def write_csv(rows, path: Path):
    fieldnames = [
        "level",
        "task_id",
        "variant",
        "input_file",
        "output_file",
        "input_chars",
        "output_chars",
        "total_chars",
        "input_tokens",
        "output_tokens",
        "total_tokens",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def stats_for(values):
    if not values:
        return {"count": 0}
    return {
        "count": len(values),
        "sum": sum(values),
        "mean": round(statistics.mean(values), 2),
        "median": statistics.median(values),
        "min": min(values),
        "max": max(values),
    }


def build_summary(rows):
    summary = {
        "token_estimation_method": TOKEN_METHOD,
        "overall": {},
        "by_variant": {},
        "by_level_and_variant": {},
    }

    summary["overall"] = {
        "input_chars": stats_for([r["input_chars"] for r in rows]),
        "output_chars": stats_for([r["output_chars"] for r in rows]),
        "total_chars": stats_for([r["total_chars"] for r in rows]),
        "input_tokens": stats_for([r["input_tokens"] for r in rows]),
        "output_tokens": stats_for([r["output_tokens"] for r in rows]),
        "total_tokens": stats_for([r["total_tokens"] for r in rows]),
    }

    variants = sorted({r["variant"] for r in rows})
    for variant in variants:
        subset = [r for r in rows if r["variant"] == variant]
        summary["by_variant"][variant] = {
            "input_chars": stats_for([r["input_chars"] for r in subset]),
            "output_chars": stats_for([r["output_chars"] for r in subset]),
            "total_chars": stats_for([r["total_chars"] for r in subset]),
            "input_tokens": stats_for([r["input_tokens"] for r in subset]),
            "output_tokens": stats_for([r["output_tokens"] for r in subset]),
            "total_tokens": stats_for([r["total_tokens"] for r in subset]),
        }

    levels = sorted({r["level"] for r in rows})
    for level in levels:
        summary["by_level_and_variant"][level] = {}
        for variant in variants:
            subset = [r for r in rows if r["level"] == level and r["variant"] == variant]
            summary["by_level_and_variant"][level][variant] = {
                "input_chars": stats_for([r["input_chars"] for r in subset]),
                "output_chars": stats_for([r["output_chars"] for r in subset]),
                "total_chars": stats_for([r["total_chars"] for r in subset]),
                "input_tokens": stats_for([r["input_tokens"] for r in subset]),
                "output_tokens": stats_for([r["output_tokens"] for r in subset]),
                "total_tokens": stats_for([r["total_tokens"] for r in subset]),
            }

    return summary


def main():
    rows = collect_rows()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    csv_path = OUT_DIR / "breakdown.csv"
    write_csv(rows, csv_path)

    summary = build_summary(rows)
    summary_path = OUT_DIR / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"Token estimation method: {TOKEN_METHOD}")
    print(f"Tasks/variants processed: {len(rows)}")
    print(f"Breakdown written to: {csv_path.relative_to(ROOT)}")
    print(f"Summary written to:   {summary_path.relative_to(ROOT)}")
    print()
    print("== overall ==")
    for key in ("input_chars", "output_chars", "input_tokens", "output_tokens", "total_tokens"):
        s = summary["overall"][key]
        print(f"  {key:14s} sum={s['sum']:>10} mean={s['mean']:>8} median={s['median']:>8} min={s['min']:>6} max={s['max']:>6}")
    print()
    for variant, stats in summary["by_variant"].items():
        print(f"== {variant} ==")
        for key in ("input_chars", "output_chars", "input_tokens", "output_tokens", "total_tokens"):
            s = stats[key]
            print(f"  {key:14s} sum={s['sum']:>10} mean={s['mean']:>8} median={s['median']:>8} min={s['min']:>6} max={s['max']:>6}")


if __name__ == "__main__":
    main()
