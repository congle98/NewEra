# NewEra v0.1

NewEra là baseline quy trình phát triển phần mềm tự động hóa cho Kiro. Nó không khóa công nghệ; mỗi dự án có thể bật hoặc bỏ các tài liệu kỹ thuật theo `docs/00-governance/document-registry.md`.

## Bắt đầu

Đọc `AGENTS.md` và `GUIDE.md` trước; GUIDE giải thích cách vận hành, còn AGENTS là luật bắt buộc.

Đường ngắn nhất để bắt đầu một dự án:

```text
/newera-intake
```

Sau đó theo trình tự:

1. Đọc `AGENTS.md`, `status-model.md`, `git-policy.md` và registry.
2. Điền `docs/01-discovery/project-intake.md`.
3. Hoàn thiện `docs/02-roadmap/roadmap.md` và `milestone-index.md`.
4. Hoàn thiện SRS, acceptance policy, traceability và Architecture.
5. Kiểm tra `environment-manifest.md`/`setup-report.md`.
6. Chọn M đã `READY`, tạo brief và dùng template trong `docs/templates/`.
7. Chạy verification trước khi chuyển Phase sang `CHECKPOINT_PENDING`.
8. Chờ người/role nghiệm thu; không tự chuyển sang `ACCEPTED`.

## Nguyên tắc trạng thái

`VERIFIED` chỉ có nghĩa là đã kiểm chứng theo tiêu chí kỹ thuật. `CHECKPOINT_PENDING` là đang chờ xem xét và chưa hoàn thành. Chỉ `ACCEPTED` mới là nghiệm thu. `PARTIAL`, `BLOCKED`, `DEFERRED` và `NOT_APPLICABLE` phải đi kèm phạm vi/lý do phù hợp.

## Cấu trúc chính

- `AGENTS.md`: hiến pháp dự án.
- `GUIDE.md`: quy trình vận hành và thư viện prompt.
- `.kiro/`: steering, agents, skills và hooks.
- `docs/`: governance, discovery, planning, requirements, architecture, environment, execution, evidence, reports, operations, templates và prompts.
- `src/`, `tests/`, `scripts/`: vùng triển khai tùy project; không tồn tại trong kernel baseline hiện tại.

## Phạm vi hiện tại

Repository này là process kernel v0.1. ROADMAP hiện vẫn để M01/P01 ở `DRAFT` vì chưa có intake/product scope cụ thể. Không coi placeholder là cam kết sản phẩm; xem residual work để biết các bước dogfood tiếp theo.

## Phiên bản

NewEra v0.1 là kernel ban đầu, ưu tiên tính dễ hiểu, truy nguyên, trung thực về trạng thái và khả năng mở rộng mà không khóa công nghệ.
