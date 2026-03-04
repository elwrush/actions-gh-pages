"""
Create Slideshow for 'Preparing Your Talk'
Based on the validated outline and Bell EP template.
"""

import os
import sys
import time

PROJECT_ROOT = r"C:\PROJECTS\LESSONS AND SLIDESHOWS 2"
os.chdir(PROJECT_ROOT)

# Ensure skills scripts are in path
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'skills', 'designing-slides'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'skills', 'designing-slides', 'scripts'))

from scripts.authenticate_google import authenticate_slides, authenticate_drive
from scripts.add_slide_content import add_image_from_url, inches, _generate_id
from scripts.format_slides import SLIDE_WIDTH, SLIDE_HEIGHT
from googleapiclient.http import MediaFileUpload

# Bell Branding Colors
BRAND_COLORS = {
    'maroon': {'red': 166/255, 'green': 45/255, 'blue': 38/255},
    'white': {'red': 1.0, 'green': 1.0, 'blue': 1.0},
    'dark_gray': {'red': 0.2, 'green': 0.2, 'blue': 0.2},
    'light_maroon': {'red': 203/255, 'green': 92/255, 'blue': 85/255},
    'header_dark': {'red': 0.35, 'green': 0.05, 'blue': 0.05},
}

TARGET_FOLDER_ID = "1_n11w9BRN6sd0uaXlqEXjqZuZ74zFiOl" # General output folder
LOGO_DIR = os.path.join(PROJECT_ROOT, "images")

def upload_file(drive_service, file_path):
    """Upload a file to Drive and return its viewable URL."""
    file_name = os.path.basename(file_path)
    mime_type = 'image/png' if file_name.endswith('.png') else 'image/jpeg'
    
    media = MediaFileUpload(file_path, mimetype=mime_type)
    file = drive_service.files().create(body={'name': file_name}, media_body=media, fields='id').execute()
    file_id = file.get('id')
    
    # Make publicly viewable so Slides API can read it
    drive_service.permissions().create(fileId=file_id, body={'type': 'anyone', 'role': 'reader'}).execute()
    print(f"✅ Uploaded {file_name}")
    
    # Return web content link for API consumption
    return f"https://drive.google.com/uc?export=view&id={file_id}"

def upload_logo(drive_service, file_name):
    """Legacy wrapper for logos in images dir."""
    return upload_file(drive_service, os.path.join(LOGO_DIR, file_name))

