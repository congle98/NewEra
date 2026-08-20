# M01-P02 - Task List

- Phase: M01-P02
- Trạng thái: IN_PROGRESS

| ID | Mô tả | Requirement | Dependency | Output | Status |
|---|---|---|---|---|---|
| TASK-NEWERA-P02-001 | Implement deterministic validator và STANDARD profile checks | P0-004/P0-005 | M01-P01 | `scripts/newera_validate.py` | VERIFIED |
| TASK-NEWERA-P02-002 | Tạo negative fixture, evidence và documentation integration | P0-004/P0-005 | TASK-P02-001 | fixture, evidence, report | VERIFIED |

Gate không được sửa state để làm test pass; fixture lỗi phải giữ để kiểm tra failure path.
