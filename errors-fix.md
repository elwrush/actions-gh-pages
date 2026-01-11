# Errors & Fixes Log

## 2025-12-26

### SVG Logo Not Rendering in Google Slides
- **Issue**: Bell.svg uploaded to Drive but wouldn't render in Slides API
- **Cause**: SVG format not well-supported by Slides API image insertion
- **Fix**: Use existing `images/Bell.png` instead of SVG

### Logo Placement Design Issues
- **Issue**: Initially placed logos at bottom corners (unconventional)
- **Fix**: Researched co-branding best practices → logos should be in header bar side-by-side ("lock-up" pattern)

### Duplicate Template Creation
- **Issue**: Created new template instead of updating existing one
- **Fix**: Rewrote script to update existing template ID; deleted duplicate

### Text Color on Maroon Background
- **Issue**: Strap line and title text initially maroon (invisible on maroon background)
- **Fix**: Changed to white text for proper contrast

---

## 2025-12-25

### No Errors Encountered
This session proceeded without errors requiring fixes. The `writing-lesson-plans` skill was designed and implemented successfully on the first attempt.

---

*Note: Future sessions should document errors and their resolutions here for reference.*

---

## 2025-12-27

### Entry Ticket Logic Errors (Intensive Reading - Politeness)
- **Issue 1**: All 5 people matched to 5 tools. User wanted only 3 matches.
- **Cause**: Initial design included tools for every profession.
- **Fix**: Changed Carlos from "chef" to "restaurant manager" (removing `whisk` match). Replaced `calculator` with `guitar` (not matching any profession).

### Entry Ticket Display Issues
- **Issue 2**: Selection box displayed items vertically instead of horizontally.
- **Cause**: Inline styling was missing on the selection box container.
- **Fix**: Added `text-align: center;` and `&nbsp;|&nbsp;` separators for horizontal layout.

### Answer Key Out of Sync
- **Issue 3**: Answer Key did not reflect the updated distractor logic.
- **Cause**: Forgot to update Answer Key after changing tool items.
- **Fix**: Rewrote Answer Key to list all 5 items with correct matches (1-A, 3-E, 5-B) and distractors (2, 4).

### Google Docs HTML Import - CSS Ignored
- **Issue**: Colored boxes, floated images, and styled divs lost formatting when pushed to Google Docs.
- **Cause**: Google Docs ignores most CSS (floats, box-shadow, border-radius, max-width) and class-based styles.
- **Fix**: 
  1. Use **1-cell tables** for colored boxes instead of `<div>` with CSS classes
  2. Use **2-column tables** for image insets instead of `float: right`
  3. Use **inline `style=""` attributes** instead of `<style>` blocks
  4. Use **`pt` units** instead of `px`
  5. Embed images as **base64 data URIs** via `push_to_gdocs.py`

### Google Docs - Empty Table Cells Not Editable
- **Issue**: Empty table cells couldn't be clicked/edited in Google Docs.
- **Fix**: Add `&nbsp;` (non-breaking space) to all empty cells.

### Google Docs - Paragraph Spacing in Tables
- **Issue**: Table text had excessive spacing after paragraphs.
- **Cause**: Google Docs applies "Normal" paragraph style with spacing after.
- **Fix**: Add explicit inline styles: `font-family: Roboto; font-size: 10pt; line-height: 1.15; margin: 0;`
- **Note**: May still require manual adjustment in Google Docs (Format → Line & paragraph spacing → Remove spacing after paragraph).

### Google Docs - Refined Design Approach (Final)
- **Issue**: Table-based layouts were hard to edit and had spacing issues.
- **Cause**: Overuse of tables for styling (colored boxes, image insets).
- **Fix**: Rewrote HTML with **zero tables**:
  1. Use **formatted paragraphs** with inline `style=""` attributes
  2. Use **circle icons (⭘)** with tabbed spacing for rating scales
  3. Use **borders** on paragraphs for emphasis (not background shading)
  4. Let content flow as natural text
- **Result**: Much easier to edit in Google Docs.

---

## 2025-12-27 (Evening) | Slideshow Development

### API Efficiency Issues
- **Issue**: Initial slideshow script made 100+ individual API calls, taking 3-4 minutes
- **Cause**: Each slide element (create, style, format) was a separate batchUpdate call
- **Fix**: Refactored to accumulate all requests and send single batchUpdate (34 seconds)

### Rate Limiting (429 Too Many Requests)
- **Issue**: Script crashed with quota error during slide creation
- **Cause**: Too many sequential API calls triggered Google's rate limit
- **Fix**: Batch all requests (reduces call count from 100+ to 1-3)

