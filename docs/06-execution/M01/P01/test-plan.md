# M01-P01 - Test Plan

- Phase: M01-P01
- Requirement scope: REQ-NEWERA-P0-001..003
- Environment: `docs/05-environment/environment-manifest.md`
- Trạng thái: IN_PROGRESS

| ID | Loại | Command/kịch bản | Expected | Status |
|---|---|---|---|---|
| TEST-NEWERA-P01-001 | Static/schema | `python3 -m json.tool` trên `.newera/**/*.json` | Tất cả JSON parse được | VERIFIED |
| TEST-NEWERA-P01-002 | State/reference | `python3 scripts/newera_validate.py --state .newera/project-state.json` | Không structural error; WARN nếu NOT_RUN | VERIFIED |

## Failure criteria

- JSON không parse.
- State ID duplicate/unknown reference.
- Evidence thiếu required field hoặc acceptance status.
- Typed edge source/target/type không hợp lệ.

## Limitations

Validator P0 dùng Python standard library; chưa phải full JSON Schema implementation. Schema file là contract, validator là enforcement subset được ghi rõ.
