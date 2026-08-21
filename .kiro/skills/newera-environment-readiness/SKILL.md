---
name: newera-environment-readiness
description: Chuẩn bị và đánh giá environment readiness trước M hoặc Phase bằng capability matrix, setup report, human/AI action boundary và gate ALLOW/BLOCKED. Dùng khi bắt đầu hoặc thay đổi môi trường kiểm chứng, tích hợp, vận hành hoặc release.
metadata:
  newera_layer: workflow
  newera_version: "0.2"
---

# NewEra Environment Readiness

## Purpose

Đảm bảo capability cần cho M/Phase được chuẩn bị trước mutation và verification. NewEra mô tả capability, không ép adopter dùng framework, vendor hoặc tool cụ thể.

## Required inputs

- M/Phase scope, requirements và acceptance criteria.
- M test capability profile.
- Environment manifest/capability matrix hiện có.
- Owner, dependency, version/constraint và evidence requirement.

## Procedure

1. Đọc `AGENTS.md`, roadmap, requirement/task, environment manifest và acceptance policy.
2. Liệt kê capability cần thiết theo product type, risk, requirement và expected evidence; phân loại required/conditional/not applicable có lý do.
3. Chọn adapter/tool do project adopter quản lý; ghi version/configuration, owner, setup, repeatability và limitation.
4. Tách hành động AI có thể thực hiện khỏi human-only action như credential, permission, billing, device, network, approval hoặc dữ liệu nhạy cảm.
5. Chạy setup/health/smoke check phù hợp; ghi expected, actual, command/kịch bản, timestamp và artifact.
6. Kết luận gate:
   - `ALLOW`: capability required đã sẵn sàng hoặc limitation được chấp thuận trong phạm vi.
   - `BLOCKED`: thiếu capability, quyền, dependency, dữ liệu hoặc human action cần thiết.
   - `PARTIAL`: chỉ là kết quả setup/verification, không tự là acceptance; chỉ allow khi phạm vi và limitation được ghi rõ.
7. Cập nhật readiness pack/setup report và handoff cho phase execution hoặc verification.

## Outputs and evidence

- M test capability profile.
- Environment capability matrix.
- Human setup action list và owner.
- Setup report, health/smoke result.
- Gate `ALLOW`/`BLOCKED` và blocker IDs nếu có.
- Evidence reference, limitation và next action.

## Stop conditions

Dừng mutation M/Phase khi gate `BLOCKED`, khi human-only action chưa hoàn tất, hoặc khi tool được chọn nhưng capability/evidence chưa chứng minh được. Không gọi setup `PARTIAL` là verification đầy đủ.

## Authority boundary

Environment readiness không phải product status mới và không tạo acceptance. Agent không tự cấp quyền, tạo credential, thanh toán, bypass security hoặc giả lập human approval.

## Canonical references

- `AGENTS.md`
- `docs/00-governance/automation-contract.md`
- `docs/05-environment/environment-manifest.md`
- `docs/05-environment/setup-report.md`
- `docs/templates/milestone-brief.md`
- `docs/00-governance/status-model.md`
