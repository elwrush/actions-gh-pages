---
name: deploying-to-github-pages
description: Deploys slideshows to GitHub Pages and synchronizes the live URL back to the lesson plan. Handles building, committing, and post-deployment linking.
---

# Skill: Deploying to GitHub Pages (`deploying-to-github-pages`)

## Description
This skill automates the deployment of Reveal.js presentations to GitHub Pages. It relies on the custom GitHub Action defined in `.github/workflows/deploy.yml`, which utilizes the [elwrush/actions-gh-pages](https://github.com/elwrush/actions-gh-pages) repository to handle the final stage of publishing. It ensures that once a slideshow is pushed to the repository, the corresponding Typst lesson plan is updated with the finalized live URL.

## Critical Rules

> [!CRITICAL]
> **POST-DEPLOYMENT SYNC**: You MUST run the `sync_lesson_plan_url.py` script immediately after push. This is a critical pedagogical step to ensure the printed/PDF lesson plan correctly links to the interactive content.

> [!IMPORTANT]
> **URL PATTERN**: For this repository, the live URL is:
> `https://elwrush.github.io/lesson-plan-agent/[FOLDER-NAME]/`

## Architectural Workflow

```mermaid
graph TD
    Start([Deployment Request]) --> Build[1. Build dist/ folder]
    Build --> Commit[2. Commit & Push via /commit]
    
    subgraph GitHub
        Commit --> Pages[GitHub Pages Auto-Build]
    end
    
    Pages --> CalcURL[3. Calculate Live URL]
    CalcURL --> Sync[4. Sync Live URL to .typ Plan]
    Sync --> GDocs[5. Push Link to Google Docs]
    GDocs --> Finish([🏁 Live Slideshow & Updated Plan])
    
    %% Semantic Requirements
    SyncNode[sync_lesson_plan_url.py] -.->|Regex Replace| Sync
```

## Workflow Steps

### 1. Build the Distribution
Run the build script to prepare the `dist/` directory. This ensures all horizontal split templates and assets are correctly bundled.
// turbo
```powershell
node scripts/build_dist.js
```

### 2. Commit and Push
Use the `/commit` workflow to push the changes to GitHub.
```bash
/commit "feat: deploy [Lesson Name] slideshow"
```

### 3. Synchronize Lesson Plan URL (CRITICAL)
Calculate the live URL and update the Typst source file. This step ensures that the PDF output of the lesson plan is functionally linked.

**Pattern**: `https://elwrush.github.io/lesson-plan-agent/[FOLDER-NAME]/`

**Command**:
// turbo
```powershell
python skills/deploying-to-github-pages/scripts/sync_lesson_plan_url.py "inputs/[FOLDER]/[FILENAME].typ" "https://elwrush.github.io/lesson-plan-agent/[FOLDER]/"
```

### 4. Push to Google Docs
Convert the link to a Google Doc for easy sharing via Google Drive.
// turbo
```powershell
$env:PYTHONIOENCODING='utf-8'; python scripts/push_to_gdocs.py --file "inputs/[FOLDER]/slideshow_link.html" --name "[Title] Slideshow Link"
```

## Reference
- [sync_lesson_plan_url.py](scripts/sync_lesson_plan_url.py) - Script for regex-based URL replacement.
- [using-skills.md](../../knowledge_base/using-skills.md) - General skill authoring and usage guidelines.
