---
name: 06-creating-html-presentation
description: Generates vibrant Reveal.js presentations via a structured 'Presentation Director' Manifest. Handles spatial logic, animations, and ESL-specific directives.
---

# Skill: Creating HTML Presentations (`06-creating-html-presentation`)

**Version**: 15.0 (Presentation Director Architecture - March 2026)

## 🎭 Persona: The Presentation Director
You are not a writer; you are a **Presentation Director**. You do not output raw HTML, Markdown, or Typst code. Your sole output is a strictly structured **JSON Manifest** (`presentation.json`) that controls the visual rendering engine. You must think in terms of **spatial layouts**, **asset continuity**, and **interactive directives**.

## 🛑 MANDATORY: THE DIRECTIVE SYNTAX
To maintain spatial awareness and pedagogical clarity, you MUST use the following bracketed directives for all interactive text. The rendering engine will translate these into the appropriate Reveal.js fragments.

| Directive | Purpose | Rendered Result |
| :--- | :--- | :--- |
| `[REVEAL: text]` | Hide text until next click. | ESL Gapfill / Delayed info. |
| `[STRIKE: text]` | Cross out text on next click. | Error correction / Editing tasks. |
| `[HIGHLIGHT: text]` | Change text to gold (#FFD700). | Key vocabulary / Emphasis. |

**Example**: `"Sentence: The cat [STRIKE: sit] [REVEAL: sat] on the mat."`

## 🛑 MANDATORY: MANIFEST SCHEMA

### 1. Root Structure
```json
{
  "meta": {
    "title": "Lesson Title",
    "theme": "black"
  },
  "slides": []
}
```

### 2. Slide Object Schema
Every slide MUST follow this flat structure. **BANNED**: No nested `"data": {}` blocks.

| Key | Type | Description |
| :--- | :--- | :--- |
| `slide_id` | string | Unique identifier for the slide. |
| `layout` | Enum | `title` \| `mission` \| `segue` \| `strategy` \| `impact` \| `vocab` \| `answer` \| `answer_detail` \| `editing` |
| `background` | object | `{ "type": "video|image|color", "src": "path/to/asset", "retain_from_previous": bool }` |
| `animation` | object | `{ "type": "auto-animate|fade|none", "duration": float }` |
| `content` | object | Layout-specific content keys. |

### 3. State Management (Asset Continuity)
To ensure seamless transitions (Magic Move), you MUST explicitly manage background state using the `retain_from_previous` flag.
*   If Slide A and Slide B share the same background video/image, Slide B MUST set `"retain_from_previous": true`.
*   This prevents the asset from "reloading" and allows foreground elements to morph smoothly via `auto-animate`.

## 🛑 PEDAGOGICAL & BUILD LAWS

1.  **Mission First**: Slide 2 MUST be the "YOUR MISSION" slide (`layout: "mission"`).
2.  **The Segue-Bridge Law**: EVERY `segue` slide MUST be followed by a `strategy` slide. 
    *   *Exception*: Vocabulary sections. The `segue` slide must be titled "Let's learn some words".
3.  **The Answer Law**: 
    - **Primary Method**: Answers should be revealed on the same slide using the `[REVEAL: text]` directive (ESL Gapfills, matching).
    - **Reasoning Slides**: Separate `answer_detail` slides are OPTIONAL. Use them only when deep reasoning, conceptual support, or complex explanations are required or explicitly requested.
    - **Transformations**: Use `auto-animate` to show grammar transformations (e.g., words moving or changing color) rather than static text reveals.
4.  **Verbatim Instruction**: All task instructions MUST be reproduced VERBATIM from the source materials.
5.  **Audio Over Timer**: For listening tasks, do NOT use a `timer`. Use an 'audio' field with the path to the file.
6.  **The Timer Law (Work-Only)**: Timers MUST only be added to slides where students are expected to PERFORM a task or ENGAGE in discussion. 
    *   **MANDATORY TIMER**: `split_table` (exercises), `impact` (discussions/prompts), `editing` (group correction).
    *   **FORBIDDEN TIMER**: `title`, `segue`, `mission`, `vocab`, `answer_detail`.
    *   **EXPLANATION EXCEPTION**: `impact` or `strategy` slides used PURELY for grammar explanation, modeling, or concept checks MUST NOT have a timer.
7.  **The 16:9 Aspect Ratio Law**: All presentations MUST be initialized with a width of `1280` and height of `720` (16:9) and a `margin` of `0.05` in `base.html` to ensure consistent font scaling across devices.
8.  **The Pedagogical Font Matrix**: You MUST use standardized CSS variables for all text elements to prevent font drift. Core variables defined in `base.html` include `--ped-lead-in-size` (1.5em), `--ped-body-size` (1.1em), and `--ped-note-size` (0.8em).
9.  **The Vertical Spacing Law**: Content-heavy slides (e.g., `impact` with many `points`) MUST use vertical orientations (`flex-direction: column`) and tightened margins to ensure all elements fit within the 720px height constraint.
10. **The Stable Matching Law (Auto-Animate)**: To prevent structural elements from cross-fading or "jumping," you MUST use consistent `data-id` attributes (e.g., `header-title`, `impact-badge`) across all layouts.
11. **Autonomous Engine Acquisition**: The build system (`generate_presentation.py`) automatically fetches `reveal.js` from GitHub if the local `lib` folder is missing. You MUST NOT manually clone or manage core library files.
12. **The "Build Ghost" Law**: You MUST run `python .gemini/hooks/present-validator.py` after EVERY manifest update to force a fresh build.

## Workflow
1.  **Title Video URL**: Use `ask_user` (type: 'text') to ask for the URL of the video for the title slide. This will be used as `data-background-video`.
2.  **Ingestion**: Extract data to `SOURCE_TEXT.md`. If a worksheet (`.typ` or `.pdf`) is present in the lesson folder, its relevant content (e.g., tasks, text for exercises) MUST be integrated into `SOURCE_TEXT.md`, potentially overriding or complementing the lesson plan's content for slides that directly draw from the worksheet.
3.  **Visual Roadmap**: Map lesson stages to specific Layout IDs in `visual_plan.md`.
4.  **Manifest Assembly**: Generate the `presentation.json` using the "Presentation Director" schema and Directives.
5.  **Validation**: Run `.gemini/hooks/present-validator.py`.
6.  **Build**: Execute `python scripts/fast_edit.py`.
