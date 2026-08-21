# MXX-PXX - Task, Test, Evidence và Checkpoint

- Phase:
- Requirement scope:
- Owner/role:
- Trạng thái: DRAFT

Template này gom toàn bộ công việc thực thi và kiểm chứng của một Phase vào một file. `requirements.md` giữ requirement/acceptance criteria; `report.md` giữ tổng kết sau Phase.

## 1. Definition of Ready cho task

Task chỉ được `READY` khi có một output kiểm tra được, dependency rõ, requirement/acceptance criteria liên quan, cách kiểm chứng và biết tài liệu nào sẽ cập nhật. Task thiếu dữ liệu quan trọng phải là `BLOCKED` hoặc `OPEN`, không giả định.

## 2. Task list

| ID | Mô tả | Requirement | Dependency | Output/changed artifact | Verification | Status |
|---|---|---|---|---|---|---|
| TASK-MXX-PXX-001 | Kiểm tra dependency | REQ- | — | Dependency/status note | TEST- | DRAFT |
| TASK-MXX-PXX-002 | Triển khai phần chính | REQ- | TASK-001 | Code/config/documentation | TEST- | DRAFT |
| TASK-MXX-PXX-003 | Viết/cập nhật test | REQ- | TASK-002 | Test artifact | TEST- | DRAFT |
| TASK-MXX-PXX-004 | Cập nhật tài liệu và traceability | REQ- | TASK-002/003 | Docs/traceability | TEST- | DRAFT |
| TASK-MXX-PXX-005 | Chạy verification | REQ- | TASK-001..004 | Verification result | TEST- | DRAFT |
| TASK-MXX-PXX-006 | Hoàn thiện evidence và checkpoint | REQ- | TASK-005 | Evidence/checkpoint record | Review | DRAFT |

### Checklist bắt buộc cho từng task

Copy block này cho mỗi task trong bảng và thay `TASK-...` bằng ID thật. Không chuyển task sang `VERIFIED` nếu còn checkbox bắt buộc chưa hoàn thành.

#### TASK-MXX-PXX-XXX - <Tên task>

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

## 3. Test plan và verification matrix

- Requirement scope:
- Owner/agent:
- Environment reference: `docs/05-environment/environment-manifest.md`
- Trạng thái: DRAFT

| ID | Loại | Requirement/criteria | Lệnh/kịch bản | Kết quả mong đợi | Kết quả thực tế | Artifact/output | Status |
|---|---|---|---|---|---|---|---|
| TEST-MXX-PXX-001 | Static/format | REQ-/AC- | Chưa xác định | Không lỗi | | | NOT_RUN |
| TEST-MXX-PXX-002 | Unit/integration | REQ-/AC- | Chưa xác định | Pass | | | NOT_RUN |
| TEST-MXX-PXX-003 | Build/lint/type | REQ-/AC- | Chưa xác định hoặc N/A | Pass hoặc lý do N/A | | | NOT_RUN |
| TEST-MXX-PXX-004 | Product/acceptance mapping | REQ-/AC- | Đối chiếu từng criteria | Có evidence tương ứng | | | NOT_RUN |
| TEST-MXX-PXX-005 | Secret/dependency audit | REQ-/SEC- | Theo tool khả dụng | Không phát hiện secret/risk ngoài ngưỡng | | | NOT_RUN |

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

## 4. Verification evidence

- Evidence ID: EVD-MXX-PXX
- M/Phase:
- Requirement IDs / acceptance criteria:
- Task IDs:
- Commit/worktree reference:
- Environment:
- Agent/operator:
- Timestamp/timezone:
- Verification status: VERIFIED | PARTIAL | FAILED | BLOCKED | NOT_RUN
- Acceptance status: NOT_ACCEPTED

### Commands hoặc kịch bản

```text
# Ghi nguyên văn command/kịch bản có thể tái chạy
- command
```

### Results

| Check ID | Expected | Actual/output summary | Artifact/link | Status |
|---|---|---|---|---|
| TEST- | | | | |

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

Evidence là bằng chứng verification kỹ thuật, không phải nghiệm thu sản phẩm. Test pass không chuyển acceptance status.

## 5. Checkpoint và review

- Checkpoint ID: CHK-MXX-PXX
- M:
- Ngày:
- Reviewer/acceptor:
- Verification status: NOT_RUN | PARTIAL | FAILED | VERIFIED | BLOCKED
- Checkpoint status: INCOMPLETE | CHECKPOINT_PENDING
- Acceptance status: NOT_ACCEPTED | ACCEPTED | REJECTED | DEFERRED

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

Checkpoint này ghi nhận điểm xem xét; nếu chưa có quyết định, giữ `CHECKPOINT_PENDING` và `NOT_ACCEPTED`. Checkpoint chưa hoàn thành không được dùng làm bằng chứng nghiệm thu.

## 6. Definition of Done

Mỗi task phải có output, dependency, requirement link, verification result và status. Task chỉ `VERIFIED` khi output đã được kiểm tra; task chưa xong không được đánh dấu hoàn thành chỉ vì code hoặc file đã tồn tại. Phase chỉ được chuyển sang checkpoint khi các section test, evidence và checkpoint trong file này đã được cập nhật. Nếu không hoàn thành, ghi residual/blocker ID và lý do.
