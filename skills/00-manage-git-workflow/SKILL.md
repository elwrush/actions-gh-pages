---
name: 00-manage-git-workflow
description: >
  Standardized Git interactions for the project. Handles commits, 
  annotated releases, and remote synchronization with safety checks.
---

# Skill: Manage Git Workflow (`00-manage-git-workflow`)

## Description
This skill provides a deterministic way to interact with the project's source repository. It ensures consistent staging, aggressive junk cleaning (desktop.ini/nul), and release tagging.

## Core Mandates
1.  **NO AUTOMATIC COMMITS**: You MUST NOT run the `commit` command unless the user explicitly uses a **Directive** (e.g., "Commit the work").
2.  **Scrubbing & Ignoring**: The `scrub` command aggressively removes system junk (desktop.ini). The script also automatically ensures Windows device files (`nul`, `NUL`) are placed in `.gitignore` to prevent fatal Git indexing errors.
3.  **Safety First**: The script automatically un-stages `dist/` to prevent repository pollution.

## Workflow

<AGENT_WORKFLOW>

### Stage 0: Status & Scrub
Check the state and clean junk without committing.
```powershell
python skills/00-manage-git-workflow/scripts/git_workflow.py scrub
python skills/00-manage-git-workflow/scripts/git_workflow.py status
```

### Stage 1: Commit (USER DIRECTIVE ONLY)
Only run if explicitly told to save/commit.
```powershell
python skills/00-manage-git-workflow/scripts/git_workflow.py commit "type: description"
```

### Stage 2: Release (Milestone)
Use for major architectural updates.
```powershell
python skills/00-manage-git-workflow/scripts/git_workflow.py release "v1.X.X" "Description"
```

</AGENT_WORKFLOW>

## Execution Layer
Located at `skills/00-manage-git-workflow/scripts/git_workflow.py`.
