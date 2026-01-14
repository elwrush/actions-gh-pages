"""
Create Bell EP Slide Template v2

Fixed version using correct Drive image URL format.
"""

import os
import sys
import time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from scripts.authenticate_google import authenticate_slides, authenticate_drive
from scripts.add_slide_content import inches, _generate_id
from scripts.format_slides import SLIDE_WIDTH, SLIDE_HEIGHT

# Brand colors extracted from ACT.png
BRAND_COLORS = {
    'maroon': {'red': 166/255, 'green': 45/255, 'blue': 38/255},
    'white': {'red': 1.0, 'green': 1.0, 'blue': 1.0},
    'dark_gray': {'red': 0.2, 'green': 0.2, 'blue': 0.2},
}

TARGET_FOLDER_ID = "1_n11w9BRN6sd0uaXlqEXjqZuZ74zFiOl"


def upload_image_to_drive(drive_service, file_path, folder_id=None):
    """Upload image to Drive and make it public."""
    file_name = os.path.basename(file_path)
    mime_type = 'image/png' if file_path.endswith('.png') else 'image/svg+xml'
    
    file_metadata = {'name': file_name}
    if folder_id:
        file_metadata['parents'] = [folder_id]
    
    media = MediaFileUpload(file_path, mimetype=mime_type)
    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    
    file_id = file.get('id')
    
    # Make public
    drive_service.permissions().create(
        fileId=file_id,
        body={'type': 'anyone', 'role': 'reader'}
    ).execute()
    
    print(f"✅ Uploaded {file_name} (ID: {file_id})")
    return file_id


def get_image_url(file_id):
    """Get working image URL for Slides API."""
    # This format works reliably with Google Slides API
    return f"https://lh3.googleusercontent.com/d/{file_id}"


