# Execution

Execution là nơi ghi lịch sử triển khai theo M/Phase; code hoặc thay đổi kỹ thuật không được tách khỏi requirements, task, test, evidence và report.

## Cấu trúc chuẩn

```text
docs/06-execution/<M>/
├── milestone-brief.md
└── <P>/
    ├── requirements.md
    ├── task.md
    ├── test-plan.md
    ├── checkpoint.md
    └── report.md

docs/07-evidence/
└── EVD-<M>-<P>.md

docs/08-reports/
├── residual-work.md
├── technical-debt.md
└── <M>-report.md
```

`docs/07-evidence/` là nguồn chính của verification evidence. Không tạo bản sao `verification-evidence.md` trong thư mục Phase trừ khi registry/decision ghi rõ lý do; nếu có bản sao, phải chỉ ra file canonical để tránh divergence.

Với kernel baseline (không có M/Phase sản phẩm), checkpoint là `docs/08-reports/CHK-NEWERA-*.md` và evidence là `docs/07-evidence/EVD-NEWERA-*.md`. Đây là ngoại lệ baseline được khai báo rõ, không phải layout Phase thứ hai.

## Điều kiện bắt đầu Phase (DoR)

- Phase tồn tại trong ROADMAP và dependency đã đạt hoặc có kế hoạch xử lý.
- Requirements có ID, acceptance criteria, in/out scope và liên kết SRS.
- Architecture/environment/registry đủ để thực hiện; phần thiếu là OPEN/BLOCKED có owner.
- Task có output, dependency, status ban đầu và tiêu chí hoàn thành.
- Test plan có check, command/kịch bản, expected result, môi trường và fail criteria.

## Điều kiện hoàn thành kỹ thuật (DoD)

- Task trong phạm vi đã hoàn tất hoặc chuyển residual/blocker có ID.
- Test, build/lint/typecheck/secret scan phù hợp đã chạy hoặc ghi `NOT_APPLICABLE` kèm lý do.
- Traceability, evidence, checkpoint, phase report và residual/debt đã cập nhật.
- Git commit hoặc worktree reference được ghi; không có secret.
- Trạng thái kỹ thuật là `VERIFIED` hoặc `PARTIAL/FAILED/BLOCKED` đúng bằng chứng; không tự đánh dấu `ACCEPTED`.

Dùng template trong `docs/templates/`. Không đánh dấu M/Phase hoàn tất nếu thiếu report, evidence hoặc residual work.
