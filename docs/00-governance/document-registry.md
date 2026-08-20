# Document Registry

Registry là danh mục có kiểm soát của tài liệu trong một project. Nó trả lời ba câu hỏi: tài liệu nào phải có, điều kiện nào kích hoạt tài liệu tùy chọn, và tài liệu hiện đang ở trạng thái nào. Registry không thay thế ROADMAP, SRS, Architecture hoặc evidence.

## Tài liệu nền bắt buộc

| Document | Path | Required | Purpose | Status | Owner/next action |
|---|---|---:|---|---|---|
| Project Intake | `docs/01-discovery/project-intake.md` | Yes | Ghi nhận ý tưởng, vấn đề, người dùng, ràng buộc và câu hỏi mở | DRAFT | Hoàn thiện trước ROADMAP |
| Project Charter | `docs/01-discovery/project-charter.md` | Yes | Chốt tầm nhìn, mục tiêu, phạm vi và tiêu chí thành công | DRAFT | Sinh từ intake đã làm rõ |
| Research Log | `docs/01-discovery/research.md` | Yes | Ghi câu hỏi chưa biết, nguồn, kết luận và độ tin cậy | DRAFT | Đóng hoặc chuyển RES ảnh hưởng cao |
| Assumptions | `docs/01-discovery/assumptions.md` | Yes | Theo dõi giả định chưa được chứng minh | OPEN | Liên kết research/decision |
| ROADMAP | `docs/02-roadmap/roadmap.md` | Yes | Nguồn sự thật về M, Phase, scope, dependency và thứ tự | DRAFT | Chỉ READY sau intake/charter |
| Milestone Index | `docs/02-roadmap/milestone-index.md` | Yes | Chỉ mục M và trạng thái tóm tắt | DRAFT | Đồng bộ với ROADMAP |
| SRS | `docs/03-requirements/srs.md` | Yes | Requirement có ID, acceptance criteria và phạm vi M/Phase | DRAFT | Hoàn thiện sau khi scope ổn định |
| Traceability | `docs/03-requirements/requirements-traceability.md` | Yes | Nối requirement → task → test → evidence → status | DRAFT | Cập nhật mỗi Phase |
| Acceptance Policy | `docs/03-requirements/acceptance-policy.md` | Yes | Phân biệt verification, checkpoint và acceptance | DRAFT | Dùng làm chuẩn nghiệm thu |
| Architecture | `docs/04-architecture/architecture.md` | Yes | Boundary, thành phần, luồng dữ liệu và giới hạn thiết kế | DRAFT | Không chốt công nghệ khi thiếu dữ liệu |
| ADR index | `docs/04-architecture/adr/README.md` | Yes | Mẫu và chỉ mục quyết định kỹ thuật dài hạn | DRAFT | Tạo ADR khi có quyết định lớn |
| Environment Manifest | `docs/05-environment/environment-manifest.md` | Yes | Runtime, tool, service và command cần cho kiểm chứng | PARTIAL | Cập nhật theo project thực tế |
| Setup Guide/Report | `docs/05-environment/setup-guide.md`, `setup-report.md` | Conditional | Cách chuẩn bị môi trường và kết quả lần kiểm tra | PARTIAL | Runtime dogfood còn OPEN |

## Tài liệu hỗ trợ và chỉ mục

| Document | Path | Required | Purpose/trigger | Status |
|---|---|---:|---|---|
| README/GUIDE | `README.md`, `GUIDE.md` | Yes | Onboarding, quy trình và prompt library | CURRENT |
| Changelog | `CHANGELOG.md` | Yes | Lịch sử thay đổi đáng kể của kernel | CURRENT |
| Execution index | `docs/06-execution/README.md` | Yes | Cấu trúc và DoR/DoD của M/Phase | CURRENT |
| Evidence index | `docs/07-evidence/README.md` | Yes | Quy ước evidence và canonical location | CURRENT |
| Baseline evidence | `docs/07-evidence/EVD-NEWERA-V01.md`, `EVD-NEWERA-DOCS-001.md` | Yes | Evidence lịch sử và lần review hiện tại | VERIFIED/PARTIAL |
| Baseline Checkpoint | `docs/08-reports/CHK-NEWERA-*.md` | Conditional | Checkpoint kernel khi chưa có M/Phase sản phẩm | CHECKPOINT_PENDING |
| Operations index | `docs/09-operations/README.md` | Conditional | Điều kiện kích hoạt tài liệu vận hành | CURRENT |

