# Designing Slides

**Capability**: Create and manipulate Google Slides presentations programmatically using the Google Slides API.

## Prerequisites

- Google Cloud project with Slides API enabled
- OAuth 2.0 credentials in `.credentials/credentials.json`
- Token file will be auto-generated at `.credentials/token.json` on first run

## Design Principles

Follow the rules in [`knowledge_base/slide-design-principles.md`](file:///c:/PROJECTS/LESSONS%20AND%20SLIDESHOWS%202/knowledge_base/slide-design-principles.md):

| Principle | Implementation |
|-----------|----------------|
| **5-7 lines max** | Limit bullet lists to 6 items |
| **One idea per slide** | Generate multiple slides for complex topics |
| **High contrast** | Use Bell maroon/white palette |
| **Large fonts** | Body 24pt+, titles 44pt+ |
| **Visuals over text** | Include images where possible |
| **30-50% white space** | Don't overcrowd slides |
| **Left-align text** | Avoid centering for body text |
| **Two font families max** | Use consistent typography |
| **Accessibility** | Test contrast ratios (WCAG 4.5:1) |

### 1. Authenticate

```python
from scripts.authenticate_google import authenticate_slides

service = authenticate_slides()
```

### 2. Create a New Presentation

```python
from scripts.create_presentation import create_presentation

presentation_id = create_presentation(
    service=service,
    title="My Lesson Slideshow"
)
```

### 3. Add Content to Slides

```python
from scripts.add_slide_content import (
    add_title_slide,
    add_content_slide,
    add_image_slide,
    add_table_slide
)

# Add title slide
add_title_slide(
    service=service,
    presentation_id=presentation_id,
    title="Unit 3: Past Progressive",
    subtitle="Bell English Program - M2/4A"
)

# Add content slide with bullet points
add_content_slide(
    service=service,
    presentation_id=presentation_id,
    title="Learning Objectives",
    bullets=[
        "Understand when to use past progressive",
        "Form affirmative and negative sentences",
        "Practice with interactive exercises"
    ]
)

# Add image slide
add_image_slide(
    service=service,
    presentation_id=presentation_id,
    title="Visual Example",
    image_path="images/example.jpg"
)
```

## Workflow

### Basic Workflow
1. **Authenticate** → Get API service
2. **Create presentation** → Get presentation ID
3. **Add slides** → Title, content, images, tables
4. **Format slides** → Apply styling, colors, fonts
5. **Share** → Get shareable link

### Integration with Lesson Plans
1. Read lesson plan from `writing-lesson-plans` skill output
2. Extract key sections (objectives, activities, materials)
3. Generate slides automatically based on lesson structure
4. Upload presentation to Google Slides
5. Return shareable link

## Scripts

### Core Scripts
- `scripts/authenticate_google.py` - OAuth authentication
- `scripts/create_presentation.py` - Create new presentations
- `scripts/add_slide_content.py` - Add content to slides
- `scripts/format_slides.py` - Apply styling and formatting
- `scripts/upload_images.py` - Upload and position images

### Utility Scripts
- `scripts/get_presentation.py` - Retrieve existing presentation
- `scripts/list_slides.py` - List all slides in presentation
- `scripts/delete_slide.py` - Remove specific slides

## Common Operations

### Get Presentation URL
```python
presentation_id = "abc123xyz"
url = f"https://docs.google.com/presentation/d/{presentation_id}/edit"
```

### Apply Template Styling
```python
from scripts.format_slides import apply_bell_theme

apply_bell_theme(
    service=service,
    presentation_id=presentation_id,
    primary_color="#8B0000",  # Maroon
    secondary_color="#FFFFFF"  # White
)
```

### Batch Create Slides from Lesson Plan
```python
from scripts.generate_from_lesson import generate_slideshow

generate_slideshow(
    lesson_plan_path="outputs/lesson-plan-unit3.md",
    output_title="Unit 3 Slideshow",
    include_images=True,
    apply_theme="bell"
)
```

## API Reference

- [Google Slides API Documentation](https://developers.google.com/slides/api)
- [Python Quickstart](https://developers.google.com/slides/api/quickstart/python)
- [API Reference](https://developers.google.com/slides/api/reference/rest)

## Notes

- **Token refresh**: The OAuth token automatically refreshes when expired
- **Rate limits**: Google Slides API has rate limits; use batch operations when possible
- **Image uploads**: Images must be uploaded to Drive first, then referenced by ID
- **Permissions**: Presentations are created in your Drive; share manually or via API
