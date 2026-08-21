# Changelog

## Unreleased

## NewEra v0.2 - 2026-08-21

- Nông cấp toàn bộ template trong `docs/templates/` với checklist, owner, status, quality gate và traceability chi tiết hơn.
- Mô rộng `task.md` thành artifact hợp nhất cho task, test plan, verification evidence và checkpoint.
- Nâng cấp SRS và ROADMAP thành template project-neutral có readiness, DoR/DoD, acceptance, dependency, risk và change-control gates.
- Cập nhật milestone index, governance, agents, skills, prompts và acceptance guidance theo canonical artifact model.
- Giᯯ nguyên kernel boundary: không tạo self-execution artifacts, self-evidence, self-report hoặc machine state cho NewEra.

- Làm rõ NewEra repository là documentation/process kernel, không phải project tự chạy quy trình của chính nó.
- Tách template/guidance khỏi project-specific M/Phase, evidence, report, residual và technical-debt artifacts.
- Bổ sung hướng dẫn optional structured mode nhưng không đưa machine runtime/state vào kernel.

## NewEra v0.1

- Khởi tạo kernel quy trình NewEra.
- Thêm governance, intake, research, roadmap, SRS và architecture.
- Thêm template M/Phase, verification, evidence và report.
- Thêm Steering, Custom Agents, Skills và Hooks tối thiểu.
- Thêm `GUIDE.md` tổng hợp quy trình và thư viện prompt.
- Không định nghĩa lại chính sách quyền tự chủ của model.