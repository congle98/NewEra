"""Deterministic graph-based change impact analysis for NewEra.

The state graph is the machine source of truth for lifecycle/reference edges.
This command reports downstream impact only; it does not change state or accept
changes. Semantic similarity is intentionally outside this deterministic tool.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any


def load_state(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("state must be a JSON object")
    return value


def build_graph(state: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, list[str]]]:
    entities: dict[str, dict[str, Any]] = {}
    for collection in ("documents", "milestones", "phases", "requirements", "tasks", "tests", "evidence", "risks", "changes"):
        for item in state.get(collection, []):
            if isinstance(item, dict) and isinstance(item.get("id"), str):
                entities[item["id"]] = {"kind": collection.rstrip("s"), **item}
    edges: dict[str, list[str]] = defaultdict(list)
    for edge in state.get("traceability", []):
        if isinstance(edge, dict) and edge.get("source") in entities and isinstance(edge.get("target"), str):
            edges[edge["source"]].append(edge["target"])
    return entities, edges


def downstream(roots: list[str], entities: dict[str, dict[str, Any]], edges: dict[str, list[str]]) -> list[str]:
    seen: set[str] = set()
    queue = deque(roots)
    for root in roots:
        entity = entities.get(root, {})
        if entity.get("kind") == "change":
            queue.extend(ref for ref in entity.get("affectedIds", []) if ref in entities)
        if entity.get("kind") == "risk":
            queue.extend(ref for ref in entity.get("requirementIds", []) if ref in entities)
    while queue:
        current = queue.popleft()
        if current in seen:
            continue
        seen.add(current)
        queue.extend(target for target in edges.get(current, []) if target in entities and target not in seen)
    return sorted(seen)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", default=".newera/project-state.json")
    parser.add_argument("--id", dest="roots", action="append", required=True, help="root ID; repeat for multiple roots")
    parser.add_argument("--format", choices=("json", "text"), default="text")
    args = parser.parse_args()
    try:
        entities, edges = build_graph(load_state(Path(args.state)))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"IMPACT ANALYSIS: FAIL ({exc})", file=sys.stderr)
        return 1
    unknown = sorted(set(args.roots) - set(entities))
    if unknown:
        print(f"IMPACT ANALYSIS: FAIL unknown root ID(s): {', '.join(unknown)}", file=sys.stderr)
        return 1
    impacted = downstream(args.roots, entities, edges)
    rows = [{"id": item_id, "kind": entities[item_id]["kind"], "status": entities[item_id].get("status")} for item_id in impacted]
    result = {"roots": args.roots, "count": len(rows), "impacted": rows}
    if args.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("CHANGE IMPACT ANALYSIS")
        print(f"roots: {', '.join(args.roots)}")
        for row in rows:
            print(f"- {row['id']} [{row['kind']}] status={row['status']}")
        print(f"IMPACT ANALYSIS: PASS impacted={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
