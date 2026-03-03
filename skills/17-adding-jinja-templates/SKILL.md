---
name: 17-adding-jinja-templates
description: Seamlessly adds new Jinja layouts to the Presentation Director engine (e.g., YouTube video templates, new interactive layouts).
---

# Skill: Adding Jinja Templates (`17-adding-jinja-templates`)

## Description
This skill provides a standardized workflow for expanding the Presentation Director's capabilities by adding new Jinja2 templates for Reveal.js slides. Use this skill when the existing layouts (e.g., `title`, `split_table`, `strategy`) are insufficient for a new pedagogical requirement, such as embedding a YouTube video or creating a novel interactive component.

## Core Mandates
1.  **Strict MVC Adherence**: New templates MUST act solely as the "View". They must not contain hardcoded lesson content. All dynamic content must be interpolated via Jinja `{{ slide.variable_name }}`.
2.  **Directive Integration**: Any text field that could contain interactive elements (like `[REVEAL: text]` or `[HIGHLIGHT: text]`) MUST be passed through the `parse_directives` filter (e.g., `{{ slide.title | parse_directives | safe }}`).
3.  **Macro Usage**: Always leverage existing macros (like `render_background` or `auto_element`) instead of rewriting boilerplate reveal.js tags.

## Workflow

### Stage 1: Template Creation
1.  Navigate to `skills/06-creating-html-presentation/templates/layouts/`.
2.  Create a new HTML file named after the layout (e.g., `youtube_video.html`).
3.  Implement the HTML structure.
    *   Do NOT wrap the content in a `<section>` tag. The outer `slide.html` wrapper handles the `<section>` tag, background transitions, and auto-animate properties automatically (unless your template explicitly requires multiple vertical `<section>` tags, in which case it handles its own wrapping like `editing.html`).
    *   Use inline styling or the existing global CSS classes (e.g., `slide-canvas`, `mission-badge`).

**Example: `youtube_video.html`**
```html
<div class="slide-canvas">
    <h2 style="color: #FFD700; text-shadow: 2px 2px 8px black;">{{ slide.title | parse_directives | safe }}</h2>
    <div style="margin-top: 20px;">
        <iframe width="{{ slide.width | default(800) }}" height="{{ slide.height | default(450) }}" 
                src="https://www.youtube.com/embed/{{ slide.youtube_id }}" 
                frameborder="0" allowfullscreen></iframe>
    </div>
    {% if slide.instruction %}
        <p style="font-size: 1.2em; margin-top: 20px;">{{ slide.instruction | parse_directives | safe }}</p>
    {% endif %}
</div>
<aside class="notes">{{ slide.notes | default('Play the video.') }}</aside>
```

### Stage 2: Schema Registration
1.  Open `skills/06-creating-html-presentation/SKILL.md`.
2.  Locate the **MANDATORY: MANIFEST SCHEMA** section.
3.  Update the `layout` Enum to include your new layout ID (e.g., add `| youtube_video`).
4.  If your new layout introduces mandatory specific keys (like `youtube_id`), document them if necessary.

### Stage 3: Validation & Testing
1.  Create a dummy `presentation.json` that uses the new layout.
2.  Run the build script `python skills/06-creating-html-presentation/scripts/generate_presentation.py <path_to_json>` to verify the engine compiles the template correctly.
3.  Open the generated `index.html` to confirm the visual rendering and directive parsing work as expected.
