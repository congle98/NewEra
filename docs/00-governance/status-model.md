# Status Model

Tài liệu này là từ điển trạng thái dùng chung cho requirement, M, Phase, task, research, change request, evidence, checkpoint và report. Các giá trị được **nhóm theo ý nghĩa**; không dùng một danh sách phẳng cho mọi artifact. Các tài liệu khác chỉ dẫn về đây và `docs/03-requirements/acceptance-policy.md`; không tự định nghĩa thêm trạng thái mới.

## Cách dùng status gọn

Một artifact chỉ dùng những nhóm áp dụng cho nó:

- Task/micro-change: lifecycle + verification.
- Phase/M: lifecycle + verification + checkpoint + acceptance.
- Research: lifecycle + discovery.
- CR/decision/ADR: lifecycle + decision.
- Từng test: check result riêng.

`PASS`/`FAIL` là kết quả của từng check; `VERIFIED`/`FAILED` là kết luận verification-level; `ACCEPTED` là quyết định nghiệm thu. Không trộn các lớp này vào một trường status duy nhất.

## Lifecycle status

Đây là bộ status chính cho tiến độ artifact:

- `DRAFT`: mới tạo hoặc đang soạn; chưa đủ điều kiện để bắt đầu.
- `READY`: đủ thông tin tối thiểu, dependency và quyền cần thiết để bắt đầu hoặc kiểm tra bước tiếp theo.
- `IN_PROGRESS`: đang thực hiện; chưa có kết luận cuối.
- `BLOCKED`: không thể tiếp tục vì thiếu quyết định, quyền, dữ liệu hoặc dependency; phải ghi rõ blocker.
- `CLOSED`: đã đạt close condition và giữ evidence/decision reference.
- `DEFERRED`: chủ động dời lại; chỉ dùng khi cần ghi một quyết định dời cùng điều kiện mở lại.
- `CANCELLED`: không còn trong phạm vi theo quyết định đã ghi.

`REJECTED` là kết quả review/acceptance/change decision, không phải lifecycle mặc định. `FINAL` là trạng thái hoàn thiện nội dung report/document; `CURRENT`, `PROPOSED`, `SUPERSEDED` là trạng thái registry/decision chuyên biệt.

## Verification, checkpoint và acceptance status

### Verification

- `NOT_RUN`: check chưa chạy.
- `PARTIAL`: chỉ một phần check hoặc criteria đạt.
- `VERIFIED`: đã chạy kiểm chứng kỹ thuật theo test plan và kết quả đạt phạm vi đã định.
- `FAILED`: kết luận verification khi có check fail chưa được xử lý.
- `NOT_APPLICABLE`: check không áp dụng, phải có lý do.

`BLOCKED` có thể dùng ở lớp verification khi chưa thể kiểm chứng vì thiếu dependency/quyền/dữ liệu. `PASS` và `FAIL` chỉ dùng cho từng check cụ thể.

### Checkpoint

- `INCOMPLETE`: checkpoint/report chưa đủ điều kiện.
- `CHECKPOINT_PENDING`: đã có đủ artifact kỹ thuật để con người xem xét; chưa phải nghiệm thu.

### Acceptance

- `PENDING`: chưa có quyết định nghiệm thu.
- `ACCEPTED`: người/role có thẩm quyền đã nghiệm thu theo acceptance policy.
- `REJECTED`: kết quả review/acceptance không đạt, phải ghi lý do và đường quay lại.
- `DEFERRED`: quyết định dời nghiệm thu, phải ghi điều kiện mở lại.

`VERIFIED` không tự động là `ACCEPTED`; `CHECKPOINT_PENDING` luôn được hiển thị là chưa hoàn thành. `PENDING` là trạng thái mặc định khi chưa có quyết định acceptance; không dùng một status acceptance khác để thay thế hoặc làm mờ trạng thái này.

## Discovery, registry và decision status

