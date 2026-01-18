---
name: developing-bespoke-materials
description: >
  Creates custom educational materials tailored to CEFR levels and skill types. Use when
  the user wants to design worksheets, transform textbook content, or develop new teaching materials.
---

# Developing Bespoke Materials

## Purpose
Guide the creation of custom educational materials tailored to specific CEFR levels, skills, and program types. Supports both transforming existing materials and developing brand new content.

---

## Workflow

### Step 1: Initial Consultation
Gather requirements BEFORE generating any content:
- **CEFR Level**: A1, A2, B1, B2, C1, or C2
- **Skill/System**: Reading, Listening, Writing, Speaking, Grammar, Vocabulary, or Pronunciation
- **Duration**: Ask "How long is this lesson?" (e.g., 46 minutes, 50 minutes, 90 minutes)

### Step 2: Material Source
Ask the user:
> Are you mainly wishing to **transform existing materials** or **write brand new materials**?

### Step 3: Program Type
Ask the user:
> Are you creating these materials for **regular classes** (Bell) or the **Intensive program**?

### Step 4: Layout & Assets
Ask the user:
> 1. **Do you require images or diagrams** in this material? 
>    If so, should the text **wrap around them** (using `meander`) or should they be placed in blocks?
> 2. **Do you want to include a Name and Student ID block?** (Default is usually 'yes', but confirm).

### Step 5: Design Strategy
Before proceeding to content development, define the visual strategy. 

> [!NOTE]
> Shift from **Modular/Functional** (boxing content) to **Creative/Editorial** (magazine style).

1.  **Layout Density**:
    *   Prioritize **High Density**. Eliminate "wasted" whitespace.
    *   Use **2-Column Grids** for reading texts and exercises (`#grid(columns: (1fr, 1fr))`) to maximize content per page.
    *   Avoid huge, empty headers. Use **Cinematic Titles** (full-width graphical banners with overlay text) that are compact (`height: 4cm`) but visually impactful.

2.  **Visual Components**:
    *   **Immersive Wrappers**: Use metaphor-driven containers (e.g., a "Tablet UI" frame for corporate profiles, a "Notepad" for informal texts) instead of generic line borders.
    *   **Bespoke Helpers**: Use specific accent colors (e.g., Teal/Maroon) for "Language Help" boxes rather than generic "Info" styles.

### Step 5.5: 🧪 Validation (Delegated)
**Note**: This orchestration skill delegates validation to its output skills:
- **Typst Worksheets**: Use `generating-worksheets/scripts/validate_worksheet.py`
- **HTML Materials**: Use `creating-html-presentation/scripts/validate_presentation.py`
- **Lesson Plans**: Use `writing-lesson-plans/scripts/validate_lesson_plan.py`

You MUST run the appropriate validator after generating any output.

### Step 6: Development Phase

#### General Principles
1.  **Header Images**:
    -   **Regular/Bell**: ALWAYS use `../images/bell-header.jpg`.
    -   **Intensive**: ALWAYS use `../images/intensive-header.jpg`.
    -   *Do not* attempt to generate custom headers unless explicitly requested AND the standard headers are unsuitable.
2.  **Input Verification**:
    -   **Hallucination Check**: When rewriting sentences or transforming text, **strictly verify** the output against the source. Do not invent new facts (e.g., changing "start a business" to "fly a plane").
3.  **Typst Technicals**:
    -   **Gap Fills**: NEVER use underscores (`___`). Use `#box(width: 1.5cm, stroke: (bottom: 1pt + black))` for robust rendering.
    -   **Writing Lines**: Use `0.85cm` vertical spacing for optimal compactness. Use `rgb("#404040")` (dark grey) dotted lines for visibility when photocopied.

#### If Transforming Existing Materials:
1. Suggest using **Gemini 3 Flash's multimodal image capabilities** to read source materials
2. Ask user to provide images/scans of the source materials
3. Extract and analyze the content
4. Work in dialog with the user to adapt and transform the materials

#### If Writing Brand New Materials:
1. Discuss the topic, context, and learning objectives with the user
2. Determine required content types:
   - 📖 Reading texts
   - 🎧 Audio scripts (for listening)
   - 🎬 **Multimedia Assets**: Identify YouTube links or record/locate `.m4a`/`.mp3` audio files.
   - 🖼️ Images (use `generate_image` tool ONLY for content illustrations, not layout elements)
3. Collaborate iteratively to develop the content

