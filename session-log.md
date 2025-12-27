# Session Log

## 2025-12-25 | Writing Lesson Plans Skill Design

### Objective
Design the `writing-lesson-plans` skill following the Skills-based architecture methodology.

### Actions Completed

1. **Ingested Skills Architecture** — Read `knowledge_base/using-skills.md` to understand the methodology
2. **Analyzed Lesson Shapes** — Reviewed `knowledge_base/lesson_shapes.yaml` (7 shapes: A-G)
3. **Identified Additional Data Fields** — Marker sentences, answer keys, transcripts, textbook/unit info
4. **Created Implementation Plan** — 8-step workflow documented in artifacts
5. **Created Skill Files**:
   - `skills/writing-lesson-plans/SKILL.md` — Main workflow (8 steps)
   - `skills/writing-lesson-plans/REFERENCE.md` — Shape summaries + example output

### Key Decisions
- Lesson plans use **markdown tables** (Stage/Aim/Procedure/Time/Interaction)
- **Answer keys** included as footer section
- **Transcripts** required for listening lessons (Shape E)
- **Materials scanning** deferred to separate multimodal skill using Gemini 2.5 Flash
- Skills directory located at `/skills`

### Related Skills (Future)
- `uploading-to-google-docs`
- ~~`designing-slides`~~ ✅ DONE
- `uploading-to-google-slides`
- `scanning-materials`

---

## 2025-12-26 | Google Slides API Integration

### Objective
Set up Google Slides API access and create the `designing-slides` skill.

### Actions Completed

1. **Researched API Options** — Ingested Google Cloud client libraries guide, confirmed using Google API Client Libraries
2. **Verified Authentication** — Tested OAuth credentials in `.credentials/credentials.json`
3. **Created Test Presentation** — Successfully authenticated and created test presentation via API
4. **Built `designing-slides` Skill**:
   - `skills/designing-slides/SKILL.md` — Main workflow documentation
   - `skills/designing-slides/REFERENCE.md` — Quick reference with code examples
   - `scripts/authenticate_google.py` — OAuth 2.0 authentication module
   - `scripts/create_presentation.py` — Presentation creation/management
   - `scripts/add_slide_content.py` — Content addition (text, images, tables)
   - `scripts/format_slides.py` — Styling, colors, Bell theme

### API Capabilities Documented
- Presentation management (create, copy, update)
- Slide operations (add, delete, reorder)
- Content insertion (text boxes, images, tables, shapes)
- Formatting (fonts, colors, backgrounds, themes)
- Batch updates for efficiency
- Integration with Google Sheets for charts

### Key Files
- **Credentials**: `.credentials/credentials.json` (OAuth client)
- **Token**: `.credentials/token.json` (auto-generated on first auth)
- **Test Script**: `test_slides_auth.py` (can be deleted after verification)

---

## 2025-12-26 | Slide Template Creation

### Objective
Create a branded Bell EP slide template with proper design principles.

### Actions Completed

1. **Extracted Brand Colors** — Analyzed `images/ACT.png` → maroon RGB(166, 45, 38)
2. **Researched Design Principles** — Ingested Noun Project slide design guide
3. **Researched Co-branding** — Logos should use "lock-up" pattern (side-by-side, equal weight)
4. **Created Template Scripts**:
   - `skills/designing-slides/update_template.py` — Updates existing template
   - `skills/designing-slides/create_template_v2.py` — Original creation script
5. **Built Title Slide Layout**:
   - Header bar with Bell + ACT logos (centered, side-by-side)
   - "Bell Language Centre" strap line
   - `{{TITLE}}` placeholder
   - Square image placeholder

