# Residual Work

Residual là phần scope đã được xác định nhưng chưa hoàn tất, blocker hoặc acceptance gap của M/Phase. Không dùng residual để hợp thức hóa scope mới.

## Register

| ID | Source M/Phase/REQ | Description | Type | Impact | Priority | Owner | Proposed M/Phase | Close condition | Next action/due | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| RESID-<PROJECT>-001 | | | INCOMPLETE/BLOCKER/ACCEPTANCE_GAP | | | | | | | OPEN |

Status: `OPEN` → `IN_PROGRESS` → `READY` → `CLOSED`, hoặc `DEFERRED`/`CANCELLED` với decision reference.

## Closure record

| ID | Resolution/actual result | Evidence/commit | Verification date/result | Acceptance/decision | Closed by/date |
|---|---|---|---|---|---|
| RESID-<RESID-ID> | | | | | |

## Review checklist

- [ ] Mỗi item có source, impact, priority, owner và next action.
- [ ] Close condition observable/testable.
- [ ] Blocker có dependency hoặc escalation path.
- [ ] Feature/scope mới đã đi qua CR và ROADMAP, không ghi như residual.
- [ ] Khi đóng có evidence, commit và verification result.
- [ ] Không xóa lịch sử hoặc chuyển CLOSED khi chỉ có giả định.
