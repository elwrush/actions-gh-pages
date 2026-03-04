import json
import os
import sys
import shutil
import re
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from PIL import Image

def resize_image_internal(src_path, dst_path, max_width=1920, quality=85):
    """Resizes an image if it exceeds max_width and saves it as optimized JPEG/PNG."""
    # Ensure they are strings for consistency
    src_path = str(src_path)
    dst_path = str(dst_path)

    try:
        with Image.open(src_path) as img:
            # Convert to RGB if saving as JPEG
            if img.mode in ("RGBA", "P") and dst_path.lower().endswith((".jpg", ".jpeg")):
                img = img.convert("RGB")

            width, height = img.size
            if width > max_width:
                ratio = max_width / float(width)
                new_size = (max_width, int(height * ratio))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
                print(f"  [RESIZE] {os.path.basename(src_path)}: {width}px -> {max_width}px")

            img.save(dst_path, optimize=True, quality=quality)

            final_size = os.path.getsize(dst_path)
            if final_size > 1024 * 1024:
                print(f"  [WARN] {os.path.basename(dst_path)} is still large: {final_size/1024/1024:.2f}MB")
    except Exception as e:
        print(f"  [ERROR] Processing {os.path.basename(src_path)}: {e}")
        shutil.copy2(src_path, dst_path)

# Manual import of jinja_parser filter
def parse_directives(text):
    if not isinstance(text, str):
        return text
    # Gapfills: [REVEAL: text] -> <span class="fragment highlight-gold">text</span>
    text = re.sub(r'\[REVEAL:\s*(.*?)\]', r'<span class="fragment" style="color: #FFD700; font-weight: bold;">\1</span>', text)
    # Strikethrough: [STRIKE: text] -> <span class="fragment strike-anim">text</span>
    text = re.sub(r'\[STRIKE:\s*(.*?)\]', r'<span class="fragment strike-anim">\1</span>', text)
    # Highlights: [HIGHLIGHT: text] -> <span style="color: #FFD700;">text</span>
    text = re.sub(r'\[HIGHLIGHT:\s*(.*?)\]', r'<span style="color: #FFD700; font-weight: bold;">\1</span>', text)
    return text

