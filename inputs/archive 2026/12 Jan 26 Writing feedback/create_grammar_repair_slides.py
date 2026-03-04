"""
Create Grammar Repair Shop Slideshow
Following Bell EP template structure and batch API patterns.
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

# Folder for 12 Jan 26 Writing feedback
TARGET_FOLDER_ID = "1_n11w9BRN6sd0uaXlqEXjqZuZ74zFiOl" 
LOGO_DIR = os.path.join(PROJECT_ROOT, "images")

def upload_to_drive(drive_service, file_path):
    file_name = os.path.basename(file_path)
    mime_type = 'image/png' if file_name.endswith('.png') else 'image/jpeg'
    media = MediaFileUpload(file_path, mimetype=mime_type)
    file = drive_service.files().create(body={'name': file_name}, media_body=media, fields='id').execute()
    file_id = file.get('id')
    drive_service.permissions().create(fileId=file_id, body={'type': 'anyone', 'role': 'reader'}).execute()
    return f"https://lh3.googleusercontent.com/d/{file_id}"

def get_title_slide_requests(slide_id, title, bell_url, act_url):
    header_bar_id, strap_id, title_id = _generate_id(), _generate_id(), _generate_id()
    bell_img_id, act_img_id = _generate_id(), _generate_id()
    
    header_height = inches(1.0)
    logo_height, logo_width = inches(0.7), inches(1.0)
    logo_y = (header_height - logo_height) / 2
    center_x = SLIDE_WIDTH / 2
    gap = inches(0.3)
    
    return [
        {'createSlide': {'objectId': slide_id, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}},
        {'updatePageProperties': {'objectId': slide_id, 'pageProperties': {'pageBackgroundFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['light_maroon']}}}}, 'fields': 'pageBackgroundFill.solidFill.color'}},
        
        # Dark header bar
        {'createShape': {'objectId': header_bar_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': SLIDE_WIDTH, 'unit': 'EMU'}, 'height': {'magnitude': header_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 0, 'translateY': 0, 'unit': 'EMU'}}}},
        {'updateShapeProperties': {'objectId': header_bar_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['header_dark']}}}, 'outline': {'propertyState': 'NOT_RENDERED'}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        
        # Strap line
        {'createShape': {'objectId': strap_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 'height': {'magnitude': inches(0.5), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 'translateY': inches(1.1), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': strap_id, 'text': 'Bell Language Centre'}},
        {'updateTextStyle': {'objectId': strap_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 18, 'unit': 'PT'}, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}},
        {'updateParagraphStyle': {'objectId': strap_id, 'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
        
        # Title
        {'createShape': {'objectId': title_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 'height': {'magnitude': inches(1.2), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 'translateY': inches(1.7), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': title_id, 'text': title}},
        {'updateTextStyle': {'objectId': title_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 36, 'unit': 'PT'}, 'bold': True, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,bold,fontFamily'}},
        {'updateParagraphStyle': {'objectId': title_id, 'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
        
        # Logos
        {'createImage': {'objectId': bell_img_id, 'url': bell_url, 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': logo_width, 'unit': 'EMU'}, 'height': {'magnitude': logo_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': center_x - logo_width - gap/2, 'translateY': logo_y, 'unit': 'EMU'}}}},
        {'createImage': {'objectId': act_img_id, 'url': act_url, 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': logo_width, 'unit': 'EMU'}, 'height': {'magnitude': logo_height, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': center_x + gap/2, 'translateY': logo_y, 'unit': 'EMU'}}}}
    ]

def get_content_slide_requests(slide_id, title, bullets):
    header_id, title_id, body_id = _generate_id(), _generate_id(), _generate_id()
    body_text = "\n".join([f"• {b}" if not b.startswith((" ", "•", "-")) else b for b in bullets])
    
    return [
        {'createSlide': {'objectId': slide_id, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}},
        {'createShape': {'objectId': header_id, 'shapeType': 'RECTANGLE', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': SLIDE_WIDTH, 'unit': 'EMU'}, 'height': {'magnitude': inches(0.8), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 0, 'translateY': 0, 'unit': 'EMU'}}}},
        {'createShape': {'objectId': title_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 'height': {'magnitude': inches(0.7), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.3), 'translateY': inches(0.05), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': title_id, 'text': title}},
        {'createShape': {'objectId': body_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 'height': {'magnitude': inches(4.5), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.5), 'translateY': inches(1.2), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': body_id, 'text': body_text}},
        {'updateShapeProperties': {'objectId': header_id, 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['maroon']}}}, 'outline': {'propertyState': 'NOT_RENDERED'}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        {'updateTextStyle': {'objectId': title_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 30, 'unit': 'PT'}, 'bold': True, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,bold,fontFamily'}},
        {'updateTextStyle': {'objectId': body_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['dark_gray']}}, 'fontSize': {'magnitude': 24, 'unit': 'PT'}, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}},
        {'updateParagraphStyle': {'objectId': body_id, 'style': {'alignment': 'START', 'spaceBelow': {'magnitude': 10, 'unit': 'PT'}}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment,spaceBelow'}}
    ]

def get_transition_slide_requests(slide_id, text):
    text_id = _generate_id()
    return [
        {'createSlide': {'objectId': slide_id, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}},
        {'updatePageProperties': {'objectId': slide_id, 'pageProperties': {'pageBackgroundFill': {'solidFill': {'color': {'rgbColor': BRAND_COLORS['maroon']}}}}, 'fields': 'pageBackgroundFill.solidFill.color'}},
        {'createShape': {'objectId': text_id, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': slide_id, 'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 'height': {'magnitude': inches(3), 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 'translateY': inches(2), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': text_id, 'text': text}},
        {'updateTextStyle': {'objectId': text_id, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}}, 'fontSize': {'magnitude': 32, 'unit': 'PT'}, 'italic': True, 'bold': True, 'fontFamily': 'Arial'}, 'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,italic,bold,fontFamily'}},
        {'updateParagraphStyle': {'objectId': text_id, 'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}}
    ]

def main():
    slides_service = authenticate_slides()
    drive_service = authenticate_drive()
    
    print("📤 Uploading logos...")
    bell_url = upload_to_drive(drive_service, os.path.join(LOGO_DIR, "Bell.png"))
    act_url = upload_to_drive(drive_service, os.path.join(LOGO_DIR, "ACT.png"))
    
    presentation_title = "11-01-2026-B1-Grammar-Repair-Shop-Slides"
    presentation = slides_service.presentations().create(body={'title': presentation_title}).execute()
    presentation_id = presentation.get('presentationId')
    
    all_requests = []
    
    # Remove initial blank slide
    initial_slide_id = presentation.get('slides')[0]['objectId']
    all_requests.append({'deleteObject': {'objectId': initial_slide_id}})
    
    # 1. Title Slide
    s1_id = _generate_id()
    all_requests.extend(get_title_slide_requests(s1_id, "THE GRAMMAR REPAIR SHOP\nPrecision Engineering for Writers", bell_url, act_url))
    
    # 2. Transition: Opening the Garage
    s2_id = _generate_id()
    all_requests.extend(get_transition_slide_requests(s2_id, "Welcome to the workshop.\nToday, we're fine-tuning your communication engine."))
    
    # 3. The Mechanic's Mindset
    s3_id = _generate_id()
    all_requests.extend(get_content_slide_requests(s3_id, "The Mechanic's Mindset", [
        "Every great car needs maintenance.",
        "Every great writer needs a 'Diagnostic Check'.",
        "Today, YOU are the lead mechanics.",
        "We identifying 'repair points', not 'mistakes'."
    ]))
    
    # 4. The Diagnostic Report (ERRANT)
    s4_id = _generate_id()
    all_requests.extend(get_content_slide_requests(s4_id, "The Diagnostic Report (ERRANT)", [
        "Cambridge University's ERRANT Toolkit.",
        "Your specialized sensor system that scans for:",
        "Missing parts (is, the, a)",
        "Broken parts (wrong word forms)",
        "Extra parts (clogging the flow)"
    ]))
    
    # 5. Reading the Data
    s5_id = _generate_id()
    all_requests.extend(get_content_slide_requests(s5_id, "Reading the Data", [
        "Your report is YOUR personalized diagnostic.",
        "It shows exactly where your engine is leaking.",
        "Focus on the Frequency – what happens most often?"
    ]))
    
    # 6. Transition: Selecting the Right Spanners
    s6_id = _generate_id()
    all_requests.extend(get_transition_slide_requests(s6_id, "A mechanic is only as good as their preparation.\nLet's pick our tools..."))
    
    # 7. Mission Prep: Mapping the Faults
    s7_id = _generate_id()
    all_requests.extend(get_content_slide_requests(s7_id, "Mission Prep: Mapping the Faults", [
        "Review your individualized Profile.",
        "Choose your Top 3 Repair Targets.",
        "Write them into your Worksheet header.",
        "Be specific: 'Noun Plurals' vs 'Nouns'."
    ]))
    
    # 8. Choosing Your Grade
    s8_id = _generate_id()
    all_requests.extend(get_content_slide_requests(s8_id, "Choosing Your Grade", [
        "Select the task that pushes your engine:",
        "Level A2: The Secret Recipe (50+ words)",
        "Level B1: The Masterchef Warning (70+ words)",
        "Level B2: Signature Dishes (100+ words)"
    ]))
    
    # 9. Transition: Activating the Sensors
    s9_id = _generate_id()
    all_requests.extend(get_transition_slide_requests(s9_id, "Before we turn the key,\nlet's switch on our high-tech monitoring systems..."))
    
    # 10. The Hero Tool: Self-Correction Radar
    s10_id = _generate_id()
    all_requests.extend(get_content_slide_requests(s10_id, "The Hero Tool: Self-Correction Radar", [
        "Use the Radar Checklist at the top of your task.",
        "It's like a dashboard warning light:",
        "Did I check my plurals? Are my articles in place?",
        "Don't wait until the end – check as you go!"
    ]))
    
    # 11. Transition: Getting Under the Hood
    s11_id = _generate_id()
    all_requests.extend(get_transition_slide_requests(s11_id, "Tools in hand, radar on.\nIt's time to get to work."))
    
    # 12. Precision Drafting
    s12_id = _generate_id()
    all_requests.extend(get_content_slide_requests(s12_id, "Precision Drafting", [
        "Write your paragraph in the workshop area.",
        "Focus on Accuracy over Speed.",
        "Listen for the 'engine noise' – does it sound right?",
        "Head Mechanic (Ed) is available for consultation."
    ]))
    
    # 13. Transition: The Mandatory Safety Check
    s13_id = _generate_id()
    all_requests.extend(get_transition_slide_requests(s13_id, "Every car needs a second pair of eyes\nbefore it leaves the workshop."))
    
    # 14. Quality Control: Peer Inspection
    s14_id = _generate_id()
    all_requests.extend(get_content_slide_requests(s14_id, "Quality Control: Peer Inspection", [
        "Swap your paragraph with a fellow mechanic.",
        "Check their 3 Targets ONLY.",
        "Highlight successes: 'This part is running smooth!'",
        "Polite feedback: 'Maybe tighten this part slightly...'"
    ]))
    
    # 15. Transition: Ready for the Road
    s15_id = _generate_id()
    all_requests.extend(get_transition_slide_requests(s15_id, "Repairs complete. The output is clean,\nefficient, and ready to go."))
    
    # 16. The Final Checkout
    s16_id = _generate_id()
    all_requests.extend(get_content_slide_requests(s16_id, "The Final Checkout", [
        "Which grammar point was the easiest to 'fix'?",
        "Which part of your writing is now 100% efficient?",
        "Hand in your worksheets and reports."
    ]))
    
    print("🚀 Executing batch slide creation...")
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': all_requests}).execute()
    
    # Move to folder
    print("📂 Organizing in Drive...")
    drive_service.files().update(fileId=presentation_id, addParents=TARGET_FOLDER_ID, removeParents='root').execute()
    
    print(f"\n✅ Slideshow created: https://docs.google.com/presentation/d/{presentation_id}/edit")

if __name__ == '__main__':
    main()
