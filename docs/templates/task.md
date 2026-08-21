# <M-ID>-<P-ID> - Task, Test, Evidence và Checkpoint

- Phase:
- Requirement scope:
- Owner/role:
- Trạng thái: DRAFT
- Task tier: ghi `MICRO`, `STANDARD` hoặc `HIGH` cho từng task trong bảng.
- Required profile: dùng đúng các section tối thiểu theo tier; tăng tier khi risk/scope thay đổi.

Template này gom toàn bộ công việc thực thi và kiểm chứng của một Phase vào một file. `requirements.md` giữ requirement/acceptance criteria; `report.md` giữ tổng kết sau Phase.

## 0. Process preflight

Mỗi mutation request phải ghi một preflight ngắn trước khi sửa:

- Request type:
- Route: `READ_ONLY` | `MICRO_CHANGE` | `NORMAL_OR_SCOPE_CHANGE`
- Project/repository:
- ROADMAP/M/Phase/task hoặc CR binding:
- Scope boundary / planned files:
- Expected output:
- Verification plan:
- Gate: `ALLOW` | `BLOCKED`
- Blocker/next action:

Với `MICRO_CHANGE`, có thể bỏ qua full foundation/Phase report khi không ảnh hưởng requirement, acceptance, API, data, security, deployment hoặc architecture. Không được bỏ task/request binding, path scope, targeted verification hoặc evidence ngắn. Nếu phát sinh thay đổi ngoài boundary, chuyển route và tạo CR nếu cần.

## 1. Definition of Ready cho task

Task chỉ được `READY` khi có một output kiểm tra được, dependency rõ, requirement/acceptance criteria liên quan, cách kiểm chứng và biết tài liệu nào sẽ cập nhật. Task thiếu dữ liệu quan trọng phải là `BLOCKED` hoặc `OPEN`, không giả định.

## 2. Task list

| ID | Tier | Mô tả | Requirement | Dependency | Output/changed artifact | Verification | Status |
|---|---|---|---|---|---|---|---|
| `TASK-<M-ID>-<P-ID>-<TASK-DEP-ID>` | STANDARD | Kiểm tra dependency | REQ-<REQ-ID> | — | Dependency/status note | TEST-<TEST-ID> | DRAFT |
| `TASK-<M-ID>-<P-ID>-<TASK-IMPL-ID>` | STANDARD | Triển khai phần chính | REQ-<REQ-ID> | `TASK-<M-ID>-<P-ID>-<TASK-DEP-ID>` | Code/config/documentation | TEST-<TEST-ID> | DRAFT |
| `TASK-<M-ID>-<P-ID>-<TASK-TEST-ID>` | STANDARD | Viết/cập nhật test | REQ-<REQ-ID> | `TASK-<M-ID>-<P-ID>-<TASK-IMPL-ID>` | Test artifact | TEST-<TEST-ID> | DRAFT |
| `TASK-<M-ID>-<P-ID>-<TASK-DOC-ID>` | STANDARD | Cập nhật tài liệu và traceability | REQ-<REQ-ID> | `TASK-<M-ID>-<P-ID>-<TASK-IMPL-ID>` / `TASK-<M-ID>-<P-ID>-<TASK-TEST-ID>` | Docs/traceability | TEST-<TEST-ID> | DRAFT |
| `TASK-<M-ID>-<P-ID>-<TASK-VERIFY-ID>` | HIGH | Chạy verification | REQ-<REQ-ID> | `TASK-<M-ID>-<P-ID>-<TASK-DEP-ID>` .. `TASK-<M-ID>-<P-ID>-<TASK-DOC-ID>` | Verification result | TEST-<TEST-ID> | DRAFT |
| `TASK-<M-ID>-<P-ID>-<TASK-EVIDENCE-ID>` | HIGH | Hoàn thiện evidence và checkpoint | REQ-<REQ-ID> | `TASK-<M-ID>-<P-ID>-<TASK-VERIFY-ID>` | Evidence/checkpoint record | Review | DRAFT |

### Tiered completion profile

Mọi task phải có các điều kiện tối thiểu sau:

- [ ] Có requirement/request binding, owner, path/scope boundary và output kiểm tra được.
- [ ] Dependency, blocker và status hiện tại đã được ghi.
- [ ] Artifact/output đã được cập nhật trong phạm vi.
- [ ] Verification result và residual/blocker/limitation đã được ghi đúng scope.

