# Document Registry

Registry là danh mục có kiểm soát của tài liệu và machine artifact trong project. Nó trả lời: artifact nào phải có, trigger nào kích hoạt artifact tùy chọn, source ownership nằm ở đâu và status hiện tại là gì. Registry không thay thế ROADMAP, SRS, Architecture hoặc evidence.

## Tài liệu nền bắt buộc

| Document | Path | Required | Purpose | Status | Owner/next action |
|---|---|---:|---|---|---|
| Project Intake | `docs/01-discovery/project-intake.md` | Yes | Ghi nhận ý tưởng, vấn đề, người dùng, ràng buộc và câu hỏi mở | DRAFT | Hoàn thiện trước ROADMAP |
| Project Charter | `docs/01-discovery/project-charter.md` | Yes | Chốt tầm nhìn, mục tiêu, phạm vi và tiêu chí thành công | DRAFT | Sinh từ intake đã làm rõ |
| Research Log | `docs/01-discovery/research.md` | Yes | Ghi câu hỏi chưa biết, nguồn, kết luận và độ tin cậy | DRAFT | Đóng hoặc chuyển RES ảnh hưởng cao |
| Assumptions | `docs/01-discovery/assumptions.md` | Yes | Theo dõi giả định chưa được chứng minh | OPEN | Liên kết research/decision |
| ROADMAP | `docs/02-roadmap/roadmap.md` | Yes | Nguồn sự thật về M, Phase, scope, dependency và thứ tự | IN_PROGRESS | CR-001/DEC-001 đã chấp thuận P0/P1 |
| Milestone Index | `docs/02-roadmap/milestone-index.md` | Yes | Chỉ mục M và trạng thái tóm tắt | IN_PROGRESS | Đồng bộ với ROADMAP/state |
| SRS | `docs/03-requirements/srs.md` | Yes | Requirement có ID, acceptance criteria và phạm vi M/Phase | IN_PROGRESS | Hoàn thiện P0 requirements |
| Traceability | `docs/03-requirements/requirements-traceability.md` | Yes | Nối requirement → task → test → evidence → commit/acceptance | IN_PROGRESS | Đồng bộ graph state |
| Acceptance Policy | `docs/03-requirements/acceptance-policy.md` | Yes | Phân biệt verification, checkpoint và acceptance | CURRENT | Gate không auto-accept |
| Architecture | `docs/04-architecture/architecture.md` | Yes | Boundary, state ownership, graph, validator và giới hạn thiết kế | IN_PROGRESS | Cập nhật P0 components |
| ADR index | `docs/04-architecture/adr/README.md` | Yes | Mẫu và chỉ mục quyết định kỹ thuật dài hạn | CURRENT | Tạo ADR khi decision dài hạn phát sinh |
| Environment Manifest | `docs/05-environment/environment-manifest.md` | Yes | Runtime, tool, service và command cần cho kiểm chứng | PARTIAL | Ghi Python standard library gate |
| Automation Contract | `docs/00-governance/automation-contract.md` | Yes | Source ownership, schema, gate result và profile invariants | IN_PROGRESS | Duy trì cùng state/schema |

## Machine-readable foundation

| Artifact | Path | Required | Purpose | Status |
|---|---|---:|---|---|
| Project State | `.newera/project-state.json` | Yes for P0 | Lifecycle, references, profile và traceability edges | IN_PROGRESS |
| Project State Schema | `.newera/schemas/project-state.schema.json` | Yes for P0 | Contract shape/version cho state | IN_PROGRESS |
| Evidence Envelope Schema | `.newera/schemas/evidence.schema.json` | Yes for P0 | Contract shape/version cho evidence máy đọc | IN_PROGRESS |
| Evidence State | `.newera/evidence/EVD-NEWERA-P0-001.json` | Yes for P0 | Verification envelope linked from state | VERIFIED |
| Governance Profiles | `.newera/governance-profiles.json` | Yes for STANDARD | Artifact/link requirements; LITE/STRICT là P1 contract | IN_PROGRESS |
| Governance Gate | `scripts/newera_validate.py` | Yes for P0 | Deterministic state/evidence/reference/profile validation | IN_PROGRESS |
| Change Diff | `scripts/newera_change.py` | P1 groundwork | Read-only requirement version diff for Change Control | PARTIAL |
| Impact Analysis | `scripts/newera_impact.py` | P1 groundwork | Downstream typed-edge impact projection | PARTIAL |
| Verification Matrix | `scripts/newera_matrix.py` | P1 groundwork | Requirement-to-test/evidence matrix projection | PARTIAL |
| Drift Detector | `scripts/newera_drift.py` | P1 groundwork | Deterministic ID/path scope check; semantic advisory only | PARTIAL |
| Invalid Gate Fixture | `.newera/fixtures/invalid-state.json` | Test-only | Chứng minh task thiếu requirement/evidence bị FAIL | CURRENT |

## Tài liệu hỗ trợ và chỉ mục

| Document | Path | Required | Purpose/trigger | Status |
|---|---|---:|---|---|
| README/GUIDE | `README.md`, `GUIDE.md` | Yes | Onboarding, quy trình và prompt library | CURRENT |
| Changelog | `CHANGELOG.md` | Yes | Lịch sử thay đổi đáng kể của kernel | CURRENT |
| Execution index | `docs/06-execution/README.md` | Yes | Cấu trúc, DoR/DoD và gate usage của M/Phase | IN_PROGRESS |
| Evidence index | `docs/07-evidence/README.md` | Yes | Quy ước evidence và canonical location | IN_PROGRESS |
| Evidence Schema Guide | `docs/07-evidence/evidence-schema.md` | Yes for P0 | Cách dùng Markdown + machine envelope | IN_PROGRESS |
| Baseline evidence | `docs/07-evidence/EVD-NEWERA-V01.md`, `EVD-NEWERA-DOCS-001.md` | Yes | Evidence lịch sử; không kéo dài cho P0 | VERIFIED/PARTIAL |
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

1. Mỗi dòng phải có path, trigger/ý nghĩa, source owner, status và next action đủ rõ để người khác tiếp tục.
2. Một machine field chỉ có một owner: state cho lifecycle/reference/edge; Markdown cho narrative/decision/context; gate FAIL khi consistency bị phá.
3. `NOT_APPLICABLE` luôn đi cùng lý do và trigger khiến nó thành `REQUIRED`.
4. Agent cập nhật registry trước khi triển khai artifact điều kiện hoặc thay đổi profile. Scope mới phải có CR.
5. Registry phải phản ánh artifact thực tế; không tạo tài liệu chỉ để làm đầy cấu trúc.
6. Status registry không thay thế acceptance status. Gate không được tự tạo `ACCEPTED`.
