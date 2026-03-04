"""
Create Presentation Structure Slideshow (v3.0 - Correct Template)
Following Bell EP template structure from update_template.py:
- Dark header bar (rgb 0.35, 0.05, 0.05) with centered logos
- "Bell Language Centre" strap line
- Centered title (36pt, bold, white)
- Square photorealistic image (2.5" x 2.5")
- Gradient body background
"""

import os
import sys
import time

PROJECT_ROOT = r"C:\PROJECTS\LESSONS AND SLIDESHOWS 2"
os.chdir(PROJECT_ROOT)

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'skills', 'designing-slides'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'skills', 'designing-slides', 'scripts'))

from scripts.authenticate_google import authenticate_slides, authenticate_drive
from scripts.add_slide_content import add_image_from_url, inches, _generate_id
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
    """Create title slide following Bell EP template structure."""
    slide_id = _generate_id()
    header_bar_id, strap_id, title_id = _generate_id(), _generate_id(), _generate_id()
    bell_img_id, act_img_id = _generate_id(), _generate_id()
    image_prompt_id = _generate_id()
    
    # Template dimensions (from update_template.py)
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
        
        # Image prompt box (since generation failed)
        {'createShape': {'objectId': image_prompt_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': image_size, 'unit': 'EMU'}, 'height': {'magnitude': image_size, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': image_x, 'translateY': inches(2.6), 'unit': 'EMU'}}}},
        {'updateShapeProperties': {'objectId': image_prompt_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': {'red': 0.9, 'green': 0.9, 'blue': 0.9}}}}, 'outline': {'outlineFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['maroon']}}}, 'weight': {'magnitude': 2, 'unit': 'PT'}}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        
        # Logos in header (centered, side-by-side)
        {'createImage': {'objectId': bell_img_id, 'url': bell_url, 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': logo_width, 'unit': 'EMU'}, 'height': {'magnitude': logo_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': center_x - logo_width - gap/2, 'translateY': logo_y, 'unit': 'EMU'}}}},
        {'createImage': {'objectId': act_img_id, 'url': act_url, 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': logo_width, 'unit': 'EMU'}, 'height': {'magnitude': logo_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': center_x + gap/2, 'translateY': logo_y, 'unit': 'EMU'}}}}
    ]
    
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': all_requests}).execute()
    print("✅ Created title slide (Bell EP template)")
    return slide_id

