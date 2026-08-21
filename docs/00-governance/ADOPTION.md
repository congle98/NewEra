# NewEra Adoption Guide

Tài liệu này mô tả cách đưa NewEra kernel vào một project thật. NewEra repository là kernel; adopter workspace mới sở hữu dữ liệu project, M/Phase, status, evidence, report và acceptance decision.

## 1. Boundary

- **NewEra kernel**: governance, policy, guidance, templates, runtime adapter và release history của NewEra.
- **Adopter workspace**: intake, charter, assumptions, ROADMAP, SRS, Architecture, environment result, M/Phase, task, evidence, report, residual, debt và product decision.
- Không dùng repository kernel làm workspace để điền dữ liệu project.
- Không commit secret, credential, dữ liệu thật hoặc acceptance decision của adopter vào kernel.

Các path như `docs/01-discovery/project-intake.md`, `docs/02-roadmap/roadmap.md`, `docs/03-requirements/srs.md`, `docs/04-architecture/architecture.md` và `docs/05-environment/environment-manifest.md` trong kernel chỉ là **reference skeleton/template target**. Project adopter tạo bản sở hữu riêng trong workspace của mình.

## 2. Chọn release và transport

Adopter phải ghi kernel release/commit đang dùng trước khi bắt đầu. Có thể đưa kernel vào project bằng một trong các cách sau:

- copy/vendoring một release đã pin;
- subtree/submodule hoặc package nội bộ;
- giữ kernel ở repository riêng và tham chiếu bằng release/commit đã pin.

NewEra không ép một cơ chế phân phối. Điều kiện bắt buộc là source, release, commit và ownership phải truy nguyên được; không dùng bản `main` không pin làm baseline.

## 3. Khởi tạo adopter workspace

1. Chọn kernel release, ghi `NEWERA_VERSION` và commit/source reference trong project registry.
2. Tạo hoặc cập nhật `AGENTS.md` của adopter; dẫn về kernel guide/policy và ghi project-specific boundary.
3. Sao chép skeleton/template cần dùng từ `docs/templates/` hoặc path tương ứng trong `docs/01-discovery/`–`docs/05-environment/` của kernel vào canonical project path của adopter.
4. Copy hoặc cấu hình `.kiro/` runtime adapter; custom agents phải nạp `AGENTS.md`, steering và skills phù hợp bằng resources.
5. Tạo intake/charter/assumptions/research của project trong workspace adopter; không sửa các reference skeleton để lưu project data vào kernel.
6. Chạy local link/reference check và xác nhận registry/ROADMAP đã có owner, scope, dependency và next action.

Một workspace tối thiểu thường có:

```text
adopter-project/
├── AGENTS.md
├── .kiro/
└── docs/
    ├── 00-governance/
    ├── 01-discovery/
    ├── 02-roadmap/
    ├── 03-requirements/
    ├── 04-architecture/
    ├── 05-environment/
    ├── 06-execution/
    ├── 07-evidence/
    └── 08-reports/
```

Không phải project nào cũng cần mọi thư mục. Registry phải ghi `REQUIRED`, `CONDITIONAL` hoặc `NOT_APPLICABLE` kèm lý do và trigger.

## 4. Ownership sau khi adopt

- ROADMAP của adopter sở hữu M/Phase/scope/order.
- SRS của adopter sở hữu product requirements và acceptance criteria.
- Architecture của adopter sở hữu solution boundary/design.
- Environment Manifest của adopter sở hữu selected adapter/tool và prerequisite.
- `task.md` của adopter sở hữu task, test plan, evidence và checkpoint.
- Report/residual/debt/decision/acceptance của adopter không được ghi vào kernel.

Kernel policy có thể được tham chiếu hoặc vendored theo release, nhưng project data luôn thuộc adopter workspace.

## 5. Upgrade kernel

Khi NewEra có release mới:

1. Ghi snapshot release/commit hiện tại và project worktree.
2. Đọc kernel CHANGELOG, migration note và thay đổi source ownership/status.
3. So sánh kernel/runtime changes với adopter overrides; không overwrite project data.
4. Áp dụng thay đổi theo từng nhóm: governance → templates → `.kiro` adapter → links/reference.
5. Chạy link, schema/conformance và targeted workflow checks của project.
6. Cập nhật `NEWERA_VERSION`, commit/reference và migration evidence trong project registry.
7. Nếu thay đổi ảnh hưởng scope/design/acceptance, tạo CR/DEC/ADR trước khi áp dụng.

Rollback phải quay về release/commit đã pin trước đó và giữ migration record; không xóa lịch sử project.

## 6. Adoption gate

Adoption chỉ được coi là `READY` khi:

- kernel release/commit và source đã được ghi;
- adopter workspace không dùng kernel làm nơi lưu project state;
- registry và ownership đã rõ;
- placeholder chưa bị trình bày như project fact;
- link/reference và runtime resources resolve;
- AGENTS/steering/skills/agents giữ đúng boundary;
- scope, owner, verification plan và next action không còn `OPEN` ngoài phần đã ghi nhận.

Nếu thiếu một điều kiện, ghi `OPEN` hoặc `BLOCKED`; không tuyên bố project đã adopt hoàn chỉnh.

## Canonical references

- `AGENTS.md`
- `docs/00-governance/document-registry.md`
- `docs/00-governance/automation-contract.md`
- `docs/00-governance/status-model.md`
- `docs/00-governance/git-policy.md`
- `docs/templates/`
