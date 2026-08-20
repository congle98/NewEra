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
- **Ba trạng thái không được đánh đồng.** `VERIFIED` là đã kiểm chứng kỹ thuật. `CHECKPOINT_PENDING` là chờ xem xét và chưa hoàn thành. `ACCEPTED` là đã nghiệm thu.
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
| Việc còn nợ | `docs/08-reports/residual-work.md` |
| Template mọi loại | `docs/templates/` |
| Prompt gốc | `docs/prompts/` |

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
              -> M01
                 P01 -> task -> code -> test -> evidence -> report -> commit
                 P02 -> ...
                -> Milestone report
                  -> Residual work
                    -> M01.1 nếu cần bồi hoàn
                      -> M02
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

Hoặc dùng prompt trong [11.1](#111-khởi-động-dự-án).

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
6. requirements-traceability.md
```

### Cách chạy

Dùng prompt [11.2](#112-tạo-tài-liệu-nền). Sau khi AI tạo xong, bạn chỉ cần đọc kỹ hai file: `roadmap.md` và `srs.md`. Sai ở hai file này sẽ lan ra toàn bộ dự án.

### Quy tắc chia M

```text
M  = một kết quả lớn có ý nghĩa với sản phẩm
P  = khối triển khai kiểm chứng được độc lập
Task = việc cụ thể, có output rõ
```

Chia theo giá trị sản phẩm, không chia theo lớp kỹ thuật. `M01 Xác thực người dùng` tốt hơn `M01 Backend`.

---

## 6. Giai đoạn 3: Chuẩn bị M

Trước khi triển khai, kiểm tra ba thứ: môi trường, dependency, và tài liệu của M.

### Cách chạy

```text
Kiểm tra môi trường cho <M-ID> theo docs/05-environment/environment-manifest.md.
Ghi kết quả vào setup-report.md.
Những gì tự xử lý được thì xử lý; những gì cần tài khoản, secret,
quyền hệ thống hoặc chi phí thì ghi BLOCKED kèm hướng dẫn cụ thể cho tôi.
```

### AI thường tự làm

Kiểm tra version, cài dependency theo lockfile, tạo file cấu hình dự án, tạo Dockerfile hoặc compose, khởi động service local, chạy migration local, chạy test.

### Thường cần bạn

Cài phần mềm ở cấp hệ thống, đăng nhập cloud, tạo API key, tạo billing, cấp quyền repository, đưa secret vào `.env` hoặc secret manager, phê duyệt chi phí, quyết định pháp lý và dữ liệu thật.

Không dán secret vào chat. Đặt vào `.env` rồi nói cho AI biết tên biến.

### Đầu ra

```text
docs/06-execution/<M>/milestone-brief.md
docs/05-environment/setup-report.md
```

---

## 7. Giai đoạn 4: Triển khai Phase

Mục tiêu: chạy liên tục nhưng luôn để lại dấu vết.

### Cách chạy

Toàn bộ một M dùng prompt [11.3](#113-triển-khai-trọn-một-m). Một Phase riêng dùng [11.4](#114-triển-khai-một-phase).

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
docs/06-execution/<M>/<P>/test-plan.md
docs/06-execution/<M>/<P>/checkpoint.md
docs/07-evidence/EVD-<M>-<P>.md
docs/06-execution/<M>/<P>/report.md
```

Nếu giữa Phase phát sinh yêu cầu mới: không làm luôn. Tạo change request theo `change-control.md`, cập nhật ROADMAP nếu được chấp thuận, rồi mới triển khai.

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

Hoặc prompt [11.5](#115-kiểm-chứng-một-phase). Hook `Run NewEra Verification Review` cũng chạy được thủ công từ UI.

### Đầu ra

Evidence theo `docs/templates/verification-evidence.md`, gồm command, expected, actual, commit, environment và limitations.

Kết quả verification chỉ được ghi `VERIFIED`, `FAILED`, `PARTIAL` hoặc `BLOCKED`. Không được ghi `ACCEPTED`.

---

## 9. Giai đoạn 6: Report và nghiệm thu

### Cách chạy

```text
/newera-reporting
```

Hoặc prompt [11.6](#116-tạo-report-cho-phase-hoặc-m).

### Phase report phải trả lời

Đã làm gì, đã kiểm chứng gì bằng lệnh nào, commit nào, chưa làm gì, nợ gì, bị chặn gì, cần bạn quyết định gì, và trạng thái ba lớp.

### Nghiệm thu

Bạn đọc report và evidence, rồi trả lời một trong ba:

```text
ACCEPTED  <M-P>  - đạt, chuyển tiếp
REJECTED  <M-P>  - không đạt, kèm lý do
DEFERRED  <M-P>  - dời lại
```

AI cập nhật trạng thái và Decision Log theo quyết định đó. Trước khi bạn trả lời, trạng thái vẫn là `CHECKPOINT_PENDING`.

---

## 10. Giai đoạn 7: Bồi hoàn M.x

Sau mỗi M, đọc lại `docs/08-reports/residual-work.md` và milestone report.

### Quy tắc đặt tên

```text
M01.1   hoàn thiện, sửa lỗi, trả nợ cho M01
M01.2   vòng bồi hoàn tiếp theo của M01
M02     mục tiêu sản phẩm mới
```

Không dùng `M01.1` để lén thêm tính năng mới. Tính năng mới phải qua change control và vào ROADMAP.

### Cách chạy

Prompt [11.7](#117-tạo-m-bồi-hoàn).

---

## 11. Thư viện prompt

Copy nguyên khối, thay `<...>` bằng giá trị thật.

### 11.1 Khởi động dự án

```text
Hãy khởi động một dự án mới theo NewEra.

1. Đọc AGENTS.md và các steering NewEra.
2. Kích hoạt skill newera-intake.
3. Hỏi tôi Vòng 1 về sản phẩm, mỗi lần một nhóm câu hỏi ngắn.
4. Sau Vòng 1, hỏi Vòng 2 để làm rõ kỹ thuật.
5. Ghi câu trả lời vào project-intake.md, project-charter.md, assumptions.md.
6. Những gì tôi trả lời "chưa rõ" thì ghi thành RES item với mức ảnh hưởng.

Chưa viết code. Kết thúc bằng danh sách câu hỏi còn mở và blocker.
```

### 11.2 Tạo tài liệu nền

```text
Dựa trên intake đã ghi, hãy tạo tài liệu nền theo NewEra.

1. Cập nhật document-registry.md: tài liệu nào Required, Conditional, Not applicable, kèm lý do.
2. Tạo ROADMAP: các M, Phase trong từng M, thứ tự, dependency, rủi ro, tiêu chí hoàn thành.
3. Tạo SRS: requirement có ID, acceptance criteria kiểm chứng được, ưu tiên, thuộc M/Phase nào.
4. Tạo Architecture: thành phần, luồng dữ liệu, lưu trữ, bảo mật, logging, triển khai, quyết định lớn.
5. Cập nhật environment-manifest.md và requirements-traceability.md.
6. Ghi quyết định lớn vào decision-log.md.

Chỗ nào chưa đủ thông tin thì ghi ASSUMED hoặc OPEN, không tự nhận là sự thật.
Cuối cùng cho tôi biết có thể bắt đầu M01 hay chưa và vì sao.
```

### 11.3 Triển khai trọn một M

```text
Bạn là NewEra Orchestrator. Hãy triển khai <M-ID> theo ROADMAP.

Chuẩn bị:
- Đọc AGENTS.md, status-model, git-policy, ROADMAP, SRS, Architecture, research liên quan.
- Kiểm tra environment-manifest và dependency. Thiếu gì tự xử lý được thì xử lý,
  còn lại ghi BLOCKED kèm hướng dẫn cho tôi.
- Tạo milestone-brief cho <M-ID>.

Với từng Phase theo đúng thứ tự dependency:
- Tạo requirements.md, task.md, test-plan.md từ template.
- Triển khai từng task, chạy test liên quan, tự sửa lỗi trong phạm vi.
- Cập nhật task status và tài liệu bị ảnh hưởng.
- Commit theo git-policy sau mỗi nhóm task logic.
- Tạo verification evidence, checkpoint, report, residual work, technical debt.

Kết thúc M:
- Tạo milestone report và cập nhật ROADMAP, milestone-index, traceability.
- Đề xuất có cần <M-ID>.1 hay không.

Ràng buộc:
- Không mở rộng phạm vi ngoài ROADMAP; phát sinh thì tạo change request.
- Không đánh dấu ACCEPTED. Dùng CHECKPOINT_PENDING và chờ tôi nghiệm thu.
- Báo cáo cuối: thay đổi, test đã chạy, commit, evidence, phần còn thiếu,
  blocker, quyết định cần tôi, trạng thái từng Phase.
```

### 11.4 Triển khai một Phase

```text
Hãy triển khai <M-ID>-<P-ID> theo NewEra bằng skill newera-phase-execution.

- Đọc ROADMAP, SRS, architecture và requirements của Phase này.
- Tạo hoặc cập nhật requirements.md, task.md, test-plan.md.
- Làm từng task, chạy test, cập nhật tài liệu, commit theo git-policy.
- Tạo evidence, checkpoint và phase report.
- Ghi mọi phần chưa xong vào residual-work.md.

Dừng và báo cho tôi nếu gặp blocker cần quyết định của tôi.
Không tự đánh dấu ACCEPTED.
```

### 11.5 Kiểm chứng một Phase

```text
Bạn là NewEra Verifier. Hãy kiểm chứng <M-ID>-<P-ID>.

- Đọc requirements và test-plan của Phase.
- Đối chiếu từng acceptance criteria với implementation và test.
- Chạy test, build, lint, typecheck nếu dự án có; không có thì ghi NOT_APPLICABLE.
- Tạo evidence gồm command, expected, actual, commit, environment, limitations.
- Cập nhật traceability, checkpoint và phase report.

Lỗi trong phạm vi thì sửa rồi chạy lại. Ngoài phạm vi thì ghi blocker hoặc residual.
Kết luận chỉ được là VERIFIED, PARTIAL, FAILED hoặc BLOCKED.
```

### 11.6 Tạo report cho Phase hoặc M

```text
Hãy tạo report cho <M-ID hoặc M-ID-P-ID> theo NewEra.

- Tổng hợp task status, test đã chạy, evidence và commit history.
- Ghi rõ: đã hoàn thành, đã kiểm chứng, chưa hoàn thành, residual work,
  technical debt, blocker, risk, quyết định cần tôi.
- Cập nhật residual-work.md, technical-debt.md và CHANGELOG nếu có thay đổi đáng kể.
- Ghi trạng thái ba lớp: verification, checkpoint, acceptance.

Không che giấu phần chưa xong. Không gọi checkpoint là nghiệm thu.
```

### 11.7 Tạo M bồi hoàn

```text
Hãy rà soát <M-ID> và lập kế hoạch bồi hoàn theo NewEra.

- Đọc milestone report, residual-work.md, technical-debt.md và các blocker.
- Nhóm các hạng mục còn nợ theo mức ảnh hưởng.
- Tạo <M-ID>.1 gồm các Phase cần thiết để đóng phần còn nợ.
- Cập nhật ROADMAP và milestone-index.
- Nếu có hạng mục thực chất là tính năng mới, tạo change request thay vì nhét vào <M-ID>.1.

Cho tôi biết cái gì trả nợ ngay, cái gì nên dời và vì sao.
```

### 11.8 Nghiên cứu một vấn đề

```text
Hãy nghiên cứu vấn đề sau theo NewEra: <vấn đề>.

- Tạo RES item với câu hỏi cụ thể và mức ảnh hưởng.
- Tìm nguồn đáng tin, ưu tiên tài liệu chính thức, ghi ngày kiểm tra.
- Tóm tắt thay vì sao chép dài, kèm link.
- So sánh phương án theo tiêu chí của dự án này.
- Kết luận kèm độ tin cậy và phần chưa chắc chắn.
- Nếu là quyết định lớn, ghi vào decision-log.md.
```

### 11.9 Đổi phạm vi giữa dự án

```text
Tôi muốn thay đổi: <mô tả thay đổi>.

Theo NewEra:
- Tạo change request trong change-control.md.
- Đánh giá ảnh hưởng tới ROADMAP, SRS, Architecture, timeline và các M đang mở.
- Đề xuất phương án: thêm Phase, thêm M, hay dời việc khác.
- Chưa triển khai cho đến khi tôi xác nhận phương án.
```

### 11.10 Tiếp tục sau khi ngắt

```text
Hãy tiếp tục công việc NewEra đang dở.

- Đọc git log gần nhất, task.md, checkpoint.md và report.md của Phase đang mở.
- Xác định chính xác task nào dở, cái gì đã kiểm chứng, cái gì chưa.
- Báo cho tôi trạng thái hiện tại trước khi làm tiếp.
- Sau đó tiếp tục theo đúng thứ tự task còn lại.
```

### 11.11 Nghiệm thu

```text
<ACCEPTED | REJECTED | DEFERRED> <M-ID hoặc M-ID-P-ID>
Lý do: <lý do>

Hãy cập nhật acceptance status, checkpoint, report, decision-log
và ROADMAP theo quyết định này, rồi commit.
```

---

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
docs(newera): define roadmap and srs
chore(M01): prepare environment
feat(auth): implement email login
test(auth): cover login failure paths
verify(M01-P02): record verification evidence
docs(M01-P02): add phase report
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
- [ ] ROADMAP và milestone-index đã cập nhật
- [ ] Đã quyết định có cần `M.x` hay không
- [ ] Đã có nghiệm thu của bạn

---

## 15. Xử lý tình huống thường gặp

**AI báo xong nhưng bạn thấy chưa ổn.** Trả lời `REJECTED <M-P>` kèm lý do. AI phải mở lại Phase, ghi vào report và tạo task sửa, không được giữ nguyên trạng thái cũ.

**AI đi lệch phạm vi.** Nhắc: đọc lại ROADMAP và change-control, hoàn lại phần ngoài phạm vi hoặc chuyển thành change request.

**Test pass nhưng sản phẩm sai ý.** Đây là lỗi requirement, không phải lỗi test. Sửa acceptance criteria trong SRS trước, rồi mới sửa code.

**AI kẹt vì thiếu secret hoặc quyền.** Đúng quy trình là AI ghi `BLOCKED` và nói rõ cần gì. Bạn đưa secret vào `.env` hoặc secret manager rồi cho biết tên biến.

**Chạy dài nhiều giờ rồi mất mạch.** Dùng prompt [11.10](#1110-tiếp-tục-sau-khi-ngắt); AI dựng lại trạng thái từ git log, task và checkpoint.

**Tài liệu phình to không cần thiết.** Rà `document-registry.md`, đánh dấu `NOT_APPLICABLE` kèm lý do. NewEra không yêu cầu tạo tài liệu chỉ để cho đủ bộ.
