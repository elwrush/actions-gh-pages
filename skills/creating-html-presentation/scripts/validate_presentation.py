import argparse
import os
import re
from bs4 import BeautifulSoup
import sys
import io

# Fix Windows console encoding for emoji
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def validate_presentation(html_path, mode):
    print(f"🔍 Validating {html_path} in '{mode}' mode...")
    
    if not os.path.exists(html_path):
        print(f"❌ CRITICAL: File not found: {html_path}")
        return False

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'html.parser')

    issues = []
    warnings = []
    
    # 1. ASSET INTEGRITY (Critical)
    # Check all images and audio
    media_tags = soup.find_all(['img', 'audio', 'video', 'source'])
    base_dir = os.path.dirname(html_path)
    
    print(f"   Checking {len(media_tags)} media assets...")
    
    for tag in media_tags:
        src = tag.get('src') or tag.get('data-src')
        if src:
            # Handle absolute/relative paths
            # In the specific failed case, source was "../../images/..." which might be valid from the server perspective 
            # but we should check if it exists relative to the file.
            
            # Simple clean up of anchors or query params
            clean_src = src.split('?')[0].split('#')[0]
            
            # Construct absolute path for checking
            if os.path.isabs(clean_src):
                full_path = clean_src
            else:
                full_path = os.path.normpath(os.path.join(base_dir, clean_src))
                
            if not os.path.exists(full_path):
                 # Try determining if it's a project root reference (common in this project)
                 # If path starts with ../ try to resolve
                 issues.append(f"❌ Broken Link: '{src}' does not exist at {full_path}")

    # 2. BRANDING ENFORCEMENT (DEPRECATED)
    # User request: No branding logos (Bell or Intensive) ever. Removed check.

    # 3. CSS HYGIENE (Critical for Layout)
    # Check for inline font sizes which cause 'explosions'
    # RELAXED: Allow font-size if used in grid layouts or specific typography tweaks
    elements_with_style = soup.find_all(attrs={"style": True})
    for el in elements_with_style:
        style = el['style'].lower()
        if "font-size" in style:
            # Check context - if it's a heading or special text, it might be intentional override
            classes = el.get('class', [])
            if isinstance(classes, str): classes = classes.split()
            
            # Allow phonemes or large headers which need overrides
            if 'phoneme' in classes or el.name == 'h1' or 'check-item' in classes:
                continue
                
            # Allow grid/flex adjustments
            if 'grid' in style or 'flex' in style:
                continue
                
            # Otherwise warn but don't fail (Downgraded from critical)
            warnings.append(f"⚠️ Inline CSS Warning: 'font-size' found in style attribute on <{el.name}>. Prefer classes where possible.")

    # 4. LAYOUT SAFETY (MERGED INTO CHECK 8)
    # Legacy check removed - now enforced via .inset-media/.constrained-media class check
    imgs = soup.find_all('img')

    # 6. ASSET PROVENANCE (Legal/Process)
    # Check that audio files have attribution (proving they came from Freesound)
    # Exception: "vocab_" files (TTS) or "generated_" (Internal)
    audio_tags = soup.find_all('audio')
    for tag in audio_tags:
        src = tag.get('src') or tag.get('data-src')
        if not src:
            source_tag = tag.find('source')
            if source_tag:
                src = source_tag.get('src')
        
        if src and not src.startswith('http'): # Only check local files
            filename = os.path.basename(src)
            if "vocab_" in filename or "tts_" in filename:
                continue # Skip TTS
             
            # Check for attribution file
            base_name = os.path.splitext(src)[0]
            attr_file = f"{base_name}_attribution.txt"
            
            # Resolve path
            clean_attr = attr_file.split('?')[0].split('#')[0]
            full_attr_path = os.path.normpath(os.path.join(base_dir, clean_attr))
            
            if not os.path.exists(full_attr_path):
                warnings.append(f"⚠️ Provenance Warning: Audio file '{filename}' has no attribution file ('{os.path.basename(attr_file)}'). Did you use the 'searching-freesound' skill?")

    # 5. TIMER COMPONENT ENFORCEMENT (New)
    # Check for <timer-pill> on task slides
    sections = soup.find_all('section')
    task_slides = []
    for i, section in enumerate(sections):
        text = section.get_text().upper()
        if 'TASK' in text and ('PRACTICE' in text or 'PRODUCTION' in text or 'CONTROLLED' in text):
            task_slides.append((i, section))
    
    for idx, section in task_slides:
        timer = section.find('timer-pill')
        if not timer:
            warnings.append(f"⚠️ Timer Missing: Slide {idx+1} appears to be a task slide but has no <timer-pill> component.")

    # 6. AUDIO FOLDER CHECK (Required for timer-pill)
    timer_pills = soup.find_all('timer-pill')
    if timer_pills:
        audio_dir = os.path.join(base_dir, 'audio')
        required_audio = ['blip.mp3', '30-seconds.mp3', 'bell.mp3']
        for audio_file in required_audio:
            audio_path = os.path.join(audio_dir, audio_file)
            if not os.path.exists(audio_path):
                issues.append(f"❌ Audio Missing: Timer component requires '{audio_file}' in audio/ folder.")

    # 7. ANSWER SLIDE INTERLEAVING CHECK (New)
    # Task slides should be followed by answer slides within 2 slides
    for i, section in enumerate(sections):
        text = section.get_text().upper()
        if 'TASK' in text and ('IDENTIFY' in text or 'FILL' in text or 'CLASSIFY' in text):
            # Look for answer slide in next 3 slides
            found_answer = False
            for j in range(i+1, min(i+4, len(sections))):
                answer_text = sections[j].get_text().upper()
                if 'ANSWER' in answer_text:
                    found_answer = True
                    break
            if not found_answer:
                warnings.append(f"⚠️ Answer Interleaving: Slide {i+1} appears to be a task but no ANSWER slide found within next 3 slides.")

    # 8. DOCUMENTED CSS CLASS ENFORCEMENT
    # Check images use .inset-media or .constrained-media
    # EXCEPTION: Images inside <slide-*> components are styled automatically
    for img in imgs:
        # Check if parent is a custom element
        parent = img.find_parent(re.compile(r'slide-.*'))
        if parent:
            continue # Skip check for components
            
        classes = img.get('class', [])
        if isinstance(classes, str):
            classes = classes.split()
        if 'inset-media' not in classes and 'constrained-media' not in classes:
            src = img.get('src') or img.get('data-src') or 'unknown'
            issues.append(f"❌ Component Violation: Image '{os.path.basename(src)}' must use '.inset-media' or '.constrained-media' class.")

    # 9. LAYOUT CONTAINER CHECK
    # Slides must use either .slide-canvas OR a <slide-*> component
    for i, section in enumerate(sections):
        canvas = section.find(class_='slide-canvas')
        component = section.find(re.compile(r'slide-.*'))
        
        # Skip segue slides (manual or component)
        text = section.get_text().upper()
        if 'PHASE' in text and ':' in text:
            continue
            
        if not canvas and not component and section.find_all(recursive=False):
            # Has content but no canvas and no component
            warnings.append(f"⚠️ Layout Warning: Slide {i+1} has no '.slide-canvas' wrapper or <slide-*> component.")

    # 10. LIBRARY CHECK (New)
    if soup.find(re.compile(r'slide-.*')):
        script = soup.find('script', src=re.compile(r'.*slide-components\.js'))
        if not script:
            issues.append("❌ Library Missing: <slide-*> components used but 'slide-components.js' not imported.")

    # 7. VIDEO CHECK
    # We prefer YouTube embeds, but if local video is used, warn to verify source.
    video_tags = soup.find_all('video')
    if video_tags:
         warnings.append(f"⚠️ Video Content: {len(video_tags)} local <video> tags found. Verify these are from Pixabay and not AI-generated.")


    # REPORTING
    print("\n--- VALIDATION REPORT ---")
    if warnings:
        for w in warnings:
            print(w)
            
    if issues:
        for i in issues:
            print(i)
        print(f"\n🚫 FAILED: {len(issues)} critical issues found.")
        return False
    else:
        print("\n✅ PASSED: No critical issues found.")
        return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate HTML Presentation against SKILL rules.")
    parser.add_argument("file", help="Path to index.html")
    parser.add_argument("--mode", choices=["bell", "intensive"], required=True, help="Branding mode")
    
    args = parser.parse_args()
    
    success = validate_presentation(args.file, args.mode)
    if not success:
        sys.exit(1)