def generate_presentation(json_path):
    # 1. Load Configuration
    with open(json_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    # 2. Setup Environment
    script_dir = Path(__file__).resolve().parent
    skill_dir = script_dir.parent
    template_dir = skill_dir / "templates"
    project_root = skill_dir.parents[1]

    # Use the internal reveal.js library
    reveal_source = project_root / "lib" / "reveal"
    
    # Target 'published' folder within the lesson directory
    lesson_dir = Path(json_path).resolve().parent
    output_dir = lesson_dir / "published"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 2.1 Surgical Cleanup (Preserve PDFs)
    print("  [CLEAN] Removing old slideshow assets (preserving PDFs)...")
    for item in ["dist", "plugin", "fontawesome", "images", "audio", "css", "index.html"]:
        target = output_dir / item
        if target.exists():
            if target.is_dir():
                shutil.rmtree(target, ignore_errors=True)
            else:
                try:
                    target.unlink()
                except:
                    pass

    # Implementation Choice: If lib/reveal is missing core folders, we try to clone the shallow repo
    if not (reveal_source / "dist").exists() or not (reveal_source / "plugin").exists():
        reveal_source.parent.mkdir(exist_ok=True)
        print(f"  [GIT] Cloning reveal.js into {reveal_source}...")
        os.system(f'git clone --depth 1 https://github.com/hakimel/reveal.js.git "{reveal_source}"')
    
    # 3. Bundle Reveal.js Engine & UI Assets
    print("[1/4] Bundling engine & UI assets...")
    for folder in ["dist", "plugin", "fontawesome"]:
        dst = output_dir / folder
        src = reveal_source / folder
        
        # Special case: fontawesome might be in project_root/lib/fontawesome instead of project_root/lib/reveal/fontawesome
        if folder == "fontawesome" and not src.exists():
            alt_src = project_root / "lib" / "fontawesome"
            if alt_src.exists():
                src = alt_src

        if src.exists():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".git", "node_modules"))
        else:
            if folder == "fontawesome":
                print(f"  [WARN] fontawesome not found in {reveal_source} or {project_root / 'lib' / 'fontawesome'}. UI icons might be missing.")
            else:
                print(f"[ERROR] Failed to acquire {folder} from {reveal_source}")
                sys.exit(1)

    # Bundling shared CSS
    css_dst = output_dir / "css"
    css_dst.mkdir(exist_ok=True)
    shared_css = project_root / "css"
    if shared_css.exists():
        for f in shared_css.glob("*.css"):
            shutil.copy2(f, css_dst)

    # 4. Resolve and Optimize Media
    print("[2/4] Resolving and optimizing media...")
    images_dst = output_dir / "images"
    images_dst.mkdir(exist_ok=True)
    
    # 4.1 Collect all referenced media from JSON content
    raw_json = json.dumps(config)
    # Match both /images/file.jpg and images/file.jpg
    # Stopping before closing quotes or backslashes
    referenced_images = set(re.findall(r'/?images/([^"\'\\]+?)(?=["\'\\])', raw_json))
    
    # Also check specific image/video/background fields
    for slide in config.get("slides", []):
        for field in ["image", "video", "background"]:
            val = slide.get(field)
            if not val:
                continue
                
            # Handle structured background object
            if field == "background" and isinstance(val, dict):
                val = val.get("src")
                if not val:
                    continue
            
            # Now val should be a string (path)
            if not isinstance(val, str):
                continue

            # Support both absolute /images/ and relative images/
            if val.startswith("/images/"):
                referenced_images.add(val.replace("/images/", ""))
            elif val.startswith("images/"):
                referenced_images.add(val.replace("images/", ""))

    # 4.1.5 Scan templates for hardcoded image references (e.g., ACT.png)
    for template_file in template_dir.glob("*.html"):
        try:
            content = template_file.read_text(encoding="utf-8")
            # Match patterns like src="images/file.png" or data-background="images/file.jpg"
            hardcoded = re.findall(r'(?:src|data-background)=["\']/?images/([^"\']+)["\']', content)
            referenced_images.update(hardcoded)
        except Exception as e:
            print(f"  [WARN] Failed to scan template {template_file.name}: {e}")

    # 4.2 Copy and Optimize referenced images
    local_images_src = lesson_dir / "images"
    root_images_src = project_root / "images"
    
    for filename in referenced_images:
        # Safety check: ensure we have a string
        if isinstance(filename, tuple):
            filename = filename[0]
            
        src = None
        # Priority 1: Lesson-specific images
        if (local_images_src / filename).exists():
            src = local_images_src / filename
        # Priority 2: Root shared images
        elif (root_images_src / filename).exists():
            src = root_images_src / filename
        
        if src:
            dst = images_dst / filename
            if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                # Optimize/Resize Images
                resize_image_internal(src, dst)
            else:
                # Copy videos/other media as-is
                shutil.copy2(src, dst)
                print(f"  [COPY] {filename}")
        else:
            print(f"  [MISSING] {filename} referenced but not found in lesson or root images/")

    # 5. Handle Audio
    print("[3/4] Processing audio...")
    audio_dst = output_dir / "audio"
    audio_dst.mkdir(exist_ok=True)

    # Lesson audio
    lesson_audio_src = lesson_dir / "audio"
    if lesson_audio_src.exists():
        shutil.copytree(lesson_audio_src, audio_dst, dirs_exist_ok=True)

    # Standard UI sounds
    root_audio_src = project_root / "audio"
    if root_audio_src.exists():
        for item in ["blip.mp3", "bell.mp3", "30-seconds.mp3", "warning.mp3"]:
            src_file = root_audio_src / item
            if src_file.exists():
                shutil.copy2(src_file, audio_dst)

    # 6. Render Template with Relative Paths
    print("[4/4] Rendering template...")
    env = Environment(loader=FileSystemLoader(str(template_dir)))
    env.filters["parse_directives"] = parse_directives
    template = env.get_template("base.html")

    
    # Update slide URLs to be relative to the published folder
    # Note: In the HTML, assets like /images/foo.png should now be ./images/foo.png
    # We can handle this by making root_path empty and ensuring no leading slash in template
    
    output_html = template.render(
        meta=config.get("meta", {}),
        slides=config.get("slides", []),
        root_path="",  # Made empty for relative pathing
    )

    # Clean up the leading slashes in rendered HTML for images/videos
    # Actually, it's safer to do this in the template, but we can do a broad replace here too
    output_html = output_html.replace('="/images/', '="images/')
    output_html = output_html.replace('="/audio/', '="audio/')

    # Save Output
    output_path = output_dir / "index.html"
    output_path.write_text(output_html, encoding="utf-8")
    print(f"[SUCCESS] Presentation bundled at: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_presentation.py <path_to_config.json>")
        sys.exit(1)

    json_path = sys.argv[1]
    generate_presentation(json_path)
