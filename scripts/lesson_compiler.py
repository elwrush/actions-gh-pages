import json
import os
import sys
from pathlib import Path

def compile_lesson(manifest_path):
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)
    
    lesson_dir = Path(manifest_path).parent
    meta = manifest['meta']
    pedagogy = manifest['pedagogy']
    content = manifest['content']

    # --- 1. GENERATE presentation.json ---
    presentation = {
        "meta": {
            "title": meta['title'],
            "subtitle": meta['subtitle'],
            "theme": "noir",
            "mode": meta['program'].lower()
        },
        "slides": []
    }

    # Extract global mission data for the mission slide
    mission_data = pedagogy.get('mission', {})

    for stage in pedagogy['stages']:
        for slide in stage.get('slides', []):
            # 1.1 Template-specific key mapping (Logic Controller)
            layout = slide.get('layout')
            
            # Title Layout logic
            if layout == 'title':
                slide['title'] = slide.get('title') or meta.get('title')
                slide['subtitle'] = slide.get('subtitle') or meta.get('subtitle')

            # Mission Layout logic
            if layout == 'mission':
                slide['title'] = mission_data.get('title', 'YOUR MISSION')
                # mission.html expects 'items' or 'objectives'
                slide['items'] = mission_data.get('objectives', [])
                slide['main_text'] = mission_data.get('text', '')

            # Strategy Layout logic
            if layout == 'strategy':
                # strategy.html expects 'content'
                if 'main_text' in slide and 'content' not in slide:
                    slide['content'] = slide['main_text']

            # 1.2 Enforce schema 15.0 standards (e.g. video_loop)
            if layout == 'title':
                slide['video_loop'] = True
            
            if layout == 'segue':
                slide['video_loop'] = True
                # Enforce Maroon Background and Zoom Transition for Segues
                slide['background'] = { "type": "color", "src": "#8B1538", "retain_from_previous": False }
                slide['transition'] = "zoom"
            
            # --- CRITICAL FIX: Background Continuity ---
            # If a background exists in the slide, preserve its 'retain_from_previous' flag.
            # If no background exists, default to color but DISABLE retention to avoid video bleed.
            if 'background' not in slide:
                slide['background'] = { 
                    "type": "color", 
                    "src": "#1a1a1a", 
                    "retain_from_previous": False # BREAK THE BLEED
                }
            
            presentation['slides'].append(slide)

    with open(lesson_dir / "presentation.json", 'w', encoding='utf-8') as f:
        json.dump(presentation, f, indent=2)
    print("✅ presentation.json compiled with FIXED background logic.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lesson_compiler.py <manifest.json>")
    else:
        compile_lesson(sys.argv[1])
