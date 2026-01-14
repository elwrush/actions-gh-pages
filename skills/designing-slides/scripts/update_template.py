"""
Update Bell EP Slide Template

Updates the existing template with:
- Header bar with logos (co-branding lock-up)
- Title/subtitle placeholders as main focus
"""

import sys
import os
import time
sys.path.insert(0, 'skills/designing-slides')

from googleapiclient.http import MediaFileUpload
from scripts.authenticate_google import authenticate_slides, authenticate_drive
from scripts.add_slide_content import inches, _generate_id
from scripts.format_slides import SLIDE_WIDTH, SLIDE_HEIGHT

# Brand colors
BRAND_COLORS = {
    'maroon': {'red': 166/255, 'green': 45/255, 'blue': 38/255},
    'white': {'red': 1.0, 'green': 1.0, 'blue': 1.0},
    'dark_gray': {'red': 0.2, 'green': 0.2, 'blue': 0.2},
}

TEMPLATE_ID = "1AdeFwA9zFkJMmkwB7c74pO88KPuJypgZRDM73haL8iw"


def upload_image(drive_service, file_path):
    """Upload image to Drive and make public."""
    file_name = os.path.basename(file_path)
    
    media = MediaFileUpload(file_path, mimetype='image/png')
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
    
    print(f"✅ Uploaded {file_name} (ID: {file_id})")
    return f"https://lh3.googleusercontent.com/d/{file_id}"


def clear_slide(slides_service, presentation_id, slide_id):
    """Remove all elements from a slide."""
    presentation = slides_service.presentations().get(
        presentationId=presentation_id
    ).execute()
    
    for slide in presentation.get('slides', []):
        if slide.get('objectId') == slide_id:
            requests = []
            for element in slide.get('pageElements', []):
                requests.append({
                    'deleteObject': {'objectId': element.get('objectId')}
                })
            
            if requests:
                slides_service.presentations().batchUpdate(
                    presentationId=presentation_id,
                    body={'requests': requests}
                ).execute()
            break


