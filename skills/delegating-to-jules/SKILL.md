---
name: delegating-to-jules
description: Orchestrates autonomous coding tasks via the Jules AI agent API. Use when a task requires end-to-end execution (clone, code, test, PR) that is too complex or out-of-scope for the current environment.
---

# Skill: Delegating to Jules (`delegating-to-jules`)

**Version**: 1.0 (Autonomous Session Management)

## Description
This skill enables the delegation of complex software engineering tasks to **Jules**, Google's autonomous AI coding agent. It manages the lifecycle of a Jules session: from prompt engineering and repository context definition to API execution and Pull Request review.

## Core Mandates
1.  **Security Mandate**: **NEVER** store the Jules API key in any file (JSON, Markdown, or Script). Always treat the API key as a transient variable or environment secret.
2.  **Source Context Accuracy**: You **MUST** verify the GitHub repository URL and the target branch (`main` by default) before initiating a session. Incorrect context leads to `Source Not Found` errors.
3.  **Prompt Fidelity**: Prompts for Jules must be **Deterministic and Context-Rich**. Include specific file paths, expected outputs (e.g., "Create a script in `scripts/`"), and reference materials (e.g., "Use mappings from `activity_matrix.md`").
4.  **No Hallucinated Features**: Do not ask Jules to use libraries or APIs not available in the project unless you explicitly instruct it to install them (e.g., "Install `beautifulsoup4` first").
5.  **Review Protocol**: Autonomous PRs from Jules **MUST** be reviewed by a human or a high-level agent before merging. Never assume Jules code is 100% correct without a test run.
6.  **Environment Awareness**: Always remind Jules if the project is running on Windows (`win32`) or a Cloud Drive (G:), as it may need to handle file locks or path slashes differently.

## Workflow

### Phase 1: Task Identification
1.  **Scope Check**: Determine if the task is too large for a single turn (e.g., "Refactor the entire build system") or requires persistent testing.
2.  **Tooling Check**: Verify if Jules has access to the required repo.

### Phase 2: Prompt Formulation
1.  **Objective**: State the goal clearly (e.g., "Automate path fixing").
2.  **Inputs**: List existing files to use as reference.
3.  **Constraints**: Define the output format (Python vs Node) and any "Iron Laws" from `AGENTS.md`.

### Phase 3: API Execution
1.  **Payload Generation**: Construct the JSON payload with `prompt`, `sourceContext`, and `title`.
2.  **Invoke**: Use PowerShell's `Invoke-RestMethod` to trigger the session.
3.  **Handoff**: Provide the user with the **Session ID** and the **Track Progress URL**.

### Phase 4: Review & Integration
1.  **PR Check**: Verify that Jules has opened a Pull Request on GitHub.
2.  **Local Sync**: Pull the Jules branch locally for verification.
3.  **Cleanup**: Merge the PR and delete the temporary Jules branch.

## 🛡️ Troubleshooting

### 🌐 The "URL Not Found" Error
If the progress URL returns a 404 on the website:
**FIX**: Ensure the user is logged into the Google account associated with the API key.

### 🔑 API Key Refusal
If the API returns a 401 (Unauthorized):
**FIX**: Do not ask for the key again. Suggest the user verifies the key in their local environment.

### 🛑 Session Stalled
If the session stays in `IN_PROGRESS` for > 30 minutes:
**FIX**: Check the `Activities` endpoint via the API to see if Jules is stuck on a test or dependency installation.

## API Patterns

### Create Session (PowerShell)
```powershell
$payload = @{
    prompt = "[Detailed Task]"
    sourceContext = @{
        source = "sources/github/[user]/[repo]"
        githubRepoContext = @{ startingBranch = "main" }
    }
    title = "[Session Title]"
} | ConvertTo-Json -Depth 10
Invoke-RestMethod -Uri "https://jules.googleapis.com/v1alpha/sessions" -Method Post ...
```

### Check Status
```powershell
Invoke-RestMethod -Uri "https://jules.googleapis.com/v1alpha/sessions/[ID]" -Method Get ...
```
