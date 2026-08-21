# Status Model

Tài liệu này là từ điển trạng thái dùng chung cho requirement, M, Phase, task, research, change request, evidence, checkpoint và report. Các tài liệu khác chỉ dẫn về đây và `docs/03-requirements/acceptance-policy.md`; không tự định nghĩa thêm trạng thái mới.

## Trạng thái vòng đời artifact

- `DRAFT`: mới tạo hoặc đang soạn; chưa đủ điều kiện để bắt đầu.
- `READY`: đủ thông tin tối thiểu, dependency và quyền cần thiết để bắt đầu hoặc kiểm tra bước tiếp theo.
- `IN_PROGRESS`: đang thực hiện; chưa có kết luận cuối.
- `BLOCKED`: không thể tiếp tục vì thiếu quyết định, quyền, dữ liệu hoặc dependency; phải ghi rõ blocker.
- `DEFERRED`: chủ động dời lại, phải ghi lý do và điều kiện mở lại.
- `REJECTED`: đã được xem xét nhưng không đạt; phải ghi lý do và đường quay lại.
- `CANCELLED`: không còn trong phạm vi theo quyết định đã ghi.
- `CLOSED`: ledger item hoặc action đã đạt close condition và giữ evidence/decision reference.
- `FINAL`: report/document content đã hoàn tất review; không đồng nghĩa product acceptance.

## Trạng thái kiểm chứng, checkpoint và acceptance

- `VERIFIED`: đã chạy kiểm chứng kỹ thuật theo test plan và kết quả đạt phạm vi đã định.
- `CHECKPOINT_PENDING`: đã có đủ artifact kỹ thuật để con người xem xét; chưa phải nghiệm thu.
- `ACCEPTED`: người/role có thẩm quyền đã nghiệm thu theo acceptance policy.
- `NOT_ACCEPTED`: chưa có quyết định nghiệm thu; đây là trạng thái acceptance, không phải trạng thái công việc.
- `PASS` / `FAIL`: kết quả của một check cụ thể.
- `PARTIAL`: chỉ một phần check hoặc acceptance criteria đạt.
- `FAILED`: kết luận của một artifact hoặc nhóm verification khi có check fail.
- `NOT_RUN`: check chưa chạy.
- `NOT_APPLICABLE`: check hoặc tài liệu không áp dụng, phải có lý do.
- `INCOMPLETE`: checkpoint/report chưa đủ điều kiện hoặc còn mục bắt buộc chưa hoàn thành.

## Trạng thái discovery, registry và decision

- `OPEN`: câu hỏi, assumption, risk hoặc issue chưa được giải quyết.
- `RESOLVED`: research/question đã có kết luận và handoff.
- `ASSUMED`: thông tin đang được dùng tạm thời nhưng chưa được kiểm chứng.
- `CONFIRMED`: fact/answer đã được xác nhận bởi nguồn hoặc người có thẩm quyền.
- `PROPOSED`, `SUPERSEDED`: vòng đời của change/decision/ADR.
- `CURRENT`: registry entry hoặc policy đang có hiệu lực.
- `NOT_STARTED`: artifact đã được đăng ký nhưng chưa được tạo/bắt đầu.
- `NOT_APPLICABLE`: tài liệu/contract không áp dụng, phải ghi lý do và trigger.

## Luật chuyển trạng thái

1. Artifact mới bắt đầu ở `DRAFT`, trừ khi template quy định rõ trạng thái kết quả khác.
2. Chỉ chuyển `DRAFT -> READY` khi đã có owner/role, phạm vi, dependency, output và tiêu chí kiểm chứng.
3. Chỉ chuyển `IN_PROGRESS -> VERIFIED` khi evidence có command/kịch bản, expected, actual, environment, thời điểm và limitation.
4. Chỉ chuyển sang `CHECKPOINT_PENDING` khi Phase/M có đủ requirements, `task.md` (test plan, evidence, checkpoint), report và residual/debt đã rà soát.
5. Chỉ người/role nghiệm thu mới chuyển `CHECKPOINT_PENDING -> ACCEPTED`, `REJECTED` hoặc `DEFERRED`; phải ghi ngày, lý do và Decision Log nếu cần.
6. `VERIFIED` không tự động dẫn tới `ACCEPTED`; `CHECKPOINT_PENDING` luôn được hiển thị là chưa hoàn thành.
7. `CLOSED`, `DEFERRED`, `REJECTED` và `CANCELLED` phải giữ nguyên lịch sử; không xóa hoặc ghi đè lý do.

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
| Blocker/environment/action | `BLOCKER`, `ENV-ISSUE`, `ENV-SVC`, `ENV-DEP`, `ACTION` | `BLOCKER-<M-ID>-<P-ID>-001` |
| Change/decision/architecture | `CR`, `DEC`, `ADR` | `CR-001`, `DEC-001`, `ADR-001` |
| Component/residual/debt | `C`, `RESID`, `DEBT` | `C-001`, `RESID-<PROJECT>-001`, `DEBT-<PROJECT>-001` |

ID là bất biến sau khi phát hành. Placeholder dùng thống nhất dạng `<M-ID>`, `<P-ID>`, `<M-ID>-<P-ID>`, `<PROJECT>`; phải thay bằng ID thật trước khi artifact chuyển `READY`. Không dùng `XXX`, `MXX`, `PXX` hoặc `001` chung chung trong artifact project đã phát hành.

## Luật nghiêm ngặt

`CHECKPOINT_PENDING` không phải `ACCEPTED`.

`VERIFIED` không phải `ACCEPTED`.

Checkpoint hoặc report chưa hoàn thành không được dùng làm bằng chứng nghiệm thu. Evidence chỉ chứng minh việc kiểm chứng kỹ thuật đã diễn ra. Chi tiết quyền nghiệm thu nằm ở `docs/03-requirements/acceptance-policy.md`.
