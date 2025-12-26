"""
Add Content to Google Slides

Functions to add various content types to slides:
- Title slides
- Content slides with bullet points
- Images
- Tables
- Text boxes
"""

import uuid
from googleapiclient.errors import HttpError


def _generate_id():
    """Generate a unique object ID."""
    return str(uuid.uuid4()).replace('-', '')[:24]


def add_slide(service, presentation_id, layout='BLANK'):
    """
    Add a new slide to the presentation.
    
    Args:
        service: Google Slides API service
        presentation_id (str): Presentation ID
        layout (str): Layout type - BLANK, TITLE, TITLE_AND_BODY, etc.
    
    Returns:
        str: New slide object ID
    """
    slide_id = _generate_id()
    
    requests = [{
        'createSlide': {
            'objectId': slide_id,
            'slideLayoutReference': {
                'predefinedLayout': layout
            }
        }
    }]
    
    body = {'requests': requests}
    service.presentations().batchUpdate(
        presentationId=presentation_id,
        body=body
    ).execute()
    
    return slide_id


def add_title_slide(service, presentation_id, title, subtitle=None):
    """
    Add a title slide with optional subtitle.
    
    Args:
        service: Google Slides API service
        presentation_id (str): Presentation ID
        title (str): Main title text
        subtitle (str, optional): Subtitle text
    
    Returns:
        str: Slide object ID
    """
    slide_id = add_slide(service, presentation_id, 'TITLE')
    
    # Get the slide to find placeholder IDs
    presentation = service.presentations().get(
        presentationId=presentation_id
    ).execute()
    
    # Find the new slide
    new_slide = None
    for slide in presentation.get('slides', []):
        if slide.get('objectId') == slide_id:
            new_slide = slide
            break
    
    if not new_slide:
        return slide_id
    
    requests = []
    
    # Find title and subtitle placeholders
    for element in new_slide.get('pageElements', []):
        shape = element.get('shape', {})
        placeholder = shape.get('placeholder', {})
        placeholder_type = placeholder.get('type')
        element_id = element.get('objectId')
        
        if placeholder_type == 'CENTERED_TITLE' or placeholder_type == 'TITLE':
            requests.append({
                'insertText': {
                    'objectId': element_id,
                    'text': title
                }
            })
        elif placeholder_type == 'SUBTITLE' and subtitle:
            requests.append({
                'insertText': {
                    'objectId': element_id,
                    'text': subtitle
                }
            })
    
    if requests:
        body = {'requests': requests}
        service.presentations().batchUpdate(
            presentationId=presentation_id,
            body=body
        ).execute()
    
    print(f"✅ Added title slide: {title}")
    return slide_id


def add_content_slide(service, presentation_id, title, bullets):
    """
    Add a slide with title and bullet points.
    
    Args:
        service: Google Slides API service
        presentation_id (str): Presentation ID
        title (str): Slide title
        bullets (list): List of bullet point strings
    
    Returns:
        str: Slide object ID
    """
    slide_id = add_slide(service, presentation_id, 'TITLE_AND_BODY')
    
    # Get the slide to find placeholder IDs
    presentation = service.presentations().get(
        presentationId=presentation_id
    ).execute()
    
    new_slide = None
    for slide in presentation.get('slides', []):
        if slide.get('objectId') == slide_id:
            new_slide = slide
            break
    
    if not new_slide:
        return slide_id
    
    requests = []
    
    for element in new_slide.get('pageElements', []):
        shape = element.get('shape', {})
        placeholder = shape.get('placeholder', {})
        placeholder_type = placeholder.get('type')
        element_id = element.get('objectId')
        
        if placeholder_type == 'TITLE':
            requests.append({
                'insertText': {
                    'objectId': element_id,
                    'text': title
                }
            })
        elif placeholder_type == 'BODY':
            # Create bullet text
            bullet_text = '\n'.join(bullets)
            requests.append({
                'insertText': {
                    'objectId': element_id,
                    'text': bullet_text
                }
            })
    
    if requests:
        body = {'requests': requests}
        service.presentations().batchUpdate(
            presentationId=presentation_id,
            body=body
        ).execute()
    
    print(f"✅ Added content slide: {title} ({len(bullets)} bullets)")
    return slide_id


