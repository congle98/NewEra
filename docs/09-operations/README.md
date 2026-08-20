# Operations

Tài liệu operations chỉ được kích hoạt khi project có runtime, dữ liệu hoặc user/production impact. Kernel NewEra hiện là repository documentation, không có deployment/service để vận hành.

## Conditional documents

| Tài liệu | Trigger | Baseline status | Khi kích hoạt phải ghi |
|---|---|---|---|
| Deployment Guide | Có môi trường deploy | NOT_APPLICABLE | artifact version, environment, rollout, rollback, owner |
| Monitoring | Có service cần quan sát | NOT_APPLICABLE | signal, threshold, alert owner, dashboard |
| Backup and Recovery | Có dữ liệu cần khôi phục | NOT_APPLICABLE | scope, RPO/RTO, restore test, retention |
| Incident Response | Có production/user impact | NOT_APPLICABLE | severity, escalation, communication, postmortem |
| Release Runbook | Có release lặp lại | NOT_APPLICABLE | preflight, approval, steps, rollback |
| Migration Plan | Có thay đổi schema/data | NOT_APPLICABLE | compatibility, backup, rehearsal, rollback |

`NOT_APPLICABLE` ở đây là trạng thái của baseline, không phải tuyên bố project con sẽ luôn không cần tài liệu. Khi trigger xuất hiện, cập nhật registry trước và tạo artifact trong scope/ROADMAP phù hợp.

## Operational readiness gate

Trước `CHECKPOINT_PENDING` của project có runtime, phải có owner vận hành, environment, deploy/rollback, monitoring, backup/recovery và incident path phù hợp. Các phần không chạy được phải là `BLOCKED` hoặc residual có ID; không giấu trong report.
