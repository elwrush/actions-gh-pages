---
name: designing-slides
description: >
  Creates Google Slides presentations using the Slides API. Use when the user
  mentions slideshows, presentations, or needs to convert lesson plans into slides.
---

# Designing Slides

**Capability**: Create and manipulate Google Slides presentations programmatically using the Google Slides API.

## Prerequisites

- Google Cloud project with Slides API enabled
- OAuth 2.0 credentials in `.credentials/credentials.json`
- Token file will be auto-generated at `.credentials/token.json` on first run

## Design Principles

| Principle | Implementation |
|-----------|----------------|
| **Expert Pedagogy** | Frame material using analogies/metaphors; don't just copy worksheets |
| **5-7 lines max** | Limit bullet lists to 6 items |
| **One idea per slide** | Generate multiple slides for complex topics |
| **High contrast** | Use Bell maroon/white palette |
| **Large fonts** | Body 24pt+, titles 44pt+ |
| **Visuals over text** | Include images where possible |
| **30-50% white space** | Don't overcrowd slides |
| **Left-align text** | Avoid centering for body text |
| **Two font families max** | Use consistent typography |
| **Accessibility** | Test contrast ratios (WCAG 4.5:1) |

### Pedagogical Framing (Critical)

Do NOT slavishly and mechanistically reproduce the structure of worksheets or lesson plans in slide format. Instead:
- **Frame and Interpret**: Present material as an expert ESL teacher would.
- **Guidance**: Use analogies, metaphors, similes, and models to guide students on HOW to do tasks properly.
- **Scaffolding**: Provide conceptual "mental models" rather than just lists of instructions.

Example:
- *Mechanistic*: "Slide 5: Fill in your worksheet now."
- *Expert*: "Slide 5: **Be the Architect**. Before a house is built, we need a sketch. Sketch your talk on your planning sheet now."

## Slide Content Rules

### Answer Slides
Each answer to a question must appear on its **own slide** containing:
- The answer (highlighted/emphasized)
- A brief explanation
- A supporting snippet from the reading/transcript (where appropriate)

### Vocabulary Slides
Each pre-taught vocabulary item must appear on its **own slide** containing:
- The mandated pattern:
  ```
  word /phonemic script/: Thai translation
  English context sentence with word **highlighted**
  Thai context sentence with word **highlighted**
  ```

### Image Policy

**CRITICAL**: The agent will NEVER attempt to generate images or add image placeholders.

- The user will ALWAYS add images manually post-upload
- Do NOT use `generate_image` tool for slideshows
- Do NOT add image placeholder boxes
- Do NOT suggest image descriptions

Focus solely on text content and layout.

## Title Slide Template Structure

All slideshows MUST use the Bell EP template structure for the title slide:

1. **Dark Header Bar** (top, 1.0" height):
   - Color: `rgb(0.35, 0.05, 0.05)` (darker maroon)
   - Contains logos (Bell + ACT) centered, side-by-side
   - Logo dimensions: 1.0" W x 0.7" H, with 0.3" gap between

2. **Gradient Body** (lighter maroon/red):
   - Background below header bar

3. **"Bell Language Centre" Strap Line**:
   - Position: Below header (y: 1.1")
   - Font: 18pt, white, Arial, centered

4. **Title**:
   - Position: y: 1.7"
   - Font: 36pt, bold, white, Arial, centered
   - Width: 8"

5. **Cover Image** (photorealistic):
   - Square: 2.5" x 2.5"
   - Centered horizontally
   - Position: y: 2.6"
   - Should summarize the lesson theme

**Reference**: See `update_template.py` for exact implementation.

---

## Batch API Pattern (Critical for Performance)

> [!IMPORTANT]
> Always use batch operations. Individual API calls are slow and trigger rate limits.

### Anti-Pattern (Slow)
```python
# ❌ BAD: Each call is a separate network request
slides_service.presentations().batchUpdate(...).execute()  # request 1
slides_service.presentations().batchUpdate(...).execute()  # request 2
# ... 100+ requests = 3-4 minutes
```

### Correct Pattern (Fast)
```python
# ✅ GOOD: Accumulate requests, execute once
all_requests = []

for slide_data in slides:
    slide_id = _generate_id()
    all_requests.extend(get_create_slide_requests(slide_id))
    all_requests.extend(get_content_requests(slide_id, slide_data))

# Single API call with all requests
slides_service.presentations().batchUpdate(
    presentationId=presentation_id,
    body={'requests': all_requests}
).execute()  # 1 request = ~30 seconds
```

### Helper Function Pattern
Functions should **return request dicts**, not execute them:

```python
def get_header_bar_requests(slide_id, title, color):
    """Returns list of request dicts (does NOT execute)."""
    return [
        {'createShape': {...}},
        {'insertText': {...}},
        {'updateShapeProperties': {...}},
    ]
```

---

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
