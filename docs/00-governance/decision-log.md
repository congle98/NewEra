# Decision Log

Decision Log là lịch sử quyết định có ảnh hưởng đến scope, architecture, process hoặc acceptance. Một quyết định phải giữ bối cảnh và các phương án để người đọc sau này hiểu vì sao hệ thống hiện tại có hình dạng đó.

| ID | Ngày | Quyết định | Bối cảnh | Ảnh hưởng | Người/role | Trạng thái |
|---|---|---|---|---|---|---|
| DEC-000 | 2026-08-20 | Đề xuất dùng NewEra v0.1 làm baseline quy trình | Cần một kernel có governance, traceability, verification và acceptance tách biệt | Áp dụng cấu trúc tài liệu, automation và triết lý hiện tại; chưa xác nhận nghiệm thu cuối | Chưa ghi nhận | PROPOSED |

`DEC-000` chỉ ghi nhận baseline đã được tạo trong repository; `PROPOSED` là cố ý vì chưa có record người/role nghiệm thu. Không dùng dòng này để suy ra sản phẩm đã được accepted.

## Quy tắc

1. ID tăng dần `DEC-001`, `DEC-002` và không tái sử dụng.
2. Quyết định lớn phải liên kết tới CR, ADR, requirement hoặc research liên quan.
3. `ACCEPTED` ở Decision Log nghĩa là quyết định đã được thông qua, không đồng nghĩa M/Phase đã nghiệm thu.
4. Khi quyết định bị thay thế, giữ bản cũ ở `SUPERSEDED`, ghi ID quyết định thay thế và không xóa lịch sử.
5. Nếu chưa biết người/role hoặc ngày, ghi `Chưa ghi nhận`/`OPEN`; không dùng placeholder như sự thật.

## Mẫu

```markdown
## DEC-XXX: Tên quyết định
- Bối cảnh:
- Nguồn/ID liên quan: CR-/RES-/RISK-/REQ-/ADR-
- Các phương án:
- Quyết định:
- Lý do:
- Ảnh hưởng scope/architecture/operations/acceptance:
- Người/role quyết định:
- Ngày:
- Quyết định thay thế (nếu có):
- Trạng thái: PROPOSED | ACCEPTED | SUPERSEDED
```