def create_content_slide(slides_service, presentation_id, title, body, image_prompt=None):
    slide_id = _generate_id()
    header_id, title_id, body_id = _generate_id(), _generate_id(), _generate_id()
    
    all_requests = [
        {'createSlide': {'objectId': slide_id, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}},
        {'createShape': {'objectId': header_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': SLIDE_WIDTH, 'unit': 'EMU'}, 'height': {'magnitude': inches(0.8), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 0, 'translateY': 0, 'unit': 'EMU'}}}},
        {'createShape': {'objectId': title_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 'height': {'magnitude': inches(0.7), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.3), 'translateY': inches(0.05), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': title_id, 'text': title}},
        {'createShape': {'objectId': body_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 'height': {'magnitude': inches(3.8), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.5), 'translateY': inches(1.2), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': body_id, 'text': body}},
        {'updateShapeProperties': {'objectId': header_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['maroon']}}}, 'outline': {'propertyState': 'NOT_RENDERED'}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        {'updateTextStyle': {'objectId': title_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 30, 'unit': 'PT'}, 'bold': True, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,bold,fontFamily'}},
        {'updateTextStyle': {'objectId': body_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['dark_gray']}}, 'fontSize': {'magnitude': 24, 'unit': 'PT'}, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}},
        {'updateParagraphStyle': {'objectId': body_id, 'style': {'alignment': 'START'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}}
    ]
    
    if image_prompt:
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
    print("🚀 Creating Presentation Structure slideshow (v3 - Correct Template)...")
    slides_service = authenticate_slides()
    drive_service = authenticate_drive()
    
    # Upload logos
    bell_url = upload_logo(drive_service, "Bell.png")
    act_url = upload_logo(drive_service, "ACT.png")
    time.sleep(2)
    
    # Create presentation
    presentation = slides_service.presentations().create(body={'title': '29-12-25-Presentation-Structure-Slides-v3'}).execute()
    presentation_id = presentation.get('presentationId')
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': [{'deleteObject': {'objectId': presentation.get('slides')[0]['objectId']}}]}).execute()
    
    # 1. Title slide (Bell EP template)
    create_title_slide(slides_service, presentation_id, "Presentation Skills: Structure", bell_url, act_url)
    
    # 2-10. Content slides
    create_content_slide(slides_service, presentation_id, "The #1 Fear",
                        "Why do we freeze when we speak in public?\n\n🦁 Analogy: Your brain treats an audience like a lion attack.\n• Heart beats fast\n• Sweaty palms\n• Mind goes blank",
                        "Cartoon lion looking in mirror seeing a nervous speaker")
    
    create_content_slide(slides_service, presentation_id, "The Video 'Fix'",
                        "Watch this tip from an expert:\n\n📺 https://youtube.com/shorts/cIeSVGLtgbM\n\nWhat is their secret weapon against fear?")
    
    create_content_slide(slides_service, presentation_id, "The Safety Net",
                        "🎪 Analogy: A tightrope walker without a net is terrified.\n\nSTRUCTURE is your safety net.\n• If you forget a word, the map catches you.\n• It tells you exactly where to go next.",
                        "Tightrope walker with a safety net shaped like an outline")
    
    create_content_slide(slides_service, presentation_id, "The Temple of a Great Talk",
                        "🏛️ Great presentations stand on 4 Pillars:\n\n1. THE HOOK (Catch them)\n2. THE ARC (Tell the story)\n3. THE ANALYSIS (Deep dive)\n4. THE GIFT (Recommendation)",
                        "Greek temple with 4 pillars labeled Hook, Arc, Analysis, Gift")
    
    create_content_slide(slides_service, presentation_id, "Pillar 1: The Hook",
                        "🎣 Analogy: The Hook is your bait.\n\n• Question: \"Have you ever...?\"\n• Imagine: \"Imagine a world where...\"\n• Fact: \"Did you know that 90% of...\"\n• Quote: \"As Einstein said...\"",
                        "Fishing hook with a speech bubble attached")
    
    create_content_slide(slides_service, presentation_id, "Pillar 2: The Story Arc",
                        "🎢 Analogy: A story is like a rollercoaster.\n\n• Introduction: Getting in the seat.\n• Rising Action: The slow climb up.\n• Climax: The big drop!\n• Resolution: Coming safely to the end.",
                        "Rollercoaster track showing 4 stages")
    
    create_content_slide(slides_service, presentation_id, "Be the Architect",
                        "✏️ Analogy: Sketch before you build.\n\nTask: Use your Planning Sheet.\n• Plan your 4 pillars.\n• Choose your bait (Hook).\n• Design your drop (Climax).")
    
    create_content_slide(slides_service, presentation_id, "The Elevator Pitch",
                        "🚀 Analogy: You have one floor to sell your idea.\n\nPractice with a partner (30 seconds):\n1. Deliver your Hook.\n2. Summarize your Climax.\nDid they want to hear more?")
    
    create_content_slide(slides_service, presentation_id, "The Flight Check",
                        "✈️ Analogy: A pilot never takes off without a check.\n\nLook at the checklist on your sheet:\n• Is my hook sharp?\n• Is my climax exciting?\n• Is my gift (recommendation) clear?")
    
    # Move to folder
    drive_service.files().update(fileId=presentation_id, addParents=TARGET_FOLDER_ID, removeParents='root').execute()
    
    print(f"\n✅ Slideshow created: https://docs.google.com/presentation/d/1{presentation_id}/edit")
    print("📌 Title slide uses Bell EP template structure")
    print("📌 Image prompts included for manual insertion")

if __name__ == '__main__':
    main()
