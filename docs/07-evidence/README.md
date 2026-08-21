# Verification Evidence

Evidence chứng minh các kiểm tra kỹ thuật đã được thực hiện trong một project sử dụng NewEra. Evidence không tự động là nghiệm thu sản phẩm và NewEra kernel không lưu evidence của chính nó.

## Canonical location and optional layers

Evidence mặc định được ghi trong phần **Verification evidence** của `task.md`. `docs/07-evidence/` chỉ dùng cho narrative/machine evidence riêng khi registry của project kích hoạt.

1. **Machine envelope:** metadata/result có schema version trong machine state của project.
2. **Human narrative:** context, interpretation, output dài và limitations trong evidence artifact hoặc `task.md`.

Hai lớp dùng cùng ID nhưng không copy mù nội dung; machine envelope sở hữu metadata/result, Markdown sở hữu context/limitations.

## Required fields

| Field | Ý nghĩa | Rule |
|---|---|---|
| `schemaVersion` | Version envelope | Tăng version khi breaking change |
| `id` | Evidence ID | Ổn định, truy nguyên được |
| `scope` | M/Phase/requirement scope | Không rỗng |
| `requirementRefs` | Requirements được chứng minh | Có ít nhất một ID khi áp dụng |
| `testRefs` | Checks/kịch bản | Có lệnh hoặc kịch bản tái chạy |
| `command` | Cách tái chạy | Không ghi “đã test” chung chung |
| `expected` / `actual` | Kết quả đối chiếu | Ghi đủ để review |
| `result` | Kết luận kỹ thuật | `VERIFIED`, `PARTIAL`, `FAILED`, `BLOCKED`, `NOT_RUN` |
| `commitRef` | Version/worktree | SHA hoặc reference rõ |
| `timestamp` | Thời điểm | ISO-8601 |
| `environment` | OS/tool/runtime | Không chứa secret |
| `acceptanceStatus` | Acceptance riêng | Mặc định `PENDING` |
| `capabilityRefs` | Năng lực/lớp kiểm chứng áp dụng | Liên kết M/Phase capability profile |
| `environmentRef` | Environment Manifest/Setup Report | Có gate và limitation tương ứng |
| `adapter` | Adapter/tool được project chọn | Ghi tên/version/config cần tái chạy; không phải NewEra default |
| `artifacts` | Evidence files | Report/log/trace/screenshot/video/network/metric/accessibility hoặc artifact phù hợp |
| `humanReview` | Review cần con người | Ghi role, scope và decision nếu có |
| `limitations` | Phần chưa chứng minh | Ghi rõ residual/blocker |

## Status semantics

`PASS`/`FAIL` là kết quả của một check; `result` là kết luận evidence-level. `VERIFIED` không tạo `ACCEPTED`. `NOT_RUN` không được dùng làm cơ sở chuyển `VERIFIED`. Status dictionary và acceptance authority nằm ở `docs/00-governance/status-model.md` và `docs/03-requirements/acceptance-policy.md`.

Nếu project có narrative evidence riêng, registry phải bật file đó và artifact vẫn phải liên kết ngược về `task.md`. Không tạo template verification-evidence độc lập trong kernel.
