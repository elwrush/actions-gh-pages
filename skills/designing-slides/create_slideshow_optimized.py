"""
Create Politeness Lesson Slideshow (Optimized)

OPTIMIZED VERSION: Uses batch API operations for efficiency.
- Single batchUpdate call instead of 100+ individual requests
- No artificial time.sleep() delays
- Cached filesystem reads
- Relative paths

Generates a complete Google Slides presentation for the B1 Intensive Reading lesson
on "What does polite mean to you?"
"""

import os
import sys
import time
import uuid

# Use relative paths from script location
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

# Brand colors
BRAND_COLORS = {
    'maroon': {'red': 166/255, 'green': 45/255, 'blue': 38/255},
    'white': {'red': 1.0, 'green': 1.0, 'blue': 1.0},
    'dark_gray': {'red': 0.2, 'green': 0.2, 'blue': 0.2},
}

# Configuration (relative paths)
TARGET_FOLDER_ID = "1_n11w9BRN6sd0uaXlqEXjqZuZ74zFiOl"
IMAGE_DIR = os.path.join(os.path.expanduser("~"), ".gemini", "antigravity", "brain", 
                         "6676dadb-d43e-4e5c-9dff-ed498947bb8c")
LOCAL_IMAGE_DIR = os.path.join(PROJECT_ROOT, "inputs", "Intensive-Reading-Politeness")


# ============================================================
# REQUEST BUILDER FUNCTIONS (Return requests, don't execute)
# ============================================================

def get_create_slide_requests(slide_id):
    """Returns request to create a blank slide."""
    return [{
        'createSlide': {
            'objectId': slide_id,
            'slideLayoutReference': {'predefinedLayout': 'BLANK'}
        }
    }]


def get_header_bar_requests(slide_id, title):
    """Returns requests to create AND style a header bar with title."""
    header_id = _generate_id()
    title_id = _generate_id()
    
    return [
        # Create header rectangle
        {
            'createShape': {
                'objectId': header_id,
                'shapeType': 'RECTANGLE',
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {
                        'width': {'magnitude': SLIDE_WIDTH, 'unit': 'EMU'},
                        'height': {'magnitude': inches(1), 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': 0, 'translateY': 0,
                        'unit': 'EMU'
                    }
                }
            }
        },
        # Create title text box
        {
            'createShape': {
                'objectId': title_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {
                        'width': {'magnitude': inches(9), 'unit': 'EMU'},
                        'height': {'magnitude': inches(0.8), 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': inches(0.5),
                        'translateY': inches(0.1),
                        'unit': 'EMU'
                    }
                }
            }
        },
        {'insertText': {'objectId': title_id, 'text': title}},
        # Style header (maroon fill)
        {
            'updateShapeProperties': {
                'objectId': header_id,
                'shapeProperties': {
                    'shapeBackgroundFill': {
                        'solidFill': {'color': {'rgbColor': BRAND_COLORS['maroon']}}
                    },
                    'outline': {'propertyState': 'NOT_RENDERED'}
                },
                'fields': 'shapeBackgroundFill.solidFill.color,outline'
            }
        },
        # Style title text (white, bold)
        {
            'updateTextStyle': {
                'objectId': title_id,
                'style': {
                    'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}},
                    'fontSize': {'magnitude': 32, 'unit': 'PT'},
                    'bold': True,
                    'fontFamily': 'Arial'
                },
                'textRange': {'type': 'ALL'},
                'fields': 'foregroundColor,fontSize,bold,fontFamily'
            }
        }
    ]


def get_body_text_requests(slide_id, text, y_offset=1.2, font_size=24):
    """Returns requests to create AND style body text."""
    body_id = _generate_id()
    
    return [
        {
            'createShape': {
                'objectId': body_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {
                        'width': {'magnitude': inches(9), 'unit': 'EMU'},
                        'height': {'magnitude': inches(4), 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': inches(0.5),
                        'translateY': inches(y_offset),
                        'unit': 'EMU'
                    }
                }
            }
        },
        {'insertText': {'objectId': body_id, 'text': text}},
        {
            'updateTextStyle': {
                'objectId': body_id,
                'style': {
                    'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['dark_gray']}},
                    'fontSize': {'magnitude': font_size, 'unit': 'PT'},
                    'fontFamily': 'Arial'
                },
                'textRange': {'type': 'ALL'},
                'fields': 'foregroundColor,fontSize,fontFamily'
            }
        }
    ]


