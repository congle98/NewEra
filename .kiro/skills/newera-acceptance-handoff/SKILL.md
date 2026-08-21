---
name: newera-acceptance-handoff
description: Chuẩn bị hồ sơ và handoff cho acceptance decision dựa trên requirements, verification, checkpoint, report và residual; không tự quyết định ACCEPTED. Dùng khi Phase/M đủ evidence hoặc cần người có thẩm quyền xem xét.
metadata:
  newera_layer: workflow
---

# NewEra Acceptance Handoff

## Purpose

Chuẩn bị decision packet có thể review được. Acceptance là human/authorized decision, không phải output tự động của test, report, hook hoặc agent.

## Preconditions

- Có M/Phase/requirement/acceptance criteria IDs.
- Verification evidence, checkpoint, report, residual/blocker và commit/worktree reference đã có.
- Environment/capability limitation đã ghi rõ.

## Procedure

1. Đọc acceptance policy, status model, requirements, task/evidence, checkpoint, report và ROADMAP.
2. Kiểm tra traceability requirement → task → test → evidence → checkpoint → report.
3. Xác nhận verification status, checkpoint status và acceptance status là ba lớp riêng.
4. Liệt kê criteria đạt/chưa đạt, limitation, residual, blocker, risk và ngoại lệ cần decision.
5. Tạo decision packet với artifact, criteria, status, evidence, người/role, ngày, lý do và điều kiện.
6. Giữ acceptance `PENDING` cho tới khi role có thẩm quyền ghi decision.
7. Sau decision, cập nhật decision log/report/ROADMAP theo ownership; không tự đổi scope hoặc xóa lịch sử.

## Outputs

- Acceptance handoff packet.
- Decision Log reference hoặc `OPEN`/`BLOCKED` next action.
- Status projection nhất quán sau human decision.

## Stop conditions

Dừng handoff khi thiếu criteria/evidence/checkpoint/authority hoặc có blocker ảnh hưởng acceptance mà chưa được ghi.

## Forbidden actions

Không tự ghi `ACCEPTED`, không suy ra acceptance từ `VERIFIED`, không dùng `CHECKPOINT_PENDING` làm accepted, không quyết định product judgment thay human/authorized role.

## Handoff

- Decision packet → designated human/authorized acceptance role.
- Missing evidence → verifier/builder.
- Scope or criteria gap → change control/roadmap owner.

## Canonical references

- `AGENTS.md`
- `docs/03-requirements/acceptance-policy.md`
- `docs/00-governance/status-model.md`
- `docs/templates/phase-report.md`
- `docs/templates/milestone-report.md`