### Logo Path Not Found
- **Issue**: Bell and ACT logos not appearing on cover slide
- **Cause**: Script looked in `skills/designing-slides/images/` but logos are in `images/` at project root
- **Fix**: Changed `LOGO_DIR` to `os.path.join(PROJECT_ROOT, "images")`

### SVG Logo Rendering (Repeated)
- **Issue**: Bell.svg caused rendering issues in some cases
- **Fix**: Use Bell.png instead (more reliable across Slides API)

### Cover Slide Layout Issues
- **Issue**: Text overlapping image, logos misplaced
- **Cause**: Positioned elements based on guesswork instead of template measurements
- **Fix**: Copied exact layout from `update_template.py` (header_height, logo_y, center_x, gap calculations)

### YouTube Video Embedding
- **Issue**: User asked if YouTube videos could be embedded
- **Cause**: Google Slides API does NOT support video embedding
- **Fix**: Created video placeholder slide with play button icon and clickable URL. Videos must be inserted manually.

---

## 2025-12-29

### Scope Creep: Script-Writing Instead of Simple Edits
- **Issue**: User asked to edit a lesson plan hook. Agent launched into writing new Python slideshow scripts.
- **Cause**: Misinterpreted "create the slideshow" as "write a generation script" instead of understanding user wanted simple HTML edits + GDocs push.
- **Fix**: When editing existing materials, stick to: **Edit HTML → Open in browser → Push to GDocs**. Do NOT write new scripts unless explicitly requested.

### Missing Duration Prompt
- **Issue**: Lesson plan created with default "50 minutes" instead of correct "46 minutes".
- **Cause**: Agent did not ask user for lesson duration before generating plan.
- **Fix**: The `developing-bespoke-materials` skill MUST prompt for duration before generating any plan.

### Intrusive Browser Automation
- **Issue**: Agent repeatedly used browser_subagent to "verify" files, taking over user's browser.
- **Cause**: Over-verification; agent assumed it needed to visually confirm every change.
- **Fix**: Use `Start-Process` to open files in user's default browser. Only use browser_subagent when user explicitly requests browser interaction.

### Premature Workflow Advancement
- **Issue**: Agent created lesson plan before worksheet was approved; attempted slideshow before lesson plan was finalized.
- **Cause**: Anticipating next steps instead of waiting for explicit user approval.
- **Fix**: Strict sequential workflow: Material → User Approval → Lesson Plan → User Approval → Slideshow. Never skip ahead.

### Skipped Slideshow Browser Review
- **Issue**: Agent successfully generated slides but notified user of "completion" instead of opening for review.
- **Cause**: Regression on the "No-Automated-Verification" vs "Manual-Review-Opening" logic. I prioritized finishing over the review step.
- **Fix**: ALWAYS use `Start-Process [link]` and wait for explicit approval before finalizing any walkthrough or moving to next steps.

### Not Following Skill Requirements (Slideshow)
- **Issue**: Created slideshow without reading `designing-slides` skill. Violated: (1) Didn't use Bell EP template, (2) Didn't attempt image generation, (3) Lazy placeholder boxes.
- **Cause**: Agent skipped the critical step of ingesting the skill's image generation rules and template requirements.
- **Fix**: ALWAYS re-read the skill file BEFORE executing any skill-based task. Follow the template ID for title slides, attempt image generation FIRST (with fallback to prompts only if generation fails).

### Incorrect Title Slide Template Structure
- **Issue**: Second attempt at title slide still wrong - used simple maroon background + logos instead of the Bell EP template structure (dark header bar, gradient body, "Bell Language Centre" strap line, centered image).
- **Cause**: Didn't reference the actual template file (`update_template.py`) which shows the exact structure: header bar (rgb 0.35, 0.05, 0.05), logos in header (centered, side-by-side), strap line (18pt, centered), title (36pt, bold, white), square image placeholder (2.5" centered).
- **Fix**: Study `update_template.py` before creating title slides. The template has specific positioning, colors, and structure that must be replicated exactly.

### YAML Brittle Multi-line Matching
- **Issue**: Attempting to patch large sections of YAML with `replace_file_content` frequently failed.
- **Cause**: YAML's sensitivity to indentation.
- **Fix**: Rebuild and overwrite the entire file with `write_to_file`.

---

## 2025-12-30

