# NewEra v0.1 Baseline Report

- Scope: NewEra process kernel
- Verification status: VERIFIED
- Checkpoint status: CHECKPOINT_PENDING
- Acceptance status: NOT_ACCEPTED
- Initial commit: eaf1e5f
- Evidence: `docs/07-evidence/EVD-NEWERA-V01.md`

## Đã hoàn thành

- AGENTS.md làm hiến pháp workspace.
- Governance: status, document registry, decision log, change control và Git policy.
- Discovery: intake, charter, assumptions và research.
- ROADMAP, milestone index, SRS, traceability và acceptance policy.
- Architecture, ADR, environment manifest và setup report.
- Template M/Phase, task, test-plan, checkpoint, evidence, report và research.
- 5 custom agent Markdown.
- 6 NewEra skills.
- 6 steering files.
- 3 hooks theo schema workspace.
- Prompt start project, execute milestone và verify phase.

## Đã kiểm chứng

- Hook JSON parse thành công.
- Diagnostics không có lỗi trên AGENTS.md và hook files.
- Không tạo autonomy policy riêng hoặc Vòng 3 quyền tự chủ.
- Git repository có commit nền và working tree sạch.

## Còn lại

- Điền intake cho dự án cụ thể.
- Xác định ROADMAP, M, Phase, SRS và Architecture thực tế.
- Chạy thử NewEra trên một dự án nhỏ.
- Kiểm chứng agent/skill/hook trong phiên Kiro thực tế.
- Điều chỉnh template sau lần dogfooding đầu tiên.

## Residual work

- RESID-NEWERA-001: Dogfood NewEra bằng một dự án mẫu.
- RESID-NEWERA-002: Thêm adapter công nghệ chỉ khi dự án đầu tiên cần.

## Blocker

Không có blocker cho việc tạo baseline. Nghiệm thu cuối cùng đang chờ người dùng xem xét.

## Quyết định nghiệm thu

Baseline đang ở `CHECKPOINT_PENDING`, chưa hoàn thành và không được dùng làm bằng chứng nghiệm thu sản phẩm.