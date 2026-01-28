---
description: Deploy slideshows to GitHub Pages and sync live URL to lesson plan
---

# Deploy Slides Workflow

This workflow builds the slideshow, pushes it to GitHub, and automatically synchronizes the live URL back into your Typst lesson plan.

## Steps

### 1. Build & Push
// turbo
1. Run the build script:
```powershell
node scripts/build_dist.js
```

2. Commit and push your changes:
```bash
/commit "feat: deploy slideshow"
```

### 2. Synchronize Live URL (CRITICAL)
// turbo
Run the sync script to update the `#slideshow_link` in your `.typ` file:
```powershell
python skills/deploying-to-github-pages/scripts/sync_lesson_plan_url.py "inputs/[FOLDER]/[FILENAME].typ" "https://elwrush.github.io/lesson-plan-agent/[FOLDER]/"
```

### 3. Google Docs Link
// turbo
Create a shareable link in Google Drive:
```powershell
$env:PYTHONIOENCODING='utf-8'; python scripts/push_to_gdocs.py --file "inputs/[FOLDER]/slideshow_link.html" --name "[Title] Slideshow Link"
```
