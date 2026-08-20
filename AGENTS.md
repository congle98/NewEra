# NewEra Project Constitution

NewEra là quy trình phát triển phần mềm ưu tiên tự động hóa, truy nguyên và nghiệm thu rõ ràng.

## Luật nền tảng

1. `docs/02-roadmap/roadmap.md` là nguồn sự thật cao nhất về phạm vi, M, Phase và thứ tự triển khai.
2. Không tự ý mở rộng phạm vi. Mọi thay đổi phải ghi vào change control và cập nhật ROADMAP.
3. Mọi yêu cầu, task, test, risk và evidence phải có ID truy nguyên được; dùng quy ước trong `docs/00-governance/status-model.md`.
4. `VERIFIED`, `CHECKPOINT_PENDING` và `ACCEPTED` là ba trạng thái khác nhau.
5. Checkpoint chưa hoàn thành không được dùng làm bằng chứng nghiệm thu.
6. Test pass là bằng chứng kiểm chứng kỹ thuật, không tự động là nghiệm thu sản phẩm.
7. Khi thiếu dữ liệu quan trọng, ghi rõ `BLOCKED`, `OPEN` hoặc `ASSUMED`; không trình bày giả định như sự thật.
8. Mỗi Phase phải có requirements, task, test-plan, verification evidence và report.
9. Mỗi M phải có milestone brief, milestone report và danh sách residual work.
10. Sau thay đổi logic, phải cập nhật test và tài liệu liên quan.
11. Sau đơn vị công việc logic đạt điều kiện, tạo Git commit mô tả được thay đổi.
12. Không lưu secret, token, mật khẩu hoặc dữ liệu cá nhân thật trong repository.
13. Chính sách an toàn và quyền thực thi của model/Kiro là lớp kiểm soát bên ngoài; NewEra không sao chép hoặc thay thế chính sách đó.

## Thứ tự đọc

1. File này và `README.md`/`GUIDE.md` để hiểu mục đích.
2. `docs/00-governance/status-model.md` để dùng đúng vocabulary/ID.
3. `docs/00-governance/git-policy.md`, `document-registry.md`, `change-control.md` và `decision-log.md`.
4. `docs/02-roadmap/roadmap.md` và `milestone-index.md`.
5. SRS, acceptance policy, traceability, Architecture và environment.
6. Tài liệu của M/Phase đang thực hiện.

## Khi kết thúc công việc

Luôn báo cáo: thay đổi, test đã chạy, commit hoặc worktree reference, phần còn thiếu, blocker, residual, evidence, trạng thái verification/checkpoint và acceptance. Không gọi `CHECKPOINT_PENDING` là nghiệm thu.
