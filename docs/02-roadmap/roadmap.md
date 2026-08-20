# ROADMAP

> Đây là nguồn sự thật cao nhất về M, Phase, phạm vi và thứ tự triển khai.

## Tầm nhìn sản phẩm

NewEra trở thành process kernel có thể đọc/ghi/kiểm tra bằng máy, trong khi Markdown vẫn phục vụ narrative, review và quyết định của con người. Traceability là capability nhận diện của NewEra; governance gate bảo vệ quy trình nhưng không thay thế acceptance.

## Quy tắc phân cấp

```text
M = kết quả lớn có ý nghĩa với sản phẩm/kernel
Phase = khối triển khai có thể kiểm chứng độc lập
Task = công việc cụ thể có output và tiêu chí hoàn thành
```

Phân chia theo giá trị và khả năng kiểm chứng, không chia theo lớp kỹ thuật. Không tạo M chỉ vì có thêm một module kỹ thuật.

## Milestone Index

| M | Tên | Mục tiêu | Phase | Dependency | Trạng thái | Readiness gap |
|---|---|---|---|---|---|---|
| M01 | Governance Automation Foundation | State, evidence, traceability, STANDARD baseline và deterministic gate | M01-P01, M01-P02 | CR-001/DEC-001, current Markdown contracts | IN_PROGRESS | P0 evidence/gate verification và documentation còn đang chạy |
| M02 | Adaptive and Impact Governance | Profiles LITE/STRICT, impact analysis, matrix, risk và drift detection | M02-P01..P04 | M01 STANDARD stable, dogfood evidence | DRAFT | Chưa bắt đầu; cần P0 graph/state trước |

## M01 — Governance Automation Foundation

### M01-P01 — Machine State, Evidence Schema và Traceability Core

- **Mục tiêu:** tạo structured state/evidence contract và graph references cho automation.
- **Phạm vi:** `.newera/project-state.json`, JSON schemas, evidence envelope, state/profile contract, traceability edges.
- **Ngoài phạm vi:** semantic code graph, tự động acceptance, YAML dependency bắt buộc.
- **Tiêu chí hoàn thành:** schema parse được; state references resolve; evidence có required fields; Markdown/state ownership policy được ghi.
- **Trạng thái:** IN_PROGRESS.

### M01-P02 — STANDARD Automated Governance Gate

- **Mục tiêu:** validator deterministic phát hiện thiếu requirement/test/evidence/reference và scope/status conflict.
- **Phạm vi:** `scripts/newera_validate.py`, STANDARD profile, PASS/WARN/FAIL, strict mode, invalid fixture.
- **Ngoài phạm vi:** semantic drift detection, adaptive profile switching runtime, auto-acceptance.
- **Tiêu chí hoàn thành:** valid state không có structural error; incomplete state WARN; strict/inconsistent state FAIL; exit code ổn định.
- **Trạng thái:** IN_PROGRESS.

## M02 — Adaptive and Impact Governance (P1)

| Phase | Mục tiêu | Dependency | Trạng thái |
|---|---|---|---|
| M02-P01 | Machine-integrated change management và requirement version diff | M01 state/graph | DRAFT |
| M02-P02 | Change impact analysis và generated verification matrix | M01 traceability graph | DRAFT |
| M02-P03 | Risk register, risk graph và LITE/STRICT profile enforcement | M01 STANDARD stable | DRAFT |
| M02-P04 | Deterministic scope drift detection, sau đó semantic advisory | M01 gate + M02 graph | DRAFT |

## Hợp đồng tối thiểu của một M/Phase

Mỗi M phải có outcome đo được, in/out scope, Phase theo thứ tự, dependency, risk có owner, acceptance criteria, registry và điều kiện chuyển tiếp. M01 P0 còn `IN_PROGRESS`; không gọi là `VERIFIED` hay `ACCEPTED` chỉ vì validator đã chạy.

Mỗi Phase phải có requirements với ID, task có output/dependency/status, test-plan, state/evidence references, checkpoint, report và residual/debt. Gate FAIL chặn technical progression; acceptance vẫn do người/role quyết định.

## Quy trình cập nhật ROADMAP

1. Đọc intake/charter, SRS, architecture, state contract và dependency.
2. Scope/architecture/timeline mới phải có CR trước.
3. Sau quyết định, cập nhật ROADMAP trước Phase/Task/implementation.
4. Đồng bộ milestone-index, registry, state, traceability, evidence và report.
5. Ghi CR/DEC trong commit/changelog hoặc decision record.

## Quy tắc thay đổi

Thay đổi ROADMAP phải đi qua `docs/00-governance/change-control.md`. Adaptive Governance, impact analysis, risk, matrix và drift detection là P1; không triển khai chúng bằng cách nới lỏng P0 gate. Residual/M01.x chỉ trả nợ mục tiêu cũ; feature mới phải qua CR và vào ROADMAP.
