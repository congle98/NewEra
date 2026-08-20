"""Generate a traceability-backed verification matrix from NewEra state."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from newera_impact import build_graph, downstream, load_state

TEST_TYPES = ("static", "unit", "integration", "e2e", "security", "product", "gate")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", default=".newera/project-state.json")
    parser.add_argument("--requirement", action="append", dest="requirements", help="limit rows; repeatable")
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    args = parser.parse_args()
    try:
        state = load_state(Path(args.state))
        entities, edges = build_graph(state)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"VERIFICATION MATRIX: FAIL ({exc})", file=sys.stderr)
        return 1
    requirements = args.requirements or [item["id"] for item in state.get("requirements", []) if isinstance(item, dict) and item.get("status") != "DRAFT"]
    unknown = sorted(set(requirements) - set(entities))
    if unknown:
        print(f"VERIFICATION MATRIX: FAIL unknown requirement ID(s): {', '.join(unknown)}", file=sys.stderr)
        return 1
    rows: list[dict[str, Any]] = []
    for requirement_id in requirements:
        impacted = downstream([requirement_id], entities, edges)
        tests = [item_id for item_id in impacted if entities[item_id].get("kind") == "test"]
        cells = {test_type: [] for test_type in TEST_TYPES}
        for test_id in tests:
            test_type = entities[test_id].get("type", "gate")
            cells.setdefault(test_type, []).append(test_id)
        evidence_ids = sorted({item_id for item_id in impacted if entities[item_id].get("kind") == "evidence"})
        rows.append({"requirementId": requirement_id, "status": entities[requirement_id].get("status"), "tests": cells, "evidenceIds": evidence_ids})
    result = {"requirements": rows, "testTypes": list(TEST_TYPES)}
    if args.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("| Requirement | Static | Unit | Integration | E2E | Security | Product | Gate | Evidence |")
        print("|---|---|---|---|---|---|---|---|---|")
        for row in rows:
            cells = [", ".join(row["tests"].get(test_type, [])) or "—" for test_type in TEST_TYPES]
            evidence = ", ".join(row["evidenceIds"]) or "—"
            print(f"| {row['requirementId']} ({row['status']}) | " + " | ".join(cells) + f" | {evidence} |")
        print("VERIFICATION MATRIX: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
