# Project Intake

> Điền tài liệu này trước khi lập ROADMAP. Đây là nơi ghi ý tưởng gốc, không phải nơi tự suy đoán yêu cầu. Mọi câu chưa biết phải giữ `OPEN` và có ID.

- Intake ID/version: INTAKE-001 / v0.1
- Trạng thái: DRAFT
- Owner/đầu mối:
- Ngày bắt đầu/cập nhật:
- Liên kết research/assumption/decision:

## Vòng 1 - Sản phẩm

### Thông tin cơ bản

- Tên dự án:
- Mô tả một câu:
- Người đề xuất:
- Nhóm người dùng chính:
- Bên liên quan/quyền quyết định:

### Vấn đề và cơ hội

- Vấn đề cần giải quyết:
- Ai đang gặp vấn đề, tần suất và mức ảnh hưởng:
- Cách giải quyết hiện tại và hạn chế:
- Vì sao cần làm bây giờ:
- Điều gì xảy ra nếu không làm:

### Kết quả mong muốn

- Kết quả sản phẩm quan sát được:
- Kết quả kinh doanh/người dùng:
- Chỉ số thành công và baseline:
- Tiêu chí thất bại hoặc dừng:
- Cách người dùng xác nhận giá trị:

### Phạm vi ban đầu

**Bắt buộc (must):**

- [ ] Chưa xác định

**Có thể làm sau (should/could):**

- [ ] Chưa xác định

**Ngoài phạm vi (won't):**

- [ ] Chưa xác định

Mỗi mục scope phải liên kết `OBJ`, `REQ`, `M/Phase` hoặc ghi `OPEN`; không dùng intake để lén thêm feature.

## Vòng 2 - Làm rõ kỹ thuật và vận hành

- Nền tảng/runtime đang có:
- Dữ liệu đầu vào/đầu ra và độ nhạy:
- Tích hợp/API/external dependency:
- Yêu cầu hiệu năng/availability/scale:
- Authentication/authorization/audit:
- Backup, recovery, migration và retention:
- Deployment/monitoring/support:
- Bảo mật, pháp lý, compliance:
- Ràng buộc thời gian, ngân sách, team và quyền:
- Tài sản/code/repository hiện có:

## Câu hỏi còn mở

| ID | Câu hỏi | Ảnh hưởng | Owner | Deadline/trigger | Liên kết | Trạng thái |
|---|---|---|---|---|---|---|
| INTAKE-001 | Chưa xác định | Chưa đánh giá | Chưa chỉ định | Trước ROADMAP READY | — | OPEN |

Câu hỏi ảnh hưởng scope/architecture/security/cost phải chuyển thành `RES`, `ASM`, `RISK` hoặc `CR` phù hợp; không đóng bằng câu trả lời phỏng đoán.

## Điều kiện hoàn tất intake

- [ ] Problem, user, outcome và success metric đã có câu trả lời.
- [ ] Must/should/won't và ngoài phạm vi đã rõ.
- [ ] Ràng buộc kỹ thuật/vận hành đã ghi hoặc đánh dấu OPEN.
- [ ] Assumptions, research, risks và decision cần thiết đã có ID.
- [ ] Người/role có quyền xác nhận scope đã được chỉ định.

## Trạng thái

`DRAFT` cho tới khi các câu hỏi ảnh hưởng trực tiếp được giải quyết hoặc chuyển thành artifact có owner/next action. Intake hoàn tất không tự làm M/Phase `READY`.
