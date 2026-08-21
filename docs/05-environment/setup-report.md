# Setup Report

- Project:
- M/Phase:
- Environment Manifest reference/version:
- Ngày:
- Máy/môi trường:
- Agent/operator:
- Commit/worktree:
- Setup result: `VERIFIED` | `PARTIAL` | `BLOCKED`
- Environment gate: `ALLOW` | `BLOCKED`
- Scope/capability profile:

Setup report là evidence của kết quả chuẩn bị thực tế cho M/Phase; không phải acceptance của product. Có thể reuse M-level setup evidence cho Phase sau nếu capability, tool/adapter, version và environment không đổi; chỉ ghi delta mới.

## Capability results

| Capability ID | Capability | Required/Conditional | Owner | Selected adapter/tool | Expected | Actual | Result | Evidence |
|---|---|---:|---|---|---|---|---|---|
| ENV-CAP-<CAP-ID> | | | AI/Human | | | | VERIFIED/PARTIAL/BLOCKED/NOT_APPLICABLE | |

`Selected adapter/tool` do project adopter chọn. Không coi một framework, MCP server, CLI hoặc service cụ thể là bắt buộc nếu manifest của project không yêu cầu.

## Human setup actions

| Action ID | Action cần con người | Vì sao AI không tự làm | Owner | Required by | Status | Completion evidence |
|---|---|---|---|---|---|---|
| ACTION-<ACTION-ID> | | Quyền/account/secret/device/approval | | | OPEN/BLOCKED/CLOSED | |

Không ghi secret, token hoặc dữ liệu cá nhân thật vào report. Chỉ ghi tên biến, secret reference hoặc nơi cấp quyền an toàn.

## AI setup actions

- Version/capability detection:
- Dependency/setup commands:
- Local service/container/emulator setup:
- Config generated from example:
- Smoke/health checks:
- Evidence/artifact references:

## Required checks

| Check ID | Check/kịch bản | Expected | Actual | Status | Limitation/blocker |
|---|---|---|---|---|---|
| TEST-<TEST-ID> | Runtime/tool detection | | | NOT_RUN/PASS/FAIL/PARTIAL | |
| TEST-<TEST-ID> | Dependency/install | | | NOT_RUN/PASS/FAIL/PARTIAL | |
| TEST-<TEST-ID> | Service/health/smoke | | | NOT_RUN/PASS/FAIL/PARTIAL | |
| TEST-<TEST-ID> | Test execution capability | | | NOT_RUN/PASS/FAIL/PARTIAL | |

## Gate decision

- Required capability unresolved:
- Blocker IDs: `ENV-ISSUE-`, `ENV-DEP-`, `BLOCKER-`, `ACTION-`
- Non-blocking limitations:
- Allowed scope if `PARTIAL`:
- Gate reason:
- Next action/owner/due:

`ALLOW` chỉ cho phép triển khai trong capability và limitation đã ghi. `BLOCKED` không được chuyển sang implementation bằng cách tự giả định setup đã xong.

## Re-check triggers

- M/Phase có capability mới:
- Runtime/dependency/service/tool/adapter version thay đổi:
- Access/secret/network/device thay đổi:
- Setup/test failure không tái hiện được:
- Deployment hoặc external integration boundary thay đổi: