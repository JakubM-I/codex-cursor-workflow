#!/usr/bin/env bash

# The default check sends one small request per installed CLI.
set -eu
reviewer_script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$reviewer_script_dir/check-reviewer-clis.py" "$@"