### Header Image Path in Lesson Plans
- **Issue**: Lesson plans referenced `bell-header.jpg` and `intensive-header.jpg` in same folder as HTML file, causing images not to appear when pushed to Google Docs.
- **Cause**: Header images are located in project root `images/` directory, not in individual material folders.
- **Fix**: Use relative path `../../images/bell-header.jpg` or `../../images/intensive-header.jpg` when including headers in HTML lesson plans stored in `inputs/[folder]/` subdirectories.
- **Note**: The `push_to_gdocs.py` script will resolve paths relative to the HTML file location.


---

## 2025-12-30 (Continued) | Worksheet Generation System

### CSS Hardcoded Backgrounds Override Transparency
- **Issue**: Bell and ACT logos appeared with white backgrounds in PDF despite using transparent PNG files
- **Cause**: CSS `.bell-logos img` selector had hardcoded `background: white; padding: 5px; border-radius: 4px;`
- **Fix**: Removed background styling from CSS. Let transparent PNGs render naturally.
- **Lesson**: Always inspect rendered HTML with `--debug` flag. CSS styling can override image transparency.

### SVG Logo Not Rendering in Playwright PDF
- **Issue**: Bell logo (`Bell.svg`) did not appear in generated PDF
- **Cause**: SVG rendering in Playwright's PDF generation is unreliable
- **Fix**: Switched from `Bell.svg` to `Bell.png`
- **Lesson**: SVG works in browsers but may fail in headless PDF generation. Use PNG for logos in PDF workflows.

### File Path Encoding with Spaces
- **Issue**: Images with spaces in directory path ("LESSONS AND SLIDESHOWS 2") sometimes failed to load
- **Cause**: Manual string concatenation (`f"file:///{path}"`) didn't properly encode spaces
- **Fix**: Use `pathlib.Path(image_path).as_uri()` for robust file URI generation
- **Example**: `file:///C:/PROJECTS/LESSONS%20AND%20SLIDESHOWS%202/images/Bell.png`

### Jinja Variables in Injected Content Not Rendering
- **Issue**: Content fragment HTML used `{{ image_root }}/icon.png` but variable wasn't replaced
- **Cause**: Jinja2 doesn't auto-process variables in content passed via `{{ content | safe }}`
- **Fix**: Pre-process content HTML with `content_html.replace("{{ image_root }}", image_root_url)` before passing to template
- **Lesson**: Nested Jinja rendering requires manual variable substitution

### Page Break Not Rendering in PDF
- **Issue**: `<div style="page-break-before: always;"></div>` was added but didn't create page breaks
- **Cause**: Page breaks need top-level margin context to work reliably
- **Fix**: Add `mt-8` class to section after break: `<section class="mb-8 mt-8">`
- **Lesson**: Page breaks in Playwright PDF require both the break div AND margin spacing on adjacent elements

### Icon Background Removal with Corner Detection
- **Issue**: Simple white-threshold scripts (`make_transparent.py`) didn't work for icons with near-white backgrounds (e.g., RGB 243,249,249)
- **Cause**: Tolerance-based detection failed when background wasn't pure white
- **Fix**: Created `smart_transparency.py` that samples corner pixel color and removes all similar pixels using Euclidean distance
- **Lesson**: For AI-generated images, always detect actual background color rather than assuming white

### Slide Outline Created Without Reading Lesson Plan
- **Issue**: Created `slide-outline-mckinsey.md` with completely different content than the lesson plan (generic presentation skills vs. book/story presentation structure)
- **Cause**: User asked for slide outline but agent didn't read the existing lesson plan file first. Instead hallucinated content based on general presentation knowledge.
- **Fix**: ALWAYS read the lesson plan HTML file FIRST before creating any slide outline. Slides must support the lesson stages, objectives, and specific examples from the plan.
- **Lesson**: Slide outlines are derivative materials - they exist to support the lesson plan, not to be created independently. Never write slides without ingesting the LP first.

---

## 2025-12-30 (Evening) | Slideshow Generation - Critical Workflow Failure

### CRITICAL: Always Use Working Examples as Templates
- **Issue**: Spent 100+ steps debugging string escaping, API formats, and syntax errors when generating slideshow script from scratch
- **Root Cause**: **Did NOT copy/adapt existing working example** (`create_presentation_structure_slides.py`) which uses the EXACT same pattern
- **Correct Workflow**:
  1. Check for existing working scripts in project (use `find_by_name`)
  2. Copy the working script as template
  3. Adapt content (slide titles/body text) to new lesson
  4. Execute
- **Wrong Approach**: Writing complex API scripts from scratch, debugging for hours
- **Lesson**: **NEVER write slideshow generation scripts from scratch. ALWAYS copy and adapt existing working examples.** The batch API pattern, EMU units, styling—all of this is already solved.

