---
name: newera-change-control
description: Phân tích và điều phối thay đổi requirement, scope, API, data, security, deployment hoặc architecture qua CR/DEC/ADR trước mutation. Dùng khi request vượt MICRO_CHANGE hoặc khi design/scope impact chưa có quyết định.
metadata:
  newera_layer: workflow
---

# NewEra Change Control

## Use when

Dùng khi request làm thay đổi scope, requirement, acceptance, API, data, security, deployment, architecture, order hoặc commitment đã ghi trong ROADMAP.

## Preconditions

- Có project/repository và request/change binding.
- Có baseline source document và người/role có thể quyết định.
- Preflight đã route `NORMAL_OR_SCOPE_CHANGE` hoặc phát hiện micro-change không còn hợp lệ.

## Procedure

1. Đọc `AGENTS.md`, ROADMAP, source document, change-control policy và decision log.
2. Gán `CR-<CR-ID>`; mô tả current state, proposed change, reason, alternatives, impact, risk, cost, dependency và rollback.
3. Xác định affected requirement/acceptance/API/data/security/deployment/architecture IDs.
4. Tách fact, assumption và recommendation; không sửa baseline như thể change đã được duyệt.
5. Handoff CR tới decision authority; ghi `PROPOSED`, `BLOCKED` hoặc trạng thái canonical phù hợp.
6. Chỉ sau khi decision được ghi mới cập nhật ROADMAP, SRS, Architecture, task hoặc environment contract.
7. Ghi traceability, residual và migration/rollback condition.

## Outputs

- CR có impact analysis và decision owner.
- DEC/ADR reference khi cần.
- Approved/rejected/deferred scope update hoặc blocker.
- Handoff task/ROADMAP sau quyết định.

## Stop conditions

Không mutation khi chưa có decision cho scope/design impact, thiếu authority, thiếu impact analysis hoặc change đang bị `OPEN`/`BLOCKED`.

## Handoff

- Approved change → roadmap/requirements/architecture/task owner.
- Scope/design uncertainty → decision authority với `OPEN`/`BLOCKED`.
- Research needed → `newera-research`.

## Canonical references

- `AGENTS.md`
- `docs/00-governance/change-control.md`
- `docs/00-governance/decision-log.md`
- `docs/02-roadmap/roadmap.md`
- `docs/00-governance/status-model.md`
