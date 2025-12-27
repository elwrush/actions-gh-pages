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

