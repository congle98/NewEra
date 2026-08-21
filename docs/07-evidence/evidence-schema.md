# Evidence Schema Guide

Evidence là bằng chứng kiểm chứng kỹ thuật của **project sử dụng NewEra**. NewEra kernel chỉ cung cấp quy tắc và template; không lưu evidence của chính kernel.

## Hai lớp evidence tùy chọn

1. **Machine envelope:** đặt trong thư mục machine state của project khi structured mode được bật.
2. **Human narrative:** đặt trong thư mục evidence canonical của project.

Hai lớp dùng cùng ID nhưng không copy mù nội dung. Machine envelope sở hữu metadata/result; Markdown sở hữu context, interpretation, output dài và limitations.

## Required fields đề xuất

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
| `acceptanceStatus` | Acceptance riêng | Mặc định `NOT_ACCEPTED` |
| `limitations` | Phần chưa chứng minh | Ghi rõ residual/blocker |

## Status semantics

`PASS`/`FAIL` là kết quả của một check; `result` là kết luận evidence-level. `VERIFIED` không tạo `ACCEPTED`. `NOT_RUN` không được dùng làm cơ sở chuyển `VERIFIED`.

## Evidence section trong task.md

Dùng phần **Verification evidence** của `docs/templates/task.md` làm template mặc định. Phần này phải ghi scope, requirement/task/test IDs, command, expected, actual, commit/worktree, environment, timestamp, result, acceptance status và limitations.

Nếu project có nhu cầu tách narrative evidence riêng, file đó phải được registry của project kích hoạt và vẫn liên kết ngược về `task.md`; không tạo template evidence độc lập trong kernel.
