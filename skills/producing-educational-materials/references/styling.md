# Educational Materials Styling Standards

This document defines the high-density Typst production standards for professional, branded worksheets.

## 1. Typography & Readability
- **Body Text**: Use **Arial 13pt** for all body text. This is the global project standard for clarity.
- **Focus Passages**: Use **Arial 13pt** (Bold for emphasis) for core reading texts. Avoid 16pt unless a specific visual "breakaway" is required.
- **Leading**: Use **0.55em** for body text leading.
- **Justification**: Text MUST be **left-justified** (ragged right). NEVER use full justification.

## 2. Layout & Spacing
- **Top Padding**: Always provide minimal space (e.g., `#v(0.1cm)`) between the top logo and the badges/hero strap.
- **Badge Positioning**: Badges MUST always be placed on the **top-left**, above the hero strap.
- **Mission Slides/Sections**:
    - Include a hook explaining relevance to the exam (e.g., B1 PET, B2 First).
    - Apply a dark vignette or gradient overlay (`data-background-gradient`) to backgrounds to ensure white text remains readable.
    - Use 3 distinct boxes (square badges) for core objectives with icons (plane, book, pen, etc.).

## 3. Interaction & Writing Space
- **Handwriting Space**: ALWAYS provide at least **0.8cm - 1.2cm** of clear vertical space between a prompt and the writing line.
- **Writing Lines**: Use **0.9cm** line spacing via `#writing_lines_dynamic(line-spacing: 0.9cm)`.
- **Numbered Lists**: 
    - Use native Typst numbering (`+`).
    - Numbers must be **boldfaced**.
    - Implementation: `#set enum(numbering: n => [*#n.*])`.

## 4. Visual Elements
- **Cinematic Headers**: Use full-width banners with overlay text.
- **Branding**: 
    - **Bell**: Assets in `C:\Users\elwru\AppData\Roaming\typst\packages\local\bell-sheets\0.1.0\images\`.
    - **Intensive**: Use specific branded straps as requested.
