# NewEra v0.1 Baseline Report

- Scope: NewEra process kernel
- Baseline commit: eaf1e5f (historical evidence)
- Current repository HEAD at documentation review start: 2c39b01
- Verification status of historical baseline: VERIFIED
- Current documentation enrichment status: IN_PROGRESS
- Checkpoint status: CHECKPOINT_PENDING
- Acceptance status: NOT_ACCEPTED
- Historical evidence: `docs/07-evidence/EVD-NEWERA-V01.md`
- Current review evidence: `docs/07-evidence/EVD-NEWERA-DOCS-001.md`
- Current checkpoint record: `docs/08-reports/CHK-NEWERA-V01.md`

## Đã hoàn thành trong baseline

- AGENTS.md làm hiến pháp workspace.
- Governance: status, document registry, decision log, change control và Git policy.
- Discovery: intake, charter, assumptions và research.
- ROADMAP, milestone index, SRS, traceability và acceptance policy.
- Architecture, ADR, environment manifest và setup report.
- Template M/Phase, task, test-plan, checkpoint, evidence, report và research.
- Custom agents, NewEra skills, steering files và hooks.
- GUIDE.md tổng hợp quy trình và thư viện prompt.

## Bổ sung trong lần rà soát tài liệu này

- Chuẩn hóa status vocabulary, trạng thái phụ, luật chuyển trạng thái và prefix ID.
- Mở rộng registry để phản ánh artifact thực tế, đường dẫn canonical và trigger tài liệu conditional.
- Bổ sung change request register, impact checklist và Decision Log có người/role.
- Làm rõ ROADMAP DoR/DoD, milestone index, traceability và acceptance policy.
- Mô tả kiến trúc kernel hiện tại, boundary, data flow, không gian ngoài phạm vi và technology neutrality.
- Làm đầy environment manifest, execution layout, task/test/checkpoint/evidence templates.
- Đồng bộ residual work/technical debt với các ID có trong report; tạo checkpoint record cho baseline.

## Kiểm chứng

Historical baseline đã có evidence riêng tại `EVD-NEWERA-V01.md`; evidence đó không được kéo dài để bao phủ các thay đổi sau commit nền. Lần rà soát hiện tại phải dùng `EVD-NEWERA-DOCS-001.md` với worktree reference, command và limitations cụ thể.

## Còn lại / residual

- `RESID-NEWERA-001`: dogfood NewEra bằng project mẫu nhỏ.
- `RESID-NEWERA-002`: chỉ thêm technology adapter khi project đầu tiên cần.
- `RESID-NEWERA-003`: hoàn tất đồng bộ vocabulary/ID trên mọi artifact còn lại.
- `RESID-NEWERA-004`: duy trì evidence/checkpoint/report theo commit hiện hành.
- `RESID-NEWERA-005`: kiểm chứng agent/skill/hook trong phiên Kiro thực tế.
- `DEBT-NEWERA-001` và `DEBT-NEWERA-002`: technical debt đang mở theo sổ debt.

## Blocker

Không có blocker cho việc làm đầy tài liệu kernel. Việc tạo project-specific ROADMAP/SRS/Architecture và runtime dogfood vẫn `OPEN`; không được tự suy đoán để đóng khoảng trống.

## Quyết định nghiệm thu

Baseline và lần enrichment này đang ở `CHECKPOINT_PENDING`/`NOT_ACCEPTED` cho đến khi người dùng hoặc role có thẩm quyền xem xét và đưa quyết định theo acceptance policy. Tài liệu này không tự tạo acceptance.
