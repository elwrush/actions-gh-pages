# Reference: Delegating to Jules

## Prompt Templates

### New Feature Creation
> "Jules, create a [Language] script in `[path]` that [Specific Action]. Use `[reference_file]` as a structural guide. Ensure the code follows the patterns in `AGENTS.md` regarding [Specific Iron Law]. Include docstrings and error handling for [Specific Edge Case]."

### Logic Refactoring (Hardening)
> "Jules, audit `[file]`. The current implementation of `[function]` uses [Fragile Method (e.g., Regex)]. Refactor this to use [Robust Method (e.g., BeautifulSoup)] to ensure [Goal (e.g., cross-platform compatibility)]. Run a test using `[test_script]` before submitting."

### Dependency Update
> "Jules, check for updates to [Library/Engine] in `[path]`. If a new version exists, download and replace the existing files, ensuring our custom modifications in `[css_path]` are preserved. Verify the build by running `[build_script]`."

## Payload Structures

### Full Session Payload (JSON)
```json
{
  "prompt": "Refactor build.py to use pathlib for all path operations.",
  "sourceContext": {
    "source": "sources/github/elwrush/lesson-plan-agent",
    "githubRepoContext": {
      "startingBranch": "main"
    }
  },
  "title": "Refactor Paths to Pathlib"
}
```

## Useful API Commands

### Get Session Status (PowerShell)
```powershell
$apiKey = "YOUR_KEY"
$sessionID = "YOUR_ID"
Invoke-RestMethod -Uri "https://jules.googleapis.com/v1alpha/sessions/$sessionID" -Method Get -Headers @{ "X-Goog-Api-Key" = $apiKey }
```

### List Recent Sessions
```powershell
Invoke-RestMethod -Uri "https://jules.googleapis.com/v1alpha/sessions" -Method Get -Headers @{ "X-Goog-Api-Key" = $apiKey }
```

## Official Documentation
*   **Main Site**: [https://jules.google](https://jules.google)
*   **API Reference**: [https://jules.google/docs/api](https://jules.google/docs/api) (Internal/Alpha)
