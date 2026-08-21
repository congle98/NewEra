# Milestone Index

Milestone index là bảng điều hướng của ROADMAP, không thay thế milestone brief/report. Mỗi dòng phải trỏ về outcome, owner, readiness và artifact thực tế.

| M ID | Tên/outcome | ROADMAP section | Brief | Phase order | Requirements | Report | Owner | Dependency/readiness gap | Next action/due | Verification | Checkpoint | Acceptance | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <M-ID> | Chưa xác định | roadmap.md#<section> | Chưa tạo | <P-ID> → <P-ID> | SRS/requirements | Chưa tạo | | | | NOT_RUN | INCOMPLETE | NOT_ACCEPTED | DRAFT |

## Quy tắc cập nhật

- Mỗi `<M-ID>` phải tồn tại trong `docs/02-roadmap/roadmap.md` và có outcome/priority/owner.
- `Phase order` phải phản ánh dependency thực tế; không dùng index để đổi thứ tự mà không cập nhật ROADMAP.
- `Readiness gap` ghi rõ tài liệu, dependency, quyết định, quyền hoặc acceptance criteria còn thiếu.
- `Next action/due` phải có owner; item `BLOCKED` phải nêu blocker và escalation path.
- Link brief/report/requirements/task.md phải thuộc project adopter; kernel không tự tạo artifact M/Phase của chính nó.
- Verification, checkpoint và acceptance là ba cột độc lập; không suy ra `ACCEPTED` từ `VERIFIED`.
- Khi M đóng, cập nhật report, residual/debt và quyết định có cần `<M-ID>.1` hay không.

## Quy tắc ID

- `<M-ID>`: milestone mới, ổn định sau khi phát hành.
- `<M-ID>.1`, `<M-ID>.2`: vòng bồi hoàn/hoàn thiện cho cùng outcome cũ; không dùng cho feature mới.
- `<M-ID>-<P-ID>`: Phase thuộc milestone.
- `TASK-<M-ID>-<P-ID>-001`: task truy nguyên được trong `task.md`.
- `REQ-<M-ID>-<P-ID>-001`, `TEST-<M-ID>-<P-ID>-001`, `EVD-<M-ID>-<P-ID>`, `CHK-<M-ID>-<P-ID>`: IDs liên kết của Phase.
- Placeholder phải được thay bằng ID thật trước khi artifact chuyển `READY`.
