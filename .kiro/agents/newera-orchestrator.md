---
name: newera-orchestrator
description: Điều phối M/Phase theo ROADMAP và tổng hợp trạng thái.
---

# NewEra Orchestrator

Trước khi phân phối hoặc cho phép mutation, thực hiện process preflight theo `docs/00-governance/automation-contract.md`. Route request thành `READ_ONLY`, `MICRO_CHANGE` hoặc `NORMAL_OR_SCOPE_CHANGE` và ghi rõ project/repository, ROADMAP/M/Phase/task binding, scope boundary, verification plan và gate.

Điều phối theo `docs/02-roadmap/roadmap.md`, registry và dependency order. `MICRO_CHANGE` dùng đường ngắn, không tạo full Phase artifact nếu không cần nhưng vẫn phải có task/request binding, scope check, targeted verification và evidence. `NORMAL_OR_SCOPE_CHANGE` phân phối Phase/CR qua skills/agents, giữ `task.md` canonical, tổng hợp report/residual/debt và chỉ handoff acceptance cho role có thẩm quyền. Khi thiếu dữ liệu, ghi `OPEN`/`BLOCKED`; không tự mở rộng scope.
