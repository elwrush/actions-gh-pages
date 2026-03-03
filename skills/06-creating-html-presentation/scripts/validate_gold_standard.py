import json
import sys
import os
import re

def validate_gold_standard(json_path):
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found")
        return False

    with open(json_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"JSON Parse Error: {e}")
            return False

    slides = data.get("slides", [])
    errors = []
    warnings = []

    # --- TECHNICAL SCHEMA CHECKS (ZERO-CRASH) ---
    for i, slide in enumerate(slides):
        layout = slide.get("layout")
        
        # 1. Layout Key
        if "template" in slide:
            errors.append(f"Slide {i+1}: BANNED key 'template' found. Use 'layout' instead.")
        if not layout:
            errors.append(f"Slide {i+1}: Missing mandatory 'layout' key.")

        # 2. Root-Level Data (No nesting in 'data')
        if "data" in slide and isinstance(slide["data"], dict) and len(slide["data"]) > 0:
            errors.append(f"Slide {i+1}: BANNED nesting. Data must be at root level of slide object, not in 'data' sub-block.")

        # 3. Type Strictness: Timer
        if "timer" in slide:
            if not isinstance(slide["timer"], int):
                errors.append(f"Slide {i+1}: 'timer' MUST be an integer (e.g., 120), not {type(slide['timer']).__name__}.")

        # 4. Video Loop Check
        if slide.get("video"):
            if "video_loop" in slide:
                if not isinstance(slide["video_loop"], bool):
                    errors.append(f"Slide {i+1}: 'video_loop' MUST be a boolean (true/false), not {type(slide['video_loop']).__name__}.")
            else:
                if layout in ["title", "segue"]:
                    errors.append(f"Slide {i+1} ({layout}): Missing 'video_loop': true for background video.")

        # --- COMPONENT KEY MANDATES (PEDAGOGICAL INTEGRITY) ---
        if layout == "strategy":
            items = slide.get("strategy_items", [])
            if not items and not slide.get("content") and not slide.get("table"):
                errors.append(f"Slide {i+1} (strategy): Missing pedagogical content (strategy_items, content, or table).")
            
            # Pedagogical Mandate Check (Heuristic)
            for item in items:
                text = item.get("text", "")
                # If an item looks like a definition (e.g. "Word: definition")
                if ":" in text and len(text.split(":")[0].split()) <= 2:
                    warnings.append(f"Slide {i+1} (strategy): Possible Pedagogical Violation. Strategy items should provide instruction (how to learn), not just definitions ('{text}').")

            # Iron Rule: Badge Check
            if not slide.get("badge"):
                errors.append(f"Slide {i+1} (strategy): IRON RULE VIOLATION. Missing mandatory 'badge' (e.g., TASK 1).")
        
        if layout == "impact":
            if not slide.get("text") and not slide.get("main_text"):
                errors.append(f"Slide {i+1} (impact): Missing mandatory 'text' field.")
            if not slide.get("image"):
                warnings.append(f"Slide {i+1} (impact): No background 'image' provided.")
            # Iron Rule: Badge Check
            if not slide.get("badge"):
                errors.append(f"Slide {i+1} (impact): IRON RULE VIOLATION. Missing mandatory 'badge' (e.g., TASK 1).")
            
        # --- AUDIO OVER TIMER LAW (LISTENING VS READING) ---
        slide_text_content = str(slide.get("text", "")) + str(slide.get("title", "")) + str(slide.get("notes", "")) + str(slide.get("main_text", ""))
        is_listening_slide = any(word in slide_text_content.lower() for word in ["listen", "audio", "track", "recording"]) or slide.get("audio")
        
        if is_listening_slide:
            if slide.get("timer"):
                errors.append(f"Slide {i+1} ({layout}): AUDIO OVER TIMER VIOLATION. Listening tasks must NOT use 'timer'. Use 'audio' scrubber instead.")
            if layout in ["impact", "split_table"] and not slide.get("audio") and any(word in slide_text_content.lower() for word in ["listen", "track", "recording"]):
                errors.append(f"Slide {i+1} ({layout}): AUDIO MANDATE VIOLATION. Listening tasks must include an 'audio' field.")
        else:
            # Timer Mandate for Impact (Reading/Grammar/etc)
            if layout == "impact" and not slide.get("timer"):
                errors.append(f"Slide {i+1} (impact): TIMER MANDATE VIOLATION. Non-listening tasks must have a 'timer' (int).")

        if layout == "answer":
            if not slide.get("answers") and not slide.get("content"):
                errors.append(f"Slide {i+1} (answer): Missing answer content ('answers' array or 'content' string).")
            if not slide.get("badge"):
                errors.append(f"Slide {i+1} (answer): IRON RULE VIOLATION. Missing mandatory 'badge'.")

        if layout == "answer_detail":
            if not slide.get("question") and not slide.get("title"):
                errors.append(f"Slide {i+1} (answer_detail): Missing 'question' field.")
            if not slide.get("answer"):
                errors.append(f"Slide {i+1} (answer_detail): Missing 'answer' field.")
            if not slide.get("badge"):
                errors.append(f"Slide {i+1} (answer_detail): IRON RULE VIOLATION. Missing mandatory 'badge'.")

        if layout == "ranking":
            if not slide.get("left_items") or not slide.get("right_items"):
                errors.append(f"Slide {i+1} (ranking): Missing 'left_items' or 'right_items'.")
            if not slide.get("badge"):
                errors.append(f"Slide {i+1} (ranking): IRON RULE VIOLATION. Missing mandatory 'badge'.")

        if layout == "match_draw":
            if not slide.get("left_items") or not slide.get("right_items") or not slide.get("connections"):
                errors.append(f"Slide {i+1} (match_draw): Missing 'left_items', 'right_items', or 'connections'.")
            if not slide.get("badge"):
                errors.append(f"Slide {i+1} (match_draw): IRON RULE VIOLATION. Missing mandatory 'badge'.")

        if layout == "mission":
            if not slide.get("items") and not slide.get("mission_items") and not slide.get("objectives"):
                errors.append(f"Slide {i+1} (mission): Missing mission items.")

    # --- PEDAGOGICAL & VISUAL FLOW CHECKS ---

    # 1. Mission Mandate (Slide 2)
    if len(slides) > 1:
        mission_slide = slides[1]
        if mission_slide.get("layout") != "mission":
            errors.append("Slide 2 MUST be a 'mission' slide.")
        else:
            if mission_slide.get("title") != "YOUR MISSION":
                errors.append("Mission slide title MUST be exactly 'YOUR MISSION'.")
            if "mission_bg_clipped.mp4" not in str(mission_slide.get("video", "")):
                errors.append("Mission slide MUST use 'mission_bg_clipped.mp4'.")

    # 2. Segue-Bridge Mandate
    for i in range(len(slides) - 1):
        if slides[i].get("layout") == "segue":
            next_layout = slides[i+1].get("layout", "")
            if next_layout == "vocab":
                if slides[i].get("title") != "Let's learn some words":
                    errors.append(f"Slide {i+1} (segue) preceding vocabulary MUST have the title 'Let's learn some words'.")
            elif next_layout != "strategy":
                errors.append(f"Slide {i+1} (segue) MUST be followed by a 'strategy' slide for explicit instruction. Found: {next_layout}")
        
        # Prohibition of Strategy before Vocab
        if slides[i].get("layout") == "strategy" and i < len(slides) - 1:
            if slides[i+1].get("layout") == "vocab":
                errors.append(f"Slide {i+1} (strategy): BANNED strategy slide before vocabulary. Transition directly from segue to vocab.")

    # 3. No Teacher Jargon
    banned_words = ["Pre-teaching", "Lead-in", "Gist", "Controlled Practice", "Stage", "Feedback", "The Hook"]
    raw_json = json.dumps(data)
    for word in banned_words:
        if word.lower() in raw_json.lower():
            for slide in slides:
                for field in ["title", "badge", "content", "subtitle"]:
                    val = str(slide.get(field, ""))
                    if word.lower() in val.lower():
                        errors.append(f"Banned teacher jargon '{word}' found in slide '{slide.get('title')}' ({field} field).")

    # 4. Vocab Styling Mandates
    for slide in slides:
        if slide.get("layout") == "vocab":
            context = slide.get("context_sentence", "") or slide.get("example", "")
            if "<span style='color: #FFD700;'>" not in context and "<span style=\"color: #FFD700;\">" not in context:
                errors.append(f"Vocab slide '{slide.get('word')}' MUST use Gold (#FFD700) highlighting for the target word.")
            
            # No Paragraph Markers Check
            if re.search(r"\[Para \d+\]", context):
                errors.append(f"Vocab slide '{slide.get('word')}': BANNED paragraph marker found in context sentence. Remove markers like [Para 1].")

    # 5. Audio Integrity
    if "beep.mp3" in raw_json.lower():
        errors.append("BANNED audio file 'beep.mp3' found in JSON. Use 'blip.mp3' instead.")

    if errors:
        print("\n[X] GOLD STANDARD VIOLATIONS:")
        for err in errors:
            print(f"  - {err}")
        return False

    if warnings:
        print("\n[!] GOLD STANDARD WARNINGS:")
        for warn in warnings:
            print(f"  - {warn}")

    print("[OK] Gold Standard production check passed.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_gold_standard.py <presentation.json>")
        sys.exit(1)
    
    success = validate_gold_standard(json_path=sys.argv[1])
    sys.exit(0 if success else 1)
