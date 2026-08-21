---
inclusion: always
---

# NewEra Core Steering

Runtime rule: đọc `AGENTS.md` trước mọi công việc và chạy process preflight trước bất kỳ mutation nào. Tham chiếu các canonical policy sau:

- Process entry/automation: `docs/00-governance/automation-contract.md`
- Scope/source: `docs/02-roadmap/roadmap.md`
- Status/transition: `docs/00-governance/status-model.md`
- Acceptance authority: `docs/03-requirements/acceptance-policy.md`
- End-of-task report: thay đổi, test, commit, evidence, blocker, residual và acceptance status.

Preflight phải chọn `READ_ONLY`, `MICRO_CHANGE` hoặc `NORMAL_OR_SCOPE_CHANGE`. Không sửa artifact khi project/repository, scope boundary, task/request binding hoặc verification plan còn thiếu; ghi `OPEN`/`BLOCKED` và next action thay vì tự đoán.
