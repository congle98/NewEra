# Architecture - Reference Template

> Sao chép skeleton này vào adopter workspace. Đây là design contract, không phải architecture state của NewEra kernel.

## Document control / Kiểm soát tài liệu

- Document status: DRAFT
- Owner/architect: `<OWNER>`
- Kernel release: `NEWERA_VERSION`
- Kernel source commit: `SOURCE_COMMIT`
- Project registry reference: `<REGISTRY-REF>`
- ROADMAP/SRS reference: `<ROADMAP-REF>` / `<SRS-REF>`
- Created/updated: `<DATE>`
- Related CR/DEC/ADR: `<REFERENCE-OR-NONE>`

## 1. Bối cảnh và boundary

- Product/system context: `<CONTEXT>`
- In scope: `<BOUNDARY>`
- Out of scope: `<EXCLUSION>`
- External actors/systems: `<ACTOR-OR-SYSTEM>`
- Relevant M/Phase/requirement IDs: `<M-ID>`, `<P-ID>`, `<REQ-ID>`

## 2. Quality attributes và mapping NFR

| ID | Quality attribute/constraint | Target/threshold | Measurement/evidence | Requirement/decision |
|---|---|---|---|---|
| `NFR-<NFR-ID>` | `<ATTRIBUTE>` | `<TARGET>` | `<MEASUREMENT>` | `<REQ/ADR-REF>` |

## 3. Thành phần và trách nhiệm

| ID | Component | Responsibility | Interface/boundary | Owner/status |
|---|---|---|---|---|
| `C-<C-ID>` | `<COMPONENT>` | `<RESPONSIBILITY>` | `<INTERFACE>` | `<OWNER>` / PROPOSED |

Nếu cần diagram hoặc biểu diễn trực quan, ghi link tới artifact của adopter workspace; không tạo diagram project-specific trong kernel.

## 4. Dữ liệu và tích hợp

- Data ownership/classification: `<DATA-REF>`
- Data flow and lifecycle: `<FLOW-REF>`
- Persistence/retention/backup: `<DATA-REF>`
- Integration contracts/dependencies: `<INT-REF>`
- Failure, retry, idempotency and consistency: `<BEHAVIOR>`

## 5. Security, privacy và trust boundary

- Authentication: `<AUTHN>`
- Authorization: `<AUTHZ>`
- Secrets/configuration boundary: `<SECRET-BOUNDARY>`
- Threat/risk/security requirements: `<SEC/RISK-REF>`
- Privacy/data handling: `<PRIVACY-REF>`
- Audit/logging requirements: `<AUDIT-REF>`

## 6. Observability và vận hành

- Logs/events: `<LOG-REF>`
- Metrics/health/SLO: `<METRIC-REF>`
- Alerts and operational ownership: `<OPS-REF>`
- Failure handling, recovery and rollback: `<RECOVERY-REF>`
- Operational NOT_APPLICABLE reason, if relevant: `<REASON-OR-NONE>`

## 7. Runtime và triển khai

- Runtime topology: `<TOPOLOGY>`
- Environment capability references: `<ENV-CAP-REF>`
- Deployment/release boundary: `<DEPLOYMENT-REF>`
- Compatibility/version constraints: `<CONSTRAINT>`
- Human-only approval/access dependency: `<ACTION-ID-OR-NONE>`

## 8. ADR và decision index

| Decision | Topic | Status | Date/owner | Architecture impact |
|---|---|---|---|---|
| `ADR-<ADR-ID>` | `<TOPIC>` | PROPOSED | `<DATE>` / `<OWNER>` | `<IMPACT>` |

Quyết định design lớn thuộc decision/ADR record của adopter và được link tại đây; index này không thay thế decision record.

## 9. Constraint, trade-off và phương án bị loại

- Constraint: `<CON-ID>` — `<DESCRIPTION>`
- Trade-off: `<TRADE-OFF>`
- Rejected option: `<OPTION>` — reason `<REASON>`
- Open architecture question: `RES-<RES-ID>` / `<OPEN>`

## Definition of Ready / Done

### DoR

- [ ] Context, boundary, owner và các reference baseline liên quan đã rõ.
- [ ] Requirements/NFR đã map tới quality attributes và target có thể đo.
- [ ] Component, data flow, trust boundary và runtime dependency đã được mô tả.
- [ ] Security, vận hành, environment và human-only action đã được xác định.
- [ ] Câu hỏi design mở là research/decision handoff, không phải assumption ẩn.

### DoD

- [ ] Architecture review đã hoàn tất bởi role được chỉ định.
- [ ] Link CR/DEC/ADR và ROADMAP/SRS đã resolve.
- [ ] Capability verification và ảnh hưởng tới evidence đã được ghi.
- [ ] Trade-off/phương án bị loại và residual design debt đã được ghi.
- [ ] Status, owner, version/source và ngày cập nhật còn đúng.
