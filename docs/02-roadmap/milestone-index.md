# Milestone Index

Milestone Index là bảng tra cứu nhanh; nội dung chi tiết và thứ tự chính thức nằm ở `docs/02-roadmap/roadmap.md`. Mọi thay đổi tên, Phase, dependency hoặc status phải đồng bộ cả hai file.

| ID | Tên | ROADMAP section | Brief | Report | State | Trạng thái |
|---|---|---|---|---|---|---|
| M01 | Governance Automation Foundation | `roadmap.md#m01--governance-automation-foundation` | Chưa tạo | Chưa tạo | `.newera/project-state.json` | IN_PROGRESS |
| M02 | Adaptive and Impact Governance | `roadmap.md#m02--adaptive-and-impact-governance-p1` | Chưa tạo | Chưa tạo | Chưa kích hoạt | DRAFT |

## Quy tắc ID và status

- `M01`, `M02`: milestone mới.
- `M01.1`, `M01.2`: vòng bồi hoàn hoặc hoàn thiện cho M01; không dùng cho tính năng mới.
- `M01-P01`: Phase thuộc M01.
- `TASK-NEWERA-P01-001`: task machine-readable có project namespace.
- `TEST-NEWERA-P01-001`: test machine-readable có project namespace.
- Mỗi M phải có brief trước khi `IN_PROGRESS`, report trước khi `CHECKPOINT_PENDING`, và quyết định nghiệm thu riêng trước `ACCEPTED`.
- Index không được tự tạo sự thật mới; `roadmap.md` là nguồn thứ tự/scope, `.newera/project-state.json` là machine lifecycle/reference projection được gate kiểm tra.