def create_template():
    """Create the Bell EP slide template with logos."""
    print("=" * 60)
    print("Creating Bell EP Slide Template v2")
    print("=" * 60)
    
    # Authenticate
    slides_service = authenticate_slides()
    drive_service = authenticate_drive()
    print("✅ Authenticated")
    
    # Upload logos
    print("\nUploading logos...")
    bell_id = upload_image_to_drive(drive_service, 'images/Bell.svg')
    act_id = upload_image_to_drive(drive_service, 'images/ACT.png')
    
    # Wait for Drive to propagate
    print("Waiting for Drive propagation...")
    time.sleep(3)
    
    bell_url = get_image_url(bell_id)
    act_url = get_image_url(act_id)
    print(f"Bell URL: {bell_url}")
    print(f"ACT URL: {act_url}")
    
    # Create presentation
    print("\nCreating presentation...")
    presentation = slides_service.presentations().create(
        body={'title': 'Bell EP Slide Template'}
    ).execute()
    presentation_id = presentation.get('presentationId')
    print(f"✅ Created: {presentation_id}")
    
    # Get default slide and delete it
    default_slide = presentation.get('slides', [])[0]['objectId']
    
    # Prepare all requests for title slide
    title_slide_id = _generate_id()
    title_text_id = _generate_id()
    subtitle_text_id = _generate_id()
    bell_img_id = _generate_id()
    act_img_id = _generate_id()
    
    requests = [
        # Delete default slide
        {'deleteObject': {'objectId': default_slide}},
        
        # Create title slide (blank)
        {
            'createSlide': {
                'objectId': title_slide_id,
                'insertionIndex': 0,
                'slideLayoutReference': {'predefinedLayout': 'BLANK'}
            }
        }
    ]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    # Set maroon background
    requests = [{
        'updatePageProperties': {
            'objectId': title_slide_id,
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
    
    # Add text elements
    requests = [
        # Title: "Bell Language Centre"
        {
            'createShape': {
                'objectId': title_text_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': title_slide_id,
                    'size': {
                        'width': {'magnitude': inches(8), 'unit': 'EMU'},
                        'height': {'magnitude': inches(1.2), 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': inches(1),
                        'translateY': inches(2),
                        'unit': 'EMU'
                    }
                }
            }
        },
        {'insertText': {'objectId': title_text_id, 'text': 'Bell Language Centre'}},
        
        # Subtitle placeholder
        {
            'createShape': {
                'objectId': subtitle_text_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': title_slide_id,
                    'size': {
                        'width': {'magnitude': inches(8), 'unit': 'EMU'},
                        'height': {'magnitude': inches(0.8), 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': inches(1),
                        'translateY': inches(3.3),
                        'unit': 'EMU'
                    }
                }
            }
        },
        {'insertText': {'objectId': subtitle_text_id, 'text': '{{SUBTITLE}}'}}
    ]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    # Format text
    requests = [
        {
            'updateTextStyle': {
                'objectId': title_text_id,
                'style': {
                    'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}},
                    'fontSize': {'magnitude': 48, 'unit': 'PT'},
                    'bold': True,
                    'fontFamily': 'Arial'
                },
                'textRange': {'type': 'ALL'},
                'fields': 'foregroundColor,fontSize,bold,fontFamily'
            }
        },
        {
            'updateTextStyle': {
                'objectId': subtitle_text_id,
                'style': {
                    'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}},
                    'fontSize': {'magnitude': 28, 'unit': 'PT'},
                    'fontFamily': 'Arial'
                },
                'textRange': {'type': 'ALL'},
                'fields': 'foregroundColor,fontSize,fontFamily'
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
        {
            'updateParagraphStyle': {
                'objectId': subtitle_text_id,
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
    
    print("✅ Created title slide with text")
    
    # Add logos
    print("\nAdding logos...")
    try:
        requests = [
            # Bell logo (bottom left)
            {
                'createImage': {
                    'objectId': bell_img_id,
                    'url': bell_url,
                    'elementProperties': {
                        'pageObjectId': title_slide_id,
                        'size': {
                            'width': {'magnitude': inches(1.8), 'unit': 'EMU'},
                            'height': {'magnitude': inches(1.7), 'unit': 'EMU'}
                        },
                        'transform': {
                            'scaleX': 1, 'scaleY': 1,
                            'translateX': inches(0.3),
                            'translateY': inches(4.2),
                            'unit': 'EMU'
                        }
                    }
                }
            }
        ]
        
        slides_service.presentations().batchUpdate(
            presentationId=presentation_id,
            body={'requests': requests}
        ).execute()
        print("✅ Bell logo added")
    except Exception as e:
        print(f"⚠️ Bell logo failed: {e}")
    
    try:
        requests = [
            # ACT logo (bottom right)
            {
                'createImage': {
                    'objectId': act_img_id,
                    'url': act_url,
                    'elementProperties': {
                        'pageObjectId': title_slide_id,
                        'size': {
                            'width': {'magnitude': inches(1.8), 'unit': 'EMU'},
                            'height': {'magnitude': inches(0.9), 'unit': 'EMU'}
                        },
                        'transform': {
                            'scaleX': 1, 'scaleY': 1,
                            'translateX': inches(7.9),
                            'translateY': inches(4.5),
                            'unit': 'EMU'
                        }
                    }
                }
            }
        ]
        
        slides_service.presentations().batchUpdate(
            presentationId=presentation_id,
            body={'requests': requests}
        ).execute()
        print("✅ ACT logo added")
    except Exception as e:
        print(f"⚠️ ACT logo failed: {e}")
    
    # Create content slide
    print("\nCreating content slide...")
    content_slide_id = _generate_id()
    header_id = _generate_id()
    content_title_id = _generate_id()
    body_id = _generate_id()
    
    requests = [
        {'createSlide': {
            'objectId': content_slide_id,
            'slideLayoutReference': {'predefinedLayout': 'BLANK'}
        }}
    ]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    # Add header bar and text
    requests = [
        # Maroon header
        {
            'createShape': {
                'objectId': header_id,
                'shapeType': 'RECTANGLE',
                'elementProperties': {
                    'pageObjectId': content_slide_id,
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
        # Title on header
        {
            'createShape': {
                'objectId': content_title_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': content_slide_id,
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
        {'insertText': {'objectId': content_title_id, 'text': '{{SLIDE_TITLE}}'}},
        # Body
        {
            'createShape': {
                'objectId': body_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': content_slide_id,
                    'size': {
                        'width': {'magnitude': inches(9), 'unit': 'EMU'},
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
        {'insertText': {'objectId': body_id, 'text': '{{CONTENT}}'}}
    ]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    # Format header and text
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
                'objectId': content_title_id,
                'style': {
                    'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}},
                    'fontSize': {'magnitude': 36, 'unit': 'PT'},
                    'bold': True,
                    'fontFamily': 'Arial'
                },
                'textRange': {'type': 'ALL'},
                'fields': 'foregroundColor,fontSize,bold,fontFamily'
            }
        },
        {
            'updateTextStyle': {
                'objectId': body_id,
                'style': {
                    'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['dark_gray']}},
                    'fontSize': {'magnitude': 24, 'unit': 'PT'},
                    'fontFamily': 'Arial'
                },
                'textRange': {'type': 'ALL'},
                'fields': 'foregroundColor,fontSize,fontFamily'
            }
        }
    ]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    print("✅ Created content slide")
    
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
    
    print("\n" + "=" * 60)
    print("🎉 Template created!")
    print(f"URL: https://docs.google.com/presentation/d/{presentation_id}/edit")
    print("=" * 60)
    
    return presentation_id


if __name__ == '__main__':
    create_template()