- Discovery/resolution: `OPEN`, `RESOLVED`, `ASSUMED`, `CONFIRMED`.
- Decision/change: `PROPOSED`, `ACCEPTED`, `REJECTED`, `DEFERRED`, `SUPERSEDED`.
- Registry/document: `CURRENT`, `FINAL`, `NOT_APPLICABLE`.
- `NOT_APPLICABLE` luôn đi cùng lý do và trigger; không dùng để che một check chưa chạy.

## Luật chuyển trạng thái

1. Artifact mới bắt đầu ở `DRAFT`, trừ khi template quy định rõ trạng thái kết quả khác.
2. Chỉ chuyển `DRAFT -> READY` khi đã có owner/role, phạm vi, dependency, output và tiêu chí kiểm chứng.
3. Chỉ ghi `VERIFIED` khi evidence có command/kịch bản, expected, actual, environment, thời điểm và limitation.
4. Chỉ chuyển sang `CHECKPOINT_PENDING` khi Phase/M có đủ requirements, `task.md` (test plan, evidence, checkpoint), report và residual/debt đã rà soát.
5. Chỉ người/role nghiệm thu mới chuyển `CHECKPOINT_PENDING -> ACCEPTED`, `REJECTED` hoặc `DEFERRED`; phải ghi ngày, lý do và Decision Log nếu cần.
6. `CLOSED`, `DEFERRED`, `REJECTED` và `CANCELLED` phải giữ nguyên lịch sử; không xóa hoặc ghi đè lý do.

## Quy ước ID và placeholder

| Loại artifact | Prefix | Ví dụ |
|---|---|---|
| Objective/user/stakeholder/success/exit | `OBJ`, `USER`, `STAKEHOLDER`, `SUCCESS`, `EXIT` | `OBJ-001`, `STAKEHOLDER-001` |
| Intake/question/charter/SRS/setup | `INTAKE`, `INQ`, `CHARTER`, `SRS`, `SETUP` | `INTAKE-001`, `INQ-001` |
| Use case/acceptance/security/performance/operations | `UC`, `AC`, `SEC`, `PERF`, `OPS` | `UC-001`, `AC-001` |
| Requirement/business/data/integration/NFR | `REQ`, `BR`, `DATA`, `INT`, `NFR` | `REQ-001`, `NFR-001` |
| Assumption/constraint/risk | `ASM`, `CON`, `RISK` | `ASM-001` |
| Research/question | `RES` | `RES-001` |
| Milestone/Phase/task/test | `M`, `P`, `TASK`, `TEST` | `<M-ID>-<P-ID>`, `TASK-<M-ID>-<P-ID>-001` |
| Evidence/checkpoint/report | `EVD`, `CHK`, `RPT` | `EVD-<M-ID>-<P-ID>`, `CHK-<M-ID>-<P-ID>` |
| Blocker/environment/action/capability | `BLOCKER`, `ENV-ISSUE`, `ENV-SVC`, `ENV-DEP`, `ENV-CAP`, `ACTION` | `BLOCKER-<M-ID>-<P-ID>-001`, `ENV-CAP-001` |
| Change/decision/architecture | `CR`, `DEC`, `ADR` | `CR-001`, `DEC-001`, `ADR-001` |
| Component/residual/debt | `C`, `RESID`, `DEBT` | `C-001`, `RESID-<PROJECT>-001`, `DEBT-<PROJECT>-001` |

ID là bất biến sau khi phát hành. Placeholder dùng thống nhất dạng `<M-ID>`, `<P-ID>`, `<M-ID>-<P-ID>`, `<PROJECT>`; phải thay bằng ID thật trước khi artifact chuyển `READY`. Không dùng `XXX`, `MXX`, `PXX` hoặc `001` chung chung trong artifact project đã phát hành.

## Luật nghiêm ngặt

`CHECKPOINT_PENDING` không phải `ACCEPTED`.

`VERIFIED` không phải `ACCEPTED`.

Checkpoint hoặc report chưa hoàn thành không được dùng làm bằng chứng nghiệm thu. Evidence chỉ chứng minh việc kiểm chứng kỹ thuật đã diễn ra. Chi tiết quyền nghiệm thu nằm ở `docs/03-requirements/acceptance-policy.md`.
