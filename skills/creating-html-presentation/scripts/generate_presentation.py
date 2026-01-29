
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
    core_dir = os.path.join(skill_dir, 'reveal_core')
    
    output_dir = os.path.dirname(json_path)
    
    # 3. Copy Assets (Reveal Core + CSS)
    # Use ignore function to skip GDrive system files and hidden files
    ignore_func = shutil.ignore_patterns('desktop.ini', '.*')
    
    for folder in ['dist', 'plugin', 'css']:
        src = os.path.join(skill_dir, folder) if folder == 'css' else os.path.join(core_dir, folder)
        dst = os.path.join(output_dir, folder)
        
        if os.path.exists(src):
            # Using dirs_exist_ok=True (Python 3.8+) to merge/update folders
            shutil.copytree(src, dst, ignore=ignore_func, dirs_exist_ok=True)
            print(f"📦 Synchronized {folder} to: {dst}")

    # 4. Copy Audio Assets
    audio_src = os.path.join(os.path.dirname(skill_dir), 'audio') # Project Root/audio
    audio_dst = os.path.join(output_dir, 'audio')
    if not os.path.exists(audio_dst):
        os.makedirs(audio_dst)
    
    for item in ['blip.mp3', 'bell.mp3', '30-seconds.mp3']:
        src_file = os.path.join(audio_src, item)
        dst_file = os.path.join(audio_dst, item)
        if os.path.exists(src_file) and not os.path.exists(dst_file):
            shutil.copy2(src_file, dst_file)
            print(f"🎵 Copied {item} to: {audio_dst}")

    # 5. Render Template
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('base.html')
    output_html = template.render(
        meta=config.get('meta', {}),
        slides=config.get('slides', [])
    )

    # 6. Save Output
    output_path = os.path.join(output_dir, 'index.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_html)
        
    print(f"✨ Presentation generated successfully at: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_presentation.py <path_to_config.json>")
        sys.exit(1)
    
    json_path = sys.argv[1]
    generate_presentation(json_path)
