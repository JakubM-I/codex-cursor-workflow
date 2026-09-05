#!/usr/bin/env python3
"""Lightweight validation for Codex-Cursor project artifacts.

This script intentionally uses only the Python standard library. It checks the
metadata and cross-artifact invariants that are easy to forget in a file-based
workflow without requiring a full Markdown parser.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PROJECT_FILES = {
    "docs/project/status.md": {
        "required": True,
        "fields": ["artifact", "version", "project_status", "current_stage", "created", "updated", "related"],
        "artifact": "project-status",
        "statuses": {
            "project_status": {"active", "paused", "blocked", "complete", "superseded"},
            "current_stage": {
                "init",
                "brief",
                "product-functional-spec",
                "design",
                "architecture",
                "implementation-plan",
                "complete",
            },
        },
    },
    "docs/project/brief.md": {
        "required": False,
        "fields": ["artifact", "version", "status", "stage", "created", "updated", "sources", "related"],
        "artifact": "project-brief",
        "statuses": {"status": {"draft", "ready-for-functional-spec", "superseded"}},
    },
    "docs/project/product-spec.md": {
        "required": False,
        "fields": ["artifact", "version", "status", "stage", "created", "updated", "sources", "related"],
        "artifact": "product-spec",
        "statuses": {"status": {"draft", "ready-for-design-and-architecture", "superseded"}},
    },
    "docs/project/functional-spec.md": {
        "required": False,
        "fields": ["artifact", "version", "status", "stage", "created", "updated", "sources", "related"],
        "artifact": "functional-spec",
        "statuses": {"status": {"draft", "ready-for-design-and-architecture", "superseded"}},
    },
    "docs/project/design-brief.md": {
        "required": False,
        "fields": ["artifact", "version", "status", "stage", "created", "updated", "sources", "related"],
        "artifact": "design-brief",
        "statuses": {"status": {"draft", "ready-for-user-review", "approved-for-architecture", "superseded"}},
    },
    "docs/project/screen-spec.md": {
        "required": False,
        "fields": ["artifact", "version", "status", "stage", "created", "updated", "sources", "related"],
        "artifact": "screen-spec",
        "statuses": {"status": {"draft", "ready-for-user-review", "approved-for-architecture", "superseded"}},
    },
    "docs/project/design-system.md": {
        "required": False,
        "fields": ["artifact", "version", "status", "stage", "created", "updated", "sources", "related"],
        "artifact": "design-system",
        "statuses": {"status": {"draft", "ready-for-user-review", "approved-for-architecture", "superseded"}},
    },
    "docs/project/technical-architecture.md": {
        "required": False,
        "fields": [
            "artifact",
            "version",
            "status",
            "stage",
            "created",
            "updated",
            "sources",
            "related",
            "stack",
            "tags",
        ],
        "artifact": "technical-architecture",
        "statuses": {"status": {"draft", "ready-for-implementation-planning", "blocked", "superseded"}},
    },
}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_RE = re.compile(r"\b(AC|F|Flow|S|ADR)-(\d{3})\b")


def parse_frontmatter(path: Path) -> tuple[dict[str, object], list[str]]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors: list[str] = []

    if not lines or lines[0].strip() != "---":
        return {}, [f"{path}: missing YAML frontmatter"]

    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        return {}, [f"{path}: unclosed YAML frontmatter"]

    data: dict[str, object] = {}
    current_list_key: str | None = None

    for line in lines[1:end]:
        if not line.strip():
            continue

        list_match = re.match(r"^\s*-\s+(.*)$", line)
        if list_match and current_list_key:
            value = data.setdefault(current_list_key, [])
            if isinstance(value, list):
                value.append(list_match.group(1).strip().strip("\"'"))
            continue

        key_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not key_match:
            errors.append(f"{path}: unsupported frontmatter line: {line}")
            current_list_key = None
            continue

        key, raw_value = key_match.groups()
        raw_value = raw_value.strip()
        current_list_key = None

        if raw_value == "[]":
            data[key] = []
        elif raw_value == "":
            data[key] = []
            current_list_key = key
        else:
            data[key] = raw_value.strip("\"'")

    return data, errors


def validate_file(root: Path, rel_path: str, spec: dict[str, object]) -> list[str]:
    path = root / rel_path
    errors: list[str] = []

    if not path.exists():
        if spec.get("required"):
            return [f"{rel_path}: required artifact is missing"]
        return []

    frontmatter, parse_errors = parse_frontmatter(path)
    errors.extend(parse_errors)

    for field in spec["fields"]:  # type: ignore[index]
        if field not in frontmatter:
            errors.append(f"{rel_path}: missing frontmatter field `{field}`")

    expected_artifact = spec.get("artifact")
    if expected_artifact and frontmatter.get("artifact") != expected_artifact:
        errors.append(
            f"{rel_path}: artifact should be `{expected_artifact}`, found `{frontmatter.get('artifact')}`"
        )

    for date_field in ("created", "updated"):
        value = frontmatter.get(date_field)
        if isinstance(value, str) and not DATE_RE.match(value):
            errors.append(f"{rel_path}: `{date_field}` should use YYYY-MM-DD")

    statuses = spec.get("statuses", {})
    if isinstance(statuses, dict):
        for field, allowed in statuses.items():
            value = frontmatter.get(field)
            if value is not None and value not in allowed:
                allowed_text = ", ".join(sorted(allowed))
                errors.append(f"{rel_path}: `{field}` has unsupported value `{value}`; expected one of: {allowed_text}")

    related = frontmatter.get("related")
    if isinstance(related, list):
        for related_path in related:
            if related_path and not (root / str(related_path)).exists():
                errors.append(f"{rel_path}: related artifact does not exist: {related_path}")

    return errors


def validate_ids(root: Path) -> list[str]:
    errors: list[str] = []
    seen: dict[str, str] = {}

    for rel_path in PROJECT_FILES:
        path = root / rel_path
        if not path.exists():
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for match in ID_RE.finditer(line):
                stable_id = match.group(0)
                location = f"{rel_path}:{line_number}"
                if stable_id in seen and seen[stable_id] != location:
                    errors.append(f"{location}: duplicate stable ID `{stable_id}` also appears at {seen[stable_id]}")
                else:
                    seen[stable_id] = location

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Codex-Cursor project artifacts.")
    parser.add_argument("project_root", nargs="?", default=".", help="Project root to validate.")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    errors: list[str] = []

    for rel_path, spec in PROJECT_FILES.items():
        errors.extend(validate_file(root, rel_path, spec))
    errors.extend(validate_ids(root))

    if errors:
        print("Project artifact validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Project artifact validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
