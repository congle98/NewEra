# Document Registry

Registry là khung hướng dẫn để **project sử dụng NewEra** quyết định tài liệu nào bắt buộc, có điều kiện hoặc không áp dụng. Các trạng thái trong bảng là trạng thái khởi tạo/template; không phải trạng thái của repository NewEra.

## Registry và canonical ownership

| Document/concern | Canonical path | Required | Ownership |
|---|---|---:|---|
| Kernel overview | `docs/00-governance/README.md` | Yes | NewEra kernel boundary and navigation |
| Kernel guide | `docs/00-governance/GUIDE.md` | Yes | NewEra kernel workflow and prompt index |
| Kernel changelog | `docs/00-governance/CHANGELOG.md` | Yes | NewEra kernel release history; not adopter product history |
| Project README/changelog | Adopter project workspace | Per project | Product/project documentation and release history; never kernel state |
| Governance baseline | `docs/00-governance/` | Yes | Status, git, change, decision và registry policy |
| Project Intake | `docs/01-discovery/project-intake.md` | Yes | Ý tưởng, bối cảnh và câu trả lời intake |
| Project Charter | `docs/01-discovery/project-charter.md` | Yes | Vision, objective, scope, stakeholder và success/exit |
| Assumptions | `docs/01-discovery/assumptions.md` | Yes | Assumption ledger; charter chỉ link tới đây |
| Research log | `docs/01-discovery/research.md` | Yes | Index/rules; chi tiết từng item dùng `docs/templates/research-item.md` |
| ROADMAP | `docs/02-roadmap/roadmap.md` | Yes | Nguồn sự thật duy nhất về M/Phase/scope/order và milestone index |
| Milestone brief | `docs/templates/milestone-brief.md` | Per M | Hồ sơ chuẩn bị một M |
| SRS | `docs/03-requirements/srs.md` | Yes | Requirement, acceptance criteria và traceability tổng thể |
| Phase requirements | `docs/templates/requirements.md` | Per Phase | Requirement/acceptance slice của Phase |
| Acceptance Policy | `docs/03-requirements/acceptance-policy.md` | Yes | Quy trình verification/checkpoint/acceptance |
| Architecture | `docs/04-architecture/architecture.md` | Yes | Boundary, data flow và solution design |
| Environment Manifest | `docs/05-environment/environment-manifest.md` | Yes | Tool/runtime/service và setup procedure |
| Setup Report | `docs/05-environment/setup-report.md` | Per M/Phase | Kết quả setup thực tế, issue và action |
| M/Phase execution | `docs/06-execution/<M>/` | Per M/Phase | Brief, Phase requirements, consolidated `task.md`, report |
| Evidence guide/schema | `docs/07-evidence/README.md` | Per verification | Evidence contract; evidence mặc định nằm trong `task.md` |
| Reports/ledgers | `docs/08-reports/` | Per project | Phase/M report, residual và technical debt |
| Operations | `docs/09-operations/` | Conditional | Deployment, monitoring, backup, incident, release; `NOT_APPLICABLE` chỉ khi project không có runtime/service/deployment boundary và lý do được ghi |

## Source ownership rules

- ROADMAP sở hữu M/Phase/scope/order; milestone index chỉ là section trong ROADMAP, không tạo file index song song.
- SRS sở hữu product requirement, acceptance criteria và traceability cấp SRS; không tạo file traceability riêng.
- `task.md` sở hữu task, test plan, verification evidence và checkpoint của Phase.
- `report.md` sở hữu Phase summary; milestone report sở hữu M summary.
- `docs/07-evidence/README.md` sở hữu evidence schema/policy; evidence mặc định được ghi trong `task.md`.
- `environment-manifest.md` sở hữu prerequisite/setup command; `setup-report.md` chỉ ghi kết quả thực tế.
- `status-model.md` là status dictionary; `acceptance-policy.md` là transition/authority policy.
- `change-control.md`, `decision-log.md` và ADR là ba lifecycle khác nhau; không dùng một file thay cho file khác.

## Templates và runtime guidance

- `docs/templates/` chứa template; không điền dữ liệu project vào kernel.
- `docs/00-governance/GUIDE.md` là kernel workflow và prompt index; `docs/prompts/README.md` là prompt source canonical duy nhất.
- `.kiro/steering/`, `.kiro/skills/` và `.kiro/agents/` chỉ giữ instruction runtime-specific và dẫn về canonical docs.
- Machine state/evidence là optional contract; chỉ bật khi registry của project ghi rõ nhu cầu.

## Quy tắc

1. Agent phải cập nhật registry của project khi tài liệu điều kiện trở thành cần thiết.
2. Không tạo tài liệu chỉ để làm đầy cấu trúc hoặc để tự chứng minh NewEra đã chạy.
3. `NOT_APPLICABLE` luôn đi cùng lý do và trigger khiến tài liệu trở thành `REQUIRED`.
4. Project-specific status, IDs, reports, evidence và acceptance không được ghi vào kernel.
5. Khi merge/xóa một canonical document, cập nhật mọi link, prompt, skill, registry và README trong cùng thay đổi.
