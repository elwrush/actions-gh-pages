"""
Create Pronunciation Soundcheck Slideshow
Based on working example: 01-Presentation-Structure/create_presentation_structure_slides.py
"""

import os
import sys
import time

PROJECT_ROOT = r"C:\PROJECTS\LESSONS AND SLIDESHOWS 2"
os.chdir(PROJECT_ROOT)

# Fix imports
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'skills', 'designing-slides'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'skills', 'designing-slides', 'scripts'))

from scripts.authenticate_google import authenticate_slides, authenticate_drive
from scripts.add_slide_content import inches, _generate_id
from scripts.format_slides import SLIDE_WIDTH, SLIDE_HEIGHT
from googleapiclient.http import MediaFileUpload

# Branding Colors
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

def create_title_slide(slides_service, presentation_id, title, subtitle, bell_url, act_url):
    """Create title slide following Bell EP template structure."""
    slide_id = _generate_id()
    header_bar_id, strap_id, title_id = _generate_id(), _generate_id(), _generate_id()
    bell_img_id, act_img_id = _generate_id(), _generate_id()
    image_prompt_id = _generate_id()
    
    header_height = inches(1.0)
    logo_height, logo_width = inches(0.7), inches(1.0)
    logo_y = (header_height - logo_height) / 2
    center_x = SLIDE_WIDTH / 2
    gap = inches(0.3)
    image_size = inches(2.5)
    image_x = (SLIDE_WIDTH - image_size) / 2
    
    all_requests = [
        {'createSlide': {'objectId': slide_id, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}},
        {'updatePageProperties': {'objectId': slide_id, 'pageProperties': {'pageBackgroundFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['light_maroon']}}}}, 'fields': 'pageBackgroundFill.solidFill.color'}},
        
        # Dark header bar
        {'createShape': {'objectId': header_bar_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': SLIDE_WIDTH, 'unit': 'EMU'}, 'height': {'magnitude': header_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 0, 'translateY': 0, 'unit': 'EMU'}}}},
        {'updateShapeProperties': {'objectId': header_bar_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['header_dark']}}}, 'outline': {'propertyState': 'NOT_RENDERED'}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        
        # Strap line
        {'createShape': {'objectId': strap_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 'height': {'magnitude': inches(0.5), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 'translateY': inches(1.1), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': strap_id, 'text': 'Bell Language Centre | ' + subtitle}},
        {'updateTextStyle': {'objectId': strap_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 18, 'unit': 'PT'}, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}},
        {'updateParagraphStyle': {'objectId': strap_id, 'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
        
        # Title
        {'createShape': {'objectId': title_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 'height': {'magnitude': inches(0.8), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 'translateY': inches(1.7), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': title_id, 'text': title}},
        {'updateTextStyle': {'objectId': title_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 36, 'unit': 'PT'}, 'bold': True, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,bold,fontFamily'}},
        {'updateParagraphStyle': {'objectId': title_id, 'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
        
        # Image Placeholder
        {'createShape': {'objectId': image_prompt_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': image_size, 'unit': 'EMU'}, 'height': {'magnitude': image_size, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': image_x, 'translateY': inches(2.6), 'unit': 'EMU'}}}},
        {'updateShapeProperties': {'objectId': image_prompt_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': {'red': 0.9, 'green': 0.9, 'blue': 0.9}}}}, 'outline': {'outlineFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['maroon']}}}, 'weight': {'magnitude': 2, 'unit': 'PT'}}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        
        # Logos
        {'createImage': {'objectId': bell_img_id, 'url': bell_url, 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': logo_width, 'unit': 'EMU'}, 'height': {'magnitude': logo_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': center_x - logo_width - gap/2, 'translateY': logo_y, 'unit': 'EMU'}}}},
        {'createImage': {'objectId': act_img_id, 'url': act_url, 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': logo_width, 'unit': 'EMU'}, 'height': {'magnitude': logo_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': center_x + gap/2, 'translateY': logo_y, 'unit': 'EMU'}}}}
    ]
    
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': all_requests}).execute()
    print("✅ Created title slide")
    return slide_id

def create_content_slide(slides_service, presentation_id, title, body, transition=False):
    slide_id = _generate_id()
    header_id, title_id, body_id = _generate_id(), _generate_id(), _generate_id()
    
    # Transition slides get a different color header
    header_color = BRAND_COLORS['light_maroon'] if transition else BRAND_COLORS['maroon']
    
    all_requests = [
        {'createSlide': {'objectId': slide_id, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}},
        {'createShape': {'objectId': header_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': SLIDE_WIDTH, 'unit': 'EMU'}, 'height': {'magnitude': inches(0.8), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 0, 'translateY': 0, 'unit': 'EMU'}}}},
        {'createShape': {'objectId': title_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 'height': {'magnitude': inches(0.7), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.3), 'translateY': inches(0.05), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': title_id, 'text': title}},
        {'createShape': {'objectId': body_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 'height': {'magnitude': inches(3.8), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.5), 'translateY': inches(1.2), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': body_id, 'text': body}},
        
        # Styles
        {'updateShapeProperties': {'objectId': header_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': header_color}}}, 'outline': {'propertyState': 'NOT_RENDERED'}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        {'updateTextStyle': {'objectId': title_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 30, 'unit': 'PT'}, 'bold': True, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,bold,fontFamily'}},
        {'updateTextStyle': {'objectId': body_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['dark_gray']}}, 'fontSize': {'magnitude': 24, 'unit': 'PT'}, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}},
        {'updateParagraphStyle': {'objectId': body_id, 'style': {'alignment': 'START'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}}
    ]
    
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': all_requests}).execute()
    print(f"✅ Created slide: {title}")
    return slide_id

def main():
    print("🚀 Creating Pronunciation Soundcheck Slideshow...")
    slides_service = authenticate_slides()
    drive_service = authenticate_drive()
    
    # Upload logos
    bell_url = upload_logo(drive_service, "Bell.png")
    act_url = upload_logo(drive_service, "ACT.png")
    
    # Create
    presentation = slides_service.presentations().create(body={'title': '12-01-2026-Pronunciation-Soundcheck-Slides'}).execute()
    presentation_id = presentation.get('presentationId')
    time.sleep(1)
    
    # Delete default first slide
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': [{'deleteObject': {'objectId': presentation.get('slides')[0]['objectId']}}]}).execute()
    
    # 1. Title
    create_title_slide(
        slides_service, presentation_id, 
        "The Pronunciation Soundcheck", 
        "B1 Speaking", 
        bell_url, act_url
    )
    
    # 2. Intro
    create_content_slide(
        slides_service, presentation_id,
        "Welcome to the Studio",
        "• Today isn't about learning NEW words.\n• It's about mixing the track you already have.\n• We are going to fix the 'glitches' in your sound."
    )
    
    # 3. Transition 1
    create_content_slide(
        slides_service, presentation_id,
        "Segue: The Mic Check",
        "Before we start the mix, we need to check the equipment.\n\nLet's listen to your current signal.",
        transition=True
    )
    
    # 4. Step 1
    create_content_slide(
        slides_service, presentation_id,
        "Step 1: The Mic Check",
        "Look at your feedback sheet.\n\nWhat are your 3 biggest distortions?\n• Is it... mumbling endings?\n• Is it... shouting the stress?\n• Is it... breaking the flow?"
    )
    
    # 5. Transition 2
    create_content_slide(
        slides_service, presentation_id,
        "Segue: The Toolchest",
        "You know the problem. Now you need the tools to fix it.\n\nOpening the Studio Toolchest...",
        transition=True
    )
    
    # 6. Tool 1
    create_content_slide(
        slides_service, presentation_id,
        "Tool 1: The Crossfader (Linking)",
        "English doesn't stop. It flows.\n\n• Robot: 'I. Want. To. Be. An. Engineer.' (Choppy)\n• DJ Mix: 'I wan‿tə be‿an‿engineer.' (Smooth)\n• The Symbol: ‿ (The glue that holds words together)"
    )
    
    # 7. Tool 2
    create_content_slide(
        slides_service, presentation_id,
        "Tool 2: The Anchor (Final Consonants)",
        "Don't drop the mic!\nThe last sound is the ANCHOR. It holds the word in my ear.\n\n• 'Engi-nee...' (Floating away...)\n• 'EngineeR' (Anchored!)"
    )
    
    # 8. Tool 3
    create_content_slide(
        slides_service, presentation_id,
        "Tool 3: The Fade-Out (Tapered Endings)",
        "Don't SHOUT the end.\n\n• Bad Mix: 'Fu-ture-AH!' 'Doc-tor-AH!'\n• Pro Mix: 'Future...' (Soft, falling, quiet)\n• Use the Fader Hand: 👇 Start high, end low."
    )
    
    # 9. Transition 3
    create_content_slide(
        slides_service, presentation_id,
        "Segue: Recording Time",
        "You have the tools. Now let's lay down a track.\n\nIt's time to record.",
        transition=True
    )
    
    # 10. Step 3
    create_content_slide(
        slides_service, presentation_id,
        "Step 3: The Blueprint",
        "Look at your script: 'My Hope for the Future'\nDon't just read it. ENGINEER it.\n\n• Mark your LINKS: ‿\n• Mark your STRESS: (underline)\n• Mark your ANCHORS: (circle)"
    )
    
    # 11. Task
    create_content_slide(
        slides_service, presentation_id,
        "Task: The Performance",
        "1 minute on the clock.\n\nDeliver your 'Future Hope' speech.\n\nPartner: You are the Sound Engineer.\nCheck the levels on the checklist."
    )
    
    # 12. Model
    create_content_slide(
        slides_service, presentation_id,
        "Model Blueprint (Success Criteria)",
        "Did you sound like this?\n\n• 'My **hope** for the **future**...' (Strong Stress)\n• '...is‿to **be‿an** **engineer**.' (Smooth Linking)\n• 'I **want** to **build**...' (Anchored T/D sounds)"
    )
    
    # 13. Transition 4
    create_content_slide(
        slides_service, presentation_id,
        "Segue: Playback",
        "Session complete.\nLet's playback the review.",
        transition=True
    )
    
    # 14. Final Mix
    create_content_slide(
        slides_service, presentation_id,
        "The Final Mix",
        "Which tool fixed your sound the most?\n\n• The Anchor? (R/S/T endings)\n• The Fade-Out? (Soft vowels)\n• The Crossfader? (Linking)\n\nKeep your blueprint. That is your sheet music."
    )
    
    # Move to folder
    drive_service.files().update(fileId=presentation_id, addParents=TARGET_FOLDER_ID, removeParents='root').execute()

    print(f"\n✅ Slideshow created: https://docs.google.com/presentation/d/{presentation_id}/edit")

if __name__ == '__main__':
    main()
