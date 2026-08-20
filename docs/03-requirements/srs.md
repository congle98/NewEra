# Software Requirements Specification

SRS là nguồn sự thật cho yêu cầu sản phẩm và acceptance criteria; ROADMAP vẫn là nguồn sự thật cho scope/M/Phase. Không điền requirement giả chỉ để làm bảng có vẻ đầy đủ.

- SRS ID/version: SRS-001 / v0.1
- Nguồn intake/charter:
- Owner/reviewer:
- Ngày:
- Trạng thái: DRAFT

## 1. Bối cảnh và problem statement

Chưa xác định. Liên kết `project-intake.md` và `project-charter.md` khi có dữ liệu đã xác nhận.

## 2. Mục tiêu và outcome

- `OBJ-001`: Chưa xác định; không dùng làm acceptance cho tới khi có target/baseline.
- Success metrics: xem charter; mỗi metric cần cách đo, nguồn và người xác nhận.

## 3. Người dùng và use case

| ID | Actor | Mục tiêu | Preconditions | Kết quả mong muốn | Liên kết |
|---|---|---|---|---|---|
| USER-001 | Chưa xác định | Chưa xác định | Chưa xác định | Chưa xác định | CHARTER- |
| UC-001 | Chưa xác định | Chưa xác định | Chưa xác định | Chưa xác định | USER-001 |

## 4. Functional Requirements

### REQ-001 (placeholder)

- Tên:
- Problem/outcome liên quan:
- Mô tả hành vi quan sát được:
- Actor:
- Điều kiện trước:
- Luồng chính:
- Luồng lỗi/edge cases:
- Dữ liệu vào/ra:
- Acceptance criteria có ID:
  - AC-001: Chưa xác định.
- Ưu tiên: Chưa xác định
- Thuộc M/Phase: Chưa xác định
- Traceability: Chưa tạo
- Trạng thái: DRAFT

Requirement thật phải kiểm chứng được, tránh mô tả implementation; nếu chưa đủ thông tin giữ DRAFT và tạo `RES`/`ASM` tương ứng.

## 5. Non-functional Requirements

| ID | Thuộc tính | Đo bằng gì | Ngưỡng/target | M/Phase | Status |
|---|---|---|---|---|---|
| NFR-001 | Performance/security/availability/usability tùy project | Chưa xác định | Chưa xác định | Chưa xác định | DRAFT |

Không ghi ngưỡng kỹ thuật không có nguồn. NFR phải có môi trường/điều kiện đo và tolerance.

## 6. Quy tắc nghiệp vụ

- `BR-001`: Chưa xác định; nếu có decision/rule phải nêu priority và conflict resolution.

## 7. Dữ liệu và tích hợp

- `DATA-001`: Chưa xác định; ghi classification, owner, retention, validation và lifecycle khi biết.
- `INT-001`: Chưa xác định; ghi contract, failure mode, retry/timeout và owner khi có integration.

## 8. Bảo mật, hiệu năng và vận hành

- `SEC-001`: Chưa xác định; trigger threat model khi có auth/dữ liệu/risk.
- `PERF-001`: Chưa xác định; nêu workload và measurement khi có target.
- `OPS-001`: Chưa xác định; liên kết deployment/monitoring/backup theo registry.

## 9. Giả định và giới hạn

- Assumption: xem `docs/01-discovery/assumptions.md`, không sao chép thành fact.
- Constraint: `CON-001` Chưa xác định.
- Open questions: xem research log.

## 10. Acceptance criteria quality gate

Mỗi criteria phải có actor/input/action/expected result hoặc điều kiện đo, có ID, không mơ hồ, có thể map tới test/evidence và nói rõ ngoài phạm vi. Requirement chỉ `VERIFIED` khi criteria bắt buộc đạt; chỉ `ACCEPTED` sau quyết định nghiệm thu.

## 11. Truy nguyên

Xem `requirements-traceability.md`. Mỗi requirement phải nối được ROADMAP → M/Phase → task → test → evidence. Nếu không thể tự động kiểm chứng, ghi lý do, cách review và Decision Log; không bỏ trống mà vẫn gọi là VERIFIED.
