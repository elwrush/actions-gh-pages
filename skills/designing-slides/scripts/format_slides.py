"""
Format Google Slides

Functions to apply styling, colors, fonts, and themes to slides.
"""

from googleapiclient.errors import HttpError

# Bell EP Theme Colors (RGB values 0-1)
BELL_COLORS = {
    'maroon': {'red': 0.545, 'green': 0.0, 'blue': 0.0},
    'dark_maroon': {'red': 0.4, 'green': 0.0, 'blue': 0.05},
    'white': {'red': 1.0, 'green': 1.0, 'blue': 1.0},
    'light_gray': {'red': 0.9, 'green': 0.9, 'blue': 0.9},
    'dark_gray': {'red': 0.2, 'green': 0.2, 'blue': 0.2},
    'black': {'red': 0.0, 'green': 0.0, 'blue': 0.0},
}

# Design Principles (from knowledge_base/slide-design-principles.md)
DESIGN_CONSTRAINTS = {
    'max_lines_per_slide': 7,       # Keep it simple: 5-7 lines max
    'max_words_per_line': 6,        # No more than 6 words per line
    'max_bullets': 6,               # Limit bullet points
    'min_body_font_pt': 24,         # Large readable fonts: 24pt+ body
    'min_title_font_pt': 44,        # 44pt+ for titles
    'min_contrast_ratio': 4.5,      # WCAG accessibility minimum
    'whitespace_percentage': 0.35,  # 30-50% empty space
    'max_font_families': 2,         # Limit typography
}


def format_text(service, presentation_id, object_id, start_index, end_index,
                bold=None, italic=None, underline=None, font_family=None,
                font_size=None, color=None, link=None):
    """
    Format text within an element.
    
    Args:
        service: Google Slides API service
        presentation_id (str): Presentation ID
        object_id (str): Shape/text box object ID
        start_index (int): Starting character index
        end_index (int): Ending character index
        bold (bool, optional): Make text bold
        italic (bool, optional): Make text italic
        underline (bool, optional): Underline text
        font_family (str, optional): Font family name
        font_size (int, optional): Font size in points
        color (dict, optional): RGB color dict {'red': 0-1, 'green': 0-1, 'blue': 0-1}
        link (str, optional): URL for hyperlink
    """
    style = {}
    fields = []
    
    if bold is not None:
        style['bold'] = bold
        fields.append('bold')
    
    if italic is not None:
        style['italic'] = italic
        fields.append('italic')
    
    if underline is not None:
        style['underline'] = underline
        fields.append('underline')
    
    if font_family:
        style['fontFamily'] = font_family
        fields.append('fontFamily')
    
    if font_size:
        style['fontSize'] = {'magnitude': font_size, 'unit': 'PT'}
        fields.append('fontSize')
    
    if color:
        style['foregroundColor'] = {
            'opaqueColor': {
                'rgbColor': color
            }
        }
        fields.append('foregroundColor')
    
    if link:
        style['link'] = {'url': link}
        fields.append('link')
    
    requests = [{
        'updateTextStyle': {
            'objectId': object_id,
            'textRange': {
                'type': 'FIXED_RANGE',
                'startIndex': start_index,
                'endIndex': end_index
            },
            'style': style,
            'fields': ','.join(fields)
        }
    }]
    
    body = {'requests': requests}
    service.presentations().batchUpdate(
        presentationId=presentation_id,
        body=body
    ).execute()


def set_shape_fill(service, presentation_id, object_id, color):
    """
    Set the fill color of a shape.
    
    Args:
        service: Google Slides API service
        presentation_id (str): Presentation ID
        object_id (str): Shape object ID
        color (dict): RGB color dict
    """
    requests = [{
        'updateShapeProperties': {
            'objectId': object_id,
            'shapeProperties': {
                'shapeBackgroundFill': {
                    'solidFill': {
                        'color': {
                            'rgbColor': color
                        }
                    }
                }
            },
            'fields': 'shapeBackgroundFill.solidFill.color'
        }
    }]
    
    body = {'requests': requests}
    service.presentations().batchUpdate(
        presentationId=presentation_id,
        body=body
    ).execute()


