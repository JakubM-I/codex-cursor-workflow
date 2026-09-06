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
                "task-specification",
                "implementation",
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
    "docs/project/asset-manifest.md": {
        "required": False,
        "fields": ["artifact", "version", "status", "stage", "created", "updated", "sources", "related"],
        "artifact": "asset-manifest",
        "statuses": {
            "status": {
                "draft",
                "ready-for-asset-decision",
                "ready-for-implementation",
                "superseded",
            }
        },
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
    "docs/project/implementation-plan.md": {
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
            "plan_depth",
            "tags",
        ],
        "artifact": "implementation-plan",
        "statuses": {
            "status": {"draft", "ready-for-task-specification", "blocked", "superseded"},
            "plan_depth": {"prototype", "standard", "high-assurance"},
        },
    },
    "docs/project/delivery-log.md": {
        "required": False,
        "fields": ["artifact", "version", "status", "created", "updated", "related"],
        "artifact": "delivery-log",
        "statuses": {"status": {"active", "complete", "superseded"}},
    },
}

TASK_SPEC = {
    "required": False,
    "fields": [
        "artifact",
        "version",
        "status",
        "stage",
        "task_id",
        "task_ref",
        "revision",
        "milestone",
        "created",
        "updated",
        "sources",
        "related",
        "depends_on",
        "tags",
    ],
    "artifact": "cursor-task-spec",
    "statuses": {
        "status": {
            "draft",
            "ready-for-cursor",
            "implementation-reported",
            "verification-in-progress",
            "changes-required",
            "accepted",
            "blocked",
            "superseded",
        },
        "stage": {"task-specification", "implementation"},
    },
}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_DEFINITION_PATTERNS = [
    re.compile(r"^#{2,6}\s+((?:F|Flow|S|M)-\d{3})\s+-\s+"),
    re.compile(r"^-\s+(AC-\d{3})\s+-\s+"),
    re.compile(r"^\|\s+(ADR-\d{3})\s+\|"),
]


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
    current_nested_key: str | None = None

    for line in lines[1:end]:
        if not line.strip():
            continue

        list_match = re.match(r"^\s*-\s+(.*)$", line)
        if list_match and current_list_key:
            value = data.setdefault(current_list_key, [])
            if isinstance(value, list):
                value.append(list_match.group(1).strip().strip("\"'"))
            continue

        if current_nested_key and re.match(r"^\s+([A-Za-z0-9_-]+):\s*(.*)$", line):
            current_list_key = None
            continue

        if current_nested_key and re.match(r"^\s+-\s+(.*)$", line):
            continue

        key_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not key_match:
            errors.append(f"{path}: unsupported frontmatter line: {line}")
            current_list_key = None
            continue

        key, raw_value = key_match.groups()
        raw_value = raw_value.strip()
        current_list_key = None
        current_nested_key = None

        if raw_value == "[]":
            data[key] = []
        elif raw_value == "":
            data[key] = []
            current_list_key = key
            current_nested_key = key
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
            for pattern in ID_DEFINITION_PATTERNS:
                match = pattern.search(line)
                if not match:
                    continue
                stable_id = match.group(1)
                location = f"{rel_path}:{line_number}"
                if stable_id in seen and seen[stable_id] != location:
                    errors.append(f"{location}: duplicate stable ID `{stable_id}` also appears at {seen[stable_id]}")
                else:
                    seen[stable_id] = location

    return errors


def validate_task_specs(root: Path) -> list[str]:
    task_dir = root / "docs/tasks"
    if not task_dir.exists():
        return []

    errors: list[str] = []
    for path in sorted(task_dir.glob("M-*/M-*-TASK-*.md")):
        frontmatter, parse_errors = parse_frontmatter(path)
        errors.extend(parse_errors)
        if frontmatter.get("artifact") != "cursor-task-spec":
            continue
        rel_path = str(path.relative_to(root))
        errors.extend(validate_file(root, rel_path, TASK_SPEC))
        task_id = frontmatter.get("task_id")
        task_ref = frontmatter.get("task_ref")
        milestone = frontmatter.get("milestone")
        revision = frontmatter.get("revision")
        if isinstance(task_id, str) and not re.fullmatch(r"TASK-\d{3}", task_id):
            errors.append(f"{rel_path}: `task_id` should use TASK-001 format")
        if isinstance(milestone, str) and not re.fullmatch(r"M-\d{3}", milestone):
            errors.append(f"{rel_path}: `milestone` should use M-001 format")
        if isinstance(task_ref, str) and not re.fullmatch(r"M-\d{3}-TASK-\d{3}", task_ref):
            errors.append(f"{rel_path}: `task_ref` should use M-001-TASK-001 format")
        if isinstance(revision, str) and not re.fullmatch(r"[1-9]\d*", revision):
            errors.append(f"{rel_path}: `revision` should be a positive integer")
        if isinstance(task_id, str) and isinstance(milestone, str):
            expected_file_prefix = f"{milestone}-{task_id}-"
            expected_task_ref = f"{milestone}-{task_id}"
            if task_ref != expected_task_ref:
                errors.append(f"{rel_path}: `task_ref` should be `{expected_task_ref}`")
            if not path.name.startswith(expected_file_prefix):
                errors.append(
                    f"{rel_path}: filename should start with `{expected_file_prefix}`"
                )
            if not path.parent.name.startswith(f"{milestone}-"):
                errors.append(
                    f"{rel_path}: parent folder should start with `{milestone}-`"
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Codex-Cursor project artifacts.")
    parser.add_argument("project_root", nargs="?", default=".", help="Project root to validate.")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    errors: list[str] = []

    for rel_path, spec in PROJECT_FILES.items():
        errors.extend(validate_file(root, rel_path, spec))
    errors.extend(validate_task_specs(root))
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
