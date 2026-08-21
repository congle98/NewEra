---
name: newera-roadmap
description: Tạo và duy trì ROADMAP, M, Phase, dependency, scope, milestone brief/report và change-control traceability. Dùng khi lập kế hoạch, sắp xếp thứ tự hoặc thay đổi phạm vi triển khai của adopter project.
metadata:
  newera_layer: workflow
  newera_version: "0.2"
---

# NewEra Roadmap

## Use when

Dùng khi tạo hoặc cập nhật ROADMAP, milestone, Phase, dependency order, scope boundary, exit condition hoặc residual work của project adopter.

## Preconditions

- Process preflight đã xác định task/Phase/CR binding.
- Có intake/charter hoặc baseline đủ để lập kế hoạch.
- Có requirement, dependency, owner và verification intent ở mức cần thiết.

## Procedure

1. Đọc `AGENTS.md`, document registry, roadmap template và canonical status model.
2. Xác nhận `docs/02-roadmap/roadmap.md` của project là source of truth cho M, Phase, scope và order.
3. Tách milestone outcome khỏi implementation detail; gán IDs cho M, Phase, task, dependency, risk, exit và residual.
4. Ghi dependency, owner/role, entry/exit condition, scope boundary và expected evidence.
5. Tạo/update milestone brief; liên kết M test capability profile và environment readiness gate trước mutation.
6. Nếu thay đổi scope/design/order đã được phê duyệt, ghi change control/decision trước khi cập nhật baseline.
7. Kiểm tra traceability và handoff sang phase execution; milestone report chỉ tổng hợp kết quả, không sở hữu scope.

## Outputs

- ROADMAP update có IDs, order, dependency và scope.
- Milestone brief với readiness/test profile.
- Change-control/decision reference nếu có.
- Handoff hoặc residual/debt list.

## Stop conditions

Dừng khi thiếu baseline, owner, dependency hoặc exit condition; không tự mở rộng scope, đổi status acceptance hoặc tạo roadmap/M/Phase artifact cho NewEra kernel.

## Canonical references

- `AGENTS.md`
- `docs/02-roadmap/roadmap.md`
- `docs/templates/milestone-brief.md`
- `docs/templates/milestone-report.md`
- `docs/00-governance/change-control.md`
- `docs/00-governance/status-model.md`
