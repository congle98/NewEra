# Research Log

Research log chứa câu hỏi chưa biết và kết luận dựa trên nguồn. Research không phải nơi sao chép tài liệu hoặc quyết định thay cho người có thẩm quyền.

## Research register

| ID | Câu hỏi/vấn đề | Ảnh hưởng | Owner | Trạng thái | Kết luận/decision |
|---|---|---|---|---|---|
| RES-000 | Cần xác định phạm vi, user, outcome và các constraint của project | CRITICAL | Người đề xuất | OPEN | Chưa có dữ liệu |

## Mẫu research item

```markdown
## RES-XXX: Câu hỏi cụ thể
- Phát sinh từ: INTAKE-/ASM-/RISK-/REQ-
- Vấn đề và phạm vi:
- Mức ảnh hưởng: LOW | MEDIUM | HIGH | CRITICAL
- Câu hỏi có thể trả lời được:
- Các phương án/giả thuyết:
- Tiêu chí so sánh:
- Nguồn chính thức/nguồn tham khảo:
- Ngày kiểm tra:
- Kết luận tóm tắt:
- Độ tin cậy: LOW | MEDIUM | HIGH
- Phần chưa chắc chắn:
- Ảnh hưởng ROADMAP/SRS/Architecture/registry:
- Decision Log/CR/ADR cần tạo:
- Owner và next action:
- Trạng thái: OPEN | IN_PROGRESS | RESOLVED | BLOCKED | DEFERRED
```

## Quy tắc chất lượng

- Câu hỏi phải cụ thể đủ để người khác tái kiểm tra; tránh “nghiên cứu công nghệ X” không có tiêu chí.
- Ưu tiên nguồn chính thức, ghi URL/version/ngày kiểm tra; không truyền secret hoặc dữ liệu riêng tư ra ngoài.
- Tóm tắt/paraphrase thay vì sao chép dài. Phân biệt fact, inference và recommendation.
- Thông tin có thể thay đổi phải có ngày kiểm tra và điều kiện hết hạn.
- Research chưa giải quyết không được trình bày như quyết định cuối cùng.
- Vấn đề ảnh hưởng phạm vi, chi phí, pháp lý hoặc bảo mật phải liên kết tới CR/Decision/ADR trước khi triển khai.
