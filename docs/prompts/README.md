# NewEra Prompt Guide

Đây là **thư viện prompt canonical duy nhất** của NewEra. Tất cả prompt dùng cho project adopter nằm trong file này; không tạo thêm prompt Markdown riêng trong `docs/prompts/`.

## Cách sử dụng theo quy trình

### 0. Quy tắc chung trước mọi prompt

1. Đọc `AGENTS.md`.
2. Đọc `GUIDE.md` để hiểu workflow tổng thể.
3. Đọc `docs/00-governance/document-registry.md` để biết artifact nào áp dụng.
4. Đọc `docs/00-governance/status-model.md` và `docs/03-requirements/acceptance-policy.md` khi prompt chạm status, verification, checkpoint hoặc acceptance.
5. Thay mọi placeholder `<...>` bằng ID/context của project adopter.
6. Không tự tạo `.newera/`, self-evidence, self-report hoặc machine state trong NewEra kernel.
7. Nếu thiếu dữ liệu, ghi `OPEN`, `ASSUMED` hoặc `BLOCKED`; không tự biến giả định thành fact.

### 1. Thứ tự vận hành chuẩn

```text
start-project
  -> prepare-foundation
    -> execute-milestone hoặc execute-phase
      -> verify-phase
        -> report-phase / report-milestone
          -> plan-repayment nếu còn nợ
            -> accept khi người có thẩm quyền quyết định
```

Các prompt phụ trợ `research-item`, `change-scope` và `resume-work` được gọi tại bước phù hợp; chúng không thay thế source document hoặc change-control policy.

### 2. Chọn prompt

