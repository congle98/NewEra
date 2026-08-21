---
inclusion: always
---

# NewEra Quality Steering

Runtime rule: dùng `docs/03-requirements/acceptance-policy.md` cho gate và `docs/00-governance/status-model.md` cho status.

- Chạy test/build/lint/typecheck/security/operational checks phù hợp.
- Ghi expected, actual, environment, commit và limitation trong `task.md`.
- Lỗi phải sửa, ghi nhận hoặc chuyển residual/blocker; không tự tạo acceptance.
