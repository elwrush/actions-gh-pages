import json
import sys
import os
import subprocess
from pathlib import Path

def get_video_duration(file_path):
    """Uses ffprobe to get video duration in seconds."""
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(file_path)
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return float(result.stdout.strip())
    except Exception:
        return None

def validate_hygiene(json_path):
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found")
        return False

    lesson_dir = os.path.dirname(json_path)
    images_dir = os.path.join(lesson_dir, "images")

    errors = []

    # 1. Local Asset Size & Duration Check
    if os.path.exists(images_dir):
        for img in os.listdir(images_dir):
            img_path = os.path.join(images_dir, img)
            if os.path.isfile(img_path):
                # Ignore system files
                if img.lower() == 'desktop.ini': continue

                # Size Check (< 10MB)
                size = os.path.getsize(img_path)
                if size > 10 * 1024 * 1024:
                    errors.append(f"File too large: {img} ({size/1024/1024:.2f}MB). Assets must be < 10MB.")

                # Video Duration Check (STRICT 7s LAW)
                if img.lower().endswith(('.mp4', '.mov', '.avi', '.webm')):
                    duration = get_video_duration(img_path)
                    if duration is not None and duration > 7.5: # 0.5s buffer for encoding drift
                        errors.append(f"RAW VIDEO DETECTED: {img} is {duration:.2f}s long. Background videos MUST be trimmed to 7 seconds using ffmpeg.")



    # 3. JSON Background Check
    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            slides = data.get('slides', [])
            for i, slide in enumerate(slides):
                layout = slide.get('layout', '')
                # Task slides (split_table, ranking, checklist, quiz, etc.)
                if any(k in layout for k in ['table', 'ranking', 'checklist', 'quiz', 'cloze', 'match']):
                    if 'image' in slide and slide['image']:
                        # Exception 1: if they explicitly override with a gradient it might be okay
                        # Exception 2: if the slide has a badge (PROFILE, SCANNING etc.), it's informational, not a pure quiz
                        if 'background_gradient' not in slide and 'badge' not in slide:
                            errors.append(f"Slide {i} ({slide.get('title')}): Question slides must not use image backgrounds. Use green radial design.")
        except Exception as e:
            errors.append(f"JSON Parse Error: {e}")

    if errors:
        print("\n[X] REPO HYGIENE VIOLATIONS:")
        for error in errors:
            print(f"  - {error}")
        print("\n[!] FAILED: Please resize images (<1MB) and move videos to root images/.")
        return False
    
    print("[OK] Repo hygiene check passed.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_hygiene.py <presentation.json>")
        sys.exit(1)
    success = validate_hygiene(sys.argv[1])
    sys.exit(0 if success else 1)