def create_title_slide(slides_service, presentation_id, title, subtitle, bell_url, act_url):
    """Create title slide following Bell EP template structure."""
    slide_id = _generate_id()
    header_bar_id, strap_id, title_id, subtitle_id = _generate_id(), _generate_id(), _generate_id(), _generate_id()
    bell_img_id, act_img_id = _generate_id(), _generate_id()
    image_prompt_id = _generate_id()
    
    # Template dimensions
    header_height = inches(1.0)
    logo_height, logo_width = inches(0.7), inches(1.0)
    logo_y = (header_height - logo_height) / 2
    center_x = SLIDE_WIDTH / 2
    gap = inches(0.3)
    image_size = inches(2.5)
    image_x = (SLIDE_WIDTH - image_size) / 2
    
    all_requests = [
        # Create slide with gradient background
        {'createSlide': {'objectId': slide_id, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}},
        {'updatePageProperties': {'objectId': slide_id, 'pageProperties': {'pageBackgroundFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['light_maroon']}}}}, 'fields': 'pageBackgroundFill.solidFill.color'}},
        
        # Dark header bar
        {'createShape': {'objectId': header_bar_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': SLIDE_WIDTH, 'unit': 'EMU'}, 'height': {'magnitude': header_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 0, 'translateY': 0, 'unit': 'EMU'}}}},
        {'updateShapeProperties': {'objectId': header_bar_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['header_dark']}}}, 'outline': {'propertyState': 'NOT_RENDERED'}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        
        # Strap line: "Bell Language Centre"
        {'createShape': {'objectId': strap_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 'height': {'magnitude': inches(0.5), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 'translateY': inches(1.1), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': strap_id, 'text': 'Bell Language Centre'}},
        {'updateTextStyle': {'objectId': strap_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 18, 'unit': 'PT'}, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}},
        {'updateParagraphStyle': {'objectId': strap_id, 'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
        
        # Title
        {'createShape': {'objectId': title_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 'height': {'magnitude': inches(0.8), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 'translateY': inches(1.7), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': title_id, 'text': title}},
        {'updateTextStyle': {'objectId': title_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 36, 'unit': 'PT'}, 'bold': True, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,bold,fontFamily'}},
        {'updateParagraphStyle': {'objectId': title_id, 'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
        
        # Subtitle
        {'createShape': {'objectId': subtitle_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 'height': {'magnitude': inches(0.6), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 'translateY': inches(5.2), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': subtitle_id, 'text': subtitle}},
        {'updateTextStyle': {'objectId': subtitle_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 20, 'unit': 'PT'}, 'italic': True, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,italic,fontFamily'}},
        {'updateParagraphStyle': {'objectId': subtitle_id, 'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},

        # Image prompt box
        {'createShape': {'objectId': image_prompt_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': image_size, 'unit': 'EMU'}, 'height': {'magnitude': image_size, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': image_x, 'translateY': inches(2.6), 'unit': 'EMU'}}}},
        {'updateShapeProperties': {'objectId': image_prompt_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': {'red': 0.9, 'green': 0.9, 'blue': 0.9}}}}, 'outline': {'outlineFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['maroon']}}}, 'weight': {'magnitude': 2, 'unit': 'PT'}}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        {'insertText': {'objectId': image_prompt_id, 'text': "📸 [Speaker Image]"}},
        {'updateParagraphStyle': {'objectId': image_prompt_id, 'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
        
        # Logos in header
        {'createImage': {'objectId': bell_img_id, 'url': bell_url, 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': logo_width, 'unit': 'EMU'}, 'height': {'magnitude': logo_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': center_x - logo_width - gap/2, 'translateY': logo_y, 'unit': 'EMU'}}}},
        {'createImage': {'objectId': act_img_id, 'url': act_url, 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': logo_width, 'unit': 'EMU'}, 'height': {'magnitude': logo_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': center_x + gap/2, 'translateY': logo_y, 'unit': 'EMU'}}}}
    ]
    
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': all_requests}).execute()
    print("✅ Created title slide")
    return slide_id

def create_content_slide(slides_service, presentation_id, title, body, variant="standard", image_prompt=None, image_url=None):
    slide_id = _generate_id()
    header_id, title_id, body_id = _generate_id(), _generate_id(), _generate_id()
    
    # Colors based on variant
    header_color = BRAND_COLORS['maroon']
    body_color = BRAND_COLORS['dark_gray']
    
    if variant == "transition":
        header_color = BRAND_COLORS['header_dark']
    elif variant == "answer":
        header_color = {'red': 0.1, 'green': 0.5, 'blue': 0.3} # Green for answers
    
    all_requests = [
        {'createSlide': {'objectId': slide_id, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}},
        {'createShape': {'objectId': header_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': SLIDE_WIDTH, 'unit': 'EMU'}, 'height': {'magnitude': inches(0.8), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 0, 'translateY': 0, 'unit': 'EMU'}}}},
        {'createShape': {'objectId': title_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 'height': {'magnitude': inches(0.7), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.3), 'translateY': inches(0.05), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': title_id, 'text': title}},
        {'createShape': {'objectId': body_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 'height': {'magnitude': inches(4.0), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.5), 'translateY': inches(1.1), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': body_id, 'text': body}},
        
        # Styles
        {'updateShapeProperties': {'objectId': header_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': header_color}}}, 'outline': {'propertyState': 'NOT_RENDERED'}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        {'updateTextStyle': {'objectId': title_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 30, 'unit': 'PT'}, 'bold': True, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,bold,fontFamily'}},
        {'updateTextStyle': {'objectId': body_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': body_color}}, 'fontSize': {'magnitude': 24, 'unit': 'PT'}, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}},
        {'updateParagraphStyle': {'objectId': body_id, 'style': {'alignment': 'START'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}}
    ]
    
    if image_url:
        img_id = _generate_id()
        all_requests.append({
            'createImage': {
                'objectId': img_id,
                'url': image_url,
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 'height': {'magnitude': inches(3), 'unit': 'EMU'}},
                    'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 'translateY': inches(4.0), 'unit': 'EMU'}
                }
            }
        })
    elif image_prompt:
        prompt_id = _generate_id()
        all_requests.extend([
            {'createShape': {'objectId': prompt_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 'height': {'magnitude': inches(0.6), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.5), 'translateY': inches(4.6), 'unit': 'EMU'}}}},
            {'insertText': {'objectId': prompt_id, 'text': f"🖼️ [IMAGE: {image_prompt}]"}},
            {'updateShapeProperties': {'objectId': prompt_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['light_maroon']}, 'alpha': 0.2}}, 'outline': {'propertyState': 'NOT_RENDERED'}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
            {'updateTextStyle': {'objectId': prompt_id, 'style': {'fontSize': {'magnitude': 12, 'unit': 'PT'}, 'italic': True, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'fontSize,italic,fontFamily'}}
        ])

    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': all_requests}).execute()
    print(f"✅ Created slide: {title}")
    return slide_id

def main():
    print("🚀 Creating 'Preparing Your Talk' Slideshow...")
    slides_service = authenticate_slides()
    drive_service = authenticate_drive()
    
    # Upload logos and images
    bell_url = upload_logo(drive_service, "Bell.png")
    act_url = upload_logo(drive_service, "ACT.png")
    
    # Upload the eye contact diagram
    diagram_path =os.path.join(PROJECT_ROOT, "inputs", "02-Preparing-Your-Talk", "eye_contact_triangle.png")
    diagram_url = upload_file(drive_service, diagram_path)
    
    time.sleep(1)
    
    # Create presentation
    presentation = slides_service.presentations().create(body={'title': '06-01-26-Preparing-Your-Talk-Slides-v2'}).execute()
    presentation_id = presentation.get('presentationId')
    
    # Delete default first slide
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': [{'deleteObject': {'objectId': presentation.get('slides')[0]['objectId']}}]}).execute()
    
    # 1. Title Slide
    create_title_slide(slides_service, presentation_id, "Preparing Your Talk", "Pronunciation, Delivery & Mental Preparation", bell_url, act_url)
    
    # 2. Transition
    create_content_slide(slides_service, presentation_id, "The Problem", "From Nerves to Confidence", variant="transition")
    
    # 3. What Scares You?
    create_content_slide(slides_service, presentation_id, "What Scares You?", 
                         "What makes you nervous about speaking?\n\n🔊 SOUND: Pronunciation, voice too quiet\n👀 SIGHT: Eye contact, looking at floor\n🧠 MIND: Forgetting words, saying 'umm'")
    
    # 4. Transition
    create_content_slide(slides_service, presentation_id, "Hero Tool #1", "The Sound of English", variant="transition")
    
    # 5. Linking
    create_content_slide(slides_service, presentation_id, "Linking Sounds (Connection)",
                         "Thai: Words are separate (First. Of. All.)\n\nEnglish: Words connect like a chain 🔗\n• FIR-stuh-VALL\n• Don't stop breathing between words!")
    
    # 6. Practice
    create_content_slide(slides_service, presentation_id, "Practice: Linking",
                         "Say it smoothly:\n\n1. First of all\n2. I'd like to\n3. Look at this\n4. Let me explain\n\n(Say it like ONE long word!)")
    
    # 7. Answer
    create_content_slide(slides_service, presentation_id, "Answer: The Flow",
                         "1. First of all → FIR-stuh-VALL\n2. I'd like to → I'd-LIKE-tuh\n3. Look at this → LOO-kuh-THIS\n4. Let me explain → LET-mee-ex-PLAIN", variant="answer")
    
    # 8. Stress
    create_content_slide(slides_service, presentation_id, "Syllable Stress (Rhythm)",
                         "Thai: Even stress (___ ___ ___)\nEnglish: ONE loud syllable (_ ___ _)\n\n❌ TRAP: Don't stress the END (imporTANT)\n✅ FIX: Stress the MIDDLE (im-POR-tant)")
    
    # 9. Practice
    create_content_slide(slides_service, presentation_id, "Practice: Fix the Stress",
                         "Where is the stress?\n\n• impor-tant\n• in-ter-est-ing\n• comf-ter-ble\n• pre-sent (verb) vs pre-sent (noun)")
    
    # 10. Answer
    create_content_slide(slides_service, presentation_id, "Answer: The Rhythm",
                         "• im-POR-tant\n• IN-ter-est-ing\n• COMF-ter-ble (3 syllables)\n• pre-SENT (Action) vs PRE-sent (Gift/Now)", variant="answer")
    
    # 11. Transition
    create_content_slide(slides_service, presentation_id, "Hero Tool #2", "Delivery Skills", variant="transition")
    
    # 12. Voice
    create_content_slide(slides_service, presentation_id, "Voice Projection",
                         "Don't speak to the front row.\n\n🧱 Throw your voice to the BACK WALL.\nImagine your voice is a ball. Make it bounce!\n\nPractice: \"Good morning everyone. Today I'm going to talk about...\"",
                         image_prompt="Ball bouncing off a wall to represent voice")
    
    # 13. Eye Contact (WITH ACTUAL IMAGE)
    create_content_slide(slides_service, presentation_id, "Eye Contact: The Triangle",
                         "Don't stare at the floor or ceiling.\n\nUse the 3-Point Triangle:\nLeft (3 sec) ➡️ Center (3 sec) ➡️ Right (3 sec)\n\nKeep moving smoothly.",
                         image_url=diagram_url)
    
    # 14. Transition
    create_content_slide(slides_service, presentation_id, "Hero Tool #3", "The Mind", variant="transition")
    
    # 15. Umm
    create_content_slide(slides_service, presentation_id, "Why do we say 'Umm'?",
                         "Problem: We say 'Umm' when we don't know what comes next.\n\nSolution: The Mental Cinema 🎬\n\nSee your talk as a movie in your head.")
    
    # 16. Scenes
    create_content_slide(slides_service, presentation_id, "The 3 Scenes",
                         "Visualize the scenes, not the words:\n\n1. 🎬 HOOK (Grab attention)\n2. 📖 BODY (Your main points)\n3. 🎯 CLOSING (Summary + Impact)")
    
    # 17. Transition
    create_content_slide(slides_service, presentation_id, "Your Turn", "Partner Practice", variant="transition")
    
    # 18. Mission
    create_content_slide(slides_service, presentation_id, "The Mission",
                         "Stand up!\nOnly speak for 60-90 seconds (Hook + Point 1).\n\nUse all 3 Tools:\n1. Link your sounds\n2. Throw your voice + Triangle eyes\n3. See your scenes\n\nPartner will give feedback!")
    
    # 19. Reflection
    create_content_slide(slides_service, presentation_id, "Reflection",
                         "• What felt easier?\n• Which tool helped the most?\n\nNext lesson: The Real Talk (2-3 minutes)")
                         
    # Move to folder
    drive_service.files().update(fileId=presentation_id, addParents=TARGET_FOLDER_ID, removeParents='root').execute()
    
    print(f"\n✅ Slideshow created: https://docs.google.com/presentation/d/{presentation_id}/edit")

if __name__ == '__main__':
    main()
