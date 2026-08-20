# Acceptance Policy

## Các lớp trạng thái

- Verification: agent chạy test và đối chiếu acceptance criteria.
- Checkpoint: sản phẩm đủ điều kiện để xem xét, nhưng chưa hoàn thành nghiệm thu.
- Acceptance: quyết định chấp thuận theo tiêu chí của dự án.

## Quy tắc mặc định

- `VERIFIED` không tự động chuyển thành `ACCEPTED`.
- `CHECKPOINT_PENDING` luôn được hiển thị là chưa hoàn thành.
- Report, checkpoint hoặc test pass không được giả làm bằng chứng nghiệm thu.
- Mọi ngoại lệ phải ghi rõ trong Decision Log và có phạm vi áp dụng.

## Mẫu quyết định

```markdown
- Phase/M:
- Verification status:
- Checkpoint status:
- Acceptance status:
- Người/role nghiệm thu:
- Ngày:
- Ghi chú:
```