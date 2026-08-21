# <M-ID> - Milestone Brief

## Document control

- M:
- Tên/outcome sản phẩm:
- Owner/sponsor/reviewer:
- ROADMAP reference/version:
- Ngày lập/cập nhật:
- Trạng thái: DRAFT | READY | IN_PROGRESS | BLOCKED | CLOSED
- Related SRS/Architecture/decision/CR:

## Mục tiêu và outcome

- Problem/user outcome:
- Mục tiêu:
- Outcome quan sát/đo được:
- Baseline/target/threshold:
- Success criteria:
- Failure/stop criteria:
- Requirement/OBJ liên quan:

## Phạm vi và boundary

### In scope

-

### Ngoài phạm vi

-

### Acceptance boundary

- Release slice:
- Included Phase:
- Known exclusions/residual policy:
- Acceptance owner:

## Phase và thứ tự

| Phase | Mục tiêu độc lập | Requirements | Dependency | Entry/exit criteria | Owner | Status |
|---|---|---|---|---|---|---|
| <M-ID>-<P-ID> | | | | | | DRAFT |

## M readiness and test capability profile

M phải xác định capability môi trường và lớp kiểm chứng trước khi chuyển `READY`. Không gán cứng tool/framework; project adopter điền adapter/tool đã chọn trong environment manifest.

| Capability/test layer | Applies | M/Phase | Expected evidence | Selected adapter/tool | Owner |
|---|---:|---|---|---|---|
| Static/quality | Yes/No | | | | |
| Unit/component | Yes/No | | | | |
| Integration/real dependency | Yes/No | | | | |
| API/contract | Yes/No | | | | |
| UI/client journey | Yes/No | | | | |
| Accessibility/usability | Yes/No | | | | |
| Visual behavior | Yes/No | | | | |
| Performance/load | Yes/No | | | | |
| Security/operations | Yes/No | | | | |

- Environment Manifest reference/version:
- Setup Report reference:
- Environment gate: ALLOW | BLOCKED
- Required human setup actions:
- Non-blocking limitations:
- Re-check triggers:

## Dependency, risk và capacity

| ID | Type | Description/impact | Owner | Mitigation/next action | Due | Status |
|---|---|---|---|---|---|---|
| DEP-<DEP-ID> | Dependency | | | | | OPEN |
| RISK-<RISK-ID> | Risk | | | | | OPEN |
| ASM-<ASM-ID> | Assumption | | | | | OPEN |

- Capacity/budget/window:
- Critical path:
- Access/environment prerequisite:

## Definition of Ready / Done

### DoR

- [ ] ROADMAP có outcome, scope, priority, acceptance boundary và order.
- [ ] SRS/requirements và acceptance criteria có ID.
- [ ] Dependency, owner, reviewer, environment và capacity rõ.
- [ ] Architecture/registry impact đã xác định.
- [ ] Risk/assumption/open question có owner và next action.
- [ ] Mỗi Phase có `requirements.md` và consolidated `task.md` plan.

### DoD

- [ ] Mọi Phase exit criteria đạt hoặc residual/blocker có ID và close condition.
- [ ] `task.md` của mỗi Phase chứa task, test plan, evidence và checkpoint đã cập nhật.
- [ ] Traceability, phase report, residual/debt và milestone report đồng bộ.
- [ ] Outcome được đối chiếu với success criteria.
- [ ] Verification limitation và acceptance decision được ghi rõ.
- [ ] Acceptance status và decision tuân thủ `docs/03-requirements/acceptance-policy.md`.

## Artifact/checklist plan

- [ ] ROADMAP §3 milestone index
- [ ] SRS / requirements / acceptance policy
- [ ] Architecture / registry / environment manifest / setup report
- [ ] M test capability profile and selected project adapters
- [ ] Human setup actions and environment gate
- [ ] Phase `task.md` (task + test + evidence + checkpoint)
- [ ] Phase report
- [ ] Residual work / technical debt
- [ ] Milestone report

## Kế hoạch báo cáo và handoff

- Phase report sau mỗi Phase:
- Milestone report:
- Quyết định cần người dùng:
- Residual/debt handoff:
- Đề xuất M.<n> nếu có:

M không được chuyển `READY` chỉ vì brief đã tạo; phải kiểm tra các gap và status trong ROADMAP.
