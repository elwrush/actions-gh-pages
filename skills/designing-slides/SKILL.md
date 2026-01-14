---
name: designing-slides
description: >
  Creates Google Slides presentations using the Slides API. Use when the user
  mentions slideshows, presentations, or needs to convert lesson plans into slides.
---

# Designing Slides

**Capability**: Create and manipulate Google Slides presentations programmatically using the Google Slides API.

## Prerequisites

> [!CRITICAL]
> **ALWAYS Use Existing Working Examples as Templates**
> 
> DO NOT write slideshow generation scripts from scratch. The project contains working examples (e.g., `create_presentation_structure_slides.py`) that demonstrate:
> - Bell EP template structure
> - Batch API patterns  
> - EMU unit conversions
> - Proper authentication flow
> 
> **Workflow**: Copy working example → Adapt slide content → Execute
> 
> Writing from scratch wastes hours debugging solved problems (string escaping, API formats, credentials paths).

- Google Cloud project with Slides API enabled
- OAuth 2.0 credentials in `.credentials/credentials.json`
- Token file will be auto-generated at `.credentials/token.json` on first run

---

## Workflow (GATED - MANDATORY)

> [!CRITICAL]
> **Markdown Preview Gate**
> 
> Before executing ANY Python script that creates a slideshow via the Google Slides API, you MUST:
> 
> 1. **Create a Markdown Outline** of all slides in the following format:
>    ```markdown
>    # Slideshow Outline: [Title]
>    
>    ## Slide 1: [Title]
>    - [Brief content summary or key bullet points]
>    
>    ## Slide 2: [Title]
>    - [Brief content summary]
>    ...
>    ```
> 
> 2. **🔍 RUN VALIDATOR**: Check outline for compliance
>    ```bash
>    python skills/designing-slides/scripts/validate_slideshow_outline.py <outline.md>
>    ```
>    - **Checks performed**:
>      - ❌ Answer key interleaving
>      - ❌ Bullet limits (max 7)
>      - ❌ Vocabulary format
>      - ❌ No image placeholders
>      - ⚠️ Mechanistic language
>    - **Fix ALL errors** before proceeding
> 
> 3. **🚦 USER REVIEW GATE**: Present the markdown outline + validation report to the user
>    - If user requests changes OR validator fails, revise and go back to step 2
>    - **DO NOT proceed until user explicitly approves AND validator passes**
> 
> 4. **Generate Python Script**: Only after approval, create/run the slideshow generation script
> 
> 5. **Execute & Upload**: Run the script to push to Google Slides
> 
> **Reason**: API calls are expensive and irreversible. The markdown gate + validator allows rapid iteration on content/structure before committing to the API.


---

## Design Principles

| Principle | Implementation |
|-----------|----------------|
| **McKinsey Logic** | Use **Action Titles** (Dots) as headers; the slide body (Dashes) must prove the title |
| **Similes over Metaphors** | Use professional similes to explain tasks; avoid 'hokey' or labored metaphors |
| **Logic Checks** | Verify **Horizontal Flow** (Story in titles) and **Vertical Flow** (Proof in body) |
| **5-7 lines max** | Limit bullet lists to 6 items |
| **One idea per slide** | Generate multiple slides for complex topics |
| **High contrast** | Use Bell maroon/Oxford blue palette |
| **Large fonts** | Body 24pt+, titles 44pt+ |
| **30-50% white space** | Don't overcrowd slides |
| **Accessibility** | Test contrast ratios (WCAG 4.5:1) |

### McKinsey Pedagogical Framing (Critical)

Do NOT slavishly and mechanistically reproduce the structure of worksheets. Avoid "Gamer", "Hacker", or "Hero" metaphors unless they are extremely light and requested. Instead:
- **Frame and Interpret**: Present material as an expert strategist would.
- **Action Titles (Dots)**: Every slide title must be an **assertion** or a **step in the story**, not just a label.
- **Guidance through Similes**: Use similes to guide students on HOW to do tasks properly.
  - *Example (Simile)*: "Analyzing this text is like using a magnifying glass—look for the small, hidden clues."
- **Avoid Hokey Framing**: 
  - *Anti-pattern*: "Slide 5: **System Architecture**. Write your code now."
  - *Good pattern*: "Slide 5: **The Strategic Plan**. Like a master architect, sketch your argument before you build."

## Slide Content Rules

### Answer Slides
Each answer to a question must appear on its **own slide** immediately after the question/task slide, containing:
- The answer (highlighted/emphasized)
- A brief explanation
- A supporting snippet from the reading/transcript (where appropriate)

**Critical**: Answer slides must be **interleaved** with question slides in the pedagogical flow, not grouped at the end of the presentation.

