# Software Requirements Specification

SRS là nguồn sự thật cho yêu cầu và acceptance criteria của NewEra kernel. ROADMAP vẫn là nguồn sự thật cho M/Phase/scope/order; `.newera/project-state.json` là machine owner cho lifecycle/reference/edge, không thay thế narrative.

- SRS ID/version: SRS-NEWERA-001 / v0.2
- Nguồn scope: CR-001, DEC-001, `docs/02-roadmap/roadmap.md`
- Owner/reviewer: NewEra maintainer / user
- Ngày: 2026-08-20
- Trạng thái: IN_PROGRESS

## 1. Bối cảnh và problem statement

NewEra hiện có governance bằng Markdown và askAgent hooks. Markdown tốt cho con người nhưng không đủ ổn định để Kiro đọc/ghi/validate lifecycle, reference, evidence và completeness một cách deterministic. P0 bổ sung machine contract mà không bỏ Markdown narrative.

## 2. Mục tiêu và outcome

- `OBJ-NEWERA-001`: Kiro có thể kiểm tra cấu trúc governance bằng state/evidence/schema/gate mà không tự tạo acceptance.
- `OBJ-NEWERA-002`: Traceability trở thành capability nhận diện, đi từ requirement đến task/test/evidence và version reference.
- `OBJ-NEWERA-003`: STANDARD profile có contract rõ; adaptive LITE/STRICT chỉ triển khai sau P0.

## 3. Users/use cases

| ID | Actor | Use case | Kết quả |
|---|---|---|---|
| USER-NEWERA-001 | Kiro/agent | Đọc state, tìm artifact còn thiếu, chạy gate | Nhận WARN/FAIL/PASS deterministic |
| USER-NEWERA-002 | Maintainer | Review graph/evidence và thay đổi scope | Có edge/reference/CR rõ ràng |
| USER-NEWERA-003 | Human acceptor | Xem evidence/checkpoint và quyết định | Acceptance vẫn tách khỏi verification |

## 4. P0 Functional Requirements

### REQ-NEWERA-P0-001 — Machine-readable Project State

- **Mục tiêu:** state versioned chứa project/profile/M/Phase/requirement/task/test/evidence/edge references.
- **Acceptance criteria:**
  - `AC-NEWERA-P0-001`: `.newera/project-state.json` parse được và có `schemaVersion`.
  - `AC-NEWERA-P0-002`: entity IDs/status/reference được validator kiểm tra; trạng thái lạ bị FAIL.
- **Thuộc:** M01-P01.
- **Trạng thái:** IN_PROGRESS.

### REQ-NEWERA-P0-002 — Evidence Schema

- **Mục tiêu:** evidence envelope máy đọc có required metadata, result và acceptance separation.
- **Acceptance criteria:**
  - `AC-NEWERA-P0-003`: evidence có ID, scope, requirementRefs, testRefs, type, command, expected, actual, result, commitRef, timestamp, environment, acceptanceStatus và limitations.
  - `AC-NEWERA-P0-004`: evidence `VERIFIED` không làm acceptance thành `ACCEPTED`; `NOT_RUN` được gate cảnh báo/strict chặn.
- **Thuộc:** M01-P01.
- **Trạng thái:** IN_PROGRESS.

### REQ-NEWERA-P0-003 — Traceability Core

- **Mục tiêu:** typed edges nối requirement → SRS/architecture → task → test → evidence; version reference được lưu rõ.
- **Acceptance criteria:**
  - `AC-NEWERA-P0-005`: task phải có requirementRefs và testRefs; test phải có evidenceRefs.
  - `AC-NEWERA-P0-006`: edge source/target/type được validate và reference không resolve bị FAIL.
- **Thuộc:** M01-P01.
- **Trạng thái:** IN_PROGRESS.

### REQ-NEWERA-P0-004 — STANDARD Automated Governance Gate

- **Mục tiêu:** gate deterministic phát hiện thiếu requirement/test/evidence, status/reference/profile conflict.
- **Acceptance criteria:**
  - `AC-NEWERA-P0-007`: state hiện tại có thể chạy gate và trả `WARN` khi còn `NOT_RUN` mà không có structural error.
  - `AC-NEWERA-P0-008`: state thiếu requirement/task/evidence link trả exit code non-zero và message lỗi cụ thể.
- **Thuộc:** M01-P02.
- **Trạng thái:** IN_PROGRESS.

### REQ-NEWERA-P0-005 — STANDARD Profile Invariants

- **Mục tiêu:** profile active yêu cầu roadmap, SRS, architecture, task, test, evidence và acceptance roles.
- **Acceptance criteria:**
  - `AC-NEWERA-P0-009`: profile STANDARD được đọc từ `.newera/governance-profiles.json` và required roles được gate kiểm tra.
- **Thuộc:** M01-P02.
- **Trạng thái:** IN_PROGRESS.

## 5. P1 Requirements đã phê duyệt về hướng

| ID | Mục tiêu | Dependency | Trạng thái |
|---|---|---|---|
| REQ-NEWERA-P1-001 | Adaptive LITE/STRICT enforcement sau STANDARD stable | M01 P0 | DRAFT |
| REQ-NEWERA-P1-002 | Machine-integrated change management và requirement diff | State/graph | DRAFT |
| REQ-NEWERA-P1-003 | Change impact analysis và generated verification matrix | Traceability graph | DRAFT |
| REQ-NEWERA-P1-004 | Risk register/graph và STRICT security/operations checks | Profile/gate | DRAFT |
| REQ-NEWERA-P1-005 | Deterministic drift detection, semantic advisory sau đó | Graph/gate | DRAFT |

P1 không được triển khai bằng cách nới lỏng P0. Semantic drift chỉ advisory cho tới khi có precision/override policy được quyết định.

## 6. Non-functional Requirements

| ID | Thuộc tính | Tiêu chí |
|---|---|---|
| NFR-NEWERA-P0-001 | Determinism | Cùng state/input cho cùng gate result và exit code |
| NFR-NEWERA-P0-002 | Technology neutrality | P0 dùng Python standard library; không khóa application runtime |
| NFR-NEWERA-P0-003 | Auditability | Schema version, command, actual, commit/worktree và limitation được lưu |
| NFR-NEWERA-P0-004 | Status honesty | Không profile/gate nào tự tạo `ACCEPTED` |
| NFR-NEWERA-P0-005 | Reversibility | State/schema migration có version; Markdown narrative không bị xóa |

## 7. Data/traceability contract

- State entities: milestone, phase, requirement, task, test, evidence, document.
- Evidence envelope: `.newera/evidence/EVD-*.json`.
- Human evidence: `docs/07-evidence/`.
- Git SHA/worktree là external version reference, không tự biến thành product requirement.
- Typed edges: `specified-by`, `architected-by`, `planned-in`, `verified-by`, `evidenced-by`, `accepted-by`.

## 8. Security/operations

P0 không xử lý application auth/database/deployment. Không lưu secret trong state/evidence. Khi project con kích hoạt risk/security/operations, registry và STRICT profile P1 sẽ yêu cầu artifact tương ứng.

## 9. Acceptance criteria quality gate

Mỗi criteria có actor/input/action/expected result hoặc điều kiện đo, có ID và map tới test/evidence. Requirement chỉ `VERIFIED` khi criteria đạt; chỉ `ACCEPTED` sau decision của human/role. Current P0 implementation remains `CHECKPOINT_PENDING`/`NOT_ACCEPTED` until evidence and review complete.

## 10. Traceability

Xem `requirements-traceability.md` và `.newera/project-state.json`. Markdown table là human projection; state graph là machine reference owner cho P0.
