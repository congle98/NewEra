# Requirements Traceability

Bảng này là đường đi hai chiều từ ý định sản phẩm tới bằng chứng. Mỗi requirement trong SRS phải đi xuống được ROADMAP → Phase → Task → Test → Evidence; khi có kết quả, evidence phải truy ngược được về acceptance criteria cụ thể.

## Ma trận product requirements hiện tại

| Requirement | ROADMAP/M | Phase | Task | Test | Evidence | Acceptance criteria | Status | Gap/next action |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | Chưa xác định | Chưa xác định | Chưa tạo | Chưa tạo | Chưa tạo | Chưa xác định | DRAFT | Hoàn thiện intake/charter trước |

Dòng `REQ-001` hiện là placeholder từ SRS, không phải bằng chứng rằng M01/P01 đã tồn tại hoặc đã kiểm chứng. Khi có requirement thật, thay nội dung bằng ID ổn định và giữ lịch sử trong diff.

## Ma trận quality attributes của kernel

Các dòng dưới đây là quality attributes trong Architecture, không tạo M/Phase sản phẩm mới. Vì ROADMAP hiện chưa có project scope, cột M/Phase ghi rõ `Không có`; evidence hiện chỉ kiểm chứng static documentation contract.

| Requirement/NFR | ROADMAP/M | Phase | Task | Test | Evidence | Status | Gap/next action |
|---|---|---|---|---|---|---|---|
| NFR-NEWERA-001 Traceability | Kernel baseline (không có M) | Không có | TASK-NEWERA-DOC-001 | TEST-NEWERA-DOCS-002/003 | EVD-NEWERA-DOCS-001 | PARTIAL | Dogfood project để kiểm tra traceability end-to-end |
| NFR-NEWERA-002 Auditability | Kernel baseline (không có M) | Không có | TASK-NEWERA-DOC-001 | TEST-NEWERA-DOCS-003/005 | EVD-NEWERA-DOCS-001 | PARTIAL | Giữ evidence/decision/CR theo commit |
| NFR-NEWERA-003 Technology neutrality | Kernel baseline (không có M) | Không có | TASK-NEWERA-DOC-001 | TEST-NEWERA-DOCS-004 | EVD-NEWERA-DOCS-001 | VERIFIED | Re-check khi project con kích hoạt adapter |
| NFR-NEWERA-004 Honest status | Kernel baseline (không có M) | Không có | TASK-NEWERA-DOC-001 | TEST-NEWERA-DOCS-004 | EVD-NEWERA-DOCS-001 | VERIFIED | Acceptance vẫn chờ người/role |
| NFR-NEWERA-005 Operability | Kernel baseline (không có M) | Không có | TASK-NEWERA-DOC-001 | TEST-NEWERA-DOCS-001/006 | EVD-NEWERA-DOCS-001 | PARTIAL | Runtime Kiro dogfood còn residual |

## Quy tắc cập nhật

1. Không tạo mapping tới M/Phase chưa có trong ROADMAP. `Kernel baseline (không có M)` ở bảng quality attributes là context, không phải M mới.
2. Một requirement có nhiều acceptance criteria phải có thể truy ngược từng criteria; có thể dùng cột `Criteria ID` hoặc tách dòng.
3. Test phải nêu được loại check và command/kịch bản; `PASS` là kết quả test, không phải acceptance.
4. Evidence phải có ID, commit/worktree reference, environment, timestamp, expected, actual và limitations.
5. Requirement chỉ được `VERIFIED` khi mọi criteria bắt buộc đã có evidence đạt hoặc có ngoại lệ được ghi rõ trong Decision Log.
6. Requirement chỉ được `ACCEPTED` sau quyết định nghiệm thu của người/role có thẩm quyền; bảng này không tự tạo acceptance.
7. Nếu một requirement bị đổi, tạo CR khi đổi nghĩa/scope; không sửa ID để che lịch sử.

## Các trạng thái truy nguyên

- `DRAFT/OPEN`: chưa đủ dữ liệu hoặc chưa có mapping.
- `IN_PROGRESS`: đang thực hiện task liên quan.
- `VERIFIED`: criteria kỹ thuật đạt, có evidence.
- `PARTIAL`: chỉ một phần criteria đạt; phần còn lại phải là residual/blocker.
- `BLOCKED`: không thể kiểm chứng vì dependency/quyền/dữ liệu.
- `ACCEPTED`: chỉ sau nghiệm thu, không suy ra từ `VERIFIED`.
