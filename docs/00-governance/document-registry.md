# Document Registry

Registry quyết định tài liệu nào bắt buộc, có điều kiện hoặc không áp dụng cho dự án.

| Document | Required | Purpose | Status |
|---|---:|---|---|
| Project Intake | Yes | Ghi nhận ý tưởng và bối cảnh | DRAFT |
| Project Charter | Yes | Mục tiêu và phạm vi | DRAFT |
| Research | Yes | Vấn đề cần tìm hiểu và nguồn | DRAFT |
| ROADMAP | Yes | Nguồn sự thật về M/Phase | DRAFT |
| SRS | Yes | Yêu cầu sản phẩm | DRAFT |
| Architecture | Yes | Giải pháp và quyết định kỹ thuật | DRAFT |
| API Specification | Conditional | Khi có API | NOT_APPLICABLE |
| Database Design | Conditional | Khi có database | NOT_APPLICABLE |
| Threat Model | Conditional | Khi có dữ liệu hoặc rủi ro bảo mật | NOT_APPLICABLE |
| Deployment Guide | Conditional | Khi có môi trường triển khai | NOT_APPLICABLE |
| Migration Plan | Conditional | Khi thay đổi dữ liệu/schema | NOT_APPLICABLE |
| UX Specification | Conditional | Khi có giao diện người dùng | NOT_APPLICABLE |

## Quy tắc

Agent phải cập nhật registry khi phát hiện tài liệu điều kiện trở thành cần thiết. Không tạo tài liệu chỉ để làm đầy cấu trúc.