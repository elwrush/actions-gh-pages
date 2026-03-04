"""
Create Useful Language Slideshow (SCR Systems - Shape I)
Following Bell EP template structure.
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
        {'createShape': {'objectId': image_prompt_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': image_size, 'unit': 'EMU'}, 'height': {'magnitude': image_size, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': image_x, 'translateY': inches(2.6), 'unit': 'EMU'}}}},
        {'updateShapeProperties': {'objectId': image_prompt_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': {'red': 0.9, 'green': 0.9, 'blue': 0.9}}}}, 'outline': {'outlineFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['maroon']}}}, 'weight': {'magnitude': 2, 'unit': 'PT'}}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        {'createImage': {'objectId': bell_img_id, 'url': bell_url, 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': logo_width, 'unit': 'EMU'}, 'height': {'magnitude': logo_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': center_x - logo_width - gap/2, 'translateY': logo_y, 'unit': 'EMU'}}}},
        {'createImage': {'objectId': act_img_id, 'url': act_url, 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': logo_width, 'unit': 'EMU'}, 'height': {'magnitude': logo_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': center_x + gap/2, 'translateY': logo_y, 'unit': 'EMU'}}}}
    ]
    
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': all_requests}).execute()
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
    return slide_id

def main():
    slides_service = authenticate_slides()
    drive_service = authenticate_drive()
    
    # Upload logos for template consistency
    bell_url = upload_logo(drive_service, "Bell.png")
    act_url = upload_logo(drive_service, "ACT.png")
    time.sleep(2)
    
    # Create presentation
    presentation = slides_service.presentations().create(body={'title': '30-12-25-Useful-Language-Slides-B1'}).execute()
    presentation_id = presentation.get('presentationId')
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': [{'deleteObject': {'objectId': presentation.get('slides')[0]['objectId']}}]}).execute()
    
    # 1. Title Slide
    create_title_slide(slides_service, presentation_id, "Useful Language: Signposting Your Story", bell_url, act_url)
    
    # 2. Situation: Best Story Warm-up
    create_content_slide(slides_service, presentation_id, "The Best Story Ever",
                        "Think about the best story you have ever read or watched.\n\n💬 Discuss with your partner:\n• What happened?\n• Why was it so good?\n• Would you recommend it?",
                        "Group of diverse students talking and laughing")
    
    # 3. Situation: Initial Trial
    create_content_slide(slides_service, presentation_id, "The 1-Minute Challenge",
                        "⏱️ You have ONE minute.\n\nTell your partner the summary of your story.\n\nRules:\n• Don't look at any notes!\n• Just talk freely.\n• Listen carefully to your partner.",
                        "Stopwatch showing 1:00")
    
    # 4. Complication: The Chaotic Presentation
    create_content_slide(slides_service, presentation_id, "The Complication: Chaotic Talk",
                        "Look at this summary:\n\n'I read Harry Potter. He lives in a house. He goes to school. I like it. He has magic. Scholastic published it. The end.'\n\n🕵️ Detective Work:\n• How does this feel to listen to?\n• Is it exciting?\n• Is it easy to follow?",
                        "A messy, tangled ball of yarn representing a confused presentation")
    
    # 5. Complication: Driving Without a Map
    create_content_slide(slides_service, presentation_id, "Driving Without a Map",
                        "🏎️ Analogy: presenting without signposts is like driving a fast car without a map.\n\n• You are moving fast...\n• ...but the audience has NO IDEA where you are going!\n• Solution: You need a GPS.",
                        "A car driving on a road that disappears into fog, with a '?' sign")
    
    # 6. Resolution: The Hero Tool (Signposts)
    create_content_slide(slides_service, presentation_id, "The Hero Tool: Signposts",
                        "📡 Signposts are your Audience GPS.\n\nThey tell the listener:\n• 'I am starting now' (Hook/Intro)\n• 'I am moving to the middle' (Exposition)\n• 'I am giving my opinion' (Evaluation)\n• 'I am finishing now' (Closing)",
                        "A bright, glowing GPS navigation screen")
    
    # 7. Resolution: The Map (Worksheet)
    create_content_slide(slides_service, presentation_id, "Your Presentation Map",
                        "Look at your Useful Language Worksheet.\n\n🗺️ Every great talk has 4 Stages:\n1. HOOK: Catch the fish.\n2. STORY: Climb the rollercoaster.\n3. OPINION: Give your gift.\n4. CLOSING: Land the plane.",
                        "A treasure map with 4 marked 'X' locations")
    
    # 8. Resolution: Thai L1 Scaffold
    create_content_slide(slides_service, presentation_id, "Connecting Your Ideas",
                        "🔗 Scaffolding for Clarity:\n\n• In Thai: 'Gin khao leaw' (Finished context).\n• In English: Signposts make 'leaw' explicit.\n\n🚀 The Bridge: 'Because' (เพราะว่า)\nDon't say: 'I like it. It's good.'\nDO say: 'I like it BECAUSE it's exciting.'",
                        "A bridge connecting two islands")
    
    # 9. Resolution: Hook Practice
    create_content_slide(slides_service, presentation_id, "Sharpen Your Hook",
                        "🎣 Your Hook must catch the audience immediately.\n\nPractice these with high energy:\n• 'Have you ever wondered...?'\n• 'Imagine waking up one day and...'\n• 'Did you know that...?'",
                        "A very sharp, shiny fishing hook")
    
    # 10. Practice: Draft Your Hero Talk
    create_content_slide(slides_service, presentation_id, "Be the Architect",
                        "✏️ Draft your 'Hero Talk' now.\n\nUse your worksheet map:\n• [STAGE 1] Choose your Hook.\n• [STAGE 3] Plan your Climax.\n• [STAGE 4] Explain WHY you like it.\n• [STAGE 5] Make your Recommendation.",
                        "An architect's blueprint for a cool structure")
    
    # 11. Practice: The Pro Sweep
    create_content_slide(slides_service, presentation_id, "The Pro Sweep",
                        "🚁 Take off! Present in your groups.\n\nAudience Task:\n• Listen for the SIGNPOSTS.\n• Put a tick on your checklist every time you hear one.\n• Give feedback: 'Your GPS was very clear!'",
                        "A helicopter flying over a clear, guided landscape")
    
    # Move to folder
    drive_service.files().update(fileId=presentation_id, addParents=TARGET_FOLDER_ID, removeParents='root').execute()
    
    print(f"\n✅ Slideshow created: https://docs.google.com/presentation/d/{presentation_id}/edit")

if __name__ == '__main__':
    main()
