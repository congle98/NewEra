# EVD-NEWERA-DOCS-001 - Documentation Review Evidence

- Evidence ID: EVD-NEWERA-DOCS-001
- Scope: Documentation/governance enrichment for NewEra v0.1
- Requirements: NFR-NEWERA-001, NFR-NEWERA-002, NFR-NEWERA-003, NFR-NEWERA-004, NFR-NEWERA-005
- Task IDs: TASK-NEWERA-DOC-001
- Baseline HEAD: `2c39b013f71871a3b4316e8254b37f0bdae1c3e8`
- Worktree: documentation changes uncommitted; evidence describes the current worktree, not a future commit
- Environment: Linux, Git 2.53.0, Python 3.14.4
- Agent/operator: Kiro
- Timestamp: 2026-08-20T20:11:47+07:00
- Verification status: PARTIAL
- Acceptance status: NOT_ACCEPTED

## Commands and results

| Check ID | Command/kịch bản | Expected | Actual | Status |
|---|---|---|---|---|
| TEST-NEWERA-DOCS-001 | `python3` với `json.loads` trên `sorted(Path('.kiro/hooks').glob('*.json'))` | Mọi hook parse được | 3/3 files `JSON_OK` | PASS |
| TEST-NEWERA-DOCS-002 | `test -f` cho 19 canonical artifacts trong governance/roadmap/requirements/architecture/environment/execution/evidence/report | Đủ file bắt buộc | 19/19 file tồn tại | PASS |
| TEST-NEWERA-DOCS-003 | Python scan legacy residual/debt/evidence IDs và path registry cũ, loại trừ mô tả check của evidence | Không còn token cũ trong artifact | Không phát hiện token stale | PASS |
| TEST-NEWERA-DOCS-004 | Python scan status terms trong status-model/acceptance-policy/checkpoint | Có `VERIFIED`, `CHECKPOINT_PENDING`, `ACCEPTED`, `NOT_ACCEPTED`; không đánh đồng | Đủ terms; acceptance không bị suy ra từ verification | PASS |
| TEST-NEWERA-DOCS-005 | `git -c core.whitespace=cr-at-eol diff --check` | Không trailing whitespace/error, coi CRLF là line ending hợp lệ của repository | Exit 0 | PASS |
| TEST-NEWERA-DOCS-006 | `grep -RInE 'AKIA...|BEGIN ... PRIVATE KEY|autonomy-policy' --exclude-dir=.git .` | Không có secret/private key/policy thay thế | Không phát hiện token cấm | PASS |
| TEST-NEWERA-DOCS-007 | Đối chiếu `docs/06-execution/README.md`, registry và evidence README | Phase evidence dùng `docs/07-evidence`; baseline exception được khai báo | Canonical path nhất quán; conditional targets chưa tạo và được ghi trigger | PARTIAL |

## Re-run snippets

```bash
python3 - <<'PY'
import json
from pathlib import Path
for path in sorted(Path('.kiro/hooks').glob('*.json')):
    json.loads(path.read_text())
    print(path, 'JSON_OK')
PY

git -c core.whitespace=cr-at-eol diff --check

grep -RInE '(^|[[:space:]])(AKIA[0-9A-Z]{16}|-----BEGIN (RSA|OPENSSH|EC) PRIVATE KEY-----|autonomy-policy)' --exclude-dir=.git .
```

The final grep is expected to return no matches. Conditional registry paths are intentionally not created until their documented trigger occurs.

## Artifacts

- `docs/00-governance/status-model.md`
- `docs/00-governance/document-registry.md`
- `docs/00-governance/change-control.md`
- `docs/00-governance/decision-log.md`
- `docs/02-roadmap/roadmap.md`
- `docs/03-requirements/acceptance-policy.md`
- `docs/03-requirements/requirements-traceability.md`
- `docs/04-architecture/architecture.md`
- `docs/05-environment/environment-manifest.md`
- `docs/06-execution/README.md`
- `docs/08-reports/CHK-NEWERA-V01.md`
- `docs/08-reports/residual-work.md`
- `docs/08-reports/technical-debt.md`
- `docs/templates/`

## Limitations and residual

- Chưa chạy agent/skill/hook trong một phiên Kiro runtime; đây là `RESID-NEWERA-005`/`DEBT-NEWERA-002`.
- Chưa có project-specific intake/scope, runtime, tests hoặc deployment; M01/P01 vẫn `DRAFT`.
- Các target path conditional trong registry chưa phải file thực tế; chỉ tạo khi trigger xuất hiện.
- Không có commit mới; reviewer phải kiểm tra worktree diff trước khi commit.

> Evidence này chứng minh review kỹ thuật của documentation worktree, không phải nghiệm thu NewEra. Acceptance vẫn `NOT_ACCEPTED`.