def get_image_requests(slide_id, image_url, x, y, width, height):
    """Returns request to insert an image."""
    image_id = _generate_id()
    return [{
        'createImage': {
            'objectId': image_id,
            'url': image_url,
            'elementProperties': {
                'pageObjectId': slide_id,
                'size': {
                    'width': {'magnitude': width, 'unit': 'EMU'},
                    'height': {'magnitude': height, 'unit': 'EMU'}
                },
                'transform': {
                    'scaleX': 1, 'scaleY': 1,
                    'translateX': x,
                    'translateY': y,
                    'unit': 'EMU'
                }
            }
        }
    }]


def get_title_slide_requests(slide_id, title, image_url=None):
    """Returns all requests for a maroon title slide."""
    title_text_id = _generate_id()
    subtitle_id = _generate_id()
    
    requests = [
        # Set maroon background
        {
            'updatePageProperties': {
                'objectId': slide_id,
                'pageProperties': {
                    'pageBackgroundFill': {
                        'solidFill': {'color': {'rgbColor': BRAND_COLORS['maroon']}}
                    }
                },
                'fields': 'pageBackgroundFill.solidFill.color'
            }
        },
        # Title text box
        {
            'createShape': {
                'objectId': title_text_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {
                        'width': {'magnitude': inches(9), 'unit': 'EMU'},
                        'height': {'magnitude': inches(1.5), 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': inches(0.5),
                        'translateY': inches(1.5),
                        'unit': 'EMU'
                    }
                }
            }
        },
        {'insertText': {'objectId': title_text_id, 'text': title}},
        # Subtitle
        {
            'createShape': {
                'objectId': subtitle_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {
                        'width': {'magnitude': inches(9), 'unit': 'EMU'},
                        'height': {'magnitude': inches(0.5), 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': inches(0.5),
                        'translateY': inches(3.2),
                        'unit': 'EMU'
                    }
                }
            }
        },
        {'insertText': {'objectId': subtitle_id, 'text': 'Bell Language Centre - B1 Reading'}},
        # Style title
        {
            'updateTextStyle': {
                'objectId': title_text_id,
                'style': {
                    'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}},
                    'fontSize': {'magnitude': 44, 'unit': 'PT'},
                    'bold': True,
                    'fontFamily': 'Arial'
                },
                'textRange': {'type': 'ALL'},
                'fields': 'foregroundColor,fontSize,bold,fontFamily'
            }
        },
        {
            'updateParagraphStyle': {
                'objectId': title_text_id,
                'style': {'alignment': 'CENTER'},
                'textRange': {'type': 'ALL'},
                'fields': 'alignment'
            }
        },
        # Style subtitle
        {
            'updateTextStyle': {
                'objectId': subtitle_id,
                'style': {
                    'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}},
                    'fontSize': {'magnitude': 24, 'unit': 'PT'},
                    'fontFamily': 'Arial'
                },
                'textRange': {'type': 'ALL'},
                'fields': 'foregroundColor,fontSize,fontFamily'
            }
        },
        {
            'updateParagraphStyle': {
                'objectId': subtitle_id,
                'style': {'alignment': 'CENTER'},
                'textRange': {'type': 'ALL'},
                'fields': 'alignment'
            }
        }
    ]
    
    # Add cover image if provided
    if image_url:
        requests.extend(get_image_requests(slide_id, image_url, 
                                          inches(3.5), inches(4), inches(3), inches(2.2)))
    
    return requests


def get_content_slide_requests(slide_id, title, content):
    """Returns all requests for a content slide with header and body."""
    requests = []
    requests.extend(get_header_bar_requests(slide_id, title))
    requests.extend(get_body_text_requests(slide_id, content))
    return requests


def get_vocab_slide_requests(slide_id, word, phonemic, thai, eng_sentence, thai_sentence, image_url=None):
    """Returns all requests for a vocabulary slide."""
    vocab_text = f"{word} {phonemic}: {thai}\n\n{eng_sentence}\n\n{thai_sentence}"
    
    requests = []
    requests.extend(get_header_bar_requests(slide_id, "Vocabulary"))
    
    if image_url:
        # Left side text (narrower)
        body_id = _generate_id()
        requests.extend([
            {
                'createShape': {
                    'objectId': body_id,
                    'shapeType': 'TEXT_BOX',
                    'elementProperties': {
                        'pageObjectId': slide_id,
                        'size': {
                            'width': {'magnitude': inches(5.5), 'unit': 'EMU'},
                            'height': {'magnitude': inches(4), 'unit': 'EMU'}
                        },
                        'transform': {
                            'scaleX': 1, 'scaleY': 1,
                            'translateX': inches(0.5),
                            'translateY': inches(1.2),
                            'unit': 'EMU'
                        }
                    }
                }
            },
            {'insertText': {'objectId': body_id, 'text': vocab_text}},
            {
                'updateTextStyle': {
                    'objectId': body_id,
                    'style': {
                        'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['dark_gray']}},
                        'fontSize': {'magnitude': 22, 'unit': 'PT'},
                        'fontFamily': 'Arial'
                    },
                    'textRange': {'type': 'ALL'},
                    'fields': 'foregroundColor,fontSize,fontFamily'
                }
            }
        ])
        # Right side image
        requests.extend(get_image_requests(slide_id, image_url, 
                                          inches(6.2), inches(1.5), inches(3.3), inches(3.3)))
    else:
        requests.extend(get_body_text_requests(slide_id, vocab_text, font_size=22))
    
    return requests