def set_slide_background(service, presentation_id, slide_id, color=None, image_url=None):
    """
    Set slide background color or image.
    
    Args:
        service: Google Slides API service
        presentation_id (str): Presentation ID
        slide_id (str): Slide object ID
        color (dict, optional): RGB color dict for solid fill
        image_url (str, optional): URL for background image
    """
    if color:
        background = {
            'solidFill': {
                'color': {
                    'rgbColor': color
                }
            }
        }
        fields = 'propertyState,solidFill.color'
    elif image_url:
        background = {
            'stretchedPictureFill': {
                'contentUrl': image_url
            }
        }
        fields = 'propertyState,stretchedPictureFill.contentUrl'
    else:
        return
    
    requests = [{
        'updatePageProperties': {
            'objectId': slide_id,
            'pageProperties': {
                'pageBackgroundFill': background
            },
            'fields': f'pageBackgroundFill.{fields}'
        }
    }]
    
    body = {'requests': requests}
    service.presentations().batchUpdate(
        presentationId=presentation_id,
        body=body
    ).execute()


def format_table_cell(service, presentation_id, table_id, row, col, 
                      bg_color=None, bold=None, font_size=None, alignment=None):
    """
    Format a table cell.
    
    Args:
        service: Google Slides API service
        presentation_id (str): Presentation ID
        table_id (str): Table object ID
        row (int): Row index (0-based)
        col (int): Column index (0-based)
        bg_color (dict, optional): Background RGB color
        bold (bool, optional): Make text bold
        font_size (int, optional): Font size in points
        alignment (str, optional): 'START', 'CENTER', 'END'
    """
    requests = []
    
    if bg_color:
        requests.append({
            'updateTableCellProperties': {
                'objectId': table_id,
                'tableRange': {
                    'location': {'rowIndex': row, 'columnIndex': col},
                    'rowSpan': 1,
                    'columnSpan': 1
                },
                'tableCellProperties': {
                    'tableCellBackgroundFill': {
                        'solidFill': {
                            'color': {'rgbColor': bg_color}
                        }
                    }
                },
                'fields': 'tableCellBackgroundFill.solidFill.color'
            }
        })
    
    if requests:
        body = {'requests': requests}
        service.presentations().batchUpdate(
            presentationId=presentation_id,
            body=body
        ).execute()


def apply_bell_theme_to_slide(service, presentation_id, slide_id, 
                               title_object_id=None, is_title_slide=False):
    """
    Apply Bell EP theme styling to a slide.
    
    Args:
        service: Google Slides API service
        presentation_id (str): Presentation ID
        slide_id (str): Slide object ID
        title_object_id (str, optional): Title element ID to format
        is_title_slide (bool): Whether this is a title slide
    """
    # Set background based on slide type
    if is_title_slide:
        set_slide_background(service, presentation_id, slide_id, 
                           color=BELL_COLORS['maroon'])
    else:
        set_slide_background(service, presentation_id, slide_id,
                           color=BELL_COLORS['white'])


def create_shape(service, presentation_id, slide_id, shape_type, 
                 x, y, width, height, fill_color=None, outline_color=None):
    """
    Create a shape on a slide.
    
    Args:
        service: Google Slides API service
        presentation_id (str): Presentation ID
        slide_id (str): Slide object ID
        shape_type (str): Shape type (RECTANGLE, ELLIPSE, etc.)
        x, y, width, height: Position and size in EMUs
        fill_color (dict, optional): Fill RGB color
        outline_color (dict, optional): Outline RGB color
    
    Returns:
        str: Shape object ID
    """
    import uuid
    shape_id = str(uuid.uuid4()).replace('-', '')[:24]
    
    requests = [{
        'createShape': {
            'objectId': shape_id,
            'shapeType': shape_type,
            'elementProperties': {
                'pageObjectId': slide_id,
                'size': {
                    'width': {'magnitude': width, 'unit': 'EMU'},
                    'height': {'magnitude': height, 'unit': 'EMU'}
                },
                'transform': {
                    'scaleX': 1,
                    'scaleY': 1,
                    'translateX': x,
                    'translateY': y,
                    'unit': 'EMU'
                }
            }
        }
    }]
    
    body = {'requests': requests}
    service.presentations().batchUpdate(
        presentationId=presentation_id,
        body=body
    ).execute()
    
    # Apply fill if specified
    if fill_color:
        set_shape_fill(service, presentation_id, shape_id, fill_color)
    
    return shape_id


# Standard slide sizes (in EMUs)
SLIDE_WIDTH = 9144000   # 10 inches
SLIDE_HEIGHT = 5143500  # 5.625 inches (16:9 ratio)
