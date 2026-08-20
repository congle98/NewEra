# Technical Debt

Technical debt là lựa chọn tạm thời có chủ ý, khác với blocker hoặc phần việc bị quên. Debt chỉ được chấp nhận khi có lý do, rủi ro, owner/điều kiện trả và liên kết nguồn.

| ID | Nguồn | Mô tả | Lý do chấp nhận | Rủi ro | Kế hoạch trả | Ưu tiên | Trạng thái |
|---|---|---|---|---|---|---|---|
| DEBT-NEWERA-001 | NewEra v0.1 | Chưa có test runner tự động cho tài liệu Markdown; hiện kiểm tra bằng lệnh repository/tooling | Kernel không khóa toolchain và baseline chưa có application code | Có thể bỏ sót link/status/ID nếu chỉ review thủ công | Tạo checker khi dogfood chứng minh nhu cầu; ghi command/evidence trong registry | MEDIUM | OPEN |
| DEBT-NEWERA-002 | NewEra v0.1 | Agent/skill/hook mới được kiểm chứng tĩnh, chưa có runtime dogfood evidence | Chưa có project mẫu hoặc phiên Kiro đã được ghi nhận | Hành vi runtime có thể khác kỳ vọng trong prompt/schema | Chạy RESID-NEWERA-005 và cập nhật evidence/skill nếu phát hiện gap | MEDIUM | OPEN |

## Quy tắc

1. Debt phải liên kết ít nhất một M/Phase hoặc residual; không dùng bảng này làm nơi chứa việc chưa phân loại.
2. Debt không được che blocker hoặc acceptance gap. Nếu không thể tiếp tục, dùng `BLOCKED` ở artifact thực hiện.
3. Khi trả debt, ghi evidence/commit và chuyển status; không xóa dòng lịch sử.
