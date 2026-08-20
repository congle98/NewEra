# ROADMAP

> Đây là nguồn sự thật cao nhất về M, Phase, phạm vi và thứ tự triển khai.

## Tầm nhìn sản phẩm

Chưa xác định. Đây là trạng thái trung thực hiện tại của intake, không phải lời mời tự suy đoán. ROADMAP chỉ được chuyển sang `READY` sau khi project intake, charter và các câu hỏi ảnh hưởng scope đã được làm rõ hoặc ghi thành `ASM`/`RES` có owner và cách xử lý.

## Quy tắc phân cấp

```text
M = kết quả lớn có ý nghĩa với sản phẩm
Phase = khối triển khai có thể kiểm chứng độc lập
Task = công việc cụ thể có output và tiêu chí hoàn thành
```

Phân chia theo giá trị sản phẩm và khả năng kiểm chứng, không chia theo lớp kỹ thuật. Một Phase có thể chứa code, test và tài liệu; không tạo M chỉ vì có thêm một module kỹ thuật.

## Milestone Index

| M | Tên | Mục tiêu | Phase | Dependency | Trạng thái | Readiness gap |
|---|---|---|---|---|---|---|
| M01 | Chưa xác định | Chưa xác định | P01 (placeholder) | Intake, charter, SRS và architecture | DRAFT | Chưa có outcome, scope, acceptance criteria và Phase thực tế |

M01/P01 là dòng khung hiện có, chưa phải cam kết triển khai. Không tạo task hoặc claim completion dựa trên dòng này cho tới khi điền đầy đủ milestone brief và được cập nhật qua change control nếu phạm vi thay đổi.

## Hợp đồng tối thiểu của một M

Mỗi M phải có: outcome đo được, in-scope/out-of-scope, Phase theo thứ tự, dependency, rủi ro có owner, acceptance criteria, tài liệu registry cần kích hoạt và điều kiện chuyển tiếp. M chỉ có thể đi từ `DRAFT` sang `READY` khi các trường này không còn `Chưa xác định` ở phần ảnh hưởng trực tiếp.

## Hợp đồng tối thiểu của một Phase

Phase phải có requirements với ID, task có output/dependency/status, test-plan với expected result, environment reference, checkpoint, evidence, report và residual/debt. Phase hoàn tất kỹ thuật ở `VERIFIED`; khi cần người xem xét thì `CHECKPOINT_PENDING`; không dùng `ACCEPTED` nếu chưa có quyết định nghiệm thu.

## Quy trình cập nhật ROADMAP

1. Đọc intake, charter, SRS, architecture và dependency hiện tại.
2. Khi phát sinh scope/architecture/timeline mới, tạo CR trước; không sửa trực tiếp để hợp thức hóa việc đã làm.
3. Sau quyết định, cập nhật ROADMAP trước khi cập nhật Phase/Task/implementation.
4. Đồng bộ `milestone-index.md`, traceability, registry và report liên quan.
5. Ghi `changed by`, ngày, CR/DEC liên quan trong commit/changelog hoặc decision record.

## Template milestone

```markdown
## MXX - Tên milestone
- Mục tiêu:
- Kết quả sản phẩm đo được:
- Phạm vi:
- Ngoài phạm vi:
- Phase và thứ tự:
- Dependency:
- Rủi ro / owner / mitigation:
- Requirement và acceptance criteria:
- Tài liệu registry cần kích hoạt:
- Tiêu chí bắt đầu (DoR):
- Tiêu chí hoàn thành (DoD):
- Dự kiến:
- CR/Decision liên quan:
- Trạng thái: DRAFT | READY | IN_PROGRESS | VERIFIED | CHECKPOINT_PENDING | ACCEPTED | BLOCKED | DEFERRED | REJECTED
```

## Quy tắc thay đổi

Thay đổi ROADMAP phải đi qua `docs/00-governance/change-control.md` và ghi Decision Log nếu là quyết định lớn. Phase không được tự ý mở rộng phạm vi. Residual hoặc `M01.x` chỉ trả nợ mục tiêu cũ; tính năng mới phải là CR và xuất hiện trong ROADMAP.
