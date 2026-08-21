# Environment Manifest

Environment Manifest là contract về **năng lực môi trường** của project adopter, không phải danh sách công cụ cố định của NewEra. Đây là reference template; adopter tạo bản sở hữu và pin version/source theo `docs/00-governance/ADOPTION.md`. Project adopter chọn runtime, framework, service, adapter và tool phù hợp với sản phẩm; kernel chỉ yêu cầu capability, owner, setup, evidence và blocking condition.

## Document control

- Document status: DRAFT
- Owner/role: `<OWNER>`
- Kernel release: `NEWERA_VERSION`
- Kernel source commit: `SOURCE_COMMIT`
- Project registry reference: `<REGISTRY-REF>`
## Runtime and capability matrix

| ID | Capability | Required | Owner | Selected adapter/tool | Version/constraint | Detection/setup | Required evidence | Blocking condition |
|---|---|---:|---|---|---|---|---|---|
| ENV-CAP-<CAP-ID> | Source control/workspace | Yes | AI/Human | Project-selected | | | Repository/access check | Không đọc/ghi được workspace |
| ENV-CAP-<CAP-ID> | Runtime execution | Yes | AI/Human | Project-selected | | | Version/output | Runtime thiếu hoặc không tương thích |
| ENV-CAP-<CAP-ID> | Dependency/package | Yes | AI | Project-selected | Lockfile/constraint | | Install/smoke result | Dependency không cài hoặc resolve được |
| ENV-CAP-<CAP-ID> | Application/service execution | Conditional | AI/Human | Project-selected | | | Service health/smoke | Service bắt buộc không chạy được |
| ENV-CAP-<CAP-ID> | Data/integration dependency | Conditional | AI/Human | Project-selected | | | Connection/schema/fixture result | Dependency cần cho M không truy cập được |
| ENV-CAP-<CAP-ID> | UI/client interaction | Conditional | AI/Human | Project-selected | | | Journey/interaction evidence | Critical user journey không tái hiện được |
| ENV-CAP-<CAP-ID> | Test execution | Yes | AI | Project-selected | | | Test command/report | Không có cách chạy test liên quan |
| ENV-CAP-<CAP-ID> | Diagnostics/observability | Conditional | AI | Project-selected | | | Log/trace/metric evidence | Không điều tra được failure quan trọng |
| ENV-CAP-<CAP-ID> | Deployment/operations | Conditional | Human/AI | Project-selected | | | Deploy/rollback/health evidence | M yêu cầu deployment nhưng thiếu quyền hoặc target |

`Selected adapter/tool` là giá trị của project adopter, không phải quy định của NewEra. Có thể là framework, CLI, MCP server, emulator, service, device hoặc quy trình manual phù hợp. Không thêm capability nếu project không cần; đánh dấu `NOT_APPLICABLE` kèm lý do và trigger.

## M test capability profile

Mỗi M phải chọn các capability và lớp kiểm chứng áp dụng trước khi chuyển sang `READY`:

| Capability/test layer | Applies | M/Phase | Expected outcome/evidence | Selected adapter/tool | Owner |
|---|---:|---|---|---|---|
| Static/quality | Yes/No | | | | |
| Unit/component | Yes/No | | | | |
| Integration/real dependency | Yes/No | | | | |
| API/contract | Yes/No | | | | |
| UI/client journey | Yes/No | | | | |
| Accessibility/usability | Yes/No | | | | |
| Visual behavior | Yes/No | | | | |
| Performance/load | Yes/No | | | | |
| Security/operations | Yes/No | | | | |

Không phải M nào cũng chạy toàn bộ lớp. Lựa chọn phải truy về requirement, risk, acceptance criteria và boundary của M. `No` hoặc `NOT_APPLICABLE` phải có lý do.

## Human/AI setup boundary

### AI có thể tự xử lý khi được phép

- Phát hiện version và capability hiện có.
- Cài dependency theo lockfile hoặc project instruction.
- Khởi động dependency local/test được phép.
- Tạo local config từ example, không chứa secret.
- Chạy setup check, smoke test và thu thập evidence.
- Đề xuất adapter/tool phù hợp với capability.

### Cần con người hoặc quyền ngoài agent

- Cài software cấp hệ thống hoặc cấp quyền administrator.
- Tạo account, cấp permission, billing hoặc cloud resource.
- Cấp secret/API key qua secret manager hoặc environment an toàn.
- Cấp thiết bị thật, device lab, VPN hoặc network đặc biệt.
- Phê duyệt dữ liệu thật, production-like data, legal/security/compliance.
- Quyết định dùng service có chi phí hoặc rủi ro vận hành.

AI phải tạo danh sách human action ngắn, có owner, lý do, quyền cần cấp và điều kiện hoàn tất; không tự giả định đã được cấp.

## M readiness gate

Trước mutation đầu tiên của M/Phase:

- Capability matrix liên quan đã có owner và selected adapter/tool hoặc lý do `NOT_APPLICABLE`.
- Required capability không còn `Unknown`/`OPEN` mà chưa có action.
- Setup report đã ghi kết quả thực tế và smoke test.
- Blocker môi trường có `ENV-ISSUE`, `ENV-DEP`, `BLOCKER` hoặc `ACTION` phù hợp.
- Gate được ghi là `ALLOW` hoặc `BLOCKED`.

Setup result dùng `VERIFIED | PARTIAL | BLOCKED`; environment gate dùng `ALLOW | BLOCKED`, không tạo status mới. `PARTIAL` chỉ được `ALLOW` nếu limitation không ảnh hưởng phạm vi đang làm và đã ghi trong task/evidence.

## Services and configuration

- Required services:
- Conditional services:
- External systems/actors:
- Data/fixture/seed requirement:
- Secret/config boundary:
- Access/network/VPN/device prerequisite:
- Human decision or approval:

## Commands

```text
Detect/version: project-selected command
Setup/install: project-selected command
Smoke/health: project-selected command
Test: project-selected command
Build: project-selected command
Run/deploy: project-selected command
```

Commands phải được project adopter điền và kiểm chứng; không ghi secret. Nếu setup command khác manifest hoặc cần quyền ngoài agent, ghi lý do và human action.

## Re-check triggers

Chạy lại capability/setup check khi có:

- M mới với capability khác;
- thay đổi runtime, dependency, service, data hoặc deployment;
- thay đổi test adapter/tool/version;
- thay đổi access/secret/network/device;
- failure không tái hiện được hoặc kết quả môi trường không còn tin cậy.

Environment Manifest là contract; kết quả thực tế, issue và action ghi trong `setup-report.md`.
