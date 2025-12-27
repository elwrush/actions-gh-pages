"""
Create Politeness Lesson Slideshow

Generates a complete Google Slides presentation for the B1 Intensive Reading lesson
on "What does polite mean to you?"

Slides include:
- Title slide
- Lead-in (Thai Wai)
- Vocabulary (5 slides with images)
- Entry Ticket answers (5 slides)
- Global Reading answers (3 slides)
- Close Reading answers (6 slides)
- Discussion prompts (2 slides)
"""

import os
import sys
import time

# Change to project root directory
PROJECT_ROOT = r"C:\PROJECTS\LESSONS AND SLIDESHOWS 2"
os.chdir(PROJECT_ROOT)

# Add parent paths for imports
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'skills', 'designing-slides'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'skills', 'designing-slides', 'scripts'))

from googleapiclient.http import MediaFileUpload
from scripts.authenticate_google import authenticate_slides, authenticate_drive
from scripts.add_slide_content import add_slide, add_text_box, add_image_from_url, inches, _generate_id
from scripts.format_slides import SLIDE_WIDTH, SLIDE_HEIGHT

# Brand colors

BRAND_COLORS = {
    'maroon': {'red': 166/255, 'green': 45/255, 'blue': 38/255},
    'white': {'red': 1.0, 'green': 1.0, 'blue': 1.0},
    'dark_gray': {'red': 0.2, 'green': 0.2, 'blue': 0.2},
    'light_maroon': {'red': 203/255, 'green': 92/255, 'blue': 85/255},
}

# Target folder from lesson-plan-GD-target.md
TARGET_FOLDER_ID = "1_n11w9BRN6sd0uaXlqEXjqZuZ74zFiOl"

# Template ID
TEMPLATE_ID = "1AdeFwA9zFkJMmkwB7c74pO88KPuJypgZRDM73haL8iw"

# Image paths (generated images)
IMAGE_DIR = r"C:\Users\elwru\.gemini\antigravity\brain\6676dadb-d43e-4e5c-9dff-ed498947bb8c"
LOCAL_IMAGE_DIR = r"C:\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\Intensive-Reading-Politeness"


def upload_image(drive_service, file_path):
    """Upload image to Drive and make public."""
    file_name = os.path.basename(file_path)
    
    # Determine mime type
    if file_path.endswith('.png'):
        mime_type = 'image/png'
    elif file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
        mime_type = 'image/jpeg'
    else:
        mime_type = 'image/png'
    
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
    
    time.sleep(1)  # Rate limiting
    print(f"✅ Uploaded {file_name}")
    return f"https://lh3.googleusercontent.com/d/{file_id}"


def create_blank_slide(slides_service, presentation_id):
    """Create a blank slide and return its ID."""
    slide_id = _generate_id()
    
    requests = [{
        'createSlide': {
            'objectId': slide_id,
            'slideLayoutReference': {'predefinedLayout': 'BLANK'}
        }
    }]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    time.sleep(1)  # Rate limiting
    return slide_id


