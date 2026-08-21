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

## Environment and testing capability contract

Phần này sở hữu capability vocabulary canonical của NewEra. GUIDE, template, steering và skill có thể dùng view rút gọn hoặc field workflow, nhưng không được tạo capability layer mới hay ngụ ý mọi capability đều tự động hóa.

View rút gọn được phép dùng trong tài liệu hướng dẫn:

| View | Mapping canonical | Authority |
|---|---|---|
| Technical checks | static/quality, unit/component, integration, API/contract, UI/client và capability kỹ thuật liên quan | AI/operator theo test plan |
| Product criteria review | đối chiếu requirement/acceptance criteria và user outcome bằng capability phù hợp | AI hỗ trợ, human product judgment khi áp dụng |
| Human review | usability, visual intent, accessibility manual assessment, operational/product judgment khi cần | Human/role được chỉ định |
| Acceptance decision | quyết định cuối dựa trên evidence, checkpoint và product judgment | Acceptance authority |

NewEra yêu cầu project chuẩn bị **capability**, không yêu cầu một thương hiệu framework hoặc tool cụ thể. Project adopter chọn adapter/tool theo product type, M risk, requirement, acceptance criteria, environment, repeatability và evidence quality.

### M readiness pack

Trước M/Phase mutation, project cần có:

- M test capability profile: lớp kiểm chứng áp dụng và lý do lớp không áp dụng.
- Environment capability matrix: capability, required/conditional, owner, selected adapter/tool, version/constraint, setup và evidence.
- Human setup action list: account, access, secret/config, device, network, billing, approval hoặc dữ liệu mà AI không được tự cấp.
- Setup report và smoke/health result.
- Gate `ALLOW` hoặc `BLOCKED`; `PARTIAL` chỉ được allow khi limitation và phạm vi được phép đã ghi.

Environment readiness là gate trước mutation, không phải một status product mới và không phải acceptance. Nếu setup được dùng lại giữa Phase, chỉ cần ghi reference và delta khi capability/environment không đổi.

### Test capability layers

M có thể chọn các lớp sau theo risk và acceptance criteria:

- static/quality;
- unit/component;
- integration với dependency thật hoặc môi trường tương đương;
- API/contract;
- UI/client journey;
- accessibility/usability;
- visual behavior;
- performance/load;
- security/operations;
- human product review.

Mỗi lớp phải có selected adapter/tool ở project adopter, expected/actual, command hoặc kịch bản tái chạy, environment reference và evidence. Agent interaction hoặc interactive diagnostic tool có thể hỗ trợ khám phá/debug; regression verification phải có cách chạy lặp lại phù hợp với project.

Không coi `tool selected` là bằng chứng đạt. Gate/check chỉ báo technical result; acceptance vẫn theo acceptance policy.

| Nội dung | Owner mặc định | Vai trò của Markdown |
|---|---|---|
| M/Phase/scope/order | `docs/02-roadmap/roadmap.md` của project | Narrative và review |
| Lifecycle/reference/typed edges | Machine state của project nếu project bật structured mode | Projection, không tạo sự thật thứ hai |
| Requirement meaning/criteria | SRS của project | Detailed contract |
| Verification metadata/result | Evidence envelope của project | Context và interpretation |
| Acceptance decision | Acceptance policy + Decision Log của project | Human decision record |

Nếu project không bật structured mode, Markdown và Git vẫn là nguồn chính theo registry của project. Không tạo `.newera/` hoặc machine state chỉ để làm đầy cấu trúc.

## Enforcement levels and adapter boundary

Kernel NewEra định nghĩa process contract và có thể cung cấp runtime reminder dạng advisory; prose hoặc hook `askAgent` không được mặc định xem là conformance gate có khả năng block. Project adopter chọn enforcement level phù hợp:

| Level | Cơ chế | Owner | Ý nghĩa |
|---|---|---|---|
| `L0_ADVISORY` | AGENTS, governance, steering, skills và human review | Kernel/adopter | Agent được hướng dẫn và reviewer được nhắc; không có machine block |
| `L1_RUNTIME` | Workspace hook hoặc tool-event adapter | Adopter runtime | Event được chọn có thể warn hoặc block theo contract của Kiro/harness đang cài |
| `L2_VALIDATOR` | Validator deterministic cho link/ID/status/evidence | Adopter project hoặc adapter đã khai báo | Invariant máy kiểm được đánh giá bằng exit status và report |
| `L3_CI_GATE` | CI/release policy gọi validator | Adopter project | Merge/release bị chặn khi conformance check bắt buộc fail |

Kernel phải dùng được ở `L0_ADVISORY`. Adopter cần enforcement phải ghi level, validator/profile, event schema được hỗ trợ và human exception path trong registry/ROADMAP của project. Validator không được tạo source of truth thứ hai hoặc quyết định product acceptance; nó chỉ có thể block record không hợp lệ và báo evidence/authority còn thiếu.

Các check có thể tự động hóa gồm local link/resource, placeholder ID trước `READY`, orphan requirement, status transition, field bắt buộc của `ACCEPTED`, tính nhất quán `NOT_RUN`/`VERIFIED` và lý do `NOT_APPLICABLE`. Script/tool cụ thể thuộc adopter hoặc adapter đã khai báo, không thuộc product-specific kernel baseline.

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