### Python String Escaping in Slide Content
- **Issue**: Syntax errors from apostrophes in slide bullet text (e.g., `'Don\'t'` causing unterminated strings)
- **Root Cause**: Escaped quotes inside triple-nested Python list structures
- **Fix**: Use double quotes for strings containing apostrophes: `"Don't"` instead of escape sequences
- **Prevention**: When copying working examples, maintain their quote style patterns

### Credentials Path from Subdirectories
- **Issue**: `authenticate_google.py` couldn't find `.credentials/credentials.json` when script runs from subdirectory
- **Fix**: Working example uses `os.chdir(PROJECT_ROOT)` at start of script before authentication
- **Lesson**: This pattern is already solved in working examples—copy it

### Google Slides API Network Connectivity
- **Issue**: `ServerNotFoundError: Unable to find the server at slides.googleapis.com` 
- **Cause**: Temporary network issue or firewall
- **Resolution**: Script succeeded on retry—network issues are transient, not code problems
- **Lesson**: Don't over-engineer around network errors; retry is usually sufficient

### The "Batch API" Pattern Is Already Solved
- **Documentation**: Lines 103-145 in `designing-slides/SKILL.md` explain batch pattern
- **Working Example**: `create_presentation_structure_slides.py` shows complete implementation
- **Pattern**: Each content slide calls `create_content_slide()` which does ONE `batchUpdate()` with all requests for that slide
- **Don't**: Try to accumulate ALL slides into a single giant batch (causes complexity)
- **Do**: Copy the working pattern exactly—one function call per slide, each with its own batch

### Answer Slide Interleaving Pattern  
- **Requirement**: Answers must appear immediately after question slides (pedagogical flow)
- **Implementation**: Just call `create_content_slide()` for answer immediately after question
- **Lesson**: Simple sequential execution handles interleaving naturally

---

## 2025-12-30 (Night) | Worksheet Generation Improvements

### Bell Header Parameter Misunderstanding
- **Issue**: Passed "Bell Language Centre" in `--header-title` when it was already hardcoded as a strap line.
- **Root Cause**: Unclear skill documentation on header hierarchy.
- **Fix**: Updated `generating-worksheets/SKILL.md` to specify that `--header-title` should only contain the topic (e.g., "Useful Language"), as the strap line is automatic.

### Quote Section Visibility & "None" Bug
- **Issue**: Template showed "None" when `--quote` was omitted; also lost spacing when quote was removed.
- **Fix**: Wrapped quote section in `{% if quote %}`. Added conditional `margin-top: 10mm` to the content wrapper when `quote` is absent to maintain visual separation from the header.

### Page Overflow in BONUS Section
- **Issue**: Worksheet spilled to 5 pages due to excessive padding/margins in the final "BONUS" box.
- **Fix**: Reduced padding from `p-6` to `p-3` and bottom margins from `mb-8` to `mb-2` for the bonus section. Compressed previous "Thanking Your Audience" section into a pipe-separated paragraph.

### Workflow & Artifact Links
- **Issue**: Failed to provide direct Markdown links to generated PDF artifacts.
- **Fix**: Always provide a direct link to the generated PDF (e.g., `[label](file:///...)`) in the final response to ensure the user can audit the result immediately.

---

## 2026-01-04

### Invalid OAuth Token Persistence
- **Issue**: Slide generation script hung or failed because `token.json` was expired or invalid, but the script didn't auto-refresh correctly.
- **Fix**: Manually deleted `.credentials/token.json` to force a new authentication flow.
- **Lesson**: If authentication fails or hangs, the first step is to clear existing tokens.

### Module Import Errors in Scripts
- **Issue**: `create_punctuation_slideshow.py` failed with `ModuleNotFoundError` for `authenticate_google` and `format_slides`.
- **Cause**: Script was in `scripts/` but trying to import from `skills/designing-slides/scripts/` without that directory being in `sys.path`.
- **Fix**: Explicitly added `SKILL_SCRIPTS_DIR = os.path.join(PROJECT_ROOT, 'skills', 'designing-slides', 'scripts')` to `sys.path`.
- **Lesson**: Scripts outside the package structure must manually add dependency directories to `sys.path`.

### Google Slides API `updatePageProperties` Error
- **Issue**: `HttpError 400` with message `At least one field must be listed in 'fields'`.
- **Cause**: The `updatePageProperties` request (used for background color) requires a `fields` parameter to specify which properties to update, unlike some other requests which infer it.
- **Fix**: Added `'fields': 'pageBackgroundFill.solidFill.color'` to the request dictionary.
- **Lesson**: Always specify `fields` for `updatePageProperties` requests in the Google Slides API.