## Tài liệu theo M/Phase

| Document | Path | Required | Điều kiện | Status |
|---|---|---:|---|---|
| Milestone Brief | `docs/06-execution/<M>/milestone-brief.md` | Yes | M được đưa vào thực hiện | NOT_STARTED |
| Phase Requirements | `docs/06-execution/<M>/<P>/requirements.md` | Yes | M có Phase | NOT_STARTED |
| Task List | `docs/06-execution/<M>/<P>/task.md` | Yes | M có Phase | NOT_STARTED |
| Test Plan | `docs/06-execution/<M>/<P>/test-plan.md` | Yes | M có Phase | NOT_STARTED |
| Checkpoint | `docs/06-execution/<M>/<P>/checkpoint.md` | Yes | Phase tới điểm xem xét | NOT_STARTED |
| Verification Evidence | `docs/07-evidence/EVD-<M>-<P>.md` | Yes | Có verification | NOT_STARTED |
| Phase Report | `docs/06-execution/<M>/<P>/report.md` | Yes | Phase tới điểm báo cáo | NOT_STARTED |
| Milestone Report | `docs/08-reports/<M>-report.md` | Yes | M kết thúc vòng thực hiện | NOT_STARTED |
| Residual Work | `docs/08-reports/residual-work.md` | Yes | Mọi M/Phase có phần chưa làm | OPEN |
| Technical Debt | `docs/08-reports/technical-debt.md` | Conditional | Có debt được chấp nhận | OPEN |

## Tài liệu điều kiện

| Document | Path | Trigger | Nếu chưa kích hoạt |
|---|---|---|---|
| API Specification | `docs/04-architecture/api-specification.md` | Có API public/internal cần contract | Ghi `NOT_APPLICABLE` kèm lý do |
| Database Design | `docs/04-architecture/database-design.md` | Có database/schema/persistence | Ghi `NOT_APPLICABLE` kèm lý do |
| Threat Model | `docs/04-architecture/threat-model.md` | Có dữ liệu, auth hoặc risk bảo mật đáng kể | Ghi `NOT_APPLICABLE` kèm lý do |
| Deployment Guide | `docs/09-operations/deployment-guide.md` | Có môi trường deploy | Ghi `NOT_APPLICABLE` kèm lý do |
| Monitoring | `docs/09-operations/monitoring.md` | Có service cần quan sát | Ghi `NOT_APPLICABLE` kèm lý do |
| Backup and Recovery | `docs/09-operations/backup-recovery.md` | Có dữ liệu cần khôi phục | Ghi `NOT_APPLICABLE` kèm lý do |
| Incident Response | `docs/09-operations/incident-response.md` | Có production/user impact | Ghi `NOT_APPLICABLE` kèm lý do |
| Release Runbook | `docs/09-operations/release-runbook.md` | Có release lặp lại | Ghi `NOT_APPLICABLE` kèm lý do |
| Migration Plan | `docs/09-operations/migration-plan.md` | Thay đổi dữ liệu/schema | Ghi `NOT_APPLICABLE` kèm lý do |
| UX Specification | `docs/03-requirements/ux-specification.md` | Có giao diện hoặc user flow | Ghi `NOT_APPLICABLE` kèm lý do |

## Quy tắc cập nhật

1. Mỗi dòng phải có path, trigger/ý nghĩa, status và next action đủ rõ để người khác tiếp tục.
2. `NOT_APPLICABLE` luôn đi cùng lý do cụ thể và điều kiện khiến nó trở thành `REQUIRED`; không dùng để che việc chưa làm.
3. Agent cập nhật registry trước khi triển khai tài liệu điều kiện. Nếu trigger phát sinh ngoài ROADMAP, tạo change request trước.
4. Registry phải phản ánh artifact thực tế; không tạo tài liệu chỉ để làm đầy cấu trúc.
5. Status của registry không thay thế status acceptance. `VERIFIED` trong một tài liệu không làm M/Phase thành `ACCEPTED`.
