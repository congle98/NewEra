# Software Requirements Specification (SRS)

SRS là contract yêu cầu của **project sử dụng NewEra**. Đây là reference template: không điền scope của repository NewEra vào file này; adopter tạo bản sở hữu trong workspace theo `docs/00-governance/ADOPTION.md`. ROADMAP sở hữu M/Phase/scope/order; SRS sở hữu ý nghĩa requirement và acceptance criteria; Architecture sở hữu solution/boundary; `task.md` sở hữu execution/test/evidence/checkpoint.

## Document control

- SRS ID:
- Kernel release/source: `NEWERA_VERSION` / `SOURCE_COMMIT`
- Project registry reference:
- Project/product:
- Version:
- Owner:
- Reviewer/approver:
- Ngày tạo/cập nhật:
- Trạng thái: DRAFT | IN_PROGRESS | READY | SUPERSEDED
- ROADMAP reference:
- Change/decision/research references:
- Supersedes/superseded by:

## SRS quality rule

Requirement phải trả lời được: **ai** cần gì, **trong điều kiện nào**, hệ thống/project phải làm gì, kết quả nào quan sát/đo được và **khi nào được coi là đạt**. Không dùng SRS để chốt công nghệ hoặc chi tiết implementation nếu chưa thuộc Architecture/ADR.

Mỗi requirement phải có ID ổn định, priority, source, owner, dependency/risk khi cần, acceptance criteria đo được và đường truy nguyên tới ROADMAP, Phase, task, test và evidence. Nội dung chưa đủ dữ liệu phải ghi `OPEN`, `ASSUMED` hoặc `BLOCKED`.

## 1. Executive summary và problem statement

- Product/project là gì:
- Vấn đề hoặc cơ hội:
- Ai bị ảnh hưởng và mức độ:
- Cách giải quyết hiện tại:
- Vì sao cần thay đổi bây giờ:
- Hậu quả nếu không làm:
- Evidence/research supporting problem:

## 2. Goals, non-goals và success measures

### Goals

| ID | Goal/outcome | Baseline | Target | Measurement/source | Owner | Due/release |
|---|---|---|---|---|---|---|
| OBJ-<OBJ-ID> | | | | | | |

### Non-goals

- Không làm:
- Không cam kết:
- Điều kiện để mở lại non-goal:

### Success and failure criteria

- Success criteria:
- Failure/stop criteria:
- Tolerance/exception policy:
- Người/role đánh giá:

## 3. Stakeholders, users và use cases

| ID | Actor/stakeholder | Need/concern | Decision/usage | Acceptance role | Owner/contact |
|---|---|---|---|---|---|
| STAKEHOLDER-<STAKEHOLDER-ID> | | | | | |
| USER-<USER-ID> | | | | | |

### Use case template

#### UC-<UC-ID> - <Tên use case>

- Actor:
- Goal:
- Trigger:
- Preconditions:
- Main flow:
- Alternate/error flows:
- Postconditions:
- Data/security/privacy concern:
- Related requirements:
- Acceptance evidence:

## 4. Glossary và domain rules

| Term/ID | Meaning | Allowed values/rules | Source/owner |
|---|---|---|---|
| | | | |

- BR-<BR-ID>:
- DATA-<DATA-ID>:
- Glossary decisions/unknowns:

## 5. Scope và boundary

### In scope

- Capability/outcome:
- User/process boundary:
- Data boundary:
- M/Phase mapping:

### Out of scope

- Capability intentionally excluded:
- Technical/runtime exclusion:
- Project/organization boundary:

### Interfaces and external systems

| ID | System/actor | Direction | Contract/input/output | Owner | Availability/security constraint |
|---|---|---|---|---|---|
| INT-<INT-ID> | | | | | |

## 6. Functional requirements

### REQ-<REQ-ID> - <Tên requirement nguyên tử>

- Tên ngắn:
- Mục tiêu/outcome:
- Actor/role:
- Trigger/input:
- Preconditions:
- Behavior/business rule:
- Output/state change:
- Main flow:
- Alternate/error/edge cases:
- Data/privacy/security constraints:
- Priority: MUST | SHOULD | COULD | WON'T
- Source: intake/charter/research/ROADMAP/decision/feedback
- Owner:
- M/Phase:
- Dependency:
- Risk/mitigation:
- Related use cases/glossary:
- Architecture/ADR reference:
- Task/test/evidence references:
- Lifecycle status: DRAFT | READY | IN_PROGRESS | BLOCKED | CLOSED | DEFERRED | CANCELLED
- Verification status: NOT_RUN | PARTIAL | VERIFIED | FAILED | BLOCKED | NOT_APPLICABLE

#### Acceptance criteria

Acceptance criteria phải độc lập, observable và testable. Dùng Given/When/Then hoặc điều kiện đo rõ; mỗi criteria có ID.

| ID | Given/precondition | When/action | Then/expected result | Measurement/tolerance | Test/evidence reference | Status |
|---|---|---|---|---|---|---|
| AC-<AC-PRIMARY-ID> | | | | | | NOT_RUN |
| AC-<AC-SECONDARY-ID> | | | | | | NOT_RUN |

#### Requirement review checklist

