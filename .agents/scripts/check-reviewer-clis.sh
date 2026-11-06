#!/usr/bin/env bash

# Reports local CLI discoverability only. It never sends a model prompt.
set -u

for reviewer_cli in codex claude gemini; do
  if command -v "$reviewer_cli" >/dev/null 2>&1; then
    reviewer_version=$("$reviewer_cli" --version 2>&1 | head -n 1)
    printf '%s\tavailable\t%s\n' "$reviewer_cli" "${reviewer_version:-version unavailable}"
  else
    printf '%s\tunavailable\tNot found on PATH\n' "$reviewer_cli"
  fi
done

printf '%s\n' 'Note: availability does not verify authentication, entitlement, model access, or a successful review.'
