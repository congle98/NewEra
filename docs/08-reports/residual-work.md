# Residual Work

Residual work là phần đã biết nhưng chưa hoàn thành hoặc chưa đủ dữ liệu để đóng. Đây là sổ theo dõi, không phải danh sách tính năng mới. Mỗi dòng phải có nguồn, ảnh hưởng, điều kiện đóng và trạng thái.

| ID | Nguồn M/Phase | Mô tả | Ảnh hưởng | Đề xuất M/Phase | Ưu tiên | Điều kiện đóng | Trạng thái |
|---|---|---|---|---|---|---|---|
| RESID-NEWERA-001 | NewEra v0.1 | Dogfood NewEra bằng một project mẫu nhỏ | HIGH: chưa kiểm chứng quy trình trên product project | M01.1 hoặc M02 sau khi scope được xác định | HIGH | Có intake → roadmap → một Phase → evidence/report và retrospective | OPEN |
| RESID-NEWERA-002 | NewEra v0.1 | Chỉ thêm technology adapter khi project đầu tiên thực sự cần | MEDIUM: có thể phát sinh nhu cầu thao tác công nghệ cụ thể | M01.1 nếu có trigger | MEDIUM | Registry ghi trigger và adapter có requirement/evidence riêng | DEFERRED |
| RESID-NEWERA-003 | Governance audit | Chuẩn hóa từ vựng status và ID trên mọi template/artifact | HIGH: tránh hiểu sai VERIFIED/CHECKPOINT_PENDING/ACCEPTED | Documentation maintenance | HIGH | Registry, status-model, traceability và template dùng cùng quy ước | IN_PROGRESS |
| RESID-NEWERA-004 | Governance audit | Đồng bộ evidence/checkpoint/report với commit và artifact hiện hành | HIGH: evidence cũ không phủ các thay đổi sau baseline | Documentation maintenance | HIGH | Có evidence mới cho lần kiểm tra hiện tại và checkpoint không bị nhầm acceptance | OPEN |
| RESID-NEWERA-005 | Governance audit | Kiểm chứng agent/skill/hook trong một phiên Kiro thực tế | MEDIUM: static parse chưa chứng minh runtime behavior | Dogfood Phase | MEDIUM | Có log/evidence phiên Kiro hoặc ghi blocker môi trường | OPEN |

## Quy tắc

1. Không âm thầm xóa residual; khi đóng phải ghi evidence hoặc link commit/decision.
2. Nếu residual ảnh hưởng tiêu chí hoàn thành, M/Phase không được chuyển sang `ACCEPTED`.
3. Hạng mục là tính năng mới phải qua change control và vào ROADMAP; không nhét vào `M01.x`.
4. `DEFERRED` cần điều kiện mở lại; `BLOCKED` cần blocker/owner; `VERIFIED` chỉ dùng khi có evidence đóng residual.
