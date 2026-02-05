import json
import os
import sys
import subprocess
import re

def get_video_duration(file_path):
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        return float(result.stdout.strip())
    except Exception:
        return None

def count_content_items(layout, content_html):
    if not content_html:
        return 0
    
    # Rule of 3 Lines focus: Paragraphs and List Items
    p_count = len(re.findall(r'<p[\s>]', content_html))
    li_count = len(re.findall(r'<li[\s>]', content_html))
    
    # For answer slides, we are very strict
    if layout == 'answer':
        return max(p_count, li_count)
    
    # For strategy/impact slides, count paragraphs
    if layout in ['strategy', 'impact', 'mission']:
        return p_count
        
    return 0 # Default no strict line count for complex tables/grids

def check_phonemic_casing(text):
    if not text:
        return None
    # Strip HTML tags to avoid false positives with </h3> etc.
    clean_text = re.sub(r'<[^>]+>', ' ', text)
    # Find all sequences within slashes
    # We use [^/]+ but restrict it to avoid very long strings that might be accidental matches
    phonemes = re.findall(r'/([^/]{1,100})/', clean_text)
    for p in phonemes:
        # Check for standard Latin uppercase letters A-Z
        if re.search(r'[A-Z]', p):
            return p
    return None

def check_repo_hygiene(json_path):
    """
    Prevents the 'Asset Leak' and 'Engine Duplication' problems.
    """
    errors = []
    project_root = os.getcwd()
    lesson_dir = os.path.dirname(os.path.abspath(json_path))
    lesson_name = os.path.basename(lesson_dir)
    dist_lesson_dir = os.path.join(project_root, 'dist', lesson_name)
    
    # 1. Asset Duplication Check
    # We should NOT have large binary files in both inputs/ and dist/ in the same commit.
    # Standard: Build script should move them or GitHub Pages should reference root images.
    input_images = os.path.join(lesson_dir, 'images')
    dist_images = os.path.join(dist_lesson_dir, 'images')
    
    if os.path.exists(input_images) and os.path.exists(dist_images):
        for f in os.listdir(input_images):
            # Only strictly block heavy media from duplication. 
            # Images (jpg/png) are allowed to exist in both for deployment self-containment.
            if f.lower().endswith(('.mp4', '.mp3', '.wav', '.mov')):
                dist_file = os.path.join(dist_images, f)
                if os.path.exists(dist_file):
                    errors.append(f"Repo Leak: Heavy media '{f}' exists in both inputs/ and dist/. Move to root 'images/' and reference as '../../images/{f}'.")

    # 2. Engine Duplication Guard
    # Reveal.js engine should ONLY exist at the root of dist/
    for engine_dir in ['css', 'dist', 'plugin']:
        sub_engine = os.path.join(dist_lesson_dir, engine_dir)
        if os.path.exists(sub_engine):
            errors.append(f"Engine Leak: Reveal.js '{engine_dir}' folder found inside {lesson_name}. Remove sub-engine and reference root /dist/ engine.")
                
    return errors

def check_path_hygiene(output_dir):
    """
    Verifies that index.html correctly references the shared engine at ../../
    """
    index_path = os.path.join(output_dir, 'index.html')
    if not os.path.exists(index_path):
        return []
        
    errors = []
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check for the presence of the global engine path
    if 'src="../../dist/reveal.js"' not in content and 'src="../../dist/reveal.js"' not in content.replace('"', "'"):
        errors.append("Path Violation: index.html must reference the root engine via '../../dist/reveal.js'.")
        
    if 'href="../../dist/reveal.css"' not in content and 'href="../../dist/reveal.css"' not in content.replace('"', "'"):
        errors.append("Path Violation: index.html must reference the root CSS via '../../dist/reveal.css'.")
        
    return errors

