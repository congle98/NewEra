---
name: newera-phase-execution
description: Lập kế hoạch và triển khai một Phase từ requirements đến task, implementation, capability-based verification, evidence, checkpoint và report. Dùng khi thực hiện Phase/M bình thường của adopter project; không dùng cho micro-change.
metadata:
  newera_layer: workflow
---

# NewEra Phase Execution

## Preconditions

- Route là `NORMAL_OR_SCOPE_CHANGE` và có ROADMAP/M/Phase/task binding.
- Requirements, Architecture/design boundary, dependency và owner đã đủ rõ.
- M test capability profile và environment readiness pack đã được chuẩn bị; gate phải là `ALLOW` trước mutation M/Phase.

## Procedure

1. Đọc `AGENTS.md`, ROADMAP, SRS/requirements, Architecture, registry, status/acceptance policy và environment manifest.
2. Xác nhận scope, dependency, entry/exit condition, risk và change-control reference.
3. Tạo/update Phase requirements và `task.md`; tách task, test, evidence, checkpoint, residual/debt bằng IDs.
4. Chọn capability verification theo requirement/risk; không gán framework hoặc tool cố định trong kernel.
5. Chạy environment readiness; nếu `BLOCKED`, dừng mutation và ghi blocker/next action.
6. Thực hiện task theo dependency bằng builder hoặc workflow phù hợp; cập nhật source artifact trước projection/report khi contract thay đổi.
7. Chạy verification, ghi expected/actual, environment, command/kịch bản, artifact, limitation và commit reference.
8. Cập nhật checkpoint, phase report, residual/debt và traceability; `VERIFIED` không tự thành `ACCEPTED`.
9. Chỉ tạo commit khi scope, validation và worktree reference đủ rõ theo git policy.

## Outputs

- Requirements và `task.md` có test plan/evidence/checkpoint.
- Implementation/test artifacts của adopter project.
- Environment readiness reference.
- Verification evidence và checkpoint.
- Phase report, residual/debt và commit reference.
- Acceptance handoff, không tự acceptance.

## Stop conditions

Dừng khi thiếu requirement/task binding, environment gate `BLOCKED`, dependency/permission chưa sẵn sàng, scope thay đổi không có CR/decision, hoặc evidence không đủ để kết luận verification.

## Canonical references

- `AGENTS.md`
- `docs/02-roadmap/roadmap.md`
- `docs/00-governance/automation-contract.md`
- `docs/00-governance/status-model.md`
- `docs/03-requirements/acceptance-policy.md`
- `docs/05-environment/environment-manifest.md`
- `docs/templates/task.md`
- `docs/templates/phase-report.md`