| Bước | Prompt section | Khi dùng | Output chính |
|---|---|---|---|
| Khởi động | [Start project](#1-start-project) | Project chưa có intake rõ | Intake, charter, assumptions, research questions |
| Tài liệu nền | [Prepare foundation](#2-prepare-foundation) | Intake đủ để lập baseline | Registry, ROADMAP, SRS, Architecture, environment |
| Triển khai M | [Execute milestone](#3-execute-milestone) | Muốn chạy trọn một M | Phase artifacts, task, report, residual/debt |
| Triển khai Phase | [Execute phase](#4-execute-phase) | Chỉ chạy một Phase | requirements, `task.md`, implementation, report |
| Kiểm chứng | [Verify phase](#5-verify-phase) | Phase đã có output cần kiểm tra | Evidence/checkpoint trong `task.md` |
| Report Phase | [Report phase](#6-report-phase) | Kết thúc một Phase | Phase report và ledger updates |
| Report M | [Report milestone](#7-report-milestone) | Kết thúc một M | Milestone report và ROADMAP handoff |
| Bồi hoàn | [Plan M.x repayment](#8-plan-mx-repayment) | Còn residual/debt của M cũ | M.x plan hoặc CR cho feature mới |
| Research | [Research item](#9-research-item) | Có câu hỏi chưa rõ | RES item và decision handoff |
| Scope change | [Change scope](#10-change-scope) | Muốn đổi scope/design | CR, impact analysis, decision gate |
| Resume | [Resume work](#11-resume-work) | Công việc bị ngắt | Snapshot và next action |
| Acceptance | [Acceptance decision](#12-acceptance-decision) | Người có thẩm quyền đã review | Acceptance decision, report/ROADMAP update |

### 3. Quy tắc chuyển bước

- Không chạy `execute-*` nếu ROADMAP/requirements/dependency chưa đủ hoặc còn blocker chưa ghi.
- `task.md` là file canonical cho task, test plan, evidence và checkpoint của Phase.
- `VERIFIED` chỉ là technical verification; `CHECKPOINT_PENDING` chưa phải acceptance; chỉ role có thẩm quyền mới tạo `ACCEPTED`.
- Scope/product/architecture change phải đi qua `docs/00-governance/change-control.md` trước khi triển khai.
- Report là summary; không dùng report để thay thế evidence, task hoặc source requirement.

## 1. Start project

Bạn là NewEra Orchestrator.

1. Đọc `AGENTS.md` và các steering NewEra.
2. Đọc `docs/templates/intake-questions.md`.
3. Hỏi theo hai vòng: sản phẩm, sau đó làm rõ kỹ thuật.
4. Ghi câu trả lời vào project intake, charter và assumptions.
5. Xác định research items và tài liệu conditional trong document registry.
6. Tạo hoặc cập nhật ROADMAP, SRS và Architecture draft.
7. Báo cáo câu hỏi còn mở, blocker, giả định và tài liệu đã tạo.

Không tạo Vòng 3 về quyền tự chủ. Không viết code khi scope và tiêu chí thành công chưa đủ rõ.

## 2. Prepare foundation

Dựa trên intake đã ghi, tạo tài liệu nền theo NewEra.

- Cập nhật registry của project và đánh dấu Required/Conditional/NOT_APPLICABLE có lý do.
- Tạo hoặc cập nhật ROADMAP với M, Phase, order, dependency, risk và exit criteria.
- Tạo SRS với requirement IDs, acceptance criteria và traceability matrix trong SRS.
- Tạo Architecture, environment manifest và decision records cần thiết.
- Chỗ chưa đủ dữ liệu phải ghi `OPEN`, `ASSUMED` hoặc `BLOCKED`.
- Không viết code hoặc tạo self-artifact trong kernel.

## 3. Execute milestone

Bạn là NewEra Orchestrator. Hãy triển khai `<M-ID>` theo ROADMAP.

- Đọc AGENTS, status model, Git policy, ROADMAP, SRS, Architecture và research liên quan.
- Tạo milestone brief, requirements và task cho từng Phase; task bao gồm test plan, evidence và checkpoint.
- Kiểm tra environment manifest và dependency.
- Triển khai từng Phase theo dependency.
- Sau mỗi task logic, chạy kiểm tra phù hợp, cập nhật `task.md` và tạo commit theo Git policy.
- Sau mỗi Phase, hoàn thiện `task.md`, phase report, residual work và technical debt.
- Sau M, tạo milestone report và cập nhật ROADMAP.

Kết thúc bằng thay đổi, test, commit, evidence, blocker, residual work, debt, trạng thái kỹ thuật và acceptance status. Không đánh dấu acceptance chỉ vì test pass hoặc checkpoint tồn tại.

## 4. Execute phase

Triển khai `<M-ID>-<P-ID>` theo ROADMAP và `docs/templates/`.

- Đọc AGENTS, status model, ROADMAP, SRS, Architecture và environment manifest.
- Tạo/cập nhật Phase requirements và `task.md`; `task.md` chứa task, test plan, evidence và checkpoint.
- Làm từng task, chạy check phù hợp, cập nhật traceability và commit theo git policy.
- Không mở rộng scope; tạo CR nếu phát sinh thay đổi.
- Hoàn thiện report, residual/debt và giữ trạng thái chờ acceptance cho đến khi có decision.

## 5. Verify phase

Bạn là NewEra Verifier.

Đọc requirements và phần test plan trong `task.md` của `<M-ID>-<P-ID>`. Đối chiếu từng requirement với implementation, test và traceability. Chạy test/build/lint/typecheck phù hợp với dự án. Ghi evidence gồm command, expected, actual, commit, environment và limitations vào phần evidence của `task.md`. Cập nhật checkpoint và phase report.

Nếu lỗi: sửa nếu thuộc phạm vi hoặc ghi blocker/residual rõ ràng. Được dùng `VERIFIED` khi kiểm chứng kỹ thuật đạt. Dùng `CHECKPOINT_PENDING` khi cần xem xét. Không tự chuyển thành acceptance.

## 6. Report phase

Tạo report cho `<M-ID>-<P-ID>`.

- Đọc requirements, `task.md`, evidence sections, commit history và residual/debt.
- Tóm tắt outcome, task, test, evidence, limitation, blocker và acceptance status.
- Cập nhật `report.md` của Phase và các ledger bị ảnh hưởng.
- Không gọi checkpoint hoặc test pass là acceptance; dùng acceptance policy.

## 7. Report milestone

Tạo milestone report cho `<M-ID>`.

- Đọc ROADMAP, milestone brief, Phase reports, residual/debt và decision records.
- Tổng hợp outcome, scope deviation, verification, checkpoint, acceptance, risk và handoff.
- Cập nhật ROADMAP section và residual/debt references khi cần.
- Đề xuất M.x chỉ cho phần trả nợ outcome cũ; feature mới phải qua CR.

## 8. Plan M.x repayment

Rà soát `<M-ID>` và lập kế hoạch `<M-ID>.1` nếu cần.

- Đọc milestone report, residual-work, technical-debt và blockers.
- Nhóm item theo impact, priority, dependency và close condition.
- Chỉ đưa phần nợ outcome cũ vào M.x; feature mới tạo CR/ROADMAP change.
- Cập nhật ROADMAP và báo rõ item trả ngay, item deferred và lý do.

## 9. Research item

Nghiên cứu câu hỏi sau theo `docs/templates/research-item.md`: `<question>`.

- Tạo RES ID, owner, impact, scope, close condition và decision boundary.
- Ưu tiên nguồn chính thức; ghi version/date, method, confidence và limitation.
- Tách fact, assumption, recommendation và uncertainty.
- Nêu impact lên ROADMAP/SRS/Architecture và tạo CR/DEC/ADR nếu cần.

## 10. Change scope

Tôi muốn thay đổi: `<change>`.

- Tạo hoặc cập nhật CR theo `docs/00-governance/change-control.md`.
- Đánh giá impact lên ROADMAP, SRS, Architecture, dependency, timeline, cost, security và evidence.
- Không triển khai scope/architecture change trước khi có decision phù hợp.
- Cập nhật source documents và traceability sau khi được chấp thuận.

## 11. Resume work

Tiếp tục `<M-ID>-<P-ID>` sau khi bị ngắt.

- Đọc git log, ROADMAP, requirements, `task.md`, report và commit gần nhất.
- Xác định task nào đã xong, evidence nào có, blocker nào còn và status hiện tại.
- Báo snapshot trước khi làm tiếp.
- Không lặp lại task đã có evidence và không tự chuyển acceptance.

## 12. Acceptance decision

Quyết định cho `<M-ID>` hoặc `<M-ID>-<P-ID>`: `ACCEPTED | REJECTED | DEFERRED`.

- Lý do: `<reason>`.
- Đối chiếu evidence, checkpoint, report và acceptance criteria.
- Cập nhật acceptance status, decision log, report và ROADMAP theo policy.
- Không chuyển `CHECKPOINT_PENDING` thành `ACCEPTED` nếu thiếu role/date/reason.