### Step 7: Draft & Approval
1. Develop all materials in **Markdown format** first for content clarity, OR directly in HTML if the design is complex.
3. **Do NOT open the file in a browser or external viewer automatically.**
4. **MANDATORY PDF LINK GATE**: You MUST provide a **clickable link** to the generated file (PDF or HTML) in the chat immediately after generation. Use the `file:///` protocol for absolute paths.
5. **Wait for explicit approval** of the visual material before proceeding to any next steps (like Lesson Plans).

### Step 7.5: 🛑 MANDATORY PDF LINK (READ CAREFULLY)
> [!CRITICAL]
> **YOU MUST NOT PROCEED TO LESSON PLANNING UNTIL THE USER HAS SEEN THE LINK.**
> 
> **Action**: Post the clickable `file:///` link to the PDF/HTML file.
> 
> **Why**: The user needs to visually verify the layout, branding, and images before you invest time in the pedagogy.

### Step 8: Export & Format

#### For Materials (PDF Output)
1. Use the **Typst-based** `generating-worksheets` skill. 
2. **Gold Standard**: ALWAYS reference `knowledge_base/templates/grammar_repair_worksheet_gold.typ`.
3. Create a `.typ` template in `skills/generating-worksheets/templates/`.
4. Compile using the Typst CLI (see `generating-worksheets/SKILL.md`).
5. **FORBIDDEN**: Do not use HTML fragments for printable worksheets. Use Typst only.
6. **IDE PREVIEW**: Provide a clickable link in the chat for the user to review the PDF within the IDE. Do NOT use `Start-Process` or `os.startfile` on PDF files.
7. Open the resulting PDF locally for user validation before publishing.

7.  **Publish & Archive**:
    - Ask the user: "Do you want to publish this to Google Drive?"
    - **Cloud Upload**: Use `publishing-worksheets` skill.
    - **Local Sync**: Copy the PDF to `G:\My Drive\A CLASSES- ED - TERM 2\M24A - M3-3A`.
    - *(Ensure naming convention is strictly followed)*

#### For Lesson Plans (GDocs Output)
- **File Location**: Save the final HTML in `inputs/[Topic]/`.
- **Styling**:
    -   **Colored Boxes**: ALWAYS use **single-cell tables** (`<table><tr><td style="background: ..."> ... </td></tr></table>`) for rule boxes, examples, or exercise containers. `<div>` background colors are often stripped by Google Docs.
    -   **No Horizontal Rules**: Do not use `<hr>` tags. Use spacing or border-bottom on headers if separation is needed.
    -   **GDocs Compatibility**:
        -   **ZERO MARGINS**: Always set `p, h1, h2, ul { margin: 0; padding: 0; }` in CSS to override Google Docs defaults. Add controlled bottom margin (e.g., `margin-bottom: 8pt`) only where needed.
        -   **Compact Headers**: Set `margin-bottom: 0` and `padding-bottom: 0` for H1 and H2 to avoid large white gaps.
        -   Use `pt` units (e.g., `11pt`) instead of `px`.
        -   Use inline styles for everything important.
        -   Avoid `flexbox` and `grid`.
    -   **Colors**: Use high-contrast colors (e.g., Bell Maroon `#A62D26`, Deep Blue `#2196F3`).

---

## Conversation Starters

Use one of these to begin the workflow:

```
Hello! I'm here to help you create bespoke educational materials.

To get started, please tell me:
1. What **CEFR level** are you targeting? (A1, A2, B1, B2, C1, C2)
2. What **skill or system** do you want to focus on? (Reading, Listening, Writing, Speaking, Grammar, Vocabulary, Pronunciation)
```

---

## Quality Standards

### Content Requirements
- Age-appropriate and culturally sensitive
- Aligned with CEFR descriptors for the target level
- Clear instructions and rubrics where applicable
- Consistent formatting throughout
- **Mandatory Answers Key**: Every worksheet MUST have a complete answer key appended at the end.
- **Mandatory Transcript**: If the materials involve a listening task, the full transcript MUST be included at the end (after the answer key).
- **Internal References**: Avoid generic terms like "Exercise 2" unless specific numbers are visibly assigned. Prefer spatial references ("words above/below") or explicit Task references ("Task 2").

