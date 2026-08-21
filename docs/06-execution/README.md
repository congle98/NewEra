# Execution

Execution artifacts belong to a project that has completed intake and created a project-specific ROADMAP. The NewEra kernel does not execute its own M/Phase.

For an adopting project, each M/Phase may use:

```text
docs/06-execution/<M>/milestone-brief.md
docs/06-execution/<M>/<P>/requirements.md
docs/06-execution/<M>/<P>/task.md
  ├── task list
  ├── test plan and verification matrix
  ├── verification evidence
  └── checkpoint and review
docs/06-execution/<M>/<P>/report.md
docs/08-reports/<M>-report.md
```

`task.md` is the canonical working file for task execution, test planning, evidence capture and checkpoint preparation. `requirements.md` keeps requirement/acceptance criteria; `report.md` keeps the Phase summary. Use templates in `docs/templates/`. Không tạo các file trên trong repository kernel chỉ để minh họa trạng thái.