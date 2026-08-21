# Status Model

Tài liệu này là từ điển trạng thái dùng chung cho requirement, M, Phase, task, research, change request, evidence, checkpoint và report. Trạng thái phải mô tả đúng loại thông tin đang được ghi; không dùng một từ cho nhiều nghĩa khác nhau.

## Trạng thái vòng đời công việc

- `DRAFT`: mới tạo hoặc đang soạn; chưa đủ điều kiện để bắt đầu.
- `READY`: đủ thông tin tối thiểu, dependency và quyền cần thiết để bắt đầu.
- `IN_PROGRESS`: đang thực hiện; chưa có kết luận cuối.
- `VERIFIED`: đã chạy kiểm chứng kỹ thuật theo test plan và kết quả đạt phạm vi đã định.
- `CHECKPOINT_PENDING`: đã có đủ artifact kỹ thuật để con người xem xét; chưa phải nghiệm thu.
- `ACCEPTED`: người/role có thẩm quyền đã nghiệm thu theo acceptance policy.
- `BLOCKED`: không thể tiếp tục vì thiếu quyết định, quyền, dữ liệu hoặc dependency; phải ghi rõ blocker.
- `DEFERRED`: chủ động dời lại, phải ghi lý do và điều kiện mở lại.
- `REJECTED`: đã được xem xét nhưng không đạt; phải ghi lý do và đường quay lại.
- `CANCELLED`: không còn trong phạm vi theo quyết định đã ghi.

## Kết quả kiểm chứng và trạng thái phụ

Các giá trị sau không thay thế trạng thái vòng đời:

- `PASS` / `FAIL`: kết quả của một check cụ thể.
- `PARTIAL`: chỉ một phần check hoặc acceptance criteria đạt.
- `NOT_RUN`: check chưa chạy.
- `NOT_APPLICABLE`: check hoặc tài liệu không áp dụng, phải có lý do.
- `NOT_ACCEPTED`: chưa có quyết định nghiệm thu; đây là trạng thái acceptance, không phải trạng thái công việc.
- `FAILED`: kết luận của một artifact hoặc nhóm verification khi có check fail; khác `FAIL` là kết quả của một check đơn lẻ.
- `INCOMPLETE`: checkpoint/report chưa đủ điều kiện hoặc còn mục bắt buộc chưa hoàn thành.
- `NOT_STARTED`: artifact đã được đăng ký nhưng chưa được tạo/bắt đầu; không thay thế `DRAFT` của nội dung đã tồn tại.
- `PROPOSED`, `SUPERSEDED`: vòng đời của ADR/decision.
- `OPEN`, `RESOLVED`: vòng đời ngắn của câu hỏi research hoặc issue; khi cần hành động thì liên kết sang `BLOCKED`, `DEFERRED` hoặc residual work.

## Luật chuyển trạng thái

1. Artifact mới bắt đầu ở `DRAFT`, trừ khi template quy định rõ trạng thái kết quả khác.
2. Chỉ chuyển `DRAFT -> READY` khi đã có owner/role, phạm vi, dependency, output và tiêu chí kiểm chứng.
3. Chỉ chuyển `IN_PROGRESS -> VERIFIED` khi evidence có command/kịch bản, expected, actual, environment, thời điểm và limitation.
4. Chỉ chuyển sang `CHECKPOINT_PENDING` khi Phase/M có đủ requirements, task status, test plan, evidence, checkpoint, report và residual/debt đã rà soát.
5. Chỉ người/role nghiệm thu mới chuyển `CHECKPOINT_PENDING -> ACCEPTED`, `REJECTED` hoặc `DEFERRED`; phải ghi ngày, lý do và Decision Log nếu cần.
6. `VERIFIED` không tự động dẫn tới `ACCEPTED`; `CHECKPOINT_PENDING` luôn được hiển thị là chưa hoàn thành.
7. `BLOCKED`, `DEFERRED`, `REJECTED` và `CANCELLED` phải giữ nguyên lịch sử; không xóa hoặc ghi đè lý do.

## Quy ước ID

| Loại artifact | Prefix | Ví dụ |
|---|---|---|
| Objective/user/stakeholder/success/exit | `OBJ`, `USER`, `STAKEHOLDER`, `SUCCESS`, `EXIT` | `OBJ-001` |
| Intake/charter/SRS/setup | `INTAKE`, `CHARTER`, `SRS`, `SETUP` | `INTAKE-001`, `SRS-001` |
| Use case/acceptance/security/performance/operations | `UC`, `AC`, `SEC`, `PERF`, `OPS` | `UC-001`, `AC-001` |
| Requirement/business/data/integration/NFR | `REQ`, `BR`, `DATA`, `INT`, `NFR` | `REQ-001`, `NFR-001` |
| Namespaced kernel quality attributes | `NFR-<PROJECT>` | `NFR-<PROJECT>-001` |
| Assumption/constraint/risk | `ASM`, `CON`, `RISK` | `ASM-001` |
| Research/question | `RES` | `RES-001` |
| Milestone/Phase/task/test | `M`, `P`, `TASK`, `TEST`, `TASK-<PROJECT>`, `TEST-<PROJECT>` | `<M>-<P>`, `TASK-<M>-<P>-001`, `TASK-<PROJECT>-001` |
| Evidence/checkpoint/report | `EVD`, `CHK`, `RPT`, `EVD-<PROJECT>`, `CHK-<PROJECT>` | `EVD-<M>-<P>`, `CHK-<M>-<P>` |
| Blocker/risk/issue | `BLOCKER`, `RISK`, `ENV-ISSUE` | `BLOCKER-<M>-<P>-001` |
| Change/decision/architecture | `CR`, `DEC`, `ADR` | `CR-XXX`, `DEC-XXX`, `ADR-XXX` |
| Environment/service/dependency/action | `ENV-SVC`, `ENV-DEP`, `ACTION` | `ENV-SVC-001`, `ENV-DEP-001` |
| Component/residual/debt | `C`, `RESID`, `DEBT` | `C-001`, `RESID-NEWERA-001`, `DEBT-NEWERA-001` |

ID là bất biến sau khi phát hành. Nếu nội dung bị thay thế, giữ ID và ghi lịch sử; nếu là nội dung mới, tạo ID mới. Không dùng `XXX`, `001` chung chung hoặc đổi prefix giữa các tài liệu. Các chuỗi `XXX`, `MXX`, `PXX`, `REQ-001` trong `docs/templates/` chỉ là placeholder có đánh dấu; phải thay bằng ID thật trước khi artifact được dùng hoặc chuyển `READY`.

## Luật nghiêm ngặt

`CHECKPOINT_PENDING` không phải `ACCEPTED`.

`VERIFIED` không phải `ACCEPTED`.

Checkpoint hoặc report chưa hoàn thành không được dùng làm bằng chứng nghiệm thu. Evidence chỉ chứng minh việc kiểm chứng kỹ thuật đã diễn ra.
