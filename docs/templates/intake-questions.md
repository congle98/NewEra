# Project Intake Questions

Dùng hai vòng để thu thập đủ context trước khi lập ROADMAP. Không tự lấp chỗ trống bằng giả định; câu trả lời chưa xác nhận phải có owner và next action.

## Document control

- Intake ID/project:
- Interviewer/owner:
- Ngày mở/cập nhật:
- Stakeholders consulted:
- Trạng thái: DRAFT | IN_PROGRESS | READY | BLOCKED
- Related charter/research/decision:

## Vòng 1 - Problem, users và outcome

1. Vấn đề/cơ hội cụ thể là gì? Ai gặp và hiện giải quyết ra sao?
2. Vì sao làm bây giờ? Hậu quả nếu không làm?
3. Người dùng chính, stakeholder, sponsor và người có quyền nghiệm thu là ai?
4. Outcome phải quan sát/đo được là gì? Baseline, target, threshold và measurement source?
5. Must-have, should-have, deferred và out of scope là gì?
6. Tiêu chí thành công, thất bại/dừng, time/cost/capacity boundary là gì?
7. Dữ liệu nào có, ai sở hữu, classification/retention/privacy/legal rule nào áp dụng?

## Vòng 2 - Delivery, quality và boundary

1. Code/repository/tài sản hiện có và constraint nền tảng là gì?
2. Runtime, integration, API, database, service hoặc external actor nào liên quan?
3. Performance, scale, availability, backup/recovery, migration và compatibility cần mức nào?
4. Authentication, authorization, audit, privacy, threat và compliance concern nào đáng kể?
5. Deployment, monitoring, support, rollback và incident response ra sao?
6. Dependency, quyền truy cập, secret/config, chi phí, skill và owner nào còn thiếu?
7. Câu hỏi nào ảnh hưởng ROADMAP/SRS/Architecture và cần RES/ASM/RISK/CR?

## Answer register

| ID | Question/decision | Answer/fact | Confidence | Source | Owner | Next action/due | Status |
|---|---|---|---|---|---|---|---|
| INQ-<INQ-ID> | | | LOW/MEDIUM/HIGH | | | | OPEN |

Mỗi câu trả lời phải đánh dấu `CONFIRMED`, `ASSUMED`, `OPEN` hoặc `BLOCKED`. Không dùng `ASSUMED` làm acceptance fact nếu chưa có kế hoạch kiểm chứng.

## Intake readiness checklist

- [ ] Problem, affected users và urgency rõ.
- [ ] Outcome, baseline, target và measurement có owner.
- [ ] In/out scope và non-goals được ghi.
- [ ] Acceptance authority và stakeholder đã xác định.
- [ ] Data/privacy/security/operational concern đã sàng lọc.
- [ ] Dependency, constraint, capacity và access gap có owner.
- [ ] Open question/research/assumption có next action.
- [ ] Không chứa secret, token hoặc dữ liệu cá nhân thật.
- [ ] Có đủ đầu vào để tạo charter và draft ROADMAP, hoặc ghi BLOCKED rõ.

## Decision handoff

- Charter reference:
- ROADMAP objective/scope candidates:
- SRS questions:
- Architecture questions:
- Research items:
- Risks/blockers:
- Người phê duyệt handoff/ngày:
