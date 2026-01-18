
---

## 2026-01-14 | Presentation Physics Overhaul & Visual Workflow

### Key Technical Achievement: "Fixed Canvas Logic"
- **Problem**: Fluid/Responsive layouts (`height: 100%`) caused content to overflow or disappear on large screens ("Webpage Logic").
- **Solution**: Adopted **Fixed Artboard Logic** (960x700px).
  - Explicit pixel heights for rows (`500px`).
  - Strict `max-height: 400px` for all media.
  - Floating "Cyber Pill" header (`absolute`, `z-index: 10`) to remove layout impact.
  - **Result**: Perfect deployment on Cloudflare (Desktop & Mobile).

### Workflow Pivot: The "Visual First" Standard
- **Change**: Moved from "Code-First" (writing HTML directly) to a **5-Step Gated Workflow**.
  1.  **Theme Selection**: Dynamic choice (Cyber, Noir, Minimal).
  2.  **Visual Plan (Markdown)**: Descriptive planning of visuals with pedagogical intent.
  3.  **User Approval**: Explicit "Stop & Check."
  4.  **Wireframe**: Canvas logic mapping (Mermaid).
  5.  **Implementation**: Copying the Gold Standard `REFERENCE_TEMPLATE.html`.

### Pedagogical Upgrades
- **Source Sync**: Slides must strictly match Worksheet task names (e.g., "TASK 2").
- **Answer Keys**: Enforced "Single Answer Interleaving" (One answer per slide, immediately following question, with 'Why' explanation).
- **Voice**: "Pop & Verve" tone mandated (e.g., "YOUR MISSION" instead of "Task").
- **Infographics**: Prioritized **Generative AI** for "Pop" visuals; restricted Mermaid to technical data.

### Feature Addition: TTS Vocabulary Audio
- **Requirement**: "Direct Vocabulary" slides must include audio pronunciation context.
- **Engine**: **Gemini 2.5 Pro Preview TTS**.
- **Implementation**:
  - Script: `skills/creating-html-presentation/scripts/generate_vocab_audio.py`
  - Output: `.wav` files in `images/audio/`
  - UI: Stylized "Cyber" audio player with "Listen!" label.

### Skill Upgrade
- **`creating-html-presentation`**: Fully rewritten to version 2.3.
- **Reference**: `REFERENCE_TEMPLATE.html` created and updated with new CSS (`.audio-player`).

---

## 2026-01-15 | Worksheet Graphics & Layout Refinement

### Visual Upgrade: "Transparent Layouts" & "Defined Motifs"
- **Goal**: Move away from blocky, whitespace-heavy images to integrated layouts.
- **Action**:
  -   **Trimming**: Implemented `trim_image.py` to auto-crop whitespace from generated assets.
  -   **Transparency**: Enforced transparent PNGs for all non-rectangular motifs.
  -   **Separators**: Standardized on "Wide Trimmed" motifs (e.g., EKG line) for section breaks.

### Usability: "The Handwriting Standard"
- **Problem**: Previous templates ignored physical space needed for handwriting.
- **Solution**:
  -   **Writing Tasks**: Dedicated page, Grouped Prompts, 10 Double-Spaced Lines (Dark Gray).
  -   **Definitions**: `Word: ____________` layout (Auto + 1fr Line) with 1.5cm spacing.
  -   **Matching**: Minimum 1cm gap between items.

### Layout: "Booklet Safety"
- **Constraint**: Printing on A3 folded (Booklet).
- **Rule**: Content must never split across the "Page 4 -> 5" boundary (Sheet transition).
- **Implementation**: Strict manual page breaks enforced at these boundaries to keep Tasks self-contained on a physical sheet.

### Skill Update
-   **`developing-bespoke-materials`**: Updated with strict rules for Pagination, Image Quality, and Handwriting Spacing.
-   **`processing-images`**: Created new skill for image hygiene.

---

## 2026-01-15 (Midday) | Typst-Only Workflow & HTML Decommissioning

### Key Technical Achievement: Typst Standardization
- **Pivot**: Successfully completed transition to **100% Typst-only** workflow for professional PDF lesson plans.
- **Decommissioning**: Fully removed legacy HTML-to-GDocs pipelines, WeasyPrint-related scripts, and the `pushing-to-gdocs` skill.
- **Centralization**: All lesson plan UI components (Headers, Metadata, Stage Tables) now live in a single library: `skills/writing-lesson-plans/templates/lesson-plan-components.typ`.

### Workflow Optimization: "The Orphan Fix"
- **Standard**: Implemented a mandatory "Self-Audit for Orphans" in the workflow.
- **Implementation**: If a Stage Heading is orphaned, the `stage_table` is split into two blocks with a manual `#pagebreak()` in between.
- **Validation**: Updated `validate_lesson_plan.py` to be 100% Typst-focused (removing HTML parsing logic).

### Branding & Pedagogy
- **Naming**: Formally adopted **"Differentiated Input"** as the standard terminology for student text choice, replacing "Optimal Input".
- **Density**: Validated "Fight or Flight" (Shape E) for detail density against the model YAML, ensuring procedures are "thick" and professional.
- **Ethics**: Implemented strict rules against **"Dojo Rewards"** (Intrinsic motivation only) and **"Hallucinated Assets"** (Lesson plans must only reference existing files).

### Housekeeping: Decommissioning
- **Action**: Deleted `design-slides` workflow and confirmed removal of legacy `designing-slides` skill artifacts. This is replaced by the modern `creating-html-presentation` standard.

---

## 2026-01-15 (Afternoon) | Presentation Workflow Violations Identified

### Critical Issue: Skill Non-Compliance
- **Problem**: During creation of "Relative Clauses" presentation, multiple violations of the `creating-html-presentation` skill workflow were identified.
- **Root Cause**: Agent did not strictly follow the 5-step gated workflow defined in `skills/creating-html-presentation/SKILL.md`.

### Violations Detected:
1. **Missing Answer Slides**: Initial version did not include answer key slides (required by pedagogical standards).
2. **Content Overflow**: Font sizes too large, causing text to overflow slide boundaries (violated Fixed Canvas Logic).
3. **Incomplete Interleaving**: Answers were not properly interleaved after each task slide.

### Corrective Actions Taken:
- Added 3 answer key slides (Task 1, 2, 3 answers).
- Reduced font sizes across all slides for proper fit within 960x700 canvas.
- Compressed table layouts and shortened text where necessary.

### Mandatory Reminder for Future Sessions:
⚠️ **ALWAYS REVIEW `skills/creating-html-presentation/SKILL.md` BEFORE CREATING PRESENTATIONS**
- The skill contains critical workflow gates and quality standards.
- Do NOT skip the Visual Plan approval step.
- Do NOT assume answer slides are optional.
- Do NOT use fluid layouts or percentage-based heights.

### Action Item:
- Future agents must explicitly confirm they have read the skill file before proceeding with presentation creation.

---

## 2026-01-16 | Full Skill Audit & Global Documentation Skills

### Major Achievement: Project-Wide Skill Compliance Audit
- **Action**: Evaluated all 8 project skills against `knowledge_base/using-skills.md` standards.
- **Result**: All skills now fully compliant with:
  - YAML frontmatter (name + description)
  - Third-person descriptions
  - Gerund naming convention
  - Deterministic validator scripts
  - Explicit workflow gates

### Skills Fixed:
| Skill | Issue | Fix |
|:---|:---|:---|
| `generating-worksheets` | Missing Bell/Intensive header logic | Added Step 0 context check + Intensive template |
| `using-meander` | No fallback strategy | Added Troubleshooting + Fallback sections |
| `hosting-presentations` | Missing YAML frontmatter | Added frontmatter, fixed naming mismatch |
| `writing-lesson-plans` | Validator not mandated | Added Step 9: Validate (MANDATORY) |
| `developing-bespoke-materials` | No validation step | Added Step 5.5 delegating to child validators |

### Deleted:
- `writing-bespoke-materials` (legacy HTML/WeasyPrint sub-skill) — superseded by parent skill.

### New Global Skills Created:
1. **`fetching-docs-context7`**: Retrieves LLM-optimized documentation from Context7 API.
2. **`crawling-official-docs`**: Scrapes official doc sites via Firecrawl API.

### Global Skill Validator Updated:
- Added `fetching-` and `crawling-` to recognized gerund patterns.
- All new skills validated and passing.

---

## 2026-01-16 (Afternoon) | Interactive Audio Timers & Web Component Architecture

### Key Technical Achievement: Immersive Audio Feedback
- **Problem**: Classroom timers were purely visual, requiring constant teacher monitoring.
- **Solution**: Integrated a synchronized audio feedback system:
  - **`blip.mp3`**: Rhythmic tick every second for urgency.
  - **`30-seconds.mp3`**: Voice warning at the wrap-up mark.
  - **`bell.mp3`**: Deep meditation chime for task completion.
- **Implementation**: Global audio singletons for performance, synchronized with the timer heartbeat.

### Architectural Pivot: Native Web Components (`<timer-pill>`)
- **Problem**: Legacy `initTimers` procedural logic was verbose (40+ lines of HTML per slide) and prone to initialization errors.
- **Solution**: Refactored the timer into a **Native Web Component** (`TimerPill`).
- **Impact**:
  - **Declarative Syntax**: `<timer-pill duration="5"></timer-pill>` replaces complex nested divs.
  - **Encapsulated Logic**: State, audio, and display are self-managed within the component class.
  - **Code Reduction**: **97.5% reduction** in per-slide HTML boilerplate.

### Modular Documentation & Quality Control
- **Created `COMPONENTS.md`**: Single source of truth for 20+ documented CSS classes and components.
- **Created `DECISION_TREE.md`**: Logic gates for implementation decisions (Text vs. Image vs. Layout).
- **Established `docs/` Folder**: Curated Reveal.js documentation for Layout and Backgrounds.
- **Workflow Update**: Step 5 now mandates "Required Reading" of these new resources to prevent common errors (font overflow, class misuse).

### Validator Upgrade: "The Enforcement Layer"
- **Enhancement**: Substantial upgrades to `validate_presentation.py`:
  - Enforces `.inset-media` or `.constrained-media` on all images.
  - Mandates `.slide-canvas` wrapper for layout stability.
  - Verifies audio dependencies (`audio/*.mp3`) for timer functionality.
  - Checks for "Answer Interleaving" (Answer slide must follow Task slide within 3 slides).
  - Detects missing timers on task-bearing slides.

### Strategic Evaluation: Vanilla vs. React
- **Action**: Evaluated Reach-based wrappers (`revealjs-react`, etc.) vs. the current Native Web Component approach.
- **Decision**: **STAY WITH VANILLA/NATIVE**.
- **Reasoning**:
  - Native Components provide 90% of React's DX (declarative tags) with **0% build overhead**.
  - No `node_modules` or build pipeline required for teachers to preview slides.
  - Simpler for LLM agents to generate correct, valid HTML.

### Compliance & Pedagogical Strengthening
- **Gate 2 Fix**: Added explicit **STOP AND WAIT** command for Audience selection (Middle vs. High School).
- **Tone Standardization**: Added a "Tone Comparison Table" showing exactly how slide titles, instructions, and motivation differ between audiences.
- **Result**: Auditor confirmed the skill is now **100% compliant** with the Antigravity Skills standard.

### Audit Result:
- **Presentation Verified**: `18-Jan-Reading/index.html` was audited using the new validator. It identified 21 critical issues, validating the power of the new enforcement system.

### Decommissioning: Branding Logos
- **Action**: Fully removed all Bell/Intensive logo logic from `SKILL.md` and `validate_presentation.py`.
- **Reason**: User requirement—"These slides should not have a Bell logo [or Intensive logo] at all, ever."
- **Status**: Presentations are now 100% unbranded/clean by default.


### 2026-01-18: Presentation Deployment Troubleshooting
- **Issue**: "Global Logistics" presentation deployment failed to load external `slide-components.js` due to path resolution errors and Cloudflare MIME type mismatches (returning 404 HTML for JS files).
- **Attempted Fixes**:
    - Corrected relative paths (`../skills/...`).
    - Moved script to root (`/js/slide-components.js`) and used absolute paths.
    - **Inlined JavaScript directly into `index.html`** (Best Practice for reliability).
    - Created `live.html` to bypass potential browser caching.
- **Deployment Failure**: Initial git push triggered "Asset too large" error (uploading `.git` folder).
- **Resolution**:
    - **Architecture**: Implemented a **"Whitelist Build Strategy"**.
    - **Script**: `scripts/build_dist.js` now builds a clean `dist/` folder containing *only* the specific presentation content and shared assets.
    - **CI**: Configured `package.json` (`postinstall`) and `wrangler.jsonc` to deploy this clean `dist/` folder.
- **Status**: **SUCCESS**. Presentation is live and fully functional at the worker URL.

