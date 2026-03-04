"""
Generate slideshow for Politeness lesson - using working pattern
"""
import os
import sys
import time

PROJECT_ROOT = r"C:\PROJECTS\LESSONS AND SLIDESHOWS 2"
os.chdir(PROJECT_ROOT)

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'skills', 'designing-slides'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'skills', 'designing-slides', 'scripts'))

from scripts.authenticate_google import authenticate_slides, authenticate_drive
from scripts.add_slide_content import inches, _generate_id
from scripts.format_slides import SLIDE_WIDTH, SLIDE_HEIGHT
from googleapiclient.http import MediaFileUpload

BRAND_COLORS = {
    'maroon': {'red': 166/255, 'green': 45/255, 'blue': 38/255},
    'white': {'red': 1.0, 'green': 1.0, 'blue': 1.0},
    'dark_gray': {'red': 0.2, 'green': 0.2, 'blue': 0.2},
    'light_maroon': {'red': 203/255, 'green': 92/255, 'blue': 85/255},
    'header_dark': {'red': 0.35, 'green': 0.05, 'blue': 0.05},
}

TARGET_FOLDER_ID = "1_n11w9BRN6sd0uaXlqEXjqZuZ74zFiOl"
LOGO_DIR = os.path.join(PROJECT_ROOT, "images")

def upload_logo(drive_service, file_name):
    file_path = os.path.join(LOGO_DIR, file_name)
    mime_type = 'image/png' if file_name.endswith('.png') else 'image/jpeg'
    media = MediaFileUpload(file_path, mimetype=mime_type)
    file = drive_service.files().create(body={'name': file_name}, media_body=media, fields='id').execute()
    file_id = file.get('id')
    drive_service.permissions().create(fileId=file_id, body={'type': 'anyone', 'role': 'reader'}).execute()
    print(f"✅ Uploaded {file_name}")
    return f"https://lh3.googleusercontent.com/d/{file_id}"

