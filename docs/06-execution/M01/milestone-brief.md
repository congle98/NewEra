# M01 - Governance Automation Foundation

- M: M01
- Outcome: NewEra có machine-readable state/evidence/traceability và STANDARD deterministic governance gate.
- ROADMAP: `docs/02-roadmap/roadmap.md`
- CR/Decision: CR-001 / DEC-001
- Owner: NewEra maintainer
- Ngày lập: 2026-08-20
- Trạng thái: IN_PROGRESS

## Phạm vi

### In scope

- M01-P01: state schema, evidence envelope schema, typed traceability graph và source ownership contract.
- M01-P02: STANDARD profile, validator CLI, WARN/FAIL/strict behavior và negative fixture.

### Ngoài phạm vi

- LITE/STRICT runtime adaptation.
- Change impact analysis, generated verification matrix, risk graph.
- Semantic code scope drift detection.
- Auto-acceptance, production deployment và technology-specific adapter.

## Phase và thứ tự

| Phase | Mục tiêu | Dependency | Status |
|---|---|---|---|
| M01-P01 | Machine state/evidence/traceability core | Current Markdown contracts | IN_PROGRESS |
| M01-P02 | STANDARD automated governance gate | M01-P01 contract | IN_PROGRESS |

## Definition of Done

- Schema/state/evidence parse và reference checks chạy được.
- Gate valid state cho WARN/PASS đúng policy; invalid fixture FAIL non-zero.
- Traceability Markdown/state cùng ID và typed edge.
- Evidence JSON + Markdown narrative có limitation và acceptance separation.
- Checkpoint/report/residual cập nhật; chưa chuyển acceptance.
