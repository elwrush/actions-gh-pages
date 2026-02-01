# Error Fix Log - Jan 31, 2026

## Media & Asset Management
- **The 4K Video Trap**: Downloading "Original" video files from Pixabay (~80MB) destroys Git repository limits and causes deployment lag.
  - **Fix**: Use `process_video.py` to auto-trim to **7 seconds** and scale to **720p** before adding to the project.
- **Git History Purge**: Accidental push of large files requires a history rewrite.
  - **Fix**: `git reset --soft [last-good-commit]`, delete the file, then `git commit --amend` and `git push --force`.
- **Audio key mapping**: Renaming audio keys in `base.html` (e.g., `blip` -> `beep`) without updating the `AudioFX.init()` and `tick()` calls causes silent failures.
  - **Fix**: ALWAYS verify every JS callsite after renaming a key in the `AudioFX` object.

## JSON & HTML Engineering
- **Nested JSON Quoting**: Including `onclick` handlers with string arguments inside a JSON `content` field leads to "quote escaping hell."
  - **Fix**: Use single quotes for HTML attributes (`onclick='...'`) and escaped double quotes for JS strings (`\"timer-id\"`).
- **Blurry Text**: Applying multiple heavy `text-shadow` layers to darkened backgrounds creates a "blurred" or "unfocused" perception.
  - **Fix**: Use crisp, single-layer shadows or rely on background dimming (`data-background-opacity="0.4"`) for contrast.
- **Vertical Overflow**: Content "spilling" off slides is often caused by unnecessary decorative headers (Badges).
  - **Fix**: Delete "MISSION/TASK" badges to reclaim 80px of vertical space. 

## Typst & Tooling
- **Typst Root Paths**: Using `--root "."` restricts relative imports like `../../`.
  - **Fix**: Use absolute-style leading slash paths (`/skills/folder/file.typ`) which Typst resolves relative to the specified root.
- **Probabilistic Timing**: Validators checking only for `[XX Min]` strings miss timings passed as function arguments.
  - **Fix**: Use explicit regex `stage\(\s*".*?"\s*,\s*".*?"\s*,\s*"(\d+)"` to capture the 3rd argument. Perform deterministic math (`sum()`) and print the calculation to the console for verification.

# Error Fix Log - Jan 28, 2026

## Typst Production & Layout
- **Library Interface**: Do NOT assume function signatures in `@local` packages. ALWAYS `view_file` the `lib.typ` file first. (e.g., `bell_header()` in `@local/bell-sheets:0.1.0` requires no arguments or specific named arguments).
- **Library Override**: Direct modification of `@local` library files (e.g., `lib.typ`) is sometimes necessary to override hardcoded defaults, such as the `image_align` parameter added to `hero_strap` to prevent cropping the subject's face.
- **Auto-Margin Bug**: Typst cannot perform math on `auto` lengths (e.g., `page.height - page.margin`). 
  - **Fix**: ALWAYS set explicit page margins in the `.typ` file: `#set page(margin: (x: 2cm, top: 2cm, bottom: 2.5cm))`.
- **Markup Evaluation (External Files)**: Loading narrative text from `.txt` via `read()` prints content literally. To enable italics (`_text_`) or bold from files:
  - **Fix**: Use `#eval(read("file.txt").replace("[", "\[").replace("]", "\]"), mode: "markup")`.
- **Bracket Escaping**: Square brackets in external text files break the Typst parser inside `eval` mode.
  - **Fix**: Always escape brackets using `.replace("[", "\[").replace("]", "\]")` before evaluation.
- **Handwriting Space (Photocopy Rule)**: For 2-up (A5 on A4) printing, use **1.1cm** for full lines and **1.0cm** for compact lines. 0.85cm is too small for younger students.
- **Narrative Density**: Use **Single-Column** layout for stories to preserve emotional pacing. Columns are for analytical/informational data ONLY.
- **Logical Proximity**: Organize worksheets in silos: **[Text] -> [Quiz] -> [Writing Task]**. Decoupling quizzes from their texts increases cognitive load during flipping.

## Pedagogical Engineering
- **Deterministic Data Gates**: LLMs exhibit "probabilistic laziness" in distractor placement (often favoring B/C). 
  - **Fix**: Generate answer keys and anchor text via a Python script (e.g., `random.randint`) **BEFORE** generating the quiz to force the LLM to write content around a fixed answer index.
- **Answer Key UX**: Always provide a **Summary Guide** (e.g., 1. A, 2. B) at the top of the answer key page for rapid manual grading, followed by detailed pedagogical explanations.
- **CEFR Differentiation**: For B2 worksheets, ensure intro boxes and instructions use academic lexis (e.g., "radiant glory," "transcendence") to set a different register than B1 materials.

## Media Processing
- **Image Extension Spoofing**: The `generate_image` tool may produce a JPEG but return a filename with a `.png` extension.
  - **Fix**: Verify the image signature if Typst fails to decode. Use a Python script to check magic bytes if unsure. Rename extension to match reality.
