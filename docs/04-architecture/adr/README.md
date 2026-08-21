# Architecture Decision Records - Reference Template

> Sao chép index/template này vào adopter workspace. NewEra kernel không chốt technology hoặc sở hữu project-specific ADR.

## Document control

- Document status: DRAFT
- Owner/role: `<OWNER>`
- Kernel release: `NEWERA_VERSION`
- Kernel source commit: `SOURCE_COMMIT`
- Project registry reference: `<REGISTRY-REF>`
- Created/updated: `<DATE>`

ADR ghi một quyết định kỹ thuật có ảnh hưởng dài hạn, khác với task implementation và khác với Decision Log ở mức governance. ADR không được tự thay đổi scope; nếu quyết định ảnh hưởng ROADMAP/SRS/timeline, liên kết CR/Decision tương ứng.

## ADR index

| ID | Tên | Scope | Trạng thái | Supersedes/superseded by |
|---|---|---|---|---|
| `ADR-<ADR-ID>` | `<TOPIC>` | `<SCOPE>` | PROPOSED | `<SUPERSEDES-REF-OR-NONE>` |

## Vòng đời

- `PROPOSED`: đang phân tích, không dùng làm contract cuối.
- `ACCEPTED`: phương án được thông qua; cập nhật Architecture/registry/implementation liên quan.
- `SUPERSEDED`: bị quyết định mới thay thế; giữ link lịch sử.

## Template

```markdown
# ADR-<ADR-ID>: Tên quyết định

- Ngày:
- Owner/reviewer:
- Liên kết: CR-<CR-ID>/DEC-<DEC-ID>/RES-<RES-ID>/REQ-<REQ-ID>
- Trạng thái: PROPOSED | ACCEPTED | SUPERSEDED

## Bối cảnh
## Vấn đề và constraint
## Các phương án
## Tiêu chí đánh giá
## Quyết định
## Lý do
## Ảnh hưởng tích cực/tiêu cực
## Security/data/operations impact
## Migration/rollback nếu có
## Consequences và follow-up
```

Không tạo ADR chỉ để điền cấu trúc; chỉ tạo khi có quyết định thực tế cần giữ lâu dài.
