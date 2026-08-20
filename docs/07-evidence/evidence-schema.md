# Evidence Schema Guide

P0 dùng hai lớp evidence có cùng ID:

1. **Machine envelope:** `.newera/evidence/EVD-*.json`, dùng cho validator/graph/gate.
2. **Human narrative:** `docs/07-evidence/EVD-*.md`, dùng giải thích context, output dài, limitation và review.

Không copy toàn bộ nội dung giữa hai lớp. JSON là owner cho metadata máy đọc; Markdown link về JSON và diễn giải kết quả.

## Required machine fields

| Field | Ý nghĩa | Rule |
|---|---|---|
| `schemaVersion` | Version envelope | Hiện tại là `1` |
| `id` | Evidence ID | `EVD-*`, trùng state reference |
| `scope` | M/Phase hoặc kernel scope | Không rỗng |
| `requirementRefs` | Requirements được chứng minh | Ít nhất một ID |
| `testRefs` | Checks/kịch bản | Ít nhất một ID |
| `type` | static/unit/integration/e2e/security/product/gate/review | Enum |
| `command` | Cách tái chạy | Không ghi “đã test” chung chung |
| `expected`/`actual` | Kết quả có thể đối chiếu | Không rỗng |
| `result` | Kết luận kỹ thuật | `VERIFIED`, `PARTIAL`, `FAILED`, `BLOCKED`, `NOT_RUN` |
| `commitRef` | Version/worktree | Git SHA hoặc `WORKTREE@SHA` |
| `timestamp` | Thời điểm | ISO-8601 |
| `environment` | OS/tool/runtime | Không chứa secret |
| `acceptanceStatus` | Acceptance riêng | Mặc định `NOT_ACCEPTED` |
| `limitations` | Phần chưa chứng minh | Array, có thể rỗng khi đầy đủ |

## Status semantics

`PASS`/`FAIL` là kết quả của từng test row; `result` là kết luận evidence-level. Evidence `VERIFIED` không tạo `ACCEPTED`. `NOT_RUN` được gate mặc định cảnh báo và strict gate chặn trước checkpoint.

## Human Markdown template

```markdown
# EVD-<...>
- Machine envelope: `.newera/evidence/EVD-<...>.json`
- Requirement IDs:
- Test IDs:
- Commit/worktree:
- Verification status:
- Acceptance status: NOT_ACCEPTED

## Interpretation
## Output and artifacts
## Limitations/residual/blocker
```

## Migration

Khi field schema thay đổi, tạo schema version mới và evidence migration note. Không sửa evidence cũ để thay đổi lịch sử kết quả.
