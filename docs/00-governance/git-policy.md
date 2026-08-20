# Git Policy

AI được tạo commit khi thay đổi logic đã đạt điều kiện kiểm tra phù hợp và có phạm vi rõ ràng. Commit phải phục vụ truy nguyên, không được dùng để che giấu trạng thái chưa hoàn thành.

## Format

```text
<type>(<scope>): <description>
```

Types: `feat`, `fix`, `test`, `docs`, `chore`, `refactor`, `verify`, `wip`.

## Commit points

- Bộ tài liệu nền.
- Một nhóm task logic.
- Một Phase đã verification.
- Evidence và phase report.
- Milestone report.

`wip` chỉ dùng để lưu trạng thái đang làm và không phải bằng chứng hoàn thành. Không commit secret. Không tự ý thay đổi phạm vi mà không cập nhật change control.