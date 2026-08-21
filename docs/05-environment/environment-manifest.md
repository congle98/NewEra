# Environment Manifest

## Runtime

| Tool | Version/constraint | Required | Detected | Status |
|---|---|---:|---|---|
| Git | Chưa xác định | Yes | Unknown | OPEN |
| Runtime | Theo dự án | Conditional | Unknown | OPEN |
| Package manager | Theo dự án | Conditional | Unknown | OPEN |
| Docker | Theo dự án | Conditional | Unknown | OPEN |

## Services

- ENV-SVC-001:

## Commands

```text
Setup: chưa xác định
Test: chưa xác định
Build: chưa xác định
Run: chưa xác định
```

## Notes

AI cập nhật phần phát hiện được và ghi phần không thể tự kiểm tra vào `setup-report.md`.
## Setup procedure

### Prerequisites

- Tool/runtime/service theo bảng Runtime và Services.
- Quyền truy cập, account, secret/config phải được cấp qua environment/secret manager; không ghi secret vào repository.

### Setup

1. Kiểm tra manifest và version các tool.
2. Cài dependency theo lockfile nếu có.
3. Tạo `.env` từ `.env.example` nếu dự án cần.
4. Khởi động service local cần thiết.
5. Chạy smoke test.

### Verification và troubleshooting

- Lệnh/kịch bản:
- Kết quả mong đợi:
- Lỗi và cách xử lý:

Ghi kết quả thực tế, issue và action vào `setup-report.md`; không xóa lịch sử phát hiện.
