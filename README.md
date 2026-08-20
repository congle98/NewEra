# NewEra v0.1

NewEra là baseline quy trình phát triển phần mềm tự động hóa cho Kiro. Nó không khóa công nghệ; mỗi dự án có thể bật hoặc bỏ các tài liệu kỹ thuật theo `docs/00-governance/document-registry.md`.

## Bắt đầu

Đọc `AGENTS.md` và `GUIDE.md` trước; GUIDE giải thích cách vận hành, còn AGENTS là luật bắt buộc.

Đường ngắn nhất để bắt đầu một dự án:

```text
/newera-intake
```

Sau đó theo trình tự:

1. Đọc `AGENTS.md`, `status-model.md`, `git-policy.md` và registry.
2. Điền `docs/01-discovery/project-intake.md`.
3. Hoàn thiện `docs/02-roadmap/roadmap.md` và `milestone-index.md`.
4. Hoàn thiện SRS, acceptance policy, traceability và Architecture.
5. Kiểm tra `environment-manifest.md`/`setup-report.md`.
6. Chọn M đã `READY`, tạo brief và dùng template trong `docs/templates/`.
7. Chạy verification trước khi chuyển Phase sang `CHECKPOINT_PENDING`.
8. Chờ người/role nghiệm thu; không tự chuyển sang `ACCEPTED`.

## Nguyên tắc trạng thái

`VERIFIED` chỉ có nghĩa là đã kiểm chứng theo tiêu chí kỹ thuật. `CHECKPOINT_PENDING` là đang chờ xem xét và chưa hoàn thành. Chỉ `ACCEPTED` mới là nghiệm thu. `PARTIAL`, `BLOCKED`, `DEFERRED` và `NOT_APPLICABLE` phải đi kèm phạm vi/lý do phù hợp.

- `docs/07-evidence/EVD-NEWERA-DOCS-001.md` ghi static review trước P0 foundation; evidence P0 mới dùng machine envelope `.newera/evidence/` và Markdown narrative tương ứng.

## P0 verification command

```text
python3 scripts/newera_validate.py --state .newera/project-state.json
python3 scripts/newera_validate.py --state .newera/project-state.json --strict
```

Default cho phép state `IN_PROGRESS` với `WARN` khi test/evidence `NOT_RUN`; strict gate phải FAIL trước checkpoint nếu còn `NOT_RUN`. Gate không tự tạo acceptance.

P1 graph/state projections (groundwork, không tự accept):

```text
python3 scripts/newera_change.py --before .newera/project-state.json --after .newera/project-state.json
python3 scripts/newera_impact.py --state .newera/project-state.json --id REQ-NEWERA-P0-001
python3 scripts/newera_matrix.py --state .newera/project-state.json
python3 scripts/newera_drift.py --state .newera/project-state.json --changed-id REQ-NEWERA-P0-001 --changed-path docs/03-requirements/srs.md --declared-path docs/03-requirements --semantic-advisory
```

Deterministic drift FAIL là blocking cho scope check; semantic drift hiện chỉ advisory.

## Cấu trúc chính

- `AGENTS.md`: hiến pháp dự án.
- `GUIDE.md`: quy trình vận hành và thư viện prompt.
- `.kiro/`: steering, agents, skills và hooks.
- `.newera/`: machine-readable state, schema, evidence envelope và governance profiles; xem `docs/00-governance/automation-contract.md`.
- `scripts/`: deterministic governance utilities: `newera_validate.py`, `newera_change.py`, `newera_impact.py`, `newera_matrix.py` và `newera_drift.py`.
- `docs/`: governance, discovery, planning, requirements, architecture, environment, execution, evidence, reports, operations, templates và prompts.

## Phạm vi hiện tại

Repository này là process kernel v0.1. ROADMAP hiện để M01 ở `IN_PROGRESS` cho P0 foundation; M02 Adaptive and Impact Governance vẫn `DRAFT`. Product-specific runtime scope và dogfood còn ghi trong residual work, không tự suy đoán.

## Phiên bản

NewEra v0.1 là kernel ban đầu, ưu tiên tính dễ hiểu, truy nguyên, trung thực về trạng thái và khả năng mở rộng mà không khóa công nghệ.
