# NewEra v0.1

NewEra là baseline quy trình phát triển phần mềm tự động hóa cho Kiro. Nó không khóa công nghệ; mỗi dự án có thể bật hoặc bỏ các tài liệu kỹ thuật theo `document-registry.md`.

## Bắt đầu

1. Đọc `AGENTS.md`.
2. Điền `docs/01-discovery/project-intake.md`.
3. Hoàn thiện `docs/02-roadmap/roadmap.md`.
4. Hoàn thiện SRS và Architecture.
5. Chọn M đầu tiên và dùng template trong `docs/templates/`.
6. Chạy verification trước khi chuyển Phase sang `CHECKPOINT_PENDING`.

## Nguyên tắc trạng thái

`VERIFIED` chỉ có nghĩa là đã kiểm chứng theo tiêu chí kỹ thuật. `CHECKPOINT_PENDING` là đang chờ xem xét và chưa hoàn thành. Chỉ `ACCEPTED` mới là nghiệm thu.

## Cấu trúc chính

- `AGENTS.md`: hiến pháp dự án.
- `.kiro/`: Steering, agents, skills và hooks.
- `docs/`: tài liệu, kế hoạch, evidence và report.
- `src/`, `tests/`, `scripts/`: vùng triển khai dự án.

## Phiên bản

NewEra v0.1 là kernel ban đầu, ưu tiên tính dễ hiểu và có thể mở rộng.