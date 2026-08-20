# Environment Manifest

Manifest ghi môi trường cần để đọc, thay đổi và kiểm chứng NewEra. Đây là baseline repository không có runtime ứng dụng; các tool/service của project con phải được thêm theo registry và ROADMAP, không suy ra từ kernel.

## Runtime và tools

| Tool | Version/constraint | Required | Detected/baseline | Status | Ghi chú |
|---|---|---:|---|---|---|
| Git | Có `git` và working tree hỗ trợ log/diff | Yes | Git 2.53.0 | VERIFIED | Cần commit/hash để traceability |
| Markdown reader/editor | Bất kỳ | Yes | Workspace/Kiro | OPEN | Không khóa IDE |
| JSON parser | Python standard `json` hoặc parser tương đương | Yes cho hook review | Python 3.14.4 `json` | VERIFIED | Chỉ áp dụng `.kiro/hooks/*.json` |
| Shell | POSIX-compatible khi chạy command minh họa | Conditional | Theo môi trường agent | OPEN | Ghi command thực tế trong evidence |
| Runtime ứng dụng | Theo project con | Conditional | Không có trong baseline | NOT_APPLICABLE | Kích hoạt khi có `src/`/service |
| Package manager | Theo project con | Conditional | Không có lockfile baseline | NOT_APPLICABLE | Không cài dependency cho kernel |
| Docker/container | Theo project con | Conditional | Không cần cho baseline | NOT_APPLICABLE | Kích hoạt khi deployment yêu cầu |

## Workspace layout được kiểm tra

- `AGENTS.md`, `README.md`, `GUIDE.md`: quy tắc và hướng dẫn.
- `.kiro/`: agents, skills, steering và hooks.
- `docs/`: governance, discovery, roadmap, requirements, architecture, environment, execution, evidence, reports, operations, templates, prompts.
- `src/`, `tests/`, `scripts/`: chưa có trong baseline hiện tại; không coi đây là blocker của kernel documentation.

## Services và external dependencies

| ID | Service/dependency | Required | Baseline status | Trigger |
|---|---|---:|---|---|
| ENV-SVC-001 | Không có service runtime | No | NOT_APPLICABLE | Khi project con cần DB/API/queue/cloud |
| ENV-DEP-001 | Quyền đọc/ghi repository | Yes | VERIFIED trong worktree review | Cần để cập nhật artifact và Git |
| ENV-DEP-002 | Kiro/agent invocation | Conditional | OPEN | Cần khi chạy skill, agent hoặc hook thực tế |

Không ghi credential, token hoặc endpoint private vào manifest. Nếu thiếu quyền, ghi `BLOCKED` trong setup-report.

## Commands và expected result

```text
Inspect: git status --short && git log -1 --oneline
Docs:    find docs .kiro -type f | sort
Hooks:   parse mọi file `.kiro/hooks/*.json` bằng JSON parser có sẵn
Tests:   NOT_APPLICABLE cho baseline không có test runner
Build:   NOT_APPLICABLE cho baseline không có application build
Run:     mở workspace và dùng GUIDE/skill phù hợp; không có server runtime
```

Expected của Inspect/Docs/Hooks là command chạy không lỗi và output phản ánh repository hiện tại. Mỗi lần kiểm tra phải ghi actual output hoặc summary vào evidence; không dùng `NOT_APPLICABLE` để bỏ qua một check có trigger.

## Cập nhật manifest

AI cập nhật phần phát hiện được sau mỗi thay đổi môi trường hoặc khi bắt đầu M. Tool version phải ghi giá trị thực tế, ngày kiểm tra và evidence liên quan. Phần không thể tự kiểm tra phải nằm trong `setup-report.md` với owner/hướng dẫn cụ thể.
