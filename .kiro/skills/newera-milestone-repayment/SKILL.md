---
name: newera-milestone-repayment
description: Lập kế hoạch M.x để hoàn thiện outcome, sửa lỗi, trả residual/debt của một milestone đã làm; phân biệt repayment với feature mới và route change control khi scope mở rộng.
metadata:
  newera_layer: workflow
---

# NewEra Milestone Repayment

## Use when

Dùng sau milestone report khi còn residual, technical debt, blocker hoặc outcome chưa đạt cần một vòng M.x.

## Required inputs

- Milestone report and acceptance/checkpoint status.
- Residual/debt/blocker records with owner and close condition.
- ROADMAP scope, dependencies, environment and decision history.

## Procedure

1. Đọc ROADMAP, milestone report, residual/debt ledger, acceptance decision và open blockers.
2. Phân loại từng item: thiếu outcome cũ, defect/regression, debt cần trả, hay feature/new outcome.
3. Gán residual/debt/blocker IDs, owner, severity, close condition và evidence need.
4. Đưa chỉ các item phục hồi outcome cũ vào M.x; feature/new scope phải tạo CR và cập nhật ROADMAP sau decision.
5. Tạo M.x brief với scope, dependency, environment readiness, capability profile, exit criteria và acceptance boundary.
6. Handoff sang phase execution hoặc change control; không dùng M.x để lén mở rộng sản phẩm.

## Outputs

- M.x scope/brief có traceability.
- Residual/debt disposition và owner.
- CR/decision handoff nếu item là feature mới.
- Verification and acceptance handoff conditions.

## Stop conditions

Dừng khi không phân biệt được residual với feature mới, thiếu close condition/owner, hoặc acceptance decision/ROADMAP chưa đủ để lập vòng repayment.

## Handoff

- Repayment scope → roadmap/phase execution.
- New feature or outcome → change control.
- Verification/acceptance gap → verifier and acceptance-handoff.

## Canonical references

- `AGENTS.md`
- `docs/02-roadmap/roadmap.md`
- `docs/templates/residual-work.md`
- `docs/templates/milestone-brief.md`
- `docs/00-governance/change-control.md`
- `docs/00-governance/status-model.md`
