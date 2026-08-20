# Document Registry

Registry là khung hướng dẫn để **project sử dụng NewEra** quyết định tài liệu nào bắt buộc, có điều kiện hoặc không áp dụng. Các trạng thái trong bảng là trạng thái khởi tạo/template; không phải trạng thái của repository NewEra.

| Document | Path/template | Required | Purpose | Initial status |
|---|---|---:|---|---|
| Project Intake | `docs/01-discovery/project-intake.md` | Yes | Ghi nhận ý tưởng và bối cảnh | DRAFT |
| Project Charter | `docs/01-discovery/project-charter.md` | Yes | Mục tiêu và phạm vi | DRAFT |
| Research | `docs/01-discovery/research.md` | Yes | Vấn đề cần tìm hiểu và nguồn | DRAFT |
| Assumptions | `docs/01-discovery/assumptions.md` | Yes | Giả định chưa được chứng minh | OPEN |
| ROADMAP | `docs/02-roadmap/roadmap.md` | Yes | Nguồn sự thật về M/Phase/scope/order | DRAFT |
| Milestone Index | `docs/02-roadmap/milestone-index.md` | Yes | Chỉ mục M và readiness | DRAFT |
| SRS | `docs/03-requirements/srs.md` | Yes | Yêu cầu và acceptance criteria | DRAFT |
| Traceability | `docs/03-requirements/requirements-traceability.md` | Yes | Requirement → task → test → evidence | DRAFT |
| Acceptance Policy | `docs/03-requirements/acceptance-policy.md` | Yes | Tách verification/checkpoint/acceptance | CURRENT |
| Architecture | `docs/04-architecture/architecture.md` | Yes | Boundary, data flow và quyết định kỹ thuật | DRAFT |
| Environment Manifest | `docs/05-environment/environment-manifest.md` | Yes | Tool/runtime/service cần kiểm chứng | DRAFT |
| Setup Report | `docs/05-environment/setup-report.md` | Per M/Phase | Kết quả kiểm tra môi trường | NOT_STARTED |
| M/Phase artifacts | `docs/06-execution/<M>/` | Per M/Phase | Brief, requirements, task, test-plan, checkpoint, report | NOT_STARTED |
| Evidence | `docs/07-evidence/` | Per verification | Bằng chứng kiểm chứng kỹ thuật | NOT_STARTED |
| Reports/ledgers | `docs/08-reports/` | Per project | Report, residual và technical debt | NOT_STARTED |
| Operations | `docs/09-operations/` | Conditional | Deployment, monitoring, backup, incident, release | NOT_APPLICABLE |

## Templates

- `docs/templates/` chứa template; không điền dữ liệu project vào kernel.
- `docs/prompts/` và `.kiro/skills/` hướng dẫn cách tạo bản project-specific sau khi project được khởi tạo.
- Machine state/evidence là optional contract; chỉ bật khi registry của project ghi rõ nhu cầu.

## Quy tắc

1. Agent phải cập nhật registry của project khi tài liệu điều kiện trở thành cần thiết.
2. Không tạo tài liệu chỉ để làm đầy cấu trúc hoặc để tự chứng minh NewEra đã chạy.
3. `NOT_APPLICABLE` luôn đi cùng lý do và trigger khiến tài liệu trở thành `REQUIRED`.
4. Project-specific status, IDs, reports, evidence và acceptance không được ghi vào kernel.
