"""
Package init for designing-slides scripts.
"""

from .authenticate_google import authenticate_slides, authenticate_docs, authenticate_drive
from .create_presentation import create_presentation, get_presentation, list_slides, delete_slide
from .add_slide_content import (
    add_slide,
    add_title_slide,
    add_content_slide,
    add_text_box,
    add_image_from_url,
    add_table,
    populate_table,
    inches,
    points,
    INCH_TO_EMU,
    PT_TO_EMU
)
from .format_slides import (
    format_text,
    set_shape_fill,
    set_slide_background,
    format_table_cell,
    apply_bell_theme_to_slide,
    create_shape,
    BELL_COLORS,
    SLIDE_WIDTH,
    SLIDE_HEIGHT
)
