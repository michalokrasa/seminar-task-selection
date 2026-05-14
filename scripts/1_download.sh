#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
DATA_DIR="$HERE/data"
mkdir -p "$DATA_DIR"
if [ -f "$DATA_DIR/tasks.parquet" ]; then
  echo "tasks.parquet already present, skipping download"
else
  curl -L -o "$DATA_DIR/tasks.parquet" \
    "https://huggingface.co/datasets/open-thoughts/CodeContests/resolve/main/tasks.parquet"
fi
