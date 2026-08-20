# Technical Debt

Technical debt là lựa chọn tạm thời có chủ ý, khác với blocker hoặc phần việc bị quên. Debt chỉ được chấp nhận khi có lý do, rủi ro, owner/điều kiện trả và liên kết nguồn.

| ID | Nguồn | Mô tả | Lý do chấp nhận | Rủi ro | Kế hoạch trả | Ưu tiên | Trạng thái |
|---|---|---|---|---|---|---|---|
| DEBT-NEWERA-001 | NewEra v0.1 | Chưa có test runner tự động cho Markdown; hiện có validator state/evidence bằng Python | Kernel không khóa toolchain và P0 tập trung machine contract | Có thể bỏ sót consistency narrative nếu không có checker | Mở rộng validator/link checker sau dogfood | MEDIUM | OPEN |
| DEBT-NEWERA-002 | NewEra v0.1 | Agent/skill/hook mới được kiểm chứng tĩnh, chưa có runtime dogfood evidence | Chưa có project mẫu/phiên Kiro được ghi nhận | Runtime behavior có thể khác prompt/schema | Chạy RESID-NEWERA-005 | MEDIUM | OPEN |
| DEBT-NEWERA-P0-001 | M01-P01 | Validator thực thi JSON/state subset, chưa là full JSON Schema engine | Python standard library giữ technology neutrality/no dependency | Một số constraint schema nâng cao chỉ được mô tả, chưa enforce | Mở rộng bằng validator contract có test hoặc thêm dependency qua CR | MEDIUM | OPEN |
| DEBT-NEWERA-P0-002 | M01-P02 | Hook Kiro mới gọi/nhắc gate qua askAgent, chưa phải blocking runtime enforcement | Hook semantics hiện tại không cung cấp deterministic shell runner trong baseline | Agent có thể bỏ qua gate nếu không có CI/pre-commit | M01.1 sau runtime dogfood | HIGH | OPEN |

## Quy tắc

1. Debt phải liên kết ít nhất một M/Phase hoặc residual; không dùng bảng này làm nơi chứa việc chưa phân loại.
2. Debt không được che blocker hoặc acceptance gap. Nếu không thể tiếp tục, dùng `BLOCKED` ở artifact thực hiện.
3. Khi trả debt, ghi evidence/commit và chuyển status; không xóa dòng lịch sử.