def rebuild_title_slide(slides_service, presentation_id, slide_id, bell_url, act_url):
    """Rebuild title slide with header, strap line, title, and image placeholder."""
    
    clear_slide(slides_service, presentation_id, slide_id)
    
    # IDs
    header_bar_id = _generate_id()
    strap_id = _generate_id()
    title_id = _generate_id()
    image_placeholder_id = _generate_id()
    bell_img_id = _generate_id()
    act_img_id = _generate_id()
    
    # Dimensions
    header_height = inches(1.0)
    logo_height = inches(0.7)
    logo_width = inches(1.0)
    logo_y = (header_height - logo_height) / 2
    center_x = SLIDE_WIDTH / 2
    gap = inches(0.3)
    
    # Square image placeholder (centered)
    image_size = inches(2.5)
    image_x = (SLIDE_WIDTH - image_size) / 2
    
    # Create elements
    requests = [
        # Header bar
        {
            'createShape': {
                'objectId': header_bar_id,
                'shapeType': 'RECTANGLE',
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {
                        'width': {'magnitude': SLIDE_WIDTH, 'unit': 'EMU'},
                        'height': {'magnitude': header_height, 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': 0, 'translateY': 0,
                        'unit': 'EMU'
                    }
                }
            }
        },
        # Strap line: "Bell Language Centre"
        {
            'createShape': {
                'objectId': strap_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {
                        'width': {'magnitude': inches(8), 'unit': 'EMU'},
                        'height': {'magnitude': inches(0.5), 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': inches(1),
                        'translateY': inches(1.1),
                        'unit': 'EMU'
                    }
                }
            }
        },
        {'insertText': {'objectId': strap_id, 'text': 'Bell Language Centre'}},
        # Title placeholder
        {
            'createShape': {
                'objectId': title_id,
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
                        'translateY': inches(1.7),
                        'unit': 'EMU'
                    }
                }
            }
        },
        {'insertText': {'objectId': title_id, 'text': '{{TITLE}}'}},
        # Square image placeholder
        {
            'createShape': {
                'objectId': image_placeholder_id,
                'shapeType': 'RECTANGLE',
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {
                        'width': {'magnitude': image_size, 'unit': 'EMU'},
                        'height': {'magnitude': image_size, 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': image_x,
                        'translateY': inches(2.6),
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
    
    # Style elements
    requests = [
        # Header bar: darker maroon
        {
            'updateShapeProperties': {
                'objectId': header_bar_id,
                'shapeProperties': {
                    'shapeBackgroundFill': {
                        'solidFill': {
                            'color': {'rgbColor': {'red': 0.35, 'green': 0.05, 'blue': 0.05}}
                        }
                    },
                    'outline': {'propertyState': 'NOT_RENDERED'}
                },
                'fields': 'shapeBackgroundFill.solidFill.color,outline'
            }
        },
        # Strap line: white, 18pt, centered
        {
            'updateTextStyle': {
                'objectId': strap_id,
                'style': {
                    'foregroundColor': {'opaqueColor': {'rgbColor': BRAND_COLORS['white']}},
                    'fontSize': {'magnitude': 18, 'unit': 'PT'},
                    'fontFamily': 'Arial'
                },
                'textRange': {'type': 'ALL'},
                'fields': 'foregroundColor,fontSize,fontFamily'
            }
        },
        {'updateParagraphStyle': {
            'objectId': strap_id,
            'style': {'alignment': 'CENTER'},
            'textRange': {'type': 'ALL'},
            'fields': 'alignment'
        }},
        # Title: white, 36pt, bold, centered
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
        {'updateParagraphStyle': {
            'objectId': title_id,
            'style': {'alignment': 'CENTER'},
            'textRange': {'type': 'ALL'},
            'fields': 'alignment'
        }},
        # Image placeholder: light gray fill with border
        {
            'updateShapeProperties': {
                'objectId': image_placeholder_id,
                'shapeProperties': {
                    'shapeBackgroundFill': {
                        'solidFill': {
                            'color': {'rgbColor': {'red': 0.9, 'green': 0.9, 'blue': 0.9}}
                        }
                    },
                    'outline': {
                        'outlineFill': {
                            'solidFill': {
                                'color': {'rgbColor': BRAND_COLORS['maroon']}
                            }
                        },
                        'weight': {'magnitude': 2, 'unit': 'PT'}
                    }
                },
                'fields': 'shapeBackgroundFill.solidFill.color,outline'
            }
        }
    ]
    
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    
    # Add logos in header
    try:
        requests = [
            # Bell logo (left of center)
            {
                'createImage': {
                    'objectId': bell_img_id,
                    'url': bell_url,
                    'elementProperties': {
                        'pageObjectId': slide_id,
                        'size': {
                            'width': {'magnitude': logo_width, 'unit': 'EMU'},
                            'height': {'magnitude': logo_height, 'unit': 'EMU'}
                        },
                        'transform': {
                            'scaleX': 1, 'scaleY': 1,
                            'translateX': center_x - logo_width - gap/2,
                            'translateY': logo_y,
                            'unit': 'EMU'
                        }
                    }
                }
            },
            # ACT logo (right of center)
            {
                'createImage': {
                    'objectId': act_img_id,
                    'url': act_url,
                    'elementProperties': {
                        'pageObjectId': slide_id,
                        'size': {
                            'width': {'magnitude': logo_width, 'unit': 'EMU'},
                            'height': {'magnitude': logo_height, 'unit': 'EMU'}
                        },
                        'transform': {
                            'scaleX': 1, 'scaleY': 1,
                            'translateX': center_x + gap/2,
                            'translateY': logo_y,
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
        print("✅ Added logos to header")
    except Exception as e:
        print(f"⚠️ Logo insertion failed: {e}")
    
    print("✅ Title slide updated with strap line and image placeholder")


def main():
    print("=" * 60)
    print("Updating Bell EP Slide Template")
    print("=" * 60)
    
    slides_service = authenticate_slides()
    drive_service = authenticate_drive()
    print("✅ Authenticated")
    
    # Upload images - using images/Bell.png
    print("\nUploading images...")
    bell_url = upload_image(drive_service, "images/Bell.png")
    act_url = upload_image(drive_service, "images/ACT.png")
    
    time.sleep(2)
    
    # Update template
    print(f"\nUpdating template: {TEMPLATE_ID}")
    presentation = slides_service.presentations().get(
        presentationId=TEMPLATE_ID
    ).execute()
    
    slides = presentation.get('slides', [])
    if slides:
        title_slide_id = slides[0].get('objectId')
        print(f"Updating title slide: {title_slide_id}")
        rebuild_title_slide(slides_service, TEMPLATE_ID, title_slide_id, bell_url, act_url)
    
    print("\n" + "=" * 60)
    print("🎉 Template updated!")
    print(f"URL: https://docs.google.com/presentation/d/{TEMPLATE_ID}/edit")
    print("=" * 60)


if __name__ == '__main__':
    main()
