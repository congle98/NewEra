# Residual Work

Residual work là phần đã biết nhưng chưa hoàn thành hoặc chưa đủ dữ liệu để đóng. Đây là sổ theo dõi, không phải danh sách tính năng mới. Mỗi dòng phải có nguồn, ảnh hưởng, điều kiện đóng và trạng thái.

| ID | Nguồn M/Phase | Mô tả | Ảnh hưởng | Đề xuất M/Phase | Ưu tiên | Điều kiện đóng | Trạng thái |
|---|---|---|---|---|---|---|---|
| RESID-NEWERA-001 | NewEra v0.1 | Dogfood NewEra bằng một project mẫu nhỏ | HIGH: chưa kiểm chứng quy trình trên product project | M02 sau khi P0 stable | HIGH | Có intake → roadmap → một Phase → evidence/report và retrospective | OPEN |
| RESID-NEWERA-002 | NewEra v0.1 | Chỉ thêm technology adapter khi project đầu tiên thực sự cần | MEDIUM: có thể phát sinh nhu cầu thao tác công nghệ cụ thể | M02 nếu có trigger | MEDIUM | Registry ghi trigger và adapter có requirement/evidence riêng | DEFERRED |
| RESID-NEWERA-005 | P0 hook integration | Kiểm chứng agent/skill/hook trong một phiên Kiro thực tế | MEDIUM: static gate chưa chứng minh runtime hook behavior | M01 follow-up | MEDIUM | Có log/evidence phiên Kiro hoặc blocker môi trường | OPEN |
| RESID-NEWERA-P0-001 | M01-P01 | Full JSON Schema engine/strict schema validation chưa triển khai; P0 dùng Python subset | MEDIUM: schema typo ngoài subset có thể chưa bị bắt | M01.1 | Validator contract được mở rộng hoặc limitation được chấp thuận | OPEN |
| RESID-NEWERA-P0-002 | M01-P02 | Gate chưa chạy trong CI/pre-commit; hook hiện chỉ askAgent gọi gate | HIGH: enforcement runtime chưa được chứng minh | M01.1 | Có integration runner/CI evidence và rollback path | OPEN |
| RESID-NEWERA-P1-001 | M02-P01 | Đã có `state.changes[]` và requirement version diff read-only; lifecycle workflow, CR mutation policy và phase evidence chưa hoàn tất | HIGH: CR narrative vẫn là canonical context | M02-P01 | Change workflow/schema/version diff và gate có phase evidence | PARTIAL |
| RESID-NEWERA-P1-002 | M02-P02 | Đã có graph traversal và generated verification matrix groundwork; chưa có phase-level impact policy/evidence | HIGH: matrix hiện là deterministic projection ban đầu | M02-P02 | Impact rules, matrix review và test có evidence | PARTIAL |
| RESID-NEWERA-P1-003 | M02-P03 | Đã có risk register machine fields; risk graph và LITE/STRICT enforcement đầy đủ chưa đóng | MEDIUM/HIGH theo project | M02-P03 | Risk schema, links và profile checks có evidence | PARTIAL |
| RESID-NEWERA-P1-004 | M02-P04 | Đã có deterministic ID/path drift check; semantic detector chưa chạy và chưa có precision/override policy | HIGH cho AI coding | M02-P04 | Deterministic rules + precision/override policy | PARTIAL |

## Quy tắc

1. Không âm thầm xóa residual; khi đóng phải ghi evidence hoặc link commit/decision.
2. Nếu residual ảnh hưởng tiêu chí hoàn thành, M/Phase không được chuyển sang `ACCEPTED`.
3. Hạng mục là tính năng mới phải qua change control và vào ROADMAP; không nhét vào `M01.x`.
4. `DEFERRED` cần điều kiện mở lại; `BLOCKED` cần blocker/owner; `VERIFIED` chỉ dùng khi có evidence đóng residual.