- **Pathing**: Use relative paths (`assets/image.jpg`) for Typst compilation. Move remote/temporary images into a local `assets/` folder within the project root before compiling.

# Error Fix Log - Jan 27, 2026

## UI/UX Lessons
- **Font Size**: NEVER use fonts smaller than 18pt in presentations. Classroom projectors make them unreadable.
- **Container Width**: Standard 900px is too narrow for large-text slides. 1100px is the new standard.
- **Atmospheric Glow**: Use radial gradients with high blur (120px) instead of box-shadows to avoid a "boxy" look.
- **Image Resolution**: Always fetch `largeImageURL` (1280px) for backgrounds; 640px looks pixelated on screens.
- **HTML Syntax**: Be extremely careful with space in comments (`< !--`) as it renders the comment as visible text.
- **Media (Shorts)**: YouTube Shorts (9:16) require explicit dimensions (e.g., 315x560) and `data-autoplay`/`data-src` for reliable Reveal.js playback.
- **Contrast**: Never use white text on light-colored backgrounds (e.g., salmon/pinks). Always use a dark overlay or darkened background behind light text.
- **Typography**: Phonemic scripts (IPA) MUST be lowercase. Global CSS `text-transform: uppercase` on headers must be overridden for IPA spans (`text-transform: none !important`).
- **Layout Locking**: Forced horizontal layouts with `flex-wrap: nowrap !important` on `.cols` containers to prevent elements from stacking vertically on smaller displays.
- **Validator Sync**: Ensure `validate_presentation.py` supports `data-src` and `data-autoplay` as valid attributes to avoid false critical errors on lazy-loaded media.

## Previous Entries

# Errors & Fixes Log

## 2026-01-12 (Night) | Slideshow Generation Refinements

### ImportError due to Non-Existent Function in SKILL.md
- **Issue**: `ImportError: cannot import name ...` and flawed batching logic.
- **Cause**: The `designing-slides` skill documentation hallucinated a "Batch Helper Library" that doesn't exist. The actual library functions (`add_slide_content.py`) are designed for immediate execution, not batch request generation.
- **Fix**: 
  1. Updated `SKILL.md` to explicitly FORBID importing slide creation functions.
  2. Mandated the **"Self-Contained Script" Pattern**: Copy the working logic (including local `batchUpdate` calls) from known good examples (e.g., `create_presentation_structure_slides.py`) into the new script.
  3. Do NOT assume library functions support batching unless verified by reading the code.

### Incorrect Relative Import Paths
- **Issue**: `ModuleNotFoundError` when running scripts in subfolders.
- **Cause**: Scripts didn't add the root or skill directories to `sys.path`.
- **Fix**: Use `sys.path.insert(0, ...)` to explicitly add project root and skill script folders before imports. Do NOT rely on relative imports.

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
### Breakthrough: Dynamic Space-Filling (Typst 0.11+)
- **Problem**: Manual line counting (`for i in range(20)...`) is fragile. Content additions above lines cause spillover, and printing 2-up (A5 effectively) makes standard spacing too small for handwriting.
- **Solution**: Use **Context-Aware Math**.
  - **Logic**: `page.height - bottom_margin - here().position().y` = exact usable space.
  - **2-Up Rule**: Use **1.1cm** line spacing. When scaled 2-up on A4, this becomes ~7.8mm, which is the sweet spot for handwriting.
  - **Full Page Rule**: Use `#layout(size => { fill-space-with-lines(size.height) })` for continuation pages.
- **Result**: "Orphan-proof" worksheets that perfectly fill every page regardless of header size.
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

## 2026-01-29: Superconsumer Slides Refactor (Post-Mortem)
### Root Causes of Friction
1.  **Template vs. Data Mismatch**: 
    - *Issue*: `presentation.json` keys (`content`) did not match `answer.html` requirements (`answer`, `explanation`, `para`).
    - *Fix*: Always verify Jinja2 variable names in `templates/*.html` BEFORE writing the JSON configuration.
2.  **Unit Logic Failure (Timers)**:
    - *Issue*: `TimerPill` component multiplied input by 60 (expecting minutes), but JSON provided seconds.
    - *Fix*: Standardize all duration inputs to SECONDS across JSON and JS components.
3.  **Layout Overflow (Vertical Stacking)**:
    - *Issue*: Excessive padding (50px-60px) in `glass-box` containers caused content to clip on 16:9 screens.
    - *Fix*: Use max 30px padding for split layouts. implement generic `overflow-y: auto` for lists.
4.  **Pedagogical Logic**:
    - *Issue*: Linearly mapping textual options (A=Para 2, B=Para 3) is cognitively too easy/wrong.
    - *Fix*: Randomize checklist options in JSON and explicitly map answer keys.
5.  **Asset Propagation**:
    - *Issue*: Hardcoded GitHub URLs for large video assets caused "Missing Video" errors before deployment completed.
    - *Fix*: Use local relative paths `../images/` for development, and only swap to absolute URLs if strictly necessary for the build.

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

