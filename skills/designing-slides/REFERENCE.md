# Google Slides API Reference

Quick reference for the designing-slides skill.

## Authentication

```python
from scripts.authenticate_google import authenticate_slides
service = authenticate_slides()
```

## Core Operations

### Create Presentation
```python
from scripts.create_presentation import create_presentation
presentation_id = create_presentation(service, "My Presentation")
```

### Add Slides
```python
from scripts.add_slide_content import (
    add_title_slide,
    add_content_slide,
    add_text_box,
    add_image_from_url,
    add_table,
    inches, points  # Unit converters
)

# Title slide
add_title_slide(service, presentation_id, "Main Title", "Subtitle")

# Content slide with bullets
add_content_slide(service, presentation_id, "Slide Title", [
    "First bullet point",
    "Second bullet point"
])

# Custom text box
add_text_box(
    service, presentation_id, slide_id,
    text="Custom text",
    x=inches(1), y=inches(1),
    width=inches(4), height=inches(1)
)

# Image from URL
add_image_from_url(
    service, presentation_id, slide_id,
    image_url="https://example.com/image.jpg",
    x=inches(5), y=inches(1),
    width=inches(3), height=inches(2)
)

# Table
add_table(
    service, presentation_id, slide_id,
    rows=3, cols=2,
    x=inches(1), y=inches(2),
    width=inches(6), height=inches(2),
    data=[
        ["Header 1", "Header 2"],
        ["Row 1 Col 1", "Row 1 Col 2"],
        ["Row 2 Col 1", "Row 2 Col 2"]
    ]
)
```

### Format Slides
```python
from scripts.format_slides import (
    format_text,
    set_shape_fill,
    set_slide_background,
    format_table_cell,
    create_shape,
    BELL_COLORS,
    SLIDE_WIDTH, SLIDE_HEIGHT
)

# Format text
format_text(
    service, presentation_id, object_id,
    start_index=0, end_index=10,
    bold=True, font_size=24,
    color=BELL_COLORS['maroon']
)

# Set slide background
set_slide_background(service, presentation_id, slide_id, 
                     color=BELL_COLORS['white'])

# Create colored shape
create_shape(
    service, presentation_id, slide_id,
    shape_type='RECTANGLE',
    x=inches(0), y=inches(0),
    width=SLIDE_WIDTH, height=inches(1),
    fill_color=BELL_COLORS['maroon']
)
```

## Unit Conversion

```python
from scripts.add_slide_content import inches, points

# EMU = English Metric Unit (Google's internal unit)
# 1 inch = 914,400 EMU
# 1 point = 12,700 EMU

x_position = inches(2)      # 2 inches from left
y_position = inches(1.5)    # 1.5 inches from top
width = inches(6)           # 6 inches wide
font_height = points(24)    # 24pt font
```

## Bell EP Color Palette

```python
from scripts.format_slides import BELL_COLORS

BELL_COLORS['maroon']      # Primary brand color
BELL_COLORS['dark_maroon'] # Darker variant
BELL_COLORS['white']       # Background
BELL_COLORS['light_gray']  # Subtle backgrounds
BELL_COLORS['dark_gray']   # Secondary text
BELL_COLORS['black']       # Primary text
```

## Layout Types

Use with `add_slide()`:
- `BLANK` - Empty slide
- `TITLE` - Title and subtitle
- `TITLE_AND_BODY` - Title with bullet list
- `TITLE_AND_TWO_COLUMNS` - Two column layout
- `TITLE_ONLY` - Just a title
- `SECTION_HEADER` - Section divider
- `ONE_COLUMN_TEXT` - Single column text
- `MAIN_POINT` - Large centered text
- `BIG_NUMBER` - Emphasis on a number

## Common Patterns

### Generate Lesson Slideshow
```python
def generate_lesson_slides(service, title, objectives, activities):
    """Create a standard lesson slideshow."""
    # Create presentation
    pid = create_presentation(service, title)
    
    # Add title slide
    add_title_slide(service, pid, title, "Bell English Program")
    
    # Add objectives
    add_content_slide(service, pid, "Learning Objectives", objectives)
    
    # Add activities
    for i, activity in enumerate(activities, 1):
        add_content_slide(service, pid, f"Activity {i}: {activity['name']}", 
                         activity['steps'])
    
    return pid
```

## API Links

- [Slides API Overview](https://developers.google.com/slides/api/guides/overview)
- [API Reference](https://developers.google.com/slides/api/reference/rest)
- [Batch Update](https://developers.google.com/slides/api/reference/rest/v1/presentations/batchUpdate)
