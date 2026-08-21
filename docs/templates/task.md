# <M-ID>-<P-ID> - Task, Test, Evidence và Checkpoint

- Phase:
- Requirement scope:
- Owner/role:
- Trạng thái: DRAFT

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

| ID | Mô tả | Requirement | Dependency | Output/changed artifact | Verification | Status |
|---|---|---|---|---|---|---|
| TASK-<M-ID>-<P-ID>-001 | Kiểm tra dependency | REQ-<REQ-ID> | — | Dependency/status note | TEST-<TEST-ID> | DRAFT |
| TASK-<M-ID>-<P-ID>-002 | Triển khai phần chính | REQ-<REQ-ID> | TASK-<M-ID>-<P-ID>-001 | Code/config/documentation | TEST-<TEST-ID> | DRAFT |
| TASK-<M-ID>-<P-ID>-003 | Viết/cập nhật test | REQ-<REQ-ID> | TASK-<M-ID>-<P-ID>-002 | Test artifact | TEST-<TEST-ID> | DRAFT |
| TASK-<M-ID>-<P-ID>-004 | Cập nhật tài liệu và traceability | REQ-<REQ-ID> | TASK-<M-ID>-<P-ID>-002/003 | Docs/traceability | TEST-<TEST-ID> | DRAFT |
| TASK-<M-ID>-<P-ID>-005 | Chạy verification | REQ-<REQ-ID> | TASK-<M-ID>-<P-ID>-001..004 | Verification result | TEST-<TEST-ID> | DRAFT |
| TASK-<M-ID>-<P-ID>-006 | Hoàn thiện evidence và checkpoint | REQ-<REQ-ID> | TASK-<M-ID>-<P-ID>-005 | Evidence/checkpoint record | Review | DRAFT |

### Checklist bắt buộc cho từng task

Copy block này cho mỗi task trong bảng và thay `TASK-...` bằng ID thật. Không chuyển task sang `VERIFIED` nếu còn checkbox bắt buộc chưa hoàn thành.

#### TASK-<M-ID>-<P-ID>-<TASK-ID> - <Tên task>

- [ ] Có requirement/acceptance criteria liên quan.
- [ ] Có owner và trạng thái hiện tại.
- [ ] Dependency đã được kiểm tra và không còn blocker chưa ghi nhận.
- [ ] Phạm vi task và artifact/output đã rõ.
- [ ] Đã triển khai hoặc cập nhật artifact trong phạm vi.
- [ ] Đã cập nhật test/verification liên quan.
- [ ] Test result và actual output đã ghi trong verification matrix.
- [ ] Evidence section có command, expected, actual, environment, commit/worktree và limitation.
- [ ] Traceability đã nối requirement → task → test → evidence.
- [ ] Tài liệu bị ảnh hưởng đã cập nhật.
- [ ] Residual/blocker/risk đã có ID hoặc ghi `NONE` kèm lý do.
- [ ] Reviewer/owner đã xác nhận điều kiện hoàn tất.
- [ ] Task status được cập nhật đúng bằng chứng.

**Task completion note:**

- Output thực tế:
- Files/artifacts:
- Verification IDs:
- Residual/blocker/risk:
- Ghi chú reviewer:

## 3. Test capability profile

- M/Phase capability profile reference:
- Environment Manifest/Setup Report reference:
- Environment gate: `ALLOW` | `BLOCKED`
- Applied verification layers: static/quality | unit/component | integration | API/contract | UI/client | accessibility/usability | visual | performance/load | security/operations | human review
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
| TEST-<M-ID>-<P-ID>-001 | Static/format | REQ-<REQ-ID>/AC-<AC-ID> | Chưa xác định | Không lỗi | | | NOT_RUN |
| TEST-<M-ID>-<P-ID>-002 | Unit/integration | REQ-<REQ-ID>/AC-<AC-ID> | Chưa xác định | Pass | | | NOT_RUN |
| TEST-<M-ID>-<P-ID>-003 | Build/lint/type | REQ-<REQ-ID>/AC-<AC-ID> | Chưa xác định hoặc N/A | Pass hoặc lý do N/A | | | NOT_RUN |
| TEST-<M-ID>-<P-ID>-004 | Product/acceptance mapping | REQ-<REQ-ID>/AC-<AC-ID> | Đối chiếu từng criteria | Có evidence tương ứng | | | NOT_RUN |
| TEST-<M-ID>-<P-ID>-005 | Secret/dependency audit | REQ-<REQ-ID>/SEC-<SEC-ID> | Theo tool khả dụng | Không phát hiện secret/risk ngoài ngưỡng | | | NOT_RUN |

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
