# Presentation Director Architecture Specification

## 1. Overview
This document outlines the Model-View-Controller (MVC) architecture for generating Reveal.js presentations and Typst worksheets. The goal is to eliminate LLM spatial hallucination by separating content generation (Agent/Controller) from visual rendering (Jinja2/View).

## 2. The Agent's Role: The Presentation Director (Model/Controller)
The agent acts strictly as a "Presentation Director." It does **not** write raw HTML, Markdown, or Typst code for layouts. Instead, it outputs a strict **YAML Manifest** representing the structural and pedagogical intent of the lesson.

### 2.1 Directives Syntax
The agent uses a proprietary bracketed syntax to define interactivity and emphasis within the text content, ensuring spatial awareness is decoupled from the content.

*   `[REVEAL: text]` -> Renders as a Reveal.js fragment (hidden until clicked).
*   `[STRIKE: text]` -> Renders as a strikethrough fragment (for error correction).
*   `[HIGHLIGHT: text]` -> Renders as highlighted text (for emphasis or vocabulary).

## 3. The YAML Manifest Schema
The `presentation.yaml` serves as the single source of truth for a lesson module.

```yaml
presentation:
  title: "Lesson Title"
  theme: "default"
  slides:
    - slide_id: "unique_slide_identifier"
      layout: "title-center" # Enum: title-center, bullet-points, split-screen, big-text, grammar-morph
      split_vertical: false
      background:
        type: "video" # Enum: video, image, color, none
        src: "assets/bg_video.mp4"
        retain_from_previous: false # CRITICAL: seamless background transitions
      animation:
        type: "auto-animate" # Enum: auto-animate, fade, none
      content:
        # Schema varies based on the 'layout' Enum.
        # Example for 'bullet-points' or 'title-center':
        body_text: "Welcome to the lesson. [REVEAL: Let's begin.]"
        
        # Example ONLY for 'grammar-morph' layout:
        morph_elements:
          - data_id: "subject"
            text: "The cat"
            position: "left"
          - data_id: "verb"
            text: "sat"
            position: "center"
```

## 4. The Rendering Engine (The View)
A Python script utilizing Jinja2 templates consumes the `presentation.yaml` and outputs the final artifact (HTML for Reveal.js, or `.typ` for Typst).

### 4.1 Jinja2 Responsibilities
1.  **Directive Parsing**: A custom Jinja filter or pre-processor translates directives into framework-specific syntax.
    *   *HTML*: `[REVEAL: word]` -> `<span class="fragment">word</span>`
    *   *Typst*: `[REVEAL: word]` -> `#pause word` (or equivalent Typst macro)
2.  **Auto-Animate State Tracking**: Jinja manages the injection of `data-auto-animate` attributes and tracks `data-id` elements across slides to ensure smooth transitions without the agent needing to manage the DOM state.
3.  **Background Continuity**: Evaluates `retain_from_previous` to prevent background asset reloading between slides.

### 4.2 Core Template Structure (Reveal.js)
*   `base.html`: The master layout containing the Reveal.js boilerplate.
*   `slide.html`: The generic slide wrapper that handles backgrounds, data-ids, and auto-animate tags.
*   `layouts/`: Sub-templates corresponding to the YAML `layout` Enums (e.g., `title-center.html`, `grammar-morph.html`).

## 5. Next Steps for Implementation
1.  Establish a test suite (pytest).
2.  Write unit tests defining the expected HTML output for various YAML configurations and directives (Red Phase).
3.  Implement the Python/Jinja2 parser to make the tests pass (Green Phase).
4.  Refactor existing Agent skills (`06-creating-html-presentation`) to output this YAML schema exclusively.
