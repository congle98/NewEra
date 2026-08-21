---
name: newera-micro-change
description: Thực hiện thay đổi cục bộ nhỏ theo route MICRO_CHANGE với request/task binding, path boundary, targeted verification và evidence ngắn. Dùng khi sửa tài liệu, code, test hoặc cấu hình mà không đổi requirement, acceptance, API, data, security, deployment hay architecture.
metadata:
  newera_layer: workflow
---

# NewEra Micro Change

## Purpose

Giảm ceremony cho thay đổi nhỏ nhưng không giảm traceability, scope check, verification hoặc evidence. Nếu điều kiện micro không còn đúng, chuyển ngay sang route bình thường.

## Preconditions

- Process preflight đã chọn `MICRO_CHANGE`.
- Có project/repository và task/request binding.
- Đã ghi path boundary, expected result và targeted verification.
- Environment không cần readiness mới; nếu có M/Phase environment impact thì dùng `newera-environment-readiness` và route bình thường.

## Procedure

1. Đọc `AGENTS.md` và policy canonical liên quan.
2. Xác nhận thay đổi không ảnh hưởng requirement, acceptance criteria, API, data model, security, deployment hoặc architecture.
3. Chốt danh sách path được phép sửa; không mở rộng sang artifact ngoài boundary.
4. Thực hiện mutation nhỏ nhất có thể.
5. Chạy targeted check phù hợp với artifact và risk; không tuyên bố verification rộng hơn phạm vi check.
6. Ghi task note/evidence ngắn: binding, paths, expected/actual, command hoặc kịch bản, environment nếu liên quan, timestamp, limitation và commit reference khi có.
7. Nếu phát sinh lỗi, scope hoặc design impact, ghi blocker/residual và chuyển `NORMAL_OR_SCOPE_CHANGE`.

## Outputs

- Request/task binding.
- Scope/path boundary.
- Changed artifact.
- Targeted verification result.
- Evidence ngắn và limitation.
- Handoff hoặc blocker nếu route không còn phù hợp.

## Stop conditions

Không tiếp tục nếu thiếu binding, path boundary hoặc verification plan; nếu phát hiện scope/design change; nếu check fail chưa được sửa, ghi nhận hoặc chuyển residual; hoặc nếu canonical source bị mâu thuẫn.

## Authority boundary

Micro-change không tự tạo acceptance, không bỏ qua environment gate khi M/Phase bị ảnh hưởng, không tạo full SRS/Architecture/Phase report chỉ vì thay đổi nhỏ và không thay đổi ROADMAP âm thầm.

## Canonical references

- `AGENTS.md`
- `docs/00-governance/automation-contract.md`
- `docs/00-governance/status-model.md`
- `docs/03-requirements/acceptance-policy.md`
