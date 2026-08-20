# Architecture

Tài liệu mô tả kiến trúc của NewEra v0.1 ở mức kernel quy trình. NewEra không phải ứng dụng nghiệp vụ có runtime; vì vậy kiến trúc hiện tại chủ yếu là cấu trúc tài liệu và các điểm tích hợp Kiro. Khi một project sản phẩm dùng kernel này, Architecture phải được mở rộng trong phạm vi project đó, không bịa công nghệ vào baseline.

## 1. Context và boundary

**Mục đích:** cung cấp một quy trình từ intake → roadmap → requirements/architecture → execution → verification → checkpoint → acceptance, có traceability và lịch sử quyết định.

**Nằm trong kernel:** governance (`AGENTS.md`, steering), discovery, roadmap, requirements, architecture record, environment record, templates, prompts, agents/skills/hooks và evidence/report conventions.

**Nằm ngoài kernel:** quyền thực thi/an toàn của model hoặc Kiro, thông tin nghiệp vụ của project sử dụng NewEra, credential/secret, production deployment và công nghệ runtime cụ thể của từng project.

**Nguồn sự thật:** ROADMAP quyết định M/Phase/scope/thứ tự; SRS quyết định requirement; Architecture quyết định boundary/design; registry quyết định tài liệu điều kiện; evidence chỉ chứng minh verification; acceptance policy quyết định cách nghiệm thu.

## 2. Quality attributes

| ID | Thuộc tính | Cách bảo vệ | Trạng thái |
|---|---|---|---|
| NFR-NEWERA-001 | Traceability | ID ổn định, registry, traceability matrix, evidence và report | DRAFT |
| NFR-NEWERA-002 | Auditability | Decision Log, Change Control, Git history và không xóa residual | DRAFT |
| NFR-NEWERA-003 | Technology neutrality | Không chốt runtime/service trong kernel; dùng registry điều kiện | DRAFT |
| NFR-NEWERA-004 | Honest status | Tách `VERIFIED`, `CHECKPOINT_PENDING`, `ACCEPTED`; ghi OPEN/BLOCKED | DRAFT |
| NFR-NEWERA-005 | Operability | GUIDE, skills, prompts, templates và hooks có đường dẫn rõ | DRAFT |

Các NFR trên mô tả ý định của kernel, chưa phải acceptance của một project sản phẩm.

## 3. Thành phần

| Component | Trách nhiệm | Giao tiếp/nguồn vào | Trạng thái |
|---|---|---|---|
| C-001 Governance | Luật bắt buộc, status, Git và change/decision control | `AGENTS.md`, `docs/00-governance/`, steering | PROPOSED |
| C-002 Discovery | Thu thập bối cảnh, scope ban đầu, assumptions và research | Người dùng, intake templates | PROPOSED |
| C-003 Planning | M/Phase/dependency/scope và roadmap index | Discovery, SRS, change control | PROPOSED |
| C-004 Product definition | Requirements, acceptance policy, traceability | Intake, roadmap, architecture | PROPOSED |
| C-005 Technical context | Boundary, quality attributes, ADR và environment | Requirements, registry, project facts | PROPOSED |
| C-006 Execution records | Brief, requirements, task, test-plan, checkpoint, report | Roadmap và templates | PROPOSED |
| C-007 Verification/reporting | Chạy check, tạo evidence, tổng hợp residual/debt | Test plan, Git, environment | PROPOSED |
| C-008 Kiro integration | Steering, agents, skills, prompts và hooks | Workspace events và user invocation | PROPOSED |

Trạng thái `PROPOSED` ở đây mô tả thành phần kiến trúc kernel; không phải trạng thái acceptance của artifact bên trong.

## 4. Luồng điều khiển và dữ liệu

```text
Người dùng/ý tưởng
  -> Discovery: intake, charter, assumptions, research
  -> Registry + ROADMAP: xác định tài liệu, M, Phase và dependency
  -> SRS + Architecture + Environment: định nghĩa contract và giới hạn
  -> Execution: requirements -> task -> implementation -> test
  -> Verification: static/test/product checks -> evidence
  -> Checkpoint: checkpoint + report + residual/debt
  -> Người có thẩm quyền: ACCEPTED | REJECTED | DEFERRED
  -> Decision Log/ROADMAP/traceability được cập nhật
```

Luồng dữ liệu chính là artifact Markdown/JSON trong repository. Git là lịch sử thay đổi; không có database/service nào được giả định cho kernel. Hooks có thể nhắc hoặc kích hoạt review nhưng không thay thế quyết định của người dùng.

## 5. Dữ liệu và lưu trữ

- Artifact dạng Markdown là nguồn đọc chính; JSON hooks phải parse được theo schema workspace.
- ID, status, path, commit và ngày là metadata cần giữ để truy nguyên.
- Không lưu secret, token, mật khẩu hoặc PII thật trong repository.
- Chỉ tạo tài liệu database riêng khi registry có trigger database/schema/persistence. Hiện baseline không có database.
- Khi project con có dữ liệu thật, phải bổ sung retention, backup/recovery và migration theo registry.

## 6. Bảo mật và quan sát

- **Authentication/Authorization:** không thuộc kernel; quyền model/Kiro và quyền repository do môi trường cung cấp.
- **Secret handling:** chỉ dùng placeholder hoặc tên biến; secret đặt ở secret manager/.env ngoài Git.
- **Change audit:** Git diff/log, Change Control, Decision Log, evidence và report.
- **Logging/Monitoring:** kernel không có service runtime; project con tự kích hoạt tài liệu operations khi có trigger.
- **Backup/recovery:** không áp dụng cho baseline không có dữ liệu runtime; ghi lý do trong registry nếu project không có dữ liệu.

## 7. Triển khai

Baseline được vận hành như một repository workspace: người dùng mở project trong Kiro, đọc `GUIDE.md`/`AGENTS.md`, gọi skill/prompt phù hợp và lưu artifact vào các thư mục chuẩn. Không yêu cầu server, package manager, container hay cloud service cho kernel hiện tại. Mọi project con có runtime phải mô tả deployment riêng sau khi registry kích hoạt.

## 8. ADR index

Các quyết định kỹ thuật có ảnh hưởng dài hạn đặt trong `docs/04-architecture/adr/` và liên kết từ Decision Log. ADR phải nêu bối cảnh, phương án, quyết định, lý do, ảnh hưởng và trạng thái; không dùng ADR để thay đổi ROADMAP mà không có change control.

## 9. Giới hạn và phương án bị loại

- Không đưa một framework/runtime cụ thể vào kernel chỉ để làm tài liệu có vẻ đầy đủ.
- Không tạo M/Phase giả hoặc gắn test/evidence vào placeholder.
- Không nhúng autonomy policy hoặc thay thế chính sách an toàn của Kiro/model.
- Không coi hook chạy thành công là nghiệm thu sản phẩm.
- Project-specific architecture vẫn `OPEN` cho tới khi intake và SRS cung cấp dữ liệu; đây là giới hạn có chủ ý, không phải thiếu sót cần che giấu.
