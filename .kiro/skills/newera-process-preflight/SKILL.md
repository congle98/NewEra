---
name: newera-process-preflight
description: Phân loại mọi request trước mutation thành READ_ONLY, MICRO_CHANGE hoặc NORMAL_OR_SCOPE_CHANGE; kiểm tra binding, scope, verification plan và gate ALLOW/BLOCKED. Dùng khi bắt đầu task, thay đổi tài liệu, code, cấu hình hoặc workflow NewEra.
metadata:
  newera_layer: workflow
---

# NewEra Process Preflight

## Purpose

Xác định route và điều kiện tối thiểu trước khi agent đọc sâu, dispatch hoặc mutation. Skill này hỗ trợ workflow; luật bắt buộc vẫn nằm trong `AGENTS.md` và `docs/00-governance/automation-contract.md`.

## Use when

- Một request có thể sửa artifact, code, test, cấu hình hoặc `.kiro`.
- Cần quyết định một thay đổi là micro-change hay task/Phase bình thường.
- Thiếu thông tin về repository, task binding, scope hoặc verification.

## Required inputs

- User request và expected outcome.
- Project/repository boundary.
- M/Phase/task/request binding nếu có.
- Planned paths hoặc artifact boundary.
- Verification plan và gate cần áp dụng.

## Procedure

1. Đọc `AGENTS.md`, automation contract, roadmap/status/acceptance policy liên quan.
2. Xác định request type: đọc/giải thích, research chưa sửa, hay mutation.
3. Chọn đúng một route:
   - `READ_ONLY`: không sửa artifact.
   - `MICRO_CHANGE`: thay đổi cục bộ, không đổi requirement, acceptance, API, data, security, deployment hoặc architecture.
   - `NORMAL_OR_SCOPE_CHANGE`: task Phase/M, thay đổi design/scope, hoặc bất kỳ thay đổi nào không thỏa điều kiện micro-change.
4. Ghi preflight tối thiểu: request type, repository, binding, route, planned paths, expected output, verification plan, gate và blocker/next action.
5. Với `MICRO_CHANGE`, kiểm tra task/request binding, path boundary và targeted verification trước mutation.
6. Với `NORMAL_OR_SCOPE_CHANGE`, đọc ROADMAP, requirement/task, Architecture và environment manifest; nếu ngoài scope thì handoff CR/DEC/ADR trước mutation.
7. Nếu thiếu dữ liệu quan trọng, dừng với `OPEN` hoặc `BLOCKED`; không tự điền giả định như sự thật.

## Outputs and evidence

Kết quả phải có route, boundary, expected result, verification plan và `ALLOW` hoặc `BLOCKED`. Nếu project có `task.md`, ghi preflight vào đó; không tạo request state hoặc `.newera/` chỉ cho NewEra kernel.

## Stop conditions

Dừng mutation khi thiếu repository/binding/scope, có conflict với canonical source, environment gate bị `BLOCKED`, hoặc phát hiện requirement/acceptance/API/data/security/deployment/architecture change trong một route micro.

## Handoff

- `READ_ONLY` → trả lời hoặc research handoff.
- `MICRO_CHANGE` → builder theo `newera-micro-change`.
- `NORMAL_OR_SCOPE_CHANGE` → orchestrator/roadmap/phase workflow.
- Scope/design impact → change control và decision authority.

## Canonical references

- `AGENTS.md`
- `docs/00-governance/automation-contract.md`
- `docs/02-roadmap/roadmap.md`
- `docs/00-governance/status-model.md`
- `docs/03-requirements/acceptance-policy.md`
