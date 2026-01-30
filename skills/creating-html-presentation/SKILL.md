---
name: creating-html-presentation
description: Generates vibrant Reveal.js HTML presentations (slideshows) from materials and instructions with high-energy visuals, timers, and answer keys.
---

# Skill: Creating HTML Presentations (`creating-html-presentation`)

**Version**: 4.0 (Local Reveal.js Core + Pixel-Perfect Standards)

## Description
This skill generates vibrant, high-energy HTML presentations using **Official Reveal.js Native Patterns**. We have abandoned custom CSS containers and fragile template wrappers in favor of the library's core classes (`r-fit-text`, `r-stretch`) and standard semantic HTML (`<table>`, `<ul>`). This ensures perfect stability, responsive scaling, and high performance across all devices.

## 💎 The "Native Core" Standards (2026 Update)
1. **Zero-Box Philosophy**: NEVER create custom `div` boxes for text backgrounds.
    - **Visibility**: Use `data-background-opacity="0.5"` (Dimming) on task slides.
    - **Contrast**: Global `text-shadow: 2px 2px 8px rgba(0,0,0,0.9)` is applied to all slide text.
2. **Gradient Overlays**: Title and transition slides MUST use `data-background-gradient` (e.g., `linear-gradient(to right, rgba(0,0,0,0.9), rgba(0,0,0,0))`) to anchor text.
3. **Mission Badges**: Learning objectives on the Mission slide must be **Square Badges** (minimal border-radius, background tint, small width ~180px) to prevent screen spillover.
4. **Table Logic**: Use native `<table>` for all answer keys and data comparisons.
5. **Flex Layouts**: Prefer `display: flex` centering for complex slides with timers to ensure vertical alignment doesn't clip content. Avoid over-reliance on `r-stack`.

## ⛔ MANDATORY CO-LOCATION & ROOT BAN (READ FIRST)

> **Canonical Location**: ALL files MUST be created inside a dedicated subfolder in `inputs/` (e.g., `inputs/28-01-2026-B1-Match-Girl-E/`). This applies to the Materials, Slideshow, Images, worksheets, and assets. Completed and approved materials should be moved to a `published/` sub-subdirectory.

> [!CRITICAL]
> **PREREQUISITE**: You MUST NOT generate a presentation until the Materials and User Instructions have been EXPLICITLY APPROVED by the user.
> 
> **ALL presentation files (`index.html`, `images/`, `audio/`) MUST be created inside the SAME folder as the source materials and worksheet.**
> 
> **Canonical Location**: `inputs/[QAD-folder]/` (e.g., `inputs/QAD-Fight-or-Flight/`)
>
> [!IMPORTANT]
> **IGNORE GDRIVE SYSTEM FILES**: Always ignore `desktop.ini` and other hidden system files created by Google Drive synchronization. These files should never be included in the presentation assets or copied to `dist/`.

## Workflow

### Phase 0: 🧠 User Discovery & Architecture (MANDATORY GATED STEPS)

You MUST NOT proceed to any code or image generation until the following questions are answered and the resulting architecture is approved.

1.  **Level Check**: Which CEFR level is this for (e.g., B1, B2)?
2.  **Skill Check**: Which specific skill is being targeted (e.g., Reading, Speaking)?
3.  **Materials Ingestion**: What are the source materials? (Read `raw_content.md`, textbook scans, etc.).
4.  **Special Requests**: Do you have any specific high-energy requirements or design preferences?
5.  **Learning Objectives**: What MUST the students be able to do by the end of the lesson? (The "Mission").
6.  **Architecture Proposal**: 
    -   Generate a markdown file (e.g., `slide_architecture.md`) detailing the slide-by-slide plan.
    -   Include: Slide Number, Title, **Layout Pattern** (Pattern Catalog), **Media Requirement**, and **Pedagogical Goal**.
    -   **Wait for Approval**: notify_user and wait for explicit approval of this architecture.