### Template Location
- **Google Slides**: [Bell EP Slide Template](https://docs.google.com/presentation/d/1AdeFwA9zFkJMmkwB7c74pO88KPuJypgZRDM73haL8iw/edit)
- **Drive Folder**: Target folder as specified

### Design Decisions
- **Header bar** with logos (not footer) per co-branding research
- **Maroon theme** from ACT.png brand color
- **White text** on maroon background for contrast
- **PNG format** for Bell logo (SVG had rendering issues)
- **Center-justified** layout for title slide elements

### Next Steps (Pending)
- [ ] Content slide template
- [ ] Two-column layout (optional)
- [ ] Review and refine spacing/sizing

---

## 2025-12-26 | Lesson Planning Skill Update

### Updates Made

1. **Added Pre-teach Vocabulary Stage** (Shape E - Receptive Skills)
   - Mandatory stage after Lead-in for all reading/listening lessons
   - Updated typical stages: Lead-in → **Pre-teach Vocab** → Pre-task → Main Task → Post-task

2. **Defined Pre-teach Vocabulary Format**
   - Select **5 words** challenging for CEFR level
   - Format per word:
     - `word /phonemic script/: Thai translation`
     - English context sentence with target word highlighted
     - Thai context sentence with translated word highlighted

### Files Modified
- `skills/writing-lesson-plans/SKILL.md`
- `skills/writing-lesson-plans/REFERENCE.md`

---

## 2025-12-26 | GitHub Integration

### Objective
Create `committing-to-github` skill and push project to GitHub repository.

### Actions Completed

1. **Created `committing-to-github` Skill**
   - 6-step workflow (status → review → stage → commit → push → confirm)
   - Automatic `desktop.ini` exclusion for Google Drive sync
   - Commit message conventions

2. **Created Project README.md**
   - Overview of all skills
   - Setup instructions
   - Project structure
   - Skills architecture explanation

3. **Created .gitignore**
   - `desktop.ini` exclusion
   - `.credentials/` exclusion (OAuth tokens)
   - Python, IDE, OS patterns

4. **Initial Git Workflow**
   - Initialized repository: `git init`
   - Configured remote: https://github.com/elwrush/lesson-plan-agent.git
   - Staged 29 files (4733 insertions)
   - Committed with conventional format
   - Pushed to master branch

### Repository Details
- **URL**: https://github.com/elwrush/lesson-plan-agent
- **Commit**: `5559892` - "feat: initial commit - lesson planning agent with skills architecture"
- **Files**: 29 files, 172.75 KiB

- Skills: `writing-lesson-plans/`, `designing-slides/`, `committing-to-github/`
- Knowledge base: lesson shapes, design principles
- Images: Bell/ACT logos, headers
- Documentation: README, session logs, error tracking

---

## 2025-12-27 | Intensive Reading Materials Development

### Objective
Transform source materials (3 JPEG scans on "Politeness") into professional GDocs-ready HTML with Entry Ticket and cross-cultural image.

### Actions Completed

1. **Skills Created/Updated**:
   - `reading-visual-content`: Multimodal extraction with honesty protocol.
   - `converting-to-gdocs-html`: GDocs-specific formatting rules.
   - `pushing-to-gdocs`: Drive API upload workflow.
   - `writing-bespoke-materials`: Updated with Answer Key/Transcript rules.

2. **Material Development**:
   - Extracted content from `skilful conv 10-12.jpeg` using Gemini 3 Flash.
   - Generated cross-cultural greeting image using `generate_image` tool.
   - Created `intensive-reading-politeness.html` with:
     - Intensive header image
     - PET Part 2 Entry Ticket (5 items, 3 matches, 2 distractors)
     - Reading passage with inset image
     - Vocabulary box with pipe separators
     - Global/Close reading exercises
     - Discussion questions
     - Complete Answer Key

3. **Entry Ticket Refinements**:
   - A-E selection box (horizontal)
   - Tools randomized: scalpel, whisk, tripod, guitar, saw
   - Matches: 1-A (Anna), 3-E (Eric), 5-B (Ben)
   - Distractors: 2 (whisk), 4 (guitar)

### Files Modified
- `outputs/intensive-reading-politeness.html`
- `inputs/Intensive-Reading-Politeness/` (synced final assets)
- `skills/reading-visual-content/SKILL.md`
- `skills/converting-to-gdocs-html/SKILL.md`
- `skills/pushing-to-gdocs/SKILL.md`
- `skills/writing-bespoke-materials/SKILL.md`

### Skills Compliance Audit
All skills audited against `knowledge_base/using-skills.md`:

| Skill | Lines | Triggers | Structure | Compliant |
|-------|-------|----------|-----------|-----------|
| reading-visual-content | 130 | ✓ | ✓ SKILL.md only | ✓ |
| converting-to-gdocs-html | 62 | — | ✓ SKILL.md only | ✓ |
| pushing-to-gdocs | 41 | — | ✓ SKILL.md only | ✓ |
| writing-bespoke-materials | 103 | ✓ | ✓ SKILL.md only | ✓ |

**Gap Identified**: Skills are missing YAML frontmatter with `name` and `description` fields (Level 1 metadata).

### Next Steps
- [ ] Push to Google Docs
- [ ] Add YAML frontmatter to all skills (optional)

---

## 2025-12-27 | Skills Compliance Fixes

### Objective
Add YAML frontmatter to all skills per the Skills Architecture specification.

### Actions Completed

1. **Audited All 7 Skills** — Verified compliance against `knowledge_base/using-skills.md`
2. **Added Frontmatter to 5 Skills**:
   - `designing-slides/SKILL.md`
   - `reading-visual-content/SKILL.md`
   - `converting-to-gdocs-html/SKILL.md`
   - `pushing-to-gdocs/SKILL.md`
   - `writing-bespoke-materials/SKILL.md`
3. **Updated 1 Skill** — Added trigger phrases to `committing-to-github/SKILL.md`

### Compliance Status (Post-Fix)

| Skill | YAML Frontmatter | Triggers | Compliant |
|-------|------------------|----------|-----------|
| `writing-lesson-plans` | ✅ | ✅ | ✅ |
| `committing-to-github` | ✅ | ✅ | ✅ |
| `designing-slides` | ✅ | ✅ | ✅ |
| `reading-visual-content` | ✅ | ✅ | ✅ |
| `converting-to-gdocs-html` | ✅ | ✅ | ✅ |
| `pushing-to-gdocs` | ✅ | ✅ | ✅ |
| `writing-bespoke-materials` | ✅ | ✅ | ✅ |

**All 7 skills now fully compliant.**

---

## 2025-12-27 | Templates Folder Creation

### Objective
Create reusable HTML templates to avoid skill bloat and capture design decisions.

### Templates Created

| Template | Purpose |
|----------|---------|
| `entry-ticket-pet-part2.html` | PET Part 2 matching (5 items, 3 matches, 2 distractors) |
| `vocabulary-box.html` | Horizontal word box with pipe separators |
| `exercise-box.html` | Blue-shaded exercise container |
| `glossary-box.html` | Red-tinted vocabulary definitions |
| `inset-image-table.html` | 2-column table for text + image layout |
| `answer-key-section.html` | Standard answer key footer |

### Files Modified
- `skills/writing-bespoke-materials/SKILL.md` — Added Templates section with links

### Design Principle
Templates accumulate reusable HTML patterns. Skills reference templates rather than embedding rules.

---

## 2025-12-27 | Google Docs HTML Push Implementation

### Objective
Push HTML materials to Google Docs with formatting preserved (colored boxes, images, tables).

### Problem Discovered
Google Docs HTML import ignores most CSS:
- No `float`, `box-shadow`, `border-radius`, `max-width`
- Class-based styles unreliable
- Local image paths don't resolve

### Solution Implemented

1. **Created Knowledge Base**: `knowledge_base/GDocs-HTML-Constraints.md`
2. **Created Push Script**: `scripts/push_to_gdocs.py`
   - Embeds images as base64 data URIs
   - Uses `MediaIoBaseUpload` for HTML content
   - Authenticates via dedicated `gdocs-token.json`
3. **Rewrote HTML** for Google Docs compatibility:
   - 1-cell tables for colored boxes
   - 2-column tables for image insets
   - Inline `style=""` attributes
   - `pt` units instead of `px`
   - `&nbsp;` in empty cells
   - Explicit `font-family: Roboto; font-size: 10pt; line-height: 1.15; margin: 0;`

### Files Created/Modified
- `knowledge_base/GDocs-HTML-Constraints.md` — Import constraint reference
- `scripts/push_to_gdocs.py` — Upload script with base64 image embedding
- `.credentials/gdocs-token.json` — OAuth token with Drive scope
- `inputs/Intensive-Reading-Politeness/intensive-reading-politeness.html` — Rewritten for Docs compatibility

### Final Output
- [27-12-25-Politeness-Reading-Intensive-v8](https://docs.google.com/document/d/1PptUYUrscc4-u-oh-04cdCxMqje8-FErANfsgAWgvjM/edit)

### Lessons Learned
- Google Docs is a paginated word processor, not a browser — design accordingly
- Table-based layouts are mandatory for multi-column content
- Manual adjustment may still be needed for paragraph spacing

### Refined Design Approach (Session Continuation)
After testing, user feedback led to a simpler approach:

**Avoid tables entirely** — use formatted paragraphs instead:
- Behavior ratings: Circle icons (⭘) with tabbed numbers
- Word boxes: Styled paragraphs with pipe separators
- Content boxes: Bordered paragraphs (optional shading)
- Images: Placed above text for manual wrapping

**Benefits:**
- Much easier to edit in Google Docs
- No table spacing issues
- Cleaner, more readable HTML

### Final Output (Revised)
- [27-12-25-Politeness-Reading-Intensive-FINAL-v2](https://docs.google.com/document/d/1Cp9b-L0P9NHQ3LMdTAsaTU0h_0CAIG-c2HlPcgS9GXk/edit)

---

## 2025-12-27 | Lesson Plan Generation & Skill Refinement

### Objective
Generate a B1 intensive reading lesson plan on politeness and refine the `writing-lesson-plans` skill.

### Actions Completed

1. **Generated Lesson Plan for Politeness Reading**
   - Collected metadata: B1, Ed Rush, 46 min, Intensive, Shape E
   - Created pre-teach vocabulary deck (5 words with phonemic script + Thai translations)
   - Incorporated special request: Thai wai video lead-in

2. **Major Skill Updates (`writing-lesson-plans/SKILL.md`)**:
   - Added Step 3: Ask Intensive vs Regular Bell lesson (header image)
   - Added Step 5: Special requests before generation
   - Changed "Aim" → "Objective" in header
   - Added "Date" field (DD-MM-YY format) after Objective
   - Changed "Page Numbers" → "Materials" with meaningful description
   - Moved pre-teach vocabulary INTO the lesson table (not header)
   - Added colored stage headers (ACT maroon) spanning table width
   - Added **Model Compliance Requirement** (critical section)
   - Defined formatting guidelines: ACT maroon colors, HTML bullets, 1.15 spacing

3. **Push Script Updates (`scripts/push_to_gdocs.py`)**:
   - Added Google Docs API scope
   - Added `set_page_format()` function to set A4 with 2cm margins via Docs API

4. **Updated `pushing-to-gdocs/SKILL.md`**:
   - Documented A4/2cm margins auto-setup
   - Updated prerequisites (Drive + Docs scopes)

### Model Compliance
Regenerated lesson plan to match Shape E model structure:
- **3 stages** (not 6): Lead-in, Reading for gist/detail, Post-reading
- Consolidated activities into logical stages matching pedagogical intent

### Files Modified
- `skills/writing-lesson-plans/SKILL.md`
- `skills/pushing-to-gdocs/SKILL.md`
- `scripts/push_to_gdocs.py`
- `inputs/Intensive-Reading-Politeness/27-12-25-LP B1-Politeness-Reading-Shape E Receptive.html`

### Final Output
- [27-12-25-LP B1-Politeness-Reading-Shape E Receptive-v3](https://docs.google.com/document/d/1kuhsdSkX3SNCqNOeA0N1YWwaFzGncW9hwHvF3J3Sjw0/edit)

---

## 2025-12-27 (Evening) | Slideshow Development from Lesson Plan

### Objective
Develop a complete Google Slides presentation from the B1 Politeness Reading lesson plan.

### Actions Completed

1. **Initial Slideshow Script** — Created `create_politeness_slideshow.py` with all slide content
2. **API Efficiency Refactor** — Rewrote to batch API pattern after user feedback:
   - Changed from 100+ individual API calls to single batchUpdate call
   - Reduced execution time from 3-4 minutes to ~30 seconds
3. **Themed Slideshow** — Created `create_slideshow_themed.py` with:
   - Color-coded headers: Vocabulary (teal), Answer (green), Activity (orange), Discussion (purple), Video (red)
   - Spotlight answer layout with highlight box, snippet, and explanation
   - Video placeholder with play button (API doesn't support embedding)
4. **Cover Slide Fix** — Fixed logo paths and layout:
   - Changed `LOGO_DIR` from `skills/.../images` to `images/` at project root
   - Used Bell.png instead of Bell.svg for reliable rendering
   - Matched layout to original template (centered logos in header)

### Key Learnings
- **Batch API is essential** — Google Slides API should always use accumulated requests + single batchUpdate
- **No video embedding** — Slides API does not support YouTube embedding; must be manual
- **Logo paths matter** — Logos stored in `images/` at project root, not skill folder
- **PNG over SVG** — PNG logos render more reliably than SVG in Slides API

### Files Created/Modified
- `skills/designing-slides/create_politeness_slideshow.py` (initial version)
- `skills/designing-slides/create_slideshow_optimized.py` (batch API)
- `skills/designing-slides/create_slideshow_themed.py` (final themed version)
- `skills/designing-slides/SKILL.md` (added image rules, workflow, batch patterns)

### Final Output
- [27-12-25-Politeness-Reading-B1-THEMED](https://docs.google.com/presentation/d/1-JNl-rJXH65aXNGVz2mV8QpguaY_hKueBs8KKn8_8-4/edit)