def add_text_box(service, presentation_id, slide_id, text, x, y, width, height):
    """
    Add a text box to a slide.
    
    Args:
        service: Google Slides API service
        presentation_id (str): Presentation ID
        slide_id (str): Slide object ID
        text (str): Text content
        x (float): X position in EMUs (1 inch = 914400 EMUs)
        y (float): Y position in EMUs
        width (float): Width in EMUs
        height (float): Height in EMUs
    
    Returns:
        str: Text box object ID
    """
    textbox_id = _generate_id()
    
    requests = [
        {
            'createShape': {
                'objectId': textbox_id,
                'shapeType': 'TEXT_BOX',
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
        },
        {
            'insertText': {
                'objectId': textbox_id,
                'text': text
            }
        }
    ]
    
    body = {'requests': requests}
    service.presentations().batchUpdate(
        presentationId=presentation_id,
        body=body
    ).execute()
    
    return textbox_id


def add_image_from_url(service, presentation_id, slide_id, image_url, x, y, width, height):
    """
    Add an image to a slide from a URL.
    
    Args:
        service: Google Slides API service
        presentation_id (str): Presentation ID
        slide_id (str): Slide object ID
        image_url (str): Public URL of the image
        x (float): X position in EMUs
        y (float): Y position in EMUs
        width (float): Width in EMUs
        height (float): Height in EMUs
    
    Returns:
        str: Image object ID
    """
    image_id = _generate_id()
    
    requests = [{
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
    
    print(f"✅ Added image from URL")
    return image_id


def add_table(service, presentation_id, slide_id, rows, cols, x, y, width, height, data=None):
    """
    Add a table to a slide.
    
    Args:
        service: Google Slides API service
        presentation_id (str): Presentation ID
        slide_id (str): Slide object ID
        rows (int): Number of rows
        cols (int): Number of columns
        x (float): X position in EMUs
        y (float): Y position in EMUs
        width (float): Width in EMUs
        height (float): Height in EMUs
        data (list, optional): 2D list of cell data [[row1], [row2], ...]
    
    Returns:
        str: Table object ID
    """
    table_id = _generate_id()
    
    requests = [{
        'createTable': {
            'objectId': table_id,
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
            },
            'rows': rows,
            'columns': cols
        }
    }]
    
    body = {'requests': requests}
    service.presentations().batchUpdate(
        presentationId=presentation_id,
        body=body
    ).execute()
    
    # Populate table if data provided
    if data:
        populate_table(service, presentation_id, table_id, data)
    
    print(f"✅ Added {rows}x{cols} table")
    return table_id


def populate_table(service, presentation_id, table_id, data):
    """
    Populate a table with data.
    
    Args:
        service: Google Slides API service
        presentation_id (str): Presentation ID
        table_id (str): Table object ID
        data (list): 2D list of cell data [[row1], [row2], ...]
    """
    requests = []
    
    for row_idx, row in enumerate(data):
        for col_idx, cell_text in enumerate(row):
            if cell_text:
                requests.append({
                    'insertText': {
                        'objectId': table_id,
                        'cellLocation': {
                            'rowIndex': row_idx,
                            'columnIndex': col_idx
                        },
                        'text': str(cell_text)
                    }
                })
    
    if requests:
        body = {'requests': requests}
        service.presentations().batchUpdate(
            presentationId=presentation_id,
            body=body
        ).execute()


# EMU conversion helpers
INCH_TO_EMU = 914400
PT_TO_EMU = 12700

def inches(value):
    """Convert inches to EMUs."""
    return int(value * INCH_TO_EMU)

def points(value):
    """Convert points to EMUs."""
    return int(value * PT_TO_EMU)
