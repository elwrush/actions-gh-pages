import os
import shutil
import re
import sys
from pathlib import Path

# --- Configuration ---
PROJECT_ROOT = Path(os.getcwd())
DIST_ROOT = PROJECT_ROOT / "dist"
INPUTS_DIR = PROJECT_ROOT / "inputs"
ENGINE_ROOT = PROJECT_ROOT / "lib" / "reveal"
GLOBAL_IMAGES = PROJECT_ROOT / "images"

# File extensions to skip during asset copy (handled by range requests or too large)
SKIP_EXTENSIONS = {'.webm', '.mov', '.avi'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB limit for individual assets in dist

def log(msg, symbol="[*]"):
    """Terminal-safe logging without emojis to avoid Windows encoding issues."""
    try:
        print(f"{symbol} {msg}")
    except UnicodeEncodeError:
        # Fallback for extremely restricted terminals
        print(f"[*] {msg}")

def clean_dir(directory):
    """Safely remove all files and folders in a directory."""
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)
        return
    
    for item in directory.iterdir():
        try:
            if item.is_dir():
                shutil.rmtree(item, ignore_errors=True)
            else:
                item.unlink()
        except Exception as e:
            pass

def copy_filtered(src, dst, filter_func=None):
    """Copy directory with filtering and size limits."""
    if not src.exists():
        return
    
    dst.mkdir(parents=True, exist_ok=True)
    
    for item in src.iterdir():
        if item.name in ('.git', 'desktop.ini'):
            continue
            
        target = dst / item.name
        
        if item.is_dir():
            copy_filtered(item, target, filter_func)
        else:
            # Apply filters
            if filter_func and not filter_func(item):
                continue
            
            # Size limit check
            try:
                if item.stat().st_size > MAX_FILE_SIZE:
                    continue
            except:
                continue
            
            try:
                shutil.copy2(item, target)
            except:
                pass

def build(target_folder=None):
    log(f"Starting {'targeted' if target_folder else 'full'} build process...", "[BUILD]")

    # 1. Clean dist
    if not target_folder:
        clean_dir(DIST_ROOT)
        log("Cleaned dist directory (Full Build).", "[CLEAN]")
    else:
        target_dist = DIST_ROOT / target_folder
        if target_dist.exists():
            try:
                shutil.rmtree(target_dist, ignore_errors=True)
            except:
                clean_dir(target_dist)
        target_dist.mkdir(parents=True, exist_ok=True)
        log(f"Cleaned target dist: {target_folder}", "[CLEAN]")

    # 2. Process Lessons (Bundled Architecture - each lesson is self-contained)
    log("Aggregating presentations...", "[PROCESS]")
    if target_folder:
        lessons_to_process = [target_folder]
    else:
        lessons_to_process = [d.name for d in INPUTS_DIR.iterdir() if d.is_dir()]
    
    for folder in lessons_to_process:
        lesson_path = INPUTS_DIR / folder
        if not lesson_path.exists():
            continue

        published_path = lesson_path / "published"
        index_html = published_path / "index.html"
        source_dir = published_path
        
        if not index_html.exists():
            index_html = lesson_path / "index.html"
            source_dir = lesson_path
            
        if index_html.exists():
            log(f"Processing lesson: {folder}", "[OK]")
            dest_lesson_dir = DIST_ROOT / folder

            try:
                # Copy entire published folder as-is (self-contained bundle)
                def asset_filter(p):
                    return p.suffix.lower() not in SKIP_EXTENSIONS
                copy_filtered(source_dir, dest_lesson_dir, asset_filter)
            except Exception as e:
                 log(f"Error processing {folder}: {e}", "[ERROR]")

    # 5. Update Dashboard
    log("Updating dashboard...", "[DASHBOARD]")
    dashboard_lessons = []
    
    if DIST_ROOT.exists():
        for d in DIST_ROOT.iterdir():
            if d.is_dir() and d.name not in ('dist', 'plugin', 'css', 'images'):
                idx = d / "index.html"
                if idx.exists():
                    try:
                        txt = idx.read_text(encoding='utf-8')
                        title_match = re.search(r'<title>(.*?)</title>', txt)
                        title = title_match.group(1) if title_match else d.name
                        dashboard_lessons.append({"folder": d.name, "title": title})
                    except:
                        dashboard_lessons.append({"folder": d.name, "title": d.name})

    dashboard_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bell Language Centre | Presentations Library</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #1a1a1a; color: white; padding: 40px; }}
        h1 {{ color: #8B1538; border-bottom: 2pt solid #8B1538; padding-bottom: 10px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; margin-top: 30px; }}
        .card {{ background: #2a2a2a; border-radius: 8px; padding: 20px; transition: transform 0.2s; border: 1px solid #444; text-decoration: none; color: white; display: block; }}
        .card:hover {{ transform: translateY(-5px); border-color: #8B1538; }}
        .card h3 {{ margin-top: 0; color: #FFD700; }}
        .card p {{ font-size: 0.9em; color: #ccc; }}
    </style>
</head>
<body>
    <h1> Presentations Library</h1>
    <div class="grid">
        {"".join([f'<a href="{l["folder"]}/" class="card"><h3>{l["title"]}</h3><p>{l["folder"]}</p></a>' for l in dashboard_lessons])}
    </div>
</body>
</html>
    """
    (DIST_ROOT / "index.html").write_text(dashboard_html, encoding='utf-8')
    log("Build complete!", "[DONE]")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else None
    build(target)
