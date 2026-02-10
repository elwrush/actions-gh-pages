# Deploy Script for GitHub Pages
# Usage: .\deploy.ps1 [-message "commit message"]

param(
    [string]$message = "feat(deploy): update presentations"
)

Write-Host "🚀 Starting deployment..." -ForegroundColor Green
Write-Host ""

# Step 1: Build dist folder
Write-Host "📦 Step 1: Building dist folder..." -ForegroundColor Cyan
node scripts/build_dist.js
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Build failed!" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Build complete" -ForegroundColor Green
Write-Host ""

# Step 2: Verify links
Write-Host "🔍 Step 2: Verifying links..." -ForegroundColor Cyan
python scripts/verify_links.py
Write-Host "✅ Link verification complete" -ForegroundColor Green
Write-Host ""

# Step 3: Add dist to git
Write-Host "📝 Step 3: Adding dist to git..." -ForegroundColor Cyan
git add dist/ -f
Write-Host "✅ Staged dist folder" -ForegroundColor Green
Write-Host ""

# Step 4: Commit
Write-Host "💾 Step 4: Committing..." -ForegroundColor Cyan
git commit -m $message --no-verify
Write-Host "✅ Committed" -ForegroundColor Green
Write-Host ""

# Step 5: Push to gh-pages
Write-Host "🚀 Step 5: Pushing to GitHub Pages..." -ForegroundColor Cyan
$sha = git subtree split --prefix dist main
git push origin "$sha`:gh-pages" --force
Write-Host "✅ Deployed to GitHub Pages!" -ForegroundColor Green
Write-Host ""

# Step 6: Cleanup temp branch
Write-Host "🧹 Step 6: Cleaning up..." -ForegroundColor Cyan
git branch -D gh-pages-temp 2>$null
Write-Host "✅ Cleanup complete" -ForegroundColor Green
Write-Host ""

Write-Host "🎉 Deployment successful!" -ForegroundColor Green
Write-Host "Live at: https://elwrush.github.io/actions-gh-pages/" -ForegroundColor Yellow
