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

## Worktree và line endings

- Trước khi sửa: chạy `git status --short` và không ghi đè thay đổi không thuộc scope.
- Sau khi sửa: chạy `git diff --check` theo line-ending policy của repository, kiểm tra `git diff --stat` và rà file ngoài scope.
- Repository baseline hiện giữ Markdown ở CRLF. Khi kiểm tra whitespace trên diff dùng `git -c core.whitespace=cr-at-eol diff --check` để CRLF không bị coi là trailing whitespace.
- Không chuẩn hóa line ending toàn repository trong một thay đổi tài liệu thông thường; nếu muốn đổi convention, tạo change request riêng và ghi ảnh hưởng diff/review.
- Commit mới phải ghi artifact/evidence/worktree reference phù hợp; không tuyên bố commit khi chưa tạo.
