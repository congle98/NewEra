# Requirements Traceability

Traceability là capability nhận diện của NewEra. Markdown matrix phục vụ human review; `.newera/project-state.json` giữ machine lifecycle/reference/typed edge. Không duy trì hai quan hệ độc lập: nếu mismatch, gate FAIL.

## P0 matrix

| Requirement | SRS | Architecture | ROADMAP/Phase | Task | Test | Evidence | Status |
|---|---|---|---|---|---|---|---|
| REQ-NEWERA-P0-001 | SRS-NEWERA-P0-001 | ARCH-NEWERA-AUTO-001 | M01-P01 | TASK-NEWERA-P01-001/002 | TEST-NEWERA-P01-001/002 | EVD-NEWERA-P0-001 | IN_PROGRESS |
| REQ-NEWERA-P0-002 | SRS-NEWERA-P0-002 | ARCH-NEWERA-AUTO-001 | M01-P01 | TASK-NEWERA-P01-001/002 | TEST-NEWERA-P01-001 | EVD-NEWERA-P0-001 | IN_PROGRESS |
| REQ-NEWERA-P0-003 | SRS-NEWERA-P0-003 | ARCH-NEWERA-AUTO-001 | M01-P01 | TASK-NEWERA-P01-002 | TEST-NEWERA-P01-002 | EVD-NEWERA-P0-001 | IN_PROGRESS |
| REQ-NEWERA-P0-004 | SRS-NEWERA-P0-004 | ARCH-NEWERA-AUTO-002 | M01-P02 | TASK-NEWERA-P02-001/002 | TEST-NEWERA-P02-001 | EVD-NEWERA-P0-001 | IN_PROGRESS |
| REQ-NEWERA-P0-005 | SRS-NEWERA-P0-005 | ARCH-NEWERA-AUTO-002 | M01-P02 | TASK-NEWERA-P02-002 | TEST-NEWERA-P02-002 | EVD-NEWERA-P0-001 | IN_PROGRESS |

## Typed graph edges

| Source | Type | Target | Owner |
|---|---|---|---|
| REQ-NEWERA-P0-* | specified-by | SRS-NEWERA-P0-* | State + SRS |
| REQ-NEWERA-P0-* | architected-by | ARCH-NEWERA-AUTO-* | State + Architecture |
| REQ-NEWERA-P0-* | planned-in | TASK-NEWERA-* | State + Phase task |
| TASK-NEWERA-* | verified-by | TEST-NEWERA-* | State + test plan |
| TEST-NEWERA-* | evidenced-by | EVD-NEWERA-P0-001 | State + evidence envelope |
| EVD-NEWERA-P0-001 | accepted-by | DEC-/acceptance decision | Future human decision |

## P1 backlog traceability

| Requirement | Future capability | Dependency | Status |
|---|---|---|---|
| REQ-NEWERA-P1-001 | Adaptive LITE/STRICT | STANDARD stable | DRAFT |
| REQ-NEWERA-P1-002 | Machine change management | State/graph | DRAFT |
| REQ-NEWERA-P1-003 | Impact analysis + verification matrix | Graph | DRAFT |
| REQ-NEWERA-P1-004 | Risk register/graph | State/profile | DRAFT |
| REQ-NEWERA-P1-005 | Deterministic then semantic drift detection | Gate/graph | DRAFT |

## Quy tắc

1. Requirement thật phải có SRS, Architecture reference khi cần, M/Phase, task, test và evidence reference.
2. Task không có requirement hoặc test, test không có evidence và evidence không có requirement là governance failure.
3. `PASS`/`FAIL` là check-level; evidence-level dùng `VERIFIED`/`PARTIAL`/`FAILED`/`BLOCKED`/`NOT_RUN`.
4. Git commit/worktree là version reference; acceptance là decision riêng, không suy ra từ graph edge.
5. Không map P1 vào M01 P0 nếu chưa có CR/ROADMAP update.
6. Graph projection có thể được sinh từ state; không sửa tay projection để che mismatch.
