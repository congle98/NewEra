# Automation Contract

Tài liệu này định nghĩa contract giữa Markdown, machine-readable state, evidence envelope và deterministic gate.

## Source ownership

Mỗi fact machine-relevant chỉ có một owner:

| Fact | Owner | Markdown role | Gate behavior |
|---|---|---|---|
| M/Phase/scope/order | `docs/02-roadmap/roadmap.md` | Narrative/source of truth | Reject state không khớp ROADMAP IDs/scope |
| Lifecycle status/reference/edge | `.newera/project-state.json` | Hiển thị/giải thích | Validate schema, enum và resolvability |
| Requirement meaning/criteria | SRS Markdown + requirement IDs | Detailed human contract | Reject requirement thiếu criteria/reference |
| Verification metadata/result | `.newera/evidence/*.json` | Markdown evidence là narrative | Reject thiếu command/expected/actual/result |
| Acceptance decision | Acceptance Policy + Decision Log | Human decision record | Không auto-create `ACCEPTED` |
| Gate policy | `.newera/governance-profiles.json` | Profile documentation | Apply required roles/links |

Không cập nhật hai nơi độc lập cho cùng một status/reference. Nếu cần hiển thị trong Markdown, ghi link hoặc generated projection; consistency mismatch là gate error.

## Schema/version policy

- `schemaVersion: 1` là version contract, không phải product version.
- Breaking change phải tạo schema version mới và migration note; không âm thầm đổi field.
- Unknown field bị validator từ chối ở machine envelope để tránh typo im lặng.
- JSON được chọn cho P0 vì repository đã có JSON parser contract và không cần thêm YAML dependency. YAML chỉ được dùng khi environment manifest khai báo parser tương ứng.

## Profile policy

P0 triển khai `STANDARD` baseline. `LITE` và `STRICT` mới là profile contract, chưa phải runtime adaptive implementation.

Profile chỉ điều chỉnh artifact/check bắt buộc; không profile nào được:

- bỏ ROADMAP khỏi scope governance;
- đánh đồng `VERIFIED`, `CHECKPOINT_PENDING`, `ACCEPTED`;
- bỏ ghi nhận residual/blocker;
- tự tạo acceptance;
- cho phép reference không resolve.

## Gate contract

```text
0  = structural PASS hoặc WARN không blocking
1  = FAIL: reference/status/completeness/profile violation

Default: NOT_RUN là WARN để cho phép state IN_PROGRESS.
Strict: NOT_RUN là FAIL trước checkpoint.
```

Gate hiện tại dùng `scripts/newera_validate.py`. Hook Kiro có thể gọi hoặc nhắc chạy gate; prompt/askAgent không thay thế exit code deterministic.

P1 bổ sung machine records và các projection deterministic nhưng không tạo source of truth thứ hai:

- `state.changes[]` giữ change ID, status, affected IDs và decision reference; Change Control Markdown vẫn giữ narrative/decision context.
- `state.risks[]` giữ risk metadata/link tối thiểu; risk graph dùng cùng traceability edges.
- `scripts/newera_change.py` so sánh requirement giữa hai state versions; output là projection read-only cho CR, không tự ghi change record hay acceptance.
- `scripts/newera_impact.py` traverse downstream typed edges để báo cáo impacted entities; không tự thay đổi state.
- `scripts/newera_matrix.py` sinh verification matrix từ requirement → task → test → evidence, không duy trì bảng độc lập.
- `scripts/newera_drift.py` kiểm tra deterministic changed IDs/path scope; semantic layer chỉ in advisory và không đổi exit code.

Các command P1:

```bash
python3 scripts/newera_impact.py --state .newera/project-state.json --id REQ-NEWERA-P0-001
python3 scripts/newera_matrix.py --state .newera/project-state.json
python3 scripts/newera_drift.py --state .newera/project-state.json \
  --changed-id REQ-NEWERA-P0-001 \
  --changed-path docs/03-requirements/srs.md \
  --declared-path docs/03-requirements --semantic-advisory
```

Các projection này là groundwork M02; chỉ gate/state P0 mới quyết định technical progression hiện tại. Semantic drift không được block và không tự tạo acceptance.

## Traceability edge contract

Edge có dạng:

```json
{"source": "REQ-...", "target": "TASK-...", "type": "planned-in"}
```

Edge type P0: `specified-by`, `architected-by`, `planned-in`, `verified-by`, `evidenced-by`, `accepted-by`. Code/commit/acceptance external refs phải được định danh rõ; không dùng text tự do làm quan hệ.