- [ ] Requirement là một outcome/hành vi nguyên tử.
- [ ] Actor, trigger, input, behavior, output và edge cases đã rõ.
- [ ] Priority, owner, source và M/Phase đã có.
- [ ] Acceptance criteria có ID, expected result và measurement.
- [ ] Dependency, assumption và risk đã ghi hoặc xác nhận `NONE`.
- [ ] Không trộn solution design chưa được Architecture/ADR duyệt.
- [ ] Có đường truy nguyên tới task, test và evidence hoặc lý do `NOT_APPLICABLE`.
- [ ] Requirement không tạo scope ngoài ROADMAP.

## 7. Non-functional, security và operational requirements

Mỗi NFR phải có baseline, target, threshold/tolerance, measurement method, environment, owner và failure response.

| ID | Category | Requirement | Baseline | Target/threshold | Measurement/test | Environment | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| NFR-<NFR-ID> | Performance/scale | | | | | | | DRAFT |
| SEC-<SEC-ID> | Security/privacy | | | | | | | DRAFT |
| OPS-<OPS-ID> | Availability/operations | | | | | | | DRAFT |
| DATA-<DATA-ID> | Integrity/retention | | | | | | | DRAFT |
| UX-<UX-ID> | Usability/accessibility | | | | | | | DRAFT |
| COMP-<COMP-ID> | Compatibility/compliance | | | | | | | DRAFT |

Categories có thể gồm performance, availability, scalability, security, privacy, accessibility, compatibility, observability, operations, data integrity, cost và compliance.

## 8. Data, privacy và integration contract

- Data entities/classification:
- Source/system of record:
- Ownership/steward:
- Retention/deletion:
- PII/sensitive data handling:
- Input validation/error handling:
- Migration/backward compatibility:
- API/event/file contract:
- Authentication/authorization/audit:
- Secret/config boundary:

## 9. Assumptions, constraints, dependencies và risks

| ID | Type | Statement | Owner | Validation/expiry | Impact if false | Status |
|---|---|---|---|---|---|---|
| ASM-<ASM-ID> | Assumption | | | | | OPEN |
| CON-<CON-ID> | Constraint | | | | | OPEN |
| DEP-<DEP-ID> | Dependency | | | | | OPEN |
| RISK-<RISK-ID> | Risk | | | | | OPEN |

Open questions phải có owner, next action và due/review date; không biến assumption thành fact nếu chưa kiểm chứng.

## 10. Release/acceptance boundary

- Release slice/Milestone:
- Requirement set included:
- Known exclusions:
- Required environments/data/accounts:
- Rollback/stop condition:
- Product acceptance role:
- Evidence required:
- Checkpoint condition:
- Residual/deferred acceptance policy:

## 11. Traceability matrix

SRS là canonical source cho traceability cấp product requirement. Phase-level execution traceability nằm trong `task.md`; không tạo file traceability độc lập.

| Requirement | ROADMAP/M/Phase | Architecture/ADR | Task | Test | Evidence in task.md | Phase report | Acceptance | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-<REQ-ID> | | | TASK-<TASK-ID> | TEST-<TEST-ID> | EVD-<EVD-ID> | RPT-<RPT-ID> | PENDING | DRAFT |

### Phase traceability view

| Requirement | ROADMAP | Phase | Task | Test | Evidence | Status |
|---|---|---|---|---|---|
| REQ-<REQ-ID> | <M-ID> | <M-ID>-<P-ID> | TASK-<TASK-ID> | TEST-<TEST-ID> | EVD-<EVD-ID> | DRAFT |

Không đánh dấu requirement là `VERIFIED` nếu chưa có test/evidence hoặc lý do `NOT_APPLICABLE` rõ ràng. Không đánh dấu `ACCEPTED` dựa chỉ trên ma trận này; áp dụng `docs/03-requirements/acceptance-policy.md`.

## 12. SRS readiness và change checklist

### Ready for ROADMAP/Phase planning

- [ ] Problem, goals, users và non-goals đã review.
- [ ] In/out scope và boundary đã rõ.
- [ ] Functional requirements atomic, có priority/owner/source.
- [ ] Acceptance criteria observable/testable và có ID.
- [ ] NFR/security/data/operations có metric hoặc lý do N/A.
- [ ] Assumptions, constraints, dependencies, risks và open questions có owner.
- [ ] Architecture/environment/registry dependency đã xác định.
- [ ] Requirement IDs ổn định và traceability plan sẵn sàng.

### Ready for implementation

- [ ] ROADMAP đã chấp thuận M/Phase/scope.
- [ ] Phase requirements đã phân rã từ SRS mà không đổi nghĩa.
- [ ] Mọi requirement trong Phase có task/test/evidence plan trong `task.md`.
- [ ] Không còn blocker/precondition chưa được xử lý hoặc ghi rõ.

### Change control

Không sửa requirement/acceptance criteria/scope âm thầm. Mọi thay đổi phải ghi CR, impact tới ROADMAP/Architecture/task/test/evidence, người quyết định, ngày hiệu lực và requirement/version history.

SRS không tự tạo acceptance; áp dụng `docs/03-requirements/acceptance-policy.md` cho verification, checkpoint và acceptance authority.
