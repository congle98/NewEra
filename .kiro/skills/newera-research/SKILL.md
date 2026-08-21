---
name: newera-research
description: Điều tra câu hỏi chưa rõ bằng nguồn đáng tin, ghi fact/assumption/recommendation, confidence và limitation, rồi handoff impact vào requirements, roadmap hoặc CR/DEC/ADR. Dùng khi cần quyết định có căn cứ trước khi mở rộng scope hoặc design.
metadata:
  newera_layer: workflow
---

# NewEra Research

## Use when

Dùng khi có unknown ảnh hưởng requirement, architecture, roadmap, environment, test capability, risk hoặc decision.

## Procedure

1. Đọc `AGENTS.md`, research rules và `docs/templates/research-item.md`.
2. Gán `RES-*` cho câu hỏi; ghi method, source, version/date, relevance và limitation trước khi kết luận.
3. Ưu tiên nguồn chính thức, specification, repository/source primary và evidence có thể kiểm tra; ghi nguồn cộng đồng như tham khảo, không coi là authority mặc định.
4. Tách rõ `Fact`, `Assumption`, `Recommendation`, `Trade-off`, `Confidence` và `Limitation`.
5. Phân tích impact lên scope, requirement, design, security, environment, testing và operations.
6. Nếu có impact cần quyết định, tạo handoff tới CR/DEC/ADR; không tự cập nhật baseline chỉ từ recommendation.
7. Cập nhật research index và liên kết traceability khi project adopter có artifact tương ứng.

## Outputs and evidence

- Research item có ID, câu hỏi, nguồn, method và ngày.
- Kết luận phân lớp fact/assumption/recommendation.
- Confidence, limitation, trade-off và impact.
- Handoff tới requirement/ROADMAP/CR/DEC/ADR hoặc ghi `OPEN`.

## Stop conditions

Dừng kết luận khi nguồn không đủ, nguồn mâu thuẫn chưa được xử lý hoặc cần human/product decision. Không trình bày recommendation như fact và không tự mở rộng scope.

## Canonical references

- `AGENTS.md`
- `docs/01-discovery/research.md`
- `docs/templates/research-item.md`
- `docs/00-governance/change-control.md`
- `docs/00-governance/document-registry.md`
