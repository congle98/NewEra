# NewEra v0.2

NewEra là baseline quy trình phát triển phần mềm tự động hóa cho Kiro. Nó không khóa công nghệ; mỗi dự án có thể bật hoặc bỏ các tài liệu kỹ thuật theo `document-registry.md`.

Repository này là **process/documentation kernel**, không phải một project sản phẩm đang chạy NewEra. M/Phase, evidence, report, residual và machine state chỉ được tạo trong workspace của project sử dụng kernel.

## Bắt đầu

Đọc `GUIDE.md` trước; đó là hướng dẫn vận hành đầy đủ kèm thư viện prompt.

Đường ngắn nhất để bắt đầu một dự án:

```text
/newera-intake
```

Sau đó theo trình tự:

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
- `GUIDE.md`: quy trình vận hành và thư viện prompt.
- `.kiro/`: Steering, agents, skills và hooks.
- `docs/`: governance, discovery, planning, requirements, architecture, environment, templates, prompts và guidance.
- `docs/06-execution/`, `docs/07-evidence/`, `docs/08-reports/`: chỉ chứa index/guidance trong kernel; project sử dụng kernel tạo artifact cụ thể ở workspace riêng.
- `src/`, `tests/`, `scripts/`: không thuộc kernel baseline; chỉ xuất hiện khi project adopter cần triển khai hoặc tích hợp adapter.

## Phiên bản

NewEra v0.2 là kernel tài liệu quy trình và documentation, ưu tiên tính dễ hiểu và có thể mở rộng.