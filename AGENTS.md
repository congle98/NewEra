# NewEra Project Constitution

NewEra là quy trình phát triển phần mềm ưu tiên tự động hóa, truy nguyên và nghiệm thu rõ ràng.

## Luật nền tảng

1. `docs/02-roadmap/roadmap.md` là nguồn sự thật cao nhất về phạm vi, M, Phase và thứ tự triển khai.
2. Không tự ý mở rộng phạm vi. Mọi thay đổi phải ghi vào change control và cập nhật ROADMAP.
3. Mọi request có khả năng làm thay đổi artifact phải qua **process preflight** trước mutation. Preflight chọn `READ_ONLY`, `MICRO_CHANGE` hoặc `NORMAL_OR_SCOPE_CHANGE`; nếu thiếu dữ liệu quan trọng thì dùng `OPEN`/`BLOCKED`, không tự đoán để sửa.
4. `MICRO_CHANGE` được dùng cho thay đổi cục bộ không đổi requirement, acceptance, API, data, security, deployment hoặc architecture. Đường này được giảm ceremony nhưng không được bỏ task/request binding, scope check, targeted verification và evidence ngắn.
5. Mọi yêu cầu, task, test, risk và evidence phải có ID truy nguyên được.
6. `VERIFIED`, `CHECKPOINT_PENDING` và `ACCEPTED` là ba trạng thái khác nhau.
7. Checkpoint chưa hoàn thành không được dùng làm bằng chứng nghiệm thu.
8. Test pass là bằng chứng kiểm chứng kỹ thuật, không tự động là nghiệm thu sản phẩm.
9. Khi thiếu dữ liệu quan trọng, ghi rõ `BLOCKED`, `OPEN` hoặc `ASSUMED`; không trình bày giả định như sự thật.
10. Mỗi Phase phải có requirements, một `task.md` bao gồm test plan, verification evidence và checkpoint, cùng phase report.
11. Mỗi M phải có milestone brief, milestone report và danh sách residual work.
12. Repository NewEra chỉ giữ kernel, guidance và templates; không tự tạo M/Phase/evidence/report/status của chính kernel nếu chưa có project scope riêng.
13. Sau thay đổi logic, phải cập nhật test và tài liệu liên quan.
14. Sau đơn vị công việc logic đạt điều kiện, tạo Git commit mô tả được thay đổi.
15. Không lưu secret, token, mật khẩu hoặc dữ liệu cá nhân thật trong repository.
16. Chính sách an toàn và quyền thực thi của model/Kiro là lớp kiểm soát bên ngoài; NewEra không sao chép hoặc thay thế chính sách đó.

## Runtime map cho Kiro

`AGENTS.md` là điểm vào bắt buộc và là hiến pháp của NewEra. `.kiro/` là runtime adapter để Kiro áp dụng kernel; không phải nguồn sự thật thứ hai và không thay thế các policy trong `docs/`.

- `.kiro/steering/`: guardrail và runtime reminder áp dụng theo workspace. Giữ ngắn, không chép nguyên văn governance dài và không chứa scope sản phẩm cụ thể.
- `.kiro/skills/`: workflow có thể tái sử dụng, kích hoạt theo nhu cầu. Mỗi skill phải có `SKILL.md` hợp lệ, description nói rõ làm gì và khi nào dùng, cùng input, procedure, output, blocker và handoff.
- `.kiro/agents/`: role, tool, permission, resource và authority boundary. Agent không sở hữu policy; agent phải dẫn chiếu tới canonical documents và skill phù hợp.
- `.kiro/hooks/`: automation theo event để nhắc hoặc kiểm tra. Hook không tự chuyển scope, status hoặc acceptance nếu chưa có authority và evidence phù hợp.
- `docs/00-governance/`, ROADMAP, SRS, Architecture, acceptance policy và các template là canonical source of truth. Khi runtime guidance mâu thuẫn với canonical document, canonical document được ưu tiên và runtime guidance phải được sửa.
- Human-facing kernel guidance mặc định dùng tiếng Việt; protocol/status/field/path names giữ English khi cần tương thích. Không chèn đoạn English dài nếu không có lý do rõ.
- Kernel release/version lấy từ canonical overview và `docs/00-governance/CHANGELOG.md`; không lặp hardcoded release trong từng skill nếu không có validator đồng bộ.

Khi dùng custom agent, resources phải bao gồm `AGENTS.md`, steering cần thiết và skills liên quan bằng `file://`/`skill://`; không giả định custom agent tự nạp toàn bộ context. Agent phải tuân thủ least authority:

- `newera-orchestrator` route và dispatch, không tự làm thay builder/verifier hoặc quyết định acceptance.
- `newera-builder` chỉ mutation trong scope đã được preflight và phải cập nhật verification/evidence liên quan.
- `newera-researcher` ghi fact, assumption, recommendation, confidence và limitation; impact scope/design phải handoff CR/DEC/ADR.
- `newera-verifier` kiểm chứng theo capability profile, ghi evidence và checkpoint; không biến technical result thành acceptance.
- `newera-report-manager` tổng hợp report, residual và debt; không đổi scope, xóa lịch sử hoặc tự acceptance.

Mọi workflow `.kiro` phải giữ các invariant của NewEra: preflight trước mutation, `MICRO_CHANGE` không bỏ binding/scope check/targeted verification/evidence, environment readiness trước M/Phase, capability-first testing, phân biệt `VERIFIED`/`CHECKPOINT_PENDING`/`ACCEPTED`, human-only decision boundary và project-adopter boundary.

## Thứ tự đọc

1. File này
2. `docs/00-governance/GUIDE.md` và `docs/00-governance/ADOPTION.md` khi làm việc với adopter project
3. `docs/00-governance/status-model.md` và `document-registry.md`
4. `docs/00-governance/git-policy.md`
5. ROADMAP, SRS và Architecture
6. Tài liệu của M/Phase đang thực hiện
7. `.kiro/` runtime layer phù hợp với role/workflow đang chạy

## Khi kết thúc công việc

Luôn báo cáo: thay đổi, test đã chạy, commit, phần còn thiếu, blocker, evidence và trạng thái nghiệm thu.
