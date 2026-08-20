# MXX-PXX - Task List

- Phase:
- Requirement scope:
- Owner/role:
- Trạng thái: DRAFT

## Definition of Ready cho task

Task chỉ được `READY` khi có một output kiểm tra được, dependency rõ, requirement/acceptance criteria liên quan, cách kiểm chứng và biết tài liệu nào sẽ cập nhật. Task thiếu dữ liệu quan trọng phải là `BLOCKED` hoặc `OPEN`, không giả định.

## Tasks

| ID | Mô tả | Requirement | Dependency | Output/changed artifact | Verification | Status |
|---|---|---|---|---|---|---|
| TASK-MXX-PXX-001 | Kiểm tra dependency | REQ- | — | Dependency/status note | TEST- | DRAFT |
| TASK-MXX-PXX-002 | Triển khai phần chính | REQ- | TASK-001 | Code/config/documentation | TEST- | DRAFT |
| TASK-MXX-PXX-003 | Viết/cập nhật test | REQ- | TASK-002 | Test artifact | TEST- | DRAFT |
| TASK-MXX-PXX-004 | Cập nhật tài liệu và traceability | REQ- | TASK-002/003 | Docs/traceability | TEST- | DRAFT |
| TASK-MXX-PXX-005 | Chạy verification | REQ- | TASK-001..004 | Evidence result | TEST- | DRAFT |
| TASK-MXX-PXX-006 | Tạo evidence, checkpoint và report | REQ- | TASK-005 | EVD/CHK/RPT | Review | DRAFT |

## Definition of Done cho task

Mỗi task phải có output, dependency, requirement link, verification result và status. Task chỉ `VERIFIED` khi output đã được kiểm tra; task chưa xong không được đánh dấu hoàn thành chỉ vì code hoặc file đã tồn tại. Nếu không hoàn thành, ghi residual/blocker ID và lý do.
