---
name: newera-verification
description: Chạy kiểm chứng kỹ thuật cho Phase hoặc M theo capability profile, environment readiness, test plan và acceptance criteria; ghi evidence/traceability/checkpoint mà không biến technical result thành acceptance. Dùng khi verify, test hoặc review evidence.
metadata:
  newera_layer: workflow
---

# NewEra Verification

## Preconditions

- Có requirement/acceptance criteria IDs và test plan trong `task.md`.
- M test capability profile đã nêu lớp áp dụng và lý do loại trừ.
- Environment readiness reference và gate phù hợp; capability thiếu phải ghi `BLOCKED`.
- Có commit/worktree reference để tái hiện phạm vi kiểm chứng.

## Procedure

1. Đọc `AGENTS.md`, requirements, task/test matrix, environment report và acceptance policy.
2. Chọn lớp check theo requirement/risk: static/quality, unit/component, integration, API/contract, UI/client journey, accessibility/usability, visual, performance/load, security/operations hoặc human review khi áp dụng.
3. Dùng adapter/tool của project adopter; ghi version/configuration, không hardcode framework/tool vào kernel.
4. Chạy check theo dependency và capability; không gọi interactive exploration là regression evidence nếu chưa có cách lặp lại.
5. Ghi evidence: `TEST-*`, requirement/criteria, command/kịch bản, expected, actual, result, environment, timestamp, artifact, commit và limitation.
6. Kết luận từng check bằng `PASS`/`FAIL`/`NOT_RUN`/`NOT_APPLICABLE`; kết luận verification bằng `VERIFIED`, `PARTIAL`, `FAILED` hoặc `BLOCKED` theo status model.
7. Sửa hoặc ghi nhận lỗi thành residual/blocker; cập nhật `task.md`, checkpoint và report.
8. Handoff acceptance cho người/role có thẩm quyền; không tự chuyển `CHECKPOINT_PENDING` thành `ACCEPTED`.

## Outputs

- Evidence có traceability và reproducibility.
- Verification result đúng phạm vi.
- Checkpoint/report update.
- Residual/blocker IDs và limitation.
- Acceptance handoff chưa quyết định.

## Stop conditions

Dừng kết luận `VERIFIED` khi environment chưa đủ, test plan/criteria thiếu, check fail chưa được xử lý hoặc evidence không tái hiện được trong phạm vi yêu cầu.

## Canonical references

- `AGENTS.md`
- `docs/00-governance/status-model.md`
- `docs/03-requirements/acceptance-policy.md`
- `docs/00-governance/automation-contract.md`
- `docs/07-evidence/README.md`
- `docs/templates/task.md`
- `docs/templates/phase-report.md`
