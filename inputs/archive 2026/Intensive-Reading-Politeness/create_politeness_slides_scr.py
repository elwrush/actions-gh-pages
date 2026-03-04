"""
Generate slideshow for "What does polite mean to you?" lesson
Shape H SCR (Situation-Complication-Resolution) narrative
Based on working presentation structure pattern
"""

import os
import sys

PROJECT_ROOT = r"C:\PROJECTS\LESSONS AND SLIDESHOWS 2"
os.chdir(PROJECT_ROOT)

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'skills', 'designing-slides'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'skills', 'designing-slides', 'scripts'))

from scripts.authenticate_google import authenticate_slides
from scripts.add_slide_content import inches, _generate_id
from scripts.format_slides import SLIDE_WIDTH, SLIDE_HEIGHT

BRAND_COLORS = {
    'maroon': {'red': 166/255, 'green': 45/255, 'blue': 38/255},
    'white': {'red': 1.0, 'green': 1.0, 'blue': 1.0},
    'dark_gray': {'red': 0.2, 'green': 0.2, 'blue': 0.2},
    'light_maroon': {'red': 203/255, 'green': 92/255, 'blue': 85/255},
}

def create_simple_slide(title, bullets, bg_maroon=False):
    """Return requests for a simple content slide"""
    slide_id = _generate_id()
    header_id, title_id, body_id = _generate_id(), _generate_id(), _generate_id()
    
    if bg_maroon:
        bg_color = BRAND_COLORS['light_maroon']
        text_color = BRAND_COLORS['white']
    else:
        bg_color = BRAND_COLORS['white']
        text_color = BRAND_COLORS['dark_gray']
    
    bullet_text = '\\n'.join(bullets)
    
    requests = [
        {'createSlide': {'objectId': slide_id, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}},
        # Background
        {'updatePageProperties': {'objectId': slide_id, 'pageProperties': {'pageBackgroundFill': {'solidFill': {'color': {'rgbColor': bg_color}}}}, 'fields': 'pageBackgroundFill'}},
        # Header bar
        {'createShape': {'objectId': header_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': SLIDE_WIDTH, 'unit': 'EMU'}, 'height': {'magnitude': inches(0.8), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 0, 'translateY': 0, 'unit': 'EMU'}}}},
        {'updateShapeProperties': {'objectId': header_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['maroon']}}}, 'outline': {'propertyState': 'NOT_RENDERED'}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        # Title
        {'createShape': {'objectId': title_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 'height': {'magnitude': inches(0.7), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.3), 'translateY': inches(0.05), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': title_id, 'text': title}},
        {'updateTextStyle': {'objectId': title_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 30, 'unit': 'PT'}, 'bold': True, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,bold,fontFamily'}},
        # Body
        {'createShape': {'objectId': body_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 'height': {'magnitude': inches(5.5), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.5), 'translateY': inches(1.2), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': body_id, 'text': bullet_text}},
        {'updateTextStyle': {'objectId': body_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': text_color}}, 'fontSize': {'magnitude': 24, 'unit': 'PT'}, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}},
        {'createParagraphBullets': {'objectId': body_id, 'textRange': {'type': 'ALL'}, 'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE'}}
    ]
    
    return requests

def create_vocab_slide(word, phonemic, thai, eng_sent, thai_sent):
    """Return requests for vocabulary slide"""
    slide_id = _generate_id()
    content_id = _generate_id()
    
    text = f"{word} /{phonemic}/: {thai}\\n\\n{eng_sent}\\n\\n{thai_sent}"
    
    requests = [
        {'createSlide': {'objectId': slide_id, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}},
        {'createShape': {'objectId': content_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 'height': {'magnitude': inches(6.5), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.5), 'translateY': inches(0.5), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': content_id, 'text': text}},
        {'updateTextStyle': {'objectId': content_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['dark_gray']}}, 'fontSize': {'magnitude': 26, 'unit': 'PT'}, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}},
        {'updateParagraphStyle': {'objectId': content_id, 'style': {'alignment': 'CENTER', 'lineSpacing': 150}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment,lineSpacing'}}
    ]
    
    return requests

def main():
    print("🔑 Authenticating...")
    slides_service = authenticate_slides()
    
    print("📊 Creating presentation...")
    presentation = slides_service.presentations().create(body={'title': '30-12-25-Politeness-Reading-B1-SCR'}).execute()
    presentation_id = presentation['presentationId']
    
    # Delete default slide
    default_slide_id = presentation['slides'][0]['objectId']
    all_requests = [{'deleteObject': {'objectId': default_slide_id}}]
    
    print("📝 Building 23 slides...")
    
    # Slide 1: Title (simple version - logos added manually)
    all_requests.extend(create_simple_slide(
        'What does polite mean to you?',
        ['B1 Reading Lesson', 'Shape H: SCR Framework', 'Teacher: Ed Rush'],
        bg_maroon=True
    ))
    
    # SITUATION ARC
    # Slide 2: Entry Ticket
    all_requests.extend(create_simple_slide(
        'Entry Ticket: Tools of the Trade',
        ['Match the tools to the people', '5 tools, 5 people (only 3 matches!)', '2 minutes - work individually']
    ))
    
    # Slide 3: ANSWER
    all_requests.extend(create_simple_slide(
        'Entry Ticket Answers',
        ['1. scalpel → A (Anna - surgeon) ✓', '2. whisk → No match (distractor)', '3. tripod → E (Eric - photographer) ✓', '4. guitar → No match (distractor)', '5. saw → B (Ben - carpenter) ✓'],
        bg_maroon=True
    ))
    
    # Slide 4: Brainstorm Frame
    all_requests.extend(create_simple_slide(
        'Your Rulebook',
        ['Just like every profession has TOOLS...', 'Every culture has RULES for politeness', 'Question: What makes someone polite?', 'Give me 3 examples']
    ))
    
    # Slides 5-7: Vocabulary
    all_requests.extend(create_vocab_slide(
        'offend', 'əˈfend', 'ทำให้ขุ่นเคือง',
        'If you tip in Japan, you might offend the waiter.',
        'ถ้าคุณให้ทิปในญี่ปุ่น คุณอาจทำให้พนักงานเสิร์ฟขุ่นเคือง'
    ))
    
    all_requests.extend(create_vocab_slide(
        'acceptable', 'əkˈseptəbl', 'ยอมรับได้',
        'Using your phone during class is not acceptable.',
        'การใช้โทรศัพท์ในระหว่างเรียนไม่ยอมรับได้'
    ))
    
    all_requests.extend(create_vocab_slide(
        'behavior', 'bɪˈheɪvjər', 'พฤติกรรม',
        'Teachers should model good behavior.',
        'ครูควรเป็นแบบอย่างของพฤติกรรมที่ดี'
    ))
    
    # Slide 8: Create Tension
    all_requests.extend(create_simple_slide(
        'Before You Read',
        ['Look at Section B on your worksheet', 'Rate these 4 behaviors: How rude are they?', "10 = Very rude, 1 = It's fine", 'You have 2 minutes', "Don't discuss yet!"]
    ))
    
    # Slide 9: Brainstorm
    all_requests.extend(create_simple_slide(
        'What Did You Circle?',
        ['Speaking on phone on BTS?', 'Interrupting someone?', 'Using left hand to greet?', 'Sending emails during meeting?', "You have your answers. Now let's see if the WORLD agrees..."]
    ))
    
    # Slide 10: Transition
    all_requests.extend(create_simple_slide(
        'The Question',
        ['These are YOUR rules', 'This is YOUR rulebook', 'But does your rulebook work EVERYWHERE?', "Let's find out..."],
        bg_maroon=True
    ))
    
    # COMPLICATION ARC
    # Slide 11: Breakdown
    all_requests.extend(create_simple_slide(
        "Your Rulebook Doesn't Work Everywhere",
        ["Imagine you're a DETECTIVE", 'Your job: Find where YOUR politeness rules FAIL', "What's polite here becomes RUDE there", "Let's investigate..."]
    ))
    
    # Slide 12: Scanning
    all_requests.extend(create_simple_slide(
        'Detective Work: Scan the Text',
        ['Scan paragraphs 2-4', 'Find 3 examples where polite → rude', 'Write them down', '4 minutes, then pair check']
    ))
    
    # Slide 13: Pattern Recognition
    all_requests.extend(create_simple_slide(
        'Topic Sentences = Headlines',
        ['Topic sentences are like HEADLINES', 'They show the main idea without every word', 'Task: Underline the topic sentence in paragraphs 2-4', '2 minutes - work individually']
    ))
    
    # Slide 14: Global Reading Task
    all_requests.extend(create_simple_slide(
        'Global Reading',
        ['Match the main ideas to paragraphs:', 'A. People use different phrases for politeness', 'B. Technology changed what is polite', 'C. Politeness varies across cultures', 'Which goes with para 2? 3? 4?']
    ))
    
    # Slide 15: ANSWER
    all_requests.extend(create_simple_slide(
        'Global Reading Answers',
        ['A. Different phrases → Paragraph 2', 'B. Technology changed → Paragraph 4', 'C. Varies across cultures → Paragraph 3', 'Each shows a DIFFERENT reason politeness changes!', '(Language, culture, technology)'],
        bg_maroon=True
    ))
    
    # Slide 16: Close Reading Frame
    all_requests.extend(create_simple_slide(
        'Zoom In: Close Reading',
        ["Now we're going DEEPER", 'Like zooming into a photo → we need DETAILS', 'Task: Fill in the gaps with info from text', 'Scan for specific words and phrases']
    ))
    
    # Slide 17: Close Reading Task
    all_requests.extend(create_simple_slide(
        'Section D: Fill the Gaps',
        ['Complete the paragraph on your worksheet:', '1. Older people say "___"', '2. Younger people say "___"', '3. In USA, ___ is polite', '4. In India, using your ___ is rude', '5. Having your ___ at dinner is rude', "6. ___ think it's very rude"]
    ))
    
    # Slide 18: ANSWER
    all_requests.extend(create_simple_slide(
        'Close Reading Answers',
        ['1. "You\'re welcome"', '2. "No problem"', '3. tipping', '4. left hand', '5. phone / cell phone', '6. older people', 'What do ALL these have in common? → Politeness CHANGES!'],
        bg_maroon=True
    ))
    
    # RESOLUTION ARC
    # Slide 19: The Insight
    all_requests.extend(create_simple_slide(
        'Politeness is a COMPASS, Not a Map',
        ['Your rulebook = MAP (works in Thailand only)', 'In Japan/USA? The map is WRONG', 'What you need = COMPASS', 'Formula: Politeness = Context (Age + Location + Technology)', 'Example: เกรงใจ in Thailand vs directness in USA'],
        bg_maroon=True
    ))
    
    # Slide 20: Critical Thinking
    all_requests.extend(create_simple_slide(
        'Critical Thinking',
        ['1. What behavior do YOU find rude?', 'Do others find YOUR behavior rude?', '', '2. Are younger people less polite than older?', 'Why / why not?', '', 'Discuss in pairs - 4 minutes']
    ))
    
    # Slide 21: Exit Reflection
    all_requests.extend(create_simple_slide(
        'Exit Reflection',
        ['BEFORE: What did "polite" mean?', "(Universal rules: say thank you, don't interrupt)", '', 'NOW: What do you know?', '(Depends on culture, age, technology)', '', 'Politeness = Reading the CONTEXT']
    ))
    
    # Slide 22: Final Metaphor
    all_requests.extend(create_simple_slide(
        'Be Like Water',
        ['"Be like water, my friend"', '', 'Water ADAPTS to the cup', 'Politeness ADAPTS to the culture', '', 'Check: Where? Who? What generation?'],
        bg_maroon=True
    ))
    
    # Slide 23: Closing
    all_requests.extend(create_simple_slide(
        'Thank You!',
        ['Remember: Your compass, not your map', '', 'Questions?']
    ))
    
    # EXECUTE BATCH
    print(f"🚀 Executing batch ({len(all_requests)} requests)...")
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': all_requests}
    ).execute()
    
    url = f"https://docs.google.com/presentation/d/{presentation_id}/edit"
    print(f"\n✅ SUCCESS!")
    print(f"📊 URL: {url}")
    print(f"📝 Total slides: 23")
    print(f"🎨 Answers interleaved with tasks (slides 3, 15, 18)")
    
    return presentation_id, url

if __name__ == '__main__':
    main()
