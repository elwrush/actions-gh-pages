---
name: hosting-presentations
description: >
  Deploys HTML presentations to Cloudflare Pages using direct API deployment.
  Use when the user wants to publish, host, or deploy a slideshow.
---

# Skill: Hosting Presentations (`hosting-presentations`)

## Description
This skill deploys HTML presentations to **Cloudflare Pages** using direct Wrangler CLI deployment with API token authentication.

## Prerequisites
- **Environment Variable**: `CLOUDFLARE_SLIDESHOW_API` must be set as a User environment variable containing a valid Cloudflare API token with **Account > Cloudflare Pages > Edit** permission.
- **Token Setup**: If missing, create at https://dash.cloudflare.com/profile/api-tokens with:
  - Permission: Account > Cloudflare Pages > Edit
  - Account Resources: Select your specific account (not "All accounts")

## Critical Rules

> [!IMPORTANT]
> **NEVER DEPLOY THE ROOT DIRECTORY (`.`)**.
> Always build a clean `dist/` directory first.

> [!IMPORTANT]
> **SOURCE LOCATION**: Presentations must exist in `inputs/[QAD-folder]/` alongside their lesson plan and worksheet.

## Workflow

### 1. Build
Run the build script without arguments to build ALL presentations found in `inputs/` into `dist/`:

```powershell
node scripts/build_dist.js
```

The script will:
- Scan `inputs/` for folders containing `index.html`
- Copy each into `dist/[folder-name]/` (Unique URLs)
- Copy shared JS/Images to `dist/`
- Generate a dashboard at `dist/index.html` pointing to all lessons.

> [!IMPORTANT]
> **OVERWRITING PREVENTION**: By using subfolders (`/folder-name/`), we can host multiple slideshows simultaneously on the same domain without they overwriting each other.

### 2. Deploy
Deploy using Wrangler with the API token:

```powershell
$env:CLOUDFLARE_API_TOKEN = [Environment]::GetEnvironmentVariable('CLOUDFLARE_SLIDESHOW_API', 'User')
npx wrangler pages deploy dist/
```

**First-time deployment**: You'll be prompted for:
- Project name (e.g., `lesson-slideshows`)
- Production branch (use `main`)

### 3. Verify
- **Production URL**: `https://<project-name>.pages.dev`
- SSL certificates may take 1-2 minutes to provision for new projects

### 4. Create Google Doc Link (MANDATORY)

> [!CRITICAL]
> You MUST create a **Google Doc** (not an HTML file) containing the slideshow link.
> HTML files do NOT work in Google Drive for sharing - they must be converted to Google Docs format.

1. Create a simple HTML file with the link:
```html
<h1>Slideshow Link</h1>
<p><a href="https://lesson-slideshows.pages.dev/QAD-Fight-or-Flight/">https://lesson-slideshows.pages.dev/QAD-Fight-or-Flight/</a></p>
```

2. Push to Google Docs (this CONVERTS to GDoc format):
```powershell
$env:PYTHONIOENCODING='utf-8'
python scripts/push_to_gdocs.py --file "path/to/link.html" --name "DD-MM-YY Slideshow Link"
```

3. Provide the Google Doc URL to the user.

## One-Liner (Quick Deploy)

```powershell
node scripts/build_dist.js QAD-Fight-or-Flight; $env:CLOUDFLARE_API_TOKEN = [Environment]::GetEnvironmentVariable('CLOUDFLARE_SLIDESHOW_API', 'User'); npx wrangler pages deploy dist/
```

## Projects

| Project | URL | Purpose |
|:---|:---|:---|
| `lesson-slideshows` | lesson-slideshows.pages.dev | Standalone presentations (direct deploy) |
| `lesson-plan-agent` | lesson-plan-agent.pages.dev | Dashboard + Git-connected presentations |

## Troubleshooting

### Token Permission Errors
If you see "missing permission", the token needs:
1. **Account > Cloudflare Pages > Edit** permission
2. **Account Resources** set to your specific account (not "All accounts")
3. After editing permissions, **Roll** the token to get a new value

### SSL Errors on New Deployments
Wait 1-2 minutes for certificate provisioning. Use the production URL (without deployment hash).

