# Assumptions

Assumption là điều đang tạm coi là đúng để lập kế hoạch nhưng chưa được chứng minh. Assumption không được viết như requirement, architecture decision hoặc fact. Assumption ảnh hưởng cao phải chuyển thành research item, risk hoặc decision.

| ID | Giả định | Cơ sở hiện có | Ảnh hưởng nếu sai | Cách kiểm chứng | Owner/trigger | Liên kết | Trạng thái |
|---|---|---|---|---|---|---|---|
| ASM-001 | Chưa có giả định sản phẩm đã được xác nhận | Intake/product scope chưa hoàn thiện | Không thể chốt M/Phase/SRS/Architecture | Hoàn thiện project intake và charter | Người đề xuất / trước ROADMAP READY | INTAKE-001 | OPEN |

## Phân loại

- **Scope assumption:** ảnh hưởng mục tiêu, user, must/won't hoặc acceptance; không được dùng để tạo task thực thi nếu chưa có owner.
- **Technical assumption:** ảnh hưởng runtime, dependency, performance, security hoặc data; liên kết `RES`/ADR.
- **Operational assumption:** ảnh hưởng quyền, cost, deployment, support, backup hoặc compliance; cần owner cụ thể.

## Quy tắc vòng đời

1. Tạo ID ngay khi assumption được phát hiện.
2. Ghi evidence hoặc nguồn làm cơ sở; nếu chưa có, ghi `Chưa có`.
3. Đặt mức ảnh hưởng và trigger kiểm chứng.
4. Khi đúng: ghi kết quả, ngày và link evidence; có thể chuyển `RESOLVED`/`ACCEPTED` tùy artifact.
5. Khi sai: cập nhật SRS/ROADMAP/Architecture qua change control nếu nghĩa hoặc scope thay đổi.
6. Không xóa assumption đã đóng; giữ lịch sử để giải thích quyết định.
