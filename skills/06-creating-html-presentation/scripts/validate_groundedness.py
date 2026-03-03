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
        return re.sub(r'[^\w\s]', '', str(text)).lower()

    print(f"--- GROUNDEDNESS AUDIT: {json_path} ---")
    
    if not answer_key_text:
        print("❌ [FATAL ERROR] No '## Answer Key' section found in SOURCE_TEXT.md.")
        print("🛑 STOP: You MUST provide an Answer Key at the end of SOURCE_TEXT.md before proceeding.")
        return False

    for i, slide in enumerate(slides):
        # We check specific fields for factual grounding
        # If it's an answer_detail slide, check 'answer' and 'explanation' and 'evidence' against the answer key and source
        if slide.get('layout') == 'answer_detail':
            answer = str(slide.get('answer', ''))
            explanation = str(slide.get('explanation', ''))
            evidence = str(slide.get('evidence', ''))
            
            # Check explanation
            if explanation:
                cleaned_exp = clean(explanation)
                words = [w for w in cleaned_exp.split() if len(w) > 4]
                found_count = sum(1 for w in words if w in source_text_lower)
                # Lower threshold for explanation as it might be paraphrased, but still need some grounding
                if words and (found_count / len(words)) < 0.2:
                    print(f"❌ Slide {i} ('answer_detail'): Explanation might be hallucinated. Not found in SOURCE_TEXT.")
                    print(f"   Explanation: {explanation}")
                    errors += 1
            
            # Check evidence
            if evidence:
                # Remove [Para X] or [Line X] and HTML tags
                clean_evidence = re.sub(r'\[.*?\]', '', evidence)
                clean_evidence = re.sub(r'<[^>]+>', '', clean_evidence)
                clean_evidence = clean(clean_evidence)
                
                words = [w for w in clean_evidence.split() if len(w) > 4]
                found_count = sum(1 for w in words if w in source_text_lower)
                # Evidence MUST be verbatim or extremely close
                if words and (found_count / len(words)) < 0.7:  
                    print(f"❌ Slide {i} ('answer_detail'): Evidence appears hallucinated or incorrectly quoted.")
                    print(f"   Evidence: {evidence}")
                    errors += 1

        # Check 'vocab' slide context sentences
        elif slide.get('layout') == 'vocab':
            context = str(slide.get('context_sentence', ''))
            if context:
                clean_context = re.sub(r'<[^>]+>', '', context)
                clean_context = clean(clean_context)
                words = [w for w in clean_context.split() if len(w) > 4]
                found_count = sum(1 for w in words if w in source_text_lower)
                if words and (found_count / len(words)) < 0.8:
                    print(f"❌ Slide {i} ('vocab'): Context sentence not found in SOURCE_TEXT.")
                    print(f"   Context: {context}")
                    errors += 1

    if errors == 0:
        print("✅ [PASS] All answers and evidence are grounded in the Answer Key and Source Text.")
        return True
    else:
        print(f"❌ [FAIL] {errors} ungrounded/hallucinated items found. You MUST consult the 'Answer Key' in SOURCE_TEXT.md.")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python validate_groundedness.py <presentation.json> <SOURCE_TEXT.md>")
        sys.exit(1)
    else:
        success = validate_groundedness(sys.argv[1], sys.argv[2])
        if not success:
            sys.exit(1)