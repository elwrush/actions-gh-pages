"""
Create Politeness Lesson Slideshow (Themed + Layouts)

FEATURES:
- Batch API operations (single batchUpdate)
- Color-coded headers by slide type
- Adventurous answer layouts (Spotlight, Side Panel, Flow)
- Proper cover slide with logos + strap line
- Video placeholder with play button
"""

import os
import sys
import time
import uuid

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
os.chdir(PROJECT_ROOT)

sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, os.path.join(SCRIPT_DIR, 'scripts'))

from googleapiclient.http import MediaFileUpload
from scripts.authenticate_google import authenticate_slides, authenticate_drive
from scripts.format_slides import SLIDE_WIDTH, SLIDE_HEIGHT

# Constants
INCH_TO_EMU = 914400

def inches(value):
    return int(value * INCH_TO_EMU)

def _generate_id():
    return str(uuid.uuid4()).replace('-', '')[:24]

# ============================================================
# THEME COLORS
# ============================================================
COLORS = {
    # Core branding
    'maroon': {'red': 166/255, 'green': 45/255, 'blue': 38/255},
    'dark_maroon': {'red': 89/255, 'green': 13/255, 'blue': 13/255},
    'white': {'red': 1.0, 'green': 1.0, 'blue': 1.0},
    'dark_gray': {'red': 0.2, 'green': 0.2, 'blue': 0.2},
    'light_gray': {'red': 0.95, 'green': 0.95, 'blue': 0.95},
    
    # Themed headers
    'vocab_teal': {'red': 0/255, 'green': 128/255, 'blue': 128/255},
    'answer_green': {'red': 46/255, 'green': 125/255, 'blue': 50/255},
    'answer_light': {'red': 232/255, 'green': 245/255, 'blue': 233/255},
    'activity_orange': {'red': 230/255, 'green': 126/255, 'blue': 34/255},
    'discussion_purple': {'red': 103/255, 'green': 58/255, 'blue': 183/255},
    'video_red': {'red': 255/255, 'green': 0/255, 'blue': 0/255},
}

# Config
TARGET_FOLDER_ID = "1_n11w9BRN6sd0uaXlqEXjqZuZ74zFiOl"
IMAGE_DIR = os.path.join(os.path.expanduser("~"), ".gemini", "antigravity", "brain", 
                         "6676dadb-d43e-4e5c-9dff-ed498947bb8c")
LOCAL_IMAGE_DIR = os.path.join(PROJECT_ROOT, "inputs", "Intensive-Reading-Politeness")
LOGO_DIR = os.path.join(PROJECT_ROOT, "images")  # Correct path: project root images/


# ============================================================
# REQUEST BUILDER FUNCTIONS
# ============================================================

def get_create_slide_requests(slide_id):
    return [{'createSlide': {'objectId': slide_id, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}}]


