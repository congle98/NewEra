"""Two-tier requirement drift detector.

The deterministic tier checks explicit IDs and declared path prefixes. The
semantic tier is deliberately advisory and is not implemented as a blocker.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path, PurePosixPath
from typing import Any


def load_state(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("state must be a JSON object")
    return value


def ids_in_state(state: dict[str, Any]) -> set[str]:
    result: set[str] = set()
    for collection in ("documents", "milestones", "phases", "requirements", "tasks", "tests", "evidence", "risks", "changes"):
        result.update(item["id"] for item in state.get(collection, []) if isinstance(item, dict) and isinstance(item.get("id"), str))
    return result


def path_allowed(changed: str, declarations: list[str]) -> bool:
    candidate = PurePosixPath(changed)
    for declaration in declarations:
        prefix = declaration.rstrip("/")
        if changed == prefix or changed.startswith(prefix + "/"):
            return True
        if candidate.match(declaration):
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", default=".newera/project-state.json")
    parser.add_argument("--changed-id", action="append", default=[])
    parser.add_argument("--changed-path", action="append", default=[])
    parser.add_argument("--declared-path", action="append", default=[])
    parser.add_argument("--semantic-advisory", action="store_true", help="report semantic tier as advisory; never changes exit status")
    args = parser.parse_args()
    try:
        known_ids = ids_in_state(load_state(Path(args.state)))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"DRIFT DETECTION: FAIL ({exc})", file=sys.stderr)
        return 1
    drift: list[str] = []
    for changed_id in args.changed_id:
        if changed_id not in known_ids:
            drift.append(f"changed ID is not declared in state: {changed_id}")
    if args.changed_path and not args.declared_path:
        drift.append("changed paths were supplied without declared path scope")
    for changed_path in args.changed_path:
        if args.declared_path and not path_allowed(changed_path, args.declared_path):
            drift.append(f"changed path is outside declared scope: {changed_path}")
    if drift:
        print("DETERMINISTIC DRIFT: FAIL")
        for item in drift:
            print(f"- {item}")
    else:
        print("DETERMINISTIC DRIFT: PASS")
    if args.semantic_advisory:
        print("SEMANTIC DRIFT: ADVISORY_NOT_RUN (non-blocking)")
    return 1 if drift else 0


if __name__ == "__main__":
    raise SystemExit(main())
