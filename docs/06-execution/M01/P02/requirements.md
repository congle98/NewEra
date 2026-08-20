# M01-P02 - Phase Requirements

- Phase: M01-P02
- M/ROADMAP: `docs/02-roadmap/roadmap.md`
- SRS: `REQ-NEWERA-P0-004`, `REQ-NEWERA-P0-005`
- Trạng thái: IN_PROGRESS

## Bối cảnh/outcome

P02 biến state/evidence contract thành deterministic STANDARD gate. Gate có default WARN cho work-in-progress và strict FAIL trước checkpoint nếu còn NOT_RUN; không auto-accept.

## Requirements

| ID | Acceptance criteria | Artifact | Status |
|---|---|---|---|
| REQ-NEWERA-P0-004 | AC-NEWERA-P0-007, AC-NEWERA-P0-008 | `scripts/newera_validate.py`, invalid fixture | IN_PROGRESS |
| REQ-NEWERA-P0-005 | AC-NEWERA-P0-009 | `.newera/governance-profiles.json` | IN_PROGRESS |

## Gate scope

- Schema/version and JSON parse.
- Valid status and unique IDs.
- Profile required document roles.
- Requirement/task/test/evidence completeness.
- Typed edge resolution.
- Acceptance conflict prevention.

Semantic drift, impact analysis, risk graph and adaptive runtime profiles are P1.
