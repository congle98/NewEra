# Technical Debt

Debt là trade-off kỹ thuật có chủ đích, được chấp nhận với rủi ro và kế hoạch trả. Không dùng debt để che blocker, acceptance gap hoặc scope chưa được duyệt.

## Register

| ID | Source M/Phase/REQ/ADR | Description | Reason accepted | Risk/impact | Probability | Owner | Repayment plan | Target/due | Priority | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| DEBT-<PROJECT>-001 | | | | | | | | | | OPEN |

Status: `OPEN` → `READY` → `IN_PROGRESS` → `VERIFIED` → `CLOSED`, hoặc `DEFERRED` với review date và decision owner.

## Debt acceptance record

- Decision/approver/date:
- Why immediate repayment is not required:
- Guardrail/monitoring:
- Trigger forcing repayment:
- Impact on security, reliability, cost, performance or maintainability:

## Repayment/closure record

| ID | Work/commit | Verification/evidence | Actual risk after repayment | Decision/date | Status |
|---|---|---|---|---|---|
| DEBT-<DEBT-ID> | | | | | |

## Review checklist

- [ ] Debt có source, owner, reason và measurable risk.
- [ ] Repayment plan/target hoặc lý do long-term có review date.
- [ ] Security/compliance debt không bị chấp nhận mà không có risk owner/mitigation.
- [ ] Debt không thay thế residual/CR/acceptance decision.
- [ ] Closure có evidence và verification result.
- [ ] Debt được review khi scope, architecture hoặc dependency thay đổi.
