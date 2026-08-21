# MXX-PXX - Phase Requirements

- Phase ID:
- M / ROADMAP reference:
- SRS references:
- Owner/product owner:
- Technical owner:
- Stakeholders/reviewer:
- Version/date:
- Trạng thái: DRAFT

## 1. Phase context và outcome

- Vấn đề cần giải quyết:
- Outcome sản phẩm/kỹ thuật quan sát hoặc đo được:
- Baseline hiện tại:
- Target sau Phase:
- In scope:
- Ngoài phạm vi:
- Preconditions/dependency:
- Assumptions/open questions:

## 2. Requirement quality rules

Mỗi requirement phải:

- Có một ID ổn định và một outcome/hành vi nguyên tử.
- Có actor, trigger/input, behavior, output và điều kiện trước khi áp dụng.
- Có acceptance criteria đo/đối chiếu được, không dùng từ mơ hồ như “tốt”, “nhanh”, “đầy đủ” nếu không có ngưỡng.
- Có priority, source, dependency, risk và owner khi cần.
- Có task/test/evidence mapping hoặc lý do rõ nếu không áp dụng.
- Không trộn solution design vào requirement nếu chưa có Architecture/ADR.

## 3. Functional requirements

### REQ-MXX-PXX-001 - <Tên requirement>

- Tên ngắn:
- Mục tiêu/outcome:
- Actor/role:
- Trigger/input:
- Behavior/rules:
- Output/state change:
- Preconditions:
- Main flow:
- Alternate flow:
- Error/edge cases:
- Data/privacy/security constraints:
- Priority: MUST | SHOULD | COULD | WON'T
- Source: intake/charter/research/ROADMAP/decision/feedback
- Dependency:
- Risk/mitigation:
- Owner:
- Task IDs dự kiến:
- Test IDs dự kiến:
- Trạng thái: DRAFT

#### Acceptance criteria

| ID | Given/precondition | When/action | Then/expected result | Measurement/evidence | Status |
|---|---|---|---|---|---|
| AC-MXX-PXX-001 | | | | | NOT_RUN |
| AC-MXX-PXX-002 | | | | | NOT_RUN |

#### Requirement review checklist

- [ ] Requirement là atomic và không trùng với requirement khác.
- [ ] Actor, trigger, input, behavior, output và edge case đã rõ.
- [ ] Acceptance criteria có expected result và measurement.
- [ ] Priority và owner đã xác định.
- [ ] Dependency/assumption/risk đã được ghi.
- [ ] Có link tới ROADMAP/SRS/Architecture khi cần.
- [ ] Task/test/evidence mapping đã có hoặc ghi lý do `NOT_APPLICABLE`.
- [ ] Không mở rộng scope ngoài ROADMAP.

## 4. Non-functional and operational requirements

Mỗi NFR phải có metric, baseline, target, threshold, measurement method và environment.

| ID | Category | Requirement | Metric/baseline | Target/threshold | Measurement | Owner | Status |
|---|---|---|---|---|---|---|---|
| NFR-MXX-PXX-001 | Performance | | | | | | DRAFT |
| SEC-MXX-PXX-001 | Security/privacy | | | | | | DRAFT |
| OPS-MXX-PXX-001 | Operability | | | | | | DRAFT |
| DATA-MXX-PXX-001 | Data/integrity | | | | | | DRAFT |

Các category có thể gồm performance, availability, security, privacy, accessibility, compatibility, observability, operations, data integrity, cost và compliance.

## 5. Dependency, assumption và change boundary

- Dependency nội bộ:
- Dependency bên ngoài/service:
- Environment/tool prerequisite:
- Assumption ID và cách xác minh:
- Research/decision/ADR liên quan:
- Open question/owner/due date:
- Blocker/mitigation:
- Điều kiện mở rộng hoặc thu hẹp scope:

## 6. Traceability và tài liệu cần cập nhật

| Requirement | ROADMAP/M/Phase | Architecture/ADR | Task | Test | Evidence | Report | Status |
|---|---|---|---|---|---|---|---|
| REQ-MXX-PXX-001 | | | TASK- | TEST- | EVD- | RPT- | DRAFT |

- SRS/ROADMAP:
- Architecture/ADR:
- Environment/registry:
- `task.md` (task, test, evidence, checkpoint):
- Phase report/residual/debt:

## 7. Phase readiness checklist

- [ ] Phase tồn tại trong ROADMAP và dependency đã đạt hoặc có kế hoạch xử lý.
- [ ] Scope in/out và outcome có thể kiểm chứng.
- [ ] Requirement/acceptance criteria đã review.
- [ ] Architecture/environment đủ hoặc gap đã ghi OPEN/BLOCKED.
- [ ] Task có owner, dependency, output và checklist.
- [ ] `task.md` có test plan, evidence và checkpoint sections.
- [ ] Traceability map không có orphan requirement.
- [ ] Change control đã xử lý mọi scope/architecture change.

## 8. Phase completion checklist

- [ ] Mọi requirement trong scope có kết luận verification.
- [ ] Mọi task có status, output và evidence/checklist tương ứng.
- [ ] Test/evidence/checkpoint đã cập nhật trong `task.md`.
- [ ] Traceability và report đã đồng bộ.
- [ ] Residual/debt/blocker/risk có ID và owner/điều kiện đóng.
- [ ] Chỉ chuyển `CHECKPOINT_PENDING` khi đủ hồ sơ; không tự chuyển `ACCEPTED`.

Không thêm requirement mới trong lúc thực hiện mà không tạo CR và cập nhật ROADMAP/SRS nguồn trước.