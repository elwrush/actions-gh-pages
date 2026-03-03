"""
validate_media_paths.py — Media Asset Validator

Ensures all media references in presentation.json point to files that:
  1. Exist locally in the lesson folder, OR
  2. Are shared assets that exist in the root /images/ folder

This prevents deploying presentations with broken media links.

Usage:
  python validate_media_paths.py <presentation.json>
"""

import json
import sys
import os
from pathlib import Path

# Known shared assets that exist in the root /images/ on gh-pages
SHARED_MEDIA = {
    "images/mission_bg_clipped.mp4",
    "images/time_machine_bg.mp4",
    "images/basement.jpg",
    "images/discussion_book.png",
    "images/ACT.png",
    "images/gold_bg.mp4",
    "images/horror_house_7s.mp4",
    "images/spooky_woods_7s.mp4",
    "images/kid_boy_7s.mp4",
    "images/microphone_icon_transparent.png"
}

def validate_media_paths(json_path):
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found")
        return False

    lesson_dir = Path(json_path).parent
    local_images_dir = lesson_dir / "images"
    root_images_dir = Path(os.getcwd()) / "images"
    
    errors = []
    warnings = []

    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"[ERROR] JSON Parse Error: {e}")
            return False

    # Check config-level media
    config = data.get('config', {})
    bg_video = config.get('background_video')
    if bg_video:
        if not is_valid_media_path(bg_video, local_images_dir, root_images_dir):
            errors.append(f"Config background_video: '{bg_video}' does not exist")

    # Check slide-level media
    slides = data.get('slides', [])
    for i, slide in enumerate(slides):
        slide_title = slide.get('title', f'Slide {i}')
        
        # Check video
        video = slide.get('video')
        if video:
            if not is_valid_media_path(video, local_images_dir, root_images_dir):
                errors.append(f"Slide {i} ({slide_title}): video '{video}' does not exist")
        
        # Check image
        image = slide.get('image')
        if image:
            if not is_valid_media_path(image, local_images_dir, root_images_dir):
                errors.append(f"Slide {i} ({slide_title}): image '{image}' does not exist")
        
        # Check audio
        audio = slide.get('audio')
        if audio:
            # Handle both /audio/ and audio/
            filename = audio.replace('/audio/', '').replace('audio/', '')
            
            # Check Priority 1: Lesson-specific audio
            local_audio_path = lesson_dir / "audio" / filename
            # Check Priority 2: Root shared audio
            root_audio_path = Path(os.getcwd()) / "audio" / filename
            
            if not local_audio_path.exists() and not root_audio_path.exists():
                errors.append(f"Slide {i} ({slide_title}): audio '{audio}' does not exist (checked {local_audio_path} and {root_audio_path})")

    if errors:
        print("\n[X] MEDIA PATH VALIDATION FAILED:")
        for error in errors:
            print(f"  - {error}")
        print("\n[!] Fix: Either add the missing files or update the JSON to reference existing assets.")
        return False
    
    if warnings:
        print("\n[!] WARNINGS:")
        for warning in warnings:
            print(f"  - {warning}")
    
    print("[OK] Media path validation passed.")
    return True


def is_valid_media_path(path, local_images_dir, root_images_dir):
    """
    Check if media path is valid. Valid means:
      1. It's a known shared asset on gh-pages, OR
      2. It exists in the local lesson images folder, OR
      3. It exists in the root images folder
    """
    # Normalize path by removing leading slash
    norm_path = path.lstrip('/')
    
    if norm_path in SHARED_MEDIA:
        return True
    
    # Check Priority 1: Local lesson folder
    filename = norm_path.replace('images/', '')
    if (local_images_dir / filename).exists():
        return True
        
    # Check Priority 2: Root images folder
    if (root_images_dir / filename).exists():
        return True
    
    return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_media_paths.py <presentation.json>")
        sys.exit(1)
    
    success = validate_media_paths(sys.argv[1])
    sys.exit(0 if success else 1)