def get_header_bar_requests(slide_id, title, header_color=None):
    """Header bar with customizable color."""
    if header_color is None:
        header_color = COLORS['maroon']
    
    header_id = _generate_id()
    title_id = _generate_id()
    
    return [
        # Header rectangle
        {'createShape': {'objectId': header_id, 'shapeType': 'RECTANGLE',
            'elementProperties': {'pageObjectId': slide_id,
                'size': {'width': {'magnitude': SLIDE_WIDTH, 'unit': 'EMU'}, 
                        'height': {'magnitude': inches(1), 'unit': 'EMU'}},
                'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 0, 'translateY': 0, 'unit': 'EMU'}}}},
        # Title text
        {'createShape': {'objectId': title_id, 'shapeType': 'TEXT_BOX',
            'elementProperties': {'pageObjectId': slide_id,
                'size': {'width': {'magnitude': inches(9), 'unit': 'EMU'}, 
                        'height': {'magnitude': inches(0.8), 'unit': 'EMU'}},
                'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.5), 
                             'translateY': inches(0.1), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': title_id, 'text': title}},
        # Style header
        {'updateShapeProperties': {'objectId': header_id,
            'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': header_color}}},
                               'outline': {'propertyState': 'NOT_RENDERED'}},
            'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        # Style title
        {'updateTextStyle': {'objectId': title_id,
            'style': {'foregroundColor': {'opaqueColor': {'rgbColor': COLORS['white']}},
                     'fontSize': {'magnitude': 32, 'unit': 'PT'}, 'bold': True, 'fontFamily': 'Arial'},
            'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,bold,fontFamily'}}
    ]


def get_body_text_requests(slide_id, text, y_offset=1.2, font_size=24, width=9):
    body_id = _generate_id()
    return [
        {'createShape': {'objectId': body_id, 'shapeType': 'TEXT_BOX',
            'elementProperties': {'pageObjectId': slide_id,
                'size': {'width': {'magnitude': inches(width), 'unit': 'EMU'}, 
                        'height': {'magnitude': inches(4), 'unit': 'EMU'}},
                'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.5), 
                             'translateY': inches(y_offset), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': body_id, 'text': text}},
        {'updateTextStyle': {'objectId': body_id,
            'style': {'foregroundColor': {'opaqueColor': {'rgbColor': COLORS['dark_gray']}},
                     'fontSize': {'magnitude': font_size, 'unit': 'PT'}, 'fontFamily': 'Arial'},
            'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}}
    ]


def get_image_requests(slide_id, image_url, x, y, width, height):
    image_id = _generate_id()
    return [{'createImage': {'objectId': image_id, 'url': image_url,
        'elementProperties': {'pageObjectId': slide_id,
            'size': {'width': {'magnitude': width, 'unit': 'EMU'}, 'height': {'magnitude': height, 'unit': 'EMU'}},
            'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': x, 'translateY': y, 'unit': 'EMU'}}}}]


# ============================================================
# THEMED SLIDE BUILDERS
# ============================================================

def get_cover_slide_requests(slide_id, title, cover_url=None, bell_url=None, act_url=None):
    """Cover slide with centered logos in header, strap line, title, and cover image below."""
    strap_id = _generate_id()
    title_id = _generate_id()
    header_id = _generate_id()
    
    # Layout constants (matching original template)
    header_height = inches(1.0)
    logo_height = inches(0.7)
    logo_width = inches(1.0)
    logo_y = (header_height - logo_height) / 2  # Vertically centered in header
    center_x = SLIDE_WIDTH / 2
    gap = inches(0.3)
    
    requests = [
        # Maroon background
        {'updatePageProperties': {'objectId': slide_id,
            'pageProperties': {'pageBackgroundFill': {'solidFill': {'color': {'rgbColor': COLORS['maroon']}}}},
            'fields': 'pageBackgroundFill.solidFill.color'}},
        # Dark header bar at top
        {'createShape': {'objectId': header_id, 'shapeType': 'RECTANGLE',
            'elementProperties': {'pageObjectId': slide_id,
                'size': {'width': {'magnitude': SLIDE_WIDTH, 'unit': 'EMU'}, 
                        'height': {'magnitude': header_height, 'unit': 'EMU'}},
                'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 0, 'translateY': 0, 'unit': 'EMU'}}}},
        {'updateShapeProperties': {'objectId': header_id,
            'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': COLORS['dark_maroon']}}},
                               'outline': {'propertyState': 'NOT_RENDERED'}},
            'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
        # Strap line (below header)
        {'createShape': {'objectId': strap_id, 'shapeType': 'TEXT_BOX',
            'elementProperties': {'pageObjectId': slide_id,
                'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 
                        'height': {'magnitude': inches(0.5), 'unit': 'EMU'}},
                'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 
                             'translateY': inches(1.1), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': strap_id, 'text': 'Bell Language Centre'}},
        {'updateTextStyle': {'objectId': strap_id,
            'style': {'foregroundColor': {'opaqueColor': {'rgbColor': COLORS['white']}},
                     'fontSize': {'magnitude': 18, 'unit': 'PT'}, 'fontFamily': 'Arial'},
            'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}},
        {'updateParagraphStyle': {'objectId': strap_id, 
            'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
        # Main title
        {'createShape': {'objectId': title_id, 'shapeType': 'TEXT_BOX',
            'elementProperties': {'pageObjectId': slide_id,
                'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 
                        'height': {'magnitude': inches(0.8), 'unit': 'EMU'}},
                'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 
                             'translateY': inches(1.7), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': title_id, 'text': title}},
        {'updateTextStyle': {'objectId': title_id,
            'style': {'foregroundColor': {'opaqueColor': {'rgbColor': COLORS['white']}},
                     'fontSize': {'magnitude': 36, 'unit': 'PT'}, 'bold': True, 'fontFamily': 'Arial'},
            'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,bold,fontFamily'}},
        {'updateParagraphStyle': {'objectId': title_id, 
            'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
    ]
    
    # Add logos CENTERED in header (Bell left of center, ACT right of center)
    if bell_url:
        requests.extend(get_image_requests(slide_id, bell_url, 
            int(center_x - logo_width - gap/2), int(logo_y), int(logo_width), int(logo_height)))
    if act_url:
        requests.extend(get_image_requests(slide_id, act_url, 
            int(center_x + gap/2), int(logo_y), int(logo_width), int(logo_height)))
    
    # Cover image (centered, below title, with proper spacing)
    if cover_url:
        image_size = inches(2.5)
        image_x = (SLIDE_WIDTH - image_size) / 2
        requests.extend(get_image_requests(slide_id, cover_url, 
            int(image_x), inches(2.6), int(image_size), int(image_size)))
    
    return requests


def get_vocab_slide_requests(slide_id, word, phonemic, thai, eng, thai_sent, image_url=None):
    """Vocabulary slide with teal header, two-column layout."""
    vocab_text = f"{word} {phonemic}: {thai}\n\n{eng}\n\n{thai_sent}"
    
    requests = get_header_bar_requests(slide_id, f"Vocabulary: {word}", COLORS['vocab_teal'])
    
    if image_url:
        # Left text (narrower)
        body_id = _generate_id()
        requests.extend([
            {'createShape': {'objectId': body_id, 'shapeType': 'TEXT_BOX',
                'elementProperties': {'pageObjectId': slide_id,
                    'size': {'width': {'magnitude': inches(5.5), 'unit': 'EMU'}, 
                            'height': {'magnitude': inches(4), 'unit': 'EMU'}},
                    'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(0.5), 
                                 'translateY': inches(1.2), 'unit': 'EMU'}}}},
            {'insertText': {'objectId': body_id, 'text': vocab_text}},
            {'updateTextStyle': {'objectId': body_id,
                'style': {'foregroundColor': {'opaqueColor': {'rgbColor': COLORS['dark_gray']}},
                         'fontSize': {'magnitude': 22, 'unit': 'PT'}, 'fontFamily': 'Arial'},
                'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}}
        ])
        # Right image
        requests.extend(get_image_requests(slide_id, image_url, inches(6.2), inches(1.5), inches(3.3), inches(3.3)))
    else:
        requests.extend(get_body_text_requests(slide_id, vocab_text, font_size=22))
    
    return requests


def get_answer_slide_spotlight(slide_id, section_title, question, answer, explanation, snippet=None):
    """Layout A: Spotlight Answer - Large centered answer box."""
    answer_box_id = _generate_id()
    question_id = _generate_id()
    snippet_id = _generate_id()
    explain_id = _generate_id()
    
    requests = get_header_bar_requests(slide_id, section_title, COLORS['answer_green'])
    
    # Light green background area
    bg_id = _generate_id()
    requests.extend([
        {'createShape': {'objectId': bg_id, 'shapeType': 'RECTANGLE',
            'elementProperties': {'pageObjectId': slide_id,
                'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 
                        'height': {'magnitude': inches(1.0), 'unit': 'EMU'}},
                'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 
                             'translateY': inches(1.8), 'unit': 'EMU'}}}},
        {'updateShapeProperties': {'objectId': bg_id,
            'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': COLORS['answer_light']}}},
                               'outline': {'propertyState': 'NOT_RENDERED'}},
            'fields': 'shapeBackgroundFill.solidFill.color,outline'}},
    ])
    
    # Question (small, top)
    requests.extend([
        {'createShape': {'objectId': question_id, 'shapeType': 'TEXT_BOX',
            'elementProperties': {'pageObjectId': slide_id,
                'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 
                        'height': {'magnitude': inches(0.5), 'unit': 'EMU'}},
                'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 
                             'translateY': inches(1.2), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': question_id, 'text': question}},
        {'updateTextStyle': {'objectId': question_id,
            'style': {'foregroundColor': {'opaqueColor': {'rgbColor': COLORS['dark_gray']}},
                     'fontSize': {'magnitude': 18, 'unit': 'PT'}, 'fontFamily': 'Arial'},
            'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}},
    ])
    
    # Large ANSWER (centered in highlight box)
    requests.extend([
        {'createShape': {'objectId': answer_box_id, 'shapeType': 'TEXT_BOX',
            'elementProperties': {'pageObjectId': slide_id,
                'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 
                        'height': {'magnitude': inches(0.8), 'unit': 'EMU'}},
                'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 
                             'translateY': inches(1.9), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': answer_box_id, 'text': f"✓ {answer}"}},
        {'updateTextStyle': {'objectId': answer_box_id,
            'style': {'foregroundColor': {'opaqueColor': {'rgbColor': COLORS['answer_green']}},
                     'fontSize': {'magnitude': 36, 'unit': 'PT'}, 'bold': True, 'fontFamily': 'Arial'},
            'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,bold,fontFamily'}},
        {'updateParagraphStyle': {'objectId': answer_box_id, 
            'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
    ])
    
    # Snippet (italicized quote)
    if snippet:
        requests.extend([
            {'createShape': {'objectId': snippet_id, 'shapeType': 'TEXT_BOX',
                'elementProperties': {'pageObjectId': slide_id,
                    'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 
                            'height': {'magnitude': inches(0.8), 'unit': 'EMU'}},
                    'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 
                                 'translateY': inches(3.0), 'unit': 'EMU'}}}},
            {'insertText': {'objectId': snippet_id, 'text': f'"...{snippet}..."'}},
            {'updateTextStyle': {'objectId': snippet_id,
                'style': {'foregroundColor': {'opaqueColor': {'rgbColor': COLORS['dark_gray']}},
                         'fontSize': {'magnitude': 16, 'unit': 'PT'}, 'italic': True, 'fontFamily': 'Arial'},
                'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,italic,fontFamily'}},
            {'updateParagraphStyle': {'objectId': snippet_id, 
                'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
        ])
    
    # Explanation
    if explanation:
        y_pos = 3.9 if snippet else 3.0
        requests.extend([
            {'createShape': {'objectId': explain_id, 'shapeType': 'TEXT_BOX',
                'elementProperties': {'pageObjectId': slide_id,
                    'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 
                            'height': {'magnitude': inches(1.0), 'unit': 'EMU'}},
                    'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 
                                 'translateY': inches(y_pos), 'unit': 'EMU'}}}},
            {'insertText': {'objectId': explain_id, 'text': f"💡 {explanation}"}},
            {'updateTextStyle': {'objectId': explain_id,
                'style': {'foregroundColor': {'opaqueColor': {'rgbColor': COLORS['dark_gray']}},
                         'fontSize': {'magnitude': 18, 'unit': 'PT'}, 'fontFamily': 'Arial'},
                'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}},
        ])
    
    return requests


def get_activity_slide_requests(slide_id, title, content):
    """Activity slide with orange header."""
    requests = get_header_bar_requests(slide_id, title, COLORS['activity_orange'])
    requests.extend(get_body_text_requests(slide_id, content))
    return requests


def get_discussion_slide_requests(slide_id, title, content):
    """Discussion slide with purple header."""
    requests = get_header_bar_requests(slide_id, title, COLORS['discussion_purple'])
    requests.extend(get_body_text_requests(slide_id, content))
    return requests


def get_video_slide_requests(slide_id, title, video_url):
    """Video placeholder slide with red header and play button."""
    play_id = _generate_id()
    url_id = _generate_id()
    note_id = _generate_id()
    
    requests = get_header_bar_requests(slide_id, title, COLORS['video_red'])
    
    # Large play symbol
    requests.extend([
        {'createShape': {'objectId': play_id, 'shapeType': 'TEXT_BOX',
            'elementProperties': {'pageObjectId': slide_id,
                'size': {'width': {'magnitude': inches(3), 'unit': 'EMU'}, 
                        'height': {'magnitude': inches(2), 'unit': 'EMU'}},
                'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(3.5), 
                             'translateY': inches(1.5), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': play_id, 'text': '▶'}},
        {'updateTextStyle': {'objectId': play_id,
            'style': {'foregroundColor': {'opaqueColor': {'rgbColor': COLORS['video_red']}},
                     'fontSize': {'magnitude': 120, 'unit': 'PT'}, 'fontFamily': 'Arial'},
            'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily'}},
        {'updateParagraphStyle': {'objectId': play_id, 
            'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
    ])
    
    # Video URL
    requests.extend([
        {'createShape': {'objectId': url_id, 'shapeType': 'TEXT_BOX',
            'elementProperties': {'pageObjectId': slide_id,
                'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 
                        'height': {'magnitude': inches(0.5), 'unit': 'EMU'}},
                'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 
                             'translateY': inches(3.7), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': url_id, 'text': video_url}},
        {'updateTextStyle': {'objectId': url_id,
            'style': {'foregroundColor': {'opaqueColor': {'rgbColor': COLORS['dark_gray']}},
                     'fontSize': {'magnitude': 18, 'unit': 'PT'}, 'fontFamily': 'Arial',
                     'link': {'url': video_url}},
            'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,fontFamily,link'}},
        {'updateParagraphStyle': {'objectId': url_id, 
            'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
    ])
    
    # Note about manual insertion
    requests.extend([
        {'createShape': {'objectId': note_id, 'shapeType': 'TEXT_BOX',
            'elementProperties': {'pageObjectId': slide_id,
                'size': {'width': {'magnitude': inches(8), 'unit': 'EMU'}, 
                        'height': {'magnitude': inches(0.5), 'unit': 'EMU'}},
                'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': inches(1), 
                             'translateY': inches(4.3), 'unit': 'EMU'}}}},
        {'insertText': {'objectId': note_id, 'text': '(Insert video: Insert → Video → By URL)'}},
        {'updateTextStyle': {'objectId': note_id,
            'style': {'foregroundColor': {'opaqueColor': {'rgbColor': COLORS['dark_gray']}},
                     'fontSize': {'magnitude': 14, 'unit': 'PT'}, 'italic': True, 'fontFamily': 'Arial'},
            'textRange': {'type': 'ALL'}, 'fields': 'foregroundColor,fontSize,italic,fontFamily'}},
        {'updateParagraphStyle': {'objectId': note_id, 
            'style': {'alignment': 'CENTER'}, 'textRange': {'type': 'ALL'}, 'fields': 'alignment'}},
    ])
    
    return requests


def get_content_slide_requests(slide_id, title, content, header_color=None):
    """Generic content slide."""
    requests = get_header_bar_requests(slide_id, title, header_color)
    requests.extend(get_body_text_requests(slide_id, content))
    return requests


# ============================================================
# IMAGE UPLOAD
# ============================================================

def upload_image(drive_service, file_path):
    file_name = os.path.basename(file_path)
    mime_type = 'image/png' if file_path.endswith('.png') else 'image/jpeg'
    if file_path.endswith('.svg'):
        mime_type = 'image/svg+xml'
    
    media = MediaFileUpload(file_path, mimetype=mime_type)
    file = drive_service.files().create(body={'name': file_name}, media_body=media, fields='id').execute()
    file_id = file.get('id')
    
    drive_service.permissions().create(fileId=file_id, body={'type': 'anyone', 'role': 'reader'}).execute()
    
    print(f"  ✅ {file_name}")
    return f"https://lh3.googleusercontent.com/d/{file_id}"


# ============================================================
# MAIN
# ============================================================

def main():
    start_time = time.time()
    
    print("=" * 60)
    print("Creating Politeness Slideshow (THEMED + LAYOUTS)")
    print("=" * 60)
    
    slides_service = authenticate_slides()
    drive_service = authenticate_drive()
    print("✅ Authenticated")
    
    # Create presentation
    presentation = slides_service.presentations().create(
        body={'title': '27-12-25-Politeness-Reading-B1-THEMED'}
    ).execute()
    presentation_id = presentation.get('presentationId')
    print(f"✅ Created: {presentation_id}")
    
    default_slide = presentation.get('slides', [])[0]['objectId']
    
    # ============================================================
    # PHASE 1: Upload images
    # ============================================================
    print("\nPhase 1: Uploading images...")
    
    # Cache generated images
    generated_images = {}
    if os.path.exists(IMAGE_DIR):
        for f in os.listdir(IMAGE_DIR):
            if f.endswith('.png'):
                for prefix in ['cover_politeness', 'vocab_behavior', 'vocab_interrupt', 
                              'vocab_appropriate', 'vocab_offend', 'vocab_acceptable']:
                    if f.startswith(prefix):
                        generated_images[prefix] = os.path.join(IMAGE_DIR, f)
                        break
    
    # Upload all images
    image_urls = {}
    for key, path in generated_images.items():
        if os.path.exists(path):
            image_urls[key] = upload_image(drive_service, path)
    
    # Upload logos (use PNG for reliable rendering)
    bell_path = os.path.join(LOGO_DIR, 'Bell.png')
    act_path = os.path.join(LOGO_DIR, 'ACT.png')
    print(f"  Looking for logos in: {LOGO_DIR}")
    if os.path.exists(bell_path):
        image_urls['bell'] = upload_image(drive_service, bell_path)
    else:
        print(f"  ⚠️ Bell logo not found at {bell_path}")
    if os.path.exists(act_path):
        image_urls['act'] = upload_image(drive_service, act_path)
    else:
        print(f"  ⚠️ ACT logo not found at {act_path}")
    
    # ============================================================
    # PHASE 2: Build all requests
    # ============================================================
    print("\nPhase 2: Building requests...")
    
    all_requests = [{'deleteObject': {'objectId': default_slide}}]
    
    # --- SLIDE 1: Cover ---
    s1 = _generate_id()
    all_requests.extend(get_create_slide_requests(s1))
    all_requests.extend(get_cover_slide_requests(s1, "What does polite mean to you?",
        image_urls.get('cover_politeness'), image_urls.get('bell'), image_urls.get('act')))
    
    # --- SLIDE 2: Objective ---
    s2 = _generate_id()
    all_requests.extend(get_create_slide_requests(s2))
    all_requests.extend(get_content_slide_requests(s2, "Learning Objective",
        "By the end of this lesson, you will have practiced:\n\n" +
        "• Reading for gist\n• Reading for specific information\n• Reading for detail\n\n" +
        "in the context of an article about politeness."))
    
    # --- SLIDE 3: Lead-in ---
    s3 = _generate_id()
    all_requests.extend(get_create_slide_requests(s3))
    all_requests.extend(get_discussion_slide_requests(s3, "Lead-in: The Thai Wai",
        "🙏 In pairs, discuss:\n\n• What are the three levels of the Thai wai?\n" +
        "• What does each level mean?\n\nYou have 2 minutes."))
    
    # --- SLIDE 4: Video ---
    s4 = _generate_id()
    all_requests.extend(get_create_slide_requests(s4))
    all_requests.extend(get_video_slide_requests(s4, "Video: The Thai Wai",
        "https://youtube.com/shorts/jG9hxz9fZ0Y"))
    
    # --- SLIDES 5-9: Vocabulary ---
    vocab_items = [
        ("behavior", "/bɪˈheɪvjə/", "พฤติกรรม",
         "Good BEHAVIOR at school includes being polite.", "พฤติกรรมที่ดีในโรงเรียนรวมถึงการสุภาพต่อครู", 'vocab_behavior'),
        ("interrupt", "/ˌɪntəˈrʌpt/", "ขัดจังหวะ",
         "Please don't INTERRUPT me when I'm speaking.", "กรุณาอย่าขัดจังหวะฉันตอนที่ฉันกำลังพูด", 'vocab_interrupt'),
        ("appropriate", "/əˈprəʊpriət/", "เหมาะสม",
         "Smart clothes are APPROPRIATE for interviews.", "เสื้อผ้าสุภาพเป็นสิ่งที่เหมาะสมสำหรับการสัมภาษณ์", 'vocab_appropriate'),
        ("offend", "/əˈfend/", "ทำให้ขุ่นเคือง",
         "I didn't mean to OFFEND you.", "ฉันไม่ได้ตั้งใจจะทำให้คุณขุ่นเคือง", 'vocab_offend'),
        ("acceptable", "/əkˈseptəbl/", "ยอมรับได้",
         "Using phones at dinner is not ACCEPTABLE.", "การใช้โทรศัพท์ระหว่างอาหารไม่เป็นที่ยอมรับ", 'vocab_acceptable'),
    ]
    
    for word, phonemic, thai, eng, thai_sent, img_key in vocab_items:
        sid = _generate_id()
        all_requests.extend(get_create_slide_requests(sid))
        all_requests.extend(get_vocab_slide_requests(sid, word, phonemic, thai, eng, thai_sent, image_urls.get(img_key)))
    
    # --- SLIDE 10: Entry Ticket Intro ---
    s10 = _generate_id()
    all_requests.extend(get_create_slide_requests(s10))
    all_requests.extend(get_activity_slide_requests(s10, "Entry Ticket: Tools of the Trade",
        "Match each tool (1-5) to a person (A-E).\n\nNot all letters are used.\n\n" +
        "Read the text on your worksheet carefully.\n\nYou have 3 minutes."))
    
    # --- SLIDES 11-15: Entry Ticket Answers (Spotlight layout) ---
    entry_answers = [
        ("1. scalpel", "A (Anna)", "Surgeons use scalpels for operations.", "chief surgeon at the local hospital"),
        ("2. whisk", "No match", "Carlos is a manager, not a chef.", None),
        ("3. tripod", "E (Eric)", "Photographers use tripods.", "takes all our school photos"),
        ("4. guitar", "No match", "No one is a musician.", None),
        ("5. saw", "B (Ben)", "Carpenters use saws.", "builds beautiful wooden furniture"),
    ]
    
    for q, ans, expl, snippet in entry_answers:
        sid = _generate_id()
        all_requests.extend(get_create_slide_requests(sid))
        all_requests.extend(get_answer_slide_spotlight(sid, "Entry Ticket: Answer", q, ans, expl, snippet))
    
    # --- SLIDE 16: Before You Read ---
    s16 = _generate_id()
    all_requests.extend(get_create_slide_requests(s16))
    all_requests.extend(get_activity_slide_requests(s16, "Before You Read",
        "Rate these behaviors (10 = Very rude, 1 = Fine):\n\n" +
        "• Speaking on your phone on public transport\n• Interrupting someone\n" +
        "• Using your left hand to greet someone\n• Sending e-mails during a meeting\n\n" +
        "Compare with your partner. 2 minutes."))
    
    # --- SLIDES 17-19: Global Reading Answers ---
    global_answers = [
        ("Main idea A", "Paragraph 2", "Discusses polite phrases in language",
         "phrases are not really used for their actual meaning but as polite social phrases"),
        ("Main idea B", "Paragraph 4", "Technology's impact on politeness",
         "Cell phones have changed what is considered polite behavior"),
        ("Main idea C", "Paragraph 3", "Cultural differences in politeness",
         "different ways to show politeness across the world"),
    ]
    
    for q, ans, expl, snippet in global_answers:
        sid = _generate_id()
        all_requests.extend(get_create_slide_requests(sid))
        all_requests.extend(get_answer_slide_spotlight(sid, "Global Reading: Answer", q, ans, expl, snippet))
    
    # --- SLIDES 20-25: Close Reading Answers ---
    close_answers = [
        ("Gap 1", '"You\'re welcome"', "Older people's response", "Older people are more likely to say 'You're welcome'"),
        ("Gap 2", '"No problem"', "Younger people's response", "younger people are more likely to say 'No problem'"),
        ("Gap 3", "tipping", "Varies by country", "tipping... is polite in the U.S.A. However, in Japan tipping is not expected"),
        ("Gap 4", "left hand", "Considered unclean in India", "the left hand is considered unclean"),
        ("Gap 5", "having your phone", "Rude at the dinner table", "having your phone at the dinner table is thought to be impolite"),
        ("Gap 6", "older people", "More likely to find it rude", "older people are much more likely to have a negative reaction"),
    ]
    
    for q, ans, expl, snippet in close_answers:
        sid = _generate_id()
        all_requests.extend(get_create_slide_requests(sid))
        all_requests.extend(get_answer_slide_spotlight(sid, "Close Reading: Answer", q, ans, expl, snippet))
    
    # --- SLIDES 26-27: Discussion ---
    s26 = _generate_id()
    all_requests.extend(get_create_slide_requests(s26))
    all_requests.extend(get_discussion_slide_requests(s26, "Discussion Question 1",
        "What behavior do you find rude in other people?\n\n" +
        "Do you think other people would find any of YOUR behavior rude?\n\n" +
        'Useful language:\n• "I really dislike it when..."\n• "It annoys me when people..."'))
    
    s27 = _generate_id()
    all_requests.extend(get_create_slide_requests(s27))
    all_requests.extend(get_discussion_slide_requests(s27, "Discussion Question 2",
        "Do you think younger people are less polite than older people?\n\nWhy / why not?\n\n" +
        'Useful language:\n• "I do think so because..."\n• "I don\'t think so because..."'))
    
    # --- SLIDE 28: Key Takeaway ---
    s28 = _generate_id()
    all_requests.extend(get_create_slide_requests(s28))
    all_requests.extend(get_content_slide_requests(s28, "Key Takeaway",
        "Politeness is cultural.\n\nWhat's polite in one culture may not be in another.\n\n" +
        "What's acceptable to one generation may not be to another.", COLORS['maroon']))
    
    # ============================================================
    # PHASE 3: Execute batch
    # ============================================================
    print(f"\nPhase 3: Sending batch ({len(all_requests)} requests)...")
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': all_requests}
    ).execute()
    
    print("✅ All slides created!")
    
    # Move to folder
    try:
        file = drive_service.files().get(fileId=presentation_id, fields='parents').execute()
        previous_parents = ",".join(file.get('parents', []))
        drive_service.files().update(
            fileId=presentation_id, addParents=TARGET_FOLDER_ID, removeParents=previous_parents
        ).execute()
        print("✅ Moved to target folder")
    except Exception as e:
        print(f"⚠️ Could not move: {e}")
    
    elapsed = time.time() - start_time
    url = f"https://docs.google.com/presentation/d/{presentation_id}/edit"
    
    print("\n" + "=" * 60)
    print(f"🎉 Themed slideshow created in {elapsed:.1f}s!")
    print(f"URL: {url}")
    print("=" * 60)
    
    return presentation_id, url


if __name__ == '__main__':
    main()
