# MXX-PXX - Test Plan

- Phase:
- Requirement scope:
- Owner/agent:
- Environment reference: `docs/05-environment/environment-manifest.md`
- Trạng thái: DRAFT

## Verification matrix

| ID | Loại | Requirement/criteria | Lệnh/kịch bản | Kết quả mong đợi | Kết quả thực tế | Artifact/output | Status |
|---|---|---|---|---|---|---|---|
| TEST-MXX-PXX-001 | Static/format | REQ-/AC- | Chưa xác định | Không lỗi | | | NOT_RUN |
| TEST-MXX-PXX-002 | Unit/integration | REQ-/AC- | Chưa xác định | Pass | | | NOT_RUN |
| TEST-MXX-PXX-003 | Build/lint/type | REQ-/AC- | Chưa xác định hoặc N/A | Pass hoặc lý do N/A | | | NOT_RUN |
| TEST-MXX-PXX-004 | Product/acceptance mapping | REQ-/AC- | Đối chiếu từng criteria | Có evidence tương ứng | | | NOT_RUN |
| TEST-MXX-PXX-005 | Secret/dependency audit | REQ-/SEC- | Theo tool khả dụng | Không phát hiện secret/risk ngoài ngưỡng | | | NOT_RUN |

## Quy tắc kết quả

- `PASS`: expected và actual khớp.
- `FAIL`: actual không đạt; sửa trong phạm vi hoặc ghi blocker/residual.
- `PARTIAL`: chỉ một phần criteria/check đạt; phải nêu phần thiếu.
- `NOT_APPLICABLE`: chỉ dùng khi trigger không tồn tại và ghi lý do trong evidence.
- `NOT_RUN`: chưa được dùng làm cơ sở chuyển `VERIFIED`.

## Tiêu chí fail

Nêu ngưỡng fail, lỗi chặn release/checkpoint, flaky behavior, dữ liệu test, cleanup và cách tái chạy. Không dùng test pass để tự suy ra nghiệm thu sản phẩm.

## Môi trường kiểm thử

- Commit/worktree:
- OS/tool versions:
- Fixture/seed/test account:
- External services/feature flags:
- Reproducibility notes:

## Ghi chú và traceability

Mỗi check phải liên kết một hoặc nhiều requirement/criteria, task và evidence. Nếu command khác với manifest, ghi lý do và cập nhật manifest/CR nếu cần.
