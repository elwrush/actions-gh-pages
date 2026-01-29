---
name: deploying-to-github-pages
description: Deploys slideshows to GitHub Pages and synchronizes the live URL back to the lesson plan. Handles building, committing, and post-deployment linking.
---

# Skill: Deploying to GitHub Pages (`deploying-to-github-pages`)

## Description
This skill automates the deployment of Reveal.js presentations to GitHub Pages. It relies on the official [peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages) engine via `.github/workflows/deploy.yml`. It ensures that once a slideshow is pushed, the corresponding Typst lesson plan is updated with the finalized live URL.

## Critical Rules

> [!CRITICAL]
> **POST-DEPLOYMENT SYNC**: You MUST run the `sync_lesson_plan_url.py` script immediately after push. This ensures the PDF lesson plan correctly links to the interactive content.

> [!IMPORTANT]
> **REPOSITORY VISIBILITY**: The repository MUST be set to **Public** for free GitHub Pages hosting.
> **PERMISSIONS**: The `GITHUB_TOKEN` in the workflow MUST have `contents: write` permissions.

## Architectural Workflow

```mermaid
graph TD
    Start([🚀 Deployment Request]) --> Discovery[1. Discovery: Verify Repo Visibility & Permissions]
    Discovery --> Build[2. Local Build: node scripts/build_dist.js]
    Build --> Commit[3. Commit & Push via /commit]
    
    subgraph CI_CD_Pipeline [GitHub Actions]
        Commit --> Trigger[Trigger: deploy.yml]
        Trigger --> Logic[peaceiris/actions-gh-pages@v4]
        Logic --> Publish[Publish to gh-pages branch]
    end
    
    Publish --> CalcURL[4. Calculate Live URL]
    CalcURL --> Sync[5. Sync Live URL to .typ Plan]
    Sync --> Finish([🏁 Live Slideshow & Updated Plan])
    
    %% Semantic Requirements
    SyncNode[sync_lesson_plan_url.py] -.->|Regex Replace| Sync
```

## Workflow Steps

### 1. Build the Distribution
Run the build script to prepare the `dist/` directory.
// turbo
```powershell
node scripts/build_dist.js
```

### 2. Commit and Push
Use the `/commit` workflow to push the changes.
```bash
/commit "feat: deploy [Lesson Name] slideshow"
```

### 3. Synchronize Lesson Plan URL (CRITICAL)
Update the Typst source file with the calculated live URL.
// turbo
```powershell
python skills/deploying-to-github-pages/scripts/sync_lesson_plan_url.py "inputs/[FOLDER]/[FILENAME].typ" "https://elwrush.github.io/lesson-plan-agent/[FOLDER]/"
```

## Global Assets (Optimization)
To avoid duplicating large files (like 5MB background videos) in every presentation:
1.  **Place the file** in the root `images/` folder of the project.
2.  **Reference it** in your `presentation.json` using the absolute GitHub Pages URL:
    - `https://elwrush.github.io/lesson-plan-agent/images/[FILENAME]`
3.  This ensures the file is uploaded only once and works in both local and live environments.

## Technical Pitfalls & Learnings
- **Gitignore Conflicts**: Ensure `.gitignore` uses root-specific paths (e.g., `/dist/`) to avoid blocking presentation-specific assets in `inputs/`.
- **Theme Sync**: The `generate_presentation.py` script must use `dirs_exist_ok=True` to ensure themes (like `noir.css`) are updated in the presentation folders.
- **Workflow Branching**: Always use the semantic version `@v4` for official actions to avoid the "missing lib/index.js" errors found in unbuilt forks.

## Reference
- [rendering-prompts-into-mermaid](../rendering-prompts-into-mermaid/SKILL.md) - Standards for this skill's architecture maps.
- [sync_lesson_plan_url.py](scripts/sync_lesson_plan_url.py) - Script for regex-based URL replacement.
