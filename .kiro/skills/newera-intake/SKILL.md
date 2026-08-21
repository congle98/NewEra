---
name: newera-intake
description: Thu thập request và context ban đầu, chuyển câu hỏi mở thành intake, charter, assumptions và research handoff có ID. Dùng khi bắt đầu project, tiếp nhận yêu cầu mới hoặc khi scope chưa đủ rõ để lập ROADMAP.
metadata:
  newera_layer: workflow
---

# NewEra Intake

## Use when

Dùng cho request mới, project mới, yêu cầu có nhiều câu hỏi mở hoặc khi chưa xác định được objective, stakeholder, constraint, scope và outcome.

## Required inputs

- User/stakeholder request và context hiện có.
- Repository/project boundary.
- Các tài liệu baseline đã tồn tại.
- Người/role có thể trả lời câu hỏi mở.

## Procedure

1. Đọc `AGENTS.md`, document registry và `docs/templates/intake-questions.md`.
2. Chạy process preflight; nếu chỉ đọc/phân tích thì giữ `READ_ONLY`, nếu ghi artifact adopter thì ghi binding và boundary.
3. Tách fact, assumption, unknown, decision cần người xác nhận và constraint.
4. Gán ID cho objective, question, stakeholder, assumption, risk và success/exit criteria.
5. Tạo hoặc cập nhật intake/charter/assumptions theo ownership của project adopter; không tạo artifact project-specific trong NewEra kernel.
6. Chuyển câu hỏi kỹ thuật hoặc domain chưa rõ sang `newera-research` với confidence, limitation và expected handoff.
7. Chỉ handoff sang roadmap khi scope, owner, dependency, outcome và điều kiện tiếp theo đủ rõ; nếu chưa, ghi `OPEN`/`BLOCKED`.

## Outputs and evidence

- Intake/charter có IDs và ownership.
- Assumptions, constraints, risks và open questions.
- Research items hoặc decision handoff.
- Next action và blocker/owner nếu chưa đủ dữ liệu.

## Stop conditions

Không tự đoán câu trả lời, không viết code trước khi scope đủ rõ, không chuyển assumption thành requirement và không tạo M/Phase của kernel khi chưa có adopter project scope.

## Canonical references

- `AGENTS.md`
- `docs/00-governance/document-registry.md`
- `docs/templates/intake-questions.md`
- `docs/01-discovery/research.md`
- `docs/00-governance/automation-contract.md`
