<#
Fast Edit Script - Streamlines presentation editing workflow

This PowerShell script eliminates the need for manual multi-file edits by:
1. Focusing on presentation.json as single source of truth
2. Automatically regenerating published HTML
3. Rebuilding dist version

Usage: .\scripts\fast_edit.ps1 <lesson_name> [-NoRebuild]
Example: .\scripts\fast_edit.ps1 05-02-2026-Gold-Infographic-B1
#>

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$LessonName,
    
    [switch]$NoRebuild
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$InputsDir = Join-Path $ProjectRoot "inputs" $LessonName
$JsonPath = Join-Path $InputsDir "presentation.json"

# Check if presentation exists
if (-not (Test-Path -Path $JsonPath -PathType Leaf)) {
    Write-Host "❌ Presentation not found: $JsonPath" -ForegroundColor Red
    Write-Host "Available presentations in inputs/:" -ForegroundColor Yellow
    $LessonFolders = Get-ChildItem -Path (Join-Path $ProjectRoot "inputs") -Directory | Select-Object -ExpandProperty Name
    foreach ($Folder in $LessonFolders) {
        Write-Host "  - $Folder" -ForegroundColor Yellow
    }
    exit 1
}

Write-Host "🚀 Fast Edit starting for: $LessonName" -ForegroundColor Green

# Step 1: Generate HTML from JSON
Write-Host ""
Write-Host "📄 Generating HTML from presentation.json..." -ForegroundColor Cyan

try {
    $GenerateCmd = @(
        "python", 
        (Join-Path $ProjectRoot "skills" "creating-html-presentation" "scripts" "generate_presentation.py"),
        $JsonPath
    )
    
    $Output = & python $GenerateCmd 2>&1
    Write-Host $Output
}
catch {
    Write-Host "❌ Error generating HTML: $_" -ForegroundColor Red
    exit 1
}

if ($NoRebuild) {
    Write-Host ""
    Write-Host "✅ Fast Edit complete! Skipping dist rebuild." -ForegroundColor Green
    $PublishedHtmlPath = Join-Path $InputsDir "published" "index.html"
    Write-Host "📁 Published HTML: $PublishedHtmlPath" -ForegroundColor Yellow
    exit 0
}

# Step 2: Rebuild dist
Write-Host ""
Write-Host "📦 Rebuilding dist..." -ForegroundColor Cyan

try {
    $BuildCmd = @(
        "node",
        (Join-Path $ProjectRoot "scripts" "build_dist.js")
    )
    
    $Output = & node $BuildCmd 2>&1
    Write-Host $Output
}
catch {
    Write-Host "❌ Error building dist: $_" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "✅ Fast Edit complete!" -ForegroundColor Green
$DistLocation = Join-Path $ProjectRoot "dist" $LessonName
Write-Host "📦 Dist location: $DistLocation" -ForegroundColor Yellow
Write-Host "🌐 URL: http://127.0.0.1:8080/$LessonName/" -ForegroundColor Yellow

exit 0