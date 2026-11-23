#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
project_dir="$(cd "$script_dir/.." && pwd)"
cd "$project_dir"
root_dir="$(git rev-parse --show-toplevel)"

if [[ "$root_dir" != "$project_dir" ]]; then
  echo "Run this script only after initializing this folder as its own Git repository." >&2
  exit 1
fi

if [[ -n "$(git status --porcelain)" ]]; then
  echo "Working tree must be clean before creating demo branches." >&2
  exit 1
fi

git show-ref --verify --quiet refs/heads/main || {
  echo "The main branch does not exist." >&2
  exit 1
}

create_branch() {
  local branch_name="$1"
  local patch_file="$2"
  local commit_message="$3"

  if git show-ref --verify --quiet "refs/heads/$branch_name"; then
    echo "Branch $branch_name already exists; skipping."
    return
  fi

  git switch --create "$branch_name" main
  git apply "$patch_file"
  git add src tests
  git commit -m "$commit_message"
}

trap 'git switch main >/dev/null 2>&1 || true' EXIT

create_branch \
  "demo/promo-discounts" \
  "$project_dir/scenarios/promo-discounts.patch" \
  "Add promotional discounts"

create_branch \
  "demo/bulk-quotes" \
  "$project_dir/scenarios/bulk-quotes.patch" \
  "Add bulk quote calculation"

git switch main
echo "Created demo/promo-discounts and demo/bulk-quotes."
