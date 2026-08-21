---
name: newera-resume-work
description: Khôi phục workflow NewEra sau khi bị gián đoạn bằng git history, ROADMAP, task, checkpoint, evidence, report và blocker; không tự đoán trạng thái hoặc tiếp tục mutation khi thiếu context.
metadata:
  newera_layer: workflow
---

# NewEra Resume Work

## Use when

Dùng khi session/work bị ngắt, agent mất context, worktree có thay đổi chưa hiểu hoặc cần xác định next action từ artifact hiện có.

## Required inputs

- Current repository/worktree and git history.
- ROADMAP, registry, current task, evidence, checkpoint, report and residual.
- Last known owner, route, environment gate and decision references.

## Procedure

1. Chạy process preflight ở route `READ_ONLY` trước khi dựng snapshot.
2. Đọc `AGENTS.md`, git status/log/diff, ROADMAP, registry, current requirements, task, evidence, checkpoint, report và residual.
3. Lập snapshot: current scope, completed outputs, verification status, open blocker, pending decision, worktree/commit và next action.
4. Phân biệt fact với assumption; không chuyển `DRAFT`, `OPEN`, `BLOCKED`, `PARTIAL` hoặc `CHECKPOINT_PENDING` thành hoàn tất.
5. Nếu cần mutation, chạy lại preflight và xác nhận binding/path/environment/verification plan trước.
6. Handoff tới builder, verifier, report manager hoặc decision authority theo next action.

## Outputs

- Resume snapshot có timestamp, source artifacts và commit/worktree.
- Next action có owner, dependency và gate.
- Blocker/open question nếu không đủ dữ liệu.

## Stop conditions

Dừng khi status mâu thuẫn, diff không rõ ownership, thiếu task/binding, environment đã thay đổi hoặc có decision chưa ghi.

## Handoff

- Safe next mutation → process preflight then builder.
- Verification gap → verifier.
- Report/status gap → report manager.
- Scope/decision gap → orchestrator or decision authority.

## Canonical references

- `AGENTS.md`
- `docs/prompts/README.md`
- `docs/00-governance/status-model.md`
- `docs/00-governance/automation-contract.md`
- `docs/templates/task.md`