### Google Slides API `updatePageProperties` Error
- **Issue**: `HttpError 400` with message `At least one field must be listed in 'fields'`.
- **Cause**: The `updatePageProperties` request (used for background color) requires a `fields` parameter to specify which properties to update, unlike some other requests which infer it.
- **Fix**: Added `'fields': 'pageBackgroundFill.solidFill.color'` to the request dictionary.
- **Lesson**: Always specify `fields` for `updatePageProperties` requests in the Google Slides API.

## 2026-01-05

### UnicodeEncodeError in Console Output (Windows)
- **Issue**: push_to_gdocs.py failed with UnicodeEncodeError: 'charmap' codec can't encode character... when printing emojis (📄, ✅) to console.
- **Cause**: Windows console default encoding (cp1252) doesn't support these emojis.
- **Fix**: Set environment variable $env:PYTHONIOENCODING='utf-8' before running the Python script in PowerShell.
- **Micro-lesson**: When scripts use rich console output (emojis), always ensure the shell or python environment is forced to UTF-8 on Windows.

---

## 2026-01-06

### PDF Permission Denied (File Locking)
- **Issue**: `[Errno 13] Permission denied` when generating PDF worksheet.
- **Cause**: The previous version of the PDF was open in a PDF viewer, which locks the file on Windows.
- **Fix**: Generate to a new filename (versioning, e.g., `-v2.pdf`) instead of failing. This is faster than asking the user to close the file.

### Logo Overlay in WeasyPrint (PDF)
- **Issue**: Bell and ACT logos overlapped in the worksheet header.
- **Cause**: `display: flex` with `gap` property is often poorly supported in WeasyPrint (PDF generator).
- **Fix**: Switched to `display: table` / `inline-block` with explicit margins for robust layout rendering in PDF.

### Missing Bespoke Images in Slides
- **Issue**: A custom AI-generated diagram (`eye_contact_triangle.png`) was ignored in the slideshow, replaced by a generic text placeholder.
- **Cause**: The `designing-slides` workflow didn't strictly mandate checking for/using existing bespoke assets.
- **Fix**: Updated `SKILL.md` to mandate checking the inputs folder for images. Updated the generation script to upload and embed the specific image.

### NameError Global Variable Scope
- **Issue**: `NameError: name 'LOGO_DIR' is not defined` in slideshow script.
- **Cause**: Moved `LOGO_DIR` definition inside a function or deleted it during refactoring, but other functions still relied on it globally.
- **Fix**: Restored `LOGO_DIR` to global scope at the top of the script.
- **Lesson**: When refactoring script structures, verify that all global constants used in helper functions remain accessible.

---

## 2026-01-11 | GDocs Lesson Plans & Slideshow Scaling

### GDocs Lesson Plan Logo Missing
- **Issue**: Header logo didn't appear in Google Docs after upload.
- **Cause**: Incorrect relative path in HTML; `push_to_gdocs.py` couldn't resolve the local image for base64 embedding.
- **Fix**: Corrected path to `../../images/bell-header.jpg` (relative to the HTML file in `inputs/[subfolder]`).

### Slideshow Outline Validation Failure
- **Issue**: `validate_slideshow_outline.py` flagged the outline because of `[IMAGE: ...]` placeholders.
- **Cause**: Strict rule in `designing-slides/SKILL.md` forbidding image placeholders in outlines (since images are added manually post-upload).
- **Fix**: Removed all image placeholder lines from the markdown outline.

### Authentication Scope & Token Expiry
- **Issue**: Slideshow script failed with `invalid_scope` or `RefreshError`.
- **Cause**: ADC token had restrictive `drive.file` scopes, and `token.json` was expired/revoked.
- **Fix**: Updated `authenticate_google.py` to:
  1. Use broader `https://www.googleapis.com/auth/drive` scope.
  2. Implement a multi-token fallback (ADC → gdocs-token → legacy token).
  3. Provide clear instructions for `gcloud auth application-default login` if all fail.

### UnicodeEncodeError: 'charmap' on Windows
- **Issue**: `authenticate_google.py` crashed when printing `✓` or `⚠` to a Windows terminal file redirection.
- **Cause**: Windows CP1252 encoding doesn't support these symbols.
- **Fix**: Replaced special symbols with ASCII-safe text: `[OK]` and `[WARN]`.

