# NewEra v0.2

NewEra là baseline quy trình phát triển phần mềm tự động hóa cho Kiro. Nó không khóa công nghệ; mỗi dự án có thể bật hoặc bỏ các tài liệu kỹ thuật theo `document-registry.md`.

Repository này là **process/documentation kernel**, không phải một project sản phẩm đang chạy NewEra. M/Phase, evidence, report, residual và machine state chỉ được tạo trong workspace của project sử dụng kernel.

Các file dưới `docs/01-discovery/` tới `docs/05-environment/` trong repository này là reference skeleton/template target. Không điền dữ liệu project vào chúng; hãy đọc [Adoption Guide](ADOPTION.md) để copy/pin chúng vào adopter workspace và quản lý version/upgrade.

## Bắt đầu

Đọc `AGENTS.md` trước để biết luật bắt buộc, sau đó đọc `docs/00-governance/GUIDE.md` để xem workflow và prompt index.

Trước khi bắt đầu project thật, đọc [Adoption Guide](ADOPTION.md) để xác định kernel release, workspace boundary, ownership và upgrade path.

Đường ngắn nhất để bắt đầu một dự án sau khi adopt:

```text
/newera-intake
```

Sau đó theo trình tự:

1. Đọc `AGENTS.md`.
2. Tạo/cập nhật `project-intake.md` trong adopter workspace từ reference template.
3. Hoàn thiện `roadmap.md`, SRS, Architecture và environment manifest trong adopter workspace.
4. Chọn M đầu tiên và dùng template trong `docs/templates/`.
5. Chạy verification trước khi chuyển Phase sang `CHECKPOINT_PENDING`.

## Nguyên tắc trạng thái

Xem `docs/00-governance/status-model.md` và `docs/03-requirements/acceptance-policy.md` để biết status, checkpoint và acceptance; README chỉ tóm tắt boundary.

## Cấu trúc chính

- `AGENTS.md`: hiến pháp dự án.
- `docs/00-governance/GUIDE.md`: quy trình vận hành và prompt index.
- `docs/prompts/README.md`: thư viện prompt canonical theo quy trình.
- `.kiro/`: Steering, agents, skills và hooks.
- `docs/`: governance, discovery, planning, requirements, architecture, environment, templates, prompt guide và guidance.
- `docs/06-execution/`, `docs/07-evidence/`, `docs/08-reports/`: chỉ chứa index/guidance trong kernel; project sử dụng kernel tạo artifact cụ thể ở workspace riêng.
- `src/`, `tests/`, `scripts/`: không thuộc kernel baseline; chỉ xuất hiện khi project adopter cần triển khai hoặc tích hợp adapter.

## Phiên bản

NewEra v0.2 là kernel tài liệu quy trình và documentation, ưu tiên tính dễ hiểu và có thể mở rộng.
