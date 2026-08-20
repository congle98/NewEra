#!/usr/bin/env python3
"""Deterministic NewEra state/evidence governance gate.

This validator deliberately uses only the Python standard library. It validates
machine-owned lifecycle/reference fields while Markdown remains the narrative
source for human context. It never creates ACCEPTED.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

STATUSES = {
    "DRAFT", "READY", "IN_PROGRESS", "VERIFIED", "CHECKPOINT_PENDING",
    "ACCEPTED", "BLOCKED", "DEFERRED", "REJECTED", "CANCELLED",
    "NOT_RUN", "NOT_APPLICABLE", "PARTIAL", "FAILED", "NOT_STARTED",
    "OPEN", "RESOLVED", "PROPOSED", "SUPERSEDED",
}
EVIDENCE_RESULTS = {"VERIFIED", "PARTIAL", "FAILED", "BLOCKED", "NOT_RUN"}
ACCEPTANCE_STATUSES = {"NOT_ACCEPTED", "ACCEPTED", "REJECTED", "DEFERRED"}
EDGE_TYPES = {
    "specified-by", "architected-by", "planned-in", "implemented-by",
    "verified-by", "evidenced-by", "mitigates", "accepted-by",
}
EXTERNAL_ID = re.compile(r"^(SRS|ARCH|ADR|DEC|COMMIT|ACCEPTANCE|DOC)-[A-Z0-9_.-]+$")


class Gate:
    def __init__(self, root: Path, strict: bool = False) -> None:
        self.root = root
        self.strict = strict
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        (self.errors if self.strict else self.warnings).append(message)

    def load_json(self, path: Path, label: str) -> dict[str, Any] | None:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            self.error(f"{label} cannot parse JSON: {exc}")
            return None
        if not isinstance(value, dict):
            self.error(f"{label} must be a JSON object")
            return None
        return value

    def require_keys(self, obj: dict[str, Any], keys: list[str], label: str) -> None:
        for key in keys:
            if key not in obj:
                self.error(f"{label} missing required field: {key}")

    def validate(self, state_path: Path, profiles_path: Path) -> None:
        state = self.load_json(state_path, "state")
        if state is None:
            return
        profiles = self.load_json(profiles_path, "profiles")
        if profiles is None:
            return

        self.require_keys(state, ["schemaVersion", "project", "documents", "milestones", "phases", "requirements", "tasks", "tests", "evidence", "risks", "changes", "traceability"], "state")
        if state.get("schemaVersion") != 1:
            self.error("state schemaVersion must be 1")
        project = state.get("project", {})
        if not isinstance(project, dict):
            self.error("state.project must be an object")
            return
        self.require_keys(project, ["id", "status", "governanceProfile", "roadmapPath"], "state.project")
        self.check_status(project.get("status"), "state.project.status")
        profile = project.get("governanceProfile")
        profile_data = profiles.get("profiles", {}).get(profile, {})
        if not isinstance(profile_data, dict):
            self.error(f"unknown governance profile: {profile}")
        self.check_path(project.get("roadmapPath"), "state.project.roadmapPath")

        collections = ["documents", "milestones", "phases", "requirements", "tasks", "tests", "evidence", "risks", "changes"]
        ids: dict[str, str] = {}
        entities: dict[str, dict[str, dict[str, Any]]] = {}
        for collection in collections:
            value = state.get(collection, [])
            if not isinstance(value, list):
                self.error(f"state.{collection} must be an array")
                entities[collection] = {}
                continue
            entities[collection] = {}
            for index, item in enumerate(value):
                label = f"state.{collection}[{index}]"
                if not isinstance(item, dict) or not isinstance(item.get("id"), str):
                    self.error(f"{label} must be an object with string id")
                    continue
                item_id = item["id"]
                if item_id in ids:
                    self.error(f"duplicate ID {item_id} in {label}; already used by {ids[item_id]}")
                ids[item_id] = label
                entities[collection][item_id] = item
                self.check_status(item.get("status"), f"{label}.status")

        self.validate_profile_documents(entities["documents"], profile_data, profile)
        self.validate_relationships(state, entities, ids)
        self.validate_evidence(state.get("evidence", []), entities["evidence"], entities["tests"])
        self.validate_edges(state.get("traceability", []), ids)
        self.validate_profile_links(state.get("traceability", []), profile_data)
        self.validate_acceptance(state.get("acceptance"), project)

    def check_status(self, value: Any, label: str) -> None:
        if value not in STATUSES:
            self.error(f"{label} has invalid status {value!r}")

    def check_path(self, value: Any, label: str) -> None:
        if not isinstance(value, str) or not value:
            self.error(f"{label} must be a non-empty path")

    def refs(self, item: dict[str, Any], field: str, label: str, ids: dict[str, str], allow_empty: bool = False) -> None:
        value = item.get(field)
        if not isinstance(value, list) or (not value and not allow_empty):
            self.error(f"{label}.{field} must contain at least one ID")
            return
        for ref in value:
            if ref not in ids:
                self.error(f"{label}.{field} references unknown ID {ref}")

    def external_or_known(self, value: Any, ids: dict[str, str]) -> bool:
        return isinstance(value, str) and (value in ids or EXTERNAL_ID.match(value) is not None)

    def validate_profile_documents(self, documents: dict[str, dict[str, Any]], profile_data: dict[str, Any], profile: Any) -> None:
        roles = {item.get("role") for item in documents.values()}
        for role in profile_data.get("requiredDocumentRoles", []):
            if role not in roles:
                self.error(f"profile {profile} requires document role {role}")
        for item_id, item in documents.items():
            path = item.get("path")
            if not isinstance(path, str) or "<" in path or "*" in path:
                self.error(f"document {item_id} has non-concrete path {path!r}")
            elif not (self.root / path).exists():
                self.error(f"document {item_id} path does not exist: {path}")

    def validate_relationships(self, state: dict[str, Any], entities: dict[str, dict[str, dict[str, Any]]], ids: dict[str, str]) -> None:
        for item_id, item in entities["milestones"].items():
            self.refs(item, "phaseIds", f"milestone {item_id}", ids, allow_empty=item.get("status") == "DRAFT")
        for item_id, item in entities["phases"].items():
            label = f"phase {item_id}"
            if item.get("milestoneId") not in entities["milestones"]:
                self.error(f"{label}.milestoneId references unknown milestone {item.get('milestoneId')}")
            for field in ["requirementIds", "taskIds", "testIds", "evidenceIds"]:
                self.refs(item, field, label, ids, allow_empty=item.get("status") == "DRAFT")
        for item_id, item in entities["requirements"].items():
            label = f"requirement {item_id}"
            self.refs(item, "acceptanceCriteriaIds", label, ids={x: "criteria" for x in item.get("acceptanceCriteriaIds", [])})
            if not self.external_or_known(item.get("srsRef"), ids):
                self.error(f"{label}.srsRef is not a resolvable SRS reference")
            for ref in item.get("architectureRefs", []):
                if not self.external_or_known(ref, ids):
                    self.error(f"{label}.architectureRefs references unknown ID {ref}")
        for collection, fields in [("tasks", ["requirementIds", "testIds"]), ("tests", ["requirementIds", "taskIds", "evidenceIds"])]:
            for item_id, item in entities[collection].items():
                for field in fields:
                    self.refs(item, field, f"{collection[:-1]} {item_id}", ids)

        for item_id, item in entities["risks"].items():
            label = f"risk {item_id}"
            if item.get("severity") not in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
                self.error(f"{label}.severity is invalid")
            if item.get("probability") not in {"LOW", "MEDIUM", "HIGH"}:
                self.error(f"{label}.probability is invalid")
            if item.get("impact") not in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
                self.error(f"{label}.impact is invalid")
            self.refs(item, "requirementIds", label, ids)
            if item.get("taskIds"):
                self.refs(item, "taskIds", label, ids)
        for item_id, item in entities["changes"].items():
            label = f"change {item_id}"
            self.refs(item, "affectedIds", label, ids)
            if not self.external_or_known(item.get("decisionRef"), ids):
                self.error(f"{label}.decisionRef is not a resolvable decision reference")

    def validate_evidence(self, summaries: Any, evidence_entities: dict[str, dict[str, Any]], test_entities: dict[str, dict[str, Any]]) -> None:
        if not isinstance(summaries, list):
            self.error("state.evidence must be an array")
            return
        for item_id, summary in evidence_entities.items():
            path_value = summary.get("path")
            if not isinstance(path_value, str) or not path_value:
                self.error(f"evidence {item_id} has no path")
                continue
            evidence_path = self.root / path_value
            data = self.load_json(evidence_path, f"evidence {item_id}")
            if data is None:
                continue
            required = ["schemaVersion", "id", "scope", "requirementRefs", "testRefs", "type", "command", "expected", "actual", "result", "commitRef", "timestamp", "environment", "acceptanceStatus", "limitations"]
            self.require_keys(data, required, f"evidence {item_id}")
            if data.get("schemaVersion") != 1 or data.get("id") != item_id:
                self.error(f"evidence {item_id} schemaVersion/id mismatch")
            if data.get("result") not in EVIDENCE_RESULTS:
                self.error(f"evidence {item_id} has invalid result {data.get('result')!r}")
            if data.get("acceptanceStatus") not in ACCEPTANCE_STATUSES:
                self.error(f"evidence {item_id} has invalid acceptanceStatus")
            if summary.get("status") != data.get("result"):
                self.error(f"evidence {item_id} state status does not match envelope result")
            if summary.get("acceptanceStatus") != data.get("acceptanceStatus"):
                self.error(f"evidence {item_id} state acceptance does not match envelope")
        for item_id, item in test_entities.items():
            if item.get("status") == "NOT_RUN":
                self.warn(f"test {item_id} is NOT_RUN")
        for item_id, item in evidence_entities.items():
            if item.get("status") == "NOT_RUN":
                self.warn(f"evidence {item_id} is NOT_RUN")

    def validate_edges(self, edges: Any, ids: dict[str, str]) -> None:
        if not isinstance(edges, list):
            self.error("state.traceability must be an array")
            return
        for index, edge in enumerate(edges):
            label = f"traceability[{index}]"
            if not isinstance(edge, dict):
                self.error(f"{label} must be an object")
                continue
            for field in ["source", "target", "type"]:
                if field not in edge:
                    self.error(f"{label} missing {field}")
            if edge.get("source") not in ids:
                self.error(f"{label} source is unknown: {edge.get('source')}")
            if not self.external_or_known(edge.get("target"), ids):
                self.error(f"{label} target is unknown: {edge.get('target')}")
            if edge.get("type") not in EDGE_TYPES:
                self.error(f"{label} has invalid type: {edge.get('type')}")

    def validate_profile_links(self, edges: Any, profile_data: dict[str, Any]) -> None:
        if not isinstance(edges, list):
            return
        link_present = {
            "requirement-to-srs": any(e.get("type") == "specified-by" and str(e.get("source", "")).startswith("REQ-") and str(e.get("target", "")).startswith("SRS-") for e in edges if isinstance(e, dict)),
            "requirement-to-architecture": any(e.get("type") == "architected-by" and str(e.get("source", "")).startswith("REQ-") for e in edges if isinstance(e, dict)),
            "requirement-to-task": any(e.get("type") == "planned-in" and str(e.get("source", "")).startswith("REQ-") and str(e.get("target", "")).startswith("TASK-") for e in edges if isinstance(e, dict)),
            "task-to-test": any(e.get("type") == "verified-by" and str(e.get("source", "")).startswith("TASK-") and str(e.get("target", "")).startswith("TEST-") for e in edges if isinstance(e, dict)),
            "test-to-evidence": any(e.get("type") == "evidenced-by" and str(e.get("source", "")).startswith("TEST-") and str(e.get("target", "")).startswith("EVD-") for e in edges if isinstance(e, dict)),
            "requirement-to-risk": any(e.get("type") == "mitigates" and str(e.get("target", "")).startswith("REQ-") for e in edges if isinstance(e, dict)),
            "risk-to-task": any(e.get("type") == "planned-in" and str(e.get("source", "")).startswith("RISK-") and str(e.get("target", "")).startswith("TASK-") for e in edges if isinstance(e, dict)),
        }
        for required in profile_data.get("requiredLinks", []):
            if not link_present.get(required, False):
                self.error(f"profile requires traceability link type {required}")

    def validate_acceptance(self, acceptance: Any, project: dict[str, Any]) -> None:
        if not isinstance(acceptance, dict):
            self.error("state.acceptance must be an object")
            return
        status = acceptance.get("status")
        if status not in ACCEPTANCE_STATUSES:
            self.error(f"state.acceptance has invalid status {status!r}")
        if status == "ACCEPTED" and not acceptance.get("decisionRef"):
            self.error("ACCEPTED state requires acceptance.decisionRef")
        if project.get("status") == "ACCEPTED" and status != "ACCEPTED":
            self.error("project status ACCEPTED conflicts with acceptance status")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the NewEra deterministic governance gate")
    parser.add_argument("--state", default=".newera/project-state.json")
    parser.add_argument("--profiles", default=".newera/governance-profiles.json")
    parser.add_argument("--strict", action="store_true", help="Treat incomplete NOT_RUN checks as failures")
    args = parser.parse_args()
    root = Path.cwd()
    gate = Gate(root, strict=args.strict)
    gate.validate(root / args.state, root / args.profiles)
    for warning in gate.warnings:
        print(f"WARN: {warning}")
    for error in gate.errors:
        print(f"ERROR: {error}")
    if gate.errors:
        print(f"GOVERNANCE GATE: FAIL ({len(gate.errors)} error(s), {len(gate.warnings)} warning(s))")
        return 1
    if gate.warnings:
        print(f"GOVERNANCE GATE: WARN ({len(gate.warnings)} warning(s))")
        return 0
    print("GOVERNANCE GATE: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