def get_answer_slide_requests(slide_id, section_title, question, answer, explanation, snippet=None):
    """Returns all requests for an answer slide."""
    content = f"{question}\n\n✓ Answer: {answer}\n\n"
    if explanation:
        content += f"{explanation}\n\n"
    if snippet:
        content += f"\"...{snippet}...\""
    
    return get_content_slide_requests(slide_id, section_title, content)


# ============================================================
# IMAGE UPLOAD FUNCTIONS (Still need individual calls)
# ============================================================

def upload_image(drive_service, file_path):
    """Upload image to Drive and make public."""
    file_name = os.path.basename(file_path)
    mime_type = 'image/png' if file_path.endswith('.png') else 'image/jpeg'
    
    media = MediaFileUpload(file_path, mimetype=mime_type)
    file = drive_service.files().create(
        body={'name': file_name},
        media_body=media,
        fields='id'
    ).execute()
    
    file_id = file.get('id')
    
    drive_service.permissions().create(
        fileId=file_id,
        body={'type': 'anyone', 'role': 'reader'}
    ).execute()
    
    print(f"  ✅ {file_name}")
    return f"https://lh3.googleusercontent.com/d/{file_id}"


def batch_upload_images(drive_service, image_map):
    """Upload all images and return URL map."""
    urls = {}
    for key, path in image_map.items():
        if os.path.exists(path):
            urls[key] = upload_image(drive_service, path)
    return urls


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():
    start_time = time.time()
    
    print("=" * 60)
    print("Creating Politeness Lesson Slideshow (OPTIMIZED)")
    print("=" * 60)
    
    # Authenticate
    slides_service = authenticate_slides()
    drive_service = authenticate_drive()
    print("✅ Authenticated")
    
    # Create presentation
    presentation = slides_service.presentations().create(
        body={'title': '27-12-25-Politeness-Reading-B1-Slideshow-v2'}
    ).execute()
    presentation_id = presentation.get('presentationId')
    print(f"✅ Created presentation: {presentation_id}")
    
    # Delete default slide
    default_slide = presentation.get('slides', [])[0]['objectId']
    
    # ============================================================
    # PHASE 1: Upload images (these must be separate calls)
    # ============================================================
    print("\nPhase 1: Uploading images...")
    
    # Cache directory listing ONCE
    generated_images = {}
    if os.path.exists(IMAGE_DIR):
        for f in os.listdir(IMAGE_DIR):
            if f.endswith('.png'):
                for prefix in ['cover_politeness', 'thai_wai_greeting', 'vocab_behavior', 
                              'vocab_interrupt', 'vocab_appropriate', 'vocab_offend', 'vocab_acceptable']:
                    if f.startswith(prefix):
                        generated_images[prefix] = os.path.join(IMAGE_DIR, f)
                        break
    
    # Add local images
    image_map = {}
    politeness_path = os.path.join(LOCAL_IMAGE_DIR, "politeness_cross_cultural.png")
    if os.path.exists(politeness_path):
        image_map['politeness'] = politeness_path
    image_map.update(generated_images)
    
    # Upload all
    image_urls = batch_upload_images(drive_service, image_map)
    
    # ============================================================
    # PHASE 2: Build ALL requests (no API calls yet!)
    # ============================================================
    print("\nPhase 2: Building slide requests...")
    
    all_requests = []
    
    # Delete default slide
    all_requests.append({'deleteObject': {'objectId': default_slide}})
    
    # --- Slide 1: Title ---
    slide1 = _generate_id()
    all_requests.extend(get_create_slide_requests(slide1))
    all_requests.extend(get_title_slide_requests(slide1, "What does polite mean to you?",
                                                  image_urls.get('cover_politeness') or image_urls.get('politeness')))
    
    # --- Slide 2: Learning Objective ---
    slide2 = _generate_id()
    all_requests.extend(get_create_slide_requests(slide2))
    all_requests.extend(get_content_slide_requests(slide2, "Learning Objective",
        "By the end of this lesson, you will have practiced:\n\n" +
        "• Reading for gist\n• Reading for specific information\n• Reading for detail\n\n" +
        "in the context of an article about politeness across cultures and generations."))
    
    # --- Slide 3: Lead-in ---
    slide3 = _generate_id()
    all_requests.extend(get_create_slide_requests(slide3))
    all_requests.extend(get_content_slide_requests(slide3, "Lead-in: The Thai Wai",
        "🙏 Discussion:\n\nIn pairs, discuss:\n• What are the three levels of the Thai wai?\n" +
        "• What does each level mean?\n\nYou have 2 minutes."))
    
    # --- Slide 4: Video ---
    slide4 = _generate_id()
    all_requests.extend(get_create_slide_requests(slide4))
    all_requests.extend(get_content_slide_requests(slide4, "Video: The Thai Wai",
        "📺 Watch the video:\n\nyoutube.com/shorts/jG9hxz9fZ0Y\n\nWere you correct about the three levels?"))
    
    # --- Slides 5-9: Vocabulary ---
    vocab_items = [
        ("behavior", "/bɪˈheɪvjə/", "พฤติกรรม",
         "Good BEHAVIOR at school includes being polite to teachers.",
         "พฤติกรรมที่ดีในโรงเรียนรวมถึงการสุภาพต่อครู", 'vocab_behavior'),
        ("interrupt", "/ˌɪntəˈrʌpt/", "ขัดจังหวะ",
         "Please don't INTERRUPT me when I'm speaking.",
         "กรุณาอย่าขัดจังหวะฉันตอนที่ฉันกำลังพูด", 'vocab_interrupt'),
        ("appropriate", "/əˈprəʊpriət/", "เหมาะสม",
         "Smart clothes are APPROPRIATE for a job interview.",
         "เสื้อผ้าสุภาพเป็นสิ่งที่เหมาะสมสำหรับการสัมภาษณ์งาน", 'vocab_appropriate'),
        ("offend", "/əˈfend/", "ทำให้ขุ่นเคือง",
         "I didn't mean to OFFEND you with my comment.",
         "ฉันไม่ได้ตั้งใจจะทำให้คุณขุ่นเคืองด้วยความเห็นของฉัน", 'vocab_offend'),
        ("acceptable", "/əkˈseptəbl/", "ยอมรับได้",
         "Using your phone during dinner is not ACCEPTABLE in some families.",
         "การใช้โทรศัพท์ระหว่างอาหารเย็นไม่เป็นที่ยอมรับในบางครอบครัว", 'vocab_acceptable'),
    ]
    
    for word, phonemic, thai, eng, thai_sent, img_key in vocab_items:
        slide_id = _generate_id()
        all_requests.extend(get_create_slide_requests(slide_id))
        all_requests.extend(get_vocab_slide_requests(slide_id, word, phonemic, thai, 
                                                     eng, thai_sent, image_urls.get(img_key)))
    
    # --- Slide 10: Entry Ticket Intro ---
    slide10 = _generate_id()
    all_requests.extend(get_create_slide_requests(slide10))
    all_requests.extend(get_content_slide_requests(slide10, "Entry Ticket: Tools of the Trade",
        "Match each tool (1-5) to a person (A-E).\n\nNot all letters are used.\n\n" +
        "Read the text on your worksheet carefully.\n\nYou have 3 minutes."))
    
    # --- Slides 11-15: Entry Ticket Answers ---
    entry_answers = [
        ("1. scalpel", "A (Anna)", "Anna is 'chief surgeon at the local hospital.' Surgeons use scalpels."),
        ("2. whisk", "No match (distractor)", "Carlos runs the restaurant, but he's a manager, not a chef."),
        ("3. tripod", "E (Eric)", "Eric 'takes all our school photos.' Photographers use tripods."),
        ("4. guitar", "No match (distractor)", "No one in the passage is a musician."),
        ("5. saw", "B (Ben)", "Ben 'builds beautiful wooden furniture.' Carpenters use saws."),
    ]
    
    for q, ans, expl in entry_answers:
        slide_id = _generate_id()
        all_requests.extend(get_create_slide_requests(slide_id))
        all_requests.extend(get_answer_slide_requests(slide_id, "Entry Ticket: Answer", q, ans, expl))
    
    # --- Slide 16: Before You Read ---
    slide16 = _generate_id()
    all_requests.extend(get_create_slide_requests(slide16))
    all_requests.extend(get_content_slide_requests(slide16, "Before You Read",
        "Rate these behaviors:\n(10 = Very rude, 1 = It's fine)\n\n" +
        "• Speaking on your phone on public transportation\n" +
        "• Interrupting someone\n• Using your left hand to greet someone\n" +
        "• Sending e-mails during a meeting\n\nCompare with your partner. 2 minutes."))
    
    # --- Slides 17-19: Global Reading Answers ---
    global_answers = [
        ("A", "Paragraph 2", "Para 2 discusses polite phrases",
         "Some phrases are not really used for their actual meaning but as polite social phrases"),
        ("B", "Paragraph 4", "Para 4 is about technology's impact",
         "Cell phones have changed what is considered polite behavior"),
        ("C", "Paragraph 3", "Para 3 gives cultural examples",
         "From tipping, to smiling... there are different ways to show politeness across the world"),
    ]
    
    for main_idea, ans, expl, snippet in global_answers:
        slide_id = _generate_id()
        all_requests.extend(get_create_slide_requests(slide_id))
        all_requests.extend(get_answer_slide_requests(slide_id, "Global Reading: Answer",
                                                      f"Main idea {main_idea}", ans, expl, snippet))
    
    # --- Slides 20-25: Close Reading Answers ---
    close_answers = [
        ("Gap 1", '"You\'re welcome"', "Response older people use",
         "Older people are more likely to say 'You're welcome'"),
        ("Gap 2", '"No problem"', "Response younger people use",
         "younger people are more likely to say 'No problem'"),
        ("Gap 3", "tipping", "A custom that varies between countries",
         "tipping... is polite in the U.S.A. However, in Japan tipping is not expected"),
        ("Gap 4", "left hand", "Considered unclean in India",
         "the left hand is considered unclean"),
        ("Gap 5", "having your phone", "Rude at the dinner table",
         "even just having your phone at the dinner table is thought to be impolite"),
        ("Gap 6", "older people", "More likely to find e-mailing rude",
         "older people are much more likely to have a negative reaction"),
    ]
    
    for q, ans, expl, snippet in close_answers:
        slide_id = _generate_id()
        all_requests.extend(get_create_slide_requests(slide_id))
        all_requests.extend(get_answer_slide_requests(slide_id, "Close Reading: Answer", q, ans, expl, snippet))
    
    # --- Slides 26-27: Discussion ---
    slide26 = _generate_id()
    all_requests.extend(get_create_slide_requests(slide26))
    all_requests.extend(get_content_slide_requests(slide26, "Discussion Question 1",
        "What behavior do you find rude in other people?\n\n" +
        "Do you think other people would find any of your behavior rude?\n\n" +
        "Useful language:\n• \"I really dislike it when...\"\n• \"It annoys me when people...\""))
    
    slide27 = _generate_id()
    all_requests.extend(get_create_slide_requests(slide27))
    all_requests.extend(get_content_slide_requests(slide27, "Discussion Question 2",
        "Do you think younger people are less polite than older people?\n\nWhy / why not?\n\n" +
        "Useful language:\n• \"I do think so because...\"\n• \"I don't think so because...\""))
    
    # --- Slide 28: Key Takeaway ---
    slide28 = _generate_id()
    all_requests.extend(get_create_slide_requests(slide28))
    all_requests.extend(get_content_slide_requests(slide28, "Key Takeaway",
        "Politeness is cultural.\n\nWhat's polite in one culture may not be in another.\n\n" +
        "What's acceptable to one generation may not be to another."))
    
    # ============================================================
    # PHASE 3: Execute SINGLE batch update
    # ============================================================
    print(f"\nPhase 3: Sending batch update with {len(all_requests)} requests...")
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': all_requests}
    ).execute()
    
    print("✅ All slides created!")
    
    # ============================================================
    # PHASE 4: Move to target folder
    # ============================================================
    try:
        file = drive_service.files().get(fileId=presentation_id, fields='parents').execute()
        previous_parents = ",".join(file.get('parents', []))
        drive_service.files().update(
            fileId=presentation_id,
            addParents=TARGET_FOLDER_ID,
            removeParents=previous_parents
        ).execute()
        print("✅ Moved to target folder")
    except Exception as e:
        print(f"⚠️ Could not move to folder: {e}")
    
    # Done!
    elapsed = time.time() - start_time
    url = f"https://docs.google.com/presentation/d/{presentation_id}/edit"
    
    print("\n" + "=" * 60)
    print(f"🎉 Slideshow created in {elapsed:.1f} seconds!")
    print(f"URL: {url}")
    print("=" * 60)
    
    return presentation_id, url


if __name__ == '__main__':
    main()