### Format Standards
- **PDF Engine**: ALWAYS use **Typst**. 
- **Headers**: Use the `#integrated_header()` function from the gold standard template.
- **Typography**: Arial is standard for Typst worksheets.
- **Written Response Tasks**:
    -   **Layout**: These tasks must fit on a **single dedicated page** (use `#pagebreak()` before).
    -   **Identity Block**: ALWAYS preface the task with the `#identity_block()` immediately after the header.
    -   **Structure**: Group all prompts/questions at the top.
    -   **The Gap**: Insert a spacing of `#v(1.5cm)` between the last question and the first ruled line.
    -   **The Lines**: Provide a **single block** of dark gray lines (`stroke: 0.5pt + rgb("#4D4D4D")`) below. **CRITICAL**: Never use light gray for ruled lines.
    -   **Spacing**: Use **Double Spacing** for the lines themselves (`row-gutter: 1.5cm`) to allow for corrections.
    -   **Line Count**: Calculate required lines assuming **10 words per line**. (e.g., 100 words = 10 lines).
- **Matching/List Questions**: When creating a list of matching questions (e.g., Question -> Answer box), ALWAYS use matching vertical spacing (e.g., `row-gutter: 1cm` or `0.8cm`) to allow space for handwriting. Do not tightly pack these items.
- **Definition Tasks**: For tasks requiring written definitions, use a **Columns + Line** layout (e.g., `columns: (auto, 1fr)`), where the word is on the left and a rule extends to the right margin. Use generous vertical spacing (e.g., `row-gutter: 1.5cm`) to allow for two lines of handwriting if needed.
- **Pagination & Duplexing**:
    -   **Orphan Prevention**: Ensure task headers are never left alone at the bottom of a page. If a task header falls at the bottom, move it to the next page.
    -   **Booklet Logic (Groups of 4)**: Materials are printed 2-up Double Sided (4 pages per sheet). Text flows freely between Pages 1-2, 2-3, 3-4.
    -   **Hard Breaks**: **CRITICAL**. Tasks MUST NOT break across the sheet boundary (e.g., Page 4 to 5, or 8 to 9). Students should not have to flip a physical sheet to finish a single task. Insert an explicit `#pagebreak()` if a task risks straddling this boundary.
- **Image Quality**:
    -   **No Gradients**: Images must be suitable for grayscale photocopying (solid colors, clear contrast).
    -   **Transparency**: Non-rectangular graphics must be **Transparent PNGs**.
    -   **No Fake Checkerboards**: **CRITICAL**. You MUST remove "fake" gray-and-white checkerboard patterns from images before use. Run the removal script in the `processing-images` skill if detected. 
    -   **Trimming**: All generated images MUST be processed with the `processing-images` skill to remove whitespace.
    -   **Aspect Ratio**: NEVER squash wide motifs. Use `width: 100%` and allow height to autosize (or use specific aspect-ratio preserving dimensions).
### Creative License & Typography
Don't settle for "cookie-cutter" designs. Use creative licence to make materials visually engaging and thematic:
- **Thematic Motifs**: Look for opportunities to include stylistic elements like ECG blips, watermarks, or border styles that reflect the topic.
- **Title Design**: 
    - Use custom-generated images for main titles if raw text cannot capture the desired emotion.
    - If using text, break titles into component parts with different styles (e.g., **Heavy** vs _Light_).
- **Readability**: While headers can be experimental, **Reading Text must remain highly readable**. Do not use overly decorative or handwriting fonts for long passages of text.
- **Font Combinations**:
  - **Aggressive/Strong**: `Arial Black`, `Impact`, `weight: "black"`.
  - **Speed/Movement**: `style: "italic"`, `weight: "light"`, `tracking: 0.2em`.
  - **Technical/Report**: `Courier New`.
- **Typst Layout Tools**: Use `#stack`, `#box`, and `align(horizon)` to create dynamic, non-linear headers.
- **Self-Checks**: Include the `#radar_box()` or peer review checklists.
- **Mandatory Page Breaks**: Use `#pagebreak()` between major sections or levels.

### File Naming Convention

```
DD-MM-YY-[Topic]-[Skill/System]-[Program]
```

| Component | Options |
|-----------|---------|
| `DD-MM-YY` | Date (e.g., `27-12-25`) |
| `Topic` | Subject matter (e.g., `Politeness`, `Presentation-Structure`) |
| `Skill/System` | `Reading`, `Listening`, `Writing`, `Speaking` |
| `Program` | `Bell` or `Intensive` |

**Examples:**
- `27-12-25-Politeness-Reading-Intensive.html`
- `29-12-25-Presentation-Structure-Speaking-Bell.html`

---

## Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| Multimodal image reading | ✅ Available | Gemini 3 Flash |
| Image generation | ⚠️ Restricted | Use `generate_image` cautiously; prefer CSS/Assets. |
| Audio generation | 🔜 Planned | Future skill |