### 2026-01-18 (Continued): Worksheet Fixes
- **Issue 1**: Intensive worksheets displayed legacy text strap instead of the mandatory `intensive-header.jpg`.
- **Fix 1**: Updated `intensive_worksheet_template.typ` and `15-01-26...Intensive.typ` to use the image header. Updated `generating-worksheets` skill to forbid text straps.
- **Issue 2**: Excessive whitespace on Page 2 due to aggressive `#pagebreak()` after Task 1.
- **Fix 2**: Removed forced page break. Verified cleaner layout.
- **Feature**: Added modular `#gapfill_exercise` component to template.
- **Fix 3**: Replaced text gaps in Task 2 with physical writing lines using the new component. Verified PDF.
- **Housekeeping**: Moved misplaced "Fight or Flight" Lesson Plan and Worksheet source (`.typ`) to `inputs/QAD-Fight-or-Flight` for consolidation.

---

## 2026-01-18 (Evening) | The "Fight or Flight" Deployment Crisis (RCA)

### Post-Mortem: "The Sprinter Ghost"
- **Issue**: Deploying the "Fight or Flight" presentation consistently served a legacy "Sprinter" theme (Maroon/Yellow) instead of the approved "Red Alert" (Cyber/Red) version.
- **Root Cause**: A perfect storm of **Path Collision** and **Cache Persistence**.
  -   The deployment pipeline was building from `presentations/18-01-26_Fight-or-Flight/`, which contained an older project version.
  -   Even after local `dist/` updates, Cloudflare Pages continued to serve the cached athlete visual.
  -   Agent confusion: Multiple copies of `index.html` existed in `inputs/`, `presentations/`, and the root, leading to "Whack-a-Mole" updates where the wrong source was repeatedly promoted.

### Failed Interventions:
1.  **Direct Overwrite**: Overwrote `dist/` and `presentations/` files - **FAILED** (Cache held old assets).
2.  **`build_dist.js` Logic**: Forced the script to pull from `inputs/QAD-Fight-or-Flight` - **FAILED** (Deployment still showed Sprinter).
3.  **Manual Header Check**: Added `v1.txt` marker - **FAILED** (404/Index redirect obscured verification).

### Corrective Strategy: "The Cache-Buster Pivot"
- **Action**: Abandoned the legacy path entirely.
- **Implementation**:
  -   Created a new, unique deployment path: `/red-alert-slides/`.
  -   Updated `build_dist.js` to target this unique folder name.
  -   Updated `link.html` and the global `presentations/index.html` to point to the new URL.
- **Strict Verification**: Mandated a manual check of `images/brain_alarm.png` existence within the build script before allowing the push.

### Status:
-   **RESOLVED**: See 2026-01-18 (Morning) below.

---

## 2026-01-18 (Morning) | Deployment Architecture Overhaul

### Key Achievement: Consolidated Deployment Pipeline
- **Problem**: Multiple copies of presentations scattered across project root, causing "Sprinter Ghost" deployment bugs.
- **Solution**: Established **single source of truth** architecture:
  1. All presentation files must live in `inputs/[QAD-folder]/` alongside lesson plan and worksheet.
  2. Deleted duplicate folders: `18-01-26_Fight-or-Flight/`, `slideshow-fight-or-flight/`, `presentations/18-01-26_Fight-or-Flight/`.
  3. Updated `creating-html-presentation` skill with **mandatory co-location rule**.

### Build Script Modernization
- **Before**: `build_dist.js` had hardcoded presentation paths.
- **After**: CLI-based invocation: `node scripts/build_dist.js <folder-name>`
  - Validates source exists in `inputs/`
  - Lists available folders if no argument provided
  - Checks for required files before completing

### Cloudflare API Token Setup
- **Issue**: Wrangler OAuth failed in headless environment; existing token lacked Pages permissions.
- **Solution**: Created new token with correct permissions:
  - Permission: **Account > Cloudflare Pages > Edit**
  - Account Resources: **Specific account** (not "All accounts")
  - Stored in `CLOUDFLARE_SLIDESHOW_API` User environment variable

### Deployment Projects
| Project | URL | Method |
|:---|:---|:---|
| `lesson-slideshows` | lesson-slideshows.pages.dev | Direct Wrangler deploy |
| `lesson-plan-agent` | lesson-plan-agent.pages.dev | Git-connected CI deploy |

### Skill Updates
- **`hosting-presentations`**: Completely rewritten for direct Wrangler deployment with API token.
- **`creating-html-presentation`**: Added mandatory co-location rule at top of SKILL.md.

### Live URLs
- **Fight or Flight Slideshow**: https://lesson-slideshows.pages.dev
- **Presentations Dashboard**: https://lesson-plan-agent.pages.dev/presentations/

