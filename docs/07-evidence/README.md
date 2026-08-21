# Verification Evidence

Evidence chứng minh các kiểm tra kỹ thuật đã được thực hiện trong một project sử dụng NewEra. Evidence không tự động là nghiệm thu sản phẩm và NewEra kernel không lưu evidence của chính nó.

Mỗi evidence của project cần có:

- ID;
- M/Phase/requirement liên quan;
- commit hoặc worktree reference;
- môi trường;
- lệnh/kịch bản đã chạy;
- expected và actual output;
- kết quả và timestamp;
- phần chưa kiểm chứng, residual hoặc blocker;
- acceptance status tách riêng.

Dùng `docs/templates/task.md` làm template chính: phần **Verification evidence** trong `task.md` là nơi ghi evidence mặc định của Phase. `docs/07-evidence/` chỉ dùng cho narrative/evidence file riêng khi registry của project yêu cầu; không còn template verification-evidence độc lập trong kernel. Không tạo file `EVD-*` trong kernel chỉ để chứng minh kernel đã được review.
