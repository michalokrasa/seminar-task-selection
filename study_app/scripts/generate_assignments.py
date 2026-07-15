#!/usr/bin/env python3
"""Generate a counterbalanced participant-assignment CSV.

Reads the approved problem pool from ../apps_selected_approved/ and assigns
each participant:
  - two distinct tasks (out of the approved pool)
  - a counterbalanced first modality order (nl -> gherkin or gherkin -> nl)
  - a deterministic Latin-square-ish condition group

The frontend expands each assigned task into both modalities, so every
participant writes four specifications in total: Gherkin + natural-language
for each of the two assigned tasks.

Output: stdout CSV with columns:
  participant_id,task_1_slug,task_1_first_modality,task_1_second_modality,
  task_2_slug,task_2_first_modality,task_2_second_modality,
  condition_group,task_1_bucket,task_2_bucket

Upload the CSV to the Google Sheet tab named `assignments`.
"""

import csv
import random
import sys
from pathlib import Path

SEED = 7
SELECTED_DIR = Path(__file__).resolve().parents[2] / "apps_selected_approved"
BUCKETS = ("introductory", "interview", "competition")


def discover_tasks():
    """Return all available task slugs grouped by bucket."""
    buckets = {}
    for bucket in BUCKETS:
        bucket_dir = SELECTED_DIR / bucket
        buckets[bucket] = [p.name for p in bucket_dir.iterdir() if p.is_dir()] if bucket_dir.exists() else []
    return buckets


def build_task_pool(tasks):
    """Return every available (slug, bucket) task, sorted for determinism.

    There are 4 tasks per difficulty bucket (introductory/interview/
    competition) = 12 tasks total. Every task in this pool is eligible to
    be used, rather than only a subset of 5.
    """
    return sorted(
        [(slug, bucket) for bucket, slugs in tasks.items() for slug in slugs],
        key=lambda x: x[0],
    )


def build_round_matching(task_pool, round_index):
    """Shuffle the full task pool and split into non-overlapping pairs.

    This is a perfect matching: every task in `task_pool` appears in
    exactly one pair. A fresh shuffle (seeded per round) is used for each
    round so that once every task has been used once (one round), the next
    round re-pairs tasks in a different combination rather than repeating
    the same pairs.
    """
    rng = random.Random(SEED + round_index)
    pool = list(task_pool)
    rng.shuffle(pool)
    return [tuple(pool[i : i + 2]) for i in range(0, len(pool) - len(pool) % 2, 2)]


def generate_assignments(task_pool, participant_ids):
    """Create a counterbalanced assignment for each participant ID.

    Balance guarantee:
      - Task usage: participants are grouped into rounds of
        `len(task_pool) // 2` (e.g. 6 participants per round for a
        12-task pool). Within a round, tasks are paired via a perfect
        matching, so every task is used EXACTLY ONCE per round — no task
        repeats until every other task has also been used once.

    Each assigned task is completed in both modalities. The order of the two
    modalities for each task is randomized per participant, so across the
    study both NL-first and Gherkin-first orders are evenly represented.
    """
    n = len(participant_ids)
    pairs_per_round = len(task_pool) // 2
    if pairs_per_round == 0:
        raise ValueError("Task pool must contain at least 2 tasks.")

    rng = random.Random(SEED)

    def shuffled_modalities():
        pair = ["nl", "gherkin"]
        rng.shuffle(pair)
        return pair

    rows = []
    current_round = -1
    round_pairs = None
    for i, pid in enumerate(participant_ids):
        round_index = i // pairs_per_round
        pos = i % pairs_per_round
        if round_index != current_round:
            round_pairs = build_round_matching(task_pool, round_index)
            current_round = round_index

        (slug1, bucket1), (slug2, bucket2) = round_pairs[pos]
        task_1_modalities = shuffled_modalities()
        task_2_modalities = shuffled_modalities()
        group = f"round{round_index}_pair{pos}_t1-{task_1_modalities[0]}_t2-{task_2_modalities[0]}"
        rows.append(
            {
                "participant_id": pid,
                "task_1_slug": slug1,
                "task_1_first_modality": task_1_modalities[0],
                "task_1_second_modality": task_1_modalities[1],
                "task_2_slug": slug2,
                "task_2_first_modality": task_2_modalities[0],
                "task_2_second_modality": task_2_modalities[1],
                "condition_group": group,
                "task_1_bucket": bucket1,
                "task_2_bucket": bucket2,
            }
        )
    return rows


def main():
    if len(sys.argv) < 2:
        print("Usage: generate_assignments.py <count_or_pid_list>", file=sys.stderr)
        print("Example: generate_assignments.py 20", file=sys.stderr)
        print("Example: generate_assignments.py p001 p002 p003", file=sys.stderr)
        sys.exit(1)

    arg = sys.argv[1]
    if arg.isdigit():
        participant_ids = [f"p{i:03d}" for i in range(1, int(arg) + 1)]
    else:
        participant_ids = sys.argv[1:]

    tasks = discover_tasks()
    task_pool = build_task_pool(tasks)
    if len(task_pool) < 2:
        print(f"Need at least 2 tasks, found {len(task_pool)}.", file=sys.stderr)
        sys.exit(1)
    if len(task_pool) % 2 != 0:
        print(f"Warning: task pool has an odd size ({len(task_pool)}); one task will be dropped per round.", file=sys.stderr)

    assignments = generate_assignments(task_pool, participant_ids)

    writer = csv.DictWriter(
        sys.stdout,
        fieldnames=[
            "participant_id",
            "task_1_slug",
            "task_1_first_modality",
            "task_1_second_modality",
            "task_2_slug",
            "task_2_first_modality",
            "task_2_second_modality",
            "condition_group",
            "task_1_bucket",
            "task_2_bucket",
        ],
        extrasaction="ignore",
    )
    writer.writeheader()
    writer.writerows(assignments)


if __name__ == "__main__":
    main()
