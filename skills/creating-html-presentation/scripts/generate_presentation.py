
import json
import os
import sys
import shutil
from jinja2 import Environment, FileSystemLoader

def generate_presentation(json_path):
    # 1. Load Configuration
    with open(json_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # 2. Setup Environment
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = os.path.dirname(script_dir)
    template_dir = os.path.join(skill_dir, 'templates')
    
    # Locate project root (assuming script is in skills/creating-html-presentation/scripts)
    # skill_dir = .../skills/creating-html-presentation
    # dirname(skill_dir) = .../skills
    # dirname(dirname(skill_dir)) = .../LESSONS AND SLIDESHOWS 2
    project_root = os.path.dirname(os.path.dirname(skill_dir))
    
    # Use the local cloned reveal.js repo as requested
    reveal_source = os.path.join(project_root, 'temp_reveal_repo')
    if not os.path.exists(reveal_source):
        print(f"[ERROR] Local reveal.js clone not found at: {reveal_source}")
        sys.exit(1)

    # Target 'published' folder within the lesson directory
    lesson_dir = os.path.dirname(json_path)
    output_dir = os.path.join(lesson_dir, 'published')
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 3. Assets Logic (REFACTORED)
    # Individual lessons no longer carry the Reveal engine (dist/plugin/css).
    # These are hosted at the root level of the library for efficiency.
    
    # Use ignore function to skip GDrive system files and hidden files
    ignore_func = shutil.ignore_patterns('desktop.ini', '.*', '.git', 'node_modules', 'test', 'examples', 'gulpfile.js', 'package.json')

    # 3.5 Copy Lesson Images (MANDATORY for published folder portability)
    images_src = os.path.join(lesson_dir, 'images')
    images_dst = os.path.join(output_dir, 'images')
    if not os.path.exists(images_dst):
        os.makedirs(images_dst)

    if os.path.exists(images_src):
        shutil.copytree(images_src, images_dst, ignore=ignore_func, dirs_exist_ok=True)
        print(f"Synchronized images to: {images_dst}")

    # Copy ACT logo from project root
    act_logo_src = os.path.join(os.path.dirname(os.path.dirname(skill_dir)), 'images', 'ACT.png')
    if os.path.exists(act_logo_src):
        shutil.copy2(act_logo_src, os.path.join(images_dst, 'ACT.png'))
        print(f"Copied ACT logo to: {images_dst}")

    # 4. Copy Audio Assets
    project_root = os.path.dirname(os.path.dirname(skill_dir))
    audio_src = os.path.join(project_root, 'audio') # Project Root/audio
    audio_dst = os.path.join(output_dir, 'audio')
    if not os.path.exists(audio_dst):
        os.makedirs(audio_dst)
    
    for item in ['blip.mp3', 'beep.mp3', 'bell.mp3', '30-seconds.mp3', 'warning.mp3']:
        src_file = os.path.join(audio_src, item)
        dst_file = os.path.join(audio_dst, item)
        if os.path.exists(src_file) and not os.path.exists(dst_file):
            shutil.copy2(src_file, dst_file)
            print(f"Copied {item} to: {audio_dst}")

    # 5. Render Template
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('base.html')
    # Pre-process slides for video URL construction
    for slide in config.get('slides', []):
        if slide.get('layout') == 'video' and slide.get('video_id'):
            start = slide.get('start', '0')
            end = slide.get('end', '')
            url = f"https://www.youtube.com/embed/{slide['video_id']}?start={start}"
            if end:
                url += f"&end={end}"
            slide['video_url'] = url
        
        # Ensure autoplay and looping for background videos as per request
        if 'video_url' in slide and slide['video_url'].endswith('.mp4'):
            # These will be used in data-background-video-* attributes
            slide['video_autoplay'] = True
            slide['video_loop'] = True

    output_html = template.render(
        meta=config.get('meta', {}),
        slides=config.get('slides', [])
    )

    # 6. Save Output
    output_path = os.path.join(output_dir, 'index.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_html)
        
    print(f"Presentation generated successfully at: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_presentation.py <path_to_config.json>")
        sys.exit(1)
    
    json_path = sys.argv[1]
    generate_presentation(json_path)
