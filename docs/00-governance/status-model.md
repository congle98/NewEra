# Status Model

## Trạng thái công việc

- `DRAFT`: mới tạo, chưa đủ điều kiện thực hiện.
- `READY`: đủ thông tin và dependency để bắt đầu.
- `IN_PROGRESS`: đang triển khai.
- `VERIFIED`: đã chạy kiểm chứng kỹ thuật theo test plan.
- `CHECKPOINT_PENDING`: đã đến điểm xem xét, chưa hoàn thành nghiệm thu.
- `ACCEPTED`: đã được nghiệm thu theo acceptance policy.
- `BLOCKED`: không thể tiếp tục vì thiếu quyết định, quyền hoặc dependency.
- `DEFERRED`: chủ động dời lại.
- `REJECTED`: không đạt nghiệm thu.
- `CANCELLED`: không còn trong phạm vi.

## Luật nghiêm ngặt

`CHECKPOINT_PENDING` không phải `ACCEPTED`.

`VERIFIED` không phải `ACCEPTED`.

Checkpoint hoặc report chưa hoàn thành không được dùng làm bằng chứng nghiệm thu. Evidence chỉ chứng minh việc kiểm chứng kỹ thuật đã diễn ra.