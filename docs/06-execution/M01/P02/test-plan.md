# M01-P02 - Test Plan

- Phase: M01-P02
- Requirement scope: REQ-NEWERA-P0-004..005
- Environment: Python standard library; `docs/05-environment/environment-manifest.md`
- Trạng thái: IN_PROGRESS

| ID | Loại | Command/kịch bản | Expected | Status |
|---|---|---|---|---|
| TEST-NEWERA-P02-001 | Negative gate | `python3 scripts/newera_validate.py --state .newera/fixtures/invalid-state.json` | Exit 1; báo task thiếu requirement và test thiếu evidence | VERIFIED |
| TEST-NEWERA-P02-002 | Strict gate | `python3 scripts/newera_validate.py --state .newera/project-state.json --strict` | Exit 1 khi NOT_RUN; sau final evidence exit 0 | VERIFIED |

## Failure criteria

- Gate trả 0 cho state invalid.
- Gate tự chuyển acceptance thành ACCEPTED.
- Strict mode cho phép NOT_RUN trước checkpoint.
- Profile STANDARD thiếu required role nhưng không báo lỗi.

## Output

Evidence machine envelope và Markdown narrative phải ghi command, exit code, expected, actual, limitation.