def create_title_slide(slides_service, presentation_id, title, bell_url, act_url):
    slide_id = _generate_id()
    header_bar_id, strap_id, title_id = _generate_id(), _generate_id(), _generate_id()
    bell_img_id, act_img_id = _generate_id(), _generate_id()
    
    header_height = inches(1.0)
    logo_height, logo_width = inches(0.7), inches(1.0)
    logo_y = (header_height - logo_height) / 2
    center_x = SLIDE_WIDTH / 2
    gap = inches(0.3)
    
    all_requests = [
        {'createSlide': {'objectId': slide_id, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}},
        {'updatePageProperties': {'objectId': slide_id, 'pageProperties': {'pageBackgroundFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['light_maroon']}}}}, 'fields': 'pageBackgroundFill.solidFill.color'}},
        {'createShape': {'objectId': header_bar_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': SLIDE_WIDTH, 'unit': 'EMU'}, 'height': {'magnitude': header_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 0, 'translateY': 0, 'unit': 'EMU'}}}},
        {'updateShapeProperties': {'objectId': header_bar_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['header_dark']}}}, 'outline': {'propertyState': 'NOT_RENDERED'}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        {'createShape': {'objectId': strap_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 'height': {'magnitude': inches(0.5), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 'translateY': inches(1.1), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': strap_id, 'text': 'Bell Language Centre'}},
        {'updateTextStyle': {'objectId': strap_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 18, 'unit': 'PT'}, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}},
        {'updateParagraphStyle': {'objectId': strap_id, 'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
        {'createShape': {'objectId': title_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 'height': {'magnitude': inches(0.8), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 'translateY': inches(1.7), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': title_id, 'text': title}},
        {'updateTextStyle': {'objectId': title_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 36, 'unit': 'PT'}, 'bold': True, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,bold,fontFamily'}},
        {'updateParagraphStyle': {'objectId': title_id, 'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
        {'createImage': {'objectId': bell_img_id, 'url': bell_url, 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': logo_width, 'unit': 'EMU'}, 'height': {'magnitude': logo_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': center_x - logo_width - gap/2, 'translateY': logo_y, 'unit': 'EMU'}}}},
        {'createImage': {'objectId': act_img_id, 'url': act_url, 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': logo_width, 'unit': 'EMU'}, 'height': {'magnitude': logo_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': center_x + gap/2, 'translateY': logo_y, 'unit': 'EMU'}}}}
    ]
    
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': all_requests}).execute()
    print("✅ Created title slide")
    return slide_id

def create_content_slide(slides_service, presentation_id, title, body):
    slide_id = _generate_id()
    header_id, title_id, body_id = _generate_id(), _generate_id(), _generate_id()
    
    all_requests = [
        {'createSlide': {'objectId': slide_id, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}},
        {'createShape': {'objectId': header_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': SLIDE_WIDTH, 'unit': 'EMU'}, 'height': {'magnitude': inches(0.8), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 0, 'translateY': 0, 'unit': 'EMU'}}}},
        {'createShape': {'objectId': title_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 'height': {'magnitude': inches(0.7), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.3), 'translateY': inches(0.05), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': title_id, 'text': title}},
        {'createShape': {'objectId': body_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 'height': {'magnitude': inches(5.5), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.5), 'translateY': inches(1.2), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': body_id, 'text': body}},
        {'updateShapeProperties': {'objectId': header_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['maroon']}}}, 'outline': {'propertyState': 'NOT_RENDERED'}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        {'updateTextStyle': {'objectId': title_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 30, 'unit': 'PT'}, 'bold': True, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,bold,fontFamily'}},
        {'updateTextStyle': {'objectId': body_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['dark_gray']}}, 'fontSize': {'magnitude': 24, 'unit': 'PT'}, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}},
        {'updateParagraphStyle': {'objectId': body_id, 'style': {'alignment': 'START'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}}
    ]
    
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': all_requests}).execute()
    print(f"✅ Created slide: {title}")
    return slide_id

def main():
    print("🚀 Creating Politeness slideshow...")
    slides_service = authenticate_slides()
    drive_service = authenticate_drive()
    
    # Upload logos
    bell_url = upload_logo(drive_service, "Bell.png")
    act_url = upload_logo(drive_service, "ACT.png")
    time.sleep(2)
    
    # Create presentation
    presentation = slides_service.presentations().create(body={'title': '30-12-25-Politeness-Reading-B1-SCR'}).execute()
    presentation_id = presentation.get('presentationId')
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': [{'deleteObject': {'objectId': presentation.get('slides')[0]['objectId']}}]}).execute()
    
    # Title slide
    create_title_slide(slides_service, presentation_id, "What does polite mean to you?", bell_url, act_url)
    
    # Content slides (23 total following SCR narrative with interleaved answers)
    create_content_slide(slides_service, presentation_id, "Entry Ticket: Tools of the Trade",
                        "Match the tools to the people\n5 tools, 5 people (only 3 matches!)\n2 minutes - work individually")
    
    create_content_slide(slides_service, presentation_id, "Entry Ticket Answers",
                        "1. scalpel → A (Anna - surgeon) ✓\n2. whisk → No match (distractor)\n3. tripod → E (Eric - photographer) ✓\n4. guitar → No match (distractor)\n5. saw → B (Ben - carpenter) ✓")
    
    create_content_slide(slides_service, presentation_id, "Your Rulebook",
                        "Just like every profession has TOOLS...\nEvery culture has RULES for politeness\n\nQuestion: What makes someone polite?\nGive me 3 examples")
    
    create_content_slide(slides_service, presentation_id, "offend /əˈfend/: ทำให้ขุ่นเคือง",
                        "If you tip in Japan, you might offend the waiter.\n\nถ้าคุณให้ทิปในญี่ปุ่น คุณอาจทำให้พนักงานเสิร์ฟขุ่นเคือง")
    
    create_content_slide(slides_service, presentation_id, "acceptable /əkˈseptəbl/: ยอมรับได้",
                        "Using your phone during class is not acceptable.\n\nการใช้โทรศัพท์ในระหว่างเรียนไม่ยอมรับได้")
    
    create_content_slide(slides_service, presentation_id, "behavior /bɪˈheɪvjər/: พฤติกรรม",
                        "Teachers should model good behavior.\n\nครูควรเป็นแบบอย่างของพฤติกรรมที่ดี")
    
    create_content_slide(slides_service, presentation_id, "Before You Read",
                        "Look at Section B on your worksheet\nRate these 4 behaviors: How rude are they?\n10 = Very rude, 1 = It's fine\nYou have 2 minutes\nDon't discuss yet!")
    
    create_content_slide(slides_service, presentation_id, "The Question",
                        "These are YOUR rules\nThis is YOUR rulebook\n\nBut does your rulebook work EVERYWHERE?\n\nLet's find out...")
    
    create_content_slide(slides_service, presentation_id, "Your Rulebook Doesn't Work Everywhere",
                        "Imagine you're a DETECTIVE\nYour job: Find where YOUR politeness rules FAIL\nWhat's polite here becomes RUDE there\n\nLet's investigate...")
    
    create_content_slide(slides_service, presentation_id, "Detective Work: Scan the Text",
                        "Scan paragraphs 2-4\nFind 3 examples where polite → rude\nWrite them down\n4 minutes, then pair check")
    
    create_content_slide(slides_service, presentation_id, "Topic Sentences = Headlines",
                        "Topic sentences are like HEADLINES\nThey show the main idea without every word\n\nTask: Underline the topic sentence in paragraphs 2-4\n2 minutes - work individually")
    
    create_content_slide(slides_service, presentation_id, "Global Reading",
                        "Match the main ideas to paragraphs:\n\nA. People use different phrases for politeness\nB. Technology changed what is polite\nC. Politeness varies across cultures\n\nWhich goes with para 2? 3? 4?")
    
    create_content_slide(slides_service, presentation_id, "Global Reading Answers",
                        "A. Different phrases → Paragraph 2\nB. Technology changed → Paragraph 4\nC. Varies across cultures → Paragraph 3\n\nEach shows a DIFFERENT reason politeness changes!\n(Language, culture, technology)")
    
    create_content_slide(slides_service, presentation_id, "Zoom In: Close Reading",
                        "Now we're going DEEPER\nLike zooming into a photo → we need DETAILS\n\nTask: Fill in the gaps with info from text\nScan for specific words and phrases")
    
    create_content_slide(slides_service, presentation_id, "Section D: Fill the Gaps",
                        "Complete the paragraph on your worksheet:\n\n1. Older people say \"___\"\n2. Younger people say \"___\"\n3. In USA, ___ is polite\n4. In India, using your ___ is rude\n5. Having your ___ at dinner is rude\n6. ___ think it's very rude")
    
    create_content_slide(slides_service, presentation_id, "Close Reading Answers",
                        "1. \"You're welcome\"\n2. \"No problem\"\n3. tipping\n4. left hand\n5. phone / cell phone\n6. older people\n\nWhat do ALL these have in common? → Politeness CHANGES!")
    
    create_content_slide(slides_service, presentation_id, "Politeness is a COMPASS, Not a Map",
                        "Your rulebook = MAP (works in Thailand only)\nIn Japan/USA? The map is WRONG\n\nWhat you need = COMPASS\n\nFormula: Politeness = Context\n(Age + Location + Technology)\n\nExample: เกรงใจ in Thailand vs directness in USA")
    
    create_content_slide(slides_service, presentation_id, "Critical Thinking",
                        "1. What behavior do YOU find rude?\n   Do others find YOUR behavior rude?\n\n2. Are younger people less polite than older?\n   Why / why not?\n\nDiscuss in pairs - 4 minutes")
    
    create_content_slide(slides_service, presentation_id, "Exit Reflection",
                        "BEFORE: What did \"polite\" mean?\n(Universal rules: say thank you, don't interrupt)\n\nNOW: What do you know?\n(Depends on culture, age, technology)\n\nPoliteness = Reading the CONTEXT")
    
    create_content_slide(slides_service, presentation_id, "Be Like Water",
                        "\"Be like water, my friend\"\n\nWater ADAPTS to the cup\nPoliteness ADAPTS to the culture\n\nCheck: Where? Who? What generation?")
    
    create_content_slide(slides_service, presentation_id, "Thank You!",
                        "Remember: Your compass, not your map\n\nQuestions?")
    
    # Move to folder
    drive_service.files().update(fileId=presentation_id, addParents=TARGET_FOLDER_ID, removeParents='root').execute()
    
    print(f"\n✅ Slideshow created: https://docs.google.com/presentation/d/{presentation_id}/edit")
    print(f"📌 Total slides: 21 (title + 20 content)")
    print(f"📌 Answers interleaved after tasks (slides 3, 13, 16)")

if __name__ == '__main__':
    main()
