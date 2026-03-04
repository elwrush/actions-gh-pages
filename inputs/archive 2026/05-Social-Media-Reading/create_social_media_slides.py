"""
Create Social Media Society Slideshow (Shape H - SCR Reading)
Based on create_presentation_structure_slides.py template
Lesson Plan: 06-01-26-LP B1-Social-Media-Reading-Shape H.html
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
    image_box_id = _generate_id()
    
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
        {'createShape': {'objectId': image_box_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': image_size, 'unit': 'EMU'}, 'height': {'magnitude': image_size, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': image_x, 'translateY': inches(2.6), 'unit': 'EMU'}}}},
        {'updateShapeProperties': {'objectId': image_box_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': {'red': 0.9, 'green': 0.9, 'blue': 0.9}}}}, 'outline': {'outlineFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['maroon']}}}, 'weight': {'magnitude': 2, 'unit': 'PT'}}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
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
        {'createShape': {'objectId': body_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 'height': {'magnitude': inches(4.2), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.5), 'translateY': inches(1.2), 'unit': 'EMU'}}}},
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
    print("🚀 Creating Social Media Society slideshow...")
    slides_service = authenticate_slides()
    drive_service = authenticate_drive()
    
    bell_url = upload_logo(drive_service, "Bell.png")
    act_url = upload_logo(drive_service, "ACT.png")
    time.sleep(2)
    
    presentation = slides_service.presentations().create(body={'title': '06-01-26-Social-Media-Society-Slides'}).execute()
    presentation_id = presentation.get('presentationId')
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': [{'deleteObject': {'objectId': presentation.get('slides')[0]['objectId']}}]}).execute()
    
    # 1. Title slide
    create_title_slide(slides_service, presentation_id, "Social Media Society", bell_url, act_url)
    
    # 2. Daily Check Poll
    create_content_slide(slides_service, presentation_id, "The Daily Check",
                        "How many social media apps do you check before breakfast?\n\n□ 0 (I sleep)\n□ 1-2\n□ 3-5\n□ 5+ (I am the internet)\n\nRaise your hands!")
    
    # 3. Vocabulary 1
    create_content_slide(slides_service, presentation_id, "Vocabulary: antisocial",
                        "antisocial /ˌæntiˈsəʊʃəl/: ไม่ชอบสังคม\n\nSome teenagers become antisocial and prefer staying in their rooms.\n\nวัยรุ่นบางคนไม่ชอบสังคมและชอบอยู่ในห้องคนเดียว")
    
    # 4. Vocabulary 2
    create_content_slide(slides_service, presentation_id, "Vocabulary: hikikomori",
                        "hikikomori /ˌhɪkiˈkɒməri/: คนที่หลบหนีสังคม (ภาษาญี่ปุ่น)\n\nThe term hikikomori describes extreme social withdrawal.\n\nคำว่าฮิกิโกะโมริหมายถึงการถอนตัวจากสังคมอย่างรุนแรง")
    
    # 5. Vocabulary 3
    create_content_slide(slides_service, presentation_id, "Vocabulary: popularity contest",
                        "popularity contest /ˌpɒpjuˈlærəti ˈkɒntest/: การแข่งขันเรื่องความนิยม\n\nSchool shouldn't be a popularity contest.\n\nโรงเรียนไม่ควรเป็นการแข่งขันเรื่องความนิยม")
    
    # 6. The Challenge
    create_content_slide(slides_service, presentation_id, "The Challenge",
                        "Your worksheet has 8 sections about social media.\n\n❓ Is social media good or bad?\n❓ What does the text say?\n\n⚠️ Problem: Too many opinions! Which are positive? Which are negative?")
    
    # 7. The Problem Deepens
    create_content_slide(slides_service, presentation_id, "Why It's Hard",
                        "Look at Section 1:\n\"Social media is changing everything...\"\n\n❓ Is this positive or negative?\n\nYou can't decide without understanding every word!\n\nBut you don't have time to translate everything...")
    
    # 8. The Hero Tool
    create_content_slide(slides_service, presentation_id, "Your Hero Tool: Skimming for Tone",
                        "Don't read everything! Look for TONE WORDS:\n\n✅ Positive (+):\n   connect, help, opportunity, socialize\n\n❌ Negative (-):\n   antisocial, anxious, depressed, unfortunately\n\n⚖️ Balanced (=):\n   \"on the one hand... on the other hand\"")
    
    # 9. Example
    create_content_slide(slides_service, presentation_id, "Detective Work Example",
                        "Section 2:\n\"Many people argue that social media makes young people antisocial.\"\n\nFirst sentence has 'antisocial' → Negative!\n\nYou didn't need to translate 'hikikomori'!")
    
    # 10. Your Turn
    create_content_slide(slides_service, presentation_id, "Your Turn: Be the Detective",
                        "Work with your partner:\n\n1. Read the FIRST SENTENCE of each section\n2. Find ONE tone word\n3. Decide: + / - / =\n4. Write your evidence\n\nYou have 18 minutes. Go!")
    
    # 11. Reflection
    create_content_slide(slides_service, presentation_id, "Before → After",
                        "Before today:\nWhat did you do with long English texts?\n\nAfter today:\nWhat will you do now?\n\nKey lesson: You don't need every word.\nYou need the RIGHT words.")
    
    # Move to folder
    drive_service.files().update(fileId=presentation_id, addParents=TARGET_FOLDER_ID, removeParents='root').execute()
    
    print(f"\n✅ Slideshow created: https://docs.google.com/presentation/d/{presentation_id}/edit")

if __name__ == '__main__':
    main()
