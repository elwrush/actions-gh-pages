---
name: creating-html-presentation
description: Generates vibrant Reveal.js HTML presentations (slideshows) from lesson plans with high-energy visuals, timers, and answer keys.
---

# Skill: Creating HTML Presentations (`creating-html-presentation`)

**Version**: 4.0 (Local Reveal.js Core + Pixel-Perfect Standards)

## Description
This skill generates vibrant, high-energy HTML presentations using **Reveal.js** via a Python generator script. It transforms lesson plans into dynamic, web-based experiences with "pop and verve." This version relies on a local Reveal.js distribution (in `reveal_core/`) to ensure offline reliability and perfect rendering.

## ⛔ MANDATORY CO-LOCATION & ROOT BAN (READ FIRST)

> [!CRITICAL]
> **ROOT FOLDER BAN**: You are STRICTLY FORBIDDEN from creating any lesson files (PDFs, Typst, Images, HTML) in the Project Root (`C:\PROJECTS\LESSONS AND SLIDESHOWS 2\`).
> 
> **Canonical Location**: ALL files MUST be created inside a dedicated subfolder in `inputs/` (e.g., `inputs/28-01-2026-B1-Match-Girl-E/`). This applies to the Lesson Plan, Slideshow, Images, worksheets, and assets. Completed and approved materials should be moved to a `published/` sub-subdirectory.

> [!CRITICAL]
> **PREREQUISITE**: You MUST NOT generate a presentation until the corresponding Lesson Plan has been EXPLICITLY APPROVED by the user.
> 
> **ALL presentation files (`index.html`, `images/`, `audio/`) MUST be created inside the SAME folder as the lesson plan and worksheet.**
> 
> **Canonical Location**: `inputs/[QAD-folder]/` (e.g., `inputs/QAD-Fight-or-Flight/`)
>
> [!IMPORTANT]
> **IGNORE GDRIVE SYSTEM FILES**: Always ignore `desktop.ini` and other hidden system files created by Google Drive synchronization. These files should never be included in the presentation assets or copied to `dist/`.

## Workflow

## Workflow

### Step 0: 🧠 Context Check (CRITICAL)
1. **Ingest History**: You MUST read `errors-fix.md` before generating any presentation to ensure previous mistakes (e.g., iframe fullscreen issues, layout stacking, malformed titles) are not repeated.
2. **Review Updates**: Check if any new layout rules (e.g., "Horizontal-First") apply to your current task.

### Step 1: 📋 Source Check (MANDATORY)
1.  **Check Context**: Ensure you are in a valid lesson folder with a lesson plan (`.typ`/`.md`) and worksheet.
2.  **Extract Content**: Create a checklist of tasks from the source materials. Use "Task" nomenclature (e.g., "Task 1", "Task 2").
3.  **Validate**: Show this checklist to the user.

### Step 1.5: 📐 Flow Visualization & Audit (Drift Check)
1.  **Activate**: `skills/rendering-prompts-into-mermaid/SKILL.md`.
2.  **Generate Flowchart**: Create a Mermaid `graph TD` mapping the Lesson Plan to specific Slide Nodes.
3.  **Strict Node Annotation**:
    -   Each node MUST identify its **Layout** (e.g., `[Strategy Slide]`, `[Task 4: Split Video]`).
    -   Multimedia nodes MUST include **Timestamps** (e.g., `Video: 01:17-01:35`).
    -   Task nodes MUST confirm **"Anti-Echo"** logic (e.g., `Options: Rephrased/Mixed`).
4.  **Pedagogical Visual Check**:
    -   Does a **Strategy Node** appear before every Task Node?
    -   Does a **Video Answer Node** immediately follow the Task?
    -   **Pedagogical Mandate**: Does a **Contextualization Slide** appear immediately after the Lead-in? This slide MUST explain the lesson objective in a student-centered way (e.g., "Today we're making you a better reader! By the end of the lesson you'll...").
6.  **Stop & Confirm**: Present this graph to the user. Do NOT proceed to code generation until the flow is approved.

### Step 2: 📦 Asset Strategy (External Generation)
**Goal**: Create high-quality visual aides via external user-led generation.

1.  **Generation Strategy (User-Led)**:
    -   **CRITICAL RULE**: Do NOT attempt to generate images internally using `generate_image`.
    -   **Action**: Provide the user with highly detailed, cinematic prompts for all required visuals (Title, Vocab, Lead-ins).
    -   **Wait**: You MUST stop all automated progress and wait for the user to provide the generated image files.
    -   **Action**: Once the user provides the images, copy/move them to the canonical `images/` folder within the lesson directory.

2.  **Pixabay Strategy (Fallback)**:
    -   Only use `skills/searching-pixabay/SKILL.md` if the user explicitly requests a photographic fallback or if external generation is not feasible.

3.  **Attribution Rules**:
    -   **AI Images**: DO NOT include any attribution text.
    -   **Pixabay Images**: MUST include attribution (e.g., "Image by [User] from Pixabay").
    -   **Styling**: Attribution text must be **10pt**, subtle, and placed directly beneath the image.

4.  **Organization Rule**:
    -   ALL images must be saved to `inputs/[Lesson]/images/`.
    -   ALL audio must be saved to `inputs/[Lesson]/audio/`.
    -   **Never** leave assets in the root folder.

### Step 3: 🎨 Config Generation (JSON)
Generate `presentation.json`. Use **Auto-Animate** (`data-auto-animate`) liberally for smooth transformations (e.g., Vocabulary matching, Grammar rules, Sentence changes). By using stable `data-id` attributes on elements across slides, Reveal.js will automatically morph them.

**Tone & Typography Guide**:
-   **Persona**: Warm, friendly, and engaging ESL Teacher.
-   **Voice**: Use short sentences and simple words. Avoid academic jargon.
-   **Typography**: NEVER use all-caps for headers or body text (except Title Deck 1).
-   **Color Palette Rule**: You MUST select a cohesive **Color Palette** (e.g., Noir, Cyber, Pastel) before generating the JSON. This ensures visual consistency across all slides.
-   **NO VISIBLE TIPS**: NEVER include "Teacher Tips", "Pro Tips", or "Pedagogical Advice" on the actual slide surface. This information belongs EXCLUSIVELY in the `notes` field for the speaker view.
-   **Context Slide Rule**: You MUST include a "Contextualization" slide after the Lead-in. It sets the student's personal goal for the lesson.
-   **Video Slide Rule**: YouTube slides MUST include 3 directive bullet points (talking points/questions) to guide viewing. Never just say "Watch this."
-   **Layout Philosophy**: Always utilize the full 16:9 horizontal space. Avoid centered "boxes in the middle".

## 📐 Layout Philosophy (16:9 Optimization)

Reveal.js presentations are 16:9. Always use horizontal space efficiently:
- ❌ **DON'T**: Create centered boxes with content stacked vertically.
- ✅ **DO**: Use split layouts (40/60, 50/50, 60/40) for most slides.
- ✅ **DO**: Place images/media on one side, text on the other.
- ✅ **DO**: Use full-width grids for checklists and multi-item content.

### Patterns:
- **Vertical Center**: ONLY for segue slides or very short, single-sentence quotes.
- **Split 40/60**: Image left (40%), content right (60%) - Default for vocab and tasks.
- **Split 60/40**: Content left (60%), media right (40%).
- **Split 50/50**: Video + Questions side-by-side.

### 🌟 New Design Standards (2026 Updates)
1.  **Strategy Slide Pattern**:
    -   **Mandatory**: Every Speaking/Listening task MUST have a preceding "Strategy" slide.
    -   **Style**: Emoji Bullet Points (e.g., 🗣️ **Speak**, 🌍 **Connect**) instead of standard bullets.
    -   **Content**: Focus on *how* to do the task, not just instructions.

2.  **Video Answer Logic (Combined Card)**:
    -   **Layout**: 50/50 Split.
    -   **Left**: Replay Video Clip (iframe) with precise start/end times.
    -   **Right**: **Combined Analysis Card**.
        -   **Top**: CORRECT ANSWER (Bold, Large).
        -   **Bottom**: EVIDENCE/TRANSCRIPT (Typewriter font, highlighted keywords, font size ~22-24px).

3.  **Anti-Echoing Rule (Pedagogical)**:
    -   **Checklists/Options**: Must **NOT** directly echo the transcript audio.
    -   **Validation**: Rephrase the options (e.g., "Rare event" -> "Unusual occurrence") and **Reorder** them so they do not match the video sequence.

4.  **Auto-Animate Checklists**:
    -   **Question Slide**: Unchecked items `[ ]`.
    -   **Answer Slide**: Checked items `[✓]` with Green/Bold styling.
    -   **Tech**: Use matching `data-id` attributes on both slides to enable smooth morphing.

5.  **Compact Layouts**:
    -   For Split Task slides, use **30px padding** (not 40px) inside glass boxes to prevent vertical overflow.
    -   Header sizes: ~45px. Body text: ~24px.


**Command**:
```bash
python skills/creating-html-presentation/scripts/generate_presentation.py inputs/[Lesson-Folder]/presentation.json
```

**JSON Structure**:
```json
{
  "meta": {
    "title": "Lesson Title",
    "subtitle": "Subtitle",
    "theme": "indonesia", // See css/themes/
    "mode": "intensive" // or "bell"
  },
  "slides": [
    {
      "layout": "title",
      "badge": "B1 INTENSIVE READING",
      "title": "THE FOOD OF INDONESIA",
      "image": "images/cover.jpg",
      "attribution": "Pixabay"
    },
    {
      "layout": "segue",
      "phase": "PHASE 1",
      "title": "SITUATION & VOCAB"
    },
    {
      "layout": "vocab",
      "word": "DOMESTIC",
      "phoneme": "/dəˈmes.tɪk/",
      // THAI TRANSLATIONS ARE BANNED because they are often inaccurate.
      // DEFINITIONS ARE BANNED. Use Context Sentence only.
      "context_sentence": "Most rice is for <span style='color: var(--accent);'>domestic</span> use.",
      "image": "images/satay.jpg"
    },
    {
      "layout": "split_task",
      "title": "PREDICTION",
      "badge": "TASK 1",
      "timer": 3,
      "image": "images/cover.jpg",
      "content": "<p>Recall the video...</p>",
      "notes": "Ask students what they see in the picture. Elicit keywords like 'border' or 'patrol'."
    }
  ]
}
```

### Step 4: 🛠️ Speaker Notes (MANDATORY)
Every slide MUST have specific `notes` in the JSON. These notes should provide the teacher with:
1.  **Pedagogical Advice**: What to ask, what to check (CCQs), how to drill.
2.  **Procedural Hints**: "Start the timer now," "Move to groups."
3.  **Transition Cues**: What is coming on the next slide.

### Step 5: 🛠️ Generation
Run the python script. It will:
1.  Read the JSON.
2.  Load Jinja2 templates from `templates/`.
3.  Render `index.html`.
4.  Copy required assets (`audio/`, shared JS).
5.  **Save Output**: The script will save `index.html` to the lesson folder. For final publication, ensure it resides in (or is mirrored to) the `published/` subfolder if requested by the user.

### Step 5: 🧪 Validation
Run the existing validators to ensure the output is perfect.
- `python skills/creating-html-presentation/scripts/validate_presentation.py`
- `python skills/creating-html-presentation/scripts/validate_pedagogical.py`

## Available Layouts (The Catalog)

1.  **`title`**: Gold Standard Split: Deck 1 (ALL CAPS) & Deck 2 (Title Case).
2.  **`segue`**: Heavy Radial Gradient with Skewed Phase markers.
3.  **`vocab`**: Glass-box container with Phonics support. (Note: Thai translations are BANNED).
4.  **`split_task`**: 35/65 Cinematic Split (Image Left / Task Glass-box Right).
5.  **`video`**: Embeds YouTube/Shorts + Floating Task Box.
6.  **`checklist`**: Grid of items for "Skim" tasks.
7.  **`answer`**: Validation slide with "Why?" explanation box.
8.  **`video_answer`**: 40/60 Split: Video clip (Left) / Answer + Transcript + Explanation (Right).
9.  **`strategy`**: Scaffolding slide.
    -   **Usage**: MUST appear before complex Tasks/Answers (e.g., Inference, Irony).
    -   **Content**: Focus on keywords (e.g., "Seemed to be") or concepts (e.g., "Irony") rather than giving the answer.
10. **`matching`**: Interactive Vocabulary Match.
    -   **Auto-Animate Rule**: Use `data-auto-animate`.
    -   **Stability Rule**: Ensure the Left Column (Words) is **Identical** in the `pairs` array for both Question and Answer slides.
    -   **ID Rule**: Use `data-id="fixed-word-{{id}}"` for words and `data-id="moving-def-{{id}}"` for definitions.
    -   **Animation**: Only the definitions (Right Column) should move.

## ⚠️ Technical Pitfalls (Learned Lessons)

1.  **Segue Transitions**:
    -   ❌ **NEVER** use `data-auto-animate` on Segue slides. It effectively disables the 'Zoom' transition if the previous slide has matching elements.
    -   ✅ **ALWAYS** rely on standard `data-transition="zoom"` for Segues to create a hard phase break.

2.  **Answer Context**:
    -   ❌ **NEVER** use short snippets (e.g., "...her father...").
    -   ✅ **ALWAYS** use full verbatim sentences that contain the **reasoning** (e.g., "She was afraid *because her father would be angry*"). The "Why" must be visible in the text.

3.  **Canvas Clipping**:
    -   ❌ **NEVER** position decorative elements (SVGs) with negative coordinates (e.g., `top: -10%`). They will be clipped and invisible on the slide canvas.
    -   ✅ **ALWAYS** keep elements within 0-100% or set `overflow: visible` explicitly (though risky).

## Assets
-   **Images**: Same rules apply (Pixabay first, Attribution mandatory).
-   **Audio**: The script automatically copies `blip.mp3`, `bell.mp3`, etc.

## CSS Themes
Themes are defined in `skills/creating-html-presentation/css/themes/`.
Available: `indonesia.css`, `thai-heritage.css` (Gold Standard), `noir.css`, `cyber.css`.