### Narrative Transitions (MANDATORY Checkpoints)

Transition slides **MUST** be inserted at these structural checkpoints:

| Checkpoint | Insert transition BEFORE... |
|------------|----------------------------|
| 1 | Vocabulary section |
| 2 | Main reading/listening/challenge |
| 3 | Hero Tool or solution reveal |
| 4 | Student practice/task |
| 5 | Reflection/wrap-up |

**Requirements**:
- Each transition = single slide with friendly guiding phrase
- Phrases must be **creative and lesson-specific** (NOT deterministic/copied)
- Purpose: Mental reset, not just labeling sections

**Anti-pattern** (robotic): "Now we will learn vocabulary."
**Good pattern** (engaging): "Before we dive in, let's arm ourselves with some key words..."
 
### Vocabulary Slides

Each pre-taught vocabulary item must appear on its **own slide** containing the mandated pattern:

```
word /phonemic script/: ภาษาไทย (actual Thai script, NOT English transliteration)

English context sentence with **target word** bolded.

ประโยคภาษาไทยที่มี **คำเป้าหมาย** เป็นตัวหนา
```

**Example**:
```
hikikomori /ˌhɪkiˈkɒməri/: คนที่หลบหนีสังคม

Toshi had such extreme **hikikomori** that he had not left his room for a week.

โทชิมีอาการ **ฮิกิโกะโมริ** อย่างรุนแรงจนไม่ได้ออกจากห้องมาหนึ่งสัปดาห์
```

> [!CRITICAL]
> - Thai translations MUST use Thai script (ภาษาไทย), NOT English phonetic transliteration
> - Target word must be **bolded** in BOTH English and Thai sentences
> - Do NOT use HTML tags - use markdown-style bold for outline, API handles styling
> - Context sentences must **ILLUSTRATE THE MEANING** of the word, not just use it
>
> **Anti-pattern** (doesn't contextualize):
> "School should not be a **popularity contest**."
>
> **Good pattern** (illustrates meaning):
> "Instagram has become a **popularity contest** where people compete for likes and followers."


### Image Policy

**CRITICAL**: The agent will NEVER attempt to generate images or add image placeholders *unless bespoke images have already been created*.

1. **Check Inputs Folder**: Before generating slides, scan the input directory for any image files (e.g., `diagrams/*.png`, `images/*.jpg`).
2. **Use Bespoke Images**: If custom images exist (e.g., diagrams created during material generation), you MUST:
   - Upload them to Google Drive (publicly viewable).
   - Insert them into the relevant slides using `createImage`.
   - **Do NOT** use a text placeholder for these images.
3. **No New Generation**: Do NOT use `generate_image` tool specifically for the slideshow if it wasn't done earlier. Only use what exists.
4. **Placeholders**: Only use text placeholders (e.g., `[IMAGE: .../`) if no bespoke image exists for that concept.

Focus solely on text content and layout, unless assets are provided.

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

> [!CRITICAL]
> **Use "Self-Contained Script" Pattern**
>
> The helper library `scripts/add_slide_content.py` functions (e.g., `add_title_slide`) execute requests immediately, which is slow and prevents batching.
>
> **Do NOT import slide creation functions.**
> **Do NOT try to use the library for batching.**
>
> Instead, you MUST:
> 1. **Copy the Working Pattern**: See `inputs/01-Presentation-Structure/create_presentation_structure_slides.py`.
> 2. **Define Local Helper Functions**: In your new script, define `create_content_slide()` locally.
> 3. **Implement Batch Logic Locally**: Build the `requests` list inside your local function and call `batchUpdate` there.
>
> This "copy-paste-adapt" approach allows you to customize the batching logic for each specific slideshow without breaking library dependencies or fighting import paths.

---

## API Usage & Code Examples

For authentication, slide creation, formatting, and batch operations, see [REFERENCE.md](REFERENCE.md).

**Key Scripts:**
- `scripts/authenticate_google.py` – OAuth authentication
- `scripts/create_presentation.py` – Create new presentations
- `scripts/add_slide_content.py` – Add content to slides
- `scripts/format_slides.py` – Apply styling and formatting
- `scripts/validate_slideshow_outline.py` – Validate outlines before generation

**External Documentation:**
- [Google Slides API](https://developers.google.com/slides/api)


## Notes

- **Token refresh**: The OAuth token automatically refreshes when expired
- **Rate limits**: Google Slides API has rate limits; use batch operations when possible
- **Image uploads**: Images must be uploaded to Drive first, then referenced by ID
- **Permissions**: Presentations are created in your Drive; share manually or via API
