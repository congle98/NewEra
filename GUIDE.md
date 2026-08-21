# NewEra Guide

Hướng dẫn vận hành NewEra từ ý tưởng đến nghiệm thu. Tài liệu này là nơi tra cứu quy trình và prompt; luật bắt buộc nằm trong `AGENTS.md`.

## Mục lục

1. [Nguyên tắc cần nhớ](#1-nguyên-tắc-cần-nhớ)
2. [Bản đồ tài liệu](#2-bản-đồ-tài-liệu)
3. [Vòng đời một dự án](#3-vòng-đời-một-dự-án)
4. [Giai đoạn 1: Intake](#4-giai-đoạn-1-intake)
5. [Giai đoạn 2: Tài liệu nền](#5-giai-đoạn-2-tài-liệu-nền)
6. [Giai đoạn 3: Chuẩn bị M](#6-giai-đoạn-3-chuẩn-bị-m)
7. [Giai đoạn 4: Triển khai Phase](#7-giai-đoạn-4-triển-khai-phase)
8. [Giai đoạn 5: Verification](#8-giai-đoạn-5-verification)
9. [Giai đoạn 6: Report và nghiệm thu](#9-giai-đoạn-6-report-và-nghiệm-thu)
10. [Giai đoạn 7: Bồi hoàn M.x](#10-giai-đoạn-7-bồi-hoàn-mx)
11. [Thư viện prompt](#11-thư-viện-prompt)
12. [Agent và Skill dùng khi nào](#12-agent-và-skill-dùng-khi-nào)
13. [Git trong NewEra](#13-git-trong-newera)
14. [Checklist nhanh](#14-checklist-nhanh)
15. [Xử lý tình huống thường gặp](#15-xử-lý-tình-huống-thường-gặp)

---

## 1. Nguyên tắc cần nhớ

Bốn điều quyết định chất lượng của cả quy trình:

- **ROADMAP là nguồn sự thật.** Mọi M, Phase, task và code phải truy về được ROADMAP.
- **Status và acceptance:** xem `docs/00-governance/status-model.md` và `docs/03-requirements/acceptance-policy.md`; GUIDE chỉ mô tả workflow.
- **Không có bằng chứng thì không có kết luận.** Mỗi verification phải có command, kết quả, commit và giới hạn.
- **Phần còn thiếu phải được ghi lại.** Không im lặng bỏ qua; đưa vào residual work, technical debt hoặc blocker.

NewEra không định nghĩa quyền hạn của AI. Quyền thực thi và chính sách an toàn thuộc model/Kiro và môi trường chạy.

---

## 2. Bản đồ tài liệu

| Khi bạn cần | Mở file |
|---|---|
| Luật bắt buộc | `AGENTS.md` |
| Ý nghĩa từng trạng thái | `docs/00-governance/status-model.md` |
| Tài liệu nào cần cho dự án này | `docs/00-governance/document-registry.md` |
| Ghi quyết định lớn | `docs/00-governance/decision-log.md` |
| Đổi phạm vi | `docs/00-governance/change-control.md` |
| Quy tắc commit | `docs/00-governance/git-policy.md` |
| Câu hỏi intake | `docs/templates/intake-questions.md` |
| Định hướng M/Phase | `docs/02-roadmap/roadmap.md` |
| Yêu cầu sản phẩm | `docs/03-requirements/srs.md` |
| Quy tắc nghiệm thu | `docs/03-requirements/acceptance-policy.md` |
| Thiết kế hệ thống | `docs/04-architecture/architecture.md` |
| Môi trường và lệnh | `docs/05-environment/environment-manifest.md` |
| Hồ sơ M/Phase đang làm | `docs/06-execution/<M>/` |
| Bằng chứng kiểm chứng | `docs/07-evidence/` |
| Việc còn nợ | `docs/templates/residual-work.md` và bản project trong `docs/08-reports/` |
| Template mọi loại | `docs/templates/` |
| Prompt gốc | `docs/prompts/README.md` |

---

## 3. Vòng đời một dự án

```text
Ý tưởng
  -> Intake (hỏi 2 vòng)
    -> Charter + Assumptions + Research
      -> Document Registry
        -> ROADMAP  (M, Phase, thứ tự)
          -> SRS + Architecture
            -> Environment check
              -> <M>
                 <P> -> task -> implementation -> test -> evidence -> report -> commit
                 <P> -> ...
                -> Milestone report
                  -> Residual work
                    -> <M>.1 nếu cần bồi hoàn
                      -> M tiếp theo
```

Con người tham gia ở ba điểm: cung cấp ý tưởng và quyết định sản phẩm, cấp thông tin/quyền không thể tự lấy, và nghiệm thu.

---

## 4. Giai đoạn 1: Intake

Mục tiêu: hiểu đúng bài toán trước khi viết dòng code nào.

### Cách chạy

Gõ skill:

```text
/newera-intake
```

Hoặc dùng prompt tương ứng trong `docs/prompts/README.md`.

### AI sẽ hỏi hai vòng

Vòng 1 về sản phẩm: vấn đề, người dùng, kết quả thành công, bắt buộc phải có, không làm, ràng buộc, dữ liệu, tiêu chí nghiệm thu.

Vòng 2 làm rõ: tài sản hiện có, yêu cầu hiệu năng/bảo mật/pháp lý/vận hành, migration, backup, monitoring, rollback, và những điều chưa biết có thể ảnh hưởng ROADMAP.

### Đầu ra

```text
docs/01-discovery/project-intake.md
docs/01-discovery/project-charter.md
docs/01-discovery/assumptions.md
docs/01-discovery/research.md
```

### Điều kiện chuyển giai đoạn

Câu hỏi ảnh hưởng phạm vi hoặc kiến trúc đã có câu trả lời, hoặc đã được ghi thành `ASM-xxx` và `RES-xxx` với mức ảnh hưởng rõ ràng. Nếu bạn chưa biết câu trả lời, cứ nói "chưa rõ" để AI ghi vào research thay vì tự đoán.

---

## 5. Giai đoạn 2: Tài liệu nền

Mục tiêu: chốt định hướng để AI có thể chạy dài mà không lệch.

### Thứ tự tạo

```text
1. document-registry.md   (dự án này cần những tài liệu nào)
2. roadmap.md             (M, Phase, thứ tự, tiêu chí hoàn thành)
3. srs.md                 (requirement có ID và acceptance criteria)
4. architecture.md        (thành phần, dữ liệu, bảo mật, triển khai)
5. environment-manifest.md
6. SRS §11 traceability matrix
```

### Cách chạy

Dùng section **2. Prepare foundation** trong `docs/prompts/README.md`. Sau khi AI tạo xong, bạn chỉ cần đọc kỹ hai file: `roadmap.md` và `srs.md`. Sai ở hai file này sẽ lan ra toàn bộ dự án.

### Quy tắc chia M

```text
M  = một kết quả lớn có ý nghĩa với sản phẩm
P  = khối triển khai kiểm chứng được độc lập
Task = việc cụ thể, có output rõ
```

Chia theo giá trị sản phẩm, không chia theo lớp kỹ thuật. `<M-ID> Kết quả người dùng` tốt hơn `<M-ID> Backend`.

---

## 6. Giai đoạn 3: Chuẩn bị M

Trước mỗi M, project phải hoàn thiện **M Environment Readiness Pack**. Đây là gate trước mutation, không phải một Phase kỹ thuật mới.

### Thứ tự chuẩn bị

```text
M trong ROADMAP
  -> M test capability profile
    -> environment capability matrix
      -> human setup actions + AI setup actions
        -> setup report + smoke/health checks
          -> environment gate: ALLOW | BLOCKED
            -> bắt đầu Phase/task
```

### AI phải rà soát

- Capability/runtime/dependency nào M cần.
- Lớp kiểm chứng nào áp dụng: static, unit/component, integration, API/contract, UI/client, accessibility/usability, visual, performance/load, security/operations hoặc human review.
- Adapter/tool nào project adopter đã chọn và version/config cần dùng.
- Setup command, smoke test, evidence artifact và limitation.
- Môi trường nào có thể reuse từ M/Phase trước và trigger nào buộc phải kiểm tra lại.

### AI có thể tự làm

Kiểm tra version, cài dependency theo lockfile, khởi động local dependency được phép, tạo config từ example không chứa secret, chạy smoke test và thu thập evidence.

### Cần con người hoặc quyền ngoài agent

Cài software cấp hệ thống, cấp account/permission, secret/API key, cloud resource/billing, VPN/network, device lab, dữ liệu thật, approval security/compliance hoặc quyết định chi phí. AI phải ghi rõ owner, lý do, quyền cần cấp và điều kiện hoàn tất; không tự giả định đã có.

### Environment gate

- `ALLOW`: required capability đã đủ hoặc limitation được giới hạn rõ.
- `BLOCKED`: thiếu capability bắt buộc, quyền, secret, service, device hoặc approval; không bắt đầu mutation.
- Setup result `VERIFIED | PARTIAL | BLOCKED` phải được ghi trong `setup-report.md`.

Mỗi M không cần dùng mọi capability hoặc mọi adapter. `NOT_APPLICABLE` phải có lý do; `PARTIAL` chỉ được tiếp tục trong phạm vi đã ghi.

### Đầu ra

```text
docs/06-execution/<M>/milestone-brief.md
docs/05-environment/environment-manifest.md
docs/05-environment/setup-report.md
docs/06-execution/<M>/<P>/task.md  (test capability profile + evidence)
```

---

## 7. Giai đoạn 4: Triển khai Phase

Mục tiêu: chạy liên tục nhưng luôn để lại dấu vết.

### Cách chạy

Toàn bộ một M dùng section **3. Execute milestone**; một Phase riêng dùng section **4. Execute phase** trong `docs/prompts/README.md`.

### Vòng lặp của AI

```text
Đọc requirements + architecture
  -> kiểm tra dependency
    -> làm một task
      -> chạy test liên quan
        -> cập nhật task + tài liệu
          -> commit nếu đạt điều kiện
            -> task tiếp theo
```

### Mỗi Phase phải có

```text
docs/06-execution/<M>/<P>/requirements.md
docs/06-execution/<M>/<P>/task.md
  ├── task list
  ├── test plan and verification matrix
  ├── verification evidence
  └── checkpoint and review
docs/06-execution/<M>/<P>/report.md
```

Nếu giữa Phase phát sinh yêu cầu mới: phân loại trước. Nếu là `MICRO_CHANGE` cục bộ, không đổi requirement, acceptance, API, data, security, deployment hoặc architecture, bind vào task/request hiện có, ghi path boundary, chạy targeted test và evidence ngắn; không tạo full Phase artifact chỉ vì thay đổi nhỏ. Nếu là `NORMAL_OR_SCOPE_CHANGE`, không làm luôn: tạo change request theo `change-control.md`, cập nhật ROADMAP nếu được chấp thuận, rồi mới triển khai.

---

## 8. Giai đoạn 5: Verification

Bốn lớp, AI tự động ba lớp đầu.

```text
Lớp 1  Static      format, lint, typecheck, dependency audit, secret scan
Lớp 2  Test        unit, integration, contract, e2e nếu có
Lớp 3  Product     đối chiếu từng acceptance criteria trong SRS
Lớp 4  Acceptance  bạn xem sản phẩm và quyết định
```

### Cách chạy

```text
/newera-verification
```

Hoặc dùng section **5. Verify phase** trong `docs/prompts/README.md`. Hook `Run NewEra Verification Review` cũng chạy được thủ công từ UI.

### Đầu ra

Evidence theo phần **Verification evidence** trong `docs/templates/task.md`, gồm command, expected, actual, commit, environment và limitations.

Kết quả verification chỉ được ghi `VERIFIED`, `FAILED`, `PARTIAL` hoặc `BLOCKED`. Không được ghi `ACCEPTED`.

---

## 9. Giai đoạn 6: Report và nghiệm thu

### Cách chạy

```text
/newera-reporting
```

Hoặc dùng section **6. Report phase** hoặc **7. Report milestone** trong `docs/prompts/README.md`.

### Phase report phải trả lời

Đã làm gì, đã kiểm chứng gì bằng lệnh nào, commit nào, chưa làm gì, nợ gì, bị chặn gì, cần bạn quyết định gì, và trạng thái ba lớp.

### Nghiệm thu

Bạn đọc report và evidence, rồi trả lời một trong ba:

```text
ACCEPTED  <M-P>  - đạt, chuyển tiếp
REJECTED  <M-P>  - không đạt, kèm lý do
DEFERRED  <M-P>  - dời lại
```

AI cập nhật trạng thái và Decision Log theo `docs/03-requirements/acceptance-policy.md`; trước quyết định, giữ trạng thái chờ xem xét.

---

## 10. Giai đoạn 7: Bồi hoàn M.x

Sau mỗi M, project adopter đọc bản residual work trong `docs/08-reports/` được tạo từ `docs/templates/residual-work.md`, cùng với milestone report.

### Quy tắc đặt tên

```text
<M>.1   hoàn thiện, sửa lỗi, trả nợ cho <M>
<M>.2   vòng bồi hoàn tiếp theo của <M>
<M-next> mục tiêu sản phẩm mới
```

Không dùng `<M-ID>.1` để lén thêm tính năng mới. Tính năng mới phải qua change control và vào ROADMAP.

### Cách chạy

Dùng section **8. Plan M.x repayment** trong `docs/prompts/README.md`.

---

## 11. Thư viện prompt

Prompt canonical duy nhất: [`docs/prompts/README.md`](docs/prompts/README.md). File này chứa cách dùng theo quy trình và toàn bộ prompt từ intake tới acceptance.

| Giai đoạn | Section trong prompt guide |
|---|---|
| Intake → foundation | 1–2 |
| M/Phase execution | 3–4 |
| Verification → reports | 5–7 |
| Repayment/research/change/resume/acceptance | 8–12 |

## 12. Agent và Skill dùng khi nào

| Tình huống | Dùng |
|---|---|
| Điều phối cả M, nhiều Phase | agent `newera-orchestrator` |
| Chưa rõ công nghệ, cần so sánh, cần nguồn | agent `newera-researcher` + `/newera-research` |
| Viết code, sửa code, cập nhật test | agent `newera-builder` |
| Đối chiếu requirement, chạy test, tạo evidence | agent `newera-verifier` + `/newera-verification` |
| Tổng hợp report, residual, changelog | agent `newera-report-manager` + `/newera-reporting` |
| Bắt đầu dự án mới | `/newera-intake` |
| Dựng hoặc sửa ROADMAP | `/newera-roadmap` |
| Chạy một Phase từ đầu đến report | `/newera-phase-execution` |

Skill nạp theo ngữ cảnh nên gọi đúng skill giúp tiết kiệm context hơn là dán cả quy trình vào chat.

---

## 13. Git trong NewEra

### Format

```text
<type>(<scope>): <description>
```

`feat`, `fix`, `test`, `docs`, `chore`, `refactor`, `verify`, `wip`.

### Ví dụ

```text
docs(<M-ID>): define roadmap and srs
chore(<M-ID>): prepare environment
feat(<scope>): implement feature
test(<scope>): cover failure paths
verify(<M-ID>-<P-ID>): record verification evidence
docs(<M-ID>-<P-ID>): add phase report
```

### Mốc nên commit

Tài liệu nền, mỗi nhóm task logic, Phase đã verification, evidence và report, milestone report, cập nhật residual work.

### Lưu ý

`wip` chỉ để lưu trạng thái giữa đường, không phải bằng chứng hoàn thành. Không commit secret. Branch gợi ý: `newera/<M-ID>` hoặc `newera/<M-ID>-<P-ID>`, và giữ bảo vệ cho nhánh chính.

---

## 14. Checklist nhanh

### Trước khi bắt đầu một Phase

- [ ] Phase có trong ROADMAP
- [ ] Requirements có acceptance criteria kiểm chứng được
- [ ] Dependency đã xong hoặc đã biết cách xử lý
- [ ] Môi trường đã kiểm tra
- [ ] Test plan đã có
- [ ] Không còn blocker nghiêm trọng

### Trước khi coi Phase là xong về kỹ thuật

- [ ] Task cần thiết đã hoàn thành
- [ ] Test đã chạy và ghi kết quả
- [ ] Build/lint/typecheck đạt, hoặc ghi rõ không áp dụng
- [ ] Tài liệu và traceability đã cập nhật
- [ ] Evidence đã tạo
- [ ] Residual work và debt đã ghi
- [ ] Report đã tạo
- [ ] Commit đã có
- [ ] Trạng thái ghi là `CHECKPOINT_PENDING`, không phải `ACCEPTED`

### Trước khi đóng một M

- [ ] Mọi Phase có report
- [ ] Milestone report đã tạo
- [ ] Residual work đã tổng hợp
- [ ] ROADMAP §3 milestone index đã cập nhật
- [ ] Đã quyết định có cần `M.x` hay không
- [ ] Đã có nghiệm thu của bạn

---

## 15. Xử lý tình huống thường gặp

**AI báo xong nhưng bạn thấy chưa ổn.** Trả lời `REJECTED <M-P>` kèm lý do. AI phải mở lại Phase, ghi vào report và tạo task sửa, không được giữ nguyên trạng thái cũ.

**AI đi lệch phạm vi.** Nhắc: đọc lại ROADMAP và change-control, hoàn lại phần ngoài phạm vi hoặc chuyển thành change request.

**Test pass nhưng sản phẩm sai ý.** Đây là lỗi requirement, không phải lỗi test. Sửa acceptance criteria trong SRS trước, rồi mới sửa code.

**AI kẹt vì thiếu secret hoặc quyền.** Đúng quy trình là AI ghi `BLOCKED` và nói rõ cần gì. Bạn đưa secret vào `.env` hoặc secret manager rồi cho biết tên biến.

**Chạy dài nhiều giờ rồi mất mạch.** Dùng section **11. Resume work** trong `docs/prompts/README.md`; AI dựng lại trạng thái từ git log, task và checkpoint.

**Tài liệu phình to không cần thiết.** Rà `document-registry.md`, đánh dấu `NOT_APPLICABLE` kèm lý do. NewEra không yêu cầu tạo tài liệu chỉ để cho đủ bộ.
