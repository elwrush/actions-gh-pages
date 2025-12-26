"""
Create Bell EP Slide Template

Creates a branded slide template with:
- Title slide with maroon background + logos
- Content slide with clean white background
- Consistent branding and typography
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from scripts.authenticate_google import authenticate_slides, authenticate_drive
from scripts.create_presentation import create_presentation
from scripts.add_slide_content import add_slide, inches, points, _generate_id
from scripts.format_slides import SLIDE_WIDTH, SLIDE_HEIGHT

# Brand colors extracted from ACT.png
BRAND_COLORS = {
    'maroon': {'red': 166/255, 'green': 45/255, 'blue': 38/255},  # RGB(166, 45, 38)
    'white': {'red': 1.0, 'green': 1.0, 'blue': 1.0},
    'light_gray': {'red': 0.95, 'green': 0.95, 'blue': 0.95},
    'dark_gray': {'red': 0.2, 'green': 0.2, 'blue': 0.2},
}

# Target folder ID
TARGET_FOLDER_ID = "1_n11w9BRN6sd0uaXlqEXjqZuZ74zFiOl"


def upload_image_to_drive(drive_service, file_path, folder_id=None):
    """Upload an image to Google Drive and return its ID."""
    file_name = os.path.basename(file_path)
    
    # Determine MIME type
    if file_path.endswith('.svg'):
        mime_type = 'image/svg+xml'
    elif file_path.endswith('.png'):
        mime_type = 'image/png'
    else:
        mime_type = 'image/jpeg'
    
    file_metadata = {'name': file_name}
    if folder_id:
        file_metadata['parents'] = [folder_id]
    
    media = MediaFileUpload(file_path, mimetype=mime_type)
    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id, webContentLink'
    ).execute()
    
    # Make the file publicly accessible
    drive_service.permissions().create(
        fileId=file.get('id'),
        body={'type': 'anyone', 'role': 'reader'}
    ).execute()
    
    print(f"✅ Uploaded {file_name} to Drive (ID: {file.get('id')})")
    return file.get('id')


def get_drive_image_url(file_id):
    """Get a direct image URL from a Drive file ID."""
    return f"https://drive.google.com/uc?export=view&id={file_id}"


def create_title_slide(slides_service, presentation_id):
    """Create the title slide with maroon background and logos."""
    slide_id = _generate_id()
    
    # Create blank slide
    requests = [{
        'createSlide': {
            'objectId': slide_id,
            'insertionIndex': 0,
            'slideLayoutReference': {'predefinedLayout': 'BLANK'}
        }
    }]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    # Set maroon background
    requests = [{
        'updatePageProperties': {
            'objectId': slide_id,
            'pageProperties': {
                'pageBackgroundFill': {
                    'solidFill': {
                        'color': {'rgbColor': BRAND_COLORS['maroon']}
                    }
                }
            },
            'fields': 'pageBackgroundFill.solidFill.color'
        }
    }]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    # Add title text box (white text)
    title_id = _generate_id()
    subtitle_id = _generate_id()
    
    requests = [
        # Main title
        {
            'createShape': {
                'objectId': title_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': slide_id,
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
        {
            'insertText': {
                'objectId': title_id,
                'text': '{{TITLE}}'
            }
        },
        # Subtitle
        {
            'createShape': {
                'objectId': subtitle_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': slide_id,
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
        {
            'insertText': {
                'objectId': subtitle_id,
                'text': '{{SUBTITLE}}'
            }
        }
    ]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    # Format title text (white, 44pt, bold)
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
        # Center align title
        {
            'updateParagraphStyle': {
                'objectId': title_id,
                'style': {'alignment': 'CENTER'},
                'textRange': {'type': 'ALL'},
                'fields': 'alignment'
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
    
    print(f"✅ Created title slide")
    return slide_id


def add_logos_to_slide(slides_service, presentation_id, slide_id, bell_url, act_url):
    """Add Bell and ACT logos to the title slide."""
    bell_id = _generate_id()
    act_id = _generate_id()
    
    try:
        requests = [
            # Bell logo (bottom left)
            {
                'createImage': {
                    'objectId': bell_id,
                    'url': bell_url,
                    'elementProperties': {
                        'pageObjectId': slide_id,
                        'size': {
                            'width': {'magnitude': inches(1.5), 'unit': 'EMU'},
                            'height': {'magnitude': inches(1.4), 'unit': 'EMU'}
                        },
                        'transform': {
                            'scaleX': 1, 'scaleY': 1,
                            'translateX': inches(0.5),
                            'translateY': inches(4.5),
                            'unit': 'EMU'
                        }
                    }
                }
            },
            # ACT logo (bottom right)
            {
                'createImage': {
                    'objectId': act_id,
                    'url': act_url,
                    'elementProperties': {
                        'pageObjectId': slide_id,
                        'size': {
                            'width': {'magnitude': inches(1.5), 'unit': 'EMU'},
                            'height': {'magnitude': inches(0.8), 'unit': 'EMU'}
                        },
                        'transform': {
                            'scaleX': 1, 'scaleY': 1,
                            'translateX': inches(8),
                            'translateY': inches(4.7),
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
        
        print(f"✅ Added logos to title slide")
    except Exception as e:
        print(f"⚠️ Could not add logos automatically: {e}")
        print("   Please add logos manually from Google Drive")


def create_content_slide(slides_service, presentation_id):
    """Create a content slide template with maroon header bar."""
    slide_id = _generate_id()
    
    # Create blank slide
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
    
    # Add maroon header bar
    header_id = _generate_id()
    title_id = _generate_id()
    body_id = _generate_id()
    
    requests = [
        # Maroon header bar
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
                        'translateX': 0,
                        'translateY': 0,
                        'unit': 'EMU'
                    }
                }
            }
        },
        # Title text box (on header)
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
        {
            'insertText': {
                'objectId': title_id,
                'text': '{{SLIDE_TITLE}}'
            }
        },
        # Body content area
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
                        'translateY': inches(1.2),
                        'unit': 'EMU'
                    }
                }
            }
        },
        {
            'insertText': {
                'objectId': body_id,
                'text': '{{CONTENT}}'
            }
        }
    ]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    # Set header bar color
    requests = [{
        'updateShapeProperties': {
            'objectId': header_id,
            'shapeProperties': {
                'shapeBackgroundFill': {
                    'solidFill': {
                        'color': {'rgbColor': BRAND_COLORS['maroon']}
                    }
                },
                'outline': {'propertyState': 'NOT_RENDERED'}
            },
            'fields': 'shapeBackgroundFill.solidFill.color,outline'
        }
    }]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    # Format text
    requests = [
        # Title: white on maroon, 36pt bold
        {
            'updateTextStyle': {
                'objectId': title_id,
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
        # Body: dark gray, 24pt
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
    
    print(f"✅ Created content slide template")
    return slide_id


def move_to_folder(drive_service, file_id, folder_id):
    """Move a file to a specific folder."""
    # Get current parents
    file = drive_service.files().get(fileId=file_id, fields='parents').execute()
    previous_parents = ",".join(file.get('parents', []))
    
    # Move to new folder
    drive_service.files().update(
        fileId=file_id,
        addParents=folder_id,
        removeParents=previous_parents,
        fields='id, parents'
    ).execute()
    
    print(f"✅ Moved presentation to target folder")


def main():
    """Create the Bell EP slide template."""
    print("=" * 60)
    print("Creating Bell EP Slide Template")
    print("=" * 60)
    
    # Authenticate
    slides_service = authenticate_slides()
    drive_service = authenticate_drive()
    print("✅ Authenticated")
    
    # Upload logos to Drive
    print("\nUploading logos...")
    bell_file_id = upload_image_to_drive(drive_service, 'images/Bell.svg')
    act_file_id = upload_image_to_drive(drive_service, 'images/ACT.png')
    
    bell_url = get_drive_image_url(bell_file_id)
    act_url = get_drive_image_url(act_file_id)
    
    # Create presentation
    print("\nCreating template...")
    presentation = slides_service.presentations().create(
        body={'title': 'Bell EP Slide Template'}
    ).execute()
    presentation_id = presentation.get('presentationId')
    print(f"✅ Created presentation: {presentation_id}")
    
    # Delete default slide
    default_slides = presentation.get('slides', [])
    if default_slides:
        slides_service.presentations().batchUpdate(
            presentationId=presentation_id,
            body={'requests': [{'deleteObject': {'objectId': default_slides[0]['objectId']}}]}
        ).execute()
    
    # Create slides
    title_slide_id = create_title_slide(slides_service, presentation_id)
    add_logos_to_slide(slides_service, presentation_id, title_slide_id, bell_url, act_url)
    create_content_slide(slides_service, presentation_id)
    
    # Move to target folder
    move_to_folder(drive_service, presentation_id, TARGET_FOLDER_ID)
    
    print("\n" + "=" * 60)
    print("🎉 Template created successfully!")
    print(f"View: https://docs.google.com/presentation/d/{presentation_id}/edit")
    print("=" * 60)
    
    return presentation_id


if __name__ == '__main__':
    main()