## 2026-01-13 | Authentication & Worksheet Pagination

### ADC Authentication "App Blocked" / Invalid Scope
- **Issue**: `gcloud auth application-default login` failed with `invalid_scope` and "This app is blocked" because it defaulted to the generic Google Cloud SDK client ID.
- **Cause**: Generic gcloud login didn't use the project's client ID.
- **Fix**: Force gcloud to use the project's client ID:
  ```powershell
  gcloud auth application-default login --client-id-file=".credentials/credentials.json" --scopes="https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/documents,https://www.googleapis.com/auth/cloud-platform"
  ```
- **Lesson**: Warn users to use project-specific auth commands.

### PDF Permission Denied (File Locking)
- **Issue**: `failed to write PDF file` during compilation.
- **Fix**: Forbid auto-opening PDFs. Use IDE preview links `[file](file:///...)`.

### Worksheet Pagination
- **Issue**: Worksheet spilled to 5 pages.
- **Fix**: Reducing writing lines and consolidating content.

---

## 2026-01-14 | Presentation Physics & Visual Process

### "Webpage Logic" vs "Slide Physics" (The Overflow Error)
- **Issue**: Presentation content "exploded" off the screen or overlapped.
- **Cause**: Treating slides like responsive webpages (using `height: 100%`, flex percentages). Slides are Fixed Artboards (960x700). Fluid percentages resolve to 0 or infinity in strange contexts.
- **Fix**: **Strict Fixed-Canvas Logic**.
  1.  Use `row-container` with explicit pixel heights (e.g., `500px`).
  2.  Hard-code `max-height: 400px` on ALL media (images/iframes).
  3.  Move branding to `absolute` position (z-index 10) so it doesn't consume flow space.
  4.  Use `r-fit-text` ONLY for titles (as it scales aggressively).

### The "Code-First" Failure
- **Issue**: Segues and layouts were ugly or broken ("poxy").
- **Cause**: Jumping straight to HTML coding (`index.html`) without a visual plan.
- **Fix**: **Mandatory 5-Step Gate**.
  1.  **Visual Plan (Markdown)**: Describe the *look* first (Goal: High Visual Engagement).
  2.  **User Approval**: Must explicitly approve the visual plan.
  3.  **Wireframe**: Map 960x700 canvas logic in Mermaid.
  4.  **Code**: Only now write HTML (using `REFERENCE_TEMPLATE.html`).
  5.  **Deploy**.

### GIF Backgrounds on Text
- **Issue**: Matrix rain GIF made text unreadable ("Yuck").
- **Lesson**: Motion backgrounds must be extremely subtle or use high-contrast text overlays. Static gradients ("Pop Style") are safer and often preferred.


---

## 2026-01-15 (Morning) | Worksheet Graphics & Layout Refinement

### Typst Grid Repeat Logic
- **Issue**: `#grid(rows: 10, line(...))` rendered only one line instead of ten.
- **Cause**: Typst grids map content to cells 1:1. A single content item fills only the first cell.
- **Fix**: Use `..range(10).map(_ => line(...))` to generate separate content items for each row.
- **Lesson**: Grids do not auto-repeat content; explicit loops are required.

### Meander & Image Alignment
- **Issue**: Using `meander` with `dy` offsets for image placement was fragile and misaligned with text paragraphs.
- **Fix**: Abandoned complex wrapping for standard block layout where possible, or placed images at `dy: 0` inside new flow contexts.
- **Refinement**: Switched to **transparent PNGs** (via `processing-images`) to avoid ugly white boxes disrupting text flow.

### Booklet Pagination Logic
- **Issue**: Tasks breaking across the "Sheet Boundary" (e.g., Page 4 to 5) in a booklet layout.
- **Fix**: Implemented strict **Manual Page Breaks** before tasks prone to spilling over sheet boundaries.
- **Rule**: "Tasks must not break across the fold (4-5, 8-9)."

### Handwriting Usability
- **Error**: "Definition" tasks used cramped 2-column grids; Writing tasks had single ruled lines.
- **Fix**:
  -   **Definitions**: Single column (or Auto+Line), Double Spacing (`1.5cm`).
  -   **Writing**: Grouped Prompts + 10 Double-Spaced Lines (Dark Gray).
  -   **Gap**: Mandatory `1.5cm` gap between prompt and first line.
  -   **Spatial References**: Use "words above" or strict Task X naming.

---

## 2026-01-15 (Midday) | Typst Lesson Planning & Cleanup

### Typst Stage Header Orphaned
- **Issue**: Stage header (maroon row) appeared alone at the bottom of the page.
- **Cause**: Typst tables don't automatically keep headers with rows when forced to break by content.
- **Fix**: Split the `stage_table` into two separate calls in the `.typ` file and insert a manual `#pagebreak()` between them.
- **Rule**: "Stage Heading + Procedure MUST share a page."

