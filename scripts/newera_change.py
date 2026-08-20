"""Compare two NewEra machine states and report requirement version drift.

This is a read-only deterministic projection. It does not write a change record,
modify ROADMAP, or infer acceptance; a human/Change Control decision remains
required before the resulting change is accepted.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def requirements(path: Path) -> dict[str, dict[str, Any]]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain an object")
    result = {}
    for item in value.get("requirements", []):
        if isinstance(item, dict) and isinstance(item.get("id"), str):
            result[item["id"]] = item
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--before", required=True, help="baseline project-state.json")
    parser.add_argument("--after", required=True, help="candidate project-state.json")
    parser.add_argument("--format", choices=("json", "text"), default="text")
    args = parser.parse_args()
    try:
        before = requirements(Path(args.before))
        after = requirements(Path(args.after))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"CHANGE DIFF: FAIL ({exc})", file=sys.stderr)
        return 1
    added = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    modified = sorted(item_id for item_id in set(before) & set(after) if before[item_id] != after[item_id])
    result = {"added": added, "removed": removed, "modified": modified, "changed": bool(added or removed or modified)}
    if args.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("REQUIREMENT VERSION DIFF")
        for label in ("added", "removed", "modified"):
            values = result[label]
            print(f"{label}: {', '.join(values) if values else '—'}")
        print(f"CHANGE DIFF: {'CHANGED' if result['changed'] else 'UNCHANGED'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