#### `MICRO` tier

Dùng khi preflight chọn `MICRO_CHANGE` và không đổi requirement, acceptance, API, data, security, deployment hoặc architecture.

- [ ] Có targeted verification.
- [ ] Có evidence ngắn: expected, actual, command/kịch bản, limitation và worktree/commit reference.
- [ ] Không tạo full Phase report/checkpoint chỉ vì thay đổi nhỏ.

#### `STANDARD` tier

Dùng cho task Phase thông thường hoặc task có nhiều artifact liên quan.

- [ ] Requirement/acceptance criteria và dependency đã map.
- [ ] Test/verification plan đã cập nhật.
- [ ] Evidence có environment, command/kịch bản tái chạy, expected, actual, artifact và limitation.
- [ ] Traceability nối requirement → task → test → evidence.
- [ ] Tài liệu bị ảnh hưởng, residual/risk/blocker và reviewer condition đã cập nhật.

#### `HIGH` tier

Dùng khi task có risk cao, security/data/deployment/architecture impact, external dependency quan trọng hoặc human/product review bắt buộc.

- [ ] M readiness pack và environment gate đã được kiểm tra.
- [ ] Capability profile đầy đủ, gồm lớp áp dụng và lý do `NOT_APPLICABLE`.
- [ ] Evidence/reproducibility và human-only action đã có owner.
- [ ] Checkpoint/reviewer/decision handoff đã được chuẩn bị.
- [ ] CR/DEC/ADR được liên kết nếu có scope/design impact.

Không đánh dấu task `VERIFIED` chỉ vì checklist đã tick; phải có output và evidence tương ứng. Khi risk/scope tăng, chuyển tier và ghi lý do.

**Task completion note:**

- Output thực tế:
- Files/artifacts:
- Verification IDs:
- Residual/blocker/risk:
- Ghi chú reviewer:

## 3. Test capability profile

Dùng vocabulary capability và gate canonical trong `docs/00-governance/automation-contract.md`; section này chỉ ghi lựa chọn của project/task, không tạo policy mới.

- M/Phase capability profile reference:
- Environment Manifest/Setup Report reference:
- Environment gate: `ALLOW` | `BLOCKED`
- Applied verification layers: static/quality | unit/component | integration | API/contract | UI/client journey | accessibility/usability | visual | performance/load | security/operations | human review
- Not applicable layers and reason:
- Selected adapters/tools and versions: project-specific; do not assume a NewEra default.
- Human setup actions/blockers:

Mỗi lớp được chọn phải có requirement/acceptance mapping, expected result, command/kịch bản tái chạy, environment reference và evidence. Interactive agent tooling có thể hỗ trợ khám phá/debug; kết luận verification cần artifact và cách chạy lặp lại phù hợp với project.

## 4. Test plan và verification matrix

- Requirement scope:
- Owner/agent:
- Environment reference: `docs/05-environment/environment-manifest.md`
- Trạng thái: DRAFT

| ID | Loại | Requirement/criteria | Lệnh/kịch bản | Kết quả mong đợi | Kết quả thực tế | Artifact/output | Status |
|---|---|---|---|---|---|---|---|
| `TEST-<M-ID>-<P-ID>-<TEST-STATIC-ID>` | Static/format | REQ-<REQ-ID>/AC-<AC-ID> | Chưa xác định | Không lỗi | | | NOT_RUN |
| `TEST-<M-ID>-<P-ID>-<TEST-UNIT-ID>` | Unit/integration | REQ-<REQ-ID>/AC-<AC-ID> | Chưa xác định | Pass | | | NOT_RUN |
| `TEST-<M-ID>-<P-ID>-<TEST-BUILD-ID>` | Build/lint/type | REQ-<REQ-ID>/AC-<AC-ID> | Chưa xác định hoặc N/A | Pass hoặc lý do N/A | | | NOT_RUN |
| `TEST-<M-ID>-<P-ID>-<TEST-PRODUCT-ID>` | Product/acceptance mapping | REQ-<REQ-ID>/AC-<AC-ID> | Đối chiếu từng criteria | Có evidence tương ứng | | | NOT_RUN |
| `TEST-<M-ID>-<P-ID>-<TEST-SECURITY-ID>` | Secret/dependency audit | REQ-<REQ-ID>/SEC-<SEC-ID> | Theo tool khả dụng | Không phát hiện secret/risk ngoài ngưỡng | | | NOT_RUN |

