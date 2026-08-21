# Automation Contract Guide

NewEra có thể được áp dụng với tài liệu Markdown thuần hoặc kết hợp machine-readable state/evidence tùy theo nhu cầu của project sử dụng. File này mô tả nguyên tắc, không phải state của repository NewEra.

## Process entry contract

Mọi user request đi vào một process preflight trước khi agent thực hiện mutation. Đây là lớp ràng buộc nhẹ, không thay thế workflow hiện tại và không yêu cầu tạo cả bộ tài liệu cho một thay đổi nhỏ.

### Request routes

| Route | Dùng cho | Tối thiểu trước mutation | Đầu ra tối thiểu |
|---|---|---|---|
| `READ_ONLY` | Đọc, giải thích, status query, research chưa sửa artifact | Không mutation | Câu trả lời hoặc research handoff nếu có |
| `MICRO_CHANGE` | Sửa cục bộ, không đổi requirement/acceptance/API/data/security/deployment/architecture | Request/task binding, path boundary, scope check, targeted verification | Task note, evidence ngắn, trạng thái kỹ thuật |
| `NORMAL_OR_SCOPE_CHANGE` | Task Phase bình thường hoặc thay đổi scope/design | ROADMAP, requirement/task; CR/decision trước nếu ngoài scope | Workflow Phase hiện tại hoặc CR → decision → task |

Preflight tối thiểu ghi rõ: request type, project/repository, M/Phase hoặc task binding, scope route, planned files/boundary, expected output, verification plan, gate `ALLOW`/`BLOCKED` và blocker/next action nếu có. Preflight có thể nằm trong `task.md` hoặc adapter của project adopter; không tạo request state cho NewEra kernel.

### Micro-change rule

`MICRO_CHANGE` chỉ giảm ceremony. Nếu project đã có `task.md`, ghi vào task đó; không tạo SRS, Architecture hoặc Phase report mới chỉ vì một sửa đổi nhỏ. Tuy nhiên vẫn phải kiểm tra không có scope/design change, chạy check phù hợp, ghi evidence và giữ traceability. Nếu phát sinh requirement, acceptance, API, data, security, deployment hoặc architecture change thì chuyển ngay sang `NORMAL_OR_SCOPE_CHANGE` và change control.

## Source ownership

| Nội dung | Owner mặc định | Vai trò của Markdown |
|---|---|---|
| M/Phase/scope/order | `docs/02-roadmap/roadmap.md` của project | Narrative và review |
| Lifecycle/reference/typed edges | Machine state của project nếu project bật structured mode | Projection, không tạo sự thật thứ hai |
| Requirement meaning/criteria | SRS của project | Detailed contract |
| Verification metadata/result | Evidence envelope của project | Context và interpretation |
| Acceptance decision | Acceptance policy + Decision Log của project | Human decision record |

Nếu project không bật structured mode, Markdown và Git vẫn là nguồn chính theo registry của project. Không tạo `.newera/` hoặc machine state chỉ để làm đầy cấu trúc.

## Optional structured mode

Structured mode chỉ được kích hoạt khi project có nhu cầu rõ ràng và đã ghi trong registry/ROADMAP của project. Khi bật, project nên có:

```text
<project>/.newera/project-state.json
<project>/.newera/schemas/
<project>/.newera/evidence/
```

Schema, validator, profile và script tích hợp phải thuộc project sử dụng NewEra hoặc một adapter được khai báo; không đặt runtime implementation vào kernel chỉ vì kernel mô tả contract.

## Invariants

- ROADMAP vẫn sở hữu M/Phase/scope/order.
- Status và acceptance phải tuân thủ `docs/00-governance/status-model.md` và `docs/03-requirements/acceptance-policy.md`.
- Gate/check chỉ báo technical result; không tự tạo acceptance.
- Reference phải resolve hoặc được ghi rõ là external/OPEN/BLOCKED.
- Machine projection không được tạo nguồn sự thật kép với Markdown.
- Semantic/advisory automation không được tự chuyển status hoặc scope.

## Khi project cần automation

1. Ghi nhu cầu và phạm vi trong project registry/ROADMAP.
2. Chọn schema/profile phù hợp hoặc tạo adapter trong project.
3. Tạo test/evidence cho adapter.
4. Giữ NewEra kernel ở vai trò template và guidance.