### Unclosed Raw Text in Component Template
- **Issue**: Typst compiler error `error: unclosed raw text`.
- **Cause**: Accidental triple backticks (```) left at the end of the `lesson-plan-components.typ` file after an edit.
- **Fix**: Deleted the stray backticks.

### Relative Image Paths in Shared Components
- **Issue**: `lesson_header()` failed to find `bell-header.jpg` (`file not found`).
- **Cause**: Path was `../../images/`, which works for root but fails when the component is imported by a file 3 levels deep (`inputs/folder/file.typ`).
- **Fix**: Corrected path to `../../../images/` in the shared component template.

### Differentiated Input Branding
- **Issue**: Rationale box showed "Optimal Input" or "Pedagogical Rationale: Optimal Input".
- **Fix**: Standardized the component to always render **Differentiated Input** (Bold) then **Pedagogical Rationale: Differentiated Input & Learner Autonomy** (Italic).

### Hallucinated Assets in Lesson Plan
- **Issue**: Lesson plan procedure instructed to "Show photo of Thai student with EKG", which did not exist.
- **Cause**: AI inventing ("hallucinating") specific visual details to make the lesson feel "real", without checking available assets.

---

## 2026-01-18 (Early Morning) | Cloudflare Deployment Catastrophe

### "Asset Too Large" & Root 404
- **Issue 1**: Cloudflare deployment failed with `Asset too large` (69.8 MiB > 25 MiB).
- **Cause**: Wrangler attempted to upload the hidden `.git/` directory because `wrangler.jsonc` was set to `assets: { directory: "." }` and `.wranglerignore` was ignored or insufficient.
- **Issue 2**: After excluding `.git`, the site deployed but returned **404**.
- **Cause**: The `build_dist.js` script copied files to `dist/` but did not include the specific presentation subfolder content at the root. The generic `index.html` was missing.
- **Fix**: Implemented a **"Whitelist Build Strategy"**:
  1.  Created `scripts/build_dist.js` to explicitly copy *only* the active presentation folder contents + shared assets (`js`, `images`, `audio`) to a clean `dist/` directory.
  2.  Targeted the specific presentation (e.g., `18-01-26_Global-Logistics...`) dynamically in the script.
  3.  Updated `wrangler.jsonc` to deploy `dist/`.
  4.  Added `"postinstall": "npm run build"` to `package.json` for CI automation.
- **Rule**: **NEVER deploy the project root (`.`)**. ALWAYS build a clean `dist/` folder containing only the production assets.

### Cloudflare API Token Permission Errors
- **Issue**: Wrangler deploy failed with "missing `Account:Cloudflare Pages:Read` permission".
- **Cause**: API token was created with "All accounts" in Account Resources, which paradoxically grants no access.
- **Fix**:
  1. Edit the token at https://dash.cloudflare.com/profile/api-tokens
  2. Set **Permission**: Account > Cloudflare Pages > Edit
  3. Set **Account Resources**: Include > [Your specific account name] (NOT "All accounts")
  4. **Roll** the token to regenerate the value after editing
  5. Update the `CLOUDFLARE_SLIDESHOW_API` User environment variable with the new token
- **Verification**: `curl "https://api.cloudflare.com/client/v4/accounts" -H "Authorization: Bearer <token>"` should return your account, not empty `result: []`.

### SSL Certificate Provisioning Delay
- **Issue**: New Cloudflare Pages deployment shows "ERR_SSL_VERSION_OR_CIPHER_MISMATCH".
- **Cause**: SSL certificates take 1-2 minutes to provision for new projects.
- **Fix**: Wait 1-2 minutes, or use the production URL (without deployment hash prefix).


---

## 2026-01-18 | Appositives Worksheet Refinements

### The "Fake PNG" Checkerboard Trap
- **Issue**: AI-generated images (Mona Lisa) had "baked-in" gray/white checkerboards instead of true transparency.
- **Cause**: Image generator simulated transparency in a flat opaque file.
- **Fix**: Created `remove_checkerboard.py` (now in `processing-images/scripts`) which samples the checkerboard colors and strips them to alpha transparency.

### Printer-Safe Branding (Intensive)
- **Issue**: Header image was clipped or inconsistent; maroon straps and text overlays were applied incorrectly.
- **Constraint**: Intensive worksheets MUST use only the full-width `intensive-header.jpg`.
- **Fix**: 
  1. Center the header image using `align(center)`.
  2. Provide at least **0.5cm of top padding** (avoid aggressive `dy: -1.5cm`).
  3. NEVER use `integrated_header()` or maroon straps for Intensive.

### Photocopier Survival (Line Visibility)
- **Issue**: Light gray ruled lines (#E0E0E0) become invisible or "noisy" on old school photocopiers.
- **Fix**: Mandate **Dark Gray (#333333)** for all handwriting lines and horizontal separators.

### Typst "Orphan" Header Prevention
- **Issue**: Task headers sitting alone at the bottom of a page.
- **Fix**: Wrap the header and its introductory text in a `#block(breakable: false)`. This forces the group to move to the next page together if they don't fit.

### Typst Syntax Robustness
- **Issue**: `warning: no text within stars` when using `**` or `*` near punctuation/nesting.
- **Fix**: Prefer Typst functional styling: `#strong[text]` and `#emph[text]` over Markdown-style stars.

### Pedagogical Whiplash (Thematic Inconsistency)
- **Issue**: Lead-in focused on Art (Mona Lisa), but Diagnostic test shifted to Bangkok Weather.
- **Cause**: Generic diagnostic examples created "pedagogical whiplash," breaking the lesson's storyline.
- **Fix**: Mandate **Thematic Consistency** in `writing-lesson-plans/SKILL.md`. All diagnostic and practice items must be linked to the core "Situation" or theme established in the Lead-in.

---

## 2026-01-18 (Midday) | Business Vocabulary: The Editorial Shift

### Typst Underscore "Emphasis" Trap
- **Issue**: Using `___` or `Task 1. ________` in Typst caused "unclosed delimiter" errors.
- **Cause**: Typst interprets underscores as emphasis/italic markers, and long strings of them can break the parser if nested.
- **Fix**: **FORBID underscores for gap fills**. Always use `#box(width: X, stroke: (bottom: 1pt + black))` for robust rendering.

### Transformation Hallucinations
- **Issue**: During "Rewrite the sentence" tasks, content drifted from source (e.g., "start a business" became "fly a plane").
- **Fix**: Implemented **Strict Source Verification Gate** in `developing-bespoke-materials`. AI must now verify every sentence against the `raw_content.md` before finalizing.

### Layout Density: "The Magazine Standard"
- **Issue**: Initial versions had too much whitespace, pushing content to Page 5.
- **Fix**:
  - Adopted **2-column grid** for reading and tasks.
  - Reduced `writing_lines` vertical spacing to **0.85cm**.
  - Increased Gap Fill `leading` to **1.8em** to ensure vertical writing space within paragraphs.
  - Used **Cinematic Headers** (full-width image + overlay) to save 2cm of vertical space compared to block-based headers.

### Validator Logic Errors
- **Issue**: `validate_lesson_plan.py` failed for lack of Thai scaffolding.
- **Resolution**: Removed the mandatory Thai check as it's no longer required by the user, and updated the script to be more flexible.

---

## 2026-01-18 (Night) | Presentation Deployment & Architecture

### Deployment Overwrite (The "Sprinter Ghost" Sequel)
- **Issue**: Deploying a new presentation (e.g., Appositives) completely removed the previous one (Fight or Flight) from the live URL.
- **Cause**: `build_dist.js` cleaned `dist/` and copied the new presentation to the root.
- **Fix**: 
  1. Updated `build_dist.js` to build ALL presentations into **unique subfolders** (e.g., `/QAD-Fight-or-Flight/`).
  2. Implemented a **Dashboard Generator** that creates an `index.html` indexing all lessons.
  3. Mandated **Stable URLs** in the `hosting-presentations` skill.
- **Result**: Multiple presentations now coexist peacefully on the same domain.

### Broken Link in Google Docs
- **Issue**: User reported "Fight or Flight" link pointed to the "wrong lesson."
- **Cause**: Link pointed to `lesson-slideshows.pages.dev` root, which had been overwritten by a subsequent project.
- **Fix**: Generated a new **Google Doc link** pointing to the stable subfolder URL. 
- **Rule**: Never link to the root; always link to the versioned/named subfolder.

---

## 2026-01-19 | Slide Design & Layout Refinements

### Split Layouts for Timer Slides (Global Rule)
- **Issue**: Timer pills were "stranded" at the bottom of slides, making layouts feel unbalanced.
- **Cause**: Slides used simple stacked layouts (Title → Content → Timer) instead of structured grids.
- **Fix**: **Whenever a slide has a `timer-pill`, use a 50/50 Split Layout**:
  - **Left Column**: Relevant image (`.col-50` + `.inset-media`).
  - **Right Column**: Instructions + Timer inside `.glass-box`.
- **Why**: This balances visual weight, gives the timer context, and makes slides look premium.

### Title Slide = Gold Standard First Impression
- **Issue**: Title slide was "horribly malformed" with a centered div overlay instead of the standard split layout.
- **Fix**: Title slides MUST follow the template's split layout:
  1. **Background**: Gradient (`var(--grad-main)`), NOT an image overlay.
  2. **Left Column (40%)**: Inset hero image with rotation (`rotate(-2deg)`) and cyan border.
  3. **Right Column (60%)**: Left-aligned text:
     - **Badge**: CEFR + Skill (e.g., "B1: VOCABULARY").
     - **Title**: Large `h1` (~60pt).
     - **Tagline**: Skewed span with maroon background.

### Teacher Notes ≠ Visible Content
- **Issue**: "Elicit: Branches, Headquarters, Exports" appeared directly on the slide.
- **Cause**: Misunderstanding of `.teacher-tip` vs `<aside class="notes">`.
- **Fix**: 
  - **`<aside class="notes">`**: For "Elicit" instructions, procedural cues (visible ONLY in Speaker View).
  - **`.teacher-tip` div**: For "Why?" explanations visible to STUDENTS on Answer slides.
- **Rule**: Students should see **questions**, not teaching prompts.

### Asset Paths are Fragile (The Growth Icon Bug)
- **Issue**: "Expand" slide showed broken image after moving `growth_icon.png`.
- **Cause**: Moved file to `images/` but forgot to update ALL `src=` references.
- **Fix**: When moving any image:
  1. Search (`grep`) for all occurrences of the filename in HTML.
  2. Update **every** reference before testing.
- **Rule**: Link changes are invisible until preview. Always verify paths immediately.

### Segue Angles Must Be Consistent
- **Issue**: "Boss Level: Transformation" segue was "angled the wrong way" (positive rotation).
- **Cause**: Inline `style="transform: rotate(2deg)"` overrode the class's default `-3deg`.
- **Fix**: **Never override `.segue-title` transform inline**. The class already has `rotate(-3deg) skew(-10deg)` for consistency.
- **Exception**: Only override if intentionally differentiating (e.g., final boss, danger warning).

### Content Belongs on Introduction Slides
- **Issue**: Put the "Expand" growth icon on the Answer slide (2.9) instead of the Vocabulary Introduction slide (13).
- **Fix**: Visual assets (icons, diagrams) belong on the slide that **introduces** a concept, not the slide that **tests** it.
- **Rule**: "First slide to name [X]" = where the visual asset goes.

### CSS Class Missing (.col-50)
- **Issue**: Split layouts broke silently because `.col-50` wasn't defined in the `<style>` block.
- **Fix**: Added `.col-50 { flex: 0 0 50%; max-width: 50%; }` to CSS.
- **Rule**: Before using any `.col-*` class, verify it exists in the HTML's `<style>` or in `COMPONENTS.md`.

---

## 2026-01-21 | Critical Slideshow Architecture Fixes

### CRITICAL: Content Hallucination/Truncation
- **Issue**: Agent invents or omits worksheet content, requiring 30+ minutes of manual repair per slideshow.
- **Root Cause**: No verification step. Agent reads worksheet once, then generates from memory.
- **Fix**: Added **Step 0.6: Source Content Extraction Gate** to `creating-html-presentation/SKILL.md`:
  1. Agent MUST extract ALL content from worksheet into a checklist BEFORE coding
  2. Checklist includes exact task names, question wording, and answers
  3. Agent presents count ("X tasks, Y questions") for user verification
  4. After coding, every checkbox must be ticked
- **Impact**: Deterministic mapping from worksheet to slides - no more invention.

### CRITICAL: Vertical Stacking Causes Hidden Content
- **Issue**: Slides stack content top-to-bottom in narrow columns, causing timers and lower content to be hidden below the 700px canvas.
- **Visual**: Content crammed in center column with wasted horizontal space.
- **Fix**: Added **HORIZONTAL-FIRST LAYOUT RULE** to `creating-html-presentation/SKILL.md`:
  - Task slides MUST use `.row-container` with 50/50 splits
  - Glass boxes must be at least 700-800px wide
  - BANNED: Narrow centered stacking (`width: 500px; margin: 0 auto`)
  - REQUIRED: Horizontal expansion using flex or grid
- **Pre-Build Checklist** added:
  - [ ] Does every content slide use `.row-container`?
  - [ ] Is all text visible within 700px height?
  - [ ] Are timers inside `.glass-box`, not floating?
  - [ ] Is glass box at least 700px wide?

### Dashboard Broken Links (Deferred)
- **Issue**: Clicking cards on `lesson-slideshows.pages.dev` causes recursive URL appending (`/folder/folder/folder/`).
- **Status**: Deferred. Direct links via Google Docs workflow unaffected.
- **TODO**: Fix relative link logic in `build_dist.js` dashboard generation.

---

## 2026-01-26 | Typst Syntax & Image Decoding

### Typst: Invalid Color/String Methods
- **Issue**: `type color has no method with_alpha` and `type string has no method upper`.
- **Cause**: Using method-style syntax (`.with_alpha()`, `.upper()`) which is not supported for these types in Typst 0.11.
- **Fix**: Use functional syntax: `rgb(r, g, b, alpha)` and `upper(string)`.

### Typst: PNG Decoding Errors
- **Issue**: `failed to decode image (Format error decoding Png)`.
- **Cause**: AI-generated PNGs sometimes have metadata or structure that Typst's decoder finds invalid.
- **Fix**: Re-save the image using Python's `PIL` library (`img.save(path, 'PNG')`) to normalize the format.

### Typst: Local File Access
- **Issue**: `failed to load file (access denied) ... cannot read file outside of project root`.
- **Cause**: Typst restricts file access to the directory it is compiled from.
- **Fix**: Always use the `--root "."` flag in the compile command to allow absolute paths from project root.

### PDF: Orphaned Task Headers
- **Issue**: Task headings floating at the bottom of pages.
- **Fix**: Wrap the heading + prompt in a `#block(breakable: false)`.

---

## 2026-01-27 | GDrive Sync Errors & Targeted Build Hardening

### GDrive "desktop.ini" Copy Failures
- **Issue**: `fs.cpSync` and `shutil.copytree` failed on Windows when trying to copy folders containing `desktop.ini` or hidden GDrive metadata.
- **Cause**: Google Drive synchronization creates hidden system files that are often locked or have restricted permissions, causing "Permission Denied" or "File Not Found" errors during recursive copies.
- **Fix**: Implemented a **System File Filter** in all build and generation scripts.
  - **Node.js**: Added a `filter` to `fs.cpSync` that checks `path.basename(src).toLowerCase() !== 'desktop.ini'` and excludes hidden files (starting with `.`).
  - **Python**: Used `shutil.ignore_patterns('desktop.ini', '.*')` in `shutil.copytree`.
- **Lesson**: Never perform raw folder copies in a GDrive-synced environment without a whitelist/blacklist filter.

### Windows Folder Lock (-4051)
- **Issue**: `fs.rmSync` or `Remove-Item` for `dist/` folder failed because the folder was "in use" by a background process (Wrangler, Browser, or File Explorer).
- **Fix**: 
  1. Wrapped cleanup in `try-catch` blocks to prevent the entire build from crashing.
  2. Pivoted from "Delete-and-Rebuild" to "Create-If-Missing & Overwrite" to handle locked directories gracefully.
- **Lesson**: Don't let a cleanup failure block a production build. Warn and proceed.

### Targeted Build Logic
- **Issue**: Full project builds (copying 10+ presentations) were slow and prone to recursive errors.
- **Fix**: Updated `build_dist.js` to support a **Target Filter**.
  - `node scripts/build_dist.js [folder-name]` now builds ONLY that specific lesson.
  - If no folder is provided, it defaults to a full build (safeguard).
- **Lesson**: Development velocity requires targeted tooling, especially when dealing with large asset counts.

### Wrangler Pages Build Directory
- **Issue**: Cloudflare Pages deployment failed or gave warnings about missing configuration.
- **Fix**: Added `"pages_build_output_dir": "dist"` to `wrangler.jsonc` and removed incompatible `assets` blocks.
- **Lesson**: Keep `wrangler.jsonc` minimal and specific to the `dist/` output for Pages.

### Windows File Locking (EBUSY) during Build (Part 2)
- **Issue**: `node scripts/build_dist.js` failed with `syscall: 'unlink'` during `fs.cpSync` because `dist` contained files locked by other processes (VS Code, Wrangler).
- **Cause**: The script's "clean `dist`" logic was commented out, leading to unsafe overwrites. Even if enabled, standard `rmSync` fails instantly on locks.
- **Fix**: Implemented `robustClean(dir)` in `build_dist.js` with a 5-step retry loop and busy-wait delay.
## 2026-01-29 | Presentation Animation & Logic

### Auto-Animate "Wreckage" (Global vs Local)
- **Issue**: Attempting to add `data-auto-animate` to ALL slide types caused title and video headers to morph unexpectedly ("wrecked" layout).
- **Cause**: Applying animation attributes globally without managing the shared `data-id` namespace.
- **Fix**: **Scope Animations Locally**. Only apply `data-auto-animate` to specific transitions (e.g., Segue -> Mission). Don't force it on static content slides like Titles unless strictly designed for it.

### Vocab Matching: Disappearing Rows
- **Issue**: Rows 3-5 vanished on the "Answer" slide during transition.
- **Cause**: The `presentation.json` for the answer slide only contained 2 items (the distractors) instead of the full set of 5. Reveal.js can't animate elements that don't exist in the DOM.
- **Fix**: **Data Parity**. The Answer slide MUST contain the exact same list of items as the Question slide. Only the `is_answer` flag should change.

### Vocab Matching: The "Floating Column"
- **Issue**: The numbered word list moved around or disappeared during animation.
- **Fix**: **Anchor the Left Column**. Use `data-id="fixed-word-{{id}}"` for the left column (words) and `data-id="moving-def-{{id}}"` for the right column (definitions). Ensure the HTML structure for the fixed column is identical on both slides.

### Video Background Loops
- **Issue**: Short looping videos (e.g., 2-second clip) are distracting behind text.
- **Fix**: Remove `data-background-video-loop`. Let the video play once and freeze on the final frame (which should be visually compatible with the text).

---

## 2026-01-29 | CI/CD, Private Repos & Asset Propagation

### GitHub Pages "Write Access Denied" (403)
- **Issue**: GitHub Actions failed with `403 Forbidden` while trying to push to the `gh-pages` branch.
- **Cause**: Default `GITHUB_TOKEN` permissions in standard workflows are restricted to read-only.
- **Fix**: Added `permissions: contents: write` to the `deploy` job in `.github/workflows/deploy.yml`.
- **Lesson**: CI/CD automation that modifies branches requires explicit write consent in the workflow YAML.

### "Unable to resolve action... version master"
- **Issue**: Deployment failed because the workflow was looking for `@master` in an action repository that only uses `@main`.
- **Fix**: Updated the `uses` field to point to the correct branch. Transitioned to official `peaceiris/actions-gh-pages@v4` for stability.

### "File not found: lib/index.js" (Action Failure)
- **Issue**: GitHub Action failed with a missing entry point error.
- **Cause**: Using source-only forked actions that haven't been compiled into the expected distribution structure.
- **Fix**: Standardized on official, pre-compiled tagged releases (@v4).

### Sub-Folder 404s (Missing Styles/JS)
- **Issue**: Presentations loaded text but no CSS/JS (404 errors).
- **Cause 1**: The `.gitignore` file was recursively masking `dist/` folders inside `inputs/`.
- **Cause 2**: `generate_presentation.py` was skipping copies if the folder already existed, missing new theme updates (e.g., `noir.css`).
- **Fix**: 
  1. Updated `.gitignore` to be root-specific (`/dist/`).
  2. Updated generation script with `dirs_exist_ok=True`.
- **Lesson**: Ensure local generation logic is "Merge-Safe" and `.gitignore` doesn't block legitimate production assets.

### Redundant Repository Bloat (40MB Redundancy)
- **Issue**: Repository size ballooned due to duplicate videos in every presentation folder.
- **Fix**: Implemented the **Global Asset Pattern**. Move shared media to root `images/` and reference via absolute HTTPS URLs from the CDN.
- **Lesson**: Use the GitHub Pages host as a centralized asset server for shared media to keep deployment folders lightweight.

### GitHub Pages 404 on Private Repos
- **Issue**: Even after "Success" in Actions, the URL returned a 404.
- **Cause**: GitHub Pages requires a paid subscription for Private repositories.
- **Fix**: Changed repository visibility to **Public**.
- **Lesson**: Public repositories are the standard for free GitHub Pages hosting.
## 2026-01-29 | Worksheet Layout Hardening

### Confusing Leading with Writing Space
- **Issue**: Worksheet text exploded vertically, breaking layouts across 5 pages.
- **Cause**: Applied "0.9cm" instruction to `#set par(leading: 0.9cm)` (body text) instead of just the handwriting lines.
- **Fix**: Updated `producing-educational-materials/SKILL.md` to strictly separate:
  - **Body Text**: `0.55em` (Compact, professional)
  - **Handwriting**: `0.9cm` (Room for student writing)

### The "Grow-D" Grid Collision
- **Issue**: Option "D" in multiple choice was pushed off the page or overlapped "C".
- **Cause**: Using a 2-column grid (`1fr, 1fr`) for long sentence options.
- **Fix**: Mandate **Single Column** grids (`columns: (1fr)`) whenever options are full sentences.

### Task Gutter Collision
- **Issue**: Question text touched the "T / F / NG" block.
- **Fix**: Added mandatory `column-gutter: 1cm` to all Task grids.

### Unprompted Script Execution
- **Issue**: Ran `node scripts/build_dist.js` repeatedly without user request, causing confusion about "GitHub uploads".
- **Fix**: Explicitly forbade unprompted deployment script usage in the Skill definition.

## 2026-01-29 | File Naming Discipline
### Incorrect Lesson Plan Filenames
- **Issue**: Lesson plan was named `27-01-2026-LP-B1-Superconsumer-Generation-E.typ`, violating the strict project convention.
- **Fix**: Updated `writing-lesson-plans/SKILL.md` to enforced the canonical format: `[DD-MM-YYYY]-LP-and-slideshow-[Level]-[Topic]-[Shape].typ`.
- **Lesson**: Do not invent filenames. Always check the `SKILL.md` "File Naming & Location Discipline" section first.

# Error Fix Log - Jan 31, 2026 (Afternoon)

## UI & Template Engineering
- **Ghost Badges**: Deleting a badge from JSON didn't remove it because templates had hardcoded fallbacks (e.g., {{ badge | default('ANSWERS') }}).
  - **Fix**: Audit all templates (nswer.html, mission.html) and remove hardcoded string fallbacks. Use strict Jinja2 if checks.
- **Audio Scrubber Overflow**: Audio players often "exploded" out of narrow table columns.
  - **Fix**: Use ox-sizing: border-box, overflow: hidden, and a responsive width: 95%. Always place players in a colspan header row if part of a grid.
- **Video Loop Fatigue**: Background videos looping continuously behind text become a distraction.
  - **Fix**: Set "video_loop": false and ensure templates remove the data-background-video-loop attribute.
- **Phonemic Uppercasing**: Browser-level 	ext-transform: uppercase destroys the accuracy of IPA symbols.
  - **Fix**: Wrap symbols in <span class='phonetic'> and use 	ext-transform: none !important in the global CSS.

## Workflow & Discipline
- **The Reasoning Trap**: Relying on the model to "remember" the Rule of 3 Lines or video duration leads to failure.
  - **Fix**: USE HOOKS. If a rule can be expressed as a regex or a duration check, it MUST be a pre-command hook.