def add_header_bar(slides_service, presentation_id, slide_id, title):
    """Add maroon header bar with white title text."""
    header_id = _generate_id()
    title_id = _generate_id()
    
    requests = [
        # Header bar
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
        # Title text
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
        {'insertText': {'objectId': title_id, 'text': title}}
    ]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    time.sleep(1)  # Rate limiting
    
    # Style header and title
    requests = [
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
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    time.sleep(1)  # Rate limiting
    return header_id, title_id



def add_body_text(slides_service, presentation_id, slide_id, text, y_offset=1.2, font_size=24):
    """Add body text to a slide."""
    body_id = _generate_id()
    
    requests = [
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
        {'insertText': {'objectId': body_id, 'text': text}}
    ]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    # Style text
    requests = [{
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
    }]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    time.sleep(1)  # Rate limiting
    return body_id


def create_vocab_slide(slides_service, presentation_id, word, phonemic, thai, 
                       eng_sentence, thai_sentence, image_url=None):
    """Create a vocabulary slide with mandated pattern."""
    slide_id = create_blank_slide(slides_service, presentation_id)
    add_header_bar(slides_service, presentation_id, slide_id, "Vocabulary")
    
    # Format vocabulary content
    vocab_text = f"{word} {phonemic}: {thai}\n\n{eng_sentence}\n\n{thai_sentence}"
    
    if image_url:
        # Text on left, image on right
        body_id = _generate_id()
        requests = [
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
            {'insertText': {'objectId': body_id, 'text': vocab_text}}
        ]
        
        slides_service.presentations().batchUpdate(
            presentationId=presentation_id,
            body={'requests': requests}
        ).execute()
        
        # Style text
        requests = [{
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
        }]
        
        slides_service.presentations().batchUpdate(
            presentationId=presentation_id,
            body={'requests': requests}
        ).execute()
        
        # Add image
        try:
            add_image_from_url(slides_service, presentation_id, slide_id, 
                             image_url, inches(6.2), inches(1.5), inches(3.3), inches(3.3))
        except Exception as e:
            print(f"⚠️ Could not add image: {e}")
    else:
        add_body_text(slides_service, presentation_id, slide_id, vocab_text, font_size=22)
    
    print(f"✅ Created vocab slide: {word}")
    return slide_id


def create_answer_slide(slides_service, presentation_id, section_title, 
                        question, answer, explanation, snippet=None):
    """Create an answer slide with explanation and optional snippet."""
    slide_id = create_blank_slide(slides_service, presentation_id)
    add_header_bar(slides_service, presentation_id, slide_id, section_title)
    
    # Build content
    content = f"{question}\n\n"
    content += f"✓ Answer: {answer}\n\n"
    if explanation:
        content += f"{explanation}\n\n"
    if snippet:
        content += f"\"...{snippet}...\""
    
    add_body_text(slides_service, presentation_id, slide_id, content, font_size=22)
    
    print(f"✅ Created answer slide: {answer}")
    return slide_id


def create_content_slide(slides_service, presentation_id, title, content):
    """Create a simple content slide."""
    slide_id = create_blank_slide(slides_service, presentation_id)
    add_header_bar(slides_service, presentation_id, slide_id, title)
    add_body_text(slides_service, presentation_id, slide_id, content)
    print(f"✅ Created slide: {title}")
    return slide_id


def create_title_slide(slides_service, presentation_id, title, image_url=None):
    """Create maroon title slide with centered title."""
    slide_id = create_blank_slide(slides_service, presentation_id)
    
    # Set maroon background
    requests = [{
        'updatePageProperties': {
            'objectId': slide_id,
            'pageProperties': {
                'pageBackgroundFill': {
                    'solidFill': {'color': {'rgbColor': BRAND_COLORS['maroon']}}
                }
            },
            'fields': 'pageBackgroundFill.solidFill.color'
        }
    }]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    # Add title
    title_id = _generate_id()
    subtitle_id = _generate_id()
    
    requests = [
        {
            'createShape': {
                'objectId': title_id,
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
        {'insertText': {'objectId': title_id, 'text': title}},
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
        {'insertText': {'objectId': subtitle_id, 'text': 'Bell Language Centre - B1 Reading'}}
    ]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    # Style title and subtitle
    requests = [
        {
            'updateTextStyle': {
                'objectId': title_id,
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
                'objectId': title_id,
                'style': {'alignment': 'CENTER'},
                'textRange': {'type': 'ALL'},
                'fields': 'alignment'
            }
        },
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
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    time.sleep(1)  # Rate limiting
    
    # Add image if provided
    if image_url:
        try:
            add_image_from_url(slides_service, presentation_id, slide_id,
                             image_url, inches(3.5), inches(4), inches(3), inches(2.2))
            time.sleep(1) # Rate limiting
        except Exception as e:
            print(f"⚠️ Could not add title image: {e}")
    
    print(f"✅ Created title slide")
    return slide_id


def main():
    print("=" * 60)
    print("Creating Politeness Lesson Slideshow")
    print("=" * 60)
    
    # Authenticate
    slides_service = authenticate_slides()
    drive_service = authenticate_drive()
    print("✅ Authenticated")
    
    # Create new presentation
    presentation = slides_service.presentations().create(
        body={'title': '27-12-25-Politeness-Reading-B1-Slideshow'}
    ).execute()
    presentation_id = presentation.get('presentationId')
    print(f"✅ Created presentation: {presentation_id}")
    
    # Delete default slide
    default_slide = presentation.get('slides', [])[0]['objectId']
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': [{'deleteObject': {'objectId': default_slide}}]}
    ).execute()
    
    # Upload images
    print("\nUploading images...")
    images = {}
    
    # Local images
    politeness_img = os.path.join(LOCAL_IMAGE_DIR, "politeness_cross_cultural.png")
    if os.path.exists(politeness_img):
        images['politeness'] = upload_image(drive_service, politeness_img)
    
    # Generated images
    for img_name in ['cover_politeness', 'thai_wai_greeting', 'vocab_behavior', 'vocab_interrupt', 
                     'vocab_appropriate', 'vocab_offend', 'vocab_acceptable']:
        for f in os.listdir(IMAGE_DIR):
            if f.startswith(img_name) and f.endswith('.png'):
                images[img_name] = upload_image(drive_service, os.path.join(IMAGE_DIR, f))
                break
    
    time.sleep(2)  # Let Drive propagate
    
    # ========== CREATE SLIDES ==========
    print("\n" + "=" * 60)
    print("Creating slides...")
    print("=" * 60)
    
    # 1. TITLE SLIDE
    create_title_slide(slides_service, presentation_id, 
                      "What does polite mean to you?",
                      images.get('cover_politeness') or images.get('politeness'))
    
    # 2. LEARNING OBJECTIVE
    create_content_slide(slides_service, presentation_id, "Learning Objective",
        "By the end of this lesson, you will have practiced:\n\n" +
        "• Reading for gist\n" +
        "• Reading for specific information\n" +
        "• Reading for detail\n\n" +
        "in the context of an article about politeness across cultures and generations.")
    
    # 3. LEAD-IN: THAI WAI
    create_content_slide(slides_service, presentation_id, "Lead-in: The Thai Wai",
        "🙏 Discussion:\n\n" +
        "In pairs, discuss:\n" +
        "• What are the three levels of the Thai wai?\n" +
        "• What does each level mean?\n\n" +
        "You have 2 minutes.")
    
    # 4. THAI WAI VIDEO
    create_content_slide(slides_service, presentation_id, "Video: The Thai Wai",
        "📺 Watch the video:\n\n" +
        "youtube.com/shorts/jG9hxz9fZ0Y\n\n" +
        "Were you correct about the three levels?")
    
    # 5-9. VOCABULARY SLIDES
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
        create_vocab_slide(slides_service, presentation_id, word, phonemic, thai,
                          eng, thai_sent, images.get(img_key))
    
    # 10. ENTRY TICKET INTRO
    create_content_slide(slides_service, presentation_id, "Entry Ticket: Tools of the Trade",
        "Match each tool (1-5) to a person (A-E).\n\n" +
        "Not all letters are used.\n\n" +
        "Read the text on your worksheet carefully.\n\n" +
        "You have 3 minutes.")
    
    # 11-15. ENTRY TICKET ANSWERS
    entry_answers = [
        ("1. scalpel", "A (Anna)", "Anna is 'chief surgeon at the local hospital.' Surgeons use scalpels for operations."),
        ("2. whisk", "No match (distractor)", "Carlos runs the Italian restaurant, but he's a manager, not a chef."),
        ("3. tripod", "E (Eric)", "Eric 'takes all our school photos and captures special events.' Photographers use tripods."),
        ("4. guitar", "No match (distractor)", "No one in the passage is a musician."),
        ("5. saw", "B (Ben)", "Ben 'builds beautiful wooden furniture in his workshop.' Carpenters use saws."),
    ]
    
    for q, ans, expl in entry_answers:
        create_answer_slide(slides_service, presentation_id, "Entry Ticket: Answer",
                           q, ans, expl)
    
    # 16. SECTION B INTRO
    create_content_slide(slides_service, presentation_id, "Before You Read",
        "Rate these behaviors:\n" +
        "(10 = Very rude, 1 = It's fine)\n\n" +
        "• Speaking on your phone on public transportation\n" +
        "• Interrupting someone\n" +
        "• Using your left hand to greet someone\n" +
        "• Sending e-mails during a meeting\n\n" +
        "Compare with your partner. 2 minutes.")
    
    # 17-19. GLOBAL READING ANSWERS
    global_answers = [
        ("A", "Paragraph 2", 
         "Paragraph 2 discusses polite phrases in language",
         "Some phrases are not really used for their actual meaning but as polite social phrases"),
        ("B", "Paragraph 4",
         "Paragraph 4 is about how technology has changed politeness norms", 
         "Cell phones have changed what is considered polite behavior"),
        ("C", "Paragraph 3",
         "Paragraph 3 gives examples of politeness varying across cultures",
         "From tipping, to smiling, and how you eat, there are different ways to show politeness across the world"),
    ]
    
    for main_idea, ans, expl, snippet in global_answers:
        create_answer_slide(slides_service, presentation_id, "Global Reading: Answer",
                           f"Main idea {main_idea}", ans, expl, snippet)
    
    # 20-25. CLOSE READING ANSWERS
    close_answers = [
        ("Gap 1", '"You\'re welcome"', 
         "Response older people use when thanked",
         "Older people are more likely to say 'You're welcome'"),
        ("Gap 2", '"No problem"',
         "Response younger people use when thanked", 
         "younger people are more likely to say 'No problem'"),
        ("Gap 3", "tipping",
         "A custom that varies between countries",
         "Take tipping for instance, which is polite... in the U.S.A. However, in Japan tipping is not expected"),
        ("Gap 4", "left hand",
         "Something considered unclean in India",
         "the left hand is considered unclean and shouldn't be used to eat, greet, or exchange money"),
        ("Gap 5", "having your phone / cell phone",
         "Something some consider rude at the dinner table",
         "To some people even just having your phone at the dinner table is thought to be impolite"),
        ("Gap 6", "older people",
         "The group more likely to find e-mailing during meetings rude",
         "older people are much more likely to have a negative reaction and find this rude"),
    ]
    
    for q, ans, expl, snippet in close_answers:
        create_answer_slide(slides_service, presentation_id, "Close Reading: Answer",
                           q, ans, expl, snippet)
    
    # 26-27. DISCUSSION SLIDES
    create_content_slide(slides_service, presentation_id, "Discussion Question 1",
        "What behavior do you find rude in other people?\n\n" +
        "Do you think other people would find any of your behavior rude?\n\n" +
        "Useful language:\n" +
        "• \"I really dislike it when...\"\n" +
        "• \"It annoys me when people...\"")
    
    create_content_slide(slides_service, presentation_id, "Discussion Question 2",
        "Do you think younger people are less polite than older people?\n\n" +
        "Why / why not?\n\n" +
        "Useful language:\n" +
        "• \"I do think so because...\"\n" +
        "• \"I don't think so because...\"")
    
    # 28. CLOSING
    create_content_slide(slides_service, presentation_id, "Key Takeaway",
        "Politeness is cultural.\n\n" +
        "What's polite in one culture may not be in another.\n\n" +
        "What's acceptable to one generation may not be to another.")
    
    # Move to target folder
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
    
    url = f"https://docs.google.com/presentation/d/{presentation_id}/edit"
    
    print("\n" + "=" * 60)
    print("🎉 Slideshow created successfully!")
    print(f"URL: {url}")
    print("=" * 60)
    
    return presentation_id, url


if __name__ == '__main__':
    main()