### Quy tắc kết quả

- `PASS`: expected và actual khớp.
- `FAIL`: actual không đạt; sửa trong phạm vi hoặc ghi blocker/residual.
- `PARTIAL`: chỉ một phần criteria/check đạt; phải nêu phần thiếu.
- `NOT_APPLICABLE`: chỉ dùng khi trigger không tồn tại và ghi lý do trong evidence.
- `NOT_RUN`: chưa được dùng làm cơ sở chuyển `VERIFIED`.

### Tiêu chí fail và môi trường

- Ngưỡng fail/lỗi chặn checkpoint:
- Flaky behavior, dữ liệu test và cleanup:
- Commit/worktree:
- OS/tool versions:
- Fixture/seed/test account:
- External services/feature flags:
- Reproducibility notes:

Mỗi check phải liên kết một hoặc nhiều requirement/criteria, task và evidence. Nếu command khác với manifest, ghi lý do và cập nhật manifest/CR nếu cần.

## 5. Verification evidence

- Evidence ID: EVD-<M-ID>-<P-ID>
- M/Phase:
- Requirement IDs / acceptance criteria:
- Task IDs:
- Commit/worktree reference:
- Environment:
- Agent/operator:
- Timestamp/timezone:
- Verification status: VERIFIED | PARTIAL | FAILED | BLOCKED | NOT_RUN
- Acceptance status: PENDING

### Commands hoặc kịch bản

```text
# Ghi nguyên văn command/kịch bản có thể tái chạy
- command
```

### Results

| Check ID | Expected | Actual/output summary | Artifact/link | Status |
|---|---|---|---|---|
| TEST-<TEST-ID> | | | | |

### Traceability và artifacts

- Requirements/criteria:
- Task list:
- Test/verification matrix:
- Checkpoint:
- Phase report:
- Logs/screenshots/output files:

### Limitations, residual và blocker

- Chưa kiểm chứng:
- NOT_APPLICABLE (kèm lý do):
- Residual IDs:
- Blocker IDs:
- Reproduction/next step:

Evidence là bằng chứng verification kỹ thuật; acceptance status áp dụng `docs/03-requirements/acceptance-policy.md`.

## 6. Checkpoint và review

- Checkpoint ID: CHK-<M-ID>-<P-ID>
- M:
- Ngày:
- Reviewer/acceptor:
- Verification status: NOT_RUN | PARTIAL | FAILED | VERIFIED | BLOCKED
- Checkpoint status: INCOMPLETE | CHECKPOINT_PENDING
- Acceptance status: PENDING | ACCEPTED | REJECTED | DEFERRED

### Điều kiện trước checkpoint

- [ ] Phase có trong ROADMAP và scope không vượt quá change control
- [ ] Requirements/acceptance criteria đã map
- [ ] Tasks có status và residual/blocker
- [ ] Test/verification matrix đã chạy, hoặc có lý do N/A
- [ ] Evidence có command, expected, actual, environment và limitation
- [ ] Traceability đã cập nhật
- [ ] Phase report và technical debt đã rà soát

### Nội dung đã kiểm chứng

- [ ] Requirements:
- [ ] Tests:
- [ ] Build/lint/type/secret scan:
- [ ] Product criteria:
- [ ] Evidence:
- [ ] Report:

### Chưa hoàn thành / cảnh báo

- RESID-:
- BLOCKER-:
- RISK-:

### Quyết định nghiệm thu

- Quyết định: CHƯA CÓ | ACCEPTED | REJECTED | DEFERRED
- Người/role:
- Ngày:
- Decision Log:
- Lý do/điều kiện:

Checkpoint này ghi nhận điểm xem xét; giữ status và acceptance theo `docs/00-governance/status-model.md` và `docs/03-requirements/acceptance-policy.md`.

## 7. Definition of Done

Mỗi task phải có output, dependency, requirement link, verification result và status. Task chỉ `VERIFIED` khi output đã được kiểm tra; task chưa xong không được đánh dấu hoàn thành chỉ vì code hoặc file đã tồn tại. Phase chỉ được chuyển sang checkpoint khi các section test, evidence và checkpoint trong file này đã được cập nhật. Nếu không hoàn thành, ghi residual/blocker ID và lý do.
