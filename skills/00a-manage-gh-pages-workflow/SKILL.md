---
name: 00a-manage-gh-pages-workflow
description: >
  Specialized Git workflow for deploying slideshows to GitHub Pages.
  Targets the 'actions-gh-pages' repository using a worktree-based 
  incremental deployment strategy.
---

# Skill: Manage GH Pages Workflow (`00a-manage-gh-pages-workflow`)

## Description
This skill manages the deployment of **standalone presentation bundles** to the `gh-pages` branch of the `actions-gh-pages` repository. It ensures that every lesson is portable, self-contained, and correctly indexed on the live dashboard.

## Core Mandates
1.  **Target Repository**: Must push to `https://github.com/elwrush/actions-gh-pages.git` (remote: `origin`).
2.  **Standalone Bundle Law**: Every presentation folder MUST contain its own `dist/` and `plugin/` folders. The `fontawesome/` folder is OPTIONAL if the FA6 CDN is utilized.
3.  **The CDN-First Asset Architecture**: Core UI assets (Reveal.js, FontAwesome) are fetched from global repositories or CDNs during build. The local `/lib/` folder is legacy and must not be used.
4.  **Root-Relative Media Standard**: All shared media references in `presentation.json` MUST use `/images/` (root-relative) to support centralized asset serving on GitHub Pages.
5.  **Incremental Updates**: Deployments only affect the specific lesson folder and the global `index.html` dashboard.
6.  **Zero Overwrite**: Lessons reside in unique subfolders to prevent cross-lesson interference.

## Workflow

### 1. Build & Bundle
Ensure the lesson is built as a standalone artifact in `dist/`.
```powershell
python build.py <LESSON-NAME>
```

### 2. Deploy to GitHub Pages
Run the deployment automation. This script manages the `git worktree`, dashboard regeneration, and remote push.
```powershell
python skills/00a-manage-gh-pages-workflow/scripts/deploy_presentation.py <LESSON-NAME>
```

### 3. Verification
Verify the live URL:
`https://elwrush.github.io/actions-gh-pages/<LESSON-NAME>/`

## Deployment Logic (Hands)
The execution logic resides in `skills/00a-manage-gh-pages-workflow/scripts/deploy_presentation.py`. It automates the following Git sequence:
1. `git worktree add` (pointing to `gh-pages`)
2. `cp -r` (copying standalone bundle)
3. `python generate_dashboard.py`
4. `git commit` & `git push origin gh-pages`
5. `git worktree remove`
