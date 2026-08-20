# Decision Log

Decision Log là lịch sử quyết định có ảnh hưởng đến scope, architecture, process hoặc acceptance. Một quyết định phải giữ bối cảnh và các phương án để người đọc sau này hiểu vì sao hệ thống hiện tại có hình dạng đó.

| ID | Ngày | Quyết định | Bối cảnh | Ảnh hưởng | Người/role | Trạng thái |
|---|---|---|---|---|---|---|
| DEC-XXX | | | | | | PROPOSED |

The NewEra repository provides the decision-log format. A project adopting NewEra owns the actual decision records and acceptance decisions in its own workspace.
## Quy tắc

1. ID tăng dần `DEC-XXX`, `DEC-YYY` và không tái sử dụng.
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
