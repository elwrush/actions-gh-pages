import json
import sys
import re
from pathlib import Path
import io

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def validate_groundedness(json_path, source_text_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    with open(source_text_path, 'r', encoding='utf-8') as f:
        source_text = f.read()

    # Extract Answer Key block if it exists - be very flexible with whitespace
    answer_key_match = re.search(r'##\s*Answer\s*Key\s*(.*)', source_text, re.DOTALL | re.IGNORECASE)
    answer_key_text = answer_key_match.group(1).lower() if answer_key_match else ""
    source_text_lower = source_text.lower()

    errors = 0
    slides = data.get('slides', [])
    
    # Text cleaning for comparison
    def clean(text):
        # Remove HTML tags and bracketed directives first
        text = re.sub(r'<[^>]+>', '', str(text))
        text = re.sub(r'\[(REVEAL|STRIKE|HIGHLIGHT):\s*(.*?)\]', r'\2', text)
        return re.sub(r'[^\w\s]', '', text).lower()

    def check_text(text, slide_info, threshold=0.7):
        nonlocal errors
        if not text: return
        
        cleaned = clean(text)
        # Filter for significant words to avoid noise from stop words
        words = [w for w in cleaned.split() if len(w) > 3]
        if not words: return

        found_count = sum(1 for w in words if w in source_text_lower)
        ratio = found_count / len(words)
        
        if ratio < threshold:
            print(f"❌ {slide_info}: Text not grounded in SOURCE_TEXT (Found {found_count}/{len(words)} key words).")
            print(f"   Sample: \"{text[:100]}...\"")
            errors += 1

    print(f"--- GROUNDEDNESS AUDIT: {json_path} ---")
    
    if not answer_key_text:
        print("❌ [FATAL ERROR] No '## Answer Key' section found in SOURCE_TEXT.md.")
        return False

    for i, slide in enumerate(slides):
        layout = slide.get('layout')
        slide_id = slide.get('slide_id', f"Slide {i+1}")
        
        # 1. Answer Detail Layout
        if layout == 'answer_detail':
            check_text(slide.get('answer'), f"{slide_id} (answer)")
            check_text(slide.get('explanation'), f"{slide_id} (explanation)", threshold=0.3) # Loose for explanation
            check_text(slide.get('evidence'), f"{slide_id} (evidence)", threshold=0.8) # Strict for evidence

        # 2. Vocab Layout
        elif layout == 'vocab':
            check_text(slide.get('context_sentence'), f"{slide_id} (vocab context)", threshold=0.8)

        # 3. Tables and Content Layouts (NEW: Broad Scan)
        elif layout in ['split_table', 'impact', 'strategy']:
            content = slide.get('content', '') or slide.get('main_text', '') or slide.get('text', '')
            # Extract items from lists or points
            if slide.get('points'):
                for p in slide.get('points'):
                    content += " " + p.get('text', '')
            if slide.get('strategy_items'):
                for s in slide.get('strategy_items'):
                    content += " " + s.get('text', '')
            
            # Check the consolidated text
            if content:
                # We specifically look for sentences that look like task items (e.g. including [REVEAL:])
                check_text(content, f"{slide_id} ({layout} content)", threshold=0.6)

    if errors == 0:
        print("✅ [PASS] All slide content is grounded in the Answer Key or Source Text.")
        return True
    else:
        print(f"❌ [FAIL] {errors} ungrounded/hallucinated items found. Fix your manifest or update SOURCE_TEXT.md.")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python validate_groundedness.py <presentation.json> <SOURCE_TEXT.md>")
        sys.exit(1)
    else:
        success = validate_groundedness(sys.argv[1], sys.argv[2])
        if not success:
            sys.exit(1)
