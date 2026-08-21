---
name: newera-builder
description: Triển khai task, cập nhật code, test và tài liệu theo Phase NewEra.
---

# NewEra Builder

Trước mọi mutation, thực hiện process preflight theo `docs/00-governance/automation-contract.md` và báo route `READ_ONLY`, `MICRO_CHANGE` hoặc `NORMAL_OR_SCOPE_CHANGE`.

- `READ_ONLY`: không sửa artifact.
- `MICRO_CHANGE`: xác định project/repository, task/request binding, path boundary, không có requirement/acceptance/API/data/security/deployment/architecture change; sau đó sửa, chạy targeted check và ghi evidence ngắn.
- `NORMAL_OR_SCOPE_CHANGE`: đọc ROADMAP, SRS/requirements, Architecture, `task.md` và environment manifest; nếu ngoài scope thì xử lý CR/decision trước.

Không tự đoán khi thiếu binding hoặc scope; ghi `OPEN`/`BLOCKED` và next action. Chỉ triển khai trong scope; cập nhật test và artifact liên quan; ghi kết quả vào `task.md`; commit theo git policy khi đủ điều kiện.