### Phase 1: 📊 Pedagogical Mapping (Mermaid)

Once Phase 0 is approved, visualize the flow:
1.  **Activate**: `skills/rendering-prompts-into-mermaid/SKILL.md`.
2.  **Generate Flowchart**: Create a Mermaid `graph TD` mapping the Materials and Instructions to specific Slide Nodes.
3.  **Mandatory Nodes**:
    -   Include a **"Discovery"** node.
    -   Include a **"Linguistic Alignment"** node (CEFR profiling).
4.  **Strict Node Annotation**:
    -   Each node MUST identify its **Layout** (e.g., `[Strategy Slide]`).
    -   Multimedia nodes MUST include **Timestamps**.
    -   Task nodes MUST confirm **"Anti-Echo"** logic.
5.  **Stop & Confirm**: Present this graph to the user. Do NOT proceed to code generation until the pedagogical flow is approved.
6.  **Visual Reference**: Refer to `skills/creating-html-presentation/WORKFLOW_VISUAL.md` for the technical mapping.

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
- **Full-Screen Background Rule**: You MUST present ALL images as full-screen backgrounds using `<section data-background="images/your-image.jpg">`. Use `data-background-opacity="0.5"` (Dimming) for task slides to ensure white-text contrast.
- **Contrast & Gradient Rule**: Apply `data-background-gradient="linear-gradient(to right, rgba(0,0,0,0.9), rgba(0,0,0,0))"` to title and transition slides.
- **Mission Slide Background Rule**: The "Mission" slide MUST use: `https://elwrush.github.io/lesson-plan-agent/images/mission_bg_clipped.mp4`. Call it using `data-background-video` with `data-background-video-muted` but **WITHOUT** `data-background-video-loop`. It must auto-start and play once.
- **Badge Styling Rule**: Objectives on the Mission slide must be presented as **Badges** (background color + rounded corners) rather than simple list items.
- **Timer Rule**: All timers MUST include a **Reset** button and trigger **Audio Cures** (bell.mp3) upon completion. The start button MUST toggle to a **Pause** state when active.

## 📐 Layout Philosophy (16:9 Optimization)

Reveal.js presentations are 16:9. Always use horizontal space efficiently:
- ❌ **DON'T**: Create centered boxes with content stacked vertically.
- ❌ **DON'T**: Use inset images for main content.
- ✅ **DO**: Use full-screen backgrounds (`data-background`) for all image slides.
- ✅ **DO**: Use glass-box containers for text overlays on top of backgrounds.
- ✅ **DO**: Use full-width grids for checklists and multi-item content.

### Patterns:
- **Vertical Center**: ONLY for segue slides or very short, single-sentence quotes.
- **Split 40/60**: Image left (40%), content right (60%) - Default for vocab and tasks.
- **Split 60/40**: Content left (60%), media right (40%).
- **Split 50/50**: Video + Questions side-by-side.

### 🌟 New Design Standards (2026 Updates)
1.  **Full-Screen Image Pattern**:
    -   **Layout**: `data-background` attribute on `<section>`.
    -   **Styling**: Use a semi-transparent glass-box to ensure text readability.

3.  **Mission Slide Pattern**:
    -   **Layout**: `data-background-video="https://elwrush.github.io/lesson-plan-agent/images/mission_bg_clipped.mp4"`.
    -   **Looping**: MUST be set to `false`.
    -   **Badges**: Standard square badges (10% smaller than default) to prevent overflow.

4.  **Anti-Echoing Rule (Pedagogical)**:
    -   **Checklists/Options**: Must **NOT** directly echo the transcript audio.
    -   **Validation**: Rephrase the options and **Reorder** them.

5.  **Native Answer Tables**:
    -   **Layout**: Native HTML `<table>`.
    -   **Columns**: Always include context (e.g., "Name" column for "Who said what").
    -   **Scaling**: Use `font-size: 0.8em` for tables to ensure fit.


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
