# Setup Guide

Tài liệu này hướng dẫn chuẩn bị NewEra kernel hoặc project con theo manifest. Không cài dependency/runtime chỉ vì template có chỗ trống; trước hết xác định trigger trong registry.

## Prerequisites

- Repository đã clone và có quyền đọc/ghi cần thiết.
- Git khả dụng để xem diff/log và ghi worktree reference.
- Kiro/workspace nếu cần chạy skill, agent hoặc hook.
- JSON parser nếu kiểm tra `.kiro/hooks/*.json`.
- Runtime/package manager/Docker chỉ khi project con kích hoạt trong registry.

## Setup baseline kernel

1. Đọc `AGENTS.md`, `README.md`, `GUIDE.md`.
2. Kiểm tra `docs/00-governance/status-model.md`, registry, git-policy, change-control và decision-log.
3. Chạy `git status --short`, `git log -1 --oneline`, `git --version`.
4. Liệt kê `docs/` và `.kiro/`; xác nhận không có secret.
5. Parse JSON hooks bằng parser sẵn có.
6. Đọc ROADMAP để xác nhận M/Phase hiện tại; không tự chuyển DRAFT thành READY.
7. Ghi actual, timestamp, tool versions và limitation vào `setup-report.md`.

## Setup project con

1. Hoàn thiện intake/charter/assumptions/research.
2. Cập nhật registry cho tài liệu conditional bị kích hoạt.
3. Ghi runtime, package manager, lockfile, service, environment variables và command vào manifest.
4. Cài dependency theo lockfile; không dán secret vào chat hoặc repository.
5. Chạy migration/service local chỉ khi được scope/permission cho phép.
6. Tạo smoke test có expected result và evidence.

## Verification

| Check | Command/kịch bản | Expected |
|---|---|---|
| Repository | `git status`, `git log` | Có reference và diff hiểu được |
| Hooks | JSON parse toàn bộ hook files | Không lỗi parse |
| Requirements | Đối chiếu SRS/ROADMAP/registry | Không có scope âm thầm |
| Runtime project | Theo manifest | Version/service đúng constraint |
| Smoke test | Theo project test plan | Pass hoặc ghi blocker |

## Troubleshooting

- Thiếu quyền/secret/service: ghi `BLOCKED`, nhu cầu cụ thể, owner và cách tiếp tục; không giả lập thành PASS.
- Tool không áp dụng: ghi `NOT_APPLICABLE` kèm trigger chưa xảy ra.
- Dependency conflict: giữ log, ghi risk/residual và không đổi architecture âm thầm.
- Worktree đã có thay đổi: dừng trước khi ghi đè, báo phạm vi và xác nhận file liên quan.

Mọi lỗi và cách xử lý phải được ghi vào setup report, không xóa lịch sử phát hiện.
