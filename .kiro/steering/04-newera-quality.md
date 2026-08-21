---
inclusion: always
---

# NewEra Quality Steering

Runtime rule: dùng `docs/03-requirements/acceptance-policy.md` cho gate, `docs/00-governance/status-model.md` cho status và `docs/00-governance/automation-contract.md` cho canonical capability vocabulary. Trước mỗi M/Phase, dùng M test capability profile và environment readiness gate; không gán cứng framework/tool vào mọi project.

- Chọn capability verification theo requirement, risk và acceptance criteria; dùng vocabulary canonical trong `docs/00-governance/automation-contract.md`, gồm technical checks, product criteria review và human review khi áp dụng.
- Dùng adapter/tool do project adopter chọn; ghi version/config, environment, expected, actual, command/kịch bản và limitation.
- Với M/Phase có UI/client boundary, kiểm tra user journey thực tế bằng capability phù hợp; không chỉ kiểm tra function phía dưới.
- Với integration boundary, ưu tiên dependency thật hoặc môi trường tương đương có thể tái tạo; ghi rõ mock/emulator limitation nếu dùng.
- Thu thập evidence phù hợp: test report, log, trace, screenshot, video, network, metric, accessibility hoặc artifact tương đương.
- Chạy test/build/lint/typecheck/security/operational checks phù hợp; kết quả `PARTIAL` không được trình bày như verification đầy đủ.
- Lỗi phải sửa, ghi nhận hoặc chuyển residual/blocker; không tự tạo acceptance.
- Human review vẫn cần cho product judgment, usability ngoài phạm vi automated checks, visual intent, accessibility manual assessment và acceptance.
