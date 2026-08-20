# Change Control

Không thay đổi mục tiêu, phạm vi, thứ tự M/Phase, timeline, kiến trúc hoặc acceptance criteria một cách âm thầm. Change control bảo vệ ROADMAP như nguồn sự thật; nó không phải cơ chế làm chậm các chỉnh sửa văn bản không ảnh hưởng scope.

## Phân loại thay đổi

- **Editorial:** sửa chính tả, link, format hoặc làm rõ câu không đổi nghĩa; ghi trong changelog/diff, không cần CR riêng.
- **Traceability:** bổ sung ID, evidence link, status hoặc registry entry mà không đổi mục tiêu; ghi ID liên quan và cập nhật artifact bị ảnh hưởng.
- **Scope/product:** thêm, bớt hoặc đổi outcome, requirement, acceptance criteria, M/Phase, dependency hoặc timeline; bắt buộc CR.
- **Architecture/operation:** đổi boundary, data flow, security, deployment, technology constraint hoặc operational contract; bắt buộc CR và ADR/Decision Log nếu ảnh hưởng dài hạn.

## Quy trình

1. Tạo ID tăng dần `CR-001`, `CR-002` trong phần Change Request Register bên dưới; không tái sử dụng ID.
2. Ghi nguồn phát sinh, vấn đề, đề xuất, lý do, phạm vi bị tác động và trạng thái ban đầu `PROPOSED`.
3. Đánh giá impact theo checklist: ROADMAP/M/Phase, SRS/acceptance, Architecture/ADR, registry, dependency, chi phí, timeline, security/data, test/evidence và residual/debt.
4. Ghi phương án thay thế và rủi ro của phương án không làm. Nếu thiếu dữ liệu, ghi `OPEN`, không tự đoán.
5. Người có thẩm quyền quyết định `ACCEPTED`, `REJECTED` hoặc `DEFERRED`; liên kết `DEC-xxx` nếu là quyết định lớn.
6. Chỉ sau khi được chấp thuận mới cập nhật ROADMAP và các tài liệu nguồn, sau đó tạo/điều chỉnh Phase/Task có truy nguyên.
7. Kiểm tra lại traceability và report; change không được làm mất lịch sử status hoặc evidence cũ.

## Change Request Register

| ID | Mô tả ngắn | Nguồn | Artifact ảnh hưởng | Trạng thái | Decision | Ngày |
|---|---|---|---|---|---|---|
| Chưa có | Chưa có change request được ghi nhận | — | — | — | — | — |

## Mẫu change request

```markdown
## CR-XXX: Tên thay đổi
- Phát sinh từ: RES-/RISK-/feedback-/issue-
- Loại: EDITORIAL | TRACEABILITY | SCOPE | ARCHITECTURE/OPERATION
- Mô tả hiện trạng:
- Đề xuất thay đổi:
- Lý do:
- Phương án thay thế / không làm:
- Ảnh hưởng ROADMAP/M/Phase:
- Ảnh hưởng SRS/acceptance:
- Ảnh hưởng Architecture/ADR:
- Ảnh hưởng registry, test, evidence, timeline, cost, security/data:
- Tài liệu cần cập nhật:
- Decision Log liên quan:
- Trạng thái: PROPOSED | ACCEPTED | REJECTED | DEFERRED
- Người/role quyết định:
- Ngày quyết định:
- Ghi chú triển khai và kiểm chứng:
```

Không triển khai một thay đổi `SCOPE` hoặc `ARCHITECTURE/OPERATION` chỉ vì người thực hiện cho rằng nó hợp lý; nếu chưa có quyết định, giữ `PROPOSED` và ghi blocker/residual phù hợp.
