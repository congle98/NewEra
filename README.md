# NewEra Kernel

NewEra là process/documentation kernel dùng để tổ chức quy trình phát triển phần mềm
theo hướng có scope, traceability, verification và acceptance rõ ràng.

Repository này chứa kernel, governance, guidance, templates và runtime instructions.
Đây không phải repository của một project sản phẩm và không chứa M/Phase/evidence/report
cụ thể của project adopter.

## Bắt đầu

1. Đọc [AGENTS.md](AGENTS.md) để biết các luật bắt buộc.
2. Đọc [Kernel overview](docs/00-governance/README.md).
3. Đọc [Kernel guide](docs/00-governance/GUIDE.md).
4. Đọc [Adoption Guide](docs/00-governance/ADOPTION.md) trước khi đưa NewEra vào project thật.
5. Dùng [prompt library](docs/prompts/README.md) khi bắt đầu hoặc tiếp tục workflow.

## Canonical documents

- [Kernel overview](docs/00-governance/README.md)
- [Kernel guide](docs/00-governance/GUIDE.md)
- [Adoption Guide](docs/00-governance/ADOPTION.md)
- [Document registry](docs/00-governance/document-registry.md)
- [Automation contract](docs/00-governance/automation-contract.md)
- [Status model](docs/00-governance/status-model.md)
- [Acceptance policy](docs/03-requirements/acceptance-policy.md)
- [Kernel changelog](docs/00-governance/CHANGELOG.md)

## Boundary

Project adopter tạo README, CHANGELOG, M/Phase, requirements, task, evidence,
report và các artifact sản phẩm trong workspace của project đó. Các baseline path
trong `docs/01-discovery/` tới `docs/05-environment/` của repository này chỉ là
reference skeleton; không điền project data vào kernel. Xem [Adoption Guide](docs/00-governance/ADOPTION.md)
để biết cách copy/pin/upgrade.
NewEra kernel không tự tạo các artifact project-specific của chính nó.
