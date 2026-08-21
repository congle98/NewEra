# Acceptance Policy

Acceptance là quyết định của người/role có thẩm quyền rằng outcome sản phẩm đạt tiêu chí đã được thống nhất. Đây là lớp khác với verification kỹ thuật và checkpoint review.

## Các lớp trạng thái

| Lớp | Ai/điều gì tạo | Ý nghĩa | Không được suy ra |
|---|---|---|---|
| Verification | Agent/operator theo phần test plan trong task.md | Check kỹ thuật và đối chiếu criteria đã chạy; kết quả có thể `VERIFIED`, `PARTIAL`, `FAILED`, `BLOCKED` | Không tự là nghiệm thu |
| Checkpoint | Artifact review của Phase/M | Hồ sơ đủ để người xem xét, hoặc ghi rõ còn thiếu | Không phải `ACCEPTED` |
| Acceptance | Người/role được chỉ định | Quyết định `ACCEPTED`, `REJECTED` hoặc `DEFERRED` dựa trên evidence và product judgment | Không do test pass/hook/report tự tạo |

## Điều kiện chuyển trạng thái

### Để ghi `VERIFIED`

- Requirement và acceptance criteria đã có ID.
- Phần test plan trong `task.md` xác định check, expected, environment và fail criteria.
- Command/kịch bản đã chạy; actual result và artifact được lưu trong evidence.
- Lỗi đã sửa, ghi nhận hoặc chuyển thành residual/blocker.
- Traceability, limitation và commit/worktree reference đã cập nhật.

### Để ghi `CHECKPOINT_PENDING`

- M/Phase có đủ requirements, task.md (bao gồm test plan, evidence và checkpoint) và report theo registry.
- Phạm vi đối chiếu ROADMAP; thay đổi ngoài scope có CR/Decision.
- Residual, technical debt, blocker và risk được liệt kê có ID.
- Chưa có quyết định acceptance hoặc người dùng còn cần xem xét.

### Để ghi `ACCEPTED`

- Có quyết định rõ của người/role nghiệm thu.
- Quyết định nêu artifact/M/Phase, verification status, checkpoint status, acceptance status, ngày, lý do và điều kiện (nếu có).
- Không có residual/blocker làm vi phạm acceptance criteria, trừ ngoại lệ được quyết định và ghi trong Decision Log.
- Report, checkpoint hoặc test pass chỉ là đầu vào; không thay thế quyết định.

## Kết quả không đạt

- `REJECTED`: ghi lý do, criteria không đạt và task/Phase cần mở lại.
- `DEFERRED`: ghi lý do, điều kiện mở lại và nơi đưa vào residual/ROADMAP.
- `BLOCKED`: dùng khi chưa thể kiểm chứng hoặc chưa thể quyết định vì thiếu dependency/quyền/dữ liệu; không gọi là accepted.

## Mẫu quyết định

```markdown
- Artifact/M/Phase:
- Requirement/criteria:
- Verification status: VERIFIED | PARTIAL | FAILED | BLOCKED
- Checkpoint status: INCOMPLETE | CHECKPOINT_PENDING
- Acceptance status: PENDING | ACCEPTED | REJECTED | DEFERRED
- Người/role nghiệm thu:
- Ngày:
- Evidence/report/checkpoint:
- Decision Log/CR:
- Ghi chú, lý do và điều kiện:
```

## Quy tắc mặc định

- `VERIFIED` không tự động chuyển thành `ACCEPTED`.
- `CHECKPOINT_PENDING` luôn được hiển thị là chưa hoàn thành.
- `PENDING` là trạng thái mặc định cho evidence và checkpoint trước quyết định.
- Mọi ngoại lệ phải ghi rõ trong Decision Log và có phạm vi áp dụng; không dùng ngoại lệ để mở rộng scope âm thầm.
