# Automation Contract Guide

NewEra có thể được áp dụng với tài liệu Markdown thuần hoặc kết hợp machine-readable state/evidence tùy theo nhu cầu của project sử dụng. File này mô tả nguyên tắc, không phải state của repository NewEra.

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
