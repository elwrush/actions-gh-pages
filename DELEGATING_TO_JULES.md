# Guide: Delegating to Jules (Autonomous Engineering)

## Overview
**Jules** is Google's autonomous AI coding agent. Unlike standard LLM turns, Jules runs in a **secure cloud sandbox** where it can clone your repository, install dependencies, run tests, and apply multi-file changes before submitting a **Pull Request (PR)**.

Use this guide to escalate complex engineering tasks that are too fragile or large for your current environment.

---

## 1. When to Delegate
**Escalate to Jules if the task involves:**
*   **Multi-file Refactoring**: e.g., "Change all path operations to use `pathlib` across all scripts."
*   **Dependency Hardening**: e.g., "Replace regex-based HTML parsing with `BeautifulSoup`."
*   **Infrastructure Creation**: e.g., "Build a new automated test suite for the build pipeline."
*   **Environment-Specific Fixes**: e.g., "Fix Windows file-locking issues in the directory cleanup logic."

---

## 2. Security Protocol (CRITICAL)
*   **API Key Handling**: NEVER commit the Jules API key to the repository.
*   **Transient Use**: Only use the key in raw terminal commands (`Invoke-RestMethod`).
*   **Credential Masking**: If providing code snippets to the user, mask the key like `AQ.Ab8...[REST_OF_KEY]`.

---

## 3. The 3-Step Delegation Workflow

### Step 1: Formulate a Deterministic Prompt
Your prompt is Jules's only instruction. Be specific.
*   **Bad**: "Fix the build script."
*   **Good**: "Audit `build.py`. The `clean_dir` function fails on Windows when files are locked. Implement a retry loop with a 1-second delay between attempts."

### Step 2: Execute via PowerShell
Use the following pattern to trigger a session.

```powershell
$apiKey = "[USER_PROVIDED_KEY]"
$url = "https://jules.googleapis.com/v1alpha/sessions"
$payload = @{
    prompt = "[Your Detailed Prompt]"
    sourceContext = @{
        source = "sources/github/elwrush/lesson-plan-agent"
        githubRepoContext = @{ startingBranch = "main" }
    }
    title = "[Descriptive Title]"
} | ConvertTo-Json -Depth 10

Invoke-RestMethod -Uri $url -Method Post -Headers @{ "X-Goog-Api-Key" = $apiKey; "Content-Type" = "application/json" } -Body $payload
```

### Step 3: Monitor and Handoff
Provide the user with the **Session ID** and the **Progress URL**.
*   **URL Pattern**: `https://jules.google/session/[SESSION_ID]`
*   **Verification**: Remind the user they must be logged into the correct Google account to view the dashboard.

---

## 4. Reviewing Jules's Work
When Jules completes a task, it will open a **Pull Request** on GitHub.
1.  **Do not merge blindly.**
2.  Review the diff for "AI hallucinations" or over-engineering.
3.  Pull the branch locally and run a test build (`python scripts/fast_edit.py [lesson]`).
4.  Once verified, merge and delete the Jules branch.

---

## 5. Pro Tips for Agents
*   **Activity Matrix**: Always tell Jules to look at `knowledge_base/reveal_activity_matrix.md` if the task involves slide layouts.
*   **Iron Laws**: Tell Jules to respect the rules in `AGENTS.md` (e.g., "No Thai translations on vocab slides").
*   **Environment**: Remind Jules that the project runs on **win32** and a **G: Cloud Drive**.

---

*For detailed technical specs, see the skill: `skills/delegating-to-jules/SKILL.md`*
