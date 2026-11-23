#!/usr/bin/env bash
set -euo pipefail

repository="${1:-}"
if [[ -z "$repository" ]]; then
  echo "Usage: $0 OWNER/REPOSITORY" >&2
  exit 2
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required to create labels." >&2
  exit 1
fi

create_or_update_label() {
  local name="$1"
  local color="$2"
  local description="$3"

  gh label create "$name" \
    --repo "$repository" \
    --color "$color" \
    --description "$description" \
    --force
}

create_or_update_label "bug" "d73a4a" "Something is not working"
create_or_update_label "feature" "a2eeef" "New user-visible behaviour"
create_or_update_label "task" "1d76db" "Engineering or documentation task"
create_or_update_label "needs-triage" "fbca04" "Classifier confidence is below threshold"

echo "Demo labels are ready in $repository."
