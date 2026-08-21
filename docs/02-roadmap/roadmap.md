# ROADMAP

> ROADMAP là nguồn sự thật cao nhất của **project sử dụng NewEra** cho M, Phase, scope, dependency, thứ tự và điều kiện chuyển tiếp. Đây là template; repository NewEra không tự điền roadmap của chính nó.

## Document control

- Project/product:
- ROADMAP ID/version:
- Owner:
- Product decision maker:
- Ngày tạo/cập nhật:
- Trạng thái: DRAFT | IN_PROGRESS | READY | SUPERSEDED
- Source: charter/SRS/research/decision/change requests:
- Review cadence:
- Supersedes/superseded by:

## 1. Vision, outcomes và success measures

- Product/problem statement:
- Target users/stakeholders:
- Desired outcome:
- Baseline hiện tại:
- Target đo được:
- Success metrics/source/owner:
- Failure/stop criteria:
- Time/cost/capacity boundary:

## 2. Planning principles và scope guard

- M là outcome lớn có ý nghĩa với product/project, không phải module kỹ thuật.
- Phase là khối outcome có thể thực hiện và kiểm chứng độc lập.
- Task là việc cụ thể có output, dependency, requirement và verification.
- ROADMAP không chứa solution detail thuộc Architecture/SRS.
- Không thêm outcome, requirement, dependency hoặc timeline âm thầm.
- Chưa đủ dữ liệu phải ghi `OPEN`, `ASSUMED` hoặc `BLOCKED`.

### Scope ledger

| Scope ID | Included/excluded | Description | Source/decision | M/Phase | Status |
|---|---|---|---|---|---|
| SCOPE-XXX | IN | | | | DRAFT |
| SCOPE-YYY | OUT | | | | DRAFT |

## 3. Milestone index

| M ID | Tên/outcome | Priority | Phase order | Dependency | Target window | Owner | Status | Readiness gap |
|---|---|---|---|---|---|---|---|---|
| <M-ID> | | MUST/SHOULD/COULD | <P-ID> → <P-ID> | | | | DRAFT | |

Status chỉ là lifecycle planning; `VERIFIED`, `CHECKPOINT_PENDING` và `ACCEPTED` phải theo status model, không suy ra từ việc có row trong bảng.

## 4. Milestone definition template

### <M-ID> - <Tên milestone/outcome>

- Mục tiêu/outcome:
- Success measure/baseline/target:
- Product decision/owner:
- Priority:
- Planned window/release:
- ROADMAP source:
- In scope:
- Out of scope:
- Requirement/objective IDs:
- Dependency/precondition:
- Assumption/research/decision:
- Risk/owner/mitigation:
- Capacity/budget constraint:
- Acceptance boundary:
- Status: DRAFT | READY | IN_PROGRESS | VERIFIED | CHECKPOINT_PENDING | ACCEPTED | BLOCKED | DEFERRED

#### Phase order and outcome

| Phase | Independent outcome | Requirements | Task/test/evidence in task.md | Dependency | Exit criteria | Owner | Status |
|---|---|---|---|---|---|---|---|
| <M-ID>-<P-ID> | | | | | | | DRAFT |

#### Milestone readiness checklist

- [ ] Outcome và success measure có thể đo/quan sát.
- [ ] In/out scope và acceptance boundary đã rõ.
- [ ] Phase order/dependency đã được review.
- [ ] Requirement/SRS source đã xác định.
- [ ] Architecture/environment/registry trigger đã xác định.
- [ ] Owner, reviewer, capacity và target window đã có.
- [ ] Risk/assumption/open question có owner và next action.
- [ ] Change/decision history đã liên kết.

#### Milestone completion checklist

- [ ] Mọi Phase exit criteria đạt hoặc chuyển residual/blocker có ID.
- [ ] `requirements.md` và `task.md` của mọi Phase đã đủ; task.md có test/evidence/checkpoint.
- [ ] Phase report, residual, debt và traceability đã cập nhật.
- [ ] Milestone report đã tạo.
- [ ] Scope/outcome được đối chiếu với success measure.
- [ ] Chỉ chuyển acceptance sau quyết định của người/role có thẩm quyền.

## 5. Phase definition template

### <M-ID>-<P-ID> - <Tên Phase>