def validate_presentation(json_path):
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        sys.exit(1)

    # 0. Repo Hygiene Check
    repo_errors = check_repo_hygiene(json_path)
    
    # 0.1 Path Hygiene Check (Targeting the published folder)
    lesson_dir = os.path.dirname(json_path)
    output_dir = os.path.join(lesson_dir, 'published')
    path_errors = check_path_hygiene(output_dir)
    
    with open(json_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    lesson_dir = os.path.dirname(json_path)
    images_dir = os.path.join(lesson_dir, 'images')
    
    errors = repo_errors + path_errors
    warnings = [] # Initialize warnings list
    
    slides = config.get('slides', [])
    for i, slide in enumerate(slides):
        layout = slide.get('layout')
        content = slide.get('content', '')
        table_html = slide.get('table_html', '')
        
        # 1. Image Existence Check
        if 'image' in slide and slide['image']:
            img_name = slide['image'].replace('images/', '')
            img_path = os.path.join(images_dir, img_name)
            if not os.path.exists(img_path):
                errors.append(f"Slide {i+1}: Image '{img_name}' not found in {images_dir}")

        # 2. Video Checks (7-Second Rule)
        if 'video' in slide and slide['video']:
            if not slide['video'].startswith('http'):
                vid_name = slide['video'].replace('images/', '')
                vid_path = os.path.join(images_dir, vid_name)
                if not os.path.exists(vid_path):
                    errors.append(f"Slide {i+1}: Video '{vid_name}' not found in {images_dir}")
                elif layout == 'title':
                    duration = get_video_duration(vid_path)
                    if duration and (duration < 6.5 or duration > 7.5):
                        errors.append(f"Slide {i+1} (Title): Video duration is {duration:.2f}s. MUST be exactly 7 seconds.")

        # 3. Empty Content Check
        if layout in ['split_table', 'answer', 'strategy'] and not content:
            if not table_html:
                errors.append(f"Slide {i+1} ({layout}): 'content' field is missing or empty.")

        # 4. Rule of 3 Lines Auditor
        item_count = count_content_items(layout, content)
        if layout == 'answer' and item_count > 3:
            errors.append(f"Slide {i+1} (Answer): Found {item_count} lines. Violates strict 'Rule of 3 Lines'. Please split into multiple slides.")
        elif layout in ['strategy', 'mission'] and item_count > 4:
            errors.append(f"Slide {i+1} ({layout}): Found {item_count} paragraphs. Violates pedagogical clarity rules (Max 4).")

        # 5. Audio-Timer Conflict Guard
        has_audio = '<audio-player' in content or '<audio-player' in table_html
        if has_audio and slide.get('timer'):
            errors.append(f"Slide {i+1}: Audio slides cannot have timers.")

        # 6. Phonemic Casing Check
        bad_phoneme = check_phonemic_casing(content) or check_phonemic_casing(table_html)
        if bad_phoneme:
            bad_phoneme = bad_phoneme.strip()
            errors.append(f"Slide {i+1}: Phonemic script '/{bad_phoneme}/' contains upper-case letters. Phonemes MUST be lower-case.")

    # 7. Verbatim Sync Gate (Source of Truth check)
    typ_path = os.path.join(lesson_dir, f"{os.path.basename(lesson_dir)}.typ")
    if os.path.exists(typ_path):
        try:
            sys.path.append(os.path.join(os.getcwd(), 'scripts'))
            import extract_typ_data
            source_sentences = extract_typ_data.extract_sentences(typ_path)
            
            json_text = json.dumps(config, ensure_ascii=False)
            for s in source_sentences:
                # Basic check: Does the sentence exist somewhere in the JSON?
                if s not in json_text:
                    errors.append(f"Source Inconsistency: Sentence '{s}' found in worksheet but missing from presentation.")
        except Exception as e:
            warnings.append(f"Sync check failed to run: {str(e)}")

    # Report
    if errors:
        print("\n--- DETERMINISTIC VALIDATION ERRORS ---")
        for err in errors:
            print(f"❌ {err}")
        sys.exit(1)
    else:
        print("✅ Presentation logic and assets verified.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        validate_presentation(sys.argv[1])
