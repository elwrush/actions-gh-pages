"""
Create Google Slides Presentations

Functions to create new presentations and manage basic structure.
"""

from googleapiclient.errors import HttpError

def create_presentation(service, title):
    """
    Create a new Google Slides presentation.
    
    Args:
        service: Google Slides API service object
        title (str): Presentation title
    
    Returns:
        str: Presentation ID
    """
    try:
        presentation = {'title': title}
        presentation = service.presentations().create(body=presentation).execute()
        
        presentation_id = presentation.get('presentationId')
        print(f"✅ Created presentation: {title}")
        print(f"   ID: {presentation_id}")
        print(f"   URL: https://docs.google.com/presentation/d/{presentation_id}/edit")
        
        return presentation_id
    
    except HttpError as error:
        print(f"❌ Error creating presentation: {error}")
        raise

def get_presentation(service, presentation_id):
    """
    Retrieve presentation metadata.
    
    Args:
        service: Google Slides API service object
        presentation_id (str): Presentation ID
    
    Returns:
        dict: Presentation metadata
    """
    try:
        presentation = service.presentations().get(
            presentationId=presentation_id
        ).execute()
        
        return presentation
    
    except HttpError as error:
        print(f"❌ Error retrieving presentation: {error}")
        raise

def list_slides(service, presentation_id):
    """
    List all slides in a presentation.
    
    Args:
        service: Google Slides API service object
        presentation_id (str): Presentation ID
    
    Returns:
        list: List of slide objects
    """
    presentation = get_presentation(service, presentation_id)
    slides = presentation.get('slides', [])
    
    print(f"Found {len(slides)} slides:")
    for i, slide in enumerate(slides, 1):
        print(f"  {i}. ID: {slide.get('objectId')}")
    
    return slides

def delete_slide(service, presentation_id, slide_id):
    """
    Delete a specific slide.
    
    Args:
        service: Google Slides API service object
        presentation_id (str): Presentation ID
        slide_id (str): Slide object ID
    """
    try:
        requests = [
            {
                'deleteObject': {
                    'objectId': slide_id
                }
            }
        ]
        
        body = {'requests': requests}
        service.presentations().batchUpdate(
            presentationId=presentation_id,
            body=body
        ).execute()
        
        print(f"✅ Deleted slide: {slide_id}")
    
    except HttpError as error:
        print(f"❌ Error deleting slide: {error}")
        raise