- Independent outcome:
- In scope:
- Out of scope:
- Requirement/SRS IDs:
- Architecture/ADR references:
- Environment/registry references:
- Dependency/precondition:
- Owner/reviewer:
- Target window:
- Entry criteria:
- Exit criteria:
- Risk/blocker/mitigation:
- Status: DRAFT

#### Phase Definition of Ready

- [ ] Phase tồn tại trong ROADMAP và không trùng/đè scope Phase khác.
- [ ] Outcome, in/out scope và acceptance boundary đã review.
- [ ] Requirements có ID và acceptance criteria.
- [ ] `task.md` được tạo với task list, checklist, test plan, evidence và checkpoint.
- [ ] Dependency, environment, owner và reviewer rõ.
- [ ] Change control xử lý mọi thay đổi đã biết.

#### Phase Definition of Done

- [ ] Scope đã hoàn tất hoặc residual/blocker được ghi.
- [ ] Mọi task có output, verification và status đúng bằng chứng.
- [ ] Test/evidence/checkpoint sections trong `task.md` đã cập nhật.
- [ ] Phase report và traceability đã cập nhật.
- [ ] Không còn gate/quality failure chưa được xử lý hoặc ghi nhận.
- [ ] Phase chưa tự chuyển `ACCEPTED`.

## 6. Dependency, sequencing và critical path

| Dependency ID | From | To | Type | Owner | Required by | Status | Mitigation if late |
|---|---|---|---|---|---|---|---|
| DEP-XXX | | | Product/technical/access/data | | | OPEN | |

- Critical path:
- Parallelizable phases/tasks:
- External decision dates:
- Environment/access lead time:
- Backward compatibility/migration order:

## 7. Risk, assumption và decision register

| ID | Type | Statement/impact | Probability | Impact | Owner | Mitigation/response | Trigger/review date | Status |
|---|---|---|---|---|---|---|---|---|
| RISK-XXX | Risk | | | | | | | OPEN |
| ASM-XXX | Assumption | | | | | | | OPEN |
| DEC-XXX | Decision needed | | | | | | | OPEN |

Không đóng risk/assumption chỉ bằng cách đổi wording; cần evidence, decision hoặc điều kiện đóng.

## 8. Capacity, timeline và release slices

| Slice/release | M/Phase | Outcome | Required capacity | Dependency | Target date/window | Go/no-go criteria | Status |
|---|---|---|---|---|---|---|---|
| <SLICE-XXX> | | | | | | | DRAFT |

- Capacity assumption:
- Resource/skill constraint:
- Cost limit:
- Calendar/blackout:
- Release/rollback rule:

## 9. Traceability and artifact plan

| M/Phase | Requirements | `task.md` | Phase report | Milestone report | Residual/debt | Acceptance owner |
|---|---|---|---|---|---|---|
| <M-ID>-<P-ID> | `requirements.md` | Task/test/evidence/checkpoint | `report.md` | | | |

`task.md` là artifact hợp nhất cho việc cần làm, test plan, verification evidence và checkpoint. Không tạo ba template/file độc lập cho cùng nội dung.

## 10. ROADMAP change control

Thay đổi phải ghi:

- Change ID và source:
- Current scope/baseline:
- Proposed change:
- Reason/options:
- Impact M/Phase/order/dependency/timeline/cost:
- Impact SRS/acceptance/Architecture/environment:
- Impact task/test/evidence/report:
- Risk of doing/not doing:
- Decision/owner/date:
- New version/effective date:

Chỉ cập nhật ROADMAP source sau khi scope/architecture change được chấp thuận theo `docs/00-governance/change-control.md`. Editorial clarification không đổi meaning có thể ghi changelog/diff mà không tạo scope change.

## 11. ROADMAP review checklist

- [ ] Vision/outcome và success measures còn đúng.
- [ ] Mỗi M có outcome, priority, owner, scope, dependency và exit criteria.
- [ ] Mỗi Phase có independent outcome, entry/exit criteria và task.md plan.
- [ ] Không có orphan requirement hoặc Phase không có source.
- [ ] Critical path, risk, assumption, decision và capacity đã review.
- [ ] Timeline/release slice phù hợp dependency và capacity.
- [ ] SRS, Architecture, registry, task/report guidance links còn đúng.
- [ ] Scope changes có CR/Decision và version/date.
- [ ] Status không bị nâng chỉ vì template/file đã tạo.

ROADMAP không phải progress report. Progress/verification nằm trong task.md, evidence và report của project; acceptance nằm trong acceptance policy và quyết định của người/role.
