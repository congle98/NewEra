---
name: newera-reporting
description: Tổng hợp Phase/M report, evidence, checkpoint, residual work, technical debt, limitation và changelog có traceability. Dùng khi kết thúc task/Phase/M hoặc chuẩn bị handoff review; không tự đổi scope hay acceptance.
metadata:
  newera_layer: workflow
---

# NewEra Reporting

## Preconditions

- Có task/Phase/M binding và document registry.
- Có requirements, task/test plan, evidence, checkpoint, commit/worktree reference và report inputs.
- Status và acceptance vocabulary lấy từ canonical policy, không tự tạo literal mới.

## Procedure

1. Đọc `AGENTS.md`, registry, task, requirements, evidence, checkpoint, report cũ, residual/debt và commit history.
2. Kiểm tra traceability từ requirement → task → test → evidence → checkpoint → report.
3. Tóm tắt scope đã làm, verification status, environment/capability limitation, blocker, risk, residual và technical debt.
4. Đối chiếu ROADMAP và change-control/decision; ghi divergence thay vì âm thầm sửa scope.
5. Cập nhật phase/milestone report và changelog đúng ownership; giữ lịch sử, không xóa evidence hoặc decision.
6. Kiểm tra điều kiện `CHECKPOINT_PENDING`; acceptance chỉ là handoff nếu chưa có quyết định của role có thẩm quyền.
7. Ghi next action, owner và điều kiện reopen cho residual/deferred work.

## Outputs

- Phase/M report có traceability, status, limitation và evidence references.
- Residual/debt/blocker list có IDs, owner và next action.
- Changelog/decision handoff nếu thuộc scope.
- Acceptance handoff với `PENDING` khi chưa có quyết định.

## Stop conditions

Dừng kết luận khi thiếu evidence, checkpoint, report input, status reference hoặc commit/worktree scope. Không tự xóa lịch sử, đổi ROADMAP, đánh dấu `ACCEPTED` hoặc biến `PARTIAL` thành `VERIFIED`.

## Canonical references

- `AGENTS.md`
- `docs/00-governance/document-registry.md`
- `docs/00-governance/status-model.md`
- `docs/03-requirements/acceptance-policy.md`
- `docs/templates/phase-report.md`
- `docs/templates/milestone-report.md`
- `docs/07-evidence/README.md`
