# GEMINI.md - Lesson Plan Agent & Slideshow Factory

## Project Overview
This project is an **AI-powered Lesson Planning Assistant and Slideshow Factory** designed specifically for **Thai Middle School ESL learners** at the Bell Language Centre. It utilizes a **Skills-based Architecture** to ensure pedagogical accuracy, visual consistency, and technical robustness.

### Core Technologies
- **Logic & Automation:** Python 3.x
- **Presentations:** Reveal.js (HTML/JS/CSS)
- **Document Generation:** Typst (Lesson Plans/Worksheets)
- **Serving:** GitHub Pages (Deployment)
- **Data Format:** JSON-driven presentations (`presentation.json`)

## Building and Running

### Building
- **Build Target Lesson**: `python build.py [lesson-name]`
- **Validation**: Run `python scripts/validate_presentation.py` or `.gemini/hooks/present-validator.py`

## Critical Mandates & Conventions

### 1. The Skill Activation Gate (MANDATORY)
Before starting ANY task, identify the task type and read the corresponding skill file in `/skills/[skill-id]/SKILL.md`.
- `00-manage-git-workflow` (Source Repo Management)
- `00a-manage-gh-pages-workflow` (Live Deployment Management)
- `01-grabbing-youtube-transcripts`
- `02-writing-lesson-plans` (Enforces Shape & Pedagogical Density)
- `03-producing-educational-materials` (Worksheets & PDFs)
- `04-searching-pixabay` (Mandatory for unique assets)
- `06-creating-html-presentation` (Standalone Bundle Engine)
- `07-generating-quizzes`
- `08-using-meander`
- `11-uploading-to-google-drive`
- `12-rendering-prompts-into-mermaid`
- `14-delegating-to-jules`
- `15-consulting-typst-repo` (MANDATORY for all .typ work)
- `16-consulting-global-repos` (GitHub API Fetcher - Authenticated via GITHUB_MCP_PAT)

### 2. Guardrails & Hooks
Automated validation is enforced via `.gemini/hooks/`:
- `lp_gatekeeper.py`: Blocks `.typ` generation until blueprint approval.
- `present-validator.py`: Enforces presentation JSON schema and verbatim alignment. **MANDATORY**: This hook MUST always force a fresh HTML build to prevent "Build Ghost" sync errors.
- `typst_guard.py`: Prevents forbidden Typst syntax, layout regressions, and enforces worksheet standards (Badges, Exam Hooks, Q&A Integrity).
- `validate_paths.py`: Ensures asset path resolution within bundles.

### 3. The 5-Phase Pipeline (Chronological Workflow)
1.  **Ingestion**: Extract content to `SOURCE_TEXT.md`.
2.  **Blueprint**: Create Typst Lesson Plan (`02-writing-lesson-plans`).
3.  **Visual Roadmap**: Create `visual_plan.md` mapping stages to Reveal.js layouts.
4.  **Asset Generation**: Acquire UNIQUE images via Pixabay (`04-searching-pixabay`).
5.  **Code Assembly**: Generate `presentation.json` and build standalone bundle.

### 3. Repository Hygiene & The 'Published' Law
- **The 'Lib' Legacy Law**: The local `/lib/` folder is **DELETED and LEGACY**. You MUST NOT assume local library files exist.
- **Typst Consultation Law**: Never "guess" Typst syntax. You MUST consult the official Typst GitHub repo via **Skill 16** (`16-consulting-global-repos`) for all syntax, pedagogical templates, and branding patterns.
- **Self-Containment**: Every lesson in `inputs/[lesson-name]/published/` MUST be a standalone bundle including its own `dist/`, `plugin/`, and `fontawesome/` folders (automatically managed by the build system via GitHub acquisition).
- **The File Separation Law**: The source `.typ` files MUST remain in the root of the lesson folder. ONLY compiled `.pdf` files and the final presentation HTML/assets go into the `published/` folder.
- **Strict Naming Standard**: Lesson plans must be named `DD-MM-YYYY-[LEVEL]-[TITLE]-LP.typ` (and `.pdf`). Worksheets must be `DD-MM-YYYY-[LEVEL]-[TITLE]-WS.typ` (and `.pdf`).
- **URL-Friendly Naming**: Lesson folders MUST use lowercase alphanumeric characters and hyphens only (e.g., `28jan-listening-wb-p9`). **Spaces and underscores are FORBIDDEN**.
- **Root-Relative Imports**: All Typst files and presentation logic must use root-relative pathing (`/images/`, `/skills/`) to support project-level automation.
- **Worksheet Permission Gate**: DO NOT create worksheets automatically as part of the lesson planning phase. You MUST ask for explicit permission before initiating the `03-producing-educational-materials` skill.

