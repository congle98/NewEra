# Verification Evidence

Evidence chứng minh các kiểm tra kỹ thuật đã được thực hiện. Evidence không tự động là nghiệm thu sản phẩm.

## Canonical location

- Evidence của Phase: `docs/07-evidence/EVD-<M>-<P>.md`.
- Evidence của baseline/kernel: `docs/07-evidence/EVD-NEWERA-*.md`.
- Checkpoint là artifact review riêng; không dùng checkpoint thay cho evidence.

## Required fields

Mỗi evidence cần có:

- ID và scope/M/Phase/requirement liên quan;
- task/test IDs và commit hoặc worktree reference;
- môi trường, agent/operator và timestamp;
- command/kịch bản có thể tái chạy;
- expected, actual/output summary, status và artifact path;
- limitations, `NOT_APPLICABLE` reason, residual và blocker;
- acceptance status rõ ràng là `NOT_ACCEPTED` nếu chưa có quyết định.

## Evidence lifecycle

1. Tạo từ test plan trước hoặc trong verification.
2. Ghi kết quả nguyên văn hoặc summary đủ tái lập, không chỉ ghi “pass”.
3. Link vào traceability, checkpoint và report.
4. Không sửa evidence cũ để đổi lịch sử; tạo revision/evidence mới khi scope hoặc commit thay đổi.
5. Evidence chỉ kết luận `VERIFIED`, `PARTIAL`, `FAILED`, `BLOCKED` hoặc `NOT_RUN`; `PASS`/`FAIL` chỉ là kết quả của từng check. Acceptance nằm ở acceptance policy.
