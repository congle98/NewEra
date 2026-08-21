---
inclusion: always
---

# NewEra Execution Steering

Runtime rule: thực hiện đúng thứ tự trong ROADMAP và dùng `task.md` làm working file canonical. Mọi mutation phải qua preflight theo `docs/00-governance/automation-contract.md`.

- Đọc dependency/environment trước task.
- Với `MICRO_CHANGE`, bind vào task/request hiện có, ghi path boundary và expected result; không tạo full foundation/Phase artifact chỉ vì thay đổi nhỏ.
- Ghi targeted test và evidence ngắn cho `MICRO_CHANGE`; lỗi hoặc scope phát sinh phải chuyển thành blocker/residual hoặc route bình thường.
- Với `NORMAL_OR_SCOPE_CHANGE`, ghi test, evidence và checkpoint trong `task.md`; report chỉ là summary.
- Scope change đi qua `docs/00-governance/change-control.md`.
- Sau Phase cập nhật report, residual/debt và traceability.