### 4. Pedagogical & Visual Constitution
- **2026 Gold Standard Enforcements**:
    - **Mission First**: Slide 2 MUST be "YOUR MISSION" with `mission_bg_clipped.mp4` and 320px single-deck badges.
    - **Worksheet Mission**: MUST include a "YOUR MISSION" block with a specific Cambridge Exam hook (PET/First).
    - **Badge Law**: Worksheets MUST feature exactly three badges: CEFR Level, Skill, and Topic.
    - **Hero Image Mandate**: EVERY worksheet MUST have a hero image (Pixabay or User-supplied).
    - **Layout Integrity**: 
        - ID Blocks go *immediately* before the writing task, preceded by a page break.
        - NEVER put manual page breaks immediately after the main reading text.
        - Questions and Ruled Lines MUST be wrapped in non-breakable blocks.
        - Minimum 0.8cm vertical clearance for all handwritten response lines.
    - **The 16:9 Aspect Ratio Law**: All presentations MUST use **1280x720** (16:9) resolution with a `margin: 0.05` to ensure consistent font scaling.
    - **The Pedagogical Font Matrix**: Standardized variables (`--ped-lead-in-size`, `--ped-body-size`) MUST be used to prevent font drift.
    - **The Stable Matching Law**: Use consistent `data-id` attributes for structural elements and sequential IDs for dynamic items to stabilize `auto-animate`.
    - **Segue-Bridge Law**: EVERY `segue` slide MUST be followed by a pedagogical bridge (`strategy`, `vocab`, `editing`, or a `PRODUCTION` task).
    - **The Timer Law (Work-Only)**: Timers are MANDATORY for active student work/discussion and FORBIDDEN for transitions, titles, and explanations.
    - **No Teacher Jargon**: BANNED: "Pre-teaching", "Lead-in", "Gist", "Practice". Use student-centric terms.
    - **Vocab Standard**: White context text, 1.1em size, gold (#FFD700) highlighting for the target word.
    - **Strategy Standard**: White titles (1.4em), balanced table font (0.95em), horizontal timer layout.
    - **Task 3 Consolidation**: ONE slide for all scan gaps, PNG images with direct 2px gold borders.
- **Immersive Audio Canvas**: Listening slides MUST NOT use foreground icons. Use thematic backgrounds (`background` field) only.
- **Zero Placeholder Tolerance**: Common placeholders (lion, bird, etc.) are blocked by programmatic hooks.
- **Answer Separation**: Strict **One-Answer-Per-Slide** enforcement (except for sequence tasks).
- **Dual Coding**: Use FontAwesome icons paired with key text.
- **Student-Centric Persona**: Use warm, encouraging ESL persona. Avoid teacher-facing jargon (Gist, Lead-in).

### 5. Security, Git & Technical Governance
- **Secret Protection**: `token.json`, `.env`, and `.credentials/` MUST be present in `.gitignore`.
- **Dual-Repo Workflow**: Use `00` for source code and `00a` for live deployments.
- **Banned Filenames**: Files named `nul`, `con`, `prn`, or other reserved OS names are strictly forbidden.
- **JSON Schema Integrity**: Presentation data MUST follow the **Flat Schema Law**:
    - Use `layout` instead of `template`.
    - ALL slide data must be at the root level (No nesting in `data: {}`).
    - Use strict types: `timer` (int), `video_loop` (bool).
- **Asset Discovery**: Use non-greedy regex for media collection to ensure filename precision.

## Key Files for Context
- `AGENTS.md`: The "Source of Truth" for persona and core mandates.
- `CRITICAL-MEMORY-RULES.md`: Essential rules to prevent regression.
- `lib/typst/lib.typ`: The local ACT branding library.
- `build.py`: The core build script for aggregating presentations into `/dist`.
